# Collaposer — Style Reference

> A scrapbook laid on a drafting table: black hairline rules, plain system type, and a wall of vintage cut-out collages doing all the talking.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the external `styles index.css` and the inline `<style>` block in `index.html`, read directly. The inline block loads after the external sheet and overrides several rules (`.pic` width, the title weight), so values below are those probed on the rendered elements. Column widths are set in `ch`, which resolves against each element's own font size: the 16px text column renders 776px wide while the 20px section-title rules render 999px wide.

## Overview

A compact, monochrome page (about 3,900px tall) on off-white rgb(252,252,252). There is no color in the chrome at all: black #040404 text and links, 1px black rules, and a gray footer strip. The header centres a two-line 32px semibold title, an 18px author line (first author bold, superscript affiliation numbers) and a 16px affiliation line. Directly under it a full-width nav strip, ruled above and below with 1px black lines, spreads three icon links (arxiv, Results, Video) across the page with `justify-content: space-between`. Content follows in a narrow 776px column: the teaser figure, a justified intro paragraph, then sections introduced by 20px medium-weight titles sitting under a full-width 1px black rule that extends past the text column on both sides, like a newspaper section head. The visual highlight is a 3×2 gallery of 360px animated collage videos (vintage photos, butterflies, moons) that lift on hover. A fixed round "home" button floats at the top left. The page ends with a full-width YouTube embed and a thin gray footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): off-white #fcfcfc 62.5%, #ffffff 12.5%, and near-whites #fdfdf9 3.1%, #fdfcfc 1.1%, #fcfcfd 0.5%, #fafdfd 0.5% (page and the teaser's white ground); parchment #ebe9e2 10.0% and taupe #a29b90 9.8% from the vintage collage material in the teaser. Black text and rules are too thin to form a cluster.

Anatomy in DOM order (desktop 1440px; `header` padding 2vh = 18px top and bottom, centred):

1. **Home button** (`a.home-corner`, fixed at 12px, 12px; 42px with border): 40px circle, rgba(252,252,252,0.92) fill, 1px rgba(4,4,4,0.25) border, shadow 0 6px 18px rgba(0,0,0,0.10), backdrop-filter blur(6px), Font Awesome solid house icon in #040404.
2. **Title** (`.title`, y=18, 94px tall incl. 20px bottom padding): two lines, 32px / 600, line-height 1.15, black, max-width 980px with 20px side padding.
3. **Authors** (`.subtitle`, y=112, 28px tall): 18px / 400, line-height 1.35, #040404 links; first author bold 700; superscript affiliation digits; comma separated. Margin-bottom 4px.
4. **Affiliations** (`.subtitle.affiliation`, y=144): 16px, "¹HKUST   ²Stanford University". Header ends at y=187 (169 + 18px padding).
5. **Nav strip** (`nav`, y=187 to 221, full width): flex, space-between, padding 4px 12% (172.8px at 1440), 1px #040404 rules top and bottom; links 16px #040404 with a leading Font Awesome icon (regular file, solid chart-bar, solid video). Not sticky; it scrolls with the page.
6. **Teaser** (`img.pic`, y=269, 776×362): margin-top 48px (after the 12px section margin), margin-bottom 24px, no border or shadow.
7. **Intro paragraph** (`.paragraph`, y=655, 776px wide): 16px / 1.65, justified, black.

The first section ends with 48px padding; the "Abstract" section title rule sits at y=821.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Off-white | #fcfcfc | (literal, rgb(252,252,252)) | page background, home button fill at 92% |
| Ink Black | #040404 | (literal) | links (authors, nav, notes), nav rules, section-title rules, home icon |
| Text Black | #000000 | (inherited default) | title, body paragraphs, section titles |
| Hover Blue | #126dc9 | (literal, rgb(18,109,201)) | link hover, home-button hover icon and border, focus outline |
| Footer Gray | #ececec | (literal, rgb(236,236,236)) | footer strip background |
| Footer Text | #646464 | (literal) | footer text |
| Gray Link | #686868 | (literal, `.gray-link`) | declared for a disabled Demo link that is commented out; not visible |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | "SF Pro Text", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif | no web font loaded; SF Pro on macOS, Segoe UI on Windows | Inter |
| Unused | Rubik 300–700 (Google Fonts link) | requested but never applied; not in fonts_loaded | — |
| Icons | Font Awesome 6.4.0 | FA 6 Free 400 and 900 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title` | 32px / 600 / 1.15 | #000000 |
| Authors | `.subtitle` | 18px / 400 / 1.35; first author 700 | #040404 |
| Affiliations | `.subtitle.affiliation` | 16px / 400 / 1.35 | #000000 |
| Nav link | `nav a` | 16px / 400 / 1.5 | #040404 |
| Section title | `.section-title` | 20px / 500 / 1.5 | #000000 |
| Note | `.note` | 16px / 400 / 1.65; key word underlined | #040404 |
| Body | `.paragraph` | 16px / 400 / 1.65, justified | #000000 |
| Footer | `footer` | 12px / 1.5 | #646464 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Home button | 999px (40px circle) | 1px rgba(4,4,4,0.25); hover 1px #126dc9 | 0 6px 18px rgba(0,0,0,0.10); backdrop-filter blur(6px) |
| Nav strip | 0 | 1px #040404 top and bottom | none |
| Section title | 0 | 1px #040404 top | none |
| Teaser and figures | 0 | none | none |
| Collage videos | 0 | none | 0 2px 4px rgba(0,0,0,0.1); hover 0 4px 8px rgba(0,0,0,0.2) with translateY(-5px) over 0.6s |
| YouTube embed | 0 | none | none |

## Layout Metrics

- **Container**: `.container { max-width: 1280px; padding: 0 20px 20px }` (x=80 to 1360 at 1440). Sections are max 1280px, margin-top 12px, padding-bottom 48px.
- **Text column**: `--content-max: 90ch` at ≥1024px (72ch below). Paragraphs and figures resolve it at 16px to 776px (x=332 to 1108); section titles resolve it at 20px to 999px (x=220 to 1219), so the rules overhang the text by about 112px on each side.
- **Header**: padding 2vh (18px at 900px tall) top and bottom; title block max 980px plus 20px side padding.
- **Nav**: padding 4px 12%, links at the two ends and the centre.
- **Figures**: `.pic` width 100%, max 776px, margin 48px auto 24px.
- **Collage gallery**: flex wrap, gap 8px, centred; items 360px wide (videos 360×234), three per row at 1440 (1096px total, x=172 to 1268), 10px bottom margin per item.
- **Video**: `.video-container` full container width (1280px) with padding-top 56.25% (720px tall).
- **Footer**: full width, padding 4px, 50px tall.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 20px container padding | 16px | 32px | text column 90ch (776px), section rules 90ch at 20px (999px) |
| <1024px | 20px | 16px | 32px | text column 72ch; figures and rules narrow with it |
| ≤768px | 20px | 16px | 32px | the "Hover the thumbnail" note is hidden (`.mobile-hide`); gallery wraps to fewer columns |
| touch devices | same | same | same | collage videos ignore pointer events; no hover lift |

## Components

- **Ruled nav strip** (`nav`): full-bleed flex row, space-between, padding 4px 12%, 1px #040404 top and bottom borders, three 16px links with a leading Font Awesome icon and a space; hover #126dc9. No background, not sticky.
- **Section title** (`.section-title`): 20px / 500 black, 1px #040404 top border, padding-top 0, margin 12px auto 4px, width 95% capped at 90ch of its own font size (999px at 1440). Notes can sit inside it as 16px lines with the verb underlined ("* Hover the thumbnail…").
- **Home button** (`.home-corner`): fixed 40px circle at (12px, 12px), rgba(252,252,252,0.92), 1px rgba(4,4,4,0.25) border, shadow 0 6px 18px rgba(0,0,0,0.10), blur(6px) backdrop; FA house icon; hover icon and border #126dc9; focus-visible 3px #126dc9 outline offset 2px.
- **Collage tile** (`.collage-item`): inline-block link wrapping a muted, looping 360px video with a GIF poster, object-fit cover, shadow 0 2px 4px rgba(0,0,0,0.1). On hover (fine pointers): translateY(-5px) over 0.6s ease-in-out and shadow 0 4px 8px rgba(0,0,0,0.2); playback starts on hover; click opens a detail page.
- **Paragraph** (`.paragraph`): 16px / 1.65 justified black text in the 776px column.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Home button | yes | fixed frosted circle with a house icon |
| Title / authors / affiliations | yes | centred, black, system font, superscript numbers |
| Link bar | present but non-standard | a ruled full-width nav strip instead of buttons |
| Teaser + summary | yes | unframed figure and justified paragraph in the 776px column |
| Abstract | yes | ruled section title, justified paragraph |
| Pipeline figure | yes | unframed figure with explanation paragraph |
| Results gallery | yes | 3×2 grid of 360px animated collage videos |
| Evaluation chart | yes | rating chart figure with paragraph |
| Video | yes | full-container YouTube embed, 16:9 |
| BibTeX | absent from the source | none |
| Venue / award badge | absent from the source | CHI 2026 appears only inside the teaser image |
| Footer | yes | thin #ececec strip, 12px #646464 |

## Adapting to Other Content

- **More authors**: keep one centred 18px line with superscript digits and wrap; bold only the first author. Affiliations stay on a single 16px line separated by two non-breaking spaces.
- **A results table**: place it in the 776px column with no fill; use 1px #040404 rules above the header row and below the last row only, 16px body text, header 500 weight. No zebra stripes or colored cells.
- **Long publication or news lists**: a plain list in the 776px column, 16px / 1.65, each item led by a date in 500 weight; separate groups with the ruled section title.
- **More gallery items**: add 360px tiles; at 1440 they wrap three per row with 8px gaps.
- **A BibTeX block**: monospace 14px black on #ececec, no radius, in the 776px column under a ruled "Citation" section title.

## Do's and Don'ts

- Do keep the chrome monochrome: black text, 1px #040404 rules, off-white #fcfcfc ground.
- Do let section rules run wider (999px) than the 776px text column.
- Do use the system font stack; no web font is needed for the look.
- Do let the imagery carry the color.
- Don't add buttons, pills or colored links; links are black and turn #126dc9 only on hover.
- Don't round or frame figures.
- Don't make the nav sticky or give it a background.

## Surfaces

One flat off-white surface (#fcfcfc). The only raised elements are the frosted home button and the softly shadowed collage tiles. The footer is a thin #ececec strip.

## Imagery

Vintage-ephemera collages: sepia botanical plates, butterflies, seals, a moon, old portraits and a seaside photo, cut out and recomposed, animated in looping videos. The teaser and pipeline figures are UI screenshots with tan-bordered panels and small blue step labels; the evaluation figure is a stacked bar chart in red-to-green Likert colors.

## Layout

Centred header, full-bleed ruled nav strip, then a single 776px reading column for text and figures, with section rules overhanging to 999px and the gallery and video breaking out to the 1280px container.

## Agent Prompt Guide

Quick colors: background #fcfcfc, text #000000, links and rules #040404, hover #126dc9, footer #ececec with #646464 text.

1. "Build a centred header on #fcfcfc with 18px top and bottom padding: title 32px / 600, line-height 1.15, max 980px; authors 18px #040404 with the first author bold and superscript affiliation digits; affiliations 16px. Under it, a full-width nav: flex space-between, padding 4px 12%, 1px #040404 top and bottom borders, three 16px #040404 links with leading Font Awesome icons, hover #126dc9."
2. "Make a section: a 20px / 500 title with a 1px #040404 top border, width 95% capped at 90ch (about 1000px), then 16px / 1.65 justified paragraphs and figures capped at 776px, centred; figures unframed with 48px above and 24px below. Sections are separated by 48px bottom padding."
3. "Create a gallery: centred flex wrap with 8px gaps of 360px looping muted videos, object-fit cover, shadow 0 2px 4px rgba(0,0,0,0.1); on hover translateY(-5px) over 0.6s and shadow 0 4px 8px rgba(0,0,0,0.2)."

## Similar Pages

- Minimal HCI project pages built by hand with system fonts and black hairline rules.
- Pages whose results are a grid of hover-to-play video thumbnails.

## Quick Start

```css
:root {
  --bg: #fcfcfc;
  --ink: #040404;
  --text: #000000;
  --hover: #126dc9;
  --footer-bg: #ececec;
  --footer-text: #646464;
  --content-max: 90ch;
  --media-w: 95%;
  --container: 1280px;
  --font: "SF Pro Text", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
}
@media (max-width: 1023px) {
  :root { --content-max: 72ch; }
}
```

## Provenance

- **URL**: https://jiayzhou.github.io/collaposer-website/
- **Paper**: Collaposer: Transforming Photo Collections into Visual Assets for Storytelling with Collages (arXiv 2601.18428), Jiayi Zhou, Liwenhan Xie, Jiaju Ma, Zheng Wei, Huamin Qu, Anyi Rao.
- **Venue**: CHI 2026.
- **Selection reason**: the arXiv comment states acceptance at CHI 2026; the project page is linked in the abstract.
- **Template credit**: none stated; a hand-built page with `styles index.css`, an inline style block and Font Awesome 6.4.0. The page has `noindex` set.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of title, nav, section titles, paragraphs, figures and gallery tiles, the 1440×900 and full-page screenshots, and both stylesheets read directly, on 2026-10-28.
