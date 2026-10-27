# Which Way Harbour Green — Style Reference

> A friendly science-museum placard, bold Montserrat over pastel green with a yellow ball.

**Theme:** light

Values come from a tokenized multi-file stylesheet set (`tokens.css`, `base.css`, `fonts.css`, and per-section files such as `hero.css`, `results.css`, `bibtex.css`, `palette.css`). `tokens.css` documents its own roles in comments, so most roles below are the authors' stated intent. The page currently ships a palette switcher with two preview accents (navy, yellow); the default green is described here. Rendered output was not viewed.

## Overview

"Which Way Did It Move?" (KHU VLL) is a diagnostic paper about directional motion blindness in video models, and its page is designed like an explainer exhibit. Headings are Montserrat 800, body Figtree, mono IBM Plex Mono, all self-hosted. The identity is a deep green accent `#2a7350` plus the yellow ball `#ffc533` from the example videos. The hero centers a green pill venue badge with a Sydney Opera House icon, a giant two-part title (question then subtitle), 600-weight authors, ink pill buttons (arXiv, Code, 🤗 Data, BibTeX), and a pastel-green TL;DR card. An animated scene shows a ball, a model, and a Q&A exchange. Every section title gets an auto-numbered green pill counter (`01`, `02`, …) and a green dot. Results use a colorblind-validated group palette (ours amber, closed blue, open teal, motion indigo). Blue means correct and red means wrong, matching the paper's figures.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Page White | `#ffffff` | `--page`, `--surface` | Background, cards, BibTeX box |
| Mint Band | `#eff7f2` | `--band` | Alternating section bands |
| Graphite | `#24292f` | `--ink` | Text, default button fill |
| Slate | `#5f6b7a` | `--ink-2` | Affiliations, secondary text |
| Hairline | `#e4e7ec` | `--line` | Borders |
| Harbour Green | `#2a7350` | `--accent`, `--sail` | Venue badge, section counters and dots, nav ball |
| Green Soft | `#e0efe6` | `--accent-soft` | Soft buttons |
| Green Pastel | `#cbe4d5` | `--accent-pastel` | TL;DR card |
| Ball Yellow | `#ffc533` | `--yellow` | The tracked object in every video and diagram |
| Harbour Wave | `#9fd3ff` / `#d2ebff` | `--wave`, `--wave-2` | Water in the Opera House badge icon |
| Signal Blue | `#2b6ff3` | `--blue` | Correct answers, button hover |
| Blue Soft | `#e8f0ff` | `--blue-soft` | Correct-answer tint |
| Error Red | `#ef5350` | `--red` | Wrong answers, gaps |
| Red Soft | `#ffe9e8` | `--red-soft` | Wrong-answer tint |
| Panel | `#f3f6fb` | `--panel` | Diagram panels |
| Stage | `#f9fafc` | `--stage` | Video stages |
| Bar Base | `#d6dce6` | `--bar-base` | Chart track |
| Ours Amber | `#eda100` | `--g-ours` | Results group: ours |
| Closed Blue | `#2b6ff3` | `--g-closed` | Results group: closed models |
| Open Teal | `#1baf7a` | `--g-open` | Results group: open models |
| Motion Indigo | `#4a3aa7` | `--g-motion` | Results group: motion-specialist models |

Preview accents: navy `#213f6e` (band `#eef2f9`) and yellow `#ffc533` (band `#fff9e6`).

## Tokens — Typography

- **Headings:** `Montserrat` 800 / 600 (self-hosted). Substitute: system bold sans.
- **Body:** `Figtree` 400 (500 on phones, because 400 reads thin). Substitute: Inter.
- **Mono:** `IBM Plex Mono`.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title question | `clamp(2.875rem, 5.75vw, 5.05rem)` | 800 | 1.05 | -0.02em, balanced |
| Subtitle | `clamp(1.4375rem, 2.3vw, 2.07rem)` | 600 | 1.25 | max 26em |
| Venue badge | `clamp(1.2rem, 1.72vw, 1.55rem)` | 800 | 1.3 | |
| Authors | `clamp(1.15rem, 1.5vw, 1.38rem)` | 600 | | |
| Section title | `clamp(1.8rem, 3vw, 2.6rem)` | 800 | 1.15 | counter pill at 0.6em |
| h3 | `clamp(1.25rem, 1.7vw, 1.5rem)` | 700 | | |
| TL;DR | `clamp(1.15rem, 1.7vw, 1.55rem)` | 500 | 1.4 | |
| Body | `clamp(1.0625rem, 1.25vw, 1.1875rem)` | 400 | | measure 37em |
| Hero buttons | 1.22rem | 600 | | |
| Key number | `clamp(1.75rem, 2.6vw, 2.25rem)` | | | |
| Small / labels | 0.94–1.125rem | | | |

## Tokens — Spacing & Shapes

Spacing scale 4, 8, 12, 16, 24, 32, 48, 64, 96px; gutter `clamp(20px, 4.4vw, 64px)`; section gap `clamp(56px, 6vw, 84px)`.

| Element | Radius |
|---|---|
| Buttons, venue badge, counters, palette switcher | 999px |
| Cards, TL;DR, BibTeX box (`--radius`) | 16px |
| Small panels (`--radius-sm`) | 10px |
| Dots, ball | 50% |

- **Shadows:** palette switcher only (`0 6px 18px rgba(36,41,47,.12)`); content is flat.
- **Layout:** `--container` 1280px; prose measure 37em; BibTeX box 820px.
- **Sticky section index:** tabs at ≥1280px (`--nav-h` 114px), a compact bar below (84px).

## Components

- **Venue badge.** Green pill, white Montserrat 800, inline SVG Sydney Opera House with green sails and blue waves.
- **Button (`.btn`).** Ink pill, white 600 text, 0.5em 1.15em padding (hero 0.55em 1.25em at 1.22rem), hover `#2b6ff3`. `.btn--soft` is green-soft with ink text, hover green with white text.
- **TL;DR card.** Pastel green, 16px radius, centered balanced text, white "TL;DR" tag pill.
- **Section title.** Green dot before the text, a green pill counter (`01`…) above it in tabular numerals.
- **Hero scene.** Animated ball video, model chip, and Q&A bubbles; color question vs direction question styled with blue/red reply marks.
- **Results board.** Group marks use both shape and color; benchmark toggles are `.btn` with `aria-pressed`.
- **BibTeX.** White box, 16px radius, 24px code padding.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered Montserrat question + subtitle |
| Venue badge | Yes | Green pill with Opera House icon |
| Link buttons | arXiv, Code, Data (HF), BibTeX | Ink pills |
| Teaser | Animated reel and scene with Pause/Replay | |
| Abstract | "Summary" section plus hero TL;DR | |
| Dataset | MoDirect benchmark section | |
| Diagnosis | "Where does directional motion blindness arise?" | |
| Method | DeltaDirect with pipeline replay | |
| Results | Benchmark-toggle board with group colors | |
| Sliders / 3D / HF Space | No | |
| BibTeX | Yes | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep blue for correct and red for wrong, as in the paper's figures.
- Do number sections with the green counter pill automatically.
- Do keep the yellow ball the same in every palette.
- Don't ship the palette switcher in a final page; the CSS marks it as a temporary preview.
- Don't use Figtree 400 on phones; the tokens bump it to 500.

## Surfaces

White page with mint bands, pastel TL;DR card, light panels and stages for diagrams and videos.

## Imagery

Short synthetic ball-motion videos, animated diagrams, and charts; the ball yellow ties them together.

## Layout

Centered hero; 1280px container with 37em prose measure; sticky section index across the top.

## Agent Prompt Guide

**Quick colors:** page `#ffffff`, band `#eff7f2`, ink `#24292f`, ink-2 `#5f6b7a`, line `#e4e7ec`, accent `#2a7350`, pastel `#cbe4d5`, yellow `#ffc533`, blue `#2b6ff3`, red `#ef5350`.

1. "Make a green pill venue badge `#2a7350` with white Montserrat 800 text and an icon, above a centered Montserrat 800 title at `clamp(2.875rem,5.75vw,5.05rem)` and a 600-weight subtitle."
2. "Create a TL;DR card on `#cbe4d5`, 16px radius, 24px 32px padding, centered balanced 500-weight text with a white pill 'TL;DR' tag."
3. "Style section titles with a green dot before the text and an auto-incremented `01` counter pill in `#2a7350` with white tabular numerals above."

## Similar Pages

Explainer-style pages such as Distill articles; within this collection ReMind also numbers its sections, and SatNav also gives each data group its own hue.

## Quick Start

```css
:root {
  --page: #ffffff; --band: #eff7f2; --ink: #24292f; --ink-2: #5f6b7a; --line: #e4e7ec;
  --accent: #2a7350; --accent-soft: #e0efe6; --accent-pastel: #cbe4d5; --on-accent: #fff;
  --yellow: #ffc533; --blue: #2b6ff3; --red: #ef5350;
  --g-ours: #eda100; --g-closed: #2b6ff3; --g-open: #1baf7a; --g-motion: #4a3aa7;
  --font-head: "Montserrat", -apple-system, "Segoe UI", sans-serif;
  --font-body: "Figtree", -apple-system, "Segoe UI", sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --container: 1280px; --measure: 37em; --radius: 16px; --radius-sm: 10px;
}
```

## Provenance

- **URL:** https://jong980812.github.io/which-way-did-it-move/
- **Paper:** Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness (arXiv 2605.22823), Jongseo Lee et al.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** none; custom tokenized CSS.
- **Measurement method:** static HTML and 13 stylesheets (9 read here) parsed with `extract_style.py` and read directly. Not viewed in a browser; the palette switcher means a visitor may see navy or yellow instead of green.
