# DiSE Aurora Cards — Style Reference

> A Fluent-style product keynote: a sunrise gradient from Microsoft blue through violet to apricot, painted on the wordmark, the buttons, the rules and the footer.

**Theme:** light

Measurements come from the page's own `style.css` on top of Bootstrap 5.3.0-alpha3 (CSS and JS from jsDelivr), plus KaTeX 0.16.7 and locally hosted Avenir Next Cyr / Segoe Print fonts. Bootstrap's `--bs-*` variables dominate the raw extractor counts; the table lists only colors the page's own rules or markup use. Roles are interpreted.

## Overview

The page is built from Bootstrap cards (16px radius, 2rem body padding) stacked in a centered container. Its identity is one gradient, `linear-gradient(107.54deg, #0078d4 .39%, #8661c5 51.23%, #ff9349 100%)`, reused five ways: clipped into the 4.2rem "DiSE" wordmark, as the fixed background of every pill link button, as a 5px rule under each card title, as the footer band, and (in pastel form `#e6eff7` → `#eeebf5` → `#fcf4ee`) as the fill of two highlight cards. Titles reference Playfair Display, but no Playfair font file is linked, so they fall back to Georgia (inferred). Body text uses Avenir / Avenir Next Cyr. Equations render with KaTeX inside a `#f8f8fb` rounded block; results use three metric cards on a pastel gradient with indigo `#423f94` figures.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Fluent Blue | `#0078d4` | (gradient stop) | Gradient start |
| Aurora Violet | `#8661c5` | (gradient stop) | Gradient middle |
| Apricot Dawn | `#ff9349` | (gradient stop) | Gradient end; link hover colour |
| Periwinkle Link | `#6567c9` | (literal) | Body links |
| Indigo Metric | `#423f94` | `.metric` | Metric-card headline numbers |
| Mist Blue → Lilac → Peach | `#e6eff7` / `#eeebf5` / `#fcf4ee` | `.x-gradient-block` | Pastel highlight-card fill |
| Metric Pastel | `#f2f7fc` / `#f5f2fb` / `#fff6f0` | `.metric-card` | Metric-card fill |
| Metric Edge | `#e4e6f0` | (literal) | Metric-card border |
| Equation Ground | `#f8f8fb` | `.equation-block` | KaTeX block fill |
| Card Ink | `#3f3f3f` | (literal) | Text in gradient cards |
| Author Ink | `#333333` | (literal) | Author names (bold) |
| Author Hover | `#007bff` | (literal) | Author link hover |
| Caption Grey | `#555555` | (literal) | Venue line, figure captions |
| Body Grey | `#4a4a4a` | (literal) | Metric-card descriptions |
| Org Grey | `#666666` / footnote `#888888` | (literal) | Affiliations / footnotes |
| Header Rule | `#e5e5e5` | (literal) | Blog-header and footer top border |
| Disabled Silver | `rgb(192,192,192)` | (literal) | Disabled link button |
| Footer White | `rgba(255,255,255,0.9)` / `0.7` | (literal) | Footer title / text |
| Bootstrap Primary | `#0d6efd` | `--bs-primary` | "Copy BibTeX" `btn-primary` |

## Tokens — Typography

- **Body / UI:** `'Avenir', 'Avenir Next Cyr', 'Config', 'Microsoft YaHei', 'Times New Roman'` set on `*`; Avenir Next Cyr is self-hosted. Substitute: Nunito Sans, Avenir Next.
- **Display:** `"Playfair Display", Georgia, "Times New Roman", serif` for `.title-font` and `.hero-mark` (Playfair not loaded; Georgia in practice, inferred).
- **Math:** KaTeX fonts (`KaTeX_Main`, `KaTeX_Math` …).
- **Also loaded:** Segoe Print (local), Bootstrap Icons, an icomoon icon font for button glyphs.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Wordmark `.hero-mark` | 4.2rem (3.1rem mobile) | 800 | 1 | gradient-clipped text |
| Title `.title-font` | 3rem (2.1rem mobile) | 600 | Bootstrap 1.2 | serif |
| Venue line | 1.2rem | 700 | | `#555` |
| Card title | Bootstrap h2 `calc(1.325rem + .9vw)` | 800 | 1.2 | Avenir, 5px gradient rule below |
| Authors | 18px | 500 (names bold) | | |
| Card text | 1.03rem | 400 | 1.5 | |
| Link button | 16px (17px hover) | 500 | | white |
| Figure caption | 0.94rem | 400 | | `#555` |
| Metric number | 1.02rem | 800 | | indigo |
| Affiliations / footnote | 0.9em / 0.8em | 400 | | |
| Footer | 15px | 800 | | white at 0.9 / 0.7 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 50px |
| Cards, gradient cards | 16px |
| Metric cards | 14px |
| Equation block | 12px |
| Card-title gradient rule | 0 (straight) |

- **Shadows:** link buttons `0px 0px 4px rgba(0,0,0,0.5)` (hover `0 0 6px rgba(0,0,0,0.75)`); figure images `0 6px 18px rgba(0,0,0,0.10)`.
- **Layout:** Bootstrap `container`; hero figure 92% and wide figures 86% of card width; two-figure grid with 20px gap; three-column metric grid with 14px gap; footer 5rem above content.

## Components

- **Wordmark hero.** "DiSE" in 4.2rem/800 with `background-clip: text` gradient, then the serif title, "ACL 2026 Main" at 1.2rem/700, authors with numeric superscripts, affiliations and footnote.
- **Gradient pill button.** Fixed 115×35px, 50px radius, white 16px/500 label, icomoon glyph before it, gradient background `fixed` so all buttons sample one continuous sweep; hover grows to 135×40px and 17px. Only an arXiv button is present.
- **Card.** Bootstrap `.card`, 16px radius, `overflow: hidden`, `card-body` 2rem padding; title 800 Avenir with a straight 5px gradient bar pulled up under it (`margin-top: -1em`).
- **Gradient card.** `x-gradient-block`: pastel blue-lilac-peach fill, `#3f3f3f` text; used for Abstract and Motivation.
- **Equation block.** `#f8f8fb`, 12px radius, 10px 14px padding, horizontal scroll.
- **Metric card.** Min-height 128px, 18px padding, 1px `#e4e6f0` border, 14px radius, pastel gradient, indigo 800 metric over `#4a4a4a` text.
- **Citation.** BibTeX printed in a card with a Bootstrap `btn-primary` "Copy BibTeX" that opens a modal confirmation.
- **Gradient footer.** Full gradient band, white 800 text, credit to Ximing Xing's template.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Gradient wordmark plus serif title |
| Venue badge | Text | "ACL 2026 Main" |
| Link buttons | arXiv | Gradient pill (Code button absent; author GitHub links only) |
| Abstract | Yes | Pastel gradient card |
| Method | Equation block (KaTeX) plus overview figure | White card |
| Results | Metric cards and table images | |
| Qualitative / ablation figures | Yes | Figure pair grid |
| Video / sliders / 3D / HF demo | No | |
| BibTeX | Yes | Card with modal copy |
| Footer | Template credit | Gradient band |

## Do's and Don'ts

- Do use one gradient everywhere and set `background-attachment: fixed` on buttons so they read as one sweep.
- Do keep the pastel version of the gradient for large fills; reserve the saturated one for small marks.
- Do render math with KaTeX inside a tinted block.
- Don't reference a display font you do not load (Playfair here).
- Don't add other accent colours; indigo and periwinkle are both drawn from the gradient's violet.

## Surfaces

White page with rounded white cards, two pastel gradient cards, tinted equation and metric blocks, and a saturated gradient footer.

## Imagery

Overview, qualitative and ablation PNGs with soft drop shadows; table images rendered as figures.

## Layout

Centered Bootstrap container, single column of cards; metric and figure grids collapse to one column under 768px.

## Agent Prompt Guide

**Quick colors:** gradient `#0078d4` → `#8661c5` → `#ff9349`, pastel `#e6eff7` → `#eeebf5` → `#fcf4ee`, link `#6567c9`, metric `#423f94`, text `#3f3f3f`, caption `#555555`.

1. "Create a gradient wordmark: 4.2rem/800 text with `background: linear-gradient(107.54deg, #0078d4 .39%, #8661c5 51.23%, #ff9349 100%)`, `background-clip: text` and transparent fill."
2. "Make pill link buttons 115×35px, 50px radius, white 16px/500 labels, the same gradient as a fixed background, `0 0 4px rgba(0,0,0,0.5)` shadow, growing to 135×40px on hover."
3. "Build a card section: 16px-radius card with 2rem padding, an 800-weight title, and a straight 5px gradient bar directly beneath it."

## Similar Pages

No other page in this batch uses a multi-stop brand gradient; Perturb-and-Revise uses a two-stop slate gradient only in its header.

## Quick Start

```css
:root {
  --grad: linear-gradient(107.54deg, #0078d4 .39%, #8661c5 51.23%, #ff9349 100%);
  --grad-pastel: linear-gradient(107.54deg, #e6eff7 .39%, #eeebf5 51.23%, #fcf4ee 100%);
  --link: #6567c9; --link-hover: #ff9349; --metric: #423f94;
  --text-card: #3f3f3f; --caption: #555555; --eq-bg: #f8f8fb;
  --font-body: 'Avenir', 'Avenir Next Cyr', sans-serif;
  --font-display: "Playfair Display", Georgia, serif;
  --radius-card: 16px; --radius-pill: 50px;
}
.card { border-radius: var(--radius-card); overflow: hidden; }
.footer { background: var(--grad); }
```

## Provenance

- **URL:** https://zhongzero.github.io/DiSE/
- **Paper:** Efficient Self-Evaluation for Diffusion Language Models via Sequence Regeneration (arXiv 2603.02760), Linhao Zhong, Linyu Wu et al. (Zhejiang University, National University of Singapore, Zhejiang University of Technology).
- **Venue:** ACL 2026 (page reads "ACL 2026 Main").
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 Main; the project page is linked in the arXiv abstract.
- **Template credit:** footer credits Ximing Xing's GithubPages-Template.
- **Measurement method:** `extract_style.py`, then a full read of `style.css` and the HTML to separate the page's rules from Bootstrap 5.3 defaults. The rendered page was not viewed, so the Playfair-to-Georgia fallback is inferred from the missing font link. The BibTeX on the page is an arXiv `@article`.
