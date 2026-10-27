# CubeDiff Panorama Strip — Style Reference

> A row of six windows onto six generated worlds, signed by six cartoon faces.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, the page's own `static/css/style.css` and its inline styles. The page loads no CSS framework, so almost every value is the author's. Color share is measured on the first 1440×900 viewport.

## Overview

A hand-written page on plain Roboto, black text on white, with no accent color at all. The hero is centred: a two-line 48px bold title, a bold "🎉 Accepted to ICLR 2025 🎉" line, six author cards each topped by a 64px illustrated avatar, a one-line affiliation key, and two charcoal #3a3a3a rounded buttons with icons. Directly below runs a full-bleed strip of six square autoplay videos (panorama spins) edge to edge, native controls visible. A large "tl;dr" heading then pairs a 3D cube render with a 19.2px justified paragraph, a short #e9e9e9 rule closes the intro, and everything after sits in a 960px left-aligned wrapper: a wide overview pipeline graphic, Abstract, Method figure, a gallery of equirectangular panoramas clipped to a 15px-rounded block, an interactive Pannellum panorama viewer with charcoal tab buttons, and a grey BibTeX box. Body text is justified with normal line height, which reads tight.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 64.6%, then the video strip: umber #4c433f 9.7%, deep teal-black #132122 8.6%, sage grey #777d75 7.6%, sky #9cb9bf 5.4%, warm grey #e6e5e1 2.8%. The black text and two charcoal buttons are below 1% each.

Anatomy in DOM order (body padding 20px; `header` has 48px top margin and is centred):

1. **Title** — `header h1`, 48px / 700 (faux bold, see Typography) / line-height normal, #000000, centred, wraps to two lines at 1440 (y=68–184). Margin-bottom 32px.
2. **Venue line** — `h4`, "🎉 Accepted to ICLR 2025 🎉", 19.2px / 700, #000000, centred (y=216–242). Margin-bottom 38.4px (inline 2em).
3. **Authors** — `#authors`, flex row, centred, wrapping; each card 200px wide: 64px avatar PNG (cartoon portraits, no radius), `<br>`, name 19.2px / 400 #000000 with superscript affiliation numbers. Avatars at y=280, names at about y=350.
4. **Affiliations** — centred `p`, "¹ ETH Zürich ² Google", 19.2px, followed by two `<br>` (y=377–427). Gap 5px.
5. **Buttons** — two `a.button`, "Arxiv" (Academicons arXiv glyph) and "(unofficial) Code" (Font Awesome GitHub), 15.36px / 400 white on #3a3a3a, padding 12px 28px, radius 8px, 5px margin; y=432–475. Gap 37px (section margin 2rem).
6. **Video strip** — `section#videos`, six `<video autoplay loop muted controls>` each `flex: 0 0 16.66%`, 233×233px, touching, spanning the 1400px body width (x=20 to 1420), y=512–745. Gap 33px.
7. **tl;dr** — `h1` inline 3rem (48px) / 700 centred, y=778. Below the fold: cube image (max-height 200px) beside a 600px-max paragraph at 19.2px justified.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | (browser default) | page background |
| Ink | #000000 | (browser default) | title, headings, venue line, author names, body text |
| Charcoal Button | #3a3a3a | `a.button` | Arxiv / Code buttons, panorama-viewer tab buttons |
| Button Hover | #1a1a1a | `a.button:hover` | button hover |
| Tab Active | #b0bec5 | `#tabContent a.is-active` | selected panorama tab fill (text #000000) |
| Tab Active Border | #90a4ae | `#tabContent a.is-active` | 1px border of the selected tab |
| Divider | #e9e9e9 | `hr color` (inline) | 560px rule after tl;dr |
| Code Grey | #f2f2f2 | `pre` (inline) | BibTeX box |
| Strip Umber | #4c433f | (video frames) | dominant tone of the hero video strip |

## Tokens — Typography

- **Sans:** declared `'Roboto', sans-serif`; Google Fonts request asks only for `Roboto:wght@400` (and Roboto Mono 200, unused). Rendered: Roboto 400 only, so every bold heading is browser-synthesized bold. Substitute: Roboto with real 700, or Inter.
- **Mono:** `pre` falls back to the browser `monospace` (rendered 13px). Substitute: Roboto Mono.
- **Icons:** Academicons 1.9.4 and Font Awesome 6 Brands (kit).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `header h1` (2.5em of header's 1.2em, `!important`) | 48px / 700 / normal |
| Venue line | `header h4` | 19.2px / 700 |
| Author names, affiliations | `header` (1.2em) | 19.2px / 400 |
| tl;dr heading | inline `font-size: 3rem` | 48px / 700 |
| tl;dr paragraph | `section#intro div` (1.2em) | 19.2px / 400, justified, last line left |
| Section titles | `h1` | 32px (2rem) / 700 |
| Sub-sections | `h2` | 24px / 700 |
| Body | `p` in `.wrapper` | 16px / 400 / normal, justified, `text-align-last: left` |
| Buttons | `a.button` | 15.36px (0.8em of 19.2px) / 400 |
| Tab buttons | `#tabContent a.button` | 12.8px / 400 |
| BibTeX | `pre` | 13px monospace |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | radius 8px, no border, no shadow, padding 12px 28px, margin 5px |
| Tab buttons | radius 8px, padding 10px 16px, margin 3px |
| Results gallery | outer `border-radius: 15px; overflow: hidden`, 5px row gap, three 33% tiles per row |
| Conditioning image | 256×256, radius 15px |
| Avatars, videos, figures | square corners |
| Divider | `hr` max-width 560px, margins 2rem top / 3rem bottom |
| Shadows | none (the cube render's shadow is in the image) |
| Reset | `* { margin: 0; padding: 0 }`, so all spacing is explicit |

## Layout Metrics

- **Page frame:** body padding 20px on all sides; no max-width on hero or video strip (1400px at 1440).
- **Reading wrapper:** `section.wrapper` max-width 960px, `margin: auto`, left aligned (x=240–1200 at 1440).
- **Hero:** header margin-top 48px (3rem); title→venue 32px; venue→authors 38.4px; authors are 200px-wide flex items.
- **Video strip:** six × 16.66% (233px squares at 1440), margin-top 32px, no gaps.
- **tl;dr row:** flex, centred, two blocks each max 600px with 20px padding.
- **Sections:** each `section.wrapper` margin-top 32px (2rem); headings followed by 16px (1rem) before figures.
- **Figures:** overview and method images 100% of 960px.
- **Panorama viewer:** 384×384 Pannellum canvas beside a 256px conditioning image, `space-evenly`.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >1240px | 20px | 16px | 48px | 6 videos per row |
| 769–1240px | 20px | 16px | 48px | 3 videos per row (two rows) |
| ≤768px | 20px | 16px | 48px | 2 videos per row; tl;dr blocks stack; author cards wrap two or three per row |
| ≤400px | 20px | 16px | 48px | panorama canvas shrinks to 256×256 |

## Components

- **Charcoal button:** `a.button`, inline-block, background #3a3a3a, text #ffffff 0.8em Roboto 400, padding 12px 28px, radius 8px, margin 5px, icon left followed by `&nbsp;`; hover background #1a1a1a and the icon plays Font Awesome `fa-bounce` once (0.7s). Disabled state at 50% opacity.
- **Avatar author card:** 200px block, 64px square illustrated portrait, line break, name with superscript numbers; cards centred in a wrapping flex row.
- **Video strip:** six square looping videos flush against each other with browser controls shown, full body width.
- **tl;dr pair:** 3D object render (max-height 200px) left, 19.2px justified paragraph right, vertically centred, under a 48px "tl;dr" heading.
- **Rounded gallery:** flex-wrap block of 2:1 panorama thumbnails (33% width each), 5px row gap, the whole group clipped to 15px corners; click opens PhotoSwipe at 2048×1024.
- **Tab selector:** JS-generated `a.button` chips (12.8px, padding 10px 16px) for prompts like "Munch", "Starry Night", "Industrial", "Space"; active tab #b0bec5 with 1px #90a4ae border and black text.
- **Code box:** `pre` on #f2f2f2, padding 16px, no radius, 13px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue | Yes | centred 48px bold title, emoji-framed bold venue h4 |
| Authors with avatars | Yes | 64px cartoon portraits in 200px cards |
| Affiliations | Yes | one centred line with superscript keys |
| Link buttons | Yes | two charcoal rounded buttons with icons |
| Hero video strip | Yes | six full-bleed square loops |
| tl;dr | Yes | image + justified paragraph |
| Overview figure | Yes | full-width pipeline graphic in the 960px wrapper |
| Abstract | Yes | 32px h1, 16px justified text with 20px side padding |
| Method | Yes | full-width figure + paragraph |
| Results gallery | Yes | rounded 3-column panorama gallery with lightbox |
| Interactive viewer | Yes | Pannellum 360° viewer with prompt tabs |
| Results table | No (absent from the source) | |
| BibTeX | Yes | #f2f2f2 pre |
| Footer | Yes | centred copyright line, no template credit |

## Adapting to Other Content

- **More authors:** the 200px avatar cards wrap; beyond about eight, drop avatars and keep names in the same 19.2px flex row, or keep avatars at 64px and let them wrap to two rows.
- **No avatars available:** use initials in 64px circles in #3a3a3a with white text, so the row keeps its rhythm.
- **Results table:** place in the 960px wrapper under a 32px h1; 16px Roboto, header row on #f2f2f2, 1px #e9e9e9 row rules, no radius to match the figures.
- **More links:** add further charcoal buttons in the same row (Paper, Data, Demo); keep icon-left and the 5px margin.
- **News:** a short list under the venue line at 16px, left aligned inside the wrapper; do not add a second accent color.

## Do's and Don'ts

- Do keep the page monochrome; the generated imagery supplies all color.
- Do run the hero media edge to edge with no gaps; the strip is the page's signature.
- Do round grouped result images as one 15px block rather than each tile.
- Don't justify long body text at normal line height in new work; use 1.5 line height and left alignment if you borrow the look.
- Don't rely on faux bold; load Roboto 700 if headings stay bold.
- Don't add borders or shadows to buttons; flat charcoal is the whole recipe.

## Surfaces

White page throughout. Flat #3a3a3a buttons, a #f2f2f2 code box, a single #e9e9e9 divider; no bands or cards.

## Imagery

Square panorama-spin videos, a 3D cube render with a painted texture, a pastel pipeline diagram (pink encoder blocks, peach UNet), wide 2:1 equirectangular panoramas, and illustrated author avatars.

## Layout

Two widths: a full-width hero (title, avatars, video strip, tl;dr) and a 960px left-aligned reading wrapper for everything after. Rendered height about 4,000px.

## Agent Prompt Guide

Quick colors: text #000000 on #ffffff, buttons #3a3a3a (hover #1a1a1a), active tab #b0bec5 / #90a4ae, divider #e9e9e9, code #f2f2f2.

1. "Create a hero: centred 48px bold Roboto title in #000000, a 19.2px bold venue line with an emoji each side, a wrapping row of 200px author cards each with a 64px avatar above the name, then two buttons: #3a3a3a background, white 15.36px Roboto text, padding 12px 28px, 8px radius, icon left, hover #1a1a1a."
2. "Under the hero, place six square autoplay muted looping videos side by side, each 16.66% of the 1400px width with no gaps; three per row below 1240px and two per row below 768px."
3. "Build a results gallery inside a 960px wrapper: flex-wrap of three 33%-wide 2:1 images with a 5px row gap, the whole block clipped to a 15px radius, each opening a lightbox."

## Similar Pages

- Small hand-built Roboto pages with avatar author rows (several Google Zurich project pages).
- Panorama and 360° generation pages that put a strip of spin videos in the hero.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --button: #3a3a3a;
  --button-hover: #1a1a1a;
  --tab-active: #b0bec5;
  --tab-active-border: #90a4ae;
  --divider: #e9e9e9;
  --code-bg: #f2f2f2;
  --font-sans: 'Roboto', sans-serif;
  --title-size: 48px;
  --h1-size: 32px;
  --body-size: 16px;
  --lead-size: 19.2px;
  --radius-button: 8px;
  --radius-gallery: 15px;
  --wrapper: 960px;
}
```

## Provenance

- **URL:** https://cubediff.github.io/
- **Paper:** CubeDiff: Repurposing Diffusion-Based Image Models for Panorama Generation (arXiv 2501.17162), Nikolai Kalischek et al.
- **Venue:** ICLR 2025 (stated on the page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the abstract.
- **Template credit:** none stated; hand-written CSS.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, 1440 screenshots (first viewport and tall), `static/css/style.css`, inline styles in the page HTML; 2026-10-28.
