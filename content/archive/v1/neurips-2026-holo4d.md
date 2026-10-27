# Holo4D Grayscale Gallery — Style Reference

> A Lato-set homepage that grew a video gallery, gray chrome and one blue link.

**Theme:** light

Values come from the single stylesheet `static/css/project.css`, which stacks several historical layers (base, a "yushi-theme" homepage layer, an "editorial" layer, final overrides). Only the last effective declaration is reported where layers conflict. Roles are interpreted from markup. Rendered output was not viewed.

## Overview

Holo4D is a hand-built page whose colors and type are deliberately borrowed from the first author's personal homepage: Lato throughout, near-black `#222` text, Jon-Barron-style link blue `#1772d0` with orange `#f09228` hover. Everything else is grayscale. The header is a large logo image (120px tall) over a two-weight title, a plain gray `NeurIPS 2026` kicker, and a centered row of dark pill buttons. A 2-minute demo video follows, then numbered-feeling sections each introduced by a small uppercase gray eyebrow and a 24px bold headline. Interactive galleries (view-mode toggles, example picker, carousel with thumbnails, blend slider) dominate the body. A muted brick red `#b03a2e` marks key phrases.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper | `#ffffff` | (literal) | Page background, alt sections also white |
| Homepage Ink | `#222222` | `--text` | Body text, active toggle fill |
| Homepage Blue | `#1772d0` | `--link`, `--accent` | Links; "ours" panel label background |
| Pumpkin Hover | `#f09228` | `--link-hover` | Link hover and focus |
| Brick Key | `#b03a2e` | `--key` | `.key` emphasized phrases, bold |
| Muted Gray | `#666666` | `--muted` | Teaser caption, secondary text |
| Kicker Gray | `rgb(85,85,85)` | (literal) | Venue kicker, section intro text |
| Eyebrow Gray | `rgb(136,136,136)` | (literal) | Section eyebrows, subheading counters |
| Pill Charcoal | `rgb(37,37,37)` | (literal) | Link buttons |
| Pill Hover | `rgb(68,68,68)` | (literal) | Link button hover |
| Hairline | `#e5e5e5` | `--line` | Section top rules, control borders |
| Light Panel | `#fafafa` | `--light` | BibTeX card, picker, framework items |
| Control Fog | `rgb(245,245,245)` | (literal) | Inactive view-mode buttons |
| Card Border | `rgb(226,232,240)` | (literal) | BibTeX card outline |
| Stage Dark | `rgb(34,34,34)` | (literal) | Comparison panel background |

## Tokens — Typography

- **Family:** `Lato`, Verdana, Helvetica, sans-serif (Google Fonts, 400/700) for everything, including buttons.
- **Mono:** SFMono-Regular, Menlo, Consolas, "Liberation Mono" for BibTeX.
- **Weights:** 400 and 700; one 550 in an older layer.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Project name (logo fallback) | 60px (40px mobile) | 700 | 1.02 | -0.065em |
| Paper title line | 40px (24px mobile) | 400 | 1.2 | -0.028em |
| Section h2 | 24px | 700 | 1.3 | -0.01em |
| Section intro / abstract | 20px (16px mobile) | 400 | 1.7 | max 860px |
| Authors | 17px | 400 | 1.8 | |
| Affiliations | 15px | 400 | | |
| Kicker, buttons, controls | 16px | 400 | | |
| Eyebrow, captions, footer | 14px | 700 eyebrow | | uppercase, 0.14em |
| BibTeX | 13.5px | 400 | 1.65 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link pills, BibTeX copy button | 999px |
| BibTeX card | 12px |
| Blend stage | 9px |
| Thumbnail button | 7px |
| View-mode buttons | 6px |
| Picker select, card playback | 5px |
| Panel labels, thumbnail images | 4px |

- **Shadows:** almost none. Back-to-top button `rgba(0,0,0,0.047) 0 3px 12px`; BibTeX card explicitly `box-shadow: none`.
- **Layout:** `--col: 1040px` for page, gallery and nav; `.text-width > *` capped at 780px; page gutter `clamp(14px, 4.5vw, 72px)`.
- **Section rhythm:** 56px vertical padding; each following section starts with a 1px `#e5e5e5` rule and 40px top padding.

## Components

- **Paper header.** Centered. Logo `img` 120px tall, title span on its own line, kicker `NeurIPS 2026` in `rgb(85,85,85)`, 0.02em tracking, no badge shape.
- **Link pills.** Paper, Video, Explore videos ↗, Code, Long-video demos ↗. Background `rgb(37,37,37)`, white text, 8px 17px padding, 999px radius, 8px gap; hover `rgb(68,68,68)`.
- **Section eyebrow.** 14px, 700, uppercase, 0.14em tracking, `rgb(136,136,136)`, 12px below.
- **View controls.** Segmented buttons on `rgb(245,245,245)`, 6px radius, 0.88rem; pressed state `#222` with white text.
- **Panel labels.** Overlaid on video, `rgba(17,17,17,0.9)` background, 4px radius; "ours" label switches to `#1772d0`.
- **Technical details.** `<details>` with gray summary; when open, 2px `#ddd` left border.
- **BibTeX card.** `#fafafa` card with `rgb(226,232,240)` border and 12px radius, pre in `#333`, white pill "Copy" button top-right.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Logo image plus two-weight title, 17px authors |
| Venue badge | Plain gray kicker text | |
| Link buttons | Paper (arXiv), Video, Code, two in-page anchors | Charcoal pills |
| Teaser | Demo video, then a 4-column mosaic (`0.65fr 1fr 1fr 0.65fr`, 6px gaps) | |
| Abstract | "Overview" section with 20px text | |
| Method figure | Pipeline figure with 0.84rem caption | |
| Results videos | Robotics, novel views, long videos, baseline comparison galleries | Toggle + picker + carousel |
| Image-comparison slider | Blend slider (`blend-stage`) | 9px radius |
| Tables / 3D / HF demo | No | |
| BibTeX | Yes | Light card with copy pill |
| Acknowledgements, concurrent works, references | Yes | Plain lists |

## Do's and Don'ts

- Do keep all chrome grayscale; blue is for links and the "ours" label only.
- Do use the brick-red `.key` sparingly for the claim words.
- Do separate sections with a hairline on the inner column, not full-bleed bands.
- Don't add shadows to cards; this page flattens them.
- Don't introduce a second typeface; Lato carries headings and UI.

## Surfaces

White everywhere; `#fafafa` and `rgb(245,245,245)` only for controls and the BibTeX card; dark `rgb(34,34,34)` stage behind comparison videos.

## Imagery

Video-first: one long demo, a six-tile teaser mosaic with portrait side tiles, many gallery clips. Static images are limited to the logo and pipeline figure.

## Layout

One 1040px column with a 780px text measure. A fixed sidebar table of contents exists in older CSS but is hidden (`display: none`) by the editorial layer; a translucent top bar (`rgba(255,255,255,0.95)`) is used instead.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#222222`, link `#1772d0`, hover `#f09228`, key `#b03a2e`, eyebrow `rgb(136,136,136)`, pill `rgb(37,37,37)`, line `#e5e5e5`, panel `#fafafa`.

1. "Make a centered header in Lato: 120px logo image, 40px weight-400 subtitle, gray 16px 'NeurIPS 2026' kicker, then charcoal pill links (8px 17px padding, 8px gap)."
2. "Add a section: 14px bold uppercase gray eyebrow with 0.14em tracking, 24px bold h2, 20px/1.7 intro capped at 860px, top hairline `#e5e5e5` with 40px padding."
3. "Build a segmented view toggle: buttons on `#f5f5f5`, 6px radius, 0.88rem; the pressed one is `#222` with white text."

## Similar Pages

Jon Barron-style homepages (same `#1772d0`/`#f09228` link pair), and editorial video galleries such as Vista4D and ReCamMaster that the page cites as concurrent work.

## Quick Start

```css
:root {
  --text: #222222; --muted: #666666;
  --link: #1772d0; --link-hover: #f09228; --key: #b03a2e;
  --line: #e5e5e5; --light: #fafafa; --pill: rgb(37,37,37);
  --font: Lato, Verdana, Helvetica, sans-serif;
  --mono: SFMono-Regular, Menlo, Consolas, monospace;
  --col: 1040px; --measure: 780px;
  --page-gutter: clamp(14px, 4.5vw, 72px);
  --radius-pill: 999px; --radius-card: 12px;
}
```

## Provenance

- **URL:** https://nirvanalan.github.io/projects/holo4d/
- **Paper:** Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion (arXiv 2610.25276), Yushi Lan et al.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** footer links Academic Project Page Template (eliahuhorwitz); the CSS itself is a custom rewrite with a homepage theme layer.
- **Measurement method:** static HTML and the single 54KB stylesheet parsed with `extract_style.py`; cascade layers resolved by reading the file in order. Not viewed in a browser.
