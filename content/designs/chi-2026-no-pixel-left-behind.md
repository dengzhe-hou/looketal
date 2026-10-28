# GapFill — Style Reference

> A clean sheet of animation paper clipped to a gray light table: charcoal pill buttons, a chick in pastel yellow, and an EN/JP switch in the corner.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `style.css`, `script.js` and `index.html` read directly. The page is bilingual: every text node exists twice (`.en-text`, `.jp-text`) and the EN/JP buttons toggle a `lang-jp` class on `body`; the values below are for the default English view. A script adds `.reveal` to every `.content-block` after the first and to `.reveal-part` items, which start at opacity 0 and translateY(16px) (12px for parts) and fade in when 15% enters the viewport, so blocks below the fold are blank in a load-time capture.

## Overview

A single white content card (`.container`, 1000px wide including its 20px side padding) centred on a light gray #f5f5f5 page and lifted only by a faint 0 0 20px rgba(0,0,0,0.03) halo. Everything is centred Roboto: a 35.2px bold #222222 title, a 17.6px author line with the first author bold, a 15.2px affiliation line, a bold 16px CHI '26 venue line and a tiny 11.2px gray WISS '25 line. Seven charcoal #333333 pill buttons with Font Awesome icons (ACM Library, two papers, Posters, Demo Video, Slides, Code) wrap in two rows. The teaser is an illustrated figure of a yellow cartoon chick being colorized, with an 8px radius and soft shadow, followed by a left-aligned italic caption at 60% black with bold italic key phrases. Sections (Abstract, Web Demo, Demo Video, Background and Conventional Methods, design principles, features, user study, BibTeX) open with centred 24px bold #444444 headings over a 1px #dddddd rule. The Web Demo sits in a dashed-border #fafafa frame with a pill launch button. Small EN/JP toggle buttons sit absolutely at the top right of the page, outside the card.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 42.4% (the card) and gray #f5f5f5 34.7% (the page on both sides); taupe #c1b9a5 12.0% and pale yellow #fdf9d1 5.7% from the teaser's line art and yellow chick; near-whites #fdfeff 2.3%, #fcfcfb 1.8%, #f2f5f8 1.0%, #feffff 0.2%. The charcoal pills are too small to form a cluster.

Anatomy in DOM order (desktop 1440px; `.container` max-width 960px plus padding 40px 20px, so the card runs x=220 to 1220 and content x=240 to 1200; everything centred unless noted):

1. **Language switch** (`.lang-switch`, absolute at top 10px, right 20px; y=10, 28px tall): "EN" active (#333333 fill, white text, 1px #333333 border) and "JP" (transparent, black text, 1px #cccccc border); 14.4px Arial (button default font), padding 5px 10px, radius 4px.
2. **Title** (`h1`, y=64, 42px tall): "No Pixel Left Behind: Filling Gaps in Anime Colorization", Roboto 35.2px (2.2em) / 700, line-height 1.2, #222222, one line. Default top margin 23.6px (0.67em) after the card's 40px padding; margin-bottom 10px.
3. **Authors** (`.authors`, y=126, 31px tall): 17.6px (1.1em), #333333, first author bold 700, superscripts. Margin-top 20px.
4. **Affiliations** (`.affiliations`, y=157): 15.2px (0.95em) #111111, "¹ The University of Tokyo; ² OLM Digital, Inc.; ³ IMAGICA GROUP Inc.". Margin-bottom 20px.
5. **Venue** (`.conference`, y=204): "CHI '26: The ACM CHI Conference on Human Factors in Computing Systems (Full Conference Paper)", 16px / 700 #222222. Margin-bottom 20px.
6. **Secondary venue** (`.conference.conference-secondary`, y=250): "& WISS '25: … (Demo Presentation)", 11.2px (0.7em) / 700 #666666. Margin-bottom 20px.
7. **Buttons** (`.link-block`, y=298 to 404, margin 30px 0): seven pills, 43px tall, 5px margins, wrapping into a row of six (y=303) and "Code" centred below (y=356).
8. **Teaser** (`img.teaser-img`, y=434, 960×326): radius 8px, box-shadow 0 4px 10px rgba(0,0,0,0.1), margin-bottom 15px; a "©IIS-P / "Ponnomichi" Production Committee" credit is part of the image.
9. **Teaser caption** (`p.caption.teaser-caption`, y=796, 115px tall): 14.4px (0.9em) italic, line-height 1.6, rgba(0,0,0,0.6), left aligned, key phrases bold. Margin-bottom 40px.

The Abstract heading follows at y=952.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Light Table | #f5f5f5 | (literal, `body`) | page background beside the card |
| Sheet | #ffffff | (literal, `.container`) | content card |
| Charcoal | #333333 | (literal) | body text, pill button fill, active EN button, authors |
| Title Ink | #222222 | (literal) | title, CHI venue line |
| Affiliation Ink | #111111 | (literal) | affiliation line |
| Heading Gray | #444444 | (literal) | section headings (h2) |
| Subheading Gray | #555555 | (literal) | h3 subheadings, pill hover fill |
| Secondary Gray | #666666 | (literal) | WISS venue line |
| Caption Gray | rgba(0,0,0,0.6) | (literal, `.caption`) | teaser caption, grid captions |
| Rule | #dddddd | (literal) | 1px line under h2 |
| Hairline | #eeeeee | (literal) | footer top rule, BibTeX border |
| Toggle Edge | #cccccc | (literal) | inactive JP button border, dashed demo frame border |
| Demo Frame | #fafafa | (literal) | Web Demo frame fill |
| Code Gray | #f4f4f4 | (literal) | BibTeX pre |
| Footer Gray | #999999 | (literal) | footer text |
| Default Link | #0000ee | (browser default) | the plain Web Demo URL link (no link color is set) |
| Video Black | #000000 | (literal) | video container background |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | 'Roboto', "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif | Roboto 400 and 700 (Google Fonts; 300 requested but unused); Japanese glyphs fall back to Hiragino or Meiryo | Inter |
| Language buttons | browser button font | Arial | — |
| Code | monospace | system monospace (Consolas on Windows) | Roboto Mono |
| Icons | Font Awesome 6.0.0 | FA 6 Free 900, FA 6 Brands 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | 35.2px / 700 / 1.2 | #222222 |
| Authors | `.authors` | 17.6px / 400 / 1.6; first author 700 | #333333 |
| Affiliations | `.affiliations` | 15.2px / 400 | #111111 |
| Venue | `.conference` | 16px / 700 | #222222 |
| Secondary venue | `.conference-secondary` | 11.2px / 700 | #666666 |
| Pill button | `.btn` | 14.4px / 700 | white |
| Section heading | `h2` | 24px / 700 / 1.6, centred | #444444 |
| Subheading | `h3` | 19.2px / 700 | #555555 |
| Body | `p` | 16px / 400 / 1.6; abstract justified | #333333 |
| Teaser caption | `.caption.teaser-caption` | 14.4px italic / 1.6, left | rgba(0,0,0,0.6) |
| Grid caption | `.grid-item p` | 14.4px / 1.4, centred | rgba(0,0,0,0.6) |
| BibTeX | `pre` | 0.85em of its parent, 11.05px here, / 1.6 | #333333 |
| Footer | `footer` | 12.8px / 1.6 | #999999 |
| Language toggle | `.lang-btn` | 14.4px / 400 | white on #333333, or black |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Content card | 0 | none | 0 0 20px rgba(0,0,0,0.03) |
| Pill buttons | 30px | none | none; hover #555555 and translateY(-2px) |
| Language buttons | 4px | 1px #cccccc; active 1px #333333 | none |
| All images and the video | 8px | none | 0 4px 10px rgba(0,0,0,0.1) |
| Video container | 8px, overflow hidden | none | none (the video inside carries the shadow) |
| Web Demo frame | 8px | 1px dashed #cccccc | none |
| BibTeX pre | 5px | 1px #eeeeee | none |
| Section heading | 0 | 1px #dddddd bottom, 10px below the text | none |
| Footer | 0 | 1px #eeeeee top | none |

## Layout Metrics

- **Card**: `.container { max-width: 960px; padding: 40px 20px; margin: 0 auto }` on a #f5f5f5 body with no margin; at 1440 the white card is 1000px wide (x=220) and runs the full page height.
- **Header stack**: title margin 23.6px 0 10px; authors margin-top 20px; affiliations, venue and secondary venue each margin-bottom 20px; buttons in `.link-block` with 30px vertical margin and 5px around each pill.
- **Sections**: `h2` margin 40px top, 20px bottom, padding-bottom 10px; `h3` margin-top 30px; paragraphs margin-bottom 15px.
- **Teaser**: full content width (960px), 15px below to the caption, caption margin-bottom 40px.
- **Video**: `.video-container` 16:9 (padding-bottom 56.25%), 960×540, margin-bottom 20px.
- **Web Demo frame**: min-height 240px, padding 20px (282px tall here), flex-centred pill.
- **Grids**: `.grid-2` auto-fit minmax(300px, 1fr) with 20px gap (two 470px columns at 1440); `.grid-3` minmax(200px, 1fr) (three 306px columns); `.media-box` 220px tall image wells; design-principles list max 760px, left aligned.
- **Footer**: margin-top 60px, padding-top 20px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| any width (no media queries) | card padding 20px | 16px | 35.2px | grids collapse automatically below 640px (`.grid-2`) and 660px (`.grid-3`) of content width via auto-fit; buttons wrap |

## Components

- **Pill button** (`.btn`): inline-block, #333333 fill, white Roboto 14.4px / 700, padding 10px 20px, radius 30px, margin 5px, Font Awesome icon with 6px right margin (book, file-pdf, video, desktop, GitHub, external-link). Hover #555555 and translateY(-2px) over 0.3s.
- **Language toggle** (`.lang-btn`): 14.4px, padding 5px 10px, radius 4px, transparent with 1px #cccccc border; active #333333 fill, white text, #333333 border. Switches all `.en-text`/`.jp-text` nodes, swaps the teaser image to its Japanese version and rewrites localized link hrefs.
- **Section heading** (`h2`): centred Roboto 24px / 700 #444444, 1px #dddddd bottom rule 10px below the text, margin 40px 0 20px.
- **Teaser caption**: left-aligned 14.4px italic at rgba(0,0,0,0.6), bold italic phrases for the key steps (a)–(g).
- **Web Demo frame** (`.demo-software-frame`): #fafafa, 1px dashed #cccccc, radius 8px, min-height 240px, a centred pill "Launch the Interactive Web Demo" with an external-link icon; a plain underlined URL line below in browser-default blue.
- **Image grid item** (`.grid-item`): image with the global 8px radius and soft shadow, then a 14.4px / 1.4 centred caption at 60% black with bold method names.
- **BibTeX** (`pre`): #f4f4f4, 1px #eeeeee border, radius 5px, padding 15px, left aligned monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Language toggle | yes | EN/JP buttons, top right of the page |
| Title / authors / affiliations | yes | centred Roboto stack |
| Venue | yes | bold CHI line plus a tiny gray WISS line |
| Link buttons | yes | seven charcoal pills |
| Teaser + caption | yes | rounded shadowed figure, italic left-aligned caption |
| Abstract | yes | justified 16px paragraph |
| Interactive demo | yes | dashed placeholder frame with a launch pill |
| Video | yes | 16:9 autoplaying muted video, 8px radius |
| Method / figures | yes | 2- and 3-column image grids with centred captions |
| Results tables | absent from the source | results are figures |
| BibTeX | yes | gray rounded pre |
| Footer | yes | contact line over a 1px #eeeeee rule |

## Adapting to Other Content

- **More authors**: keep one centred 17.6px line inside the 960px column and let it wrap; bold only the first author; affiliations stay on one 15.2px line separated by semicolons.
- **A results table**: centre it in the 960px column with 14.4px Roboto, header 700 #444444, 1px #dddddd row rules, no fills; caption below at 14.4px rgba(0,0,0,0.6).
- **Long publication or news lists**: use the left-aligned design-principles list (max 760px, 8px between items) with dates bold #333333.
- **More links**: add pills; they wrap and centre, six per row at 1440.
- **A second language**: follow the page's pattern of paired `.en-text`/`.jp-text` spans and swap with the same toggle; keep Hiragino Sans and Meiryo in the stack for Japanese.

## Do's and Don'ts

- Do keep the white card on #f5f5f5 with only the 3% halo.
- Do use #333333 pills with bold 14.4px labels and icons.
- Do give every image the same 8px radius and 0 4px 10px rgba(0,0,0,0.1) shadow.
- Do keep section headings centred, #444444, with the 1px #dddddd rule.
- Don't introduce an accent color; the illustrations supply all color.
- Don't center the teaser caption; it is the one left-aligned italic block.
- Don't enlarge the secondary venue line; it stays at 11.2px.

## Surfaces

Two levels: #f5f5f5 page and a full-height white card. Inside the card, #fafafa for the demo frame, #f4f4f4 for code and a black 16:9 well behind the video.

## Imagery

Flat, pastel anime illustration: a yellow chick character colorized with a paint bucket, pink-outlined gap highlights, zoomed pixel insets, and step labels (a)–(g) in a serif face inside the teaser image. Later figures are paint-software screenshots, system UI captures and study charts. A title-card video opens with CHI26, University of Tokyo and AniMins logos.

## Layout

One centred 960px column inside a white card: header stack, pills, teaser, then sections separated by ruled headings. Grids appear only for side-by-side figures. No navigation, no sidebar.

## Agent Prompt Guide

Quick colors: page #f5f5f5, card #ffffff, text #333333, title #222222, headings #444444, rules #dddddd, captions rgba(0,0,0,0.6), pills #333333 (hover #555555).

1. "Build a white card (max-width 960px, padding 40px 20px, box-shadow 0 0 20px rgba(0,0,0,0.03)) centred on a #f5f5f5 page. Inside, centred Roboto: title 35.2px / 700 #222222, authors 17.6px #333333 with the first name bold, affiliations 15.2px #111111, venue 16px / 700 #222222, secondary venue 11.2px / 700 #666666, each 20px apart."
2. "Make pill buttons: #333333, white Roboto 14.4px / 700, padding 10px 20px, radius 30px, margin 5px, Font Awesome icon 6px before the label; hover #555555 and translateY(-2px). Add an EN/JP toggle positioned absolute at top 10px, right 20px: 14.4px, padding 5px 10px, radius 4px, 1px #cccccc border, active #333333 fill with white text."
3. "Create a section: centred h2 24px / 700 #444444 with a 1px #dddddd bottom border and 10px padding-bottom, margin 40px 0 20px; images with radius 8px and box-shadow 0 4px 10px rgba(0,0,0,0.1); a dashed demo frame (#fafafa, 1px dashed #cccccc, radius 8px, min-height 240px) holding one centred pill."

## Similar Pages

- Bilingual (English/Japanese) research pages from Japanese labs with an in-page language toggle.
- Card-on-gray project pages with charcoal pill buttons.

## Quick Start

```css
:root {
  --page: #f5f5f5;
  --card: #ffffff;
  --text: #333333;
  --title: #222222;
  --heading: #444444;
  --subheading: #555555;
  --rule: #dddddd;
  --hairline: #eeeeee;
  --caption: rgba(0, 0, 0, 0.6);
  --pill: #333333;
  --pill-hover: #555555;
  --font: 'Roboto', "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
  --card-max: 960px;
  --radius-media: 8px;
  --shadow-media: 0 4px 10px rgba(0, 0, 0, 0.1);
}
```

## Provenance

- **URL**: https://marc2825.github.io/GapFill/
- **Paper**: No Pixel Left Behind: Filling Gaps in Anime Colorization (arXiv 2609.00800), Masahiro Kono, Akinobu Maejima, Yuki Koyama, Yotam Sechayk, Takeo Igarashi.
- **Venue**: CHI 2026 (Full Conference Paper); also WISS 2025 demo presentation, as listed on the page.
- **Selection reason**: the arXiv comment states publication in the Proceedings of CHI 2026; the project page is linked in the paper body (arXiv HTML).
- **Template credit**: none stated; hand-built `style.css` and `script.js` with Google Fonts Roboto and Font Awesome 6.0.0.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of the header stack, demo frame, video, grids and footer, the 1440×900 and full-page screenshots, and `style.css`, `script.js` and `index.html` read directly, on 2026-10-28.
