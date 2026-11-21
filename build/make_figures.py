#!/usr/bin/env python3
"""
Original figures for "Is the Riemann Hypothesis Solved?"

Every figure is produced here for this book: computed where a computation is
possible (the critical line, psi(x) - x), drawn from the audit's own
measurements where not (the library census, the dependency chain), or drawn
as schematics redrawn from the cited sources.

Output: vector PDF into ../figures/
"""
import cmath
import math
import os
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle, Circle

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0C1016"
PANEL = "#151D27"
EDGE = "#27333F"
ACCENT = "#8FD6C0"
ACCENTDIM = "#4C7D70"
TXT = "#E6EBEF"
TXTDIM = "#8B9BA7"
AMBER = "#E0A458"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": TXT,
    "axes.labelcolor": TXTDIM,
    "xtick.color": TXTDIM,
    "ytick.color": TXTDIM,
    "axes.edgecolor": EDGE,
    "grid.color": EDGE,
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.titleweight": "bold",
    "axes.titlecolor": TXT,
    "figure.dpi": 200,
    "pdf.fonttype": 42,
})


def save(fig, name):
    p = OUT / name
    fig.savefig(p, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    print("wrote", p)


# ---------------------------------------------------------------- zeta ----
_BERNOULLI = [1.0, -1.0/2, 1.0/6, -1.0/30, 1.0/42, -1.0/30, 5.0/66, -691.0/2730,
              7.0/6, -3617.0/510]


def zeta(s, N=28, K=7):
    """Euler-Maclaurin evaluation of the analytic continuation of zeta."""
    s = complex(s)
    total = 0j
    for n in range(1, N):
        total += n ** (-s)
    total += 0.5 * N ** (-s)
    total += (N ** (1 - s)) / (s - 1)
    # rising factorial (s)_{2k-1}
    fact = 1.0 + 0j
    for k in range(1, K + 1):
        if k == 1:
            fact = s
        else:
            fact = fact * (s + 2 * k - 3)
        total += (_BERNOULLI[k] / math.factorial(2 * k)) * fact * N ** (-s - 2 * k + 1)
    return total


def fig_critical_line():
    t = np.linspace(0.2, 46.0, 4600)
    z = np.array([zeta(0.5 + 1j * ti) for ti in t])
    fig, ax = plt.subplots(figsize=(4.6, 2.15))
    ax.plot(t, z.real, color=ACCENT, lw=0.8, label=r"$\Re\,\zeta(\frac{1}{2}+it)$")
    ax.plot(t, z.imag, color=AMBER, lw=0.8, ls=(0, (4, 2)), label=r"$\Im\,\zeta(\frac{1}{2}+it)$")
    ax.axhline(0, color=EDGE, lw=0.8)
    # mark the first few zeros of the critical line
    zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
    for zr in zeros:
        ax.axvline(zr, color=ACCENTDIM, lw=0.6, ls=(0, (1, 3)))
    ax.set_xlabel(r"imaginary part $t$")
    ax.set_xlim(0, 46)
    ax.set_title(r"The critical line: $\zeta(\frac{1}{2}+it)$ for $0<t<46$")
    ax.grid(alpha=0.25, lw=0.5)
    ax.legend(facecolor=PANEL, edgecolor=EDGE, fontsize=7, labelcolor=TXT, loc="upper right")
    ax.text(0.015, 0.06,
            "tick marks: the first five zeros on the critical line",
            transform=ax.transAxes, color=TXTDIM, fontsize=6.5)
    save(fig, "fig_critical_line.pdf")


def fig_psi():
    """psi(x) - x computed by summing Lambda(n) exactly."""
    N = 400000
    psi = np.zeros(N + 1)
    # sieve of smallest prime factors
    spf = np.zeros(N + 1, dtype=np.int32)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i * i, N + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    vals = np.zeros(N + 1)
    for n in range(2, N + 1):
        p = spf[n]
        m = n
        k = 0
        while m % p == 0:
            m //= p
            k += 1
        vals[n] = math.log(p) if m == 1 else 0.0
    psi = np.cumsum(vals)
    xs = np.arange(0, N + 1)
    y = psi - xs
    fig, ax = plt.subplots(figsize=(4.6, 2.1))
    w = 400
    ys = np.convolve(y, np.ones(w) / w, mode="valid")
    ax.plot(xs[w // 2:len(ys) + w // 2], ys, color=ACCENTDIM, lw=0.6, alpha=0.85,
            label=r"$\psi(x)-x$")
    ax.plot(xs[w // 2:len(ys) + w // 2], ys, color=ACCENT, lw=0.8, alpha=0.9,
            label="running mean")
    ax.axhline(0, color=EDGE, lw=0.8)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$\psi(x)-x$")
    ax.set_xlim(0, N)
    ax.set_title(r"Exact computation of $\psi(x)-x$ to $x=400\,000$")
    ax.grid(alpha=0.25, lw=0.5)
    ax.legend(facecolor=PANEL, edgecolor=EDGE, fontsize=7, labelcolor=TXT)
    ax.text(0.015, 0.06,
            r"$\psi(x)=\sum_{n\leq x}\Lambda(n)$ computed exactly by sieving; "
            r"RH is equivalent to $\psi(x)=x+O(x^{1/2}\log^2 x)$",
            transform=ax.transAxes, color=TXTDIM, fontsize=6.2)
    save(fig, "fig_psi.pdf")


# ------------------------------------------------------------- library ----
def fig_library():
    libs = [("Development", 141928, ACCENT),
            ("Formalism", 18254, ACCENT),
            ("GroundTheory", 8507, ACCENT),
            ("ReciprocityTheory", 3845, ACCENT),
            ("CompanionTheory", 2027, ACCENT),
            ("PositivityTheory", 449, ACCENTDIM),
            ("Lemmata", 167, ACCENTDIM),
            ("BuildAid", 5, AMBER),
            ("Supplements", 3, AMBER),
            ("Main", 1, AMBER)]
    names = [n for n, _, _ in libs]
    vals = np.log10([v for _, v, _ in libs])
    cols = [c for _, _, c in libs]
    fig, ax = plt.subplots(figsize=(4.6, 2.3))
    y = np.arange(len(names))[::-1]
    ax.barh(y, vals, color=cols, height=0.62)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel(r"$\log_{10}$(number of .lean files)")
    ax.set_title("The submitted development: 175,187 files across ten libraries")
    for yi, v in zip(y, [v for _, v, _ in libs]):
        ax.text(np.log10(v) + 0.12, yi, f"{v:,}", va="center", fontsize=6.6, color=TXTDIM)
    ax.grid(axis="x", alpha=0.25, lw=0.5)
    ax.set_xlim(0, 6.4)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_library.pdf")


# --------------------------------------------------------------- chain ----
def _box(ax, x, y, w, h, text, fc, tc, fs=6.0, ec=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.008,rounding_size=0.012",
                                fc=fc, ec=ec or EDGE, lw=0.6, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=tc, zorder=3, linespacing=1.35)


def fig_chain():
    fig, ax = plt.subplots(figsize=(4.6, 6.3))
    ax.set_xlim(0, 4.6)
    ax.set_ylim(0, 6.3)
    ax.axis("off")
    ax.text(5, 13.55, "The traced proof chain, from Mathlib's statement to the Lefschetz formula",
            ha="center", fontsize=8.2, color=TXT, fontweight="bold")

    rows = [
        ("RiemannHypothesis", "Mathlib's own definition\n(Mathlib/NumberTheory/LSeries/RiemannZeta.lean:185)", ACCENT),
        ("riemannHypothesis", "src/Main.lean", ACCENT),
        ("riemannHypothesis_of_everyCharacter", "functional equation + trivial-zero classification", ACCENT),
        ("everyCharacter", "every Dirichlet L-function non-zero for Re(s) > 1/2", ACCENT),
        ("galoisLocalGlobalStrong_recParameter", "the local-global reciprocity condition", ACCENTDIM),
        ("galoisRepresentations_of_thetaLift", "from the theta lift", ACCENTDIM),
        ("geoOne_holds", "geometric realisation of weight one", ACCENTDIM),
        ("lefschetz_fixedPoint_finite_etale_correspondence",
         "integral clopen decomposition + fixed-point formula", AMBER),
    ]
    y = 12.9
    h = 1.0
    gap = 0.30
    for i, (name, note, col) in enumerate(rows):
        _box(ax, 1.1, y - h, 7.8, h, "", PANEL, TXT)
        ax.text(5, y - h / 2 + 0.19, name, ha="center", va="center",
                fontsize=6.4, color=col, family="DejaVu Sans Mono")
        ax.text(5, y - h / 2 - 0.27, note, ha="center", va="center",
                fontsize=5.6, color=TXTDIM)
        if i < len(rows) - 1:
            ax.add_patch(FancyArrowPatch((5, y - h - 0.02), (5, y - h - gap + 0.02),
                                         arrowstyle="-|>", mutation_scale=7,
                                         color=ACCENTDIM, lw=0.8))
        y -= h + gap

    # the audited gap
    ax.add_patch(Rectangle((0.55, 0.18), 8.9, 2.05, fc="#2A1D14", ec=AMBER,
                            lw=0.8, ls=(0, (3, 2)), zorder=1))
    ax.text(5, 1.32, "NOT AUDITED: does the theta lift statement carry the classical content,\n"
                     "or does it restate the hard part under a familiar name?",
            ha="center", va="center", fontsize=6.1, color=AMBER, zorder=3, linespacing=1.4)
    ax.text(5, 0.52, "Everything above this box was read in the source and checked.",
            ha="center", va="center", fontsize=5.9, color=TXTDIM, zorder=3)
    save(fig, "fig_chain.pdf")


# ------------------------------------------------------- trust boundary ---
def fig_architecture():
    fig, ax = plt.subplots(figsize=(4.6, 4.3))
    ax.set_xlim(0, 4.6)
    ax.set_ylim(0, 4.3)
    ax.axis("off")
    ax.text(5, 8.85, "Three different questions, and the tools that answer each",
            ha="center", fontsize=8.4, color=TXT, fontweight="bold")

    layers = [
        (7.35, 1.35, "Q1  Does it compile?", "toolchain v4.33.1, Mathlib at a pinned revision",
         ACCENT, "ANSWERED 2026-11-20"),
        (5.20, 1.35, "Q2  Does it use only standard axioms?",
         "#print axioms -> propext, Classical.choice, Quot.sound", ACCENT, "ANSWERED (static scan)"),
        (3.05, 1.35, "Q3  Does the formal statement mean what the author claims?",
         "a referee's reading of the load-bearing inputs", AMBER, "UNANSWERED"),
    ]
    for y, h, q, sub, col, status in layers:
        _box(ax, 0.5, y, 9.0, h, "", PANEL, TXT)
        ax.text(0.8, y + h - 0.34, q, fontsize=7.0, color=col, va="center", fontweight="bold")
        ax.text(0.8, y + h - 0.70, sub, fontsize=6.1, color=TXTDIM, va="center")
        ax.text(9.25, y + h - 0.50, status, fontsize=5.8, color=col, va="center", ha="right",
                family="DejaVu Sans Mono")
    for y in (7.20, 5.05):
        ax.add_patch(FancyArrowPatch((5, y), (5, y - 0.16), arrowstyle="-|>",
                                     mutation_scale=8, color=ACCENTDIM, lw=1.0))
    ax.text(5, 1.95,
            "The Lean kernel certifies Q1 and Q2. It cannot certify Q3.\n"
            "arXiv:2606.29493 states this explicitly: the kernel does not check that a formal\n"
            "statement matches the informal claim it is meant to capture.",
            ha="center", va="center", fontsize=6.2, color=AMBER, linespacing=1.55)
    ax.plot([0.7, 9.3], [1.05, 1.05], color=EDGE, lw=0.8, ls=(0, (3, 2)))
    ax.text(0.7, 0.62, "Above the line: mechanical. Below the line: mathematical.",
            fontsize=6.2, color=TXTDIM, ha="left")
    save(fig, "fig_architecture.pdf")


# ------------------------------------------------------------ barriers ----
def fig_barriers():
    fig, ax = plt.subplots(figsize=(4.6, 3.7))
    ax.set_xlim(0, 4.6)
    ax.set_ylim(0, 3.7)
    ax.axis("off")
    ax.text(5, 7.85, "Four obstacles on the route from the method to a proof of RH",
            ha="center", fontsize=8.4, color=TXT, fontweight="bold")

    bars = [
        ("The function-field barrier", "Stepanov's method needs a product of a geometric and an\n"
         "arithmetic coordinate. Over Z that product is one-dimensional.",
         "van Frankenhuijsen, arXiv:0806.0044"),
        ("The automorphy gap", "No general theorem establishes automorphy and analyticity of\n"
         "the third-place theta lift. Only special cases are known.",
         "Gross-Prasad: unitary proved, orthogonal open"),
        ("The surviving H^1 classes", "Classes in H^1_o that twisting does not kill. The author\n"
         "names a significant weakening of Vandiver as the needed remedy.",
         "Vandiver: open; verified below 2^31"),
        ("The two-thirds ceiling", "The author's own timeline entry 14 records that the method\n"
         "'would stop at 2/3 a priori'. Entry 20 claims GRH the next day.",
         "Remark, items 14 and 20"),
    ]
    y = 6.55
    for i, (title, body, src) in enumerate(bars):
        col = AMBER if i >= 2 else ACCENT
        _box(ax, 0.4, y - 1.42, 9.2, 1.42, "", PANEL, TXT)
        ax.add_patch(Rectangle((0.4, y - 1.42), 0.055, 1.42, fc=col, ec="none", zorder=3))
        ax.text(0.72, y - 0.30, title, fontsize=7.2, color=col, va="center", fontweight="bold")
        ax.text(0.72, y - 0.80, body, fontsize=6.0, color=TXT, va="center", linespacing=1.5)
        ax.text(0.72, y - 1.22, src, fontsize=5.6, color=TXTDIM, va="center")
        y -= 1.72
    save(fig, "fig_barriers.pdf")


# --------------------------------------------------------- theta lifts ----
def fig_theta_lift():
    fig, ax = plt.subplots(figsize=(4.6, 2.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.4)
    ax.axis("off")
    ax.text(5, 5.08, "The iterated theta lift: each step wins one unit of multiplicity",
            ha="center", fontsize=8.2, color=TXT, fontweight="bold")

    xs = np.linspace(1.0, 9.0, 4)
    labels = [r"$U(X_0)$", r"$U(X_1)$", r"$U(X_2)$", r"$U(X_m)$"]
    for i, (x, lab) in enumerate(zip(xs, labels)):
        _box(ax, x - 0.85, 2.05, 1.7, 0.85, "", PANEL, TXT)
        ax.text(x, 2.47, lab, ha="center", va="center", fontsize=8, color=ACCENT,
                family="DejaVu Sans Mono")
        ax.text(x, 1.80, "multiplicity %d" % i, ha="center", va="center",
                fontsize=5.8, color=TXTDIM)
        if i < 3:
            ax.add_patch(FancyArrowPatch((x + 0.88, 2.47), (xs[i + 1] - 0.88, 2.47),
                                         arrowstyle="-|>", mutation_scale=9,
                                         color=ACCENTDIM, lw=1.0))
    ax.text(5, 3.45, r"$m \approx \sqrt{X}$", ha="center", fontsize=8, color=AMBER)
    ax.text(5, 3.12, "the length of the chain the remark proposes to take",
            ha="center", fontsize=6.0, color=TXTDIM)
    ax.text(5, 0.92,
            r"Each lift is supposed to buy one 'multiplicity' -- the feature that exists in the"
            "\n"
            r"function-field proof of Stepanov and Bombieri but has no analogue over the"
            "\n"
            r"integers. The remark calls it 'corresponding to something like differentiating"
            "\n"
            r"whole numbers'. Whether a chain of length $\sqrt{X}$ can be built, and paid for,"
            "\n"
            r"is the analytic content of item 14.",
            ha="center", va="center", fontsize=6.1, color=TXT, linespacing=1.5)
    save(fig, "fig_theta_lift.pdf")


# ------------------------------------------------------------- records ----
def fig_records():
    fig, ax = plt.subplots(figsize=(4.6, 2.5))
    rows = [
        ("Conrey (1989) / Pratt-Robles-Zaharescu (2020)", 0.417293,
         "on the critical line (asymptotic)"),
        ("Alpöge-Furman (2026), arXiv:2608.13637", 0.6725,
         "simple AND on the line"),
        ("Alpöge-Furman (2026), arXiv:2608.13637", 0.83625,
         "distinct zeros on the line"),
        ("Lamzouri (2026), arXiv:2609.02882", 0.8876,
         "simple OR critical"),
    ]
    names = [r[0] for r in rows]
    vals = [r[1] for r in rows]
    notes = [r[2] for r in rows]
    y = np.arange(len(rows))[::-1]
    cols = [ACCENTDIM, ACCENT, ACCENT, ACCENTDIM]
    ax.barh(y, [v * 100 for v in vals], color=cols, height=0.55)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=6.6)
    ax.set_xlim(0, 100)
    ax.set_xlabel("per cent of zeros")
    ax.set_title("The record on the proportion of zeros on the critical line")
    for yi, v, n in zip(y, vals, notes):
        ax.text(v * 100 + 1.2, yi + 0.06, f"{v*100:.3f}%", va="center", fontsize=6.6, color=TXT)
        ax.text(v * 100 + 8.5, yi + 0.06, f"({n})", va="center", fontsize=5.8, color=TXTDIM)
    ax.axvline(100, color=AMBER, lw=1.0, ls=(0, (3, 2)))
    ax.text(99.4, len(rows) - 0.35, "RH = 100%", color=AMBER, fontsize=6.2, ha="right")
    ax.grid(axis="x", alpha=0.25, lw=0.5)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_records.pdf")


# ------------------------------------------------------------ protocol ----
def fig_protocol():
    fig, ax = plt.subplots(figsize=(4.6, 4.1))
    ax.set_xlim(0, 4.6)
    ax.set_ylim(0, 4.1)
    ax.axis("off")
    ax.text(5, 9.25, "A protocol that would settle the claim", ha="center",
            fontsize=8.4, color=TXT, fontweight="bold")

    steps = [
        ("1", "Rebuild from the pinned revision",
         "lake build at Mathlib 0df444a3..., record the elapsed time", "mechanical"),
        ("2", "Read the axiom set",
         "#print axioms riemannHypothesis -> propext, Classical.choice, Quot.sound", "mechanical"),
        ("3", "Replay the kernel independently",
         "lean4export + an external kernel (NanoDa, lean4checker)", "mechanical"),
        ("4", "Check the statements, not the proofs",
         "read TLiftK, Tools_k, EpsOf_k, Hyps against the classical theorems", "mathematical"),
        ("5", "Look for the empty hole",
         "a weakened input wearing a classical name, or a statement proved only for\n"
         "the trivial character", "mathematical"),
        ("6", "Read the remark against the code",
         "does the code do what item 14 and item 17 say it does?", "mathematical"),
    ]
    y = 8.35
    for num, title, sub, kind in steps:
        col = ACCENT if kind == "mechanical" else AMBER
        _box(ax, 0.4, y - 1.28, 9.2, 1.28, "", PANEL, TXT)
        ax.add_patch(Circle((0.92, y - 0.64), 0.30, fc="none", ec=col, lw=0.9, zorder=3))
        ax.text(0.92, y - 0.64, num, ha="center", va="center", fontsize=7.2, color=col, zorder=4)
        ax.text(1.40, y - 0.36, title, fontsize=6.9, color=col, va="center", fontweight="bold")
        ax.text(1.40, y - 0.90, sub, fontsize=5.9, color=TXT, va="center", linespacing=1.4)
        ax.text(9.35, y - 0.64, kind, fontsize=5.6, color=TXTDIM, va="center", ha="right")
        y -= 1.44
    save(fig, "fig_protocol.pdf")


if __name__ == "__main__":
    fig_critical_line()
    fig_psi()
    fig_library()
    fig_chain()
    fig_architecture()
    fig_barriers()
    fig_theta_lift()
    fig_records()
    fig_protocol()
    print("figures written to", OUT)
