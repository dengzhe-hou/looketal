# PREPING Harbor Serif — Style Reference

> A tidy briefing memo on cool blue-gray stock, Georgia headlines over Inter notes.

**Theme:** light

Values are read from the single hand-written stylesheet `styles.css` (cache-busted as `?v=20261014-original-blue`). No framework, no Google Fonts request: Inter is named first but falls back to system UI unless installed. Roles are interpreted. Rendered output was not viewed.

## Overview

PREPING (KAIST, DeepAuto.ai) is a compact, custom-coded page with a restrained steel-blue palette. A sticky frosted nav (Abstract, Method, Results, BibTeX) sits over a pale `#f6f9fc` page. The hero is centered: an uppercase accent eyebrow "Accepted at NeurIPS 2026", a Georgia serif title whose method name sits on its own line in deep navy at 0.82em, slash-separated author list, a monospaced email line, a muted lead sentence, and two pill buttons (navy filled Paper, white outlined Code). A white bordered figure card with a soft navy shadow holds the concept image. Sections use Georgia h2s, three-column method cards, Georgia metric numerals, a 2×2 square figure grid, and a dark navy BibTeX block.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Harbor Mist | `#f6f9fc` | `--bg` | Page background, nav backdrop |
| Panel White | `#ffffff` | `--panel` | Cards, figures, outline buttons |
| Deep Harbor | `#182a3c` | `--ink` | Headings and primary text |
| Slate Note | `#5b6e80` | `--muted` | Body paragraphs, nav links, captions |
| Pier Line | `#d8e3ed` | `--line` | Borders, nav bottom rule, footer rule |
| Steel Blue | `#326ca3` | `--accent`, `--rose` | Eyebrow, superscripts, alternating metric numerals |
| Navy Anchor | `#163e64` | `--accent-dark` | Method name, author links, primary button, metric numerals |
| Foam | `#e5eff9` | `--accent-soft` | Online metric cards |
| Dusk Blue | `#5b83a8` | `--gold` | Third metric numeral |
| Slash Gray | `#a6b5c3` | (literal) | Author separators |
| Night Code | `#152d44` | (literal) | BibTeX `pre` background |
| Code Text | `#deedfa` | (literal) | BibTeX text |

The `--rose` and `--gold` tokens are named for warm colors but resolve to blues; the file version string says "original-blue", so the palette was deliberately unified (inferred).

## Tokens — Typography

- **Headings:** Georgia, "Times New Roman", serif (h1, h2, metric numerals).
- **Body / UI:** Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI". Not loaded from a CDN, so most visitors see their system sans (inferred).
- **Mono:** "SFMono-Regular", Consolas, "Liberation Mono" for email and BibTeX.
- **Weights:** 650 (nav, authors, captions), 700–800 (eyebrow, buttons), Georgia at normal bold heading weight.

| Role | Size | Weight | Line height |
|---|---|---|---|
| h1 | `clamp(32px, 4.3vw, 50px)`; name line 0.82em | bold (UA) | 1.08 |
| h2 | `clamp(30px, 3.3vw, 42px)` | bold (UA) | 1.12 |
| h3 | 18px (22px in online card) | bold | 1.25 |
| Lead | `clamp(18px, 2vw, 22px)` | 400 | 1.6 |
| Body | 17px | 400 | 1.6 |
| Metric numeral | `clamp(34px, 4vw, 48px)` Georgia | | 1 |
| Affiliations | 15px | 650 | |
| Nav, caption, footer, email | 14px | 650 | 1.4 |
| Eyebrow | 13px uppercase | 800 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons | 999px |
| Figure cards, method cards, metrics, BibTeX | 8px |
| Images inside cards | 4px |

- **Shadows:** `--shadow: 0 18px 42px rgba(24,42,60,.1)` on figure cards; buttons `0 8px 22px rgba(24,42,60,.06)`.
- **Layout:** hero, sections, footer max 1120px; abstract section narrowed to 860px; h1 max 940px; lead 820px.
- **Rhythm:** sections `clamp(58px, 7vw, 92px) 24px`; hero top `clamp(56px, 8vw, 96px)` and `min-height: calc(100vh - 54px)`.

## Components

- **Sticky nav.** Centered links, 14px/650 muted, `rgba(246,249,252,.92)` with blur(16px), hairline bottom.
- **Eyebrow.** 13px/800 uppercase `#326ca3`, carries the acceptance note.
- **Author line.** Names separated by a `/` pseudo-element in `#a6b5c3`; links navy with 4px underline offset; superscripts 800 steel blue.
- **Button.** Min-height 44px, 10px 18px padding, pill, 1px `#d8e3ed` border, white fill, navy 750 text. Primary is navy-filled with white text. Full width (max 280px) on phones.
- **Figure card.** White, 1px line border, 8px radius, `clamp(10px,2vw,18px)` padding, large soft shadow.
- **Method grid.** Three bordered white cards, 22px padding, 16px gap.
- **Metric card.** Big Georgia numeral in navy or steel blue over a 650-weight muted label; online metrics on `#e5eff9`.
- **BibTeX.** `#152d44` pre with `#deedfa` text, 14px/1.5, 8px radius.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Georgia title, slash-separated authors, mono email |
| Venue badge | Eyebrow text "Accepted at NeurIPS 2026" | |
| Link buttons | Paper (arXiv), Code (GitHub) | Pills, primary filled |
| Teaser | Concept figure in shadowed card with caption | |
| Abstract | Narrow 860px section | |
| Method | "Controlled Synthetic Practice" with 3-card grid | |
| Results | Metric grid, online-init two-column card, 2×2 square figure grid | |
| Tables / videos / sliders / 3D / demo | No | |
| BibTeX | Dark navy block | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do pair a serif headline with a sans body.
- Do keep every accent in the blue family; even "rose" and "gold" are blue here.
- Do put the acceptance note in the eyebrow rather than a badge.
- Don't use pure black; the darkest text is `#182a3c`.
- Don't add colored section bands; all sections share the mist background.

## Surfaces

Mist page, white cards, foam-blue metric cards, a navy code block.

## Imagery

Static PNG figures: one wide concept figure and square result plots set `object-fit: contain` on white.

## Layout

Centered hero; left-aligned section content in a 1120px column. Grids drop from 3 to 2 columns at 900px and to 1 at 640px; the nav becomes horizontally scrollable.

## Agent Prompt Guide

**Quick colors:** bg `#f6f9fc`, panel `#ffffff`, ink `#182a3c`, muted `#5b6e80`, line `#d8e3ed`, accent `#326ca3`, navy `#163e64`, soft `#e5eff9`, code `#152d44`.

1. "Create a centered hero: 13px/800 uppercase `#326ca3` eyebrow, Georgia title with the method name on its own line in `#163e64` at 0.82em, authors separated by gray slashes."
2. "Make pill buttons 44px tall: white with 1px `#d8e3ed` border and navy 750 text; the primary one filled `#163e64` with white text."
3. "Build a metric card grid (auto-fit, min 190px): white cards with 8px radius, Georgia 48px navy numerals, 650-weight `#5b6e80` labels."

## Similar Pages

Custom single-file pages from LLM-agent groups; within this collection the serif-over-sans pairing is closest to ReMind's.

## Quick Start

```css
:root {
  --bg: #f6f9fc; --panel: #ffffff; --ink: #182a3c; --muted: #5b6e80;
  --line: #d8e3ed; --accent: #326ca3; --accent-dark: #163e64;
  --accent-soft: #e5eff9; --code-bg: #152d44; --code-fg: #deedfa;
  --font-head: Georgia, "Times New Roman", serif;
  --font-body: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  --radius: 8px; --radius-pill: 999px; --max: 1120px;
  --shadow: 0 18px 42px rgba(24, 42, 60, 0.1);
}
```

## Provenance

- **URL:** https://dozi01.github.io/preping-project-page/
- **Paper:** PREPING: Zero-Task Agent Memory Construction via Self-Practice (arXiv 2605.13880), Yumin Choi et al., KAIST and DeepAuto.ai.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** none stated; custom HTML/CSS.
- **Measurement method:** static HTML and `styles.css` parsed with `extract_style.py` and read in full. Not viewed in a browser; the font actually rendered depends on whether Inter is installed locally.
