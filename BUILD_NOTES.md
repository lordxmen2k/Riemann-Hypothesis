# Build Notes

**Title:** Is the Riemann Hypothesis Solved?
**Subtitle:** A Critical Audit of the Lean Formalization, the Theta-Lift Method, and the Two-Thirds Ceiling
**Author:** Gerald Enrique Nelson Mc Kenzie
**Publisher / imprint:** Tico Internet LLC
**Edition:** 2026 First Edition
**Licence:** Apache License 2.0
**DOI:** 10.5281/zenodo.23874214 (single field, `source/preamble.tex`, `\bookDOI`)
**Facts current as of:** 21 November 2026

---

## Extent

| | |
|---|---|
| Trim size | 6 × 9 in (432 × 648 pt) |
| Pages | 156 (154 numbered + full-bleed front and back covers) |
| Word count | 31,736 (body, front matter and back matter, excluding the cover artwork and the LaTeX control words) |
| Chapters | 15, in 5 parts |
| Figures | 9 (4 computed charts, 5 diagrams) |
| Tables | 4 |
| Index entries | 95 |
| Glossary terms | 63 |
| Fonts embedded | Outfit, JetBrains Mono, Fira Math, DejaVu Sans — all subsets, all embedded |
| PDF bookmarks | 114 outline entries matching the table of contents |
| Link annotations | 3 external URIs (Apache licence, DOI on the copyright page, DOI in the colophon) plus internal cross-references from the table of contents, figures and lists |

## Cover

**Style drawn:** watercolour.

The style was drawn at random from the fixed pool, as required. The procedure
and its seed are recorded in `research/cover_draw.json`:

```
seed_material : "Is the Riemann Hypothesis Solved? | Tico Internet LLC | 2026-11-21"
seed          : 58067312192058
method        : python random.Random(seed).choice on a shrinking list, 14 draws
draw order    : watercolour, Swiss / International style, blueprint / technical
                drawing, holographic gradient, vaporwave, minimalist geometric,
                retro sci-fi pulp, woodcut / linocut, isometric 3D, paper-cut
                layers, vintage NASA poster, cyberpunk neon, art deco,
                ink and line art
DRAWN         : watercolour
```

Sanity check against the subject: a watercolour rendering of the critical
strip, with the critical line as a luminous horizon and the zeros as drifting
marks, suits a book about a conjecture that lives in a narrow vertical band.
Retained on the first draw; no redraw was needed.

**Artwork.** Original, generated for this book: a deep indigo watercolour wash
with a luminous pale-green vertical line and drifting dark droplets, with warm
amber blooming at the foot. No text, no watermark, no logo, no badge; all four
corners checked.

**Typography.** Set in vector over the plate, not rasterised, so the identity
block is exact and legible at thumbnail size. The front cover carries the full
identity block: title, subtitle, author, imprint, edition, licence and DOI.
The back cover carries the blurb, the five parts, and the footer.

## What was tested, and what was not

**Tested end to end.** The PDF was rendered and inspected page by page, not
just checked for a zero exit status: the front cover, the half-title, the
title page, the copyright page, a part opener, a chapter opener, a Key
Takeaways box, a body page, four figure pages, the glossary, a notes page, the
index, the colophon and the back cover. LaTeX reports **0 errors** and **0
undefined references**. The extracted text contains **no stray control
sequences** (checked for `\idx{`, `\begin{`, `\end{`, `\item`, `PLACEHOLDER`,
`TODO`, `XXX`, code fences). All fonts are embedded. The outline matches the
contents.

**Not tested.** The book was not proof-read by a second reader, and the
mathematics has not been checked by a number theorist. The author is not a
number theorist, and the book says so where it matters.

## The independent Lean build

An independent build of the submitted artifact was attempted for this book.
The outcome is reported honestly, because the book makes a claim about it.

| Step | Result |
|---|---|
| Toolchain | `elan` installed; `leanprover/lean4:v4.33.1` fetched |
| Mathlib | Checked out and **confirmed** at the revision the submission pins: `0df444a360eaa60ab8c11dca51a86af692955474` |
| Cache | `lake exe cache get` retrieved 8,690 prebuilt artefacts for the pinned revision |
| Build | `lake build Main` launched; the submission's own modules began compiling (`src/Statements.olean`, `Formalism/TameInertiaTowers/StatementGroup.olean`) |
| Completion | **Did not complete.** The sandbox has 2 cores and 3 GB of RAM; the mirror's own README warns this is a ~17 M-line build that needs many cores and plenty of RAM and "expect it to run for a long time" |

The build was left running and its log retained at `/workspace/rr/build3.log`.
No claim in the book depends on it: the book states only what was observed —
that the submission's own modules began compiling with Mathlib satisfied
entirely from cache. Two independent compilations by others (Andrew Sutherland
at MIT, Simon DeDeo at CMU) are reported in Chapter 10 and are attributed to
the source that reported them.

## Claims flagged as uncertain or unverified

Carried in the text as uncertainty, not smoothed over. Full detail in
`research/corrections.md`.

1. **The faithfulness of the load-bearing inputs.** Whether `TLiftK`,
   `Tools_k`, `EpsOf_k`, `Hyps`, `Af.Hypotheses_2`, `GlobalTheory.Ord2.admitted`
   and the vanishing statements correspond to the classical theorems they are
   named for. **Not verified.** This is the book's central open question and
   is stated as such in Chapters 8, 12 and 13.
2. **Whether the formalised epsilon estimate is the remark's item 10.** The
   formalized `EpsOf_k` is a signature computation for Hermitian forms; the
   remark describes a "sufficient lower bound on divisibility". These are
   different shapes of statement. Flagged in Chapter 8.
3. **The 15-to-16 November transition.** The remark records a two-thirds
   ceiling and then GRH, with no account of the change. Flagged in Chapters 1,
   4, 5, 13 and 14 as the first question a reviewer must answer.
4. **Bost's slope inequality.** The source paper was located (ASENS 30 (1997)
   no. 1, 229–288) but the inequality itself was not retrieved from a primary
   text, so the book paraphrases the method and does not quote the inequality.
5. **Behrend 1940.** No DOI or OpenAlex record was retrievable, and the
   Serre/Komatsu/Katsura attributions could not be verified. The book cites
   Behrend for the mathematical content only, with no identifier.
6. **The "Saouter–Demichel–Planchat" paper and the "LP method with crossing
   value L = 0.40".** No such paper or value was located in arXiv, Crossref,
   HAL or OpenAlex. The two-thirds result is attributed to arXiv:2608.13637
   (Alpöge & Furman) and no crossing value is asserted anywhere in the book.
7. **Lamzouri's paper title.** The arXiv identifier is cited; the title was not
   independently confirmed and is not asserted.
8. **Individual primary citations for the classical results behind
   `Hypotheses_2`** (Jacquet–Shalika rigidity, Borel injectivity, Gelfand–
   Kazhdan, Kato) were not separately retrieved. The artifact's own derivation
   chains are cited in the text instead.

## Items needing owner review

1. **DOI.** `10.5281/zenodo.23874214` is the standing placeholder. It lives in
   exactly one field, `\bookDOI` in `source/preamble.tex`; swapping it is a
   single edit and the build script re-injects it on the next run.
2. **ISBN.** `978-1-0000-0000-0` on the copyright page is a placeholder.
3. **Source-code link in the colophon.** The colophon field reads "None
   published for this edition". No repository has been supplied for this title,
   and none was invented. Supply one and it goes in the same place.
4. **Cover style.** Drawn at random and recorded, as required. If the owner
   wants a different treatment, the draw record should be replaced, not
   overwritten silently.
5. **Back-cover blurb.** Written for this edition; adjust freely.
6. **Scope note.** The standing remit for this imprint is AI, Quantum and
   Space. This title sits in the AI field: an AI-assisted mathematical proof,
   the formal-verification methodology used to test it, and what the episode
   says about the reliability of machine-generated mathematics. Recorded in
   `research/research_log.md` under M2.

## Build environment

Debian 12, XeLaTeX with `fontspec` + `unicode-math`, `makeindex`,
`pdfimages`/`pdftoppm` (poppler) for inspection, Python 3 with matplotlib and
Pillow. Fonts shipped in `fonts/`: Outfit, JetBrains Mono, Fira Math,
XCharter Math.

## Repository

No remote is configured for this project in the delivery environment, so the
work is committed locally with semantic messages. The history is:

```
aa952bc  chore: initialize Riemann hypothesis book project with the submitted remark
8c5dfca  feat(book): complete manuscript, figures, covers and build pipeline
```

plus a final commit for the verified PDF and these notes.
