# ARENA brand identity: working folder

**Status: Phase 6, the logo book gate.** Open `05_Logo_Book/Arena Brand Identity Design.pdf` and pick a direction (D1–D7) or a hybrid.
Phases 7–11 (refinement, final systems, brand elements, exports at exact dimensions, guidelines PDF) start after the pick.

| Folder | What's in it | Use it for |
|---|---|---|
| `00_Process/` | plan.md, decisions_log.md, user_interventions.md, skills_installed.md, qa/ | What was done, why, and what needs you |
| `01_Research/` | logo_method.md, visual_direction.md, competitive_audit.md, app_store_and_specs.md, positioning_grid.svg, tutorial_notes/ | The evidence behind every decision (moodboard images are local only, see below) |
| `02_Strategy/` | brand_platform.md, word_matrix.md | Purpose, positioning, attributes, voice; how ideas were generated and scored |
| `03_Sketches/` | contact sheets per direction | The 40+ thumbnails per symbol direction behind each pick |
| `04_Directions/D1…D7/` | recipe.json (construction), build/ (mark, wordmark, lockups as SVG; colour versions; construction.svg; check.json), Dn_system_sheet.png | Each direction's files and its system: 3 circle modes, 3 lockups, 6 status poses |
| `05_Logo_Book/` | **Arena Brand Identity Design.pdf** (decision gate, 63 pages), book/ (make-logo pages), pages_src/ (cover, contents, title and system pages) | Choosing |
| `06_Final_Logo/` … `09_Brand_Guidelines/` | empty until you pick | Final package, brand elements, social/store assets, mockups, guidelines |
| `tools/` | arena_build.py, letters.py, sketches.py, directions.py, system_sheet.py, pixel.py, supplement.py | Rebuild anything: `python3 tools/directions.py && python3 tools/system_sheet.py && python3 tools/pixel_sheet.py`, then make-logo logo_book.py and `python3 tools/doc.py` |

The seven directions: D1 Court Lines (wordmark) · D2 Match Day (wordmark) · D3 Pixel Scoreboard (symbol + mascot) ·
D4 Live Pin (symbol) · D5 Convergence Crest (symbol) · D6 Pin in the A (integrated lockup) · D7 Centre Light (symbol).

Reference images (Are.na, Pinterest) are kept out of git on purpose: they belong to their owners, make-logo forbids
redistributing them, and this repository is public. Their notes, measurements and manifests are kept.
