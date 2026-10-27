# Scaling Chart Nerfies — Style Reference

> A one-chart argument: a big annotated scaling plot sits where the teaser video would be, then a grey abstract and a quiet grid of audio players tagged by GPU budget.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the title, authors, venue line, buttons, teaser image, section headings, audio tables, `pre` and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot and the full-page capture, and the page's own `static/css/index.css` plus an inline `<style>` block for GPU tags, over Bulma 0.9 from the Academic Project Page Template. Positions are document coordinates at 1440px wide.

## Overview

Slamming is a short Academic Project Page Template page (about 3,350px tall) that commits its teaser to a single matplotlib figure: a 912×752 scatter of TopicStoryCloze score against training compute, with labelled blue and green bubbles, a dashed red predicted-scaling line and a dashed purple "24h on A5000" marker. Above it sits the standard template hero: a two-line Google Sans 48px title with "Slamming" in italic, three #209cee author links with asterisks, an "equal contribution" note, a plain "ACL 2025 (Findings)" line, and four dark (#363636) pill buttons including a 🤗 "Models & Data" button. A #f5f5f5 abstract band follows. The "Generation Examples" section widens to a 1070px column and lays out native audio players in a four-column Bulma table; the column headers carry small colored GPU badges (green "1*A5000", yellow "4*A100", red "160*V100") that encode training cost. A second table of longer generations, a BibTeX `pre` and the #fafafa template footer close the page. Nothing else is colored.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 84.8%, chart bubble blue-grey #a9b8cd 4.4%, dark grey #605e60 3.2% (title, axis labels, buttons), near-white #fcfbfb 3.0%, pale bubble green #d9eaeb 2.2%, #fdfdfd 2.1%, remainder under 0.2%. The chart's blue and green bubbles, its red dashed line and the purple marker are the only color above the fold.

Anatomy in DOM order (y = top of element box):

1. **Title** (`h1.title.is-1.publication-title`), y 48, 960px, two lines, Google Sans 48px/54px weight 600, #363636, centered; "Slamming" in `<em>` (synthesized italic). Gap 24px.
2. **Authors** (`.publication-authors a`), y 182, Google Sans 20px/30px, three #209cee links each followed by a #4a4a4a asterisk. No gap.
3. **Equal-contribution note** (`span.author-block`), y 210, "* indicates equal contribution", 20px/30px #4a4a4a. No gap.
4. **Venue line** (`span.author-block`), y 240, "ACL 2025 (Findings)", 20px/30px weight 400 #4a4a4a, no badge. Gap 17px.
5. **Link buttons** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 287, Paper 105px, Code 100px, arXiv 98px, "🤗 Models & Data" 176px; 40px tall, #363636, white Noto Sans 16px/400, padding 7px 20px, icon left. The hero ends at y 392.
6. **Teaser chart** (`section.hero.teaser center img`), y 392, 912×752, centered, no frame; `.teaser .hero-body` has no top padding. The fold falls at the chart's 72.5 tick; the chart ends at y 1144 and the abstract band starts at y 1199.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Heading Ink | #363636 | Bulma `.title`, `th` | Title, white-section headings, table headers |
| Body Grey | #4a4a4a | Bulma body | Asterisks, notes, venue line, section intros, `pre` text |
| Band Text | rgba(0,0,0,.7) | Bulma `.hero.is-light` | "Abstract" heading and abstract text on the grey band |
| Author Blue | #209cee | `.publication-authors a` | Author names |
| Link Blue | #3273dc | Bulma `a` | Footer links (template credit, license) |
| Button Dark | #363636 | `.button.is-dark` | Paper, Code, arXiv, Models & Data (white text) |
| Band Grey | #f5f5f5 | `.hero.is-light`, `.content pre` | Abstract band, BibTeX block |
| Row Rule | #dbdbdb | Bulma `.table td` border, inline `thead` rule | 1px rules between audio rows; 2px header rules where a second header row exists |
| Row Hover | #fafafa | Bulma `.table.is-hoverable` | Audio row on hover; also the footer band |
| Small Compute | #6cbb3c | `.gpu-tag.small-compute` | "1*A5000" badge |
| Medium Compute | #ffbe0b | `.gpu-tag.medium-compute` | "4*A100" badge |
| Large Compute | #e63946 | `.gpu-tag.large-compute` | "160*V100" badge |
| Chart Blue | #a9b8cd | chart pixels (quantized) | Blue bubbles in the teaser chart |
| Chart Green | #d9eaeb | chart pixels (quantized) | Green bubbles in the teaser chart |
| White | #ffffff | page | Page, hero, examples, BibTeX section; GPU badge text |

## Tokens — Typography

- **Title, authors, teaser**: declared `'Google Sans', sans-serif`. Rendered: Google Sans 400 only (`fonts_loaded`); the 600 title and the italic "Slamming" are synthesized. Substitute: Figtree.
- **Body and headings**: declared `'Noto Sans', sans-serif`. Rendered: Noto Sans 400 only.
- **Code**: generic `monospace` (Consolas on Windows).

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 54px | 600 | #363636 |
| Section heading | `h2.title.is-3` | 32px / 36px | 600 | #363636, rgba(0,0,0,.7) on grey |
| BibTeX heading | `h2.title` | 28px / 31.5px | 600 | #363636, left |
| Authors, notes, venue | `.publication-authors` | 20px / 30px | 400 | #209cee / #4a4a4a |
| Body, intros | `.content p`, column text | 16px / 24px | 400 | #4a4a4a, intros centered, abstract justified |
| Table header | `th` | 16px | 700 | #363636, centered |
| GPU badge | `.gpu-tag` | 12.8px (0.8em) | 400 | #ffffff |
| Code | `pre code` | 14px / 21px | 400 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link button | 290486px | 1px transparent | none |
| GPU badge | 8px | none | none; padding 2px 6px, margin-top 4px |
| Audio table rows | 0 | 1px solid #dbdbdb bottom | none |
| Teaser chart | 0 | none (the chart has its own axis frame) | none |
| `pre` | 0 | none | none |

## Layout Metrics

- **Containers**: hero, teaser, abstract and BibTeX use `.container.is-max-desktop`, 960px (x 240–1200). The Generation Examples section uses the full Bulma `.container` (1344px at ≥1408px) with a four-fifths column, so the audio tables are 1070px wide (x 185–1255).
- **Hero**: `.hero-body` padding 48px 24px; title margin-bottom 24px; author, note and venue lines stack at 30px line height.
- **Teaser**: `.teaser .hero-body` padding 0 24px 48px; chart 912px wide (natural 1000×1000 attributes scaled down).
- **Sections**: `.section` padding 48px 24px; abstract in a 768px four-fifths column, justified.
- **Audio tables**: `table.audio-table.table.is-hoverable.is-fullwidth` with transparent background; header cells padding 8px 12px; each body row about 76px tall holding a full-width native `<audio>` control per cell; four columns in the first table, three in the second.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | 960px hero, 1344px examples container | 16px | 48px | as described |
| 1024–1407px | 960px hero; examples container 960–1152px | 16px | 48px | audio tables narrow with the container |
| 769–1023px | fluid, 24px | 16px | 48px | four-fifths columns remain |
| ≤768px | fluid, 24px | 16px | 48px | columns full width; audio tables keep four columns and the players shrink |

## Components

- **Dark pill button**: Bulma `.button.is-dark.is-rounded`, #363636, white 16px Noto Sans, padding 7px 20px, 40px tall, Font Awesome or Academicons icon left (an emoji for Hugging Face), no shadow.
- **Plain venue line**: the venue as an ordinary 20px #4a4a4a author line, no bold and no badge.
- **Chart teaser**: one large static PNG chart centered at 912px directly under the buttons, no caption, no frame.
- **GPU badge**: inline-block `div.gpu-tag` under a column title, 0.8em white text on #6cbb3c, #ffbe0b or #e63946, padding 2px 6px, 8px radius, 4px top margin. The color scale encodes training cost.
- **Audio comparison table**: Bulma hoverable full-width table, transparent background, bold centered column headers (model name, with `<em>` for the method), one native audio control per cell at 100% width, 1px #dbdbdb rules, hover row #fafafa.
- **Grey abstract band**: full-bleed #f5f5f5, padding 48px 24px, centered 32px heading and justified 16px text at rgba(0,0,0,.7).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title, authors, venue | yes | template hero, venue as plain text |
| Link buttons | yes | four dark pills |
| Teaser | present but non-standard | a scaling chart instead of a video or method figure |
| Abstract | yes | grey band |
| Audio samples | yes | Bulma tables of native players with GPU badges |
| Results table | present but non-standard | the chart carries the result; no numeric table |
| Method figure | absent from the source | |
| BibTeX | yes | grey `pre` |
| Navigation | absent from the source | |
| Footer | yes | #fafafa template credit |

## Adapting to Other Content

- **More authors**: keep one or two centered 20px lines with asterisks or superscripts, then the note and venue lines.
- **A results table**: a Bulma `.table.is-fullwidth.is-hoverable` in the 960px container, 16px, 700 #363636 headers with a 2px #dbdbdb rule under the header, 1px rules between rows, best values in bold; reuse the GPU badge colors to tag compute budgets.
- **Video samples**: replace each audio control with a 100%-width video in the same table cells.
- **News**: a short centered 16px list in a grey band between the chart and the abstract.
- **Long publication lists**: a single 960px column, 16px, bold titles and #3273dc links.
- **A second chart**: centered at 912px in its own white section with a 32px heading; keep charts unframed.

## Do's and Don'ts

- Do put the single most persuasive chart where the teaser goes, at full container width.
- Do use the green, yellow and red badge scale only for the cost dimension.
- Do keep audio tables transparent with hairline rules and no cell fills.
- Do keep the hero stock: Google Sans title, blue authors, dark pills.
- Don't caption or frame the chart; its annotations do the work.
- Don't introduce other accent colors; color lives in the chart and the badges.
- Don't let the examples table exceed the wide container; 1070px is already wider than the text column.

## Surfaces

White page with one full-bleed #f5f5f5 abstract band, #f5f5f5 BibTeX block and a #fafafa footer. No cards or shadows.

## Imagery

A matplotlib bubble chart (bubble size for model size, blue for speech-only models, green for models trained with text, a dashed red scaling line, a dashed purple compute marker, bold labels for the method). The rest of the media is audio, shown as Chrome's native grey player controls.

## Layout

A centered 960px Nerfies column for hero, chart, abstract and BibTeX, with a wider 1070px column for the audio tables. Rendered height is about 3,350px at 1440px.

## Agent Prompt Guide

Quick colors: title #363636, text #4a4a4a, authors #209cee, buttons #363636, band #f5f5f5, rules #dbdbdb, badges #6cbb3c / #ffbe0b / #e63946.

1. "Build a template hero in a 960px column: centered Google Sans 48px/54px weight 600 #363636 title with the method name in italic; 24px below, three #209cee author links with asterisks, then '* indicates equal contribution' and the venue as plain 20px/30px #4a4a4a lines; then four #363636 pill buttons, white 16px Noto Sans, padding 7px 20px, icon left. Directly below, a 912px centered chart image with no frame or caption."
2. "Add an audio comparison table: Bulma table, full width, hoverable, transparent background; bold 16px #363636 centered column headers, each with a small badge below (white 0.8em text, padding 2px 6px, 8px radius, #6cbb3c, #ffbe0b or #e63946 by compute budget); each cell holds a 100%-width native audio control; 1px #dbdbdb row rules; hover row #fafafa."
3. "Add an abstract band: full-bleed #f5f5f5, padding 48px 24px, a centered Noto Sans 32px/36px 600 'Abstract' heading and 16px/24px justified text in rgba(0,0,0,.7), 768px wide."

## Similar Pages

- Academic Project Page Template pages for speech and audio models with sample tables.
- Pages from the same lab (adiyoss-lab on pages.cs.huji.ac.il) share the template.

## Quick Start

```css
:root {
  --heading: #363636;
  --text: #4a4a4a;
  --band-text: rgba(0, 0, 0, .7);
  --author: #209cee;
  --button: #363636;
  --band: #f5f5f5;
  --rule: #dbdbdb;
  --row-hover: #fafafa;
  --gpu-small: #6cbb3c;
  --gpu-medium: #ffbe0b;
  --gpu-large: #e63946;
  --font-title: 'Google Sans', Figtree, sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --section-pad: 48px 24px;
}
```

## Provenance

- **URL**: https://pages.cs.huji.ac.il/adiyoss-lab/slamming/
- **Paper**: Slamming: Training a Speech Language Model on One GPU in a Day (arXiv 2502.15814), Gallil Maimon, Avishai Elmakies, Yossi Adi.
- **Venue**: ACL 2025 Findings.
- **Selection reason**: the arXiv 2502.15814 comment states ACL 2025 (Findings) and links the page. Chosen for using a large annotated scaling chart as the teaser, the grey abstract band and a tidy grid of audio players with colored GPU badges in the column headers.
- **Template credit**: footer credits the Academic Project Page Template, adopted from Nerfies.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot and full-page capture, `static/css/index.css`, the inline GPU-tag styles and the HTML. Date 2026-10-28.
