# StructVisuals Sunrise Leaderboard — Style Reference

> A benchmark report bound in a blue-to-tangerine sunrise: Georgia masthead, gradient pills, and a leaderboard that sorts itself.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's own `style.css`, the inline `<style>` blocks for the two leaderboards, and Bootstrap 5.3.0-alpha3 from jsDelivr. A global `*` rule sets `'Avenir', 'Avenir Next Cyr', …`; Avenir is not installed on Windows, so the self-hosted Avenir Next Cyr (400, 500, 700, 900) renders. The title asks for Playfair Display, which is never loaded, so it renders in Georgia. Color share is measured on the first viewport.

## Overview

A wide Bootstrap page (1320px container) that opens with a thin grey rule, a 96px chart-icon logo, and a two-line 48px Georgia bold masthead: "Factuality Matters:" in a blue (#0078d4) to violet (#8661c5) to tangerine (#ff9349) text gradient, then "When Image Generation and Editing Meet Structured Visuals" in black. A second rule closes the masthead. Below sit three lines of bold black author names, four lines of grey affiliations, and five pill links (Paper, Arxiv, Code, Dataset, StructBench) filled with the same sunrise gradient fixed to the viewport, so each pill shows a different slice: blue at the left, violet in the middle, rose at the right. The teaser is a 1296px Bootstrap thumbnail with a hairline border and 6px corners. The rest of the page is a stack of cards: an Abstract card on a pale blue-lilac-peach gradient, then a StructBench Leaderboard card with a cyan welcome alert and two sortable tables whose headers are pale blue and whose best and second-best accuracies carry small blue and green squares. A full-width sunrise gradient footer ends the page.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 64.2%, blue-grey #c5cbd5 9.7% and pale steel #e7eef2 7.2% (teaser panels), mauve #877286 6.5% (teaser chart and labels), blush #f9f0f2 5.7%, near-whites 6.8%. The gradient title and pills are each under 2%.

Anatomy in DOM order (`header.container`, 1320px, x=60–1380, padding 0 12px):

1. **Top rule** — Bootstrap `hr`, 1px, #212529 at 25% opacity (renders #c8c9ca), y≈16. Margin 16px 0.
2. **Logo** — `img`, 96×96px chart icon at x=128, y=33, margin-right 4.8px, inline before the title.
3. **Title** — `span.title-font.x-gradient-font` "Factuality Matters:" plus `a.title-font` "When Image Generation and Editing Meet Structured Visuals", 48px, weight 600 requested, rendered Georgia bold, line-height 72px; gradient text `linear-gradient(107.54deg, #0078d4 0.3%, #8661c5 40.23%, #ff9349 100%)` on the first part, #000000 on the rest; centered, two lines (y=53–216).
4. **Second rule** — Bootstrap `hr` as above (y≈240). Gap about 20px.
5. **Authors** — `.author-name a`, Avenir Next Cyr 18px / 500, #000000, 10px side margins, superscripts, three centered lines (y=260–336); hover #333333 underlined.
6. **Affiliations** — four `.col-12.organization` rows, 16px, #666666, 10px top margin each (about y=365–490).
7. **Link pills** — `#links`, five 140×38 slots with 8px side margins; each `a` 115×35px, padding 8px 16px, #ffffff 16px / 500, 50px radius, shadow `0 0 4px rgba(0,0,0,0.5)`, icomoon icon left, gradient fill with `background-attachment: fixed` (y=513–548).
8. **Teaser** — `figure > img.img-thumbnail`, 1296×446px at y=593 (x=72–1368), 4px padding, 1px #dee2e6 border, 6px radius, white fill; caption in Bootstrap `.figure-caption` (14px, #6c757d) centered below, with a bold "Overview of our work." lead.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | `body` | page, teaser thumbnail fill, card fill |
| Ink | #000000 | `.author-name a`, title link | title second part, author names |
| Bootstrap Body | #212529 | `--bs-body-color` | body text, table text, card titles (except Abstract) |
| Sunrise Blue | #0078d4 | x-gradient stop | title gradient start, link pills, footer, card-title bars |
| Sunrise Violet | #8661c5 | x-gradient stop | gradient middle |
| Sunrise Tangerine | #ff9349 | x-gradient stop | gradient end, link hover color |
| Link Periwinkle | #6567c9 | `a` | inline links |
| Affiliation Grey | #666666 | `.organization` | affiliations |
| Abstract Ink | #3f3f3f | `.x-gradient-block` | Abstract card text and title |
| Abstract Wash | #e6eff7 → #eeebf5 → #fcf4ee | `.x-gradient-block` | Abstract card background (107.54°) |
| Rule Grey | #c8c9ca | Bootstrap `hr` (25% opacity) | masthead rules |
| Thumb Border | #dee2e6 | `.img-thumbnail` | teaser border |
| Caption Grey | #6c757d | `.figure-caption`, `.text-bg-secondary` | figure captions, "Ours" badge fill |
| Table Head Blue | #cfe2ff | `.table-primary` | first header row of each leaderboard |
| Alert Cyan | #cff4fc | `.alert-info` | welcome alert fill |
| Alert Ink | #055160 | `.alert-info` | welcome alert text |
| Best Blue | #3b82f6 | inline `td.best::before` | 0.7em square before the best accuracy |
| Second Green | #22c55e | inline `td.second::before` | square before the second-best accuracy |
| Button Blue | #0d6efd | `.btn-primary` | Copy BibTex button |
| Code Pink | #d63384 | Bootstrap `code` | BibTeX text |
| Footer White | rgba(255,255,255,0.9) | `.footer-title` | footer text on the gradient |

## Tokens — Typography

- **Everything except the title:** global `* { font-family: 'Avenir', 'Avenir Next Cyr', 'Config', 'Microsoft YaHei', 'Times New Roman' }`; renders Avenir Next Cyr 400, 500, 700, 900 (self-hosted). On macOS, system Avenir renders instead. Substitute: Nunito Sans (close x-height and round geometry).
- **Title:** `.title-font` declares `"Playfair Display", Georgia, "Times New Roman", serif`; Playfair is not loaded, so Georgia bold renders. Substitute that keeps the rendered look: Gelasio Bold. If you want the intended face: Playfair Display 600.
- **Icons:** icomoon (self-hosted) in the link pills; Bootstrap Icons available.
- **Code:** Bootstrap `code` stack (SFMono-Regular, Menlo, Monaco, Consolas), 14px.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Masthead | `.title-font` | 48px / bold (Georgia) / 72px |
| Card title | `.card-title` | 32px / 800 (900 face) / 1.2 |
| Authors | `.author` | 18px / 500 / 27px |
| Affiliations | `.organization` | 16px / 400 |
| Link pills | `#links a` | 16px / 500 (17px on hover) |
| Body, table cells | `body`, `td` | 16px / 400 / 24px |
| Table headers | `th` | 16px / 700 |
| Figure caption | `.figure-caption` | 14px |
| Footer | `.footer-title`, `.footer-text` | 15px / 800 |
| Code | `code` | 14px / 21px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link pills | 50px radius, 115×35px (135×40px on hover), shadow `0 0 4px rgba(0,0,0,0.5)` (hover `0 0 6px rgba(0,0,0,0.75)`), 0.2s transition |
| Abstract card | 16px radius, no border |
| Other cards | Bootstrap `.card`, 6px radius, 1px rgba(0,0,0,0.175) border |
| Teaser thumbnail | 6px radius, 1px #dee2e6 border, 4px padding |
| Best / second markers | 0.7em squares with 2px radius, 0.4em right margin |
| Card-title bar | `hr.body-hr`, 5px tall gradient bar pulled up 1em under titles, shown at Bootstrap's 25% `hr` opacity |
| Alert | Bootstrap `.alert`, 6px radius, padding 16px |

## Layout Metrics

- **Container:** Bootstrap `.container`, max-width 1320px at ≥1400 with 12px side padding (content x=72–1368 at 1440).
- **Masthead:** `header.container` with rules above and below the title; logo and title on one centered line.
- **Cards:** stacked in `main.container`, card-body padding 16px; card titles margin-bottom 0.7em (22.4px).
- **Tables:** `.table-responsive`, full card width (1262px at 1440), 8px cell padding, numbers right-aligned with tabular figures.
- **Footer:** full-bleed gradient band, margin-top 80px, padding 16px 0, two columns (title left, credit right at ≥768).

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1400px | (viewport − 1296)/2 | 16px | 48px | five link pills on one row |
| 1200–1399px | (viewport − 1116)/2 | 16px | 48px | none |
| 992–1199px | (viewport − 936)/2 | 16px | 48px | title wraps to three lines |
| 768–991px | (viewport − 696)/2 | 16px | 48px | link pills wrap to two rows |
| 576–767px | (viewport − 516)/2 | 16px | 48px (no mobile rule) | footer columns stack and center; tables scroll horizontally |
| <576px | 12px | 16px | 48px | as above |

## Components

- **Gradient masthead:** 48px Georgia bold, the first phrase painted with the 107.54° sunrise gradient via `background-clip: text`, the rest black; a 96px icon before it; thin grey rules above and below.
- **Sunrise link pill:** 115×35px, #ffffff 16px / 500, padding 8px 16px, 50px radius, icon left with 8px gap, background `linear-gradient(107.54deg, #0078d4 0.39%, #8661c5 51.23%, #ff9349 100%) fixed` so a row of pills reads as one continuous gradient; soft dark glow; hover grows to 135×40 and 17px.
- **Gradient abstract card:** borderless card, 16px radius, background `linear-gradient(107.54deg, #e6eff7 0.39%, #eeebf5 51.23%, #fcf4ee 100%)`, centered 32px / 800 title and 16px #3f3f3f justified text.
- **Leaderboard card:** Bootstrap card with a left-aligned 32px title, a faint gradient bar, a cyan `.alert-info` welcome note with an emoji and contact links, a legend line with blue and green squares, then the table.
- **Sortable leaderboard table:** `.table.table-hover.align-middle`; first header row `.table-primary` #cfe2ff with bold group names (Math, Chart, Graph, Puzzle, Science, Table, Overall) and a rowspan "Model" cell; second row "Acc ↑ / PSNR ↑"; clickable headers show ▲/▼; best accuracy prefixed by a #3b82f6 square, second by #22c55e; proprietary models separated from open models by a heavier rule; the last row tagged with a #6c757d "Ours" badge and bold values.
- **Copy BibTeX:** Bootstrap `.btn-primary` #0d6efd, 6px radius, padding 6px 12px, under a `code` block in #d63384.
- **Gradient footer:** full-width sunrise gradient band, 15px / 800 white text at 90% and 70% opacity.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo + title | Yes | icon plus gradient-and-black Georgia masthead between rules |
| Authors / affiliations | Yes | bold black names, grey affiliation rows |
| Link buttons | Yes | five sunrise gradient pills |
| Teaser | Yes | 1296px thumbnail-framed overview figure with caption |
| Abstract | Yes | pastel gradient card |
| Leaderboard (HTML tables) | Yes | two sortable tables with best/second markers |
| Call for submissions | Yes | cyan alert inside the leaderboard card |
| Dataset / benchmark figures | Yes | cards titled "Structured Image Dataset", "Benchmark Construction" |
| BibTeX | Yes | pink `code` with a copy button |
| Footer | Yes | gradient band with credit |
| Navigation bar | No (absent from the source) | |
| Video | No (absent from the source) | |

## Adapting to Other Content

- **More authors:** keep `.author-name` inline blocks with 10px margins; three to four centered lines read fine at 18px / 500.
- **Results table:** this style already has one; for a new benchmark reuse `.table-primary` headers, the square best/second markers and the "Ours" badge, and keep numbers right-aligned in tabular figures.
- **Long publication or news list:** a Bootstrap card titled in 32px / 800 with the gradient bar, entries as a `list-group` with dates in #666666.
- **More links:** add pills; the fixed gradient means extra pills simply take the next slice of the sunrise.
- **Narrow screens:** add a font-size rule for `.title-font` below 768px (for example 32px); the source keeps 48px.

## Do's and Don'ts

- Do use the one sunrise gradient for the title phrase, pills, bars and footer.
- Do mark best and second-best with small colored squares rather than coloring the numbers.
- Do keep the Abstract on its pale gradient card and everything else on white Bootstrap cards.
- Don't mix serif into body text; Georgia is only the masthead.
- Don't give the pills individual gradients; `background-attachment: fixed` is what makes the row continuous.
- Don't depend on a font you do not load; name Georgia (or load Playfair) explicitly.

## Surfaces

White page; pastel gradient Abstract card; white bordered cards; #cfe2ff table headers; #cff4fc alert; full-bleed sunrise footer.

## Imagery

An infographic teaser (structured image generation and editing examples: math plots, charts, graphs, puzzles, tables; a "Structured vs Natural" comparison; a radial bar chart of scores), dataset sample grids and benchmark construction diagrams.

## Layout

A wide 1320px Bootstrap container with stacked cards; the masthead spans the full container. Rendered height about 7,500px.

## Agent Prompt Guide

Quick colors: gradient #0078d4 → #8661c5 → #ff9349, text #212529, names #000000, affiliations #666666, table head #cfe2ff, best #3b82f6, second #22c55e, abstract wash #e6eff7 → #eeebf5 → #fcf4ee with #3f3f3f text.

1. "Build a masthead: two thin #c8c9ca rules framing a centered 48px Georgia bold title at line-height 72px; the first phrase filled with linear-gradient(107.54deg, #0078d4 0.3%, #8661c5 40.23%, #ff9349 100%) via background-clip text, the rest #000000; then 18px weight-500 black author names and 16px #666666 affiliation rows."
2. "Create link pills: 115×35px, padding 8px 16px, #ffffff 16px/500 label with an icon, 50px radius, box-shadow 0 0 4px rgba(0,0,0,0.5), background linear-gradient(107.54deg, #0078d4 0.39%, #8661c5 51.23%, #ff9349 100%) fixed; on hover grow to 135×40px and 17px."
3. "Style a leaderboard: Bootstrap table-hover, first header row #cfe2ff with bold group names, second row 'Acc ↑ / PSNR ↑'; sortable headers with ▲/▼; best accuracy cells prefixed by a 0.7em #3b82f6 square with 2px radius, second-best by #22c55e; our row tagged with a #6c757d badge and bold numbers."

## Similar Pages

- Bootstrap-based benchmark pages from CUHK MMLab with leaderboard cards.
- Pages built from the same `x-gradient-font` stylesheet (blue-violet-tangerine 107.54° gradient on title text, pills and footer).

## Quick Start

```css
:root {
  --sunrise: linear-gradient(107.54deg, #0078d4 0.39%, #8661c5 51.23%, #ff9349 100%);
  --sunrise-soft: linear-gradient(107.54deg, #e6eff7 0.39%, #eeebf5 51.23%, #fcf4ee 100%);
  --text: #212529;
  --ink: #000000;
  --muted: #666666;
  --abstract-text: #3f3f3f;
  --link: #6567c9;
  --link-hover: #ff9349;
  --table-head: #cfe2ff;
  --best: #3b82f6;
  --second: #22c55e;
  --font-body: 'Avenir', 'Avenir Next Cyr', 'Nunito Sans', sans-serif;
  --font-title: Georgia, 'Gelasio', serif;
  --title-size: 48px;
  --title-lh: 72px;
  --pill-radius: 50px;
  --container: 1320px;
}
```

## Provenance

- **URL:** https://structvisuals.github.io/
- **Paper:** Factuality Matters: When Image Generation and Editing Meet Structured Visuals (arXiv 2510.05091), Le Zhuo et al.
- **Venue:** ICLR 2026 (per the arXiv comment; the page itself carries no venue line).
- **Selection reason:** the arXiv comment reads "Accepted by ICLR 2026" and links the page; chosen for its soft gradient-card look and a fully styled sortable leaderboard that marks best and second-best values in color. The uneven title comes from the missing Playfair font: Georgia bold sets the gradient phrase and black phrase with tight spacing and a wide 72px line-height.
- **Template credit:** none stated beyond the footer credit to the site author.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `style.css`, inline leaderboard styles, Bootstrap 5.3.0-alpha3 defaults, page HTML; 2026-10-28.
