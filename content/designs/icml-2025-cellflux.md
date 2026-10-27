# Midnight Peach Distill — Style Reference

> A lab notebook opened at dusk, the ink still warm with sunset.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the hero, key-point list, buttons, byline, jump tiles, article headings, figures and appendix, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `static/css/style.css` over the Distill v2 template script. The hero is dark but the body (about 88% of the page height) is white, so the theme is light. Positions are document coordinates at 1440px wide.

## Overview

CellFlux uses the Cambrian-style Distill template: a full-viewport header and then a Distill article. The header is a diagonal gradient that runs from black at the top left through deep navy (#122153) to peach (#feae6f) and a cream corner (#f4eacb) at the bottom right. On it, left-aligned in a 650px column, sit an italic Merriweather title and subtitle in peach, a cream intro paragraph, four emoji-bulleted key points with golden bold lead-ins, and two pale-butter pill buttons. The right half holds a rounded hero illustration with a soft shadow; the illustration looks AI-generated. Below the fold the page turns into a calm white Distill read in Merriweather. A ruled byline lists black author names and a red bold "ICML 2025", and an abstract is followed by four light-blue jump tiles with 3px blue borders, a grey "Click to jump to each section" hint and emoji-led section titles. Figures break out to a 1056px width. Everything, including the body, is set in Merriweather.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): near-black navy #081029 13.4%, navy #0e193e 13.4%, warm taupe #928177 13.4% (gradient midtones and image), slate #39445e 12.9%, ink navy #1a2146 12.8%, sand #d8b591 11.6%, mauve #6c5a5f 11.6%, black #02050d 10.8%. The header gradient fills the whole first viewport (header height 903px); no white is visible above the fold.

Anatomy in DOM order (y = top of element box):

1. **Title** (`.header-content h1`, inline `font-size: 2.5rem`), y 50, left-aligned at x 50, "CellFlux:" in Merriweather 40px/700 italic, line-height 48px, #feae6f. The subtitle is pulled up by a -22.8px top margin.
2. **Subtitle** (`h2.responsive-subtitle`), y 95, two lines, Merriweather 30.4px/700, line-height 36.48px, #feae6f, with "Flow Matching" in italic. Gap to intro 24px.
3. **Intro paragraph**, y 192, 650px wide, Merriweather 19.2px/400, line-height 30.72px, #fff7d4; "CellFlux" in bold italic #ffe099. Gap 32px.
4. **Key-point list** (`.icon-container`), y 378, four `.icon-item` rows each 77px tall with 15px gaps: an emoji (🔮 💡 🛠️ 💎) at 32px on the left, then text in Merriweather 16.8px/400 #fff7d4 with a bold lead-in in #ffe099 ("Method Overview:"). Gap 32px.
5. **Buttons** (`.button-container a.button`), y 767, two pills, Paper (Font Awesome file-pdf icon) and Code (GitHub icon), 50px tall, left-aligned. Bottom of the header at y 903.
6. **Hero image** (`.header-image img`), right column, x 773, y 276, 585×332, 8px radius, shadow `0 4px 20px rgba(0,0,0,0.1)`, vertically centered against the text column.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Night | #000000 | gradient stop 10% | Header gradient top-left; author names |
| Deep Navy | #122153 | gradient stop 55% | Header gradient middle |
| Sunset Peach | #feae6f | gradient stop 85%, `.header-container` color | Header gradient lower right; title and subtitle |
| Cream Corner | #f4eacb | gradient stop 100% | Header gradient bottom-right corner |
| Cream Text | #fff7d4 | `.header-content` color | Intro paragraph and key-point text |
| Gold Lead | #ffe099 | `.header-content strong` | Bold lead-ins in key points, bold "CellFlux" |
| Butter Pill | #fff0ce | `.button-container a.button` | Paper and Code button fill |
| Amber Edge | rgba(255,193,7,0.5) | button border | Paper and Code button 2px border |
| Toasted Peach | #eab682 | button hover | Button fill on hover (text turns white) |
| Article Ink | rgba(0,0,0,0.8) | Distill `d-article` color | Body text, abstract, section h1 and h3 |
| Caption Grey | rgba(0,0,0,0.6) | Distill `figcaption` | Figure captions |
| Rule Grey | rgba(0,0,0,0.1) | `.byline` borders, `hr` | Byline top and bottom rules, section divider, appendix top rule |
| Venue Red | #ff0000 | inline `color: red` | "ICML 2025" in the byline |
| Note Grey | #999999 | `.author-note` | "*Equal contribution" |
| Link Blue | #007bff | `.author-link:hover`, `.click-hint strong` | Author hover, "Click to jump to each section." |
| Tile Sky | #d6eefb | `.icon-link` background | Jump tiles |
| Tile Border | #508af6 | `.icon-link` border | Jump tile 3px border |
| Tile Hover | #88c2fa | `.icon-link:hover` | Jump tile fill on hover |
| Hint Border | #cccccc | `.click-hint` border | Jump hint box 2px border |
| Hint Text | #333333 | `.click-hint` color | Jump hint box text and icon line |
| Code Paper | #f9f9f9 | Distill `pre` | BibTeX block background |
| Code Ink | #222222 | Distill `pre` | BibTeX text |
| White | #ffffff | page | Article background |

## Tokens — Typography

- **All text**: declared `'Merriweather', serif` via Google Fonts `@import` (300–900, roman and italic). Rendered: Merriweather 400, 700, 400 italic and 700 italic loaded (`fonts_loaded`). Substitute: PT Serif (similar large x-height and sturdy serifs).
- **Code**: Distill default `"Courier New", Courier, monospace` for the BibTeX block.
- **Icons**: Font Awesome 5 (Free 900, Brands 400) for button icons; emoji glyphs for the key-point and jump-tile markers.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Title | `.header-content h1` (inline 2.5rem) | 40px / 48px italic | 700 | #feae6f |
| Subtitle | `h2.responsive-subtitle` | 30.4px / 36.48px | 700 | #feae6f |
| Intro | header `p` (inline 1.2rem) | 19.2px / 30.72px | 400 | #fff7d4 |
| Key point | `.icon-item div` (inline 1.05rem) | 16.8px / 25.6px | 400, lead-in 700 | #fff7d4, lead-in #ffe099 |
| Button label | `.button-container a.button` | 15.2px / 25.6px | 700 | #000000 |
| Author name | `.author-link` | 20.352px / 36.8px | 400 | #000000 |
| Venue | byline `p` (inline 1.35em) | 22.896px | 700 | #ff0000 |
| Abstract | `p.text.abstract` | 18.4px / 28.832px | 400 | rgba(0,0,0,0.8) |
| Section title | `d-article h1.text` | 27.136px / 28.832px | 700 | rgba(0,0,0,0.8) |
| Conclusion title | `h2.text` | 23.744px / 29.68px | 600 | rgba(0,0,0,0.8) |
| Subsection | `d-article h3` | 16px / 22.4px | 700 | rgba(0,0,0,0.8) |
| Body | `d-article p` | 16.96px / 28.832px | 400 | rgba(0,0,0,0.8) |
| Caption | `figcaption` | 16.112px / 24.168px | 400 | rgba(0,0,0,0.6) |
| Jump hint | `.click-hint` | 15px | 700 (strong) | #007bff |
| Author note | `.author-note` | 14.4px | 400 | #999999 |
| BibTeX | `d-appendix pre` | 12.16px / 20.672px | 400 | #222222 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Paper / Code pill | 20px | 2px solid rgba(255,193,7,0.5) | none |
| Hero image | 8px | none | `0 4px 20px rgba(0,0,0,0.1)` |
| Jump tile (`.icon-link`) | 10px | 3px solid #508af6 | none |
| Jump hint (`.click-hint`) | 5px | 2px solid #cccccc | `0 4px 8px rgba(0,0,0,0.1)` |
| Byline | 0 | 1px rgba(0,0,0,0.1) top and bottom | none |
| BibTeX `pre` | 0 | none | none |

## Layout Metrics

- **Header**: `.header-container` is a flex row, `max-width: 1600px`, padding 50px, centered; `.header-content` and `.header-image` each take `max-width: calc(50% - 20px)` (650px at 1440px), and the image renders at 90% of its column (585px). Header height is set by content, 903px at 1440px.
- **Article grid**: Distill v2 grid. At ≥1180px the text column is 704px (8 columns of 60px with 32px gaps) at x 368, and elements with `.text` (width 150%, margin-left -20%) break out to 1056px at x 227. Figures inside `d-figure` use the same 1056px width.
- **Byline**: 704px wide, padding 0 5px 10px, margin-bottom 20px; `.byline-container` padding 32px top and 8px bottom.
- **Jump tiles**: `.icon-row` flex wrap with 20px padding; each tile is 146×82, padding 10px, margin 10px, `flex: 1 1 100px`.
- **Section rhythm**: `hr` margin 60px 0 between the intro block and the sections; section h1 margins 27px above and below; figures margin 25px top, 42px bottom.
- **Appendix**: margin-top 60px, padding 60px 0 48px, 1px rgba(0,0,0,0.1) top rule.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1180px | Distill outer 1fr | 16.96px | 40px | text 704px, breakouts 1056px |
| 1000–1179px | Distill outer 1fr | 16.96px | 40px | Distill 50px columns with 16px gaps |
| 769–999px | Distill outer 1fr | Distill default | 40px | Distill 45px columns |
| 600–768px | 50px header padding (the later ≥600px rule wins) | Distill default | 40px (inline size wins over the 2.5em rule) | `.text` drops to 100% width; hero image centered at 90% |
| <600px | 16px header padding, 32px top | Distill default | 40px | header stacks and centers (flex rule only applies ≥600px); subtitle 22.8px; jump tiles take 45% each, two per row |

## Components

- **Dusk header**: `background: linear-gradient(-235deg, #000000 10%, #122153 55%, #feae6f 85%, #f4eacb 100%)`, full width. Content column left, image column right, both vertically centered.
- **Emoji key-point list**: flex column with 15px gaps; each row is a 32px emoji with 8px right margin, then a 16.8px Merriweather line in #fff7d4 starting with a bold #ffe099 lead-in and a colon.
- **Butter pill button**: `a.button`, background #fff0ce, text #000000 15.2px/700, padding 10px 20px, margin 5px 2px, 20px radius, 2px solid rgba(255,193,7,0.5) border, Font Awesome icon left. Hover: background #eab682, text white, 0.3s transition.
- **Byline**: centered block with 1px rgba(0,0,0,0.1) rules top and bottom; author names 20.352px black with superscript affiliation numbers, `white-space: nowrap`, hover underline and #007bff; affiliations in the same style; venue in #ff0000 22.896px/700 with a 1px rgba(0,0,0,0.4) underline; note #999999 14.4px.
- **Jump tile**: `.icon-link`, column flex, 24px emoji above a two-line label, #d6eefb fill, 3px solid #508af6 border, 10px radius, padding 10px, margin 10px; hover fill #88c2fa.
- **Jump hint**: `.click-hint`, centered block at 85% width, 15px #333333 text with an animated click GIF, bold #007bff label, 2px solid #cccccc border, 5px radius, padding 10px, shadow `0 4px 8px rgba(0,0,0,0.1)`.
- **Emoji section title**: `h1.text`, 27.136px/700 Merriweather rgba(0,0,0,0.8), prefixed with the same emoji as its jump tile, at breakout width 1056px.
- **Figure**: `d-figure > figure` at 1056px, image then a 16.112px caption in rgba(0,0,0,0.6) starting "Figure N:"; images open in medium-zoom.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Hero with title, summary and image | yes | dusk gradient, left text column, right shadowed image |
| Key points | yes | four emoji-bulleted lines in the header |
| Link buttons | yes | two butter pills (Paper, Code) |
| Authors and affiliations | present but non-standard | below the header in a ruled byline, not in the hero |
| Venue | yes | red bold "ICML 2025" link in the byline |
| Abstract | yes | 18.4px Merriweather paragraph with bold numbers |
| Jump-to-section tiles | yes | four light-blue tiles plus a hint box |
| Method and results figures | yes | 1056px breakout figures with "Figure N:" captions |
| Navigation bar or table of contents | absent from the source | Distill `d-contents` styles exist in the CSS but no contents block is rendered |
| Results table | absent from the source | results are figures |
| BibTeX | yes | Distill appendix `pre` on #f9f9f9 |
| Footer | present but non-standard | the Distill appendix (12.16px rgba(0,0,0,0.5)) serves as the footer |

## Adapting to Other Content

- **More authors**: they already sit outside the hero, so the header does not grow; let the byline wrap with `nowrap` names and keep one line for affiliations.
- **A results table**: place it at the 1056px breakout width inside `d-figure`, Merriweather 15px, a 1px rgba(0,0,0,0.1) rule under the header row, bold best numbers in rgba(0,0,0,0.8), caption below in rgba(0,0,0,0.6).
- **More key points**: keep four to five; each extra row adds 92px to the header, which already fills the first viewport at 1440×900.
- **Long publication or related-work lists**: use plain Distill paragraphs at 704px with author lists in rgba(0,0,0,0.6); avoid adding more tiles.
- **News**: a short dated list under the byline in 15px with the date bold, separated from the abstract by the existing rule.
- **Without an illustration**: a key teaser figure or video can take the right column at the same 8px radius and soft shadow; a photo-real AI illustration is the weakest part of the source.

## Do's and Don'ts

- Do keep the gradient angle and stops exactly: black 10%, #122153 55%, #feae6f 85%, #f4eacb 100%.
- Do set the title in italic peach and the hero text in cream (#fff7d4) with gold (#ffe099) bold lead-ins.
- Do keep the whole page in one serif, Merriweather, including the body.
- Do match each section title's emoji to its jump tile.
- Don't put white cards inside the dark hero; the pills are the only light surface there.
- Don't add a second accent hue in the body; it already has the tile blue and the red venue.
- Don't let the header exceed one viewport; trim key points before shrinking type.

## Surfaces

Two worlds. The hero is the dusk gradient with one light element type (butter pills) and one raised image. The article is white, with light-blue jump tiles, a bordered hint box, a #f9f9f9 BibTeX block and hairline rules at rgba(0,0,0,0.1).

## Imagery

A glossy, AI-looking illustration of a cell under holographic displays in the hero. In the body, flat scientific schematics with pastel cells, bar charts and generated microscopy grids, all on white with no frames.

## Layout

A split hero (50/50 at ≥600px), then a single Distill reading column of 704px with figures and section titles breaking out to 1056px. Rendered height about 7,800px at 1440px.

## Agent Prompt Guide

Quick colors: hero gradient #000000 → #122153 → #feae6f → #f4eacb, title #feae6f, hero text #fff7d4, lead-ins #ffe099, pill #fff0ce with rgba(255,193,7,0.5) border and #eab682 hover, body rgba(0,0,0,0.8), captions rgba(0,0,0,0.6), venue #ff0000, tiles #d6eefb with #508af6 border.

1. "Build a split hero: full-width `linear-gradient(-235deg, #000000 10%, #122153 55%, #feae6f 85%, #f4eacb 100%)`, flex row with 50px padding, max-width 1600px. Left column (max-width calc(50% - 20px)): Merriweather 40px/700 italic #feae6f title, 30.4px/700 #feae6f subtitle, 19.2px/30.72px #fff7d4 intro. Right column: image at 90% width, 8px radius, `0 4px 20px rgba(0,0,0,0.1)`."
2. "Add an emoji key-point list: flex column, 15px gap; each row a 32px emoji then 16.8px Merriweather #fff7d4 text with a bold #ffe099 lead-in. Follow with pill buttons: #fff0ce fill, 2px solid rgba(255,193,7,0.5) border, 20px radius, padding 10px 20px, 15.2px/700 #000000 label with icon left; hover #eab682 fill and white text."
3. "Create jump tiles: a centered flex row of tiles, each a 24px emoji over a two-line Merriweather label, #d6eefb fill, 3px solid #508af6 border, 10px radius, padding 10px, margin 10px; hover #88c2fa. Under them a hint box at 85% width, 2px solid #cccccc, 5px radius, padding 10px, `0 4px 8px rgba(0,0,0,0.1)`, bold #007bff label."

## Similar Pages

- Cambrian-1 style Distill project pages (dark gradient header, emoji key points, jump tiles).
- Distill-template research pages with a full-viewport hero and a Merriweather or serif article.

## Quick Start

```css
:root {
  --hero-gradient: linear-gradient(-235deg, #000000 10%, #122153 55%, #feae6f 85%, #f4eacb 100%);
  --title: #feae6f;
  --hero-text: #fff7d4;
  --hero-strong: #ffe099;
  --pill: #fff0ce;
  --pill-border: rgba(255, 193, 7, 0.5);
  --pill-hover: #eab682;
  --ink: rgba(0, 0, 0, 0.8);
  --caption: rgba(0, 0, 0, 0.6);
  --rule: rgba(0, 0, 0, 0.1);
  --venue: #ff0000;
  --note: #999999;
  --link: #007bff;
  --tile: #d6eefb;
  --tile-border: #508af6;
  --tile-hover: #88c2fa;
  --code-bg: #f9f9f9;
  --font: 'Merriweather', 'PT Serif', serif;
  --text-col: 704px;
  --wide-col: 1056px;
  --radius-pill: 20px;
  --radius-tile: 10px;
  --radius-image: 8px;
}
```

## Provenance

- **URL**: https://yuhui-zh15.github.io/CellFlux/
- **Paper**: CellFlux: Simulating Cellular Morphology Changes via Flow Matching (arXiv 2502.09775), Yuhui Zhang, Yuchang Su et al. (Stanford, Tsinghua, MIT).
- **Venue**: ICML 2025.
- **Selection reason**: the arXiv 2502.09775 comment states acceptance at ICML 2025 and the abstract links the page. Chosen for the dark navy-to-peach hero with serif italic title, icon-bulleted key points and side image, and the jump-to-section tiles; the hero image looks AI-generated.
- **Template credit**: Distill v2 template (`distill_template.v2.js`) with the Cambrian-style header, jump tiles and `.text` breakout rules in `static/css/style.css`; no explicit credit line on the page.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of the header, byline, tiles, headings, figures and appendix, the first-viewport screenshot and scaled full-page capture, `style.css` and the HTML. Date 2026-10-28.
