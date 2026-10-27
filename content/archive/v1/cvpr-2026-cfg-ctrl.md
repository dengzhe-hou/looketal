# CFG-Ctrl Style Reference

> Twin monitors on a control-room desk, baseline left and ours right.

**Theme:** light

Measurements come from the page's own static/css/index.css, its HTML, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

CFG-Ctrl runs the 2025 refresh of the Academic Project Page Template (Bulma 0.9 plus a slate/blue variable layer and Inter) and adds one purpose-built module: a paired text-to-image comparison carousel. Each slide is two images side by side, capped at 420px each, under a column header where the baseline label is slate (#1e293b) and the method label is blueprint blue (#2563eb), 800 weight. Prompt captions below each pair highlight the key phrase in the same blue. Otherwise the page is spare: header, abstract band, method figure, comparison carousel, BibTeX.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Slate Ink | #1e293b | --text-primary | Body, title, button fill, left (baseline) column label |
| Blueprint Blue | #2563eb | --primary-color | Author links, right (method) column label, prompt emphasis, button hover, carousel dots |
| Deep Blueprint | #1d4ed8 | --primary-hover | Hover |
| Fog Slate | #64748b | --text-secondary | Abstract text, carousel subtitles |
| Mist Slate | #94a3b8 | --text-light | Minor icons |
| Paper White | #ffffff | --background-primary | Page |
| Frost Band | #f8fafc | --background-secondary | hero.is-light band, footer (measured rgb 248,250,252) |
| Ice Tile | #f1f5f9 | --background-accent | BibTeX pre (measured) |
| Hairline | #e2e8f0 | --border-color | Band and card borders |
| Orchid to Coral | #f093fb to #f5576c | --gradient-accent | Bar under section titles |
| Section Title Grey | rgba(0,0,0,0.7) | Bulma hero.is-light title colour | Section h2 inside light bands (measured) |
| Copied Green | #10b981 | (literal) | Copy-BibTeX success |

Bulma's default palette (#00d1b2, #ffdd57, #3273dc) is present in the framework file but not rendered.

## Tokens · Typography

- **Family**: Inter (Google Fonts) with "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif.
- **Mono**: browser monospace for BibTeX.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 800 | #1e293b, line-height 1.1 |
| Section title (h2.title.is-3) | 32px | 700 | rgba(0,0,0,.7) in bands, #1e293b elsewhere |
| Comparison column label | 19.2px (1.2rem) | 800 | #1e293b left, #2563eb right, letter-spacing .02em |
| Prompt caption (h2.subtitle) | 16px (1rem) | 500 | #64748b, emphasis #2563eb 700 |
| Authors | 20px | 600 | #2563eb |
| Body / abstract | 16px; abstract 17.6px | 400 | #1e293b / #64748b |
| Button | 16px | 600 | #ffffff |
| BibTeX | 14.4px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, pre, comparison images | 12px |
| Carousel card, video frames | 16px |
| Carousel dots, scroll-to-top | 50% |

- **Shadows**: md `0 4px 6px -1px rgb(0 0 0/.1), 0 2px 4px -2px rgb(0 0 0/.1)`, lg and xl steps as in the template; buttons lift 2px on hover.
- **Spacing changes vs stock refresh**: hero-body padding 2rem top, 4rem bottom; header 6rem 1.5rem 4rem.
- **Comparison grid**: flex row, gap 1.25rem, max-width 960px, each image calc(50% - .625rem) up to 420px.
- **Layout**: container.is-max-desktop (960px, inferred from class).

## Components

- **Link button**: dark slate (#1e293b) Inter 600 with 12px radius and shadow-md, hover #2563eb; Paper, Code, arXiv.
- **Comparison header**: `.comparison-header` flex row with `.comparison-col-left` (slate) and `.comparison-col-right` (blue) labels, 800 weight.
- **Comparison slide**: `.results-carousel .item .item-image`, two images side by side, 20px padding, 12px image radius.
- **Prompt caption**: centred h2.subtitle in #64748b with `.comparison-emphasis` spans in #2563eb 700.
- **Method figure**: inline image at 70% width, centred.
- **BibTeX**: #f1f5f9 pre, 12px radius, blue Copy button.
- **Footer**: #f8fafc with template credit and CC license.

## Page Modules

- **Title/author block**: h1, six authors, Tsinghua University, CVPR 2026 line, equal-contribution/corresponding notes.
- **Link buttons**: Paper, Code, arXiv.
- **Abstract**: light band.
- **Method figure**: "Method Overview" image.
- **Paired comparison carousel**: "Visual Comparison", 11 prompt slides (baseline vs CFG-Ctrl).
- **BibTeX** with copy button.
- **Absent**: teaser video, results table, slider, 3D, demo.

## Do's and Don'ts

- Do colour the method side blue and the baseline slate, consistently in labels and caption emphasis.
- Do cap each comparison image at 420px so pairs sit side by side at 960px.
- Do keep prompt text grey with only the tested phrase emphasized.
- Don't add a third colour for "ours"; blue already carries it.
- Don't let Bulma's pill radius override the 12px button radius.

## Surfaces

White page, #f8fafc bands with hairlines, #f1f5f9 code tiles, white carousel cards with soft shadows.

## Imagery

Generated images (square, photographic and typographic prompts) presented strictly in pairs. Diagrams for the method.

## Layout

Single column up to 960px. Rendered height about 4,800px.

## Agent Prompt Guide

Quick colors: text #1e293b, secondary #64748b, method blue #2563eb, band #f8fafc, code #f1f5f9, hairline #e2e8f0.

1. "Build a paired comparison slide: header row with 'Baseline' in #1e293b and 'Ours' in #2563eb, Inter 1.2rem/800; below, two images each calc(50% - .625rem) up to 420px with 12px radius and 1.25rem gap; caption 1rem/500 #64748b with the key phrase in #2563eb 700."
2. "Make dark link buttons: #1e293b fill, white Inter 600, 12px radius, shadow-md, hover #2563eb with 2px lift."
3. "Make a section title: 32px/700 Inter centred, with a 60x3px linear-gradient(135deg,#f093fb,#f5576c) bar beneath."

## Similar Pages

- Omni-MMSI (CVPR 2026), same template refresh.
- VideoScene (CVPR 2025), same author, older Nerfies-based template.

## Quick Start

```css
:root {
  --primary-color: #2563eb;
  --primary-hover: #1d4ed8;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --background-secondary: #f8fafc;
  --background-accent: #f1f5f9;
  --border-color: #e2e8f0;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --border-radius: 12px;
  --border-radius-lg: 16px;
  --compare-max: 960px;
  --compare-cell: 420px;
  --compare-gap: 1.25rem;
  --font-sans: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

## Provenance

- **URL**: https://hanyang-21.github.io/CFG-Ctrl/
- **Paper**: CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance (arXiv 2603.03281), Hanyang Wang et al.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states CVPR 2026 acceptance and links this page.
- **Template credit**: footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method**: extract_style.py on static HTML/CSS, a diff of this page's index.css against Omni-MMSI's copy of the same template (differences in hero padding and the comparison classes), and computed styles plus one reduced screenshot in a browser tab on 2026-10-27. The screenshot caught the fade-in animation mid-way, so colours were taken from computed style, not pixels.
