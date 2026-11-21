#!/usr/bin/env python3
"""Restore the Key Takeaways item text.

An earlier repair script (fix_keytakeaways.py) removed the redundant inner
\\begin{itemize} wrapper correctly but also dropped the item bodies between
\\begin{keytakeaways} and \\end{keytakeaways}. This script refills each empty
environment with the text it should carry, in file order.
"""
import pathlib
import re
import sys

CH = pathlib.Path(__file__).resolve().parent.parent / "source" / "chapters"

BLOCKS = {
    "ch01.tex": [
        """\\item The document under examination is a four-page narrative plus a Lean
bundle. It contains no proof, no theorem statement in prose, and no definition
of the objects it names.
\\item The author states plainly that he has not mastered the surrounding
mathematics, that his own summary is ``slop'', and that the formalisation
``should suffice to clarify everything''.
\\item The author's timeline records an a-priori ceiling at two thirds and an
obstruction requiring a weakening of Vandiver --- both on 15 November --- with
GRH recorded the following day and no account of how either was closed.
\\item The remark's central mathematical idea --- finding an arithmetic
substitute for Stepanov's multiplicity over $\\ZZ$ --- is a real and sharp
observation about where the difficulty lies.""",
    ],
    "ch02.tex": [
        """\\item \\textbf{The statement is the real statement.} The submission does not
weaken the target. It proves Mathlib's own \\texttt{RiemannHypothesis}, and
Mathlib's own definition is the one written above.
\\item \\textbf{The submission is not conditional.} There are no hypotheses in
\\texttt{Main.lean} and no hypotheses in \\texttt{Statements.lean}.""",
    ],
    "ch03.tex": [
        """\\item The zeta function is defined by a convergent series only for
$\\Re s > 1$; everything interesting requires the analytic continuation, and the
Euler product cannot be used past that line.
\\item RH says every non-trivial zero of $\\zeta$ has real part exactly
$\\tfrac12$. It is a statement about one function, and a single counterexample
would refute it.
\\item Weil's criterion is a \\emph{positivity} condition,
$\\sum_\\rho \\hat g(\\rho)\\hat g(1-\\rho) \\ge 0$. The related inequality often
quoted in its place is not the criterion.
\\item Landau's oscillation theorem means that a \\emph{one-sided} bound on
$\\psi(x)-x$ at the $x^{1/2+\\varepsilon}$ scale would suffice for RH. This is
the form any analytic attack must take.
\\item RH is load-bearing for the prime number theorem's error term, for
randomness results about primes, and for much of the analytic theory of
$L$-functions.""",
    ],
    "ch04.tex": [
        """\\item The Stepanov--Bombieri method works over finite fields because the
product of the geometric and arithmetic coordinates is two-dimensional. Over
$\\ZZ$ it is one-dimensional, and the method does not transfer. This is the
structural reason the problem is hard.
\\item Automorphy of the required theta lift is, in the generality the remark
needs, an open problem; the unitary Gross--Prasad theorem is proved, the
orthogonal case is not, and no general result on the third-place lift was
located.
\\item Item 17 names a significant weakening of Vandiver as its remedy.
Vandiver is open; no such weakening is known; and the remark's own footnote
to that item is hedged with ``maybe?''.
\\item Item 14 records that the method ``would stop at 2/3 a priori'' on
15 November, and item 20 records GRH on 16 November, with no account of the
change. That gap is the central open question of this book.""",
    ],
    "ch05.tex": [
        """\\item The method has four stages: a sign-only Weil positivity statement, an
arithmetic divisibility engine based on CM curves and the identity
$qN = Mk + R$, an iterated theta-lift chain supplying the missing multiplicity,
and the automorphic/cocycle apparatus (relative trace formula, Rallis seesaw,
Iwasawa tower) needed to make the estimates legitimate.
\\item The vocabulary throughout is that of genuine research --- GGP periods,
interlacing weights, Chowla--Selberg, Siegel mass, Rallis seesaw, Bost's
slope method --- and the dates span six weeks of intensive work.
\\item The remark explicitly disclaims the authority of its own summary, and
disclaims the author's understanding of the parts he did not personally
develop.
\\item The remark does not explain how the two-thirds ceiling of 15 November
was crossed on 16 November. That is the central open question of this book,
and it is a question about the artifact, because the remark says the Lean
``should suffice to clarify everything''.""",
    ],
    "ch06.tex": [
        """\\item A proof assistant mechanically checks a finite term against inference
rules. It does not check that the proposition being proved is the interesting
one.
\\item \\texttt{\\#print axioms} is the standard check, and a clean result lists
only \\texttt{propext}, \\texttt{Classical.choice} and \\texttt{Quot.sound}. The
submission's axiom list is clean, which is a real and necessary result.
\\item Compilation establishes that a term of type \\texttt{RiemannHypothesis}
exists and depends on nothing unproved. It does not establish that the
statement of that type means what the claim says it means. That step is
human, and it is called statement review.
\\item The community's tooling for going further --- independent kernel replay
via \\texttt{lean4export} and NanoDa, sandboxed execution via
\\texttt{landrun}, third-party checking via \\texttt{lean4checker}, and the
Palomar registry --- is aimed squarely at the mechanical layers. None of it
reaches the mathematical one.""",
    ],
    "ch07.tex": [
        """\\item This link is mathematically correct. It is the standard reduction, it
handles the trivial zeros correctly, and it does not assume anything beyond
the non-vanishing hypothesis and the functional equation.""",
        """\\item The eight-link chain from Mathlib's \\texttt{RiemannHypothesis} down to a
proved Lefschetz formula is well-typed and mathematically well-formed at every
link examined.
\\item The reduction from non-vanishing to RH is the standard argument, handles
the trivial zeros correctly, and assumes nothing beyond the functional
equation and the hypothesis.
\\item The statement \\texttt{UpperTheory.EveryCharacter} is faithful and
non-vacuous, and it covers the Riemann zeta function as the $N=1$ instance.
\\item The bottom of the chain is a real proof of an étale Lefschetz fixed-point
formula, not a placeholder.
\\item Everything above the bottom of the chain is short. The mathematics is in
the inputs, and those are where the next chapter goes.""",
    ],
    "ch08.tex": [
        """\\item The automorphy step is carried by the bundle \\texttt{Hypotheses\\_2},
whose field \\texttt{newform} supplies the automorphic representation that the
downstream theorem consumes.
\\item The bundle's other fields are not assumptions in disguise: they are
derived in the source from named published results, through chains such as
\\texttt{clozelConjC\\_of\\_steps} above.
\\item The open question is therefore neither ``is this proved?'' nor ``is this
assumed?'' but the sharper one: \\emph{is each re-derivation faithful to the
published theorem it re-derives?}""",
        """\\item The development's architecture is sound and appropriate: published
results are re-derived, bundled, and then consumed by the argument.
\\item The automorphy step is carried by the bundle
\\texttt{Af.Hypotheses\\_2}, whose fields are derived in the source from named
published results --- not assumed, but re-derived, and the fidelity of those
re-derivations is the open question.
\\item The structure named \\texttt{admitted} means ``admitted into the
theory'', not ``admitted without proof''. It is a real admissibility
condition.
\\item The formalised epsilon estimate is a signature computation; whether it
corresponds to the remark's item 10 is an open discrepancy between the two
documents.
\\item The \\texttt{Hyps} package is constructed from row conditions rather
than assumed, which is the right shape for the kind of bundle that carries
the most risk.""",
    ],
    "ch09.tex": [
        """\\item Two independent scans agree: zero axioms, zero \\texttt{sorry}, zero
\\texttt{native\\_decide}, zero custom kernel escapes.
\\item A scan searches for markers of a specific failure mode. The failure mode
most likely to be present in a large, sophisticated development is a
\\emph{weakened hypothesis statement wearing a classical name}, and that
failure mode leaves no marker at all.
\\item A theorem whose proof is one line long, whose hypothesis is a structure
with a classical name, and whose axiom list is clean, has told you nothing
until you have read the structure's fields against the published theorem.""",
    ],
    "ch10.tex": [
        """\\item Two independent compilations succeeded on 20 November 2026, by
Andrew Sutherland at MIT and Simon DeDeo at CMU, and a third using a variant
of Lean.
\\item Compilation establishes completeness, reproducibility, pinning and the
axiom question. It does not establish that the statements mean what the claim
says they mean.
\\item The build attempted for this book reached the stage of compiling the
submission's own modules with Mathlib satisfied from cache, on a
two-core machine, and did not complete within the time available.
\\item The community's own history contains a case of a cleanly compiling
development withdrawn for a mathematical error. That is why ``compiled and
checked'' has two clauses.""",
    ],
    "ch11.tex": [
        """\\item The two-thirds theorem --- arXiv:2608.13637, Alpöge and Furman, August
2026 --- is the same method, the same author, and the same programme as the
claim under examination, three months earlier.
\\item It was independently reproduced by a third party, Lamzouri,
arXiv:2609.02882. It is a rigorous result, and it is the strongest positive
evidence about the method's quality.
\\item It is a \\emph{proportion} theorem: 67.25 per cent of zeros are simple
and on the line. It is not a proof of RH.
\\item The remark's item 14 records that the method ``would stop at 2/3
a priori''. The most economical explanation of the 15-to-16 November sequence
is that the extra work produced something the remark does not describe.""",
    ],
    "ch12.tex": [
        """\\item There is no preprint, no refereed report, no statement review and no
written proof. There is a remark, a mirror, two compilations, and press
coverage.
\\item The steps that have been completed are the mechanical ones: build, axiom
check, and the structural trace of Chapter~7. The steps that remain are the
mathematical ones, and they are the ones that decide the question.
\\item The absence of a review is evidence about the process, not about the
mathematics. It is not evidence of a defect and it is not evidence of
correctness.
\\item The remark itself consistently disclaims the authority that would make
review unnecessary. That disclaimer is the most credible thing in the
document, and it is also the reason a review is needed.""",
    ],
    "ch13.tex": [
        """\\item The finding: the claim is \\textbf{unresolved} as of 21 November 2026.
Neither established nor refuted.
\\item The artifact is clean, its reduction is sound, and its architecture is
appropriate. This is a serious submission, not a fabrication.
\\item The unexamined part is the fidelity of the load-bearing inputs to the
published theorems they encode.
\\item The remark's own timeline records two obstacles --- a two-thirds ceiling
and a Vandiver-dependent obstruction --- and does not say how either was
crossed.
\\item Three outcomes remain live: the artifact contains the missing
ingredient; the remark is out of date; or the formal theorem is weaker than
the headline. The available evidence does not discriminate between them.""",
    ],
    "ch14.tex": [
        """\\item Phase 1 --- build, axiom check, kernel replay, static scan --- is
mechanical and has effectively been done. It is cheap and reproducible.
\\item Phase 2 --- confirming the chain and confirming that the statement is
Mathlib's --- takes days and protects against working with the wrong version.
\\item Phase 3 --- statement review of the five load-bearing inputs, their
applications, and the remark against the code --- is weeks to months of
specialist work, and it is the step that decides the question.
\\item A successful review could refute the claim as well as confirm it. That
is what makes it worth doing.""",
    ],
    "ch15.tex": [
        """\\item If confirmed, RH would transform the error terms in analytic number
theory and would be the first major theorem established in a machine-checked
form.
\\item The AI dimension is best stated modestly: a structured, checkable
candidate was produced that a human could not have produced at all. The
August two-thirds theorem is the cleanest verified example.
\\item If refuted, the outcome would still be valuable: the formalised
programme would remain as a toolkit, and the subject's history is full of
cases where a failed attempt supplied the tools for a later success.
\\item What is true regardless: RH is not settled; more than two thirds of the
zeros are simple and on the line; the method works; verification at this
scale is feasible; and the evaluation procedure is known.""",
    ],
}


def main():
    for fname, blocks in BLOCKS.items():
        p = CH / fname
        t = p.read_text(encoding="utf-8")
        # fill each empty \begin{keytakeaways}...\end{keytakeaways}
        for body in blocks:
            pat = re.compile(r"(\\begin\{keytakeaways\}\s*)\\end\{keytakeaways\}")
            m = pat.search(t)
            if not m:
                print(f"  WARN: {fname}: no empty keytakeaways block for a pending body")
                continue
            t = t[:m.start()] + m.group(1) + "\n" + body + "\n" + m.group(0)[m.end(1) - m.start(1):] \
                if False else t[:m.start()] + m.group(1) + "\n" + body + "\n\\end{keytakeaways}" + t[m.end():]
        p.write_text(t, encoding="utf-8")
        print(f"{fname}: restored {len(blocks)} block(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
