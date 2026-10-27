# JARVIS-VLA · Lato Video Wall — Style Reference

> A Minecraft lab notebook pasted full of gameplay clips.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bootstrap 5.0.2 plus the page's `css/app.css`); roles are interpreted from markup and one rendered viewport. Bootstrap's full color set appears in the frequency scan, but only colors used by classes in the markup are listed below.

## Overview

JARVIS-VLA is a Bootstrap page with a Jon Barron-lineage stylesheet: Lato everywhere, link blue `#1772d0` that flips to orange `#f09228` on hover, and a highlight yellow. The header is a large centered bold title over a row of five icon links (Paper, Code, Video, Dataset, Model), then a pipeline figure and a long sequence of Bootstrap cards whose headers hold colored `btn` pills used as tabs. The page carries 68 `<video>` elements in a dense gallery, which is its real signature.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Plain White | `#ffffff` | `--bg` | Page background |
| Barron Blue | `#1772d0` | `--link` | All links |
| Hover Ember | `#f09228` | `--link-hover` | Link hover and focus |
| Highlighter | `#ffffd0` | `--highlight` | `span.highlight` fill |
| Body Ink | `#212529` | `--text` | Bootstrap body text |
| Muted Graphite | `#6c757d` | `--text-muted` | Secondary text, `btn-secondary` |
| Primary Blue | `#0d6efd` | `--btn-primary` | `btn-primary` tab pills |
| Success Green | `#198754` | `--btn-success` | `btn-success` pills |
| Warning Gold | `#ffc107` | `--btn-warning` | `btn-warning` pills |
| Info Cyan | `#0dcaf0` (inferred, Bootstrap 5.0 default) | `--btn-info` | `btn-info` pills |
| Danger Red | `#dc3545` | `--btn-danger` | `btn-danger` pills |
| Card Header Mist | `rgba(0,0,0,.03)` (inferred, Bootstrap 5.0 default) | `--card-head` | Card header strip |
| Hairline | `#dee2e6` | `--border` | Card and table borders |

## Tokens — Typography

- **Family:** Lato 400/700 italic and roman, self-declared `@font-face` from fonts.gstatic.com; fallbacks Verdana, Helvetica, sans-serif.
- **Code:** CodeMirror at .8em and highlight.js default theme.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`h2`) | calc(1.325rem + .9vw), 2rem at ≥1200px | 700 | 1.2 |
| Section heading (`h3`) | calc(1.3rem + .6vw) | 500 | 1.2 |
| Legacy `name` tag | 32px | 400 | — |
| Legacy `heading` | 22px | 400 | — |
| Body | 1rem | 400 | 1.5 |
| `strong`, `papertitle` | 14px | 700 | — |
| Buttons | 1rem (`.875rem` small) | 400 | 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons | .25rem |
| Cards | .25rem |
| Images, videos | 0 (Bootstrap default) |

Shadows: only Bootstrap focus rings, `0 0 0 .25rem rgba(13,110,253,.25)`. Container max widths 540 / 720 / 960 / 1140px by breakpoint.

## Components

- **Icon link row:** five centered icons (paper, GitHub, video, database, cubes) with a small bold caption under each; no button chrome.
- **Card with tab pills:** Bootstrap `card` with `card-header` holding several `btn btn-*` pills in different contextual colors; `card-body` swaps the active video set.
- **Video grid:** `width="100%"` videos in Bootstrap columns, autoplay loops, labeled by task ("Cook", "Harvest", "Kill Mobs").
- **Related project tiles:** 240px-wide thumbnails (OmniJARVIS, JARVIS-1, DEPS) with paper title and links.
- **Code block:** CodeMirror box, `pre.codegen` fixed at 300px height with vertical scroll.

## Page Modules

- **Title/author block:** centered bold title, author names in link blue, team logo line "Team CraftJarvis".
- **Venue badge:** none in the header (the venue appears only in the BibTeX).
- **Link buttons:** Paper, Code, Video, Dataset, Model as icon links.
- **Teaser:** pipeline figure directly below the links.
- **Abstract:** plain paragraph under an `h3`.
- **Results videos:** "Master thousands of skills in Minecraft", "More Results", "Long rollout", "Failure cases analysis" (68 videos in total).
- **Results table:** one Bootstrap table.
- **Datasets:** section listing released data.
- **BibTeX:** `pre` block under "BibTex".

## Do's and Don'ts

- Do let the videos carry the page; text stays in short labels.
- Do use the orange hover on every link to keep the Barron feel.
- Don't round thumbnails or add shadows; this style is flat.
- Don't mix in a second font; Lato covers headings and body.

## Surfaces

Flat white page; Bootstrap cards with hairline borders and a faint header strip are the only containers.

## Imagery

Minecraft gameplay video loops with in-frame instruction captions, one architecture diagram, three related-work thumbnails.

## Layout

Bootstrap `.container` (1140px max at xl), centered header, card stack below, grid rows of 2 to 4 video columns.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, text `#212529`, link `#1772d0`, link hover `#f09228`, highlight `#ffffd0`, border `#dee2e6`.

1. "Build a header icon row: five centered 48px icons with bold 14px Lato captions underneath, links in `#1772d0`, hover `#f09228`, no borders."
2. "Build a video tab card: Bootstrap card, header with `btn-primary`, `btn-success`, `btn-warning` pills as tabs; body is a 3-column grid of looping muted videos at 100% width."
3. "Build a related-project row: 240px thumbnails with no border, bold 14px Lato title to the right, link list beneath."

## Similar Pages

Jon Barron's homepage stylesheet lineage; CraftJarvis sibling projects (JARVIS-1, OmniJARVIS).

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #212529; --text-muted: #6c757d;
  --link: #1772d0; --link-hover: #f09228; --highlight: #ffffd0;
  --border: #dee2e6; --radius: .25rem;
  --font: 'Lato', Verdana, Helvetica, sans-serif;
  --max-width: 1140px;
}
a { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); }
```

## Provenance

- **URL:** https://craftjarvis.github.io/JarvisVLA/
- **Paper:** JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse (arXiv 2503.16365), Muyao Li et al.
- **Venue:** ACL 2025.
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and the abstract links this page.
- **Template credit:** no footer credit. The `app.css` rules (`name`, `heading`, `papertitle` tags, `#1772d0`/`#f09228`) match the Jon Barron homepage stylesheet; this attribution is inferred from the code, not stated on the page.
- **Measurement method:** extract_style.py frequency scan of HTML plus linked CSS, manual reading of `app.css` and the inline `<style>`, and one rendered viewport viewed in a browser. Bootstrap contextual colors are listed because the markup uses those `btn-*` classes; the info cyan value is the Bootstrap 5.0 default and was not in the scan's top list.
