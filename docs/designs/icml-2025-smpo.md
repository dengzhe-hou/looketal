# Starfield Banner Bulma — Style Reference

> A cosmic fire-lion poster dimmed to half, with the paper title glowing white across it.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the banner, title, authors, buttons, teaser, abstract band, section titles, text and footer), the scaled full-page capture, and the page's own `static/css/index.css` over Bulma (Academic Project Page Template). The shared first-viewport capture caught the page before its banner and teaser images loaded (grey banner, broken teaser icon), so the color share and first-viewport description below come from a second 1440×900 capture taken 6 seconds after load. Positions are document coordinates at 1440px wide.

## Overview

SmPO keeps the Academic Project Page Template almost unchanged but replaces the plain hero with a full-bleed illustrated banner. A painting of a fiery, star-flecked lion on a deep night-sky background is dimmed by a 50% black overlay. Across it sit a three-line white Google Sans title at 48px, sky-blue author links (#209cee), white affiliations and venue with a soft text shadow, and four dark fully rounded pills (#363636). The banner ends abruptly at a white teaser band showing a 5-by-2 SDXL versus SmPO-SDXL sample grid with serif prompt captions. Then comes the template's #f5f5f5 abstract band with justified Noto Sans text, and white "Pipeline" and "Results" sections with left-aligned 32px titles, one large pipeline figure and sample grids. The only extra accent is an indigo (#4857dc) for the method name in running text.

## First Viewport

Color share of the 1440×900 first viewport, from the second capture with images loaded (median-cut quantization): white #ffffff 21.9%, near-black night #03000f 20.8%, plum #2f1d30 13.3%, warm sand #c1aaa1 12.9% (sample photos), rust #5f342c 11.6% (lion fur), taupe #827b73 10.3%, indigo night #130c2b 5.2%, linen #ebe6e2 3.9%. The banner covers y 0–455 (51% of the viewport); the white teaser band fills the rest. Before the images load, the banner shows as flat #7f7f7f (the 50% black overlay over the white page).

Anatomy in DOM order (y = top of element box):

1. **Banner** (`section.hero.banner`), y 0, height 455px, full width: `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(banner.png) center / cover`, `min-height: 30vh`, white text with `text-shadow: 0 1px 3px rgba(0,0,0,0.5)`.
2. **Title** (`h1.title.is-1.publication-title > span`), y 48, three centered lines in a 960px box, Google Sans 48px/600, line-height 54px, #ffffff (inline span color). Gap 24px.
3. **Authors** (`.publication-authors a`), y 234, one centered line, Google Sans 20px/400, #209cee names with white superscripts and commas. Gap 0.
4. **Affiliations**, y 269, one centered line, Google Sans 20px/400 #ffffff with superscript numerals. Gap 0.
5. **Venue**, y 303, "ICML 2025", Google Sans 20px/400 #ffffff. Gap 17px.
6. **Pills** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 350, 40px tall, Paper (PDF icon), 🤗 Hugging Face, Code (GitHub), arXiv (X-style Academicons mark); #363636 fill, white 16px Noto Sans. Banner ends at y 455.
7. **Teaser grid** (`section.hero.is-small img`), y 479, 960×441, two labelled rows (SDXL, SmPO-SDXL) of five samples with serif prompt captions beneath; no frame. The fold cuts the captions.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Night Overlay | rgba(0,0,0,0.5) | `.banner` gradient layer | Dimming layer over the banner image |
| Banner Night | #03000f | banner image | Dominant dark tone of the banner illustration |
| Title White | #ffffff | inline `color: white`, `.banner { color: white }` | Title, affiliations, venue, pill labels |
| Text Shadow | rgba(0,0,0,0.5) | `.banner` text-shadow | 0 1px 3px shadow under banner text |
| Author Sky | #209cee | `.publication-authors a` (hsl(204,86%,53%) !important) | Author names |
| Pill Dark | #363636 | Bulma `.is-dark` | Pill fill; section titles on white |
| Pill Hover | #2f2f2f | Bulma `.is-dark:hover` | Pill fill on hover |
| Graphite | #4a4a4a | Bulma `$text` | Body text, BibTeX text, footer |
| Light Section Ink | rgba(0,0,0,0.7) | Bulma `.hero.is-light` | "Abstract" title and text |
| Light Band | #f5f5f5 | Bulma `$light` | Abstract band, BibTeX `pre` |
| Method Indigo | #4857dc | inline `rgb(72,87,220)` | "SmPO-SDXL" in Results text |
| Link Blue | #3273dc | Bulma `$link` | Footer links |
| Footer Haze | #fafafa | Bulma footer | Footer band |
| White | #ffffff | page | Teaser band and white sections |

## Tokens — Typography

- **Body**: `index.css` sets `body { font-family: 'Noto Sans', sans-serif }`. Rendered: Noto Sans 400 (`fonts_loaded`); bold text is synthesized. Substitute: Open Sans (same humanist proportions).
- **Title, authors**: `'Google Sans', sans-serif` on `.publication-title` and `.publication-authors`. Rendered: Google Sans 400 only, so the 600 title is synthesized bold. Substitute: Albert Sans.
- **Captions inside figures**: serif type is baked into the images, not live text.
- **Icons**: Font Awesome (all.min) and Academicons.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title span` | 48px / 54px | 600 | #ffffff |
| Authors | `.publication-authors a` | 20px / 30px | 400 | #209cee |
| Affiliations, venue | `.publication-authors`, `.author-block` | 20px / 30px | 400 | #ffffff |
| Pill label | `.button.is-normal` | 16px / 24px | 400 | #ffffff |
| Section title | `h2.title.is-3` | 32px / 36px | 600 | #363636, rgba(0,0,0,0.7) in the band |
| BibTeX title | `h2.title` | 28px / 31.5px | 600 | #363636 |
| Body | `.content p`, section `p` | 16px / 24px | 400 | #4a4a4a |
| BibTeX | `pre` | 14px / 21px | 400 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill | 9999px (`is-rounded`) | 1px solid transparent | none |
| Banner | 0 | none | text-shadow `0 1px 3px rgba(0,0,0,0.5)` on its text |
| Teaser and figures | 0 | none | none |
| BibTeX `pre` | 0 | none | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop`, 960px at ≥1024px, centered (x 240–1200 at 1440px).
- **Banner**: hero-body padding 48px 24px; `min-height: 30vh` (270px at 900px tall), so content sets the height, 455px at 1440×900. Background `center / cover`, so the crop of the illustration changes with width.
- **Teaser band**: `section.hero.is-small`, hero-body padding 24px; image fills 960px.
- **Abstract band**: `section.section.hero.is-light`, padding 48px 24px, `.column.is-four-fifths` gives a 763px justified text column.
- **Pipeline and Results**: `hero is-small` sections, 24px padding, left-aligned 32px titles and 16px text across the full 960px, figures at 960px.
- **BibTeX**: `section.section` 48px 24px, `pre` padding 17.5px 21px.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | container 960px | 16px | 48px | as described |
| 769–1023px | 24px hero and section padding | 16px | 48px | container becomes fluid; banner crop narrows |
| ≤768px | 24px | 16px | 48px (no override in `index.css`) | abstract column goes full width; pills wrap; title wraps to more lines and the banner grows with it |

## Components

- **Illustrated banner hero**: full-width section with a two-layer background (`linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5))` over the image, `no-repeat center center / cover`), white centered text with `text-shadow: 0 1px 3px rgba(0,0,0,0.5)`. Authors stay #209cee for contrast against the dark overlay.
- **Dark pill**: `a.external-link.button.is-normal.is-rounded.is-dark`, 40px tall, padding 7px 20px, 5px vertical margins, #363636 fill, white Noto Sans 16px/400, icon left; hover #2f2f2f. On the dimmed banner they read as solid dark lozenges.
- **Comparison grid teaser**: one image with row labels set vertically on the left (SDXL, SmPO-SDXL) and prompt captions under each column, bold words marking the tested attributes.
- **Abstract band**: #f5f5f5 full width, centered 32px/600 title in rgba(0,0,0,0.7), justified 16px/24px text at 763px.
- **Plain section**: left-aligned 32px/600 #363636 title, a 16px #4a4a4a paragraph with the method name in #4857dc, then a 960px figure.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Illustrated hero banner | yes | half-dimmed full-bleed image with white type |
| Title, authors, affiliations, venue | yes | centered on the banner |
| Link buttons | yes | four dark rounded pills |
| Teaser | yes | before/after sample grid at 960px |
| Abstract | yes | #f5f5f5 band, justified |
| Method / pipeline figure | yes | one large two-step diagram |
| Results | yes | sample grids, conditional-generation grid |
| Results table | absent from the source | results are images |
| Navigation | absent from the source | none |
| BibTeX | yes | #f5f5f5 `pre` |
| Footer | yes | #fafafa template credit |

## Adapting to Other Content

- **Another banner image**: keep the 50% black overlay so white text stays legible on any illustration; choose art whose subject sits off-center so the title column stays readable.
- **More authors**: add lines; the banner grows because only `min-height` is set. Keep names #209cee and everything else white.
- **A results table**: in a white `hero is-small` section, Bulma `table is-fullwidth is-striped` at 16px Noto Sans, header #363636, method row name in #4857dc and bold.
- **News**: a short list inside the #f5f5f5 band above the abstract, date in 600 weight.
- **Long publication lists**: plain list in the 960px column, titles as #3273dc links.
- **More links**: stay with the #363636 pills; never invert them to white on the banner.

## Do's and Don'ts

- Do keep the banner overlay at rgba(0,0,0,0.5) and the text shadow on white text.
- Do keep author names #209cee even on the dark banner.
- Do let the comparison grid follow the banner directly with no heading.
- Do left-align section titles after the abstract, as the source does.
- Don't set a fixed banner height; `min-height: 30vh` plus content is what makes it work across sizes.
- Don't add more accent colors; #4857dc for the method name is the only one in the body.
- Don't ship the banner image without a dark fallback color; before load it shows as flat grey.

## Surfaces

A dark illustrated banner, then white. The abstract band and BibTeX block are #f5f5f5, and the footer is #fafafa. There are no cards or shadows.

## Imagery

A painterly, glowing lion-of-flames illustration on a starry night sky as the banner; photographic text-to-image samples in comparison grids with serif prompt captions; a flat pipeline diagram with pale blue and pale yellow panels, red crosses and green ticks.

## Layout

A full-bleed banner over a 960px centered column. The abstract is narrowed to 763px; other sections use the full column. Rendered height about 3,830px at 1440px, a short page.

## Agent Prompt Guide

Quick colors: banner overlay rgba(0,0,0,0.5) over the image, banner text #ffffff with rgba(0,0,0,0.5) shadow, authors #209cee, pills #363636 (hover #2f2f2f), body #4a4a4a, abstract band #f5f5f5, method name #4857dc, footer #fafafa.

1. "Build an illustrated hero: full-width section, `background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(banner.png) no-repeat center center; background-size: cover; min-height: 30vh`, padding 48px 24px, white text with `text-shadow: 0 1px 3px rgba(0,0,0,0.5)`. Centered Google Sans 48px/600 white title (line-height 54px) in a 960px column, 20px #209cee author links, 20px white affiliations and venue."
2. "Add dark pills: fully rounded, 40px tall, padding 7px 20px, #363636 fill, white Noto Sans 16px label with icon left, hover #2f2f2f, centered with small gaps."
3. "Follow with a #f5f5f5 abstract band: padding 48px 24px, centered 32px/600 'Abstract' in rgba(0,0,0,0.7), justified Noto Sans 16px/24px text in a 763px column; then white sections with left-aligned 32px/600 #363636 titles and 960px figures."

## Similar Pages

- Academic Project Page Template pages with a custom image banner instead of the plain white hero.
- Diffusion-alignment project pages that lead with before/after sample grids.

## Quick Start

```css
:root {
  --banner-overlay: rgba(0, 0, 0, 0.5);
  --banner-fallback: #03000f;
  --banner-text: #ffffff;
  --author: #209cee;
  --pill: #363636;
  --pill-hover: #2f2f2f;
  --text: #4a4a4a;
  --title: #363636;
  --light-ink: rgba(0, 0, 0, 0.7);
  --band: #f5f5f5;
  --method: #4857dc;
  --link: #3273dc;
  --footer: #fafafa;
  --font-body: 'Noto Sans', sans-serif;
  --font-display: 'Google Sans', 'Albert Sans', sans-serif;
  --container: 960px;
}
```

## Provenance

- **URL**: https://jaydenlyh.github.io/SmPO-project-page/
- **Paper**: Smoothed Preference Optimization via ReNoise Inversion for Aligning Diffusion Models with Varied Human Preferences (arXiv 2506.02698), Yunhong Lu, Qichao Wang, Hengyuan Cao, Xiaoyin Xu, Min Zhang (Zhejiang University).
- **Venue**: ICML 2025.
- **Selection reason**: existing verified entry in entries.json; the arXiv 2506.02698 comment says "Accepted by ICML 2025". Chosen for the full-bleed illustrated hero with a legible white title and dark pill links, the crisp before/after sample grid and the pipeline figure.
- **Template credit**: footer says the page was built using the Academic Project Page Template.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 (its screenshot caught the page before images loaded), a second 1440×900 capture 6 seconds after load for color share, targeted computed-style probes of the banner, authors, sections and footer, the scaled full-page capture, `index.css` and the HTML. Date 2026-10-28.
