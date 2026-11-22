"""Phase 4: the six ARENA directions as recipes, built with arena_build.py into 04_Directions/<D>/build.

    python3 directions.py
"""
import json
import os
import sys
from functools import partial

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arena_build as A  # noqa: E402
import letters as T  # noqa: E402
import sketches_lib as S  # noqa: E402
import pixel as PX  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "04_Directions")


def letter_mark(fn, cap_to=40, grid=48, **kw):
    """One constructed letter, scaled from the 100-unit cap grid onto the 48 grid, centred (optically: 0.5 unit up)."""
    shapes, w = fn(0, **kw)
    sc = cap_to / 100
    ox, oy = (grid - w * sc) / 2, (grid - cap_to) / 2 - 0.5
    return [{"shape": "group", "items": scale_shapes(shapes, sc, ox, oy)}]


def scale_shapes(shapes, sc, ox, oy):
    out = []
    for s in shapes:
        s = dict(s)
        k = s["shape"]
        if k == "group":
            s["items"] = scale_shapes(s["items"], sc, ox, oy)
        elif k == "rect":
            s.update(x=s["x"] * sc + ox, y=s["y"] * sc + oy, w=s["w"] * sc, h=s["h"] * sc)
            if "r" in s:
                s["r"] *= sc
        elif k in ("circle", "ring", "arc"):
            s.update(cx=s["cx"] * sc + ox, cy=s["cy"] * sc + oy, r=s["r"] * sc)
            if "width" in s:
                s["width"] *= sc
        elif k == "polygon":
            s["points"] = [[x * sc + ox, y * sc + oy] for x, y in s["points"]]
        out.append(s)
    return out


D = {}

# D1 ----------------------------------------------------------------------------------------------------------
w1, _ = T.word([T.d1_A, T.d1_R, partial(T.d1_E, float_bar=None), T.d1_N, T.d1_A], [5, 11, 15, 8])
eb = [s for s in T.d1_E(5 + 80 + 11 + 68)[0]][-1]  # the floating bar of E, drawn as the accent
D["D1_Wordmark_CourtLines"] = {
    "name": "ARENA", "kind": "wordmark", "title": "Court Lines",
    "idea": "ARENA drawn with the court's own geometry: the A is the trapezoid key, its crossbar the free-throw line; the E's middle arm floats free like a painted lane line.",
    "grid": 48, "mark": letter_mark(T.d1_A),
    "wordmark_shapes": {"grid": 100, "cap": 100, "shapes": w1, "accent": [eb]},
    "lockup": {"mode": "word"},
    "palette": {"ink": "#0E0E12", "paper": "#F3EEE4", "accent": "#C8553D", "neutral": "#8C8579", "tint": "#E6DFD2"},
}

# D2 ----------------------------------------------------------------------------------------------------------
fa2 = partial(T.d2_A, c=15, w=58)
w2, _ = T.word([fa2, partial(T.d2_R, c=15), T.d2_E, T.d2_N, fa2], [6, 6, 7, 6])
def centred_glyph(text, font, weight, size, grid=48, mirror=False):
    """An OFL glyph outlined and centred on the grid by its ink box (two passes: build, measure, place)."""
    g = {"shape": "glyph", "text": text, "font": font, "weight": weight, "x": 0, "y": 0, "cap": size}
    x0, y0, x1, y1 = A.build_shapes([g], grid).bounds
    return [dict(g, x=(grid - (x1 - x0)) / 2 - x0, y=(grid - (y1 - y0)) / 2 - y0, **({"mirror": "x"} if mirror else {}))]


D["D2_Wordmark_MatchDay"] = {
    "name": "ARENA", "kind": "wordmark", "title": "Match Day",
    "idea": "Poster-weight extended lowercase in Syne ExtraBold: loud like a match-day poster. Each a has its counter filled and a location pin carved into the optical centre of the bowl; both a's match, so the word reads clean and symmetrical around the pins.",
    "grid": 48, "mark": centred_glyph("a", "Syne", 800, 29), "mark_pin_counter": {"style": "enclosed", "head": 0.32, "lift": 0.18},
    "wordmark": {"text": "arena", "font": "Syne", "weight": 800, "tracking": -20, "pin_counters": {"style": "enclosed", "head": 0.32, "lift": 0.18}},
    "lockup": {"mode": "word"},
    "palette": {"ink": "#15121C", "paper": "#F1EADB", "accent": "#1F9D63", "neutral": "#8E8798", "tint": "#D7EEDF"},
}

# D3 ----------------------------------------------------------------------------------------------------------
D["D4_Symbol_LivePin"] = {
    "name": "ARENA", "kind": "symbol", "title": "Live Pin",
    "idea": "A map pin whose head is a stadium seen from above (the racetrack shape geometry literally calls a 'stadium'), with a live light switched on at its shoulder: there's a game near you, and it's on now.",
    "grid": 48,
    "mark": T.pin_shapes(24, 20, 17, 46.5) + [S.stadium(24, 20, 26, 17, "cut"), S.stadium(24, 20, 17, 8)],
    "accent": [{"shape": "circle", "cx": 38.5, "cy": 7.5, "r": 4.25}], "accent_halo": 2.25,
    "wordmark": {"text": "ARENA", "font": "Bricolage Grotesque", "weight": 700, "tracking": 10},
    "lockup": {"mark_scale": 1.75, "gap": 0.55},
    "palette": {"ink": "#0F3B2B", "paper": "#F3F1EA", "accent": "#22E27A", "neutral": "#6F8A7E", "tint": "#DCE8E1"},
}

# D4 ----------------------------------------------------------------------------------------------------------
D["D5_Symbol_ConvergenceCrest"] = {
    "name": "ARENA", "kind": "symbol", "title": "Convergence Crest",
    "idea": "A tournament bracket (four entrants, two semis, one final) carved into a shield: everyone meets here, the path resolves to one winner, and the venue is verified.",
    "grid": 48,
    "mark": [S.shield(top=5, w=38, sh=21, tip=46.5)] + S.bracket_cuts(top=10.5, w=3.5, spread=10, join=27, tiers=2, bottom=47),
    "wordmark": {"text": "ARENA", "font": "Archivo", "weight": 800, "tracking": 40},
    "lockup": {"mark_scale": 1.7, "gap": 0.6},
    "palette": {"ink": "#0F2340", "paper": "#F2EEE5", "accent": "#C9A24A", "neutral": "#8691A3", "tint": "#E3E6EC"},
}

# D5 ----------------------------------------------------------------------------------------------------------
pinA = partial(T.d5_A, w=80)
w5, wid5 = T.word([pinA, T.d5_R, T.d5_E, T.d5_N, partial(T.d5_A, w=80, counter="o")], [6, 8, 9, 6])
x_lastA = wid5 - 80
D["D6_Lockup_Integrated"] = {
    "name": "ARENA", "kind": "integrated", "title": "Pin in the A",
    "idea": "The first A's counter is a map pin standing on the A's crossbar (find); the last A's counter holds the live light (play). Find it, then it's on: one word, the whole product.",
    "grid": 48, "mark": letter_mark(pinA),
    "wordmark_shapes": {"grid": 100, "cap": 100, "shapes": w5,
                        "accent": [{"shape": "circle", "cx": x_lastA + 40, "cy": 42, "r": 8}]},
    "lockup": {"mode": "integrated"},
    "palette": {"ink": "#0E0E12", "paper": "#F3EEE4", "accent": "#4B2BFF", "neutral": "#8A86A0", "tint": "#E4E0F7"},
}

# D6 ----------------------------------------------------------------------------------------------------------
D["D7_Symbol_CentreLight"] = {
    "name": "ARENA", "kind": "symbol", "title": "Centre Light",
    "idea": "The centre circle seen from the floodlight gantry: two halves split by the halfway line, gathered around the spot where every game starts, and the spot is lit.",
    "grid": 48,
    "mark": [{"shape": "ring", "cx": 24, "cy": 24, "r": 21.5, "width": 10},
             {"shape": "rect", "x": 21, "y": 0, "w": 6, "h": 48, "op": "cut"}],
    "accent": [{"shape": "circle", "cx": 24, "cy": 24, "r": 5}],
    "wordmark": {"text": "ARENA", "font": "Sora", "weight": 600, "tracking": 30},
    "lockup": {"mark_scale": 1.6, "gap": 0.6},
    "palette": {"ink": "#0B1020", "paper": "#EEF1F5", "accent": "#58C7FF", "neutral": "#7D8698", "tint": "#DCE6F0"},
}

# D7 ----------------------------------------------------------------------------------------------------------
_s, _a = PX.pose("live")
D["D3_Pixel_Scoreboard"] = {
    "name": "ARENA", "kind": "symbol", "title": "Pixel Scoreboard",
    "idea": "A square-pixel pin mascot lit like a stadium LED scoreboard, with six poses that are the app's own statuses (available, live, booked, closed, fully booked, ask).",
    "grid": 48, "mark": _s, "accent": _a,
    "wordmark": {"text": "arena", "font": "Familjen Grotesk", "weight": 700, "tracking": -30, "dot": True, "dot_size": 0.2},
    "lockup": {"mark_scale": 1.9, "gap": 0.7},
    "palette": {"ink": "#0B0D0E", "paper": "#F2F5EE", "accent": "#B8FF2C", "neutral": "#1B1F21", "tint": "#E4E9DC",
                "signal": "#FF5A4F"},
}

if __name__ == "__main__":
    only = sys.argv[1:] or list(D)
    for k in only:
        d = os.path.join(ROOT, k)
        os.makedirs(d, exist_ok=True)
        json.dump(D[k], open(os.path.join(d, "recipe.json"), "w"), indent=1)
        r = A.build(D[k], os.path.join(d, "build"))
        print(k, r["mark_box"])
