# Gallery Lab Notebook — Style Reference

> A studio portfolio for research: a framed portrait in a slate sidebar, a strip of painted news tiles, and projects that open with big shadowed thumbnails.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), a DOM probe of the sidebar, news tiles and project rows, the 1440×900 and full-page screenshots, and the Gatsby page's emotion `<style>` blocks, Tailwind utility classes and Ant Design stylesheet read directly. Lato 700 and Montserrat 400–700 load as web fonts. The layout wrapper is a fixed `w-[1280px]` grid, so the page does not reflow at narrower widths.

## Overview

A pale #fafafa page with slate-grey #47515c text. A fixed 280px left column holds a 280px square portrait with 5px corners and a wide soft 0 0 38px rgba(0,0,0,0.2) glow, the name in 24px Montserrat 500, "AI Researcher at Meta", four grey social icons, a 2px #e8ecf2 rule, and three icon lines (email, location, CV). The right column (872px) opens with a 40px Lato bold name and a 16px Montserrat bio, then "News": a horizontally scrolling strip of white tiles (168px wide, 1px #e5e7eb border, 6px radius) each topped by a square painterly illustration, a 14px caption with medium-weight #265ed4 links and a #9ca3af date pinned to the bottom, with a round arrow at the right edge. "Projects" lists papers as rows: a 305px thumbnail at left (35%), then a 24px Lato title, 13.5px author and venue lines with #265ed4 author links, an amber #874d00 award in bold after a 🎉 emoji, a white "TLDR" chip, and a row of tiny pill links (orange PDF, Semantic Scholar, Website, GitHub, arXiv) separated by grey dots. A Software section closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): page grey #fafafa 53.8% plus #fafaf9 5.4%, #fbfafa 2.2%; mid taupe #6f6960 13.7% (portrait and news illustrations); cool light grey #e4e6e8 12.5% (tile borders, portrait glow, image skies); white #fefefe 11.0% (news tiles).

Anatomy in DOM order (desktop 1440px; wrapper 1280px at x=80, padding 0 32px, grid `280px 1fr` with a 64px column gap; sidebar at x=112, main at x=456):

1. **Portrait** (sidebar, y=64, 280×280): radius 5px, shadow 0 0 38px rgba(0,0,0,0.2). Gap 15px.
2. **Sidebar name** (y=359): Montserrat 24px / 500 / 32px, #47515c. Gap 0.
3. **Role** ("AI Researcher at Meta", y=391): 15px / 400, #47515c. Gap 12px.
4. **Social icons** (y=424): GitHub, Google Scholar, LinkedIn, Twitter as 19–22px white SVGs under `filter: invert(0.6)` (rendered mid grey), 16px apart; hover opacity 0.85. Gap 24px.
5. **Rule** (`hr`, y=469): 2px #e8ecf2, 280px. Gap 24px.
6. **Contact lines** (y=497–556): 18px outline icons left, 15px #47515c text; "CV" in #265ed4.
7. **Main name** (`h1`, x=456, y=68): Lato 40px / 700 / 55px, #47515c. Gap 13px.
8. **Bio** (y=136): Montserrat 16px / 400 / 22px, #47515c, four lines across 872px. Gap 48px.
9. **News heading** (`h3`, y=272): Lato 30px / 700 / 41px, #47515c. Gap 17px.
10. **News strip** (y=330, tiles 168×376, 7px apart): five visible tiles, a 20px #6b7280 chevron in a white circle at the right edge. Gap 50px.
11. **Projects heading** (`h3`, y=756) and the first project row (y=827): blue-grey gradient "Introducing Muse Spark" card on the left, 24px title on the right; the fold cuts the TLDR.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Page Grey | #fafafa | `body` background | page background |
| Slate Text | #47515c | `body` color | names, headings, bio, captions, sidebar text |
| Link Blue | #265ed4 | `a` color | author links, news links, CV, venue sub-links, pill link text |
| Secondary Text | #434343 | `.css-wej1q` | author / affiliation lines in project rows |
| Award Amber | #874d00 | `.css-m5plhe` | bold award text ("Best Paper Honorable Mention") |
| PDF Orange | #d46b08 | `.css-nu42f8` | PDF pill label |
| Pill Border | #bfbfbf | `.css-nu42f8` | PDF pill border, separator dots between links |
| Pill Hover Border | #8c8c8c | `.css-nu42f8:hover` | PDF pill border on hover, dot before the award |
| Icon Blue | #0050b3 | `.css-3jgaw0` and link labels | Blog / Semantic Scholar link icons and labels |
| Chip Ink | #1f1f1f | `.css-2xzwto` | "TLDR" chip text |
| Chip Glow | #d9d9d9 | `.css-2xzwto` | TLDR chip shadow |
| Tile White | #ffffff | `bg-white` | news tiles, TLDR chip, PDF pill |
| Tile Border | #e5e7eb | Tailwind `border` | news tile border |
| Date Grey | #9ca3af | `text-gray-400` | news tile dates |
| Arrow Grey | #6b7280 | `text-gray-500` | news strip chevrons |
| Sidebar Rule | #e8ecf2 | `hr` | 2px rule in the sidebar |
| Gradient Card | #edf6ff → #dbe8f6 → #c8d7e8 | `.css-1isi7bd` | text-only project thumbnail (Muse Spark), text #9aa8b7 |
| Gradient Card Text | #9aa8b7 | `.css-17ygd7s` | "Introducing / Muse Spark" text inside the gradient card |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | Lato, "Helvetica Neue", Helvetica, -apple-system, … | Lato 700 | Source Sans 3 Bold |
| Text | Montserrat, sans-serif | Montserrat 400, 500, 600, 700 | Raleway |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Main name | `h1` | Lato 40px / 700 / 55px | #47515c |
| Section heading | `h3` (News, Projects, Software) | Lato 30px / 700 / 41.25px | #47515c |
| Project title | `h4` | Lato 24px / 700 / 33px | #47515c |
| Sidebar name | `.font-medium.text-2xl` | Montserrat 24px / 500 / 32px | #47515c |
| Sidebar text | `.css-1ol9r24` | Montserrat 15px / 400 / 20.6px | #47515c |
| Bio | `h1 + p` | Montserrat 16px / 400 / 22px | #47515c |
| News caption | `.mt-2.px-2.text-sm` | Montserrat 14px / 400 / 20px; links 500 | #47515c, links #265ed4 |
| News date | `.text-gray-400.text-sm` | Montserrat 14px / 400 | #9ca3af |
| Authors / affiliation | `p.css-wej1q` | Montserrat 13.5px / 400 / 18.6px | #434343, links #265ed4 |
| Venue line | `.css-1tgjqot` | Montserrat 13.5px / 500 | #47515c; award bold #874d00 |
| TLDR text | `.css-1fw7xto` | Montserrat 13.5px / 400 | #47515c |
| TLDR chip | `.css-2xzwto` | Montserrat 13.5px / 600 | #1f1f1f |
| Link pills | `.css-zg88vb` | Montserrat 12.5px / 500; labels 12px | #265ed4 / #0050b3; PDF #d46b08 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 5px | none | 0 0 38px rgba(0,0,0,0.2) |
| News tile | 6px | 1px solid #e5e7eb | none |
| Project thumbnail | 8px | none | `drop-shadow(0 1px 1px rgba(0,0,0,0.05))` on images; gradient card 0 6px 22px rgba(77,101,130,0.16) |
| TLDR chip | 5px | none | 0 0 3px #d9d9d9 |
| PDF pill | 25px | 1px solid #bfbfbf (hover #8c8c8c) | none |
| Other link pills | 25px | none | none |
| Sidebar rule | 0 | 2px solid #e8ecf2 | none |
| News arrow | 50% | thin light-grey ring (seen in the screenshot) | none |

## Layout Metrics

- **Wrapper**: `mx-auto mt-12 grid grid-cols-[280px_1fr] w-[1280px] px-8 gap-x-16` = fixed 1280px, 48px top margin, 32px side padding, 64px column gap; main column 872px.
- **Sidebar**: portrait 280px; text block margin-top 15px; icons row margin 12px 0 0 -5px; `hr` margin 24px 0.
- **Sections**: `.css-15u9bv0` margin-bottom 50px; `h3` margin-bottom 17px; bio margin-bottom 24px plus a 48px spacer.
- **News strip**: `grid grid-cols-8 gap-x-[7px]` running wider than the column (tiles 168px, 7px gaps, about five visible), tiles padded 0 0 40px with the date absolutely positioned 12px from the bottom; images square 166px.
- **Project rows**: `.css-emt8cc` margin-bottom 80px; thumbnail `width: 35%` (305px), text `width: 65%; padding-left: 30px`; title margin-bottom 15px; author line margin -10px 0 18px; TLDR margin 8px 0 15px; link row margin-top 5px.
- **Page height**: 5,388px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1280px | (100% − 1280px)/2 + 32px | 16px | 40px | sidebar 280px + main 872px |
| <1280px | 32px; page scrolls horizontally | 16px | 40px | none: the wrapper stays 1280px (renders at 1024, 768 and 390 were identical) |

## Components

- **Profile sidebar card**: portrait with 5px radius and a 38px soft glow; 24px Montserrat 500 name; 15px role; grey social glyphs (white SVGs inverted 60%); 2px #e8ecf2 rule; three 18px outline-icon rows (envelope, pin, document) with 15px text.
- **News tile**: white, 1px #e5e7eb border, 6px radius, 168px wide, fixed 376px tall; square painted illustration flush at the top; 14px caption with 8px side padding, links in #265ed4 weight 500; date 14px #9ca3af pinned 12px from the bottom. Navigation by circular chevron buttons overlapping the strip edges.
- **Project row**: 35/65 split; thumbnail 8px radius (photo, figure collage, or a gradient card from #edf6ff to #c8d7e8 with centred #9aa8b7 text); 24px Lato title; 13.5px author list with each name linked #265ed4 and the site owner listed first; venue line "CVPR 2025 · 🎉 Best Paper Honorable Mention" with a 2.5px #8c8c8c dot and the award in bold #874d00.
- **TLDR chip**: inline-block white chip, 13.5px weight 600 #1f1f1f, padding 0 6px, 5px radius, shadow 0 0 3px #d9d9d9; the summary follows on the same line.
- **Link pill row**: 12.5px weight 500 flex row; first a PDF pill (white, 1px #bfbfbf border, 25px radius, 18px tall, label #d46b08, hover border #8c8c8c), then text links with small brand icons (Semantic Scholar logo, globe, GitHub mark, arXiv) separated by 2.5px #bfbfbf dots.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sidebar profile | yes | portrait, name, role, icons, rule, contact lines |
| Bio | yes | 16px paragraph under the 40px name |
| News | yes | horizontally scrolling illustrated tiles |
| Publications | yes | project rows with thumbnails, authors, venue, TLDR, link pills |
| Awards | present but non-standard | amber bold text in venue lines and news captions |
| Software | yes | further rows in the same pattern |
| Navigation bar | absent from the source | none |
| Footer | absent from the source | page ends after Software |
| Responsive layout | absent from the source | fixed 1280px wrapper |

## Adapting to Other Content

- **Long publication lists**: keep the 35/65 rows for featured work; for older papers drop the thumbnail and keep title (Lato 24px is large; use 18px Lato 700 for a compact list), 13.5px authors and the pill row.
- **Papers without images**: use the gradient card (#edf6ff → #dbe8f6 → #c8d7e8, 8px radius, 0 6px 22px rgba(77,101,130,0.16)) with the title in #9aa8b7.
- **More news**: the strip already scrolls; keep tiles 168px with square art and dates at the bottom. Without illustrations, use a #fafafa square with an emoji or logo.
- **Talks or teaching**: rows with a video still and pills for Slides / Video.
- **Phones**: the source does not adapt; if you need it, stack the sidebar above the main column and let tiles scroll.

## Do's and Don'ts

- Do pair Lato bold headings with Montserrat body text, both in slate #47515c.
- Do use square, colourful illustrations for news so the strip reads as a gallery.
- Do show the TLDR chip and the pill row under every project.
- Don't colour headings; only links (#265ed4), awards (#874d00) and the PDF pill (#d46b08) carry colour.
- Don't box project rows; they sit directly on #fafafa with 80px between them.
- Don't use hard shadows; the portrait glow and thumbnail shadows are diffuse.

## Surfaces

#fafafa page; white news tiles with #e5e7eb borders; white TLDR chips and PDF pills; a pale blue gradient card for imageless projects.

## Imagery

A studio-lit headshot; AI-generated painterly illustrations for news (a futuristic green city, a Van Gogh-style photographer, confetti robots, a teddy-bear explorer with gadgets, a forest path); project thumbnails mixing photos, 3D object collages, rendered house interiors and a phone-scan pipeline diagram.

## Layout

Fixed two-column grid: sidebar (portrait, name, icons, contact) and main (name, bio, News strip, Projects, Software). About 5,388px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: background #fafafa, text #47515c, links #265ed4, secondary #434343, award #874d00, PDF #d46b08, pill border #bfbfbf, tile border #e5e7eb, dates #9ca3af, rule #e8ecf2.

1. "Build a fixed two-column layout: 1280px wrapper, 32px padding, grid 280px + 1fr with 64px gap on #fafafa. Sidebar: 280px square portrait, radius 5px, box-shadow 0 0 38px rgba(0,0,0,0.2); 24px Montserrat 500 name and 15px role in #47515c; a row of grey social icons; a 2px #e8ecf2 rule with 24px margins; contact lines with 18px icons."
2. "Make a news strip: white tiles 168px wide and 376px tall, 7px apart, 1px #e5e7eb border, 6px radius, a square illustration on top, a 14px Montserrat caption with 8px side padding and #265ed4 weight-500 links, and a 14px #9ca3af date 12px from the bottom; round white chevron buttons in #6b7280 at the edges."
3. "Make a project row: thumbnail 35% wide with 8px radius, text 65% with 30px left padding; Lato 24px bold title in #47515c; 13.5px #434343 author line with #265ed4 names; a 13.5px weight-500 venue line ending in a bold #874d00 award; a white TLDR chip (13.5px 600 #1f1f1f, padding 0 6px, radius 5px, shadow 0 0 3px #d9d9d9) before the summary; then a 12.5px pill row starting with a PDF pill (1px #bfbfbf border, 25px radius, 18px tall, #d46b08 label); 80px between rows."

## Similar Pages

- Gatsby / Ant Design researcher portfolios with a fixed sidebar and TLDR chips.
- Personal pages that use AI-generated illustrations for news items.

## Quick Start

```css
:root {
  --bg: #fafafa;
  --text: #47515c;
  --link: #265ed4;
  --secondary: #434343;
  --award: #874d00;
  --pdf: #d46b08;
  --pill-border: #bfbfbf;
  --tile-border: #e5e7eb;
  --date: #9ca3af;
  --rule: #e8ecf2;
}
body { background: var(--bg); color: var(--text); font-family: Montserrat, sans-serif; font-size: 16px; line-height: 22px; }
h1, h3, h4 { font-family: Lato, "Helvetica Neue", Helvetica, sans-serif; font-weight: 700; }
.layout { width: 1280px; margin: 48px auto 0; padding: 0 32px; display: grid; grid-template-columns: 280px 1fr; column-gap: 64px; }
.portrait { border-radius: 5px; box-shadow: 0 0 38px rgba(0,0,0,.2); }
.news-tile { width: 168px; background: #ffffff; border: 1px solid var(--tile-border); border-radius: 6px; padding-bottom: 40px; position: relative; }
.tldr { background: #ffffff; color: #1f1f1f; font-weight: 600; padding: 0 6px; border-radius: 5px; box-shadow: 0 0 3px #d9d9d9; }
.pill-pdf { border: 1px solid var(--pill-border); border-radius: 25px; padding: 0 8px; height: 18px; color: var(--pdf); background: #ffffff; }
```

## Provenance

- **URL**: https://mattdeitke.com/
- **Person**: Matt Deitke, embodied AI and open vision-language models.
- **Award**: CVPR 2025 Best Paper Honorable Mention, "Molmo and PixMo" (first author). https://tc.computer.org/tcpami/awards/cvpr-paper-awards/
- **Selection reason**: award rule (first or last author); chosen for the image-led news carousel and project rows with large thumbnails and TLDRs.
- **Template credit**: none stated; Gatsby build with emotion CSS-in-JS, Tailwind utilities and Ant Design CSS.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), DOM probes at 1440, 1024, 768 and 390 wide, the 1440×900 and full-page screenshots, and the inline emotion styles and markup read directly, on 2026-10-28.
