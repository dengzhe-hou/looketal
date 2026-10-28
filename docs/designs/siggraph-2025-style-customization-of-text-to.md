# CustomSVG — Style Reference

> A sticker sheet pinned to a white wall: rows of flat orange, red and violet icons, each with a handwritten label, ruled off by dashed lines.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the author lines, figures, BibTeX heading and footer, the 1440×900 and full-page screenshots, and the page's own `index.html` and `static/css/index.css` read directly. The page is the Nerfies template (Bulma 0.9). The captioned icon grids, handwritten labels and dashed dividers that give it its look are all inside two PNGs (`teaser.png`, `result.png`), not HTML; their colours are sampled from the 1440 screenshot. The BibTeX entry is commented out in the markup, so its `pre` renders empty.

## Overview

A short, white, centred Nerfies page (3705px tall at 1440). The hero has a two-line Google Sans 48px/600 title in #363636, a 20px author line with #209cee names and superscripts, a 20px affiliation line, and three dark rounded pills (Paper, Code, "More SVG Results ⭐️" with the emoji inside the label). The teaser is a 912px-wide figure: on the left a column of three exemplar style icons, a dashed vertical rule, then a 7×3 grid of generated icons with handwritten quoted prompts above each column ("boy", "house", "camera" …), the last column boxed with thin gray frames and dashed sub-dividers showing path layers; bold sans labels "(a) Exemplar Style" and "(b) Style Customization of Text-to-Vector Generation" sit under it. A 20px Google Sans caption follows. Then come a 763px justified Abstract, a Methods section with a 936px pipeline diagram and justified caption, a Results section with one 936×1027 grid image of pixel-art, cartoon and flat icons ruled by dashed lines and lifted by a soft 2px shadow, an empty BibTeX block and a #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 78.6% (plus #faf5ee 1.7%, #fdffff and #fffffc 1.6%); taupe #997f76 5.4% and dark brown #5c3635 5.0% (icon outlines and filled shapes blended); sand #d2bfa3 4.4%; light gray #e6e9eb 3.4%. Sampled saturated icon fills in the teaser are dominated by amber #f0a030 (about 40% of coloured pixels), then vermilion #e04000, coral #e05040, orchid #c050a0 and cornflower #5060c0.

Anatomy in DOM order (desktop 1440px, centred inside `.container.is-max-desktop`, 960px at x=240):

1. **Hero** (`section.hero`, 0–371px): `.hero-body` padding 48px 24px.
2. **Title** (`h1.title.is-1.publication-title`, y=48, 108px, two lines): Google Sans 48px/600, line-height 54px, #363636. Gap 24px.
3. **Authors** (`div.is-size-5.publication-authors`, y=180, 35px): Google Sans 20px/400; names #209cee, superscripts and commas #4a4a4a; a trailing comma after the last name. No gap.
4. **Affiliations** (y=215, 35px): "¹City University of Hong Kong, ²Adobe Research", Google Sans 20px/400 #4a4a4a. Gap 16px.
5. **Buttons** (`a.button.is-dark.is-rounded`, y=266, 40px): Paper (`fa-file-pdf`), Code (`fa-github`), "More SVG Results ⭐️" (image icon); #363636 fill, white 16px/400 Noto Sans, padding 7px 20px, fully rounded, 4px apart. Hero ends at 371.
6. **Teaser figure** (`img#teaser.interpolation-image`, x=264, y=371, 912×357): icon grid PNG with handwritten labels and dashed dividers. Gap 8px.
7. **Teaser caption** (`h2.subtitle`, y=736, 50px): Google Sans 20px/400 #4a4a4a, centred, two lines. Teaser section ends at 833.
8. **Abstract** (`h2.title.is-3`, y=882): Noto Sans 32px/600 #363636, centred; begins just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, button text |
| Title Charcoal | #363636 | (Bulma `$text-strong`, `$dark`) | paper title, section titles, button fills |
| Body Gray | #4a4a4a | (Bulma `$text`) | body text, subtitles, affiliations, superscripts, footer text |
| Author Sky | #209cee | `hsl(204, 86%, 53%)` | author name links |
| Code Well | #f5f5f5 | (Bulma `$white-ter`) | empty BibTeX `pre` |
| Footer Gray | #fafafa | (Bulma `$scheme-main-bis`) | footer |
| Icon Amber | #f0a030 | (image pixels, sampled) | dominant fill of the teaser icons (crowns, baskets, folders) |
| Icon Vermilion | #e04000 | (image pixels, sampled) | red-orange fills in the teaser icons |
| Icon Orchid | #c050a0 | (image pixels, sampled) | magenta and violet fills (boy's hair, trophy, gift ribbon) |
| Icon Cornflower | #5060c0 | (image pixels, sampled) | blue-violet fills (camera, trophy base, basket) |
| Figure Shadow | rgba(0,0,0,0.2) | (`.shadow-style` in index.css: `box-shadow: 0 2px 4px rgba(0,0,0,0.2)`) | 0px 2px 4px 0px shadow under the Results grid image |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`, `.teaser`) | Google Sans 400 (600 synthesized) | Product Sans |
| Text | 'Noto Sans', sans-serif (`body`) | Noto Sans 400 | Noto Sans |
| Figure labels | none (inside images) | a handwritten marker hand for prompts; bold sans for "(a)" and "(b)" labels | Gochi Hand |
| Icons | Font Awesome (SVG via JS) | inline SVG; Academicons CSS linked | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 600 / 54px, Google Sans | #363636 |
| Section title | `h2.title.is-3` | 32px / 600 / 36px, Noto Sans | #363636 |
| BibTeX title | `#BibTeX h2.title` | 28px / 600 / 31.5px, left-aligned | #363636 |
| Authors / affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px, Google Sans | names #209cee, rest #4a4a4a |
| Teaser caption | `.teaser h2.subtitle` | 20px / 400 / 25px, Google Sans | #4a4a4a |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px | 1px solid transparent | none |
| Teaser and pipeline images | 0px | none | none |
| Results grid image (`img.shadow-style`) | 0px | none | rgba(0,0,0,0.2) 0px 2px 4px 0px |
| BibTeX `pre` | 0px | none | none |

The dashed dividers and thin gray frames are drawn in the PNGs, not with CSS borders.

## Layout Metrics

- **Containers**: `.container.is-max-desktop` 960px (x=240–1200) for every section; footer `.container` 1344px with an `is-8` column (888px text).
- **Hero**: padding 48px 24px; title margin-bottom 24px; author and affiliation lines 35px each; button row in a `.column` (12px padding) with 5px link margins; hero 371px tall.
- **Teaser**: `.teaser .hero-body { padding-top: 0; padding-bottom: 3rem }` → image at y=371, 912px wide; caption 8px below; section ends at 833.
- **Abstract**: `section.section` padding 48px 24px; `.column.is-four-fifths` → 763px justified text at x=338.
- **Methods**: a bare `<section>` (no padding) with a `.column.is-full-width` → pipeline image 936px at x=252, caption justified at the same width.
- **Results**: `section.section`, `.columns.is-variable` with -12px margins → grid image 936×1027 at x=252.
- **Footer**: padding 48px 24px 96px; two centred 25px icon links above the licence text.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | is-max-desktop 960px | 16px | 48px | as described |
| ≤1023px | container fluid, 24px section padding | 16px | 48px | figures scale with the column |
| ≤768px | 24px | 16px | 48px | Bulma columns stack; abstract full width; button row wraps |

## Components

- **Dark pill button** (`.button.is-normal.is-rounded.is-dark`): #363636, white 16px/400 Noto Sans, height 40px, padding 7px 20px, radius 290486px, icon at left; the third label ends with an emoji ⭐️.
- **Author line**: centred Google Sans 20px/400, #209cee names with #4a4a4a superscript numbers and commas; affiliations on the next line with superscripts before each institution.
- **Captioned icon grid** (in the image): square flat icons about 80px at display size in equal columns; each column headed by a quoted, handwritten prompt in near-black; exemplar column split from results by a dashed vertical rule; extra columns framed by 1px gray boxes with dashed internal dividers; bold sans panel labels "(a) …" and "(b) …" below.
- **Results grid** (in the image): rows of icons in different styles (pixel art, cartoon, flat) with handwritten quoted labels under each icon, cells separated by dashed lines; the image carries `box-shadow: rgba(0,0,0,0.2) 0px 2px 4px 0px`.
- **Section heading**: Noto Sans 32px/600 #363636, centred, 24px below.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | centred Nerfies hero |
| Venue | absent from the source | no venue line or badge on the page |
| Link buttons | yes | three dark pills, one with an emoji |
| Teaser | yes | captioned icon grid PNG with dashed dividers |
| Abstract | yes | 763px justified text |
| Method figure | yes | 936px pipeline diagram with justified caption |
| Results gallery | yes | one 936px grid image with a soft shadow |
| Video / carousel | absent from the source | carousel scripts are loaded but unused |
| Results tables | absent from the source | results are icon grids only |
| BibTeX | present but non-standard | heading and gray `pre` render, but the entry is commented out so the block is empty |
| Footer | yes | #fafafa, icon links and licence text |

## Adapting to Other Content

- **More authors**: keep the 20px Google Sans line at 960px; it wraps centred at about seven names per line.
- **A results table**: in a `section.section` at 960px, Bulma table 16px Noto Sans, header 600 #363636, 1px #dbdbdb rules; illustrate rows with small icons (32px) instead of colour fills, matching the icon-led visual system.
- **Long publication or news lists**: a centred 32px/600 heading and a left-aligned 16px list in the 912px column; no cards.
- **More result figures**: compose them as grids in the same manner as the source (square icons on white, handwritten quoted prompt per cell, dashed dividers), export at 936px wide for a section or 912px for the teaser, and give gallery images the rgba(0,0,0,0.2) 0px 2px 4px 0px shadow.
- **A venue**: add a plain centred Google Sans 20px #4a4a4a line under the affiliations rather than a badge.

## Do's and Don'ts

- Do let the outputs carry the design: square flat icons in amber #f0a030, vermilion #e04000, orchid #c050a0 and cornflower #5060c0 on white.
- Do label each output with its prompt in a handwritten hand, in quotes, centred over or under the cell.
- Do separate grid groups with dashed lines, not solid borders or coloured backgrounds.
- Do keep the HTML chrome stock Nerfies: Google Sans title, #209cee names, #363636 pills.
- Don't add colour to headings or buttons; all colour comes from the icons.
- Don't crop icons into rounded tiles; they sit on the white ground.
- Don't publish the BibTeX block empty; fill the `pre` or remove the section.

## Surfaces

White page and sections; #f5f5f5 only in the BibTeX `pre`; #fafafa footer. The Results image is the only element with a shadow.

## Imagery

Vector icons generated in a chosen style: thick-outlined flat icons in warm amber, red and violet; chunky pixel-art sprites; soft cartoon figures. Each sits on white with a handwritten quoted prompt; the pipeline figure is a pastel boxed diagram with small icon thumbnails.

## Layout

A centred 960px Nerfies column: a 371px hero, a 912px teaser grid with a 20px caption, then Abstract, Methods, Results and BibTeX sections at 48px padding, all images at 912–936px.

## Agent Prompt Guide

Quick colors: background #ffffff, title #363636, body #4a4a4a, authors #209cee, pills #363636, footer #fafafa; icon fills #f0a030 / #e04000 / #c050a0 / #5060c0.

1. "Build a centred Nerfies hero in a 960px container, padding 48px 24px: title Google Sans 48px/600 #363636 on two lines; authors Google Sans 20px with #209cee names and #4a4a4a superscripts; affiliations 20px #4a4a4a; three pills (#363636, white 16px Noto Sans, padding 7px 20px, radius 290486px) with icons at left."
2. "Make a teaser figure 912px wide: a column of exemplar icons, a dashed vertical rule, then a grid of square flat icons in #f0a030, #e04000, #c050a0 and #5060c0 on white, each column headed by a handwritten quoted prompt; bold sans '(a)' and '(b)' panel labels below; under the image a centred Google Sans 20px/400 #4a4a4a caption."
3. "Show results as one 936px grid image: cells separated by dashed lines, a handwritten quoted label under each icon, and box-shadow rgba(0,0,0,0.2) 0px 2px 4px 0px on the image; section title Noto Sans 32px/600 #363636 centred above it."

## Similar Pages

- Nerfies-template pages for vector-graphics, icon and font generation papers whose results are grids of small graphics.
- Pages where the teaser is a labelled specimen sheet rather than a photo or video.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --code-well: #f5f5f5;
  --footer: #fafafa;
  --icon-amber: #f0a030;
  --icon-vermilion: #e04000;
  --icon-orchid: #c050a0;
  --icon-cornflower: #5060c0;
  --figure-shadow: rgba(0, 0, 0, 0.2) 0px 2px 4px 0px;
  --font-display: "Google Sans", sans-serif;
  --font-text: "Noto Sans", sans-serif;
  --container: 960px;
  --radius-pill: 290486px;
}
```

## Provenance

- **URL**: https://customsvg.github.io/
- **Paper**: Style Customization of Text-to-Vector Generation with Image Diffusion Priors (arXiv 2505.10558), Peiying Zhang, Nanxuan Zhao, Jing Liao.
- **Venue**: SIGGRAPH 2025 (Conference Paper); the arXiv comment states "Accepted by SIGGRAPH 2025 (Conference Paper)". The page itself shows no venue.
- **Selection reason**: a clean centred layout whose teaser and results are captioned icon grids with dashed dividers, so the work itself becomes the visual system.
- **Template credit**: Nerfies project page template (Bulma 0.9, Font Awesome, Academicons); footer carries the template's Creative Commons licence text.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, pixel sampling of the teaser in the 1440 screenshot, the 1440×900 and full-page screenshots, and the page's `index.html` and `static/css/index.css` read directly, on 2026-10-28.
