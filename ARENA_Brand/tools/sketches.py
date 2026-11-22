"""Phase 3: rapid thumbnail sweeps per direction (black only, no polish), rendered to contact sheets.

    python3 sketches.py <out dir>
"""
import itertools
import math
import os
import subprocess
import sys
from functools import partial

import resvg_py

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arena_build as A  # noqa: E402
import build_logo as B  # noqa: E402
import letters as T  # noqa: E402
from sketches_lib import C, ellipse, stadium, shield, bracket_cuts  # noqa: E402,F401

OUT = sys.argv[1]
TMP = os.path.join(OUT, "_tiles")
os.makedirs(TMP, exist_ok=True)


# ------------------------------------------------------------------ D3 Bowl / Live Pin
def d3_variants():
    v = []
    # a) pin, stadium (racetrack) ring carved in the head, live dot
    for rw, rh, t, dot in itertools.product([24, 28], [14, 18], [3, 4], [0, 4]):
        s = T.pin_shapes(24, 19, 17, 46)
        s += [stadium(24, 19, rw, rh, "cut"), stadium(24, 19, rw - 2 * t, rh - 2 * t)]
        if dot:
            s += [C(24, 19, dot, "cut"), C(24, 19, dot - 1.5)]
        v.append(("a", s))
    # b) tiers: pin head as concentric rings (the bowl's stands) + dot
    for n, g in itertools.product([1, 2], [3, 4]):
        s = T.pin_shapes(24, 19, 17, 46)
        r = 17 - 4
        for i in range(n):
            s += [C(24, 19, r, "cut"), C(24, 19, r - g)]
            r -= g + 3
        s += [C(24, 19, max(r, 3), "cut")] if n == 1 else []
        v.append(("b", s))
    # c) bowl in perspective: a wide elliptical ring whose bottom drops to the pin point, dot = live
    for ry, t, tip in itertools.product([10, 12, 14], [4, 5], [42, 46]):
        s = [ellipse(24, 18, 20, ry), {"shape": "polygon", "points": [[12, 18 + ry * .6], [36, 18 + ry * .6], [24, tip]]},
             ellipse(24, 18, 20 - t, ry - t, "cut"), C(24, 18, 3.5)]
        v.append(("c", s))
    # d) pin with a pitch (vertical rounded rect) carved; halfway line
    for w, h, line in itertools.product([12, 14], [20, 24], [0, 1]):
        s = T.pin_shapes(24, 19, 17, 46) + [{"shape": "rect", "x": 24 - w / 2, "y": 19 - h / 2, "w": w, "h": h, "r": 3, "op": "cut"}]
        if line:
            s += [{"shape": "rect", "x": 24 - w / 2, "y": 18, "w": w, "h": 2}, C(24, 19, 3)]
        v.append(("d", s))
    # e) bowl from above = thick ring; ring opens at the bottom into the point (a pin drawn as a stadium bowl)
    for t, gap, dot in itertools.product([5, 6, 7], [0, 2], [3, 5]):
        s = T.pin_shapes(24, 19, 17, 46) + [C(24, 19, 17 - t, "cut"), C(24, 19, dot)]
        if gap:
            s += [{"shape": "rect", "x": 24 - gap / 2, "y": 30, "w": gap, "h": 18, "op": "cut"}]
        v.append(("e", s))
    return v


# ------------------------------------------------------------------ D4 Convergence / Bracket Crest
def d4_variants():
    v = []
    # a) solid shield, bracket carved as negative lines
    for w, sp, j, tiers in itertools.product([3, 4], [8, 10], [20, 24], [1, 2]):
        v.append(("a", [shield()] + bracket_cuts(w=w, spread=sp, join=j, tiers=tiers)))
    # b) stepped crest: the silhouette IS a bracket (tiers narrow toward the final)
    for g, steps in itertools.product([2, 3], [3, 4]):
        s, y, ww = [], 4, 40
        h = (34 - g * (steps - 1)) / steps
        for i in range(steps):
            s.append({"shape": "rect", "x": 24 - ww / 2, "y": y, "w": ww, "h": h})
            y += h + g
            ww -= 40 / (steps + 1)
        s.append({"shape": "polygon", "points": [[24 - ww / 2 - 2, y - g], [24 + ww / 2 + 2, y - g], [24, 46]]})
        s.append({"shape": "rect", "x": 23, "y": 4, "w": 2, "h": 44, "op": "cut"})
        v.append(("b", s))
    # c) positive bracket strokes whose outer contour is a crest
    for w, sp in itertools.product([5, 6, 7], [12, 14, 16]):
        s = []
        for sx in (-1, 1):
            s += [{"shape": "rect", "x": 24 + sx * sp - w / 2, "y": 4, "w": w, "h": 18},
                  {"shape": "stroke", "a": [24 + sx * sp, 21], "b": [24, 33], "w": w, "extend": w / 2}]
        s += [{"shape": "rect", "x": 24 - w / 2, "y": 30, "w": w, "h": 16}]
        v.append(("c", s))
    # d) converging paths into a seal: two chevrons meeting at a point inside a disc (verified)
    for t, ang in itertools.product([4, 5], [30, 38, 46]):
        s = [C(24, 24, 22)]
        for sx in (-1, 1):
            x0 = 24 + sx * 14
            s.append({"shape": "stroke", "a": [x0, 6], "b": [24, 6 + 18 * math.tan(math.radians(90 - ang)) / 2], "w": t, "op": "cut", "extend": 2})
        s.append({"shape": "rect", "x": 24 - t / 2, "y": 22, "w": t, "h": 30, "op": "cut"})
        v.append(("d", s))
    # e) shield of two halves (two sides meet) with the final as the centre seam + a top bracket bar
    for gap, bar in itertools.product([2, 3, 4], [0, 4]):
        s = [shield(), {"shape": "rect", "x": 24 - gap / 2, "y": 4 + bar + (2 if bar else 0), "w": gap, "h": 44, "op": "cut"}]
        if bar:
            s.append({"shape": "rect", "x": 6, "y": 6 + bar, "w": 36, "h": gap, "op": "cut"})
        v.append(("e", s))
    return v


# ------------------------------------------------------------------ D6 Centre Light
def d6_variants():
    v = []
    # a) centre circle split by the halfway line, centre spot
    for t, gap, dot in itertools.product([6, 8, 10], [3, 4, 6], [4, 6]):
        v.append(("a", [{"shape": "ring", "cx": 24, "cy": 24, "r": 21, "width": t},
                        {"shape": "rect", "x": 24 - gap / 2, "y": 0, "w": gap, "h": 48, "op": "cut"}, C(24, 24, dot)]))
    # b) crowd: segmented ring (the gathering) + spot
    for n, t in itertools.product([4, 6, 8, 12], [6, 8]):
        s = [{"shape": "ring", "cx": 24, "cy": 24, "r": 21, "width": t}]
        s.append({"shape": "rect", "x": 22.5, "y": 0, "w": 3, "h": 12, "op": "cut", "repeat": {"count": n, "rotate": 360 / n, "about": [24, 24]}})
        s.append(C(24, 24, 5))
        v.append(("b", s))
    # c) floodlight beams: a spot under nested arcs opening downward (light falling on the centre)
    for n, t in itertools.product([2, 3], [4, 5]):
        s = [C(24, 34, 5)]
        r = 12
        for i in range(n):
            s.append({"shape": "arc", "cx": 24, "cy": 34, "r": r + t, "width": t, "start": 200, "end": 340})
            r += t + 3
        v.append(("c", s))
    # d) disc with the centre circle carved, halfway line carved, spot remains (pitch centre negative)
    for t, line in itertools.product([3, 4], [2, 3]):
        v.append(("d", [C(24, 24, 22), {"shape": "ring", "cx": 24, "cy": 24, "r": 13, "width": t, "op": "cut"},
                        {"shape": "rect", "x": 24 - line / 2, "y": 0, "w": line, "h": 48, "op": "cut"}, C(24, 24, 4)]))
    # e) two half-discs (two sides) facing, spot between (kick-off)
    for gap, dot in itertools.product([6, 8, 10], [3, 4]):
        v.append(("e", [C(24, 24, 22), {"shape": "rect", "x": 24 - gap / 2, "y": 0, "w": gap, "h": 48, "op": "cut"},
                        C(24, 24, gap / 2 + 2.5, "cut"), C(24, 24, dot)]))
    return v


def wm_variants(which):
    v = []
    if which == "D1":
        for top, fb, base in itertools.product([28, 36, 44], [True, False], [76, 84]):
            fa = partial(T.d1_A, top=top, base=base)
            g, _ = T.word([fa, T.d1_R, partial(T.d1_E, float_bar=fb), T.d1_N, fa], [5, 11, 15, 4])
            v.append((f"t{top}b{base}{'F' if fb else ''}", g))
    if which == "D2":
        for c, w in itertools.product([10, 15, 20], [48, 54, 58]):
            fa = partial(T.d2_A, c=c, w=w)
            g, _ = T.word([fa, partial(T.d2_R, c=c), T.d2_E, T.d2_N, fa], [6, 6, 7, 6])
            v.append((f"c{c}w{w}", g))
    if which == "D5":
        for w, c2 in itertools.product([72, 80, 88], ["pin", "o"]):
            g, _ = T.word([partial(T.d5_A, w=w), T.d5_R, T.d5_E, T.d5_N, partial(T.d5_A, w=w, counter=c2)], [6, 9, 12, 6])
            v.append((f"w{w}{c2}", g))
    return v


def tile(shapes, grid, label, px=200, pad=0.12):
    p = A.build_shapes(shapes, grid)
    x0, y0, x1, y1 = p.bounds
    s = B.svg(B.d_of(p), (0, 0, grid, grid) if grid == 48 else p.bounds, pad=(grid if grid == 48 else (x1 - x0)) * pad)
    f = os.path.join(TMP, label + ".png")
    w = px if grid == 48 else px * 2
    open(f, "wb").write(bytes(resvg_py.svg_to_bytes(svg_string=s, width=w, background="#ffffff")))
    return f


def sheet(name, items, grid, cols):
    files = []
    for i, (fam, s) in enumerate(items):
        lab = f"{name}_{i+1:02d}_{fam}"
        files.append((tile(s, grid, lab), lab))
    args = ["montage"]
    for f, lab in files:
        args += [f]  # no labels or file names on the sheets
    args += ["-tile", f"{cols}x", "-geometry", "+10+10", "-background", "#f3efe7",
             os.path.join(OUT, f"{name}_contact_sheet.png")]
    subprocess.run(args, check=True)
    return len(files)


n3 = sheet("D4_Symbol_LivePin", d3_variants(), 48, 10)
n4 = sheet("D5_Symbol_ConvergenceCrest", d4_variants(), 48, 10)
n6 = sheet("D7_Symbol_CentreLight", d6_variants(), 48, 10)
n1 = sheet("D1_Wordmark_CourtLines", wm_variants("D1"), 100, 3)
n5 = sheet("D6_Lockup_Integrated", wm_variants("D5"), 100, 3)
print(n1, n3, n4, n5, n6)
