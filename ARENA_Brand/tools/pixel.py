"""D3 Pixel Scoreboard: a square-pixel pin mascot for ARENA, lit like a stadium LED scoreboard.
A 16 x 16 square-pixel pin mascot (unit = 2.75 on the 48 grid, about 29 px at 512), stepped diagonals, hard corners."""
U = 2.75
# head + stepped point, row: (x0, x1) inclusive, in pixel units on a 16 grid
PIN = {0: (5, 10), 1: (3, 12), 2: (2, 13), 3: (1, 14), 4: (1, 14), 5: (1, 14), 6: (1, 14), 7: (1, 14), 8: (2, 13),
       9: (2, 13), 10: (3, 12), 11: (4, 11), 12: (5, 10), 13: (6, 9), 14: (7, 8), 15: (7, 8)}
OY = 1  # rows start at pixel row 1


def px(x, y, w=1, h=1, op="add"):
    return {"shape": "rect", "x": x * U, "y": (y + OY) * U, "w": w * U, "h": h * U, "op": op}


def body():
    return [px(a, r, b - a + 1, 1) for r, (a, b) in PIN.items()]


# The inner location pin: the outer pin's own silhouette at about 3/7 scale (6 px wide, 6 rows tall against
# 14 x 16), centred on the head; replaces the two eye dots in the core mark and the idle / live poses.
INNER_PIN = [(6, 3, 4, 1), (5, 4, 6, 1), (5, 5, 6, 1), (5, 6, 6, 1), (6, 7, 4, 1), (7, 8, 2, 1)]

# faces: cut pixels (x, y, w, h); extras: added pixels outside the body
POSES = {
    "idle":    {"cut": INNER_PIN, "add": [], "note": "available: courts free near you"},
    "live":    {"cut": INNER_PIN, "add": [(14, 0, 1, 1), (15, -1, 1, 1), (13, -1, 1, 1)],
                "note": "live now: people are playing"},
    "happy":   {"cut": [(4, 6, 2, 1), (3, 5, 1, 1), (6, 5, 1, 1), (10, 6, 2, 1), (9, 5, 1, 1), (12, 5, 1, 1)], "add": [(14, -1, 1, 1), (13, 0, 3, 1)],
                "note": "booked: you're in"},
    "sleep":   {"cut": [(3, 6, 3, 1), (10, 6, 3, 1)], "add": [(14, -1, 2, 1), (15, 0, 1, 1), (14, 1, 2, 1)], "note": "closed: unavailable"},
    "booked":  {"cut": [(4, 5, 1, 1), (5, 6, 1, 1), (4, 7, 1, 1), (6, 5, 1, 1), (6, 7, 1, 1), (9, 5, 1, 1), (10, 6, 1, 1), (11, 5, 1, 1), (9, 7, 1, 1), (11, 7, 1, 1)],
                "add": [], "note": "fully booked (the only use of signal red)"},
    "ask":     {"cut": [(6, 3, 4, 1), (9, 4, 1, 2), (7, 6, 2, 1), (7, 7, 1, 1), (7, 9, 1, 1)], "add": [], "note": "ask: 'nearest 5-a-side?'"},
}


def pose(name):
    p = POSES[name]
    s = body() + [px(*c, op="cut") for c in p["cut"]]
    acc = [px(*a) for a in p["add"]]
    return s, acc
