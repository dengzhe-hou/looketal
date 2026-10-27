# PIG Spectrum Notebook — Style Reference

> A math-heavy Nerfies page in Arial, its acronym dyed in an eight-color spectrum.

**Theme:** light

Values come from the static HTML, the page's `static/css/index.css` (Nerfies-based, with a custom `.depth` rule), an inline `<style>` block, and Bulma 0.9 defaults. Bulma's palette inflates the raw counts, so only colors the page uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

PIG modifies Nerfies in two visible ways. First, the inline style block resets `body` to Arial with line-height 1.6 and a 20px margin, and narrows `.content` to 800px, so the page reads more like a typeset note than the stock template. Second, the acronym "PIG" in the `title is-2` heading is a `.depth` span whose text is clipped from a 90deg gradient running firebrick, chocolate, amber, olive, steel blue, cadet blue, navy and purple; on hover the gradient shifts and the span scales 1.1x. Under the title a plain `is-size-4` "ICLR 2025" line acts as the venue. The method section is a sequence of numbered `h4` steps with inline MathJax (`\(\texttt{FE}_\phi\)`, `\mathbb{R}^d`). Results are four PDE case studies (Klein-Gordon, Flow-Mixing, Helmholtz, Lid-Driven Cavity), each an autoplay video or figure followed by a sentence with the relative L2 error.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Code Mist | `#f5f5f5` | (Bulma) | BibTeX `pre` |
| Bulma Graphite | `#363636` | (Bulma) | Titles, dark pill buttons |
| Body Gray | `#4a4a4a` | (Bulma) | Body text |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author links (about `#209CEE`) |
| Spectrum Firebrick | `#b22222` | (`.depth` stop 1) | Acronym gradient |
| Spectrum Chocolate | `#d2691e` | (`.depth` stop 2) | Acronym gradient |
| Spectrum Amber | `#f5a83c` | (`.depth` stop 3) | Acronym gradient |
| Spectrum Olive | `#6b8e23` | (`.depth` stop 4) | Acronym gradient |
| Spectrum Steel | `#4682b4` | (`.depth` stop 5) | Acronym gradient |
| Spectrum Cadet | `#5f9ea0` | (`.depth` stop 6) | Acronym gradient |
| Spectrum Navy | `#000080` | (`.depth` stop 7) | Acronym gradient |
| Spectrum Purple | `#800080` | (`.depth` stop 8) | Acronym gradient |
| Note Red | `red` (`#FF0000`) | (inline) | One emphasized remark |

## Tokens — Typography

- **Body:** Arial, sans-serif (inline override of the Nerfies Noto Sans). Substitute: Helvetica.
- **Display:** Google Sans on `.publication-title` and authors (index.css). Substitute: Product Sans, Inter.
- **Math:** MathJax inline `\( \)` delimiters.
- Montserrat appears only in a commented-out title line.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`is-2`) | 2.5rem | 600 | `margin-bottom: 4px` |
| Venue (`is-size-4`) | 1.5rem | 400 | `margin-top: 4px` |
| Section title (`is-3`) | 2rem | 600 | centered |
| Method step (`h4`) | 1.3em | inherited | left aligned, 12px bottom margin |
| Centered labels | 125% | 400 | `text-align: center; font-size: 125%` (4 uses) |
| Body | 1rem | 400 | line-height 1.6 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Body margin | 20px |
| `.content` | max-width 800px, centered |
| `.equation` | centered, 20px vertical margin |
| Link buttons | 290486px radius (pill) |
| Section spacing | repeated `</br></br></br>` between case studies |
| Container | `is-max-desktop` (960px, Bulma `.container` rule) |

Shadows: Bulma defaults only.

## Components

- **Hero:** `title is-2 publication-title` with gradient `.depth` "PIG", authors, "ICLR 2025", three pill buttons.
- **Link buttons:** Paper (arXiv abs), arXiv (href `https://arxiv.org/`, a placeholder), Code (GitHub).
- **Teaser:** autoplay training-visualization video with caption "Each Gaussian is displayed as the ellipsoids...".
- **Method:** main figure at 100%, a second figure at 75% centered, numbered `h4` steps with inline math.
- **Case study:** `h3` equation name, autoplay video or figure, one paragraph with the error figure.
- **Footer:** "This template is a modification of Nerfies' project page."

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Gradient acronym in title |
| Venue badge | Yes | Plain `is-size-4` "ICLR 2025" |
| Link buttons | Yes | Paper, arXiv (placeholder link), Code |
| Teaser video | Yes | Training visualization loop |
| Abstract | Yes | Justified |
| Method figure | Yes | Two figures plus numbered derivation with MathJax |
| Results | Yes | Four PDE case studies with videos/figures |
| Image comparison slider / 3D / demo | No | |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do confine the spectrum gradient to the acronym; all other text stays neutral.
- Do write the method as numbered steps with inline math rather than a single figure.
- Do end each case study with the quantitative result in one sentence.
- Don't point a visible arXiv button at the arXiv homepage.
- Don't space sections with stacked `<br>` tags if reproducing; use margins.

## Surfaces

All white. No `hero is-light` bands.

## Imagery

Teaser video, two method figures, four case-study videos/figures (4 `<img>`, 4 `<video>` in static HTML).

## Layout

960px Bulma column with an 800px `.content` measure; Arial body narrows the visual tone.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, text `#4a4a4a`, author link `hsl(204,86%,53%)`, acronym gradient `#b22222 #d2691e #f5a83c #6b8e23 #4682b4 #5f9ea0 #000080 #800080`.

1. "Render the acronym in the title as gradient text: 90deg through `#b22222, #d2691e, #f5a83c, #6b8e23, #4682b4, #5f9ea0, #000080, #800080`, `background-clip: text`, scale 1.1 on hover."
2. "Write a method section of numbered h4 steps at 1.3em, left aligned, each followed by an 800px paragraph with inline MathJax and a centered display equation."
3. "Lay out a PDE case study: h3 equation name, an autoplay muted looping video, then one sentence reporting the relative L2 error."

## Similar Pages

Nerfies-derived pages in this collection (LARP, SeTok); PIG is the most equation-dense.

## Quick Start

```css
:root {
  --bg: #ffffff; --title: #363636; --text: #4a4a4a;
  --author-link: hsl(204, 86%, 53%);
  --font-body: Arial, sans-serif; --font-display: "Google Sans", sans-serif;
  --measure: 800px; --radius-pill: 290486px;
}
.depth {
  background: linear-gradient(90deg, #b22222, #d2691e, #f5a83c, #6b8e23, #4682b4, #5f9ea0, #000080, #800080);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
```

## Provenance

- **URL:** https://namgyukang.github.io/Physics-Informed-Gaussians/
- **Paper:** PIG: Physics-Informed Gaussians as Adaptive Parametric Mesh Representations (arXiv 2412.05994), Namgyu Kang et al.
- **Venue:** ICLR 2025 (text under title).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** modification of the Nerfies project page (footer).
- **Measurement method:** `extract_style.py` plus manual reading of the inline style block, inline attributes and the `.depth` rule in index.css. Rendered page not viewed.
