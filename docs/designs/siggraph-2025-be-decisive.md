# Be Decisive — Style Reference

> A Nerfies page that learned to write by hand: every prompt is a crayon-coloured caption, and each coloured word points at its subject in the picture.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the author lines, teaser, carousel, figures and footer, the 1440×900 and full-page screenshots, and the page's own `index.html` and `static/css/index.css` read directly. The page is the Nerfies template (Bulma 0.9) with its stock stylesheet. Its distinguishing handwritten, colour-coded prompt captions are not HTML text: they are drawn into the teaser and result JPEGs, so no CSS colour or font can be quoted for them; the values given for them are sampled from image pixels.

## Overview

A white, centred, single-column Nerfies page. The hero has a two-line 48px/600 Google Sans title in #363636, sky-blue author links with superscripts, a gray affiliation line, a 32px/600 "SIGGRAPH 2025" line set as a second `h1.title`, and two dark rounded pills (arXiv, Code). The teaser is one 912px-wide image: two prompt groups, each with a handwritten caption in which the subject nouns are coloured (blue (#1078c0) for "sea turtle", "jellyfish", "octopus"; green (#58a840) for "three ginger kittens", "brown dog"), above generated images and rows of coloured layout masks. Two 20px Google Sans subtitle paragraphs follow. A full-container (1344px) carousel shows one strip of six lake scenes at a time under a handwritten caption with "sailboat", "motorboat" and "kayak" in #4070c0 blue, #e87830 orange and #70a848 green. Then come a 763px justified Abstract, "Noise-Induced Layouts" and "How does it work?" sections with images capped at 800px and 600px, and a BibTeX block in a #f5f5f5 `pre`.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 70.9% (plus #f0f3f3 3.2%, #fdffff and #fffffd 1.3%); dark navy-gray #263038 7.7% (title text, buttons and the underwater images); olive gray #6c7369 7.1% and sage #98b09f 5.3% (the kitten photos and mask rows); warm beige #d6cbbe 4.6%. The handwritten caption colours are too small to form clusters.

Anatomy in DOM order (desktop 1440px, everything centred inside `.container.is-max-desktop`, 960px at x=240):

1. **Hero** (`section.hero`, 0–455px): `.hero-body` padding 48px 24px.
2. **Title** (`h1.title.is-1.publication-title`, y=48, 108px, two lines): Google Sans 48px/600, line-height 54px, #363636. Gap 24px.
3. **Authors** (`div.is-size-5.publication-authors`, y=180, 35px): Google Sans 20px/400, names #209cee, superscripts 16.67px #4a4a4a; author blocks separated by spaces only. No gap.
4. **Affiliations** (y=215, 35px): "¹Tel-Aviv University ²Snap Research", Google Sans 20px/400 #4a4a4a. Gap 23px.
5. **Venue line** (`h1.title`, y=273, 36px): "SIGGRAPH 2025", Noto Sans 32px/600 #363636 (Bulma `.title` default size). Gap 41px (column padding plus link margins).
6. **Buttons** (`a.button.is-dark.is-rounded`, y=350, 40px): arXiv (X-logo icon) and "Code (coming soon)" (GitHub icon); #363636 fill, white 16px Noto Sans, padding 7px 20px, fully rounded, 4px apart. Hero ends at 455.
7. **Teaser image** (`.teaser img`, y=455, 912×355): one JPEG with two handwritten, colour-coded prompt captions, four generated images and four rows of mask thumbnails. Gap 7px.
8. **Teaser subtitle** (`h2.subtitle`, y=817, 50px): Google Sans 20px/400 #4a4a4a, centred, "''Be Decisive''" in bold. Gap 24px.
9. **Second subtitle** (`h3.subtitle`, y=891, 75px): same 20px/400 #4a4a4a, centred, three lines. Teaser section ends at 1014.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, button text, carousel arrow and dot fills |
| Title Charcoal | #363636 | (Bulma `$text-strong`, `$dark`) | paper title, venue line, section titles, button fills |
| Body Gray | #4a4a4a | (Bulma `$text`) | body text, subtitles, affiliations, superscripts, BibTeX text, footer text |
| Author Sky | #209cee | `hsl(204, 86%, 53%)` | author name links |
| Code Well | #f5f5f5 | (Bulma `$white-ter`) | BibTeX `pre` |
| Footer Gray | #fafafa | (Bulma `$scheme-main-bis`) | footer |
| Link Blue | #3273dc | (Bulma `$link`) | footer links |
| Control Shadow | rgba(50,50,50,0.1) | (bulma-carousel literal) | shadow under carousel arrows and dots |
| Caption Ink | #111111 | (image pixels, sampled) | handwritten caption text inside the teaser and carousel images |
| Caption Blue | #1078c0 | (image pixels, sampled from the 1440 shot) | coloured subject words in the teaser's ocean caption |
| Caption Green | #58a840 | (image pixels, sampled from the 1440 shot) | coloured subject words in the teaser's kitten caption |
| Slate Blue | #4070c0 | (image pixels, sampled from `results/0.jpeg`) | "sailboat" in the first carousel caption |
| Caption Orange | #e87830 | (image pixels, sampled from `results/0.jpeg`) | "motorboat" in the first carousel caption |
| Leaf Green | #70a848 | (image pixels, sampled from `results/0.jpeg`) | "kayak" in the first carousel caption |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`, `.teaser`) | Google Sans 400 (600 synthesized) | Product Sans |
| Text | 'Noto Sans', sans-serif (`body`) | Noto Sans 400 | Noto Sans |
| Handwriting | none (inside images) | rasterized in the JPEGs; a rounded marker hand | Patrick Hand |
| Code | monospace | system monospace | JetBrains Mono |
| Icons | Font Awesome (SVG via `fontawesome.all.min.js`), Academicons | Academicons 400; Font Awesome rendered as inline SVG | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 600 / 54px, Google Sans | #363636 |
| Venue line | `h1.title` | 32px / 600 / 36px, Noto Sans | #363636 |
| Section title | `h2.title.is-3` | 32px / 600 / 36px, Noto Sans | #363636 |
| Authors / affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px, Google Sans; sup 16.67px | names #209cee, rest #4a4a4a |
| Teaser subtitle | `.teaser h2.subtitle`, `h3.subtitle` | 20px / 400 / 25px, Google Sans | #4a4a4a |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| BibTeX | `pre` | 14px / 400 / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px | 1px solid transparent | none |
| Carousel arrows (`.slider-navigation-previous/next`) | fully round, 42px | 1px solid #ffffff | rgba(50,50,50,0.1) 0px 2px 5px 0px |
| Carousel dots (`.slider-page`) | fully round; 10px, active 14px | none | rgba(50,50,50,0.1) 0px 2px 5px 0px |
| Teaser, carousel and method images | 0px | none | none |
| BibTeX `pre` | 0px | none | none |

`.results-carousel .item` declares a 1px solid #bbb border and 10px radius, but the carousel children here are bare `<img>` elements without the `.item` class, so no border or radius renders.

## Layout Metrics

- **Containers**: `.container.is-max-desktop` max-width 960px (x=240–1200) for hero, teaser and text sections; the carousel uses the plain `.container`, 1344px at ≥1408px (x=48–1392).
- **Hero**: `.hero-body` padding 48px 24px; title margin-bottom 24px; hero total 455px.
- **Teaser**: `.teaser .hero-body { padding-top: 0; padding-bottom: 3rem }` → image directly at y=455, 912px wide (960 minus 24px padding each side); section ends at 1014.
- **Carousel**: `section.hero.is-small .hero-body` padding 24px; one slide shown (`data-slides-to-show="1"`), each slide image 1344×282; arrows 42px at the container edges, vertically centred (margin-top -20px); pagination row 26px tall at the bottom with 8px 16px padding and 3px dot margins.
- **Abstract**: `section.section` padding 48px 24px; `.column.is-four-fifths` → 763px justified text at x=338.
- **Method sections**: `section.hero.is-small`, padding 24px; text full 912px, justified; figures `img.my-image` with inline widths 800px and 600px (the `.my-image { width: 70% }` rule is overridden by the inline style), a later figure renders 960px.
- **BibTeX**: `section.section.is-light` padding 48px 24px on white (Bulma has no `.section.is-light` fill); `pre` padding 17.5px 21px.
- **Footer**: #fafafa, padding 48px 24px 96px, 888px text column.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | carousel container 1344px; is-max-desktop 960px | 16px | 48px | as described |
| 1216–1407px | carousel 1152px | 16px | 48px | same |
| 1024–1215px | carousel 960px | 16px | 48px | same |
| ≤1023px | containers fluid with 24px padding | 16px | 48px | images scale to column width |
| ≤768px | 24px | 16px | 48px | abstract column full width; button row wraps |

## Components

- **Author line**: centred `div.is-size-5.publication-authors` in Google Sans 20px/400; names #209cee (`!important`, hover underline) with 16.67px #4a4a4a superscripts; affiliations on the next line with the same size and gray, superscript numbers before each institution.
- **Venue line**: a plain `h1.title` "SIGGRAPH 2025" in Noto Sans 32px/600 #363636, centred, no badge.
- **Dark pill button** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, white 16px/400 Noto Sans, height 40px, padding 7px 20px, radius 290486px, 1px transparent border, icon at left (X logo, GitHub), 4px between pills.
- **Handwritten prompt caption** (inside the image): a centred two-line quote in a rounded marker hand, near-black #111111 with each subject noun coloured (#1078c0, #58a840 in the teaser; #4070c0, #e87830, #70a848 in the carousel) to match the coloured mask in the layout thumbnails below; the caption sits directly over its image group with about 10px of space.
- **Result carousel**: Bulma Carousel, one 1344×282 strip of six images per slide; 42px white round arrows with 1px white border and shadow rgba(50,50,50,0.1) 0px 2px 5px 0px; white dots 10px, active 14px.
- **Teaser subtitle**: `h2.subtitle` / `h3.subtitle` centred, Google Sans 20px/400 #4a4a4a, the method name bold in doubled quotes.
- **BibTeX**: centred `h2.title.is-3` then `pre` #f5f5f5, padding 17.5px 21px, 14px monospace #4a4a4a.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | centred Nerfies hero, Google Sans, sky-blue names |
| Venue | present but non-standard | a second `h1.title` at 32px/600, not a badge |
| Link buttons | yes | two dark Bulma pills |
| Teaser | yes | one 912px composite image with handwritten coloured captions |
| Teaser summary | yes | two centred 20px Google Sans subtitles |
| Results carousel | yes | full-container one-slide carousel with white round controls |
| Abstract | yes | 763px justified Noto Sans |
| Method sections | yes | centred 32px titles, justified text, 600–800px figures |
| Video | absent from the source | the template's paper-video block is commented out |
| Results tables | absent from the source | results are image strips only |
| BibTeX | yes | Bulma `pre` on white |
| Footer | yes | #fafafa, Nerfies credit and source link |

## Adapting to Other Content

- **More authors**: keep the 20px Google Sans line at 960px; it wraps centred at about seven names per line. Keep superscripts at 16.67px #4a4a4a.
- **A results table**: place it in a `section.hero.is-small` inside the 960px container; Bulma table at 16px Noto Sans, header 600 #363636, 1px #dbdbdb row rules, best value bold. Do not colour cells; colour belongs to the handwritten captions.
- **Long publication or news lists**: a `section.section` with a centred 32px/600 title and a left-aligned 16px list in the 912px column, dates bold #363636.
- **New figures with prompts**: draw the prompt above the image in the same marker hand with each subject noun in its mask colour, and export it as part of the image at the column width (912px for the teaser, 800px for method figures). Keep 3–4 hues and reuse them for the matching masks.
- **More results**: add slides to the one-up carousel; each slide is one wide strip (1344px at 1440).

## Do's and Don'ts

- Do colour-code each subject word in a prompt caption with the same hue as its mask or region in the image below.
- Do keep captions handwritten and inside the image, so they read as annotations rather than UI text.
- Do keep the hero plain: Google Sans 48px title, 20px authors, a 32px venue line and two dark pills.
- Do run the results carousel at full container width (1344px at 1440) with one strip per slide.
- Don't add borders, radii or shadows to figures; the images sit directly on white.
- Don't add accent colours to the HTML text; the only coloured HTML text is the #209cee author links.
- Don't set body text in Google Sans; only the title, authors and teaser subtitles use it.

## Surfaces

White everywhere; #f5f5f5 only inside the BibTeX `pre`; #fafafa footer. The colour on the page comes from the generated images and the handwritten captions inside them.

## Imagery

Generated multi-subject scenes (sea creatures, kittens and a dog, boats on a lake, astronauts and robots) shown as square tiles with rows of semi-transparent coloured layout masks beneath them, each group under a handwritten prompt whose subject nouns are coloured to match. Method figures are mask overlays and diagrams on white.

## Layout

A centred Nerfies column: a 455px hero, a 912px teaser with two subtitle paragraphs, a full-width 1344px carousel that breaks out of the 960px column, then Abstract, two method sections and BibTeX at 960px, each section padded 24–48px.

## Agent Prompt Guide

Quick colors: background #ffffff, title #363636, body #4a4a4a, authors #209cee, code well #f5f5f5, footer #fafafa; caption hues in images #1078c0 / #58a840 (teaser) and #4070c0 / #e87830 / #70a848 (carousel) on #111111.

1. "Build a centred Nerfies hero inside a 960px container, padding 48px 24px: title Google Sans 48px/600 line-height 54px #363636; authors Google Sans 20px with names #209cee and 16.67px #4a4a4a superscripts; affiliations 20px #4a4a4a; a plain 32px/600 #363636 venue line; dark pills (#363636, white 16px Noto Sans, padding 7px 20px, radius 290486px) with icons."
2. "Make a teaser figure: one 912px image whose top carries a handwritten two-line prompt in a marker hand, #111111 with each subject noun coloured #1078c0 or #58a840 to match its mask in the thumbnails below; under it two centred Google Sans 20px/400 #4a4a4a subtitles, the method name bold."
3. "Add a one-slide results carousel at full container width (1344px): each slide one wide strip of six images, a handwritten coloured prompt above; white 42px round arrows with a 1px white border and shadow rgba(50,50,50,0.1) 0px 2px 5px 0px; white dots 10px, active 14px."

## Similar Pages

- Nerfies-template pages for text-to-image papers that annotate prompts directly in the figures.
- Pages that link caption words to image regions by colour (layout, grounding and segmentation papers).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --code-well: #f5f5f5;
  --footer: #fafafa;
  --link: #3273dc;
  --caption-ink: #111111;
  --caption-blue: #1078c0;
  --caption-green: #58a840;
  --caption-orange: #e87830;
  --font-display: "Google Sans", sans-serif;
  --font-text: "Noto Sans", sans-serif;
  --font-hand: "Patrick Hand", cursive;
  --container: 960px;
  --radius-pill: 290486px;
}
```

## Provenance

- **URL**: https://omer11a.github.io/be-decisive/
- **Paper**: Be Decisive: Noise-Induced Layouts for Multi-Subject Generation (arXiv 2505.21488), Omer Dahary, Yehonathan Cohen, Or Patashnik, Kfir Aberman, Daniel Cohen-Or.
- **Venue**: SIGGRAPH 2025 (the page shows "SIGGRAPH 2025"; the arXiv comment reads "SIGGRAPH 2025. Project page ...", a weak acceptance wording flagged in selection).
- **Selection reason**: a Nerfies base made distinctive by handwritten, colour-coded prompt captions that tie the text to the images, plus a full-width carousel and well-paced sections.
- **Template credit**: footer states the website source code is based on the Nerfies project page (Bulma 0.9, Bulma Carousel, Font Awesome, Academicons).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and the page's `index.html` and `static/css/index.css` read directly, on 2026-10-28. Caption colours are sampled from the 1440 screenshot and from `static/images/results/0.jpeg` because they are part of the images.
