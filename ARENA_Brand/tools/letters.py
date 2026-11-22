"""Custom ARENA letterforms, constructed on a 100-unit cap grid (y down, baseline at y=100).

Each function returns shapes (arena_build recipe format) for one letter at x offset `x`, plus its advance width.
No font outlines are used: these are original drawings built from rectangles, polygons, circles and arcs.
"""
import math


def P(pts, op="add"):
    return {"shape": "polygon", "points": [[round(a, 3), round(b, 3)] for a, b in pts], "op": op}


def R(x, y, w, h, op="add", r=0):
    d = {"shape": "rect", "x": x, "y": y, "w": w, "h": h, "op": op}
    if r:
        d["r"] = r
    return d


# ---------------------------------------------------------------- D1 Court Lines (monoline, the basketball key)
S1 = 14.0  # stroke


def d1_A(x, top=36, base=80, bar=(56, 69)):
    """Flat-topped A: the old trapezoid key (paint) seen from above; the crossbar is the free-throw line."""
    t0, t1 = x + (base - top) / 2, x + (base + top) / 2
    k = (base - top) / 2 / 100  # run per unit height
    hs = S1 * math.sqrt(1 + k * k)
    xl = lambda y: t0 - k * y
    xr = lambda y: t1 + k * y
    out = [P([(x, 100), (t0, 0), (t1, 0), (x + base, 100)])]
    y0 = S1 - 1  # optically thinner top bar
    out.append(P([(xl(y0) + hs, y0), (xr(y0) - hs, y0), (xr(bar[0]) - hs, bar[0]), (xl(bar[0]) + hs, bar[0])], "cut"))
    out.append(P([(xl(bar[1]) + hs, bar[1]), (xr(bar[1]) - hs, bar[1]), (xr(101) - hs, 101), (xl(101) + hs, 101)], "cut"))
    return out, base


def d1_R(x):
    s = S1
    out = [R(x, 0, s, 100), R(x, 0, 30, s), R(x, 57 - s, 30, s),
           {"shape": "arc", "cx": x + 30, "cy": 28.5, "r": 28.5, "width": s, "start": -90, "end": 90},
           P([(x + 24, 57 - s + 2), (x + 24 + 15.5, 57 - s + 2), (x + 68, 100), (x + 52.5, 100)])]
    return out, 68


def d1_E(x, float_bar=True):
    s = S1
    out = [R(x, 0, s, 100), R(x, 0, 54, s - 1), R(x, 101 - s, 54, s - 1)]
    if float_bar is not None:
        out.append(R(x + (s + 7 if float_bar else 0), 43.5, 48 - (s + 7 if float_bar else 0), 13))
    return out, 54


def d1_N(x):
    s = S1
    return [R(x, 0, s, 100), R(x + 58, 0, s, 100), P([(x, 0), (x + s + 2.5, 0), (x + 72, 100), (x + 72 - s - 2.5, 100)])], 72


def d1_word(float_bar=True, gaps=(5, 11, 15, 4)):
    sh, x = [], 0
    for i, f in enumerate([d1_A, d1_R, lambda xx: d1_E(xx, float_bar), d1_N, d1_A]):
        s, w = f(x)
        sh += [dict(z) for z in s]
        x += w + (gaps[i] if i < 4 else 0)
    # cuts must apply only to their own letter: wrap each letter as a group
    return sh, x


def grouped(letters):
    """letters: list of (shapes) -> list of group shapes (cuts stay inside their letter)."""
    return [{"shape": "group", "items": s} for s in letters]


def word(fns, gaps):
    groups, x = [], 0
    for i, f in enumerate(fns):
        s, w = f(x)
        groups.append({"shape": "group", "items": s})
        x += w + (gaps[i] if i < len(gaps) else 0)
    return groups, x - (gaps[len(fns) - 1] if len(gaps) >= len(fns) else 0)


# ---------------------------------------------------------------- D2 Match Day (condensed jersey block)
def d2_A(x, w=54, st=19, c=15):
    return [P([(x, 100), (x, c), (x + c, 0), (x + w - c, 0), (x + w, c), (x + w, 100)]),
            P([(x + st, st + 2 + 6), (x + st + 6, st + 2), (x + w - st - 6, st + 2), (x + w - st, st + 2 + 6), (x + w - st, 50), (x + st, 50)], "cut"),
            R(x + st, 66, w - 2 * st, 40, "cut")], w


def d2_R(x, w=52, st=19, c=15):
    return [P([(x, 0), (x + w - c, 0), (x + w, c), (x + w, 44), (x + w - 7, 51), (x + w, 58), (x + w, 100),
               (x + w - st, 100), (x + w - st, 66), (x + st, 66), (x + st, 100), (x, 100)]),
            P([(x + st, st - 2), (x + w - st - 5, st - 2), (x + w - st, st + 3), (x + w - st, 49), (x + st, 49)], "cut")], w


def d2_E(x, w=42, st=19):
    return [R(x, 0, w, 100), R(x + st, 17, w, 25, "cut"), R(x + st, 58, w, 25, "cut"), R(x + w - 6, 42, 10, 16, "cut")], w


def d2_N(x, w=54, st=19):
    return [R(x, 0, w, 100),
            P([(x + st, 0), (x + w - st, 0), (x + w - st, 58)], "cut"),
            P([(x + st, 42), (x + w - st, 100), (x + st, 100)], "cut")], w


# ---------------------------------------------------------------- D5 Integrated (heavy arch letters, pin counter)
S5 = 21.0


def tangent_pin(cx, cy, r, tip_y):
    """Pin outline points: the two tangent points from the tip to the circle (Illustrator: Shape Builder of a
    circle and a triangle whose sides are tangent)."""
    d = tip_y - cy
    a = math.asin(r / d)
    # tangent point angle measured from the downward vertical
    th = math.pi / 2 - a
    tx = r * math.sin(th)
    ty = r * math.cos(th)
    return (cx - tx, cy + ty), (cx + tx, cy + ty)


def pin_shapes(cx, cy, r, tip_y, op="add"):
    l, rr = tangent_pin(cx, cy, r, tip_y)
    return [{"shape": "circle", "cx": cx, "cy": cy, "r": r, "op": op}, P([l, rr, (cx, tip_y)], op)]


def d5_A(x, w=80, counter="pin"):
    r = w / 2
    out = [R(x, r, w, 100 - r), {"shape": "circle", "cx": x + r, "cy": r, "r": r}]
    cr = r - S5
    if counter == "pin":
        out += [{"shape": "group", "op": "cut", "items": pin_shapes(x + r, r + 2, cr, 75)}]
    else:
        out += [{"shape": "circle", "cx": x + r, "cy": r + 2, "r": cr, "op": "cut"}]
    out += [R(x + S5, 84, w - 2 * S5, 20, "cut")]
    return out, w


def d5_R(x, w=70):
    s = S5
    br = 31
    return [R(x, 0, s, 100), R(x, 0, 38, 2 * br), {"shape": "circle", "cx": x + 38, "cy": br, "r": br},
            {"shape": "circle", "cx": x + 38, "cy": br, "r": br - s, "op": "cut"}, R(x + s, br - (br - s), 17, 2 * (br - s), "cut"),
            P([(x + 30, 2 * br - 6), (x + 52, 2 * br - 6), (x + w, 100), (x + w - 23, 100)])], w


def d5_E(x, w=54):
    s = S5
    return [R(x, 0, s, 100), R(x, 0, w, 19), R(x, 40.5, w - 6, 19), R(x, 81, w, 19)], w


def d5_N(x, w=76):
    s = S5
    return [R(x, 0, s, 100), R(x + w - s, 0, s, 100), P([(x, 0), (x + s + 4, 0), (x + w, 100), (x + w - s - 4, 100)])], w
