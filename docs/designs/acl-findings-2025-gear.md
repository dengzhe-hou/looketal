# GeAR · Charcoal Code Window — Style Reference

> A Nerfies page that opens a dark IDE tab halfway down the scroll.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9 plus the page's own `static/css/index.css`); component roles are interpreted from markup and one rendered viewport. Bulma ships a full palette, so only colors that the page's markup or custom CSS actually uses are listed.

## Overview

GeAR keeps the Nerfies / Academic Project Page Template skeleton (Google Sans title, Noto Sans body, dark pill link buttons) and adds three custom pieces of furniture: white "innovation" cards that lift on hover, numbered process steps with a blue circular badge, and a VS Code-style code window with traffic-light dots, tabs and Dark+ syntax colors. Sections alternate between white and Bulma's `#f5f5f5` light hero bands, which gives the long page a soft striped rhythm. The container is pinned to 960px.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Body and white section bands, card faces |
| Bench Grey | `#f5f5f5` | `--bg-band` | `section hero is-light` alternating bands (5 of 9 sections) |
| Ink Black | `#000000` | `--text-strong` | Body text and title (custom `body { color:#000 }`) |
| Author Sky | `#209cee` | `--link-author` | Author links, from `hsl(204,86%,53%)` |
| Venue Slate | `#555555` | `--text-venue` | `.publication-venue` line |
| Bulma Blue | `#3273dc` | `--accent` | Innovation icons, hover titles, step-number circles |
| Charcoal Console | `#2d2d2d` | `--code-frame` | Code-window chrome and the CTA button |
| Editor Night | `#1e1e1e` | `--code-bg` | Active tab and code body |
| Idle Tab | `#3d3d3d` | `--code-tab` | Inactive tabs |
| Console Text | `#d4d4d4` | `--code-fg` | Default code text |
| Traffic Red / Amber / Green | `#ff5f56` / `#ffbd2e` / `#27c93f` | `--dot-*` | Window-control dots |
| arXiv Cardinal | `#b31b1b` | `--arxiv` | arXiv icon inside dark buttons |
| Question Crimson | `#d32f2f` | `--q` | "Question" label in worked example |
| Answer Forest | `#2e7d32` | `--a` | "Answer" label and final-answer border |
| Answer Mint | `#e8f5e9` | `--a-bg` | Final-answer panel fill |
| Midnight Slate | `#2c3e50` | `--text-heading-alt` | Iteration headers, card hover text |
| Fog Border | `#e0e0e0` | `--border-soft` | Iteration container border |

Syntax colors follow VS Code Dark+: keyword `#569cd6`, class/builtin `#4ec9b0`, function `#dcdcaa`, comment `#6a9955`, string `#ce9178`, number `#b5cea8`, variable `#9cdcfe`.

## Tokens — Typography

- **Display:** Google Sans (substitute: Product Sans, Inter) for title, authors and `.teaser`.
- **Body:** Noto Sans, sans-serif.
- **Code:** JetBrains Mono 400/500/600 (Google Fonts), fallbacks Fira Code, Monaco.
- **Weights:** 400 body, 600 card titles, 700 title and step numbers.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem | 600 | 1.125 |
| Section title (`title is-3`) | 2rem | 600 | 1.125 |
| Iteration header | 1.25rem | 500 | 1.25 |
| Body / abstract | 1rem (`is-size-5` blocks at 1.25rem) | 400 | 1.5 |
| Code content | 17px | 400 | 1.6 |
| Tab label | 14px | 400 | 1 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (Bulma `is-rounded` pill) |
| Code window | 20px |
| Innovation / process cards | 10px |
| Iteration container | 12px |
| Example steps, CTA, QA image | 8px |
| Tabs | 8px 8px 0 0 |

Shadows: card `0 2px 15px rgba(0,0,0,0.1)`, card hover `0 8px 25px rgba(0,0,0,0.15)`, code window `0 4px 6px rgba(45,45,45,0.2)`. Layout max width 960px (`.container.is-max-desktop` override).

## Components

- **Link buttons:** `button is-normal is-rounded is-dark`, Bulma dark `#363636` fill, white text, Font Awesome / Academicons icon left. Labels arXiv, PDF, Code Snippets.
- **Innovation card:** white, padding 2rem, radius 10px, centered; 2.5rem blue icon that scales to 1.1 on hover; card rises 5px.
- **Process step:** white card with a 40px `#3273dc` circle numbered in bold white, offset -20px top-left; grid `repeat(auto-fit,minmax(300px,1fr))`, gap 2rem.
- **Code window:** `#2d2d2d` frame, 36px header with three 12px dots, horizontally scrolling tabs, `#1e1e1e` body, 20px padding.
- **Collapsible iteration:** 2px `#e0e0e0` border, 12px radius, header strip `#f8f9fa` turning `#edf2f7` on hover, chevron toggle.
- **CTA button:** `#2d2d2d`, padding 1.5rem 2rem, 1.25rem text, hover `#504f4f` with 2px lift.

## Page Modules

- **Title/author block:** centered, Google Sans, sky-blue author links, affiliation line, venue line "Submitted to ACL 2025" in the rendered header (the arXiv comment states Findings), equal-contribution footnote.
- **Venue badge:** plain text line, no pill.
- **Link buttons:** arXiv, PDF, Code Snippets (no data or demo link).
- **Teaser:** none; the page opens straight into "Key Innovations" cards.
- **Method:** "How it Works" numbered steps plus a worked multi-hop example with collapsible iterations.
- **Results:** "Retrieval Results" and "Question-Answering Results" as images in a Bulma carousel (no HTML tables).
- **Pseudocode:** tabbed code window.
- **BibTeX:** Nerfies `pre` block.
- **Footer:** Academic Project Page Template credit, CC BY-SA 4.0.

## Do's and Don'ts

- Do keep cards white on the grey bands so the alternation reads.
- Do reserve `#3273dc` for icons, step badges and hover states.
- Don't color the code window with the page accent; it stays Dark+ neutral.
- Don't add a second display face; Google Sans carries every heading.

## Surfaces

Three levels: `#f5f5f5` band, `#ffffff` card with soft shadow, and the dark code console as an inset "screen".

## Imagery

Icon-led cards (Font Awesome), result plots as PNG figures with 8px radius and soft shadow, no video.

## Layout

Single 960px column, centered headings, 2- or 4-up card grids, generous vertical section padding from Bulma `.section`.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, band `#f5f5f5`, text `#000000`, accent `#3273dc`, console `#1e1e1e`/`#2d2d2d`, author link `#209cee`.

1. "Build an innovation card: white, radius 10px, padding 2rem, shadow `0 2px 15px rgba(0,0,0,.1)`, 2.5rem `#3273dc` icon, Google Sans h3; on hover translateY(-5px)."
2. "Build a code window: `#2d2d2d` frame radius 20px, 36px header with 12px dots `#ff5f56 #ffbd2e #27c93f`, tabs `#3d3d3d` inactive and `#1e1e1e` active, JetBrains Mono 17px/1.6 in `#d4d4d4`."
3. "Build a numbered process step: white card radius 10px; a 40px circle `#3273dc` with white bold numeral pinned at top:-20px left:-20px."

## Similar Pages

Nerfies; Academic Project Page Template (eliahuhorwitz); other Bulma pages in this batch such as InstructPart and NegVQA.

## Quick Start

```css
:root {
  --bg: #ffffff; --bg-band: #f5f5f5; --text: #000000;
  --accent: #3273dc; --author: #209cee; --venue: #555555;
  --code-frame: #2d2d2d; --code-bg: #1e1e1e; --code-fg: #d4d4d4;
  --radius-card: 10px; --radius-code: 20px; --radius-pill: 290486px;
  --shadow-card: 0 2px 15px rgba(0,0,0,.1);
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-code: 'JetBrains Mono', monospace;
  --max-width: 960px;
}
```

## Provenance

- **URL:** https://gear-rag.github.io/
- **Paper:** GeAR: Graph-enhanced Agent for Retrieval-augmented Generation (arXiv 2412.18431), Zhili Shen et al.
- **Venue:** ACL 2025 Findings.
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 Findings and the abstract links this page.
- **Template credit:** footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method:** colors, sizes and radii from the extract_style.py frequency scan of HTML and linked CSS plus a manual read of `index.css`; Bulma defaults (for example the `#363636` button fill) are named only where markup uses the class. One rendered viewport was viewed in a browser. `#209cee` is converted from the HSL value in CSS.
