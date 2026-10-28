# ProJo4D — Style Reference

> A monochrome lab notebook bound in book type: Castoro headings over Noto Sans, hairline rules, outlined pills, and results tables set like a printed appendix.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css` (headed "ProJo4D — minimal monochrome design system") read with `index.html`. Bulma 0.9 is also loaded; where Bulma wins the cascade (the `<hr>` and `<strong>` colors) the rendered value is given. The page has no dark mode.

## Overview

A long (9,888px) results-heavy project page in pure greyscale. White ground, near-black ink #111111, greys #2a2a2a / #5a5a5a / #8a8a8a for secondary text, and hairlines #e6e6e6 / #f0f0f0. There is no accent color at all; emphasis is done with weight (600 active nav, 700 table winners) and with uppercase tracked labels. Headings are Castoro (a book serif, regular weight only) and everything else is Noto Sans. A 200px sticky "On this page" list with a 1px left rule sits to the left of a 744px centred content column. The hero is centred: large four-line serif title, underlined author names, a tracked uppercase venue line and two outlined pill buttons. The teaser pairs a concept illustration with a 4×2 grid of small comparison videos labelled GROUND TRUTH / PROJO4D / GIC / SPRING-GAUS. Sections (Method, Results, Acknowledgment, BibTeX) are separated by full-width hairline rules; Results holds three wide metrics tables and many four-up video comparison rows.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 83.3% plus near-whites #fefefe / #fafaf8 5.5%; near-black #0a0a15 4.4% (the black teaser video backgrounds and title text); grey #8c8c88 3.4% and #dcdcd0 3.3% (the grey camera icons in the concept image and anti-aliased text). The yellow-blue objects in the teaser are too small to form clusters.

Anatomy in DOM order (desktop 1440px). `.page-shell` is a grid `200px minmax(0,1fr)` with a 48px gap, max-width 1040px and 24px side padding (x=200–1240), so the nav column is x=224–424 and the main column x=472–1216 (744px).

1. **Side nav** (`.sidenav-col`, sticky top 32px, x=224, y=32): 1px #e6e6e6 left border, 16px left padding. Title "ON THIS PAGE" Noto Sans 11.2px/400 uppercase, letter-spacing 2.016px (0.18em), #5a5a5a, margin-bottom 12px; then six links (Overview, Method, Spring-Gaus, PAC-NeRF, Real-world, BibTeX) 13.6px, padding 8px 0 (rows 35px), #5a5a5a; the active link is #111111 600.
2. **Hero** (`header.hero-paper`, y=0–572): padding 96px 0 48px, centred, max-width 920px (renders at the 744px column width).
3. **Title** (`h1.paper-title`, y=96, 228px tall): Castoro 49.6px/400, line-height 57.04px (1.15), letter-spacing -0.744px, #111111, centred, four lines; margin-bottom 24px.
4. **Authors** (`p.paper-authors`, y=348): Noto Sans 16px, line-height 27.2px, #2a2a2a; names #111111 with a 1px #8a8a8a bottom border (padding-bottom 1px), superscript numerals 0.75em #5a5a5a; margin-bottom 12px.
5. **Affiliations** (`p.paper-affil`, y=389): 15.2px #5a5a5a, joined by a middle dot; margin-bottom 24px.
6. **Venue** (`p.paper-venue`, y=438): "TRANSACTIONS ON MACHINE LEARNING RESEARCH (TMLR), 2026", 12.8px/400 uppercase, letter-spacing 2.048px (0.16em), #111111.
7. **Buttons** (`.btn-row`, y=482, margin-top 24px): OpenReview and Code, 42px tall outlined pills, 12px apart; the hero ends at y=524 + 48px padding = 572.
8. **Teaser** (`section.teaser`, padding 24px 0 48px; grid at y=596): `grid-template-columns: 1.1fr 2.4fr; gap 32px` → concept image 224px wide at x=472, video block 488px at x=728. Video block header row (y=611) 12.48px uppercase, letter-spacing 0.998px, #5a5a5a, centred; then two rows of four 87×87px black videos (radius 2px, 8px gaps) with a 110px right-aligned row label "Novel-view rendering" 13.6px/500 #2a2a2a.
9. **TL;DR caption** (`p.teaser-caption`, y=894, 32px below the grid): 16.32px, line-height 1.65, #2a2a2a, centred, max-width 760px; "TL;DR." and the key phrase in 700 #363636 (Bulma's `strong` color).

The first hairline rule is at y=1124 and "Method" at y=1222, both below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | --bg | page background, button and table-header fill, COPY button fill |
| Ink | #111111 | --ink | body text, title, section titles, author names, venue line, active nav link, button border and text, table header bottom rule, bold winners |
| Ink 2 | #2a2a2a | --ink-2 | author line, TL;DR and section paragraphs, table body cells, teaser row label, BibTeX code, acknowledgment |
| Bulma Strong | #363636 | (Bulma `strong`) | bold phrases inside the TL;DR caption |
| Muted | #5a5a5a | --muted | nav title and links, affiliations, superscripts, column headers, "METRICS"/"VISUALIZATIONS" labels, video column heads, row labels |
| Muted 2 | #8a8a8a | --muted-2 | author underline, link underline, "n/a" placeholders |
| Rule | #e6e6e6 | --rule | nav left border, section `hr` top border, result-block dividers, table group and row-header rules, BibTeX border, COPY button border |
| Rule 2 | #f0f0f0 | --rule-2 | table row bottom borders |
| Bulma Rule Fill | #f5f5f5 | (Bulma `hr` background) | the 2px `hr.rule` body under its #e6e6e6 top border |
| Soft | #fafafa | --bg-soft | BibTeX panel, table row hover |
| Video Black | #000000 | (literal) | video letterbox background |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Headings | 'Castoro', 'Times New Roman', Georgia, serif | Castoro 400 (Google Fonts) | Libre Caslon Text |
| Text / UI | 'Noto Sans', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif | Noto Sans 400, 500, 600, 700 | Open Sans |
| Code | ui-monospace, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace | system monospace (Consolas on Windows) | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.hero-paper .paper-title` | clamp(1.9rem, 1.2rem + 2.4vw, 3.1rem) → 49.6px / 400 / 1.15, letter-spacing -0.015em | #111111 |
| Section title | `.section-title` | clamp(1.5rem, 1rem + 1.4vw, 2rem) → 32px / 400 / 49.6px, letter-spacing -0.01em, centred | #111111 |
| Result block title | `.result-block__title` | 24px / 400 / 37.2px, centred | #111111 |
| Body | `body` | 16px / 400 / 1.55 | #111111 |
| Section paragraph | `.section-sub` | 16px / 400 / 1.65, centred, max 760px | #2a2a2a |
| TL;DR caption | `.teaser-caption` | 16.32px / 400 / 1.65, centred | #2a2a2a |
| Authors | `.paper-authors` | 16px / 400 / 1.7 | #2a2a2a, names #111111 |
| Affiliations | `.paper-affil` | 15.2px / 400 | #5a5a5a |
| Venue line | `.paper-venue` | 12.8px / 400, uppercase, letter-spacing 0.16em | #111111 |
| Button | `.btn` | 14.4px / 500 | #111111 |
| Eyebrow label | `.result-sub` | 12.48px / 500, uppercase, letter-spacing 0.14em | #5a5a5a |
| Nav title | `.sidenav__title` | 11.2px / 400, uppercase, letter-spacing 0.18em | #5a5a5a |
| Nav link | `.sidenav a` | 13.6px / 400 / 1.35 (active 600) | #5a5a5a (active #111111) |
| Table header | `table.metrics thead th` | 11.52px / 500, uppercase, letter-spacing 0.1em, right-aligned | #5a5a5a |
| Table cell | `table.metrics tbody td` | 14.08px / 400, tabular-nums, right-aligned; mean column 500; winners 700 | #2a2a2a, winners #111111 |
| Video column head | `.video-row__head` | 11.52px / 400, uppercase, letter-spacing 0.14em | #5a5a5a |
| BibTeX | `.bibtex pre` | 13.12px / 400 / 1.55 | #2a2a2a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero / BibTeX buttons | 999px | `.btn` 1px solid #111111; COPY 1px solid #e6e6e6 | none |
| Teaser and result videos | 2px | none | none |
| Section rule (`hr.rule`) | 0 | 1px solid #e6e6e6 top over a 2px #f5f5f5 fill | none |
| Result block | 0 | 1px solid #e6e6e6 bottom (none on the last) | none |
| Side nav | 0 | 1px solid #e6e6e6 left | none |
| Metrics table | 0 | header bottom 1px #111111; row bottoms 1px #f0f0f0; metric groups 1px #e6e6e6 top; row-header and mean column 1px #e6e6e6 right | none |
| BibTeX panel | 4px | 1px solid #e6e6e6 | none |

Spacing scale (`--s-1`…`--s-9`): 4, 8, 12, 16, 24, 32, 48, 72, 96px.

## Layout Metrics

- **Shell**: `.page-shell { display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 48px; max-width: 1040px; margin: 0 auto; padding: 0 24px }` → nav x=224–424, main x=472–1216 (744px).
- **Hero**: padding 96px 0 48px, max-width 920px; title-to-authors 24px, authors-to-affiliations 12px, affiliations-to-venue 24px, venue-to-buttons 24px.
- **Sections**: `section { padding: 48px 0 }`; consecutive sections are separated by an `hr.rule` with 48px margins, so section titles sit 48px + 2px + 48px + 48px below the previous section's content.
- **Teaser grid**: `1.1fr 2.4fr`, gap 32px → 224px + 488px; video grid `110px repeat(4, 1fr)` with 8px gaps → 87px squares.
- **Method figure**: `width: 720px; max-width: 100%`, centred (x=484).
- **Result blocks**: padding 32px 0 with a bottom hairline; eyebrow labels margin 32px 0 12px.
- **Video comparison rows**: `.video-row.cols-4` → four 177px videos with 12px gaps; `.cols-3` rows are 206.7px each; `.labeled-row` adds an 88px right-aligned uppercase label column.
- **Tables**: `.table-wrap { overflow-x: auto }`; the Spring-Gaus table renders 780px in the 744px column and scrolls horizontally.
- **BibTeX**: max-width 760px (renders 744px), padding 24px, COPY button absolute at 12px from top and right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px (incl. 1440) | 24px | 16px | 49.6px (cap) | 200px sticky nav + main column |
| ≤900px | 24px | 16px | 1.2rem + 2.4vw (≈40px at 860px) | nav hidden, single column |
| ≤720px | 24px | 16px | ≈36px at 700px | teaser stacks; teaser row labels hidden; labelled rows stack with a ruled label |
| ≤600px | 24px | 16px | ≈33px at 580px | `.hide-sm` elements hidden |
| ≤466px | 24px | 16px | 30.4px floor (1.9rem) | — |

## Components

- **Outline pill button** (`.btn`): inline-flex, gap 8px, padding 8.8px 17.6px, Noto Sans 14.4px/500 #111111 on #ffffff, 1px solid #111111, radius 999px, no icon, renders 42px tall. Hover inverts: background #111111, text #ffffff (0.15s).
- **Underlined author link**: #111111 text, no text-decoration, 1px #8a8a8a bottom border with 1px padding; hover border #111111.
- **Sticky side nav** (`.sidenav`): 1px #e6e6e6 left rule, 16px padding; title 11.2px uppercase 0.18em #5a5a5a; links block, padding 8px 0, #5a5a5a, hover #111111, active `is-active` #111111 600.
- **Section rule** (`hr.rule`): full 744px, 48px above and below, 1px #e6e6e6 top on a 2px #f5f5f5 body.
- **Eyebrow label** (`.result-sub`): "METRICS", "VISUALIZATIONS"; 12.48px/500 uppercase, letter-spacing 0.14em, #5a5a5a, left-aligned, margin 32px 0 12px.
- **Metrics table** (`table.metrics`): full width, collapsed; header 11.52px/500 uppercase #5a5a5a on #ffffff with a 1px #111111 bottom rule; metric name (CD ↓, EMD ↓, PSNR ↑) as a row-spanning `th` 14.08px/500 #111111 with a 1px #e6e6e6 right rule; method names left, numbers right in tabular numerals #2a2a2a; MEAN column 500 weight with a 1px #e6e6e6 right rule; winners `strong` 700 #111111; row hover #fafafa; cell padding 12px (mean 12px 16px 12px 12px).
- **Video comparison row**: uppercase 11.52px column heads #5a5a5a, 8px above a row of square black-backed videos (`object-fit: contain`, radius 2px), 12px gaps.
- **BibTeX panel**: #fafafa, 1px #e6e6e6, radius 4px, monospace 13.12px #2a2a2a, padding 24px; COPY pill top-right 11.52px uppercase, 1px #e6e6e6, hover inverts to #111111.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Side table of contents | yes | sticky 200px list with a hairline left rule |
| Title / authors / affiliations | yes | centred Castoro title, underlined names, grey affiliations |
| Venue line | yes | tracked uppercase line, no badge |
| Link buttons | yes | two outlined pills (OpenReview, Code), no icons |
| Teaser | yes | concept image beside a labelled 4×2 video comparison grid |
| TL;DR | yes | centred paragraph with a bold "TL;DR." lead |
| Abstract | absent from the source | the TL;DR and Method paragraph replace it |
| Method figure | yes | 720px pipeline diagram plus centred paragraph |
| Results tables | yes | three monochrome metrics tables with bold winners |
| Video comparisons | yes | four-up and three-up rows with uppercase heads; labelled rows for materials |
| Acknowledgment | yes | centred 15.2px paragraph |
| BibTeX | yes | soft grey panel with a COPY pill |
| Footer | absent from the source | page ends after the BibTeX section |

## Adapting to Other Content

- **More authors**: keep one centred `p.paper-authors` at 16px/1.7 and let it wrap inside 744px; each name keeps the 1px #8a8a8a underline and a 0.75em #5a5a5a superscript.
- **More link buttons**: add `.btn` pills to the centred row (12px gaps, wrapping); never fill them, the hover inversion is the only filled state.
- **A news or update list**: use the `.result-sub` eyebrow (12.48px/500 uppercase #5a5a5a) for the date, followed by a 16px #2a2a2a line, with 1px #f0f0f0 rules between items.
- **Image results instead of videos**: reuse `.video-row.cols-4` (four 177px squares at 1440 with 12px gaps) with the same uppercase heads; keep the black letterbox and 2px radius.
- **A long abstract**: put it in `.section-sub` (16px/1.65 #2a2a2a, centred, max 760px) under a 32px Castoro "Abstract" title; switch to left alignment if it runs past six lines.

## Do's and Don'ts

- Do stay strictly greyscale: #111111, #2a2a2a, #5a5a5a, #8a8a8a, #e6e6e6, #f0f0f0 on white.
- Do use Castoro 400 only for h1–h3; never bold the serif.
- Do mark winners in tables with 700 weight, not color or shading.
- Do label every comparison grid with uppercase tracked heads in #5a5a5a.
- Don't add colored badges, icons or filled buttons.
- Don't use shadows; separation is by 1px hairlines and 48px section padding.
- Don't centre table numbers; they are right-aligned in tabular numerals.

## Surfaces

White page throughout. The only tinted surfaces are the BibTeX panel and table row hover (#fafafa) and the 2px #f5f5f5 body of the section rules. Videos sit on black.

## Imagery

A light-ground concept illustration (grey cameras around a yellow-to-blue deforming object, Times-style label "Sparse Multi-View Video"), a black-and-colour pipeline diagram at 720px, and many small square simulation videos on black (yellow-blue rendered objects), shown side by side against ground truth and baselines.

## Layout

A two-column shell: a 200px sticky contents list on the left and a 744px centred reading column on the right. Everything inside the column is centred except tables, eyebrow labels and the BibTeX code. The page flows hero → teaser + TL;DR → rule → Method → rule → Results (three result blocks, each with metrics table and video comparisons) → rule → Acknowledgment → rule → BibTeX.

## Agent Prompt Guide

Quick colors: background #ffffff, ink #111111, secondary text #2a2a2a, muted #5a5a5a, underline #8a8a8a, rules #e6e6e6 and #f0f0f0, soft panel #fafafa. No accent.

1. "Build a centred paper hero (padding 96px 0 48px): Castoro 49.6px/400 title, line-height 1.15, letter-spacing -0.015em, #111111; authors in Noto Sans 16px/1.7 with #111111 names underlined by a 1px #8a8a8a bottom border; affiliations 15.2px #5a5a5a; venue line 12.8px uppercase, letter-spacing 0.16em, #111111; then outlined pills (padding 8.8px 17.6px, 14.4px/500, 1px #111111, radius 999px) that invert to #111111 fill and white text on hover."
2. "Create a sticky left contents list, 200px wide, top 32px: 1px #e6e6e6 left border, 16px left padding; title 'ON THIS PAGE' 11.2px uppercase, letter-spacing 0.18em, #5a5a5a; links 13.6px, padding 8px 0, #5a5a5a, active link #111111 600."
3. "Style a results table: Noto Sans 14.08px, tabular numerals, right-aligned; header 11.52px/500 uppercase, letter-spacing 0.1em, #5a5a5a with a 1px #111111 bottom rule; row bottoms 1px #f0f0f0; metric-group rows get a 1px #e6e6e6 top rule; best values 700 #111111; row hover #fafafa; cell padding 12px."

## Similar Pages

- Monochrome rewrites of the Nerfies/Bulma academic template that keep Bulma underneath but replace its styling with a small token sheet.
- Project pages with a sticky left "On this page" list and centred serif section titles.

## Quick Start

```css
:root {
  --ink: #111111;
  --ink-2: #2a2a2a;
  --muted: #5a5a5a;
  --muted-2: #8a8a8a;
  --rule: #e6e6e6;
  --rule-2: #f0f0f0;
  --bg: #ffffff;
  --bg-soft: #fafafa;
  --serif: "Castoro", "Times New Roman", Georgia, serif;
  --sans: "Noto Sans", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif;
  --mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  --maxw: 1040px;
  --maxw-narrow: 760px;
  --nav-width: 200px;
  --section-pad: 48px;
  --radius-pill: 999px;
}
```

## Provenance

- **URL**: https://daniel03c1.github.io/ProJo4D/
- **Paper**: ProJo4D: Progressive Joint Optimization for Sparse-View Inverse Physics Estimation, Daniel Rho, Jun Myeong Choi, Biswadip Dey, Roni Sengupta (University of North Carolina at Chapel Hill; Meta Reality Labs).
- **Venue**: TMLR 2026 (OpenReview pqvVrqlXCZ, May 2026).
- **Selection reason**: linked from the jmlr.org/tmlr/papers accepted list; curl returned 200 text/html.
- **Template credit**: no footer or credit line; the markup is built on Bulma (Nerfies-style base) with a custom "minimal monochrome design system" sheet.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the rules, teaser grid, tables, video rows, BibTeX panel and sticky nav, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
