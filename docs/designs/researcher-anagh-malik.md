# Anagh Malik — Style Reference

> The Barron table, warmed with apricot: Lato at 14px, blue links that flash orange, and the papers that matter sitting in a band of late-afternoon light.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and `stylesheet.css` plus the inline table attributes in the markup, read directly. Lato loads in 400, 400 italic and 700 and renders everywhere; there is no other face. The layout is the Jon Barron template (the footer credits it), with two added modules, a Recent Media card grid and a scrolling News card, both styled in the author's additions to `stylesheet.css`.

## Overview

A 900px table centred on white with the body's default 8px margin. The header row splits 63/40: on the left the name in Lato 32px/400 centred, two 14px bio paragraphs with #1772d0 links, a centred obfuscated email and a centred "Twitter / Resume / Google Scholar / GitHub" line; on the right a portrait at 75% of its cell with 16px rounded corners. "Recent Media" (Lato 22px/400) introduces three white cards with 12px corners in a grid: 16:9 thumbnails, a small dark play disc in the corner, an apricot pill for the source, a bold blue title and a grey one-line description. "News" sits in a #fafafa rounded card that scrolls internally, each row led by an apricot date pill. "Research" then lists papers in the classic two-cell rows: a 160px square thumbnail that swaps to a looping video on hover, and a text cell with a bold blue 14px title, authors (own name bold), italic venue, red bold award notes, slash-separated links and a one-line summary. Key papers get a full-row apricot #fbe5ba background. A small right-aligned credit closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 69.3% (page), #f9f9fa 9.0% (the #fafafa news card), #190f0f 8.7% (dark media thumbnails), #e0e4e7 6.4% (card borders, light thumbnail areas), #87837f 5.0% (portrait). The apricot pills are small but are the only warm color above the fold.

Anatomy in DOM order (desktop 1440px; table 900px at x=270; header cells padded 2.5% = 22.5px):

1. **Name** (`name` inside `p`, x=293–815, y=45): Lato 32px/400, #000000, centred in the 63% cell. Gap 14px.
2. **Bio** (`p`, y=98 and 180, 522px wide): Lato 14px/400, normal line height (17px), #000000, paragraph margins 14px; links #1772d0. Gap 14px.
3. **Email** (`p`, y=245, centred): "Email:" line and the obfuscated address, then two blank lines.
4. **Link line** (y=313, centred): Twitter / Resume / Google Scholar / GitHub, #1772d0 links separated by "&nbsp;/&nbsp;".
5. **Portrait** (right cell, 40%, centred, y≈78): image at 75% of the cell (about 216px), border-radius 16px. Header row ends at y=366.
6. **"Recent Media" heading** (`heading`, y≈386, cell padding 20px): Lato 22px/400 #000000. Gap 10px.
7. **Media cards** (`a.media-card`, y=423, three at x=290, 582, 874, each 276×261): see Components. Gap about 50px.
8. **"News" heading** (y≈735) and the news card (y≈778) with its first three rows cross the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Link Blue | #1772d0 | (literal) | all links, paper titles, media card titles |
| Hover Orange | #f09228 | (literal) | link hover and focus, media card title on card hover |
| Apricot | #fbe5ba | (literal, also `bgcolor`) | highlighted paper rows, news date pills, media source pills |
| Apricot Edge | #f2d59b | (literal) | border of date pills and source pills |
| Ink | #000000 | (default) | name, headings, bio and paper text |
| Pill Ink | #222222 | (literal) | text inside date and source pills |
| Meta Grey | #666666 | (literal) | media card date line |
| Desc Grey | #444444 | (literal) | media card description |
| Award Red | #ff0000 | (`<font color="red">`) | bold award and presentation notes, e.g. "(Oral Presentation)" |
| News Card | #fafafa | (literal) | scrolling news card fill, scrollbar thumb border |
| Card Edge | #e6e6e6 | (literal) | media card and news card borders |
| Row Rule | #ededed | (literal) | separators between news rows |
| Thumb Fill | #eeeeee | (literal) | media thumbnail placeholder; contained thumbnails use #000000 |
| Play Disc | rgba(0,0,0,0.65) | (literal) | round play badge on media thumbnails |
| Scroll Thumb | #d6d6d6 | (literal) | news card scrollbar (hover #bdbdbd) |
| Alt Link | #0066cc | (inline style) | one paper's title and "project page" link (Opportunistic Single-Photon Time of Flight) |
| White | #ffffff | (default) | page, media cards |

Declared but not visible: `span.highlight` (#ffffd0) is not used in the markup.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Lato', Verdana, Helvetica, sans-serif | Lato 400, 400 italic, 700 | Carlito |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `name` | 32px / 400 / normal, centred | #000000 |
| Section heading | `heading` | 22px / 400 / normal | #000000 |
| Body | `body, td, p, a` | 14px / 400 / normal (about 17px) | #000000 |
| Paper title | `papertitle` | 14px / 700 | #1772d0 |
| Own name | `strong` | 14px / 700 | #000000 |
| Venue | `em` | 14px / 400 italic | #000000 |
| Award note | `font[color=red] strong` | 14px / 700 | #ff0000 |
| Media title | `.media-title` | 14px / 700 / 1.4 | #1772d0 |
| Media meta | `.media-meta` | 0.8em = 11.2px / 400 | #666666 |
| Source pill | `.media-source` | 11.2px / 700 | #222222 |
| Media description | `.media-desc` | 0.9em = 12.6px / 400 | #444444 |
| News date pill | `.news-date-pill` | 0.85em = 11.9px / 700 / 1.8, centred | #222222 |
| News text | `.news-text` | 14px / 400 / 1.45 | #000000 |
| Credit | footer `p` | small (13px), right-aligned | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 16px | none | none |
| Media card | 12px (overflow hidden) | 1px #e6e6e6 | 0 1px 2px rgba(0,0,0,0.05); hover 0 6px 16px rgba(0,0,0,0.1) |
| News card | 12px | 1px #e6e6e6 | 0 1px 2px rgba(0,0,0,0.05) |
| Date and source pills | 999px | 1px #f2d59b | none |
| Play disc | 50% (30px) | none | none |
| Paper thumbnails | 0 | none | none |
| Highlighted paper row | 0 | none | none |

## Layout Metrics

- **Container**: outer table `width: 100%; max-width: 900px`, centred, inside the body's 8px margin; at 1440 it spans x=270–1170.
- **Header row**: cells padded 2.5% (22.5px), widths 63% and 40%, vertical-align middle; portrait 75% of the right cell.
- **Section rows**: cells padded 20px; content width 860px.
- **Media grid**: `grid-template-columns: repeat(auto-fit, minmax(180px, 1fr))`, gap 16px, margin-top 10px; three 276px cards at 900px. Card body padding 10px 12px 12px; play disc 30px at 10px from the bottom-right.
- **News card**: margin-top 10px, padding 6px 10px, max-height 210px with internal scroll; rows padding 10px 6px, gap 12px; date pill min-width 78px, padding 0 10px.
- **Paper rows**: two cells padded 20px at 25% / 75%; thumbnail box `.one` 160×160 with `.two` video stacked on top (opacity 0 → 1 on row hover, 0.2s).
- **Page height**: 2,791px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >916px | auto around 900px | 14px | 32px | three media cards per row |
| 600–916px | 8px body margin | 14px | 32px | table shrinks with the window; media grid fits as many 180px+ columns as possible |
| <600px | 8px | 14px | 32px | no media query exists; header and paper rows stay two cells side by side and narrow, media cards drop to two then one column |

## Components

- **Media card** (`a.media-card`): flex column, #ffffff, 1px #e6e6e6, 12px radius, overflow hidden, shadow 0 1px 2px rgba(0,0,0,0.05); 16:9 thumbnail (cover on #eeeeee, or contain on #000000), 30px rgba(0,0,0,0.65) play disc with a white CSS triangle; meta line 11.2px #666666 starting with an apricot source pill (#fbe5ba, 1px #f2d59b, 999px, padding 0 8px, 700 #222222) and "· Mon YYYY"; title 14px/700 #1772d0; description 12.6px #444444. Hover: translateY(-2px), shadow 0 6px 16px rgba(0,0,0,0.1), title #f09228, 0.15s.
- **Scrolling news card**: #fafafa, 1px #e6e6e6, 12px radius, padding 6px 10px, max-height 210px; each row a flex line with an apricot pill date (YYYY-MM, 11.9px/700, min-width 78px) and 14px/1.45 text; #ededed separators; slim 10px scrollbar with a #d6d6d6 pill thumb.
- **Paper row**: left 160×160 still that cross-fades to a looping muted video on row hover; right a bold #1772d0 title, authors with own name bold, italic venue and year, optional #ff0000 bold note in parentheses (sometimes with a trophy emoji), "project page / arXiv / code" links separated by slashes, then a one-sentence summary paragraph.
- **Highlighted paper row**: the whole `<tr>` gets `bgcolor="#fbe5ba"`, edge to edge across the 900px table, with no border or radius.
- **Links**: #1772d0, no underline; hover and focus #f09228.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name, bio, contact | yes | Barron header row with right portrait |
| Social links | yes | centred slash-separated text links |
| Recent media | yes | three-card grid with source pills |
| News | yes | scrolling #fafafa card with date pills |
| Research statement | yes | one 14px paragraph under "Research" |
| Publications | yes | Barron rows with hover videos; key rows apricot |
| Award notes | yes | red bold parentheticals |
| Navigation bar | absent from the source | — |
| Footer | present but non-standard | one small right-aligned template credit |

## Adapting to Other Content

- **Long publication lists**: keep the 160px thumbnails and highlight at most a third of rows in #fbe5ba so the bands still mean something; split into eras with another 22px `heading` row.
- **More news**: the card already scrolls at 210px, so add rows freely; keep YYYY-MM pills for alignment.
- **More media**: the auto-fit grid wraps into extra rows of three; keep 16:9 thumbnails and one source pill per card.
- **Talks or teaching**: reuse the media card with a slide or venue photo as the thumbnail.
- **Students and collaborators**: a plain 14px list under a `heading`; do not add new colors.

## Do's and Don'ts

- Do keep every text size at 14px except the 32px name and 22px headings (and the small pill and meta text inside cards).
- Do use #fbe5ba for three things only: highlighted paper rows, date pills, and source pills.
- Do keep the orange #f09228 as a hover color, never at rest.
- Don't round the paper thumbnails or the highlighted rows; rounding belongs to the added cards and the portrait.
- Don't give headings weight; `heading` is Lato 400.
- Don't add a navbar; the page is one long table.

## Surfaces

White page; white media cards with hairline borders and faint shadows; a #fafafa news card; apricot #fbe5ba bands behind featured papers.

## Imagery

A casual portrait with rounded corners, YouTube and podcast thumbnails (often dark, with bold overlay text), and paper thumbnails that are mostly dark renders (transient light, lidar, a penguin silhouette) with looping videos on hover.

## Layout

Header row, Recent Media, News, Research statement, nine publication rows, credit. About 2,791px tall at 1440.

## Agent Prompt Guide

Quick colors: text #000000, links #1772d0 (hover #f09228), highlight #fbe5ba with edge #f2d59b, pill text #222222, card edge #e6e6e6, news card #fafafa, award #ff0000, meta #666666, description #444444, page #ffffff.

1. "Build a media card grid: grid with repeat(auto-fit, minmax(180px, 1fr)) and 16px gap; each card #ffffff, 1px solid #e6e6e6, 12px radius, box-shadow 0 1px 2px rgba(0,0,0,0.05); 16:9 cover thumbnail with a 30px rgba(0,0,0,0.65) play disc 10px from the bottom-right; body padding 10px 12px 12px with a Lato 11.2px #666666 meta line led by a 999px pill (#fbe5ba, 1px solid #f2d59b, 700 #222222), a 14px/700 #1772d0 title and a 12.6px #444444 description; hover translateY(-2px), box-shadow 0 6px 16px rgba(0,0,0,0.1), title #f09228."
2. "Make a scrolling news card: #fafafa, 1px solid #e6e6e6, 12px radius, padding 6px 10px, max-height 210px, overflow-y auto; rows flex with 12px gap, padding 10px 6px, 1px #ededed separators; date pill min-width 78px, Lato 11.9px/700, line-height 1.8, #222222 on #fbe5ba with a 1px #f2d59b border and 999px radius."
3. "Create a featured publication row: a table row with background #fbe5ba spanning the 900px table; left cell 25% with 20px padding and a 160×160 thumbnail that fades to a looping video on hover; right cell 75% with a Lato 14px/700 #1772d0 title, authors with the owner in 700, italic venue, a bold #ff0000 note in parentheses, slash-separated #1772d0 links and a one-line summary."

## Similar Pages

- Jon Barron template pages, especially ones that add card modules for media or news.
- Computational imaging student pages that colour-band their key papers.

## Quick Start

```css
:root {
  --link: #1772d0;
  --link-hover: #f09228;
  --apricot: #fbe5ba;
  --apricot-edge: #f2d59b;
  --pill-ink: #222222;
  --card-edge: #e6e6e6;
  --news-card: #fafafa;
  --award: #ff0000;
  --font: 'Lato', Verdana, Helvetica, sans-serif;
}
body, td, th, tr, p, a { font-family: var(--font); font-size: 14px; }
a { color: var(--link); text-decoration: none; }
a:hover, a:focus { color: var(--link-hover); }
name { font-size: 32px; }
heading { font-size: 22px; }
papertitle { font-size: 14px; font-weight: 700; }
```

## Provenance

- **URL**: https://anaghmalik.com/
- **Person**: Anagh Malik (computational imaging, neural rendering).
- **Venue / award**: CVPR 2025 Best Student Paper, "Neural Inverse Rendering from Propagating Light".
- **Selection reason**: award rule (first/last author). https://tc.computer.org/tcpami/awards/cvpr-paper-awards/
- **Template credit**: footer reads "Template stolen from Jon Barron's website."
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `stylesheet.css` and the markup (table attributes, `bgcolor`, `<font color>`) read directly, on 2026-10-28.
