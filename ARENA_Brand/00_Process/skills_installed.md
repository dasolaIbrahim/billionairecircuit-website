# Skills and tools installed

| Skill / tool | Source | Licence | Worked? | Notes |
|---|---|---|---|---|
| make-logo | design.how skills index (archive, sha256 verified) | free agent skill (design.how) | Yes | `npx skills add` failed (Node ignores the proxy); installed manually into `.claude/skills/make-logo`. Used for Are.na pull, measure, calibrate, check, logo book. Package step after the pick. |
| make-font, build-design-system, design-system-boss, token-mapping, ui-review, make-motion | design.how (same) | same | Installed | For Phases 7–10 (type, tokens, UI review of mockups, launch-reveal motion). |
| kaankiziltug/logo-design, neonwatty/logo-designer-skill, zstvns/design-skills | GitHub | — | Not installed | github.com is blocked for this session except the user's repos; their methods (SAD bar, iteration previews, PNG ladder) are applied by hand in QA and packaging. |
| Anthropic frontend-design / pdf | — | — | Not available here | PDF assembly done with Playwright print-to-PDF + pypdf. |
| Previous pipeline (thesidecircuit / Dayrate Club / GhostRevenue) | User upload (GhostRevenue brand.json, design-system.json, foundation, SVGs) | user's own | Used | GhostRevenue's pixel direction cloned as D7; its "3 circle modes, 3 lockups, 6 poses" system applied to all seven at the user's request. |
| shapely 2.2, skia-pathops 0.9, fonttools 4.68, uharfbuzz, svgpathtools, picosvg, cairosvg, resvg-py, coloraide, scikit-image, scipy, pypdf | PyPI | BSD/MIT/Apache | Yes | Pathfinder-equivalent booleans, outlining, rendering, checks. |
| potrace, ImageMagick, ffmpeg, yt-dlp | apt / PyPI | GPL/Apache/LGPL/Unlicense | Yes | yt-dlp fetched reel captions; video CDN blocked. |
| Playwright + Chromium | preinstalled | Apache-2.0 | Yes | Pinterest capture, book rendering, PDF. |
| Inkscape, svgo | — | — | Not installed yet | Needed at export (Phase 9); svgo via npx. |
