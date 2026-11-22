"""Shape helpers shared by sketches.py and directions.py."""
import math


def C(cx, cy, r, op="add"):
    return {"shape": "circle", "cx": cx, "cy": cy, "r": r, "op": op}


def ellipse(cx, cy, rx, ry, op="add"):
    k = 0.5522847498
    d = (f"M{cx+rx} {cy} C{cx+rx} {cy+ry*k} {cx+rx*k} {cy+ry} {cx} {cy+ry} C{cx-rx*k} {cy+ry} {cx-rx} {cy+ry*k} {cx-rx} {cy} "
         f"C{cx-rx} {cy-ry*k} {cx-rx*k} {cy-ry} {cx} {cy-ry} C{cx+rx*k} {cy-ry} {cx+rx} {cy-ry*k} {cx+rx} {cy} Z")
    return {"shape": "path", "d": d, "op": op}


def stadium(cx, cy, w, h, op="add"):
    return {"shape": "rect", "x": cx - w / 2, "y": cy - h / 2, "w": w, "h": h, "r": min(w, h) / 2, "op": op}


def shield(top=6, w=36, sh=20, tip=46, cx=24):
    x0, x1 = cx - w / 2, cx + w / 2
    return {"shape": "path", "d": f"M{x0} {top} L{x1} {top} L{x1} {sh} C{x1} {sh+14} {cx+8} {tip-6} {cx} {tip} C{cx-8} {tip-6} {x0} {sh+14} {x0} {sh} Z"}


def bracket_cuts(cx=24, top=6, w=3.5, spread=10, join=20, tiers=1, bottom=46):
    s = []
    if tiers == 2:
        for sx in (-1, 1):
            a, b = cx + sx * (spread + 5), cx + sx * (spread - 5)
            s += [{"shape": "rect", "x": a - w / 2, "y": top - 1, "w": w, "h": 8, "op": "cut"},
                  {"shape": "rect", "x": b - w / 2, "y": top - 1, "w": w, "h": 8, "op": "cut"},
                  {"shape": "rect", "x": min(a, b) - w / 2, "y": top + 6, "w": abs(a - b) + w, "h": w, "op": "cut"},
                  {"shape": "rect", "x": cx + sx * spread - w / 2, "y": top + 6, "w": w, "h": join - top - 6, "op": "cut"}]
    else:
        for sx in (-1, 1):
            s += [{"shape": "rect", "x": cx + sx * spread - w / 2, "y": top - 1, "w": w, "h": join - top + 1, "op": "cut"}]
    s += [{"shape": "rect", "x": cx - spread - w / 2, "y": join - w, "w": 2 * spread + w, "h": w, "op": "cut"},
          {"shape": "rect", "x": cx - w / 2, "y": join - w, "w": w, "h": bottom - join + w - 6, "op": "cut"}]
    return s


