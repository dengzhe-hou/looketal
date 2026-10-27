# SatNav Survey Plate — Style Reference

> A VGGT-style white title page that turns into a data-desk of charts and flight logs.

**Theme:** light

Values come from nine section stylesheets (`header.css`, `teaser.css`, `navigation.css`, `statistics.css`, `results.css`, `framework.css`, `memory-ablation.css`, `real-world.css`, `citation.css`). The header file's own comment says the opening is a local rebuild using VGGT's page as visual reference. No framework is loaded. Roles are interpreted. Rendered output was not viewed.

## Overview

SatNav is a benchmark page for long-horizon UAV vision-language navigation. Its opening imitates the Nerfies/VGGT look without Bulma: white page, Bulma-ink `#363636` text, Noto Sans (self-hosted as `SatNavSans`, 400 and 600), a 48px project name over a balanced subtitle, cyan-blue author names `#1687ba`, a venue line in plain 21–28px text, and a row of six charcoal pill buttons (Paper, Code, 🤗 Dataset, 🤗 Models, SwiftVLN, Wiki). Below the abstract, each section is a hand-built data visualization: an interactive satellite-view canvas, three donut-style statistic charts, an animated dot-and-bar results chart with per-benchmark accent colors, a framework figure, a memory ablation, real-world flight videos, and a GitHub-like citation box.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper | `#ffffff` | `--paper` | Page background, button text |
| Bulma Ink | `#363636` | `--ink`, `--button` | Text, headings, pill buttons |
| Pill Pressed | `#242424` | `--button-hover` | Button hover |
| Secondary Gray | `#555555` | `--secondary` | Venue-adjacent notes, captions, citation intro |
| Author Cyan | `#1687ba` | `--author` | Author names |
| Focus Blue | `#167eb0` | `--focus` | Focus outlines |
| Results Blue | `#287ac3` | `--result-accent` | Primary benchmark accent in results and ablation |
| Forest Accent | `#218057` | `--result-accent` (variant) | Second benchmark accent |
| Ochre Accent | `#91680b` | `--result-accent` (variant) | Third benchmark accent |
| Mint Soft | `#eff8f3` | `--result-soft` | Table header fill (green variant) |
| Sky Soft | `#f3f8fc` | `--result-soft` | Table header fill (blue variant) |
| Grid Line | `#eef1f4` | `--result-grid` | Table row rules |
| Rule Gray | `#dce3eb` | `--teaser-rule`, citation border | Citation box border, rules |
| Code Panel | `#f6f8fa` | (literal) | Citation box background |
| Stripe | `#fafbfc` | (literal) | Odd table rows |
| Muted Slate | `#667080` | `--teaser-muted` | Teaser status text |

Teaser tokens also define `--teaser-blue #3880ed`, `--teaser-green #77a83f`, `--teaser-yellow #e8b800`, `--teaser-red #ef4657` for trajectory overlays; statistics charts use softer `#638ff5`, `#62d7a8`, `#ffa34d` sector fills.

## Tokens — Typography

- **Family:** `SatNavSans` = self-hosted Noto Sans 400/600, fallback Segoe UI, sans-serif.
- **Mono:** ui-monospace, SFMono-Regular, Consolas, "Liberation Mono".
- **Weights:** 400 and 600 only.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Project name | 48px (42px mobile) | 600 | 1.15 | |
| Subtitle | `clamp(25px, 3.1vw, 36px)` | 600 | 1.25 | -0.85px, `text-wrap: balance` |
| Venue line | `clamp(21px, 2.4vw, 28px)` | 400 | 1.6 | |
| Authors | 20px (18/16px mobile) | 400 | 1.6 | |
| Affiliations | 17px | 400 | 1.7 | |
| Section h2 | 32px (28px mobile) | 600 | 1.25 | -0.5px, centered |
| Abstract body | 17px | 400 | 1.8 | left-aligned |
| Button | 16px (14px ≤420px) | 400 | 1.5 | |
| Citation code | 14px | 400 | 1.8 | |
| Chart labels, notes | 12–13px | 400/600 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Resource pill buttons | 999px |
| Citation box, nav panels | 8px |
| Ablation cards / table chips | 5–6px |
| Real-world thumbnails | 4px |
| Result dots | 50% |

- **Shadows:** none in the measured CSS; separation is by hairlines and soft fills.
- **Layout widths:** header 1120px (h1 1060px, authors 740–940px); teaser `min(1056px, 80% - 38.4px)`; abstract 860px; citation 960px.
- **Rhythm:** header padding 48px 28px 64px; sections end with 72–80px bottom margin (48px mobile).

## Components

- **Resource pill.** `#363636` fill, white text, min-height 41px, 8px 18px padding, 8px gap between 17px stroked SVG icon (or 🤗 emoji) and label, 7px gap between pills. Hover `#242424`; 3px `#167eb0` focus ring.
- **Venue line.** Plain text, `margin: -6px auto 26px`, no badge.
- **Results chart.** Grid rows `150px | 1fr | 140px`; each model is a track with an 11px ringed dot sliding to its score; accent per benchmark via `--row-color`.
- **Results table.** Right-aligned numerals, 10px 9px padding, soft-tinted header, odd rows `#fafbfc`, best value 600 weight and underlined, caption below in gray.
- **Statistics charts.** Three charts per row, 24px gap, sector strokes in white, centered legends.
- **Citation box.** `#f6f8fa`, 1px `#dce3eb` border, 8px radius, toolbar row with a 13px/600 label and copy button.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered, two-tier title, cyan author names |
| Venue badge | Plain text "NeurIPS 2026 Evaluations & Datasets" | |
| Link buttons | Paper, Code, Dataset (HF), Models (HF), SwiftVLN, Wiki | Charcoal pills |
| Teaser | Video in fixed-aspect stage | |
| Abstract | Yes | 860px, 32px centered heading |
| Interactive demo | Canvas satellite view with heading (no WebGL 3D) | |
| Dataset statistics | Three charts | |
| Results | Animated chart plus tables | Per-benchmark accent colors |
| Method figure | SwiftVLN framework | |
| Ablation | Memory module section | |
| Real-world videos | UAV flights | |
| BibTeX | Citation box | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep the header monochrome; color belongs to the data sections.
- Do give each benchmark its own accent and reuse it across chart, table header tint and hover.
- Do use plain text for the venue; pills are reserved for resources.
- Don't add drop shadows; this page has none.
- Don't use more than two weights.

## Surfaces

White page; soft tinted fills (`#f3f8fc`, `#eff8f3`) only inside tables and charts; `#f6f8fa` for the citation box.

## Imagery

Satellite map crops, trajectory overlays and UAV flight videos; charts are drawn in SVG/HTML rather than embedded as images.

## Layout

Centered single column whose width changes per section (860 to 1120px). Statistics use a 3-column grid; results rows stack labels above tracks under 700px.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, ink `#363636`, secondary `#555555`, authors `#1687ba`, accent `#287ac3`, alt accents `#218057` and `#91680b`, rules `#dce3eb`, code `#f6f8fa`.

1. "Build a centered header in Noto Sans: 48px/600 project name, balanced 36px subtitle, 20px authors with `#1687ba` names, a plain 28px venue line, then charcoal `#363636` pill links 41px tall with 17px line icons."
2. "Make a results chart row: grid `150px 1fr 140px`, a light track with an 11px white dot ringed in `#287ac3` positioned at the score, value text right-aligned."
3. "Style a citation box: `#f6f8fa`, 1px `#dce3eb` border, 8px radius, a toolbar with 'BibTeX' at 13px/600 gray and a copy button, then 14px/1.8 mono pre."

## Similar Pages

VGGT's project page (named in the CSS as the visual reference) and other Nerfies-derived pages; KungfuBot and V2W in this collection share the header look.

## Quick Start

```css
:root {
  --paper: #ffffff; --ink: #363636; --secondary: #555555;
  --author: #1687ba; --button: #363636; --button-hover: #242424; --focus: #167eb0;
  --accent: #287ac3; --accent-2: #218057; --accent-3: #91680b;
  --soft: #f3f8fc; --grid: #eef1f4; --rule: #dce3eb; --code: #f6f8fa;
  --font: "Noto Sans", "Segoe UI", sans-serif;
  --mono: ui-monospace, SFMono-Regular, Consolas, monospace;
  --radius-pill: 999px; --radius-box: 8px;
}
```

## Provenance

- **URL:** https://eku127.github.io/SatNav/
- **Paper:** SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation (arXiv 2609.31507), Jiajun Jiang et al.
- **Venue:** NeurIPS 2026, Evaluations and Datasets Track
- **Selection reason:** arXiv comment states acceptance at the NeurIPS 2026 Track on Evaluations and Datasets and links this page.
- **Template credit:** none in footer; `header.css` comment cites VGGT's page as visual reference for a local rebuild.
- **Measurement method:** static HTML plus nine stylesheets parsed with `extract_style.py` and read directly. Not viewed in a browser; chart animation and canvas behavior are described from CSS and markup only.
