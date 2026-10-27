# PRMBench · Pastel Leaderboard Ledger — Style Reference

> A grey-ruled scorebook with three faint highlighter colors for model families.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9, stock Nerfies `index.css`, plus `leaderboard.css`, `prmbench_leaderboard.css` and `image_carousel.css`); roles are interpreted from markup and one rendered viewport. Bulma palette colors in the frequency scan are listed only where used.

## Overview

PRMBench follows the MathVista lineage of Nerfies pages: a top navbar with a "More Research" dropdown, a centered Google Sans title, sky-blue authors, the venue "ACL 2025 Main" in plain red, and six dark pill buttons. The overview figure comes first, then a YouTube tutorial, then two sortable leaderboards whose rows are tinted by model family (PRMs pale blue, proprietary LLMs pale yellow, open LLMs pale green). Grey header rows, 17px table text and bold/underlined best scores make the leaderboard the visual center.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Bulma Ink | `#363636` | `--text-heading` | Titles; dark pill fill |
| Body Grey | `#4a4a4a` | `--text` | Body text |
| Author Sky | `#209cee` | `--link-author` | Author links (`hsl(204,86%,53%)`) |
| Venue Signal Red | `red` (`#ff0000`) | `--venue` | "ACL 2025 Main" inline color |
| Header Ash | `#e6e6e6` | `--th-top` | First header row, reset cell |
| Header Smoke | `#f2f2f2` | `--th-sub` | Second header row |
| Rule Grey | `#dddddd` | `--border` | Table border, header bottom borders |
| Row Rule | `#eeeeee` | `--row-rule` | Row separators |
| PRM Tint | `rgba(174,214,241,0.2)` | `--row-prm` | PRM rows |
| Proprietary Tint | `rgba(255,208,80,0.1)` | `--row-closed` | Proprietary LLM rows |
| Open Tint | `rgba(170,230,170,0.2)` | `--row-open` | Open LLM rows |
| Score Red | `#e74c3c` | `--score-red` | Red bold numbers |
| Table Link | `#007bff` | `--ext-link` | Links inside the table |
| Analysis Highlights | `rgb(201,229,221)`, `rgb(255,243,213)`, `rgb(211,209,209)`, `rgb(224,146,124)`, `rgb(126,176,149)` | `--hl-*` | Inline highlighter spans in analysis text |

## Tokens — Typography

- **Display:** Google Sans (title, authors), loaded from the Google Fonts family set "Google Sans | Noto Sans | Castoro".
- **Body:** Noto Sans (declared in `prmbench_leaderboard.css`).
- **Table:** 17px, 14px under 768px.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem | 600 | 1.125 |
| Section heading (`title is-3`) | 2rem | 600 | 1.125 |
| Leaderboard cells | 17px | 400; best score 700; second best underlined | 1.5 |
| Family label | .9em | 700 | — |
| Sort arrows | .8em superscript ▲ ▼ | — | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px pill |
| Family labels | 3px |
| Carousel images | 8px |
| Carousel dots | 50% |
| Table | 0 |

Cell padding 8px; table min-width 800px inside a horizontally scrolling wrapper. Shadows: carousel `rgba(0,0,0,0.1)` soft shadows. Container `is-max-desktop` (960px), leaderboard can be `is-fullwidth`; a few blocks capped at 800px.

## Components

- **Navbar:** Bulma navbar with home icon and "More Research" hoverable dropdown.
- **Pill buttons:** `is-dark is-rounded`, six of them with icons.
- **Family legend:** three inline labels ("PRMs", "Proprietary LLMs", "Open LLMs") in the same tints as the rows, 4px 10px padding, radius 3px.
- **Sortable leaderboard:** two-row header (`#e6e6e6` over `#f2f2f2`), clickable column groups (Simplicity, Soundness, Sensitivity), cell hover `#f5f5f5`.
- **Example carousel:** custom image carousel with `#f8f8f8` frame, 8px radius, round dots.

## Page Modules

- **Title/author block:** centered title, sky-blue authors with numbered affiliations (Fudan, Soochow, Shanghai AI Lab, Stony Brook, CUHK).
- **Venue badge:** red text line "ACL 2025 Main".
- **Link buttons:** Paper, arXiv, Code, Dataset, Documentation, Bilibili.
- **Teaser:** overview figure with long caption as an `h2`-styled block.
- **Video:** "Tutorial Video" YouTube iframe (Nerfies `.publication-video`, 10px radius).
- **Results tables:** "Leaderboard on PRMBench" and "Leaderboard on PRMBench-STEM".
- **Analysis:** "Analysis and Takeaways" with colored highlight spans; "Detailed Classifications"; "Examples" carousel.
- **Abstract:** placed near the end, after examples.
- **BibTeX:** present.
- **Footer:** adapted from Nerfies and MathVista, CC BY-SA 4.0.

## Do's and Don'ts

- Do tint whole rows by model family and repeat the tints in a legend.
- Do mark best with bold and second best with underline, not color.
- Don't give the table rounded corners or shadow; it is a flat ruled ledger.
- Don't move the venue into a pill; it stays as a red text line.

## Surfaces

White page; the leaderboard is the only dense surface, with grey header strata.

## Imagery

Overview figure with radar chart, an embedded tutorial video, example screenshots in a carousel.

## Layout

960px main column; leaderboards may run full width with horizontal scroll. Abstract sits late in the page order.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, header rows `#e6e6e6`/`#f2f2f2`, rules `#ddd`/`#eee`, PRM `rgba(174,214,241,.2)`, closed `rgba(255,208,80,.1)`, open `rgba(170,230,170,.2)`.

1. "Build a leaderboard: collapsed borders `1px solid #ddd`, 17px text, 8px padding, top header `#e6e6e6` centered bold, second header `#f2f2f2` with 2px bottom border, rows tinted by family."
2. "Build a family legend: three inline labels, padding 4px 10px, radius 3px, bold .9em `#333` text, backgrounds matching the row tints."
3. "Build the header: Google Sans title 3rem, sky-blue authors `#209cee`, a red 'ACL 2025 Main' line, six dark pill buttons."

## Similar Pages

MathVista project page (stated source); TUNA in this batch (same MathVista/Video-MME lineage).

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #4a4a4a; --heading: #363636;
  --author: #209cee; --venue: red;
  --th-top: #e6e6e6; --th-sub: #f2f2f2; --border: #ddd; --row-rule: #eee;
  --row-prm: rgba(174,214,241,.2); --row-closed: rgba(255,208,80,.1); --row-open: rgba(170,230,170,.2);
  --radius-pill: 290486px;
  --font-display: 'Google Sans', sans-serif; --font-body: 'Noto Sans', sans-serif;
  --max-width: 960px;
}
```

## Provenance

- **URL:** https://prmbench.github.io/
- **Paper:** PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv 2501.03124), Mingyang Song et al.
- **Venue:** ACL 2025 (main).
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and links this page.
- **Template credit:** footer says the site is adapted from Nerfies and MathVista, CC BY-SA 4.0.
- **Measurement method:** extract_style.py scan, manual reading of three custom CSS files and inline styles, one rendered viewport. `leaderboard.css` also defines a `#dee` sort highlight and a `--UCLA-darkblue` header variable that is never defined; the PRMBench table uses the `prmbench_leaderboard.css` rules instead (inferred from table ids).
