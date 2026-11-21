Title: Is the Riemann Hypothesis Solved? A Critical Audit of the Lean Formalization, the Theta-Lift Method, and the Two-Thirds Ceiling

Creator: Gerald Enrique Nelson Mc Kenzie
Publisher: Tico Internet LLC
Edition: 2026 First Edition
License: Apache License 2.0
DOI: 10.5281/zenodo.24408811

On 20 November 2026 a mathematician published a four-page note claiming to have proved the Riemann Hypothesis, working with Claude, together with a Lean development of 175,187 files and 17.4 million lines. Two university teams compiled it the same day. The world's newspapers called it the greatest mathematical result of the century. On 21 November the Lean and Mathlib communities certified the formal status, with the endorsement of the Lean FRO and the Mathlib Initiative: the theorem proved is exactly Mathlib's own statement of the Riemann Hypothesis, matched by two independent tools, and the exported proof is accepted by Lean's kernel and by several independently written checkers, two of which carry formal soundness proofs relative to set theory. No mathematician has read the argument.

This book takes the artifact seriously, reads it, and reports what it establishes and what remains unestablished. It is not a book about the Riemann hypothesis; it is a book about what it takes to know whether a machine-checked proof of the Riemann hypothesis is a proof, worked through a specific case.

The finding is that the claim is formally certified and mathematically unaudited. The submitted formalisation contains no axioms and no admitted gaps, and the reduction from Mathlib's own RiemannHypothesis down to a proved holomorphic Lefschetz fixed-point formula was traced by hand and found mathematically sound. The book also identifies what remains unaudited: whether the load-bearing inputs carry the classical content they are named for. They are proved inside the library, so there is no logical gap in the chain; the open question is whether each of those statements is true. The author's own timeline records an a-priori ceiling at two thirds of the zeros and an obstruction whose stated remedy requires a weakening of Vandiver's conjecture, which is still open. The book reports what was checked, what was not, and gives a verification protocol that would settle the question.

Part III sets the method out step by step in eleven chapters, with the two-thirds ceiling computed directly from the submitted source, where it turns out to be a literal constant in the segment-degree threshold arithmetic. Part IV writes the same argument as mathematics, so that a reader with a mathematics background can follow it and arrive at the result, with the two places where the proof stops marked in place rather than at the end. Part V is the verification audit; Parts VI and VII give the state of play and the verdict.

The mathematics is explained from first principles: the zeta function, its analytic continuation, the functional equation, the critical strip, Weil's criterion in its positivity form, Landau's oscillation theorem, and the four obstacles that any method must clear, namely the collapse of the Stepanov-Bombieri geometric-arithmetic product over the integers, the open automorphy of the required theta lift, the surviving first cohomology classes, and the author's own recorded two-thirds ceiling.

Attribution: the mathematics examined in this book is the work of Levent Alpoge, who published the remark and the Lean development in public under his own name. This book reads that mathematics, sets it out in prose, and reports what has and has not been verified.

This book is for readers who want the mathematics and are willing to be walked through it, for readers who work on formal verification and want to know what the trust boundary actually is, and for readers who want to know how to evaluate the next claim of this kind.

285 numbered pages, plus full-bleed front and back covers. 34 chapters in 7 parts, 9 original figures, 5 tables, 43 glossary terms, 84 index headwords, 243 PDF bookmarks.

The Lean development examined in the book is the work of Levent Alpöge and is not redistributed here. This book quotes from the author's own remark and from the submitted source for the purposes of criticism and review, with attribution, and links to the original.

This book is published under the Apache License, Version 2.0. The complete licence text is available at https://www.apache.org/licenses/LICENSE-2.0.

Subject headings: Riemann hypothesis - Mathematical verification; Number theory - Computational methods; Formalization (Computer science); Machine learning - Mathematical applications; Proof assistants; Theta functions; Iwasawa theory.

Keywords
--------

Generic (10): mathematics; number theory; proof; theorem prover; formal verification;
computer-assisted proof; open problems; mathematics book; research monograph; mathematical
criticism.

Specific (10): Riemann hypothesis; Lean 4 theorem prover; Levent Alpöge; two thirds of zeros on
the critical line; Weil criterion; theta lift; Stepanov method; Vandiver conjecture; holomorphic
Lefschetz fixed-point formula; proof audit.
