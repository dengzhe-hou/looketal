# Camera Rig Rainbow — Style Reference

> A frosted-glass lab poster whose title sways like a handheld camera.

**Theme:** light

Values come from the page's four inline `<style>` blocks (no framework, no external CSS) and its HTML. Measurements are normalized to CSS units as written; roles are interpreted from usage. The rendered page was not viewed.

## Overview

I2VControl-Camera is a hand-written single-file page. A soft slate gradient (`#f8fafc` to `#f1f5f9`) sits behind a translucent white header card with `backdrop-filter: blur(8px)`. The title is the signature move: 3.2rem/800 text filled with an animated nine-stop rainbow gradient that both flows (`colorFlow`, 8s) and pans and tilts (`cameraPan`, 2s), a literal nod to camera motion. Below it, nine teal author chips (`rgb(148,211,202)`) sit in a 9-column grid with hover tooltips. Link buttons are blue-to-indigo gradient rectangles. Content is split into white rounded cards (`.paper-section`, 12px radius) with emoji-prefixed blue h2s, and the results are 51 GIFs laid out in fixed-percentage table cells. An "ICLR 2025" banner with party emoji floats on the card's top edge.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Tech Blue | `#2563eb` | `--primary` | Button gradient start, section h2 color |
| Indigo Pull | `#4f46e5` | `--secondary` | Button gradient end |
| Slate Ink | `#1e293b` | `--text` | Declared text token (body color not explicitly set) |
| Morning Slate | `#f8fafc` | `--background` | Page gradient start, BibTeX `pre` background |
| Cloud Slate | `#f1f5f9` | (literal) | Page gradient end |
| Frosted Card | `rgba(255,255,255,0.92)` | (literal) | Header card fill |
| Section Card | `rgba(255,255,255,0.9)` | (literal) | Content card fill |
| Chip Teal | `rgb(148,211,202)` | (literal) | Author chip background |
| Muted Graphite | `#4a5568` | (literal) | Subtitle, author names, list text, affiliations |
| Footnote Blue | `#3b82f6` | (literal) | Affiliation markers, ToC numbers, ToC left rule |
| Caption Slate | `#64748b` | (literal) | Affiliation text |
| ToC Ink | `#1f2937` | (literal) | ToC link text |
| Tooltip Night | `rgba(0,0,0,0.9)` | (literal) | Author hover tooltip |
| Title Rainbow | `#FF0000 → #FF7300 → #FFFB00 → #48FF00 → #00FFD5 → #002BFF → #7A00FF → #FF00C8 → #FF0000` | (gradient) | Animated title fill |

## Tokens — Typography

- **Loaded:** Inter 400/500/600 from Google Fonts. No rule in the page assigns `font-family: Inter`, so body text most likely renders in the browser default serif (inferred).
- **Mono:** `'Courier New', monospace` for BibTeX only.
- Weights in use: 800 (title), 600 (author names, ToC numbers).

| Role | Size | Weight | Line height |
|---|---|---|---|
| Animated title | 3.2rem (2.4rem under 768px) | 800 | default |
| Subtitle | 2.2rem (1.9rem mobile), `#4a5568`, text-shadow `0 2px 4px rgba(0,0,0,0.1)` | default | 1.4 |
| Venue banner | 2.3rem, `<strong>` | bold | default |
| Section h2 | 1.5em, `#2563eb` | default | default |
| ToC number | 1.1rem, `#3b82f6` | 600 | default |
| ToC title | 1rem | 400 | default |
| Affiliations | 0.9em | 400 | default |
| Footnote marker | 0.75em | 400 | 1 |
| BibTeX | 0.9em (0.8em mobile) | 400 | 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Header card | 16px |
| Section cards | 12px |
| Link buttons, BibTeX pre, teaser and pipeline images, ToC items | 8px |
| Tooltip | 6px |
| Author chips, table GIFs, ToC hover | 4px |

**Shadows:** header card `0 4px 24px rgba(0,0,0,0.06)`; section cards and chips `0 2px 8px rgba(0,0,0,0.08)`; images `0 2px 8px rgba(0,0,0,0.1)`; button hover `0 4px 12px rgba(65,103,185,0.3)`; venue banner `0 2px 12px rgba(99,102,241,0.1)`.

**Layout widths:** header card 1200px; section column 1270px; GIF tables 800px; teaser `min(120vw, 960px)` with fixed 120/127px side padding.

## Components

- **Header card:** frosted white, 2rem padding, 1px `rgba(255,255,255,0.4)` border, 16px radius, blur 8px.
- **Animated title:** inline-block, gradient text with `background-size: 400% 400%`, two keyframe animations running together.
- **Venue banner:** absolutely positioned at `top: -12px`, centered, white background, "🎉🎉🎉 ICLR 2025 🎉🎉🎉".
- **Author chip:** 200px wide teal tile, 0.3rem padding, lifts 3px on hover, shows `data-bio` tooltip with a 6px arrow.
- **Link button (`.paper-link`):** `0.8rem 1.5rem` padding, 8px radius, 135deg gradient `#2563eb → #4f46e5`, white text. Buttons: Paper (arXiv), Youtube (href `#`, placeholder), Code.
- **Table of contents:** 4px `#3b82f6` left rule, 4-column grid (3, 2, 1 at 1280/1024/640px), numbered items.
- **Section card:** white 90%, 1.5rem padding, 1.5rem vertical margin.
- **BibTeX block:** `#f8fafc` pre, 1.2rem padding, 8px radius.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Rainbow animated title, subtitle, 9-column author chip grid, affiliations with blue superscripts |
| Venue badge | Yes | Floating banner "ICLR 2025" with emoji |
| Link buttons | Yes | Paper, Youtube (placeholder), Code; gradient rectangles |
| Teaser figure / video | Yes | Static teaser PNG (`teaser_1.png`), 8px radius |
| Abstract | Partial | "🌼 Overview" card instead of a formal abstract heading |
| Method figure | Yes | `pipeline-img` in "💡 Method and Analysis" |
| Results tables / videos | Yes | 6 HTML tables holding 51 GIFs at 20 to 34% cell widths |
| Image comparison slider | No | |
| Interactive 3D / HF demo | No | |
| BibTeX | Yes | "Citation" card with Courier New pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep the title animation only on the title; everything else is calm slate and white.
- Do use emoji as section glyphs (🌼, 🔥, 💡) consistently.
- Do keep the blue/indigo pair for buttons and headings only.
- Don't rely on the fixed `padding-left: 90px / 190px` author grids at narrow widths; they collapse to one column only under 768px.
- Don't forget to assign the loaded Inter font if reproducing; the original never applies it.

## Surfaces

Slate gradient page, frosted header card, then stacked translucent white cards with soft shadows. No dark bands.

## Imagery

Animated GIF results dominate (51 GIF references, 41 `<img>` tags in the static HTML). Two static figures: teaser and pipeline.

## Layout

Centered column up to 1270px; header 1200px; GIF grids capped at 800px. ToC grid adapts at 1280/1024/640px.

## Agent Prompt Guide

**Quick colors:** bg gradient `#f8fafc`→`#f1f5f9`, card `rgba(255,255,255,0.9)`, text `#4a5568`, primary `#2563eb`, secondary `#4f46e5`, marker `#3b82f6`, chip `rgb(148,211,202)`.

1. "Create a hero card: white at 92% opacity, 16px radius, `0 4px 24px rgba(0,0,0,0.06)` shadow, blur(8px) backdrop, with a 3.2rem/800 title filled by an animated rainbow gradient that pans left-right with slight rotation."
2. "Make link buttons with 0.8rem 1.5rem padding, 8px radius, a 135deg `#2563eb`→`#4f46e5` gradient and white text; on hover add `0 4px 12px rgba(65,103,185,0.3)`."
3. "Build a numbered table of contents: 4-column grid, 4px `#3b82f6` left border, numbers 1.1rem/600 blue, titles 1rem `#1f2937`."

## Similar Pages

Other hand-built ByteDance-style demo pages with emoji headers and GIF tables; within this collection it is closest to pages that skip Bulma entirely.

## Quick Start

```css
:root {
  --primary: #2563eb; --secondary: #4f46e5;
  --text: #1e293b; --muted: #4a5568; --marker: #3b82f6;
  --background: #f8fafc; --background-2: #f1f5f9;
  --chip: rgb(148,211,202);
  --radius-card: 16px; --radius-section: 12px; --radius: 8px;
  --shadow-card: 0 4px 24px rgba(0,0,0,0.06);
  --shadow-section: 0 2px 8px rgba(0,0,0,0.08);
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "Courier New", monospace;
}
body { background: linear-gradient(145deg, var(--background), var(--background-2)); }
```

## Provenance

- **URL:** https://wanquanf.github.io/I2VControlCamera
- **Paper:** I2VControl-Camera: Precise Video Camera Control with Adjustable Motion Strength (arXiv 2411.06525), Wanquan Feng et al.
- **Venue:** ICLR 2025 (banner on page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** none; custom single-file HTML/CSS with Chinese code comments.
- **Measurement method:** static HTML parsed with `extract_style.py` plus manual reading of the inline style blocks. Rendered page not viewed, so the actual body font and the visual effect of the animation are not confirmed.
