# TapSampling Quiet Navy — Style Reference

> A product launch page for a robot policy, typeset like a calm keynote slide.

**Theme:** light

Values are read from the page's single hand-written stylesheet (`static/css/index.css`), which declares its tokens on `:root`. Measurements are normalized (rem kept where the CSS uses rem) and roles are interpreted from usage. No framework is loaded.

## Overview

TapSampling is a custom, framework-free project page with a sticky frosted header (brand at left, centered anchor nav, "Preview / EN" at right), a very large centered display title, and content set in rounded white cards on an off-white `#fbfbfb` page. The palette is nearly monochrome: near-black text `#1e1e1e`, gray `#6a6a6a` for everything secondary, and one navy accent `#12487e` used for the first half of the title, the small vertical bar before method headings, and the table header tint. Link buttons are soft lavender-white pills. The overall feeling is a modern SaaS landing page applied to a paper: generous 120px section gaps, 28px card radius, a whisper of shadow.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Harbor Navy | `#12487e` | `--accent` | Title accent span ("Tap"), method-heading bar, table header tint base |
| Navy Mist | `#eff1f9` | `--accent-soft` | Results-table header background |
| Fog Page | `#fbfbfb` | `--bg` | Page background; media letterbox |
| Card White | `#ffffff` | `--surface` | Cards, tables, citation block |
| Lavender Pill | `#f5f6ff` | `--surface-soft` | Link-button fill (`.pill-button-static`) |
| Pill Hover | `#e7edf5` | (literal) | Pill hover fill |
| Graphite Ink | `#1e1e1e` | `--text` | Body text, headings |
| Hover Ink | `#101010` | (literal) | Pill text on hover |
| Pencil Gray | `#6a6a6a` | `--muted` | Nav, kicker, subtitle, authors, captions, paragraphs in cards |
| Hairline | `#e8e8e8` | `--line` | Card borders, table row rules |
| Strong Line | `rgba(0,0,0,0.12)` | `--line-strong` | Pill and table-wrapper borders |
| Gain Green | `#1f7a3f` | (literal) | `.gain-score` improvement deltas in the results table |
| Ours Wash | `rgba(27,44,197,0.06)` | (literal) | Highlight for "ours" rows |
| Variant Wash | `rgba(18,72,126,0.035)` | (literal) | Variant rows |
| Ablation Rose | `rgba(180,44,44,0.08)` | (literal) | "No co-train" rows (defined; not confirmed in use) |
| Section Rule | `#a3a7ad` | (literal) | 2px top border at table group starts |
| Video Black | `#111111` | (literal) | Background behind grid videos |

Note: `.tapsampling-row td` sets a saturated `rgba(60,122,247,0.9)`, but those rows also carry `.ours-row`, whose rule has equal specificity and comes later, so the pale `rgba(27,44,197,0.06)` wash wins (inferred from cascade order; not confirmed in a render).

## Tokens — Typography

- **Sans (everything):** `"Segoe UI", "PingFang SC", "Noto Sans SC", sans-serif`. No web font is loaded, so the page renders in the OS UI face. Substitute: Inter, system-ui.
- **Mono:** `"SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace` for BibTeX.
- Weights in use: 400, 500 (kicker), 600 (brand, venue), 700 (title).

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Hero title | `clamp(3.0rem, 7vw, 5.0rem)` | 700 | 1 | letter-spacing -0.03em; two-color split |
| Hero subtitle | `clamp(1.15rem, 2vw, 1.65rem)` | 400 | 1.45 | muted, max 860px |
| Venue line | 1.5rem | 600 | | "ICML 2026", ink color |
| Section h2 | `clamp(1.8rem, 3.6vw, 3rem)` | 700 (UA default) | 1.1 | -0.03em, centered |
| Method h3 | 1.4rem | UA bold | 1.3 | 4px navy bar before |
| Body / captions | 1rem | 400 | 1.7 | muted |
| Kicker, nav, pills | 0.98rem | 500 / 400 | | |
| Table cells | 0.96rem | 400 | | header also 400 |
| BibTeX | 0.94rem mono | 400 | 1.75 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Cards, method figure, citation (`--radius-xl`) | 28px |
| Table wrapper (`--radius-lg`) | 20px |
| Grid videos (`--radius-md`) | 16px |
| Pill buttons, accent bar | 999px |

- **Shadows:** `--shadow: 0 2px 10px rgba(0,0,0,0.05)` on every card; the table wrapper alone gets the deeper `0 12px 28px rgba(0,0,0,0.06)`.
- **Spacing:** page padding 84px top / 120px bottom, 24px sides (18px under 640px); `.section-block` margin-top 120px (92px on phones); section heading margin-bottom 38px; card padding 28px; button gap 16px.
- **Widths:** `--content-width` 1248px; hero copy 980px; text card, caption and citation 880px; section heading and subtitle 860px; single media card fixed 640px.

## Components

- **Sticky header.** `rgba(251,251,251,0.92)` with `backdrop-filter: blur(12px)` and a 1px `rgba(0,0,0,0.04)` bottom rule; three-column grid (brand / nav / meta), padding 24px 24px 18px. Nav links 0.98rem gray, 34px gap, hover to ink.
- **Pill button.** Inline-flex, min-height 42px, padding 0 20px 0 18px with an 18px SVG icon and 10px gap, 1px `rgba(0,0,0,0.12)` border, 999px radius, `#f5f6ff` fill, ink text 0.98rem. Hover: `#e7edf5` fill, `rgba(0,0,0,0.18)` border. Full width under 640px.
- **Text card.** White, 1px `#e8e8e8` border, 28px radius, soft shadow, 28px padding, muted 1rem/1.7 paragraphs. Used for the abstract.
- **Method shell.** Two-column grid `760px 550px`, 28px gap: figure card on the left, stacked `.method-item` cards on the right, each h3 preceded by a 4px x 1.1em navy rounded bar.
- **Results table.** Inside a 20px-radius bordered wrapper with horizontal scroll; min-width 920px; cells 0.9rem x 1rem padding, `#e8e8e8` row rules; header rows tinted `rgba(18,72,126,0.12)`; group starts get a 2px `#a3a7ad` top rule; gains in `#1f7a3f`; best scores marked by class, second-best underlined 2px.
- **Citation card.** White card, 22px padding, 880px max, mono 0.94rem/1.75 pre.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered; kicker "TapSampling Research", two-color display title, muted subtitle, venue line, underlined author links (1.5px, 0.14em offset), affiliations and notes as wrapped flex rows |
| Venue badge | Text line "ICML 2026" | 1.5rem/600 ink, no chip |
| Link buttons | Paper, Code, Model | Lavender pills with SVG icons |
| Teaser | Single 640px media card | Image with centered muted figcaption |
| Abstract | Yes | Text card |
| Method figure | Yes | "Framework" with Action Sampling / Action Verification cards |
| Results | One performance table | See above |
| Videos / sliders / 3D / HF demo | No | 0 video elements in static HTML |
| BibTeX | Yes | Citation card |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep navy to three places: title accent, method bar, table header tint.
- Do put every content block in a 28px-radius white card on the `#fbfbfb` page.
- Do use gray `#6a6a6a` for all secondary text, including the abstract.
- Don't add a web font; the look depends on the native UI face.
- Don't use dark buttons; links are pale pills with hairline borders.

## Surfaces

Off-white page, white cards, one frosted sticky header. No alternating bands, no dark sections.

## Imagery

Three images (teaser, overview figure, one more), shown contained on the page color with no cropping.

## Layout

Single 1248px column, centered hero, centered section titles. The method area is the only two-column layout and collapses to two equal columns under 1080px and one column under 820px.

## Agent Prompt Guide

**Quick colors:** page `#fbfbfb`, card `#ffffff`, ink `#1e1e1e`, muted `#6a6a6a`, line `#e8e8e8`, accent `#12487e`, pill `#f5f6ff`, gain `#1f7a3f`.

1. "Build a centered hero: 0.98rem/500 gray kicker, a `clamp(3rem,7vw,5rem)` 700 title with letter-spacing -0.03em whose first word is `#12487e`, a muted subtitle up to 860px, and a 1.5rem/600 venue line."
2. "Make pill link buttons: min-height 42px, 999px radius, `#f5f6ff` fill, 1px `rgba(0,0,0,0.12)` border, 18px icon plus label at 0.98rem; hover fill `#e7edf5`."
3. "Create a method card: white, 1px `#e8e8e8` border, 28px radius, shadow `0 2px 10px rgba(0,0,0,0.05)`, 19px padding; the h3 has a 4px navy pill bar at its left."

## Similar Pages

Other framework-free 2026 pages with tokenized `:root` palettes, such as ReMind in this collection; the pill-button plus rounded-card look also resembles Apple-style product pages.

## Quick Start

```css
:root {
  --bg: #fbfbfb; --surface: #ffffff; --surface-soft: #f5f6ff;
  --text: #1e1e1e; --muted: #6a6a6a; --line: #e8e8e8;
  --line-strong: rgba(0,0,0,0.12); --accent: #12487e; --accent-soft: #eff1f9;
  --gain: #1f7a3f;
  --shadow: 0 2px 10px rgba(0,0,0,0.05);
  --radius-xl: 28px; --radius-lg: 20px; --radius-md: 16px;
  --content-width: 1248px;
  --font-sans: "Segoe UI", "PingFang SC", "Noto Sans SC", system-ui, sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}
body { background: var(--bg); color: var(--text); font-family: var(--font-sans); line-height: 1.6; }
```

## Provenance

- **URL:** https://aipixel.github.io/TapSampling/
- **Paper:** TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robot Manipulation (arXiv 2605.25547), Sizhe Zhao et al.
- **Venue:** ICML 2026 (shown on the page as "ICML 2026").
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit:** none stated; hand-written HTML/CSS. The `<title>` reads "TapSampling | Homepage Preview" and the header says "Preview / EN", so the page may still be marked as a preview build.
- **Measurement method:** static HTML and `index.css` parsed with `extract_style.py` and read by hand; tokens come straight from `:root`. Rendered page not viewed, so the row-highlight cascade and final title weights are not visually confirmed.
