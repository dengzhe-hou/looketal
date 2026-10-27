# T3-Video Brick Red Nerfies — Style Reference

> A Nerfies page with a brick-red product name and one charcoal band of bullet points.

**Theme:** light

Values come from the static HTML, its inline `<style>` block and the stock Nerfies `index.css` over Bulma 0.9. Bulma framework colors that the markup never uses are left out. Measurements are normalized; roles are interpreted.

## Overview

T3-Video keeps the classic Nerfies skeleton: centered Google Sans title, author list with numbered affiliations, a row of dark rounded link buttons, a YouTube video, the abstract, and BibTeX. Two touches make it its own. The method name in the title and in the teaser headline is set in brick red `#b02418`, and a full-width Bulma `hero is-dark is-small` band (charcoal `#363636`) carries the "High-lights for the T3 Module" list with "High-lights" in salmon `#f49d95`. A JS-driven results gallery adds rounded slate-tinted group headers, black 14px-radius video frames and a blue gradient pill for prev/next. The title is enlarged inline to 2.6rem on a `title is-2`.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Brick Red | `#b02418` | (inline) | "T3-Video" in the title and teaser headline |
| Salmon Highlight | `#f49d95` | (inline) | "High-lights" word on the dark band |
| Bulma Charcoal | `#363636` | `hero is-dark` / `button is-dark` | Highlights band, link buttons, titles |
| Body Gray | `#4a4a4a` | Bulma `$text` | Body text (inferred Bulma default) |
| Overview Ink | `#222222` | `.overview-text` | Justified overview paragraph |
| Author Sky | `hsl(204, 86%, 53%)` | Nerfies `.publication-authors a` | Author links (≈ `#209cee`) |
| Gallery Navy | `#1f2a44` | `.group-header` | Group header text |
| Header Wash | `rgba(48,70,141,0.07)` | `.group-header` | Group header fill, border `rgba(58,92,180,0.18)` |
| Gradient Start | `#2951ff` | `.carousel-button` | Prev/next pill gradient start |
| Bulma Blue | `#3273dc` | `$link` | Gradient end, body links |
| Source Blue | `#1e70bf` | `.source-label` | Caption label "source" |
| Edit Orange | `#ff8c00` | `.edit-label` | Caption label "edit" |
| Target Pink | `#e91e63` | `.target-label` | Caption label "target" |
| Category Burgundy | `#800020` | `.category-label` | Group category label |
| Subcategory Mint | `#10d87b` | `.subcategory-label` | Group subcategory label |
| Caption Paper | `#f9f9f9` | `.video-caption` | Scrollable caption box, 4px `#e0e0e0` left rule |
| Label Gray | `#5b5b5b` | `.video-label` | Uppercase labels under videos |
| Film Black | `#000000` | `.video-frame` | Video frame background |

## Tokens — Typography

- **Display / authors:** `Google Sans` (Google Fonts link also requests Noto Sans and Castoro). Substitute: Product Sans, Inter.
- **Body:** `Noto Sans`, sans-serif (Nerfies). Castoro is loaded but no rule uses it (inferred).
- **Method token:** `"Courier New", Courier, monospace` bold `#333` (`.overview-text .method`).

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title | 2.6rem (inline override of `is-2`) | 600; method name bold | Google Sans |
| Teaser headline (`title is-4`) | 1.5rem | 600 | Contains red "T3-Video" |
| Section h2 (`title is-3`) | 2rem | 600 | |
| Overview text | 1.05rem | 400 | line-height 1.65, justified, hyphenated, max 900px |
| Video caption | 14px | 400 | line-height 1.8 |
| Video label | 0.82rem | 600 | uppercase, 0.02em tracking |
| Gallery pill | 0.95rem | 600 | 0.02em tracking |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (Bulma rounded) |
| Gallery pill | 999px |
| Gallery wrapper | 18px |
| Group header, video frame | 14px |
| Caption box, YouTube wrapper (Nerfies) | 8px / 10px |
| Images (inline) | 8px |

- **Shadows:** video frames `0 10px 24px -12px rgba(15,23,42,0.45)`; gallery pill `0 12px 22px -12px rgba(50,115,220,0.85)`, deepening on hover.
- **Layout:** `.hero.teaser .container` max 1000px; content `container is-max-desktop` (960px); video rows sized by `--video-target-height: clamp(100px, 10vw, 200px)` with 16:9 or square tiles and 5px gaps.

## Components

- **Dark pill link button.** Bulma `external-link button is-normal is-rounded is-dark`. Visible labels: Paper, arXiv, Data, Data-Long; Code and Models buttons are commented out in the source.
- **Highlights band.** `hero is-dark is-small`: charcoal full-bleed band, centered `title is-3` with the salmon "High-lights" word, then a justified list of numbered `<strong>1)</strong>` points.
- **Gallery group header.** Flex column, padding 0.85rem 1.2rem, `rgba(48,70,141,0.07)` fill, 1px `rgba(58,92,180,0.18)` border, 14px radius, `#1f2a44` text; colored bold labels for category, subcategory and edit.
- **Video tile.** Black frame with 14px radius, contain-fit for wide clips and cover-fit for square ones, uppercase gray label below.
- **Gradient pill.** `linear-gradient(135deg, #2951ff, #3273dc)`, white 0.95rem/600 text, padding 0.75rem 1.75rem, lifts 1px on hover; disabled at 0.55 opacity.
- **Caption box.** `#f9f9f9`, 4px `#e0e0e0` left border, 8px radius, max-height 220px with a thin custom scrollbar.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Nerfies centered; affiliations with superscripts; `#` marks corresponding authors |
| Venue badge | No | The page does not mention ICML |
| Link buttons | Paper, arXiv, Data, Data-Long | Dark rounded |
| Teaser | `hero teaser` with headline | Image at 8px radius |
| Video | YouTube embed | Nerfies 16:9 wrapper |
| Abstract | Yes | Justified Bulma content |
| Method highlights | Dark band | See above |
| Results gallery | JS-driven grouped video gallery | Group headers, video rows, gradient pills |
| Tables | No `<table>` in static HTML; sortable `.leaderboard-table` CSS is defined but unused (inferred) | |
| BibTeX | Yes | Nerfies pre block |
| Acknowledgements | No | |

## Do's and Don'ts

- Do color only the method name red; the rest of the title stays charcoal.
- Do use the dark band once, for the key bullet list.
- Do keep gallery chrome cool and slate-tinted so the video frames read first.
- Don't mix the caption label colors into headings; they are a legend for edit captions only.
- Don't add a venue badge the page does not have.

## Surfaces

White page, one charcoal `#363636` full-bleed band, a near-white `rgba(255,255,255,0.92)` gallery wrapper, black video frames.

## Imagery

4K video generation samples, wide and square, in black frames; static teaser and figure images with 8px corners.

## Layout

Centered 960px column (1000px for the teaser). Gallery rows wrap and center; under 640px the group-header rows wrap horizontally.

## Agent Prompt Guide

**Quick colors:** text `#4a4a4a`, title `#363636`, method red `#b02418`, band `#363636`, band accent `#f49d95`, gallery ink `#1f2a44`, pill `#2951ff→#3273dc`.

1. "Write a Nerfies title in Google Sans at 2.6rem where only the method name 'T3-Video:' is bold `#b02418`."
2. "Create a full-bleed charcoal `#363636` highlights band with a centered 2rem title whose first word is salmon `#f49d95`, followed by numbered justified points in white."
3. "Build a gallery group header: padding 0.85rem 1.2rem, fill `rgba(48,70,141,0.07)`, 1px `rgba(58,92,180,0.18)` border, 14px radius, `#1f2a44` text, with bold labels in `#800020`, `#10d87b` and `#ff8c00`."

## Similar Pages

Nerfies-based video generation pages such as RIFLEx and FR3D in this collection.

## Quick Start

```css
:root {
  --text: #4a4a4a; --title: #363636; --method-red: #b02418;
  --band: #363636; --band-accent: #f49d95;
  --gallery-ink: #1f2a44; --gallery-wash: rgba(48,70,141,0.07);
  --gallery-line: rgba(58,92,180,0.18);
  --pill-grad: linear-gradient(135deg, #2951ff, #3273dc);
  --caption-bg: #f9f9f9; --caption-rule: #e0e0e0;
  --font-display: "Google Sans", "Inter", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --container: 960px; --teaser: 1000px;
}
```

## Provenance

- **URL:** https://zhangzjn.github.io/projects/T3-Video/
- **Paper:** Transform Trained Transformer for Accelerating Native 4K Video Generation (arXiv 2512.13492), Jiangning Zhang et al.
- **Venue:** ICML 2026, per the arXiv comment. The page itself shows no venue.
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit:** Nerfies structure and stock `index.css`; the footer keeps the Nerfies CC BY-SA 4.0 wording but does not name Nerfies.
- **Measurement method:** `extract_style.py` plus manual reading of the inline styles and `index.css`; commented-out markup excluded. Rendered page not viewed, so the JS gallery's populated state is inferred from CSS.
