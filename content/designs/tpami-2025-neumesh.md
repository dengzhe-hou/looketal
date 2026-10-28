# NeuMesh++ — Style Reference

> A wire sculpture on a museum plinth: the name spun from pale blue mesh above a plain white gallery of demo reels.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css` read with `index.html`. The base is the Nerfies/HyperNeRF Bulma template (Bulma 0.9, bulma-slider, slick carousel CSS, Font Awesome 5, Academicons); most of `index.css` is template leftovers (interpolation panels, hyper-space widgets, author portraits) that no element on this page uses. The single custom touch in the header is an image wordmark and an inline `color:#5a6268` on the venue line. There is no dark mode.

## Overview

A long (9,600px), centred, video-heavy project page on white. A 52px white Bulma navbar carries only a centred "More Research" dropdown with a blue chevron. The signature is the wordmark: "NeuMesh++" rendered as an image of letters woven from pale blue wire mesh with a soft mirror reflection, 774×257px in a 7/12 column. Under it sit a two-line Google Sans 40px title in #363636, a grey "IEEE TPAMI 2025" line at 32px, sky-blue author names #209cee with superscripts, affiliations and a 16px contribution note, and five charcoal pill buttons (Paper, arXiv, Video, GUI Video, Code) with white icons. A 960×540 GUI demo video follows with a centred 20px caption (italic "NeuMesh++"), then a justified abstract in a 763px column, two embedded YouTube players with 10px rounded corners, a hairline divider and a long run of centred 32px section titles (Framework Overview, Real-Time Interactive Editing, Geometry Editing, … Hybrid Editing), each with a justified paragraph and a 960px video. A grey BibTeX block and a #fafafa footer close the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 67.7% plus #fefefe / #fefdfe 11.4%; pale steel blue #9cbec9 8.8% (the mesh wordmark and the blue marbled backdrop of the demo video); slate #49636d 6.5% (wordmark shadows, title text, buttons); pale grey-blue #edf1f3 5.1% (the wordmark reflection). The #209cee author names are too small to form a cluster.

Anatomy in DOM order (desktop 1440px, everything centred; Bulma `.container` is 1344px at x=48):

1. **Navbar** (`nav.navbar`, 0–52px): white; a single centred "More Research" dropdown link, Noto Sans 16px #4a4a4a, padding 8px 40px 8px 12px, with a 10px chevron drawn by `::after` (3px #3273dc left and bottom borders, rotated -45deg).
2. **Hero** (`section.hero > .hero-body`, 52–780px): padding 48px 24px.
3. **Wordmark image** (y=100, 774×257px, x=333): inside a centred `column is-7` (798px with 12px padding); no border.
4. **Title** (`h1.title.is-2.publication-title`, y=387, 90px): Google Sans 40px/600, line-height 45px, #363636, two lines broken by `<br/>`; margin-bottom 24px.
5. **Venue** (`h1.title.is-size-3`, y=501): "IEEE TPAMI 2025", Noto Sans 32px/600, line-height 36px, #5a6268 (inline style); margin-bottom 24px.
6. **Authors** (`.is-size-5.publication-authors`, y=561): Google Sans 20px, line-height 30px; names #209cee (hsl(204,86%,53%)), commas and superscripts #4a4a4a.
7. **Affiliations** (y=596): 20px #4a4a4a, one line with superscript numbers.
8. **Note** (`.is-size-6`, y=631): "*Equal contribution. †Corresponding authors." 16px.
9. **Buttons** (`.publication-links`, y=670; pills at y=675, 40px tall): five Bulma `is-rounded is-dark` pills with 5px vertical margins and 4–5px between them (inline-block spacing).
10. **Teaser video** (`section.hero.teaser`, hero body padding 0 24px 48px; video at y=780): 960×540px, x=240; the video top edge is visible at the bottom of the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (literal) | page, navbar, button text and icons |
| Text Grey | #4a4a4a | (Bulma body) | body text, affiliations, notes, captions, abstract, navbar link, BibTeX text |
| Heading Grey | #363636 | (Bulma `.title`, `is-dark`) | paper title, section titles, button fill |
| Venue Slate | #5a6268 | (inline style) | "IEEE TPAMI 2025" line |
| Author Blue | #209cee | hsl(204, 86%, 53%) | author names |
| Link Blue | #3273dc | (Bulma link) | navbar chevron, footer links |
| Light Grey | #f5f5f5 | (Bulma `hr`, `pre`) | 2px divider fill, BibTeX background |
| Footer Grey | #fafafa | (Bulma `.footer`) | footer background |
| Mesh Blue | #9cbec9 | (image) | wordmark wire letters (part of the PNG) |
| Video Black | #000000 | (literal) | YouTube player letterbox |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors / teaser | 'Google Sans', sans-serif | Google Sans 400; 600 synthesised | Outfit |
| Body / headings | 'Noto Sans', sans-serif | Noto Sans 400; 600 synthesised | Open Sans |
| Code | monospace | system monospace (Consolas on Windows) | IBM Plex Mono |
| Icons | Font Awesome 5 (SVG), Academicons | inline SVG; Academicons 400 for arXiv | — |
| Wordmark | image (title.png) | raster | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | Google Sans 40px / 600 / 45px | #363636 |
| Venue line | `h1.title.is-size-3` | Noto Sans 32px / 600 / 36px | #5a6268 |
| Authors / affiliations | `.is-size-5.publication-authors` | Google Sans 20px / 400 / 30px | #209cee names, #4a4a4a text |
| Note | `.is-size-6.publication-authors` | Google Sans 16px / 400 | #4a4a4a |
| Teaser caption | `.teaser h2.subtitle` | Google Sans 20px / 400 / 25px, centred; name italic | #4a4a4a |
| Section title | `h2.title.is-3` | Noto Sans 32px / 600 / 36px | #363636 |
| Video heading | `h2.title.is-2` | 40px / 600 / 45px | #363636 |
| Video sub-heading | `h2.title.is-5` | 20px / 600 / 22.5px | #363636 |
| Body / abstract | `.content.has-text-justified` | Noto Sans 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-rounded.is-dark` | Noto Sans 16px / 400 | #ffffff |
| BibTeX | `pre` | 14px / 1.5 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill buttons | 290486px (Bulma `is-rounded`) | 1px transparent | none |
| YouTube embeds (`.publication-video`) | 10px (`!important`) | none | none |
| Demo videos and figures | 0 | none | none |
| Divider (`hr`) | 0 | none; 2px #f5f5f5 fill | none |
| Navbar chevron | 2px | 3px #3273dc left and bottom | none |
| BibTeX `pre` | 0 | none | none |

## Layout Metrics

- **Containers**: Bulma `.container` 1344px at x=48 for the hero; content sections use `.container.is-max-desktop` (960px at x=240); abstract and YouTube embeds sit in a 4/5 column (763px at x=338).
- **Hero**: body padding 48px 24px; wordmark column is-7 (798px, image 774px); title→venue 24px, venue→authors 24px; authors, affiliations and note stacked on 30px lines; buttons 5px vertical margins.
- **Teaser**: `.teaser .hero-body` padding 0 24px 48px; 960×540 video; 20px caption directly below.
- **Sections**: `.section` padding 48px 24px; section titles margin-bottom 24px; each editing section is title → justified paragraph → 960px video; a full-width `hr` (2px #f5f5f5, margin 24px 0) separates the abstract/video block from the editing gallery and the gallery from BibTeX.
- **YouTube embeds**: 763 × 429px (56.25% padding-bottom), radius 10px.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (incl. 1440) | `.container` 1344px; content 960px | 16px | 40px | wordmark in 7/12 column |
| 1216–1407px | `.container` 1152px | 16px | 40px | — |
| 1024–1215px | `.container` 960px | 16px | 40px | navbar dropdown inline |
| ≤1023px | 24px section padding | 16px | 40px | Bulma navbar collapses to a burger |
| ≤768px | 24px | 16px | 40px | columns stack; wordmark spans the full width |

## Components

- **Image wordmark**: the project name as a raster title image (pale blue wire-mesh letters with a fading mirror reflection on white), centred at 774px; no HTML title for the name itself (the `h1` for it is commented out).
- **Venue line**: plain 32px/600 heading in slate #5a6268 between title and authors, no badge.
- **Pill button** (`.external-link.button.is-rounded.is-dark`): #363636 fill, white Noto Sans 16px, padding 7px 20px, fully rounded, 40px tall, 24px white icon box (file-pdf, Academicons arXiv, YouTube, YouTube, GitHub).
- **Teaser block**: 960×540 video with no frame, then a centred 20px Google Sans caption whose method name is italic.
- **Rounded YouTube embed** (`.publication-video`): responsive 16:9 wrapper, radius 10px, under a centred 20px/600 sub-heading.
- **Editing section**: centred 32px/600 #363636 title, justified 16px paragraph in the 960px column, then a 960px demo video, repeated for each editing mode.
- **Dropdown navbar**: one centred "More Research" link listing sibling projects (NeuMesh, Object-NeRF, NR-in-a-Room, …) with a blue chevron.
- **BibTeX**: Bulma `pre` on #f5f5f5, 14px #4a4a4a, padding 17.5px 21px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | white bar with a centred "More Research" dropdown |
| Wordmark | yes | textured mesh-letter image with reflection |
| Title / venue / authors / affiliations | yes | centred; blue names; slate venue line |
| Link buttons | yes | five charcoal pills with white icons |
| Teaser | yes | 960px GUI demo video with italic-name caption |
| Abstract | yes | justified 16px text in a 763px column |
| Video embeds | yes | two YouTube players with 10px radius |
| Framework figure | yes | 960px image under "Framework Overview" |
| Demo gallery | yes | ten titled sections, each with paragraph and 960px video |
| Results tables | absent from the source | — |
| BibTeX | yes | grey `pre` |
| Footer | yes | #fafafa with HyperNeRF/NeuMesh credit |

## Adapting to Other Content

- **More authors**: authors wrap within 1344px at 20px; keep affiliations on their own 20px line and notes at 16px.
- **No wordmark image**: set the name as a 48px Google Sans 600 #363636 heading (Bulma `is-1`) where the image sits; do not imitate the mesh texture with CSS.
- **A results table**: centre it in the 960px column under a 32px/600 #363636 title; header 16px/600 #363636 with a 2px #f5f5f5 bottom rule, body 16px #4a4a4a, best values bold.
- **News or updates**: a short centred list under the buttons, 16px #4a4a4a, dates bold, no boxes.
- **More editing modes**: add another titled section (32px title, justified 16px paragraph, 960px video) in the same column; keep sections 24px apart by title margin.

## Do's and Don'ts

- Do let the wordmark image carry the identity; everything else stays Bulma-plain.
- Do keep the venue as a quiet 32px slate #5a6268 line, not a badge.
- Do give each demo a centred title and a short justified paragraph above a full-width 960px video.
- Do round only the YouTube embeds (10px); local videos stay square.
- Don't add colored backgrounds or cards; the page is white with one #f5f5f5 divider and code block.
- Don't color buttons; all five are charcoal pills.
- Don't shrink demo videos below the 960px column at desktop.

## Surfaces

White page and navbar, a 2px #f5f5f5 divider, a #f5f5f5 BibTeX block and a #fafafa footer. All color comes from the wordmark image and the videos.

## Imagery

A pale blue wire-mesh wordmark with reflection; a GUI demo video of an interactive editor (a toy mouse on white, control panel at the right) over a turquoise marbled backdrop; YouTube title cards on black; a framework diagram; and many editing demo videos (geometry deformation, physical simulation, texture swapping, filling and painting) on neutral backgrounds.

## Layout

Centred. A 1344px hero holding the 774px wordmark and header text, then a 960px column for the teaser, a 763px column for the abstract and YouTube embeds, and a 960px column for the long gallery of editing sections, ending with BibTeX and the footer.

## Agent Prompt Guide

Quick colors: page #ffffff, text #4a4a4a, headings #363636, venue #5a6268, author links #209cee, navbar chevron #3273dc, code and divider #f5f5f5, footer #fafafa.

1. "Build a centred hero (padding 48px 24px): a wordmark image 774px wide, then a Google Sans 40px/600 title with 45px line-height in #363636, a 32px/600 venue line in #5a6268, 20px Google Sans authors in #209cee with superscripts, a 20px #4a4a4a affiliation line and a 16px note, each 24px or one line apart."
2. "Make link pills: Bulma-style #363636 buttons, fully rounded, padding 7px 20px, 40px tall, white Noto Sans 16px with a white 24px icon on the left (PDF, arXiv, YouTube, GitHub), 5px vertical margins, centred in one row."
3. "Create a demo section in a 960px column: a centred Noto Sans 32px/600 #363636 title with 24px below, a justified 16px/24px #4a4a4a paragraph, then a 960×540 video with no frame; for YouTube embeds use a 16:9 wrapper with border-radius 10px."

## Similar Pages

- HyperNeRF/Nerfies Bulma pages whose identity rests on a custom title image rather than CSS.
- ZJU3DV project pages that share the "More Research" dropdown navbar and long demo-video galleries.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #4a4a4a;
  --heading: #363636;
  --venue: #5a6268;
  --author: #209cee;
  --link: #3273dc;
  --code-bg: #f5f5f5;
  --footer-bg: #fafafa;
  --font-title: "Google Sans", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --content-width: 960px;
  --embed-radius: 10px;
}
```

## Provenance

- **URL**: https://zju3dv.github.io/neumeshplusplus/
- **Paper**: NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field, Chong Bao, Yuan Li, Bangbang Yang, Yujun Shen, Hujun Bao, Zhaopeng Cui, Yinda Zhang, Guofeng Zhang (Zhejiang University State Key Lab of CAD&CG; Ant Research; Google; ByteDance).
- **Venue**: IEEE TPAMI 2025.
- **Selection reason**: found in an arXiv cs.CV listing scan; the arXiv comment reads "TPAMI 2025; Project Page: ..."; curl returned 200 text/html. Chosen over the similar ViewCrafter and MOWA pages for its stronger wordmark.
- **Template credit**: footer reads "The website template is borrowed from HyperNeRF" and links NeuMesh; Bulma 0.9, slick, bulma-slider, Font Awesome 5, Academicons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the hero, authors, buttons, teaser caption, sections, embeds, videos, divider, navbar chevron and footer links, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
