# Translate Noise Style Reference

> A darkroom light table with a sliding loupe.

**Theme:** light

Measurements come from the page HTML (including its inline `<style>` block), its local static/css/index.css, and computed styles read in a rendered browser tab. Values are normalized to hex; roles are interpreted from where each value is applied.

## Overview

This is a near-stock Nerfies page (Bulma 0.9, Google Sans + Noto Sans) whose personality comes from content, not chrome. Under a centred Google Sans title sit a "CVPR 2026 Findings" subtitle, sky-blue author links and three charcoal pill buttons. The body is a run of noisy/clean image pairs, each shown in a custom before/after slider: a 4px white divider with a 20px white knob and black-translucent corner labels. Everything stays greyscale so the denoising results carry the colour.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal | #363636 | Bulma text-strong (measured rgb 54,54,54) | Title, pill button fill |
| Graphite | #4a4a4a | Bulma text (measured rgb 74,74,74) | Body copy, subtitles |
| Nerfies Sky | #209cee | hsl(204,86%,53%) in index.css (measured rgb 32,156,238) | Author links |
| Venue Grey | #555555 | .publication-venue | Venue label style |
| Plate Grey | #f5f5f5 | Bulma light / pre | BibTeX pre, interpolation panel |
| Footer Haze | #fafafa | Bulma footer (measured rgb 250,250,250) | Footer band |
| Frame Line | #bbbbbb | .results-carousel .item border | Carousel item border |
| Slider White | #ffffff | .slider-handle | Divider line and knob |
| Label Veil | rgba(0,0,0,0.5) | .overlay-text | "Noisy"/"Clean" label chip |
| Award Pink | #ff3860 | .publication-awards | Declared, unused here |

Bulma's #00d1b2, #ffdd57 and #3273dc appear in raw frequency counts only through the framework stylesheet.

## Tokens · Typography

- **Display/heading**: Google Sans (Google Fonts), sans-serif fallback.
- **Body**: Noto Sans, sans-serif.
- **Also loaded**: Castoro (unused on rendered elements checked).
- **Mono**: browser monospace in the BibTeX pre.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #363636 |
| Venue subtitle | 24px (is-size-4, inferred) | 400 | #4a4a4a |
| Authors | 20px | 400 | #209cee |
| TL;DR line (h2) | 20px | 400 | #4a4a4a |
| Section title (h2.title.is-3) | 32px (inferred from Bulma is-3) | 600 | #363636 |
| Body | 16px | 400 | #4a4a4a |
| Slider label | 16px | bold | #ffffff with 1px 1px 2px black text-shadow |
| BibTeX | 14px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (full pill) |
| Carousel items, interpolation panel | 10px |
| Slider labels, interpolation images | 5px |
| Slider knob | 50% |

- **Shadows**: none of its own; Bulma's focus ring `0 0 0 .125em rgba(50,115,220,.25)` only.
- **Layout**: Bulma container (1152/1344px breakpoints) with the comparison area capped at 900px and 90% wide, centred; 20px gap between stacked comparisons; images aspect-ratio 1/1.

## Components

- **Link button**: `.external-link.button.is-normal.is-rounded.is-dark`, #363636 fill, white Noto Sans 16px, pill radius, icon left (Paper, arXiv, Code).
- **Before/after slider**: `.image-comparison` square box, max 900px; the clean image clipped with `clip-path: inset(0 0 0 50%)`; `.slider-handle` 4px white bar with a 20px white circle at mid-height, col-resize cursor, no transition.
- **Corner label**: white bold 16px on rgba(0,0,0,.5), padding 5px 10px, 5px radius, 10px from top-left (noisy) or top-right (clean).
- **Figure container**: flex column, max 900px, image 100% width.
- **BibTeX**: Bulma section with h2 title and pre on #f5f5f5, square corners.
- **Footer**: #fafafa band with Creative Commons notice and icon links in black at 25px.

## Page Modules

- **Title/author block**: h1, "CVPR 2026 Findings" subtitle, four authors with superscripts, affiliations, contact emails, equal-contribution note.
- **Link buttons**: Paper, arXiv, Code.
- **Teaser figure**: three-panel figure (noise translation network, Gaussian denoising network) directly under buttons.
- **TL;DR**: one-line summary in h2.
- **Abstract**: standard Nerfies abstract column.
- **Method figure**: "Overall Framework" diagram.
- **Image-comparison sliders**: NIND samples, ~4K samples without ground truth.
- **Results**: "Comparisons with other denoising methods" and an out-of-distribution PSNR figure (image, not an HTML table).
- **Carousel**: bulma-carousel is loaded and styled.
- **BibTeX**.
- **Absent**: video, 3D viewer, HF demo.

## Do's and Don'ts

- Do keep the chrome greyscale; let photographs supply colour.
- Do label both halves of every comparison inside the image with the dark veil chip.
- Do cap comparisons at 900px so they stay legible without horizontal scroll.
- Don't animate the slider handle; it tracks the pointer with 0s transitions.
- Don't introduce Bulma's turquoise primary.

## Surfaces

Plain white page, #f5f5f5 for code and panels, #fafafa footer. No cards with shadows.

## Imagery

Square, high-resolution photo crops (statues, textures) shown at up to 900px. Labels sit on the image rather than in captions.

## Layout

Single centred column. Hero, teaser, abstract, framework, two slider groups, comparison figures, BibTeX, footer. Rendered height about 5,400px.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, links #209cee, code #f5f5f5, footer #fafafa, slider #ffffff, label veil rgba(0,0,0,.5).

1. "Build a before/after slider: square box max 900px, two stacked images, top one clipped with clip-path inset(0 0 0 50%), a 4px white vertical handle with a 20px white circle at its centre, labels 'Noisy' and 'Clean' in white bold 16px on rgba(0,0,0,.5) with 5px radius."
2. "Make a Nerfies header: Google Sans 48px/600 title in #363636, venue subtitle, authors in #209cee 20px, and three #363636 pill buttons with white Noto Sans labels and icons."
3. "Add a BibTeX section: h2 'BibTeX', then a pre on #f5f5f5 in monospace 14px, no radius."

## Similar Pages

- Nerfies and its many direct forks.
- PAR, ViCaS, VideoScene, Argus in this batch (same Bulma base).

## Quick Start

```css
:root {
  --text-strong: #363636;
  --text: #4a4a4a;
  --link-author: #209cee;
  --code-bg: #f5f5f5;
  --footer-bg: #fafafa;
  --frame-border: #bbbbbb;
  --label-veil: rgba(0, 0, 0, 0.5);
  --radius-pill: 290486px;
  --radius-card: 10px;
  --radius-label: 5px;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --compare-max: 900px;
}
```

## Provenance

- **URL**: https://hij1112.github.io/learning-to-translate-noise/
- **Paper**: Learning to Translate Noise for Robust Image Denoising (arXiv 2412.04727), Inju Ha et al.
- **Venue**: CVPR 2026 Findings.
- **Selection reason**: the arXiv comment states CVPR 2026 Findings acceptance and links this page.
- **Template credit**: no explicit credit line; the footer reuses Nerfies' Creative Commons wording and the CSS is Nerfies' index.css, so the base is Nerfies (inferred).
- **Measurement method**: static HTML/CSS via extract_style.py, inline style block and index.css read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. The extractor's image_compare_slider flag was false because the slider is hand-written CSS; it was identified from the style block.
