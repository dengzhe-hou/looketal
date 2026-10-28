# WIR3D — Style Reference

> A lab notebook made of keycaps: a pale-blue title slab with a lab badge pinned to its corner, navy keys you could press, and pencil-line sketches floating on white.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, scrolled viewport shots at y=5200 and 6100, a probe of rendered elements (logo badge, title box, nav keys, gray boxes, captions, last section), and the page's own `style.css` and `index.html`. The two other linked stylesheets (`assets/css/styles.css`, `assets/css/Highlight-Clean.css`) return GitHub's 404 page, so they contribute nothing. Most sizes are set by stepped `min-width` media queries (100, 350, 430, 660, 900, 1281 and 1700px); the values below are those of the 1281px+ step that applies at 1440.

## Overview

A hand-built, airy page (about 6,900px tall) on plain white with a tactile "keycap" vocabulary: every box has a 10px radius, a solid offset shadow 4–5px below it in a darker shade of its own color, and a soft 3px 3px 15px drop shadow. The header is a lifted pale-blue (#e9f0f7) title slab holding a 42.4px Manrope title in charcoal #363636, with an 80px white "3DL threedle" lab badge overlapping its top-left corner and a row of keys hanging off its bottom-right edge: a light "📍 ICCV 2025" key and navy (#263966) Paper, arXiv and Code keys. Navy Manrope author names, a university line and a teaser strip of eight overlapping turntable videos (a small colored shape, then its large black-line sketch abstraction) follow. Every section is a centred Manrope h2 over figures or video galleries, with text in light gray (#f5f5f5) rounded boxes that use the same keycap shadow; the gallery sits as a sparse grid of colored source shapes beside their curve sketches. Acknowledgements, a template credit and the BibTeX are gray boxes too; there is no footer element.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 53.6% (plus #fffffe 1.8%, #fbffff 0.6%); the pale-blue title slab #ebf1f6 13.9%; gray boxes #f5f5f5 11.2% and #f9f9f9 3.9%; #dcdddf 8.0% and #90949b 7.1% are offset shadows, the nav keys and the gray sketch renders.

Anatomy in DOM order (desktop 1440px; body margin 8px; sections 1040px wide at x=200 with 35px side padding, content x=235 to 1205):

1. **Intro section** (`section.intro`, from y=8): padding 2px 35px 15px, Manrope 700 throughout.
2. **Lab badge** (`.logobox`, y=10–90, x=235): 80×80px white, 10px radius, shadow `0px 4px 0px 0px #aea9a3, 3px 3px 15px #23232348`; the 3DL logo image at 96% width. It sits absolutely, overlapping the title slab's top-left corner. Hover: `0px 0px 4px #537998` glow and a 1.5px downward nudge.
3. **Title slab** (`.titlebox`, y=50–283, x=288, 864px wide): margins 40px top and 52.8px sides (0.5 and 0.66 × the 80px icon size), background #e9f0f7, 10px radius, padding 3px 40px, shadow `0px 5px 0px` in `color-mix(in oklab, #e9f0f7 70%, #46579b 30%)` (renders #b4c1dc) plus `3px 3px 15px #23232348`.
4. **Title** (`h1`, y=77–251): Manrope 42.4px/700 (2.65rem), #363636, left-aligned in the slab, three lines; margins 0.57em top, 0.67em bottom.
5. **Key row** (`nav`, y=264–306): pulled up 18.72px so it overlaps the slab's bottom edge; flex, right-aligned with a 10% (97px) right margin, 10.5px column gap. Keys: Manrope 18.72px/700, padding 8px 20.97px, 10px radius. "📍 ICCV 2025" is #f5f5f5 with #363636 text and a `0px 4px 0px 0px #aea9a3` underside; Paper, arXiv and Code are #263966 with rgb(242,247,252) #f2f7fc text and a `0px 4px 0px 0px #4e649e` underside; all add `3px 3px 15px #23232348`.
6. **Authors** (`.authors`, y≈326): 80% wide flex row, Manrope 20.8px/700, names #263966 spread evenly (Richard Liu, Daniel Fu, Noah Tan, Itai Lang, Rana Hanocka); underline 2px on hover.
7. **Affiliation** (y=364): "University of Chicago", Manrope 18px/700 #363636, centred. The intro ends at y≈403.
8. **Teaser strip** (`section.teaser`, y=407–574): a 12-column grid at 85% width; four pairs of looping videos, each a 69px colored source shape raised 10px followed by a 137px sketch that overlaps it by 15px; 8px radius.
9. **Abstract box** (`p.graybox`, from y=612): #f5f5f5, 10px radius, padding 19.2px 25.6px, Source Sans 3 19.2px; bold "Abstract." then italic text in #363636. It crosses the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Charcoal | #363636 | --fore | title, h2 headings, body and box text, affiliation, venue key text |
| Navy | #263966 | --accent | Paper / arXiv / Code keys, author names, gallery prompt captions, `em` text |
| Navy Underside | #4e649e | --accent-shaded | 4px offset shadow under navy keys |
| Steel Blue | #537998 | --accentlight | key hover fill, hover glow ring |
| Title Blue | #e9f0f7 | --accentbg | title slab background |
| Title Underside | #b4c1dc | --accentbg-shaded (oklab mix, rendered) | 5px offset shadow under the title slab |
| Not-White | #f5f5f5 | --notwhite | gray text boxes, venue key |
| Warm Underside | #aea9a3 | --notwhite-shaded | 4px offset shadow under gray boxes, venue key and logo badge |
| Key Text | #f2f7fc | (literal rgb(242,247,252)) | text on navy keys |
| White | #ffffff | (page, `.logobox`) | page background, logo badge |
| Prompt Gray | #717171 | (literal, `.promptprefix`) | italic prompt prefixes in galleries |
| Drop Shadow | #23232348 | --dropshadow | soft 3px 3px 15px shadow on every box and key |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display (intro, h1, h2) | "Manrope", sans-serif (Google Fonts, 700 only) | Manrope 700 | Manrope |
| Text | "Source Sans 3", system-ui, -apple-system, sans-serif | Source Sans 3 variable 200–900, roman and italic | Source Sans 3 |
| Icons | Font Awesome 5, Academicons (inline @font-face) | Font Awesome 5 Free 900 / Brands 400, Academicons 400 | — |
| Math | MathJax | MJXTEX fonts | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.intro .titlebox h1` | 2.65rem = 42.4px / 700 / normal, left | #363636 |
| Section heading | `h2` | 2.3rem = 36.8px / 700, centred, padding 4px 19.2px | #363636 |
| Nav key | `.intro nav > *` | 1.17rem = 18.72px / 700 | #f2f7fc on navy; #363636 on venue |
| Authors | `.intro .authors` | 1.3rem = 20.8px / 700 | #263966 |
| Affiliation | `.intro .affiliations` | 18px / 700 | #363636 |
| Body / boxes | `p`, `.graybox` | 1.2rem = 19.2px / 400 / normal | #363636 |
| Abstract text | `.graybox i` | 19.2px italic | #363636 |
| Gallery caption | `.promptcaption` | 1.1rem = 17.6px italic | #263966 |
| Prompt prefix | `.promptprefix` | 17.6px italic, pencil icon at 50% opacity | #717171 |
| BibTeX | `.graybox` | 19.2px Source Sans 3 (no monospace) | #363636 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Logo badge | 10px | none | `0px 4px 0px 0px #aea9a3, 3px 3px 15px #23232348` |
| Title slab | 10px | none (declared `1px none`) | `0px 5px 0px #b4c1dc, 3px 3px 15px #23232348` |
| Navy keys | 10px | none | `0px 4px 0px 0px #4e649e, 3px 3px 15px #23232348`; hover fill #537998, `0px 0px 4px #537998, 3px 3px 15px #23232348`, translate(0, 1.5px) |
| Venue key | 10px | none | `0px 4px 0px 0px #aea9a3, 3px 3px 15px #23232348` |
| Gray boxes (`.graybox`) | 10px | none | `0px 4px 0px 0px #aea9a3, 3px 3px 15px #23232348, 0px 0px 10px rgba(0, 0, 0, 0.2)` |
| Teaser videos | 8px | none | none |
| Widget boxes (`.widgetbox`) | 10px | none | as navy keys |

## Layout Metrics

- **Sections**: every `section` is `width: calc(50vw + 280px - 30px)` = 970px content plus `padding: 15px 35px` → 1040px boxes at x=200 (centred by `margin: 4px auto`); body keeps the default 8px margin.
- **Intro**: `--iconsz: 80px`; title slab margin-top 40px, side margins 52.8px, padding 3px 40px; key row pulled up by 1 × 18.72px and right-aligned with a 10% right margin; authors 20px top / 10px bottom margin, 80% width.
- **Width helpers** at this step: `--medwidthflex-w: 85%` (figures, teaser), `--halfwidthflex-w: 49%`, `--eqnwidthmult: 0.55`.
- **Teaser**: grid `repeat(12, 1fr)`, gap 0, items aligned to the bottom; odd videos span 1 column and are raised 10px, even videos span 2 and overlap by -15px.
- **Galleries**: `.qtrwidthflex` items 24.5% wide (half of 49%), margin 10px auto, source video 32% and result 66% of each item; caption below.
- **Gray boxes**: padding 19.2px 25.6px, separated by the 4px section margins; headings sit about 70px above their boxes.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1281px | 35px; section 50vw + 250px | 19.2px | 42.4px (h2 36.8px) | keys 18.72px; authors 20.8px; figures 85% |
| 900–1280px | 30px; section 60vw + 160px | 19.2px | 38px (h2 32px) | keys 17.6px; authors 20px; figures 90%; nav right-aligned |
| 660–899px | 25px; section 72vw + 50px | 19.2px | 29.6px (h2 28.8px) | icon 68px; keys 16.8px; nav centred above authors; figures 92.5%; teaser grid 6 columns (≤900px) |
| 350–659px | 20px; section 92.5vw - 30px | 19.2px | 25.6px (h2 24.8px) | icon 48px; keys 14.4px, single row from 430px |
| <350px | 15px; section 94.5vw - 30px | 19.2px | 24px (h2 24px) | icon 32px; keys wrap at 25% basis |
| ≤500px | — | — | — | teaser becomes 2 columns, no overlap |

## Components

- **Keycap button** (`.intro nav > a`): flex, centred, padding 8px 20.97px, 10px radius, #263966, #f2f7fc Manrope 18.72px/700, Font Awesome or Academicons icon with 8px right margin; solid `0px 4px 0px 0px #4e649e` underside plus `3px 3px 15px #23232348`. Hover: #537998 fill, a 4px #537998 glow replaces the underside, and the key drops 1.5px as if pressed.
- **Venue key** (`.venue`): same shape in #f5f5f5 with #363636 text, a 📍 map-marker icon and a #aea9a3 underside; not a link.
- **Title slab** (`.titlebox`): #e9f0f7 rounded block with a #b4c1dc 5px underside; the lab badge overlaps its top-left corner and the key row overlaps its bottom-right edge.
- **Lab badge** (`.logobox`): 80px white square, 10px radius, #aea9a3 underside, links to the lab site.
- **Gray box** (`.graybox`): #f5f5f5, 10px radius, padding 19.2px 25.6px, three-layer shadow (warm underside, soft drop, 10px halo); text 19.2px Source Sans 3 with a bold lead-in ("Abstract.", "Gallery of results.").
- **Section heading** (`h2`): Manrope 36.8px/700 #363636, `width: fit-content`, centred, padding 4px 19.2px.
- **Gallery cell** (`.qtrwidthflex`): a small colored source video (32%) next to a larger sketch result (66%), with an optional italic navy caption.
- **Teaser strip**: alternating small raised source videos and large overlapping sketch videos in a 12-column grid.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Lab badge | yes | 80px white keycap overlapping the title slab |
| Title | yes | pale-blue slab, 42.4px Manrope, left-aligned |
| Venue badge | yes | light "📍 ICCV 2025" key in the button row |
| Link buttons | yes | navy keycaps hanging off the slab |
| Authors / affiliation | yes | navy Manrope names, centred university line |
| Teaser | yes | overlapping turntable video strip |
| Abstract | yes | gray box, bold label, italic text |
| Gallery | yes | grid of source + sketch videos with a caption box |
| Method figures | yes | network and keypoint diagrams at 85% width |
| Interactive / control demos | yes | level-of-abstraction and deformation video rows |
| Results tables | absent from the source | — |
| BibTeX | present but non-standard | plain text in a gray box, proportional font |
| Footer | present but non-standard | no footer; a gray box credits the template (Nam Anh Dinh) |

## Adapting to Other Content

- **More authors**: the 80% flex row wraps at 20.8px; keep navy Manrope 700 and add a second affiliation line at 18px.
- **A results table**: place it inside a `.graybox` (10px radius, #f5f5f5, keycap shadows) at 85% width; header Manrope 700 #263966, body Source Sans 3 19.2px #363636, 1px #aea9a3 row rules, best values bold navy.
- **Long publication or news lists**: one gray box per group, items as Source Sans 3 19.2px lines with bold dates; links in #263966.
- **More buttons**: add navy keys to the nav row; keep the venue as the only light key.
- **A code block**: keep it in a gray box; switch to a monospace face only if alignment matters.

## Do's and Don'ts

- Do give every box and button the keycap treatment: 10px radius, a solid 4–5px underside in its own darker shade, plus the soft #23232348 drop shadow.
- Do let the lab badge and key row overlap the title slab; the overlaps are the header's signature.
- Do keep headings in Manrope 700 and running text in Source Sans 3.
- Do leave large white gaps between sections so the sketches float.
- Don't fill sections with color; the only tinted surfaces are the #e9f0f7 slab and #f5f5f5 boxes.
- Don't use navy for large areas; it is for keys, names and captions.
- Don't add borders; edges come from the offset shadows.

## Surfaces

White page; one pale-blue title slab; light gray text boxes; navy and light keys; a white lab badge. All raised by the same two-part keycap shadow.

## Imagery

Turntable videos of textured 3D shapes (Nefertiti bust, jade dragon, airplanes, animals, furniture) beside black curve-sketch abstractions with soft gray ground shadows; a pencil-style method diagram; keypoint and deformation demos.

## Layout

A single centred 1040px column. The header is asymmetric (badge top-left, keys bottom-right of the slab), everything below is centred: h2, media at 85% width, gray text box, repeated with generous spacing.

## Agent Prompt Guide

Quick colors: text #363636, navy #263966, navy underside #4e649e, hover #537998, title slab #e9f0f7, slab underside #b4c1dc, box #f5f5f5, box underside #aea9a3, key text #f2f7fc, drop #23232348.

1. "Build a keycap header: a #e9f0f7 title slab (10px radius, padding 3px 40px, box-shadow 0px 5px 0px #b4c1dc, 3px 3px 15px #23232348) with a left-aligned Manrope 42.4px/700 #363636 title; an 80px white logo badge (10px radius, 0px 4px 0px 0px #aea9a3 underside) overlapping its top-left corner by 40px; a right-aligned key row pulled up 18.72px over its bottom edge."
2. "Make keycap buttons: padding 8px 20.97px, 10px radius, #263966 fill, #f2f7fc Manrope 18.72px/700 with a leading icon, box-shadow 0px 4px 0px 0px #4e649e, 3px 3px 15px #23232348; hover #537998, glow 0px 0px 4px #537998 and translate(0, 1.5px). The venue key uses #f5f5f5 with #363636 text and a #aea9a3 underside."
3. "Create sections 1040px wide (padding 15px 35px): a centred Manrope 36.8px/700 #363636 heading, media at 85% width, then a #f5f5f5 text box (10px radius, padding 19.2px 25.6px, box-shadow 0px 4px 0px 0px #aea9a3, 3px 3px 15px #23232348, 0px 0px 10px rgba(0,0,0,0.2)) in Source Sans 3 19.2px with a bold lead-in."

## Similar Pages

- Other UChicago 3DL (threedle) project pages built on Nam Anh Dinh's template.
- Pages with "physical button" styling: solid offset shadows under rounded blocks.

## Quick Start

```css
:root {
  --fore: #363636;
  --accent: #263966;
  --accent-shaded: #4e649e;
  --accentlight: #537998;
  --accentbg: #e9f0f7;
  --accentbg-shaded: color-mix(in oklab, var(--accentbg) 70%, #46579b 30%);
  --notwhite: #f5f5f5;
  --notwhite-shaded: #aea9a3;
  --dropshadow: 3px 3px 15px #23232348;
  --buttonshadowsz: 0px 4px 0px 0px;
  --bordrad: 10px;
  --font-display: "Manrope", sans-serif;
  --font-text: "Source Sans 3", system-ui, -apple-system, sans-serif;
  --section-w: calc(50vw + 280px - 30px);
}
```

## Provenance

- **URL**: https://threedle.github.io/wir3d/
- **Paper**: WIR3D: Visually-Informed and Geometry-Aware 3D Shape Abstraction (arXiv 2505.04813), Richard Liu, Daniel Fu, Noah Tan, Itai Lang, Rana Hanocka (University of Chicago).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: "Website template made by Nam Anh Dinh" (in a gray box at the end); hand-written `style.css` with nested CSS.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, two scrolled viewport shots, a rendered-element probe, and `style.css` and `index.html` read directly, on 2026-10-28.
