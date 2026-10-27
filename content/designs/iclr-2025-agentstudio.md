# AgentStudio Sky Banner Boards — Style Reference

> A sky-blue masthead over a stack of outlined scoreboards, each stamped with a dark date chip.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, the page's `main_page_resources/styles.css` (SWE-bench template), `fonts.css`, and inline styles. Color share is measured on the first 1440×900 viewport.

## Overview

The first screen is split between a solid sky-blue #46aeeb banner and white. In the banner, everything is white and centred: a 60px bold "AgentStudio", a 24px bold tagline, a 20px bold "ICLR 2025", plain author and affiliation lines, and three white rounded buttons whose labels and icons are the banner blue (Paper, Code, 🤗 Data). Below, the page is a column of outlined boxes (1px #40434b border, 7px radius) on white, each opened by a 21.28px bold title: a TL;DR with a pastel overview table image, a Resources box with a row of black-outlined pill links, then a sequence of leaderboards. Tables have a #f2f2f2 header with 7px top corners, zebra rows in white and #f2f2f2, bold best scores, and a small dark #40434b date chip in the last column. The page ends with a charcoal BibTeX block outlined in the banner blue. Type is Lato throughout.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 42.0%, banner blue #46aeeb 38.0% (plus #45aeeb 2.4% from antialiasing), pale grey #ebefee 6.6%, and the overview figure's pastels: light blue #9bc4db 4.7%, steel blue #7198af 3.3%, cream #fff7ec 1.1%.

Anatomy in DOM order (banner `section` full width, 0–399px; content wrapper 1200px at x=120):

1. **Wordmark** — `h1` inline 60px / 700 / 69px, #ffffff, Lato, padding-top 0.4em (24px), centred (y=32–125). Wrapper padding-bottom 15px.
2. **Tagline** — `h2`, 24px / 700, #ffffff, "A Toolkit for Building General Virtual Agents" (y=140–168).
3. **Venue** — `h3` inline 20px / 700, #ffffff, padding-top 1.2em, "ICLR 2025" (y=168–215).
4. **Authors** — `p`, 16px / 400, #ffffff, centred, margin-top 1em, superscripts and asterisks, no links (y=231).
5. **Affiliations** — `p`, 16px / 400, #ffffff, centred, margin-top 1em, `&nbsp;` separated, ending "(*Equal contribution)" (y=265).
6. **Buttons** — row in a `.content-wrapper` with margin-top 2em: three `button.outline` at 21.33px (16pt) / 400, #46aeeb text on #ffffff, 149×43 (7em × 2em), radius 10.67px (0.5em), no border, margin 4.27px 10.67px, FA icon left (y=320–363). Banner ends at y=399 (title-wrapper padding 2em 5em).
7. **TL;DR box** — `.content-box` at y≈415: 1px #40434b border, 7px radius, padding 16px; `h2.text-title` 21.28px / 700 #000000 (y=448); overview PNG 680px wide (60%) centred; `p.text-content` 15.2px / 500 / 25.33px, #000000, bold phrases, underlined links in #34566f.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Sky Banner | #46aeeb | `--dark_accent_color` | header band, hero button text, BibTeX border, download-pill hover, scrollbar thumb |
| Paper | #ffffff | `--odd_line_color` | page, hero buttons, odd table rows, banner type |
| Ink | #000000 | `--black` | box titles, body text, table text, download pill border |
| Graphite | #40434b | `--grey` | content-box border, date chips, BibTeX background |
| Zebra | #f2f2f2 | `--even_line_color` | table header and even rows |
| Link Slate | #34566f | `--blue` | underlined links inside `.text-content` |
| Wheat | #f5deb3 | `wheat` | hero button text on hover |
| Pastel Blue | #9bc4db | (image) | overview figure tint |

## Tokens — Typography

- **Sans:** declared `"DIN", "DM-Sans", "Lato", sans-serif`. DIN is not provided and the local DM-Sans files did not load, so the page renders in Lato (Google Fonts, 400 and 700 loaded). Substitute: Lato itself, or Source Sans 3.
- **Code:** `"Courier New", Courier, monospace`, 14px / 800.
- **Icons:** Font Awesome 6.2 (file, GitHub, paperclip).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Wordmark | banner `h1` (inline 60px) | 60px / 700 / 69px |
| Tagline | banner `h2` | 24px / 700 |
| Venue | banner `h3` (inline 20px) | 20px / 700 |
| Authors, affiliations | banner `p` | 16px / 400 |
| Hero buttons | `button.outline` | 21.33px (16pt) / 400 |
| Box title | `h2.text-title` | 21.28px (1.33em) / 700, padding 0.2em 0, margin-bottom 0.3em |
| Table subtitle | `h3.text-subtitle` | 18.72px / 700 |
| Body | `.text-content` | 15.2px (0.95em) / 500 declared (renders Lato 400) / 1.6667em |
| Table cells | `.table th, td` | 16px; th 700 |
| Date chip | `.label-date` | 12.8px (0.8em), #ffffff |
| BibTeX | `code` | 14px / 800 Courier New, #ffffff |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Content box | 1px solid #40434b, radius 7px, padding 1em, margin 1em 0 |
| Hero button | radius 0.5em (10.67px), no border, 7em × 2em |
| Download pill | `.download`: 3em tall, 2px solid #000000, radius 2em, transparent fill |
| Table header | top-left and top-right radius 7px on first/last `th`, padding 5px 10px |
| Date chip | radius 0.5em, padding 0.2em 0.6em |
| BibTeX block | 2px solid #46aeeb border, radius 0.5em (8px), padding 15px |
| Shadows | none |

## Layout Metrics

- **Container:** `.content-wrapper` max-width 1200px at ≥1140px (700px at 769–1139px), margin auto, padding 0 1em; content boxes are 1168px with 1134px text width at 1440.
- **Banner:** full-width `section` in #46aeeb; inner `.title-wrapper` padding 2em 5em (32px 80px), column flex, centred; height 399px at 1440.
- **Main:** `section.main-container` padding-top 1em; boxes 1em apart; page wrapper padding-bottom 50px.
- **Figures:** overview image `width: 60%` centred.
- **Tables:** `display: block` scrollable, about 80% of the box (907px at 1440), centred; first column `width: 100%`, other columns `nowrap`.
- **Resource pills:** a row of `.content-box.column` cells, each link 120% of its cell, pill 80% wide.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1140px | (viewport − 1200)/2 + 16px | 15.2px | 60px | wrappers in a row; resource pills one row of six |
| 769–1139px | (viewport − 700)/2 + 16px | 15.2px | 60px | 700px column; `.grid-1-2` halves; images 350px |
| 450–768px | 16px | 15.2px | 60px | wrappers stack (column flex); banner keeps 80px side padding |
| <450px | 16px | 15.2px | 60px | `.subtitle` offset removed; tables scroll horizontally |

## Components

- **Banner header:** full-bleed #46aeeb block, all type white and centred, bold 60/24/20px stack, then plain 16px credits.
- **Hero button:** `button.outline`, white fill, #46aeeb 16pt label with icon left, 0.5em radius, no border, fixed 7em width; hover turns the label #f5deb3 (wheat) with a 0.2s transition.
- **Outlined section card:** `.content-box`, 1px #40434b border, 7px radius, 16px padding, 21.28px bold title, then content.
- **Download pill:** `.download`, 3em tall, 2px #000000 border, 2em radius, black text with icon or 🤗; hover turns text and border #46aeeb.
- **Leaderboard table:** header row #f2f2f2 with 7px rounded top corners, sticky `th`, cells 5px 10px, zebra rows #ffffff / #f2f2f2, best scores bold, model name column taking the remaining width.
- **Date chip:** `span.label-date`, #40434b fill, #ffffff 0.8em text, 0.5em radius, padding 0.2em 0.6em, e.g. "2024-10-02".
- **BibTeX block:** `pre#citation`, #40434b background, 2px #46aeeb border, 0.5em radius, 15px padding, white 14px bold Courier New.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Banner header with wordmark | Yes | solid #46aeeb band, white type |
| Venue line | Yes | bold 20px white |
| Authors / affiliations | Yes | plain white text, no author links |
| Link buttons | Yes | three white rounded buttons with blue labels |
| TL;DR | Yes | outlined box with overview table image |
| Resources | Yes | black-outlined download pills |
| Leaderboards | Yes | four outlined boxes with zebra tables and date chips |
| Task config sample | Yes | key-value table in the same style |
| Environment / tools | Yes | figures and an embedded Google Drive video iframe |
| Teaser image or video at top | No (absent from the source) | |
| BibTeX | Yes | charcoal block with blue border |
| Footer | Present but non-standard | credit "Website template from SWE-bench" inside the last box; a fixed, empty footer bar |

## Adapting to Other Content

- **Teaser figure:** place it in the first outlined box under a 21.28px title rather than in the banner; keep the banner text-only.
- **More authors:** keep the plain white paragraph; add links only if they stay white with an underline on hover.
- **Long results:** one outlined box per benchmark, each with its own table and date chips; add a "Submit" download pill for new entries.
- **News:** an outlined box titled "News" with dates in `.label-date` chips at the start of each line.
- **Narrow screens:** reduce the banner's 80px side padding to 16px under 768px; the source does not.

## Do's and Don'ts

- Do keep the banner one flat blue with only white type and white buttons.
- Do frame every section in the same 1px #40434b, 7px box.
- Do use the dark date chip to timestamp leaderboard entries.
- Don't add colour to tables beyond #f2f2f2 zebra and bold best scores.
- Don't use the wheat hover elsewhere; it is the only warm tone on the page.
- Don't rely on a font stack whose first two families never load; name Lato directly.

## Surfaces

A full-bleed #46aeeb banner, then white with outlined boxes; #f2f2f2 table headers and stripes; one charcoal #40434b BibTeX block. No shadows or tinted cards.

## Imagery

A pastel overview table image (green, blue and orange row labels), screenshots of the environment and annotation tools, and an embedded demo video. Most content is tables.

## Layout

Banner header, then a single 1200px column of stacked outlined boxes. Rendered height about 10,100px, mostly leaderboard tables.

## Agent Prompt Guide

Quick colors: banner #46aeeb, page #ffffff, text #000000, box border and chips #40434b, zebra #f2f2f2, inline links #34566f, button hover #f5deb3.

1. "Create a header band: full-width #46aeeb, padding 32px 80px, centred white Lato: 60px bold name, 24px bold tagline, 20px bold venue, 16px authors and affiliations; then three buttons 7em × 2em, white fill, #46aeeb 16pt labels with icons, 0.5em radius, no border; hover label #f5deb3."
2. "Wrap each section in a box with 1px solid #40434b border, 7px radius and 16px padding inside a 1200px column; open with a 21.28px bold #000000 title; body text Lato 15.2px with 1.6667em line height and links in #34566f underlined."
3. "Build a leaderboard table: header row #f2f2f2 with 7px rounded top corners and bold labels, cells padded 5px 10px, rows alternating #ffffff and #f2f2f2, best scores bold, and a last-column date chip with #40434b fill, white 0.8em text, 0.5em radius, padding 0.2em 0.6em."

## Similar Pages

- SWE-bench (the stated template source) and other benchmark sites built from it with banner headers and leaderboard tables.
- Dataset and benchmark pages that are mostly tables (leaderboard-first layouts).

## Quick Start

```css
:root {
  --banner: #46aeeb;
  --bg: #ffffff;
  --text: #000000;
  --border: #40434b;
  --zebra: #f2f2f2;
  --link: #34566f;
  --button-hover: #f5deb3;
  --font-sans: "Lato", sans-serif;
  --font-code: "Courier New", Courier, monospace;
  --wordmark-size: 60px;
  --box-title-size: 1.33em;
  --body-size: 0.95em;
  --radius-box: 7px;
  --radius-chip: 0.5em;
  --container: 1200px;
}
```

## Provenance

- **URL:** https://ltzheng.github.io/agent-studio/
- **Paper:** AgentStudio: A Toolkit for Building General Virtual Agents (arXiv 2403.17918), Longtao Zheng et al.
- **Venue:** ICLR 2025 (stated on the page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the comment.
- **Template credit:** "Website template from SWE-bench" at the end of the page.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, 1440 screenshots (first viewport and tall), `main_page_resources/styles.css`, `fonts.css`, inline styles and page HTML; 2026-10-28.
