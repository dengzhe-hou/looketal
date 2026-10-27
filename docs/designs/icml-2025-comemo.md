# CoMemo Acronym Chips — Style Reference

> A Nerfies page that spells its acronym out of blue chips inside the title.

**Theme:** light

Values come from the static HTML, inline image-sizing attributes and a customized Academic Project Page Template `index.css` over Bulma 0.9. Bulma's unused palette is excluded. Measurements are normalized; roles are interpreted.

## Overview

CoMemo uses the Academic Project Page Template with two small but distinctive additions in `index.css`. In the title "CoMemo: LVLMs Need Image Context with Image Memory", the letters "Co" and "Memo" are wrapped in `.highlight` chips: white bold text on `#007acc` with 5px corners, so the acronym is spelled out visually. In captions, key claims get a `.soft-highlight`: dark teal `#004d40` bold text on pale aqua `#e0f7fa`. The light hero bands are repainted from Bulma's `#f5f5f5` to a cooler `#fafafa`. The body is long and argument-driven ("Design Thinking for CoMemo" with numbered h3 questions), with figures placed in flex rows at percentage widths and many `subtitle has-text-centered` h2s used as figure captions. Results are table images, not HTML tables.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Acronym Blue | `#007acc` | `.highlight` background | Chips behind "Co" and "Memo" in the title |
| Chip White | `#ffffff` | `.highlight` color | Chip text, bold |
| Deep Teal | `#004d40` | `.soft-highlight` color | Highlighted claim text in captions |
| Aqua Wash | `#e0f7fa` | `.soft-highlight` background | Highlighted claim fill |
| Band Paper | `#fafafa` | `.hero.is-light` override | Light section bands |
| Bulma Charcoal | `#363636` | `.title`, `button is-dark` | Title text, section titles, link buttons |
| Body Gray | `#4a4a4a` | Bulma `$text` | Body text and caption subtitles (Bulma default) |
| Author Sky | `hsl(204, 86%, 53%)` | template `.publication-authors a` | Author links (≈ `#209cee`) |
| Card Rule | `#cccccc` | `.my-card` | Defined card border (not used on this page) |

## Tokens — Typography

- **Display / authors:** `Google Sans` (Google Fonts link also loads Noto Sans and Castoro). Substitute: Product Sans, Inter.
- **Body:** `Noto Sans`, sans-serif.
- No math library.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`title is-1`) | 3rem | 600; chips bold | Line break after "Need" |
| Affiliations and venue | `is-size-5` 1.25rem | 400 | "ICML 2025" on its own line inside the affiliation block |
| Section h2 (`title is-3`) | 2rem | 600 | Design Thinking, Method, Main Results, BibTeX |
| Question h3 | Bulma content h3 1.5em (inferred) | 600 | Numbered "1. Why LVLMs Tend to 'lose in the middle'?" |
| Caption h2 (`subtitle has-text-centered`) | 1.25rem | 400 | Long figure captions with bold "Left:"/"Right:" |
| Body | 1rem | 400 | Justified |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Acronym chip | 5px |
| Soft highlight | 3px |
| Link buttons | 290486px (Bulma rounded) |
| Carousel items | 10px (template) |

- **Chip padding:** `.highlight` 0 5px; `.soft-highlight` 2px 4px.
- **Shadows:** none added.
- **Layout:** Bulma `container is-max-desktop` (960px); figure rows `display:flex; justify-content:center; gap:10px; margin:20px 0` with images at 30%, 35%, 53%, 65% or 70% max-width.

## Components

- **Acronym chip.** `span.highlight`: `#007acc` background, white bold text, 0 5px padding, 5px radius, inline in the 3rem title.
- **Soft highlight.** `span.soft-highlight`: `#e0f7fa` background, `#004d40` bold text (`!important`), 2px 4px padding, 3px radius; used on the one-sentence takeaway in captions.
- **Dark pill link button.** Bulma `external-link button is-normal is-rounded is-dark`: Paper, Supplementary, Code, Model, arXiv.
- **Image row.** Flex row of two or three figures at percentage widths with 10px gaps, followed by a centered subtitle caption.
- **Light band.** `section hero is-light` at `#fafafa` for the abstract-adjacent design discussion and results.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Chips inside the title |
| Venue badge | "ICML 2025" text in the affiliation line | No chip |
| Link buttons | Paper, Supplementary, Code, Model, arXiv | Dark rounded |
| Teaser | Figure with long caption and soft-highlighted takeaway | `hero teaser` |
| Abstract | Yes | Template |
| Design rationale | "Design Thinking for CoMemo" with three numbered questions | `#fafafa` band |
| Method figure | "Method" (RoPE-DHR computation) | Image row |
| Results | "Main Results" with three table images (Tables 1–3) | Captions as subtitles |
| Carousel | Template carousel scripts loaded | |
| Video / sliders / 3D / HF | No | |
| BibTeX | Yes | Template pre |
| Acknowledgements | No | Footer credits the template |

## Do's and Don'ts

- Do spell the acronym in the title with solid chips, and use the chip color nowhere else.
- Do give each figure caption one soft-highlighted takeaway sentence.
- Do size figures in a row by percentage so their heights roughly match.
- Don't use the soft highlight for whole paragraphs; it marks one clause.
- Don't leave template meta text such as `KEYWORDS SHOULD BE PLACED HERE` in the head, as this page does.

## Surfaces

White hero and BibTeX sections, `#fafafa` light bands for the design and results sections.

## Imagery

Charts (attention heatmaps, needle-in-a-haystack results, remote-decay curves), architecture diagrams and table screenshots; 12 images.

## Layout

Single 960px Bulma column; figures in centered flex rows; captions centered under them.

## Agent Prompt Guide

**Quick colors:** text `#4a4a4a`, title `#363636`, chip `#007acc` with white text, takeaway `#004d40` on `#e0f7fa`, band `#fafafa`.

1. "Write a 3rem Google Sans title where the letters 'Co' and 'Memo' are inline chips: `#007acc` background, white bold text, padding 0 5px, 5px radius."
2. "Under a figure row, add a centered 1.25rem subtitle caption with bold 'Left:' and 'Right:' labels, and wrap the key claim in a `#e0f7fa` highlight with bold `#004d40` text, 2px 4px padding, 3px radius."
3. "Make a light section band in `#fafafa` holding a 2rem section title and numbered h3 questions, each followed by a paragraph and a flex row of figures with 10px gaps."

## Similar Pages

Other Academic Project Page Template pages in this collection (SmPO, EQ-VAE, WAM); DPLM-2.1 shares the long, report-like section structure.

## Quick Start

```css
:root {
  --text: #4a4a4a; --title: #363636; --author: hsl(204, 86%, 53%);
  --chip: #007acc; --chip-text: #ffffff;
  --takeaway: #004d40; --takeaway-bg: #e0f7fa;
  --band: #fafafa;
  --font-display: "Google Sans", "Inter", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --container: 960px;
}
.highlight { color: var(--chip-text); background: var(--chip); padding: 0 5px; border-radius: 5px; font-weight: bold; }
.soft-highlight { color: var(--takeaway); background: var(--takeaway-bg); padding: 2px 4px; border-radius: 3px; font-weight: bold; }
```

## Provenance

- **URL:** https://lalbj.github.io/projects/CoMemo/
- **Paper:** CoMemo: LVLMs Need Image Context with Image Memory (arXiv 2506.06279), Shi Liu et al.
- **Venue:** ICML 2025 (text in the affiliation block).
- **Selection reason:** arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- **Template credit:** footer says it "was built using the Academic Project Page Template which was adopted from the Nerfies project page".
- **Measurement method:** `extract_style.py` plus manual reading of `index.css` and inline styles; commented-out markup excluded. Rendered page not viewed.
