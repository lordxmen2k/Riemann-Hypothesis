#!/usr/bin/env python3
"""Move \\idx{...} markers out of fragile command arguments.

The index markers are inserted by add_index.py at the first occurrence of an
anchor, which may land inside \\texttt{...}. \\index is a protected command and
is not safe there: it can corrupt the surrounding list. This script finds any
marker nested inside one of the listed commands and relocates it to just after
that command's closing brace.
"""
import pathlib
import re
import sys

CH = pathlib.Path(__file__).resolve().parent.parent / "source" / "chapters"
CMDS = ["texttt", "emph", "textbf", "textit", "textsf", "texttt"]


def matching_brace(s, open_idx):
    """Index of the '}' matching the '{' at open_idx."""
    depth = 0
    i = open_idx
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def find_marker(s, start):
    """Return (marker_start, marker_end) for the \\idx{...} at/after start."""
    m = re.compile(r"\\idx\{").search(s, start)
    if not m:
        return None
    open_idx = s.index("{", m.start())
    close = matching_brace(s, open_idx)
    return m.start(), close + 1


def fix_text(t):
    changed = 0
    guard = 0
    while guard < 500:
        guard += 1
        pos = None
        for cmd in CMDS:
            for m in re.finditer(r"\\" + cmd + r"\{", t):
                open_idx = t.index("{", m.start())
                close = matching_brace(t, open_idx)
                if close < 0:
                    continue
                seg = t[m.start():close]
                if "\\idx{" in seg:
                    pos = (m.start(), close, cmd)
                    break
            if pos:
                break
        if not pos:
            break
        mstart, close, cmd = pos
        mk = find_marker(t, mstart)
        if not mk:
            break
        a, b = mk
        marker = t[a:b]
        t = t[:a] + t[b:]
        # re-find the enclosing command's closing brace after removal
        open_idx = t.index("{", mstart)
        close = matching_brace(t, open_idx)
        t = t[:close + 1] + marker + t[close + 1:]
        changed += 1
    return t, changed


def main():
    total = 0
    for p in sorted(CH.glob("ch*.tex")):
        t = p.read_text(encoding="utf-8")
        nt, n = fix_text(t)
        if n:
            p.write_text(nt, encoding="utf-8")
            print(f"{p.name}: moved {n} marker(s)")
            total += n
    print(f"total moved: {total}")
    # sanity: no marker left inside a fragile command
    bad = 0
    for p in sorted(CH.glob("ch*.tex")):
        t = p.read_text(encoding="utf-8")
        for cmd in set(CMDS):
            for m in re.finditer(r"\\" + cmd + r"\{", t):
                open_idx = t.index("{", m.start())
                close = matching_brace(t, open_idx)
                if close > 0 and "\\idx{" in t[m.start():close]:
                    print(f"STILL NESTED: {p.name} \\{cmd}")
                    bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
