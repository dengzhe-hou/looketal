# Track4Gen Style Reference

> A charcoal title card pinned above a corkboard of video tiles.

**Theme:** light

Measurements come from the single-file HTML (one `<style>` block plus inline styles, no external CSS) and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

Track4Gen is written from scratch with no framework. The page sits on a pale grey (#f7f7f7) ground with 2em of body padding. The header is a rounded charcoal (#333333) slab with white bold sans title, white Google Sans author names, the venue line and a ghost "Arxiv" button: translucent grey fill and a 2px white outline. Below, each section is a white rounded card (1em radius, soft 1em blur shadow) holding rows of rounded video tiles. Captions are colour-coded semantically: teal-green (#097969) for "consistency", red (#cc0000) for "inconsistency". Results continue on page2 to page4, reached by small black chip links.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal Slab | #333333 | .hero background, body color | Header card, body text |
| Pale Ground | #f7f7f7 | body background | Page canvas |
| Card White | #ffffff | .teaser background | Section cards, hero text |
| Consistency Teal | #097969 | inline color | "Pixel/Feature-space Consistency" captions |
| Inconsistency Red | #cc0000 | inline color | "Pixel/Feature-space Inconsistency" captions |
| Pager Black | #000000 | inline background | Page 2 to 4 chip links |
| Ghost Fill | rgba(154,156,156,0.2) | inline background | Arxiv button fill |
| Muted Link | #777777 | a, a:link | Default links |
| Link Hover | #333333 | a:hover | Link hover |

## Tokens · Typography

- **Main**: generic `sans-serif` (renders as the system sans; Arial-like on Windows).
- **Authors**: 'Google Sans', sans-serif, declared but not loaded from Google Fonts (falls back unless installed).
- **No mono, no webfont imports.**

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (.hero h1) | 40px (2.5em) | 700 | #ffffff |
| Venue line | larger / about 1.2em | 400 | #ffffff |
| Authors | 20px | 400 | #ffffff |
| Section title (.teaser-title) | 32px (2em) | 700 | #333333 |
| Section description | 19.2px (1.2em) | 400 | #333333, max-width 1150px |
| Video caption | larger, 1.2em bold | 700 | #097969 or #cc0000 |
| Arxiv button | 18px | 400 | #ffffff |
| Body | 16px | 400 | #333333 |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Hero slab, section cards | 1em (16px) |
| Video tiles, iframes | 0.5em (8px) |
| Arxiv ghost button | 5px |
| Pager chips | 0.3em |

- **Shadows**: tiles and iframes `0 0 1em 0 rgba(0,0,0,0.15)`; cards `0 0 1em 0 rgba(0,0,0,0.1)`.
- **Spacing**: body padding 2em; hero padding 2.5em; card padding 2em with 3em bottom margin; visual rows flex-wrap with 2em gap.
- **Layout**: full-width cards inside body padding; description text capped at 1150px; each video tile max-width 30em (480px).

## Components

- **Hero slab**: centred, #333333, 1em radius, 2.5em padding, 2em bottom margin; white title, authors, affiliations (Adobe Research, KAIST, UCL), venue.
- **Ghost button**: Arxiv link with rgba(154,156,156,.2) fill, 2px solid white border, padding 10px 20px, 18px text, 5px radius.
- **Section card**: `.teaser`, white, centred text, 1em radius, soft shadow.
- **Video tile**: `<video>` 100% width up to 30em, 0.5em radius, shadow 0.15; bold caption under it.
- **Pager**: "Page 1" in bold text, then black chips (padding .4em .8em, .3em radius, white text) linking page2.html to page4.html, separated by bullets.
- **Instruction row**: flex row of 36px icons with 1.5em labels (template slot for usage hints).

## Page Modules

- **Title/author block**: in the charcoal hero slab, with "CVPR 2025".
- **Link buttons**: Arxiv only. No Code or BibTeX on this page.
- **Pagination**: results spread over four HTML pages.
- **Teaser videos**: Motivation card with consistency/inconsistency comparisons.
- **Results videos**: "Real-world Video Tracking", "Generated Video Tracking" cards; 12 videos on page 1.
- **Method figure**: "Overview" card with a fixed 1073x330 diagram (no radius, no shadow).
- **Math**: MathJax present.
- **Absent**: BibTeX, abstract block, code link, carousel, slider, 3D, demo.

## Do's and Don'ts

- Do keep the semantic caption pair: teal for good tracking, red for failure.
- Do wrap every section in a white 1em-radius card on the #f7f7f7 ground.
- Do give video tiles the same 0.5em radius and soft shadow.
- Don't introduce a framework; the page is one HTML file with one style block.
- Don't rely on Google Sans without loading it.
- Don't size the method diagram in fixed pixels if the page must work on phones (the 1073px image overflows small screens).

## Surfaces

Pale grey canvas, one charcoal slab, white cards. Depth comes from blur-only shadows with no offset.

## Imagery

Short generated or real video clips with point-track overlays, arranged in wrap rows of up to three, each about 480px wide.

## Layout

Stacked full-width cards. Rendered height about 7,450px for page 1 of 4.

## Agent Prompt Guide

Quick colors: ground #f7f7f7, slab #333333, card #ffffff, good #097969, bad #cc0000, pager #000000, link #777777.

1. "Make a header slab: #333333 background, 1em radius, 2.5em padding, centred white bold 2.5em sans title, white 20px authors, and a ghost button with rgba(154,156,156,.2) fill, 2px white border, 5px radius, padding 10px 20px."
2. "Make a section card: white, 1em radius, 2em padding, box-shadow 0 0 1em rgba(0,0,0,.1), centred 2em bold title in #333333, then a flex-wrap row of videos (max 30em, 0.5em radius, shadow 0 0 1em rgba(0,0,0,.15)) with bold captions in #097969 or #cc0000."
3. "Add a pager: bold 'Page 1', then black chip links (padding .4em .8em, .3em radius, white text) separated by bullet characters."

## Similar Pages

- Single-file, framework-free video-generation pages with paginated results.
- VoxelSplat in this batch (also hand-written CSS, no framework).

## Quick Start

```css
:root {
  --ground: #f7f7f7;
  --slab: #333333;
  --card: #ffffff;
  --good: #097969;
  --bad: #cc0000;
  --pager: #000000;
  --link: #777777;
  --ghost-fill: rgba(154, 156, 156, 0.2);
  --radius-card: 1em;
  --radius-tile: 0.5em;
  --shadow-tile: 0 0 1em 0 rgba(0, 0, 0, 0.15);
  --shadow-card: 0 0 1em 0 rgba(0, 0, 0, 0.1);
  --font-sans: sans-serif;
}
```

## Provenance

- **URL**: https://hyeonho99.github.io/track4gen/
- **Paper**: Track4Gen: Teaching Video Diffusion Models to Track Points Improves Video Generation (arXiv 2412.06016), Hyeonho Jeong et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: none stated; custom single-file page.
- **Measurement method**: extract_style.py on the static HTML (zero external CSS files), the style block and inline styles read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. Only page 1 of the four result pages was measured.
