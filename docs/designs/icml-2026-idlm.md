# IDLM — Style Reference

> Plain-paper notebook with shields.io badges and a muted lavender frame.

**Theme:** light

Measurements are normalized from static HTML and the page's single stylesheet `styles.css` (about 6 KB, no framework) and roles are interpreted from selectors and one rendered look. All hex values below are declared in that file or in the shields.io badge URLs.

## Overview

IDLM is a compact custom page that keeps Nerfies' fonts (Google Sans, Noto Sans, Castoro loaded) but drops Bulma. The hero opens with a muted grey "ICML 2026" line above a very large black title (up to 3.75rem). Authors are steel-blue `#24588f` links. Instead of pill buttons the link row is five shields.io badges (Blog Post, arXiv number, Hugging Face Models, GitHub Code, YouTube Recording), 28px tall. A 1.42rem tagline states the speed-up in bold. The teaser figure sits in a white frame with a thin lavender border `rgba(148,102,168,.25)` and a soft purple-black shadow. Body text is 18px Noto Sans at 1.62 line height.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--paper` | Page background, figure frame |
| Wash | `#f5f5f5` | `--wash` | `.section.light` bands |
| Code Grey | `#f7f7f7` | — | BibTeX `pre` |
| Charcoal | `#262626` | `--text` | Body text |
| Title Black | `#141414` | — | `h1` |
| Author Ink | `#252525` | `--button` | Author names, button color token |
| Muted Slate | `#5d6470` | `--muted` | Venue line, separators |
| Line Grey | `#d8dce2` | `--line` | `pre` border |
| Copy Border | `#c7cbd1` | — | Copy button border |
| Link Blue | `#2b5d9b` | `--link` | Links; Blog badge color |
| Author Blue | `#24588f` | — | Author links |
| Tagline Ink | `#2c3137` | — | Tagline text |
| Callout Ink | `#252f3a` | — | Speed callout |
| Lavender | `#9466a8` | `--accent` | Accent token; frame border at 22–25% alpha |
| Lavender Wash | `#f4edf7` | `--soft-accent` | Soft accent token |
| Ochre | `#d29a2e` | `--gold` | Declared accent (sparse) |
| arXiv Red | `#b31b1b` | badge | arXiv badge |
| HF Yellow | `#ffcc4d` | badge | Hugging Face badge |
| GitHub Black | `#181717` | badge | GitHub badge |

## Tokens — Typography

- **Body family:** `"Noto Sans", "Google Sans", Arial, sans-serif`. Substitute: Open Sans.
- **Heading family:** `"Google Sans", "Noto Sans", Arial, sans-serif`. Substitute: Inter.
- **Mono:** `"SFMono-Regular", Consolas, "Liberation Mono", monospace`.
- **Weights:** 700 title, h2, copy button; 600 callout; 500 venue and author links.

| Level | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| Title (`h1`) | clamp(2.2rem, 4.3vw, 3.75rem) (2.08rem mobile) | 700 | 1.12 | `#141414`, max 940px |
| Venue (`.venue`) | 1.55rem | 500 | — | Muted slate |
| Section (`h2`) | 1.82rem | 700 | — | Centered |
| Tagline | 1.42rem (1.18rem mobile) | 400 | 1.45 | Max 840px |
| Speed callout | 1.16rem | 600 | 1.5 | Centered, max 820px |
| Authors | 1.1rem (0.96rem mobile) | 500 links | — | Comma separators via `::after` |
| Body | 18px (16px mobile) | 400 | 1.62 | — |
| Copy button | 0.9rem | 700 | — | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Teaser frame, `pre` | 8px |
| Copy button | 5px |
| Shields badges | 3px (shields.io default, inferred) |

- **Shadows:** teaser `0 16px 36px rgba(27,20,36,.08)`.
- **Widths:** `--max-width: 980px`, `--narrow-width: 820px`; title and authors 940px.
- **Spacing:** hero padding 54px 0 28px (38px top on mobile); teaser 22px 0 38px; badge row gap 10px.

## Components

- **Badge link** (`.shield-link`): inline-flex, min-height 42px, image height 28px. Badges: Blog Post (`#2b5d9b`), arXiv 2602.19066 (`#b31b1b`), 🤗 Hugging Face Models (`#ffcc4d`), GitHub Code (`#181717`), YouTube Recording (red).
- **Venue line:** muted, 1.55rem/500, above the title.
- **Teaser frame:** white image with 1px `rgba(148,102,168,.25)` border, 8px radius, soft shadow.
- **Innovation list:** ordered grid list, gap 18px, left padding 1.35rem.
- **Speed callout:** centered bold sentence under the generation comparison.
- **BibTeX:** `pre` on `#f7f7f7`, 1px `#d8dce2`, 8px radius, 20px padding; copy button white with `#c7cbd1` border, 5px radius.

## Page Modules

- **Title/author block:** venue line, title, eight authors with markers, affiliations (MBZUAI, AIRI, AXXX, EPITA) and equal-contribution note.
- **Venue badge:** "ICML 2026" text above the title.
- **Link buttons:** five shields.io badges including a YouTube recording.
- **Tagline:** one-sentence summary with bold "4x–64x".
- **Teaser:** method diagram in a lavender-bordered frame.
- **Key Innovations** list, **Abstract**, **Text Generation: DLM vs. IDLM** comparison figure with speed callout.
- **BibTeX** with copy button.
- **Not present:** comparison slider, 3D viewer, HF Space embed, results tables, acknowledgements.

## Do's and Don'ts

- Do put the venue above the title in muted grey.
- Do use shields.io badges with each service's own color for links.
- Do frame the teaser with a faint lavender border and soft shadow.
- Don't add colored backgrounds; only `#f5f5f5` light sections.
- Don't use the lavender accent at full strength for text.
- Don't mix pill buttons with badges in the same row.

## Surfaces

White page, occasional `#f5f5f5` sections, framed teaser and `#f7f7f7` code block.

## Imagery

Hand-drawn-style method diagram with emoji check/cross marks, histogram sketches, side-by-side generated text samples.

## Layout

Centered 980px column, narrower 820px blocks for tagline and callouts.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#262626`, title `#141414`, muted `#5d6470`, link `#2b5d9b`, author `#24588f`, line `#d8dce2`, accent `#9466a8`.

1. "Build a hero with a muted `#5d6470` 1.55rem venue line above a 700-weight title at clamp(2.2rem,4.3vw,3.75rem) in `#141414`, then Noto Sans authors in `#24588f`."
2. "Make a centered row of shields.io badges (28px tall, gap 10px): Blog Post `#2b5d9b`, arXiv `#b31b1b`, Hugging Face `#ffcc4d`, GitHub `#181717`, YouTube red."
3. "Frame the teaser image in white with a 1px `rgba(148,102,168,.25)` border, 8px radius and shadow `0 16px 36px rgba(27,20,36,.08)`."

## Similar Pages

d2 in this batch (same research area, Nerfies template); DynaTok (another framework-free page with a token block).

## Quick Start

```css
:root {
  --text: #262626;
  --muted: #5d6470;
  --line: #d8dce2;
  --paper: #ffffff;
  --wash: #f5f5f5;
  --button: #252525;
  --button-hover: #111111;
  --link: #2b5d9b;
  --accent: #9466a8;
  --soft-accent: #f4edf7;
  --gold: #d29a2e;
  --max-width: 980px;
  --narrow-width: 820px;
  --font-body: "Noto Sans", "Google Sans", Arial, sans-serif;
  --font-head: "Google Sans", "Noto Sans", Arial, sans-serif;
}
```

## Provenance

- **URL:** https://david-cripto.github.io/idlm-project-page/
- **Paper:** IDLM: Inverse-distilled Diffusion Language Models (arXiv 2602.19066), David Li et al.
- **Venue:** ICML 2026, stated on the page and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links the project page.
- **Template credit:** none found; custom stylesheet using Nerfies' font trio.
- **Measurement method:** `extract_style.py` counts, reading of `styles.css` and badge URLs, one rendered screenshot. Badge corner radius is the shields.io default, inferred.
