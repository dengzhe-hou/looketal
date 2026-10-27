# AGSM — Style Reference

> Source Sans on white, with a red-to-blue gradient running through the title.

**Theme:** light

Measurements are normalized from static HTML and the page's single stylesheet `static/css/index.css?v=light-theme` (about 9 KB, no framework) and roles are interpreted from selectors and one rendered look. All hex values below are declared in that file.

## Overview

AGSM is a custom, framework-free page in a neutral zinc palette with one signature move: the words "Alignment-Guided Score Matching" are filled with a four-stop gradient (`#ff2626 → #ff8383 → #6f9dff → #3474ff`), red to blue, mirroring positive and negative guidance. The second title line is plain black. Below the authors, "ICML 2026 (Spotlight)" is set large in a saturated `#1b44e9`. Four outlined pill buttons (Paper, Code, Checkpoints, BibTeX) sit on a pale slate fill. Sections alternate white and `#f7f7f8`, titles are centered at clamp(1.9rem, 3vw, 2.7rem), and the TL;DR repeats the gradient on the word "AGSM". Method cards and equations use 8px radii and 1px zinc borders.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg-primary`, `--panel-bg` | Page, cards, table cells |
| Zinc Wash | `#f7f7f8` | `--bg-secondary` | `.section-alt` bands |
| Slate Fill | `#f1f5f9` | `--bg-tertiary` | Button fill |
| Zinc Panel | `#f4f4f5` | `--panel-bg-strong` | Strong panels |
| Equation Snow | `#f8fafc` | — | Equation boxes |
| Pure Black | `#000000` | `--text-primary` | Titles, body |
| Zinc 900 | `#18181b` | `--text-secondary` | `pre` text |
| Zinc 600 | `#52525b` | `--text-muted` | Captions, button hover border |
| Zinc Line | `#d4d4d8` | `--border-color` | Buttons, cards, table rules |
| Button Hover | `#e5e7eb` | — | Button hover fill |
| Ultramarine | `#1b44e9` | — | Venue line |
| Signal Red | `#ff2626` | `--accent-gradient` stop 1 | Gradient title start |
| Blush | `#ff8383` | stop 2 | Gradient |
| Cornflower | `#6f9dff` | stop 3 | Gradient |
| Azure | `#3474ff` | stop 4 | Gradient end |
| Sky Glow | `#60a5fa` | `--accent-primary` | Hero radial glow (14% alpha) |
| Periwinkle | `#818cf8` | `--accent-secondary` | Hero linear wash (5% alpha) |

## Tokens — Typography

- **Family:** Source Sans 3 (Google Fonts, weights 300–700), `--font-sans` with `-apple-system` fallback. Substitute: Source Sans Pro, Inter.
- **Mono:** JetBrains Mono (400/500) for BibTeX.
- **Weights:** 700 title and gradient text, 800 venue, 650 section titles, 600 buttons.

| Level | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| Paper title (`.publication-title`) | clamp(2.05rem, 4.45vw, 4rem) | 700 | 1.18 | Max 1280px; line 1 gradient |
| Title line 2 | clamp(1.7rem, 3.35vw, 2.75rem) (inferred pairing) | 700 | — | Black |
| Venue (`.venue`) | 1.5rem | 800 | — | 0.04em tracking, `#1b44e9` |
| Section title | clamp(1.9rem, 3vw, 2.7rem) | 650 | 1.22 | Centered |
| Subsection (`h3`) | clamp(1.35rem, 2vw, 1.75rem) | 600 | — | — |
| Body | about 1.05rem | 400 | 1.7 | — |
| Figure caption | 1rem | 400 | 1.55 | Zinc 600, centered, max 980px |
| Button | 1.04rem | 600 | — | — |
| Equation / `pre` | 0.96rem | 400 | 1.6 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons | 999px |
| Method cards, equations | 8px |
| Panels | 10px |
| Small chips | 4px |

- **Shadows:** none declared; depth comes from borders and section bands.
- **Containers:** `.container` max 1120px, padding 0 5%; `.container-wide` max 1500px, padding 0 4%; text blocks 920–1040px.
- **Hero:** padding 78px 0 38px (36px 0 32px on mobile); background `radial-gradient(ellipse 72% 44% at 50% -15%, rgba(96,165,250,.14), transparent)` over a 5% periwinkle linear wash.

## Components

- **Pill button** (`.btn`): min-height 48px, padding 11px 24px, 1px `#d4d4d8`, 999px, fill `#f1f5f9`, black 1.04rem/600, icon gap 9px; hover fill `#e5e7eb`, border `#52525b`, lift 1px. Full width on mobile.
- **Gradient text** (`.gradient-text`): `background-clip: text` with the four-stop accent gradient.
- **Venue line:** `#1b44e9`, 1.5rem/800, not uppercase.
- **Method card:** padding 22px, 1px zinc border, 8px radius, white.
- **Equation box:** flex-centered, `#f8fafc`, 1px zinc border, 8px radius, 18px padding, 0.96rem.
- **Results table:** cells padding 12px 14px, bottom rule `#d4d4d8`, right-aligned numbers.
- **BibTeX:** `pre` padding 24px, JetBrains Mono 0.96rem, `#18181b`.

## Page Modules

- **Title/author block:** two-line title, four authors (KAIST) with equal-contribution note.
- **Venue badge:** "ICML 2026 (Spotlight)" text in ultramarine.
- **Link buttons:** Paper, Code, Checkpoints, BibTeX.
- **TL;DR:** on the `#f7f7f8` band with gradient "AGSM".
- **Key Contributions:** four contribution items.
- **Method Overview:** two method cards ("From Contrastive Pushes to Score Guidance", "Dual Soft Tokens") with equations (math rendering).
- **Results:** Text-to-Image Generation, Text-Guided Image Editing, Complementary to Diffusion RL as media blocks with captions; results table styles present.
- **References** list and **BibTeX**.
- **Not present:** video, comparison slider, 3D viewer, HF Space demo.

## Do's and Don'ts

- Do confine the red-to-blue gradient to the method name.
- Do keep chrome in zinc neutrals and black text.
- Do use 8px radii for content boxes and full pills only for buttons.
- Don't add shadows; borders and band changes carry structure.
- Don't use the ultramarine venue color for links or buttons.
- Don't uppercase the venue (the rule is present but commented out).

## Surfaces

White and `#f7f7f8` bands alternate; content boxes are white or `#f8fafc` with 1px zinc borders. The hero has a faint blue radial glow at the top.

## Imagery

Large text-to-image sample grids, editing comparisons, method diagrams; images span the wide container (up to 1500px).

## Layout

Centered hero, then full-width bands, each with a centered section title and a constrained text or media block.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f7f7f8`, button fill `#f1f5f9`, border `#d4d4d8`, text `#000000`, muted `#52525b`, venue `#1b44e9`, gradient `#ff2626 → #ff8383 → #6f9dff → #3474ff`.

1. "Set a paper title in Source Sans 3 at clamp(2.05rem,4.45vw,4rem)/700 where the method name uses `background-clip:text` with `linear-gradient(135deg,#ff2626,#ff8383 33%,#6f9dff 66%,#3474ff)`."
2. "Make outlined pill buttons: min-height 48px, padding 11px 24px, 1px `#d4d4d8`, fill `#f1f5f9`, 600 weight; hover `#e5e7eb` with `#52525b` border."
3. "Create an equation box: centered flex, `#f8fafc`, 1px `#d4d4d8`, 8px radius, 18px padding, 0.96rem text, horizontal scroll on overflow."

## Similar Pages

Custom-CSS diffusion paper pages with gradient wordmarks; IDLM in this batch is another framework-free page with a single accent.

## Quick Start

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f7f7f8;
  --bg-tertiary: #f1f5f9;
  --text-primary: #000000;
  --text-secondary: #18181b;
  --text-muted: #52525b;
  --border-color: #d4d4d8;
  --accent-primary: #60a5fa;
  --accent-secondary: #818cf8;
  --accent-gradient: linear-gradient(135deg, #ff2626 0%, #ff8383 33%, #6f9dff 66%, #3474ff 100%);
  --venue: #1b44e9;
  --font-sans: "Source Sans 3", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}
```

## Provenance

- **URL:** https://jaayeon.github.io/AGSM/
- **Paper:** Alignment-Guided Score Matching for Text-to-Image Alignment in Diffusion Models (arXiv 2605.30038), Jaa-Yeon Lee et al., KAIST.
- **Venue:** ICML 2026. The page labels it "ICML 2026 (Spotlight)"; the batch metadata lists ICML 2026 without the Spotlight tag.
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links the project page.
- **Template credit:** none found; custom stylesheet.
- **Measurement method:** `extract_style.py` counts, reading of `index.css` rules, one rendered screenshot. Body font size and title line 2 size are inferred from rule pairing.
