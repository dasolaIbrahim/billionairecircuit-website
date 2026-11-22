# Reels De9BI8gNCXi (2026-10-26) and De5EVS_ySng (2026-10-24), account @quigsart ("Quigs Art")

Access (2026-11-22):
- yt-dlp read both posts' metadata from www.instagram.com, using both /reel/<id>/ and /reels/<id>/.
- The video files would not download. The proxy refused the CDN host with "403 Forbidden (agent proxy: no rule or network setting allows this host)". The video host was `scontent-ord5-2.cdninstagram.com` and the thumbnail host was `scontent-ord5-1.cdninstagram.com`.
- Neither post has captions or subtitle tracks.
- Listing the account's other reels (`instagram.com/quigsart/reels/`) failed with HTTP 429 Too Many Requests.
- WebFetch could not open www.instagram.com (the host is not in the allowed domains).
- I extracted no frames and looked at no images.

Caption on both posts: "From photo to the final logo process ✨ #logodesign #illustrator #logo #graphicdesign"

## What can be stated
- The genre is "photo to logo" in Adobe Illustrator: you start from a photograph of a real object, animal or person and finish with a flat vector mark.
- The two posts came out two days apart with the same caption, so they are probably a series using the same method on two subjects.

## Standard "photo to logo" Illustrator workflow (reconstructed from the genre, NOT observed in these reels)
1. Pick a photo with a strong, readable silhouette (side profile, high contrast).
2. Place it, lower its opacity to about 30-50% and lock the layer.
3. Simplify: block out the major masses only, either with the Pen tool (few anchors, placed at extrema, handles horizontal or vertical) or by laying circles and ellipses over the curves ("circle construction").
4. Combine with Shape Builder or Pathfinder (Unite, Minus Front). Delete the construction leftovers.
5. Use negative space: cut details such as eyes, separations or feather lines as gaps rather than drawing them as strokes.
6. Make the gaps and stroke weights consistent and snap to a grid. Round or sharpen the corners consistently.
7. Hide the photo and check the silhouette alone in solid black, then at small size.
8. Pair it with a wordmark, then present it on mockups.

## ARENA takeaways
- Treat the photo (a court, a ball, a player in motion, a stadium bowl) as underlay only. Never trace it literally; rebuild it from primitives.
- In code, the equivalent of "lower the opacity and draw over it" is: potrace the photo silhouette as a guide → fit circles and lines to it → rebuild with shapely or pathops → throw the trace away.
