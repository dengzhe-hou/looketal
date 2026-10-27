# CoSyn — Style Reference

> A university press catalogue: small-caps serif title, a colour wheel of specimens and an earthy bar chart.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero, teaser, chart, notes, carousels and footer), the 1440×900 and full-page screenshots plus a mid-page capture, and the page's `static/css/index.css`, inline `<style>` blocks and Chart.js settings read directly (Bulma 0.9 underneath). Crimson Text loads from Google Fonts in its 400 weight only, so the 600-weight title and headings are browser-synthesized bolds.

## Overview

A Nerfies/Bulma page set entirely in Crimson Text at a generous 22px body size. The hero is centred on white: a three-line 48px title in small caps (#363636), Bulma-blue author links with numeric superscripts, two lines of affiliations and the equal-contribution note in #4a4a4a, two #3273dc email links, and five dark #363636 rounded buttons (Paper, arXiv, Code, CoSyn-400K, CoSyn-Point). The teaser is a 960px autoplay video showing a radial wheel of nine dataset categories (Document, Chart, Math, Table, Diagram, Graphics…) over a mosaic of example images in muted terracotta, rose, sand and sage tiles. Under it, a centred 22px caption and a Chart.js horizontal bar chart: open-source models in pale olive #e9edc9, proprietary models in sage #ccd5ae, and "Ours" in tan #d4a373 with black outlines, followed by a small right-aligned bracketed note. Below come justified 22px sections with centred 32px headings, demo videos, three full-width Bulma carousels of generated examples with captions, a results table shown as an image, a second chart, a grey BibTeX block and a #fafafa footer. One demo video area loads lazily and shows as blank white space in a static capture.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 64.5% plus #fbfcfb 3.7%, #fffffd 2.2%, #fdffff 0.7%; teaser tile tones #c5beaf 10.2% (sand), #977971 7.0% (terracotta-brown), #d8e2df 6.3% (sage-grey), #f6ece5 5.3% (blush). Title, buttons and author links are too thin to form clusters.

Anatomy in DOM order (desktop 1440px; Bulma `.container.is-max-desktop` 960px at x=240):

1. **Title** (`h1.publication-title` with `.small-caps`, y=43, three lines, 171px): Crimson Text 48px/600 (synthesized), `font-variant: small-caps`, line-height 54px, #363636, centred. Gap 20px.
2. **Authors** (y=234 and 268): 20px/400, line-height 30px; names #209cee, commas and superscripts #4a4a4a. Gap 0.
3. **Affiliations and note** (y=301–368): 20px #4a4a4a, "¹University of Pennsylvania, ²Allen Institute for Artificial Intelligence" then "*Equal Contribution" on its own line.
4. **Emails** (y=371): 20px #3273dc links, two side by side. Gap 19px.
5. **Buttons** (y=416, 40px tall, 5px apart): #363636 rounded, white Crimson Text 16px, icons left (PDF, arXiv, GitHub, database ×2). Gap 65px.
6. **Teaser video** (`video#teaser`, y=521, 960×386): radial category wheel over an image mosaic; about 380px of it shows above the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Title Ink | #363636 | Bulma `$text-strong` | title, section headings, buttons |
| Body Grey | #4a4a4a | Bulma `$text` | body text, affiliations, captions, bracketed notes, BibTeX |
| Author Blue | #209cee | hsl(204,86%,53%) | author links |
| Link Blue | #3273dc | Bulma `$link` | email links, inline links |
| Chart Tan | #d4a373 | (Chart.js) | "Ours" bars, with #000000 outline |
| Chart Sage | #ccd5ae | (Chart.js) | proprietary-model bars and legend |
| Chart Olive Mist | #e9edc9 | (Chart.js) | open-source-model bars and legend |
| Code Grey | #f5f5f5 | Bulma `pre` | BibTeX block |
| Footer Grey | #fafafa | Bulma footer | footer band |
| Modal Shade | rgba(0,0,0,0.8) | (inline style) | image zoom modal backdrop |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | 'Crimson Text', sans-serif | Crimson Text 400; 600 synthesized | Crimson Pro (has real 600) |
| Mono | Bulma monospace | Consolas | Courier Prime |
| Icons | Font Awesome 5 (SVG), Academicons | Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `.title.is-1.publication-title .small-caps` | 48px / 600 / 54px, small caps | #363636 |
| Section heading | `h2.title.is-3` | 32px / 600 / 36px, centred | #363636 |
| Body | `body` (index.css) | 22px / 400 / 1.5 (33px) | #4a4a4a |
| Section text | `.content.has-text-justified p` | 22px / 400 / 33px, justified | #4a4a4a |
| Authors / affiliations | `.publication-authors` (`is-size-5`) | 20px / 400 / 30px | #209cee links, #4a4a4a text |
| Buttons | `.button.is-dark.is-rounded` | 16px / 400 | #ffffff |
| Figure caption | `p.has-text-centered` | 22px / 400, centred | #4a4a4a |
| Bracketed note | `h2.subtitle` (inline `font-size: medium`) | 16px / 400 / 20px, right-aligned | #4a4a4a |
| Carousel caption | `.caption` | 22px / 400, centred | #4a4a4a |
| Chart labels | Chart.js | Crimson Text 18px; "Ours" rows bold | chart default grey |
| BibTeX | `pre` | 16px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 290486px (Bulma rounded) | 1px transparent | none |
| Teaser video, figures, carousel images | 0 | none | none |
| "Ours" chart bars | 0 | 1px #000000 | none |
| Carousel arrows | fully round (42px) | 1px #ffffff | 0 2px 5px rgba(50,50,50,0.1) |
| BibTeX pre | 0 | none | none |

Nothing on the page is rounded apart from the buttons and carousel arrows.

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop` 960px (x=240); content columns `is-five-fifths` with 12px padding; sections padding 48px 24px.
- **Hero**: Bulma `.hero-body` padding 48px 24px with `padding-bottom: 0` on the hero; title starts at y=43.
- **Teaser block**: `#demo` section with no top padding; video full 960px; caption directly under it; chart wrapper `width: 100%; margin: 20px auto` with a 300px canvas; bracketed note right-aligned, 10px below.
- **Carousels**: the example carousels run at Bulma's full container width (1344px at x=48), images fixed at 200px tall, three per view, 42px white round arrows at the edges.
- **Results**: table image at 960px with a justified bracketed note under it.
- **Footer**: #fafafa, padding 48px 24px 96px, centred icon links (25px black) and a reference line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px | (100% − 960px)/2 | 22px | 48px | carousels span 1344px |
| 1024–1215px | (100% − 960px)/2 | 22px | 48px | carousels narrow with the container |
| 769–1023px | 24px (fluid container) | 22px | 48px | — |
| ≤768px | 24px | 22px (no override) | 48px (Bulma keeps is-1) | Bulma columns stack; carousels show one slide |

## Components

- **Small-caps title**: Crimson Text in `font-variant: small-caps`, 48px, three centred lines broken by hand.
- **Dark pill button** (Bulma `.button.is-dark.is-rounded`): #363636, white 16px serif, 40px tall, padding 7px 20px, icon left; five in a row, wrapping.
- **Teaser video**: autoplay muted loop, full 960px, no frame, with a centred 22px caption beneath.
- **Earthy bar chart** (Chart.js horizontal bar): bars #e9edc9 (open-source), #ccd5ae (proprietary), #d4a373 with 1px #000000 border (ours); legend boxes on top; Crimson Text labels at 18px, bold for "Ours" rows; light grid; x-axis 60–83.
- **Bracketed note** (`h2.subtitle`): 16px #4a4a4a right-aligned (or justified) text in square brackets, 10px above the next caption.
- **Example carousel** (Bulma carousel): slides of a 22px caption above a 200px-tall image (`object-fit: contain`), white circular arrows with a soft shadow; images zoom into a dark modal on click.
- **BibTeX**: Bulma `pre`, #f5f5f5, padding 20px 24px, 16px monospace.
- **Footer**: #fafafa band, black icon links, centred 22px credit text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | small-caps serif title, blue author links, emails |
| Venue | absent from the source | no ACL line on the page |
| Link buttons | yes | five dark rounded buttons |
| Teaser | yes | radial category-wheel video |
| Headline chart | yes | Chart.js bar chart in earthy greens and tan |
| Abstract | yes | justified 22px paragraph under a centred heading |
| Method demo | yes | video (lazily loaded; blank in a static capture) |
| Example gallery | yes | three full-width Bulma carousels with captions |
| Results tables | present but non-standard | the main results table is an image with a bracketed note |
| Generalization and pointing | yes | videos with captions and a second chart |
| BibTeX | yes | grey Bulma pre |
| Footer | yes | Nerfies-style credit |

## Adapting to Other Content

- **An HTML results table**: set it in Crimson Text 18px, booktabs style (2px #363636 top and bottom rules, 1px under the header), best values bold and second-best underlined to match the image table; bracketed note right-aligned below.
- **More authors**: keep 20px author lines with numeric superscripts; put affiliations on one line and notes on the next.
- **More charts**: reuse the three bar colours (#e9edc9, #ccd5ae, #d4a373 with a black outline for your method) and Crimson Text labels.
- **News or publication lists**: 22px justified paragraphs with bold dates; no cards or tints.
- **A venue**: add a 22px small-caps #363636 line between the title and authors rather than a badge.

## Do's and Don'ts

- Do keep the whole page in Crimson Text; the small-caps title is the signature.
- Do keep the palette earthy and muted (sand, sage, terracotta, tan) in figures and charts.
- Do keep body text large (22px) and justified in the 960px column.
- Don't add colour to headings or buttons; they stay #363636.
- Don't round or shadow figures; only buttons and carousel arrows are round.
- Don't rely on lazily loaded media near the top without a poster image; static captures show a blank box.

## Surfaces

White throughout, #f5f5f5 BibTeX, #fafafa footer, a dark modal for zoomed images.

## Imagery

A radial wheel of synthetic text-rich images (documents, charts, math, tables, diagrams, chemical structures, circuits, music sheets, vector graphics) over tiles tinted terracotta, rose, sand and sage; example renders of charts, menus, business cards, booking sites; a booktabs results table image; demo videos.

## Layout

Centred hero; teaser video and headline chart; Abstract; Code Guided Synthetic Data Generation; CoSyn can Generate Diverse Text-rich Images (carousels); Model Trained on CoSyn-400K Achieves SOTA Performance; Domain Generalization; Synthetic Pointing Data; BibTeX; footer. About 6,400px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, authors #209cee, links #3273dc, chart #e9edc9 / #ccd5ae / #d4a373, code #f5f5f5, footer #fafafa.

1. "Build a centred serif hero in a 960px column: title Crimson Text 48px/600 in font-variant small-caps, #363636, line-height 54px, three lines; authors 20px with #209cee links and #4a4a4a superscripts; affiliations 20px #4a4a4a; emails 20px #3273dc; then five #363636 fully rounded 40px buttons with white 16px labels and icons left."
2. "Make a horizontal bar chart with Chart.js: open-source bars #e9edc9, proprietary bars #ccd5ae, our bars #d4a373 with a 1px #000000 border; Crimson Text 18px labels, our rows bold; legend on top; then a right-aligned 16px #4a4a4a bracketed note."
3. "Write body sections: centred h2 Crimson Text 32px/600 #363636, 24px below it a justified 22px/33px #4a4a4a paragraph in the 960px column; figures and videos full width with no radius or shadow, captions centred 22px."

## Similar Pages

- Nerfies/Bulma pages restyled with a single serif family and small caps.
- Dataset pages that open on a radial or mosaic overview of data categories.

## Quick Start

```css
:root {
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --link: #3273dc;
  --bar-open: #e9edc9;
  --bar-proprietary: #ccd5ae;
  --bar-ours: #d4a373;
  --code-bg: #f5f5f5;
  --footer: #fafafa;
  --serif: 'Crimson Text', Georgia, serif;
}
body { font-family: var(--serif); font-size: 22px; line-height: 1.5; color: var(--text); background: #ffffff; }
.small-caps { font-variant: small-caps; }
.container.is-max-desktop { max-width: 960px; margin: 0 auto; }
```

## Provenance

- **URL**: https://yueyang.ai/cosyn/
- **Paper**: Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation (arXiv 2502.14846), Yue Yang, Ajay Patel et al.
- **Venue**: ACL 2025.
- **Selection reason**: existing verified entry; the arXiv comment states publication in ACL 2025 and links this page.
- **Template credit**: footer says the website was developed by referencing the Nerfies project page.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and components, the 1440×900 and full-page screenshots, a mid-page capture of the carousels and results table, and `index.css`, inline styles and the Chart.js configuration read directly, on 2026-10-28.
