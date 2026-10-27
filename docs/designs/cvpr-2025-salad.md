# SALAD Biolinum Bands — Style Reference

> A quiet typeset monograph, its grey and white plates turning one after another.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 3,607px page, the page's `static/css/index.css` and its markup. The page is the Academic Project Page Template (Nerfies lineage, Bulma 0.9 with bulma-carousel); the author's one strong decision is to set every text role in Linux Biolinum at weight 400. Color share is measured on the first 1440×900 viewport.

## Overview

A centred, almost colourless page whose character comes from the typeface. Linux Biolinum (the humanist sans companion of Linux Libertine, with flared, calligraphic strokes that read close to a serif) sets a two-line 48px title in #363636 at regular weight, a row of sky-blue author links, the lab and "CVPR 2025" as two plain grey lines, and two charcoal rounded Bulma buttons. A YouTube teaser (763px, 10px radius) fills the rest of the first screen. Below, full-width sections alternate #f5f5f5 and white: Abstract (grey, justified 17.92px text in a 763px column), Overview (white, three wide schematic figures with 20px subtitles), Editing Results (grey band holding a carousel of 1344px-wide white-background motion videos with black dots), then a #fafafa footer.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 69.4%, mint-white #fafff9 10.2% and #f9fff9 4.4% (the near-white background of the teaser video frame), warm grey #7d7877 8.5% (title, text, buttons and the video's dark parts), pale grey #ebedee 5.1% (the start of the #f5f5f5 Abstract band at the bottom edge and video UI), plus traces of near-white. The author blue and the YouTube red are each under 1%.

Anatomy in DOM order (all centred in the 960px `.container.is-max-desktop`, hero-body padding 48px 24px):

1. **Title** — `h1.title.is-1.publication-title`, 48px / 400 / line-height 54px, Linux Biolinum, #363636, two lines (y=48–156). Gap 24px (margin-bottom).
2. **Authors** — `.publication-authors` line, `.author-block` 19.52px (1.22rem) / 400 / 29.28px; names are links in #209cee separated by grey commas (y=180–210). Gap 0.
3. **Lab and venue** — second `.publication-authors`, "Visual Media Lab, KAIST" then `<br>` "CVPR 2025", 19.52px / 400 #4a4a4a, no bold and no badge (y=210–269). Gap 17px.
4. **Buttons** — two `a.button.is-normal.is-rounded.is-dark`, "Paper" (Academicons arXiv glyph) and "Code" (Font Awesome GitHub), 16px / 400 Linux Biolinum, #ffffff on #363636, pill radius, padding 7px 20px, 5px vertical margin, 4px apart (y=286–326). Gap 53px (end of hero section at y=391, then the teaser container).
5. **Teaser video** — `.publication-video` YouTube iframe, 763×429 (16:9 via padding-bottom 56.25%), radius 10px with `overflow: hidden`, x=338–1101, y=391–820. Gap 48px to the grey Abstract band (y=868).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `html` background | page, Overview section, carousel video backgrounds |
| Title Charcoal | #363636 | Bulma `.title` color, `.button.is-dark` fill | paper title, Overview heading, button fill |
| Body Grey | #4a4a4a | Bulma body color | lab and venue lines, author commas, figure subtitles, footer text |
| Band Text | rgba(0,0,0,0.7) | Bulma `.hero.is-light` color | Abstract heading and text, Editing Results heading and captions |
| Author Sky | #209cee | `.publication-authors a` (hsl(204,86%,53%) !important) | author names |
| Button Hover | #2f2f2f | Bulma `.button.is-dark:hover` | button hover fill |
| Bulma Link | #3273dc | Bulma `a` | footer links |
| Band Grey | #f5f5f5 | Bulma `.hero.is-light` | Abstract and Editing Results sections |
| Footer Haze | #fafafa | Bulma `.footer` | footer band |
| Dot Black | #000000 | `.slider-pagination .slider-page` | carousel pagination dots |
| Arrow Shadow | #323232 | bulma-carousel navigation | `0 2px 5px rgba(50,50,50,0.1)` on the white round arrows and dots |

## Tokens — Typography

- **Sans (humanist):** declared `'Linux Biolinum', Arial, sans-serif` on `body`, `.title`, `.subtitle`, `.content`, `.button`, `.publication-authors` (via `@import url('https://fonts.cdnfonts.com/css/linux-biolinum')`). Rendered: Linux Biolinum 400 for every role; headings are explicitly weight 400, so nothing is synthesized. Substitute: Linux Biolinum O from CTAN or, on Google Fonts, Alegreya Sans.
- **Unused request:** Google Fonts `Google+Sans|Noto+Sans|Castoro` is still linked by the template but never applied.
- **Icons:** Academicons (arXiv), Font Awesome 5 (GitHub, SVG).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 400 / 54px |
| Authors, lab, venue | `.publication-authors`, `.author-block` | 19.52px (1.22rem) / 400 / 29.28px |
| Section titles | `h2.title.is-3` | 32px / 400 / 36px |
| Figure subtitles | `h2.subtitle` | 20px / 400 / 25px |
| Body | `.content p` (1.12rem) | 17.92px / 400 / 26.88px, justified in the Abstract |
| Carousel captions | `.item p` | 17.92px / 400, centred |
| Buttons | `.button.is-normal` | 16px / 400 / 24px |
| Footer | `.footer .content p` | 17.92px / 400 / 26.88px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | Bulma `is-rounded` pill (radius 9999px), padding 7px 20px, 1px transparent border, no shadow |
| Teaser video | radius 10px, `overflow: hidden` |
| Carousel arrows | 42px white circles, 1px #ffffff border, shadow `0 2px 5px rgba(50,50,50,0.1)` |
| Pagination dots | about 10px black circles, active dot larger (13px), same shadow |
| Figures, videos | square corners, no borders |
| Bands | full-bleed, no rules between them |

## Layout Metrics

- **Hero column:** `.container.is-max-desktop`, max-width 960px, centred (x=240–1200 at 1440); hero-body padding 48px 24px.
- **Teaser:** `.column.is-four-fifths` inside the 960px container, so the video is 763px wide (x=338); teaser hero-body padding-top 0, padding-bottom 3rem (48px).
- **Sections:** `section.section.hero` padding 48px 24px; h2 margin-bottom 24px; Abstract text 763px wide (x=338–1101).
- **Overview figures:** plain `.container` (max-width 1344px at 1440, margin 0 24px), each schematic 1344px wide, subtitle under each; this section is wider than the text above it.
- **Editing carousel:** 1344px wide, one slide at a time, each 1344×672 video with a caption above; arrows at the container edges, dots under the video.
- **Footer:** padding 48px 24px 96px, text block 888px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1408px | 960px column / 1344px wide sections | 17.92px | 48px | as described |
| 1216–1407px | 960px / 1152px | 17.92px | 48px | wide sections narrow to Bulma's widescreen container |
| 1024–1215px | 960px column for both | 17.92px | 48px | Overview figures shrink to 960px |
| ≤1023px | 24px | 17.92px | 48px | containers go fluid; Bulma columns stack below 769px, so the teaser runs full width |

## Components

- **Rounded dark button:** Bulma `.button.is-rounded.is-dark`, #363636 fill, #ffffff 16px Linux Biolinum 400, padding 7px 20px, icon left in `span.icon`; hover is Bulma's slightly darker fill (#2f2f2f).
- **Author row:** inline-block names in #209cee with grey commas, underline on hover, at 19.52px; lab and venue below as plain grey text.
- **Rounded teaser embed:** 16:9 wrapper with 10px radius around a YouTube iframe.
- **Alternating band:** `section.section.hero.is-light` on #f5f5f5 with rgba(0,0,0,0.7) text, followed by a white `section` with #4a4a4a text.
- **Schematic stack:** full-width figure, 20px subtitle "(a) …" under it, repeated three times.
- **Video carousel:** bulma-carousel, one wide slide, 17.92px caption above each video, white circular arrows, black dot pagination.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / lab | Yes | centred Biolinum stack |
| Venue | Yes (non-standard) | "CVPR 2025" as a plain second line under the lab, no badge or bold |
| Link buttons | Yes | two dark pill buttons |
| Teaser video | Yes | YouTube embed, 10px radius |
| Abstract | Yes | grey band, justified |
| Method figures | Yes | three Overview schematics with subtitles |
| Results carousel | Yes | editing videos on a grey band |
| Results table | No (absent from the source) | |
| BibTeX | No (absent from the source) | |
| Footer | Yes | #fafafa, template credit and CC licence |

## Adapting to Other Content

- **More authors:** the inline-block author row wraps cleanly; keep it in #209cee and add superscript affiliation numbers in #4a4a4a before the lab line.
- **Results table:** put it on a white band in the 960px column; Bulma `.table` at 17.92px Biolinum, header weight 400 to match the headings, and rely on the band alternation instead of zebra stripes.
- **BibTeX:** a grey band like the Abstract with a `pre` on #ffffff so it reads against #f5f5f5.
- **Award or highlight:** keep it typographic, a second plain line or italic, not a coloured badge; the page has no accent color beyond the author links.
- **Long publication or news lists:** a white band with a 17.92px left-aligned list in the 960px column.

## Do's and Don'ts

- Do set every role, including headings and buttons, in one humanist face at weight 400.
- Do alternate full-width #f5f5f5 and white sections to separate content instead of rules or cards.
- Do let schematics run wider (1344px) than the reading column (763px).
- Don't bold headings; size alone carries the hierarchy here.
- Don't add accent colors; the only hue is the author blue.
- Don't frame figures; they sit directly on the band.

## Surfaces

White hero and Overview, #f5f5f5 bands for Abstract and Editing Results, #fafafa footer. The dark pill buttons are the only filled shapes.

## Imagery

A YouTube teaser of stylised 3D characters on grey floor tiles, clean line schematics in pale green and peach, and stick-figure skeleton videos (red and blue limbs on grey plates) on white backgrounds.

## Layout

Centred single column for text (763–960px), wider containers for figures and carousel (1344px at 1440), bands alternating grey and white. Rendered height about 3,600px.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, band text rgba(0,0,0,0.7), authors #209cee, bands #f5f5f5 alternating with #ffffff, buttons #363636 with #ffffff text, footer #fafafa, links #3273dc.

1. "Create a centred hero in a 960px column: a 48px Linux Biolinum title at weight 400 in #363636 (line-height 54px, 24px below), a 19.52px author row in #209cee, lab and venue as two plain #4a4a4a lines, then pill buttons with #363636 fill, #ffffff 16px text, padding 7px 20px and an icon left."
2. "Under it, embed a 16:9 video 763px wide with a 10px radius and overflow hidden, then start alternating full-width sections: #f5f5f5 with rgba(0,0,0,0.7) text, then #ffffff with #4a4a4a text, each padded 48px 24px with a 32px weight-400 heading."
3. "Build a figure stack: images 1344px wide, each followed by a centred 20px subtitle '(a) …' in #4a4a4a, and a one-slide video carousel with white 42px round arrows and #000000 dot pagination."

## Similar Pages

- Academic Project Page Template and Nerfies pages that swap Google Sans for a book face.
- Motion-generation project pages with stick-figure carousels.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --band: #f5f5f5;
  --footer: #fafafa;
  --title: #363636;
  --text: #4a4a4a;
  --band-text: rgba(0, 0, 0, 0.7);
  --author: #209cee;
  --link: #3273dc;
  --button: #363636;
  --font-sans: 'Linux Biolinum', 'Alegreya Sans', Arial, sans-serif;
  --title-size: 48px;
  --h2-size: 32px;
  --subtitle-size: 20px;
  --body-size: 17.92px;
  --author-size: 19.52px;
  --radius-video: 10px;
  --column: 960px;
}
```

## Provenance

- **URL:** https://seokhyeonhong.github.io/projects/salad/
- **Paper:** SALAD: Skeleton-aware Latent Diffusion for Text-driven Motion Generation and Editing (arXiv 2503.13836), Seokhyeon Hong et al., Visual Media Lab, KAIST.
- **Venue:** CVPR 2025 (stated under the lab name).
- **Selection reason:** existing verified entry (entries.json).
- **Template credit:** footer credits the Academic Project Page Template, adopted from the Nerfies project page.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, `static/css/index.css`, page HTML; 2026-10-28.
