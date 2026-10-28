# HERMES++ — Style Reference

> A field station in early spring: pale sage light across a white page, forest-green labels, and charcoal buttons parked in a neat row.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css` read with `index.html`. Bulma 0.9 (from the Nerfies template) sits underneath; where Bulma wins the cascade (title color, title and subtitle margins, subtitle size) the rendered value is given, not the custom rule. There is no dark mode.

## Overview

A compact centred project page (5,786px) that dresses the Nerfies template in a soft green palette. The hero is a 323px band, `radial-gradient(circle at 12% 0%, rgba(65,139,84,0.12), transparent 34%), linear-gradient(180deg, #ffffff 0%, #f4f8f5 100%)`, closed by a 1px #e6ece7 rule. It holds a green pill kicker "Unified Driving World Model", a 44.8px Google Sans title in Bulma grey #363636, a row of authors in link blue #1f6feb (plain text for two authors without pages), affiliations in grey-green #53605a and five charcoal #17201a buttons with white Font Awesome icons. Below, the Abstract section (white) sets a justified 891px paragraph, then three small white cards with green headings summarise the contributions, then a full-width teaser figure. Pipeline sits on the slightly off-white body #fbfcfb with the large diagram in a white rounded frame with a soft green-black shadow; Demo pairs two video cards; Main Results holds green subtitles, centred notes, figure panels and an analysis split; a monospace BibTeX block on a pale green well and a mint footer end the page. Body text is dark green-grey #415047; the green #2c7a3f is used only for small headings.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 47.8% and #fdfefe 6.6%; sage tints #f0f5f2 14.4% and #f9fbf9 12.7% (the hero gradient and its green radial glow at the top-left); light grey #dce1df 11.5% (justified abstract text at reading size, card borders); mid grey #888e8b 6.5% (dark title and button text anti-aliased). The charcoal buttons and blue author names are too small to form clusters.

Anatomy in DOM order (desktop 1440px, everything centred). Bulma `.container.is-max-desktop` is forced to 1120px (`max-width: 1120px !important`), x=160–1280.

1. **Hero band** (`section.hero.project-hero`, 0–323px): gradient above, `.hero-body` padding 21.6px 24px 24.8px, 1px #e6ece7 bottom border.
2. **Kicker pill** (`p.project-kicker`, y=22, 32px tall): "Unified Driving World Model", Google Sans 14.4px/700, #256f39 on #eef7f0, 1px #cfe3d3 border, radius 999px, padding 0 13.6px; margin-bottom 11.2px.
3. **Title** (`h1.publication-title`, y=65, 100px tall): Google Sans 44.8px/600, line-height 1.12, #363636 (Bulma `.title`), max-width 1060px, two lines; rendered margin-bottom 24px (Bulma `.title:not(:last-child)` overrides the declared 0.55rem).
4. **Authors** (`.author-row`, y=189): Google Sans 15.68px, line-height 1.42, names with pages #1f6feb (underline on hover), names without pages #18211d, superscripts; author blocks 2.88px apart.
5. **Affiliations** (y=220, 5.6px below): 14.4px #53605a, three entries with leading superscripts.
6. **Buttons** (`.publication-links`, y=258, 12px below, 40px tall): Paper, Code, Weights, Conference Version, Conference Version Code; flex, gap 12px, centred. The hero ends at y=323.
7. **Abstract** (`section.abstract-section`, white, padding 28px 24px; h2 at y=351): "Abstract" Google Sans 32px/600 #17201a, 24px below it the paragraph at y=411 in the 4/5 column (x=274, 891px wide), Noto Sans 15.68px, line-height 1.55, #415047, justified.
8. **Contribution cards** (`.tl-dr-grid`, y=778): three 366px white cards, gap 10.4px; partly visible at the bottom of the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Off-white | #fbfcfb | (body) | page background, visible behind the Pipeline section |
| White | #ffffff | (literal) | hero gradient start, Abstract / Demo / Results section backgrounds, cards, figure frames |
| Sage End | #f4f8f5 | (literal) | hero gradient end |
| Green Glow | rgba(65,139,84,0.12) | (literal) | hero radial glow at 12% 0% |
| Hero Rule | #e6ece7 | (literal) | hero bottom border |
| Kicker Green | #256f39 | (literal) | kicker pill text |
| Kicker Fill | #eef7f0 | (literal) | kicker pill background |
| Kicker Border | #cfe3d3 | (literal) | kicker pill border |
| Title Grey | #363636 | (Bulma `.title`) | paper title |
| Charcoal | #17201a | (literal) | section titles, button fill, BibTeX text |
| Ink | #18211d | (body) | body default, unlinked author names |
| Link Blue | #1f6feb | (literal, `!important`) | linked author names |
| Grey Green | #53605a | (literal) | affiliations, footer text |
| Text Green-Grey | #415047 | (literal) | abstract, card text, demo labels, result notes, analysis text |
| Forest Green | #2c7a3f | (literal) | contribution card headings, result subtitles |
| Card Border | #e1e8e2 | (literal) | contribution cards, demo cards, analysis card |
| Figure Border | #e5ebe6 | (literal) | framed figures |
| Code Border | #dfe9df | (literal) | BibTeX `pre` border |
| Code Well | #f7fbf8 | (literal) | BibTeX `pre` background |
| Mint Footer | #eef6f0 | (literal) | footer background |
| Video Black | #000000 | (literal) | demo video background |
| Shadow Green-Black | rgba(25,42,31,0.05–0.07) | (literal) | card, demo and figure shadows |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Headings / names | 'Google Sans', sans-serif | Google Sans 400 (Google Fonts); 600 and 700 are synthesised bold | Product Sans → Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400 | Open Sans |
| Code | monospace | system monospace (Consolas on Windows) | IBM Plex Mono |
| Icons | Font Awesome 5 (SVG) | rendered as inline SVG | — |

Castoro is requested in the Google Fonts link but is not used by any rendered element.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.publication-title` | clamp(1.65rem, 3.8vw, 2.8rem) → 44.8px / 600 / 1.12 | #363636 |
| Section title | `h2.title.section-title` | 32px / 600 / 36px, centred | #17201a |
| Result subtitle | `.subtitle.result-subtitle` | 20px / 700 / 1.25, centred (left inside the analysis card) | #2c7a3f |
| Card heading | `.tl-dr-card h3` | 15.68px / 700 / 1.5 | #2c7a3f |
| Kicker | `.project-kicker` | 14.4px / 700 | #256f39 |
| Authors | `.author-row` | Google Sans 15.68px / 400 / 1.42 | #1f6feb links, #18211d plain |
| Affiliations | `.affiliations` | 14.4px / 400 / 1.5 | #53605a |
| Abstract | `.content p` | Noto Sans 15.68px / 400 / 1.55, justified | #415047 |
| Card text | `.tl-dr-card p` | 16px / 400 / 1.55 | #415047 |
| Result note | `.result-note` | 15.04px / 400 / 1.42, centred, max 900px | #415047 |
| Button | `.publication-links .button` | Noto Sans 16px / 400 | #ffffff |
| Demo label | `.demo-item p` | Google Sans 16px / 700, centred | #415047 |
| BibTeX | `pre` | monospace 14.08px / 1.5 | #17201a |
| Footer | `.project-footer` | 16px / 400, centred | #53605a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Kicker pill | 999px | 1px #cfe3d3 | none |
| Buttons | 6px | 1px transparent | none |
| Contribution cards, analysis card | 8px | 1px #e1e8e2 | 0 8px 20px rgba(25,42,31,0.05) |
| Demo cards | 8px (videos inside 6px) | 1px #e1e8e2 | 0 10px 24px rgba(25,42,31,0.07) |
| Framed figures (pipeline, results) | 8px | 1px #e5ebe6 | 0 16px 38px rgba(25,42,31,0.07) |
| Teaser figure (`.intro-figure`) | 8px | none | none |
| BibTeX `pre` | 8px | 1px #dfe9df | none |
| Hero | 0 | 1px #e6ece7 bottom | none |

## Layout Metrics

- **Container**: `.container.is-max-desktop { max-width: 1120px !important }` → x=160–1280 at 1440. The abstract sits in `.column.is-four-fifths` (915px including 12px column padding, text 891px at x=274).
- **Hero**: `.hero-body` padding 21.6px 24px 24.8px; 323px tall; kicker→title 11.2px, title→authors 24px, authors→affiliations 5.6px, affiliations→buttons 12px.
- **Sections**: `.section` padding 28px 24px (Bulma left/right); section title margin-bottom 24px; alternating white (Abstract, Demo, Results) and transparent over #fbfcfb (Pipeline).
- **Contribution cards**: `grid-template-columns: repeat(3, minmax(0,1fr)); gap: 10.4px; margin: 14.4px 0 16px` → three 366px cards, padding 12px.
- **Figures**: full 1120px; the pipeline image renders 1120 × 686px with 5.6px inner padding.
- **Demo**: `grid-template-columns: repeat(2, minmax(0,1fr)); gap: 13.6px` → two 553px cards with 8px padding.
- **Analysis split**: `minmax(260px, .75fr) minmax(420px, 1.25fr)`, gap 13.6px → 415px text card + 692px figure.
- **Footer**: padding 48px 24px 96px, mint background.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1168px (incl. 1440) | container 1120px centred inside 24px section padding | 16px | 44.8px (cap) | 3 cards, 2 demos, analysis split |
| 1024–1167px | 24px section padding, container fills the width | 16px | 3.8vw ≈ 39–44.8px | same |
| 769–1023px | 24px | 16px | 3.8vw ≈ 29–39px | Bulma columns still side by side |
| ≤768px | 24px (section padding 24px top and bottom) | 16px | ≈29px at 768 | cards, demos and analysis stack to 1 column; Bulma columns stack |
| ≤694px | 24px | 16px | 26.4px floor (1.65rem) | — |

## Components

- **Kicker pill** (`.project-kicker`): inline-flex, min-height 32px, padding 0 13.6px, Google Sans 14.4px/700 #256f39 on #eef7f0, 1px #cfe3d3, radius 999px.
- **Button** (`.publication-links .button.is-dark`): Bulma button, #17201a fill, white Noto Sans 16px, radius 6px, padding 7px 16px, 40px tall; leading 24px Font Awesome icon box (file-pdf, GitHub, database, external-link). Bulma's `is-dark` hover darkens the fill slightly.
- **Contribution card** (`.tl-dr-card`): white, 1px #e1e8e2, radius 8px, padding 12px, `box-shadow: 0 8px 20px rgba(25,42,31,0.05)`; heading Google Sans 15.68px/700 #2c7a3f with 3.2px below; text 16px #415047.
- **Framed figure** (`.paper-figure img`): full-width image on white, 1px #e5ebe6, radius 8px, `box-shadow: 0 16px 38px rgba(25,42,31,0.07)`; the pipeline variant adds 5.6px padding; the teaser variant drops border and shadow.
- **Demo card** (`.demo-item`): white, 1px #e1e8e2, radius 8px, padding 8px, `box-shadow: 0 10px 24px rgba(25,42,31,0.07)`; video radius 6px on black; caption "Example n" Google Sans 16px/700 #415047, 5.6px below.
- **Result subtitle + note**: centred 20px/700 #2c7a3f subtitle, then a 15.04px #415047 note, max 900px, line-height 1.42.
- **Analysis card** (`.analysis-copy`): as the contribution card with 13.6px padding; left-aligned green subtitle and 15.04px text paragraphs 6.4px apart.
- **BibTeX** (`pre`): #f7fbf8, 1px #dfe9df, radius 8px, padding 17.6px 21.12px, monospace 14.08px #17201a, horizontal scroll.
- **Footer**: #eef6f0 band, centred 16px #53605a credit line, padding 48px 24px 96px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Kicker / topic pill | yes | green pill above the title |
| Title / authors / affiliations | yes | centred, blue linked names, grey-green affiliations |
| Link buttons | yes | five charcoal buttons with white icons |
| Abstract | yes | justified 891px paragraph on white |
| TL;DR / contribution cards | yes | three small white cards with green headings |
| Teaser figure | yes | full-width comparison figure without frame |
| Pipeline figure | yes | large framed diagram with soft shadow |
| Demo videos | yes | two framed video cards side by side |
| Results | present but non-standard | results are shown as figure images (tables rendered as images), with green subtitles and notes; no HTML tables |
| Analysis split | yes | text card beside a figure |
| BibTeX | yes | pale green well |
| Footer | yes | mint band with Nerfies credit |
| Navigation bar | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep the centred `.author-row` at 15.68px with blue linked names and 2.88px gaps; affiliations stay on one 14.4px #53605a line and wrap inside 1120px.
- **More buttons**: add charcoal `.button.is-dark` items to the flex row (gap 12px, wrapping); do not introduce colored buttons.
- **An HTML results table**: put it in a white card like `.analysis-copy` (1px #e1e8e2, radius 8px, shadow 0 8px 20px rgba(25,42,31,0.05)); header 15.04px/700 #2c7a3f, body 15.04px #415047, rows divided by 1px #e1e8e2, best values bold #17201a; title above as a centred 20px/700 #2c7a3f subtitle.
- **News or updates**: a column of contribution-style cards (padding 12px, green 15.68px/700 date heading, 16px #415047 text), 10.4px apart.
- **More contributions**: keep three cards per row (366px each at 1440); add a second row rather than a fourth column.

## Do's and Don'ts

- Do keep green to small labels: the kicker pill, card headings and result subtitles.
- Do frame large figures and videos in white 8px-radius cards with the soft rgba(25,42,31,…) shadows.
- Do alternate white and #fbfcfb section grounds; the difference is subtle and should stay subtle.
- Do keep all buttons charcoal #17201a with white icons.
- Don't use the green for buttons, rules or large fills.
- Don't let the title pick up a color; it stays Bulma grey #363636 while section titles are #17201a.
- Don't add borders to the teaser figure; only the pipeline and result figures are framed.

## Surfaces

A sage-tinted hero band (white to #f4f8f5 with a green radial glow at the top-left) over a near-white page #fbfcfb; white section bands for Abstract, Demo and Results; white cards with green-black soft shadows; a #f7fbf8 code well; a mint #eef6f0 footer.

## Imagery

Light, academic diagrams: a four-panel teaser contrasting generation, understanding and the unified model with a bar chart, a large pipeline diagram with pastel blue, green, orange and pink blocks, and result figures rendered as images. Two demo videos show multi-view driving footage, BEV point clouds and green-highlighted text answers on black.

## Layout

Centred single column at 1120px. Hero band → Abstract (4/5 column) with three cards and a full-width teaser → Pipeline figure → two demo videos → Main Results (subtitles, notes, figures, an analysis split) → BibTeX → footer. Sections are separated only by their background change and 28px padding.

## Agent Prompt Guide

Quick colors: page #fbfcfb, white #ffffff, title #363636, headings #17201a, text #415047, green #2c7a3f, kicker #256f39 on #eef7f0, author links #1f6feb, borders #e1e8e2, footer #eef6f0.

1. "Build a centred hero band with background radial-gradient(circle at 12% 0%, rgba(65,139,84,0.12), transparent 34%), linear-gradient(180deg, #ffffff 0%, #f4f8f5 100%), a 1px #e6ece7 bottom border and padding 21.6px 24px 24.8px. Inside a 1120px container: a pill kicker (Google Sans 14.4px/700, #256f39 on #eef7f0, 1px #cfe3d3, radius 999px, min-height 32px), a Google Sans 44.8px/600 title (line-height 1.12, #363636), 15.68px authors in #1f6feb, 14.4px #53605a affiliations, and a row of #17201a buttons (radius 6px, padding 7px 16px, white text and icons, gap 12px)."
2. "Make three contribution cards in a 3-column grid with 10.4px gaps: white, 1px #e1e8e2, radius 8px, padding 12px, box-shadow 0 8px 20px rgba(25,42,31,0.05); heading Google Sans 15.68px/700 #2c7a3f, text Noto Sans 16px #415047, line-height 1.55."
3. "Present a figure: full 1120px image on white with 1px #e5ebe6 border, radius 8px, 5.6px padding and box-shadow 0 16px 38px rgba(25,42,31,0.07), under a centred Google Sans 32px/600 #17201a section title with 24px below it."

## Similar Pages

- Nerfies-template project pages restyled with a single soft accent hue, a gradient hero band and card-wrapped figures.
- Autonomous-driving and world-model pages that pair a pipeline diagram with side-by-side demo videos.

## Quick Start

```css
:root {
  --page: #fbfcfb;
  --white: #ffffff;
  --hero-end: #f4f8f5;
  --hero-rule: #e6ece7;
  --title: #363636;
  --heading: #17201a;
  --ink: #18211d;
  --text: #415047;
  --muted: #53605a;
  --green: #2c7a3f;
  --kicker: #256f39;
  --kicker-bg: #eef7f0;
  --kicker-border: #cfe3d3;
  --link: #1f6feb;
  --card-border: #e1e8e2;
  --code-bg: #f7fbf8;
  --footer-bg: #eef6f0;
  --font-head: "Google Sans", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --container: 1120px;
  --radius: 8px;
  --shadow-card: 0 8px 20px rgba(25, 42, 31, 0.05);
  --shadow-figure: 0 16px 38px rgba(25, 42, 31, 0.07);
}
```

## Provenance

- **URL**: https://h-embodvis.github.io/HERMESV2/
- **Paper**: HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation, Xin Zhou, Dingkang Liang, Xiwu Chen, Feiyang Tan, Dingyuan Zhang, Hengshuang Zhao, Xiang Bai (Huazhong University of Science and Technology; Mach Drive; The University of Hong Kong).
- **Venue**: IEEE TPAMI 2026.
- **Selection reason**: found in an arXiv cs.CV listing scan; the arXiv comment reads "Accepted by IEEE TPAMI. ... Project page: ..."; curl returned 200 text/html.
- **Template credit**: footer reads "This website is adapted from the Nerfies project page template"; Bulma 0.9, Font Awesome 5 and Academicons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the hero, kicker, authors, buttons, sections, cards, figures, demo cards, result subtitles, analysis split and footer, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
