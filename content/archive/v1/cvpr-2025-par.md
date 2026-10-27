# PAR Style Reference

> Contact sheets laid edge to edge on a white light box.

**Theme:** light

Measurements come from the page HTML (with a short inline `<style>` block), its static/css/index.css, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

PAR keeps the Nerfies skeleton (Bulma 0.9, Google Sans titles, Noto Sans body, sky-blue author links, charcoal pill buttons, Nerfies "More Research" navbar dropdown) and stretches it for image generation results. The authors added a wide video container (up to 1600px, 90% of the viewport) and thin #dbdbdb rules between major sections, so the page reads as a sequence of wide galleries separated by hairlines. The teaser is an animated latency comparison (sequential vs parallel decoding). Gallery images carry a 1px #bbb frame with 10px corners.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal | #363636 | Bulma text-strong (measured rgb 54,54,54) | Title, button fill |
| Graphite | #4a4a4a | Bulma text (measured rgb 74,74,74) | Body, subtitles |
| Nerfies Sky | #209cee | hsl(204,86%,53%) (measured rgb 32,156,238) | Author links |
| Divider Grey | #dbdbdb | .section-divider | Hairline between sections |
| Frame Grey | #bbbbbb | .results-carousel img border | Gallery image frame |
| Panel Grey | #f5f5f5 | Bulma light / pre | BibTeX, interpolation panel |
| Footer Haze | #fafafa | Bulma footer (measured) | Footer |
| Venue Grey | #555555 | .publication-venue | Venue style |
| Award Pink | #ff3860 | .publication-awards | Declared, unused |

## Tokens · Typography

- **Headings and authors**: Google Sans (Google Fonts).
- **Body**: Noto Sans. Castoro loaded but unused.
- **Mono**: browser monospace in BibTeX.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #363636 |
| TL;DR subtitle (h2) | 20px | 400 | #4a4a4a |
| Section title (h2.title.is-3, .section-title centred) | 32px (inferred from Bulma is-3) | 600 | #363636 |
| Authors | 20px | 400 | #209cee |
| Body | 16px | 400 | #4a4a4a |
| .smaller-text | 12.8px (0.8rem) | 400 | captions |
| .smallest-text | 8px (0.5rem) | 400 | dense labels |
| BibTeX | 14px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Gallery images, carousel content, video frames | 10px |
| Single images (.publication-img) | 5px |

- **Shadows**: Bulma focus/box defaults only.
- **Section divider**: border-top 1px #dbdbdb, margin 3rem top and bottom.
- **Layout**: Bulma container for text (1152/1344px); `.wider-video-container` max-width 1600px, width 90%; teaser video 80% wide with 10% side margins; wider columns padding 0.75rem.

## Components

- **Link button**: `.external-link.button.is-normal.is-rounded.is-dark`, #363636, white Noto Sans 16px, pill; arXiv (with arXiv logo icon) and Code.
- **More Research navbar**: centred Bulma navbar dropdown linking related projects (Nerfies default, kept).
- **Section divider**: `.section-divider` hairline.
- **Gallery image**: 100% width, 1px #bbb border, 10px radius.
- **Side-by-side**: `.side-by-side` 50% width columns for paired visuals.
- **Video card**: `.card-image video` scaled 150% with object-fit cover inside cards (gif-card pattern).
- **BibTeX**: pre on #f5f5f5, square corners.

## Page Modules

- **Title/author block**: h1, ten authors with project-lead and corresponding marks, HKU, ByteDance, PKU.
- **Link buttons**: arXiv, Code.
- **Teaser video**: "Latency Comparison" animation (sequential vs parallel generation).
- **TL;DR**: subtitle line under teaser.
- **Abstract**.
- **Key Insight** and **Approach**: method figures.
- **Visual Comparison**: wide video container.
- **Qualitative Results**: image galleries / carousel.
- **Quantitative Results**: result figures (images, not HTML tables).
- **More Visualizations**: additional galleries.
- **BibTeX**.
- **Absent**: slider, 3D, demo, dataset link.

## Do's and Don'ts

- Do widen media beyond the text column (up to 1600px) when the content is image grids.
- Do separate major blocks with one 1px #dbdbdb hairline and 3rem space.
- Do frame gallery images with 1px #bbb and 10px radius.
- Don't widen the text column with the media; abstract stays in the Bulma container.
- Don't add colour accents beyond the author-link blue.

## Surfaces

White throughout; #f5f5f5 for code; #fafafa footer. Structure from hairlines rather than bands.

## Imagery

Grids of generated ImageNet-style and text-to-image samples, an animated latency diagram, method schematics.

## Layout

Centred text column with selectively wider media rows. Rendered height about 8,350px.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, authors #209cee, rule #dbdbdb, frame #bbbbbb, code #f5f5f5, footer #fafafa.

1. "Create a wide gallery section: centred section title in Google Sans 32px/600 #363636, then a container max-width 1600px and width 90% holding images with 1px #bbb borders and 10px radius."
2. "Separate sections with a div that has border-top 1px solid #dbdbdb and 3rem margin above and below."
3. "Build a Nerfies header with Google Sans 48px/600 title, #209cee author links, and #363636 pill buttons for arXiv and Code."

## Similar Pages

- Nerfies and direct forks.
- Translate Noise, ViCaS, VideoScene, Argus in this batch.

## Quick Start

```css
:root {
  --text-strong: #363636;
  --text: #4a4a4a;
  --link-author: #209cee;
  --rule: #dbdbdb;
  --frame: #bbbbbb;
  --code-bg: #f5f5f5;
  --footer-bg: #fafafa;
  --radius-pill: 290486px;
  --radius-media: 10px;
  --wide-max: 1600px;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL**: https://yuqingwang1029.github.io/PAR-project/
- **Paper**: Parallelized Autoregressive Visual Generation (arXiv 2412.15119), Yuqing Wang et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: footer says the template is borrowed from Nerfies.
- **Measurement method**: extract_style.py on static HTML/CSS, inline style block and index.css read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. Section title size inferred from Bulma's is-3 class; it was not separately measured.
