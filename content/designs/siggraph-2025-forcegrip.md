# ForceGrip — Style Reference

> A tidy lab report on one sheet of paper: conference sticker top left, visitor counter top right, a bold title and one annotated figure that tells the whole story.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the logo, hit badge, video, paragraphs and BibTeX block, the 1440×900 and full-page screenshots, and the page's own `index.html` and `style.css` read directly. The stylesheet declares `font-family: 'Segoe UI', sans-serif` with no web font, so the face depends on the system: Segoe UI renders on Windows (the capture), the default sans elsewhere. `style.css` also contains an unused `.event-announcement` gradient card recipe.

## Overview

A hand-written page with no framework: the `body` is a 900px column (padding 32px, centred) on white, set in Segoe UI with #333333 text. A small colour SIGGRAPH 2025 logo (150px) sits top left and a hits.sh TODAY/TOTAL counter badge (orange #fe7d37 value on #fafafa) sits top right, both absolutely positioned above a left-aligned 32px/700 #111111 title on two lines. The full-width annotated teaser (900×505) follows: a VR hand dropping a can into a bin, white rounded callout boxes, a red-to-cream force bar and three controller-trigger sketches with red circles. Under it, centred, come bold underlined author names, italic affiliations with underlined lab links, and three blue (#0066cc) underlined icon links (Paper, Supp., Code). Then "Video" (a full-width YouTube embed), "Abstract" (three 16px paragraphs) and "BibTeX" in an italic gray block on #f7f7f7 with a 4px #cccccc left bar, and a small gray footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 69.5% (plus #faf8f6 4.2%, #fcffff and #fffff6 1.3%); plum-gray #4a4249 8.1% (title text and the dark floor in the teaser); slate #6a6e77 7.5% (the teaser's gray backdrop); light gray #b8bcbf 5.9% (the hand renders); pale blush #efe1dc 3.4% (the cream end of the force bar and the trigger sketches). The red force arrows and #0066cc links cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, column x=270–1170):

1. **Column** (`body`): max-width 900px, margin auto, padding 32px; content starts at y=32.
2. **Title container** (`.title-container`, y=32, relative, padding-top 12.8px).
3. **SIGGRAPH logo** (`.logo-badge img.siggraph-logo`, x=270, y=32, 150×38): colour conference logo, absolutely positioned top left, linked to s2025.siggraph.org.
4. **Hit counter** (`.hit-badge img`, x=998, y=32, 156×20): hits.sh flat-square badge "TODAY/TOTAL" with a #fafafa label and #fe7d37 value, absolutely positioned top right.
5. **Title** (`h1`, y=66, 102px, two lines): Segoe UI 32px/700, line-height 51.2px, #111111, left-aligned; margin 21.44px 0. The logo sits in the 34px above it. Gap 22px.
6. **Teaser** (`.image img`, y=190, 900×505): annotated figure, no border. Gap 15px.
7. **Authors** (`.authors p`, y=710, 59px, two lines): centred, 16.8px (1.05rem), line-height 1.6; names in `<strong>` 700 #333333; linked names underlined in the same colour; superscripts. Gap 8px.
8. **Affiliations** (`p.affiliations`, y=777, 88px, three lines): centred, 16.8px italic #333333, lab names underlined links in #333333 at weight 400. Gap 20px.
9. **Icon links** (`.icon-links p`, y=885, 31px): centred, 19.2px (1.2rem) #0066cc, underlined, each with a Font Awesome icon (`fa-file-alt`, `fa-file-alt`, `fa-github`) and 8px icon gap; links 16px apart (margin-right 1rem). Hover removes the underline.
10. **Video heading** (`h2`, y=935): 24px/700 #111111, left-aligned; the YouTube iframe follows at y=993, 900×506.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (`body` background) | page background |
| Title Ink | #111111 | (`h1, h2`) | title, section headings |
| Text | #333333 | (`body` color) | body text, author names, affiliations |
| Link Blue | #0066cc | (`a`) | icon links and their icons |
| Footer Gray | #888888 | (footer) | copyright footer text |
| Quote Gray | #808080 | `gray` (`.placeholder`) | BibTeX text |
| Code Paper | #f7f7f7 | (`.placeholder`) | BibTeX block background |
| Quote Bar | #cccccc | (`.placeholder`) | 4px left border of the BibTeX block |
| Counter Orange | #fe7d37 | (hits.sh badge URL `color=fe7d37`) | value half of the visitor badge |
| Counter Label | #fafafa | (hits.sh badge URL `labelColor=fafafa`) | label half of the visitor badge |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | 'Segoe UI', sans-serif | no web font loaded; Segoe UI (system) on Windows, the default sans-serif elsewhere | Selawik |
| Icons | Font Awesome 6.5 | Font Awesome 6 Free 900, Brands 400 | — |

Selawik is Microsoft's open metric-compatible stand-in for Segoe UI.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1` | 32px / 700 / 51.2px, left | #111111 |
| Section heading | `h2` | 24px / 700 / 38.4px, left | #111111 |
| Body | `body`, `p` | 16px / 400 / 25.6px | #333333 |
| Authors | `.authors p`, `.authors a` | 16.8px / 700 names / 26.88px, centred | #333333 |
| Affiliations | `p.affiliations` | 16.8px / 400 italic, centred | #333333 |
| Icon links | `.icon-links` | 19.2px / 400 / 30.72px, underlined | #0066cc |
| BibTeX | `.placeholder` | 16px / 400 italic / 25.6px | #808080 |
| Footer | `footer` | 14.4px / 400 / 23.04px | #888888 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Teaser, video | 0px | none | none |
| BibTeX block (`.placeholder`) | 0px | left 4px solid #cccccc | none |
| Logo and badge | 0px (badge is a flat-square SVG) | none | none |
| Links | — | underline on icon, author and lab links | none |

`.event-announcement` (declared, unused): `background: linear-gradient(135deg, #2c3e50, #4e7cb3)`, white text, padding 2rem, radius 10px, `box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1)`.

## Layout Metrics

- **Column**: `body { max-width: 900px; margin: 0 auto; padding: 2rem }` → content x=270–1170 at 1440.
- **Header**: `.title-container` padding-top 12.8px; logo and badge `position: absolute; top: 0` on the left and right; title margin 21.44px 0 → title at y=66.
- **Teaser and video**: both 900px wide; video iframe `aspect-ratio: 16 / 9` → 506px tall.
- **Author block**: paragraphs margin 8px 0; `.authors` margin-bottom 16px.
- **Icon links**: paragraph margin 19.2px 0.
- **Sections**: `h2` margin 19.92px 0; paragraphs 16px apart.
- **BibTeX**: padding 16px, text lines broken with `<br>` and indented with `&nbsp;`.
- **Footer**: margin-top 48px, 14.4px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| all widths | 32px body padding | 16px | 32px | no media queries; the 900px column shrinks with the viewport and the absolute logo and badge can overlap the title on narrow screens |

## Components

- **Conference sticker**: the official SIGGRAPH 2025 colour logo PNG at 150px wide, absolutely positioned at the top-left of the title block, linked to the conference site.
- **Visitor badge**: a hits.sh flat-square SVG (label "TODAY/TOTAL" on #fafafa, count on #fe7d37) at the top-right.
- **Title**: left-aligned 32px/700 #111111 on two lines under the sticker.
- **Author block**: centred 16.8px; names bold #333333, linked names underlined (hover removes it), superscript affiliation marks; affiliations in italic with underlined lab-name links at weight 400.
- **Icon link row**: centred 19.2px #0066cc text links with a Font Awesome icon 8px before each label, underlined, 16px apart; hover removes the underline.
- **BibTeX quote block** (`.placeholder`): #f7f7f7, 4px solid #cccccc left border, padding 16px, italic #808080 16px text with manual line breaks.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Conference logo | yes | colour SIGGRAPH 2025 logo top left |
| Visitor counter | yes | hits.sh badge top right |
| Title | yes | left-aligned 32px bold |
| Teaser | yes | full-column annotated figure |
| Authors / affiliations | yes | centred, bold names, italic affiliations |
| Link row | yes | three underlined blue icon links, no buttons |
| Video | yes | full-column YouTube embed |
| Abstract | yes | three plain paragraphs |
| Results figures / tables | absent from the source | the teaser and video carry all results |
| BibTeX | present but non-standard | an italic gray quote block, not a `pre` |
| Footer | yes | small gray copyright line |

## Adapting to Other Content

- **More authors**: keep the centred 16.8px block and break lines with `<br>` after about three names, as the source does; bold every name and underline only those with pages.
- **A results table**: place it in the 900px column under a 24px/700 `h2`; 16px #333333 cells, 1px #cccccc rules, header bold #111111, no fills; it spans the full 900px.
- **Long publication or news lists**: a left-aligned list at 16px in the 900px column, dates bold; or reuse the `.placeholder` block (#f7f7f7, 4px #cccccc left bar) for a short news note.
- **More figures**: add full-width 900px images under `h2` headings with a 16px #333333 caption paragraph.
- **A different venue**: swap the logo PNG at 150px wide; keep it top-left above the title.

## Do's and Don'ts

- Do keep everything in one 900px column with the title and section headings left-aligned.
- Do centre only the author, affiliation and link blocks.
- Do use plain underlined #0066cc text links with icons instead of buttons.
- Do let the annotated teaser run the full column width with no frame.
- Don't add background bands, cards or shadows; the page is white throughout.
- Don't load a web font; the system UI face is part of the look.
- Don't use the unused gradient announcement card for the main content.

## Surfaces

White everywhere; #f7f7f7 only for the BibTeX block. The only colour blocks are the conference logo, the orange counter badge and the teaser itself.

## Imagery

One explanatory teaser: rendered pale VR hands grasping red soda cans over a dark gray stage, white rounded callout labels in black sans, red motion arrows, a vertical red-to-cream force scale labelled 10KG and 1KG, and a row of black-outlined cartoon sketches of a VR controller trigger with red circles.

## Layout

A single centred 900px column: logo and counter, title, teaser, centred credits and links, then Video, Abstract and BibTeX sections and a footer. The page is about 2440px tall.

## Agent Prompt Guide

Quick colors: background #ffffff, title #111111, text #333333, links #0066cc, BibTeX #f7f7f7 with #cccccc bar and #808080 text, footer #888888, counter #fe7d37.

1. "Make the body a 900px column: max-width 900px, margin 0 auto, padding 32px, font 'Segoe UI', Selawik, sans-serif, 16px, line-height 1.6, color #333333 on #ffffff. Put a 150px conference logo absolutely at the top-left of a relative title block (padding-top 12.8px) and a small counter badge at the top-right; title h1 32px/700 #111111, left-aligned, two lines."
2. "Under a full-width teaser image, add a centred author block: 16.8px, names bold #333333 with underlines on linked names, superscripts; affiliations italic with underlined lab links; then a centred row of 19.2px #0066cc underlined links, each with a Font Awesome icon 8px before the label, 16px apart, underline removed on hover."
3. "Style the BibTeX as a quote block: background #f7f7f7, border-left 4px solid #cccccc, padding 16px, italic 16px #808080, lines broken manually; section headings h2 24px/700 #111111 left-aligned."

## Similar Pages

- Single-file, framework-free paper pages written by the authors, with a conference logo and a hit counter.
- VR and HCI project pages that rely on one annotated teaser and a video.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #111111;
  --text: #333333;
  --link: #0066cc;
  --quote-bg: #f7f7f7;
  --quote-bar: #cccccc;
  --quote-text: #808080;
  --footer: #888888;
  --counter: #fe7d37;
  --font: "Segoe UI", Selawik, sans-serif;
}
body { font-family: var(--font); max-width: 900px; margin: 0 auto; padding: 2rem; line-height: 1.6; color: var(--text); background: var(--bg); }
```

## Provenance

- **URL**: https://han-dongheun.github.io/ForceGrip/
- **Paper**: ForceGrip: Reference-Free Curriculum Learning for Realistic Grip Force Control in VR Hand Manipulation (arXiv 2503.08061), DongHeun Han, Byungmin Kim, RoUn Lee, KyeongMin Kim, Hyoseok Hwang, HyeongYeop Kang.
- **Venue**: SIGGRAPH 2025 Conference Papers; the arXiv comment states "Accepted to SIGGRAPH Conference Papers '25".
- **Selection reason**: a narrow single column with a conference badge and a strong annotated teaser; a restrained document style that differs from the centred Nerfies pages.
- **Template credit**: none; a hand-written `index.html` and `style.css` with Font Awesome 6.5 and a hits.sh counter; footer "© 2025 DongHeun Han, …".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and the page's `index.html` and `style.css` read directly, on 2026-10-28.
