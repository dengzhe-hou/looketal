# Raster2Seq — Style Reference

> An architect's drafting table: a typewriter-mono wordmark, pastel room swatches, and a quiet scroll-spy rail of hollow circles down the left margin.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), a second probe of rendered elements (buttons, rules, tabs, table rows, side-rail markers, note card, BibTeX), the 1440×900 and tall screenshots, and the page's `style.css?v=62` and `index.html`. The header buttons are Bulma-style `.button` elements whose computed font is Bulma's system stack (Segoe UI on Windows), not DM Sans; table header text renders #363636 from a Bulma default rather than the page's ink. The teaser caption is a hover overlay that slides up only on hover.

## Overview

A white, information-design page in muted slate. The title "Raster2Seq" is set in Space Mono 64px bold with tight -2px tracking, over a DM Sans 30px slate subtitle, blue author links, a 30px "SIGGRAPH 2026" line and three outlined pill buttons. The teaser is a 360px-tall white figure (12px radius, soft shadow) of floorplans and their pastel polygon reconstructions, followed by a centred colour legend of room categories (Outdoor, Kitchen, Living room…) with red door and dashed blue window lines. A fixed scroll-spy rail on the left lists sections beside hollow 15px circles on a thin vertical line. Content narrows to a 65% column for the TL;DR and abstract, separated by fading gradient hairlines, then widens for a tabbed qualitative-results carousel (pill tabs, slate active state, a coral-outlined "WAFFLE" tab), booktabs-style quantitative tables with a peach "Ours" row, heatmap cards, and a dark navy BibTeX block. Two accents carry the interface: slate blue #3d5a80 for active states and coral #e07a5f for hover and the WAFFLE dataset.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #feffff / #ffffe5 together 83.7%; pale sage #e7e9e0 4.5%, beige #e1ceb7 4.1%, taupe #988984 3.8% and silver #bfc3c6 3.7% (floorplan scans, the 3D view and the pastel room fills in the teaser); butter #fcf4ca 0.2% (yellow reconstructions). The slate and blue text cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px; `.page-container` 90% = 1296px at x=72, everything centred):

1. **Scroll-spy rail** (`nav.section-navigator`, fixed, x=0–190, vertically centred at y=303–597): padding 18px 14px 18px 18px, gap 8px; a 1px rgba(61,90,128,0.18) line at left 25px; seven links (Overview, TL;DR, Abstract, Qualitative Results, Quantitative Results, Method, BibTeX), each a 15px circle (1px rgba(61,90,128,0.28) border, rgba(255,255,255,0.45) fill) and a DM Sans 13px/500 label at opacity 0.58 in rgba(85,91,110,0.5). Hover: circle and label turn #e07a5f, label 800 and fully opaque, circle scales 1.18.
2. **Title** (`h1.ourh1`, y=70, 70px box): "Raster2Seq" Space Mono 64px/700, line-height 1.1, letter-spacing -2px, #2b2d42; margin-top 70px. Gap 10px.
3. **Subtitle** (`h2.ourh2`, y=150): DM Sans 30px/700, letter-spacing 0.5px, #555b6e. Gap 10px.
4. **Authors** (`section.authors_block`, y=211–283): "Hao Phung", "Hadar Averbuch-Elor" at DM Sans 20px/400 in hsl(204, 86%, 53%) (#209cee), underline on hover; "Cornell University" 20px #555b6e on the next line.
5. **Venue** (`p.venue-heading`, y=291): "SIGGRAPH 2026", DM Sans 30px/700, line-height 1.3, letter-spacing 0.5px, #555b6e; margin 8px auto. Gap 27px.
6. **Buttons** (y=357, 40px tall, gap 4px): arXiv, Code, Interactive Visualization; `button.button` white, 2px #878686 border, radius 24px, system-UI 16px/400 black, 24px icon box with margin 0 4px 0 -9px; hover border #000000. Gap 10px.
7. **Teaser** (`#site-teaser`, y=407, 955×360): height fixed by `--teaser-height: 360px`, width fit-content, image radius 12px, `box-shadow: 0 8px 30px rgba(0,0,0,0.08)`; hover overlay rgba(20,20,20,0.62) with `backdrop-filter: blur(6px)` and 13.44px white caption slides up from the bottom.
8. **Legend** (y=797–860): "CubiCasa5K Semantic Categories" 17px #555b6e, then a centred row of 12px swatches (2px radius) with labels at 13.12px black, gap 10px 16px, and a second row with a 24×3px red door line and a dashed blue window line.
9. **TL;DR** (`.intro-container`, 65% = 842px, y=885): DM Sans 20px/1.8 #555b6e, justified, with a bold #2b2d42 lead and a #3d5a80 medium link phrase.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | --bg-light / --bg-card | page, buttons, cards, table background |
| Ink | #2b2d42 | --text-primary | title, h2, table text, bold phrases, table rules (2px/1.5px) |
| Slate | #555b6e | --text-secondary | subtitle, venue line, affiliations, body paragraphs, captions, inactive tabs |
| Author Blue | #209cee | (hsl(204, 86%, 53%)) | author links |
| Slate Blue | #3d5a80 | --secondary-accent | active tabs and swiper labels, note icon, method subheadings, task highlights, active carousel dot |
| Coral | #e07a5f | --primary-accent | rail hover, tab hover borders, WAFFLE tab and inline links |
| Navy | #1a1a2e | --primary-dark | BibTeX block |
| Warm Line | #e8e4df | --border-subtle | tab borders, table row rules, gradient hr centre, BibTeX text |
| Sand | #f7f3ef | (literal) | inactive tab fill, dataset header rows in tables |
| Peach Wash | rgba(251, 207, 177, 0.16) | (literal) | "Ours" table row |
| Button Gray | #878686 | (literal) | button border |
| Bulma Heading | #363636 | (Bulma default) | table header and dataset-row text |
| Sage | #81b29a | --highlight-preserve | highlighted phrases |
| Sand Gold | #f2cc8f | --highlight-blend | highlighted phrases |
| Room Pastels | rgba(141,211,199,.59), rgba(255,255,179,.59), rgba(190,186,218,.59), rgba(251,128,114,.59), rgba(128,177,211,.59), rgba(253,180,98,.59), rgba(179,222,105,.59), rgba(252,205,229,.59), rgba(217,217,217,.59) | (literal, ColorBrewer Set3) | legend swatches and room fills |
| Door / Window | rgba(255, 0, 0, 0.59) / rgba(0, 0, 255, 0.59) | (literal) | legend lines (window dashed) |
| Tooltip Ink | rgba(38, 48, 68, 0.96) | (literal) | dataset-row tooltip, refinement-card arrow shadows |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Wordmark / code | 'Space Mono', monospace | Space Mono 400, 700 | IBM Plex Mono |
| Body / headings | 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif | DM Sans 400, 400 italic, 500, 700 | Inter |
| Handwritten labels | 'Caveat', cursive | Caveat 700 (WAFFLE building names) | Kalam |
| Buttons | Bulma system stack (BlinkMacSystemFont, -apple-system, "Segoe UI", Roboto…) | Segoe UI on Windows | Inter |
| Math | MathJax | MJXTEX, MJXTEX-I, MJXZERO | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `h1.ourh1` | Space Mono 64px / 700 / 1.1, letter-spacing -2px | #2b2d42 |
| Subtitle | `h2.ourh2` | 30px / 700, letter-spacing 0.5px | #555b6e |
| Venue line | `.venue-heading` | 30px / 700 / 1.3, letter-spacing 0.5px | #555b6e |
| Section heading | `h2` | 32px / 700 / 1.7 | #2b2d42 |
| Sub-panel title | `.cross-eval-title` | 22px / 700 | #2b2d42 |
| Method subheading | `h3.method-subheading` | 22px / 600 | #3d5a80 |
| Authors | `.author-block` | 20px / 400 | #209cee / #555b6e |
| TL;DR | `.intro-paragraph p` | 20px / 1.8, justified | #555b6e |
| Body | `p` | 17px / 1.7 | #555b6e |
| Intro text | `.qual-results-intro`, `.quant-results-intro` | 16px | #555b6e |
| Tab | `.qual-results-tab`, `.qual-swiper-label` | 16px / 600 (swiper 15px) | #555b6e; active #ffffff |
| Table | `.quant-results-table` | 15px; headers 700 | #2b2d42 |
| Rail label | `.section-navigator-title` | 13px / 500 / 1.25 at opacity 0.58 | rgba(85,91,110,0.5) |
| Image label | `.qual-results-label` | 13px / 1.3 | #555b6e |
| BibTeX | `.bib-container code` | Space Mono 14px / 1.6 | #e8e4df |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Header buttons | 24px | 2px #878686 (hover #000000) | none |
| Tabs, swiper labels, slider tabs | 999px | 1px #e8e4df (active #3d5a80, WAFFLE #e07a5f) | none; hover translateY(-1px) |
| Teaser image | 12px | none | `0 8px 30px rgba(0,0,0,0.08)` |
| Embedded figure frame | 12px | none | `0 4px 20px rgba(0,0,0,0.08)` |
| Refinement cards | 14px, padding 18px | none | `0 4px 20px rgba(0,0,0,0.07)` |
| Qualitative note | 18px, padding 14px 18px | 1px rgba(61,90,128,0.18) | `0 10px 24px rgba(43, 45, 66, 0.06)` |
| BibTeX block | 10px, padding 20px | none | none |
| Carousel arrows | 50%, 38px | 1px #e8e4df | `0 2px 8px rgba(0,0,0,0.08)` |
| Rail circles | 999px, 15px | 1px rgba(61,90,128,0.28) | none |
| Legend swatches | 2px, 12px | none | none |

Section dividers: `hr { height: 1px; background: linear-gradient(90deg, transparent, var(--border-subtle), transparent); margin: 40px 0 20px 0 }`. Qualitative note fill: `linear-gradient(135deg, rgba(61, 90, 128, 0.08), rgba(224, 122, 95, 0.1))`.

## Layout Metrics

- **Containers**: `.page-container { width: 90%; max-width: 1400px }` = 1296px at x=72; text columns (`.intro-container`, `.abstract-container`, `.method-container`, `.bib-container`) are 65% of their parent (842px for the TL;DR and abstract, x=299); qualitative results max 1180px; quantitative results max 1060px with tables at 88% (919px, x=261).
- **Header**: title margin-top 70px; title→subtitle 10px; venue margin 8px; buttons→teaser 10px; teaser height 360px; legend margin-top 18px with 12px padding-top.
- **Sections**: separated by gradient `hr` (40px above, 20px below); h2 margin 30px 0 15px; text blocks margin-bottom 30px.
- **Qualitative grid**: 2 pairs per row, each pair 2 columns (input, output) with 256px media rows; gaps 18px 28px between pairs, 8px 10px inside; tabs gap 12px, margin-bottom 24px.
- **Tables**: cells padding 9px 12px with 1px #e8e4df row rules; header has 2px #2b2d42 top and bottom rules; dataset rows are #f7f3ef bands with 1.5px #2b2d42 rules.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px | 5% each side | 17px | 64px | scroll-spy rail visible |
| ≤900px | 5% | 17px | 64px | rail hidden; Structured3D images fill width |
| ≤768px | 2.5% (95% container) | 17px | 64px | text columns 90%; teaser height 300px |
| ≤480px | 2.5% | 17px | 32px | heatmap cells narrowed to 96px |

## Components

- **Mono wordmark**: Space Mono 64px/700, letter-spacing -2px, #2b2d42, centred, with a DM Sans 30px/700 #555b6e subtitle beneath.
- **Outlined pill button** (`.button`): white, 2px #878686, radius 24px, 40px tall, system-UI 16px black, 24px Font Awesome or Academicons icon pulled left by -9px; hover border #000000. Buttons sit inline with 4px gaps.
- **Scroll-spy rail** (`.section-navigator`): fixed left at 50% height, 190px wide; hollow 15px circles on a 1px slate line with 13px/500 labels at 58% opacity; hover fills the circle and label coral #e07a5f and bolds the label to 800.
- **Teaser with legend**: fixed-height (360px) figure with 12px radius and soft shadow, hover caption overlay, then a centred legend of 12px pastel swatches and 24px door/window strokes.
- **Pill tabs** (`.qual-results-tab`, `.qual-swiper-label`): #f7f3ef fill, 1px #e8e4df, radius 999px, padding 8–10px 18px, 15–16px/600 #555b6e; hover coral border and lift; active #3d5a80 fill with white text; the WAFFLE variant is coral-outlined and fills coral when active.
- **Booktabs table** (`.quant-results-table`): white, 15px DM Sans, 2px #2b2d42 header rules, 1px #e8e4df row rules, #f7f3ef dataset bands with hover tooltips (rgba(38,48,68,0.96), 10px radius), "Ours" row on rgba(251,207,177,0.16), second-best underlined.
- **Note card** (`.qual-results-note`): 760px, radius 18px, slate-to-coral 135deg wash, 34px #3d5a80 round icon with white glyph, 15px text with a bold slate link.
- **BibTeX** (`.code-container`): #1a1a2e, radius 10px, padding 20px, Space Mono 14px/1.6 #e8e4df, inside a 65% column.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Scroll-spy side nav | yes | fixed left rail of hollow circles and faint labels |
| Title / subtitle / authors / affiliation | yes | mono wordmark, DM Sans subtitle, blue author links |
| Venue badge | present but non-standard | a 30px bold text line, not a pill |
| Link buttons | yes | three outlined 24px-radius pills with icons |
| Teaser + legend | yes | 360px figure with hover caption and a room-colour legend |
| TL;DR | yes | 20px justified paragraph in a 65% column |
| Abstract | yes | 17px justified text in a 65% column |
| Qualitative results | yes | tabbed swiper of input/output pairs with dataset legends |
| Quantitative results | yes | tabbed booktabs tables, robustness heatmaps, generalization panel |
| Interactive figure | yes | embedded iframe in a 12px-radius frame |
| Method | yes | figure and text with slate subheadings |
| Video | absent from the source | no video on the page |
| BibTeX | yes | navy code block |
| Footer | absent from the source | page ends after BibTeX |

## Adapting to Other Content

- **More authors**: keep 20px #209cee names on one centred line with affiliations on the next line at 20px #555b6e; wrap within the 1296px container.
- **Another results table**: reuse the booktabs recipe (2px #2b2d42 header rules, 1px #e8e4df rows, #f7f3ef group bands, peach "Ours" row) at 88% of a 1060px column.
- **Long publication or news lists**: put them in a 65% column as rows of 17px #555b6e text with a Space Mono 14px #3d5a80 date, separated by the gradient hairline `hr`.
- **More sections**: add each to the scroll-spy rail; the rail fits about ten entries between 300px and 600px at 1440×900.

## Do's and Don'ts

- Do keep Space Mono for the wordmark and code only; everything else is DM Sans.
- Do use slate blue #3d5a80 for active states and coral #e07a5f for hover and highlight, never as large fills.
- Do keep the soft ColorBrewer pastels at 59% alpha for categorical colour, with legends that match the figures.
- Do separate sections with the fading gradient hairline, not boxes or bands.
- Don't put body text wider than the 65% column.
- Don't fill the header buttons; they are white with a 2px gray outline.
- Don't add a coloured page background; the page is pure white.

## Surfaces

Pure white page and cards; #f7f3ef sand for inactive tabs and table group bands; a peach-tinted "Ours" row; the slate-to-coral wash on the note card; a #1a1a2e navy BibTeX block; soft shadows only on the teaser, refinement cards and embedded figure.

## Imagery

Architectural floorplans: scanned and rendered black-line plans, pastel polygon reconstructions with red doors and dashed blue windows, a beige 3D extrusion, and yellow reconstructions of real historic building plans. Images sit on white with no frames except the 12px-radius teaser.

## Layout

Centred header in a 1296px container with a fixed left rail; a 360px teaser and legend; then alternating narrow (65%) text sections and wide result modules (1180px qualitative, 1060px quantitative), separated by gradient hairlines; BibTeX ends the page. About 7,550px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #2b2d42, slate #555b6e, author blue #209cee, active #3d5a80, hover #e07a5f, line #e8e4df, sand #f7f3ef, code #1a1a2e.

1. "Build a centred header on white: 'Raster2Seq' in Space Mono 64px/700, letter-spacing -2px, #2b2d42, margin-top 70px; subtitle DM Sans 30px/700 #555b6e, letter-spacing 0.5px; authors DM Sans 20px #209cee; a 30px/700 #555b6e venue line; three outlined pill buttons (white, 2px #878686, radius 24px, 40px tall, 16px text with a left icon; hover border #000000)."
2. "Make a fixed left scroll-spy rail 190px wide at 50% height: a 1px rgba(61,90,128,0.18) vertical line, 15px hollow circles (1px rgba(61,90,128,0.28)), DM Sans 13px/500 labels in rgba(85,91,110,0.5) at opacity 0.58; hover turns circle and label #e07a5f with label weight 800."
3. "Create pill tabs and a booktabs table: tabs #f7f3ef, 1px #e8e4df, radius 999px, padding 10px 18px, DM Sans 16px/600 #555b6e, active #3d5a80 with white text; table DM Sans 15px #2b2d42 with 2px #2b2d42 header rules, 1px #e8e4df row rules, #f7f3ef dataset bands and our row on rgba(251,207,177,0.16)."

## Similar Pages

- Graphics project pages that pair a monospace wordmark with a sans body and a scroll-spy side rail.
- Floorplan and vector-graphics papers whose figures use ColorBrewer pastel categories with an on-page legend.

## Quick Start

```css
:root {
  --primary-dark: #1a1a2e;
  --primary-accent: #e07a5f;
  --secondary-accent: #3d5a80;
  --highlight-preserve: #81b29a;
  --highlight-blend: #f2cc8f;
  --text-primary: #2b2d42;
  --text-secondary: #555b6e;
  --bg-light: #ffffff;
  --border-subtle: #e8e4df;
  --sand: #f7f3ef;
  --author-blue: hsl(204, 86%, 53%);
  --font-mono: 'Space Mono', monospace;
  --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --teaser-height: 360px;
}
```

## Provenance

- **URL**: https://cornell-vailab.github.io/Raster2Seq/
- **Paper**: Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction (arXiv 2602.09016), Hao Phung, Hadar Averbuch-Elor (Cornell University).
- **Venue**: SIGGRAPH 2026.
- **Selection reason**: the arXiv comment states acceptance at SIGGRAPH 2026 and links this project page.
- **Template credit**: none stated; a custom `style.css` with Bulma-style buttons, Font Awesome and Academicons icons, Swiper and MathJax.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), an additional computed-style probe, the 1440×900 and tall screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
