#!/usr/bin/env python3
"""
Computed figures for "Is the Riemann Hypothesis Solved?"

This script draws the four figures that are computed: the critical line, the
exact psi(x) - x, the library census and the record on zeros. The five
schematic diagrams are drawn by make_diagrams.py, which owns them; keeping
one generator per figure is the point.

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
    # reserve an empty band at the top so that the legend cannot sit on the curve
    lo, hi = ax.get_ylim()
    ax.set_ylim(lo, hi + 0.62 * (hi - lo))
    ax.legend(facecolor=PANEL, edgecolor=EDGE, fontsize=7, labelcolor=TXT,
              loc="upper right", framealpha=0.92)
    ax.text(0.015, 0.955,
            "tick marks: the first five zeros on the critical line",
            transform=ax.transAxes, color=TXTDIM, fontsize=6.5, va="top",
            bbox=dict(facecolor=BG, edgecolor="none", alpha=0.78, pad=1.6))
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
            r"$\psi(x)$ is $\sum \Lambda(n)$ over $n\leq x$, computed exactly by sieving;" "\n"
            r"RH is equivalent to $\psi(x)=x+O(x^{1/2}\log^2 x)$",
            transform=ax.transAxes, color=TXTDIM, fontsize=6.2,
            bbox=dict(facecolor=BG, edgecolor="none", alpha=0.72, pad=1.6))
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
            ("Main + Statements", 2, AMBER)]
    names = [n for n, _, _ in libs]
    vals = np.log10([v for _, v, _ in libs])
    cols = [c for _, _, c in libs]
    fig, ax = plt.subplots(figsize=(4.6, 2.3))
    y = np.arange(len(names))[::-1]
    ax.barh(y, vals, color=cols, height=0.62)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel(r"$\log_{10}$(number of .lean files)")
    ax.set_title("The submitted development: 175,187 files across nine directories")
    for yi, v in zip(y, [v for _, v, _ in libs]):
        ax.text(np.log10(v) + 0.12, yi, f"{v:,}", va="center", fontsize=6.6, color=TXTDIM)
    ax.grid(axis="x", alpha=0.25, lw=0.5)
    ax.set_xlim(0, 6.4)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_library.pdf")


# --------------------------------------------------------------- chain ----
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
    # the qualification of each record goes into the tick label, so that the
    # percentage at the end of the bar has the whole row to itself
    ax.set_yticklabels([f"{n}\n({note})" for n, note in zip(names, notes)], fontsize=6.0)
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.75, len(rows) - 0.25)
    ax.set_xlabel("per cent of zeros")
    ax.set_title("Zeros on the critical line: the record", fontsize=8.4)
    for yi, v in zip(y, vals):
        ax.text(v * 100 + 1.4, yi, f"{v*100:.3f}%", va="center", fontsize=6.6, color=TXT)
    ax.axvline(100, color=AMBER, lw=1.0, ls=(0, (3, 2)))
    ax.text(99.2, -0.58, "RH = 100%", color=AMBER, fontsize=6.2, ha="right", va="center")
    ax.grid(axis="x", alpha=0.25, lw=0.5)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_records.pdf")


if __name__ == "__main__":
    fig_critical_line()
    fig_psi()
    fig_library()
    fig_records()
    print("figures written to", OUT)
