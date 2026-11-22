# ARENA brand identity: execution plan

Executor: Claude Code (orchestrator) + parallel subagents. Free / open-source tools only. No local LLMs.
Change from the master prompt: **six creative directions instead of five** (user instruction, 2026-11-22).
This also matches make-logo's own default of six.

## The six directions
| # | Kind | Working name | Core pair from word matrix |
|---|------|--------------|-----------------------------|
| D1 | Wordmark A | Court Lines (geometric / kinetic) | court + line |
| D2 | Wordmark B | Match Day (condensed / heritage-athletic) | scoreboard + jersey |
| D3 | Symbol A | The Bowl / Live Pin | pin + bowl + live |
| D4 | Symbol B | Convergence / Bracket Crest | bracket + convergence + crest |
| D5 | Integrated lockup | Symbol inside the letterform | A-counter + pin / goalposts |
| D6 | Symbol C (new) | Centre Light: centre circle seen from above as a floodlit "live" signal | centre circle + floodlight + gather |
| D7 | Symbol + mascot (user request, mid-run) | Pixel Scoreboard: the GhostRevenue pixel system cloned for ARENA | pixel pin + six status poses |

User additions (2026-11-22, mid-run): (1) clone the GhostRevenue "pixel green" direction as a direction → D7;
(2) give every direction the same depth: three circle modes, three lockups, six poses → `Dn_system_sheet.png` in each folder.

Why D6 is a third symbol: the brief's strongest product moment ("Live Now" / the lit court) and the crowd/ring
territory were otherwise only partly covered. D3 is about *place*, D4 about *competition*, D6 about *gathering
and being on*. All three are symbols, not monograms.

## Phases (status kept in decisions_log.md)
| Phase | Work | Subagents | Gate |
|---|---|---|---|
| 0 | Plan, folders, install make-logo + companions, toolchain, interventions | — | — |
| 1 | Research: Are.na pull (make-logo), measure, calibrate; Pinterest pins + moodboards; logo-method/tutorial research; competitive + app-store audit | 3 in parallel | — |
| 2 | Brand platform, word-combination matrix | — | Platform summary sent (continue unless objection) |
| 3 | 40+ thumbnails per symbol direction, contact sheets | — | — |
| 4 | Build six directions (grid construction, boolean ops, custom wordmarks), palette + type per direction | — | — |
| 5 | make-logo checks, SAD bar, independent anti-tacky review, redraw | 1 reviewer | — |
| 6 | Logo book PDF | — | **STOP: user picks** |
| 7–11 | Refine, systems, elements, exports at exact dimensions, guidelines PDF, final QA | 2–4 | after pick |

## Toolchain
make-logo scripts (build_logo, check_logo, distance, measure, calibrate, logo_book, render_book, package_logo),
shapely, skia-pathops, fonttools + uharfbuzz, svgpathtools, picosvg, cairosvg, resvg-py, coloraide (OKLCH, WCAG, APCA),
Pillow, numpy, scikit-image, potrace, ImageMagick, ffmpeg, yt-dlp, Playwright/Chromium (PDF), svgo (npx).
Fonts: Google Fonts OFL families only, OFL.txt saved per family.
