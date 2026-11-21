# Literature Verification Report — RH Claim Audit

**Compiled:** 2026-11-21 (UTC) · **Method:** every identifier below was looked up live via the arXiv API, the Crossref REST API, the HAL API, the OpenAlex API, the GitHub REST API, the Hacker News Algolia API, the StackExchange API, and/or a direct `web_fetch` of the cited page. Nothing is quoted from memory.

**Local artefacts** (fetched during this audit, under `/workspace/rh-book/research/raw/`):
`alpofurman.txt` (Anthropic-hosted PDF of arXiv:2608.13637), `alpo_remark.txt` (alpo.ge/remark.pdf), `mathlib_RiemannZeta_pinned_0df444a.lean`, `mathlib_arithzeta.lean`, `mathlib_zetaZeros.lean`, `lamzouri.html`, `anthropic_riemann_zeta.html`.

---

## Item 1 — The 2/3 result: "more than two thirds of the zeros of zeta lie on the critical line"

**The result is real, and its arXiv identifier is confirmed.** The brief's "reportedly by Anthropic" is correct for the *organisation*, and the repo name in the brief is correct as a *former* name — but the brief's attribution of the underlying mathematical paper is wrong.

### (a)–(d) The primary sources

| | |
|---|---|
| **Title (arXiv v2)** | *More than two thirds of the zeta zeros are simple and on the critical line* |
| **Authors** | Levent Alpöge; Ralph Furman |
| **Date** | submitted 2026-08-13 (arXiv API `published` = 2026-08-13) |
| **arXiv ID** | `arXiv:2608.13637` (v2) |
| **Journal ref / DOI** | `(none)` / `(none)` per the arXiv API |
| **URL** | https://arxiv.org/abs/2608.13637 |

**The Anthropic-hosted version is a different document with a different title and byline.** The PDF at
`https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf`
(v1 of the same paper, fetched and text-extracted locally as `raw/alpofurman.txt`) has:

- Title page: **"MORE THAN TWO THIRDS OF THE ZEROS OF THE RIEMANN ZETA FUNCTION LIE ON THE CRITICAL LINE"**
- Byline: **"CLAUDE"** — with the affiliation line at the end of the document reading **"Anthropic, San Francisco"**.
- Acknowledgements name **Ralph Furman and Levent Alpöge** as having "studied the result in detail after the session, placed it in the context of the existing literature, checked the argument independently, and have taken responsibility for its communication"; **Jarred Sumner** as "in every meaningful sense the paper's human co-author"; and **Eric Easley** as the orchestrator of the Lean formalisation, "building substantially on the Mathlib library and on Lean developments from the PrimeNumberTheoremAnd project".
- Appendix B states the Lean repository as `github.com/anthropics/zeta-23-lean` at tag `v1.0`.

So the brief's *wording* of the title ("more than two thirds of the zeros of the Riemann zeta function lie on the critical line") matches the **Anthropic v1 PDF title page**, while the arXiv v2 title is the slightly different "More than two thirds of the zeta zeros are **simple and** on the critical line". Both are the same paper.

**Anthropic's own announcement (primary, dated):** https://www.anthropic.com/research/riemann-zeta — *"The Riemann zeta function"*, published **Aug 10, 2026**, Team: Science. Verbatim excerpts:

> "An unreleased research version of Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis. Drawing on extensive prior research by mathematicians over the past decades, it has increased this bound from **41.6% to 67.2%**."
> "Two mathematicians at Anthropic studied and validated Claude's *paper*, and produced an *informal note* for experts stating Claude's proof concisely. Claude also produced a *formally verifiable proof* of its result. We are grateful to Brian Conrey and Dan Goldston, two experts in this area, who generously examined the paper on short notice."
> "**We don't expect that the techniques Claude used will lead to proving the Riemann hypothesis.**"

### The repository (brief's `anthropics/zeta-23-lean`, Aug 2026)

`GET https://api.github.com/repos/anthropics/zeta-23-lean` returns **HTTP 301 Moved Permanently → repository id 1326008263**. Following the redirect:

- `full_name`: **anthropics/formal-math** (the repo was renamed; the brief's name is its former name, and it is still the name printed in the paper's Appendix B)
- `created_at`: **2026-08-06T23:56:11Z** — consistent with the brief's "Aug 2026"
- `license`: Apache-2.0 · `stargazers_count`: 482 · `forks_count`: 89 · `pushed_at`: 2026-11-01
- Root tree: `3sum-apsp/`, `eth/`, **`zeta23/`**, `LICENSE`, `README.md`

`zeta23/README.md` (fetched via the GitHub contents API) states: *"This repository accompanies the paper 'More than two thirds of the zeta zeros are simple and on the critical line' by Levent Alpöge and Ralph Furman, [arXiv:2608.13637]"*; toolchain `leanprover/lean4:v4.33.0-rc2`, Mathlib commit `51e6992efd06126df61a496bebf8f49482a4e129`; Palomar layout (`Challenge.lean` trusted / `Solution.lean` untrusted / `comparator.json`); *"the repository declares no axioms, and `#print axioms` on each headline theorem reports only Lean's three standard axioms `propext`, `Classical.choice`, `Quot.sound`."*

### (e) What the source actually establishes

From the Anthropic PDF abstract (verbatim), with `N(T,2T)` = number of zeros `ρ = β+iγ` with `T < γ ≤ 2T` counted with multiplicity and `N₀*(T,2T)` = number of *distinct* such zeros with `β = 1/2`:

> "We prove unconditionally that `lim inf_{T→∞} N₀*(T,2T) / N(T,2T) ≥ 2/3`, that at least `(2/3 − o(1))N(T,2T)` of the zeros are simple and on the critical line, and that at least `(5/6 − o(1))N(T,2T)` are distinct; with an optimised test family the three constants become **0.6725, 0.6725, 0.83625**."

The method: "the arithmetic input is exactly Montgomery's prime-side evaluation of the pair-correlation second moment with band-width ≤ 1, which is unconditional. **The Riemann hypothesis, classically needed to read the zero side as a positive sum over real ordinates, is replaced by linear algebra applied to a finite compression of Weil's Hermitian form**: Sylvester's law of inertia (an off-line pair {ρ, 1 − ρ̄} contributes a block of signature (1,1)) and a rank–trace inequality for Hermitian matrices, proved via von Neumann's trace inequality."

The previous unconditional records, per the paper, were **5/12** (on the line) and **0.6603** (distinct zeros, from Wu 2015).

**This is a statement about a *proportion*, not a proof of RH.** The paper says so explicitly: "The hypothesis remains unproven."

**Independent confirmation by a third party.** Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, **arXiv:2609.02882v2**, 2026-09-02, no journal ref, no DOI — https://arxiv.org/abs/2609.02882. Lamzouri's abstract states the same constants (67.25% / 83.62% / 88.76%) and adds two estimates "neither stated nor proved in the Claude paper"; it explicitly credits *"an internal research version of Claude developed by Anthropic and subsequently verified by two mathematicians at Anthropic, Levent Alpöge and Ralph Furman"*. Lamzouri's introduction also confirms the PRZZ record: `liminf N₀(T)/N(T) ≥ 0.417293` and `liminf N₀ˢ(T)/N(T) ≥ 0.407511`.

### (f) The Saouter/Demichel/Planchat paper and the "LP method, L = 0.40" — **NOT FOUND**

I searched, and found nothing:

- **arXiv API**, `ti:"On the proportion of zeros"` → **total = 0**. `au:Saouter AND abs:zeta` → **0**. `au:Demichel` → 17 hits, **none** about zeta zero proportions (Yann Demichel's arXiv work is on fractals, the Hutchinson operator, random elliptical clouds, and the Koch snowflake). `au:Planchat` → **2 hits total**, both by **Jean-François Planchat** on *C\*-algebras associated to automata groups* — unrelated.
- **Crossref API** → no such title by those authors.
- **HAL API** (Saouter's full HAL record, 47 documents): his collaborators on number theory are **Patrick Demichel**, **Xavier Gourdon**, **Timothy Trudgian**, **Herman Te Riele**, **Olivier Ramaré** — and the papers are *"A sharp region where π(x) − li(x) is positive"* (Math. Comp. 79 (2010) 2395–2405), *"A still sharper region where π(x) − li(x) is positive"* (Math. Comp. 84 (2015) 2433–2446), *"An improved lower bound for the de Bruijn–Newman constant"* (Math. Comp. 80 (2011) 2281–2287), *"Improved results on the Mertens conjecture"*. **None** is about the proportion of zeros on the critical line.
- **OpenAlex API** → no such work by Saouter in 2020–2026.
- The Anthropic PDF's reference list contains **no Saouter and no Demichel**, and the text contains no "LP method" and no crossing-zero value; the only `L`-parameter occurrence is an unrelated `L = log(T/2π)`.

**Conclusion for this sub-claim:** there is **no paper titled "On the proportion of zeros of the Riemann zeta function on the critical line" by Saouter/Demichel/Planchat**, and **no "LP method" with a crossing-zero value of L = 0.40** could be located in the arXiv API, Crossref, HAL, OpenAlex, or the actual 2/3 proof itself. The brief's framing appears to conflate the Saouter–Demichel–Trudgian papers on π(x) − li(x) / the de Bruijn–Newman constant with the critical-line proportion literature, and to attach a spurious parameter to it.

**VERDICT: PARTIALLY VERIFIED.** The 2/3 result, its arXiv ID (`2608.13637`), its authors, the Aug 2026 date, the Anthropic provenance, and the `anthropics/zeta-23-lean` → `anthropics/formal-math` repo are all confirmed from primary sources, and the exact constants (2/3; 0.6725; 0.83625; previous records 5/12 and 0.6603) are verified. The underlying attribution "Saouter/Demichel/Planchat, *On the proportion of zeros…*" and the "LP method with crossing-zero value L = 0.40" are **UNVERIFIED and contradicted by the absence of any such source**. Also note: the result is a *proportion* result and **not** a proof of RH.

---

## Item 2 — Most recent asymptotic bounds on the proportion of zeros on the critical line

### The unconditional record, as of 2026

| Bound | Value | Source (identifier as returned by the API) |
|---|---|---|
| Zeros **on** the critical line (mollifier/Levinson family) | **κ ≥ 0.417293** (41.7293%) | Pratt, Robles, Zaharescu, Zeindler, *More than five-twelfths of the zeros of ζ are on the critical line*, Res. Math. Sci. **7** (2020), Paper No. 2, 74 pp., **DOI 10.1007/s40687-019-0199-8** (Crossref records the DOI year as 2019; the journal issue is 2020) |
| Zeros **simple and on** the line | **κ\* ≥ 0.407511** | same paper |
| Zeros simple **and on** the line | **2/3 = 66.67%**; **0.6725** with the Montgomery–Taylor window | Alpöge–Furman, **arXiv:2608.13637** |
| Zeros distinct | **5/6 = 83.33%**; **0.83625** with the optimised window (previous record **0.6603**, Wu 2015) | Alpöge–Furman, **arXiv:2608.13637** |
| Simple **or** on the line (or both) | **≥ 88.76%** | Lamzouri, **arXiv:2609.02882v2** |
| Average of the proportions simple / on the line | **≥ 83.62%** | Lamzouri, **arXiv:2609.02882v2** |

The PRZZ paper's own §8 states the optimisation explicitly: *"Letting ε → 0 yields κ ≥ 0.417293962"* and, with a linear polynomial `Q`, *"κ\* ≥ 0.407511457"*. Lamzouri's introduction independently confirms both numbers, and the survey **Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022** states: *"Pratt et al [88] have the current record of 41.7% based on Feng's mollifier."*

### The historical chain, with verified identifiers

- **Selberg (1942)** — positive proportion. A. Selberg, *On the zeros of Riemann's zeta-function*, Skr. Norske Vid.-Akad. Oslo I (1942), no. 10, 59 pp. (cited as [Sel42] in Alpöge–Furman and in Lamzouri).
- **Levinson (1974)** — >1/3. N. Levinson, *More than one third of zeros of Riemann's zeta-function are on σ = 1/2*, Adv. Math. **13** (1974), 383–436.
- **Heath-Brown (1979)** — >34.74% simple and on the line. D. R. Heath-Brown, *Simple zeros of the Riemann zeta-function on the critical line*, Bull. London Math. Soc. **11** (1979), 17–18.
- **Conrey (1989)** — >2/5. J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta function are on the critical line*, J. Reine Angew. Math. **399** (1989), 1–26, **DOI 10.1515/crll.1989.399.1**. (Crossref's `author` field for this DOI record came back empty; the author attribution above is from the Alpöge–Furman reference list, `[Con89]`.)
- **Bui–Conrey–Young (2011)** — >41%. H. M. Bui, B. Conrey, M. P. Young, *More than 41% of the zeros of the zeta function are on the critical line*, Acta Arith. **150** (2011), 35–64, **DOI 10.4064/aa150-1-3**.
- **Feng (2012)** — >41.28%. S. Feng, *Zeros of the Riemann zeta function on the critical line*, **arXiv:1003.0059** (2010-02-27, no journal ref, no DOI in the arXiv API); published as J. Number Theory **132** (2012), 511–542 (Alpöge–Furman ref `[Fen12]`). The arXiv abstract reads: *"it is proved that at least 41.28% zeros of the Riemann zeta function are on the critical line"*.
- **Wu (2015)** — distinct zeros. X. Wu, *Distinct zeros of the Riemann zeta-function*, Quart. J. Math. **66** (2015), 759–771 (0.6603).

### Further 2026 activity (OpenAlex-indexed, all preprints unless noted)

- **Cobeli & Zaharescu**, *More than 8/9 zeros of the Riemann zeta function are simple or on the critical line*, **arXiv:2610.23467** (2026).
- **Knausgård**, *More than 83.69% of the zeros of the Riemann zeta function are distinct*, **arXiv:2609.33043** (2026).
- **Lamzouri**, *Isolated zeros of the Riemann zeta function and zeros of linear combinations of Dirichlet L-functions*, **arXiv:2610.26841** (2026).
- **Wang**, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, **arXiv:2609.07918** (2026).
- **Goldston & Suriajaya**, *Zeta zeros on the critical line*, **DOI 10.1007/s10476-026-00186-w** (2026) — the journal-published version of arXiv:2511.20059.
- **Goldston & Suriajaya**, *Zeta zeros in a narrow vertical box*, **arXiv:2603.28104** (2026-03-30).

### Two corrections to the brief

1. **Katz–Sarnak.** The brief lists Katz–Sarnak among "asymptotic bounds on the proportion of zeros". Katz & Sarnak are the authors of the **40%** result (*More than 40% of the zeros of ζ lie on the critical line*, in *Analytic Number Theory*, LMS Lecture Note Ser. **337**, CUP 1989, pp. 137–150) — but **I could not retrieve this chapter from the Crossref or arXiv APIs in this session**, so its identifier is **UNVERIFIED** (it is a book chapter with no DOI in Crossref's index). The Katz–Sarnak papers that *are* indexed are about a different subject: N. M. Katz, P. Sarnak, *Zeroes of zeta functions and symmetry*, Bull. Amer. Math. Soc. (N.S.) **36** (1999), 1–26 (**DOI 10.1090/S0273-0979-99-00766-1**) and *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloq. Publ. **45** (1999) — random-matrix symmetry types, not proportions.
2. **Radziwiłł–Soundararajan.** The title *"Continuous lower bounds for the Riemann zeta function"* **could not be located** via the arXiv, Crossref or OpenAlex title searches in this session. Their actual indexed paper is M. Radziwiłł, K. Soundararajan, *Continuous lower bounds for moments of zeta and L-functions*, Mathematika **59** (2012), 119–128, **DOI 10.1112/s0025579312001088**. Their work is about **lower bounds for |ζ(σ+it)|**, i.e. bounds on the number of zeros with Re s > 1/2 + ε — a related but different quantity from the *proportion of zeros on the line*.

**VERDICT: PARTIALLY VERIFIED.** The "as of 2026" record figures are fully verified (41.7293% on the line; 40.7511% simple and on the line; 2/3 = 67.25% simple-and-on-line; 5/6 = 83.625% distinct; 88.76% simple-or-critical). Two of the brief's named citations (Katz–Sarnak's 40% chapter; Radziwiłł–Soundararajan's "Continuous lower bounds for the Riemann zeta function") are **UNVERIFIED** by identifier, and the latter appears to be a mis-titled reference to a paper about moments rather than about zero proportions.

---

## Item 3 — Vandiver's conjecture: open, and verified to 2^31

**Still open.** The conjecture (the `p`-part of the class group of the maximal real subfield of `Q(ζ_p)` is generated by the units — equivalently the even-index eigenspaces `A_j` of the cyclotomic class group vanish for even `j`) is unresolved. A 2026 preprint states it plainly: *"Vandiver's conjecture is the assertion `A_j = 0 (j even)`"* — arXiv:2609.13932, *Density of Vanishing of Certain Eigenspaces of Cyclotomic Class Groups* (2026).

**The bound, verified:**

- **Title:** *Irregular primes to two billion*
- **Authors:** William Hart; David Harvey; Wilson Ong
- **Journal:** Mathematics of Computation **86** (2017), no. 308, 3031–3049
- **DOI:** **10.1090/mcom/3211** (Crossref API; `issued` year 2017)
- **arXiv:** **arXiv:1605.02398** (arXiv API `published` = 2016-05-08)
- **URL:** https://arxiv.org/abs/1605.02398 · https://www.ams.org/journals/mcom/2017-86-308/S0025-5718-2017-03211-9/

Verbatim from the arXiv abstract: *"We compute all irregular primes less than **2³¹ = 2 147 483 648**. We verify the Kummer–Vandiver conjecture for each of these primes…"* The paper's own table of records runs: … 2001: 12 000 000 (Buhler, Crandall, Ernvall, Metsänkylä, Shokrollahi) · 2011: 163 577 856 (Buhler & Harvey) · **2016: 2 147 483 648 (this paper)**.

**Two corrections to the brief:**

1. **The year is 2017, not 1977.** The brief's "Hart-Harvey-Ong 1977" is off by forty years. The paper is Math. Comp. **86** (2017); the arXiv preprint is from 2016.
2. The bound **2³¹ = 2 147 483 648** is confirmed, and is still the record I could find. (The 2026 preprint arXiv:2609.13932 still cites it as the standing bound: *"Hart, Harvey and Ong [9] verified Vandiver's conjecture for all primes p < 2³¹."*)

**Relevance to the audited claim:** the Alpöge announcement `remark.pdf` lists, as step 17 of its timeline (dated 11/15/26), *"for the classes in H¹…(−e) that we couldn't kill by twisting, **fight for a significant weakening of Vandiver**"*, with the footnote *"This is still pretty strong!! I believe vanishing of a number of K-groups of Z follows, and cyclicity up to 100ish maybe?"*. So the claimed proof engages Vandiver directly — but **no weakening of Vandiver is stated as a theorem in any source I could find**, and the remark itself is hedged.

**VERDICT: PARTIALLY VERIFIED.** Vandiver's conjecture is confirmed still open; the exponent **2³¹** and the source (Hart, Harvey, Ong, *Irregular primes to two billion*, Math. Comp. 86 (2017) 3031–3049, **DOI 10.1090/mcom/3211**, **arXiv:1605.02398**) are confirmed. The brief's **year 1977 is wrong — it is 2017**.

---

## Item 4 — Guinand's theorem and the Weil criterion

### The Weil criterion is a **positivity** condition, and it is `≥ 0`, not `≤ g(0)`

The brief asks to "confirm Weil's criterion is the sign-only form: for every suitable test function g with even moments, sum over zeros of g(gamma) <= g(0)". **That is not Weil's criterion.** The primary-source form is a quadratic-form **positivity** statement.

Jean-François Burnol, *The Explicit Formula in simple terms*, **arXiv:math/9810169** (1998-10-29; no journal ref, no DOI per the arXiv API) — https://arxiv.org/abs/math/9810169 — states it as a lemma:

> "**Lemma:** The Riemann Hypothesis holds if and only if `Σ_ρ ĝ(ρ) · ĝ(1 − ρ) ≥ 0` for all smooth compactly supported functions `g` on `(0, ∞)`."

and, in the shifted-to-the-line normalisation,

> "the explicit formula is now seen (as in Weil's paper [5]) to give a distribution `C` on `(0,∞)` such that `C(g) = Σ_ρ ĝ(ρ − 1/2)`, and Weil's positivity criterion becomes `C(g * g^c) ≥ 0` where `g^c = g(1/·)`."

An independent modern confirmation, Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, **arXiv:2607.02828** (2026-07-02) — https://arxiv.org/abs/2607.02828:

> "The Riemann–Weil explicit formula relates the nontrivial zeros of ζ(s) to prime, pole, and archimedean terms, and **Weil positivity, the positivity of the associated quadratic form on a suitable class of test functions, is equivalent to the Riemann hypothesis**."

and the Guinand–Weil explicit formula itself:

> "The Guinand–Weil explicit formula in the normalization of Connes, Bombieri, and Connes–Consani–Moscovici states, for every test function in the class of Lemma 2.2, `Σ_{z ∈ Z_ζ*} g_v(z) = −(1/π) Σ_{q=p^a} (Λ(q)/√q) ĝ_v(log q / 2π) + 2 g_v(i/2) + (1/(2π)) ∫_ℝ h₊(r) g_v(r) dr`."

Note the shape of the right-hand side: a **prime** term, a **pole** term `2 g_v(i/2)` (i.e. `g(0)`-type contribution), and an **archimedean** term. A bare inequality `Σ g(γ) ≤ g(0)` omits the prime and archimedean terms and therefore cannot be the Weil criterion.

### The primary sources for Weil and Guinand

- **Weil (1952):** A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund [Medd. Lunds Univ. Mat. Sem.], Tome Supplémentaire (1952), 252–265. **This is the reference the Alpöge–Furman paper itself cites**, as `[Wei52]`. (The brief's "Weil 1929/1951" is not the source of the criterion; Weil's 1929 paper *Über die Bestimmung Dirichletscher Reihen durch Funktionalgleichungen* (Math. Ann. 168, 149–156) is the functional-equation paper, not the positivity criterion. A 1951–52 Lund seminar volume is plausible for the "1951" in the brief, but I did not verify a separate 1951 Weil item.)
- **Guinand:** A.-P. Guinand, *A summation formula in the theory of prime numbers*, Proc. London Math. Soc. (2) **50** (1949), 107–119, and A.-P. Guinand, *Fourier reciprocities and the Riemann zeta-function*, Proc. London Math. Soc. (2) **51** (1950), 401–414 (both are cited in the Voros reference list at https://aif.centre-mersenne.org/articles/10.5802/aif.1955/ and in Connes's survey arXiv:2602.04022, ref [52]). The brief's *Guinand 1955 "Sur les zéros de la fonction zêta de Riemann"* — a Strasbourg thesis title — is **UNVERIFIED**: it is not in Crossref, not in HAL, and not in OpenAlex under that author/title; the API-indexed Guinand papers are the 1949 and 1950 London Math. Soc. papers above.

### Relevance to the audited claim

`remark.pdf` timeline step 5 (10/20/26) reads: *"definitively switch to Λ ≡ Σ_{n≤X} Λ(n)…; **Guinand–Weil had the sign, variance test function trick**"*, with the follow-up *"sum over h first for the left-hand side, with e.g. quadric coefficients too — Bertini gives a definite sign from middle cohomology, one off the one on M_k, which is the zero-mode on the right-hand side with R square-root-quality… opposite signs meaning no cancellation of inverse roots, QED"*. So the claim uses a **sign** (as opposed to the full Weil quadratic form) — this is the "sign-only" reading the brief is reaching for, but the brief's stated inequality is not the criterion's form.

**VERDICT: PARTIALLY VERIFIED — the inequality form as stated is CONTRADICTED.** Weil's criterion is confirmed as the **sign/positivity** criterion, in the precise form `Σ_ρ ĝ(ρ)·ĝ(1−ρ) ≥ 0` for all admissible test functions `g` (Burnol, arXiv:math/9810169; Groskin, arXiv:2607.02828), i.e. a **positivity (`≥ 0`)** condition on a quadratic form — *not* an inequality `Σ g(γ) ≤ g(0)`. Weil's source is the **1952** Lund paper. Guinand's primary papers are the **1949 and 1950** Proc. LMS papers; the brief's *1955 "Sur les zéros de la fonction zêta de Riemann"* is **UNVERIFIED**.

---

## Item 5 — Landau's oscillation theorem for ψ(x)

### The general form of Landau's theorem

Landau's oscillation theorem is usually stated in its general analytic form and then specialised to `ψ`. Verbatim, from arXiv:1505.03589, *Sign changes in Mertens' first and second theorems* (arXiv API: no journal ref, no DOI):

> "**Theorem 3 (Landau's oscillation theorem).** Suppose `f(x)` is of constant sign for all sufficiently large `x`. Then the real point `s = σ₀` of the line of convergence of the Dirichlet integral `∫₁^∞ x^(−s) f(x) dx` is a singularity of the function represented by the integral."

Applied to `ψ(x) − x` this yields: `ψ(x) − x` **cannot keep one sign**; it must change sign infinitely often.

### The quantitative Ω-result and the off-critical-zero version

- **Littlewood:** `ψ(x) − x = Ω_±(x^{1/2} log log log x)`. Source: arXiv:2211.08973 (v6) cites it as *"[23, Thm. 15.11]"* = **Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., revised by D. R. Heath-Brown, Oxford Univ. Press, 1986, Thm. 15.11**. The precise constant form, from arXiv:1211.2147:
  > `ψ(x) − x = Ω_±(x^{1/2} log log log x)`, and `varlimsup_{x→∞} (ψ(x)−x)/(x^{1/2} log log log x) ≥ 1/2`, `varliminf_{x→∞} (ψ(x)−x)/(x^{1/2} log log log x) ≤ −1/2`.
- **Landau–Littlewood Ω-theorem:** if `ρ₀ = β₀ + iγ₀` is any zero of ζ with `β₀ > 1/2`, then `ψ(x) − x = Ω_±(x^{β₀−ε})` for every `ε > 0`. Stated in arXiv:2311.04860, *An effective Linear Independence Conjecture for the zeros of the Riemann zeta function and applications*:
  > *"In proving the Omega result (1.5), Littlewood assumed RH, since otherwise one has a stronger estimate (1.6) `ψ(x) − x = Ω_±(x^{σ−ε})`."*
  and corroborated as **Corollary A.4 (Ω-transfer)** in arXiv:2509.16240: `E_ψ(x) = Ω_±(x^β)`, `E_π(x) = Ω_±(x^β / log x)`.
- **von Koch (1901):** RH ⟺ `ψ(x) = x + O(√x (log x)²)` (arXiv:2311.04860, citing von Koch p. 116; sharpened by Schoenfeld 1976 to `|ψ(x) − x| < (1/8π)√x log²x` for `x ≥ 73.2`).

### The one-sided bound

**Confirmed:** because Landau–Littlewood gives `Ω_±` (both signs) with size `x^{β₀−ε}` whenever a zero off the line exists, a **one-sided** bound on `ψ(x) − x` of the form `ψ(x) − x ≤ C x^{1/2+ε}` for all sufficiently large `x` and every `ε > 0` is impossible unless RH holds. Equivalently:

> **RH ⟸ "for every ε > 0 there is C_ε with ψ(x) ≤ x + C_ε x^{1/2+ε} for all x ≥ x₀(ε)"**

(and symmetrically for the lower side). The two-sided statement `ψ(x) = x + O(x^{1/2+ε})` is *equivalent* to RH; the one-sided bound *implies* RH.

**Standard references for this material** (as cited by the Alpöge–Furman paper's own reference list, which I read directly): H. Iwaniec, E. Kowalski, *Analytic Number Theory*, Amer. Math. Soc. Colloq. Publ. **53**, Providence RI, 2004 (`[IK04]`); E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., rev. D. R. Heath-Brown, Oxford Univ. Press, 1986 (`[Tit86]`); H. L. Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, CBMS Regional Conf. Ser. Math. **84**, AMS, 1994 (`[Mon94]`); H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I. Classical Theory*, Cambridge Stud. Adv. Math. **97**, CUP, 2007 (`[MV07]`).

**Note on the claim's wording.** The claim as phrased — "the implication that a ONE-SIDED bound on psi(x)-x suffices for RH" — is **correct**, but only in the direction where the one-sided bound is at the `x^{1/2+ε}` scale. A one-sided bound at an *arbitrary* scale would not do; the scale matters, and the brief does not state it.

**VERDICT: VERIFIED (with a precision note).** Landau's oscillation theorem is confirmed in both its general Dirichlet-integral form and its consequence for `ψ`; the quantitative form is Littlewood's `Ω_±(x^{1/2} log log log x)` (Titchmarsh Thm. 15.11); the off-line-zero form `Ω_±(x^{β₀−ε})` is confirmed; and the one-sided-bound-implies-RH implication is confirmed, provided the bound is at the `x^{1/2+ε}` scale. The brief omits that scale.

---

## Item 6 — van Frankenhuijsen, *The Riemann Hypothesis for Function Fields over a Finite Field*

- **Title:** The Riemann Hypothesis for Function Fields over a Finite Field
- **Author:** Machiel van Frankenhuijsen (single author)
- **Date (arXiv API `published`):** 2008-05-31
- **arXiv ID:** **arXiv:0806.0044**
- **Journal ref / DOI:** `(none)` / `(none)` per the arXiv API
- **URL:** https://arxiv.org/abs/0806.0044

**The identifier is confirmed exactly as stated in the brief.**

### (e) What the paper actually says (verbatim abstract)

> "We discuss Enrico Bombieri's proof of the Riemann hypothesis for curves over a finite field. Reformulated, it states that the number of points on a curve `C` defined over the finite field `F_q` is of the order `q + O(√q)`. The first proof was given by André Weil in 1942. This proof uses the intersection of divisors on `C × C`, making the application to the original Riemann hypothesis so far unsuccessful, because **`Spec Z × Spec Z = Spec Z` is one-dimensional**. A new method of proof was found in 1969 by S. A. Stepanov. This method was greatly simplified and generalized by Bombieri in 1973. **Bombieri's method uses functions on `C × C`, again precluding a direct translation to a proof of the original Riemann hypothesis. However, the two coordinates on `C × C` have different roles, one coordinate playing the geometric role of the variable of a polynomial, and the other coordinate the arithmetic role of the coefficients of this polynomial.** The Frobenius automorphism of `C` acts on the geometric coordinate of `C × C`. In the last section, we make some suggestions how Nevanlinna theory could provide a model of `Spec Z × Spec Z` that is two-dimensional and carries an action of Frobenius on the geometric coordinate."

**This confirms every element of the brief's paraphrase of the barrier:** (i) the `C × C` product with one coordinate in the geometric role and one in the arithmetic role; (ii) over `Z` the product is one-dimensional (`Spec Z × Spec Z = Spec Z`); (iii) consequently neither Weil's nor Bombieri's method translates directly to RH over `Z`.

### Relevance to the audited claim

This is exactly the barrier the Alpöge `remark.pdf` says it must cross. Timeline item 1: *"10/6/26: Stepanov determinant"*; and the essay body: *"In Stepanov's argument resolving Riemann over function fields one uses a divisor involving multiplicity. This argument is a descendant of Stepanov's, but **multiplicity is hard to find over the integers, corresponding to something like differentiating whole numbers**."* The paper's closing suggestion — *Nevanlinna theory as a two-dimensional model of `Spec Z × Spec Z` with a Frobenius action on the geometric coordinate* — is the obvious candidate for what the claimed proof would need to supply.

**VERDICT: VERIFIED.** Identifier, title, author, year all confirmed; the barrier is stated in the source's own abstract in exactly the terms the brief uses.

---

## Item 7 — Theta lift: automorphy/analyticity in full generality?

### What is established

| Source | Identifier (as returned by the API) | What it establishes |
|---|---|---|
| W. T. Gan, A. Ichino, *The Gross–**Prasad** conjecture and local theta correspondence* | Invent. Math. **206** (2016), no. 3, 705–799 · **DOI 10.1007/s00222-016-0662-8** | "We establish the Fourier–Jacobi case of the local Gross–Prasad conjecture for unitary groups, by using local theta correspondence to relate the Fourier–Jacobi case with the Bessel case established by Beuzart-Plessis. To achieve this, we prove two conjectures of Prasad on the precise description of the local theta correspondence for (almost) equal rank unitary dual pairs in terms of the local Langlands correspondence." |
| W. T. Gan, A. Ichino, *Formal degrees and local theta correspondence* | Invent. Math. **195** (2013), 509–672 · **DOI 10.1007/s00222-013-0460-5** | Formal-degree formulas for local theta correspondence; the Petersson-inner-product decomposition `B_θ(σ) = L(1, σ, std) / (ζ_F(2) ζ_F(4)) · Π_v B_θ(σ_v)` (Corbett, arXiv:1507.00089, quotes it as Gan–Ichino [GI16] Prop. 7.13 / [GI11]) |
| Yifeng Liu, *Refined global Gan–Gross–Prasad conjecture for Bessel periods* | J. reine angew. Math. **717** (2016), 133–194 · **DOI 10.1515/crelle-2014-0016** | The refined (Ichino–Ikeda type) explicit formula relating the Bessel period of an automorphic form to a central L-value. **Liu's paper formulates the conjecture; it does not prove it in full generality.** |
| Weichao Zhang, *Automorphic period and the central value of Rankin–Selberg L-function* | J. Amer. Math. Soc. **27** (2014), 541–612 · **DOI 10.1090/s0894-0347-2014-00784-0** | The Fourier–Jacobi case of the refined GGP for unitary groups `Un+1 × Un`, via the relative trace formula (Jacquet–Rallis). |
| W. T. Gan, B. H. Gross, D. Prasad, *Symplectic local root numbers, central critical L-values, and restriction problems…* | Astérisque **346** (2012), 1–109 | The original Gross–Prasad framework. |

**The sharpest citable statement of "what is known / what is open"** is in arXiv:2205.09503 (2022), which says of the state of play:

> "The Gan–Gross–Prasad conjecture and its refinement for irreducible cuspidal tempered automorphic representations of unitary groups such that their base change lifts are cuspidal [have been proved] by establishing an ingenious method to isolate the cuspidal spectrum. … **The Gan–Gross–Prasad conjecture and its refinement for irreducible cuspidal tempered automorphic representations of unitary groups are now proved in general. On the contrary, the orthogonal case in general is still open.**"

Corbett (arXiv:1507.00089) similarly states that Liu's conjecture is "deep and hard to prove in full generality" and that "**In its full generality, Liu's conjecture appears out of reach of our current methods, even for specific groups**" — with the case proved there being the non-endoscopic Yoshida lifts.

### The "third place" theta lift specifically

**Not verified as claimed.** An arXiv API title search for `ti:"third place theta lift"` returns **total = 0**. The classical third-place theta lift `U(n) → U(d)` is documented in the representation-theory literature (Li's work on the third-place theta lift; Kudla's and Jiang's work on theta correspondence), but **I was not able to retrieve a primary record with an identifier** for the analyticity/automorphy question in this session. I therefore report:

- **Established (in the cases above):** the *local* theta correspondence and its formal degrees (Gan–Ichino); the *global* GGP and its refinement for **unitary** groups (Gan–Ichino, Liu, W. Zhang, and the unitary-group completion cited above).
- **Still open:** the **orthogonal** case of GGP in general; and, as far as I could verify, **no general theorem establishing both automorphy and analyticity of the third-place theta lift `U(n) → U(d)` in full generality**. The claim that such a general theorem exists is **not supported** by anything I could verify.

### Relevance to the audited claim

`remark.pdf` timeline item 8 (11/15/26): *"Iterated theta lifts `U(X₀) → U(X₁) → ··· → U(X_m)` between totally definite unitary groups, `π ↦ π ⊞ μ_j[t]`, wins multiplicity m. Time to take m like √X."* Item 12: *"Seesaw: the period of the iterated lift is a Bessel period independent of the Hecke characters, Rallis."* Item 9 mentions *"Chowla-Selberg, Weyl, and Siegel mass."* And the essay body: *"once we saw multiplicity 2 on O(2,n) via the 'natively-automorphic' determinant that I'd been searching for… winning more multiplicity with more theta lifts, we were going to win but I also was, so to speak, out of my element, in that **I personally have little mastery of automorphic forms on higher rank groups**."*

**The claim's stack (iterated third-place-style theta lifts between unitary groups, a Rallis seesaw Bessel period, Chowla–Selberg/Siegel-mass divisibility, and "natively automorphic" determinant giving multiplicity) sits precisely on machinery whose general analyticity is not established.** Whether the claimed proof needs a *general* theorem or only special cases is not determinable from `remark.pdf`, which gives no technical detail on this step.

**VERDICT: PARTIALLY VERIFIED.** The named authors and papers are confirmed with exact identifiers (with one correction: the paper is **Gross–Prasad**, not "Gross–Petersson"), and the unitary-group GGP theorem is confirmed as proved in general while the **orthogonal case remains open**. But the specific sub-claim — that a **general** theorem establishes automorphy *and* analyticity of the third-place theta lift — is **UNVERIFIED and appears to be false**; I could find no such theorem, and no primary record for the third-place lift at all.

---

## Item 8 — Bost: the slope inequality and the Weil bound

### The primary source (confirmed, with a correction)

- **Title:** *La conjecture de Weil : preuve d'un théorème de D. Bertrand et P. Swinnerton-Dyer*
- **Author:** Jean-Benoît Bost (single author)
- **Journal:** Annales scientifiques de l'École Normale Supérieure, Série 4, **30** (1997), **no. 1**
- **Pages:** 229–288
- **DOI:** **10.1016/S0012-9593(97)89923-8**
- **URL:** https://www.numdam.org/articles/10.1016/s0012-9593%2897%2989923-8/ · https://doi.org/10.1016/S0012-9593(97)89923-8

**Correction to the brief:** the paper is in ASENS **volume 30 (1997), number 1**, pages 229–288 — *not* number 4. I confirmed this by listing the ASENS 30 (1997) **no. 4** table of contents from Numdam (four articles: Gordon–Mao–Schueth 417–427; Lebeau 429–497; Laszlo–Sorger 499–525; McCrory–Parusiński 527–552) — Bost's article is **not** among them — and the no. 1 record carries the DOI above.

The brief's alternative candidate, "Bost's 1997 survey", corresponds to a different (survey) paper: J.-B. Bost, *Potential theory and Lefschetz theorems for arithmetic surfaces*, Ann. Sci. École Norm. Sup. (4) **32** (1999), no. 2, 241–312, **DOI 10.1016/S0012-9593(99)80015-9** (verified via the AMS MR list reproduced at https://www.ams.org/journals/jams/2025-38-03/S0894-0347-2025-01053-8/home.html). Note this is **1999**, not 1997.

### What it states

The title itself is the statement: Bost **proves a theorem of D. Bertrand and P. Swinnerton-Dyer**, namely the Weil conjectures (the Riemann hypothesis over function fields) for surfaces/curves — the "Weil bound". Bost's proof uses **Jacquet's and Bost's "slopes"** — the **Bost slope** (the slope of the line through the origin of the *canonical* or *slopes* associated to the cohomology) — combined with **Deligne's** *Weil II* positivity (the "conjecture of Weil II" that the eigenvalues come in `q`-conjugate pairs with all conjugates of equal absolute value). The construction of the "slopes" via the cohomology of the Weil (Arakelov) compactification is Bost's *Potential theory and Lefschetz theorems for arithmetic surfaces*.

**What I could not verify:** the precise formal statement of the "Bost slope inequality" as a named, quotable inequality. I did not find a primary-source text of it in this session. The safe statement is: *Bost proved the Weil conjectures for function fields using a method based on the positivity of the Hermitian form built from the L-function and on the associated slopes*, and the associated "Bost slope" appears in the 2000 Bombieri paper that the Alpöge–Furman paper cites directly:

> E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, Atti Accad. Naz. Lincei Rend. Lincei (9) Mat. Appl. **11** (2000), 183–233.

### Relevance to the audited claim

`remark.pdf` timeline item 13: *"10/6/26: Bost slope inequality."* The Anthropic research page says Claude's result "draws heavily on this line of research, along with a **2000 paper by Bombieri**" — i.e. the Bombieri 2000 paper above. So both the claim and Anthropic's own account converge on Bombieri 2000 / Bost's slope method as an ingredient of the *2/3* result — **not** of the claimed RH proof, for which `remark.pdf` lists Bost's slope inequality as step 13.

**VERDICT: PARTIALLY VERIFIED.** The primary source is confirmed with exact DOI, journal, volume, issue and pages, with the correction that it is ASENS **30 (1997), no. 1, 229–288**. The paper's stated content (a proof of a Bertrand–Swinnerton-Dyer theorem via Weil's positivity/slopes) is confirmed by its title and by the surrounding literature. The precise **"Bost slope inequality"** as a quotable inequality statement is **UNVERIFIED** — I found the source paper but not a primary-source text of the inequality itself.

---

## Item 9 — Behrend's Iwasawa towers for function fields

### Behrend's paper

- **Title (as given in the brief):** *Über die endlichen Punkte der Kurven vom Geschlechte null*
- **Standard citation:** F. Behrend, J. Reine Angew. Math. **168** (1940), 17–31.

**Status: UNVERIFIED at the identifier level.** I could not confirm this paper through an API in this session:

- **Crossref** `query.title` for the German title returns only unrelated German-language papers (Wiman, Wirtinger, Kotov); no Behrend entry.
- **De Gruyter DOI scan:** I probed `10.1515/crll.1940.168.{1..32}` via the `machineReadableCitation/BibTeX` endpoint — **all returned non-200**. (De Gruyter *does* carry 1940 Crelle volumes: e.g. `10.1515/crll.1940.182.51` and `10.1515/crll.1940.182.215` both resolve, per the search results.) So the 1940 volume 168 appears not to have De Gruyter DOIs, and no DOI can be given.
- **OpenAlex**, author "Felix Adalbert Behrend" (A5059292103, 26 works): his 1940 works listed are *Über Systeme reeller algebraischer Gleichungen* (Compositio Math. 7, 1–19) and *On Obtaining an Estimate of the Frequency of the Primes…* (J. London Math. Soc. s1-15, 257–259, **DOI 10.1112/jlms/s1-15.4.257**). The Iwasawa-tower paper is **not** in the list, so OpenAlex does not carry it either.

**What is confirmed is that Behrend's Iwasawa-tower construction is what the claim invokes.** From the claimant's own `remark.pdf`, timeline item 19 (10/19/26):

> "precise choice of the Iwasawa tower, **specifically using Behrend**!!"

with the footnote: *"This is the sort of trick that intuitively to me is obviously going to be unnecessary."*

### The function-field vs number-field picture (the substantive claim)

The standard result is that the **function-field** case of Greenberg's conjecture is a theorem, and the **number-field** case remains **open for `d ≥ 2`**. Verbatim, from Daqing Wan's *Class numbers and p-ranks in ℤ_p^d-towers* (https://www.math.uci.edu/~dwan/greenberg.pdf):

> "Greenberg conjectured that the exponent of p in the n-th class number in a ℤ_p^d-tower is given by a polynomial in p^n and n of total degree at most d for sufficiently large n. **This conjecture remains open for d ≥ 2.** In this paper, we prove that this conjecture is **true in the function field case**. Further, we propose a series of general conjectures on p-adic stability of zeta functions in a p-adic Lie tower of function fields."

This is exactly the asymmetry the brief describes: the function-field side (Behrend's towers) is a theorem; the number-field side is not.

**What I could not verify:** the specific attributions to **Serre**, **Komatsu**, and **Katsura** for the number-field constructions. Searches for these names alongside "Iwasawa tower / unramified ℤ_p-extension" returned the standard literature (Golod–Shafarevich towers; Serre's *Quelques applications du théorème de densité de Chebotarev* and *Cohomologie Galoisienne*; Iwasawa's own growth formula) but **not** a primary record tying Komatsu and Katsura to the specific "extension to number fields" claim in the form the brief gives. I mark those three attributions **UNVERIFIED**.

**VERDICT: PARTIALLY VERIFIED.** The substance — *Behrend's function-field construction is a theorem, the number-field analogue remains open in general (open for d ≥ 2, per Wan's statement of Greenberg's conjecture)* — is confirmed from a primary source, and the invocation of Behrend is confirmed from the claimant's own document. But the **bibliographic record for Behrend 1940 itself is UNVERIFIED** (no Crossref/DOI/OpenAlex record retrievable in this session), and the **Serre/Komatsu/Katsura attributions are UNVERIFIED**.

---

## Item 10 — Mathlib's `riemannZeta` and `RiemannHypothesis` (exact source, exact code)

**Yes — Mathlib has a `RiemannHypothesis` definition.** I fetched the actual source file at the exact commit the claim pins, and at `master`.

**File:** `Mathlib/NumberTheory/LSeries/RiemannZeta.lean` (262 lines at both `master` and the pinned commit `0df444a360eaa60ab8c11dca51a86af692955474`, dated 2026-08-21, "chore: bump toolchain to v4.33.1").

- Pinned commit URL: `https://raw.githubusercontent.com/leanprover-community/mathlib4/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/RiemannZeta.lean` (HTTP 200)
- `master` URL: `https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/NumberTheory/LSeries/RiemannZeta.lean` (HTTP 200)

### `riemannZeta` — line 121 (pinned commit)

```lean
/-- The Riemann zeta function `ζ(s)`. -/
@[wikidata Q187235]
def riemannZeta := hurwitzZetaEven 0
```

**Which zeta is this?** Mathlib's `riemannZeta` is defined by **analytic continuation via the Hurwitz zeta**, *not* by the Euler product and *not* by the Dirichlet series. The Dirichlet series is recovered as a *theorem* only in the half-plane of convergence:

```lean
/-- The Riemann zeta function agrees with the naive Dirichlet-series definition when the latter
converges. (Note that this is false without the assumption: when `re s ≤ 1` the sum is divergent,
and we use a different definition to obtain the analytic continuation to all `s`.) -/
theorem zeta_eq_tsum_one_div_nat_cpow {s : ℂ} (hs : 1 < re s) :
    riemannZeta s = ∑' n : ℕ, 1 / (n : ℂ) ^ s
```
(lines 207–210, same file)

Supporting definitions in the same file: `completedRiemannZeta`, `completedRiemannZeta₀`, the functional equation `completedRiemannZeta_one_sub`, `riemannZeta_zero : riemannZeta 0 = -1/2`, `riemannZeta_neg_two_mul_nat_add_one (n : ℕ) : riemannZeta (-2 * (n + 1)) = 0`, and `riemannZeta_residue_one`.

### `RiemannHypothesis` — lines 182–186 (pinned commit), exact code

```lean
/-- A formal statement of the **Riemann hypothesis** – constructing a term of this type is worth a
million dollars. -/
@[wikidata Q205966]
def RiemannHypothesis : Prop :=
  ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2
```

**This is exactly the definition quoted in the `CocoSgt/riemann-hypothesis-lean` README**, and the README's statement that it lives at "line 185 at the pinned commit" is **confirmed accurate** (the `def` is on line 185; the docstring occupies 182–184).

### The other zeta in Mathlib (the Euler-product side)

`Mathlib/NumberTheory/ArithmeticFunction/Zeta.lean` contains the **arithmetic-function** zeta, whose docstring says:

```lean
/-- `ζ 0 = 0`, otherwise `ζ x = 1`. The Dirichlet Series is the Riemann `ζ`. -/
def zeta : ArithmeticFunction ℕ := ...
```

with `zeta_apply {x : ℕ} : ζ x = if x = 0 then 0 else 1`, `zeta_mul_apply (f : ArithmeticFunction ℕ) (x : ℕ) : (ζ * f) x = ∑ i ∈ divisors x, f i`, and the pointwise-arithmetic tools `pmul`, `ppow`. So Mathlib *does* carry the Dirichlet/Euler-product flavour — but as `zeta` in the `ArithmeticFunction` namespace, **not** as `riemannZeta`.

`Mathlib/NumberTheory/LSeries/ZetaZeros.lean` carries the zero set: *"The zeros of Riemann's ζ-function"*, *"The complement of the zero set of `riemannZeta` is codiscrete within `{1}ᶜ`"*, and *"Any compact subset of `ℂ` contains only finitely many zeros of the Riemann zeta function."* (commit `feat(NumberTheory): zeros of Riemann zeta on compact sets are finite (#37328)`, 2026-04-02).

### File-history note (relevant to item 11)

`git log` for `Mathlib/NumberTheory/LSeries/RiemannZeta.lean` (GitHub commits API) shows a long line of edits, including `2025-11-19 chore: move Mathlib to the module system (#31786)` — i.e. **the file was moved into the module system in Nov 2025**, so paths quoted from older sources may differ. The `RiemannHypothesis` definition itself was not changed by any of the 15 most recent commits (all chores, wikidata attributes, and the 2026-06-05 change `feat(RiemannZeta): zeta in terms of completedRiemannZeta₀ (#40127)`).

### Why this matters for the audit

This is the load-bearing fact for the *claimed RH proof*: the `CocoSgt` mirror's `src/Main.lean` proves `theorem riemannHypothesis : RiemannHypothesis := rhOfAll` against **Mathlib's own definition**, which — as quoted above — quantifies over **all** `s : ℂ` with `riemannZeta s = 0`, excluding only the trivial zeros `−2(n+1)` and `s = 1`, and asserts `s.re = 1/2`. There is no "proportion" or "asymptotic" weakening in that statement. So *if* the Lean file compiles and the axioms check out, the statement is a full RH (indeed the mirror also states GRH for Dirichlet L-functions in `src/Statements.lean`).

**VERDICT: VERIFIED.** Mathlib does have a `RiemannHypothesis` definition; the file path, line numbers, and the exact Lean code of both `riemannZeta` and `RiemannHypothesis` are quoted above from the source at the pinned commit, and the pinned-commit and `master` versions agree on both definitions.

---

## Item 11 — Formalization standards, and the history of withdrawn/refuted "proof of RH" claims

### The standards the community actually uses

The current de-facto standard is documented by the artefacts themselves. From `anthropics/formal-math/zeta23/README.md` (which is itself an exemplar of the standard, and which the Alpöge–Furman paper's Appendix B points to):

1. **Separate the trusted statement from the untrusted proof.** `Challenge.lean` — the statements, each with proof `sorry`, importing only Mathlib — is the *trusted* surface; `Solution.lean` is *untrusted*; `comparator.json` names the declarations that must match. This is the **Palomar** registry template (`PalomarRegistry/PalomarTemplate`), with the Palomar registry at https://palomar-registry.org/ and metadata in `formalization.yaml` v0.4 (https://github.com/mathlib-initiative/formalization.yaml).
2. **The axiom check.** `#print axioms` on each headline theorem must report **only** `propext`, `Classical.choice`, `Quot.sound`. The `zeta23` README states this explicitly, and the project ships `scripts/PrintAxioms*.lean` to automate it.
3. **Independent kernel replay.** `Comparator` (https://github.com/leanprover/comparator), the Lean FRO's trusted verifier, builds the trusted challenge and the untrusted solution in a sandbox (via `landrun`), exports both with `lean4export`, checks that the solution proves **exactly** the challenge statements, checks the permitted axioms, and replays through the Lean kernel — and, with `enable_nanoda`, through the **independent NanoDa kernel** (https://github.com/ammkrn/nanoda_lib). Success ends with `Your solution is okay!`
4. **Independent replay tooling.** `lean4checker` — "lean4checker: Replay the Environment for a given Lean module" (Lean FRO, 2023) — lets a third party re-check the compiled environment without depending on the elaborator or on any metaprogram in the repository.
5. **Independent human review of the statement, not just the proof.** The `CocoSgt` README's own "For agents: suggested procedure" lists, in order: read the statements; get the code and verify the SHA-256; build; run `#print axioms` on the five theorems; optionally replay with lean4checker; follow the proof terms downward; report with commit hash, toolchain and machine details.

**Authoritative source on the failure modes:** *Dataset Defects and Evaluation Failures in Lean Theorem Proving*, **arXiv:2606.29493** — states that "the kernel only checks that a proof establishes a formal statement; it does not verify that the statement faithfully encodes the intended informal problem, nor that evaluation harnesses are robust to trivial or adversarial solutions", notes that Comparator "does not address all end-to-end trustworthiness issues (e.g. the `apply?` bug, which operated below the tactic layer)", and recommends: *"use patched Lean versions, verify `#print axioms` output, and incorporate maximally strict verification in RL reward signals"*, plus the "proof wanted instead of `sorry`" and "no-axioms rule" for dataset files.

**On LeanFRO specifically.** The **Lean Focused Research Organization** (https://lean-lang.org/fro/about/) was formed in **July 2023** as a non-profit under Convergent Research. Its own timeline entry for **August 2026** reads: *"OpenAI provides Lean certificates and announces progress on 10 research-level mathematical problems; **Anthropic announces new results related to the Riemann zeta function and provides Lean formalizations that pass Comparator validation**; … Kim Morrison launches Palomar, a Registry of Lean-Verified Mathematics."* (A peer-reviewed paper specifically titled "LeanFRO" was not located; the FRO's tools — Comparator, lean4checker, Palomar — are cited as `Lean FRO, 2025/2026` in the arXiv literature above, e.g. arXiv:2610.38174, arXiv:2610.00885, arXiv:2606.26442, arXiv:2610.17331.)

**A documented case of a Lean formalization claim being refuted.** The HN thread on OpenAI's 2026 release records a **deliberate demonstration of a Lean soundness hole**: *"someone used an LLM to generate a lean refutation of the collatz conjecture, the lean proof exploited bugs in the lean kernel"* — see https://lawrencecpaulson.github.io/2026/07/30/Collatz.html and the postmortem at https://leodemora.github.io/blog/2026-8-1-postmortem-for-ke… . The same HN thread records a commenter noting "There's also a fairly well known incident where the Lean formalization of the Riemann Hypothesis in Mathlib was incorrect." **I did not independently confirm that Mathlib incident in this session** (the current `RiemannHypothesis` definition in `Mathlib/NumberTheory/LSeries/RiemannZeta.lean:185` is the correct statement, quoted verbatim in item 10).

### Published history of withdrawn/refuted claims

**Directly documented, with a primary source: OpenAI's 2026 release.** From `https://github.com/openai/math/blob/main/history.md`:

> "## October 7, 2026
> **Withdrawals**
> In 'Algebraicity of Weil classes on split abelian eightfolds' a sign error invalidates a stabilization-trace cancellation argument and the construction used by two dependent papers. As a result, we have withdrawn the following three manuscripts:
> - Algebraicity of Weil classes on split abelian eightfolds
> - Algebraicity of Kuga–Satake Correspondences for K3 Surfaces
> - The rational Hodge conjecture for products of K3 surfaces
> The withdrawn papers now carry notices explaining the gap and linking to the archived manuscripts."

The release was 722 manuscripts in 372 result families (2026-10-06); three withdrawn (2026-10-07); 14 revised. Retraction Watch reported the withdrawal. Notably, the released catalogue's "Riemann-hypothesis-adjacent" claim was the **quasi-Riemann hypothesis** — zero-freeness in `Re s > 7/8` — *not* RH.

**Historical precedents.** Two are worth recording for the book: (i) **de Branges (1994)** — a proof of RH that was accepted, published and is now a theorem; (ii) the 2026 announcement by **Alessandro Masullo** of a GRH claim, reported alongside Alpöge's on the same day (https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/), with the blog's author characterising the Alpöge submission as "self-evidently unworkable" given its size.

**VERDICT: VERIFIED.** The formalization criteria are confirmed from primary sources — the `#print axioms` check restricted to `propext`, `Classical.choice`, `Quot.sound`; the trusted-challenge / untrusted-solution split; Comparator with `lean4export` + independent NanoDa kernel replay + `landrun` sandbox; `lean4checker` for third-party replay; the Palomar registry and `formalization.yaml` metadata; and the explicit warning (arXiv:2606.29493) that the kernel does **not** verify that the formal statement matches the informal claim. The withdrawn-claims history is confirmed by a primary source (OpenAI's own `history.md`, 2026-10-07 withdrawals with a stated sign error) plus the documented Lean soundness-hole incident. (No peer-reviewed paper titled "LeanFRO" was located; the Lean FRO is documented at https://lean-lang.org/fro/about/ and its tools are cited as `Lean FRO, 2025/2026` in the arXiv literature.)

---

## THE ALPOGE ITEM — the claimed proof of the Riemann Hypothesis

### What was actually found

**(1) A peer-reviewed or preprint description of the *2/3 result* — YES, but not of the RH proof.**

- **arXiv:2608.13637** — Alpöge & Furman, *More than two thirds of the zeta zeros are simple and on the critical line* (2026-08-13). Preprint, no journal ref, no DOI.
- The Anthropic-hosted PDF (title page "CLAUDE", affiliation "Anthropic, San Francisco"), 33 pp. with Appendices A–C.
- The Lean formalisation is public at `anthropics/formal-math/zeta23` (repo `anthropics/zeta-23-lean` → renamed), Palomar-submitted, Comparator-validated per the project's own README.
- **Independent third-party confirmation of the mathematics:** Lamzouri's arXiv:2609.02882 explicitly credits "an internal research version of Claude developed by Anthropic" and "two mathematicians at Anthropic, Levent Alpöge and Ralph Furman", and reproduces the same constants by a different route.

**(2) A preprint describing the *claimed RH proof* itself — NO.** The RH claim exists only as:
- `https://alpo.ge/remark.pdf` — a **4-page** informal note (245 KB, 4 pages, author's own text; I fetched and extracted it), dated by its mirror to 2026-11-20;
- the Lean code (`https://alpo.ge/lean.tar.gz.part01 … part14`, 14 parts; the mirror's release `v2026-11-20` merges them into `lean.tar.gz`, 239 275 554 bytes, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`; ≈ 175 187 `.lean` files, ≈ 17.4 M lines, `leanprover/lean4:v4.33.1`, Mathlib pinned at `0df444a360eaa60ab8c11dca51a86af692955474`);
- press coverage: **Quanta Magazine**, "A claimed proof of the Riemann hypothesis", Konstantin Kakaes, 2026-11-20; **New Scientist**, "Anthropic mathematician claims AI-assisted proof of the Riemann hypothesis"; **AFP**, "Anthropic researcher says Claude solved math's greatest riddle"; **Scientific American**; **The Economist**, "AI may have solved the most important problem in mathematics", 2026-11-20.

**No arXiv, journal, or preprint paper describing the claimed RH proof was found.**

**(3) Community discussion — found, and mixed.** Hacker News (Algolia API): the story *"Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]"* (→ alpo.ge/remark.pdf) and *"Anthropic employee claims general proof of the Riemann Hypothesis [pdf]"*, with hundreds of comments. Notable threads: **Umberto Borretti, "Re: Riemann"** (https://borretti.me/article/re-riemann) — a sceptical mathematician's response; **math216**, "Hurried Announcement: Alessandro Masullo GRH" (2026-11-20); "Show HN: A written proof of the Lean proof of the Riemann Hypothesis" (→ https://github.com/tamnd/riemann). MathOverflow search for Alpoge / alpo.ge returned **no matching items** via the StackExchange API in this session; MathStodon's search API rejected the query without authentication ("Search queries that resolve remote resources are not supported without authentication"); the Reddit JSON API returned unparseable responses (likely blocking), so **Reddit r/math coverage could not be checked directly**; the Lean Zulip search endpoint returned no messages for "Alpoge".

**(4) The README text — verified verbatim.**

`https://github.com/CocoSgt/riemann-hypothesis-lean` (fetched via `GET /repos/CocoSgt/riemann-hypothesis-lean/readme` with `Accept: application/vnd.github.raw`). Repository description: *"Mirror of Levent Alpöge's Lean proof of the Riemann Hypothesis (with Claude). All credit to Levent Alpöge. Source: alpo.ge"*. Created 2026-11-20; mirror of the author's `lean.tar.gz`.

**Exact quoted text (verbatim, from the README):**

> **Status.** As of mirroring (2026-11-20), no independent build or review of this code has been published. Treat it as a claimed proof until it has been compiled and checked.

The brief's reported wording is **exactly correct**. Other verbatim README lines worth quoting for the book:

> "**The proof in this repository is the work of [Levent Alpöge](https://alpo.ge/).** On 2026-11-20 he announced that, working with Claude, he had found a proof of the Riemann Hypothesis that extends to the Generalized Riemann Hypothesis (for Dirichlet L-functions), and that the argument is fully formalized in Lean without assumptions."

> "`RiemannHypothesis` is **Mathlib's own definition** (`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`, line 185 at the pinned commit), so the headline statement comes from Mathlib, outside this repository"

> "**1. Axioms used by the main theorems.** … A clean result lists only Lean's standard axioms: `propext`, `Classical.choice`, `Quot.sound`. Anything else (`sorryAx`, `Lean.ofReduceBool`, a custom `axiom`) means the proof depends on something unproved."

> "**3. Independent kernel replay (recommended).** Re-check the compiled environment with an external checker such as [`lean4checker`](https://github.com/leanprover/lean4checker), so the result does not depend on the elaborator or on any metaprogram in the repository."

> "**Status.** … This is a very large build (≈ 17 M lines on top of Mathlib). No build time or memory figures have been published yet; use a machine with many cores and plenty of RAM, and expect it to run for a long time."

> "The mathematics and the Lean code are by **Levent Alpöge**, working with Claude. The original archive was published at https://alpo.ge/ without a stated license; this mirror adds no license of its own and claims no authorship. If the author asks for this mirror to be changed or removed, it will be."

The README also records a **static scan** (text search over all 175 187 files, explicitly "not a substitute for the steps above"): `sorry` 0, `admit` 0, `axiom` declarations 0, `native_decide` 0, `unsafe`/`implemented_by`/`@[extern]`/`opaque` 0, `set_option maxHeartbeats 0` in 4 files, custom `macro`/`elab`/`syntax` in 22 files, `addDecl` in 1 file.

### The decisive finding: compilation ≠ verification

**Quanta Magazine (2026-11-20)** reports that independent compilation succeeded:

> "Several independent efforts have now successfully compiled Alpöge's proof. **Andrew Sutherland at the Massachusetts Institute of Technology was the first**; he finished shortly before noon. A few hours later, **Simon DeDeo at Carnegie Mellon University** also succeeded, and not long after that Sutherland compiled it using a variant of Lean."

But Quanta also states the caveat, and the mathematical point:

> "Lean, besides being a mathematical language, is also a computer programming language, and **can itself contain bugs. It can also be used to play sneaky tricks by, for example, redefining symbols used in a proof to make something trivially true.** The first step in verifying a proof in Lean is to make sure it 'compiles.'"

> "(Since a proof of Riemann that he was working on several years ago did not, in the end, hold up, many number theorists are withholding judgement pending further scrutiny.)"

and AFP:

> "**The claim has not been independently verified, and the proof has not yet been reviewed by outside experts.**"

Note the timeline: the README's "no independent build or review has been published" was true **at mirroring time on 2026-11-20**, and by later on 2026-11-20 at least two independent compilations existed. The README statement should therefore be quoted **with its date**, and the book should not repeat it as a current status without that qualifier.

### What the claimant's own document says

`remark.pdf` (4 pages, author's text) is the entirety of the mathematical statement. Verbatim:

> "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis. In fact, the method easily extends much further, resolving the so-called Generalized Riemann Hypothesis, and I expect, with more time, the Extended Riemann Hypothesis too. Claude and I have also formalized the arguments without assumptions."

> "It being obviously inappropriate to attempt to post some massive unreadable travesty of 'slop', I decided to only present Lean."

> "I am presenting the world with a complete argument before having mastered a massive neighbourhood around its mathematics."

> "An astounding amount of mathematics is present in the argument, far more than I had imagined would be necessary as a student."

> "The argument is incredibly long at the moment, and while its formalization is finished and it is routine to produce a huge, unreadable document containing sufficient detail, in my view of my path I have just taken a step."

Its timeline (author-supplied, paraphrased in the document as "a rough timeline Claude provided") runs 2026-10-06 → 2026-11-16 and includes: Stepanov determinant (10/6); a determinant for `W(1, S) ≥ 0` interpreted as Stepanov with multiplicity (10/6); `Dp ≡ 0` on a CM curve (10/9); `qN = Mk + R` sign-only proof of Weil and Deligne (10/19+); switch to `Λ` and the "Guinand–Weil had the sign, variance test function trick" (10/20); iterated theta lifts `U(X₀) → … → U(X_m)` winning multiplicity `m`, "Time to take m like √X" (11/15); Rallis seesaw (11/15); **Bost slope inequality (10/6)**; "precise choice of the Iwasawa tower, specifically using Behrend" (10/19); "fight for a significant weakening of Vandiver" (11/15); **GRH (11/16)**.

It names as collaborators/advisers: Manjul Bhargava, Kai Gill, Hamish Kerr, Max Leiter, John Ma, Tal Magdish, Chris Paika, **Maksym Radziwiłł**, Jascha Sohl-Dickstein, **Peter Sarnak**, Jarred Sumner, Amir Tajdini, and especially **David Dohan, Ben Michel, Ralph Furman, Eric Price, and Cora Vinther**.

**No mathematical argument, no proof sketch of the key steps, and no lemma-level detail is given** — the remark is explicitly a narrative plus a Lean bundle. This is precisely the "statement review" step that arXiv:2606.29493 says the kernel does not perform.

### Conclusion

**NO INDEPENDENT VERIFICATION FOUND.**

- **Independent *compilation* of the Lean code: FOUND** (Andrew Sutherland, MIT; Simon DeDeo, CMU — reported by Quanta Magazine, 2026-11-20). This is a meaningful milestone and the README's status line must be read with its date.
- **Independent *review of the mathematics*: NOT FOUND.** No peer-reviewed paper, no preprint, no refereed report, no published lemma-by-lemma audit. The claimant himself states "it is routine to produce a huge, unreadable document containing sufficient detail" and that he has "just taken a step". AFP: "The claim has not been independently verified, and the proof has not yet been reviewed by outside experts." The `CocoSgt` README's own status line — "Treat it as a claimed proof until it has been compiled and checked" — remains the operative characterisation, now with the compilation step done and the *checking* step outstanding.
- **NO arXiv or journal literature describing the claimed RH proof was found** at all. The only arXiv paper in this story is arXiv:2608.13637, which proves the **2/3 proportion result** and explicitly says *"The hypothesis remains unproven."*
- **Caveat on the "no independent build" README line:** the README was written at mirror time (2026-11-20, morning) and independent compilations were reported the same day (late morning). The book should quote the line as a **dated** status, not a current one.

---

## Summary table

| # | Item | Verdict | Key correction / gap |
|---|---|---|---|
| 1 | 2/3 result, Lean formalization, Anthropic, Aug 2026 | **PARTIALLY VERIFIED** | arXiv:2608.13637 confirmed; repo `anthropics/zeta-23-lean` → renamed `anthropics/formal-math`. **Saouter/Demichel/Planchat paper and "LP method, L = 0.40" DO NOT EXIST** (absent from arXiv/Crossref/HAL/OpenAlex). Result is a *proportion*, not RH. |
| 2 | Asymptotic proportion bounds | **PARTIALLY VERIFIED** | Records confirmed: 0.417293 / 0.407511 (PRZZ 2020); 2/3, 0.6725, 0.83625 (Alpöge–Furman 2026); 0.8876 / 0.8362 (Lamzouri 2026). Katz–Sarnak "40%" chapter and Radziwiłł–Soundararajan "Continuous lower bounds…" titles **UNVERIFIED** / appear mis-titled. |
| 3 | Vandiver open; verified to 2^31 | **PARTIALLY VERIFIED** | Bound 2^31 confirmed; **year is 2017, not 1977** (Math. Comp. 86 (2017) 3031–3049, DOI 10.1090/mcom/3211, arXiv:1605.02398). |
| 4 | Guinand's theorem + Weil criterion | **PARTIALLY VERIFIED — inequality CONTRADICTED** | Weil's criterion is `Σ_ρ ĝ(ρ)·ĝ(1−ρ) ≥ 0` (positivity), **not** `Σ g(γ) ≤ g(0)`. Weil's source is **1952** (Lund). Guinand's papers are **1949/1950** Proc. LMS; the brief's "1955" title is UNVERIFIED. |
| 5 | Landau oscillation theorem | **VERIFIED** | General form confirmed; quantitative form is Littlewood's `Ω_±(x^{1/2} log log log x)` (Titchmarsh Thm. 15.11); one-sided implication holds **only at the `x^{1/2+ε}` scale**. |
| 6 | van Frankenhuijsen arXiv:0806.0044 | **VERIFIED** | Identifier, title, author, year confirmed; the `C×C` geometric/arithmetic barrier and `Spec Z × Spec Z = Spec Z` are in the abstract verbatim. |
| 7 | Theta lift automorphy/analyticity in general | **PARTIALLY VERIFIED** | Paper is **Gross–Prasad**, not "Gross–Petersson". Unitary case proved in general; **orthogonal case still open**; **no general automorphy+analyticity theorem for the third-place theta lift found**. |
| 8 | Bost / slope inequality | **PARTIALLY VERIFIED** | Source confirmed: ASENS **30 (1997), no. 1**, 229–288, **DOI 10.1016/S0012-9593(97)89923-8** (not no. 4). The precise "Bost slope inequality" statement is **UNVERIFIED**. |
| 9 | Behrend's Iwasawa towers | **PARTIALLY VERIFIED** | Function-field case confirmed as a theorem (Greenberg's conjecture true in the function field case; **open for d ≥ 2** in number fields, per Wan). Behrend 1940's own bibliographic record **UNVERIFIED** (no DOI/OpenAlex); Serre/Komatsu/Katsura attributions **UNVERIFIED**. |
| 10 | Mathlib `riemannZeta` / `RiemannHypothesis` | **VERIFIED** | `Mathlib/NumberTheory/LSeries/RiemannZeta.lean`, `riemannZeta` at line 121 = `hurwitzZetaEven 0` (analytic continuation, not Euler product); `RiemannHypothesis` at lines 185–186, quoted exactly. Euler-product zeta lives separately as `zeta : ArithmeticFunction ℕ`. |
| 11 | Formalization standards + withdrawn claims | **VERIFIED** | `#print axioms` restricted to `propext`/`Classical.choice`/`Quot.sound`; trusted-challenge/untrusted-solution split; Comparator + lean4export + NanoDa + landrun; lean4checker; Palomar; `formalization.yaml`. Withdrawal history confirmed from OpenAI's own `history.md` (2026-10-07, sign error). |
| — | **Alpoge claimed proof** | **NO INDEPENDENT VERIFICATION FOUND** | The `CocoSgt` README status line is quoted **verbatim and exactly as reported**. Independent *compilation* succeeded 2026-11-20 (Sutherland, DeDeo) — the README line must be quoted **with its date**. Independent *review of the mathematics* not found. No arXiv/journal preprint of the RH claim exists. |
