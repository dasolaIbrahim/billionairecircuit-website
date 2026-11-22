# ARENA — App Store Research & Platform Specs

**Date:** 22 Nov 2026 · **Phase:** 01 Research (brief item 4.4) · **Companion:** `competitive_audit.md`

**Evidence key**
- ✔ = verified this session against an official page.
- ◐ = third-party guide (2026), consistent across sources.
- ○ = strategist knowledge.

Store-pattern observations come from the strategist's knowledge of the 2025–26 stores. The listings were not screen-captured this session.

---

## 1. Icon silhouettes: top sports, booking, fitness, maps & ticketing apps

| App | Silhouette | Read at 29 px |
|---|---|---|
| Strava | White chevron pair on a solid orange field | Excellent. One abstract symbol, one colour |
| Hudl | White lowercase wordmark on orange | Fair. Text shrinks |
| Playtomic | Single letter/glyph on dark field | Good |
| Playo | Wordmark/“p” on green | Fair. Reads as yet another green sports app |
| Sofascore | White glyph on electric blue | Excellent |
| FotMob | Ball/“f” on green | Fair |
| OneFootball | White mark on black | Good |
| LiveScore | Orange letters on black | Good, but it shares the betting-app look |
| start.gg | Four-colour quadrant square | Excellent. A geometric symbol |
| Eventbrite | Orange “e” | Good |
| Google Maps | Multicolour pin | Excellent, and owned by Maps. Do not imitate |
| Nike Run Club / Nike Training | Black tile + white swoosh/wordmark | Excellent, and owned by Nike |
| Bet9ja / SportyBet / Betway (NG Top Charts neighbours) | Green or red tile with letters/ball | These are the icons ARENA will sit beside on Nigerian phones. Contrast is key |

**Patterns**
- Winners use **one flat symbol, centred, on a solid or near-solid field, filling about 55–65% of the canvas**.
- Wordmarks in icons are illegible in Spotlight, Settings and notifications. Apple HIG also discourages text unless it is essential.
- Category colour bands are orange (community sport), green (football/betting), blue (data) and black (media).

## 2. Store screenshot patterns

1. **Headline-over-device (dominant):** a 3–6 word benefit headline in heavy type at the top (e.g. "Book a court in 30 seconds"), with a device frame or a frameless UI crop below. Used by Playtomic, Strava, Sofascore and most booking apps.
2. **Full-bleed photo with UI overlay:** an action photo with a floating card (a booking confirmation or a score). Used by fitness and padel apps, and by Fever and Eventbrite for events.
3. **Panoramic "story strip":** the first 3 screenshots form one continuous image across the carousel. Effective in Search results, where only the first 3 portrait shots show.
4. **Bold type-only opener:** screenshot 1 is pure brand and type ("Your city's game is live"). Lifestyle brands use this. It is risky without awareness.
5. **Social proof:** "#1 in…" or ratings badges. Apple restricts misleading claims. Google Play's feature-graphic guidance discourages store badges and rankings (◐).

**Specific to Nigeria:** the store fills with betting apps that use money and odds imagery. Screenshots showing **real Nigerian players, real courts and naira pricing** build trust and stand apart.

## 3. Onboarding & splash patterns

- **Splash:** an icon symbol centred on the brand colour for at most 1 s, then a hand-off into the first screen. Strava, Sofascore and Playtomic all keep it minimal. Apple's guidance is that the launch screen should look like the app's first screen, not an ad.
- **Onboarding:** sport picker ("What do you play?" as chips with sport pictograms), then location permission explained by value ("See courts live near you"), then optional sign-in (Apple/Google/phone OTP; phone OTP is critical in NG), then the map.
- **Map-first home (Playo, Playtomic):** the map with status-coloured pins *is* the hero. ARENA's Live Now map should appear in screenshot 1 or 2.
- **Skeleton-loading and haptics** on booking confirmation are table stakes.

## 4. Ten rules for ARENA's icon, screenshots and splash

1. **One abstract symbol, no wordmark, no ball, no pin** in the icon. The ARENA enclosure/ring idea should be legible at 29 pt and in iOS **tinted / clear / dark** and Android **themed monochrome** modes.
2. **Brand field colour ≠ status colours.** The icon background must not be green, amber, red or gray. Use the ultraviolet/indigo territory so ARENA pops beside green and red betting icons.
3. **Design on Apple's 1024 × 1024 grid as layered vectors** (Icon Composer: background + 1–2 foreground layers, no baked shadows or glows). Export a 108 dp Android adaptive pair with the symbol inside the **66 dp safe zone** (logo 48–66 dp).
4. **Same symbol everywhere:** app icon, splash, map "you are here" puck, Live Now pulse and social avatar. One shape, many scales.
5. **Screenshot 1 = Live Now map** with a 3–5 word headline ("Find a game near you. Live."). Screenshot 2 = booking in two taps with ₦/$ pricing. Screenshot 3 = tournament bracket. Screenshot 4 = community/media feed. Screenshot 5 = venue owners ("List your arena").
6. **Headline system:** brand display face, sentence case, maximum two lines, high-contrast ink on bone or bone on ultraviolet. **Never** set the headline over busy photography without a scrim.
7. **Real local photography** (Lagos courts, night 5s, padel at golden hour) in a consistent grade. No stock athletes and no gradient-mesh backgrounds.
8. **Status semantics stay functional:** green/amber/red/gray appear only *inside* UI (pins, slot chips), never as decorative brand colour in screenshots or the splash.
9. **Splash ≤ 1 s:** symbol centred on the brand field, then a subtle "live pulse" ring animation into the map. Show the "by DAC Sports" endorsement on first launch only, small, at the bottom.
10. **Localise:** an English (NG) set first with naira and local venue names, then global sets. Keep every caption inside safe areas so a single 6.9" set scales to all iPhones. Provide alt text for Play graphics.

---

## 5. Verified platform specs (as of Nov 2026)

### Apple App Store / iOS

| Asset | Spec | Status | Source |
|---|---|---|---|
| App icon (iOS/iPadOS/macOS) | **1024 × 1024 px**, square, unmasked (system applies rounded corners), layered. Appearances: default, dark, clear light/dark, tinted light/dark. sRGB / Display P3 | ✔ (HIG changelog dated 28 Oct 2026) | https://developer.apple.com/design/human-interface-guidelines/app-icons |
| Icon format | Layered Icon Composer file preferred. A flat bitmap is allowed, and the system auto-segments it into 2 layers | ✔ | same |
| iPhone 6.9" screenshots ("Dynamic Island, large display") | **1320 × 2868**, 1290 × 2796, 1260 × 2736 (portrait; landscape reversed). The **6.7" size 1290 × 2796** sits in the same accepted set | ✔ | https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications |
| iPhone 6.5" ("Face ID, large") | 1284 × 2778, 1242 × 2688. Required if no Dynamic-Island-large set is provided | ✔ | same |
| iPhone 6.1"/6.3" ("Dynamic Island, medium") | 1206 × 2622, 1179 × 2556. Apple's page states at least one screenshot is required for this class (some third-party guides disagree; recheck at submission) | ✔ | same |
| iPhone 5.5" | 1242 × 2208 | ✔ | same |
| iPad 13" | 2064 × 2752 or 2048 × 2732. Required if the app runs on iPad | ✔ | same |
| General | JPEG/PNG, **no alpha**, 1–10 per size. App Store Connect scales the largest set down | ✔ | same |

### Google Play / Android

| Asset | Spec | Status | Source |
|---|---|---|---|
| Play Store icon | **512 × 512 px**, 32-bit PNG with alpha, ≤ 1024 KB | ◐ (Google help page content via search; direct fetch blocked) | https://support.google.com/googleplay/android-developer/answer/9866151 · https://developer.android.com/google-play/resources/icon-design-specifications |
| Feature graphic | **1024 × 500 px**, JPEG or 24-bit PNG (no alpha). Required to publish. Avoid device frames and store badges | ◐ (same) | same |
| Adaptive launcher icon | **108 × 108 dp** layers (foreground + opaque background, plus an optional monochrome layer for themed icons). **66 × 66 dp safe zone** never masked. Logo 48–66 dp. The outer 18 dp per side is reserved for masks and parallax. Android 16 QPR2 auto-themes apps without a monochrome layer | ✔ | https://developer.android.com/develop/ui/views/launch/icon_design_adaptive |
| Phone screenshots | 2–8; 320–3840 px per side; 16:9 or 9:16 (1080 × 1920 recommended) | ○ (known Play spec; not re-fetched) | Play Console help (above) |

### Social profiles (late 2026)

Platforms do not publish all of these. Figures are the 2026 third-party consensus, with conflicts noted.

| Platform | Profile image | Cover / header | Status / note | Sources |
|---|---|---|---|---|
| **Instagram** | 320 × 320 upload (displays ~110 px, circular crop) | n/a. Feed posts 1080 × 1350 (4:5); **profile grid is now 3:4, so 1080 × 1440 is recommended**; Stories/Reels 1080 × 1920 | ◐. The date of the 3:4 grid change varies by source (Jan 2025 to early 2026) | https://blog.hootsuite.com/social-media-image-sizes-guide/ · https://www.linearity.io/blog/instagram-size-guide/ · https://buffer.com/resources/social-media-image-sizes/ |
| **X** | 400 × 400 | **1500 × 500** (no animated GIF headers) | ◐ consistent | Hootsuite, Buffer (above) |
| **LinkedIn (personal)** | 400 × 400 | **1584 × 396**, ≤ 8 MB | ◐ consistent | Hootsuite, Buffer |
| **LinkedIn (company page)** | 300 × 300 logo | **1128 × 191** (≈ 5.9:1; 2256 × 382 for retina). Some guides still say 1128 × 376, which is outdated | ◐ majority | https://www.kontentino.com/blog/social-media-image-sizes/ · https://buffer.com/resources/social-media-image-sizes/ · https://www.digitalapplied.com/blog/social-media-image-sizes-2026-every-platform |
| **Facebook Page** | 320 × 320+ upload (displays 176 desktop / 196 mobile, circular) | **851 × 315** display (Buffer). Other guides say 820 × 312 desktop / 640 × 360 mobile. **Design at 1640 × 624 or larger** with key content centred in the 640 × 312 overlap | ◐ conflicting | https://buffer.com/resources/social-media-image-sizes/ · https://www.constantcontact.com/blog/social-media-image-sizes/ |

**Production advice:**
- Make the **ARENA symbol avatar** centred within an 80% circle-safe area, so it works on IG, X, LinkedIn and FB alike.
- Build covers with a **centred safe band** so one master can be cropped to 1500 × 500, 1584 × 396, 1128 × 191 and 1640 × 624.
- Re-verify all social sizes on each platform's help centre at launch. They change without notice.

### Not reachable this session

support.google.com (Play help, quoted via search), buffer.com and sproutsocial.com (quoted via search), www.instagram.com.
