# Optimus-2 Style Reference

> A crafting table under overcast grey, three clips to a row.

**Theme:** light

Measurements come from the page HTML (inline section backgrounds and font sizes), its heavily edited static/css/index.css plus a local Myriad Pro @font-face file, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

Optimus-2 starts from the Nerfies scaffold (Bulma 0.9, charcoal pill buttons) but swaps the type: the title is Myriad Pro (self-hosted, with Open Sans fallback) and the body falls to Arial. A small pixel-art agent icon sits above the title, and "CVPR 2025" is set as a big 35px bold line under it. Content sections alternate white and a translucent cool grey (#efeff0 at about 50% alpha). The core of the page is three-up video grids of Minecraft tasks, each video in a padded box that scales to 1.05 on hover, with the task instruction as a caption.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal | #363636 | Bulma text-strong (measured) | Title, button fill |
| Graphite | #4a4a4a | Bulma text (measured) | Body, venue line, section titles |
| Overcast | #efeff081 | inline section background (measured rgba(239,239,240,.506)) | Alternating section bands |
| Paper White | #ffffff | inline section background | Alternating bands |
| Bulma Link Blue | #3273dc | Bulma default link (inferred) | Author name links |
| Emerald Author | hsl(121,100%,36%) | .publication-authors a in index.css | Declared author colour; author anchors on this page sit outside that selector |
| Conference Grey | hsl(0,0%,16%) | .conference-authors a | Declared, not observed |
| Panel Grey | #f5f5f5 | Bulma pre, .interpolation-panel | BibTeX |
| Hover Grey | #f0f0f0 | .box:hover | Video box hover |

## Tokens · Typography

- **Title and teaser**: "Myriad-Pro" via local @font-face (fonts/MyriadPro-Regular.woff etc.), fallback "Open Sans", sans-serif.
- **Body**: Arial, sans-serif (index.css sets body to Myriad Pro and then overrides to Arial in the same rule).
- **Imported but secondary**: Source Code Pro, Open Sans (CSS @import). Google Sans/Noto Sans/Castoro also linked from the original template.
- **Mono**: browser monospace in BibTeX.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #363636, Myriad Pro |
| Venue line (h2 "CVPR 2025") | 35px | 700 | #4a4a4a |
| Section title (h2) | 35px measured | 700 | #4a4a4a |
| Author block | 22px declared | 400 | names in link blue |
| Affiliation line | 10px inline on .publication-authors wrapper | 400 | |
| Task caption | 30px or 125% / 110% inline | 400 | centred |
| Body | 16px Arial | 400 | #4a4a4a |
| BibTeX | 14px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Video wrappers, carousel items | 10px |
| Video boxes | 0 |

- **Shadows**: none custom (a 3D shadow on videos is commented out).
- **Spacing**: `section` padding 20px with border-box; video grid gap 10px and padding 20px; box padding 20px; video height fixed at 150px, object-fit cover.
- **Layout**: body is a flex column centred; containers is-max-desktop for text and is-max-widescreen for video rows; `.video-container` grid of three equal columns.

## Components

- **Link button**: #363636 pill, white Arial 16px, icon left; arXiv, PDF, Code.
- **Header icon**: small pixel-art agent image above the title.
- **Video box**: `.box` flex column, 20px padding, transition transform .3s; hover scale(1.05) and #f0f0f0 background; video 100% wide, 150px tall, object-fit cover; caption centred below with 20px padding.
- **Three-up grid**: `.video-container` repeat(3, 1fr), gap 10px.
- **Overcast band**: `<section style="background-color:#efeff081">`.
- **BibTeX**: pre on #f5f5f5.

## Page Modules

- **Title/author block**: icon, h1, "CVPR 2025" line, six authors, HIT Shenzhen and Peng Cheng Laboratory, corresponding-author mark.
- **Link buttons**: arXiv, PDF, Code.
- **Abstract**: overcast band.
- **Atomic Task videos**: three clips (mine dirt, chop trees, mine stone).
- **Long-horizon Task videos**: three clips (iron sword, golden pickaxe, diamond hoe).
- **Open-Ended Instruction videos**: three clips with natural-language prompts as captions.
- **Method figure**: "Overview framework of our Optimus-2".
- **Results**: figures (no HTML tables).
- **BibTeX**.
- **Absent**: footer credit, slider, 3D, demo.

## Do's and Don'ts

- Do show agent behaviour as uniform three-up video grids with the instruction as caption.
- Do alternate white and translucent grey section bands.
- Do keep video tiles a fixed height with object-fit cover so rows align.
- Don't declare a font stack and override it in the same rule (body ends up Arial while Myriad Pro is loaded).
- Don't leave author colour rules that the markup never hits.

## Surfaces

White and #efeff081 bands, flat boxes, #f5f5f5 code.

## Imagery

Minecraft gameplay clips (first-person), a method diagram, an agent pixel icon.

## Layout

Centred column for text, widescreen container for video grids. Rendered height about 5,300px.

## Agent Prompt Guide

Quick colors: title #363636, text #4a4a4a, band #efeff081, hover #f0f0f0, code #f5f5f5, author links #3273dc (inferred).

1. "Build a three-column video grid: grid-template-columns repeat(3,1fr), gap 10px, padding 20px; each cell a box with 20px padding, a 150px-tall object-fit cover video and a centred caption; on hover scale(1.05) and background #f0f0f0 over .3s."
2. "Alternate sections between #ffffff and #efeff081 backgrounds, each with a centred 35px bold h2 in #4a4a4a."
3. "Header: small pixel icon, Myriad Pro (fallback Open Sans) 48px/600 title in #363636, then 'CVPR 2025' at 35px bold, then #363636 pill buttons arXiv, PDF, Code."

## Similar Pages

- Optimus-1 and Optimus-3 project pages from the same group (inferred, not measured).
- Embodied-agent pages built on Nerfies with video grids.

## Quick Start

```css
:root {
  --text-strong: #363636;
  --text: #4a4a4a;
  --band: #efeff081;
  --box-hover: #f0f0f0;
  --code-bg: #f5f5f5;
  --link: #3273dc;
  --radius-pill: 290486px;
  --grid-gap: 10px;
  --video-h: 150px;
  --font-display: 'Myriad-Pro', 'Open Sans', sans-serif;
  --font-body: Arial, sans-serif;
}
```

## Provenance

- **URL**: https://cybertronagent.github.io/Optimus-2.github.io/
- **Paper**: Optimus-2: Multimodal Minecraft Agent with Goal-Observation-Action Conditioned Policy (arXiv 2502.19902), Zaijing Li et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: no footer credit; the index.css is a modified Nerfies stylesheet (Nerfies class names such as .dnerf remain), so the base is Nerfies (inferred).
- **Measurement method**: extract_style.py on static HTML/CSS, index.css and the Myriad Pro font file read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. The author link colour was not captured by the computed-style probe; #3273dc is inferred from Bulma's default and the screenshot.
