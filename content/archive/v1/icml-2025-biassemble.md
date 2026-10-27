# BiAssemble Google Sites Serif — Style Reference

> A Google Sites page where the authors hand-typed a paper header in Times New Roman.

**Theme:** light

Values come from the static HTML of a published Google Sites page: the theme stylesheet embedded in `<style>` (Material 3 `--gm3-*` and `--ws-sys-*` variables, mostly unused system tokens) and the editor's inline `<span style>` attributes, which carry the authors' real choices. Measurements are normalized; Google Sites sizes are in pt. Roles are interpreted.

## Overview

BiAssemble is built in Google Sites with a light theme whose defaults are Lato body text at 11pt in `#212121` and Lato Light h1s in steel teal `#226e93`. The authors override the header by hand: the title is bold black Times New Roman, the venue line "International Conference on Machine Learning (ICML) 2025" is bold forest green `#38761d`, author names are underlined leaf green `#6aa84f`, and the links are bracketed bold underlined text, "[Paper] [Code] [Dataset]", at 15pt. Section titles (Abstract, Video Presentation, Framework, Real-World Benchmark, experiments) switch to bold Lato in dark red `#980000`. Figures carry long bold-numbered captions; the abstract is set larger at 14pt. All seven videos are Google Drive preview iframes. The page title tag is "首页" (Home) and the standard Google Sites footer ("Report abuse", "Page details") remains.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Title Black | `#000000` | inline | Paper title, punctuation between authors |
| Forest Venue | `#38761d` | inline | Venue line, bold |
| Leaf Author | `#6aa84f` | inline | Author names, underlined |
| Section Maroon | `#980000` | inline | Section titles, bold Lato |
| Note Gray | `#4a4a4a` | inline | "(* denotes equal contribution)" and link separators |
| Theme Ink | `rgba(33,33,33,1)` (`#212121`) | `.zfr3Q` | Default paragraph text |
| Theme Teal | `rgba(34,110,147,1)` (`#226e93`) | `.duRjpb` | Default h1 color (overridden by inline black on the title) |
| Paper | `#ffffff` | theme | Page background |
| Google Blue | `#0b57d0` | `--gm3-sys-color-primary` | Google Sites chrome (search, nav, footer); not part of the content |

## Tokens — Typography

- **Header (inline override):** `'Times New Roman', Arial` for title, venue, authors and bracketed links. Substitute: Tinos, Liberation Serif.
- **Theme text and section titles:** `Lato` (Google Fonts, 300/400/700 with italics). Substitute: Carlito.
- **Site chrome:** Google Sans and Roboto (Google Sites UI only).

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (h1 `.duRjpb`) | theme 34pt (responsive steps 24–64pt) | 700 inline | Times New Roman, black, line-height 0.96, centered |
| Venue line | inherits h1 size | 700 | Forest green |
| Authors | theme body (inferred) | 400 | Underlined green |
| Links "[Paper]" etc. | 15pt | 700 | Underlined, color inherited from the link |
| Equal-contribution note | 15pt | 400 | `#4a4a4a` |
| Section titles | inherits block style | 700 | Lato, `#980000` |
| Abstract | 14pt | 400 | |
| Body / captions | 11pt (theme) | 400 | line-height 1.6667; caption lead-ins "Figure 1." bold |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Content images, video iframes | 0 (Google Sites default, inferred) |
| Site chrome buttons | 4px, 9999px (Material components) |

- **Shadows:** only Google Sites chrome uses Material elevation (e.g. `0 1px 3px 0 rgba(60,64,67,.3), 0 4px 8px 3px rgba(60,64,67,.15)`); content blocks have none.
- **Layout:** Google Sites 12-column grid with full-width text blocks and centered paragraphs; embedded Drive videos sized by the editor (common max widths 720px and 444px in the theme CSS).

## Components

- **Hand-styled header.** Centered h1 lines in bold black Times New Roman, then the green venue line, green underlined authors separated by black commas and asterisks, a gray contribution note, and a centered row of bracketed links.
- **Bracket link.** `[Paper]`, `[Code]`, `[Dataset]`: Times New Roman 15pt bold underlined text inside an anchor with `color: inherit; text-decoration: none`, separated by gray spaces.
- **Maroon section title.** Bold Lato text colored `#980000`, used in place of a styled heading level.
- **Figure with caption.** Full-width image followed by a long justified caption whose "Figure N." and "(A)/(B)/(C)" labels are bold Lato.
- **Drive video embed.** Google Drive `/preview` iframe per video, captioned with the object name (Mug, Plate, TeaCup, WineGlass, Bowl, BeerBottle).

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Hand-styled serif header |
| Venue badge | Full venue line | Bold green text |
| Link buttons | Paper, Code, Dataset | Bracketed underlined text |
| Teaser | Figure 1 with (A)(B)(C) caption | |
| Abstract | Yes | 14pt |
| Video | "Video Presentation" | Drive iframe |
| Method figure | "Framework" (Figure 2) | |
| Benchmark | "Real-World Benchmark" (Figure 3) | |
| Results | Simulation figure, real-world affordance and manipulation videos | 6 Drive iframes |
| Tables / sliders / 3D / HF | No | |
| BibTeX | No | |
| Acknowledgements | No | Google Sites footer only |

## Do's and Don'ts

- Do keep the header serif and the section titles sans; the contrast is the page's signature.
- Do use exactly three accent hues: green for venue and authors, maroon for section titles, black for the title.
- Do write long, labeled figure captions.
- Don't rely on the theme teal `#226e93`; the authors overrode it everywhere it matters.
- Don't count the Google blue `#0b57d0` as a content color; it belongs to the Sites chrome.

## Surfaces

Plain white page from the Google Sites theme; no bands, cards or tinted blocks.

## Imagery

Robot bimanual assembly figures, point-cloud affordance maps, and real-robot videos hosted on Google Drive.

## Layout

Single centered column from the Google Sites grid; header centered, body paragraphs left or justified, videos stacked.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#212121`, title `#000000`, venue `#38761d`, authors `#6aa84f`, sections `#980000`, note `#4a4a4a`.

1. "Create a centered paper header: bold black Times New Roman title, a bold `#38761d` venue line, underlined `#6aa84f` author names with black commas, and a 15pt gray '(* denotes equal contribution)' note."
2. "Add a link row of bracketed text links '[Paper] [Code] [Dataset]' in Times New Roman 15pt bold underlined, separated by spaces."
3. "Style section titles as bold Lato in `#980000` above 11pt Lato `#212121` body text with line-height 1.6667."

## Similar Pages

Other robotics project pages built on Google Sites (common in the PKU Hao Dong group lineage); none of the Bulma or Tailwind pages in this collection share this look.

## Quick Start

```css
:root {
  --text: #212121; --title: #000000; --venue: #38761d; --author: #6aa84f;
  --section: #980000; --note: #4a4a4a; --bg: #ffffff;
  --font-header: "Times New Roman", "Tinos", serif;
  --font-body: "Lato", "Carlito", sans-serif;
  --fs-body: 11pt; --fs-abstract: 14pt; --fs-links: 15pt;
}
body { font-family: var(--font-body); font-size: var(--fs-body); line-height: 1.6667; color: var(--text); background: var(--bg); }
```

## Provenance

- **URL:** https://sites.google.com/view/biassembly/
- **Paper:** BiAssemble: Learning Collaborative Affordance for Bimanual Geometric Assembly (arXiv 2506.06221), Yan Shen, Ruihai Wu et al. (the page heading spells it "BiAssemble"; the URL uses "biassembly").
- **Venue:** ICML 2025 (venue line on the page).
- **Selection reason:** arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- **Template credit:** Google Sites (built-in theme); no academic template.
- **Measurement method:** `extract_style.py` on the static HTML, then manual tally of inline span styles; the large `--gm3-*` / `--ws-sys-*` variable sets are Google system tokens and were excluded. Rendered page not viewed, so final title size at each breakpoint is inferred from the theme CSS.
