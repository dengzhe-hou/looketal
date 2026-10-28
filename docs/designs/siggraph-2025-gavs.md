# GaVS — Style Reference

> A steady camera in a gray card: a black aperture badge, side-by-side shaky and stable clips, a strip of thumbnails to pick from, and one bright blue TL;DR pill.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the teaser card, thumbnails, TL;DR pill, comparison tabs, sections and footer, the 1440×900 and full-page screenshots, and the page's own `index.html` (several inline `<style>` blocks; the page is a saved copy of a Nerfies/Easi3R build with local `gavs_files/` assets) read directly. The page declares 'Google Sans' and 'Noto Sans', but neither font loads (`document.fonts` reports only Academicons), so all text renders in the browser's default sans-serif, Arial on Windows. The weights and sizes below are what that fallback renders.

## Overview

A white Bulma page in Arial-rendered type. The hero is centred: a 96px black aperture logo, a 32px/600 title "GaVS: 3D-Grounded Video Stabilization" with a 24px/600 subtitle line, #209cee author links, a 20px affiliation line, a 24px/600 "SIGGRAPH 2025" line, and four compact dark pills (arXiv, Code, Dataset, Result Collection) with #f5f5f5 labels. The teaser is a card (#fafafa, 1px #cccccc border, 8px radius, 20px padding) holding a 3:1 side-by-side video (unstable left, stabilized right) and a centred row of five 100×70 thumbnails with 6px radius and a soft gray glow, the active one ringed 3px #92a8d1. Under the card a full-width #209cee rounded notification carries the white 17px TL;DR. Sections then alternate white and #f5f5f5 bands: Abstract (gray), Method Overview (white), Introduction Video (gray), Qualitative Comparison with tab buttons (active tab #cccccc), Qualitative Results in another card, Evaluation, Stability Control, Limitations, Related Work, Acknowledgements and BibTeX.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 52.0%; card gray #fafafa 16.4%; olive-dark #353b26 12.3% (foliage and shadows in the teaser video); warm gray #959186 11.4% (the hills, house and person in the video); light stone #deddda 6.4%; pale apricot #fcebd8 0.3%. The blue author links and the TL;DR pill (just below the fold at y=967) cover too little area in the first viewport to form clusters.

Anatomy in DOM order (desktop 1440px, centred):

1. **Hero** (`section.hero`, 0–416px): container 1152px (x=144).
2. **Logo** (`img`, x=672, y=48, 96×96): black-and-white aperture badge, max-width 96px. No gap.
3. **Title** (`h1.title.is-3.publication-title`, y=144, 36px): "GaVS: 3D-Grounded Video Stabilization", 32px/600 #363636, max-width 85%, margin-bottom 0.
4. **Subtitle** (`h2.title.is-4.publication-title`, y=180, 27px): "via Temporally-Consistent Local Reconstruction and Rendering", 24px/600 #363636. Gap 12px.
5. **Authors** (`div.is-size-5.publication-authors`, y=219, 30px): 20px/400; names #209cee, superscripts #4a4a4a, about 36px between names. No gap.
6. **Affiliations** (y=249, 30px): "¹ETH Zurich ²Huawei Research Center, Zurich ³University of Tübingen, Tübingen AI Center", 20px/400 #4a4a4a. Gap 12px.
7. **Venue** (`h2.title.is-4.publication-title`, y=291, 27px): "SIGGRAPH 2025", 24px/600 #363636. Gap 29px.
8. **Buttons** (`a.button.is-dark.is-rounded`, y=347, 36px): arXiv (PDF icon), Code (GitHub), Dataset and Result Collection (Hugging Face-style cube icons); #363636 fill, #f5f5f5 16px labels, padding 5px 16px, fully rounded, 5px apart. Hero ends at 416.
9. **Teaser card** (`div.column.is-full.panel-style`, x=156, y=424, 1128×511): #fafafa, 1px solid #cccccc, radius 8px, padding 20px.
10. **Comparison video** (`video#disentangle-video`, x=177, y=445, 1086×362): `aspect-ratio: 3/1`, unstable and stabilized clips side by side. Gap 27px.
11. **Thumbnails** (`img.thumbnail`, y=834, 100×70 each, 10px apart, centred): radius 6px, `box-shadow: 0 0 4px #888`, inactive border 2px solid #ffffff, active border 3px solid #92a8d1; hover `transform: scale(1.1)`. Card ends at 935. Gap 32px.
12. **TL;DR pill** (`div.notification.is-info.is-rounded`, y=967, 1104×54): #209cee, radius 10px, padding 8px 40px 8px 24px; text `h6.title` 17px/600 #ffffff, centred, two lines.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, Method and Results sections, TL;DR text, inactive thumbnail borders |
| Title Charcoal | #363636 | (Bulma `$text-strong`, `$dark`) | title, subtitle, venue, section titles, button fills |
| Body Gray | #4a4a4a | (Bulma `$text`) | body text, affiliations, superscripts, BibTeX text, footer |
| Info Blue | #209cee | (Bulma `$info`, also author links via `hsl(204, 86%, 53%)`) | author names, TL;DR notification fill |
| Button Label | #f5f5f5 | (Bulma `.is-dark` text, `$light`) | pill labels and icons |
| Band Gray | #f5f5f5 | (Bulma `.has-background-light`) | Abstract and Introduction Video bands, BibTeX `pre` |
| Card Gray | #fafafa | (`.panel-style`) | teaser and results cards |
| Card Border | #cccccc | (`.panel-style`) | card borders; active comparison tab fill |
| Thumb Ring | #92a8d1 | (inline style from the thumbnail script) | 3px border on the active thumbnail |
| Thumb Glow | #888888 | (`.thumbnail` box-shadow) | 0 0 4px glow around thumbnails |
| Tab Ink | #000000 | (comparison nav `a.active`) | active tab label |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`, `.teaser`) | not loaded; browser default sans-serif (Arial on Windows) | Arial |
| Text | 'Noto Sans', sans-serif (`body`) | not loaded; Arial on Windows | Arial |
| Code | monospace | system monospace | JetBrains Mono |
| Icons | Font Awesome (SVG via JS), Academicons, Tabler icons | Academicons 400; Font Awesome inline SVG | — |

Arial is the right substitute because it is what renders; supplying Google Sans would change the look to the standard Nerfies page.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1.title.is-3.publication-title` | 32px / 600 / 36px | #363636 |
| Subtitle and venue | `h2.title.is-4.publication-title` | 24px / 600 / 27px | #363636 |
| Authors / affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px | names #209cee, rest #4a4a4a |
| TL;DR | `.notification h6.title` (inline 17px) | 17px / 600 / 19.125px | #ffffff |
| Section title | `h2.title.is-3` | 32px / 600 / 36px, centred | #363636 |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` (compact) | 16px / 400 / 24px | #f5f5f5 |
| Comparison tab | `nav a` | 16px / 400 / 24px | #4a4a4a; active #000000 |
| BibTeX | `pre` | 14px / 400 / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px | 1px solid transparent | none |
| Teaser / results card (`.panel-style`) | 8px | 1px solid #cccccc | none |
| Thumbnails | 6px | 2px solid #ffffff; active 3px solid #92a8d1 | 0 0 4px #888 |
| TL;DR notification | 10px (inline) | none | none |
| Comparison tabs | 5px | none | none; active fill #cccccc |
| Videos | 0px | none | none |
| BibTeX `pre` | 0px | none | none |

## Layout Metrics

- **Containers**: hero `.container` 1152px at 1440 (x=144); text sections `.container.is-max-desktop` with a `.column.is-four-fifths` → 917px text at x=262; teaser `.container.fluid` with the card at x=156, 1128px wide.
- **Hero**: logo 48–144, title 144–180, subtitle 180–207, authors 219, affiliations 249, venue 291–318, buttons 347–383; hero 416px.
- **Teaser card**: margin 20px auto, padding 20px; video 1086px wide at 3:1 (362px); `.thumbnail-container` flex, wrap, centred, gap 10px, margin 20px auto 10px.
- **TL;DR**: Bulma `.notification` in a `.column`; 1104px wide, 54px tall, 32px below the card.
- **Sections**: `section.section` padding 48px 24px; bands alternate: Abstract #f5f5f5 (1069–1545), Method Overview white (1545–2194), Introduction Video #f5f5f5 (2194–2866), the rest white (a later `has-background-light` band is commented out). Qualitative Results uses padding 32px 24px 48px and a second `.panel-style` card (1176px).
- **Intro video**: YouTube iframe 871×516 inside a 16:9 `.video-container`.
- **Comparison tabs**: a `nav` row of tab links (padding 10px 20px, radius 5px), the active one #cccccc with #000000 text; compare videos at 90% width above 768px.
- **Footer**: padding 32px 24px, one line "Design borrowed from nerfies and Easi3R."

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| 1440 (measured) | hero `.container.is-max-desktop` renders 1152px wide (x=144) under the page's stacked Bulma copies | 16px | 32px | as described |
| 769px and up | same | 16px | 32px | compare videos 90% width; compare descriptions fixed at 60px tall |
| ≤768px | 24px | 16px | 32px | thumbnails shrink to 80px wide; compare descriptions grow to auto height; Bulma columns stack |

## Components

- **Aperture logo**: a 96px black-on-white circular aperture badge centred above the title.
- **Compact dark pill** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, #f5f5f5 16px label, height 36px, padding 5px 16px, radius 290486px, icon at left.
- **Teaser card** (`.panel-style`): #fafafa, 1px solid #cccccc, radius 8px, padding 20px; holds a 3:1 side-by-side video and a thumbnail selector.
- **Thumbnail selector** (`.thumbnail`): 100×70 `object-fit: cover`, radius 6px, 2px solid #ffffff border, `box-shadow: 0 0 4px #888`, `transition: transform 0.3s ease`, hover scale 1.1; clicking swaps the video and moves the 3px #92a8d1 ring.
- **TL;DR pill** (`.notification.is-info.is-rounded`): #209cee fill, radius 10px, padding 8px 40px 8px 24px, centred white 17px/600 text beginning "TL;DR:".
- **Alternating section bands**: `section.section` with `.has-background-light` (#f5f5f5) on alternate sections; centred 32px/600 #363636 heading and 917px justified text.
- **Comparison tabs**: a row of text tabs (padding 10px 20px, radius 5px), the active one filled #cccccc with #000000 text, switching the compare video beneath.
- **BibTeX**: Bulma `pre` #f5f5f5, padding 20px 24px, 14px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo | yes | 96px aperture badge |
| Title / subtitle / authors | yes | centred, 32px + 24px titles, #209cee names |
| Venue | yes | 24px/600 line |
| Link buttons | yes | four compact dark pills |
| Teaser | yes | carded 3:1 comparison video with thumbnail selector |
| TL;DR | yes | full-width #209cee rounded notification |
| Abstract | yes | #f5f5f5 band, 917px justified text |
| Method figure | yes | white section, full-width diagram and paragraph |
| Intro video | yes | #f5f5f5 band, YouTube embed |
| Comparison player | yes | tab row and compare video |
| Results gallery | yes | second card with videos |
| Evaluation / ablations | yes | plain white sections |
| Results tables | absent from the source | evaluation is shown as figures |
| Related work / acknowledgements | yes | plain text sections |
| BibTeX | yes | Bulma `pre` |
| Footer | yes | one centred credit line on white |

## Adapting to Other Content

- **More authors**: keep the centred 20px line with #209cee names and about 36px gaps; it wraps at about six names at 1440; keep affiliations on one line below.
- **A results table**: put it in a white `section.section` at 917px, or inside a `.panel-style` card (#fafafa, 1px #cccccc, 8px radius, 20px padding); header 600 #363636, 1px #cccccc rules, best value bold.
- **Long publication or news lists**: use an alternating #f5f5f5 band with a centred 32px/600 heading and a 16px list at 917px.
- **More example videos**: add 100×70 thumbnails to the selector row (10px gaps, wraps centred) rather than a carousel.
- **A second key message**: reuse the #209cee rounded notification only once per page; for secondary notes use plain 16px text.

## Do's and Don'ts

- Do put the main comparison video and its thumbnail selector inside one #fafafa card with a 1px #cccccc border and 8px radius.
- Do ring the active thumbnail with 3px #92a8d1 and give all thumbnails the 0 0 4px #888 glow.
- Do alternate white and #f5f5f5 section bands for the first sections.
- Do keep the TL;DR as a single full-width #209cee pill with white text.
- Don't use #209cee anywhere else except author links.
- Don't round the videos; only the card, thumbnails, pill and tabs are rounded.
- Don't rely on Google Sans; the page renders in the system sans and its proportions are part of the look.

## Surfaces

White page with alternating #f5f5f5 bands (Abstract, Introduction Video); #fafafa cards with #cccccc hairlines for the teaser and results; a saturated #209cee pill for the TL;DR; #f5f5f5 BibTeX block.

## Imagery

Handheld outdoor and street footage (stairs, forest paths, roadsides, a dancer) shown as unstable and stabilized clips side by side, with cropped thumbnails; a method diagram with pastel boxes, depth maps and Gaussian splat illustrations; a YouTube talk with author portraits.

## Layout

A centred hero, a wide teaser card, the TL;DR pill, then a column of centred sections at 917px text width with alternating bands, comparison players and a second card, closing with BibTeX and a one-line footer.

## Agent Prompt Guide

Quick colors: background #ffffff, bands #f5f5f5, card #fafafa with #cccccc border, title #363636, body #4a4a4a, accent #209cee, thumbnail ring #92a8d1, glow #888888, pill labels #f5f5f5.

1. "Build a centred hero: a 96px black aperture logo; title 32px/600 #363636 and subtitle 24px/600 #363636 with no gap; authors 20px with #209cee names; affiliations 20px #4a4a4a; 'SIGGRAPH 2025' 24px/600; four compact pills (#363636, #f5f5f5 16px labels, padding 5px 16px, radius 290486px, height 36px) with icons. Use Arial (the declared Google Sans is not loaded)."
2. "Make a teaser card: background #fafafa, 1px solid #cccccc, radius 8px, padding 20px; a side-by-side video at aspect-ratio 3/1; below it a centred flex row (gap 10px) of 100×70 thumbnails with radius 6px, 2px solid #ffffff border, box-shadow 0 0 4px #888, hover scale(1.1), the active one with a 3px solid #92a8d1 border."
3. "Under the card add a TL;DR pill: background #209cee, radius 10px, padding 8px 40px 8px 24px, centred #ffffff 17px/600 text. Then sections with padding 48px 24px, alternating #ffffff and #f5f5f5 backgrounds, centred 32px/600 #363636 headings and 917px justified 16px #4a4a4a text."

## Similar Pages

- Nerfies and Easi3R-derived pages with thumbnail-selector teasers and alternating section bands.
- Video-processing papers (stabilization, deblurring, interpolation) that lead with side-by-side before/after clips.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --band: #f5f5f5;
  --card: #fafafa;
  --card-border: #cccccc;
  --title: #363636;
  --text: #4a4a4a;
  --accent: #209cee;
  --pill-label: #f5f5f5;
  --thumb-ring: #92a8d1;
  --thumb-glow: 0 0 4px #888888;
  --font: Arial, Helvetica, sans-serif;
  --radius-card: 8px;
  --radius-thumb: 6px;
  --radius-pill: 290486px;
}
```

## Provenance

- **URL**: https://sinoyou.github.io/gavs/
- **Paper**: GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local Reconstruction and Rendering (arXiv 2506.23957), Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai.
- **Venue**: SIGGRAPH 2025 (the page shows "SIGGRAPH 2025"; the arXiv comment reads "siggraph 2025, project website ...", a weak acceptance wording flagged in selection).
- **Selection reason**: adds variety with a carded video teaser and thumbnail selector, a highlighted TL;DR pill and alternating gray and white section bands.
- **Template credit**: footer reads "Design borrowed from nerfies and Easi3R." (Bulma, Bulma Carousel, Font Awesome, Academicons, Tabler icons, MathJax).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and the page's `index.html` with its inline styles read directly, on 2026-10-28.
