#!/usr/bin/env python3
"""
Front and back covers for "Is the Riemann Hypothesis Solved?"

Front cover: the generated watercolour artwork, full bleed, with the full
identity block set in vector over a legibility scrim.
Back cover: a different crop of the same plate, heavily scrimmed, with the
blurb, the parts list and the footer.

Outputs (6 x 9 in, 300 dpi raster on vector type):
    figures/cover_front.pdf / .png
    figures/cover_back.pdf  / .png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "figures" / "cover_art.jpg"
OUT = ROOT / "figures"

W_IN, H_IN = 6.0, 9.0
DPI = 300

INK = "#0C1016"
ACCENT = "#8FD6C0"
TEXT = "#E6EBEF"
DIM = "#8B9BA7"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Outfit", "DejaVu Sans"],
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})


def tracked(ax, x, y, text, size, colour=ACCENT, weight="normal", track=0.0,
            ha="left", va="baseline", family="sans-serif"):
    """Draw text with manual letter spacing."""
    fig = ax.figure
    r = fig.canvas.get_renderer()
    from matplotlib.font_manager import FontProperties
    fp = FontProperties(family=family, weight=weight, size=size)
    adv = [r.get_text_width_height_descent(ch, fp, ismath=False)[0] / fig.dpi
           for ch in text]
    gap = track * size / 72.0
    total = sum(adv) + gap * (len(text) - 1)
    cursor = x if ha == "left" else (x - total if ha == "right" else x - total / 2)
    for ch, cw in zip(text, adv):
        ax.text(cursor, y, ch, fontsize=size, fontweight=weight, color=colour,
                family=family, ha="left", va=va, zorder=20)
        cursor += cw + gap
    return cursor


def text_w(fig, txt, size, weight="normal", family="sans-serif"):
    from matplotlib.font_manager import FontProperties
    r = fig.canvas.get_renderer()
    fp = FontProperties(family=family, weight=weight, size=size)
    return r.get_text_width_height_descent(txt, fp, ismath=False)[0] / fig.dpi


def wrap(fig, txt, size, max_w_in, weight="normal", family="sans-serif"):
    lines, cur = [], ""
    for word in txt.split():
        trial = word if not cur else cur + " " + word
        if text_w(fig, trial, size, weight, family) <= max_w_in:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def scrim(ax, stops, colour=INK):
    """Overlay a vertical alpha ramp: stops = [(y_frac, alpha), ...]."""
    n = 800
    ys = np.linspace(0, 1, n)
    alphas = np.zeros(n)
    for (y0, a0), (y1, a1) in zip(stops[:-1], stops[1:]):
        m = (ys >= y0) & (ys <= y1)
        alphas[m] = a0 + (a1 - a0) * (ys[m] - y0) / max(y1 - y0, 1e-9)
    alphas[ys < stops[0][0]] = stops[0][1]
    alphas[ys > stops[-1][0]] = stops[-1][1]
    rgb = np.array([int(colour[i:i + 2], 16) for i in (1, 3, 5)]) / 255.0
    rgba = np.zeros((n, 2, 4))
    rgba[..., 0] = rgb[0]
    rgba[..., 1] = rgb[1]
    rgba[..., 2] = rgb[2]
    rgba[:, :, 3] = alphas[:, None]
    ax.imshow(rgba, extent=[0, W_IN, 0, H_IN], origin="lower", aspect="auto",
              zorder=5, interpolation="bilinear")


def canvas():
    fig = plt.figure(figsize=(W_IN, H_IN), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W_IN)
    ax.set_ylim(0, H_IN)
    ax.axis("off")
    return fig, ax


def save(fig, name):
    for ext in ("pdf", "png"):
        path = OUT / f"{name}.{ext}"
        if ext == "png":
            fig.savefig(path, dpi=DPI, facecolor=INK)
        else:
            fig.savefig(path, facecolor=INK)
    plt.close(fig)
    print(f"wrote {OUT}/{name}.pdf and .png")


def front_cover():
    fig, ax = canvas()
    img = Image.open(ART).convert("RGB").resize((int(W_IN * 300), int(H_IN * 300)),
                                               Image.LANCZOS)
    ax.imshow(img, extent=[0, W_IN, 0, H_IN], aspect="auto", zorder=0)
    scrim(ax, [(0.00, 0.92), (0.30, 0.88), (0.45, 0.42), (0.52, 0.30),
               (0.60, 0.58), (0.72, 0.74), (0.86, 0.82), (1.00, 0.95)])

    x0 = 0.60
    x1 = W_IN - 0.52

    # --- eyebrow --------------------------------------------------------
    y = H_IN - 0.58
    tracked(ax, x0, y, "A CRITICAL AUDIT OF A CLAIMED PROOF", 7.0,
            ACCENT, "normal", track=0.30)

    # --- title ----------------------------------------------------------
    y -= 0.66
    ax.text(x0, y, "IS THE RIEMANN", fontsize=33.5, fontweight="bold",
            color=TEXT, family="sans-serif", ha="left", va="baseline", zorder=20)
    y -= 0.475
    ax.text(x0, y, "HYPOTHESIS", fontsize=33.5, fontweight="bold",
            color=TEXT, family="sans-serif", ha="left", va="baseline", zorder=20)
    y -= 0.475
    ax.text(x0, y, "SOLVED?", fontsize=33.5, fontweight="bold",
            color=ACCENT, family="sans-serif", ha="left", va="baseline", zorder=20)

    # --- rule -----------------------------------------------------------
    y -= 0.40
    ax.add_patch(Rectangle((x0, y), x1 - x0, 0.028, facecolor=ACCENT,
                           edgecolor="none", zorder=20))

    # --- subtitle -------------------------------------------------------
    y -= 0.34
    for line in ["A Critical Audit of the Lean Formalization,",
                 "the Theta-Lift Method, and the",
                 "Two-Thirds Ceiling"]:
        ax.text(x0, y, line, fontsize=10.4, color=TEXT, family="sans-serif",
                ha="left", va="baseline", zorder=20)
        y -= 0.195

    # --- tagline --------------------------------------------------------
    y -= 0.20
    ax.text(x0, y, "It compiles. It has no axioms.\nNobody has checked the mathematics.",
            fontsize=9.4, color=DIM, family="sans-serif", style="italic",
            ha="left", va="baseline", linespacing=1.55, zorder=20)

    # --- credits --------------------------------------------------------
    bx = x0
    by = 2.42
    ax.text(bx, by, "GERALD ENRIQUE", fontsize=12.2, fontweight="bold",
            color=TEXT, family="sans-serif", ha="left", va="baseline", zorder=20)
    by -= 0.205
    ax.text(bx, by, "NELSON MC KENZIE", fontsize=12.2, fontweight="bold",
            color=TEXT, family="sans-serif", ha="left", va="baseline", zorder=20)

    by -= 0.30
    ax.add_patch(Rectangle((bx, by), 0.56, 0.020, facecolor=ACCENT,
                           edgecolor="none", zorder=20))

    by -= 0.27
    for line in ["Tico Internet LLC",
                 "2026 First Edition",
                 "Licensed under the Apache License 2.0",
                 "DOI 10.5281/zenodo.23874214"]:
        ax.text(bx, by, line, fontsize=8.4, color=DIM, family="sans-serif",
                ha="left", va="baseline", zorder=20)
        by -= 0.163

    save(fig, "cover_front")


def back_cover():
    fig, ax = canvas()
    img = Image.open(ART).convert("RGB")
    w, h = img.size
    # a different crop, so the back is not a repeat of the front
    img = img.crop((int(w * 0.02), int(h * 0.02), int(w * 0.62), int(h * 0.72)))
    img = img.resize((int(W_IN * 300), int(H_IN * 300)), Image.LANCZOS)
    ax.imshow(img, extent=[0, W_IN, 0, H_IN], aspect="auto", zorder=0)
    scrim(ax, [(0.00, 0.92), (0.58, 0.84), (1.00, 0.94)])

    x0 = 0.60
    x1 = W_IN - 0.52

    y = H_IN - 0.70
    tracked(ax, x0, y, "IS THE RIEMANN HYPOTHESIS SOLVED?", 9.2, ACCENT,
            "bold", track=0.20)
    y -= 0.28
    ax.add_patch(Rectangle((x0, y), x1 - x0, 0.022, facecolor=ACCENT,
                           edgecolor="none", zorder=20))
    y -= 0.32
    ax.text(x0, y, "Gerald Enrique Nelson Mc Kenzie", fontsize=9.8, color=DIM,
            family="sans-serif", ha="left", va="baseline", zorder=20)

    # --- blurb ----------------------------------------------------------
    y -= 0.48
    blurb = (
        "In November 2026 a mathematician published four pages claiming to have "
        "proved the Riemann Hypothesis, together with a Lean development of "
        "175,187 files and roughly 17.4 million lines. Two university teams "
        "compiled it the same day. The world's newspapers called it the greatest "
        "mathematical result of the century.\n\n"
        "None of it has been reviewed.\n\n"
        "This book takes the artifact seriously, reads it, and traces the proof "
        "chain from Mathlib's own definition of the hypothesis down to a proved "
        "fixed-point formula. It reports what the code actually establishes, "
        "identifies the load-bearing inputs that nobody has audited, and sets "
        "out the author's own admissions: a computed ceiling at two thirds of "
        "the zeros, and an obstruction whose stated remedy requires a conjecture "
        "that is still open.\n\n"
        "The finding is neither applause nor dismissal. The claim is unresolved, "
        "and Chapter 14 gives the protocol that would settle it."
    )
    blurb_lines = []
    for para in blurb.split("\n\n"):
        blurb_lines.extend(wrap(fig, para, 8.3, x1 - x0))
        blurb_lines.append("")
    blurb_lines = blurb_lines[:-1]
    for i, line in enumerate(blurb_lines):
        weight = "bold" if line == "None of it has been reviewed." else "normal"
        ax.text(x0, y - i * 0.148, line, fontsize=8.3, color=TEXT,
                family="sans-serif", fontweight=weight, ha="left", va="baseline",
                zorder=20)

    # --- parts ----------------------------------------------------------
    y = 2.62
    tracked(ax, x0, y, "INSIDE", 6.8, ACCENT, "bold", track=0.30)
    y -= 0.235
    for p in ["I    The Claim",
              "II   The Mathematics",
              "III  The Verification",
              "IV   The State of Play",
              "V    The Verdict"]:
        ax.text(x0, y, p, fontsize=8.6, color=TEXT, family="sans-serif",
                ha="left", va="baseline", zorder=20)
        y -= 0.196

    # --- footer ---------------------------------------------------------
    fy = 0.92
    ax.add_patch(Rectangle((x0, fy), x1 - x0, 0.010, facecolor=DIM,
                           edgecolor="none", alpha=0.45, zorder=20))
    ax.text(x0, fy - 0.26, "Tico Internet LLC  ·  2026 First Edition  ·  "
            "Apache License 2.0", fontsize=7.6, color=DIM, family="sans-serif",
            ha="left", va="baseline", zorder=20)
    ax.text(x0, fy - 0.46, "DOI 10.5281/zenodo.23874214", fontsize=7.6,
            color=DIM, family="sans-serif", ha="left", va="baseline", zorder=20)

    save(fig, "cover_back")


if __name__ == "__main__":
    front_cover()
    back_cover()
