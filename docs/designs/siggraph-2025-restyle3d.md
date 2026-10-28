# ReStyle3D — Style Reference

> A paint palette emoji and a wordmark that shades letter by letter from forest green to teal, set over a gray gallery wall where the room video plays.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the hero, teaser band, overview figure, result players and iframe, the 1440×900 and full-page screenshots, and the page's own `index.html` (inline colour spans and two small `<style>` blocks) plus `css/index.css` and `css/pages.css` read directly. The page is the Nerfies template (Bulma 0.9) with its own touches: a per-letter coloured wordmark, a light-gray video band, coloured icons in the buttons, and custom page-dot controls under the result videos.

## Overview

A white Nerfies page with a centred hero: a 40px "🎨 ReStyle3D" wordmark whose nine letters step from #006400 to #009090, a two-line 48px/600 Google Sans subtitle-title in #363636, a 24px/600 "SIGGRAPH 2025" line, two lines of #3273dc author links at 20.8px with superscripts, an affiliation line, a small "Equal contribution" note, and five dark pills (Paper with an orangered PDF icon, Video with a red YouTube icon, Code, "🤗 Model", Dataset with a small SVG icon). Below the hero, a full-width #f5f5f5 band frames a 912px looping room video under a 20px heading in which "ReStyle3D" repeats the green-to-teal letters. The rest of the page is white: a 960px overview figure with a 950px caption paragraph, an Abstract, "How it works" with two stage diagrams, "Semantic Appearance Transfer" with a 912px figure, three "End-to-end Results" video players with round arrow and dot thumbnails, a 960×640 Sketchfab embed for stylized reconstructions, and BibTeX.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 54.8% (plus #fffffd and #fdffff 1.2%); band gray #f5f5f5 19.0%; peach #cca99a 14.1% and clay #997668 7.6% (the pink-walled room in the teaser video); cool gray #dfe2e6 2.5%; pale apricot #fbdfc8 0.9%. The green-teal wordmark and blue links cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, centred inside `.container.is-max-desktop`, 960px at x=240):

1. **Hero** (`section.hero`, 0–567px): `.hero-body` padding 48px 24px.
2. **Wordmark** (`h2.title.is-2.publication-title`, y=48, 45px): "🎨" emoji then "ReStyle3D" in Google Sans 40px/600 inside `<strong>`; letters coloured #006400, #006666, #006D6D, #007373, #007979, #008080, #008686, #008B8B, #009090 by inline spans. Gap 24px.
3. **Title** (`h1.title.is-1.publication-title`, y=117, 108px, two lines): "Scene-level Appearance Transfer with Semantic Correspondences", Google Sans 48px/600, line-height 54px, #363636. Gap 36px (24px margin + 12px column padding).
4. **Venue** (`h2.title.is-4`, y=261, 27px): "SIGGRAPH 2025", Noto Sans 24px/600 #363636. Gap 18px.
5. **Authors** (inline-styled `div`, font-size 1.3em = 20.8px, line-height 1.6, y=306 and 343): two lines of three names, links #3273dc, superscripts #4a4a4a, 8px left margins between names.
6. **Affiliations** (third line, y≈375): "¹Stanford University ²NVIDIA Research ³Zillow Group", 20.8px #4a4a4a, 10px gaps; then "*Equal contribution" at 0.8em (16.6px). Gap about 20px.
7. **Buttons** (`a.button.is-dark.is-rounded`, y=462, 40px): five #363636 pills, white 16px Noto Sans, padding 7px 20px; icons: Font Awesome `fa-file-pdf` in orangered #ff4500, `fa-youtube` in red #ff0000, `fa-github` white, 🤗 emoji, a 16px dataset SVG. Hero ends at 567.
8. **Teaser band** (`section.hero.teaser.is-small.is-light`, 567–1182): #f5f5f5; heading `h2.title.is-5` at y=591, Google Sans 20px/600 rgba(0,0,0,0.7) with the green-teal "ReStyle3D"; 24px below it the 912×513 autoplay video at y=637.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Forest | #006400 | (inline span) | first letter "R" of the wordmark and of every in-text "ReStyle3D" |
| Teal Step | #008080 | (inline span) | middle letter "l" of the wordmark ramp |
| Teal | #009090 | (inline span) | last letter "D" of the wordmark ramp |
| White | #ffffff | (Bulma `$white`) | page background, button text, GitHub icon |
| Title Charcoal | #363636 | (Bulma `$text-strong`, `$dark`) | title, venue, section titles, button fills |
| Body Gray | #4a4a4a | (Bulma `$text`) | body text, captions, affiliations, superscripts, BibTeX text |
| Link Blue | #3273dc | (Bulma `$link`) | author names, in-text and footer links |
| Gallery Gray | #f5f5f5 | (Bulma `$light`) | teaser video band, BibTeX `pre` |
| Band Ink | rgba(0,0,0,0.7) | (Bulma `.hero.is-light`) | teaser band heading text |
| PDF Orangered | #ff4500 | `orangered` (inline) | Paper button icon |
| YouTube Red | #ff0000 | `red` (inline) | Video button icon |
| Footer Gray | #fafafa | (Bulma `$scheme-main-bis`) | footer |

The full wordmark ramp is #006400, #006666, #006D6D, #007373, #007979, #008080, #008686, #008B8B, #009090.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (`.publication-title`, `.teaser`) | Google Sans 400 (600 synthesized) | Product Sans |
| Text | 'Noto Sans', sans-serif (`body`) | Noto Sans 400 | Noto Sans |
| Code | monospace | system monospace | JetBrains Mono |
| Icons | Font Awesome (SVG via JS) | inline SVG | — |
| Math | MathJax 3 | loaded on demand | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `h2.title.is-2.publication-title strong span` | 40px / 600 / 45px, Google Sans | #006400 → #009090 per letter |
| Title | `h1.title.is-1.publication-title` | 48px / 600 / 54px, Google Sans | #363636 |
| Venue | `h2.title.is-4` | 24px / 600 / 27px, Noto Sans | #363636 |
| Authors | inline `div` (1.3em, line-height 1.6) | 20.8px / 400 / 33.28px, Noto Sans | names #3273dc, rest #4a4a4a |
| Band heading | `.teaser h2.title.is-5` | 20px / 600 / 22.5px, Google Sans | rgba(0,0,0,0.7) |
| Section title | `h2.title.is-3`, `h3.title.is-3` | 32px / 600 / 36px, Noto Sans | #363636 |
| Result heading | `.teaser h2.title.is-4` | 24px / 600 / 27px, Google Sans | #363636 |
| Overview caption | `h2.content` (max-width 950px) | 16px / 400 / 24px | #4a4a4a, method name in small caps |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| Note | `h3.title.is-7` | 12px / 600 | #363636 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px | 1px solid transparent | none |
| Disabled button (declared) | 290486px | none | none; background #4a4a4a, opacity 0.8 |
| Teaser and result videos | 0px | none | none |
| Figures and diagrams | 0px | none | none |
| Sketchfab iframe | 0px | none | none |
| Result page dots (`.pages img`) | SVG shapes, 32px tall | none | none |

## Layout Metrics

- **Containers**: `.container.is-max-desktop` 960px (x=240–1200); videos and figures inside `.hero-body` render 912px (x=264).
- **Hero**: padding 48px 24px; wordmark 48–93, title 117–225, venue 261–288, authors from 306 at 33.28px line-height, buttons 462–502; hero 567px tall.
- **Teaser band**: `section.hero.teaser.is-small.is-light`, #f5f5f5 full width, `.hero-body` padding 24px; heading 24px above a 912×513 video; band 567–1182.
- **Overview**: `section.hero.is-small`, image `.publication-teaser-img` 960×340 at y=1205, caption `h2.content` max-width 950px with margin 16px auto.
- **Abstract**: `section.section.pt-0` (padding 0 24px 48px), 960px justified text.
- **Result players**: three `section.hero.teaser.is-small` blocks, each 658px tall: a 24px/600 Google Sans heading, a 912×513 video, and a centred `.pages` row of 32px-tall SVGs (round left arrow, small circles, round right arrow) 7px below.
- **Sketchfab**: 960×640 iframe under a 24px "Stylized Reconstruction" heading and a 12px note.
- **BibTeX**: `section.section` padding 48px 24px, `pre` padding 17.5px 21px.
- **Footer**: `footer.footer.pt-4.pb-0`, padding 16px 24px 0, #fafafa.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | is-max-desktop 960px | 16px | 48px | as described |
| ≤1023px | containers fluid with 24px padding | 16px | 48px | videos and figures scale to column |
| ≤768px | 24px | 16px | 48px | Bulma columns stack; button row wraps |
| ≤750px | same | 16px | 48px | `.colorbar-img` narrows from 250px to 150px |

## Components

- **Gradient wordmark**: an emoji glyph (🎨) followed by the name in Google Sans 600, each letter wrapped in an inline span with one step of a nine-step ramp from #006400 to #009090; reused at 20px inside headings and captions wherever the method is named.
- **Dark pill button with coloured icon** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, white 16px Noto Sans, height 40px, padding 7px 20px, radius 290486px; the icon keeps its brand colour (PDF #ff4500, YouTube #ff0000) or is an emoji (🤗) or a 16px SVG.
- **Gray video band** (`section.hero.teaser.is-small.is-light`): full-width #f5f5f5, 24px padding, centred 20px/600 Google Sans heading in rgba(0,0,0,0.7), 912px video with no frame.
- **Overview figure**: 960px image, then a 16px caption paragraph (max-width 950px) that begins "Overview of ReStyle3D." with the name in small caps.
- **Result player**: centred 24px/600 Google Sans heading, 912×513 video, and a `.pages` control row of SVG round arrows and small circles (32px tall) that switch videos on click.
- **BibTeX**: Bulma `pre` #f5f5f5, padding 17.5px 21px, 14px monospace #4a4a4a.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo / wordmark | yes | emoji plus green-to-teal per-letter name |
| Title / venue / authors | yes | centred Nerfies hero, #3273dc names |
| Link buttons | yes | five dark pills with brand-coloured icons and emoji |
| Teaser video | yes | 912px video in a #f5f5f5 band |
| Overview figure | yes | 960px image with a long caption paragraph |
| Abstract | yes | 960px justified text |
| Method diagrams | yes | two-stage figures and a 912px semantic-transfer figure |
| Results | yes | three video players with SVG page controls |
| 3D viewer | yes | Sketchfab playlist iframe |
| Results tables | absent from the source | results are videos and figures |
| BibTeX | yes | Bulma `pre` |
| Footer | yes | #fafafa, Nerfies credit |

## Adapting to Other Content

- **More authors**: keep the 20.8px block with three names per line and 8px margins; add lines with `<br>` rather than letting it wrap freely, as the source does.
- **A results table**: place it in a `section.section` at 960px; header 600 #363636, 1px #dbdbdb rules, white cells; write the method name with the green-teal letter ramp in its row label and keep numbers #4a4a4a.
- **Long publication or news lists**: a `section.section` with a centred 32px/600 heading and a 16px list in the 960px column, dates bold.
- **More videos**: add another `section.hero.teaser.is-small` player (24px heading, 912px video, `.pages` dot row), or a gray `is-light` band for a single hero-level video.
- **A different method name**: build its ramp in the same way, one inline span per letter, from a dark green to teal or another adjacent-hue pair, nine steps or one per letter.

## Do's and Don'ts

- Do colour the method name letter by letter from #006400 to #009090 every time it appears in a heading.
- Do keep the teaser video in a full-width #f5f5f5 band directly under the hero.
- Do let button icons keep their brand colours on the #363636 pills.
- Do show results as 912px videos with the small round SVG controls below.
- Don't apply the green-teal ramp to body links; links stay #3273dc.
- Don't frame the videos; they sit edge to edge on the gray or white ground.
- Don't add more gray bands; only the teaser band is tinted.

## Surfaces

White page with one full-width #f5f5f5 band for the teaser video; #f5f5f5 also in the BibTeX `pre`; #fafafa footer. No cards or shadows.

## Imagery

Real indoor scenes (living rooms, bedrooms) captured as video and restyled to match a design image; overview and method figures with labelled rows of room photos, arrows and pastel blocks; a Sketchfab viewer of stylized 3D reconstructions.

## Layout

A centred 960px Nerfies column: a 567px hero, a full-width gray video band, then overview, Abstract, How it works, Semantic Appearance Transfer, three End-to-end Results players, the 3D viewer and BibTeX.

## Agent Prompt Guide

Quick colors: background #ffffff, band #f5f5f5, title #363636, body #4a4a4a, links #3273dc, pills #363636, wordmark ramp #006400 → #008080 → #009090, icons #ff4500 and #ff0000, footer #fafafa.

1. "Build a centred Nerfies hero (960px container, padding 48px 24px): an emoji plus the method name in Google Sans 40px/600 with each letter coloured along a ramp from #006400 to #009090; title Google Sans 48px/600 #363636 on two lines; 'SIGGRAPH 2025' Noto Sans 24px/600 #363636; author lines at 20.8px, line-height 1.6, names #3273dc with #4a4a4a superscripts, three per line."
2. "Make dark pills: #363636, white 16px Noto Sans, padding 7px 20px, radius 290486px; icons keep brand colours: PDF #ff4500, YouTube #ff0000, GitHub white, plus emoji icons where suitable."
3. "Add a full-width gray band (#f5f5f5, padding 24px) under the hero: a centred Google Sans 20px/600 heading in rgba(0,0,0,0.7) with the method name in the green-teal letter ramp, then a 912px autoplay video with no border."

## Similar Pages

- Nerfies-template pages that brand the method name with per-letter colour or gradient text.
- Scene-editing and 3D stylization pages with a gray video band and Sketchfab embeds.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --band: #f5f5f5;
  --title: #363636;
  --text: #4a4a4a;
  --link: #3273dc;
  --pill: #363636;
  --ramp-start: #006400;
  --ramp-mid: #008080;
  --ramp-end: #009090;
  --icon-pdf: #ff4500;
  --icon-video: #ff0000;
  --footer: #fafafa;
  --font-display: "Google Sans", sans-serif;
  --font-text: "Noto Sans", sans-serif;
  --container: 960px;
  --radius-pill: 290486px;
}
```

## Provenance

- **URL**: https://restyle3d.github.io/
- **Paper**: ReStyle3D: Scene-Level Appearance Transfer with Semantic Correspondences (arXiv 2502.10377), Liyuan Zhu, Shengqu Cai, Shengyu Huang, Gordon Wetzstein, Naji Khosravan, Iro Armeni.
- **Venue**: SIGGRAPH 2025 (page BibTeX: SIGGRAPH 2025 Conference Papers; the arXiv comment reads "SIGGRAPH 2025. Project page ...", a weak acceptance wording flagged in selection).
- **Selection reason**: a logo mark plus a coloured wordmark, a gray band framing the hero video and a well-captioned overview figure; a polished take on the template.
- **Template credit**: footer states the template is based on Nerfies (Bulma 0.9, Bulma Carousel, twentytwenty, Font Awesome, MathJax 3).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and the page's `index.html`, `css/index.css` and `css/pages.css` read directly, on 2026-10-28.
