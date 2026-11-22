# ARENA: how professional designers build a logo, and how we reproduce it in code

Written 2026-11-22. Tutorial notes are in `01_Research/tutorial_notes/`.
This file drives the Python pipeline: shapely, skia-pathops, fontTools/uharfbuzz, svgpathtools, resvg and potrace.

---

## 1. Sources studied (and how much of each we could actually access)

| # | Source | What we accessed | What we learned |
|---|---|---|---|
| 1 | instagram.com/reel(s)/De9BI8gNCXi (@quigsart, 2026-10-26) | **Metadata and caption only.** Tried both /reel/ and /reels/. Video download blocked by the proxy: `scontent-ord5-2.cdninstagram.com` 403 "no rule or network setting allows this host". No captions exist. No frames. | Caption: "From photo to the final logo process", made in Illustrator. The method is reconstructed from the genre (see §2), not observed. |
| 2 | instagram.com/reel(s)/De5EVS_ySng (@quigsart, 2026-10-24) | Same as #1: metadata only, CDN blocked. | Same caption. A series: photo → silhouette → vector mark. |
| 3 | instagram.com/reel(s)/Df-5JMMjKiw (@griffinwooldridge1, 2026-11-21) | Metadata and full caption. Video blocked (same CDN host). | Promotes the design.how **make-logo** agent skill by Arlan Marat. |
| 4 | make-logo skill source: `.claude/skills/make-logo/` (installed copy of arla6ka/design.how `skills/make-logo`) | **Full text.** SKILL.md, references/building.md, measuring.md, distance.md and logo-book.md, plus the scripts build_logo.py, trace_ref.py, check_logo.py and measure_logo.py. | The complete pipeline: brief → references → measuring → calibrated distance → 6 grid-recipe directions → 16 px checks → logo book → package. **This is our strongest source.** |
| 5 | instagram.com/quigsart/reels/ (account listing) | Failed: HTTP 429 Too Many Requests. | — |
| 6 | YouTube (captions with `--write-auto-subs`) | **Blocked.** www.youtube.com CONNECT 403 from the proxy. | — |
| 7 | design.how, logogeek.uk, cursa.app, learn.scannerlicker.net (WebFetch) | **Blocked.** The hosts are not in the session's allowed domains. Only WebSearch result summaries were readable. | See rows 8-12. |
| 8 | Search summaries: Wikipedia "Overshoot (typography)"; Slate on Tobias Frere-Jones; TypeDrawers threads | Text snippets | Overshoot is about 1-3% of the height for O. Karow gives about 3% for O and 5% for A. Pointed shapes need more than round ones, and squarish rounds need less. |
| 9 | Search summaries: logogeek "Optical corrections every logo designer should know"; creativebloq on typographic optical illusions; uxdesign.cc "Ink traps and pals"; scannerlicker "Art of Eyeballing IV" | Text snippets | Horizontals look heavier than verticals, so they are drawn thinner. Ink traps go in acute junctions. |
| 10 | Search summaries: Tim Frame (CreativeLive) icon matrix; Ian Paget (Logo Geek) word mapping; cursa.app concept routes; SymbolFinder (CHI 2021 / UIST 2021, Columbia) | Text snippets | Word list → pairing matrix (attribute × object × action × shape system) → 20-40 rough ideas, each kept to one silhouette or two strokes → group by metaphor → filter. |
| 11 | Search summaries: tutvid "Bat logo with circular grid and golden ratio"; George Bokhua (Skillshare) golden-ratio gridding; Adobe Learn on Shape Builder and Pathfinder; Adobe Community "logo tips" | Text snippets | Golden circles: duplicate and divide W/H by 1.618 → Pathfinder Divide → delete faces. Shape Builder drag merges, Alt-drag deletes. Pathfinder results are permanent unless applied as shape modes. Caveat from an expert: "golden ratio is snake oil, construction from basic shapes is the real value". |
| 12 | Background knowledge from type-design practice (not fetched this session) | — | Used for the numbers in §6. These are the common studio heuristics; check every one by rendering. |

**Honesty note:** no video frame of any tutorial was seen. The proxy blocked every Instagram CDN host and YouTube. The reel breakdowns for #1 and #2 are reconstructions of the standard "photo → logo" Illustrator workflow, labelled as such.

---

## 2. Reel-by-reel method breakdowns

### Reels 1 and 2: @quigsart "From photo to the final logo process" (reconstructed, not observed)
1. Pick a reference photo with a strong silhouette: a side profile, high contrast and one dominant gesture.
2. Place it in Illustrator, set its opacity to 30-50% and lock it as an underlay.
3. Block out the major masses only. Use circles and ellipses for the curves (circle construction) and Pen-tool lines for the straights. Put anchors only at extrema (top, bottom, left and right of each curve), with handles horizontal or vertical.
4. Merge with Shape Builder (drag across the faces to keep, Alt-drag to delete) or Pathfinder Unite and Minus Front.
5. Turn internal detail into negative-space cuts of one constant width rather than strokes.
6. Make everything consistent: one gap width, one corner radius, one stroke weight. Snap to the grid.
7. Hide the photo and judge the black silhouette alone at 512 px and at 16-32 px.
8. Add the wordmark and lockup, then mockups.

**For ARENA:** photograph or trace a reference (a ball, a court diagram, a stadium bowl, a player's stride) → potrace it as a guide layer → **rebuild from primitives** → discard the trace.

### Reel 3: the design.how make-logo skill (read in full from source)
1. Ask once: name, what it does, ONE idea, 3-6 liked logos, where it will be used, colours, mark and/or wordmark.
2. Gather the client's references, about 100 craft references from Are.na, and a set from the product's own world.
3. Measure each reference: aspect, coverage, solidity, median stroke, stroke contrast, counters, symmetry, compactness, corners and centre offset.
4. Calibrate a distance model (IoU, edge distance, DCT hash) with a limit set where 10% of references hit their nearest neighbour.
5. Targets are the client's references' numbers within the Are.na spread. If the references disagree, ask the client.
6. Write six directions, each a different answer. Mix traced-and-changed, shape-built idea marks, and typographic marks, with at least half pictorial. Each is a JSON recipe on a 48-unit grid with integer or half-unit coordinates, using add, cut, keep or xor (pathops UNION, DIFFERENCE, INTERSECTION, XOR) plus rotate, mirror and repeat.
7. Check: stroke at 16 px ≥ 1.5 px; counters at 16 px match those at 512 px; ink/paper contrast ≥ 4.5:1 and accent ≥ 3:1; distance to the nearest reference under the limit.
8. Logo book: in use, construction grid (at most 5 guides per side), colour, sizes 16/24/32/64, side by side.
9. Package: SVG variants (ink, reversed, accent, black), PNGs from 16 to 1024 px, favicon.ico, licences, trademark sheet.

Doctrine: "Agents place shapes well and draw curves badly." Lead with ONE move made from 2-3 primitives. Literal pictograms read as stock icons. When a mark is too close to a reference, change the outline, not an inner detail. Use square terminals unless the curve is the idea.

---

## 3. The consolidated ARENA logo method

1. **Discovery brief.** Gather: product (local-sports discovery and booking), audience (casual players, parents, clubs), places it will be used (app icon first, map pins, web header, venue signage, kit), competitors, and 3-6 liked logos. Output: `02_Strategy/brief.json`.
2. **Strategy → attributes.** Pick 3-5 brand attributes with opposites, for example *local (not global), energetic (not aggressive), inclusive (not elite), instant (not bureaucratic), communal*. Write one positioning sentence.
3. **Word mapping.** For each attribute and for the noun "arena", list 10-15 associations in three columns: objects, actions and shapes (§7.1).
4. **Combination matrix.** Cross the columns: attribute × object × action × shape. Write each cell as a one-line visual metaphor, for example "a pin + a ball = place to play", or "a stadium bowl seen from above = an A", or "a court's centre line + a pin".
5. **Thumbnail volume.** Draw 30-40 ideas at thumbnail size (2-3 cm, or 64 px), each one silhouette with at most two moves. In code: quick primitive recipes rendered at 64 px on one contact sheet.
6. **Reduce** (§7.2). Cluster by metaphor, keep the best 6 from different clusters, and strip each to its fewest primitives.
7. **Measure references.** Use make-logo's `measure_logo.py` on the liked logos and on the sports or identity Are.na set. Set targets for stroke (about 59/1000 of height is the median), solidity and counters.
8. **Construct on a grid.** Use a 48-unit square, integer or half-unit coordinates, and circles with radii from one series (e.g. 24, 18, 12, 6, or the golden ratio φ: r, r/1.618, r/2.618). Build with boolean ops only: no freehand curves.
9. **Typography.** Pick a display or grotesk OFL face with character, shape it with HarfBuzz, outline it, track it, kern its pairs optically, and modify 1-2 letterforms. For ARENA the candidate letters are the A apex/crossbar and the R leg, and the shared shape is the repeated A-A rhythm "AR-NA".
10. **Optical correction pass** (§6): overshoot, thinned horizontals, crossbar height, optical centring, ink traps if the logo will be small.
11. **Lockups.** Horizontal (mark at about 1.6-2.0× cap height, gap about 0.6-0.8 cap height), stacked, mark-only, wordmark-only. Define clear space as the cap height of the A (or the stroke width × 2).
12. **Test.**
    - Render at 16/24/32/64/512 px with resvg.
    - Stroke at 16 px ≥ 1.5 px. Counters must survive.
    - Contrast: ink ≥ 4.5:1, accent ≥ 3:1.
    - Reversed (white on dark), one-colour, and on a photo.
    - Distance check against references.
    - Squint test (blur σ = 2-4 px): it should still read.
13. **Refine.** Fix anchors, merge collinear points, snap to the grid, and re-run the tests. Iterate on the outline, not on decoration.
14. **System.** Palette (ink, paper, accent, neutral, tint), type pairing, icon style derived from the mark's geometry (same stroke, radius and terminals), patterns (repeat or crop the mark), motion (how the mark assembles).
15. **Guidelines and package.** Construction page, clear space, minimum sizes (e.g. mark 16 px or 6 mm, lockup 80 px), misuse examples, SVG/PNG/ICO exports, licences.

---

## 4. Illustrator action → Python / Inkscape equivalent

Common setup:
```python
import shapely, pathops, math
from shapely.geometry import Point, Polygon, LineString, box, MultiPolygon
from shapely.ops import unary_union, polygonize
from shapely import affinity
```
Use shapely for geometry thinking (buffers, offsets, faces). Use skia-pathops for exact bezier booleans on font or potrace curves. Convert at the boundaries: flatten curves to polygons with ≥ 64 segments per quarter circle, or keep everything in pathops when curves must stay as true beziers.

| # | Illustrator action | Python / Inkscape equivalent | Snippet |
|---|---|---|---|
| 1 | Ellipse tool (circle on grid) | shapely Point.buffer, or a pathops path with 4 cubic arcs (k = 0.5523) | `c = Point(24,24).buffer(20, quad_segs=64)` |
| 2 | Rectangle / Rounded Rectangle | `box()` then round the corners | `r = box(4,4,44,44).buffer(-6).buffer(6, join_style="round")` |
| 3 | Pathfinder Unite / Shape Builder merge | `unary_union` / `pathops.op(a,b,UNION)` | `u = unary_union([a,b])`; `pathops.op(pa,pb,pathops.PathOp.UNION)` |
| 4 | Pathfinder Minus Front | difference | `a.difference(b)`; `pathops.op(pa,pb,pathops.PathOp.DIFFERENCE)` |
| 5 | Pathfinder Intersect | intersection | `a.intersection(b)` / `PathOp.INTERSECTION` |
| 6 | Pathfinder Exclude | symmetric difference / XOR | `a.symmetric_difference(b)` / `PathOp.XOR` |
| 7 | Pathfinder Divide | node the boundaries → polygonize → every face | `faces = list(polygonize(unary_union([g.boundary for g in geoms])))` |
| 8 | Shape Builder (keep and delete faces) | Divide, then select faces by a test point or predicate, then union | `keep = unary_union([f for f in faces if f.contains(Point(30,12)) or f.area>50])` |
| 9 | Offset Path (miter) | `buffer(d, join_style="mitre", mitre_limit=4)` | `o = shape.buffer(2, join_style="mitre", mitre_limit=4)` |
| 10 | Offset Path (round) / inset | positive or negative buffer | `inset = shape.buffer(-3, join_style="round")` |
| 11 | Outline Stroke (butt caps) | `LineString.buffer(w/2, cap_style="flat", join_style="mitre")` | `bar = LineString([(8,24),(40,24)]).buffer(3, cap_style="flat")` |
| 12 | Outline Stroke (round caps, round joins) | `cap_style="round"` | `LineString(pts).buffer(3, cap_style="round", join_style="round")` |
| 13 | Stroke an arc (ring segment) | annulus ∩ wedge | `ring = Point(c).buffer(R).difference(Point(c).buffer(R-w)); arc = ring.intersection(Polygon([c, p0, p1, p2]))` |
| 14 | Round Corners effect / Live Corners (all) | open (round outer corners) or close (round inner corners) | `outer = g.buffer(-r).buffer(r)`; `inner = g.buffer(r).buffer(-r)` |
| 15 | Live Corner on one corner only | build the corner arc locally: subtract the corner square, add a quarter circle | `g = g.difference(box(x-r,y-r,x,y)).union(Point(x-r,y-r).buffer(r).intersection(box(x-r,y-r,x,y)))` |
| 16 | Snap to grid / Align to pixel grid | round every coordinate to the grid unit; render at multiples of the unit | `snap = lambda g,u=0.5: shapely.set_precision(g, u)` |
| 17 | Align / Distribute, optical centring | align bboxes, then shift by the centroid−bbox difference × 0.5-1.0 | `dx = (g.centroid.x - (g.bounds[0]+g.bounds[2])/2); g = affinity.translate(g, -dx*0.7, 0)` |
| 18 | Reflect tool | `affinity.scale(g, -1, 1, origin=(cx,cy))` | `half_m = affinity.scale(half, -1, 1, origin=(24,24)); full = unary_union([half, half_m])` |
| 19 | Rotate / Transform Each / Ctrl-D repeat | loop of affine rotations | `petals = unary_union([affinity.rotate(p, i*360/n, origin=(24,24)) for i in range(n)])` |
| 20 | Blend tool (steps between shapes) | interpolate the transform params, or `shapely` interpolation of matched points | `steps = [affinity.scale(s, 1-t*0.5, 1-t*0.5, origin=c) for t in np.linspace(0,1,5)]` |
| 21 | Golden-ratio circles | radii `r/φ^k`; place tangentially | `phi=(1+5**.5)/2; rs=[24/phi**k for k in range(6)]` |
| 22 | Type → Create Outlines | fontTools glyphSet + pen, positions from uharfbuzz | see §4.1 |
| 23 | Tracking (Character panel) | add `tracking/1000 * upm` to each advance | `x += pos.x_advance + track*upem/1000` |
| 24 | Kerning (optical, per pair) | dict of per-pair offsets in font units, applied after shaping | `x += kern.get((a,b),0)` |
| 25 | Direct Selection: edit a letterform | operate on the glyph path: boolean cut or extend, or move specific contour points | `R_new = pathops.op(R, cut_path, PathOp.DIFFERENCE)` |
| 26 | Object → Path → Simplify | `shapely simplify` (Douglas-Peucker); potrace `--alphamax` / `--opttolerance` | `g.simplify(0.05, preserve_topology=True)`; `potrace -a 1.0 -O 0.4 -t 60` |
| 27 | Image Trace | potrace on a thresholded PBM | `potrace in.pbm -s --flat -t 60 -O 0.4 -o out.svg` |
| 28 | Clean up / remove stray points | merge near-duplicate and collinear vertices | `g = g.simplify(0.01)`; `pathops.simplify(p)` |
| 29 | Add anchor at extrema / anchor discipline | svgpathtools: split curves at x and y extrema | see §4.2 |
| 30 | Scale stroke weight separately (horizontals thinner) | non-uniform buffer: build H bars with a smaller `w` | `vert_w=6; hor_w=vert_w*0.9` |
| 31 | Overshoot | scale the round shapes from their centre by 1.01-1.03 vertically | `o = affinity.scale(o, 1, 1.02, origin="center")` |
| 32 | Expand Appearance / flatten to compound path | union everything into one MultiPolygon, then export an evenodd or nonzero path | `final = unary_union(parts)` |
| 33 | Export SVG / PNG | write `d` from the polygon exteriors and interiors; render with resvg | see §4.3 |
| 34 | Inkscape CLI equivalents | `inkscape --actions="select-all;path-union;export-do"`; `object-stroke-to-path`; `path-simplify` | `inkscape in.svg --actions="select-all;object-stroke-to-path;path-union;export-filename:out.svg;export-do"` |

### 4.1 Create Outlines with shaping, tracking and kerning
```python
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import pathops

def outline_text(font_path, text, size=1000, track=40, kern={}):
    blob = hb.Blob.from_file_path(font_path); face = hb.Face(blob); font = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": False})
    tt = TTFont(font_path); gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    upem = tt["head"].unitsPerEm
    out = pathops.Path(); x = 0
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        name = order[info.codepoint]
        gs[name].draw(TransformPen(out.getPen(), (1, 0, 0, 1, x + pos.x_offset, pos.y_offset)))
        pair = (text[i], text[i+1]) if i + 1 < len(text) else None
        x += pos.x_advance + track * upem / 1000 + kern.get(pair, 0)
    return pathops.simplify(out)   # y-up font units: flip when you write the SVG
```

### 4.2 Anchor-point discipline (points at extrema, no redundant nodes)
```python
from svgpathtools import parse_path, CubicBezier
def split_at_extrema(seg):     # seg: svgpathtools CubicBezier -> list of pieces with nodes at x/y extrema
    ts = sorted(set(round(t, 6) for t in _extrema_t(seg) if 0.001 < t < 0.999))
    pieces, rest, t0 = [], seg, 0.0
    for t in ts:
        a, rest = rest.split((t - t0) / (1 - t0)); pieces.append(a); t0 = t
    return pieces + [rest]
def _extrema_t(seg):            # roots of the derivative of x(t) and y(t)
    import numpy as np
    P = np.array([complex(p) for p in seg.bpoints()])
    d = 3*np.array([P[1]-P[0], P[2]-P[1], P[3]-P[2]])
    ts = []
    for comp in (d.real, d.imag):
        a, b, c = comp[0]-2*comp[1]+comp[2], 2*(comp[1]-comp[0]), comp[0]
        ts += [r.real for r in np.roots([a, b, c]) if abs(r.imag) < 1e-9]
    return ts
# Rule: every curve has nodes at its extrema with horizontal or vertical handles; no node sits mid-straight;
# total nodes are about the same as in a hand-drawn Illustrator version (the count is a lint metric: report it per mark).
```

### 4.3 Polygon → SVG path
```python
def poly_d(g, H=48):
    def ring(r): return "M" + "L".join(f"{x:.3f},{y:.3f}" for x, y in r.coords[:-1]) + "Z"
    geoms = g.geoms if hasattr(g, "geoms") else [g]
    return "".join(ring(p.exterior) + "".join(ring(i) for i in p.interiors) for p in geoms)
# <path fill-rule="evenodd" d="..."/>; render: resvg in.svg out.png -w 16
```

---

## 5. Construction rules (how studio marks are drawn)

- **Grid.** Use a 48-unit (or 24 / 96) square. Every coordinate is a whole or half unit. Draw the grid and the key circles on the construction page; only the lines that matter, at most 5 per side.
- **One radius family.** All circles come from one series, e.g. 24 / 18 / 12 / 6, or the golden series r, r/φ, r/φ². All corner radii are equal, or follow a 2:1 inner/outer rule (inner radius = outer radius − stroke width), so that parallel curves stay parallel.
- **One stroke weight, one gap width.** Negative-space cuts are the same width as each other and are ≥ the stroke at 16 px (≥ 1.5 px → with a 48-unit grid rendered at 16 px, ≥ 4.5 units).
- **Primitives → booleans → done.** Never draw a freehand bezier where a circle intersection will do.
- **Anchors only at extrema and corners**, with handles horizontal or vertical. A clean mark has few nodes (a simple monogram typically has 8-30).
- **One move.** The concept should be describable in one sentence of ≤ 12 words: "An A whose counter is a map pin."

---

## 6. Optical-correction rules (numbers are starting points; always confirm by rendering)

| Correction | Rule |
|---|---|
| Overshoot, round shapes | Circles and bowls extend **1-3% of the height** past the flat lines (cap height and baseline) on each side. Use about 1.5% for a geometric logo, up to 3% for a perfect circle beside squares. |
| Overshoot, pointed shapes | An apex (A, V, triangle point) extends **3-5%** past the line, more than rounds do, because a point carries almost no mass at the line. |
| Circle vs square size | A circle that looks equal to a square has a diameter of about **1.03-1.06×** the square's side (the area looks equal at about 1.13×; designers settle around 1.05). |
| Horizontals thinner than verticals | In a monoline sans, horizontal strokes are about **5-10% thinner** than verticals (heavier display weights: 10-15%). The bowl of an O is thinnest at 12 and 6 o'clock (about 85-92% of the stem). |
| Crossbar placement | Optical centre sits above geometric centre. Put the H/E crossbar **2-5% of the cap height above the middle**, and the A crossbar lower (often 30-40% up from the baseline) so the upper counter is not too small. The upper counters of B, E, S and R are **smaller** than the lower ones (the top half is about 46-48% of the height). |
| Diagonal and junction thinning | Diagonals are drawn about 3-8% thinner than stems. Where two strokes meet (the A apex, V, M, N, junctions with bowls), thin each stroke **10-25%** near the joint so the joint does not form a dark blob. |
| Ink traps | Only for marks used ≤ 24 px, in signage or in print on uncoated stock. Notch acute inside corners by about **10-20% of the stroke width** (a cut wedge or circle). At 512 px they must be invisible as a "feature"; at 16 px they keep the corner open. |
| Optical centring | Centre by visual mass, not by bounding box. Triangles and play-button shapes move toward their flat side by about **5-10% of their width**. An asymmetric mark in a circle or app tile moves until the centroid sits ~60-80% of the way from the bbox centre to its true centroid. Put a mark in an app icon slightly above the geometric centre (about 1-2% of the tile height). |
| Minimum stroke | At 16 px: **≥ 1.5 px** (the make-logo gate). At 24 px: ≥ 2 px. Gaps and counters at 16 px: **≥ 1.5 px** open, so the counters seen at 512 px must still be present at 16 px. In grid terms: on a 48-unit canvas rendered at 16 px, 1 unit = 0.33 px, so the stroke must be ≥ 4.5 units (we use ≥ 5-6). |
| Tracking (wordmark) | All-caps wordmarks open up to **+20 to +80/1000 em**. Track tighter as size grows; for the small-size version add +10-20. |
| Kerning | Equalise the visual **area** between letters, not the distance between them. For ARENA, look closely at A–R (move them together), R–E (the R leg against the E), N–A (tighten, since diagonal to diagonal leaves an empty triangle) and E–N (straight-to-straight stems are the widest spacing; set them as the reference). Rough order of spacing between letter sides: straight–straight (widest) > straight–round > round–round > diagonal pairs (tightest). |
| Pixel fitting | For the 16/24/32 px favicon variants, snap the stems to whole pixels (on a grid that is a multiple of 16). Draw a separate simplified favicon rather than scaling the master down. |
| Visual weight of colour | Light-on-dark looks bolder: make the reversed version about **2-4% thinner** (e.g. `buffer(-0.02*stroke)`). |

---

## 7. Checklists

### 7.1 Word-combination ideation
- [ ] Write the brand's 3-5 attributes and their opposites (what ARENA is *not*).
- [ ] Write the noun core: "arena", "local", "play", "book", "near".
- [ ] For each, list 10-15 associations in three columns: **objects** (ball, court lines, net, whistle, pin, ticket, bench, scoreboard, stadium bowl, jersey number), **actions** (kick-off, serve, join, gather, tap to book, find nearby, rally), and **shapes/systems** (oval, ring, court rectangle, centre circle, lane lines, bracket, grid of times).
- [ ] Build the matrix: rows = attributes, columns = objects, with a cell for each "attribute + object (+ action)" pair. Fill at least 30 cells with a one-line visual metaphor, and skip cells that do not spark.
- [ ] Look for **double readings** (the strongest marks): a letter that is also an object (A = stadium bowl in section or a court seen in perspective; R leg = a running stride; pin + centre circle).
- [ ] Look for **negative-space** readings: the counter of the A as a pin, a ball or a court.
- [ ] Group the ideas by metaphor (place, motion, gathering, the venue itself, the letterform). Keep at most 2 per group.
- [ ] Reject: generic sports clichés (swooshes, flames, plain balls), anything that needs colour or detail to read, and anything that looks like an existing league or brand.
- [ ] Choose 6 directions from different groups. At least 3 pictorial, at least 1 typographic, at least 1 monogram (A).

### 7.2 Sketch reduction
- [ ] Draw thumbnails at 2-3 cm (code: render at 64 px). Judge only silhouettes.
- [ ] Each idea: ≤ 3 primitives and ≤ 2 boolean moves.
- [ ] Remove a part; if it still reads, keep it removed. Repeat until removing anything breaks it.
- [ ] Merge near-equal values: radii, stroke widths, angles (0/15/30/45/60/90° only) and gaps go to one family.
- [ ] Fill test: all black, no lines. Does it read?
- [ ] Size test: 16 px and 32 px. If the idea dies, simplify or make a dedicated small version.
- [ ] Squint/blur test (Gaussian σ = 3 px at 256 px): is the gesture still clear?
- [ ] Mirror and rotate test: does it accidentally form an unwanted image or letter?
- [ ] Reversed test: white on ink.
- [ ] Distance test against references (make-logo `check_logo.py`).
- [ ] Finally redraw it cleanly on the grid. Never vectorise the sketch as is.

---

## 8. Quality bar: studio-level vs "generic AI-looking"

| Studio-level | Generic / AI-looking |
|---|---|
| One idea, statable in a sentence; often a double reading (letter + object) | Many ideas stacked (ball + pin + swoosh + star) |
| Built from a small set of primitives on a visible grid; radii and strokes from one family | Arbitrary curves, slightly-off radii, wobbly beziers, uneven stroke |
| Optical corrections present: overshoot, thinned horizontals and junctions, centring by mass | Mathematically equal everything, which looks *wrong* (round shapes look small, joints blobby, centring looks off) |
| Clean anchors at extrema, few nodes, crisp terminals | Thousands of traced nodes, lumpy curves, inconsistent terminal angles |
| Holds at 16 px in one colour; has a dedicated favicon | Depends on gradients, glow, 3D or texture; mush at small size |
| Negative space is deliberate and consistent in width | Accidental slivers, near-tangencies, gaps that close at small size |
| Wordmark kerned by eye, with 1-2 custom letterform details that echo the mark | A default font at default tracking, or an over-distorted "techy" face |
| Distinct from category clichés; checked against references | Stock icon (a plain ball, pin or trophy) or an imitation of a famous mark |
| Comes with a system: lockups, clear space, colour, icon family from the same geometry | Logo in isolation |
| Restrained palette (1 ink + 1 accent), contrast-checked | Rainbow gradients, low-contrast accents |

**Automatic gates in our pipeline** (fail = redesign):
- stroke at 16 px ≥ 1.5 px
- counters at 16 px match those at 512 px
- every coordinate on the half-grid
- ≤ 3 distinct radii and ≤ 2 distinct stroke widths
- node count per contour ≤ 2× a hand-drawn estimate
- contrast ≥ 4.5:1 (ink) and ≥ 3:1 (accent)
- distance to the nearest reference < calibrated limit
- the mark's centroid within 3% of the tile's optical centre in the app icon

**Human or visual gates:**
- reads as its idea at 64 px
- not a stock icon
- passes the blur test
- reversed version checked
