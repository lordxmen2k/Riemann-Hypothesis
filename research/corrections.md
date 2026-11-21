# Corrections Log

A record of claims that were corrected, downgraded, or dropped during research. Corrections of
*my own* prior assumptions are listed first because those are the ones that would otherwise have
gone into print unchecked; corrections to the wider record are listed second.

---

## A. Corrections to my own working assumptions

| # | I initially held | The primary record says | Resolution in the book |
|---|---|---|---|
| A1 | The independent compilation of the Lean artifact had not happened; the mirror README's "no independent build" line was the current status. | The README line is dated 2026-11-20 (mirror time, morning). Quanta reported that day that Andrew Sutherland (MIT) compiled the artifact shortly before noon and Simon DeDeo (CMU) succeeded a few hours later. | The README line is quoted **with its date**, never as a current status. Ch. 10 reports the compilations as established. This changed the book's verdict from "unbuilt" to "built, unaudited". |
| A2 | The "2/3 of zeros on the critical line" result was by Saouter–Demichel–Planchat, obtained by the LP method with a crossing-zero value $L = 0.40$. | No such paper exists in arXiv, Crossref, HAL, or OpenAlex. The result is arXiv:2608.13637, **Alpöge & Furman** (13 Aug 2026), same author as the RH claim. | The attribution is corrected throughout. No $L = 0.40$ value appears in the book. Ch. 11. |
| A3 | The two-thirds result was a known pre-existing result that the submission merely reproduced. | It is the **same author's** own work, three months earlier, with the same method family, formally verified in Lean. | This is a major interpretive point, not a footnote: the method demonstrably produces rigorous results, and it demonstrably stopped at two thirds. Ch. 11. |
| A4 | Hart–Harvey–Ong verified Vandiver to $2^{31}$ in 1977. | *Math. Comp.* **86 (2017)** 3031–3049, DOI 10.1090/mcom/3211, arXiv:1605.02398. The year is 2017. | Corrected to 2017 throughout. |
| A5 | Weil's criterion reads $\sum_\gamma g(\gamma) \le g(0)$. | Weil's criterion is a **positivity** condition on a quadratic form: $\sum_\rho \hat g(\rho)\hat g(1-\rho) \ge 0$ for all admissible test functions. Weil's source is the **1952** Lund paper. | The book's statement of the criterion uses the correct positivity form. Ch. 3. |
| A6 | Guinand's relevant paper is *Sur les zéros de la fonction zêta de Riemann* (1955). | Guinand's relevant papers are the **1949 and 1950** Proc. LMS papers; the 1955 title could not be verified. | The book cites Guinand by the verified 1949/1950 records and makes no 1955 attribution. |
| A7 | Bost's *La conjecture de Weil* appeared in ASENS no. 4. | ASENS **30 (1997), no. 1**, 229–288, DOI 10.1016/S0012-9593(97)89923-8. | Corrected. |
| A8 | The higher-rank theta-lift theorem is due to "Gross–Petersson". | It is **Gross–Prasad**; the unitary case is proved in general, the orthogonal case remains open. | Corrected, and the unitary/orthogonal distinction is stated. |
| A9 | "LeanFRO" is a peer-reviewed paper. | No such paper was located. The Lean FRO is documented at `lean-lang.org/fro/about/`, and its tools are cited in the arXiv literature as "Lean FRO, 2025/2026". | The book refers to the FRO's *tools* and cites the arXiv literature's usage, not a nonexistent paper. |
| A10 | Radziwiłł–Soundararajan, "Continuous lower bounds for the Riemann zeta function", is a source for the proportion-of-zeros record. | The title as given could not be verified and appears to be mis-titled; the paper is about moments, not zero proportions. | Not cited. The record table uses only the sources actually verified. |
| A11 | Katz–Sarnak's 40\% chapter is a citable source for the proportion record. | Not verified as stated. | Not cited as such; the PRZZ and Lamzouri figures are used instead, with their own identifiers. |
| A12 | Behrend 1940 has a retrievable bibliographic record (and the Serre/Komatsu/Katsura number-field attributions are citable). | Behrend 1940 has no retrievable DOI/OpenAlex record in this session, and the Serre/Komatsu/Katsura attributions could not be verified. | The book cites Behrend for the mathematical content only, with no bibliographic identifier, and says explicitly that the number-field analogue remains open for $d\ge 2$. |
| A13 | The remark's item 14 ("one would stop at 2/3 a priori") is a description of a limitation the *Lean* overcomes. | The remark's item 14 is dated 11/15/26 and item 20 ("GRH") is dated 11/16/26. The remark offers no statement of how the 2/3 ceiling is crossed, and its author states that the timelines are "a rough timeline Claude provided" and that he is "paraphrasing a 'slop' summary". | The book does **not** assert that the formalization crosses the ceiling, nor that it fails to. It records the admission, records the absence of any explanation of the crossing, and identifies this as the first question a referee must answer. Ch. 5, 12, 13. |

## B. Corrections to the wider record

| # | Claim encountered | Correction | Source |
|---|---|---|---|
| B1 | The mirror README's static scan reports `opaque` 0, `unsafe`/`implemented_by`/`@[extern]` 0, `native_decide` 0, `admit` 0, `axiom` 0, `sorry` 0, `set_option maxHeartbeats 0` in 4 files, custom `macro`/`elab`/`syntax` in 22 files, `addDecl` in 1 file. | Retained, but quoted with the README's own caveat that the scan is "not a substitute for the steps above". The presence of `addDecl` in one file and of custom `macro`/`elab`/`syntax` in 22 is *not* treated as evidence of anything, in either direction. | Mirror README, static-scan section. |
| B2 | The mirror's description of the proof's structure is a summary of the author's own organisation. | Used only as a map of the file layout. Every structural claim in the book is re-derived from the source files directly. | Local extraction. |
| B3 | Community threads (Hacker News, Borretti's "Re: Riemann", a "Show HN" written proof of the Lean proof, a separate "Hurried Announcement: Alessandro Masullo GRH") constitute evidence about the state of the claim. | They are evidence that discussion exists and that independent attempts at a written proof were made, and nothing more. None is cited as a mathematical source, and none is used to support or refute the claim. | Research log only. |
| B4 | The remark's author names a list of mathematicians he consulted. | The list is reported as what the remark says, in the remark's own framing ("a lot of people I want to praise"). The book draws no inference from the presence of a name about the state of the proof, and in particular does not report any of these people as having endorsed it. | Remark, p. 2. |

## C. Claims deliberately left unverified, and flagged as such in the book

1. Whether the formalized inputs `TLiftK`, `Tools_k`, `EpsOf_k`, `Hyps`/`AllRows`, `Af.NewformAut`,
   `Af.AdVanishK`, `Af.AdVanishQ` and `Af.CongruenceNumberRankThree` correspond to the classical
   theorems their names suggest. **Not verified.** This is the book's central open question and is
   stated as such rather than resolved in either direction.
2. The precise statement of Bost's slope inequality as used in the argument. The source paper was
   located but the inequality itself was not retrieved from a primary text, so the book paraphrases
   Bost's method rather than quoting the inequality.
3. Whether the remark's `qN = Mk + R` is meant to be a Weil bound for a specific $L$-function, and
   which one. The remark's own footnote calls its description "obviously ... lossily compressed".
   The book reports the formula as the remark gives it and does not build on it.
4. The behaviour of the other compiler of the same method reported in a community thread
   ("Alessandro Masullo GRH"). No primary record was found; it is mentioned only as a fact about
   the attention landscape, with no mathematical content attributed to it.

## D. Numbers in the book that were recomputed rather than copied

- The library file counts (141 928 / 18 254 / 8 507 / 3 845 / 2 027 / 449 / 167 / 5 / 3 / 1) were
  recomputed locally from the extraction; they sum to 175 187, matching the mirror's figure.
- The proportions in the record table of Ch. 11 are given as the published decimals and as
  percentages, converted once, and are labelled with the distinction the sources make between
  "simple and on the line", "on the line", "distinct", and "simple or critical" — a distinction
  that is easy to lose and that materially changes which record is being claimed.
- The critical-line figure in Ch. 3 was computed for this book by a Riemann-von Mangoldt
  summation of $\zeta(\tfrac12+it)$ and is labelled as such; it is an illustration, not evidence
  for RH.
