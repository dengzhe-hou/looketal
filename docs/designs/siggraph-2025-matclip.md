# MatCLIP — Style Reference

> A materials catalogue laid out like a lab notebook: chair renders in neat 2×2 swatches, a soft peach arrow in the middle, and one gray band for the abstract.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the author block, figures, result carousels and controls, the 1440×900 and full-page screenshots, and the page's own `index.html` and `static/css/index.css` read directly. The page is the Academic Project Page Template (Bulma 0.9, Nerfies lineage). The labelled flow arrow and the boxed overview diagram are drawn inside images; the peach arrow colour is sampled from the 1440 screenshot.

## Overview

A white, centred Bulma page. The hero has a two-line Google Sans 48px/600 title in #363636, a 20px author line with #209cee names and superscripts, a three-line 20px block with two affiliations and "SIGGRAPH 2025" as plain text, and two dark pills (Paper (arXiv), Code (coming soon)). The teaser is a 912×276 image: a 2×2 grid of RGB chair renders from a diffusion model, a peach (#fcd0a1) trapezoid arrow labelled "MatCLIP", the matching 2×2 grid of PBR results, a thin black vertical rule, and a 2×2 comparison grid, with centred labels below; a four-line 20px Google Sans caption follows. The Abstract sits in a full-width #f5f5f5 band at 763px. Then the page widens: "Overview" is a left-aligned 32px heading over a 1344px boxed diagram (gray rounded panels, a blue network panel), followed by a 20px centred caption; three result carousels ("Result Videos", "Result Images (FLUX)", "Result Images (Stable Diffusion)") each show a target image and a rotating video side by side at 1334px; a Limitations section and a BibTeX `pre` close the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 70.5% (plus #fffffd and #fdffff 1.5%); mid gray #9d9a9c 7.9% (chair renders' studio backgrounds); umber #584d48 6.6% (dark chairs, title and button text); light gray #cbc8c5 6.0%; band gray #f7f7f7 4.8% (the top of the Abstract band entering at the bottom edge); cool gray #eceff1 2.6%. The peach arrow and blue links cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, centred inside `.container.is-max-desktop`, 960px at x=240):

1. **Hero** (`section.hero`, 0–436px): `.hero-body` padding 48px 24px.
2. **Title** (`h1.title.is-1.publication-title`, y=48, 108px, two lines): Google Sans 48px/600, line-height 54px, #363636. Gap 24px.
3. **Authors** (`div.is-size-5.publication-authors`, y=180, 35px): Google Sans 20px/400; names #209cee, superscripts and commas #4a4a4a. No gap.
4. **Affiliations and venue** (second `.publication-authors`, y=215, 99px): "¹King Abdullah University of Science and Technology, KSA", "²Miami University, USA", "SIGGRAPH 2025", each on its own line, Google Sans 20px/400 #4a4a4a. Gap 17px.
5. **Buttons** (`a.button.is-dark.is-rounded`, y=331, 40px): "Paper (arXiv)" with a PDF icon and "Code (coming soon)" with a GitHub icon; #363636 fill, white 16px Noto Sans, padding 7px 20px, 4px apart. Hero ends at 436.
6. **Teaser image** (`img.fit-picture`, x=264, y=436, 912×276): three 2×2 chair grids with a #fcd0a1 "MatCLIP" arrow between the first two and a black rule before the third; bold sans labels "Conditional LDM", "Our Result", "3DCoMPaT++" beneath. Gap 7px.
7. **Teaser caption** (`h2.subtitle`, y=719, 100px, four lines): Google Sans 20px/400 #4a4a4a, centred. Teaser section ends at 867, where the #f5f5f5 Abstract band begins.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, button text, carousel arrow fills |
| Title Charcoal | #363636 | (Bulma `$text-strong`, `$dark`) | title, section titles, button fills |
| Body Gray | #4a4a4a | (Bulma `$text`) | body text, captions, affiliations, venue, BibTeX text |
| Author Sky | #209cee | `hsl(204, 86%, 53%)` | author name links |
| Band Gray | #f5f5f5 | (Bulma `$light`) | Abstract band, BibTeX `pre` |
| Band Ink | rgba(0,0,0,0.7) | (Bulma `.hero.is-light`) | Abstract heading and text |
| Arrow Peach | #fcd0a1 | (image pixels, sampled) | "MatCLIP" flow arrow in the teaser |
| Dot Black | #000000 | (template `.slider-pagination .slider-page` override) | carousel pagination dots |
| Footer Gray | #fafafa | (Bulma `$scheme-main-bis`) | footer |
| Link Blue | #3273dc | (Bulma `$link`) | footer links |
| Control Shadow | rgba(50,50,50,0.1) | (bulma-carousel) | shadow under carousel arrows and dots |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`, `.teaser`) | Google Sans 400 (600 synthesized) | Product Sans |
| Text | 'Noto Sans', sans-serif (`body`) | Noto Sans 400 | Noto Sans |
| Code | monospace | system monospace | JetBrains Mono |
| Icons | Font Awesome (SVG via JS), Academicons | inline SVG | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1.title.is-1.publication-title` | 48px / 600 / 54px, Google Sans | #363636 |
| Section title | `h2.title.is-3` | 32px / 600 / 36px, Noto Sans; centred in the abstract, left-aligned in wide sections | #363636 (rgba(0,0,0,0.7) in the band) |
| Authors / affiliations / venue | `.publication-authors.is-size-5` | 20px / 400 / 30px, Google Sans | names #209cee, rest #4a4a4a |
| Teaser caption | `.teaser h2.subtitle` | 20px / 400 / 25px, Google Sans | #4a4a4a |
| Overview caption | `.hero.is-small h2.subtitle` | 20px / 400 / 25px, Noto Sans, centred | #4a4a4a |
| Body | section text and `.content p` | 16px / 400 / 24px; abstract and limitations justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| BibTeX | `pre` | 14px / 400 / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px | 1px solid transparent | none |
| Teaser, overview and result media | 0px | none | none |
| Carousel arrows | fully round, 42px | 1px solid #ffffff | rgba(50,50,50,0.1) 0px 2px 5px 0px |
| Carousel dots | fully round; 10px, active 14px | none | rgba(50,50,50,0.1) 0px 2px 5px 0px |
| BibTeX `pre` | 0px | none | none |

The overview's rounded gray panels, the blue architecture panel and the boxed teaser arrow are inside the images.

## Layout Metrics

- **Two widths**: hero, teaser, abstract and BibTeX use `.container.is-max-desktop` (960px, x=240); Overview, Result and Limitations sections use the plain `.container` (1344px at ≥1408px, x=48).
- **Hero**: padding 48px 24px; title margin-bottom 24px; author block 35px; affiliation block 99px; button column padding 12px with 5px link margins; hero 436px.
- **Teaser**: `.teaser .hero-body { padding-top: 0; padding-bottom: 3rem }` → image at y=436, 912px wide; caption 7px below; section ends at 867.
- **Abstract band**: `section.section.hero.is-light`, #f5f5f5, padding 48px 24px, `.column.is-four-fifths` → 763px justified text; band 867–1359.
- **Overview**: `section.hero.is-small`, padding 24px; left-aligned h2 at y=1383; diagram 1344×536 at y=1443; 20px centred caption below.
- **Result carousels**: `.results-carousel .item { margin: 5px; padding: 20px }` → 1334px items; inside, `.media-container` is a flex row with a 10px gap and two `.media-item` children at 50% (target image 647px, video 637px with its controls). Arrows 42px at the container edges; dots under each carousel.
- **BibTeX**: `section.section` padding 48px 24px, `pre` padding 17.5px 21px.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | wide container 1344px; is-max-desktop 960px | 16px | 48px | as described |
| 1216–1407px | wide container 1152px | 16px | 48px | result items narrower |
| 1024–1215px | wide container 960px | 16px | 48px | wide and narrow sections become the same width |
| ≤1023px | fluid, 24px padding | 16px | 48px | images scale |
| ≤768px | 24px | 16px | 48px | Bulma columns stack; the image/video pair stays side by side (flex row) |

## Components

- **Author block**: centred Google Sans 20px/400, #209cee names with #4a4a4a superscripts; affiliations one per line, and the venue as a plain final line in the same style.
- **Dark pill button** (`.button.is-normal.is-rounded.is-dark`): #363636, white 16px Noto Sans, height 40px, padding 7px 20px, radius 290486px, icon at left.
- **Teaser figure** (in the image): 2×2 swatch grids of chair renders on gray studio backgrounds, about 112px per tile at display size with about 5px white gutters (measured on the 1440 screenshot); a #fcd0a1 trapezoid arrow with the method name in black sans; a 2px black vertical rule before the baseline grid; bold black labels below each grid.
- **Gray abstract band** (`section.section.hero.is-light`): #f5f5f5 full width, centred 32px/600 heading in rgba(0,0,0,0.7), 763px justified text.
- **Wide section** (`section.hero.is-small` with `.container`): left-aligned 32px/600 #363636 heading, a 16px intro paragraph across 1344px, then the figure or carousel.
- **Image/video pair carousel**: Bulma Carousel, one item per slide; each item has 20px padding and a flex row (gap 10px) of the target image and a looping autoplay video with controls, each 50% wide; white 42px round arrows with shadow rgba(50,50,50,0.1) 0px 2px 5px 0px; black dots 10px, active 14px.
- **BibTeX**: Bulma `pre` #f5f5f5, padding 17.5px 21px, 14px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | centred Bulma hero |
| Venue | present but non-standard | "SIGGRAPH 2025" as the last line of the affiliation block |
| Link buttons | yes | two dark pills |
| Teaser | yes | 912px labelled flow figure with peach arrow |
| Abstract | yes | gray full-width band, 763px text |
| Overview diagram | yes | 1344px boxed diagram, left-aligned heading, centred caption |
| Results carousels | yes | three image/video pair carousels at 1334px |
| Limitations | yes | justified paragraph and figure |
| Results tables | absent from the source | results are visual only |
| BibTeX | yes | Bulma `pre` |
| Footer | yes | #fafafa, template credit |

## Adapting to Other Content

- **More authors**: keep the 20px Google Sans line in the 960px hero; it wraps centred at about six names; keep affiliations one per line and the venue last.
- **A results table**: place it in a wide `section.hero.is-small` under a left-aligned 32px/600 heading, inside the 1344px container; Bulma table at 16px, header 600 #363636, 1px #dbdbdb rules, best value bold.
- **Long publication or news lists**: a wide section with a left-aligned 32px heading and a 16px list; or a gray `is-light` band at 763px for a short list.
- **More comparisons**: compose them like the teaser (2×2 swatch grids, a #fcd0a1 labelled arrow for the method, a thin black rule before baselines, bold labels below) at 912px.
- **More results**: add items to an image/video pair carousel; each item is one target and one video at 50% each.

## Do's and Don'ts

- Do keep the hero and abstract narrow (960px and 763px) and let Overview and Results run at the wide 1344px container.
- Do left-align the wide-section headings and centre the hero, teaser and abstract headings.
- Do use the soft peach #fcd0a1 only for the method's arrow in figures.
- Do pair each target image with its result video side by side in carousels.
- Don't add colour to HTML text beyond the #209cee author links; the colour lives in the renders.
- Don't add more gray bands; only the Abstract is tinted.
- Don't frame the media; images and videos sit directly on white.

## Surfaces

White page with one full-width #f5f5f5 Abstract band; #f5f5f5 also in the BibTeX `pre`; #fafafa footer. The overview diagram brings its own light gray rounded panels and a pale blue network panel.

## Imagery

Product-style renders of chairs, sofas and furniture on neutral gray studio backgrounds, before and after material assignment; a technical overview diagram with gray rounded panels, Blender logos and a pale blue architecture box; FLUX and Stable Diffusion target images paired with turntable videos.

## Layout

A centred 960px hero and teaser, a full-width gray Abstract band, then wide 1344px sections (Overview, Result Videos, Result Images ×2, Limitations) with left-aligned headings, and a 960px BibTeX.

## Agent Prompt Guide

Quick colors: background #ffffff, band #f5f5f5, title #363636, body #4a4a4a, authors #209cee, pills #363636, arrow #fcd0a1, carousel dots #000000, footer #fafafa.

1. "Build a centred Bulma hero in a 960px container, padding 48px 24px: title Google Sans 48px/600 #363636 on two lines; authors Google Sans 20px with #209cee names; a second 20px #4a4a4a block with one affiliation per line and 'SIGGRAPH 2025' as the last line; two dark pills (#363636, white 16px Noto Sans, padding 7px 20px, radius 290486px)."
2. "Make a teaser figure 912px wide: a 2×2 grid of input renders, a #fcd0a1 trapezoid arrow labelled with the method name in black sans, the 2×2 grid of results, a 2px black vertical rule, a 2×2 baseline grid, and bold labels under each grid; below it a centred Google Sans 20px/400 #4a4a4a caption."
3. "Create a wide results section (container 1344px): a left-aligned Noto Sans 32px/600 #363636 heading, a 16px intro paragraph, and a carousel whose items (padding 20px) hold a flex row with a 10px gap of a target image and a looping video at 50% each; white 42px round arrows with shadow rgba(50,50,50,0.1) 0px 2px 5px 0px and #000000 dots."

## Similar Pages

- Academic Project Page Template pages that switch between the narrow and the wide Bulma container.
- Material, texture and appearance papers that present before/after swatch grids.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --band: #f5f5f5;
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --pill: #363636;
  --arrow: #fcd0a1;
  --dot: #000000;
  --footer: #fafafa;
  --font-display: "Google Sans", sans-serif;
  --font-text: "Noto Sans", sans-serif;
  --container-narrow: 960px;
  --container-wide: 1344px;
  --radius-pill: 290486px;
}
```

## Provenance

- **URL**: https://birsakm.github.io/matclip/
- **Paper**: MatCLIP: Light- and Shape-Insensitive Assignment of PBR Material Models (arXiv 2501.15981), Michael Birsak, John Femiani, Biao Zhang, Peter Wonka.
- **Venue**: SIGGRAPH 2025 (Conference Track); the arXiv comment states "Accepted at SIGGRAPH 2025 (Conference Track)".
- **Selection reason**: a clear teaser with a labelled flow arrow, a well-boxed overview diagram and large result videos; clean, if template-based.
- **Template credit**: footer credits the Academic Project Page Template, adapted from Nerfies (Bulma 0.9, Bulma Carousel, Font Awesome, Academicons).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, pixel sampling of the teaser arrow, the 1440×900 and full-page screenshots, and the page's `index.html` and `static/css/index.css` read directly, on 2026-10-28.
