# Hairline Geometric Column — Style Reference

> A museum wall label: one clean typeface, generous air, and diagrams that move when you touch them.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the hero, buttons, TLDR, teaser video, section titles, dividers, dropdown selects, table and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `static/css/custom.css` and `fonts.css` over Bulma (Nerfies template) with Bootstrap 4.0 also loaded for its carousel. Positions are document coordinates at 1440px wide.

## Overview

This page strips the Nerfies template down to a quiet single column set entirely in DM Sans. The white hero carries a two-line 40px title in #363636, three sky-blue author links (#209cee), a black "UC Berkeley" line, a bold "ICML 2025", and two dark rounded pills (arXiv, Code). A centered TLDR line and an italic note about the previous title follow, then the teaser, a custom vector diagram rendered as a video that animates when clicked, with a small hand-icon "Click to animate figure" button beneath. Every section after that is separated by a 2px #ededed full-width (90vw) divider, opens with a centered 24px title and sets its text left-aligned in a 739px column. Interactivity is understated. Underlined native `<select>` menus are written inline ("Task: Country-Capital"), with a pale grey hint, and they swap the rows of a small bordered table or the result figures. Body text is black, not grey, which keeps the page crisp.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 85.3%, diagram blue-grey #d9dee8 4.6%, mid grey #b4b5b7 2.9%, dark grey #646064 2.8% (title and diagram ink), diagram pink #f4e8e8 2.3%, remainder under 2.2%. The page is almost all white; the only tints come from the diagram's pale blue and pale red panels.

Anatomy in DOM order (y = top of element box):

1. **Title** (`h1.title.is-2.publication-title`), y 48, two centered lines broken by `<br>`, DM Sans 40px/600, line-height 45px, #363636. Gap 26px.
2. **Authors** (`.publication-authors a`), y 164, one centered line, 20px/400, #209cee, three names 16px apart. Gap 0.
3. **Affiliation**, y 192, "UC Berkeley", 20px/400 #000000, centered. Gap 32px (a `<br>`).
4. **Venue**, y 254, "ICML 2025", 20px/700 #000000, centered. Gap 19px.
5. **Link pills** (`a.button.is-rounded.is-dark`), y 299, height 40px, arXiv (Academicons) and Code (Font Awesome GitHub), #363636 fill, white 16px text, icon left. Hero ends at y 364.
6. **TLDR** (`section p`), y 380, centered 16px/24px #000000: bold "TLDR:" then the sentence; second line italic "Previous Title: …". Gap 24px.
7. **Teaser** (`video#teaser` in `.max-width-content`, max 720px), y 452, 720×420, a vector diagram with blue and red task panels over a grey latent-space ribbon; click to play. Gap 7px.
8. **Animate button** (`button.button.is-white.btn-teaser`), y 879, left-aligned under the video at x 360, hand SVG icon then "Click to animate figure" in the system sans 16px #0a0a0a; hover underlines. The fold cuts through it.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Title Charcoal | #363636 | Bulma `$text-strong` | Paper title, section titles, table text |
| Ink | #000000 | `body { color: black }` | Body text, TLDR, affiliation, venue, select menus |
| Author Sky | #209cee | Nerfies `.publication-authors a` | Author names |
| Link Blue | #3273dc | Bulma `$link` | Inline body links (Hendel et al., Todd et al.), footer links |
| Pill Dark | #363636 | Bulma `.button.is-dark` | arXiv and Code pill fill |
| Pill Dark Hover | #2f2f2f | Bulma `.is-dark:hover` | Pill fill on hover |
| Button Ink | #0a0a0a | Bulma `.button.is-white` | "Click to animate figure" label |
| Divider | #ededed | `hr { background-color: #edededff }` | 2px section dividers (90vw) |
| Hint Grey | #c7c7c7 | inline style | "Click the underlined text for dropdown menu" hint |
| Table Border | #dbdbdb | Bulma `$border` | Task-table cell borders |
| Code Grey | #f5f5f5 | Bulma `pre` | BibTeX block background |
| Code Ink | #4a4a4a | Bulma `pre` | BibTeX text |
| Footer Haze | #fafafa | Bulma footer | Footer band |
| White | #ffffff | page | Page, hero, table background, animate button |

## Tokens — Typography

- **Text and headings**: `fonts.css` sets `body { font-family: 'DM Sans', sans-serif !important }` with self-hosted woff2. Only the 400 face is declared and loaded (`fonts_loaded`: DM Sans 400), so the 600 title and 700 venue are browser-synthesized bold. Substitute: DM Sans from Google Fonts with real 600 and 700 weights (same design; if DM Sans is unavailable, Manrope).
- **Controls**: Bulma buttons and native selects keep the system stack (`BlinkMacSystemFont, -apple-system, "Segoe UI", …`), so "Click to animate figure" and the select values render in Segoe UI on Windows.
- **Mono**: DM Mono 400 is declared in `fonts.css`; the BibTeX `pre` renders in the browser monospace.
- **Root size**: `html { font-size: 12pt }`, which equals 16px.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px / 45px | 600 | #363636 |
| Authors, affiliation | `.publication-authors` (`.is-size-5`) | 20px / 30px | 400 | #209cee names, #000000 affiliation |
| Venue | `.publication-authors b` | 20px / 30px | 700 | #000000 |
| Section title | `h2.title.is-4` | 24px / 27px | 600 | #363636 |
| Body | `.content p` | 16px / 24px | 400 | #000000 |
| Pill label | `.button.is-dark` | 16px / 24px | 400 | #ffffff |
| Inline select | `select` | 16px / 24px | 400, underlined | #000000 |
| Hint | inline div | 16px / 24px | 400 | #c7c7c7 |
| Table header | `th` | 16px / 24px | 700 | #363636 |
| BibTeX | `pre` | 14px / 21px | 400 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link pill | 9999px (Bulma `is-rounded`) | 1px solid transparent | none |
| Animate button | 4px | 1px solid transparent | none |
| Section divider (`hr`) | 0 | none (2px #ededed fill) | none |
| Task table | 0 | 1px solid #dbdbdb on every cell (`is-bordered`) | none |
| BibTeX `pre` | 0 | none | none |
| Inline select | 0 | none, underline only | none (focus ring removed) |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop`, 960px max at ≥1024px. The hero column uses the full width (title box 930px); body sections use `.column.is-four-fifths`, giving a 739px text column at x 350.
- **Hero**: inline `padding: 3rem 1.5rem 0.5rem`, so 48px top and 8px bottom; hero height 364px at 1440px.
- **Teaser section**: `padding-top: 1rem` (16px) then Bulma's 48px bottom; teaser capped by `.max-width-content` at 720px (inline) and 70vw.
- **Sections**: `section.section` padding 48px 24px. Section titles have 24px bottom margin.
- **Dividers**: `hr` 2px tall, `width: 90vw` (1296px at 1440px), `margin: auto`, so it overhangs the text column on both sides.
- **Result videos**: `.max-width-results`, `max-width: min(600px, 80vw)`, centered in the 739px column.
- **Table**: `min-width: 480px`, full column width, scrollable in `.task-examples` (max-height 75vh).
- **Carousel**: Bootstrap 4 carousel with 550px cards and arrows offset 50px outside the card.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | container 960px centered | 16px | 40px | text column 4/5 of the container |
| 769–1023px | 24px section padding | 16px | 40px | container becomes fluid; text column still 4/5 |
| ≤768px | 24px | 16px | 40px (Bulma `is-2` is not reduced by this page) | columns stack to full width; `.max-width-content` limits media to 70vw; result videos 80vw |

## Components

- **Dark link pill**: `a.external-link.button.is-normal.is-rounded.is-dark`, 40px tall, padding 7px 20px, margin 5px, #363636 fill, white DM Sans 16px/400 label, icon left (Academicons arXiv, Font Awesome 6 GitHub), fully rounded. Hover fill #2f2f2f.
- **Click-to-animate figure**: a `<video muted playsinline>` without autoplay showing a vector figure; clicking the video or the button below plays it. The button is `.button.is-white.btn-teaser`, padding 0, left-aligned flex, 20px hand SVG with 5px right margin, label in the system sans 16px #0a0a0a; hover keeps a transparent background and underlines.
- **Hairline section divider**: `hr` with #ededed fill, 2px tall, 90vw wide, centered between sections.
- **Inline dropdown selector**: `select` with `appearance: none`, no border, no background, underlined text inside a sentence ("Model: Idefics2   Task: Average"), each `span` padded 5px; on change it shows the matching table row or figure. A hint line beneath in #c7c7c7 with a 20px info icon.
- **Task table**: `table.table.is-bordered.is-hoverable`, 1px #dbdbdb cell borders, header 16px/700, cells 16px/400 #363636 with italic instructions and bold answers, padding 8px 12px, small 50px flag images.
- **BibTeX**: Bulma `pre`, #f5f5f5, padding 17.5px 21px, 14px monospace #4a4a4a, in the full 930px hero-width column.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title, authors, affiliation, venue | yes | centered DM Sans on white |
| Link buttons | yes | two dark fully rounded pills |
| TLDR | yes | centered line with bold lead-in |
| Teaser | yes | click-to-animate vector video at 720px |
| Abstract | yes | left-aligned 16px black paragraph in the 739px column |
| Method figure | yes | click-to-animate video at 600px |
| Interactive selectors | yes | underlined native selects that swap table rows and figures |
| Results table | yes | small bordered example table |
| Results figures | yes | per-model, per-task images switched by selects; one Bootstrap carousel |
| Navigation | absent from the source | none |
| BibTeX | yes | #f5f5f5 `pre` |
| Footer | yes | #fafafa band with Nerfies and Readout Guidance credits |

## Adapting to Other Content

- **More authors**: keep them on centered 20px lines in #209cee; add superscript numbers and a second black affiliation line only if there are several institutions.
- **A larger results table**: keep `is-bordered` with #dbdbdb hairlines, 16px DM Sans, bold best values, no fills; let `.table-container` scroll horizontally on phones instead of shrinking type.
- **Many result variants**: use more inline selects in the same sentence pattern rather than tabs or buttons.
- **Long publication lists**: a left-aligned list in the 739px column, 16px black text, titles as #3273dc links.
- **News**: a few dated lines under the TLDR, centered, 16px, the date in bold; keep it above the teaser only if short.
- **Static figures**: drop the animate button and keep the figure at 600–720px, centered, with no frame.

## Do's and Don'ts

- Do use one typeface (DM Sans) for all reading text, with black body copy.
- Do separate sections with the 2px #ededed divider spanning 90vw.
- Do keep figures as clean vector graphics, animated on click rather than autoplay.
- Do write controls into sentences (underlined selects) instead of adding UI chrome.
- Don't add colored backgrounds or cards; the diagrams supply the only color.
- Don't use more than the two dark pills in the hero.
- Don't widen the text column past 739px at desktop.

## Surfaces

White page, a #f5f5f5 BibTeX block and a #fafafa footer. The table is white with hairline borders. No shadows.

## Imagery

Custom vector diagrams with a restrained palette: navy and crimson markers, pale blue and pale pink task panels, a grey latent-space ribbon, token boxes with lavender highlights. They are delivered as short videos that animate on click. Result plots and example tables use small flag and food images.

## Layout

One centered column: a 930px hero, a 720px teaser, then 739px text sections divided by 90vw hairlines. Text is left-aligned under centered section titles. Rendered height about 6,440px at 1440px.

## Agent Prompt Guide

Quick colors: title #363636, body #000000, authors #209cee, links #3273dc, pills #363636 with white text (hover #2f2f2f), divider #ededed, hint #c7c7c7, table border #dbdbdb, code #f5f5f5, footer #fafafa.

1. "Build a quiet hero on white: DM Sans throughout; centered two-line 40px/600 title in #363636 (line-height 45px); authors 20px #209cee; affiliation 20px #000000; venue 20px/700 #000000; two fully rounded #363636 pills (40px tall, padding 7px 20px, white 16px label, icon left, hover #2f2f2f)."
2. "Separate sections with an hr that is 2px tall, background #ededed, width 90vw, margin auto. Each section has 48px vertical padding, a centered 24px/600 #363636 title with 24px bottom margin, and left-aligned 16px/24px #000000 text in a 739px column."
3. "Make an inline selector: a sentence like 'Task: <select>' where the select has no border, no background, `appearance: none`, underlined text; under it a #c7c7c7 hint with a 20px info icon; on change, swap the visible row of a bordered table (1px #dbdbdb cells, padding 8px 12px, 16px text)."

## Similar Pages

- Nerfies-template pages restyled with a single geometric sans and no colored bands.
- Readout Guidance (same first author), credited in the footer, with the same select-driven figures.

## Quick Start

```css
:root {
  --title: #363636;
  --ink: #000000;
  --author: #209cee;
  --link: #3273dc;
  --pill: #363636;
  --pill-hover: #2f2f2f;
  --divider: #ededed;
  --hint: #c7c7c7;
  --border: #dbdbdb;
  --code-bg: #f5f5f5;
  --code-ink: #4a4a4a;
  --footer: #fafafa;
  --font: 'DM Sans', sans-serif;
  --font-mono: 'DM Mono', monospace;
  --container: 960px;
  --text-col: 739px;
  --teaser: 720px;
  --figure: 600px;
}
```

## Provenance

- **URL**: https://vlm-cross-modal-reps.github.io/
- **Paper**: Vision-Language Models Create Cross-Modal Task Representations (arXiv 2410.22330; previous title "Task Vectors are Cross-Modal"), Grace Luo, Trevor Darrell, Amir Bar (UC Berkeley).
- **Venue**: ICML 2025.
- **Selection reason**: existing verified entry in entries.json; the arXiv 2410.22330 comment says ICML 2025. Chosen for the geometric sans, narrow centered column, full-width hairline dividers, click-to-animate vector teasers and inline dropdown tables.
- **Template credit**: footer says the site is based on the Nerfies website and Readout Guidance.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of dividers, columns, selects, video and footer links, the first-viewport screenshot and scaled full-page capture, `custom.css`, `fonts.css` and the HTML. Date 2026-10-28.
