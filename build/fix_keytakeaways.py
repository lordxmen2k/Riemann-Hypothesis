#!/usr/bin/env python3
"""Remove the redundant itemize wrapper inside keytakeaways / commonmyths.

Both environments are defined in the preamble as

    \\newenvironment{keytakeaways}{\\begin{takeaway}{Key Takeaways}\\small
      \\begin{itemize}...}{\\end{itemize}\\end{takeaway}}

so the caller writes \\item directly. A nested \\begin{itemize} inside them
produces a second list, and LaTeX reports "Something's wrong--perhaps a
missing \\item" at the first \\item of the inner list.

This script strips the inner \\begin{itemize} ... \\end{itemize} pair.
"""
import pathlib
import re
import sys

CH = pathlib.Path(__file__).resolve().parent.parent / "source" / "chapters"
ENVS = ["keytakeaways", "commonmyths"]


def fix(t):
    changed = 0
    for env in ENVS:
        guard = 0
        while guard < 200:
            guard += 1
            m = re.search(r"\\begin\{" + env + r"\}\s*\n\s*\\begin\{itemize\}", t)
            if not m:
                break
            # find the matching \end{itemize} for this \begin{itemize}
            start = m.end() - len("\\begin{itemize}")
            depth = 0
            i = start
            while i < len(t):
                if t.startswith("\\begin{itemize}", i):
                    depth += 1
                    i += len("\\begin{itemize}")
                elif t.startswith("\\end{itemize}", i):
                    depth -= 1
                    if depth == 0:
                        end = i + len("\\end{itemize}")
                        break
                    i += len("\\end{itemize}")
                else:
                    i += 1
            else:
                break
            # the \end{itemize} must be the last thing before \end{env}
            rest = t[end:]
            stripped = rest.lstrip()
            if not stripped.startswith("\\end{" + env + "}"):
                break
            # keep any whitespace that preceded \end{itemize} so the
            # \end{env} stays on its own line
            t = t[:m.start()] + "\\begin{" + env + "}" + rest
            changed += 1
    return t, changed


def main():
    total = 0
    for p in sorted(CH.glob("ch*.tex")):
        t = p.read_text(encoding="utf-8")
        nt, n = fix(t)
        if n:
            p.write_text(nt, encoding="utf-8")
            print(f"{p.name}: removed {n} nested itemize wrapper(s)")
            total += n
    print(f"total: {total}")
    left = 0
    for p in sorted(CH.glob("ch*.tex")):
        t = p.read_text(encoding="utf-8")
        for env in ENVS:
            for m in re.finditer(r"\\begin\{" + env + r"\}\s*\\begin\{itemize\}", t):
                print(f"STILL WRAPPED: {p.name} {env}")
                left += 1
    return 1 if left else 0


if __name__ == "__main__":
    sys.exit(main())
