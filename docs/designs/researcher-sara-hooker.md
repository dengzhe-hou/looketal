# Typewriter Press Kit — Style Reference

> A press kit typed on a typewriter: justified monospace beside a tall portrait, then a wall of headlines.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share and DOM boxes from `tools/computed_style.py`, plus a selector probe of the header, banner, bio columns, gallery and footer), the 1440×900 and full-page screenshots, a screenshot scrolled to y=2450 (collapsed header and press gallery), and the page's Weebly theme stylesheet `/files/main_style.css` and the inline theme-override `<style>` read directly. It is a Weebly site with a stock Weebly theme (fixed header, banner section, 1100px panel); fonts come from Weebly's CDN, and Lato 400/400i, Montserrat 700, Inconsolata 400, Cabin 700, Actor 400 (bold synthesized), Karla 400 and the `wsocial` icon font all load. The page is 4835px tall at 1440 wide.

## Overview

A white 1100px page panel centred on a pale blue-grey ground (#f2f6f7). A fixed white header holds "Sara Hooker" in Actor 31.5px bold black on the left and four tracked uppercase Karla 12.6px menu items on the right (the current one greyed to #a6a6a6). Under it, a flat light-grey (#f8f8f8) banner, 260px tall, centres "Welcome!" in Cabin 42px bold and "I teach machines how to think." in Actor 24px bold, both #2a2a2a. The body is a two-column Weebly table: a tall, unframed portrait photo (447×596px) on the left, and on the right a justified Inconsolata 16px bio with 29px leading in #2a2a2a, some sentences in pure black, links in #24678d with underlines, then a list of essay links and three small grey social icons. A hairline rule introduces a full-width YouTube embed (the "Hardware Lottery" talk), another rule introduces a four-column gallery of press clippings (240×180px crops), and a wide image precedes a "Proudly powered by Weebly" footer. Monospace body text against a bright portrait and a mosaic of headlines is what gives it the editorial feel.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 30.4% (header and body panel), page ground #f2f6f7 23.7% plus #f1f6f7 8.8% and #f6f9fb 0.6%, banner grey #f8f8f8 21.8%, warm photo grey #bab3ac 13.3% (portrait wall, shirt and text anti-aliasing), near-whites #fffefd 1.4% and #fffffd 0.1%. The portrait's red hair and blue shirt and the #24678d links are each under 1%.

Anatomy in DOM order (desktop 1440px; panel x=170, 1100px wide, inner padding 50px):

1. **Fixed header** (`#header-wrap` fixed; `#header.content-wrap`, x=170, y=0, 1100×125px): white, 1px radius; on scroll the body gets `.collapse` and the header shrinks to 60px with shadow 0 2px 3px -1px rgba(30,30,30,0.1).
2. **Site title** (`#wsite-title`, x=220, y=44): Actor 31.5px/700 (synthetic bold), line-height 1.2, letter-spacing 1px, #000000, left aligned.
3. **Menu** (`.wsite-menu-item`, y=46, right-aligned ending at x=1220): Karla 12.6px/400, uppercase, letter-spacing 1px, padding 10px 15px; HOME #a6a6a6 (current), RESEARCH, TALKS, CONTACT #525252. Header ends at y=125.
4. **Banner** (`.wsite-header-section`, y=125, 1100×260px): #f8f8f8, table-cell, vertically centred; `#banner` padding 3.5em.
5. **Banner title** (`#banner h2 font`, y=173): Cabin 42px/700, line-height 1.2, letter-spacing 2px, #2a2a2a, centred, text-shadow 0 0 1px rgba(0,0,0,0.3). Gap 34px.
6. **Banner tagline** (`#banner .paragraph font font`, y=261): Actor 24px/700 (synthetic), line-height 1.5, #2a2a2a, centred. Banner ends at y=385; gap 50px.
7. **Portrait** (`.wsite-image img`, x=220, y=445): 447×596px, no border, no radius, in a 46% table column with 15px padding.
8. **Bio** (`.paragraph`, x=697, y=435, 523px wide): Inconsolata 16px/400, line-height 29px, justified, #2a2a2a with some spans in #000000; links #24678d underlined; paragraphs separated by blank lines (29px).

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ground | #f2f6f7 | theme `body` | page background outside the 1100px panel |
| Panel White | #ffffff | (literal) | header, body panel |
| Banner Grey | #f8f8f8 | (inline section style) | welcome banner |
| Ink | #2a2a2a | theme override (`color: #2a2a2a !important`) | bio paragraphs, banner title and tagline |
| Black | #000000 | (inline spans, theme) | site title, emphasised bio sentences |
| Body Grey | #525252 | theme `body` | menu items |
| Current Grey | #a6a6a6 | theme | active menu item (HOME) |
| Link Teal | #24678d | theme override | inline links and essay list |
| Icon Grey | #a3b3bb | Weebly social | mail, LinkedIn and X icons |
| Rule | rgba(0,0,0,0.13) | Weebly `.styled-hr` | 1px dividers before the video and the gallery |
| Footer Grey | #8e8e8e | theme `#footer-wrap` | "Proudly powered by Weebly" footer |

Declared but not visible: the theme's banner background image (`landing-bg.jpg`, 550px) and white banner text are overridden by the inline #f8f8f8 section colour and `<font color="#2a2a2a">`; button colours (#294252, #d9e6ec) are unused.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Mono (bio) | "Inconsolata" !important (theme override) | Inconsolata 400 | IBM Plex Mono |
| Display (banner title) | "Cabin" !important | Cabin 700 | Cabin (Google Fonts) |
| Site title / tagline | "Actor" !important | Actor 400, bold synthesized | Actor (Google Fonts) |
| Menu | "Karla" !important | Karla 400 | Karla (Google Fonts) |
| UI base | 'Lato', Arial, sans-serif (theme body) | Lato 400, 400i | Lato |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site title | `#wsite-title` | 31.5px / 700 / 1.2, letter-spacing 1px | #000000 |
| Menu item | `.wsite-menu-item` | 12.6px / 400 / 1, uppercase, letter-spacing 1px | #525252; current #a6a6a6 |
| Banner title | `#banner h2` | 42px / 700 / 1.2, letter-spacing 2px, centred | #2a2a2a |
| Banner tagline | `#banner .paragraph font[size=5]` | 24px / 700 / 1.5, centred | #2a2a2a |
| Bio | `#wsite-content .paragraph` (text in `font`/`span`) | 16px / 400 / 29px, justified | #2a2a2a; emphasised spans #000000 |
| Link | `.paragraph a` | 16px, underline | #24678d |
| Footer | `.wsite-footer` | 14px / 400 | #8e8e8e |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Header panel | 1px | none | none; collapsed 0 2px 3px -1px rgba(30,30,30,0.1) |
| Portrait / gallery images | 0 | none | none |
| Divider | 0 | 1px rgba(0,0,0,0.13) fill | none |
| Footer | 0 | 4px #f2f6f7 top | none |

## Layout Metrics

- **Panel**: `.container`, `.wsite-footer` and the header max-width 1100px, centred (x=170 at 1440); inner padding 0 50px, so content is 1000px wide at x=220.
- **Header**: fixed, 125px tall (60px after scrolling); `#main-content` padding-top 125px.
- **Banner**: 260px tall at 1440, `#banner` padding 3.5em (49px), h2 margin-bottom 0.8em, tagline margin-bottom 2.5em.
- **Bio row**: Weebly multicol table, margin 0 -15px, columns 46.1% and 53.9% with 15px padding; portrait 447px, text column 523px; row starts 50px below the banner.
- **Rules and embeds**: hr 1000px; YouTube iframe 1000×593px; gallery 1000px, four 240px columns with 10px gaps and 4:3 (180px) crops; wide image 1000×458px.
- **Footer**: padding 3.5em 50px, 4px top border in the ground colour.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≤767px | 0 (panel full width), footer 25px | theme base 12px; bio stays 16px | banner h2 2em | header becomes a hamburger with a slide-in `#navmobile` menu; main padding-top 40px; banner padding 50px 25px; Weebly multicol stacks |
| 768–992px | 25px footer padding | base 13px | banner h2 3.5em rule (overridden by the 42px inline size) | header 120px; banner padding 100px 25px |
| 993–1180px | panel 96% wide | 14px | 42px | — |
| >1180px | panel 1100px centred | 14px | 42px | — |

## Components

- **Fixed panel header**: 1100px white bar, 125px tall, title left in Actor 31.5px bold black with 1px tracking, menu right in Karla 12.6px uppercase with 1px tracking and 10px 15px padding; current item #a6a6a6; collapses to 60px with a soft shadow on scroll.
- **Flat welcome banner**: #f8f8f8 block spanning the panel, 260px tall, centred two-line greeting (Cabin 42px bold, then Actor 24px bold) in #2a2a2a with a 1px soft text shadow.
- **Typewriter bio**: Inconsolata 16px with 29px leading, justified, #2a2a2a, key sentences in #000000; #24678d underlined links; blank-line paragraph breaks.
- **Essay link list**: one #24678d underlined link per paragraph line, 29px apart, under an "Other writings:" lead-in.
- **Social row**: three 21px `wsocial` glyphs (mail, LinkedIn, X) in #a3b3bb, 5px side margins.
- **Press gallery**: Weebly image gallery, four columns of 240×180px cover-cropped clippings with 10px gaps, no captions, no borders.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Site title / navigation | yes | fixed panel header with uppercase menu |
| Welcome banner | yes | flat grey block with a two-line greeting |
| Portrait | yes | tall unframed photo, left column |
| Bio | yes | justified monospace, right column |
| Essay links | yes | underlined teal links, one per line |
| Social icons | yes | three grey glyphs |
| Talk video | yes | full-width YouTube embed between rules |
| Press / media coverage | yes | four-column gallery of article screenshots |
| Publication list | absent from the source | on the separate Research page |
| News | present but non-standard | press clippings stand in for a news list |
| Footer | yes | Weebly credit in #8e8e8e |

## Adapting to Other Content

- **A publication list**: keep Inconsolata 16px/29px, one paper per paragraph: title as a #24678d underlined link, authors and venue in #2a2a2a on the next line; no thumbnails, since the gallery already carries imagery.
- **News**: short dated paragraphs in the same monospace starting "Oct 2026:", separated by blank lines, or reuse the clipping gallery for coverage.
- **A results table**: Inconsolata 14px, 1px rgba(0,0,0,0.13) row rules, no fills, full 1000px width.
- **More media**: add more 240×180 gallery tiles; keep four per row and no captions.
- **More authors on a paper**: inline, comma-separated, own name in #000000 to match the emphasised spans.

## Do's and Don'ts

- Do keep the bio in justified Inconsolata 16px with 29px leading; it is the voice of the page.
- Do keep the 1100px white panel on the #f2f6f7 ground with 50px inner padding.
- Do use #24678d underlined links only; no buttons.
- Don't frame or round the portrait or the gallery tiles.
- Don't put an image in the banner; it is a flat #f8f8f8 block.
- Don't mix in a second monospace or a serif for body text.

## Surfaces

Pale blue-grey ground (#f2f6f7), a white 1100px panel, a flat #f8f8f8 banner inside it, and a fixed white header that gains a soft shadow on scroll.

## Imagery

A tall, bright, natural-light portrait in front of a whiteboard; a YouTube talk thumbnail; a mosaic of news-article screenshots and magazine illustrations (Fortune, VentureBeat, CACM, Time) cropped to 4:3; one wide promotional image near the end.

## Layout

Single 1100px panel: fixed header, banner, a 46/54 photo-and-bio row, a rule, a full-width video, a rule, a four-column press gallery, a wide image, footer. About 4835px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: ground #f2f6f7, panel #ffffff, banner #f8f8f8, text #2a2a2a, emphasis #000000, menu #525252 (current #a6a6a6), link #24678d, icons #a3b3bb, rule rgba(0,0,0,0.13), footer #8e8e8e.

1. "Make a fixed panel header: 1100px white bar centred on a #f2f6f7 page, 125px tall, padding 0 50px; left the name in Actor 31.5px bold #000000 with 1px letter-spacing; right four uppercase Karla 12.6px menu links with 1px letter-spacing and 10px 15px padding in #525252, the current one #a6a6a6; on scroll shrink to 60px with box-shadow 0 2px 3px -1px rgba(30,30,30,0.1)."
2. "Build the bio row: a two-column table (46% / 54%, 15px cell padding) with an unframed 447px-wide portrait on the left and on the right justified Inconsolata 16px text with 29px line-height in #2a2a2a, key sentences #000000, links #24678d underlined, blank lines between paragraphs."
3. "Add a press gallery under a 1px rgba(0,0,0,0.13) rule: 1000px wide, four columns of 240×180px cover-cropped article screenshots with 10px gaps, no borders, no captions."

## Similar Pages

- Personal sites built on stock Weebly themes with a fixed panel header.
- Researcher pages that double as a press kit, with a media-coverage mosaic.

## Quick Start

```css
:root {
  --ground: #f2f6f7;
  --panel: #ffffff;
  --banner: #f8f8f8;
  --ink: #2a2a2a;
  --menu: #525252;
  --menu-current: #a6a6a6;
  --link: #24678d;
  --rule: rgba(0, 0, 0, 0.13);
  --font-mono: "Inconsolata", monospace;
  --font-title: "Actor", sans-serif;
  --font-display: "Cabin", sans-serif;
  --font-menu: "Karla", sans-serif;
}
body { background: var(--ground); margin: 0; }
.panel { max-width: 1100px; margin: 0 auto; padding: 0 50px; background: var(--panel); box-sizing: border-box; }
.banner { background: var(--banner); text-align: center; padding: 49px; }
.banner h2 { font: 700 42px/1.2 var(--font-display); letter-spacing: 2px; color: var(--ink); }
.bio p { font: 400 16px/29px var(--font-mono); text-align: justify; color: var(--ink); }
.bio a { color: var(--link); text-decoration: underline; }
.menu a { font: 400 12.6px var(--font-menu); text-transform: uppercase; letter-spacing: 1px; color: var(--menu); padding: 10px 15px; }
```

## Provenance

- **URL**: https://www.sarahooker.me/
- **Person**: Sara Hooker (efficient and multilingual AI).
- **Venue / award**: ACL 2024 Best Paper, "Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model" (last author). https://2024.aclweb.org/program/best_papers/
- **Selection reason**: award rule (first/last author); chosen for the monospace body beside a large portrait, the talk video and the image strip.
- **Template credit**: footer reads "Proudly powered by Weebly"; a stock Weebly theme with site-level font overrides.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, DOM boxes), a selector probe of header, banner, bio, gallery and footer, the 1440×900, full-page and scrolled screenshots, and `main_style.css` plus the inline override styles read directly, on 2026-10-28.
