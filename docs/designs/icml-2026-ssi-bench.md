# SSI-Bench — Style Reference

> Tsinghua purple frosted glass over a lilac-grey benchmark console.

**Theme:** light

Measurements are normalized from static HTML and the page's single stylesheet `assets/styles.css` (about 29 KB, no framework) and roles are interpreted from selectors and one rendered look. Most colors are declared as alpha values on two base hues: a purple-black `rgb(45,21,56)` for lines and `rgb(25,18,36)` for shadows.

## Overview

SSI-Bench is a benchmark site rather than a paper page. A sticky translucent nav (blur 12px) carries the wordmark and Dataset / Leaderboard / Analysis links separated by hairline rules. The hero centers a geometric logo with a soft drop shadow, a heavy Inter title (weight 780), a long author list, "Tsinghua University" and "International Conference on Machine Learning (ICML), 2026" in Tsinghua purple, and four small pill resource links (Paper, Dataset, GitHub, arXiv). Below, sections switch to slightly different lilac-grey backgrounds and present a dataset viewer, a sortable leaderboard with category legend swatches, and analysis cards that lift 6px on hover. Everything uses translucent white panels with purple-tinted borders.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Lilac Mist | `#f7f6fb` | `--bg` | Page and hero background |
| Viewer Lavender | `#f3f0fa` | `--bgViewer` | Dataset viewer section |
| Board Haze | `#f6f5fb` | `--bgLeaderboard` | Leaderboard section |
| Frost Panel | `rgba(255,255,255,0.78)` | `--surface` | Panels, cards |
| Frost Soft | `rgba(255,255,255,0.6)` | `--surfaceSoft` | Ghost buttons, card gradients |
| Plum Line | `rgba(45,21,56,0.14)` | `--border` | Default borders |
| Plum Line Strong | `rgba(45,21,56,0.22)` | `--borderStrong` | Tabs, emphasized borders |
| Night Ink | `rgba(17,14,26,0.92)` | `--text` | Body text |
| Night Muted | `rgba(17,14,26,0.62)` | `--muted` | Secondary text (22 `.muted` uses) |
| Tsinghua Purple | `#82318e` | `--brand` | Brand, active tab gradient, venue |
| Resource Plum | `rgb(102,8,116)` | — | Hero resource pill text |
| Wisteria | `#a889d6` | `--brand2` | Brand gradient end |
| Brand Ring | `rgba(130,49,142,0.22)` | `--brandRing` | Hover borders, pill borders |
| Rose Alert | `#e34a6f` | `--danger` | Negative values |
| Jade OK | `#1aa37a` | `--ok` | Positive values |
| Proprietary Blush | `rgba(255,233,238,0.95)` | — | Leaderboard swatch, proprietary rows |
| Open Ice | `rgba(233,242,255,0.98)` | — | Leaderboard swatch, open-source rows |
| Baseline Cream | `rgba(255,248,224,0.98)` | — | Leaderboard swatch, baseline rows |

## Tokens — Typography

- **Family:** Inter (Google Fonts) for both `--sans` and `--display`, falling back to system UI (Segoe UI Variable Text/Display). Substitute: system-ui.
- **Mono:** `ui-monospace, SFMono-Regular, Menlo, …` for code and numbers.
- **Weights:** 780 title, 750/800 headings and figures, 650 pills, 600 buttons, 400 body.

| Level | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| Hero title | clamp(28px, 3vw, 42px) | 780 | 1.1 | −0.02em |
| Section title (`h2`) | clamp(24px, 2.4vw, 32px) | 750–800 (inferred) | 1.15 | Centered |
| Subsection (`h3`) | clamp(18px, 2vw, 24px) | 700 | — | — |
| Body | 15px | 400 | 1.65 | letter-spacing 0.1px |
| Table cells, meta | 13px | 400–600 | — | 11 uses of 13px |
| Resource pill | 13px | 650 | 1 | `rgb(102,8,116)` |
| Code | 0.95em | 400 | — | Plum-tinted background |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Panels, analysis figures | 16px (`--radius`) |
| Buttons, tabs, table wrap | 12px |
| Cards | 14px |
| Resource pills, legend items | 999px |
| Legend swatches | 4px |

- **Shadows:** `--shadow 0 18px 70px rgba(25,18,36,.12)`; `--shadowSm 0 10px 32px rgba(25,18,36,.1)`; figures `0 16px 44px rgba(25,18,36,.1)`; hover `0 26px 90px rgba(25,18,36,.16)`.
- **Text measures:** 76–80ch for paragraphs, 35ch for narrow captions.
- **Motion:** 140ms transforms; panels lift −6px on hover.

## Components

- **Sticky nav:** `rgba(244,245,247,.74)` with `backdrop-filter: blur(12px)`, bottom hairline, links separated by 1px × 16px plum rules.
- **Resource pill** (`.heroResource`): white 72%, 1px brand ring, pill, 8px 12px, icon + 13px/650 label, shadow `0 10px 26px rgba(25,18,36,.08)`.
- **Button:** 1px plum border, 12px radius, 10px 12px, white 74%; ghost variant 60%.
- **Leaderboard tab:** white 86%, 12px radius, padding 10px 18px; active fills with `--brandGrad` (`#82318e → #a889d6`) and white text.
- **Leaderboard table:** wrap with 1px border and 12px radius; header `rgba(244,245,247,.72)`; group headers tinted blue `rgba(80,120,190,.12)` or green `rgba(70,160,120,.12)`; row backgrounds by model category.
- **Analysis card / panel:** translucent white gradient, radial purple glow in panels, lift on hover.

## Page Modules

- **Title/author block:** logo, title, 15+ authors with linked and unlinked names (`author--link`, `author--nolink`), affiliation.
- **Venue badge:** text line "International Conference on Machine Learning (ICML), 2026" in brand purple.
- **Link buttons:** Paper, Dataset, GitHub, arXiv pills.
- **Dataset section:** Overview figure, interactive Dataset Viewer, Construction Pipeline.
- **Leaderboard:** JS-rendered sortable table with category legend and tabs ("Loading leaderboard…" placeholder in static HTML).
- **Analysis:** Key Results, Impact of Thinking, Error Analysis cards with figures.
- **Not present:** BibTeX block (none in static HTML), video, 3D viewer, HF Space, acknowledgements.

## Do's and Don'ts

- Do derive every border and shadow from the plum base hues with alpha.
- Do reserve solid Tsinghua purple for the brand gradient, venue and active states.
- Do keep panels translucent over the lilac background.
- Don't introduce pure black text; use `rgba(17,14,26,.92)`.
- Don't use more than three category tints in the leaderboard.
- Don't omit a BibTeX block on a benchmark page; it is missing here.

## Surfaces

Three background tones (`#f7f6fb`, `#f3f0fa`, `#f6f5fb`) switch by section; translucent white panels with plum hairlines and wide soft shadows; radial purple glow behind the analysis section.

## Imagery

Geometric line logo, task taxonomy diagrams, sample images from constraint-governed spatial puzzles, result plots.

## Layout

Sticky nav, centered hero, then full-width sections with centered headers and grid layouts (overview grid collapses to one column under 900px).

## Agent Prompt Guide

**Quick colors:** bg `#f7f6fb`, panel `rgba(255,255,255,.78)`, border `rgba(45,21,56,.14)`, text `rgba(17,14,26,.92)`, muted `rgba(17,14,26,.62)`, brand `#82318e`, brand2 `#a889d6`, danger `#e34a6f`, ok `#1aa37a`.

1. "Build a sticky translucent nav: `rgba(244,245,247,.74)`, blur 12px, bottom hairline `rgba(45,21,56,.12)`, Inter links separated by thin vertical rules."
2. "Make resource pills: white 72%, 1px `rgba(130,49,142,.22)` border, 999px radius, 13px/650 Inter label in `rgb(102,8,116)` with an icon, shadow `0 10px 26px rgba(25,18,36,.08)`."
3. "Create leaderboard tabs: white 86%, 12px radius, padding 10px 18px; active tab uses `linear-gradient(135deg, rgba(130,49,142,.98), rgba(168,137,214,.88))` with white text."

## Similar Pages

Benchmark landing sites with leaderboards and dataset viewers; compare Thinking-in-Structures with other leaderboard-first pages rather than Nerfies-style paper pages.

## Quick Start

```css
:root {
  --bg: #f7f6fb;
  --bgViewer: #f3f0fa;
  --bgLeaderboard: #f6f5fb;
  --surface: rgba(255, 255, 255, 0.78);
  --surfaceSoft: rgba(255, 255, 255, 0.6);
  --border: rgba(45, 21, 56, 0.14);
  --borderStrong: rgba(45, 21, 56, 0.22);
  --text: rgba(17, 14, 26, 0.92);
  --muted: rgba(17, 14, 26, 0.62);
  --brand: #82318e;
  --brand2: #a889d6;
  --brandGrad: linear-gradient(135deg, rgba(130,49,142,.98), rgba(168,137,214,.88));
  --danger: #e34a6f;
  --ok: #1aa37a;
  --shadow: 0 18px 70px rgba(25, 18, 36, 0.12);
  --radius: 16px;
  --sans: "Inter", ui-sans-serif, system-ui, sans-serif;
}
```

## Provenance

- **URL:** https://ssi-bench.github.io/
- **Paper:** Thinking in Structures: Evaluating Spatial Intelligence in Constraint-Governed Spaces (arXiv 2602.07864), Chen Yang et al., Tsinghua University.
- **Venue:** ICML 2026, stated on the page and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links the project page.
- **Template credit:** none found; custom stylesheet (comment in CSS names the "Tsinghua purple" color system).
- **Measurement method:** `extract_style.py` counts, reading of `assets/styles.css` `:root` and component rules, one rendered screenshot. The leaderboard is JS-rendered and was not inspected in its loaded state; `h2` weight is inferred.
