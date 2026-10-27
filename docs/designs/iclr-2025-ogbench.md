# OGBench Cornflower Benchmark — Style Reference

> A tidy lab notebook: one cornflower-blue syllable, a grid of little worlds, then plain prose under thin rules.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, and the page's own `css/app.css`, the shared site `stylesheet.css` and Bootstrap 3.3.5. Where Bootstrap's defaults and the render disagree, the render is reported. Color share is measured on the first 1440×900 viewport.

## Overview

A Bootstrap 3 page in Seohong Park's personal-site style: one 1140px column, Source Sans 3 everywhere, #333333 text on white, and a single accent, cornflower blue #598be7, used for the "OG" in the SVG wordmark, every link, and task captions. The hero is a stack of centred lines (wordmark, 39px semibold title, four author links over affiliations, two 24px text links "Paper" and "Code"), then a 9×3 grid of environment thumbnails with monospace labels baked into one PNG, then a 24px centred pitch. Below, the page reads like a technical README: 48px light h1 section titles each preceded by a 1px #eeeeee rule, 32px semibold h2 subheads, 18px body, a GitHub-grey code box, and three-up looping videos with monospace dataset names. There are no buttons, cards, shadows or coloured bands.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 65.7%, slate navy #424b64 8.8% and #182433 8.5% (the checkerboard floors and dark robot scenes in the teaser grid), grey-blue #8a94a3 8.0%, pale #c2ccd2 4.3%, warm cream #f0ede4 3.0%. Text pixels are too thin to register; the blue accent is under 1%.

Anatomy in DOM order (all centred in a 1140px column starting at x=150):

1. **Wordmark** — `assets/ogbench.svg`, 360×71 (col-md-4, width 100%), top at y=30 (`.top30`). "OG" bold #598be7, "Bench" light #333333. Gap to title 31px.
2. **Title** — `h1.text-title`, "OGBench: Benchmarking Offline Goal-Conditioned RL", 39px / 600 / line-height 42.9px, #333333, centred, one line (y=132–175). Gap 10px.
3. **Authors** — `ul.list-inline` of four `li`, each an author link (18px / 400, #598be7) with a `<br>` and the affiliation in #333333 18px below; items separated by 1em. y=185–235. Gap 22px.
4. **Links** — two `h3.text-toplink` inside links, "Paper" and "Code", 24px / 400, #598be7, no icons, no background; y=257–283. Gap about 51px (h3 bottom margin plus `.top30` on the teaser).
5. **Environment teaser** — `assets/env_teaser.png`, 1140×415, 9 columns × 3 rows of square renders with monospace names (maze, antmaze, humanoidmaze, antsoccer, visual-maze, cube, scene, puzzle, powderworld) inside the image. y=334–749. Gap 20px.
6. **Pitch** — `div.text-large`, 24px / 400, #333333, centred, two lines, "OGBench" bold 700. Margin-bottom 30px, then the first `<hr>` and the 48px "Overview" h1 at y=931, just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | body background | page |
| Graphite | #333333 | Bootstrap `body` color | title, section h1/h2, body text, affiliations, pitch |
| Cornflower | #598be7 | `a` (site stylesheet), `.text-blue`, `.text-caption-task` | "OG" in wordmark, author links, Paper/Code, inline links, "Task: …" captions, "Show the full benchmark table" |
| Cornflower Hover | #9bb9f1 | `a:hover` | link hover (no underline either state) |
| Signal Red | #f54254 | `.text-red` | the variant suffix in dataset names (`antmaze-large-` **navigate** / stitch / explore) |
| Rule Grey | #eeeeee | Bootstrap `hr` border-top | 1px rule above every section h1 |
| Code Wash | #f6f8fa | `.codebox-pre`, `.codebox-code` | pip snippet and BibTeX box |
| Code Ink | #24292e | highlight.js github theme | code text |
| Slate Floor | #424b64 | (image) | dominant tone of the teaser grid renders |

## Tokens — Typography

- **Sans:** declared `'Source Sans 3', 'Lato', Verdana, Helvetica, sans-serif` (self-hosted variable woff2, weights 300–700, normal and italic). Rendered: Source Sans 3. Substitute: Source Sans Pro.
- **Mono:** declared `'Source Code Pro', 'Lato', Verdana, Helvetica, monospace` for code and `.text-tt`. Rendered: Source Code Pro 400 and 600 (Google Fonts). Substitute: IBM Plex Mono.
- **Math:** MathJax 3 CHTML fonts.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1.text-title` | 39px / 600 / 42.9px |
| Section title | `h1` | 48px / 300 / 52.8px, margin 30px 0 10.5px |
| Subsection | `h2` | 32px / 600 / 35.2px |
| Top links, toggles | `h3.text-toplink`, `h3` | 24px / 400 (toggle 600 via `<b>`) |
| Pitch | `.text-large` | 24px / 400 |
| Video caption | `.text-caption` | 20px / 400, centred, block |
| Dataset name | `.text-tt` | Source Code Pro 600, inherits 20px in captions |
| Body | `body, p, a, td` (≥992px) | 18px / 400 / 25.7px |
| Code | `.codebox-pre` | 17px / 400 / 24.3px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Radius | none on the page; code box keeps Bootstrap `pre` 4px with `border: none` |
| Shadows | none |
| Borders | only the 1px #eeeeee `hr` (margin 20px 0) |
| Code box | padding 10px outer, 17px inner `code`, background #f6f8fa |
| Spacing utilities | `.top5/.top10/.top20/.top30` and `.bottom5…30` set margin in px |

## Layout Metrics

- **Container:** Bootstrap 3 `.container`, fixed width 1170px at ≥1200px (content 1140px after 15px padding), 970px at ≥992px, 750px at ≥768px, fluid below. Centred.
- **Hero:** no padding wrapper; spacing comes from margins (wordmark 30px top, title 20px top, links 10px top, teaser 30px top, pitch 20px top / 30px bottom).
- **Sections:** `hr` (20px margins) + h1 with 30px top margin; h2 30px top; body text directly in `col-md-12` without paragraph margins.
- **Wordmark width:** col-md-4 centred (360px at 1440).
- **Teaser:** full 1140px column, 415px tall.
- **Media grid:** three-up `col-md-4` (360px each, 30px gutters) for videos and results plots; `col-md-3` four-up for manipulation tasks; `col-md-offset-2 col-md-4` pairs for two-up rows.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1200px | (1440−1170)/2 + 15px = 150px | 18px | 39px | 3- and 4-up media |
| 992–1199px | 15px inside 970px | 18px | 39px | same |
| 768–991px | 15px inside 750px | 16px | 39px | `.desktop-only` hides the teaser grid and pitch; media columns stack to one per row; `.mobile-only` blocks appear |
| <768px | 15px | 16px | 39px | wordmark widens to col-xs-8 / col-sm-6 |

## Components

- **Wordmark:** inline SVG image, two weights of the same sans: heavy "OG" in #598be7, light "Bench" in #333333, centred at one-third column width.
- **Text link row:** `ul.list-inline` (inline-block items, 0.5em side margins) of `h3` 24px / 400 text in #598be7, no icon, no border; hover #9bb9f1, never underlined.
- **Author block:** inline list, name link 18px #598be7, line break, affiliation 18px #333333.
- **Section head:** `<hr>` 1px #eeeeee, then 48px / 300 h1 in #333333, left aligned.
- **Code box:** `pre.codebox-pre` with no border, background #f6f8fa, 17px Source Code Pro, highlight.js github colours (red keywords, navy strings, grey comments).
- **Video tile:** `<video width=100% autoplay loop muted playsinline>` in a col-md-4, then a centred 20px caption: dataset name in Source Code Pro 600 (variant word in #f54254), `<br>`, plain "Example dataset trajectory"; manipulation tiles use "Task: …" in #598be7.
- **Collapse toggle:** Bootstrap collapse link wrapping a bold 24px h3 "Show the full benchmark table" in #598be7, revealing a table PNG.
- **Statement box (declared):** `.block-statement` (2px cornflower border, pale blue fill, 10px radius) exists in app.css but is not used on this page.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Wordmark logo | Yes | two-weight SVG, centred |
| Title / authors / affiliations | Yes | centred stack, blue name links |
| Venue line | No (absent from the source) | ICLR appears only in the BibTeX |
| Link buttons | Present but non-standard | two 24px text links, no buttons or icons |
| Teaser | Yes | 9×3 environment PNG grid with mono labels |
| One-line pitch | Yes | 24px centred, product name bold |
| Overview prose + feature list | Yes | h2 subheads, Bootstrap bullets with bold numbers |
| Quickstart code | Yes | #f6f8fa code box |
| Environment galleries | Yes | autoplay video tiles, 3- or 4-up, mono captions |
| Results | Present but non-standard | six plot PNGs three-up, full table as PNG in a collapse |
| Results table (HTML) | No | |
| BibTeX | Yes | same code box |
| Footer | Yes | one justified line crediting Michaël Gharbi and Jon Barron, after an hr |

## Adapting to Other Content

- **More authors:** keep the inline list; it wraps to centred rows of name-over-affiliation pairs. Past about eight, drop affiliations into a numbered line below.
- **Venue:** add a 20px #333333 line between authors and links, weight 600 (the site's `.text-conference`), no colour.
- **Results table:** use an HTML table in 18px Source Sans 3 with 1px #eeeeee row rules and the best value bold; keep it under an h2, not in a card.
- **More links:** extend the `h3` text-link row (Paper · Code · Data · Leaderboard); keep 24px / 400 blue, no icons.
- **News or changelog:** a plain `ul` under an h2, date in Source Code Pro 600.

## Do's and Don'ts

- Do keep one accent, #598be7, for every interactive or labelled element.
- Do open each major section with a hairline `hr` and a light 48px h1; it is the page's only structural device.
- Do set environment and dataset names in Source Code Pro 600.
- Don't add buttons, pills, cards or shadows; links are bare blue text.
- Don't underline links, even on hover; lighten to #9bb9f1 instead.
- Don't show the dense teaser grid on narrow screens; the source hides it below 992px.

## Surfaces

All white. The only tinted surface is the #f6f8fa code box. Colour on the page comes from the renders themselves (navy checkerboards, robot scenes).

## Imagery

A single PNG mosaic of 27 square environment renders as the hero; dozens of small autoplaying MuJoCo videos in square tiles; matplotlib bar charts for results. No photos, no diagrams with brand colours.

## Layout

Single Bootstrap column, 1140px at desktop, centred hero then left-aligned documentation sections. Rendered height about 15,200px, driven by the video galleries.

## Agent Prompt Guide

Quick colors: text #333333, accent #598be7 (hover #9bb9f1), variant red #f54254, rule #eeeeee, code box #f6f8fa with #24292e text, page #ffffff.

1. "Build a hero: centred SVG wordmark 360px wide with a bold #598be7 first syllable and light #333333 remainder; below it a 39px / 600 Source Sans 3 title in #333333; an inline author list (18px #598be7 names, affiliations on the next line in #333333); then 24px / 400 text links 'Paper' and 'Code' in #598be7, hover #9bb9f1, no underline."
2. "Write a section header: a 1px #eeeeee horizontal rule with 20px margins, then an h1 at 48px / 300 #333333 left aligned, followed by h2 subheads at 32px / 600 and 18px body text."
3. "Make a video tile row: three equal columns 360px wide with 30px gutters, each an autoplay muted looping video, then a centred 20px caption with the dataset name in Source Code Pro 600 (variant word in #f54254) and a plain second line."

## Similar Pages

- Seohong Park's other project pages (HIQL, METRA) and Jon Barron–derived Bootstrap pages with text-only link rows.
- Benchmark READMEs rendered as web pages: Gymnasium or D4RL docs with code-first structure.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #333333;
  --accent: #598be7;
  --accent-hover: #9bb9f1;
  --variant: #f54254;
  --rule: #eeeeee;
  --code-bg: #f6f8fa;
  --code-text: #24292e;
  --font-sans: 'Source Sans 3', 'Source Sans Pro', sans-serif;
  --font-mono: 'Source Code Pro', monospace;
  --title-size: 39px;
  --h1-size: 48px;
  --h2-size: 32px;
  --body-size: 18px;
  --container: 1170px;
}
```

## Provenance

- **URL:** https://seohong.me/projects/ogbench/
- **Paper:** OGBench: Benchmarking Offline Goal-Conditioned RL (arXiv 2410.20092), Seohong Park, Kevin Frans, Benjamin Eysenbach, Sergey Levine.
- **Venue:** ICLR 2025.
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the abstract.
- **Template credit:** footer says the template was partly borrowed from Michaël Gharbi and Jon Barron.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, 1440 screenshots (first viewport and tall), `css/app.css`, `/stylesheet.css`, `assets/ogbench.svg`, page HTML; 2026-10-28.
