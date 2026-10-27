# Argus Style Reference

> A reading-room report with its headings set left and bold.

**Theme:** light

Measurements come from the page HTML (a short inline `<style>` block and inline image sizing), its static/css/index.css, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

Argus is a Nerfies-derived page (Bulma 0.9 loaded from a shared ../shared/bulma folder, Google Sans title, Noto Sans body) that reads more like a paper than a landing page. Section headings are forced to bold 150% and set left, so "Overview", "Findings" and "Main Results" look like report headings rather than centred banners. A small logo image sits inline before the title. Only two charcoal pill buttons show (arXiv, Video). Figures are sized by hand with inline widths (100%, 97%, 60%, 50%) to keep a tight column. The stylesheet carries a cyan-to-magenta gradient-text class that the page never uses.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal | #363636 | Bulma text-strong (measured) | Title, section headings, button fill |
| Graphite | #4a4a4a | Bulma text (measured) | Body |
| Nerfies Sky | #209cee | hsl(204,86%,53%) (measured rgb 32,156,238) | Author links |
| Table Rule | #dddddd | inline style td, th border | Table cell borders |
| Panel Grey | #f5f5f5 | Bulma pre | BibTeX |
| Footer White | #ffffff | footer (measured rgb 255,255,255) | Footer band |
| Select Fade | #f9f9f9 to #ffffff | select background-image | Dropdown styling (no select on page) |
| Neon Cyan to Magenta | #00dbde to #fc00ff | .fontGrad-bg | Declared gradient text, unused |
| Award Pink | #ff3860 | .publication-awards | Declared, unused |

## Tokens · Typography

- **Title and authors**: Google Sans.
- **Body and section headings**: Noto Sans (measured on h2). Castoro loaded, unused.
- **Mono**: browser monospace.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 48px | 600 | #363636 |
| Section heading (h2) | 24px (150% !important) | 600 to bold | #363636, left-aligned |
| Authors | 20px | 400 | #209cee |
| Supervision/email note | 16px (inferred) | 400 | #4a4a4a |
| Venue line "CVPR 2025" | 16px (inferred) | 400 | #4a4a4a |
| Body | 16px | 400 | #4a4a4a, justified |
| Tables | 92% (!important) | 400 | |
| BibTeX | 14px | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Carousel items, video wrappers | 10px |
| Select | 0.25em |
| Figures | 0 |

- **Shadows**: Bulma defaults only.
- **Tables**: width 100%, border-collapse, td/th 8px padding with 1px #ddd borders, 10px top margin.
- **Layout**: Bulma container; figures capped at 1000px in one case, otherwise inline percentage widths; a flex row with 20px gap for side-by-side figures.

## Components

- **Link button**: #363636 pill, white Noto Sans 16px, icon left. Visible: arXiv, Video. A Paper button exists in the HTML but is commented out.
- **Title logo**: inline image 20mm square with -5mm bottom margin, placed before the title text.
- **Report heading**: h2 bold, 150% size, left-aligned, charcoal.
- **Figure**: block image, centred with auto margins, inline width (100%, 97%, 60%, 50%).
- **Paired figures**: flex row, centre aligned, 20px gap.
- **BibTeX**: pre on #f5f5f5.
- **Footer**: white, Nerfies CC BY-SA wording.

## Page Modules

- **Title/author block**: logo plus h1, eight authors, UIUC and NVIDIA, equal-supervision note with email, venue line.
- **Link buttons**: arXiv, Video (Video links back to the page itself).
- **Overview**: abstract-length overview text with a teaser figure.
- **Method figure**: "Visual-CoT Designs".
- **Findings**: figures.
- **Main Results**: result figures (the counted tables are zero in static HTML; table CSS is present).
- **Carousel**: bulma-carousel loaded.
- **BibTeX**.
- **Absent**: video player, slider, 3D, demo, footer template credit.

## Do's and Don'ts

- Do left-align bold section headings for a report-like reading flow.
- Do size figures deliberately rather than leaving every image at 100%.
- Don't leave buttons that point to unrelated targets (the commented Paper link points to a different arXiv PDF; Video points to the page itself).
- Don't keep unused decorative classes such as the neon gradient text.

## Surfaces

White page and white footer, #f5f5f5 code. No bands.

## Imagery

Grounded chain-of-thought diagrams with bounding boxes, method schematics, result plots.

## Layout

Centred Bulma column with left-aligned headings. Rendered height about 6,260px.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, authors #209cee, table rule #dddddd, code #f5f5f5, footer #ffffff.

1. "Make report-style section headings: h2 in Noto Sans, bold, font-size 150%, color #363636, left-aligned, followed by justified 16px #4a4a4a text."
2. "Build a header: 20mm logo inline before a Google Sans 48px/600 #363636 title, authors in #209cee 20px, then arXiv and Video pill buttons in #363636."
3. "Add a results table: width 100%, border-collapse, cells with 8px padding and 1px #ddd borders, font-size 92%."

## Similar Pages

- Nerfies forks that share one Bulma copy across several project folders.
- PAR, ViCaS, Translate Noise in this batch.

## Quick Start

```css
:root {
  --text-strong: #363636;
  --text: #4a4a4a;
  --link-author: #209cee;
  --table-rule: #dddddd;
  --code-bg: #f5f5f5;
  --footer-bg: #ffffff;
  --radius-pill: 290486px;
  --h2-size: 150%;
  --table-size: 92%;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL**: https://yunzeman.github.io/argus/
- **Paper**: Argus: Vision-Centric Reasoning with Grounded Chain-of-Thought (arXiv 2505.23766), Yunze Man et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: no explicit credit line; footer reuses Nerfies' license wording and index.css is the Nerfies stylesheet with additions, so the base is Nerfies (inferred).
- **Measurement method**: extract_style.py on static HTML/CSS, inline style block and index.css read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27.
