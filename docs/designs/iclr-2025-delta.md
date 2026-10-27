# DELTA Stacked Cards — Style Reference

> Offprints pinned to a white board: every section its own rounded sheet with a soft grey halo.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, the page's `files/style.css`, three inline `<style>` blocks, and Bootstrap 3.4.1 (loaded last, after Bulma, so its heading and box-sizing rules win). The declared "Google Sans" never loads, so the page renders in the browser's default serif; that is what is described. Color share is measured on the first 1440×900 viewport.

## Overview

The page is a column of fourteen white cards, each 1000px wide with 15px corners and a soft `0 0 10px #999999` shadow, separated by 25px of white. The first card holds the hero: a bold two-line serif title in #333333, grey author links, black underlined affiliations, a 28px "ICLR 2025" line, and four bracketed text links "[Paper] [Arxiv] [Code] [BibTeX]" in grey. Under them, 800px looping videos show an input clip beside two "3D tracks" point-cloud views with coloured labels baked into the frames. Each later card opens with a bold 30px left-aligned heading (Abstract, Motivation, Method, results, applications) and holds one figure or video group and a justified 17.5px paragraph. The serif look is accidental (the font stack names only "Google Sans", which is not loaded), but it is what readers see, and it gives the page its academic-offprint feel.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 65.9% plus near-whites #fdfdfd 6.4% and #fbf9f8 3.2% (video backgrounds), warm taupe #998a7d 9.7% and plum-charcoal #413941 7.7% (the car and butterfly clips), sage #d2d9cc 5.7%. The card shadow and text are below 1%.

Anatomy in DOM order (card spans x=220–1220, content x=270–1170; body padding 28px; card top at y=53):

1. **Title** — `h1 > strong`, "DELTA: Dense Efficient Long-range / 3D Tracking for Any video" (forced `<br>`), 36px / 700 / line-height 43.2px, #333333, centred, rendered serif (y=98–184). Margin-bottom 10px.
2. **Authors** — `p#authors`, seven `span > a` with 10px side margins, 20px / 400 rendered, #777777, superscript numbers 14px; two centred lines (y=195–242). Gap 9px.
3. **Affiliations** — `.institution` links, 18px, #000000, underlined in grey, 15px apart (y=251–271). Gap 28px.
4. **Venue** — `span.conference`, "ICLR 2025", 28px / 400, #000000, centred (y=299–324). Gap 25px.
5. **Links** — `<font size=+2>` paragraph, four bracketed links 24px, #777777, separated by four `&nbsp;`, no icons (y=348–374). Gap 35px.
6. **Teaser videos** — `video.round`, 800px wide, centred (x=320–1120), first 800×208 at y=409, then 800×208 at y=642 and 800×178 at y=875, separated by `<br>` (about 25px). Labels "Input" (red on white chip) and "3D tracks (view 1/2)" (green) are inside the video frames.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Board | #ffffff | `body` | page background and card fill |
| Graphite | #333333 | Bootstrap `body` color | title, section headings, body paragraphs, captions |
| Link Grey | #777777 | inline `a, a:link` | author names, [Paper]/[Arxiv]/[Code]/[BibTeX], inline links |
| Ink | #000000 | `.institution a`, `.conference` | affiliation links (grey underline), "ICLR 2025" |
| Halo | #999999 | `.content` box-shadow | card shadow `0 0 10px` |
| Dash Grey | #737373 | `.divider`, `.divider_horizontal` | 2px dashed separators between comparison videos |
| Dot Grey | #dddddd | `.navDot`, `#prevButton` | carousel dots and round arrow buttons |
| Dot Active | #555555 | `.navDotSelected` | current carousel dot |

## Tokens — Typography

- **Card text:** declared `font-family: "Google Sans"` on `.content` (no fallback); body declares `sans-serif` and `'Open-Sans'` (misspelled, never matches). Rendered: Google Sans is not loaded, so cards render in the browser default serif (Times New Roman on Windows Chrome, Times on macOS). Substitute that keeps the rendered look: Tinos or Liberation Serif. If you want what the author intended: Google Sans → Product Sans or Inter.
- **Body outside cards:** sans-serif 14px (only reachable in empty margins).
- **Icons:** Glyphicons Halflings (carousel chevrons).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.content h1 > strong` | 36px / 700 / 43.2px (inline line-height 1.2) |
| Venue | `#authors .conference` | 28px / 400 |
| Section heading | `h2 > strong`, left aligned | 30px / 700 / 33px |
| Top links | `<font size=+2>` anchors | 24px / 400 |
| Authors | `#authors` | 20px / 400 (declared 300, serif has no 300) |
| Affiliations | `#authors .institution` | 18px |
| Body | `.content p` | 17.5px / 400 / 25px, justified |
| Result captions | `h4.title.is-3` | 18px Bootstrap h4 / 500, bold runs via `<strong>` |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Card | width 1000px (border-box), padding 25px 50px, margin 25px auto, radius 15px, shadow `0 0 10px #999999`, no border |
| Embedded viewer (`iframe`) | 27.5em square, radius 0.5em, shadow `0 0 1em 0 rgba(0,0,0,0.15)`, no border |
| Carousel arrows | 50% radius, #dddddd fill, padding 10px |
| Carousel dots | 10px circles, 5px side margins |
| Dashed dividers | 2px dashed #737373 |
| Videos and figures | square corners (`.round` has no radius rule) |

## Layout Metrics

- **Container:** fixed `.content` width 1000px centred, inner measure 900px (x=270–1170 at 1440); no max-width or fluid rule.
- **Page padding:** body 2em (28px); cards 25px apart (vertical margins collapse to 25px).
- **Hero card:** title margin 20px top / 10px bottom; authors margin-bottom 20px; links paragraph 10px bottom; teaser videos 800px wide, centred via `<center>`.
- **Section cards:** heading margin 20px 0 10px, figure `width: 100%` (900px) with -10px bottom margin, paragraph after one or two `<br>`.
- **Figures:** Motivation and Method are single 900px PNGs (the "table beside chart" is one image).

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1100px | (viewport − 1000)/2 | 17.5px | 36px | none |
| 769–1099px | 28px, card overflows | 17.5px | 36px | horizontal scroll; cards stay 1000px |
| ≤768px | 28px | 17.5px | 36px | only the embedded iframe goes to 100% width × 30em; everything else stays fixed |

## Components

- **Section card:** `div.content`, white, 1000px, padding 25px 50px, 15px radius, `box-shadow: 0 0 10px #999999`, heading 30px bold serif #333333 left aligned, one full-width figure, then a 17.5px justified paragraph with bold key phrases.
- **Bracket links:** plain text "[Paper]" style anchors at 24px #777777, separated by non-breaking spaces; no hover rule beyond Bootstrap's underline on hover.
- **Author line:** inline spans with 10px margins, grey links, 14px superscripts pulled tight (-2px right margin); affiliations as black links with a grey underline.
- **Labelled video triptych:** one wide video per row (800px) composed of input clip plus two 3D views; the labels are burned in, so no HTML captions.
- **Comparison block:** videos separated by 2px dashed #737373 vertical or horizontal dividers; Bulma `h4.title.is-3` captions with "Click here" links.
- **Viewer embed:** iframe 27.5em square, 0.5em radius, faint shadow, with icon-and-text instructions in a centred flex row (36px icons, 1.2em text).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | Yes | centred serif stack in the first card |
| Venue line | Yes | 28px black "ICLR 2025" |
| Link buttons | Present but non-standard | bracketed grey text links, no buttons |
| Teaser | Yes | stacked 800px input + 3D-view videos |
| Abstract | Yes | own card, justified |
| Motivation figure | Yes | table-and-chart PNG in its own card |
| Method figure | Yes | architecture PNG in its own card |
| Qualitative results | Yes | Bootstrap carousel and video grids |
| Comparisons | Yes | side-by-side videos with dashed dividers |
| Interactive 3D viewer | Yes | embedded iframe with instruction icons |
| Results table (HTML) | No (absent from the source) | numbers are in figures and the paper |
| BibTeX | Present but non-standard | link to a .txt file only |
| Footer | Yes | acknowledgements card crediting MonST3R and 4Real templates |

## Adapting to Other Content

- **More authors:** keep the inline span list and break lines manually with `<br>` every four names, as the source does.
- **Results table:** put it in its own card under a 30px bold heading; use 17.5px serif cells, a 1px #333333 top and bottom rule like a paper booktabs table, no fills.
- **Long publication or news list:** one card titled "News", entries as justified 17.5px paragraphs with the date bold.
- **Many result videos:** one card per comparison family, each with a single heading; separate items inside a card with the 2px dashed #737373 divider rather than new cards.
- **Narrow screens:** the source has no responsive rule; if reusing, change card width to `min(1000px, 100% - 32px)` and padding to 16px under 768px.

## Do's and Don'ts

- Do give every section its own card with the same radius and shadow; the stack is the identity.
- Do keep headings left aligned and bold inside cards, and only the hero centred.
- Do keep links grey and bracketed if you want the same plain academic tone.
- Don't add color to the chrome; the only hues come from point-cloud renders and figure labels.
- Don't declare a font with no fallback unless the serif fallback is what you want; name it explicitly instead.
- Don't nest cards; the source has an accidental nested `.content` at the footer that doubles the shadow.

## Surfaces

White page and white cards separated only by the 10px grey halo; no tinted bands. Carousel controls are flat #dddddd circles.

## Imagery

Wide composite videos (input clip plus rainbow-coloured 3D track point clouds on white), a paper-style table-and-scatter figure, a schematic architecture diagram with green and blue attention blocks and orange upsampler, comparison videos, and an embedded 3D viewer.

## Layout

A single fixed 1000px column of stacked cards, centred, hero card first. Rendered height about 8,000px.

## Agent Prompt Guide

Quick colors: page and cards #ffffff, text #333333, links #777777, affiliations and venue #000000, card shadow #999999, dashed divider #737373.

1. "Create a section card: 1000px wide, white, padding 25px 50px, 15px radius, box-shadow 0 0 10px #999999, 25px margin between cards; inside, a 30px bold Times New Roman heading in #333333 left aligned, a full-width figure, then a 17.5px justified paragraph with 25px line height."
2. "Build the hero card: centred 36px bold serif title in #333333 over two lines, authors at 20px in #777777 with 14px superscripts, affiliations at 18px in #000000 with grey underlines, a 28px 'ICLR 2025' line, and bracketed text links [Paper] [Arxiv] [Code] [BibTeX] at 24px #777777."
3. "Separate comparison videos inside one card with a 2px dashed #737373 line, and caption each group with an 18px line containing bold method names."

## Similar Pages

- MonST3R and 4Real project pages (the stated template sources) and other Snap Research pages using the `.content` card stack.
- Older Jon Barron–era pages that use fixed-width white cards with drop shadows.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --card: #ffffff;
  --text: #333333;
  --link: #777777;
  --ink: #000000;
  --halo: #999999;
  --dash: #737373;
  --font-card: 'Times New Roman', Tinos, serif;
  --title-size: 36px;
  --h2-size: 30px;
  --body-size: 17.5px;
  --body-lh: 25px;
  --card-width: 1000px;
  --card-pad: 25px 50px;
  --card-radius: 15px;
  --card-shadow: 0 0 10px var(--halo);
}
```

## Provenance

- **URL:** https://snap-research.github.io/DELTA/
- **Paper:** DELTA: Dense Efficient Long-range 3D Tracking for any video (arXiv 2410.24211), Tuan Duc Ngo et al.
- **Venue:** ICLR 2025 (stated on the page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the comment.
- **Template credit:** acknowledgements say the template is borrowed from MonST3R and 4Real.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 screenshots (first viewport and tall), `files/style.css`, inline style blocks, page HTML; 2026-10-28.
