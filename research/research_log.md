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

Structure designed **after** the research was collected and reviewed, as required. Five parts,
fifteen chapters:

| Part | Chapters | Purpose |
|---|---|---|
| I — The Claim | 1–2 | What was said, and what was submitted |
| II — The Mathematics | 3–5 | RH from first principles; the four barriers; the method as described |
| III — The Verification | 6–9 | What Lean can and cannot certify; the traced chain; the load-bearing inputs; the static scan |
| IV — The State of Play | 10–12 | The independent compilations; the two-thirds theorem; the absence of review |
| V — The Verdict | 13–15 | The finding stated precisely; a verification protocol; what a proof would change |

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
