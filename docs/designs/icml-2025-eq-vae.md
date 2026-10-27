# EQ-VAE Ubuntu Traffic Lights — Style Reference

> A Nerfies page in Ubuntu type with a row of big charcoal, yellow and blue pill buttons.

**Theme:** light

Values come from the static HTML, inline `<style>` blocks, inline attributes and a modified Academic Project Page Template `index.css` over Bulma 0.9. Bulma colors are listed only where the markup uses them (dark, warning, info buttons and the light band). Measurements are normalized; roles are interpreted.

## Overview

EQ-VAE runs on the Academic Project Page Template but swaps the body face for Ubuntu at a forced 20px (`font-size: 20px !important`), which makes the page feel larger and rounder than stock Nerfies. The title is an h2 `title is-1` whose method name "EQ-VAE" is set in Consolas teal, like a LaTeX `\texttt`. Link buttons are `is-large`: charcoal Code and arXiv, a Bulma-yellow Models (Hugging Face) and a Bulma-blue "ICML 2025" pill that doubles as the venue badge, giving a traffic-light row. A wide teaser (80% width) carries a two-part caption with `code` tokens in black, the abstract sits in a `hero is-light` gray band, and the BibTeX block has a blue absolute-positioned copy button.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Method Teal | `teal` (`#008080`) | `.texttt` | "EQ-VAE" in the title, Consolas |
| Bulma Charcoal | `#363636` | `button is-dark` | Code and arXiv buttons; titles |
| Bulma Yellow | `#ffdd57` | `button is-warning` | Models (Hugging Face) button; text `rgba(0,0,0,0.7)` |
| Bulma Info Blue | `#3298dc` | `button is-info` | "ICML 2025" venue button, white bold text |
| Body Gray | `#4a4a4a` | Bulma `$text` | Body text (inferred Bulma default) |
| Code Black | `#000000` | `code { color: black !important }` | Inline code tokens (`SD-VAE`, `DiT-XL/2`) |
| Code Pink Fill | `#f5f5f5` | Bulma `code` background | Inline code chip (Bulma default, inferred) |
| Light Band | `#f5f5f5` | `hero is-light` | Abstract band |
| Bib Box | `#f5f5f5` | `.code-container` | BibTeX container, 1px `#ddd` border |
| Copy Blue | `#007bff` | `.copy-btn` | Copy button; hover `#0056b3`; text `#fff` |
| Author Sky | `hsl(204, 86%, 53%)` | template `.publication-authors a` | Author links (≈ `#209cee`) |

## Tokens — Typography

- **Body:** `'Ubuntu', sans-serif` at 20px (`index.css` uses `!important`, overriding the inline 10px rule). Google Fonts link loads Ubuntu.
- **Display / authors:** `Google Sans` (template). Substitute: Product Sans, Inter.
- **Method token:** `Consolas`, teal, 1em.
- **Math:** MathJax is loaded.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`h2.title.is-1`) | 3rem | 600 | Google Sans; method name Consolas teal |
| Section h2 (`title is-3`) | 2rem | 600 | |
| Sub-heads h4 | 1.5rem (Bulma `is-4`, inferred) | 600 | |
| Body | 20px | 400 | Ubuntu |
| Teaser caption | 1rem (inline) | 400 | Left-aligned, bold lead-ins |
| Inline headline span | 2rem bold (inline) | 700 | Used once for emphasis |
| Buttons (`is-large`) | 1.5rem | 400; venue label bold | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (Bulma rounded) |
| BibTeX container, copy button | 5px |
| Carousel items | 10px (template) |

- **Shadows:** none added.
- **Layout:** teaser `container is-fullhd` at 80% max-width with 5% side padding; abstract `container is-max-fullhd` with a three-quarter column; other sections `is-max-desktop` (960px) and inline wrappers at 1200px or 1800px; floated figures 470px (right) and 500px (left).

## Components

- **Large pill buttons.** Bulma `external-link button is-large is-rounded` in three colors: `is-dark` (Code, arXiv), `is-warning` (Models with a Hugging Face icon), `is-info` (ICML 2025 with a scroll icon and bold label, linking to the ICML virtual poster). A smaller `is-normal is-dark` Supplementary button also appears.
- **Teletype method name.** `.texttt` span: Consolas, teal, no letter-spacing.
- **Floated figure.** `.right-float` 470px or `.left-float` 500px images with 10px margins, wrapping body text.
- **BibTeX with copy.** `.code-container` relative box (`#f5f5f5`, 1px `#ddd`, 5px radius, 10px padding) with an absolute `#007bff` copy button at top-right; `pre` right padding 170px leaves room for it.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Nerfies-style centered |
| Venue badge | "ICML 2025" as an `is-info` pill button | Blue large button |
| Link buttons | Supplementary, Code, arXiv, Models, ICML 2025 | Large rounded, three colors |
| Teaser | Wide figure with two-part caption | 80% width |
| Abstract | Yes | `hero is-light` band, justified |
| Method | "Method" section with latent visualizations | Floated figures |
| Results / analysis | "Results", "Analysis", "Additional Visualizations" | Images; no HTML tables |
| Carousel | Template carousel scripts loaded | |
| Video / sliders / 3D | No | |
| BibTeX | "Cite Us" | Box with copy button |
| Acknowledgements | No | Footer credits the template |

## Do's and Don'ts

- Do render the method name like `\texttt` in teal monospace inside the title.
- Do make the venue a link button to the conference poster page.
- Do keep inline code black on the light chip so it reads as code, not as a link.
- Don't nest link-block anchors as the source does (several `</a></span>` are unbalanced); a reproduction should close each button.
- Don't leave Bulma's 1rem body; this page's tone depends on 20px Ubuntu.

## Surfaces

White page with one `#f5f5f5` light band for the abstract and a gray BibTeX box.

## Imagery

PCA visualizations of latent spaces, training curves and reconstruction grids (23 images), several floated beside text.

## Layout

Mixed container widths: full-HD 80% for the teaser, three-quarter column for the abstract, 960px for most text, 1200–1800px wrappers for wide figures.

## Agent Prompt Guide

**Quick colors:** text `#4a4a4a`, dark button `#363636`, yellow button `#ffdd57`, info button `#3298dc`, method teal `#008080`, band `#f5f5f5`, copy `#007bff`.

1. "Write a 3rem Google Sans title where the method name 'EQ-VAE' is set in Consolas, teal, followed by ': Equivariance Regularized Latent Space…' in the normal face."
2. "Make a row of Bulma `is-large is-rounded` buttons: Code and arXiv `is-dark`, Models `is-warning` with a Hugging Face icon, and a bold 'ICML 2025' `is-info` button linking to the poster."
3. "Build a BibTeX box: `#f5f5f5` fill, 1px `#ddd` border, 5px radius, 10px padding, with a `#007bff` copy button absolutely placed 10px from top and right; pre gets 170px right padding."

## Similar Pages

Other Academic Project Page Template pages; SmPO, CoMemo and WAM in this collection share the template.

## Quick Start

```css
:root {
  --text: #4a4a4a; --dark: #363636; --warning: #ffdd57; --info: #3298dc;
  --method: teal; --band: #f5f5f5; --bib-line: #dddddd;
  --copy: #007bff; --copy-hover: #0056b3;
  --font-body: "Ubuntu", sans-serif; --font-display: "Google Sans", "Inter", sans-serif;
  --font-tt: Consolas, "Liberation Mono", monospace;
}
body { font-family: var(--font-body); font-size: 20px; }
.texttt { font-family: var(--font-tt); color: var(--method); }
```

## Provenance

- **URL:** https://eq-vae.github.io/
- **Paper:** EQ-VAE: Equivariance Regularized Latent Space for Improved Generative Image Modeling (arXiv 2502.09509), Theodoros Kouzelis et al.
- **Venue:** ICML 2025 (shown as an `is-info` button linking to the ICML 2025 virtual poster).
- **Selection reason:** arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- **Template credit:** footer says it "was built using the Academic Project Page Template which was adopted from the Nerfies project page".
- **Measurement method:** `extract_style.py` plus manual reading of inline styles and `index.css`. Bulma button colors are Bulma 0.9 defaults for the classes in the markup. Rendered page not viewed; the effect of the unbalanced anchors on button layout is not confirmed.
