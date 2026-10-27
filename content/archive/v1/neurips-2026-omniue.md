# OmniUE Midnight Gradient — Style Reference

> A product launch keynote slide, navy night sky fading into a cool slate page.

**Theme:** light (with a dark hero)

Values come from `static/css/index.css`, which overrides Bulma 0.9.4 almost completely. Bulma's own palette (`#485fc7`, `#00d1b2`, `#48c78e`) inflates the frequency counts but is not visible on the page. Roles are interpreted from markup. Rendered output was not viewed.

## Overview

OmniUE (Sony AI and Sony Group) reskins Bulma into a SaaS-style landing page. A dark hero (`#060a14` with three radial navy and cyan glows plus a 26px dot grid) holds a pill "NeurIPS 2026" badge with a glowing cyan dot, an 800-weight Inter title filled with a white-to-ice gradient, white author links underlined with translucent rules, and a gradient pill button. A white teaser card (22px radius, deep shadow) overlaps the hero edge by 2.5rem. Below, the page shifts to slate `#f8fafc` with alternating `#eef2f8` sections, gradient-dotted uppercase kickers, stat cards with a 3px gradient top bar, pipeline chips, example cards, and four results tables with navy headers and a highlighted "ours" row.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Night Base | `#060a14` | (literal) | Hero background under radial glows |
| Slate Page | `#f8fafc` | `--bg` | Page background below hero |
| Slate Band | `#eef2f8` | `--bg-soft` | Alternating sections, table group rows, footer |
| Deep Ink | `#0b1526` | `--ink` | Headings, primary text |
| Slate Ink | `#4a5872` | `--ink-soft` | Body paragraphs, captions |
| Faint Slate | `#8892a6` | `--ink-faint` | Table notes, footer text |
| Hairline | `#e2e7f0` | `--line` | Card borders, table rules, nav border |
| Card White | `#ffffff` | `--card` | Cards, teaser frame |
| Sony Navy | `#003366` | `--sony-blue`, `--violet` | Kickers, best scores, links |
| Signal Blue | `#0072ce` | `--violet-2` | Affiliation marks, selection tint |
| Ice Cyan | `#00b4d8` | `--cyan` | Badge dot, gradient end, hover |
| Abyss | `#001f3f` | `--pink`, gradient start | Gradient start, "ours" best values |
| Header Navy | `#071a3d` | (literal) | Results table `thead` |
| Ours Wash | `#eaf1fb` | (literal) | Highlighted "ours" row |
| Code Night | `#0a1830` | (literal) | BibTeX block background |
| Code Text | `#dbe7fb` | (literal) | BibTeX text |

**Gradients:** `--gradient: linear-gradient(120deg, #001f3f 0%, #003366 35%, #0072ce 70%, #00b4d8 100%)` for buttons, dots and stat bars; title text `linear-gradient(115deg, #ffffff 15%, #a9c8f2 45%, #7fe3ff 75%)`.

## Tokens — Typography

- **Family:** `Inter` (Google Fonts, 400–800), fallback Segoe UI, system.
- **Mono:** Bulma `monospace` / SF Mono for BibTeX.
- **Weights:** 800 for titles, headings, kickers and stat numbers; 700 for buttons and authors; 600 nav; 500 author line.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Hero title | `clamp(2.4rem, 5.5vw, 4rem)` (2.1rem ≤560px) | 800 | 1.06 | -0.035em, gradient text |
| Section h2 (`title is-3`) | `clamp(1.7rem, 3vw, 2.35rem)` | 800 | | -0.025em |
| Stat number | 2rem | 800 | | gradient text |
| Body (`has-text-justified`) | 1.06rem | 400 | 1.8 | max 820px |
| Authors | 1.02rem | 500 (links 700) | 1.8 | |
| Caption | 0.98rem | 400 | 1.65 | max 760px |
| Badge | 0.78rem | 700 | | uppercase, 0.04em |
| Kicker | 0.76rem | 800 | | uppercase, 0.14em |
| Table body / header | 0.85rem / 0.72rem | 400 / 700 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Teaser frame / inner image | 22px / 16px |
| Cards, figure frames, BibTeX (`--radius`) | 18px |
| Stat cards, figure images (`--radius-sm`) | 12px |
| Buttons, badge, pipeline chips, copy button | 999px |
| Carousel arrows, dots | 50% |

- **Shadows:** `--shadow-sm 0 2px 8px -2px rgb(11 21 38 / .06)`, `--shadow-md 0 12px 28px -10px rgb(11 21 38 / .14)`, `--shadow-lg 0 30px 60px -20px rgb(11 21 38 / .28)` (teaser). Primary button `0 14px 32px -10px rgba(0,51,102,.6)`.
- **Layout:** hero inner 880px; teaser frame 1080px; body text 820px; Bulma `container is-max-desktop` for sections.
- **Section rhythm:** `.section-tight` 5rem 1.5rem (3.4rem 1.1rem on mobile); hero 5.5rem 1.5rem 5rem.

## Components

- **Sticky frosted nav.** `rgba(249,250,252,.72)` with blur(16px), bottom hairline; brand item 800 weight with a 9px gradient dot.
- **Hero badge.** Pill, `rgba(255,255,255,.08)` fill, 1px `rgba(255,255,255,.16)` border, 7px cyan dot with glow.
- **Primary button.** Gradient pill, 1.55em 1.6em padding, 700 weight, lifts 3px on hover. Only "Read the paper" (arXiv) is present; an outline variant is defined but unused.
- **Section kicker.** Navy uppercase 0.76rem/800 with a 6px gradient dot.
- **Stat card.** White, 12px radius, 3px gradient top bar, gradient number, 4 per row (2 under 900px).
- **Pipeline chips.** White pills with 8px gradient dot, joined by faint arrows.
- **Results table.** Navy `#071a3d` header with `#e7f1ff` text; "ours" row `#eaf1fb` with a gradient "Ours" pill; best values bold navy.
- **BibTeX.** `#0a1830` block, `#1b3a63` border, 18px radius, gradient pill copy button.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Dark hero, gradient title, icon-marked affiliations (Sony Group, Sony AI) |
| Venue badge | Yes | Glass pill with cyan dot |
| Link buttons | arXiv only ("Read the paper") | Gradient pill |
| Teaser | Static image in overlapping white card | |
| Abstract | Justified 820px text | |
| Method | Pipeline chips plus figure frame | |
| Results tables | 4 tables | Navy headers, highlighted ours row |
| Example carousel | OmniCHOIR prompt/candidate cards with videos | Arrow buttons and dots |
| Sliders / 3D / HF demo | No | |
| BibTeX | Yes | Dark navy block |
| Acknowledgements | No | |

## Do's and Don'ts

- Do confine the dark treatment to the hero and code block.
- Do use the four-stop navy-to-cyan gradient for every accent dot, bar and primary button.
- Do overlap the teaser card into the hero with a negative margin.
- Don't use Bulma's default primary or link colors anywhere.
- Don't flatten cards; this style relies on soft navy-tinted shadows.

## Surfaces

Night hero, slate page, slate-band alternates, white cards, navy table headers and code.

## Imagery

One wide teaser image in a padded white frame; figure frames with 1.4rem padding; videos inside example cards.

## Layout

Centered hero, then Bulma columns inside `is-max-desktop` containers. Prompt grids use `1.2fr 1fr 1fr` and collapse to one column under 900px.

## Agent Prompt Guide

**Quick colors:** hero `#060a14`, page `#f8fafc`, band `#eef2f8`, ink `#0b1526`, body `#4a5872`, line `#e2e7f0`, navy `#003366`, blue `#0072ce`, cyan `#00b4d8`.

1. "Make a dark hero on `#060a14` with navy and cyan radial glows and a faint 26px dot grid; centered Inter 800 title with a white-to-`#7fe3ff` text gradient and a glass pill venue badge."
2. "Create stat cards: white, 1px `#e2e7f0` border, 12px radius, 3px navy-to-cyan gradient top bar, 2rem/800 gradient number, 0.83rem label in `#4a5872`."
3. "Style a results table: `#071a3d` header with `#e7f1ff` 0.72rem bold text, hairline rows, the 'ours' row on `#eaf1fb`, best values bold `#003366`."

## Similar Pages

Startup landing pages built on Bulma; within this collection, SatNav and AEON also use a dark hero with a light body.

## Quick Start

```css
:root {
  --bg: #f8fafc; --bg-soft: #eef2f8; --card: #ffffff;
  --ink: #0b1526; --ink-soft: #4a5872; --ink-faint: #8892a6; --line: #e2e7f0;
  --navy: #003366; --blue: #0072ce; --cyan: #00b4d8; --abyss: #001f3f;
  --hero: #060a14; --thead: #071a3d; --code: #0a1830;
  --gradient: linear-gradient(120deg, #001f3f 0%, #003366 35%, #0072ce 70%, #00b4d8 100%);
  --font: "Inter", "Segoe UI", -apple-system, sans-serif;
  --radius: 18px; --radius-sm: 12px;
  --shadow-sm: 0 2px 8px -2px rgb(11 21 38 / .06);
  --shadow-lg: 0 30px 60px -20px rgb(11 21 38 / .28);
}
```

## Provenance

- **URL:** https://wywywang.github.io/omniue-demo/
- **Paper:** Omni-Interactive Universal Embedder (OmniUE, arXiv 2608.27044), Wei-Yao Wang et al., Sony Group Corporation and Sony AI.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** footer says layout follows the Academic Project Page Template, adapted from Nerfies; styling is a heavy custom override of Bulma 0.9.4.
- **Measurement method:** static HTML and `index.css` parsed with `extract_style.py`; Bulma defaults filtered by reading the custom CSS. Not viewed in a browser, so the visual weight of the hero glow is inferred.
