"""ARENA logo-book supplement: front matter + system sheets + recommendation, same 1600x900 page and face as
make-logo's book. Then merges: front -> make-logo book -> back into 05_Logo_Book/ARENA_Logo_Book.pdf.

    python3 supplement.py
"""
import base64
import json
import os
import shutil
import subprocess

from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
BR = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(BR, "05_Logo_Book", "supplement")
os.makedirs(OUT, exist_ok=True)
shutil.copy(os.path.join(BR, "05_Logo_Book", "book", "fonts", "book.ttf"), os.path.join(OUT, "book.ttf"))
DIRS = sorted(d for d in os.listdir(os.path.join(BR, "04_Directions")) if d[:2] in [f"D{i}" for i in range(1, 8)])
REC = json.load(open(os.path.join(HERE, "recommendation.json")))


def img(path):
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


CSS = """
@font-face { font-family: "Book"; src: url("book.ttf"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
@page { size: 1600px 900px; margin: 0; }
body { font-family: "Book"; color: #161616; -webkit-font-smoothing: antialiased; }
.pg { width: 1600px; height: 900px; position: relative; overflow: hidden; page-break-after: always; background: #f3f1ec; padding: 64px 72px; }
.pg.ink { background: #111214; color: #f3f1ec; }
h1 { font-size: 88px; font-weight: 500; letter-spacing: -0.035em; line-height: .95; }
h2 { font-size: 44px; font-weight: 500; letter-spacing: -0.025em; margin-bottom: 28px; }
h3 { font-size: 15px; font-weight: 600; letter-spacing: .02em; text-transform: uppercase; margin-bottom: 10px; color: #6a6760; }
.ink h3 { color: #9d9a92; }
p, li { font-size: 19px; line-height: 1.45; font-weight: 400; }
.sm p, .sm li { font-size: 15.5px; line-height: 1.45; }
ul { padding-left: 20px; }
.cols { display: grid; gap: 40px; }
.foot { position: absolute; left: 72px; right: 72px; bottom: 34px; font-size: 12px; color: #8b887f; display: flex; justify-content: space-between; }
.sheet { position: absolute; left: 20px; top: 20px; width: 1560px; height: 720px; border-radius: 6px; }
.cap { position: absolute; left: 72px; right: 72px; bottom: 60px; font-size: 18px; line-height: 1.4; }
.contact { width: 100%; height: 640px; object-fit: contain; background: #fff; border-radius: 6px; }
table { border-collapse: collapse; width: 100%; font-size: 15px; }
td, th { text-align: left; padding: 9px 10px; border-bottom: 1px solid #d8d4cc; vertical-align: top; }
th { font-weight: 600; color: #6a6760; font-size: 13px; text-transform: uppercase; letter-spacing: .03em; }
.pill { display: inline-block; padding: 4px 12px; border-radius: 99px; font-size: 14px; font-weight: 600; }
"""


def page(body, cls="", foot="ARENA · Logo directions"):
    return f'<section class="pg {cls}">{body}<div class="foot"><span>{foot}</span><span>{"Supplement"}</span></div></section>'


def front():
    pp = []
    pp.append(page(f"""
      <div style="position:absolute;left:72px;top:72px;font-size:15px;color:#9d9a92">Find, book, play and share local sport</div>
      <div style="position:absolute;left:72px;bottom:150px"><h1>ARENA</h1>
      <div style="font-size:44px;color:#9d9a92;letter-spacing:-.02em;margin-top:8px">Logo book · seven directions</div></div>
      <div style="position:absolute;right:72px;bottom:150px;width:520px" class="sm"><p style="color:#c9c6bd">{esc(REC['cover_note'])}</p></div>""", "ink"))
    pp.append(page(f"""<h2>The brief in one page</h2><div class="cols" style="grid-template-columns:1fr 1fr 1fr">
      <div><h3>Purpose</h3><p>Get more people playing, by making every local arena discoverable, bookable and alive.</p>
      <h3 style="margin-top:28px">Positioning</h3><p>The home of local sport: where players find the game and venues fill their slots. Unlike directories, ARENA shows what's live now, runs the competition and vouches for the venue.</p></div>
      <div><h3>Attributes</h3><p>Live · Competitive · Communal · Trusted · Local with global ambition · Effortless · Energetic but premium</p>
      <h3 style="margin-top:28px">Personality</h3><p>The confident captain: organises the game, knows every court, keeps it fair, isn't loud about it.</p></div>
      <div><h3>The tension</h3><p>Street-court energy versus a trusted, premium platform. Resolution: the mark is calm and engineered; motion, photography and one live accent carry the noise.</p>
      <h3 style="margin-top:28px">What the category taught us</h3><p>Avoid: green pitch rectangles, balls, swooshes, neon lime on black, generic pins, triangle As, orange "live" icons, flags. Open territory: ultraviolet, bone, clay; the place itself (bowl, ring, court) as the idea.</p></div></div>"""))
    pp.append(page("""<h2>From words to pictures</h2><div class="sm"><table>
      <tr><th>Direction</th><th>Kind</th><th>Word pair → one picture</th><th>Says</th></tr>
      <tr><td>D1 Court Lines</td><td>Wordmark</td><td>court + line → letters drawn with the court's own geometry</td><td>Precise, effortless, modern</td></tr>
      <tr><td>D2 Match Day</td><td>Wordmark (your direction)</td><td>poster + pin → Syne lowercase, a pin in each a, last a reversed</td><td>Loud, friendly, face-off tension</td></tr>
      <tr><td>D3 Live Pin</td><td>Symbol</td><td>pin + bowl + live → a stadium on the map, switched on</td><td>There's a game near you, and it's on now</td></tr>
      <tr><td>D4 Convergence Crest</td><td>Symbol</td><td>bracket + converge + crest → a bracket carved in a shield</td><td>Everyone meets here; fair; verified</td></tr>
      <tr><td>D5 Pin in the A</td><td>Integrated lockup</td><td>A counter + pin, last A + live light</td><td>Find it, then it's on: the whole product in one word</td></tr>
      <tr><td>D6 Centre Light</td><td>Symbol</td><td>centre circle + floodlight + gather</td><td>Where every game starts, lit</td></tr>
      <tr><td>D7 Pixel Scoreboard</td><td>Symbol + mascot</td><td>The GhostRevenue pixel system, cloned (your request): pin mascot + 6 poses</td><td>Playful, systemised, LED-scoreboard energy</td></tr>
      </table><p style="margin-top:22px;color:#6a6760">40+ thumbnails were drawn per symbol direction and 6–12 per wordmark before these were picked; the contact sheets follow. Every direction was built on a grid from rectangles, circles, arcs and polygons with boolean operations (no traced reference, no stock icon, no font outlines in D1, D2 and D5).</p></div>"""))
    for d in ["D3_Symbol_LivePin", "D4_Symbol_ConvergenceCrest", "D6_Symbol_CentreLight"]:
        pp.append(page(f'<h2 style="margin-bottom:16px">Sketches · {d[3:].replace("_", " ")}</h2><img class="contact" src="{img(os.path.join(BR, "03_Sketches", d + "_contact_sheet.png"))}">'))
    return pp


def back():
    pp = []
    for d in DIRS:
        k = d[:2]
        f = os.path.join(BR, "04_Directions", d, f"{k}_system_sheet.png")
        note = REC["system_notes"].get(k, "")
        pp.append(page(f'<img class="sheet" src="{img(f)}"><div class="cap sm"><p>{esc(note)}</p></div>', "", f"ARENA · {k} system: three circle modes, three lockups, six poses"))
    pp.append(page(f"""<h2>Status colour and the brand colour</h2><div class="cols sm" style="grid-template-columns:1.2fr 1fr">
      <div>{''.join(f'<p style="margin-bottom:12px">{esc(x)}</p>' for x in REC['status_note'])}</div>
      <div><table><tr><th>Status</th><th>Product colour</th><th>Cue without colour</th></tr>
      <tr><td>Live Now</td><td><span class="pill" style="background:#1fbf6a;color:#06210f">green</span></td><td>pulse + filled badge</td></tr>
      <tr><td>Available</td><td><span class="pill" style="background:#d6efe0;color:#0d3b22">green tint</span></td><td>plain mark</td></tr>
      <tr><td>Limited</td><td><span class="pill" style="background:#f2b53a;color:#3a2600">amber</span></td><td>half badge</td></tr>
      <tr><td>Fully booked</td><td><span class="pill" style="background:#e5484d;color:#fff">red</span></td><td>X badge</td></tr>
      <tr><td>Unavailable</td><td><span class="pill" style="background:#c9c9c9;color:#222">gray</span></td><td>dimmed + minus</td></tr></table></div></div>"""))
    pp.append(page(f"""<h2>Independent review</h2><div class="cols sm" style="grid-template-columns:1fr 1fr">
      <div><h3>Ranking (reviewer who didn't make the work)</h3><ol style="padding-left:22px">{''.join(f'<li>{esc(x)}</li>' for x in REC['ranking'])}</ol></div>
      <div><h3>Fixed after review</h3><ul>{''.join(f'<li>{esc(x)}</li>' for x in REC['fixed'])}</ul></div></div>"""))
    pp.append(page(f"""<h2>Recommendation</h2><div class="cols" style="grid-template-columns:1.1fr 1fr">
      <div><p style="font-size:26px;line-height:1.35;letter-spacing:-.01em">{esc(REC['recommendation'])}</p></div>
      <div class="sm">{''.join(f'<p style="margin-bottom:12px">{esc(x)}</p>' for x in REC['recommendation_detail'])}</div></div>"""))
    pp.append(page(f"""<h1 style="font-size:64px">Your pick</h1><div class="sm" style="margin-top:36px;max-width:980px">
      <p>Reply with one direction (D1–D7), or a hybrid (for example "D5 wordmark with the D3 status system"). Everything after this page (refining the pick, the full colour and type systems, icons, badges, tournament kit, social and store assets at exact sizes, the guidelines PDF) waits for your choice.</p>
      <p style="margin-top:18px;color:#9d9a92">Passing the distance check means a mark isn't a near copy of the 96 references it was measured against. It is not a legal clearance: a trademark search in classes 9, 35, 41 and 42 is still needed, especially as other "Arena" apps exist in Nigerian sport.</p></div>""", "ink"))
    return pp


def write(pages, path):
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    open(path.replace(".pdf", ".html"), "w").write(html)


def main():
    write(front(), os.path.join(OUT, "front.pdf"))
    write(back(), os.path.join(OUT, "back.pdf"))
    subprocess.run(["node", os.path.join(HERE, "print_pages.mjs"), os.path.join(OUT, "front.html"), os.path.join(OUT, "back.html")], check=True)
    w = PdfWriter()
    for f in [os.path.join(OUT, "front.pdf"), os.path.join(BR, "05_Logo_Book", "book", "logobook.pdf"), os.path.join(OUT, "back.pdf")]:
        for pg in PdfReader(f).pages:
            w.add_page(pg)
    dst = os.path.join(BR, "05_Logo_Book", "ARENA_Logo_Book.pdf")
    w.write(dst)
    print("wrote", dst, len(w.pages), "pages")


main()
