# LTGS Style Reference

> A navy-ruled lab ledger in rounded Nunito.

**Theme:** light

Measurements come from the page HTML, its own css/styles.css, the Bulma 1.0.1 CDN build it loads, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

LTGS is a hand-assembled Bulma 1.0 page (not a Nerfies fork) with a softer, rounder voice. Nunito sets the title, authors and text; buttons are deep navy (#143163) full pills with off-white labels; author names and the lab-logo row are a muted indigo (#50549b) that fades to dusty blue (#9bb4c2) on hover. A centred lab logo (3D Lab Vision) sits between affiliations and buttons. The html element forces `data-theme="light"`, so Bulma 1.0's built-in dark scheme never activates.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Harbor Navy | #143163 | .link-button | Pill button fill and border |
| Sail White | #f5f5f5 | .link-button color | Button label, BibTeX box fill |
| Dusk Indigo | #50549b | .author-blocks, .logo-list | Author names, affiliation/logo row |
| Haze Blue | #9bb4c2 | .author-blocks:hover | Author hover |
| Deep Ink Navy | #14274e | .publication-keywords | Keyword line |
| Title Slate | #2e333d | Bulma 1.0 strong text (measured rgb 46,51,61) | h1 |
| Body Slate | #404654 | Bulma 1.0 text (measured rgb 64,70,84) | Body, h2 |
| Footer Mist | #f9fafb | Bulma 1.0 footer (measured rgb 249,250,251) | Footer band |
| Paper White | #ffffff | scheme main (inferred) | Page |

Bulma 1.0 expresses its palette through HSL custom properties (--bulma-*-h/s/l); none of its brand hues appear on the rendered page.

## Tokens · Typography

- **Display and text**: Nunito (Google Fonts, variable 200 to 1000), applied to title, authors, institutes, .content, TL;DR and buttons.
- **Base body stack**: Bulma 1.0 default Inter, "SF Pro", "Segoe UI", Roboto (visible in footer and unstyled text).
- **Mono**: Roboto Mono for the BibTeX box.
- **Also linked, little or no visible use**: Encode Sans, Architects Daughter, Quicksand.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #2e333d |
| Venue line "CVPR 2026 (Findings)" | about 20px (inferred) | 400 | #404654 |
| Authors | 20px | 500 | #50549b |
| Institute | 16px (inferred) | 400 | #50549b |
| Affiliation number | 12px | 400 | |
| TL;DR | 20px | 400 | #404654, centred |
| Section h2 | 20px (measured first h2) | 400 | #404654 |
| Button | 16px | 500 | #f5f5f5 |
| BibTeX | 16px Roboto Mono | 400 | #404654 |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 9999px (Bulma 1.0 radius-rounded, measured) |
| BibTeX box / pre | 12px (measured) |
| Video frame | 10px |
| Images | 0 |

- **Shadows**: Bulma 1.0 defaults only; nothing custom.
- **Spacing**: `.section` padding overridden to 1.5rem 0.75rem (tighter than Bulma's 3rem); link block margin-top 1rem; button side margins 0.1rem, bottom 0.5rem; lab logo max-height 60px.
- **Layout**: Bulma container (1152/1344px breakpoints); results videos 80% wide, centred; GIF cells 20% wide.

## Components

- **Link button**: `.button.link-button.is-rounded`, #143163 fill and border, #f5f5f5 Nunito 500 label, full pill, hover identical (no colour change). Five buttons: Paper, arXiv, Video, Code, Dataset.
- **Author row**: Nunito 500 in #50549b, hover #9bb4c2, affiliation numbers 12px with 40px right margin.
- **Logo row**: `.logo-list`, flex nowrap centred, indigo text, 30px top margin, logo max-height 60px.
- **TL;DR**: centred Nunito 20px paragraph introducing LTGS.
- **Video**: 16:9 `.publication-video` wrapper, 10px radius, YouTube iframe; plus autoplay looping `<video>` at 80% width.
- **BibTeX**: `.bibtex-box` #f5f5f5 with Roboto Mono.
- **Footer**: #f9fafb band with CC BY-SA notice.

## Page Modules

- **Title/author block**: three-line h1, venue line, four authors, Seoul National University, lab logo.
- **Link buttons**: Paper, arXiv, Video, Code, Dataset.
- **Teaser figure**: timeline strip of scene updates (t0 to tN) under the buttons.
- **TL;DR** sentence.
- **Abstract**.
- **Video**: section titled "Video (todo)" with a YouTube embed (heading placeholder left in).
- **Method figure**.
- **Results**: "Long-term Scene Reconstruction" autoplay videos and result figures.
- **Math**: MathJax loaded.
- **BibTeX**.
- **Absent**: carousel, comparison slider, interactive 3D viewer (the extractor's 3D flag fired on the word "Splatting"), HF demo, results table.

## Do's and Don'ts

- Do set every visible text element in Nunito; the rounded terminals are the identity.
- Do keep buttons navy full pills with off-white text; no hover recolour.
- Do use indigo #50549b for people and institutions, not for links in body text.
- Don't rely on Bulma 1.0's automatic dark mode; this page pins light.
- Don't load decorative fonts you do not apply (three extra families are linked).
- Don't ship "(todo)" headings.

## Surfaces

White page, #f5f5f5 code box, #f9fafb footer. Flat, no cards or shadows.

## Imagery

Timeline strips of indoor scenes, autoplay videos of reconstructions, a method diagram. Media centred at 80% width.

## Layout

Single centred column, compact section padding. Rendered height about 4,850px.

## Agent Prompt Guide

Quick colors: button #143163 on #f5f5f5 text, authors #50549b (hover #9bb4c2), keywords #14274e, title #2e333d, body #404654, footer #f9fafb.

1. "Build a link-button row: five pill buttons (radius 9999px) with #143163 background and border, #f5f5f5 Nunito 500 16px labels, icon left, 0.1rem side margins."
2. "Set a header: Nunito 600 48px title in #2e333d, venue line, authors in Nunito 500 20px #50549b with #9bb4c2 hover, then a centred 60px lab logo."
3. "Add a BibTeX box: #f5f5f5 background, Roboto Mono 16px, 12px radius, full container width."

## Similar Pages

- Other hand-rolled Bulma 1.0 project pages that pin `data-theme="light"`.
- Track4Gen and VoxelSplat in this batch, also built without the Nerfies index.css.

## Quick Start

```css
:root {
  --btn-bg: #143163;
  --btn-text: #f5f5f5;
  --author: #50549b;
  --author-hover: #9bb4c2;
  --keywords: #14274e;
  --title: #2e333d;
  --text: #404654;
  --code-bg: #f5f5f5;
  --footer-bg: #f9fafb;
  --radius-pill: 9999px;
  --radius-code: 12px;
  --font-display: 'Nunito', sans-serif;
  --font-mono: 'Roboto Mono', monospace;
}
```

## Provenance

- **URL**: https://mkjjang3598.github.io/LTGS/
- **Paper**: LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates (arXiv 2510.09881), Minkwan Kim et al.
- **Venue**: CVPR 2026 Findings.
- **Selection reason**: the arXiv comment states CVPR 2026 Findings acceptance and links this page.
- **Template credit**: none stated; custom Bulma 1.0.1 build with its own styles.css.
- **Measurement method**: extract_style.py on static HTML/CSS, styles.css read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. The extractor's dark_mode_toggle flag reflects Bulma 1.0's built-in dark scheme in the CDN CSS; the page has no toggle and forces light.
