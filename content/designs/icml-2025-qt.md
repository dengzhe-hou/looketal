# Khaki-Teal Wordmark — Style Reference

> A lab signboard: a huge wordmark on a khaki-to-sea-glass wash, then numbers in clean rows.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the hero, wordmark, subtitle, authors, logos, venue, buttons, one-line summary, teaser, abstract, both table styles, BibTeX and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's inline styles and `static/css/index.css` over Bulma (Nerfies lineage). Positions are document coordinates at 1440px wide.

## Overview

QT-DoG takes the Nerfies Bulma page and gives it a poster-like header. A left-to-right gradient from khaki (#d2d2ac) to sea-glass teal (#90c7c4) fills a 609px hero. In it a 96px Google Sans wordmark "QT-DoG" sits over a 48px all-caps title, then a line of sky-blue authors (#209cee), the EPFL and CVLab logos side by side at 200px each, a magenta venue line ("ICML 2025, Vancouver", #a91097) and four dark rounded pills. Below the hero, a single centered 24px summary sentence leads into a bubble-chart teaser comparing domain-generalization methods. After that the page is plain white Bulma. It has a 684px justified abstract, a borderless comparison table with a grey header row, bold rows for the authors' methods and an underlined runner-up, GradCAM figures, and Bulma striped tables. A grey BibTeX block with a green Copy button and a #fafafa footer holding a single paper icon link close the page.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): sage-teal #abccba 34.8%, white #ffffff 27.3%, khaki sage #c0d0b4 25.0%, deep teal #8caca6 6.7%, khaki #d4d8bc 3.4%, near-white 2.6%. The gradient hero covers y 0–609 (68% of the viewport); white begins with the summary sentence.

Anatomy in DOM order (y = top of element box):

1. **Wordmark** (`h1.title.is-1.publication-title`, inline `font-size: 6rem`), y 48, "QT-DoG", Google Sans 96px/600, line-height 108px, #363636, centered. Gap 24px.
2. **Title** (second `h1.title.is-1`, inline 3rem), y 180, two centered lines in capitals, Google Sans 48px/600, line-height 54px, #363636. Gap 27px.
3. **Authors** (`.publication-authors a`), y 315, one centered line, Google Sans 24px/400, #209cee names with #4a4a4a commas. Gap 11px.
4. **Lab logos**, y 356, EPFL (red wordmark) and CVLab (black) images, each 200px wide, inline-block, vertically centered; the CVLab logo is a link. Gap 16px.
5. **Venue** (`span.univerity-block`), y 459, "ICML 2025, Vancouver", Google Sans 20px/400, #a91097, centered. Gap 20px.
6. **Pills** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 504, 40px tall: Paper (file-pdf), Video (YouTube), Code (GitHub), Data (images icon); #363636 fill, white Noto Sans 16px. Hero ends at y 609.
7. **Summary line** (`h3.is-size-4.publication-title`), y 657, two centered lines, Google Sans 24px/400, line-height 36px, #4a4a4a, spanning 1392px. Gap 48px.
8. **Teaser chart** (`section.hero img`), y 777, 775×416 (85% width), bubble chart in pale blue and green; the fold cuts it.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Khaki | #d2d2ac | inline hero gradient start | Hero left edge |
| Sea Glass | #90c7c4 | inline hero gradient end | Hero right edge |
| Charcoal | #363636 | Bulma `$text-strong`, `.is-dark` | Wordmark, title, section titles, pill fill, striped-table text |
| Graphite | #4a4a4a | Bulma `$text` | Body text, summary line, first-table cells, caption, BibTeX |
| Author Sky | #209cee | `.publication-authors a` | Author names |
| Venue Magenta | #a91097 | inline `rgb(169,16,151)` | "ICML 2025, Vancouver" |
| Pill Hover | #2f2f2f | Bulma `.is-dark:hover` | Pill fill on hover |
| Header Grey | #f2f2f2 | inline `th` background | Comparison-table header row |
| Stripe | #fafafa | Bulma `.is-striped` | Even rows of striped tables; footer band |
| Table Rule | #dbdbdb | Bulma `$border` | Striped-table 2px header rule and 1px row rules |
| Code Grey | #f5f5f5 | Bulma `pre` | BibTeX block |
| Copy Green | #4caf50 | inline button style | Copy button fill |
| Link Blue | #3273dc | Bulma `$link` | Inline body links |
| White | #ffffff | page | Page and table backgrounds |

## Tokens — Typography

- **Body**: `index.css` sets `body { font-family: 'Noto Sans', sans-serif }`. Rendered: Noto Sans 400 (`fonts_loaded`); 700 text is synthesized. Substitute: Open Sans.
- **Display**: `'Google Sans', sans-serif` on `.publication-title` and `.publication-authors`. Rendered: Google Sans 400 only, so the 600 wordmark and title are synthesized bold. Substitute: Albert Sans.
- **Code**: browser monospace in `pre`.
- **Math**: MathJax 3.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Wordmark | `h1.title.is-1` (inline 6rem) | 96px / 108px | 600 | #363636 |
| Title | `h1.title.is-1` (inline 3rem) | 48px / 54px, uppercase in source | 600 | #363636 |
| Authors | `.publication-authors` (`is-size-4`) | 24px / 36px | 400 | #209cee |
| Venue | `span.univerity-block` | 20px / 30px | 400 | #a91097 |
| Pill label | `.button.is-normal` | 16px / 24px | 400 | #ffffff |
| Summary line | `h3.is-size-4.publication-title` | 24px / 36px | 400 | #4a4a4a |
| Section title | `h2.title.is-3` | 32px / 36px | 600 | #363636 |
| Table caption | `caption` | 19.2px / 28.8px | 700 | #4a4a4a |
| Body | `.content p` | 16px / 24px | 400 | #4a4a4a |
| Table cell | `td` | 16px / 24px | 400, own methods 700 | #4a4a4a (first table), #363636 (striped) |
| BibTeX | `pre` | 14px / 21px | 400 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill | 9999px (`is-rounded`) | 1px solid transparent | none |
| Comparison table | 0 | none (`border-collapse: collapse`, no rules) | none |
| Striped table | 0 | 2px #dbdbdb under header, 1px #dbdbdb under rows | none |
| BibTeX `pre` | 0 | none | none |
| Copy button | 5px | none | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop` (960px at ≥1024px) for hero content and BibTeX; text sections use `.column.is-two-thirds` (684px text at x 378), and tables `.column.is-four-fifths` (763px at x 338).
- **Hero**: inline gradient background, Bulma hero-body padding 48px 24px; height 609px at 1440px. Logo row margins 8px top and bottom.
- **Summary line**: in its own `section.hero`, full container width (1392px), 48px top padding.
- **Teaser**: image at 85% width (775px), pulled up with a -3rem margin; its caption block uses negative margins (-4rem) and renders empty.
- **Sections**: `section.section` padding 48px 24px; some titles pulled up by -32px margins.
- **Comparison table**: 100% of the 763px column, cells padding 10px, caption 16px below-gap.
- **Striped tables**: Bulma `.table.is-striped.is-fullwidth`, cells padding 8px 12px, 16px top margin.
- **BibTeX**: 960px `pre`, padding 17.5px 21px; the Copy button is absolutely positioned 10px from the bottom right.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | container 960px | 16px | 96px wordmark, 48px title | columns as described |
| 769–1023px | 24px | 16px | 96px, 48px (inline sizes) | container fluid; columns keep their fractions |
| ≤768px | 24px | 16px | 96px, 48px (inline sizes are not reduced) | columns go full width; the title wraps to four or more lines; logos stack if the row is narrower than 400px; the comparison table scrolls horizontally (`overflow-x: auto`) |

## Components

- **Gradient poster hero**: `background: linear-gradient(to right, #d2d2ac, #90c7c4)`, full width; stacked centered wordmark (96px), capitalised title (48px), authors, a logo row and a colored venue line, then pills.
- **Logo row**: two images at 200px width, `display: inline-block; vertical-align: middle`, centered, 8px vertical margins.
- **Dark pill**: `a.external-link.button.is-normal.is-rounded.is-dark`, 40px tall, padding 7px 20px, #363636 fill, white Noto Sans 16px/400, icon left; hover #2f2f2f.
- **Comparison table**: borderless, 16px centered text, a bold 19.2px caption above, header cells on #f2f2f2 with 10px padding, the authors' rows in bold (`.best-performing`), the second-best values underlined, no zebra striping.
- **Striped results table**: Bulma `table is-striped is-fullwidth has-text-centered`, header 16px/700 #363636 with a 2px #dbdbdb rule, rows with 1px #dbdbdb rules and #fafafa even rows, values written as "86.9 ± 0.2".
- **BibTeX with Copy**: #f5f5f5 `pre`, 14px monospace, a #4caf50 Copy button (white text, padding 5px 10px, 5px radius) pinned bottom right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Wordmark and title | yes | 96px wordmark over a 48px capitalised title |
| Authors | yes | 24px #209cee line |
| Affiliation | present but non-standard | lab logos instead of text |
| Venue | yes | magenta line with city |
| Link buttons | yes | four dark pills |
| One-line summary | yes | 24px centered sentence below the hero |
| Teaser | yes | bubble chart at 85% width |
| Abstract | yes | 684px justified column on white |
| Results table | yes | borderless comparison table and Bulma striped tables |
| Figures | yes | GradCAM grids, loss-flatness plots |
| BibTeX | yes | grey block with a green Copy button |
| Footer | yes | #fafafa band with one paper (PDF) icon link, no text |
| Navigation | absent from the source | none |

## Adapting to Other Content

- **More authors**: keep the single 24px #209cee line and wrap to a second centered line; add superscripts only if the logo row no longer explains affiliations.
- **More institutions**: extend the logo row with 200px-wide logos; above four, drop to 160px so the row stays on one line at 960px.
- **Larger results tables**: use the striped Bulma style for dense grids and keep the borderless #f2f2f2-header style for the single headline comparison; bold own methods and underline the runner-up in both.
- **News**: a short list in the white band under the summary sentence, 16px, dates in bold.
- **Long publication lists**: plain list in the 684px column, titles as #3273dc links.
- **A shorter name**: the 96px wordmark only works for a short acronym; for long names, set the full title at 48px and drop the wordmark.

## Do's and Don'ts

- Do keep the hero gradient horizontal and muted (#d2d2ac → #90c7c4).
- Do let the acronym carry the hero at 96px with the full title beneath it in capitals.
- Do color only the venue line (#a91097) inside the hero; keep the title charcoal.
- Do mark winners with bold and runners-up with underline rather than colored cells.
- Don't add borders to the headline comparison table; the grey header row is enough.
- Don't put text over the gradient beyond the title block.
- Don't mix more than two table styles on one page.

## Surfaces

A gradient hero, then white. Tables use a #f2f2f2 header or #fafafa stripes, BibTeX sits on #f5f5f5 and the footer on #fafafa. There are no cards and no shadows.

## Imagery

A bubble chart (pale blue for single models, pale green for ensembles), GradCAM heatmap grids over PACS images, loss-surface plots, and two institutional logos in the hero.

## Layout

A centered column: 960px hero content, a 684px text column and a 763px table column, with figures at 85%. Rendered height about 5,890px at 1440px.

## Agent Prompt Guide

Quick colors: hero #d2d2ac → #90c7c4, title #363636, authors #209cee, venue #a91097, pills #363636 (hover #2f2f2f), body #4a4a4a, table header #f2f2f2, stripes #fafafa, rules #dbdbdb, code #f5f5f5, Copy #4caf50.

1. "Build a poster hero: full-width `linear-gradient(to right, #d2d2ac, #90c7c4)`, padding 48px 24px, centered: a 96px/600 Google Sans acronym in #363636 (line-height 108px), a 48px/600 capitalised title, 24px #209cee authors, a row of two 200px logos, a 20px #a91097 venue line, then dark rounded pills (#363636, white 16px text, 40px tall, padding 7px 20px)."
2. "Create a headline comparison table: full column width, `border-collapse: collapse`, no borders, centered 16px text in #4a4a4a, cells padding 10px, header cells on #f2f2f2 bold, a bold 19.2px caption above; bold the authors' rows and underline second-best values."
3. "Add a striped results table: Bulma style, header 16px/700 #363636 with a 2px #dbdbdb bottom rule, rows with 1px #dbdbdb rules, even rows #fafafa, cells padding 8px 12px, values like '86.9 ± 0.2'."

## Similar Pages

- Nerfies-lineage Bulma pages with an inline gradient hero and institutional logos.
- EPFL CVLab project pages using the acronym-as-wordmark header.

## Quick Start

```css
:root {
  --hero-from: #d2d2ac;
  --hero-to: #90c7c4;
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --venue: #a91097;
  --pill: #363636;
  --pill-hover: #2f2f2f;
  --table-head: #f2f2f2;
  --stripe: #fafafa;
  --rule: #dbdbdb;
  --code-bg: #f5f5f5;
  --copy: #4caf50;
  --link: #3273dc;
  --font-body: 'Noto Sans', sans-serif;
  --font-display: 'Google Sans', 'Albert Sans', sans-serif;
  --wordmark-size: 96px;
  --title-size: 48px;
  --container: 960px;
}
```

## Provenance

- **URL**: https://saqibjaved1.github.io/QT_DoG/
- **Paper**: QT-DoG: Quantization-aware Training for Domain Generalization (arXiv 2410.06020), Saqib Javed, Hieu Le, Mathieu Salzmann (EPFL CVLab).
- **Venue**: ICML 2025.
- **Selection reason**: the arXiv 2410.06020 comment states acceptance at ICML 2025 and links the page. Chosen for the khaki-to-teal gradient header with a large display title and lab logos, the clean bubble-chart teaser and the well-set comparison table with bolded rows.
- **Template credit**: Nerfies-derived Bulma template (`index.css` and markup match it); the footer has no credit text, only a paper icon link.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of the caption, text column, both table styles and BibTeX, the first-viewport screenshot and scaled full-page capture, inline styles, `index.css` and the HTML. Date 2026-10-28.
