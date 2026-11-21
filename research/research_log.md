# Research Log

Chronological record of what was done, what was decided, and why. Written so that another
researcher can see the shape of the investigation rather than only its conclusions.

---

## M1 — Research and verification (2026-11-20 to 2026-11-21)

### 1.1 The document

Read `Riemann_remark.pdf` (4 pp.) from the attachments. `pdftotext` mangled the display
mathematics, so pages 1–4 were rendered to PNG at `/workspace/rr/pages/p-*.png` and read
visually; a plain-text extraction was kept at `research/remark_extracted.txt` for search.

The author is Levent Alpöge. The document is a four-page narrative plus a twenty-item timeline
dated 2026-10-06 through 2026-11-16. It contains no proof, no lemma statement, and no
definition of the objects it names.

### 1.2 The artifact

The remark's footnote points to `https://alpo.ge/lean.tar.gz.part01` … `.part14`. All fourteen
parts were downloaded (18 MB each; 239 275 554 bytes total), concatenated, and extracted to
`/workspace/rr/src/lean/` — **175 187 `.lean` files**, roughly 17.4 M lines, approximately 1 GB
on disk. Toolchain `leanprover/lean4:v4.33.1`; Mathlib pinned to
`0df444a360eaa60ab8c11dca51a86af692955474`.

### 1.3 Static audit (this book's own)

Full-tree scans with ripgrep over all 175 187 files:

| Pattern | Count |
|---|---|
| `^\s*axiom\s` (axiom declarations) | **0** |
| `\bsorry\b` | **0** |
| `^\s*opaque\s` | 0 |

This is a necessary condition, not a sufficient one. The mirror README's own scan reports the
same and adds `admit` 0, `native_decide` 0, `unsafe`/`implemented_by`/`@[extern]` 0,
`set_option maxHeartbeats 0` in 4 files, custom `macro`/`elab`/`syntax` in 22 files, `addDecl`
in 1 file.

The dangerous failure mode for a formalized proof is not a `sorry`; it is an unproved statement
dressed as a theorem whose *statement* carries the hard content, with the proof term being a
repackaging of a hypothesis. So the audit proceeded by tracing the dependency chain by hand.

### 1.4 Dependency chain, traced

`src/Main.lean` exports six theorems, all reducing to `rhOfAll`. The chain:

```
riemannHypothesis  (src/Main.lean)
  ← UpperTheory.FinalTheorems.riemannHypothesis
  ← UpperTheory.riemannHypothesis_of_everyCharacter      (RiemannHypothesisOfEveryCharacter.lean)
  ← UpperTheory.FinalTheorems.everyCharacter             (MainConclusion.lean)
  ← UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter   (RowSrc.lean)
  ← UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift    (GaloisRepresentationsOfThetaLift.lean)
  ← UpperTheory.Gal.Int.galoisLocalGlobalStrong_of_geometry_lift  (Development.lean)
  ← UpperTheory.Gal.Int.Geo.geoOne_holds                 (WeightOneGeometricRealization.lean)
  ← UpperTheory.Gal.Int.Geo.weight_one_geometric_realization
  ← GlobalTheory.T.lefschetz_fixedPoint_finite_etale_correspondence
  ← UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence
```

**Finding 1 — the reduction is sound.** `riemannHypothesis_of_everyCharacter` is a correct and
standard argument: non-vanishing to the right of $\Re s = \tfrac12$, plus the functional equation,
plus the classification of trivial zeros via `Complex.Gammaℝ_eq_zero_iff`, gives RH. The
`EveryCharacter` statement itself is faithful, not weakened:

```lean
def UpperTheory.EveryCharacter : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ), 1/2 < s.re →
    (χ ≠ 1 ∨ s ≠ 1) → DirichletCharacter.LFunction χ s ≠ 0
```

**Finding 2 — the bottom of the chain is real mathematics.** The Lefschetz theorem is proved, not
asserted: the proof builds an integral clopen decomposition $\{V_j\}$ of $Z$, pulls it back along
the two finite étale maps $c_1, c_2$, forms the cells $W_{jk} = c_1^{-1}(V_j) \cap c_2^{-1}(V_k)$,
and compares the Lefschetz traces against the local factors
$\det(1 + X A_y) / \det(1 - A_y)$. This is the classical mechanism by which an L-function's
local factors come out of a fixed-point formula.

**Finding 3 — the hypothesis packages are constructed, not assumed.** `Hyps` — the bundle of
hyperplane-section hypotheses the proof needs — is instantiated by
`GlobalTheory.Fc.nonempty_hyps_of_allRows`, which assembles it from `AllRows`, `ExBL` and
`BaseCond` rather than taking it as an input. The deep bundle `Tools_k` is likewise assembled
from roughly twenty named component theorems (Siegel–Weil, frame conjugacy, finite level,
stability of the point 2, box section, signature/epsilon estimate, group-theoretic topology,
theta basics, pairwise exterior, split-freeness, vacuum fixing, action exterior, first and second
Lie algebra identities).

**Finding 4 — what has NOT been checked.** Whether `TLiftK` (the existence of a theta lift with
prescribed weight), `EpsOf_k` (the divisibility estimate), `Af.NewformAut` (automorphy),
`Af.AdVanishK` / `Af.AdVanishQ` (vanishing), and `Af.CongruenceNumberRankThree` correspond to
the classical theorems their names suggest, rather than being restatements of the hard content
under a familiar name. This is the gap in the verification, and it is exactly the gap that
arXiv:2606.29493 warns the Lean kernel does not close.

### 1.5 Build attempt

A third independent build was attempted for this book: elan installed the pinned toolchain,
mathlib was fetched and confirmed at the pinned revision, `lake exe cache get` retrieved 8 690
prebuilt artefacts, and `lake build Main` was launched. The machine has 2 cores and 3 GB RAM —
the mirror README itself warns this is "a very large build (≈ 17 M lines on top of Mathlib)".
Outcome is reported in Ch. 10 and in the build notes, honestly, including the case where it did
not finish.

Two independent compilations were already reported on 2026-11-20 — Andrew Sutherland at MIT
first, Simon DeDeo at CMU a few hours later (Quanta Magazine, 2026-11-20).

### 1.6 Literature

Verified against primary records via the Crossref and arXiv APIs and direct fetches. Results in
`research/literature_verification.md`; the curated subset used in the book is in
`research/source_ledger.md`; corrections to my own priors are in `research/corrections.md`.

Load-bearing corrections: the two-thirds result is arXiv:2608.13637 (Alpöge & Furman), not the
paper I had assumed; the independent compilations happened on the same day as the mirror README's
"no independent build" line; Vandiver's $2^{31}$ verification is 2017, not 1977; Weil's criterion
is a positivity condition, not an inequality of the form I had assumed.

### 1.7 Verdict reached

**Unresolved.** The artifact compiles, contains no axioms and no `sorry`, and its reduction to
Mathlib's `RiemannHypothesis` is mathematically correct — genuinely more than the usual
"AI-proved-RH" submission. But no independent review of the mathematics exists, and the author's
own account of the method records an a-priori ceiling at two thirds and an obstruction requiring a
weakening of Vandiver, which is open. The book states this precisely and gives the protocol that
would settle it.

---

## M2 — Structure (2026-11-21)

Structure designed **after** the research was collected and reviewed, as required. Seven parts,
thirty-four chapters:

| Part | Chapters | Purpose |
|---|---|---|
| I — The Claim | 1–2 | What was said, and what was submitted |
| II — The Mathematics | 3–5 | RH from first principles; the four barriers; the method as described |
| III — The Method, Step by Step | 6–16 | The nine steps in full, the two thirds computed from the source, and a step-to-declaration map |
| IV — The Proof in Natural Language | 17–24 | The same argument as mathematics, with the two gaps marked in place |
| V — The Verification | 25–28 | What Lean can and cannot certify; the traced chain; the load-bearing inputs; the static scan |
| VI — The State of Play | 29–31 | The independent compilations; the two-thirds theorem; the absence of review |
| VII — The Verdict | 32–34 | The finding stated precisely; a verification protocol; what a proof would change |

### The two thirds, located

The remark's item 14 records that the method "would stop at 2/3 a priori". The
constant is not the author's summary of a hand-waving estimate: it is a literal
`2 / 3` in the submitted source, in
`Formalism/SharpRestriction/GrowthBounds/SegmentDegree/`, in the threshold
arithmetic of `ThresholdPowerBoundOfCounts.lean`:

    threshold_arith_letter_case : c / 2 <= 2 / 3 * bo - k * Ns
    threshold_arith_w_case     : c / 2 <= 2 / 3 * (fl - ...) - k * Ns

and in the path decomposition of `AtypicalPathSmallWeight.lean`, where the
typical path carries `2 / 3 * B (od i) <= plPart mu (lastIdx r)` and the
atypical path is allowed an extra `2 * B (od i)` of slack. The missing third is
the price of the atypical path. The same fraction is the headline of the
author's own published two-thirds theorem of three months earlier.

### The natural-language proof part

Added on the owner's instruction, so that the book stands on its own as
mathematics: eight chapters writing the argument as propositions and proofs,
with the corresponding Lean declaration cited at each statement, and with the
two places the proof does not close -- the budget factor and the `H^1_o`
classes -- marked where they occur rather than at the end.

### Attribution

The mathematics is Levent Alpoge's. Attribution appears on the title page, the
copyright page, the Part IV opener, the cover and the back cover. This book is
the analysis and the exposition of that work.

### Scope note

The standing scope for this publisher is Artificial Intelligence, Quantum Computing/Physics, and
Space. This book falls inside the AI field: its subject is an AI-assisted mathematical proof, the
formal-verification methodology used to test it, and what the episode says about the reliability
of AI-generated mathematics and machine-checked proofs. It is treated as an AI-and-verification
book with a mathematical core, not as a general number-theory text.

---

## M3 — Figures (2026-11-21)

All figures are original, produced for this book. The critical-line figure is computed by
Riemann–von Mangoldt summation in pure Python; every other figure is drawn from the audit's own
measurements or is a schematic redrawn from the sources.

---

## M4 — Cover (2026-11-21)

Style drawn at random from the fixed pool. Seed material:
`"Is the Riemann Hypothesis Solved? | Tico Internet LLC | 2026-11-21"`;
seed `58067312192058`; `random.Random(seed).choice` on a shrinking list, 14 draws.
Full order and result in `research/cover_draw.json`.

Draw order: watercolour, Swiss / International style, blueprint / technical drawing, holographic
gradient, vaporwave, minimalist geometric, retro sci-fi pulp, woodcut / linocut, isometric 3D,
paper-cut layers, vintage NASA poster, cyberpunk neon, art deco, ink and line art.

**Drawn: watercolour.** Sanity-checked against the subject and retained: a watercolour rendering
of the critical strip, with the critical line as a luminous horizon and the zeros as drifting
marks, suits a book about a conjecture that lives in a narrow vertical band.

**Implementation.** The plate was generated as an original watercolour artwork. The legibility
scrim is baked into a 300 DPI JPEG by `build/make_cover_art.py`, and the typography is set in
LaTeX over it in the book's own fonts (`source/cover_front.tex`, `source/cover_back.tex`), so
the cover type is vector. The same artwork drawn with a raster scrim layer cost 17 MB in the
finished PDF; baked into the plate and set in LaTeX it costs 1.5 MB.

---

## M5 — Typographic and factual correction pass (2026-11-21)

Driven by the owner's screenshots of two rendered pages, then continued to a full pass over
every figure and every page.

**Missing glyphs.** The math font (FiraMath) carries neither U+211C nor U+229E. Because the
font machinery reinstated both commands as literal characters, every occurrence typeset as a
missing-glyph box — 32 real-part signs and 10 circled pluses. A one-page harness
(`source/tb.tex`) established that the commands *were* correctly redefined and still boxed, which
placed the cause in the font fallback and not in the preamble. Fix: `\\Re` → `\\mathrm{Re}` and
`\\boxplus` → a TikZ `\\tboxplus`, with a thin space after `\\mathrm{Re}`.

**Mono face.** JetBrains Mono lacked four glyphs used in the Lean quotations. Switched to DejaVu
Sans Mono, and the 42 code blocks were converted from `Verbatim` to a `leanquote` environment so
that long quotations wrap inside the measure.

**Tables.** All prose columns set ragged-right (`ragged2e`) with hyphenation disabled inside
cells. The Chapter 6 "Nine steps" table had been fully justified, which stretched the spacing and
broke "multiplicity", "determinant" and "remainder" at arbitrary points.

**Figures.** All nine were rendered in place and inspected. Four had overlapping elements (the
critical-line legend, the psi sum's lower limit, the records chart, and the zero-length bar on the
logarithmic census); one, the three-questions diagram, was badly broken.

**Root cause found.** `build/make_figures.py` contained a second, older copy of the five schematic
diagram generators, drawn on a canvas whose axes limits did not match the coordinates used to draw
them, so the boxes were clipped and the titles fell outside the canvas. The copies were deleted,
and `build.sh` now runs `make_figures.py` then `make_diagrams.py`.

**Census corrected.** The library census table omitted `Statements.lean`, so its rows summed to
175,186 against a stated total of 175,187, and one library was described as "ten" when the
Lakefile declares eleven (one of them virtual). Recounted from the extracted tree: nine
directories holding 175,185 files and two top-level modules holding two; 175,187 in all.

**Stale text.** The back cover listed five parts for a seven-part book. The copyright page and
the colophon said no source repository was published; the owner has supplied one for this title
and both now name it.

**Verification after the pass.** 0 LaTeX errors, 0 missing characters, 0 overfull hboxes above
25 pt, 0 words outside the safe area, 0 blank pages, all fonts embedded, 241 bookmarks, 526 link
annotations, 276 numbered pages plus two cover leaves, 57,326 words.

**Second correction round.** A page-by-page sweep of the rendered book with
the extracted word boxes found two tables overrunning the text block, with
the running foot printed on top of the last row. The Chapter 6 table of nine
steps is now set one size down with tighter rows; the Chapter 16 directory
census is rebalanced, which both fixed the overflow and stopped the
descriptions from breaking every two words. A folio-overlap check across
every page now returns nothing.

The build log, which had carried 42 warnings, is now silent. The enumitem
complaints about the description lists are resolved by stating the label
width rather than leaving it to be derived; the hyperref complaints about
mathematics in section titles are resolved with plain-text bookmark
alternatives; the caption complaints are resolved by issuing the per-type
skips at the start of the document; and the two microtype complaints are
resolved by switching off microtype's own protrusion tables, which XeTeX's
native protrusion makes redundant, with the typesetting checked to be
identical.

The covers were carrying a second typeface: most of their type is set in
`sffamily`, and without an explicit sans face that resolves to Latin Modern
Sans. Both cover files now set the sans and mono faces, and the finished
cover uses Outfit alone.

---

## M6 — Revision of the verdict (2026-11-21, evening)

A critique of the book arrived after the first build, holding that the verdict was out of date and
partly self-contradictory. It was checked against primary sources rather than answered from
memory, and it was substantially right on the formal side.

**Sources read directly.**

- The Lean and Mathlib communities' joint statement of 2026-11-21 13:55 UTC, endorsed by the Lean
  FRO and the Mathlib Initiative, at `leanprover-community.github.io/blog/posts/riemann-hypothesis/`.
- Andrew Sutherland's verification page at `math.mit.edu/~drew/grh/`, last updated 2026-11-21
  12:55 UTC, including the full check table and the provenance block.
- The community verification repository `github.com/leanprover-community/riemann-hypothesis`, in
  particular `verification/NOTES.md`, for the size figures, the static scan, the tactics and the
  stated limits.

**What the critique got right.** The draft verdict said the claim was not "pending compilation" and
that the second step of review "has not happened". Both were true when written and were false by
the evening of 21 November. The phrase "neither established nor refuted" read, against the joint
statement, as a claim about the formal status, which was not open.

**What the critique got wrong.** It held that the load-bearing-inputs worry "does not follow"
because every input is proved inside the library. The book already says this, in Ch. 8, and the
point is sharpened rather than abandoned: the inputs are proved, so there is no logical gap, and
the open question is whether each is the classical theorem it is named for. It held that the four
obstacles contradict the book's premises; they are walls of the informal route, and the development
meets each of them with a proved lemma, which is now stated explicitly in Ch. 4. It held that the
two-thirds ceiling is conflated with the August proportion theorem; the remark's item 14 is a cost
accounting of the method, and the two are different statements, which Ch. 11 now separates.

**What the critique asserted without checking, and is now confirmed.** The 175,187 files and the
17.4 million lines: the community's notes give 175,187 `.lean` files, 1,030,531,854 bytes,
17,374,215 lines of which 15,531,759 are non-blank, with no comments, and 818,755 theorem and
lemma declarations.

**What the critique got right about the book.** The body does not omit Claude — Ch. 1 quotes the
remark's own opening sentence — but the cover copy did not name it. The cover and back cover now
do.

**A finding neither the critique nor the book had.** The community's notes record that a custom
tactic, `kexactB`, assigns a term to the goal without the elaborator checking that its type
matches, and is used in 67 files; `kcopy` does the same by rebuilding a term field by field. The
kernel still checks every declaration, so the proof is sound, and this is precisely why the proof
was re-checked with independent kernels. Now in Ch. 10.

**The revised verdict.** Formally certified, mathematically unaudited. The changes are set out in
`BUILD_NOTES.md` and the corrections log; the correction is recorded in the open rather than
quietly amended.
