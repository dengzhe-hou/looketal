# Seeing the Wind Butter Bands — Style Reference

> An autumn almanac printed on butter-yellow stock, a single leaf drifting past the masthead and amber tabs marking the chapters.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against the inline `<style>` block in `index.html`, the Nerfies `static/css/index.css` and Bulma 0.9 with bulma-carousel. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

A Nerfies/Bulma page re-skinned with one idea: full-width sections alternate between butter yellow (`#ffecb3`) and white. The hero and the TL;DR band are both yellow, so the whole first screen reads as one warm field. The 48px Google Sans title is led by a 96px leaf-and-wind icon. Bulma-blue author links run on two lines, then a bold "NeurIPS 2025" line and three pill buttons: two amber gradient pills (Paper, arXiv) and a grey "Code (Coming Soon)" pill. A centred 10px-radius TL;DR video sits in the second yellow band. Abstract, method figure and a numbered list follow on white, then three demo bands (Video Generation on yellow, Motion Editing on white, Force Field Visualization on yellow). Each is a full-width carousel of side-by-side video pairs with small captions above and round dark arrows. A white BibTeX section and Bulma's `#fafafa` footer close the page. Document height is about 3,945px.

## First Viewport

Color share of the first 1440×900 viewport: `#ffecb3` 69.9% (hero and TL;DR bands), `#5f748d` 11.0% and `#3e5571` 10.5% (sky in the TL;DR video), `#c9bd98` 4.1% (video edges and grey pill blended with yellow), `#ffefb5` 2.1%, `#fdecb3` 0.9%, `#fdecb5` 0.7%, `#feecb2` 0.6% (anti-aliased band tones).

Anatomy in DOM order (all centred):

1. Hero `section.hero.bg-cream`, full width, `#ffecb3`; `.hero-body` padding 48px 24px; content in a 960px `.container.is-max-desktop`.
2. Title `h1.title.is-1.publication-title`, Google Sans 48px/600, `#363636`, line-height 54px, preceded inline by `leaficon.png` at 2em (96px) with a 10px right margin. Gap about 31px.
3. Authors line 1 (4 names) and line 2 (4 names), `.publication-authors.is-size-5`, Google Sans 20px/400, links `#209cee`, symbol superscripts (`*`, `¶`, `$`), commas in `#4a4a4a`. Lines 34px apart.
4. "* Equal Contribution" then the affiliation line "¶ University of Southern California $ Stanford University", 20px/400, `#4a4a4a`. Gap about 10px.
5. Venue `p` "NeurIPS 2025", Noto Sans 24px/700, `#4a4a4a`, inline margin 10px 0 -15px. Gap about 17px.
6. Button row `.publication-links`, flex, centred, 15px gap: Paper and arXiv amber pills (116×44px and 109×44px), then the grey Code (Coming Soon) pill. Hero ends at y=474, about 60px below the buttons.
7. TL;DR band, second `section.hero.bg-cream`, same yellow, 48px top padding: `h2.title.is-4` "TL;DR Seeing Wind: Differentiable Framework for Force Estimation & Video Editing", Noto Sans 24px/600, `#363636`. Gap 24px.
8. Teaser video in `column is-10`, 796×338px visible at x=322, 10px radius, autoplay with native controls; it runs off the bottom of the viewport.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Butter | `#ffecb3` | `.bg-cream` | Hero, TL;DR band, Video Generation and Force Field bands |
| Paper | `#ffffff` | `.bg-white` | Abstract/method section, Motion Editing band, BibTeX section |
| Title Ink | `#363636` | Bulma `.title` | Paper title, section `h2` titles, TL;DR heading |
| Body Ink | `#4a4a4a` | Bulma body | Abstract, list, affiliations, venue line, carousel captions, BibTeX text |
| Author Blue | `#209cee` | `.publication-authors a` (`hsl(204,86%,53%)`) | Author names |
| Amber Light | `#ffb74d` | `.arxiv-link` gradient start | Paper and arXiv pills |
| Amber | `#ffa726` | `.arxiv-link` gradient end | Paper and arXiv pills |
| Pill Grey | `#9e9e9e` | `.coming-soon-link` gradient start | Code (Coming Soon) pill, at 0.8 opacity |
| Pill Grey Dark | `#757575` | `.coming-soon-link` gradient end | Code (Coming Soon) pill |
| Pill Shadow | `rgba(0,0,0,0.1)` | `.highlighted-link` box-shadow | All three pills |
| Arrow Scrim | `rgba(0,0,0,0.5)` | `.slider-navigation-*` | Round carousel arrows (0.8 on hover) |
| Dot Grey | `#dbdbdb` | `.slider-page` | Carousel dots |
| Dot Active | `#3273dc` | `.slider-page.is-active` | Active carousel dot (scaled 1.4) |
| Code Grey | `#f5f5f5` | Bulma `pre` | BibTeX block |
| Footer Haze | `#fafafa` | Bulma `.footer` | Footer band |

## Tokens — Typography

- **Declared:** Google Fonts link for Google Sans, Noto Sans and Castoro (Nerfies). `body` is `'Noto Sans', sans-serif`; `.publication-title` and `.publication-authors` are `'Google Sans', sans-serif`.
- **Rendered:** Google Sans 400 and Noto Sans 400 loaded (`fonts_loaded`); bold weights are synthesized from those. Icons: Font Awesome 6 (Free 900, Brands 400) and Academicons. Substitute for Google Sans: Product Sans is not public, so use Outfit or DM Sans, whose round geometric shapes and wide "a" match best.
- **Mono:** Bulma `monospace` in the BibTeX `pre`.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px | 600 | 54px | `#363636`, Google Sans |
| Section title | `h2.title.is-3` | 32px | 600 | 36px | `#363636`, centred by inline rule |
| TL;DR heading | `h2.title.is-4` | 24px | 600 | 27px | `#363636` |
| Venue line | inline `p` 1.5em | 24px | 700 | 36px | `#4a4a4a` |
| Authors, affiliations | `.publication-authors.is-size-5` | 20px | 400 | 30px | links `#209cee` |
| Carousel caption | `h4.subtitle.is-5` | 20px | 400 | 25px | `#4a4a4a`, centred |
| Body | `body`, `.content p`, `ol` | 16px | 400 | 24px | `#4a4a4a` |
| Pill label | `.highlighted-link` | 16px | 700 | 24px | `#ffffff`, icon 20px |
| BibTeX | `pre` | 14px | 400 | 21px | `#4a4a4a` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Pill buttons `.highlighted-link` | 25px |
| TL;DR video | 10px (inline) |
| Carousel videos | 0 (square); the inline `.custom-carousel video` and `#paired-carousel video` rules declare 6px, but no element on the page uses those selectors |
| Carousel arrows, dots | 50% |
| BibTeX `pre` | Bulma default 4px |

- **Shadows:** pills `0 2px 4px rgba(0,0,0,0.1)`, hover `0 4px 6px rgba(0,0,0,0.15)`. The `0 4px 10px rgba(0,0,0,0.1)` video shadow is declared for the unused carousel selectors and is not visible.
- **Borders:** none on the rendered elements; `#paired-carousel video` declares 1px `#eeeeee` but the page has no element with that id (declared but not visible).
- **Motion:** pills lift `translateY(-2px)` on hover over 0.3s; the grey Coming Soon pill does not move.

## Layout Metrics

- **Containers:** hero, TL;DR, abstract and BibTeX use `.container.is-max-desktop` (960px at ≥1024px). The three demo bands use a plain `.container`, which is 1344px at 1440px (Bulma fullhd), so carousels run almost edge to edge with 48px side margins.
- **Hero padding:** `.hero-body` 48px 24px for the hero and TL;DR band; demo bands are `.hero.is-small` with 24px vertical padding.
- **Abstract section:** no `.hero-body`; three `<br>` above and below create about 72px of vertical air.
- **BibTeX section:** Bulma `.section` padding 48px 24px. Footer padding 48px 24px 96px.
- **Teaser:** `column is-10` inside 960px, so about 800px wide.
- **Carousel slides:** Bulma `.columns` with two `.column`s (0.75rem padding each), each a caption over a video; `.slider-container video` max-height 400px, `object-fit: contain`. Each demo band is 528px tall.
- **Button row:** flex, centred, 15px gap, 20px top margin.

| Breakpoint | Container | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1408px | 960px text / 1344px demo bands | 48px beside demo carousels | 16px | 48px | two videos per slide |
| 1216–1407px | 960px / 1152px | 32px | 16px | 48px | same |
| 1024–1215px | 960px / 960px | 32px | 16px | 48px | same |
| 769–1023px | fluid | 24px (hero padding) | 16px | 48px | same |
| ≤768px | fluid | 24px | 16px | 48px | `.columns` stack, so slide captions and videos become one column; authors wrap to more lines |

## Components

- **Leaf title.** `h1` with an inline PNG icon (`height: 2em; vertical-align: middle; margin-right: 10px`) before the 48px/600 Google Sans title in `#363636`.
- **Amber pill.** `a.highlighted-link.arxiv-link`: `display: inline-flex`, padding 10px 20px, `linear-gradient(45deg, #ffb74d, #ffa726)`, white 16px bold label, 20px icon left with 8px gap, 25px radius, shadow `0 2px 4px rgba(0,0,0,0.1)`; hover lifts 2px with `0 4px 6px rgba(0,0,0,0.15)`. Icons: `fa-file-pdf` for Paper, `ai-arxiv` for arXiv.
- **Coming Soon pill.** Same recipe as a `span` with `linear-gradient(45deg, #9e9e9e, #757575)`, opacity 0.8, default cursor, no hover lift; GitHub icon.
- **Band section.** `section.hero` with `.bg-cream` or `.bg-white`; centred `h2.title.is-3` 32px/600; no rules or cards between bands.
- **Paired video carousel.** bulma-carousel `.slider-container` with slides of two columns; each column a centred 20px `h4.subtitle.is-5` caption ("Original", "New Object Insertion", "2x Mass") above an autoplay looping video with controls. Arrows are round `rgba(0,0,0,0.5)` buttons with white chevrons on the slide edges, 0.8 on hover; dots are 10px `#dbdbdb` circles, active `#3273dc` scaled 1.4.
- **Method list.** Full-width method PNG, then a lead sentence and a Bulma `.content ol` numbered list in 16px `#4a4a4a`.
- **BibTeX.** `h2.title` then Bulma `pre` on `#f5f5f5`, padding 17.5px 21px, 14px monospace.
- **Footer.** Bulma `.footer` on `#fafafa`, one line "This website is borrowed from here." linking the source template.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Yellow band, leaf icon, Google Sans title, blue authors |
| Venue badge | Yes, as text | Bold 24px "NeurIPS 2025" line |
| Link buttons | Paper, arXiv, Code (Coming Soon) | Amber gradient pills, grey disabled pill |
| TL;DR teaser | Yes | Second yellow band, `h2.is-4` heading, 10px-radius video |
| Abstract | Yes | White section, centred `h2`, plain paragraph |
| Method figure + list | Yes | Full-width PNG and numbered list |
| Result carousels | Three | Side-by-side video pairs in alternating yellow/white bands |
| Results table, sliders, 3D viewer | Absent from the source | |
| BibTeX | Yes | `#f5f5f5` `pre` on white |
| Footer | Yes | `#fafafa` band, one-line credit |

## Adapting to Other Content

- **More authors:** keep splitting names into separate `.publication-authors` rows of about four, all 20px `#209cee`; the symbol superscripts already handle multiple affiliations.
- **More links:** add amber pills for live resources (Code, Data, Demo); keep grey pills only for "Coming Soon".
- **A results table:** give it its own band in the alternation (yellow if the previous was white), a centred `h2.title.is-3`, and a white table on yellow bands so it reads as a card; header row in 600 `#363636`, best values in bold.
- **Long galleries:** add more carousel bands and keep alternating `#ffecb3` and `#ffffff`; never put two yellow bands in a row below the fold (only the hero and TL;DR share yellow).
- **News:** a short list in the white abstract section, 16px `#4a4a4a`, dates in 700 weight, above the abstract heading.

## Do's and Don'ts

- Do alternate full-width `#ffecb3` and `#ffffff` bands; the rhythm is the identity.
- Do keep the amber gradient (`#ffb74d` → `#ffa726`) for every live link pill so buttons echo the bands.
- Do centre every section title and caption.
- Do keep the leaf icon at 2em next to the title; it is the only illustration in the hero.
- Don't add a second accent hue; author blue is the Bulma default and stays confined to names.
- Don't put cards or borders on bands; colour change alone separates sections.

## Surfaces

Two surfaces alternate across the full width: butter `#ffecb3` and white. The BibTeX block is `#f5f5f5` and the footer `#fafafa`. Videos carry the only dark areas.

## Imagery

A small leaf-and-wind PNG icon in the title. The rest is video: a TL;DR explainer with a coloured leaf trajectory over sky, side-by-side physics edits of cherry blossom and leaf scenes, and force-field visualizations. One method diagram PNG.

## Layout

Centred 960px reading column for text, widened to 1344px for the demo carousels. Every section spans the full width as a colour band, with content centred inside.

## Agent Prompt Guide

Quick colors: band `#ffecb3`, page `#ffffff`, titles `#363636`, text `#4a4a4a`, authors `#209cee`, pill gradient `#ffb74d` → `#ffa726`, disabled pill `#9e9e9e` → `#757575`, code `#f5f5f5`, footer `#fafafa`.

1. "Build a hero band: full-width `#ffecb3`, padding 48px 24px, a 96px icon inline before a 48px/600 Google Sans title in `#363636`, two rows of 20px author links in `#209cee`, a 24px/700 venue line in `#4a4a4a`, and a centred flex row of pills with 15px gap."
2. "Make link pills: inline-flex, padding 10px 20px, 25px radius, `linear-gradient(45deg, #ffb74d, #ffa726)`, white bold 16px label with a 20px left icon, shadow `0 2px 4px rgba(0,0,0,0.1)`; on hover translateY(-2px) and shadow `0 4px 6px rgba(0,0,0,0.15)`."
3. "Create a demo band: full-width section alternating `#ffecb3` and `#ffffff`, 24px vertical padding, centred 32px/600 heading, then a carousel whose slides hold two equal columns, each a centred 20px caption over an autoplay video, with round `rgba(0,0,0,0.5)` arrows."

## Similar Pages

Other Nerfies-derived Bulma pages share the skeleton, but few re-colour whole bands. In this NeurIPS 2025 batch, ThermalGen alternates grey and white bands with the same idea at lower contrast.

## Quick Start

```css
:root {
  --band: #ffecb3;
  --page: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --pill: linear-gradient(45deg, #ffb74d, #ffa726);
  --pill-muted: linear-gradient(45deg, #9e9e9e, #757575);
  --pill-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  --code-bg: #f5f5f5;
  --footer: #fafafa;
  --font-display: 'Google Sans', 'DM Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-pill: 25px;
  --radius-video: 10px;
}
.bg-cream { background: var(--band); }
.bg-white { background: var(--page); }
.highlighted-link { display: inline-flex; padding: 10px 20px; border-radius: var(--radius-pill); background: var(--pill); color: #fff; font-weight: 700; box-shadow: var(--pill-shadow); }
```

## Provenance

- **URL:** https://chaoren2357.github.io/seeingthewind/
- **Paper:** Seeing the Wind from a Falling Leaf (arXiv 2512.00762), Zhiyuan Gao, Jiageng Mao, Hong-Xing Yu, Haozhe Lou, Emily Yue-ting Jia, Jernej Barbič, Jiajun Wu, Yue Wang (University of Southern California, Stanford University).
- **Venue:** NeurIPS 2025 (shown on the page).
- **Selection reason:** the arXiv comment states acceptance at NeurIPS 2025; the project page is linked in the abstract.
- **Template credit:** footer says the site is borrowed from the Nerfies template.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, the inline `<style>` block, `static/css/index.css` and Bulma defaults. Captured 2026-10-28.
