# WAM Wavelet Night Banner — Style Reference

> A conference poster hung behind smoked glass, with the title chalked on in white.

**Theme:** light (dark image hero over a white page)

Values come from the static HTML, its inline `<style>` and attributes, and a heavily customized Academic Project Page Template `index.css` over Bulma 0.9. Bulma's unused palette is excluded. Measurements are normalized; roles are interpreted.

## Overview

The WAM page opens on a `hero is-medium` whose background is a 1200x630 wavelet banner image under a 60% black overlay (`rgba(0,0,0,0.6)`, easing to 0.5 on hover). Title, authors and the "Accepted at ICML 2025" subtitle are forced white, with white underlined author links. Two rows of dark rounded pills follow: external links (ICML Poster, OpenReview, Code, Colab Notebook) and four sub-pages of extra material (Proposed approach, Applications, Quantitative evaluation, Additional illustrations), which makes the page a hub with satellite HTML pages. The custom `index.css` adds motion everywhere: buttons lift 1px with a ripple, carousel cards scale 1.01 with a soft shadow, every image scales 1.01 on hover, author links grow a 2px underline, and the footer tints gray on hover. Inside the image carousel, captions color-code wavelet scales: fine `#2d50ff`, intermediate `#f44156`, coarse `#ffdd00`, and target audio `#078c14`. A clickable 720px poster thumbnail with 16px corners opens a Bulma modal.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Smoked Overlay | `rgba(0,0,0,0.6)` | `.hero::before` | Overlay on the banner image (0.5 on hover) |
| Chalk White | `#ffffff` | `.hero .title`, `.hero a` | Title, authors, hero links (`!important`) |
| Link Hover Gray | `#dddddd` | `.hero a:hover` | Hero link hover |
| Fine-Scale Blue | `#2d50ff` | inline | "fine texture details", "Fine scales" in captions |
| Mid-Scale Red | `#f44156` | inline | "intermediate-scale contours" |
| Coarse-Scale Yellow | `#ffdd00` | inline | "coarse edges", "Coarse scales" |
| Target Green | `#078c14` | inline | "parts of the target class audio" |
| Bulma Charcoal | `#363636` | `button is-dark`, `.title` | Pill buttons, section titles |
| Body Gray | `#4a4a4a` | Bulma `$text` | Body text (Bulma default) |
| Author Sky | `hsl(204, 86%, 53%)` | `.publication-authors a` | Author link color outside the hero; hover `hsl(204, 86%, 40%)` |
| Focus Ring | `rgba(0,123,255,0.25)` | `.external-link.button:focus` | 3px button focus ring |
| Ripple White | `rgba(255,255,255,0.3)` | `.ripple` | Button click ripple |
| Footer Hover | `#f5f5f5` | `.footer:hover` | Footer background on hover |
| Scrollbar | `#f1f1f1` / `#888888` / `#555555` | `::-webkit-scrollbar*` | Track, thumb, thumb hover |
| Dot Black | `#000000` / `#333333` | `.slider-pagination .slider-page` | Carousel dots and dot hover |

## Tokens — Typography

- **Display / authors:** `Google Sans` (Google Fonts link also loads Noto Sans and Castoro). Substitute: Product Sans, Inter.
- **Body:** `Noto Sans`, sans-serif; `scroll-behavior: smooth` on body.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`title is-1`) | 3rem | 600 | White on banner |
| Venue subtitle h2 | Bulma `subtitle` 1.25rem (inferred) | 400 | "Accepted at ICML 2025", white |
| Section h2 (`title is-3`) | 2rem | 600 | |
| Carousel caption h2 | `font-size: medium` (inline) | 400; lead-in bold | "Image Explanation.", "Audio Explanation." |
| Body | 1rem | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (Bulma rounded) |
| Poster thumbnail frame | 16px |
| Carousel cards | 12px; images inside 8px |
| Scrollbar thumb | 4px |

- **Shadows:** button hover `0 4px 15px rgba(0,0,0,0.1)`; carousel card hover `0 5px 20px rgba(0,0,0,0.08)`.
- **Motion:** buttons `cubic-bezier(0.4, 0, 0.2, 1)` 0.3s lift; ripple 0.6s; hero body fades in over 1s; modal content scales from 0.9; dots scale 1.2 on hover and 1.3 when active; a global `* { transition: color/background-color/border-color 0.3s }`.
- **Layout:** Bulma `container is-max-desktop` (960px); carousel items padded 20px; poster frame max 720px.

## Components

- **Smoked image hero.** `section.hero.is-medium` with inline `background-image` (cover, centered), `::before` overlay at `rgba(0,0,0,0.6)`, `.hero-body` raised above it with `z-index: 1`.
- **Dark pill link button.** Bulma `external-link button is-normal is-rounded is-dark` with lift, ripple and blue focus ring. Two rows: external resources, then four sub-page links to `static/content/*.html`.
- **Scale-coded caption.** Carousel caption where each wavelet scale is named in its own color (blue, red, yellow), matching the figure's overlays.
- **Hover-lift carousel card.** 12px radius, 20px padding, scale 1.01 and soft shadow on hover; inner image 8px radius scaling 1.02.
- **Poster modal.** 720px thumbnail in a 16px-radius, overflow-hidden frame with pointer cursor; click opens a Bulma `.modal` that slides in from scale 0.9.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | White on smoked banner |
| Venue badge | "Accepted at ICML 2025" subtitle | White text, no chip |
| Link buttons | ICML Poster, OpenReview, Code, Colab Notebook, plus four sub-page links | Dark rounded with motion |
| Teaser | Banner image is the teaser | |
| Abstract | Yes | Template |
| Method | "Motivation and proposed approach" | Figure plus text |
| Results | "Explanation of different modalities" carousel (image, audio, volume) | Scale-coded captions |
| Poster | Yes | Thumbnail opening a modal |
| Interactive demo | Colab notebook link | |
| Video / tables / sliders / 3D | No (template video and second carousel are commented out) | |
| BibTeX | Yes | Template pre |
| Acknowledgements | No | Footer credits the template |

## Do's and Don'ts

- Do keep the overlay at 0.6 so white text holds over a busy banner.
- Do color-code scales in captions with the same hues used in the figures.
- Do move long supplementary material to linked sub-pages and keep the main page short.
- Don't let the `.hero` overlay rule leak to other heroes; here it targets every `.hero`, which works only because the banner is the sole hero.
- Don't copy the global `*` transition and `img:hover` scale blindly; they animate every element.

## Surfaces

Dark image hero, then plain white sections and a white footer that tints `#f5f5f5` on hover.

## Imagery

Wavelet decompositions of images, audio spectrograms and 3D volumes; a wavelet-pattern banner; the ICML poster as a thumbnail.

## Layout

Single 960px Bulma column below a full-width medium hero; button rows wrap and center.

## Agent Prompt Guide

**Quick colors:** overlay `rgba(0,0,0,0.6)`, hero text `#ffffff`, text `#4a4a4a`, buttons `#363636`, scales `#2d50ff` / `#f44156` / `#ffdd00`, target `#078c14`.

1. "Build a medium hero with a cover background image and a `::before` overlay of `rgba(0,0,0,0.6)` that lightens to 0.5 on hover; set the 3rem Google Sans title, authors and links in white."
2. "Write a figure caption that names fine scales in `#2d50ff`, intermediate scales in `#f44156` and coarse scales in `#ffdd00`, with a bold lead-in like 'Image Explanation.'"
3. "Show a 720px poster thumbnail in a 16px-radius overflow-hidden frame with a pointer cursor; clicking opens a modal whose content scales in from 0.9 over 0.3s."

## Similar Pages

SmPO in this collection uses the same darkened-banner hero (at 50%); other Academic Project Page Template pages share the button row.

## Quick Start

```css
:root {
  --text: #4a4a4a; --title: #363636; --hero-text: #ffffff;
  --overlay: rgba(0,0,0,0.6); --overlay-hover: rgba(0,0,0,0.5);
  --scale-fine: #2d50ff; --scale-mid: #f44156; --scale-coarse: #ffdd00; --target: #078c14;
  --focus: rgba(0,123,255,0.25);
  --font-display: "Google Sans", "Inter", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --container: 960px;
}
.hero { position: relative; color: #fff; }
.hero::before { content: ""; position: absolute; inset: 0; background: var(--overlay); }
.hero .hero-body { position: relative; z-index: 1; }
```

## Provenance

- **URL:** https://gabrielkasmi.github.io/wam/
- **Paper:** One Wave To Explain Them All: A Unifying Perspective On Feature Attribution (arXiv 2410.01482), Gabriel Kasmi et al.
- **Venue:** ICML 2025 (subtitle "Accepted at ICML 2025").
- **Selection reason:** arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- **Template credit:** footer says it "was built using the Academic Project Page Template".
- **Measurement method:** `extract_style.py` plus manual reading of the inline style block, inline attributes and the customized `index.css`. Commented-out template leftovers (lorem-ipsum subtitle, "Another Carousel", video section, arXiv button) were excluded. Rendered page not viewed, so the banner image colors are not described.
