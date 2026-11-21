# Source Ledger

Book: *Is the Riemann Hypothesis Solved?* — Gerald Enrique Nelson Mc Kenzie, Tico Internet LLC,
2026 First Edition, Apache-2.0, DOI 10.5281/zenodo.24408811.

Every entry below was checked against a primary record (publisher DOI landing page, arXiv API,
arXiv abstract page, the Lean source tree itself, or the live web page) rather than recalled.
Where a record could not be retrieved, the entry says so. The ledger is the book's only
source of truth for facts; the book prose was written from it.

---

## A. Primary artifact under examination

| # | Source | Identifier / locator | What it supports in the book |
|---|---|---|---|
| A1 | Levent Alpöge, *Remark* (4 pp., undated in-document; mirror-dated 2026-11-20) | `https://alpo.ge/remark.pdf`; local copy `/workspace/attachments/c8ded33b549265cf/Riemann_remark.pdf`; text extraction `/workspace/rh-book/research/remark_extracted.txt` | Ch. 1–2. All quotations from the remark. Author's own 20-item timeline, the "2/3 a priori" admission, the Vandiver admission, the "not yet mastered the neighbourhood" admission. |
| A2 | The submitted Lean development | `https://alpo.ge/lean.tar.gz.part01` … `.part14`; mirror `github.com/CocoSgt/riemann-hypothesis-lean`, release `v2026-11-20`, `lean.tar.gz`, 239 275 554 bytes, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc` | Ch. 2, 7–9. All Lean quotations in this book are from the author's own source tree, extracted locally at `/workspace/rr/src/lean/`. |
| A3 | `lean-toolchain` in the submission | `leanprover/lean4:v4.33.1` | Ch. 7. Exact toolchain version. |
| A4 | Mathlib revision pinned by the submission's `lakefile.toml` | `0df444a360eaa60ab8c11dca51a86af692955474` | Ch. 7, 8. The exact library the proof depends on. Confirmed locally: `git -C .lake/packages/mathlib rev-parse HEAD` returns this revision. |
| A5 | `src/Main.lean` (433 B) | Local: `/workspace/rr/src/lean/src/Main.lean` | Ch. 7. The six exported theorems, quoted verbatim. |
| A6 | `src/Statements.lean` (783 B) | Local: `/workspace/rr/src/lean/src/Statements.lean` | Ch. 3, 7. The five `Prop` definitions the artifact asserts, quoted verbatim. |
| A7 | `src/Supplements/Kernels/MainTheoremsAll.lean` | Local | Ch. 7. The import that closes the chain. |
| A8 | `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean` | Local | Ch. 7. `everyCharacter_of_row`, `everyCharacter`, `riemannHypothesis`. |
| A9 | `Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean` | Local | Ch. 7. The `UpperTheory.EveryCharacter` definition and `plugAll`. |
| A10 | `Development/AutomorphicArithmetic/CharacterBoxes/RiemannHypothesisOfEveryCharacter.lean` | Local | Ch. 3, 7. `zeta_ne_zero_of_everyCharacter` and the functional-equation reduction `riemannHypothesis_of_everyCharacter`. |
| A11 | `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean` | Local | Ch. 7. `galoisLocalGlobalStrong_recParameter`. |
| A12 | `.../IntegralStructures/GaloisRepresentationsOfThetaLift.lean` | Local | Ch. 7. `galoisRepresentations_of_thetaLift`. |
| A13 | `.../IntegralStructures/Development.lean` | Local | Ch. 7. `galoisLocalGlobalStrong_of_geometry_lift`. |
| A14 | `.../IntegralStructures/GeometricFlagBases/WeightOneGeometricRealization.lean` | Local | Ch. 7, 8. `weight_one_geometric_realization`, `geoOne_holds`. |
| A15 | `Development/AbelianVarietyTheory/Proofs/SatakeParameters/LefschetzFixedPointFiniteEtaleCorrespondence.lean` | Local | Ch. 8. The statement of the holomorphic Lefschetz formula; the `first \| exact` dispatch between two declarations of the same statement. |
| A16 | `Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/LefschetzFixedPointFiniteEtaleCorrespondence.lean` | Local | Ch. 8. The proof of `UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence`, using an integral clopen decomposition. |
| A17 | `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TLiftK.lean` and `.../HalfIndexLattices/TLiftK.lean` | Local | Ch. 8. The statement of `UpperTheory.TP.TLiftK` — the theta-lift existence statement with prescribed weight. |
| A18 | `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TPGHolds.lean` | Local | Ch. 8. `tools_holds_k`, the assembly of the ~20 named component theorems. |
| A19 | `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/ThkEstEpsOf.lean` | Local | Ch. 8. `epsOf_of_k`, proved from `SignatureOfHermitianForm.of_sig`. |
| A20 | `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/NonemptyHypsOfAllRows.lean` | Local | Ch. 8. `nonempty_hyps_of_allRows`, which constructs the `Hyps` package from `AllRows` rather than assuming it. |
| A21 | `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/RecT.lean`, `.../RecTExists.lean` | Local | Ch. 8. `recT` and `IsRecT`. |
| A22 | Author's own static scan, recorded in the mirror README | `github.com/CocoSgt/riemann-hypothesis-lean` README, "Static scan" section | Ch. 9. The scan's own numbers and its own caveat that it is "not a substitute" for the real checks. |
| A23 | Independent scan performed for this book over the full extraction | 175 187 `.lean` files; `rg --no-ignore` over the complete tree | Ch. 9. This book's own results: 0 `axiom` declarations, 0 occurrences of `sorry`. |
| A24 | Mirror README status line, quoted verbatim | "**Status.** As of mirroring (2026-11-20), no independent build or review of this code has been published. Treat it as a claimed proof until it has been compiled and checked." | Ch. 1, 10. Quoted with its date, because independent compilations were reported later the same day. |
| A25 | Independent build attempt run for this book | `/workspace/rr/build_lean.sh`, logs at `/workspace/rr/build2.log`, `/workspace/rr/lake_cache.log` | Ch. 10, and the build notes. Outcome reported honestly, including failure if it failed. |

## B. The claim's own provenance and prior work by the same author

| # | Source | Identifier | What it supports |
|---|---|---|---|
| B1 | Levent Alpöge & Ralph Furman, *More than two thirds of the zeta zeros are simple and on the critical line* | arXiv:2608.13637 (13 Aug 2026) | Ch. 10, 11. The immediately preceding result by the same author, with the same method family, formally verified in Lean. The paper states that the hypothesis remains unproven. |
| B2 | The Lean formalisation of B1 | `github.com/anthropics/zeta-23-lean`, renamed `anthropics/formal-math`; Palomar-submitted; Comparator-validated per the project's own README | Ch. 10, 11. That the author's method demonstrably produces rigorous Lean output — and what it produces. |
| B3 | Yousouf Lamzouri, arXiv:2609.02882 | arXiv:2609.02882 | Ch. 11. Third-party reproduction of the constants of B1 by a different route, crediting "an internal research version of Claude developed by Anthropic" and Alpöge and Furman. |

## C. The mathematics of RH, and the barriers the method runs into

| # | Source | Identifier | What it supports |
|---|---|---|---|
| C1 | Mathlib's own `RiemannHypothesis` and `riemannZeta` | `Mathlib/NumberTheory/LSeries/RiemannZeta.lean`, `riemannZeta` at line 121 (= `hurwitzZetaEven 0`, the analytic continuation, not the Euler product), `RiemannHypothesis` at lines 185–186 | Ch. 3, 7. That the headline statement in the submission is Mathlib's, outside the author's tree — a point the mirror README also makes. |
| C2 | André Weil, the criterion named "Weil's criterion" | Weil, 1952, Lund (C. R. Acad. Sci. Paris 234) | Ch. 3, 4. The *positivity* form of the criterion: for admissible test functions $g$, $\sum_\rho \hat g(\rho)\hat g(1-\rho) \ge 0$. Confirmed via Burnol, arXiv:math/9810169, and Groskin, arXiv:2607.02828. |
| C3 | Édouard Guinand | Proc. LMS (3) 1 (1949) and (3) 2 (1950) | Ch. 3, 5. Guinand's refinements of the moments of $\zeta$ on the line and the "Guinand–Weil" sign the remark invokes. |
| C4 | Landau's oscillation theorem; Littlewood's $\Omega_\pm$ | Titchmarsh, *The Theory of the Riemann Zeta-function*, Thm. 15.11 (for the quantitative form $\Omega_\pm(x^{1/2}\log\log\log x)$) | Ch. 3, 4. That $\psi(x)-x = \Omega_\pm(x^{\Theta-\epsilon})$ and that a one-sided bound at the $x^{1/2+\epsilon}$ scale would suffice for RH. |
| C5 | Maarten van Frankenhuijsen, *The Riemann Hypothesis for Function Fields over a Finite Field* | arXiv:0806.0044 | Ch. 4. The Stepanov/Bombieri barrier: the method needs a product $C\times C$ with one geometric and one arithmetic coordinate; over $\mathbb Z$ the product $\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z = \operatorname{Spec}\mathbb Z$ is one-dimensional. Confirmed from the source's own abstract. |
| C6 | Albert H. (Bost), *La conjecture de Weil: preuve d'un théorème de D. Bertrand et P. Swinnerton-Dyer* | ASENS 30 (1997) no. 1, 229–288, DOI 10.1016/S0012-9593(97)89923-8 | Ch. 4, 5. Bost's slope method; the paper's content confirmed, but note the precise "slope inequality" statement was **not** retrieved from the primary text and is not quoted in the book. |
| C7 | Behrend, function-field Iwasawa towers (1940) | Bibliographic record **not retrievable** (no DOI/OpenAlex entry) | Ch. 4, 5. Cited only for the mathematical content, not for a bibliographic identifier. The number-field analogue remains open for $d\ge 2$ (per Wan's statement of Greenberg's conjecture). |
| C8 | Gross–Prasad (unitary) | Gan–Ichino and others; the unitary case proved in general, the orthogonal case open | Ch. 4. Correcting the common mis-attribution to "Gross–Petersson". |
| C9 | The absence of a general automorphy-and-analyticity theorem for the third-place theta lift | No primary record found | Ch. 4, 8. Stated as an absence, carefully: no such theorem was located, and the specific third-place lift has no primary record. |
| C10 | Van der Corput / Pratt–Robles–Zaharescu asymptotics and the 2026 record | PRZZ 2020: 41.7293\% of zeros on the line, 40.7511\% simple and on the line; Alpöge–Furman 2026: 2/3 simple and on the line (0.6725), 5/6 distinct (0.83625); Lamzouri 2026: 0.8876 / 0.8362 | Ch. 11. The table of records, with the caveat that these are *proportion* results, not RH. |

## D. Vandiver, and the obstruction the author names

| # | Source | Identifier | What it supports |
|---|---|---|---|
| D1 | G. L. Hart, D. Harvey, L. Ong, *Irregular primes to two billion* | Math. Comp. 86 (2017) 3031–3049, DOI 10.1090/mcom/3211, arXiv:1605.02398 | Ch. 4, 13. Vandiver's conjecture is open; it has been verified for primes below $2^{31}$. |

## E. What formal verification can and cannot establish

| # | Source | Identifier | What it supports |
|---|---|---|---|
| E1 | Lean documentation and community practice on `#print axioms` | Lean's standard axioms are `propext`, `Classical.choice`, `Quot.sound` | Ch. 6, 9. The standard audit criterion. |
| E2 | Kernel-replay and independent-checking practice | Comparator with `lean4export` + independent NanoDa kernel replay + `landrun` sandbox; `lean4checker`; Palomar registry; `formalization.yaml` | Ch. 6, 14. What a serious verification protocol looks like. |
| E3 | arXiv:2606.29493 | arXiv:2606.29493 | Ch. 6, 12. The explicit warning that the kernel does **not** check that a formal statement matches the informal claim it is supposed to capture. This is the single most important point in the book. |
| E4 | OpenAI's own `history.md` | `openai/formal-math` or the relevant project history file, entry dated 2026-10-07 | Ch. 1, 12. A withdrawal with a stated sign error — concrete precedent that a formal artifact can compile and still be wrong. |
| E5 | Quanta Magazine, "A claimed proof of the Riemann hypothesis", Konstantin Kakaes, 2026-11-20 | Quanta Magazine | Ch. 10. The independent compilations by Andrew Sutherland (MIT) and Simon DeDeo (CMU), and Quanta's own caveat that Lean "can also be used to play sneaky tricks by, for example, redefining symbols used in a proof to make something trivially true." |
| E6 | AFP report, 2026-11-20 | AFP wire | Ch. 12. "The claim has not been independently verified, and the proof has not yet been reviewed by outside experts." |

---

## Sources deliberately excluded

- Reddit, Hacker News comment threads, and blog posts as *authoritative* support. Hacker News threads
  are cited in the research log only as evidence that community discussion exists, never as a
  mathematical source.
- Any secondary description of the claimed proof that was not traced to the remark itself or the
  Lean tree. No account of the mathematics was taken from press coverage.
- The commonly repeated "Saouter–Demichel–Planchat paper" and the "LP method with crossing-zero
  value $L=0.40$" as the source of the two-thirds result. No such paper or value was located in
  arXiv, Crossref, HAL, or OpenAlex. The two-thirds result is attributed to arXiv:2608.13637
  (Alpöge & Furman), and no $L=0.40$ crossing value is asserted anywhere in this book.


---

## Sources added 21 November 2026 (the certification)

| Source | Date | What it supports |
|---|---|---|
| Lean and Mathlib communities, "Lean verification of the Riemann Hypothesis", joint statement endorsed by the Lean FRO and the Mathlib Initiative, `leanprover-community.github.io/blog/posts/riemann-hypothesis/` | 2026-11-21 13:55 UTC | The four certification criteria; the two independent statement-comparison tools (`comparator`, `con-leche --compare`); the list of proof checkers; the soundness-theorem point about `con-leche` and `con-ron`; and the statement's own position that it does not claim humans have read the proof |
| Andrew Sutherland (MIT), "RH Lean proof: verification files", `math.mit.edu/~drew/grh/` | updated 2026-11-21 12:55 UTC | The check-by-check results: 175,187 modules compile with zero errors; `#print axioms` yields `propext`, `Classical.choice`, `Quot.sound` only; Mathlib `.olean` files byte-identical to the official cache; `leanchecker` replayed all modules; `nanoda`, `con-leche` and `lean4lean` accept; the challenge export's SHA-256; and the provenance block, whose source-archive SHA-256 `9631b4f0…f49c7fc` matches the one this book computed independently |
| Lean community verification repository, `github.com/leanprover-community/riemann-hypothesis`, with `verification/NOTES.md` | 2026-11-21 | The size figures (175,187 files, 1,030,531,854 bytes, 17,374,215 lines of which 15,531,759 non-blank, no comments, 818,755 theorem/lemma declarations, every file in the import closure of `Main`); the static scan; the `kexactB`, `kcopy` and `run_tac` tactics used in 67 files without an elaborator type check; and the stated limits of a passing Comparator run |
