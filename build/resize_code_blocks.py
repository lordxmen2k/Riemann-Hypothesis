#!/usr/bin/env python3
"""Set the Lean code blocks in the new chapters at a size that fits the column.

The code blocks sit inside a breakable tcolorbox, where fancyvrb's line
breaking misbehaves and corrupts the float placement that follows. Plain
\\begin{verbatim} is safe there but neither wraps nor honours a size change on
its own, so this script

  1. wraps each block in {\\footnotesize ...} so the code is set at 8pt, and
  2. re-wraps any line still too wide for the measure.

The re-wrapped lines are the same text; only the line breaks move.
"""
import pathlib
import re
import sys

CH = pathlib.Path(__file__).resolve().parent.parent / "source" / "chapters"
LIMIT = 60          # characters that fit the column at footnotesize
INDENT_CONT = 2     # extra spaces on a continuation line

BLOCK = re.compile(r"(\\begin\{verbatim\})(.*?)(\\end\{verbatim\})", re.S)


def wrap_line(line, limit):
    if len(line) <= limit:
        return [line]
    indent = len(line) - len(line.lstrip(" "))
    cont = " " * (indent + INDENT_CONT)
    words = line.split(" ")
    out, cur = [], ""
    for w in words:
        cand = (cur + " " + w) if cur else w
        if len(cand) <= limit or not cur:
            cur = cand
        else:
            out.append(cur)
            cur = cont + w
    out.append(cur)
    return out


def process(text):
    def one(m):
        head, body, tail = m.group(1), m.group(2), m.group(3)
        lines = body.split("\n")
        newlines = []
        for l in lines:
            newlines.extend(wrap_line(l, LIMIT))
        body = "\n".join(newlines)
        return ("{\\footnotesize\n" + head + body + tail + "\n}")

    return BLOCK.sub(one, text)


def main():
    total = 0
    for i in range(6, 17):
        p = CH / f"ch{i:02d}.tex"
        t = p.read_text(encoding="utf-8")
        nt = process(t)
        if nt != t:
            p.write_text(nt, encoding="utf-8")
            n = nt.count("{\\footnotesize")
            print(f"{p.name}: {n} code block(s) resized and re-wrapped")
            total += n
    print("blocks processed:", total)
    # report any line that is still too long because it is one long token
    for i in range(6, 17):
        p = CH / f"ch{i:02d}.tex"
        for m in BLOCK.finditer(p.read_text(encoding="utf-8")):
            for l in m.group(2).split("\n"):
                if len(l) > LIMIT:
                    print(f"  STILL WIDE {p.name}: {len(l)} chars: {l[:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
