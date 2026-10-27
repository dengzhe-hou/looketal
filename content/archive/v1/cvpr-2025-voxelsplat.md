# VoxelSplat Style Reference

> Cotton-candy dawn over a driving simulator.

**Theme:** light

Measurements come from the single HTML file (one `<style>` block, no external CSS or framework) and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

VoxelSplat is hand-written HTML in Arial. Its header is a pastel left-to-right gradient, pale turquoise to pink at 60% opacity, with the title in dark grey and the method name picked out in Bootstrap blue (#007bff). Authors are navy (#024fa1). Three fully rounded buttons each get their own colour: saffron for arXiv, Bootstrap green for Code, and a hot-pink-to-orange gradient for BibTeX. Below, everything sits in a 900px column of justified Arial text and full-width figures, with a plain grey Courier BibTeX box at the end.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Lagoon Mist | rgba(175,238,238,0.6) | .hero gradient start | Header gradient, left |
| Blossom Mist | rgba(251,207,251,0.6) | .hero gradient end | Header gradient, right |
| Title Grey | #333333 | .hero h1, captions | Title, image captions, BibTeX heading |
| Signal Blue | #007bff | .hero-title-highlight, .button | Method name in title, generic button |
| Deep Signal | #0056b3 | .button:hover | Generic button hover |
| Harbor Navy | #024fa1 | .hero-authors | Author line |
| Affiliation Grey | #555555 | .hero-affiliations | Affiliations |
| Saffron | #fcb636 | .btn-arxiv | arXiv button (hover #e0a22f) |
| Field Green | #28a745 | .btn-code | Code button (hover #218838) |
| Flare Pink to Ember | #ff416c to #ff4b2b | .btn-citation | BibTeX button gradient (45deg) |
| Near Black | #222222 | .image-labels, .bibtex-container | Labels, BibTeX text |
| Code Grey | #f7f7f7 | .bibtex-container | BibTeX box |
| Box Line | #dddddd | .bibtex-container border | BibTeX border |

## Tokens · Typography

- **Family**: Arial, sans-serif everywhere.
- **Mono**: 'Courier New', monospace for BibTeX.
- **No webfonts.**

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (.hero h1) | 35.2px (2.2rem) | 700 | #333333, line-height 1.3 |
| Venue (.conference) | 24px | bold | #000000 |
| Authors | 16px (1rem) | 400 | #024fa1 |
| Affiliations | 14.4px (0.9rem) | 400 | #555555 |
| Hero button | 16px | 500 | #ffffff |
| Section title (h2) | 24px | 700 | #000000 |
| Body / abstract | 16px | 400 | line-height 1.6, justified |
| Image caption | 15px | 400 | #333333, justified |
| Image labels | 14px | 500 | #222222 |
| BibTeX | 14px Courier New | 400 | #222222, line-height 1.5 |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Hero buttons | 25px (pill) |
| Flow comparison image | 6px |
| Generic button | 5px |
| Row images, BibTeX box | 4px |

- **Shadows**: row images only, `0 0 5px rgba(0,0,0,0.1)`.
- **Spacing**: hero padding 40px 20px; hero buttons padding 10px 20px with 10px gap; BibTeX section 40px vertical margin; image rows 20px gap.
- **Layout**: `.container` 80% wide with 20px padding; abstract, figures, captions and BibTeX capped at 900px; paired row images max 420px.

## Components

- **Gradient hero**: full-width band, linear-gradient(to right, rgba(175,238,238,.6), rgba(251,207,251,.6)), centred content.
- **Colour-coded pill buttons**: `.hero-buttons .btn` inline-flex row, 25px radius, white 500 text; arXiv #fcb636, Code #28a745, BibTeX gradient #ff416c to #ff4b2b (hover opacity .9).
- **Figure block**: image max 900px, centred, with a 15px justified caption padded 10px 20px.
- **Flow comparison grid**: 80px label column with vertical-rl row labels, image in the second column, 6px radius.
- **Image labels row**: flex space-between labels in 14px/500 above or below a grid image.
- **BibTeX box**: #f7f7f7, 1px #ddd border, 4px radius, Courier New 14px, white-space pre, preceded by an h3 at 20px.

## Page Modules

- **Title/author block**: gradient hero with highlighted method name, six authors, Nankai University, UIUC, Baidu VIS; "CVPR 2025" line.
- **Link buttons**: arXiv, Code, BibTeX (anchor to the BibTeX section).
- **Abstract**: justified, with bolded contribution labels.
- **Video demo**: "Video Demo" section with two videos.
- **Method figure**: "Method Overview".
- **Results**: "Improvement on nuScenes Dataset", "Occupancy Prediction", "Scene Flow Prediction", convergence plot, rendering visualizations, all as images with labels.
- **BibTeX**.
- **Absent**: carousel, slider, 3D viewer (extractor flag fired on "Splatting"), table, footer credit.

## Do's and Don'ts

- Do keep the hero gradient translucent (0.6 alpha) so it stays pastel.
- Do give each primary link its own saturated pill colour, as here.
- Do cap text and figures at 900px.
- Don't mix more gradients in; the BibTeX button is the only gradient besides the hero.
- Don't use the generic #007bff .button alongside the coloured pills (it is declared but off-pattern).

## Surfaces

Pastel gradient hero, then plain white. A single grey code box. Almost no shadow.

## Imagery

Driving-scene occupancy renders, flow fields, nuScenes comparisons and plots, arranged in 900px blocks or 420px pairs.

## Layout

Gradient header band, then a centred 80% container with 900px inner blocks. Rendered height about 4,700px.

## Agent Prompt Guide

Quick colors: hero rgba(175,238,238,.6) to rgba(251,207,251,.6), title #333333 with highlight #007bff, authors #024fa1, arXiv #fcb636, Code #28a745, BibTeX #ff416c to #ff4b2b, code box #f7f7f7 with #ddd.

1. "Build a pastel hero: linear-gradient(to right, rgba(175,238,238,.6), rgba(251,207,251,.6)), padding 40px 20px, centred Arial 2.2rem/700 title in #333 with the method name in #007bff, authors 1rem #024fa1, affiliations .9rem #555."
2. "Add three pill buttons (25px radius, padding 10px 20px, white 500 text): arXiv #fcb636 (hover #e0a22f), Code #28a745 (hover #218838), BibTeX linear-gradient(45deg,#ff416c,#ff4b2b)."
3. "Add a BibTeX box: max-width 900px, #f7f7f7 background, 1px solid #ddd, 4px radius, 12px padding, Courier New 14px, line-height 1.5, color #222, white-space pre."

## Similar Pages

- Track4Gen in this batch (framework-free, single file).
- Hand-written project pages with Bootstrap-era colour buttons.

## Quick Start

```css
:root {
  --hero-from: rgba(175, 238, 238, 0.6);
  --hero-to: rgba(251, 207, 251, 0.6);
  --title: #333333;
  --highlight: #007bff;
  --authors: #024fa1;
  --affil: #555555;
  --btn-arxiv: #fcb636;
  --btn-code: #28a745;
  --btn-cite: linear-gradient(45deg, #ff416c, #ff4b2b);
  --code-bg: #f7f7f7;
  --code-border: #dddddd;
  --radius-pill: 25px;
  --content-max: 900px;
  --font-sans: Arial, sans-serif;
  --font-mono: 'Courier New', monospace;
}
```

## Provenance

- **URL**: https://zzy816.github.io/VoxelSplat-Demo/
- **Paper**: VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction (arXiv 2506.05563), Ziyue Zhu et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: none stated; custom single-file page (comments in the CSS are in Chinese).
- **Measurement method**: extract_style.py on the static HTML, the full style block read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27.
