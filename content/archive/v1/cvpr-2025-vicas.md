# ViCaS Style Reference

> Annotator's highlighter pens on a grey dataset card.

**Theme:** light

Measurements come from the page HTML (inline colour spans), its static/css/index.css, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

ViCaS is a dataset page on the original Academic Project Page Template (Nerfies-derived, Bulma 0.9). The chrome is stock: Google Sans title, sky-blue authors, five charcoal pill buttons including a Hugging Face link. What sets it apart is a "Highlights" list that colour-codes three kinds of term in the running text: deep red for the data claim ("human-annotated"), cobalt for the two benchmark tasks, forest green for the baseline model name. A full-width sample video opens the page, and grey #f5f5f5 bands carry the abstract and benchmark sections. Carousel pagination dots are switched to black.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal | #363636 | Bulma text-strong (measured) | Title, section titles, button fill |
| Graphite | #4a4a4a | Bulma text (measured) | Body |
| Nerfies Sky | #209cee | hsl(204,86%,53%) (measured rgb 32,156,238) | Author links |
| Annotation Red | #c70909 | inline rgb(199,9,9) | Dataset property emphasis |
| Task Cobalt | #1032ab | inline rgb(16,50,171) | Benchmark task names |
| Baseline Forest | #136542 | inline rgb(19,101,66) | Baseline model name |
| Band Grey | #f5f5f5 | hero.is-light (measured rgb 245,245,245) | Abstract/benchmark bands, BibTeX |
| Band Title | rgba(0,0,0,0.7) | Bulma hero.is-light text | Text inside bands |
| Footer Haze | #fafafa | Bulma footer (measured) | Footer |
| Dot Black | #000000 | .slider-pagination .slider-page | Carousel dots |

Bulma's turquoise/yellow/link-blue defaults are framework-only.

## Tokens · Typography

- **Headings and authors**: Google Sans.
- **Body and section titles**: Noto Sans (measured on h2). Castoro loaded, unused.
- **Mono**: browser monospace.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #363636 |
| Section title (h2.title) | 32px | 600 | #363636 |
| Authors | 20px | 400 | #209cee |
| Highlights bullets | 20px (inline font-size) | 400 | #4a4a4a with coloured spans |
| Equal-contribution note | smaller | 400 | |
| Body | 16px | 400 | #4a4a4a |
| BibTeX | 14px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Video wrappers | 10px |
| Carousel items | none (padding 20px, overflow hidden) |

- **Shadows**: Bulma defaults only.
- **Layout**: Bulma container, `is-max-desktop` columns for text (inferred from template), full-width teaser video; hero is-big band for the abstract area.

## Components

- **Link button**: #363636 pill, white Noto Sans 16px, icon left; Paper, Supplementary, GitHub, Hugging Face (with emoji), arXiv.
- **Highlights list**: bulleted list at 20px with `<span style="color: rgb(...)">` emphasis in red, cobalt and green.
- **Grey band**: `hero is-light is-big` and `is-small` sections, #f5f5f5.
- **Carousel**: bulma-carousel with black pagination dots and 20px item padding.
- **BibTeX**: pre on #f5f5f5.
- **Footer**: #fafafa with template credit and CC license.

## Page Modules

- **Title/author block**: three-line title, three authors, ByteDance Inc.
- **Link buttons**: Paper, Supplementary, GitHub, HuggingFace (dataset), arXiv.
- **Teaser video**: "Dataset Sample" full-width video.
- **Highlights**: three coloured bullet claims.
- **Abstract**: grey band.
- **Benchmark Tasks**: figure.
- **Dataset Samples**: carousel.
- **Dataset Comparison**: comparison figure.
- **Method figure**: Video-LLaVA-Seg baseline architecture.
- **BibTeX**.
- **Absent**: slider, 3D, interactive demo (HF link is a dataset page, not a Space).

## Do's and Don'ts

- Do assign one colour per category of term (data, task, model) and keep it consistent.
- Do keep the colour coding inside body text only; chrome stays greyscale.
- Do put the dataset host (Hugging Face) among the primary buttons.
- Don't use more than three highlight colours.
- Don't recolour buttons; they stay #363636.

## Surfaces

White page, #f5f5f5 bands, #fafafa footer, flat.

## Imagery

Video frames with captions and segmentation masks, comparison tables rendered as images, an architecture diagram.

## Layout

Centred single column with a full-bleed sample video at top. Rendered height about 4,900px.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, authors #209cee, band #f5f5f5, data #c70909, task #1032ab, model #136542.

1. "Write a Highlights list at 20px in #4a4a4a where the dataset property is wrapped in #c70909, task names in #1032ab and the baseline model name in #136542."
2. "Make five pill buttons in #363636 with white Noto Sans labels: Paper, Supplementary, GitHub, HuggingFace, arXiv."
3. "Wrap the abstract in a Bulma hero is-light band (#f5f5f5) with a centred 32px/600 #363636 title."

## Similar Pages

- Original Academic Project Page Template pages.
- PAR, Translate Noise, VideoScene, Argus in this batch.

## Quick Start

```css
:root {
  --text-strong: #363636;
  --text: #4a4a4a;
  --link-author: #209cee;
  --band: #f5f5f5;
  --footer-bg: #fafafa;
  --hl-data: #c70909;
  --hl-task: #1032ab;
  --hl-model: #136542;
  --dot: #000000;
  --radius-pill: 290486px;
  --radius-video: 10px;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL**: https://ali2500.github.io/vicas-project/
- **Paper**: ViCaS: A Dataset for Combining Holistic and Pixel-level Video Understanding using Captions with Grounded Segmentation (arXiv 2412.09754), Ali Athar et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method**: extract_style.py on static HTML/CSS, index.css and inline spans read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. The inline rgb highlight values were converted to hex.
