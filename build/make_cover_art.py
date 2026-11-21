#!/usr/bin/env python3
"""Prepare the cover plates and the legibility scrims.

Both plates are 6 x 9 in at 300 DPI (1800 x 2700 px), saved as JPEG so that
LaTeX embeds them as DCTDecode rather than as raw RGB. The front uses the
whole artwork; the back uses a different crop so it is not a repeat.

The scrim is the alpha ramp that keeps the cover type legible over the
watercolour. It is emitted as a table of TikZ fill commands so that the
cover documents stay free of arithmetic.
"""
import pathlib

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
FIG = HERE.parent / "figures"
SRC = FIG / "cover_art.jpg"
DPI = 300
W, H = 6 * DPI, 9 * DPI
STEPS = 256

FIG.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC).convert("RGB")
w, h = im.size

FRONT_STOPS = [(0.00, 0.68), (1.20, 0.80), (2.70, 0.88), (4.05, 0.48),
               (4.68, 0.34), (5.40, 0.62), (6.48, 0.78), (7.74, 0.86),
               (9.00, 0.95)]
BACK_STOPS = [(0.00, 0.93), (5.22, 0.88), (7.98, 0.92), (9.00, 0.94)]
INK = (0x0C, 0x10, 0x16)


def ramp(stops, y):
    """Alpha at height y (inches from the foot) for a list of (y, alpha) stops."""
    if y <= stops[0][0]:
        return stops[0][1]
    if y >= stops[-1][0]:
        return stops[-1][1]
    for (y0, a0), (y1, a1) in zip(stops[:-1], stops[1:]):
        if y0 <= y <= y1:
            return a0 + (a1 - a0) * (y - y0) / (y1 - y0)
    return stops[-1][1]


def scrim(plate, stops):
    """Bake the legibility ramp into the plate.

    Doing it here rather than in the cover document keeps the PDF free of
    hundreds of vector rectangles and keeps the artwork as a single JPEG.
    """
    import numpy as np
    a = np.asarray(plate).astype("float32")
    h = a.shape[0]
    ys = (1.0 - np.arange(h) / h) * 9.0        # inches from the foot
    alphas = np.array([ramp(stops, float(y)) for y in ys], dtype="float32")
    alphas = alphas[:, None, None]
    ink = np.array(INK, dtype="float32")[None, None, :]
    out = a * (1.0 - alphas) + ink * alphas
    return Image.fromarray(out.clip(0, 255).astype("uint8"))


front = scrim(im.resize((W, H), Image.BICUBIC), FRONT_STOPS)
front.save(FIG / "cover_front_art.jpg", "JPEG", quality=84, optimize=True,
           progressive=True, subsampling=1)

back = im.crop((int(w * 0.02), int(h * 0.02), int(w * 0.62), int(h * 0.72)))
back = scrim(back.resize((W, H), Image.BICUBIC), BACK_STOPS)
back.save(FIG / "cover_back_art.jpg", "JPEG", quality=84, optimize=True,
         progressive=True, subsampling=1)


def ramp(stops, y):
    """Alpha at height y (inches from the foot) for a list of (y, alpha) stops."""
    if y <= stops[0][0]:
        return stops[0][1]
    if y >= stops[-1][0]:
        return stops[-1][1]
    for (y0, a0), (y1, a1) in zip(stops[:-1], stops[1:]):
        if y0 <= y <= y1:
            return a0 + (a1 - a0) * (y - y0) / (y1 - y0)
    return stops[-1][1]


for p in (FIG / "cover_front_art.jpg", FIG / "cover_back_art.jpg"):
    print(f"wrote {p}  ({p.stat().st_size // 1024} KB)")
