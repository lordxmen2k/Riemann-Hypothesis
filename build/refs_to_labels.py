#!/usr/bin/env python3
"""Convert literal chapter and part cross-references to \\ref{}.

The manuscript referred to chapters and parts by number in prose ("Chapter~7",
"Chapters~6 to~9", "Part III"). Adding and reordering chapters would then
require hand-editing ninety references. Converting them to \\ref{} once makes
the numbering a LaTeX concern.

Run BEFORE reordering chapters, so the mapping below refers to the current
numbering.
"""
import pathlib
import re
import sys

SRC = pathlib.Path(__file__).resolve().parent.parent / "source"

CHLABEL = {
    1: "ch:claim", 2: "ch:artifact", 3: "ch:rh", 4: "ch:barriers",
    5: "ch:method", 6: "ch:lean", 7: "ch:chain", 8: "ch:inputs",
    9: "ch:scan", 10: "ch:compilations", 11: "ch:twothirds",
    12: "ch:noreview", 13: "ch:verdict", 14: "ch:protocol",
    15: "ch:consequences",
}
PARTLABEL = {
    "I": "part:claim", "II": "part:math", "III": "part:verify",
    "IV": "part:play", "V": "part:verdict",
}

NUM = r"(?:~?\s*\d+|~?\s*[IVX]+)"
LIST_RE = re.compile(
    r"\b(Chapters?|Parts?)((?:\s*" + NUM + r")"
    r"(?:\s*(?:,|and|to|through)\s*" + NUM + r")*)"
)


def convert(text):
    def one(m):
        head, body = m.group(1), m.group(2)
        is_part = head.startswith("Part")
        table = PARTLABEL if is_part else CHLABEL

        def repl_num(nm):
            tok = nm.group(0).strip()
            tilde = "~" if "~" in nm.group(0) else ""
            tok = tok.replace("~", "").strip()
            if is_part:
                label = table.get(tok)
                if label is None:
                    return nm.group(0)
                return "\\ref{" + label + "}"
            label = table.get(int(tok))
            if label is None:
                return nm.group(0)
            return "\\ref{" + label + "}"

        # normalise the separators to " ~ " around each ref
        parts = re.split(r"(\s*(?:,|and|to|through)\s*)", body)
        out = []
        for i, piece in enumerate(parts):
            if i % 2 == 0:
                out.append(repl_num(re.match(NUM, piece)))
            else:
                sep = piece.strip()
                if sep == ",":
                    out.append(", ")
                elif sep == "and":
                    out.append(" and ")
                elif sep in ("to", "through"):
                    out.append(" to ")
                else:
                    out.append(piece)
        newbody = "".join(out)
        newbody = re.sub(r"(?<=[^{])~(?=\\ref)", "~", newbody)
        return head + "~" + newbody

    return LIST_RE.sub(one, text)


def main():
    total = 0
    for p in sorted(list(SRC.glob("chapters/*.tex")) + [SRC / "frontmatter.tex",
                                                      SRC / "backmatter.tex"]):
        t = p.read_text(encoding="utf-8")
        nt = convert(t)
        if nt != t:
            n = len(re.findall(r"\\ref\{", nt)) - len(re.findall(r"\\ref\{", t))
            p.write_text(nt, encoding="utf-8")
            print(f"{p.name}: {n} reference(s) converted")
            total += n
    print("total converted:", total)
    left = 0
    for p in sorted(list(SRC.glob("chapters/*.tex")) + [SRC / "frontmatter.tex",
                                                      SRC / "backmatter.tex"]):
        for m in re.finditer(r"\b(Chapters?|Parts?)((?:\s*~?\s*\d+)+)", p.read_text(encoding="utf-8")):
            print("  STILL LITERAL:", p.name, m.group(0))
            left += 1
    return 1 if left else 0


if __name__ == "__main__":
    sys.exit(main())
