#!/usr/bin/env python3
"""
Diagram figures for "Is the Riemann Hypothesis Solved?", drawn at true print
size.

The five diagram figures are laid out in INCH coordinates on a 4.6 x H inch
canvas, which is the exact text width of the 6 x 9 trim. They are therefore
included at \\textwidth with no scaling, so every label is at its stated point
size in the finished book.

The four chart figures are computed and sized to the same text width.
"""
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

W = 4.6          # text width, inches
L = 0.30         # left margin
R = W - 0.30     # right edge

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
    "axes.titlesize": 8.5,
    "axes.titleweight": "bold",
    "axes.titlecolor": TXT,
    "figure.dpi": 200,
    "pdf.fonttype": 42,
})


def save(fig, name):
    p = OUT / name
    fig.savefig(p, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    print("wrote", p)


def canvas(h):
    fig, ax = plt.subplots(figsize=(W, h))
    ax.set_xlim(0, W)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, fc=PANEL, ec=EDGE, lw=0.6, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.004,rounding_size=0.02",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def arrow(ax, x0, y0, x1, y1, color=ACCENTDIM, lw=0.8, ms=6):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=ms, color=color, lw=lw,
                                 zorder=3, shrinkA=0, shrinkB=0))


# ------------------------------------------------------------- the chain ---
def fig_chain():
    H = 7.15
    fig, ax = canvas(H)
    ax.text(W / 2, H - 0.22, "The traced proof chain", ha="center", va="top",
            fontsize=8.4, color=TXT, fontweight="bold")
    ax.text(W / 2, H - 0.48, "from Mathlib's statement to the Lefschetz formula",
            ha="center", va="top", fontsize=6.6, color=TXTDIM)

    rows = [
        ("RiemannHypothesis", "Mathlib/NumberTheory/LSeries/RiemannZeta.lean:185", ACCENT),
        ("riemannHypothesis", "src/Main.lean", ACCENT),
        ("riemannHypothesis_of_everyCharacter", "functional equation, trivial zeros", ACCENT),
        ("everyCharacter", "every Dirichlet L-function non-zero for Re(s) > 1/2", ACCENT),
        ("galoisLocalGlobalStrong_recParameter", "the local-global reciprocity condition", ACCENTDIM),
        ("galoisRepresentations_of_thetaLift", "from the theta lift", ACCENTDIM),
        ("geoOne_holds", "geometric realisation of weight one", ACCENTDIM),
        ("lefschetz_fixedPoint_finite_etale_correspondence",
         "integral clopen decomposition, fixed-point formula", AMBER),
    ]
    top = H - 0.66
    bh = 0.50
    gap = 0.145
    for i, (name, note, col) in enumerate(rows):
        y = top - (i + 1) * bh - i * gap
        box(ax, L, y, R - L, bh)
        ax.text(W / 2, y + bh * 0.66, name, ha="center", va="center",
                fontsize=6.0, color=col, family="DejaVu Sans Mono")
        ax.text(W / 2, y + bh * 0.24, note, ha="center", va="center",
                fontsize=5.4, color=TXTDIM)
        if i < len(rows) - 1:
            arrow(ax, W / 2, y - 0.015, W / 2, y - gap + 0.015, ms=5)

    ybot = top - len(rows) * (bh + gap) + gap
    box(ax, L, 0.10, R - L, ybot - 0.28, fc="#2A1D14", ec=AMBER, lw=0.8)
    ax.text(W / 2, ybot - 0.30, "NOT AUDITED", ha="center", va="center",
            fontsize=6.2, color=AMBER, family="DejaVu Sans Mono")
    ax.text(W / 2, ybot - 0.58,
            "Does the theta lift statement carry the classical\n"
            "content, or does it restate the hard part under\n"
            "a familiar name?",
            ha="center", va="center", fontsize=5.8, color=AMBER, linespacing=1.45)
    ax.text(W / 2, ybot - 0.95,
            "Everything above was read in the source and checked.",
            ha="center", va="center", fontsize=5.4, color=TXTDIM)
    save(fig, "fig_chain.pdf")


# ------------------------------------------------------ trust boundary ----
def fig_architecture():
    H = 4.35
    fig, ax = canvas(H)
    ax.text(W / 2, H - 0.20, "Three questions, three different tools",
            ha="center", va="top", fontsize=8.4, color=TXT, fontweight="bold")

    layers = [
        ("Q1   Does it compile?",
         "toolchain v4.33.1, Mathlib at a pinned revision",
         "ANSWERED 2026-11-20", ACCENT),
        ("Q2   Does it use only standard axioms?",
         "#print axioms -> propext, Classical.choice, Quot.sound",
         "ANSWERED (static scan)", ACCENT),
        ("Q3   Does the statement mean what is claimed?",
         "a referee's reading of the load-bearing inputs",
         "UNANSWERED", AMBER),
    ]
    top = H - 0.52
    bh = 0.62
    gap = 0.24
    for i, (q, sub, status, col) in enumerate(layers):
        y = top - (i + 1) * bh - i * gap
        box(ax, L, y, R - L, bh)
        ax.text(L + 0.12, y + bh * 0.66, q, fontsize=6.6, color=col,
                va="center", fontweight="bold")
        ax.text(L + 0.12, y + bh * 0.26, sub, fontsize=5.5, color=TXTDIM,
                va="center")
        ax.text(R - 0.10, y + bh * 0.5, status, fontsize=5.0, color=col,
                va="center", ha="right", family="DejaVu Sans Mono")
        if i < len(layers) - 1:
            arrow(ax, W / 2, y - 0.02, W / 2, y - gap + 0.02, lw=1.0, ms=7)

    yb = top - len(layers) * (bh + gap) + gap
    ax.plot([L, R], [yb - 0.10, yb - 0.10], color=EDGE, lw=0.8, ls=(0, (3, 2)))
    ax.text(W / 2, yb - 0.34,
            "The kernel certifies Q1 and Q2. It cannot certify Q3.\n"
            "arXiv:2606.29493 says so explicitly: the kernel does not\n"
            "check that a formal statement matches the informal claim\n"
            "it is meant to capture.",
            ha="center", va="center", fontsize=5.9, color=AMBER, linespacing=1.5)
    ax.text(L, yb - 1.06, "Above the line: mechanical. Below: mathematical.",
            fontsize=5.6, color=TXTDIM, ha="left")
    save(fig, "fig_architecture.pdf")


# ----------------------------------------------------------- barriers -----
def fig_barriers():
    H = 4.35
    fig, ax = canvas(H)
    ax.text(W / 2, H - 0.18, "Four obstacles on the route to a proof",
            ha="center", va="top", fontsize=8.4, color=TXT, fontweight="bold")

    bars = [
        ("The function-field barrier",
         "Stepanov's method needs a product of a geometric and\n"
         "an arithmetic coordinate. Over Z that product is\n"
         "one-dimensional.",
         "van Frankenhuijsen, arXiv:0806.0044", ACCENT),
        ("The automorphy gap",
         "No general theorem establishes automorphy and\n"
         "analyticity of the third-place theta lift. Only\n"
         "special cases are known.",
         "Gross-Prasad: unitary proved, orthogonal open", ACCENT),
        ("The surviving H1 classes",
         "Classes in H1 that twisting does not kill. The author\n"
         "names a significant weakening of Vandiver as the\n"
         "remedy.",
         "Vandiver: open; verified below 2^31", AMBER),
        ("The two-thirds ceiling",
         "The author's own entry 14 records that the method\n"
         "'would stop at 2/3 a priori'. Entry 20 claims GRH\n"
         "the next day.",
         "Remark, items 14 and 20", AMBER),
    ]
    top = H - 0.46
    bh = 0.83
    gap = 0.135
    for i, (title, body, src, col) in enumerate(bars):
        y = top - (i + 1) * bh - i * gap
        box(ax, L, y, R - L, bh)
        ax.add_patch(Rectangle((L, y), 0.045, bh, fc=col, ec="none", zorder=3))
        ax.text(L + 0.14, y + bh - 0.16, title, fontsize=6.8, color=col,
                va="center", fontweight="bold")
        ax.text(L + 0.14, y + bh - 0.42, body, fontsize=5.6, color=TXT,
                va="center", linespacing=1.45)
        ax.text(L + 0.14, y + 0.11, src, fontsize=5.2, color=TXTDIM, va="center")
    save(fig, "fig_barriers.pdf")


# --------------------------------------------------------- theta lifts ----
def fig_theta_lift():
    H = 2.75
    fig, ax = canvas(H)
    ax.text(W / 2, H - 0.16, "The iterated theta lift", ha="center", va="top",
            fontsize=8.4, color=TXT, fontweight="bold")

    xs = np.linspace(0.72, W - 0.72, 4)
    for i, (x, lab) in enumerate(zip(xs, [r"$U(X_0)$", r"$U(X_1)$",
                                          r"$U(X_2)$", r"$U(X_m)$"])):
        box(ax, x - 0.44, 1.42, 0.88, 0.42)
        ax.text(x, 1.63, lab, ha="center", va="center", fontsize=8,
                color=ACCENT, family="DejaVu Sans Mono")
        ax.text(x, 1.28, "multiplicity %d" % i, ha="center", va="center",
                fontsize=5.4, color=TXTDIM)
        if i < 3:
            arrow(ax, x + 0.46, 1.63, xs[i + 1] - 0.46, 1.63, lw=1.0, ms=7)

    ax.text(W / 2, 2.08, r"$m \approx \sqrt{X}$", ha="center", va="center",
            fontsize=8, color=AMBER)
    ax.text(W / 2, 1.92, "the chain length the remark proposes to take",
            ha="center", va="center", fontsize=5.6, color=TXTDIM)

    ax.text(W / 2, 0.60,
            "Each lift is meant to buy one unit of the\n"
            "multiplicity that the function-field method gets\n"
            "for free over a finite field. Whether a chain of\n"
            "length sqrt(X) can be built, and paid for, is the\n"
            "analytic content of item 14.",
            ha="center", va="center", fontsize=5.9, color=TXT, linespacing=1.5)
    save(fig, "fig_theta_lift.pdf")


# ------------------------------------------------------------ protocol ----
def fig_protocol():
    H = 4.5
    fig, ax = canvas(H)
    ax.text(W / 2, H - 0.18, "A protocol that would settle the claim",
            ha="center", va="top", fontsize=8.4, color=TXT, fontweight="bold")

    steps = [
        ("1", "Rebuild from the pinned revision",
         "lake build at Mathlib 0df444a3...", "mechanical"),
        ("2", "Read the axiom set",
         "#print axioms -> the three standard ones", "mechanical"),
        ("3", "Replay the kernel independently",
         "lean4export + an external kernel", "mechanical"),
        ("4", "Check the statements, not the proofs",
         "read TLiftK, Tools_k, EpsOf_k, Hyps against the\n"
         "classical theorems", "mathematical"),
        ("5", "Look for the empty hole",
         "a weakened input wearing a classical name", "mathematical"),
        ("6", "Read the remark against the code",
         "does the code do what items 14 and 17 say?", "mathematical"),
    ]
    top = H - 0.46
    bh = 0.52
    gap = 0.115
    for i, (num, title, sub, kind) in enumerate(steps):
        y = top - (i + 1) * bh - i * gap
        col = ACCENT if kind == "mechanical" else AMBER
        box(ax, L, y, R - L, bh)
        ax.add_patch(Circle((L + 0.22, y + bh / 2), 0.135, fc="none", ec=col,
                            lw=0.9, zorder=3))
        ax.text(L + 0.22, y + bh / 2, num, ha="center", va="center",
                fontsize=6.4, color=col, zorder=4)
        ax.text(L + 0.44, y + bh * 0.68, title, fontsize=6.4, color=col,
                va="center", fontweight="bold")
        ax.text(L + 0.44, y + bh * 0.26, sub, fontsize=5.5, color=TXT,
                va="center", linespacing=1.35)
        ax.text(R - 0.09, y + bh / 2, kind, fontsize=5.0, color=TXTDIM,
                va="center", ha="right")
    save(fig, "fig_protocol.pdf")


if __name__ == "__main__":
    fig_chain()
    fig_architecture()
    fig_barriers()
    fig_theta_lift()
    fig_protocol()
    print("diagram figures written to", OUT)
