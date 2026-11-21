#!/usr/bin/env python3
"""Insert index entries into the chapter sources.

Each entry anchors on an exact substring that must occur in the file; the
\\idx marker is appended after the FIRST occurrence only, so the index points
at the substantive treatment rather than at a passing mention.
"""
import pathlib
import sys

CH = pathlib.Path(__file__).resolve().parent.parent / "source" / "chapters"

# (file, anchor, index entry)
ENTRIES = [
    ("ch01.tex", "Levent Alpöge", "Alpöge, Levent"),
    ("ch01.tex", "Claude", "Claude (AI assistant)"),
    ("ch01.tex", "Stepanov's argument", "Stepanov's method"),
    ("ch01.tex", "multiplicity is hard to find", "multiplicity"),
    ("ch01.tex", "It being obviously inappropriate", "statement review"),

    ("ch02.tex", "src/Main.lean", "Lean development:structure of"),
    ("ch02.tex", "src/Statements.lean", "Lean development:statements"),
    ("ch02.tex", "There are no axioms", "axioms (Lean)"),
    ("ch02.tex", "CocoSgt/riemann-hypothesis-lean", "CocoSgt mirror"),
    ("ch02.tex", "no independent build or review", "status line, dated"),

    ("ch03.tex", "analytic continuation", "analytic continuation"),
    ("ch03.tex", "Euler product", "Euler product"),
    ("ch03.tex", "Riemann--von Mangoldt formula", "Riemann--von Mangoldt formula"),
    ("ch03.tex", "Weil's criterion", "Weil's criterion"),
    ("ch03.tex", "Guinand's theorem", "Guinand's theorem"),
    ("ch03.tex", "Landau's criterion", "Landau's oscillation theorem"),
    ("ch03.tex", "von Mangoldt function", "von Mangoldt function"),
    ("ch03.tex", "de la Vallée Poussin", "de la Vallée Poussin, de"),

    ("ch04.tex", "Stepanov--Bombieri method", "Stepanov--Bombieri method"),
    ("ch04.tex", "van Frankenhuijsen", "van Frankenhuijsen, Maarten"),
    ("ch04.tex", "Gross--Prasad", "Gross--Prasad theorem"),
    ("ch04.tex", "Vandiver's conjecture", "Vandiver's conjecture"),
    ("ch04.tex", "Hart,", "Hart--Harvey--Ong bound"),
    ("ch04.tex", "two thirds a priori", "two-thirds ceiling"),
    ("ch04.tex", "H^1_o", "H^1_o classes"),

    ("ch05.tex", "Stepanov determinant", "Stepanov determinant"),
    ("ch05.tex", "qN = Mk + R", "qN = Mk + R"),
    ("ch05.tex", "Guinand--Weil", "Guinand--Weil sign"),
    ("ch05.tex", "Iterated theta lifts", "theta lift:iterated"),
    ("ch05.tex", "Rallis seesaw", "Rallis seesaw"),
    ("ch05.tex", "Iwasawa tower via analogy", "Iwasawa tower"),
    ("ch05.tex", "Behrend", "Behrend construction"),
    ("ch05.tex", "Relative trace formula", "relative trace formula"),
    ("ch05.tex", "Bost slope inequality", "Bost's slope method"),

    ("ch06.tex", "proof assistant", "proof assistant"),
    ("ch06.tex", "print axioms", "axiom check"),
    ("ch06.tex", "propext", "propext"),
    ("ch06.tex", "Classical.choice", "Classical.choice"),
    ("ch06.tex", "Quot.sound", "Quot.sound"),
    ("ch06.tex", "sorryAx", "sorryAx"),
    ("ch06.tex", "Lean.ofReduceBool", "native\\_decide"),
    ("ch06.tex", "kernel is", "kernel (Lean)"),
    ("ch06.tex", "lean4checker", "lean4checker"),
    ("ch06.tex", "landrun", "landrun"),
    ("ch06.tex", "Palomar", "Palomar registry"),
    ("ch06.tex", "statement review", "statement review"),
    ("ch06.tex", "arXiv:2606.29493", "arXiv:2606.29493"),

    ("ch07.tex", "riemannHypothesis", "RiemannHypothesis (Mathlib)"),
    ("ch07.tex", "UpperTheory.EveryCharacter", "EveryCharacter"),
    ("ch07.tex", "zeta\\_ne\\_zero\\_of\\_everyCharacter", "zeta\\_ne\\_zero\\_of\\_everyCharacter"),
    ("ch07.tex", "galoisLocalGlobalStrong\\_recParameter", "galoisLocalGlobalStrong\\_recParameter"),
    ("ch07.tex", "TLiftK", "TLiftK"),
    ("ch07.tex", "lefschetz\\_fixedPoint\\_finite\\_etale\\_correspondence",
     "Lefschetz fixed-point formula"),
    ("ch07.tex", "integral clopen decomposition", "clopen decomposition"),
    ("ch07.tex", "completedRiemannZeta\\_one\\_sub", "functional equation"),

    ("ch08.tex", "Tools\\_k", "Tools\\_k"),
    ("ch08.tex", "Hypotheses\\_2", "Hypotheses\\_2"),
    ("ch08.tex", "newformAut", "newformAut"),
    ("ch08.tex", "ClozelConjC", "Clozel's conjecture"),
    ("ch08.tex", "BorelInjC", "Borel injectivity"),
    ("ch08.tex", "GelfandKazhdan", "Gelfand--Kazhdan correspondence"),
    ("ch08.tex", "admitted", "admitted (structure)"),
    ("ch08.tex", "VanishOrd", "VanishOrd"),
    ("ch08.tex", "Selmer", "Selmer group"),
    ("ch08.tex", "EpsOf\\_k", "EpsOf\\_k"),
    ("ch08.tex", "SignatureOfHermitianForm", "signature of a Hermitian form"),
    ("ch08.tex", "nonempty\\_hyps\\_of\\_allRows", "Hyps package"),
    ("ch08.tex", "IsRecT", "IsRecT"),
    ("ch08.tex", "Kato", "Kato's Euler systems"),

    ("ch09.tex", "ripgrep", "static scan"),
    ("ch09.tex", "admit", "admit"),
    ("ch09.tex", "addDecl", "addDecl"),
    ("ch09.tex", "maxHeartbeats", "maxHeartbeats"),

    ("ch10.tex", "Andrew Sutherland", "Sutherland, Andrew"),
    ("ch10.tex", "Simon DeDeo", "DeDeo, Simon"),
    ("ch10.tex", "variant of Lean", "variant of Lean"),
    ("ch10.tex", "sign error", "sign error (withdrawn formalisation)"),

    ("ch11.tex", "arXiv:2608.13637", "arXiv:2608.13637"),
    ("ch11.tex", "Ralph Furman", "Furman, Ralph"),
    ("ch11.tex", "Lamzouri", "Lamzouri, Yousouf"),
    ("ch11.tex", "Pratt--Robles--Zaharescu", "Pratt--Robles--Zaharescu"),
    ("ch11.tex", "Conrey", "Conrey, John"),

    ("ch12.tex", "no preprint", "preprint, absence of"),
    ("ch12.tex", "refereed report", "refereed report, absence of"),
    ("ch12.tex", "Four Colour Theorem", "four-colour theorem"),
    ("ch12.tex", "Prime Number Theorem for arithmetic progressions",
     "prime number theorem, formalised"),

    ("ch13.tex", "unresolved", "verdict"),
    ("ch13.tex", "neither established nor refuted", "possibility A/B/C"),

    ("ch14.tex", "lake exe cache get", "lake build"),
    ("ch14.tex", "lean4export", "lean4export"),
    ("ch14.tex", "NanoDa", "NanoDa"),
    ("ch14.tex", "print axioms Main", "axiom check"),

    ("ch15.tex", "Katz--Sarnak", "Katz--Sarnak"),
    ("ch15.tex", "Artin holomorphy", "Artin holomorphy conjecture"),
    ("ch15.tex", "Does it compile, and did more than one person do it?", "evaluation procedure"),
]


def main():
    missing = []
    touched = 0
    for fname, anchor, entry in ENTRIES:
        p = CH / fname
        t = p.read_text(encoding="utf-8")
        if anchor not in t:
            missing.append((fname, anchor))
            continue
        if f"\\idx{{{entry}}}" in t:
            continue
        # insert after the first occurrence, keeping the marker out of URLs
        i = t.index(anchor)
        j = i + len(anchor)
        t = t[:j] + "\\idx{%s}" % entry + t[j:]
        p.write_text(t, encoding="utf-8")
        touched += 1
    print(f"inserted {touched} index markers")
    if missing:
        print(f"NOT FOUND ({len(missing)}):")
        for f, a in missing:
            print(f"  {f}: {a!r}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
