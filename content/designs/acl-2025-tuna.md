# TUNA · Ocean Gradient Venue — Style Reference

> A benchmark page with a fish mascot and a venue line that shimmers from sea blue to seafoam.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9, a MathVista-derived `index.css`, `leaderboard.css`, `video-player.css` and an inline `<style>`); roles are interpreted from markup and one rendered viewport. Bulma palette colors in the frequency scan are listed only where used.

## Overview

TUNA comes from the MathVista / Video-MME family of benchmark pages. A Bulma navbar with a "More Research" dropdown sits on top; the title is a fish logo at 1.6em beside "TUNA" set with a small-caps trick (`T` plus smaller `UNA`), followed by a two-line Google Sans subtitle, sky-blue authors, and the venue "ACL 2025 Main" painted with a `#0077be → #00c9a7` text gradient. Four dark pill buttons lead to arXiv, Code, Dataset and Leaderboard. Major parts (Benchmark, Method, Analysis, More Data Examples, Citation) open with large `title is-1` headings inside `hero is-light is-small` bands. Video examples use custom play buttons in translucent red and teal-grey control buttons.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Light Band | `#f5f5f5` | `--bg-band` | `hero is-light is-small` part dividers (5) |
| Sea Blue | `#0077be` | `--venue-start` | Venue gradient start |
| Seafoam | `#00c9a7` | `--venue-end` | Venue gradient end |
| Bulma Ink | `#363636` | `--text-heading` | Titles; dark pill fill |
| Body Grey | `#4a4a4a` | `--text` | Body text |
| Author Sky | `#209cee` | `--link-author` | Author links (`hsl(204,86%,53%)`) |
| Org Caption Grey | `#858383` | `--text-org` | 12px organization labels under leaderboard models (21 uses) |
| Lagoon | `#69a8b2` | `--btn-teal` | Video control buttons |
| Deep Lagoon | `#3e9aa8` | `--btn-teal-hover` | Control button hover |
| Driftwood | `#cbcbc4` | `--btn-neutral` | Neutral control button |
| Play Coral | `rgba(255,60,60,0.8)` | `--play` | Video play button (solid on hover) |
| Midnight Slate | `#2c3e50` | `--text-player` | Player labels |
| Code Ash / Code Pink | `#f4f4f4` / `#d63384` | `--code-bg` / `--code-fg` | `pre` background and inline code color |
| Rule Grey | `#dddddd` | `--border` | Code block and table borders |
| Sort Highlight | `#ddeeee` (`#dee`) | `--sort` | Sorted leaderboard column |
| Best Crimson | `#c6011f` | `--best` | Best-score text |

## Tokens — Typography

- **Display:** Google Sans for title, subtitle, authors. A `CustomFont` (Gilroy Bold Italic, 80px, `.mathvista`) is declared from the MathVista template.
- **Body:** Noto Sans.
- **Tables:** Arial, Helvetica 16px.
- **Code:** Consolas, "Courier New", monospace.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Logo title (`title is-1`) | 3rem, "UNA" at `smaller` | 600 | 1.125 |
| Subtitle (`subtitle is-3`) | 2rem | 400 | 1.25 |
| Part heading (`title is-1`, `.mathvista_other`) | 3rem | 700 | 1.125 |
| Section heading (`title is-3`) | 2rem | 600 | 1.125 |
| Venue | 1.25rem gradient text | 700 | 1.5 |
| Leaderboard | 16px | 400; header 600 | — |
| Org caption | 12px | 400 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px pill |
| Video control buttons | 5px |
| Play button | 50% |
| Code block | 5px |
| Org banners | 0 |

Shadows: player `rgba(0,0,0,0.2)`–`rgba(0,0,0,0.3)` soft shadows. Leaderboard cells 8px padding (12px top and bottom in header). Stats images max-height 250px; content columns at 90% and 50% widths. Container `is-max-desktop` (960px).

## Components

- **Navbar:** Bulma navbar with a hoverable "More Research" dropdown linking sibling projects.
- **Logo title:** inline logo image at 1.6em, vertical-align middle, then the small-caps name.
- **Gradient venue:** `background: linear-gradient(to right,#0077be,#00c9a7)` with `background-clip:text` and transparent fill.
- **Pill buttons:** `is-dark is-rounded` with emoji or icon: arXiv, Code, 🤗 Dataset, 🏆 Leaderboard.
- **Leaderboard:** sortable, Arial 16px, `#ddd` borders, even rows `#f5f5f5`, hover `#ddd`, best score crimson, org name in 12px grey under each model.
- **Video player:** custom controls with coral round play button and teal-grey 5px buttons.
- **Org banner row:** flex-wrapped logos at 6em height.

## Page Modules

- **Title/author block:** logo title, subtitle, sky-blue authors with affiliations (Northeastern University, Kuaishou Technology), corresponding-author note.
- **Venue badge:** gradient text line "ACL 2025 Main".
- **Link buttons:** arXiv, Code, Dataset, Leaderboard.
- **Abstract:** centered heading, justified text.
- **Results table:** "Leaderboard (TUNA-CAP)".
- **Benchmark:** "Data Examples" with 5 videos, "Dataset Statistics", "Benchmark Comparison".
- **Method:** "Pipeline" figure.
- **Analysis:** "Video Complexity / Input Frames".
- **Carousel:** "More Data Examples".
- **BibTeX:** under "Citation".
- **Footer:** the visible credit (adapted from Video-MME, CC BY-SA 4.0) sits inside an HTML comment remnant, so its rendering was not confirmed.

## Do's and Don'ts

- Do keep the gradient for the venue line only.
- Do separate major parts with big `title is-1` headings on light bands.
- Don't use the coral red outside the play button.
- Don't drop the small-caps "UNA"; it is the wordmark.

## Surfaces

White body, light grey part dividers, flat tables; video players carry the only shadows.

## Imagery

Fish logo, dense dynamic video clips, statistics charts capped at 250px tall, organization logos.

## Layout

960px column with navbar above; part headings centered; 90% wide figures.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, band `#f5f5f5`, venue gradient `#0077be → #00c9a7`, authors `#209cee`, controls `#69a8b2`/`#3e9aa8`, play `rgba(255,60,60,.8)`.

1. "Build a gradient venue line: bold 1.25rem text, `background: linear-gradient(to right,#0077be,#00c9a7)`, `-webkit-background-clip:text`, transparent text fill."
2. "Build a logo title: 1.6em logo image beside 'T' and smaller 'UNA', Google Sans 3rem/600, two-line subtitle at 2rem/400 below."
3. "Build a leaderboard row: Arial 16px, `#ddd` borders, model name with a 12px `#858383` organization caption, best score in `#c6011f`."

## Similar Pages

MathVista and Video-MME project pages; PRMBench in this batch.

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f5f5f5; --text: #4a4a4a; --heading: #363636;
  --author: #209cee; --venue: linear-gradient(to right, #0077be, #00c9a7);
  --control: #69a8b2; --control-hover: #3e9aa8; --play: rgba(255,60,60,.8);
  --org: #858383; --best: #c6011f; --border: #ddd;
  --radius-pill: 290486px; --radius-control: 5px;
  --font-display: 'Google Sans', sans-serif; --font-body: 'Noto Sans', sans-serif;
  --max-width: 960px;
}
```

## Provenance

- **URL:** https://friedrichor.github.io/projects/TUNA/
- **Paper:** TUNA: Comprehensive Fine-grained Temporal Understanding Evaluation on Dense Dynamic Videos (arXiv 2505.20124), Fanheng Kong et al.
- **Venue:** ACL 2025 (main).
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and links this page.
- **Template credit:** footer text says adapted from Video-MME under CC BY-SA 4.0, but it is wrapped in a stray comment marker; the CSS (`.mathvista`, Gilroy CustomFont) shows MathVista lineage.
- **Measurement method:** extract_style.py scan, manual reading of `index.css`, `leaderboard.css`, `video-player.css` and inline styles, one rendered viewport. `leaderboard.css` header uses an undefined `--UCLA-darkblue` variable, so the rendered header color was not determined.
