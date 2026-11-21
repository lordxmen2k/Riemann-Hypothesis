# Is the Riemann Hypothesis Solved?

**A Critical Audit of the Lean Formalization, the Theta-Lift Method, and the
Two-Thirds Ceiling**

Gerald Enrique Nelson Mc Kenzie — Tico Internet LLC
2026 First Edition · Apache License 2.0 · DOI 10.5281/zenodo.24408811

---

## What this book is

On 20 November 2026 a mathematician published a four-page note claiming to have
proved the Riemann Hypothesis, together with a Lean development of 175,187
files and roughly 17.4 million lines. Two university teams compiled it the
same day. The world's newspapers called it the greatest mathematical result of
the century. Nobody has reviewed the mathematics.

This book takes the artifact seriously, reads it, and reports what it
establishes and what remains unestablished. It is not a book about the Riemann
hypothesis; it is a book about what it takes to know whether a machine-checked
proof of the Riemann hypothesis is a proof — worked through a specific case.

**The finding: the claim is unresolved.** The submitted formalisation is axiom-
free, sorry-free, and its reduction from Mathlib's own `RiemannHypothesis` down
to a proved fixed-point formula was traced by hand and found sound. But the
load-bearing inputs have never been audited by anyone outside the author; the
author's own timeline records an a-priori ceiling at two thirds of the zeros and
an obstruction whose stated remedy requires a conjecture that is still open; and
the remark does not explain how either was crossed. The claim is neither
established nor refuted. Chapter 14 sets out the protocol that would settle it.

## Contents

```
source/          the LaTeX manuscript
  preamble.tex   identity, design tokens, page furniture
  frontmatter.tex, body.tex, backmatter.tex
  chapters/      ch01.tex .. ch15.tex
figures/         cover_front, cover_back, and nine book figures
build/           figure, cover, index and repair scripts
research/        source ledger, corrections log, research log,
                 literature verification, cover-style draw record
output/          the finished PDF
```

## Building

```sh
./build.sh
```

Requires XeLaTeX, `makeindex`, Python 3 with matplotlib and Pillow, and the
fonts in `fonts/` (Outfit, DejaVu Sans Mono, Fira Math, XCharter Math). The
script copies the fonts into `~/.fonts`, regenerates the figures, counts the
words, runs XeLaTeX four times, runs `makeindex`, then re-runs XeLaTeX twice to
inject the final page and word counts into the colophon.

Regenerating the artwork:

```sh
python3 build/make_figures.py     # four computed charts
python3 build/make_diagrams.py    # five diagrams, laid out in inches at 4.6 in
./build/make_covers.sh            # front and back covers
```

One generator owns each figure: the four computed charts come from
`make_figures.py` and the five schematic diagrams from `make_diagrams.py`.
`build.sh` runs both, so neither can overwrite the other's work.

The cover artwork itself was generated as an original watercolour plate and is
not reproducible from the scripts. `build/make_cover_art.py` crops it, bakes in
the legibility scrim and writes the 300 DPI plates; `source/cover_front.tex` and
`source/cover_back.tex` set the typography over them, so the cover type is
vector and uses the book's own fonts.

## The research materials

`research/` is the evidentiary record behind the book, and it is meant to be
read alongside it.

| File | What it holds |
|---|---|
| `source_ledger.md` | Every source relied on, with what each one supports |
| `corrections.md` | What was corrected during research, including the writer's own initial assumptions |
| `research_log.md` | The chronological record of the investigation and its decisions |
| `literature_verification.md` | Full verification report, with a verdict line per item |
| `cover_draw.json` | The recorded random draw of the cover style, with its seed |

## Licence

Apache License 2.0. The complete text is at
<https://www.apache.org/licenses/LICENSE-2.0>.

No source repository is published for this edition. The Lean development
examined in the book is the work of its author and is not redistributed here.
