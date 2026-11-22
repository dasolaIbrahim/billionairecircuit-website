# Reel Df-5JMMjKiw (2026-11-21), @griffinwooldridge1: the design.how "make-logo" agent skill

Access:
- yt-dlp read the post's metadata and full caption.
- The video file was refused by the proxy on `scontent-ord5-2.cdninstagram.com` (403).
- design.how and the skill's GitHub repo (arla6ka/design.how) could not be reached directly: design.how is not an allowed domain, and the GitHub API returned "repository access not enabled".
- A copy of the same skill is installed in this project at `/home/user/billionairecircuit-website/.claude/skills/make-logo/`. I read all of its references and its main scripts.

Caption summary: Claude asks about the brand and a few logos you like, pulls more references from Are.na, measures their proportions, writes six directions, lays them out in a PDF logo book with mockups, then packages SVG, PNG and favicon. Some directions trace a reference logo and change it.

## The skill's method, from its SKILL.md and references
1. **Ask once.** Collect the name, what the product does and for whom, ONE idea the mark could carry (a letter, object, motion or word), 3-6 logos the client likes, where the logo will live, colour limits, and whether they want a mark, a wordmark or both.
2. **Gather.** Use the client's references, about 100 logos from Are.na for craft, and an Are.na set from the product's own world (field + "logo" or "identity").
3. **Measure** every reference as numbers:
   - Shape: aspect, coverage, solidity (ink over its convex hull), compactness (P²/4πA), corners, centre_offset, symmetry.
   - Stroke: median stroke (2 × the distance transform sampled on the skeleton), stroke_contrast (90th over 10th percentile).
   - Structure: components, counters.
   - Medians over 98 Are.na logos: aspect 1.36, coverage 0.34, solidity 0.42, stroke 59/1000 of height, 3 counters, compactness 30, 62 corners.
4. **Calibrate** a distance model:
   - Features: IoU, edge distance and DCT hash, combined by logistic regression.
   - Training pairs: real pairs of different logos, and synthetic near-copies made by turning 4°, thickening or thinning, stretching 10%, cutting a part away, adding a part, and mirroring.
   - The limit is the score that 10% of references reach against their nearest other reference.
5. **Targets.** The client's references give the target and the wider set gives the range. If the references disagree, ask the client rather than averaging.
6. **Six directions**, each a different answer to the idea:
   - Mix traced marks, idea marks built from shapes, and typographic marks. At least half carry the idea as a picture.
   - Each direction is a JSON recipe: shapes on a 48-unit grid (rect with r, circle, ring, arc, polygon, glyph, trace) combined with the ops add, cut, keep or xor (union, difference, intersection, xor in skia-pathops), plus rotate, mirror and repeat. Every coordinate is a whole or half grid unit.
   - "Agents place shapes well and draw curves badly."
7. **Check** every mark rendered with resvg:
   - stroke at 16 px ≥ 1.5 px
   - the counters at 16 px match those at 512 px
   - ink/paper contrast ≥ 4.5:1 and accent ≥ 3:1
   - the nearest reference scores under the limit
8. **Logo book** (1600×900 PDF):
   - Cover and the directions page.
   - For each direction: in use (lockup reversed, browser tab, poster), construction (grid with at most 5 guides per side), colour (5 swatches), and sizes (16/24/32/64 px).
   - Side by side with all checks, then photo credits.
9. **Package**:
   - SVGs of the mark, wordmark, lockup and stacked lockup, each in ink, reversed, accent and black.
   - PNGs from 16 to 1024 px, plus favicon.ico.
   - Licences, brand.json and a trademark-search sheet.

## Design doctrine worth stealing
- Lead with abstract marks that make ONE move with 2-3 primitives: two squares overlapped and xor'd, a disc cut once, one shape repeated and turned.
- Literal pictograms read as stock icons, so use them last.
- If the silhouette is too close to a reference, change the OUTLINE (split, cut, extend), not a detail inside it.
- Use crisp square terminals; curve an end only when the curve is the idea.
- Give each direction its own face and palette, so the client compares ideas, not colours.
- Display faces with character (OFL): Bagel Fat One, Abril Fatface, Fraunces heavy, Syne, Bricolage Grotesque, Instrument Serif, Unbounded.
- Never use Remix Icon (its licence bans logos) or any brand-icon set.
- Lockup: mark_scale is the mark height over the cap height (example 1.9); the gap is 0.8 cap heights.
