# RoSE Normal Map Classic — Style Reference

> The Nerfies house style wearing iridescent normal maps: grey type, blue names, and lavender-cyan surfaces doing all the talking.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's `static/css/index.css` (the stock Nerfies file), `twentytwenty.css`, Bulma and bulma-carousel. Google Fonts serves only the regular weights of Google Sans and Noto Sans to this page (the stylesheet link asks for `family=Google+Sans|Noto+Sans|Castoro` without weights), so every 600-weight heading renders as a browser-synthesized bold of the 400 face. Color share is measured on the first viewport.

## Overview

A white, centered Nerfies-template page. The header stacks a two-line Google Sans title in charcoal, a large "ICLR 2026 (Oral)" line, ten blue author links over two lines, two lines of grey affiliations, an equal-contribution note, and four charcoal pill buttons (arXiv, Video, Code, Dataset). The teaser is a single 912px image that combines a qualitative strip (reference image, then DSINE, StableNormal, Neural LightRig, NiRNE and Ours as purple-blue normal maps of a warrior figure and a spaceship) with a grouped bar chart of mean angular error where "Ours" is lowest. A one-line caption follows. Then a justified abstract, a teapot "3D misalignment" figure with red and blue zoom boxes, a Gallery band on light grey (#f5f5f5) with an autoplaying carousel of before/after sliders that reveal RGB photos and normal maps, a pipeline figure and BibTeX.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 78.9%, sky #9fc1d7 4.8%, plum #5b3e70 4.1% (dark render areas), lavender #a68dd1 3.8% and periwinkle #7187ce 3.2% (normal-map surfaces), cool grey #e7e8ec 3.1%. Charcoal title and buttons and blue author links are each under 1.5%.

Anatomy in DOM order (centered on x=720; Bulma `.container.is-max-desktop`, 960px):

1. **Title** — `h1.title.is-1.publication-title`, Google Sans 48px, weight 600 requested and rendered as synthesized bold of the 400 face, line-height 54px, #363636, two lines (y=48–156). Margin-bottom 24px.
2. **Venue** — `h3.title.has-text-centered`, "ICLR 2026 (Oral)", Noto Sans 32px, synthesized bold, #363636 (y=180–216). Margin-bottom 24px.
3. **Authors** — `.is-size-5.publication-authors`, Google Sans 20px, links #209cee, superscript markers (`*` equal contribution, `†` corresponding), two lines (y=247–306).
4. **Affiliations** — second `.is-size-5.publication-authors`, Google Sans 20px, #4a4a4a, two lines (about y=318–375).
5. **Note** — `.is-size-6.publication-authors`, "*Equal Contribution †Corresponding Author", 16px, #4a4a4a (about y=395–418).
6. **Buttons** — four `a.external-link.button.is-dark.is-rounded`, 40px tall, #363636, #ffffff Noto Sans 16px, padding 7px 20px, pill, 5px vertical margins and about 4px apart, icon left (y=447–487). Hero body bottom padding 24px.
7. **Teaser** — `section.hero.teaser img`, 912×559px at y=552: six labeled columns of normal maps over a bar chart "Comparison of Methods on Three Datasets".
8. **Caption** — `h2.subtitle.has-text-centered`, "RoSE is the new state-of-the-art method for monocular normal estimation.", Google Sans 20px / 400, #4a4a4a (y=1118). Teaser body bottom padding 48px.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `$white` | page background, button text |
| Charcoal | #363636 | Bulma `$grey-darker` / `.title` | title, venue line, section titles, button fill |
| Body Grey | #4a4a4a | Bulma body | affiliations, note, captions, abstract text, `pre` text |
| Author Blue | #209cee | `.publication-authors a` (`hsl(204,86%,53%)`) | author links |
| Light Band | #f5f5f5 | Bulma `.hero.is-light`, `pre` | Gallery band, BibTeX block |
| Band Text | rgba(0,0,0,0.7) | Bulma `.hero.is-light` | text color inside the Gallery band |
| Footer Fog | #fafafa | Bulma `.footer` | footer |
| Slide Frame | #bbbbbb | `.results-carousel .item-list` | 1px border of gallery slides |
| Slide Base | #000000 | `.results-carousel .item-list` | slide background behind the slider images |

## Tokens — Typography

- **Headings and authors:** `'Google Sans', sans-serif` (`.publication-title`, `.publication-authors`, `.teaser`); renders Google Sans 400 only, with synthesized bold where 600 is asked. Substitute: Product Sans, or Outfit 500 to approximate the faux-bold title.
- **Body:** Bulma's stack is replaced by `'Noto Sans', sans-serif`; renders Noto Sans 400 only, synthesized bold for `.title` headings. Substitute: Open Sans.
- **Code:** browser monospace (Consolas on Windows).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.title.is-1.publication-title` | 48px / 600 (synthesized) / 1.125 |
| Venue line | `h3.title` | 32px / 600 (synthesized) / 1.125 |
| Section title | `h2.title.is-3` | 32px / 600 (synthesized), centered |
| Authors, affiliations | `.is-size-5.publication-authors` | 20px / 400 / 1.5 |
| Note | `.is-size-6.publication-authors` | 16px / 400 |
| Captions | `h2.subtitle` | 20px / 400 / 1.25 |
| Abstract | `.content.has-text-justified` | 16px / 400 / 1.5, justified |
| Buttons | `.button.is-dark` | 16px / 400 |
| Code | `pre` | 14px / 1.5 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | pill radius (Bulma `is-rounded`, 290486px), padding 7px 20px |
| Gallery slides | 10px radius, 1px #bbbbbb border, overflow hidden, 56px bottom margin for pagination |
| Carousel arrows | Bulma round arrows with `box-shadow: 0 0 12px rgba(0,0,0,1)`, 15px in from each edge |
| Carousel dots | white with `0 0 4px rgba(0,0,0,1)` shadow |
| Before/after slider | twentytwenty white handle and divider, aspect 4:3 (horizontal) or 3:4 (vertical) |
| Teaser and figures | square corners, no shadow |
| `pre` | no radius, padding 17.5px 21px |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px (x=240–1200 at 1440); abstract column `is-four-fifths` (768px).
- **Hero:** `.hero-body` padding 48px 24px; teaser body padding 0 top, 48px bottom.
- **Sections:** `.section` padding 48px 24px; Gallery heading section padding 0 24px 16px, band `margin-top` 16px.
- **Teaser:** 912px image (95% of the column).
- **Gallery:** full-width #f5f5f5 band, carousel container 1344px (x=48–1392), three slides visible.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px | 48px | three gallery slides |
| 769–1023px | 24px | 16px | 48px | columns stay side by side |
| ≤768px | 24px | 16px | 48px (Bulma `is-1` has no mobile step) | columns stack; carousel keeps its slide count unless a breakpoint is set (the testimonials carousel sets one) |

## Components

- **Charcoal pill button:** Bulma `.button.is-dark.is-rounded`, #363636 fill, #ffffff 16px label, padding 7px 20px, icon left (academicons arXiv, YouTube, GitHub, a dataset icon); Bulma hover darkens the fill slightly.
- **Author line:** inline-block author spans, #209cee links with underline on hover, superscript numbers and symbols.
- **Combined teaser:** one image holding a labeled qualitative comparison strip and a grouped bar chart (orange, blue, green bars per method, black average line, red value for Ours).
- **Misalignment callout:** a figure of six teapots with red zoom boxes on normals and blue on surfaces, captioned in 20px #4a4a4a.
- **Before/after gallery card:** twentytwenty slider inside a 10px-radius slide with a 1px #bbbbbb border; drag the white circular handle to reveal the RGB render against its normal map; three per view, autoplaying, looping.
- **BibTeX:** Bulma `pre` on #f5f5f5, 14px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors / affiliations | Yes | stock Nerfies header with large venue line |
| Link buttons | Yes | four charcoal pills |
| Teaser | Yes | qualitative strip plus bar chart in one image |
| Abstract | Yes | justified 16px in a four-fifths column |
| Illustration / callout figure | Yes | 3D misalignment teapots |
| Gallery | Yes | before/after slider carousel on a grey band |
| Method figure | Yes | pipeline image with caption |
| Results table (HTML) | No (absent from the source) | numbers live in the teaser chart |
| Video | Present but non-standard | link button only |
| BibTeX | Yes | grey `pre` |
| Footer | Yes | #fafafa, "Website template based on Nerfies" |

## Adapting to Other Content

- **More authors:** the source already runs ten names over two 20px lines; keep inline blocks and let them wrap, with affiliations on their own 20px grey lines.
- **Results table:** a centered Bulma `.table` in the four-fifths column, Noto Sans 16px, #363636 bold headers, best in bold; no colored fills, matching the page's restraint.
- **Long publication or news list:** a plain `ul` in the four-fifths column, 16px #4a4a4a, dates bold.
- **Video teaser:** swap the teaser image for a 912px autoplay loop and keep the 20px caption below.
- **Real bold:** request the weights in the font link (`Google+Sans:400,600`, `Noto+Sans:400,600`) so headings stop using synthesized bold.

## Do's and Don'ts

- Do keep the chrome to charcoal, grey and one blue for names; the normal maps provide all the color.
- Do use the grey `.hero.is-light` band only for the interactive gallery.
- Do put before/after pairs in sliders rather than side by side when they share a viewpoint.
- Don't round or shadow figures.
- Don't add a second link color; keep inline links Bulma's default blue family.
- Don't leave weight-600 headings on a 400-only font load if a crisp bold matters.

## Surfaces

White page and header, one #f5f5f5 gallery band, #f5f5f5 code block, #fafafa footer. Gallery slides have black bases behind white-background renders.

## Imagery

Purple-cyan-pink surface-normal maps of characters, vehicles, helmets, bottles and teapots; RGB renders on white; a grouped bar chart; a pipeline diagram.

## Layout

Single centered 960px column with one full-width grey band. Rendered height about 4,500px, among the shortest in the set.

## Agent Prompt Guide

Quick colors: text #363636, body #4a4a4a, author links #209cee, band #f5f5f5, footer #fafafa, slide border #bbbbbb, page #ffffff.

1. "Build a Nerfies header: centered Google Sans 48px title in #363636; a 32px venue line 'ICLR 2026 (Oral)'; 20px Google Sans authors with #209cee links and superscripts; 20px #4a4a4a affiliations; a 16px note; four pill buttons with #363636 fill, #ffffff 16px Noto Sans labels, padding 7px 20px and an icon on the left."
2. "Create a gallery band: full-width #f5f5f5 section with a carousel showing three slides; each slide has a 10px radius, 1px #bbbbbb border and holds a before/after slider (white handle) comparing an RGB render and its normal map; arrows with a 0 0 12px black glow, white dots below."
3. "Add a teaser: one 912px image combining a labeled method-comparison strip and a bar chart, square corners, followed by a centered 20px Google Sans #4a4a4a caption."

## Similar Pages

- Nerfies template pages (stock `index.css`, Bulma, Google Sans titles).
- Normal and depth estimation pages that pair a comparison strip with a metric chart in the teaser.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --author-link: #209cee;
  --band: #f5f5f5;
  --footer: #fafafa;
  --slide-border: #bbbbbb;
  --font-heading: 'Google Sans', 'Outfit', sans-serif;
  --font-body: 'Noto Sans', 'Open Sans', sans-serif;
  --title-size: 48px;
  --h2-size: 32px;
  --author-size: 20px;
  --body-size: 16px;
  --container: 960px;
  --btn-padding: 7px 20px;
  --slide-radius: 10px;
}
```

## Provenance

- **URL:** https://xinhua694.github.io/RoSE.github.io/
- **Paper:** Monocular Normal Estimation via Shading Sequence Estimation (RoSE, arXiv 2602.09929), Zongrui Li, Xinhua Ma et al.
- **Venue:** ICLR 2026, Oral (stated under the title).
- **Selection reason:** the arXiv comment reads "ICLR 2026 (Oral)" and links the page; chosen for its teaser that combines a qualitative strip with a summary bar chart, the callout illustration and the before/after slider gallery.
- **Template credit:** footer reads "Website template based on Nerfies".
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `static/css/index.css`, carousel options in the page script, page HTML; 2026-10-28.
