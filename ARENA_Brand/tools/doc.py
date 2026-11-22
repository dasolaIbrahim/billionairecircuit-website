"""Build "Arena Brand Identity Design.pdf": own pages (front, contents, introduction, brief, sketches, title pages,
system sheets, thank-you) interleaved with make-logo's book pages (restyled), then a footer overlay with the
document name, the "Designed by" credit and page numbers.

    python3 doc.py            (run make-logo's logo_book.py first; this patches and renders it)
"""
import base64
import json
import os
import re
import shutil
import subprocess

from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
BR = os.path.abspath(os.path.join(HERE, ".."))
BOOK = os.path.join(BR, "05_Logo_Book", "book")
OUT = os.path.join(BR, "05_Logo_Book", "pages_src")
FINAL = os.path.join(BR, "05_Logo_Book", "Arena Brand Identity Design.pdf")
ML = os.path.join(BR, "..", ".claude", "skills", "make-logo", "scripts")
os.makedirs(OUT, exist_ok=True)
shutil.copy(os.path.join(BOOK, "fonts", "book.ttf"), os.path.join(OUT, "book.ttf"))

DARK, MINT, DEEP, PAPER, INK, MUTED = "#0C0D0D", "#A6F0C6", "#0F6B45", "#F3F1EC", "#141515", "#6C6A64"
LOGO = "data:image/svg+xml;base64," + base64.b64encode(
    open(os.path.join(BR, "00_Process", "assets", "prodoktiv-logo-orange.svg"), "rb").read()).decode()

DIRS = [("D1_Wordmark_CourtLines", "Court Lines"), ("D2_Wordmark_MatchDay", "Match Day"),
        ("D3_Pixel_Scoreboard", "Pixel Scoreboard"), ("D4_Symbol_LivePin", "Live Pin"),
        ("D5_Symbol_ConvergenceCrest", "Convergence Crest"), ("D6_Lockup_Integrated", "Pin in the A"),
        ("D7_Symbol_CentreLight", "Centre Light")]
KIND = {"D1": "Wordmark", "D2": "Wordmark", "D3": "Symbol + mascot", "D4": "Symbol", "D5": "Symbol",
        "D6": "Integrated lockup", "D7": "Symbol"}
SKETCHES = [("D4_Symbol_LivePin", "Live Pin"), ("D5_Symbol_ConvergenceCrest", "Convergence Crest"),
            ("D7_Symbol_CentreLight", "Centre Light"), ("D1_Wordmark_CourtLines", "Court Lines"),
            ("D6_Lockup_Integrated", "Pin in the A")]
DETAIL = ("ARENA is the home of local sport: find courts near you, see where people are playing right now, book in a "
          "couple of taps, join tournaments and share the moment. Built for players and for the venues that host them.")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def img(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()


def idea(d):
    return json.load(open(os.path.join(BR, "04_Directions", d, "build", "build.json")))["idea"]


CSS = f"""
@font-face {{ font-family: "Book"; src: url("book.ttf"); font-weight: 100 900; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
@page {{ size: 1600px 900px; margin: 0; }}
body {{ font-family: "Book"; color: {INK}; -webkit-font-smoothing: antialiased; }}
.pg {{ width: 1600px; height: 900px; position: relative; overflow: hidden; break-after: page; background: {PAPER}; }}
.dark {{ background: {DARK}; color: #E9E9E4; }}
.mega {{ font-weight: 600; letter-spacing: -0.058em; line-height: .78; color: {MINT}; }}
.kicker {{ font-size: 15px; letter-spacing: .08em; text-transform: uppercase; color: #8E8E88; }}
.h {{ position: absolute; left: 64px; top: 52px; font-size: 104px; font-weight: 600; letter-spacing: -0.048em; line-height: .9; color: {DEEP}; }}
.sub {{ position: absolute; left: 68px; top: 168px; font-size: 18px; color: {MUTED}; }}
.credit {{ display: flex; align-items: center; gap: 12px; font-size: 14px; color: #9A9A94; }}
.credit img {{ height: 15px; }}
p {{ font-size: 19px; line-height: 1.5; }}
"""


def front():
    return f"""<section class="pg dark">
      <div class="kicker" style="position:absolute;left:64px;top:60px">Brand Identity Design</div>
      <div class="kicker" style="position:absolute;right:64px;top:60px">November 2026</div>
      <p style="position:absolute;right:64px;top:250px;width:430px;color:#B8B8B2;font-size:20px">{esc(DETAIL)}</p>
      <div class="mega" style="position:absolute;left:46px;bottom:150px;font-size:410px">ARENA</div>
      <div class="credit" style="position:absolute;left:64px;bottom:58px">Designed by <img src="{LOGO}"></div>
      <div class="kicker" style="position:absolute;right:64px;bottom:60px">Seven logo directions</div></section>"""


def thanks():
    return f"""<section class="pg dark">
      <div class="kicker" style="position:absolute;left:64px;top:60px">Brand Identity Design</div>
      <div class="kicker" style="position:absolute;right:64px;top:60px">ARENA</div>
      <p style="position:absolute;right:64px;top:250px;width:430px;color:#B8B8B2;font-size:20px">Seven directions, one brand. Tell us which one moves you, or which two you'd like to see together, and we'll take it from here.</p>
      <div class="mega" style="position:absolute;left:52px;bottom:140px;font-size:220px;line-height:.86">Thank you<br><span style="color:#5E8F73">for your time.</span></div>
      <div class="credit" style="position:absolute;left:64px;bottom:58px">Designed by <img src="{LOGO}"></div>
      <div class="kicker" style="position:absolute;right:64px;bottom:60px">November 2026</div></section>"""


def title(num, name, line=""):
    size = 230 if len(name) <= 12 else 170
    return f"""<section class="pg dark">
      <div class="kicker" style="position:absolute;left:64px;top:60px;color:{MINT}">{esc(num)}</div>
      <div class="mega" style="position:absolute;left:52px;bottom:190px;font-size:{size}px;max-width:1500px">{esc(name)}</div>
      {f'<p style="position:absolute;left:64px;bottom:96px;width:900px;color:#A9A9A3;font-size:19px">{esc(line)}</p>' if line else ''}</section>"""


def contents(toc):
    rows = []
    for group, items in toc:
        rows.append(f'<div style="font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:{MUTED};margin:22px 0 8px">{esc(group)}</div>')
        for num, name, page in items:
            rows.append(f'<div style="display:flex;align-items:baseline;gap:22px;border-top:1px solid #D9D5CC;padding:9px 0">'
                        f'<span style="width:44px;font-size:15px;color:{DEEP};font-weight:600">{esc(num)}</span>'
                        f'<span style="flex:1;font-size:24px;letter-spacing:-.02em">{esc(name)}</span>'
                        f'<span style="font-size:15px;color:{MUTED};font-variant-numeric:tabular-nums">{page:02d}</span></div>')
    return f"""<section class="pg"><div class="h" style="font-size:150px;top:60px">Contents</div>
      <p style="position:absolute;left:68px;top:250px;width:420px;color:{MUTED};font-size:18px">Foundations first, then the seven directions, each with its system and its mockups, then all of them side by side.</p>
      <div style="position:absolute;left:640px;right:64px;top:44px">{''.join(rows)}</div></section>"""


def intro():
    cols = [("What ARENA is", "A mobile platform that makes local sport easy to find, book, play and share. Players see courts near them and who's playing right now; venues fill their slots, run tournaments and earn a Verified badge."),
            ("What's inside", "Seven identity directions: two wordmarks, four symbols and one integrated lockup. Each is drawn on a grid, checked down to favicon size, and comes with its own system: three circle modes, three lockups and six status poses."),
            ("How to choose", "Read each direction as a whole: its idea, its system, then the mockups. Finish on the side-by-side pages. Pick one, or name two you'd like to see combined.")]
    c = "".join(f'<div><div style="font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:{DEEP};font-weight:600;margin-bottom:14px">{esc(a)}</div><p>{esc(b)}</p></div>' for a, b in cols)
    return f"""<section class="pg"><div class="h" style="font-size:150px;top:60px">Introduction</div>
      <p style="position:absolute;left:68px;top:250px;width:860px;font-size:34px;line-height:1.25;letter-spacing:-.02em">Seven ways to say: there's a game near you, and it's on right now.</p>
      <div style="position:absolute;left:68px;right:64px;top:470px;display:grid;grid-template-columns:repeat(3,1fr);gap:56px">{c}</div></section>"""


def brief():
    blocks = [("Purpose", "Get more people playing, by making every local arena discoverable, bookable and alive."),
              ("Positioning", "The home of local sport: where players find the game and venues fill their slots. ARENA shows what's live now, runs the competition and vouches for the venue."),
              ("Attributes", "Live · Competitive · Communal · Trusted · Local with global ambition · Effortless · Energetic but premium."),
              ("Personality", "The confident captain: organises the game, knows every court, keeps it fair, isn't loud about it."),
              ("The tension", "Street-court energy against a trusted, premium platform. The mark stays calm and engineered; motion, photography and one live accent carry the noise."),
              ("What to avoid", "Green pitch rectangles, balls, swooshes, neon on black, generic pins, triangle As, flags. The place itself (bowl, ring, court) is the richer idea.")]
    c = "".join(f'<div><div style="font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:{DEEP};font-weight:600;margin-bottom:10px">{esc(a)}</div><p style="font-size:18px">{esc(b)}</p></div>' for a, b in blocks)
    return f"""<section class="pg"><div class="h">The brief</div>
      <div style="position:absolute;left:68px;right:64px;top:250px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px 56px">{c}</div></section>"""


def words():
    rows = [("01", "Court Lines", "Wordmark", "court + line: letters drawn with the court's own geometry"),
            ("02", "Match Day", "Wordmark", "poster + pin: extended lowercase with a pin carved into each a"),
            ("03", "Pixel Scoreboard", "Symbol + mascot", "scoreboard + pin: a pixel pin with six status faces"),
            ("04", "Live Pin", "Symbol", "pin + bowl + live: a stadium on the map, switched on"),
            ("05", "Convergence Crest", "Symbol", "bracket + crest: four, two, one, carved in a shield"),
            ("06", "Pin in the A", "Integrated lockup", "A counter + pin, last A + live light: find it, then it's on"),
            ("07", "Centre Light", "Symbol", "centre circle + floodlight: where every game starts, lit")]
    r = "".join(f'<tr><td style="color:{DEEP};font-weight:600">{a}</td><td style="font-size:22px;letter-spacing:-.02em">{esc(b)}</td><td style="color:{MUTED}">{esc(c)}</td><td>{esc(d)}</td></tr>' for a, b, c, d in rows)
    return f"""<section class="pg"><div class="h">From words to pictures</div>
      <table style="position:absolute;left:68px;right:64px;top:250px;border-collapse:collapse;font-size:17px">
      <style>td{{padding:13px 12px 13px 0;border-top:1px solid #D9D5CC;vertical-align:baseline}}</style>{r}</table></section>"""


def picture(heading, sub, png, top=230, maxh=600):
    return f"""<section class="pg"><div class="h">{esc(heading)}</div><div class="sub">{esc(sub)}</div>
      <img src="{img(png)}" style="position:absolute;left:64px;right:64px;top:{top}px;width:1472px;height:{maxh}px;object-fit:contain;object-position:left top"></section>"""


# ------------------------------------------------------------------------------------------- make-logo pages
def patch_book():
    p = os.path.join(BOOK, "index.html")
    s = open(p).read()
    s = re.sub(r"<tr><td>nearest reference</td>.*?</tr>", "", s)
    over = f"""<style>
h2 {{ font-size: 104px !important; font-weight: 600 !important; letter-spacing: -0.048em !important; line-height: .9 !important; color: {DEEP} !important; }}
.label {{ top: 52px !important; }}
.foot, .num {{ display: none !important; }}
section.page {{ background: {PAPER}; }}
</style></head>"""
    s = s.replace("</head>", over, 1)
    open(p, "w").write(s)


def main():
    patch_book()
    r = subprocess.run(["node", os.path.join(ML, "render_book.mjs"), BOOK], capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-400:])
    ml_pages = {slug: i for i, (n, slug) in enumerate(json.load(open(os.path.join(BOOK, "pages.json")))["pages"])}

    # The sequence: ("own", html) or ("ml", slug); footer flag; dark flag; toc label
    seq = []
    own = lambda html, foot=True, dark=False: seq.append(("own", html, foot, dark))
    # full-bleed mockup spreads (tiles run to 30 px from the edge) carry no footer, so nothing collides
    ml = lambda slug: seq.append(("ml", slug, not slug.endswith(("-use", "-build")), False))
    marks = {}

    own(front(), foot=False, dark=True)
    own("__CONTENTS__")
    marks["Introduction"] = len(seq) + 1; own(intro())
    marks["The brief"] = len(seq) + 1; own(title("Foundations", "The brief", "Purpose, positioning, attributes and the ideas each direction grew from."), dark=True)
    own(brief()); own(words())
    marks["Sketches"] = len(seq) + 1; own(title("Foundations", "Sketches", "Forty and more thumbnails per symbol before any of them was chosen."), dark=True)
    for d, name in SKETCHES:
        own(picture(f"{name}", "Sketches", os.path.join(BR, "03_Sketches", f"{d}_contact_sheet.png"), top=210, maxh=630))
    marks["Seven directions"] = len(seq) + 1; own(title("Directions", "Seven directions", "Two wordmarks, four symbols and one integrated lockup."), dark=True)
    for k in ("directions-1", "directions-2", "directions-3"):
        ml(k)
    for i, (d, name) in enumerate(DIRS, 1):
        marks[f"{i:02d}|{name}"] = len(seq) + 1
        own(title(f"Direction {i:02d} · {KIND[d[:2]]}", name, idea(d)), dark=True)
        own(picture(f"{name} system", "Three circle modes · three lockups · six status poses", os.path.join(BR, "04_Directions", d, f"{d[:2]}_system_sheet.png")))
        for part in ("use", "build", "colour", "sizes"):
            ml(f"d{i}-{part}")
    marks["Side by side"] = len(seq) + 1; own(title("Directions", "Side by side", "Every mark large and at 16 px, with its checks."), dark=True)
    for k in ("compare-1", "compare-2", "compare-3"):
        ml(k)
    marks["Thank you"] = len(seq) + 1; own(thanks(), foot=False, dark=True)

    toc = [("Foundations", [("", "Introduction", marks["Introduction"]), ("", "The brief", marks["The brief"]), ("", "Sketches", marks["Sketches"])]),
           ("Directions", [("", "Seven directions", marks["Seven directions"])] +
            [(k.split("|")[0], k.split("|")[1], v) for k, v in marks.items() if "|" in k]),
           ("Close", [("", "Side by side", marks["Side by side"]), ("", "Thank you", marks["Thank you"])])]

    # own pages -> one HTML/PDF
    own_html = [contents(toc) if x[1] == "__CONTENTS__" else x[1] for x in seq if x[0] == "own"]
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(own_html)}</body></html>'
    open(os.path.join(OUT, "own.html"), "w").write(doc)
    # footer overlay: one page per document page
    foots = []
    for n, x in enumerate(seq, 1):
        if not x[2]:
            foots.append('<section class="pg" style="background:transparent"></section>')
            continue
        col = "#9A9A94" if x[3] else "#8B887F"
        foots.append(f'<section class="pg" style="background:transparent">'
                     f'<div style="position:absolute;left:64px;bottom:32px;font-size:13px;color:{col}">Arena Brand Identity Design</div>'
                     f'<div class="credit" style="position:absolute;right:64px;bottom:28px;font-size:13px;color:{col}">Designed by <img src="{LOGO}" style="height:12px"><span style="margin-left:18px;font-variant-numeric:tabular-nums">{n:02d}</span></div></section>')
    fh = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} html,body{{background:transparent}}</style></head><body>{"".join(foots)}</body></html>'
    open(os.path.join(OUT, "foot.html"), "w").write(fh)
    subprocess.run(["node", os.path.join(HERE, "print_pages.mjs"), os.path.join(OUT, "own.html"), os.path.join(OUT, "foot.html")], check=True)

    ownr = PdfReader(os.path.join(OUT, "own.pdf"))
    mlr = PdfReader(os.path.join(BOOK, "logobook.pdf"))
    footr = PdfReader(os.path.join(OUT, "foot.pdf"))
    w = PdfWriter()
    oi = 0
    for n, x in enumerate(seq):
        if x[0] == "own":
            page = ownr.pages[oi]; oi += 1
        else:
            page = mlr.pages[ml_pages[x[1]]]
        w.add_page(page)
        if x[2]:
            w.pages[-1].merge_page(footr.pages[n])
    w.add_metadata({"/Title": "Arena Brand Identity Design", "/Author": "Prodoktiv"})
    w.write(FINAL)
    print("wrote", FINAL, len(w.pages), "pages")


if __name__ == "__main__":
    main()
