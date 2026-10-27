# VideoScene Style Reference

> A single red flare on a grey screening-room wall.

**Theme:** light

Measurements come from the page HTML, its static/css/index.css, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

VideoScene uses the original Academic Project Page Template (Nerfies lineage, Bulma 0.9, Google Sans and Noto Sans). It is a video-first page: eight `<video>` elements, starting with a large black-framed result player directly under the header. The only colour outside the author links is the venue line, where "Highlight" is set in plain CSS red with a fire emoji. The authors' index.css carries an unused before/after slider kit (bal-* classes) from another project; it does not render on this page.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal | #363636 | Bulma text-strong (measured) | Title, button fill |
| Graphite | #4a4a4a | Bulma text (measured) | Body, subtitles |
| Nerfies Sky | #209cee | hsl(204,86%,53%) (measured rgb 32,156,238) | Author links |
| Flare Red | red (#ff0000) | inline `color: red` | "Highlight" award tag |
| Band Grey | #f5f5f5 | hero.is-light (measured) | Abstract and section bands, BibTeX |
| Band Text | rgba(0,0,0,0.7) | Bulma hero.is-light | Band titles |
| Footer Haze | #fafafa | Bulma footer (measured) | Footer |
| Frame Grey | #bbbbbb | .results-carousel .item border | Carousel frames |
| Slider Label Black | #121212 | .bal-beforePosition (unused) | Declared only |

## Tokens · Typography

- **Headings and authors**: Google Sans.
- **Body**: Noto Sans. Castoro loaded, unused.
- **Mono**: browser monospace.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #363636 |
| TL;DR subtitle (h2) | 20px | 400 | #4a4a4a |
| Section title (h2.title.is-3) | 32px (inferred from class) | 600 | rgba(0,0,0,.7) in bands |
| Authors | 20px | 400 | #209cee |
| Venue line | 16px (inferred) | 400 | #4a4a4a, "Highlight" in red |
| Body | 16px | 400 | #4a4a4a |
| BibTeX | 14px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Carousel items, video wrappers, interpolation panel | 10px |
| Images in panels | 5px |

- **Shadows**: Bulma defaults; the unused slider handle declares `0 0 10px rgb(12,12,12)`.
- **Layout**: Bulma container; hero is-light is-small bands; result player spans the container width.

## Components

- **Link button**: #363636 pill, white Noto Sans 16px, icon left; Paper, Supplementary, Code, arXiv.
- **Venue tag**: "CVPR 2025" followed by red "Highlight" and a fire emoji.
- **Result player**: autoplay video with black letterbox and an on-video timer, full container width.
- **Grey band**: hero is-light is-small sections for abstract and method.
- **Poster**: embedded poster section (template module).
- **BibTeX**: pre on #f5f5f5.
- **Footer**: #fafafa with template credit and CC license.

## Page Modules

- **Title/author block**: two-line title, four authors, Tsinghua University, venue with Highlight tag, equal-contribution and corresponding marks.
- **Link buttons**: Paper, Supplementary, Code, arXiv.
- **Teaser video**: large result player.
- **TL;DR** subtitle.
- **Abstract** band.
- **Method figure**: "Method Overview".
- **Test-Time Scaling**: results figure.
- **Video Results**: grid of generated 3D-scene fly-through videos.
- **Poster**.
- **BibTeX**.
- **Absent**: interactive 3D viewer (the extractor's 3D flag fired on the word "Splat"), slider (CSS only), demo, table.

## Do's and Don'ts

- Do let video carry the page; keep chrome greyscale.
- Do mark an award (Highlight, Oral) in one saturated colour next to the venue.
- Don't ship unused component CSS from another project if it confuses reuse.
- Don't add borders or shadows to the hero player; the black letterbox is the frame.

## Surfaces

White page alternating with #f5f5f5 bands; #fafafa footer.

## Imagery

Paired input views and generated 3D-scene videos, a method diagram, the conference poster.

## Layout

Centred single column, video first. Rendered height about 3,430px, short for a video page.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, authors #209cee, award red #ff0000, band #f5f5f5, footer #fafafa.

1. "Under the author list, add a venue line 'CVPR 2025' followed by 'Highlight' in color red with a fire emoji, centred, 16px Noto Sans."
2. "Place an autoplay muted looping video at full container width directly under the link buttons, no radius, black background."
3. "Make four #363636 pill buttons: Paper, Supplementary, Code, arXiv, white Noto Sans labels with icons."

## Similar Pages

- CFG-Ctrl (same author, newer refreshed template).
- ViCaS, Translate Noise, PAR, Argus in this batch.

## Quick Start

```css
:root {
  --text-strong: #363636;
  --text: #4a4a4a;
  --link-author: #209cee;
  --award: #ff0000;
  --band: #f5f5f5;
  --footer-bg: #fafafa;
  --frame: #bbbbbb;
  --radius-pill: 290486px;
  --radius-media: 10px;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL**: https://hanyang-21.github.io/VideoScene/
- **Paper**: VideoScene: Distilling Video Diffusion Model to Generate 3D Scenes in One Step (arXiv 2504.01956), Hanyang Wang et al.
- **Venue**: CVPR 2025 (page marks it Highlight).
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method**: extract_style.py on static HTML/CSS, index.css read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. The bal-* slider classes were checked in the rendered DOM and are not used.
