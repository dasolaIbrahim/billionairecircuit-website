"""System sheet per direction: core mark in 3 circle modes, 3 lockups, 6 poses (= ARENA's statuses).

D7 uses its own pixel poses (pixel_sheet.py). The others get status poses constructed in their own geometry:
a status badge knocked into the mark's shoulder (Offset Path + Minus Front), square or round to match the mark's
corner logic.

    python3 system_sheet.py [D1_... D2_...]
"""
import json
import os
import re
import sys

import pathops
import resvg_py

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arena_build as A  # noqa: E402
import build_logo as B  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "04_Directions")
SIGNAL = "#E5484D"
STYLE = {"D1": "square", "D2": "square", "D3": "round", "D4": "square", "D5": "round", "D6": "round"}
POSES = [("available", "courts free near you"), ("live", "people are playing now"), ("booked", "you're in"),
         ("closed", "unavailable"), ("full", "fully booked"), ("ask", "'nearest 5-a-side?'")]


def P(d):
    p = pathops.Path()
    from fontTools.svgLib.path import parse_path
    parse_path(d, p.getPen())
    return p


def badge(kind, style, cx, cy, r):
    """Returns (badge path, cut-inside path) in mark units."""
    sq = style == "square"
    body = A.build_shapes([{"shape": "rect", "x": cx - r, "y": cy - r, "w": 2 * r, "h": 2 * r, "r": 0}] if sq else
                          [{"shape": "circle", "cx": cx, "cy": cy, "r": r}], 1)
    w = r * 0.36
    inner = []
    if kind == "booked":
        inner = [{"shape": "stroke", "a": [cx - r * .5, cy + r * .02], "b": [cx - r * .12, cy + r * .4], "w": w, "extend": w / 2},
                 {"shape": "stroke", "a": [cx - r * .12, cy + r * .4], "b": [cx + r * .55, cy - r * .38], "w": w, "extend": w / 2}]
    elif kind == "closed":
        inner = [{"shape": "rect", "x": cx - r * .55, "y": cy - w / 2, "w": r * 1.1, "h": w}]
    elif kind == "full":
        inner = [{"shape": "stroke", "a": [cx - r * .45, cy - r * .45], "b": [cx + r * .45, cy + r * .45], "w": w},
                 {"shape": "stroke", "a": [cx - r * .45, cy + r * .45], "b": [cx + r * .45, cy - r * .45], "w": w}]
    elif kind == "ask":
        if sq:
            inner = [{"shape": "rect", "x": cx - r * .45, "y": cy - r * .62, "w": r * .9, "h": w},
                     {"shape": "rect", "x": cx + r * .45 - w, "y": cy - r * .62, "w": w, "h": r * .55},
                     {"shape": "rect", "x": cx - w / 2, "y": cy - r * .2, "w": r * .45 + w / 2, "h": w},
                     {"shape": "rect", "x": cx - w / 2, "y": cy - r * .2, "w": w, "h": r * .35},
                     {"shape": "rect", "x": cx - w / 2, "y": cy + r * .35, "w": w, "h": w}]
        else:
            inner = [{"shape": "arc", "cx": cx, "cy": cy - r * .25, "r": r * .42, "width": w, "start": 170, "end": 400},
                     {"shape": "rect", "x": cx - w / 2, "y": cy - r * .05, "w": w, "h": r * .3},
                     {"shape": "circle", "cx": cx, "cy": cy + r * .55, "r": w * .55}]
    cut = A.build_shapes(inner, 1) if inner else pathops.Path()
    return body, cut


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def sheet(key):
    D = os.path.join(ROOT, key)
    b = os.path.join(D, "build")
    info = json.load(open(os.path.join(b, "build.json")))
    p = info["palette"]
    ink, paper, acc, neu = p["ink"], p["paper"], p["accent"], p["neutral"]
    style = STYLE[key[:2]]
    rec = json.load(open(os.path.join(D, "recipe.json")))
    base = A.build_shapes(rec["mark"], rec.get("grid", 48))
    accp = A.build_shapes(rec["accent"], rec.get("grid", 48)) if rec.get("accent") else pathops.Path()
    if rec.get("accent") and rec.get("accent_halo"):
        hal = A.build_shapes([dict(c, r=c["r"] + rec["accent_halo"]) for c in rec["accent"]], 48)
        base = pathops.op(base, hal, pathops.PathOp.DIFFERENCE)
    x0, y0, x1, y1 = pathops.simplify(A.union(base, accp)).bounds
    mw, mh = x1 - x0, y1 - y0

    def mark_g(x, y, size, fg, ac, pose=None, fit=0.62):
        # place the mark box (plus room for a badge) into a size x size square
        s = size * fit / max(mw, mh)
        bx = x + (size - mw * s) / 2 - x0 * s
        by = y + (size - mh * s) / 2 - y0 * s
        layers = []
        bpath, acc_l, col = base, accp, fg
        if pose and pose != "available":
            r = max(mw, mh) * 0.16
            cx, cy = x1 - r * 0.35, y0 + r * 0.35
            if key.startswith("D3"):  # the live light already sits on the shoulder: the badge replaces it
                acc_l = pathops.Path()
                cx, cy = rec["accent"][0]["cx"], rec["accent"][0]["cy"]
                r = rec["accent"][0]["r"] * 1.25
            halo = A.build_shapes([{"shape": "rect", "x": cx - r - 1.6, "y": cy - r - 1.6, "w": 2 * r + 3.2, "h": 2 * r + 3.2}] if style == "square"
                                  else [{"shape": "circle", "cx": cx, "cy": cy, "r": r + 1.6}], 1)
            bpath = pathops.op(base, halo, pathops.PathOp.DIFFERENCE)
            acc_l = pathops.op(acc_l, halo, pathops.PathOp.DIFFERENCE)
            body, cut = badge(pose, style, cx, cy, r)
            bcol = {"live": ac, "booked": ac, "closed": neu, "full": SIGNAL, "ask": ac}[pose]
            if pose == "closed":
                col = neu
            if pose == "full":
                col = SIGNAL
            if pose == "live":
                body = pathops.op(body, A.build_shapes([{"shape": "rect", "x": cx - r * .3, "y": cy - r * .3, "w": r * .6, "h": r * .6}] if style == "square" else
                                                       [{"shape": "circle", "cx": cx, "cy": cy, "r": r * .38}], 1), pathops.PathOp.DIFFERENCE)
                body = pathops.op(body, A.build_shapes([{"shape": "rect", "x": cx - r * .16, "y": cy - r * .16, "w": r * .32, "h": r * .32}] if style == "square" else
                                                       [{"shape": "circle", "cx": cx, "cy": cy, "r": r * .2}], 1), pathops.PathOp.UNION)
            body = pathops.op(body, cut, pathops.PathOp.DIFFERENCE)
            layers.append((body, bcol))
        layers = [(bpath, col), (acc_l, ac if pose in (None, "available") else (ac if pose != "full" else SIGNAL))] + layers
        return f'<g transform="translate({bx:.2f} {by:.2f}) scale({s:.4f})">' + "".join(
            f'<path fill="{c}" d="{B.d_of(q)}"/>' for q, c in layers) + "</g>"

    def lockup_g(x, y, w, h, mode):
        svg = open(os.path.join(b, "lockup-colour.svg")).read()
        vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
        paths = re.findall(r'<path fill="([^"]+)" d="([^"]*)"/>', svg)
        s = min(w * 0.78 / vb[2], h * 0.42 / vb[3])
        tx = x + (w - vb[2] * s) / 2 - vb[0] * s
        ty = y + (h - vb[3] * s) / 2 - vb[1] * s
        out = []
        for c, d in paths:
            if mode == "dark":
                c = paper if c == ink else c
            elif mode == "accent":
                c = ink
            out.append(f'<path fill="{c}" d="{d}"/>')
        return f'<g transform="translate({tx:.2f} {ty:.2f}) scale({s:.4f})">{"".join(out)}</g>'

    W, H = 1560, 720
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="#D9D9D9"/>',
         f'<text x="28" y="52" font-family="Inter, sans-serif" font-weight="700" font-size="24" fill="#0B0D0E">ARENA: {esc(info["title"])} system ({key[:2]})</text>',
         f'<text x="28" y="76" font-family="Inter, sans-serif" font-size="13" fill="#0B0D0E">core mark in 3 modes | 6 poses = app statuses | lockups | tokens: ink {ink}, paper {paper}, accent {acc}, neutral {neu}, signal {SIGNAL} (fully booked only)</text>']
    dark_fg = paper
    for i, (bg, fg, ac) in enumerate([(ink, dark_fg, acc), (acc, ink, ink), (paper, ink, acc)]):
        cx = 143 + i * 254
        o.append(f'<circle cx="{cx}" cy="206" r="115" fill="{bg}"/>' + mark_g(cx - 115, 206 - 115, 230, fg, ac))
    for i, (bg, mode) in enumerate([(ink, "dark"), (acc, "accent"), (paper, "light")]):
        y = 92 + i * 138
        o.append(f'<rect x="790" y="{y}" width="520" height="130" fill="{bg}"/>' + lockup_g(790, y, 520, 130, mode))
    for i, (n, note) in enumerate(POSES):
        x = 28 + i * 144
        o.append(f'<rect x="{x}" y="525" width="132" height="120" fill="{ink}"/>' + mark_g(x + 6, 525, 120, paper, acc, n, fit=0.6))
        o.append(f'<text x="{x+66}" y="662" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="#0B0D0E">{n}</text>')
        o.append(f'<text x="{x+66}" y="678" text-anchor="middle" font-family="Inter, sans-serif" font-size="10" fill="#55585c">{esc(note)}</text>')
    o.append("</svg>")
    s = "".join(o)
    open(os.path.join(D, f"{key[:2]}_system_sheet.svg"), "w").write(s)
    open(os.path.join(D, f"{key[:2]}_system_sheet.png"), "wb").write(bytes(resvg_py.svg_to_bytes(svg_string=s, width=W)))


if __name__ == "__main__":
    keys = sys.argv[1:] or [k for k in sorted(os.listdir(ROOT)) if k[:2] in STYLE]
    for k in keys:
        sheet(k)
        print("sheet", k)
