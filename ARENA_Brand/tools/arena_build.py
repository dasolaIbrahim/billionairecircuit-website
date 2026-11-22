"""ARENA direction builder.

Extends make-logo's build_logo.py (same pathops boolean engine, same output files) with:
  * "path" shapes: hand-drawn cubic Beziers in grid units ({"shape": "path", "d": "M.. C.."})
  * "stroke" shapes: a straight painted line of width w between two points, flat caps (Illustrator: Outline Stroke)
  * custom-constructed wordmarks ("wordmark_shapes"), not only font-set ones
  * an accent layer ("accent": [...]) drawn in the palette accent for colour versions; it is unioned into the
    one-colour mark so the mono mark always works on its own
  * lockup modes: "mark+word" (default), "word" (wordmark-only directions), "integrated"

Writes into --out: mark.svg, mark-grid.svg, wordmark.svg, lockup.svg, lockup-stacked.svg, build.json (read by
make-logo's check_logo.py / logo_book.py / package_logo.py) plus mark-colour.svg, lockup-colour.svg,
construction.svg.

    python3 arena_build.py recipe.json --out build/D1
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ML = os.path.join(HERE, "..", "..", ".claude", "skills", "make-logo", "scripts")
sys.path.insert(0, os.path.abspath(ML))
import build_logo as B  # noqa: E402
import fonts as F  # noqa: E402
import pathops  # noqa: E402
from fontTools.pens.transformPen import TransformPen  # noqa: E402
from fontTools.svgLib.path import parse_path  # noqa: E402

FONTS = os.path.expanduser("~/.cache/make-logo/fonts")
_orig_shape_path = B.shape_path


def shape_path(s, grid, fonts_dir, m=(1, 0, 0, 1, 0, 0)):
    k = s["shape"]
    if k in ("path", "stroke"):
        if "rotate" in s:
            cx, cy = s.get("about") or (grid / 2, grid / 2)
            m = B.mul(B.rot(s["rotate"], cx, cy), m)
        if s.get("mirror") == "x":
            m = B.mul((-1, 0, 0, 1, grid, 0), m)
        d = B.Draw(m)
        if k == "path":
            parse_path(s["d"], TransformPen(d.pen, m))
            return pathops.simplify(d.path)
        (x0, y0), (x1, y1), w = s["a"], s["b"], s["w"]
        L = math.hypot(x1 - x0, y1 - y0)
        nx, ny = -(y1 - y0) / L * w / 2, (x1 - x0) / L * w / 2
        ext = s.get("extend", 0)
        ux, uy = (x1 - x0) / L * ext, (y1 - y0) / L * ext
        pts = [(x0 - ux + nx, y0 - uy + ny), (x1 + ux + nx, y1 + uy + ny), (x1 + ux - nx, y1 + uy - ny), (x0 - ux - nx, y0 - uy - ny)]
        d.move(pts[0]); [d.line(p) for p in pts[1:]]; d.close()
        return d.path
    if k == "group":  # a sub-recipe with its own op order, then treated as one shape
        acc = pathops.Path()
        for c in s["items"]:
            acc = pathops.op(acc, shape_path(c, grid, fonts_dir, m), B.OPS[c.get("op", "add")])
        return acc
    return _orig_shape_path(s, grid, fonts_dir, m)


B.shape_path = shape_path


def build_shapes(shapes, grid):
    return B.build_mark({"grid": grid, "mark": shapes}, FONTS)


def xform(path, m):
    out = pathops.Path()
    path.draw(TransformPen(out.getPen(), m))
    return out


def union(*ps):
    acc = pathops.Path()
    for p in ps:
        acc = pathops.op(acc, p, pathops.PathOp.UNION)
    return acc


def pin_counters(path, select=None, head=0.46, lift=0.0, style="through", tail=0.5, width=0.5):
    """style: "through" (pin cut through to the baseline), "tail" (keep the counter, grow a point from its base),
    "enclosed" (fill, carve a small pin inside the bowl), "side" (counter becomes a teardrop on its side)."""
    if style != "through":
        return _pin_styles(path, select, style, head, lift, tail, width)
    return _pin_through(path, select, head, lift)


def _holes(path):
    conts = list(path.contours)
    boxes = [c.bounds for c in conts]
    inside = lambda a, b: a[0] > b[0] and a[1] > b[1] and a[2] < b[2] and a[3] < b[3]
    return conts, boxes, [(i, j) for i, a in enumerate(boxes) for j, b in enumerate(boxes) if i != j and inside(a, b)]


def _pin_styles(path, select, style, head, lift, tail, width):
    import letters as T
    conts, boxes, holes = _holes(path)
    out = pathops.simplify(path)
    for i, j in holes:
        if select and not select(boxes[i]):
            continue
        hx0, hy0, hx1, hy1 = boxes[i]
        h, w = hy1 - hy0, hx1 - hx0
        cx, cy = (hx0 + hx1) / 2, (hy0 + hy1) / 2
        if style == "tail":
            # the counter keeps its own curve; a point grows from its base (a pin seen at a low angle)
            # tangents from the tip to the counter's ellipse (a = w/2, b = h/2): touch at y = b^2/d below centre
            a, b = w / 2, h / 2
            d = (hy1 + h * tail) - cy
            ty = b * b / d
            tx = a * (1 - (ty / b) ** 2) ** 0.5
            tri = build_shapes([{"shape": "polygon", "points": [[cx - tx, cy + ty - 0.01], [cx + tx, cy + ty - 0.01], [cx, cy + d]]},
                                {"shape": "rect", "x": cx - tx, "y": cy, "w": 2 * tx, "h": ty}], 48)
            out = pathops.op(out, tri, pathops.PathOp.DIFFERENCE)
        elif style == "enclosed":
            out = pathops.op(out, conts[i], pathops.PathOp.UNION)  # fill the counter
            r = head * h
            pc = cy - lift * h
            # centre on the bowl (outer edge to the stem side of the counter), not on the counter, which in this
            # face sits toward the stem: the user found the pin "too far to the end of the letter"
            ox0, _, ox1, _ = boxes[j]
            stem_right = (ox1 - hx1) < (hx0 - ox0)
            cx = (ox0 + hx1) / 2 if stem_right else (hx0 + ox1) / 2
            out = pathops.op(out, build_shapes(T.pin_shapes(cx, pc, r, pc + r * 2.35), 48), pathops.PathOp.DIFFERENCE)
        elif style == "side":
            out = pathops.op(out, conts[i], pathops.PathOp.UNION)
            r = h * 0.5
            # teardrop on its side: round end away from the stem, point toward it
            stem_right = boxes[j][2] - hx1 < hx0 - boxes[j][0]
            ccx = hx0 + r if stem_right else hx1 - r
            tipx = hx1 if stem_right else hx0
            l, rr = T.tangent_pin(0, 0, r, abs(tipx - ccx))
            pts = [[ccx + (l[1] if stem_right else -l[1]), cy + l[0]], [ccx + (rr[1] if stem_right else -rr[1]), cy + rr[0]], [tipx, cy]]
            out = pathops.op(out, build_shapes([{"shape": "circle", "cx": ccx, "cy": cy, "r": r}, {"shape": "polygon", "points": pts}], 48), pathops.PathOp.DIFFERENCE)
    return pathops.simplify(out)


def _pin_through(path, select=None, head=0.46, lift=0.0):
    """Fill a letter's counter and carve a location pin in its place, the pin's point running down through the
    bowl to the baseline (Illustrator: Pathfinder Unite the counter away, then Minus Front a circle+tangent
    triangle). `select(hole_bbox) -> bool` picks which counters (holes) to treat; default all."""
    import letters as T
    conts = [c for c in path.contours]
    boxes = [c.bounds for c in conts]

    def inside(a, b):
        return a[0] > b[0] and a[1] > b[1] and a[2] < b[2] and a[3] < b[3]

    holes = [(i, j) for i, a in enumerate(boxes) for j, b in enumerate(boxes) if i != j and inside(a, b)]
    keep, pins = pathops.Path(), []
    drop = set()
    for i, j in holes:
        if select and not select(boxes[i]):
            continue
        drop.add(i)
        hx0, hy0, hx1, hy1 = boxes[i]
        h = hy1 - hy0
        cx, cy = (hx0 + hx1) / 2, (hy0 + hy1) / 2 - lift * h
        r = head * h
        bottom = boxes[j][3] + 2
        pins.append(build_shapes(T.pin_shapes(cx, cy, r, bottom), 48))
    # rebuild: every contour except the dropped holes, unioned with nonzero fill -> the counters fill in
    for i, c in enumerate(conts):
        if i in drop:
            continue
        if any(i == hi for hi, _ in holes if hi not in drop):
            continue
        keep = pathops.op(keep, c, pathops.PathOp.UNION)
    for i, c in enumerate(conts):  # put back the holes we didn't select
        if i not in drop and any(i == hi for hi, _ in holes):
            keep = pathops.op(keep, c, pathops.PathOp.DIFFERENCE)
    for p in pins:
        keep = pathops.op(keep, p, pathops.PathOp.DIFFERENCE)
    return pathops.simplify(keep)


def svg_multi(layers, box, pad=0.0):
    x0, y0, x1, y1 = box
    w, h = x1 - x0 + 2 * pad, y1 - y0 + 2 * pad
    body = "".join(f'<path fill="{c}" d="{B.d_of(p)}"/>' for p, c in layers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0 - pad:.2f} {y0 - pad:.2f} {w:.2f} {h:.2f}" '
            f'width="{w:.2f}" height="{h:.2f}">{body}</svg>\n')


def build(spec, out):
    os.makedirs(out, exist_ok=True)
    g = spec.get("grid", 48)
    pal = spec["palette"]
    base = build_shapes(spec["mark"], g)
    acc = build_shapes(spec["accent"], g) if spec.get("accent") else pathops.Path()
    # The accent sits in a knocked-out gap: cut a halo around it from the base (Illustrator: Offset Path + Minus Front)
    halo = spec.get("accent_halo", 0)
    if spec.get("accent") and halo:
        hal = build_shapes([dict(c, **({"r": c["r"] + halo} if c["shape"] == "circle" else {})) for c in spec["accent"]], g)
        base = pathops.op(base, hal, pathops.PathOp.DIFFERENCE)
    if "mark_pin_counter" in spec:
        base = pin_counters(base, **spec["mark_pin_counter"])
    mark = pathops.simplify(union(base, acc))
    mb = mark.bounds
    open(os.path.join(out, "mark.svg"), "w").write(B.svg(B.d_of(mark), mb))
    open(os.path.join(out, "mark-grid.svg"), "w").write(B.svg(B.d_of(mark), (0, 0, g, g)))
    open(os.path.join(out, "mark-colour.svg"), "w").write(svg_multi([(base, pal["ink"]), (acc, pal["accent"])], mb))
    result = {"name": spec["name"], "grid": g, "mark_box": [round(v, 3) for v in mb], "guides": B.guides(spec),
              "kind": spec.get("kind", "symbol")}

    # Wordmark: custom-built or font-set
    if "wordmark_shapes" in spec:
        ws = spec["wordmark_shapes"]
        wpath = build_shapes(ws["shapes"], ws.get("grid", 100))
        wacc = build_shapes(ws["accent"], ws.get("grid", 100)) if ws.get("accent") else pathops.Path()
        whalo = ws.get("accent_halo", 0)
        if ws.get("accent") and whalo:
            hal = build_shapes([dict(c, r=c["r"] + whalo) for c in ws["accent"] if c["shape"] == "circle"], ws.get("grid", 100))
            wpath = pathops.op(wpath, hal, pathops.PathOp.DIFFERENCE)
        cap = ws["cap"]
        # shift so the baseline is at y=0 (shapes are drawn y-down with baseline at y=cap)
        sh = (1, 0, 0, 1, 0, -cap)
        wbase, wacc = xform(wpath, sh), xform(wacc, sh)
        word = pathops.simplify(union(wbase, wacc))
        result["wordmark"] = {"text": "ARENA", "font": "custom-constructed", "weight": 0, "cap": cap,
                              "licence": "original drawing (no font outlines)", "reserved_names": []}
        result["fonts"] = {}
    else:
        wm = spec["wordmark"]
        info = F.fetch(wm["font"], FONTS)
        font = F.load(info, wm.get("weight", 500))
        text = wm["text"]
        if wm.get("mirror_last"):
            # Set all but the last letter, then the last letter reflected about its own ink box
            # (Illustrator: Reflect, vertical axis), placed after the rest with an optical gap in em/1000.
            t = F.set_text(font, text[:-1], wm.get("tracking", 0))
            wbase = pathops.Path()
            t["pen"].replay(TransformPen(wbase.getPen(), (1, 0, 0, -1, 0, 0)))
            last = F.set_text(font, text[-1], 0)
            lp = pathops.Path()
            last["pen"].replay(TransformPen(lp.getPen(), (1, 0, 0, -1, 0, 0)))
            lx0, _, lx1, _ = lp.bounds
            _, _, rx1, _ = pathops.simplify(wbase).bounds
            gap = wm.get("mirror_gap", 60) / 1000 * t["upem"]
            # reflect: x -> (lx0 + lx1) - x, then move so its left ink edge sits `gap` after the rest's right ink edge
            m = (-1, 0, 0, 1, (lx0 + lx1) - lx0 + rx1 + gap, 0)
            wbase = union(wbase, xform(lp, m))
        else:
            t = F.set_text(font, text, wm.get("tracking", 0))
            wbase = pathops.Path()
            t["pen"].replay(TransformPen(wbase.getPen(), (1, 0, 0, -1, 0, 0)))
        wbase = pathops.simplify(wbase)
        if "pin_counters" in wm:
            # only the counters of the first and last letters (the two a's in "arena")
            x0w, _, x1w, _ = wbase.bounds
            edge = (x1w - x0w) * wm["pin_counters"].get("edge", 0.2)
            sel = lambda b: b[2] < x0w + edge or b[0] > x1w - edge
            wbase = pin_counters(wbase, select=sel, **{k: v for k, v in wm["pin_counters"].items() if k != "edge"})
        wacc = pathops.Path()
        cap = t["cap"]
        if wm.get("dot"):  # a square full stop in the accent (pixel), sitting on the baseline
            sz = cap * wm.get("dot_size", 0.2)
            wacc = build_shapes([{"shape": "rect", "x": t["advance"] + cap * 0.06, "y": -sz, "w": sz, "h": sz}], 48)
        word = pathops.simplify(union(wbase, wacc))
        result["wordmark"] = {"text": wm["text"], "font": wm["font"], "weight": wm.get("weight", 500), "cap": cap,
                              "licence": info["licence"], "reserved_names": info["reserved_names"]}
        result["fonts"] = {wm["font"]: info["licence"]}
    open(os.path.join(out, "wordmark.svg"), "w").write(B.svg(B.d_of(word), word.bounds))
    open(os.path.join(out, "wordmark-colour.svg"), "w").write(svg_multi([(wbase, pal["ink"]), (wacc, pal["accent"])], word.bounds))

    lk = spec.get("lockup", {})
    mode = lk.get("mode", "mark+word")
    mx0, my0, mx1, my1 = mb
    wx0, wy0, wx1, wy1 = word.bounds
    if mode in ("word", "integrated"):
        layers_h = [(wbase, pal["ink"]), (wacc, pal["accent"])]
        lock = word
    else:
        mh = lk.get("mark_scale", 1.6) * cap
        sc = mh / (my1 - my0)
        gap = lk.get("gap", 0.7) * cap
        hm = (sc, 0, 0, sc, -mx0 * sc - (mx1 - mx0) * sc - gap, -cap / 2 - (my0 + (my1 - my0) / 2) * sc)
        lb, la = xform(base, hm), xform(acc, hm)
        lock = pathops.simplify(union(lb, la, word))
        layers_h = [(lb, pal["ink"]), (la, pal["accent"]), (wbase, pal["ink"]), (wacc, pal["accent"])]
    open(os.path.join(out, "lockup.svg"), "w").write(B.svg(B.d_of(lock), lock.bounds))
    open(os.path.join(out, "lockup-colour.svg"), "w").write(svg_multi(layers_h, lock.bounds))
    # Stacked
    sm_h = lk.get("stack_scale", 2.2) * cap
    ss = sm_h / (my1 - my0)
    smt = (ss, 0, 0, ss, (wx0 + wx1) / 2 - (mx0 + mx1) / 2 * ss, -cap - lk.get("stack_gap", 1.0) * cap - my1 * ss)
    sb, sa = xform(base, smt), xform(acc, smt)
    stack = pathops.simplify(union(sb, sa, word))
    open(os.path.join(out, "lockup-stacked.svg"), "w").write(B.svg(B.d_of(stack), stack.bounds))
    open(os.path.join(out, "lockup-stacked-colour.svg"), "w").write(
        svg_multi([(sb, pal["ink"]), (sa, pal["accent"]), (wbase, pal["ink"]), (wacc, pal["accent"])], stack.bounds))

    # Construction drawing: the grid, the recipe's keylines and circles, the mark in ink at 18% over the outline
    result.update({k: spec[k] for k in ("title", "idea", "palette", "traced_from", "rationale") if k in spec})
    construction(spec, mark, g, os.path.join(out, "construction.svg"))
    json.dump(result, open(os.path.join(out, "build.json"), "w"), indent=1)
    return result


def construction(spec, mark, g, path):
    S = 20  # px per grid unit
    W = g * S
    lines = []
    for i in range(0, g + 1):
        c = "#d9d6cf" if i % 4 else "#bdb8ad"
        lines.append(f'<line x1="{i*S}" y1="0" x2="{i*S}" y2="{W}" stroke="{c}" stroke-width="{1 if i % 4 else 1.4}"/>')
        lines.append(f'<line x1="0" y1="{i*S}" x2="{W}" y2="{i*S}" stroke="{c}" stroke-width="{1 if i % 4 else 1.4}"/>')
    key = []
    for s in spec["mark"] + spec.get("accent", []) + spec.get("keylines", []):
        if s["shape"] in ("circle", "ring", "arc") or s["shape"] == "keycircle":
            key.append(f'<circle cx="{s["cx"]*S}" cy="{s["cy"]*S}" r="{s["r"]*S}" fill="none" stroke="#e2462f" stroke-width="2"/>')
            if s["shape"] == "ring":
                key.append(f'<circle cx="{s["cx"]*S}" cy="{s["cy"]*S}" r="{(s["r"]-s["width"])*S}" fill="none" stroke="#e2462f" stroke-width="2"/>')
        if s["shape"] == "keyline":
            (x0, y0), (x1, y1) = s["a"], s["b"]
            key.append(f'<line x1="{x0*S}" y1="{y0*S}" x2="{x1*S}" y2="{y1*S}" stroke="#2b6cff" stroke-width="2" stroke-dasharray="8 6"/>')
    d = B.d_of(mark)
    body = (f'<g transform="scale({S})"><path d="{d}" fill="#0f1115" fill-opacity=".14" stroke="#0f1115" '
            f'stroke-width="{2.2/S}"/></g>')
    # anchor points
    pts = []
    for verb, p in mark:
        for (x, y) in p:
            pts.append(f'<rect x="{x*S-4}" y="{y*S-4}" width="8" height="8" fill="#fff" stroke="#0f1115" stroke-width="1.6"/>')
    svgs = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 {W+40} {W+40}" width="{W+40}" height="{W+40}">'
            f'<rect x="-20" y="-20" width="{W+40}" height="{W+40}" fill="#f6f4ef"/>{"".join(lines)}{body}{"".join(key)}'
            f'{"".join(pts[:400])}</svg>')
    open(path, "w").write(svgs)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("recipe")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    r = build(json.load(open(a.recipe)), a.out)
    print(f"built {r['name']} mark box {r['mark_box']}")
