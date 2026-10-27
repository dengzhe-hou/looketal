# DexTrack Orange-Lavender Brand — Style Reference

> A Nerfies page dressed in a team jersey: orange and lavender from the logo all the way into the abstract.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share; the page never fires its load event, so the render was taken after a timeout), the 1440-wide screenshots, the Nerfies `static/css/index.css`, Bulma 0.9 defaults, and the many inline `style` attributes. Color share is measured on the first 1440×900 viewport.

## Overview

A Nerfies (Bulma) page with a brand layer. At the top, a small illustrated logo (a purple hand holding an orange object) sits beside a "DexTrack" wordmark in bold orange #ffa500 "Dex" and lavender #c890fc "Track". The 48px three-line title repeats the trick: "**Track**ing" in violet #b56cf9 and "**Dex**terous" in orange. Below come Nerfies-blue author links, a bold "ICLR 2025", and five dark #363636 pill buttons. The hero is a 912px dark video of a real robot hand, followed by a centred 20px caption whose key phrases are bold in five different colours (violet, pink, green, mint, orange). A #f5f5f5 band holds two Bulma carousels of rounded simulation and real-robot videos. The Abstract keeps the coloured bold keywords (orange, blue, mint, green), so the page is lively but colour-busy. A YouTube embed under "Video" sits close against the heading, and its overlay title visually collides with the section above in the render.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 67.6% (plus near-whites 3.8%), the dark hero video's navy-blacks #181c24 6.8%, #0b1119 6.3%, #13171f 5.7%, slate #4f4e55 5.2% and light grey #dfdedd 4.6% (robot arm). Orange and lavender type are each under 1%.

Anatomy in DOM order (Bulma `container is-max-desktop`, 960px):

1. **Logo + wordmark** — `h1.title.is-1.publication-title` containing a 60×78 image (`margin: 0 -3px -10px 0`) and spans "Dex" (#ffa500) and "Track" (#c890fc), Google Sans 48px / 700, centred (y=48–127). Margin-bottom 24px.
2. **Title** — `h2.title.is-1.publication-title`, Google Sans 48px / 600 (synthesized from the 400 face) / 54px, #363636, centred, three lines (y=151–313); "Track" in #b56cf9 and "Dex" in #ffa500, both bold. Gap 31px.
3. **Authors** — `.publication-authors.is-size-5`, Google Sans 20px / 400, links #209cee, superscripts, comma separated (y=344).
4. **Affiliations** — one line, 20px, #4a4a4a, superscript keys (about y=376).
5. **Venue** — bold "ICLR 2025", 20px / 700, #4a4a4a (y=408–433). Gap 20px.
6. **Buttons** — five Bulma `button is-normal is-rounded is-dark`: 40px tall, padding 7px 20px, #363636 fill, #ffffff Noto Sans 16px, 290486px radius, margin 5px 0, icons left (PDF, arXiv, GitHub, YouTube, slides): "Paper", "arXiv", "Code", "Video", "Slides (100MB)" (y=453–493). Gap 65px.
7. **Hero video** — `section.hero.teaser`, `<video>` 912×513 at y=558, dark scene with the logo and repo URLs burned in.
8. **Caption** — `h2.subtitle.has-text-centered`, Google Sans 20px / 400 / 25px, #4a4a4a, coloured bold phrases (y=1078–1178), below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma background | page |
| Heading Ink | #363636 | Bulma `$text-strong` | title, section titles, dark pill buttons |
| Body Grey | #4a4a4a | Bulma `$text` | body text, affiliations, venue, captions |
| Author Sky | #209cee | Nerfies `.publication-authors a` | author names |
| Dex Orange | #ffa500 | inline `color: orange` | "Dex" in wordmark and title, bold keywords |
| Track Lavender | #c890fc | inline | "Track" in the wordmark |
| Track Violet | #b56cf9 | inline | "Track" in the title |
| Keyword Purple | #9235ee | inline | bold keyword phrases in captions |
| Keyword Blue | #248fec | inline | bold keyword phrases in abstract and captions |
| Keyword Pink | #fd7dd4 | inline | "complex object movements" |
| Keyword Mint | #00ffbf | inline | "subtle in-hand re-orientations", "homotopy optimization" |
| Keyword Green | #09b700 | inline | "adaptivity, generalizability, and robustness" and similar |
| Band Grey | #f5f5f5 | Bulma `.hero.is-light` | carousel band |
| Tile Border | #bbbbbb | Nerfies `.results-carousel .item` | 1px border of carousel video tiles |
| Footer Grey | #fafafa | Bulma `.footer` | footer |
| Video Navy | #181c24 | (video) | dominant tone of the hero video |

## Tokens — Typography

- **Display:** declared `'Google Sans', sans-serif` for `.publication-title`, authors and teaser caption; Google Fonts request `Google+Sans|Noto+Sans|Castoro` (400 only). Rendered: Google Sans 400, with 600/700 synthesized. Substitute: Product Sans, or Plus Jakarta Sans with a real 600.
- **Body:** declared `'Noto Sans', sans-serif`. Rendered: Noto Sans 400. Substitute: Open Sans.
- **Icons:** Font Awesome (bundled), Academicons.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Wordmark | `h1.publication-title` spans | 48px / 700 |
| Paper title | `h2.title.is-1.publication-title` | 48px / 600 / 54px |
| Authors, affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px |
| Venue | `<b>` in authors block | 20px / 700 |
| Teaser caption | `.teaser h2.subtitle` | 20px / 400 / 25px, centred |
| Section title | `h2.title.is-3` | Noto Sans 32px / 600 / 36px, centred |
| Body | `.content.has-text-justified` | Noto Sans 16px / 400 / 24px, justified |
| Keyword highlight | inline span | inherits size, `font-weight: bold`, coloured |
| Buttons | `.button.is-normal` | Noto Sans 16px / 400 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Pill buttons | radius 290486px, 1px transparent border, 40px tall, padding 7px 20px |
| Carousel items | Nerfies `.results-carousel .item`: margin 5px, 1px #bbbbbb border, radius 10px, overflow hidden |
| Carousel arrows | Bulma-carousel white circles with dark chevrons; dots under the track |
| Video embed | `.publication-video`: 16:9 padding box, radius 10px, overflow hidden |
| Shadows | none on the page chrome |
| Divider (declared) | `.line` 1px rgb(172,170,170) and `.horizontal_line` 5px dotted black in an inline style block |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px max at ≥1024px; hero and sections centre within it.
- **Hero:** `.hero-body` padding 48px 24px; title margin-bottom 24px; buttons in `.publication-links` with 5px vertical margins.
- **Teaser:** `.teaser .hero-body` padding-top 0, video 912px (960 − 2×24).
- **Carousel band:** `section.hero.is-light.is-small`, #f5f5f5, `.hero-body` padding 24px (is-small), three items visible per slide at about 290px.
- **Sections:** `section.section` padding 48px 24px; text in `column is-four-fifths` (763px) for Abstract and Video; wider results sections use `columns is-centered` with nested columns.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px | 48px | carousel shows 3 items |
| 769–1023px | 24px | 16px | 48px | container fluid; buttons wrap |
| ≤768px | 24px | 16px | 48px | columns stack; carousel shows 1 item; buttons wrap two per row |

## Components

- **Two-tone wordmark:** small logo image (60px wide, nudged down 10px) followed by "Dex" in #ffa500 and "Track" in #c890fc, 48px bold Google Sans, no space.
- **Coloured-initials title:** the syllables that form the name are bold and coloured inside the title ("Track" #b56cf9, "Dex" #ffa500); the rest #363636.
- **Dark pill button:** Bulma `is-dark is-rounded`, #363636 fill, white 16px Noto Sans, icon left, 40px tall; Bulma hover darkens slightly.
- **Keyword highlight:** inline `<span style="color: …; font-weight: bold">` on 3 to 6 phrases per paragraph, each phrase a different colour from the keyword set.
- **Rounded video carousel:** Bulma-carousel on a #f5f5f5 band, items with 1px #bbbbbb border and 10px radius, autoplay muted loops with native controls.
- **Video embed:** YouTube iframe in a 16:9 rounded box under a centred 32px "Video" heading.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo / wordmark | Yes | illustration + two-tone bold wordmark |
| Title with coloured syllables | Yes | violet and orange inside a black title |
| Authors / affiliations / venue | Yes | Nerfies blue links, bold venue |
| Link buttons | Yes | five dark pills incl. Video and Slides |
| Hero video | Yes | 912px dark real-robot clip |
| Teaser caption | Yes | centred 20px with coloured bold phrases |
| Carousels | Yes | two rounded video carousels on a grey band |
| Abstract | Yes | justified, coloured bold keywords |
| Video embed | Yes | YouTube iframe |
| Results galleries | Yes | many video grids (sim, real-world, homotopy, failure cases) |
| Results table | No (absent from the source) | |
| BibTeX | No (absent from the source) | |
| Footer | Yes | #fafafa, "The template is borrowed from Nerfies" |

## Adapting to Other Content

- **Name without obvious syllables:** colour whichever letters spell the name, keeping exactly two brand colours (orange and lavender/violet) across logo and title.
- **More authors:** the Nerfies author block wraps; keep superscripts and a single affiliation line.
- **Results table:** use Bulma `table is-striped` at 16px Noto Sans, header #363636, and colour only the best method's name in #ffa500 bold; avoid adding more highlight colours.
- **Keyword discipline:** if you reuse the highlight idea, pick two colours from the brand (orange, violet) rather than the six used here.
- **BibTeX:** add a Nerfies `pre` section at the end; the source has none.

## Do's and Don'ts

- Do carry the logo's two colours into the title so the brand reads twice in the first screen.
- Do run media on a #f5f5f5 band in rounded carousels to separate it from text sections.
- Do keep buttons uniform dark pills.
- Don't colour keywords in six hues; it dilutes the brand pair and hurts readability (the mint #00ffbf is hard to read on white).
- Don't place a video embed tight under a heading without margin; the render shows overlap.
- Don't rely on synthesized bold; load Google Sans 500/700 or switch to a family with real weights.

## Surfaces

White page; one #f5f5f5 carousel band; #fafafa footer. Rounded 10px video tiles; no cards or shadows.

## Imagery

A dark real-robot hero video with the logo burned in, simulation clips on chequered floors, real-robot clips on black, the illustrated logo of a purple hand, and coloured human-object interaction renders.

## Layout

Nerfies structure: centred hero (logo, title, authors, buttons), full-width hero video, grey carousel band, then centred 763px text sections alternating with wide video grids. Rendered height about 10,100px.

## Agent Prompt Guide

Quick colors: heading #363636, text #4a4a4a, authors #209cee, brand orange #ffa500, lavender #c890fc, violet #b56cf9, band #f5f5f5, footer #fafafa, buttons #363636 with #ffffff text.

1. "Create a wordmark: a 60px illustrated logo inline before the word 'DexTrack' in 48px bold Google Sans, 'Dex' in #ffa500 and 'Track' in #c890fc; below, a 48px / 600 three-line title in #363636 where the matching syllables are bold #b56cf9 and #ffa500."
2. "Add five dark pill buttons: Bulma is-dark is-rounded, #363636 fill, white 16px Noto Sans, padding 7px 20px, 40px tall, icon left, labels Paper, arXiv, Code, Video, Slides."
3. "Build a carousel band: full-width #f5f5f5 section with 24px padding, a 960px container holding three autoplay video tiles per view, each with 1px #bbbbbb border and 10px radius, white circular arrows at the sides and dots below."

## Similar Pages

- Nerfies-derived Bulma pages with a logo wordmark (for example, pages from Tsinghua and Shanghai Qi Zhi robotics groups).
- Project pages that colour the acronym's letters inside the full title (compare REPA in this collection).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --heading: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --brand-orange: #ffa500;
  --brand-lavender: #c890fc;
  --brand-violet: #b56cf9;
  --band: #f5f5f5;
  --footer: #fafafa;
  --button: #363636;
  --font-display: 'Google Sans', 'Product Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --title-size: 48px;
  --h2-size: 32px;
  --body-size: 16px;
  --radius-tile: 10px;
  --container: 960px;
}
```

## Provenance

- **URL:** https://meowuu7.github.io/DexTrack/
- **Paper:** DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References (arXiv 2502.09614), Xueyi Liu et al.
- **Venue:** ICLR 2025 (stated on the page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the comment.
- **Template credit:** footer reads "The template is borrowed from Nerfies".
- **Evidence used:** render at 1440×900 via a copy of `tools/computed_style.py` that tolerates a missing load event (the page loads 134 videos), screenshot color share, 1440 screenshots (first viewport and tall), page HTML and inline styles, Nerfies and Bulma defaults; 2026-10-28.
