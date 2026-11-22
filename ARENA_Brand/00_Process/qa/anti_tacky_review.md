# ARENA logo directions: anti-tacky review

Reviewer: independent brand-identity critique (not the author of the work). Date: 2026-11-22.
Inputs reviewed: `04_Directions/ARENA_directions_overview.png`, all seven `D*_system_sheet.png`, every `recipe.json` and `build/check.json`, `01_Research/competitive_audit.md`, `01_Research/visual_direction.md`, and the moodboards. Each mark was also downsampled from the overview to 16 px and 32 px, and each wordmark to about 22 px cap height, to check how it holds up small.

Contrast figures are WCAG ratios that I computed from the recipe hex values. The status semantics are: green = Live/Available, amber = Limited, red = Fully Booked (signal `#E5484D`), gray = Unavailable.

---

## 0. The headline problem

The marks are not the main source of tackiness here. **The system around them is.**

1. **Five of seven brand accents sit in, or next to, a status hue.**

   | Direction | Accent | Hue | Clashes with |
   |---|---|---|---|
   | D1 | terracotta `#C8553D` | 10° | Fully Booked red at 358° (only 1.11:1 apart) |
   | D2 | hot pink `#FF4F9A` | 334° | red, 24° away |
   | D3 | `#22E27A` | — | it *is* the Live status green |
   | D4 | gold `#C9A24A` | 42° | amber/Limited |
   | D7 | lime `#B8FF2C` | 80° | reads as "available" on a map |

   Your own audit (§3.5) says the brand primary must sit **outside** those four hues. Only D5 (violet) and D6 (sky blue) comply.

2. **Every direction (D1–D6) wears the same status template.** It has a square or round badge top-right, the whole mark repaints red for "full", and a gray mark for "closed". That makes the "system" look generated rather than designed.

   It also has two functional bugs:
   - A badge in the top-right corner of an app icon reads as a permanent **iOS notification badge**.
   - Repainting the *logo* red for Fully Booked means the brand itself turns into an error state.

3. **The research contradicts itself.** `visual_direction.md` §(d) makes Pitch green and Live green the hero colours, while `competitive_audit.md` §3–4 says to go violet and stay out of green. D3 followed one document and D5 followed the other. Pick one before the book goes out. My vote is violet. The reasons are below.

---

## 1. Per direction

### D1 Court Lines: monoline custom wordmark, trapezoid "key" A, floating E bar

**SAD: Simple 4 · Appropriate 3 · Distinct 2 = 9/15**

**Strong**
- It is the most "premium" and restrained of the seven. A real custom wordmark, not a font with tracking.
- Stem discipline is good: verticals 14, horizontals 13 (a correct optical compensation), and the N diagonal comes out at about 14.4 perpendicular. It is calm and legible at 22 px cap height.

**Weaknesses**
- **The idea dies below about 48 px.**
  - At 16 px the A is just a slightly flat-topped A. The "basketball key" reading needs explaining even at full size.
  - The floating E bar, at 27 × 13 with a 7-unit gap to the spine, reads as `AR[-NA` or `AR:NA` at small sizes. At favicon size it is a smudge.
- **The A is a trope.** A flat-topped trapezoid A is audit trope #5 (A-triangle/tent), and it edges toward the arena swimwear "sharp triangle a" that the audit says to avoid.
- **The A is too wide for the word.**
  - A is 80 units wide; N is 72, E 54, R 68. Its 36-unit flat apex (x 22→58) makes it look bottom-heavy and block-like next to the narrow E.
  - The two As also bookend the word with mass while the middle (E with no middle arm) goes hollow, so the word has a hole in it.
- **Diagonal logic is inconsistent.** There are three different diagonal angles: A legs dx 22/100, R leg dx 28.5/100, N dx 55.5/100. A monoline system wants at most two.
- **Spacing is uneven.**
  - Gaps are A–R 5, R–E 11, E–N 15, N–A **4**. The N–A pair collides; you can see it in the overview row.
  - E–N looks wider than it measures because the E is open on the right.
- **Colour has two problems.**
  - Terracotta `#C8553D` against the signal `#E5484D` is **1.11:1** with a 12° hue difference, so they are indistinguishable for most users and fully merged for protan/deutan viewers.
  - The "live" pose uses terracotta, not Live green. That directly contradicts the UI semantics.
- **The status poses repaint the A red for "full"**, so the logo becomes an error message.

**Fixes**
1. Narrow the A apex from 36 to 24 units (x 28→52). Pull both legs in so the A is 72 wide, matching N.
2. Unify diagonals to two angles: A at dx 22 and R/N at a single dx of about 40.
3. Respace the word:
   - Set the E–floating-bar gap to 10 units (from 7) and lengthen the bar to 34 (from 27), in **ink**, so the E survives small sizes.
   - Use the accent bar only at ≥ 64 px display sizes.
   - Kern N–A to 8 (from 4) and A–R to 7 (from 5). Measure optically, not by bounding box.
4. Replace terracotta with violet `#4B2BFF`, or keep laterite as a *marketing-only* colour and never use it in the mark.
5. Use the full ARENA wordmark as the primary logo, not the lone A. As an app icon, the A alone has no idea left.

---

### D2 Match Day: condensed chamfered jersey-block wordmark

**SAD: Simple 3 · Appropriate 3 · Distinct 3 = 9/15**

**Strong**
- It has real street-energy and real attitude: stadium signage and shirt numerals.
- The heaviest letterforms give it the most presence on a poster or kit.
- Stems are a consistent 19 throughout.

**Weaknesses**
- **The A reads as a house with a door.** The gabled window counter over a rectangular "door" cut (20 × 40) is literally a home icon. At 16 px it reads as a house, a tombstone, or an "H" with a hat.
- **In the status poses the badge covers the chamfered shoulder and the A becomes an H.** Look at the "live", "booked" and "full" tiles: they say **H**.
- **Corner logic is inconsistent.**
  - A has two 15-unit chamfers; R has one chamfer plus an odd 7-unit inward notch at (109, 51).
  - E and N are dead-square slabs.
  - The family looks like it was assembled from two fonts.
- **E construction is fussy.** A solid block with two 25-high slots plus a 10 × 16 notch trimming the middle arm. At 16 px both slots fill in, giving a black rectangle.
- **The word is too dense.**
  - Ink share is 0.69, the heaviest in the set. Counters (20) barely exceed stems (19).
  - Letter gaps are 6/6/7/6. At app-store sizes the word clogs into a barcode.
- **Copying risk.** The nearest-reference score is **0.756 against a 0.791 limit**, the closest to a third-party reference of any direction.
- **Colour has three problems.**
  - Hot pink `#FF4F9A` on paper is 2.56:1 and fails even the 3:1 graphics threshold.
  - It sits 24° from the Fully Booked red, a 1.27:1 luminance difference. Pink badges next to red badges in the UI will blur together.
  - Pink plus condensed caps is the 2022 "hype poster" template seen in the cautionary moodboard pins.
- **Category trope.** Condensed caps are what the audit calls the exhausted "pitch dialect / italic speed" territory (minus the italic).

**Fixes**
1. Replace the rectangular door with a 12-unit-high gap at the foot, or remove the crossbar cut and keep a closed counter, to kill the house reading.
2. Pick one corner rule: chamfer **every** outer top corner at 15 units (A, R, E, N), or only the two As.
3. Drop the R notch and the E's 10 × 16 trim.
4. Open the counters to 24 (stems stay 19) and set letter gaps to 9 units.
5. Swap pink for violet, or accept pink as a marketing colour only and never put it in UI badges.
6. Rebuild the A so it diverges further from the 0.756 reference before anything is filed.

---

### D3 Live Pin: map pin with a carved stadium and a live dot

**SAD: Simple 3 · Appropriate 3 · Distinct 1 = 7/15**

**Strong**
- It is the most literal expression of the product ("there's a game near you, it's on now").
- The construction is competent: a clean circle-plus-triangle pin and a properly concentric racetrack. The live dot has a halo, so it does not merge.

**Weaknesses**
- **A pin-as-logo is trope #4.** Every local-discovery app uses one (Playfinder, Google/Apple Maps grammar). In the map UI it will be literally indistinguishable from the venue pins it sits among. A brand that is also a UI glyph loses both jobs.
- **The pin reads as a face.** The racetrack-in-a-pin reads as a **robot or astronaut visor**, a toggle switch, or a sports-car steering wheel. Combined with the dot, it is a Discord/Android-ish bot head.
- **The live dot sits where an iOS notification badge sits.** On the home screen, ARENA will look like it permanently has an unread notification. Apple's HIG explicitly discourages faking badges.
- **Colour is the worst-placed in the set.**
  - The brand accent *is* the Live status green `#22E27A`, so every brand surface says "available".
  - Pitch green + Chalk + Live green is close to **green-white-green** (NFF/Super Eagles trade dress) and to **Bet9ja/Betway green**. Audit §3.4: "sport + green reads as a betting app."
  - With the red Fully Booked pose it becomes green + red, which the audit flags as PDP/Labour Party drift.
  - White on Live green is only 1.52:1.
- **The type is a default.** Bricolage Grotesque 700 set with +10 tracking is a font, not a wordmark. Its quirky ink-traps fight the geometric pin. It also sits at least 0.55 × mark height away, which is too loose.

**Fixes**
- If kept at all, demote it to a **product map-pin / "Live now" glyph** inside a different brand.
- If it must be the logo:
  - Remove the dot from the resting mark. Show Live only in product.
  - Recolour Pitch green to ink or violet.
  - Close the racetrack to a solid "stadium" bar (counter height 8 → 6) to lose the visor face.

---

### D4 Convergence Crest: tournament bracket carved into a shield

**SAD: Simple 2 · Appropriate 2 · Distinct 2 = 6/15**

**Strong**
- The idea (four entrants converge to one winner, a "verified" venue) is the most conceptually complete of the symbols.
- Navy reads as trust.

**Weaknesses**
- **The shield is on the avoid list twice.** "Shield crests that mimic football clubs" (visual_direction §e) and trope #9 (audit §7).
- **The bracket does not read as a bracket. It reads as:**
  - a **trident** (Maserati, the Barbados flag);
  - a **pitchfork**, which is a real liability in Nigeria's strongly evangelical market (devil iconography);
  - a **menorah/candelabrum** (an unwanted religious reading);
  - the Greek **Ψ**;
  - a circuit trace.

  At 16 px it is a white blob in a shield.
- **The bracket strokes are far too thin.** Cut strokes of 3.5/48 (7.3%) become about 1.2 px at 16 px, so the internal geometry mushes.
- **The stem nearly splits the shield.** It runs to y 41 against a tip at 46.5, leaving a 5.5-unit sliver, so the shield nearly breaks in two and looks fragile.
- **The shield profile reads as a stock vector.** Top corners are square while the bottom is soft Béziers.
- **Navy + gold reads as FirstBank Nigeria / legacy banking and insurance**, not "energetic". Gold `#C9A24A` (hue 42°) sits in the **amber/Limited** status band.
- **The wordmark is generic.** Archivo 800 extended at +40 tracking looks like a corporate default. Its weight barely matches the shield.

**Fixes**
- Don't take it forward.
- If the bracket idea survives, use it as a hairline **graphic device** (the research already allows "the bracket line" as a layout device):
  - Strokes of at least 6/48.
  - No shield.
  - Stem stops at y 36.
  - Two tiers only (two into one) to kill the trident.

---

### D5 Pin in the A: heavy arch wordmark, pin counter in the first A, live dot in the last A

**SAD: Simple 3 · Appropriate 4 · Distinct 4 = 11/15**

**Strong**
- It is the only direction where the word itself carries the idea. It fits the audit's own white-space note: "an A built from an arena bowl rather than a triangle".
- The arch A reads as a stadium tunnel/gate and as an enclosure, which is a culturally neutral and positive shape.
- It is heavy and warm with real street confidence, but its geometry is controlled. Stems are 21 throughout; the arcs are true circles.
- The palette complies with the audit: violet + bone + ink, outside all status hues, not a party colour, not betting.
- It is the most ownable thing in the set.

**Weaknesses**
- **The pin counter creates unintended readings.**
  - Arch silhouette + pin counter + notch = **keyhole / padlock** (a security app) or a **tombstone**. At 16 px it is unmistakably a keyhole.
  - It is also the pin trope (#4) again, just hidden in a letter.
- **The crossbar is starved.** The pin tip ends at y 75 and the foot notch starts at y 84, leaving a **9-unit crossbar against 21-unit stems**. At small sizes the pin tip visually touches the notch and the A splits into two legs.
- **The last A reads as an eyeball, a camera lens, or Ω.** Its ring counter with a violet dot also differs from the first A, so the word looks inconsistent rather than intentional unless you read the story. Two ideas (find + live) in one five-letter word is one too many.
- **The R has a squared inner counter** (rect 107–124 × 21–41 merged with an r10 circle). It is the only square counter in a round-countered word.
- **E arms are uneven.** Top and bottom are 54, the middle is 48 (fine), but the arm height of 19 against stems of 21 makes the E look lighter than its neighbours.
- **Spacing is uneven.** Gaps are A–R 6, R–E 9, E–N **12**, N–A 6. The hole between E and N is visible in every lockup.
- **Colour has two contrast failures.**
  - Violet on ink is **2.83:1**, which fails 3:1. The "violet" lockup strip on the system sheet sets **ink type on violet**, which is illegible in sunlight.
  - The live dot on a dark field relies on its paper ring.
- **It shares the status-template issues** (iOS badge; the whole A goes red for "full").

**Fixes**
1. Raise the pin so its tip lands at y 69 (from 75), or shorten the notch so it starts at y 88. Target crossbar ≥ 15 (≈ 0.7 × stem).
2. Better still, **drop the pin**: give the first A a plain round counter (r 19 at cy 42, like the last A). The arch alone is the idea.
3. Keep the lit spot in the last A only, as the single colour moment.
4. Replace the R's square counter with a round r10 bowl counter.
5. Respace to optical gaps of about 9 between straight pairs and about 6 next to round shoulders. Specifically, change E–N from 12 to 9 and R–E from 9 to 8.
6. Colour rule: on violet fields always use **bone type** (5.88:1). Never use ink on violet.

---

### D6 Centre Light: split centre circle plus lit spot

**SAD: Simple 5 · Appropriate 3 · Distinct 3 = 11/15**

**Strong**
- It is the simplest and most robust shape in the set. One ring, one cut, one dot.
- It passes the "one operation" test, survives 16 px best of all seven, and works stencilled on a court wall, embroidered, and mono.
- It is sport-agnostic (centre circle, centre court, tip-off, kick-off).
- It is the only symbol with a premium, non-template feel.

**Weaknesses**
- **The split ring reads as other things.**
  - A ring split by a vertical bar reads as **I/O / a power button**, a target/crosshair, a lifebuoy, or "( • )".
  - Rotated 90° it becomes a **Pokéball**, so never rotate it.
  - The crosshair reading (target + dot) is the most damaging. It needs the halfway line to be clearly a *line*, not a sight.
- **The cut is too thin.** Its width of 4/48 (8.3%) is about 1.3 px at 16 px. In the downsample the split nearly vanishes and the mark becomes a donut.
- **Ring proportions are off.** The ring width of 10 against an inner radius of 11.5 makes it slightly bloated. The 5-radius dot leaves a 6.5 gap, close to ring width but not equal, so the system has no single module.
- **The palette is "trusted tool" blue** (audit §3.3: Sofascore, CourtReserve, Paystack/Stripe).
  - Sky `#58C7FF` on navy is cold, not energetic, and carries zero Lagos.
  - Light blue + white + the app's status green is the **APC palette** the audit flags as political.
  - Sky on paper is 1.68:1.
- **The wordmark is generic.** Sora 600 at +30 tracking is an off-the-shelf geometric. It also reads "tech start-up" next to the symbol, whose 21% stroke weight is much heavier than the type.

**Fixes**
1. Widen the cut from 4 to 6 (12.5%).
2. Unify the module: ring width 9, inner radius 12, dot radius 5, and dot-to-ring gap 7 to match the cut so cut, gap and stroke relate.
3. Optionally extend the halfway line 2 units beyond the ring at top and bottom so it reads as a pitch line, not a sight.
4. Recolour to the D5 palette: ink, bone, and **violet as the lit spot**.
5. Pair it with a drawn wordmark (see §3), not Sora.

---

### D7 Pixel Scoreboard: pixel pin mascot cloned from GhostRevenue, lime on ink

**SAD: Simple 3 · Appropriate 1 · Distinct 2 = 6/15**

**Strong**
- It is the only direction with real personality and a working pose system. The faces make statuses instantly emotional.
- The pixel grid is internally consistent at 2.75 units throughout, and it holds 16 px perfectly because it is already pixels.
- The client asked for it, and as a sticker or empty-state illustration set it is genuinely useful.

**Weaknesses**
- **It hits four items on the research's own avoid lists at once:**
  - neon lime on black (trope #3, avoid list line 1);
  - a mascot in the mark (avoid list);
  - a pin as logo (trope #4);
  - LED / "VR-neon" futurism.

  This is the exact "hype dialect / betting" look the audit says Nigeria reads as a bookie.
- **Lime-on-navy/black is Playtomic's look** (lime `#D4FF3A` on navy), and Playtomic is the closest global competitor. It is also Veo's accent.
- **Cloning another client brand's system** produces a portfolio sameness. Anyone who knows GhostRevenue will see a reskin, and it undermines "Trusted".
- **The face reads as an alien, skull or ghost head**, not a pin. The "booked" pose (red, X-eyes) is the **dead** emoji, and it uses signal red, which in the UI means *Fully Booked*, not "you're booked". That is a semantic error.
- **The lime is unusable on light fields.** Lime on bone is **1.10:1**, so it disappears and the light-mode mark has to fall back to ink. At hue 80°, lime on the map will read as "available".
- **The wordmark is a cliché.** Lowercase "arena." with a coloured full stop is the most over-used start-up device of the decade; it appears on the moodboard itself (kaiko.). Familjen Grotesk at −30 tracking crowds e/n.
- **The three-pixel sparkle** (2.75 units) is invisible below 32 px.

**Fixes**
- Do not use it as the master brand.
- Keep the pixel pin as a **secondary character and illustration system** (empty states, loading, stickers):
  - Recolour to violet/bone.
  - Make "booked" a happy/check face in violet; red X-eyes only for "full", and only in UI.
- If the client insists on it as the logo, change the accent to a non-status colour and drop the full stop.

---

## 2. Cross-direction issues

1. **One palette recipe repeated seven times.** It is warm cream or bone paper + near-black + one saturated accent. That is the default 2024–26 "AI brand kit" look, and six of seven directions use it. Combined with identical sheet layouts (three circles, three strips, six tiles), the book will look generated. Vary the presentation per direction and show real applications: iOS icon at 60 px and 29 px, a map pin, a shirt, a court wall, a WhatsApp avatar.
2. **The identical status-badge template** is duplicated across D1–D6.
   - It mimics the iOS notification badge.
   - It occludes letterforms (D2's A becomes an H).
   - It repaints the logo red.

   Status belongs in the UI chips and map pins, not in logo poses. Reduce the "poses" to: resting mark, plus **one** live state (the spot or dot animates to Live green in product only).
3. **The pin appears in three of seven directions** (D3, D5, D7), even though it is trope #4 in your own audit.
4. **Dots are everywhere.** There is a live dot or spot in D3, D5, D6 and D7, plus the full stop in D7. The "one colour moment" idea is right; four versions of it is a tic.
5. **Off-the-shelf type in four symbol lockups** (Bricolage, Archivo, Sora, Familjen). Each is set with flat tracking and no kerning, and none is weight-matched to its symbol. That is the main source of the "AI-made" feel in the lockups.
6. **Accents collide with the status hues** (see §0). Only violet (D5) is genuinely clear. Sky blue (D6) is clear of status hues but trips the political and "tool-blue" problems.
7. **The research disagrees with itself** (green hero in visual_direction versus violet in the audit). That must be resolved and written into the book.

---

## 3. Ranking and recommendation

| Rank | Direction | SAD | One-line verdict |
|---|---|---|---|
| 1 | **D5 Pin in the A** | 11 | The most ownable: the word *is* the arena. It needs the pin removed and the crossbar fixed. |
| 2 | **D6 Centre Light** | 11 | The best symbol craft and small-size survival, in the wrong palette and with a generic font. |
| 3 | D1 Court Lines | 9 | Tasteful but generic. Its idea vanishes at small sizes, and terracotta clashes with Fully Booked. |
| 4 | D2 Match Day | 9 | Energy without trust. The house/H reading, pink, and the copying risk count against it. |
| 5 | D3 Live Pin | 7 | Category-generic pin, betting/flag green, a fake notification badge. |
| 6 | D4 Convergence Crest | 6 | Shield cliché, trident/pitchfork/menorah readings, banking palette. |
| 7 | D7 Pixel Scoreboard | 6 | Breaks four avoid-list rules, is a cloned system, and lime equals Playtomic or a bookie. Keep it as a character set only. |

**Recommendation: take D5 and D6 forward as one hybrid**, named precisely:

> **"Arch & Centre Light"**
> - **Wordmark:** D5's arch wordmark with the pin removed. Both As get round counters; the last A keeps the lit spot.
> - **Symbol / app icon:** D6's split ring, with the cut at 6 units and a unified module.
> - **Palette:** D5's ink `#0E0E12`, bone `#F3EEE4`, violet `#4B2BFF`. The lit spot is violet at rest and turns Live green **only** when something is actually live, in product.

Why the hybrid is stronger than either direction alone:
- The arch A and the centre ring share the same circle geometry, so the wordmark and symbol rhyme.
- The lit spot links them: it is the counter of the last A and the centre of the ring.
- The pin trope disappears.
- The palette clears every status, betting and party collision.

The fallback, if the client wants a lighter, more premium wordmark, is the D6 symbol + D1 wordmark in violet. To make that work:
- Thicken D1's stems from 14 to 17/100 to match the ring's weight.
- Restore the E bar in ink.

---

## 4. Must fix before the logo book (most important first)

1. **Take brand colour out of the status hues everywhere.**
   - Lock violet `#4B2BFF` as the brand accent and retire terracotta, pink, Live green, gold and lime as *mark* colours.
   - Resolve the visual_direction vs competitive_audit contradiction in writing.
2. **Kill the shared status-badge template.**
   - No top-right badges on the mark (they look like iOS notification badges).
   - No red or gray repaints of the logo.
   - Status lives in UI chips and pins. The only mark state is the resting mark plus a live spot shown in product.
3. **Remove the map pin from the lead direction.**
   - In D5 it reads as a keyhole/tombstone and starves the crossbar to 9 against 21-unit stems.
   - If the pin stays anyway, the crossbar must be at least 15.
4. **Fix the D6 split.**
   - Cut from 4 to 6/48.
   - One module for ring, gap and cut.
   - Never rotate it, because a horizontal split reads as a Pokéball.
   - Check the crosshair and power-button readings at 29 px.
5. **Respace the custom wordmarks optically.**
   - D5: E–N 12 → 9, R–E 9 → 8, and replace the square R counter with a round one.
   - D1: N–A 4 → 8.
   - Show a 22 px test.
6. **Contrast rules in the book.**
   - Never set ink on violet (2.83:1); always use bone on violet (5.88:1).
   - Never set an accent on paper below 3:1 (D2 pink 2.56, D6 sky 1.68, D7 lime 1.10).
7. **Replace off-the-shelf lockup type with a drawn, weight-matched wordmark** (derive it from D5). No flat +30/+40 tracking, and no lowercase-plus-full-stop.
8. **Clear the cultural and resemblance flags in the book's rationale.**
   - D4: trident / pitchfork / menorah, and FirstBank navy-gold.
   - D3: flag and betting green.
   - D6: light blue + green + white reads as APC.
   - D2: house/H reading, and a 0.756 reference distance, too close to the limit to file.
   - D7: alien/dead face, and the Playtomic and GhostRevenue sameness.

   Mark which ones are fixed and which are retired.
