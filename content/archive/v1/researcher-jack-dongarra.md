# Dongarra Netlib Frame — Style Reference

> A 2001 lab intranet printed on grey card stock.

**Theme:** light

Measurements come from the page's static HTML (no external stylesheet exists; one inline `<style>` block plus `<body>` and `<font>` attributes). Values are read directly from attributes such as `bgcolor`, `link` and `face`, so there are no framework defaults to filter out. Roles are interpreted, not declared by the author. The rendered page was not viewed.

## Overview

Jack Dongarra's netlib page is a classic table-layout homepage. An 800px content table sits on a mid-grey `#cccccc` page, framed by 4px GIF corner and edge images (`topleft.gif`, `top.gif`, `sides.gif`). The name is a 303x50 JPEG banner (`jack.jpg`) on white, followed by a grey `#999999` navigation strip with white Verdana bold links separated by pipes (home | books | courses | jobs | notes | papers | projects | talks). Below that, a white body holds affiliations, a contact block, a list of maps, and a long "Other Information" list of reports and op-eds (Fugaku, Frontier, Sunway TaihuLight, the Nature "Ten computer codes" piece). Links are un-underlined navy and turn red on hover. There are no cards, no shadows, no web fonts and no responsive behaviour.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Card Stock Grey | `#cccccc` | `--page` | `<body bgcolor>`, the margin around the content table |
| Sheet White | `#ffffff` | `--surface` | Banner cell and content cells |
| Strip Grey | `#999999` | `--nav-bg` | Navigation bar cell |
| Strip Ink | `#ffffff` | `--nav-text` | Verdana bold nav labels and pipes |
| Netlib Navy | `#003399` | `--link` | `<body link>` |
| Visited Navy | `#003366` | `--link-visited` | `<body vlink>` |
| Active Maroon | `#660000` | `--link-active` | `<body alink>` |
| Hover Red | `#cc0000` | `--link-hover` | `a:hover` in the inline style block |
| Body Black | `#000000` (inferred) | `--text` | Browser default text color; no `text` attribute set |

## Tokens — Typography

- **Family:** `Verdana, Arial, Helvetica, sans-serif` via `<font face>` throughout. Substitute: Verdana is near-universal; fall back to `Tahoma` or `DejaVu Sans`.
- **Symbol glyphs:** a few spans set `font-size: 12px; font-family: "SymbolMT", serif` (pasted from a Word or PDF source).
- **Weights:** bold (`<b>`) for nav labels and headings; regular otherwise.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Name line (text fallback) | `<font size="+3">` (about 24px, inferred) | bold | The visible name is the JPEG banner |
| Nav strip | `<font>` default 3 (about 16px, inferred) | bold | White on `#999999`, right-aligned |
| Body lists | `size="2"` (about 13px, inferred) | 400 | Verdana |
| Fine print | `size="1"` (about 10px, inferred) | 400 | Footer-style notes |
| Pasted symbols | 12px | 400 | SymbolMT |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything | 0 (square table cells) |

- **Frame:** 4px corner GIFs top-left, 6px right edge (`sides.gif`), 800px top edge; the frame reads as a thin bevel.
- **Shadows:** none.
- **Layout max-width:** 800px fixed table (`width="800"`); inner columns at 224px, 260px, 300px and 303px.
- **Spacing:** `cellpadding="0"`, `border="0"`; spacing comes from transparent spacer GIFs (`trans.gif` at 30x30 and 56x20).

## Components

- **Name banner.** `<img src="images/jack.jpg" width="303" height="50">` in a white cell spanning four columns, left-aligned.
- **Nav strip.** One `<td bgcolor="#999999" align="center">` containing a right-aligned div of `<b><font face="Verdana..." color="#ffffff">` links separated by `|`.
- **Affiliation block.** Stacked lines (Emeritus Professor, University of Tennessee; Turing Fellow, Manchester; Adjunct Professor, Rice) with no separators.
- **Contact block.** Postal address, e-mail and phone as plain lines.
- **Report list.** Long bulleted list of titled reports, each a navy link followed by authors and date in plain text.
- **Video links.** Two YouTube links rendered as plain text links, not embeds.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Banner image only, no headshot | 303x50 JPEG on white |
| Affiliations / contact | Yes | Plain Verdana lines |
| News | No dedicated section | Recent reports lead the "Other Information" list |
| Publication list | Linked out (`papers` nav item) | Not on the home page |
| Talks / books / courses | Linked out from the nav strip | |
| Awards | No | |
| Maps | Yes | Five link list (ICL, Knoxville, ORNL, world) |
| Results table | One layout table | Not a data table |

## Do's and Don'ts

- Do keep the page as one fixed 800px sheet on a grey ground.
- Do use white bold Verdana on `#999999` for the nav strip.
- Do keep links un-underlined navy with a red hover.
- Don't add rounded corners, shadows or web fonts; the look depends on their absence.
- Don't make the layout fluid; the GIF frame assumes the fixed width.

## Surfaces

Three flat surfaces: `#cccccc` page, `#ffffff` sheet, `#999999` nav strip. The sheet edge is a 4 to 6px GIF bevel.

## Imagery

A single name banner JPEG plus decorative frame GIFs and spacer GIFs. No portrait, figures or thumbnails on the home page.

## Layout

Centered fixed table: banner row, nav row, then content rows with a narrow left column for affiliations and a wider right column for lists. Nothing reflows on mobile; the page scrolls horizontally below 800px.

## Agent Prompt Guide

**Quick colors:** page `#cccccc`, sheet `#ffffff`, nav `#999999` with white text, link `#003399`, visited `#003366`, hover `#cc0000`.

1. "Make an 800px fixed-width white sheet centered on a `#cccccc` page with a 4px bevel frame; no radius, no shadow."
2. "Add a full-width `#999999` nav bar with right-aligned bold white Verdana links separated by ` | `."
3. "Write a report list in 13px Verdana: navy `#003399` un-underlined titles, red `#cc0000` on hover, plain author and date after each."

## Similar Pages

Late-1990s Dreamweaver-era faculty pages with table frames and spacer GIFs; compare the Barto and Sutton pages in this batch, which share the no-CSS approach but drop the frame.

## Quick Start

```css
:root {
  --page: #cccccc;
  --surface: #ffffff;
  --nav-bg: #999999;
  --nav-text: #ffffff;
  --link: #003399;
  --link-visited: #003366;
  --link-active: #660000;
  --link-hover: #cc0000;
  --font: Verdana, Arial, Helvetica, sans-serif;
  --sheet: 800px;
}
body { background: var(--page); font-family: var(--font); }
a { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); }
```

## Provenance

- **URL:** https://netlib.org/utk/people/JackDongarra/
- **Person:** Jack Dongarra, high-performance numerical computing
- **Venue / award:** ACM A.M. Turing Award 2021
- **Selection reason:** Rule A, Turing Award 2021 laureate (https://awards.acm.org/turing); personal page on netlib.
- **Template credit:** none; hand-built HTML table layout (no generator meta tag, no external CSS).
- **Measurement method:** `extract_style.py` on static HTML found only `#cc0000`, 12px and one bold weight, so the remaining values were read from `body`, `td` and `font` attributes in the curl'd HTML. Pixel sizes for `<font size>` levels are browser-default conversions and marked inferred. The rendered page was not viewed.
