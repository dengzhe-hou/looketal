# Matérn Noise — Style Reference

> A tidy lab notebook with alternating gray and white pages: one wide octopus strip up top, then calm columns of math beside colourful noise fields.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), a second probe of rendered elements (author lines, toggle buttons, carousel tiles, slider controls, side-by-side layout, footer), the 1440×900 and tall screenshots, and the page's `static/css/index.css` on top of Bulma, bulma-carousel and the Nerfies template markup. Google Sans loads only its 400 file, so the 600 title and bold venue line are synthesised bold. The results carousel videos had not painted at capture time, so their tiles show as empty white squares in the tall screenshot.

## Overview

A classic Nerfies-template page kept close to the original and lightly extended. Text is Bulma's #4a4a4a in Noto Sans, headings #363636, with Google Sans for the title, venue line, authors and teaser caption. The centred hero has a two-line 48px title, a bold gray venue line ("ACM Transactions on Graphics (SIGGRAPH 2026)"), bright-blue author links with superscripts, an affiliation line and five dark rounded Bulma buttons. A wide teaser strip of octopus meshes progressing through the denoising process sits on white above a 20px caption with an italic phrase. Rhythm then comes from alternating bands: a #f5f5f5 Abstract section with justified text, a white explainer with inline MathJax math, a white overview diagram, a #f5f5f5 hero band holding a two-button gradient toggle and a three-up video carousel, white result sections, a #f5f5f5 BibTeX block and a #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fffffd / #fdffff together 58.7%; light gray #f5f5f5 23.8% (the Abstract band starting at y=676); mauve-gray #a8979e 12.6% (the magenta and pastel octopus meshes plus dark buttons blended); off-whites #f7f5f3 / #fafafa / #f1f7fa 4.9%. The author blue is too small to form a cluster.

Anatomy in DOM order (desktop 1440px, centred in a 960px column at x=240):

1. **Hero** (`section.hero`, 0–401px): Bulma `.hero-body` padding 3rem 1.5rem, white, no navigation bar.
2. **Title** (`h1.title.is-1.publication-title`, y=48, 108px, two lines): Google Sans 48px / 600 (synthesised) / 54px, #363636. Gap 24px.
3. **Venue** (`span.publication-venue`, y=180): Google Sans 20px bold, #555555, width fit-content, line-height 30px.
4. **Authors** (y=217): Google Sans 20px/400, links #209cee (forced with `!important`, `hsl(204, 86%, 53%)`), superscripts and commas #4a4a4a; hover underline.
5. **Affiliations** (y≈247): Google Sans 20px #4a4a4a with superscripts ("Université de Montréal & Mila, Brown University"). Gap ≈19px.
6. **Buttons** (y=296, 40px tall, margin 5px 0, gap ≈4px): arXiv, Paper (compressed) (12MB), Paper (82MB), Code, Data; Bulma `.button.is-dark.is-rounded`: #363636 fill, white Noto Sans 16px/400, radius 290486px, padding 7px 20px, 1px transparent border, Font Awesome or Academicons icon left.
7. **Teaser** (`section.hero.teaser`, 401–676px): `.hero-body` padding 0 top, 3rem bottom; a 912×171 image (x=264) with no frame or radius, then the caption `h2.subtitle.has-text-centered` at y=603, Google Sans 20px/400 #4a4a4a with an italic "triangulation-agnostic".
8. **Abstract band** (`section.section.has-background-light`, from y=676): #f5f5f5, padding 48px 24px; "Abstract" h2 Noto Sans 32px/600 #363636 centred at y=724; justified 16px/24px #4a4a4a text in a 763px column (x=338).

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma) | page, hero, teaser, explainer and result sections |
| Light | #f5f5f5 | `has-background-light` / `.hero.is-light` | Abstract band, carousel hero band, BibTeX pre |
| Footer Gray | #fafafa | (Bulma footer) | footer background |
| Text | #4a4a4a | (Bulma body) | body text, author commas, affiliations, teaser caption, footer |
| Heading | #363636 | (Bulma title) | h1, section h2, dark button fill |
| Venue Gray | #555555 | (literal) | venue line, unselected toggle text |
| Author Blue | #209cee | hsl(204, 86%, 53%) | author links, body links |
| Hero Text | rgba(0, 0, 0, 0.7) | (Bulma `.hero.is-light`) | carousel band headings |
| Toggle Border | #e6e6e6 / #fbfbfb | (literal) | unselected toggle border / fill |
| Toggle Selected | linear-gradient(110deg, #dff2d8 0%, #edf8f6 52%, #dce8ff 100%) | (literal) | selected toggle fill |
| Selected Border | #bfe0f3 / #25292b | (literal) | selected toggle border / text |
| Tile Border | #bbbbbb | (literal) | carousel video tile border |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors / teaser caption | 'Google Sans', sans-serif | Google Sans 400 only; 600 and bold synthesised | Outfit |
| Body / section headings | 'Noto Sans', sans-serif | Noto Sans 400 (600 headings synthesised) | Noto Sans |
| Toggle buttons | Bulma system stack (BlinkMacSystemFont, -apple-system, "Segoe UI", Roboto…) | Segoe UI on Windows | Inter |
| Code | Bulma `monospace` | system monospace | JetBrains Mono |
| Math | MathJax 3 (tex-svg) | rendered as inline SVG paths, so no math font loads | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title.is-1.publication-title` | 3rem = 48px / 600 / 54px | #363636 |
| Venue | `.publication-venue` | 20px / 700 / 30px | #555555 |
| Authors, affiliations | `.publication-authors` | 20px / 400 / 30px | #209cee links, #4a4a4a text |
| Teaser caption | `.teaser h2.subtitle` | 20px / 400 / 25px | #4a4a4a |
| Section heading | `.title.is-3` | 2rem = 32px / 600 / 36px | #363636 |
| Results subheading | `h2.title.is-5` inside sections | 20px / 600 / 22.5px | #363636 |
| BibTeX heading | `#BibTeX h2` | 28px / 600 | #363636 |
| Content heading | `.content-heading` | 16px / 700, margin-bottom 0.5rem | #4a4a4a |
| Body | `body` | 16px / 400 / 24px | #4a4a4a |
| Button | `.button.is-dark` | 16px / 400 | #ffffff |
| Toggle | `.video-toggle .button` | 1.2rem = 19.2px / 500 (selected 600) / 1 | #555555 / #25292b |
| BibTeX | `pre` | 14px / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px (full pill) | 1px transparent | none |
| Toggle buttons (58px tall, min-width 17.5rem) | 23px | 2px #e6e6e6; selected 2px #bfe0f3 | none; focus `0 0 0 0.125em rgba(82, 146, 210, 0.2)` |
| Carousel video tiles (438px squares) | 10px | 1px #bbbbbb | none |
| Carousel arrows (42px) and dots (10–14px) | full round | 1px #ffffff | `0 2px 5px rgba(50, 50, 50, 0.1)` |
| Teaser and figures | 0 | none | none |
| BibTeX pre | 0 | none | none; padding 17.5px 21px on #f5f5f5 |

## Layout Metrics

- **Containers**: Bulma `.container.is-max-desktop` = 960px (x=240) for the hero, explainer and BibTeX; the teaser image is 912px (x=264); the Abstract uses `.column.is-four-fifths` = 763px (x=338); the carousel band uses the full `.container` (1344px, x=48).
- **Hero**: `.hero-body` padding 48px 24px; title margin-bottom 24px; buttons margin 5px 0; teaser `.hero-body` padding 0 0 48px.
- **Sections**: `.section` padding 48px 24px; h2 margin-bottom 24px; the light hero band has its own `hero-body` padding.
- **Explainer** (`.noise-comparison-layout`): grid `minmax(280px, 1fr) minmax(240px, 50%)` rendering 448px text + 480px figure, gap 2rem = 32px, items centred.
- **Carousel**: bulma-carousel showing three 438px square tiles with 5px margins; arrows 42px at the container edges; dots below.
- **Footer**: padding 48px 24px 96px on #fafafa, centred 16px text in an 888px column.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1023px | 24px | 16px | 48px | 960px column; explainer side by side; 3-up carousel |
| ≤1023px | 24px | 16px | 48px | Bulma columns stack; carousel shows fewer tiles |
| ≤700px | 24px | 16px | 48px | explainer stacks to 1 column |
| ≤480px | 24px | 16px | 48px | toggle buttons stack full width; BibTeX 12px with 16px padding |

## Components

- **Dark pill button** (`.button.is-dark.is-rounded`): #363636, white Noto Sans 16px, padding 7px 20px, full-round radius, 40px tall, 1em icon left; Bulma hover darkens the fill slightly.
- **Venue line**: a bold 20px #555555 text line above the authors, not a badge.
- **Teaser strip**: a wide, frameless white-ground image (912×171 at 1440) followed by a 20px Google Sans caption with italic emphasis.
- **Gray band section**: full-width #f5f5f5 with a centred 32px/600 heading and justified 16px body in a 763px column.
- **Text + figure explainer**: bold 16px content headings, paragraphs with inline math, and a figure with a bold caption on the right at 50% width.
- **Gradient toggle** (`.video-toggle .button`): 58px tall, min-width 17.5rem, radius 23px, padding 0 40px, 19.2px; unselected #fbfbfb fill, 2px #e6e6e6, #555555 text; selected `linear-gradient(110deg, #dff2d8 0%, #edf8f6 52%, #dce8ff 100%)`, 2px #bfe0f3, #25292b 600; gap 1rem.
- **Video carousel** (`.results-carousel .item`): square tiles with 1px #bbbbbb border and 10px radius, 5px margins, autoplay videos; white round arrows and dots with a faint shadow.
- **BibTeX**: Bulma `pre` on #f5f5f5, 14px monospace, padding 17.5px 21px, under a 28px heading.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | absent from the source | no top bar or side nav |
| Title / venue / authors / affiliations | yes | centred Google Sans, bold gray venue line, blue author links |
| Venue badge | present but non-standard | a bold text line, not a pill |
| Link buttons | yes | five dark full-round Bulma buttons |
| Teaser | yes | frameless wide image strip with a 20px caption |
| Abstract | yes | #f5f5f5 band, justified text |
| Method explainer | yes | text with inline math beside a comparison figure |
| Overview figure | yes | wide pipeline diagram with italic-led caption |
| Video carousel with toggle | yes | gradient two-way toggle above three square video tiles |
| Results galleries | yes | further white sections of generated poses |
| Results tables | absent from the source | results are shown as videos |
| BibTeX | yes | Bulma pre on light gray |
| Footer | yes | #fafafa with Creative Commons and template credit text |

## Adapting to Other Content

- **More authors**: keep the 20px Google Sans author line with #209cee links; wrap at 960px, and keep affiliations as a separate 20px #4a4a4a line.
- **A results table**: use a Bulma `.table` inside the 960px column on white; header #363636 600, 16px #4a4a4a cells, 1px #e6e6e6 rules, best value bold.
- **Long publication or news lists**: put them in a #f5f5f5 band section with 16px/24px rows and bold 16px `.content-heading` dates.
- **More video sets**: add a third toggle button with the same 58px recipe; the selected state keeps the green-to-blue gradient.

## Do's and Don'ts

- Do alternate white and #f5f5f5 full-width bands to separate sections.
- Do keep the hero centred and unadorned: title, bold venue line, blue authors, dark pills.
- Do pair explanation text with a figure side by side, using inline math and bold content headings.
- Do frame carousel videos with a 1px #bbbbbb border and 10px radius; leave other figures frameless.
- Don't add a navigation bar or venue pill; the original template has neither.
- Don't colour headings; colour is reserved for author links and the toggle gradient.
- Don't round the teaser or figures.

## Surfaces

White page and sections, #f5f5f5 full-width bands for the Abstract, the carousel hero and the BibTeX block, a #fafafa footer; the only tinted fill is the selected toggle's pale green-to-blue gradient.

## Imagery

Mesh renderings: magenta and pastel octopus meshes morphing through denoising steps, colourful Matérn noise fields (jet and coolwarm) on square grids and a Stanford bunny, a pastel pipeline diagram (pink, blue, gray boxes), and videos of elastic octopus states and yoga poses of humanoid meshes.

## Layout

A centred 960px column with a full-width teaser, then alternating bands: Abstract (gray), explainer (white), overview (white), carousel band (gray, full container), results (white), BibTeX (gray), footer. About 4,100px tall, short for the template.

## Agent Prompt Guide

Quick colors: page #ffffff, band #f5f5f5, footer #fafafa, text #4a4a4a, headings #363636, venue #555555, author links #209cee, toggle border #e6e6e6, selected border #bfe0f3.

1. "Build a centred hero in a 960px column with 48px 24px padding: Google Sans 48px/600 title in #363636, a bold 20px #555555 venue line, 20px authors with #209cee links and superscripts, a 20px affiliation line, then five dark full-round buttons (#363636, white 16px, padding 7px 20px, icon left)."
2. "Make an abstract band: full-width #f5f5f5, padding 48px 24px, centred Noto Sans 32px/600 #363636 heading, justified 16px/24px #4a4a4a text in a 763px column."
3. "Create a two-button toggle above a video carousel: buttons 58px tall, min-width 17.5rem, radius 23px, padding 0 40px, 19.2px text; unselected #fbfbfb with 2px #e6e6e6 and #555555 text; selected linear-gradient(110deg, #dff2d8 0%, #edf8f6 52%, #dce8ff 100%) with 2px #bfe0f3 and #25292b 600. Below, square video tiles with 1px #bbbbbb border and 10px radius."

## Similar Pages

- Nerfies-template project pages that keep Bulma's defaults (dark pill buttons, gray bands, #209cee author links).
- Geometry-processing pages that pair inline-math explanations with side-by-side figures.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --band: #f5f5f5;
  --footer: #fafafa;
  --text: #4a4a4a;
  --heading: #363636;
  --venue: #555555;
  --link: hsl(204, 86%, 53%);
  --button-dark: #363636;
  --tile-border: #bbbbbb;
  --toggle-selected: linear-gradient(110deg, #dff2d8 0%, #edf8f6 52%, #dce8ff 100%);
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --column: 960px;
  --section-pad: 3rem 1.5rem;
}
```

## Provenance

- **URL**: https://matern-fm.github.io/
- **Paper**: Matérn Noise for Triangulation-Agnostic Flow Matching on Meshes (arXiv 2605.19305), Tianshu Kuai, Arman Maesumi, Daniel Ritchie, Noam Aigerman (Université de Montréal & Mila, Brown University).
- **Venue**: ACM Transactions on Graphics (SIGGRAPH 2026).
- **Selection reason**: the arXiv comment states acceptance at SIGGRAPH 2026 (ACM TOG) and links this project page.
- **Template credit**: the Nerfies project-page template (Bulma, bulma-carousel, Font Awesome, Academicons), with a small custom `index.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), an additional computed-style probe, the 1440×900 and tall screenshots, and `index.css` and `index.html` read directly, on 2026-10-28.
