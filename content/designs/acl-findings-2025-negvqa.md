# NegVQA · Aliceblue Emoji Nerfies — Style Reference

> A one-screen benchmark card with an emoji next to every heading.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9, stock Nerfies `index.css`, a small `custom.css` and an inline `<style>`); roles are interpreted from markup and one rendered viewport. Bulma's palette shows up in the frequency scan, but only colors actually used are listed.

## Overview

NegVQA is the shortest page in its batch (about 10 KB of HTML). It keeps the Nerfies frame but strips it down: a title, a venue line as its own heading, black author names instead of Nerfies blue, four dark pill buttons, then three content sections whose `h2` titles start with emoji (🔮 Abstract, 💎 Dataset, 📈 Evaluation). The hero sits on an aliceblue band defined in `custom.css`. It reads like a dataset card rather than a showcase.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Aliceblue Wash | `aliceblue` (`#f0f8ff`, CSS named color) | `--bg-hero` | `.space-background` hero band |
| Paper White | `#ffffff` | `--bg` | Page and section background |
| Bulma Ink | `#363636` | `--text-heading` | Titles; dark button fill |
| Body Grey | `#4a4a4a` | `--text` | Bulma body text |
| Author Black | `#000000` (`black`) | `--link-author` | Author links (Nerfies blue commented out) |
| Venue Slate | `#555555` | `--text-venue` | Venue text |
| Code Smoke | `#f5f5f5` | `--bg-code` | BibTeX `pre` background (inline style) |
| Link Blue | `#3273dc` | `--link` | Body links (Bulma default) |

## Tokens — Typography

- **Display:** Google Sans (substitutes Product Sans, Inter) for title, authors and venue.
- **Body:** Noto Sans.
- **Math:** MathJax is loaded (detected) for inline notation.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-2`) | 2.5rem | 600 | 1.125 |
| Venue line (`h1`, `is-size-5`-scale) | 1.25rem | 600 | 1.25 |
| Section heading (`title is-3`) | 2rem | 600 | 1.125 |
| Abstract (justified) | 1rem | 400 | 1.5 |
| Affiliations | .75rem superscript markers | 400 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px pill |
| Figures | 0 |
| Code block | 4px (Bulma `pre` default, inferred) |

Shadows: none beyond Bulma focus rings. Layout: `container is-max-desktop` (960px at desktop, 1152 / 1344px at larger breakpoints); approach figure fixed to `50vw`.

## Components

- **Pill buttons:** `button is-normal is-rounded is-dark`, white text with icon: arXiv (X-style icon), Code (GitHub), 🤗 Dataset, 📊 Model Predictions.
- **Emoji section header:** centered `title is-3` with a leading emoji, no rule or underline.
- **Approach figure:** `figure` centered, width 50vw, no border.
- **Centered text box:** 90% width, 10px padding, centered (declared in `index.css`).

## Page Modules

- **Title/author block:** title, then "ACL 2025 Findings" as a separate heading, black author names with superscript affiliations (Stanford, Tsinghua).
- **Venue badge:** text heading, no pill.
- **Link buttons:** arXiv, Code, Dataset (Hugging Face), Model Predictions.
- **Teaser:** none; abstract follows the buttons.
- **Abstract:** justified paragraph under "🔮 Abstract".
- **Method/data figure:** "💎 Dataset: NegVQA" with one figure.
- **Results:** "📈 Evaluation of NegVQA" as a figure (no HTML table).
- **BibTeX:** `pre` on `#f5f5f5`.
- **Footer:** one line crediting the Nerfies template.

## Do's and Don'ts

- Do keep authors black; the page deliberately drops Nerfies blue.
- Do use one emoji per section heading, always leading.
- Don't add carousels or video; the page is a static three-section card.
- Don't put the venue in a badge; it is a centered text heading.

## Surfaces

Aliceblue hero, white body, light grey code block. No cards or shadows.

## Imagery

Two figures only: dataset construction diagram and results plot.

## Layout

Single centered column inside 960px; headings centered, body justified.

## Agent Prompt Guide

Quick colors: hero `#f0f8ff`, bg `#ffffff`, heading `#363636`, text `#4a4a4a`, authors `#000000`, code bg `#f5f5f5`.

1. "Build a minimal paper header on an aliceblue band: Google Sans title 2.5rem/600, a separate 1.25rem venue line, black author names, four dark pill buttons (`#363636`, white text, fully rounded)."
2. "Build an emoji section heading: centered Google Sans 2rem/600 with a single leading emoji, no divider."
3. "Build a BibTeX block: `pre` with background `#f5f5f5`, monospace, no border."

## Similar Pages

Nerfies; GeAR and InstructPart in this batch (same Bulma base, more furniture).

## Quick Start

```css
:root {
  --bg: #ffffff; --bg-hero: aliceblue; --bg-code: #f5f5f5;
  --text: #4a4a4a; --text-heading: #363636; --author: #000000;
  --button: #363636; --radius-pill: 290486px;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --max-width: 960px;
}
```

## Provenance

- **URL:** https://yuhui-zh15.github.io/NegVQA/
- **Paper:** NegVQA: Can Vision Language Models Understand Negation? (arXiv 2505.22946), Yuhui Zhang et al.
- **Venue:** ACL 2025 Findings.
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 Findings and the abstract links this page.
- **Template credit:** footer says the template is from the Nerfies project page.
- **Measurement method:** extract_style.py scan of HTML and CSS, manual diff of `index.css` against stock Nerfies, reading `custom.css` and the inline style, and one rendered viewport viewed in a browser. The aliceblue hero placement is taken from the `.space-background` class on the page (2 uses); its exact extent was not measured.
