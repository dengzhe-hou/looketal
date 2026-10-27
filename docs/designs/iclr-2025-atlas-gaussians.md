# Atlas Gaussians Orange TL;DR — Style Reference

> A clean template page that shouts its two-line TL;DR in orange-red.

**Theme:** light

Values come from the static HTML, the APPT/Nerfies `static/css/index.css`, and Bulma 0.9 defaults. Bulma's palette inflates the raw counts, so only colors used by the page's markup or index.css are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

Atlas Gaussians is a near-stock Academic Project Page Template page (footer credits APPT and Nerfies). What makes it recognizable is the TL;DR band: directly under the hero, inside a `hero is-light` band, a centered 25px paragraph in CSS `OrangeRed` states the two contributions, with "infinite" in bold. The venue sits inside the affiliation line, "ICLR 2025" followed by "(Spotlight)" in pure red. The rest is four full-width static figures, each with a centered `subtitle` caption, MathJax-rendered symbols (`\( \mathcal{A} \)`), and a closing "Further Information" block that lists the authors' paper and four concurrent works as indented plain links.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| TL;DR Band | `#f5f5f5` | (Bulma `hero is-light`) | TL;DR and alternating bands, BibTeX `pre` |
| Bulma Graphite | `#363636` | (Bulma) | Titles, dark pill buttons |
| Body Gray | `#4a4a4a` | (Bulma) | Body text |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author links (about `#209CEE`) |
| Bulma Link | `#3273dc` | (Bulma) | Plain links in Further Information |
| TL;DR Orange-Red | `OrangeRed` (`#FF4500`) | (inline named color) | TL;DR paragraph |
| Spotlight Red | `red` (`#FF0000`) | (inline named color) | "(Spotlight)" tag |

## Tokens — Typography

- **Display:** Google Sans (title, authors). Substitute: Product Sans, Inter.
- **Body:** Noto Sans. Substitute: Open Sans.
- **Math:** MathJax 3 (script included four times).

| Role | Size | Weight |
|---|---|---|
| Title (`is-1`) | 3rem | 600 |
| TL;DR | 25px (inline), inside `h2.subtitle` | 400, key words bold |
| Section title (`is-3`) | 2rem | 600 |
| Figure caption (`h2.subtitle`) | Bulma subtitle 1.25rem | 400 |
| Authors (`is-size-5`) | 1.25rem | 400 |
| Further Information list | `h3.subtitle` with 2em left indents | 400, labels bold |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Carousel items / video | 10px (template default) |
| Bulma controls | 4px |

No custom shadows. Container `is-max-desktop` (960px, Bulma default, inferred). Figures use `max-width: 100%; height: auto`.

## Components

- **Hero:** title, authors, affiliation line "The University of Texas at Austin, Alibaba Group" then "ICLR 2025 (Spotlight)" on a new line, two dark pill buttons.
- **Link buttons:** Paper (arXiv PDF) and Code (GitHub); `is-dark is-rounded`.
- **TL;DR band:** `section hero is-light`, centered `h2.subtitle` holding a 25px OrangeRed paragraph with `<br>` breaks and a ‡ footnote marker.
- **Figure block:** `title is-3` heading, full-width PNG, centered caption below.
- **Further Information:** bold "Ours:" and "Several concurrent works by others:" labels, each link in a `margin-left: 2em` div with the raw arXiv URL visible.
- **BibTeX:** Bulma `pre`.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Stock APPT |
| Venue badge | Yes | Text in affiliation line, "(Spotlight)" in red |
| Link buttons | Yes | Paper, Code |
| Teaser | Yes | TL;DR text band takes the teaser slot; no teaser image or video |
| Abstract | Yes | Justified, `is-four-fifths` |
| Method figure | Yes | "Atlas Gaussians representation", "VAE architecture" |
| Results | Yes | "Analysis (diversity & controllability & originality)", "Text-conditioned 3D generation" comparison figure |
| Related / concurrent work list | Yes | "Further Information" with five arXiv links |
| Image comparison slider / interactive 3D / demo | No | Extractor's 3D flag was triggered by the word "Splatting" only |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do put the one-sentence claim in a single loud color right under the hero.
- Do credit concurrent work openly in a closing list with full URLs.
- Don't mix OrangeRed and pure red elsewhere; they are used once each.
- Don't leave `alt="MY ALT TEXT"` on figures (the template placeholder remains on all four).

## Surfaces

White hero, grey `hero is-light` TL;DR band, white figure sections.

## Imagery

Four static PNG figures from the paper. No video, no carousel content.

## Layout

Centered 960px column; figures span the column; captions centered.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f5f5f5`, title `#363636`, text `#4a4a4a`, TL;DR `#FF4500`, spotlight `#FF0000`, author link `hsl(204,86%,53%)`.

1. "Add a TL;DR band: Bulma `hero is-light`, centered, 25px text in `#FF4500`, two numbered claims separated by line breaks, key word bold."
2. "In the affiliation line, put 'ICLR 2025' on a new line followed by '(Spotlight)' in `#FF0000`."
3. "Create a 'Further Information' block with bold group labels and each paper title plus raw arXiv URL indented 2em."

## Similar Pages

Other APPT pages in this collection (Sitcom-Crafter, AIF, PR-IQA); the TL;DR band is the distinguishing element.

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f5f5f5; --title: #363636; --text: #4a4a4a;
  --link: #3273dc; --author-link: hsl(204, 86%, 53%);
  --tldr: #FF4500; --award: #FF0000;
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --fs-tldr: 25px; --radius-pill: 290486px;
}
```

## Provenance

- **URL:** https://yanghtr.github.io/projects/atlas_gaussians/
- **Paper:** Atlas Gaussians Diffusion for 3D Generation (arXiv 2408.13055), Haitao Yang et al.
- **Venue:** ICLR 2025, marked Spotlight on the page.
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** Academic Project Page Template adapted from Nerfies (footer).
- **Measurement method:** `extract_style.py` plus manual reading of inline styles. Named colors converted to hex by CSS definition. Rendered page not viewed.
