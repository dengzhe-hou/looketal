# LeCun · Grey-Bar Table Page — Style Reference

> A 1990s lab homepage that never stopped growing, still laid out in tables.

**Theme:** light

There is no CSS on this page. Every value below comes from HTML presentational attributes (`bgcolor`, `text`, `link`, `vlink`, `<font face size color>`, `width`, `cellpadding`) read from the source, and roles are interpreted from markup and one rendered viewport. Normalized here means attribute values are restated as hex and CSS equivalents.

## Overview

Yann LeCun's home page is a long, table-built document. A left sidebar 140px wide on a cream `#f4e8d1` table holds his photo thumbnail and a stack of uppercase links (HOME, BIO, PUBLICATIONS, arXiv Papers, G-Scholar Profile, SOFTWARE, CBLL, RESEARCH, TEACHING, WHAT'S NEW, then project links), separated by a 13px GIF rule. The main column opens with a 492×90 GIF wordmark "Yann LeCun", a dense affiliation paragraph, then about 30 sections, each introduced by a full-width `#d8d8d8` grey bar with a bold Arial heading. Body text is the browser default serif in slate `#40556b`, links in deep blue `#124a9c`. It is content-first and has outlived several design eras without changing.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Page White | `#ffffff` | `--bg` | `<body bgcolor>` |
| Slate Text | `#40556b` | `--text` | `<body text>` |
| Deep Link Blue | `#124a9c` | `--link` | `<body link>` |
| Visited Teal-Blue | `#2c7aa4` | `--link-visited` | `<body vlink>` |
| Section Bar Grey | `#d8d8d8` | `--bar` | Section header rows (29 uses) |
| Parchment Sidebar | `#f4e8d1` | `--sidebar` | Left navigation table |
| Alert Brick | `#d04040` | `--bar-alert` | "Older Content" header row (1 use) |
| Timestamp Grey | `#808080` | `--meta` | "last updated" small text |

The section-bar `<font>` tags carry a malformed `color=""#8da9ca"`; browsers do not apply it, so bar headings render in link or text color (observed in render as blue links on grey).

## Tokens — Typography

- **Body:** browser default serif (Times New Roman on most systems); no font is set on body text.
- **Headings and sidebar:** Arial, Helvetica via `<font face>`.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Wordmark | 90px-tall GIF image | — | `name.gif`, 492×90 |
| Section bar heading | `size="3"` (≈16px) | bold | Arial, in grey bar |
| Sidebar links | ≈13–16px (inferred from render) | 400 | Uppercase, Arial |
| Body | 16px default (inferred) | 400 | Serif |
| Meta / timestamp | `size=-2` (≈10px) | 400 | Arial, `#808080` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything | 0 (tables and GIFs only) |

Section bars: `table width=100% cellpadding=4 cellspacing=0 border=0`. Sidebar table: `width=140 cellpadding=1 cellspacing=0`. No shadows. No max width: the main column spans the window.

## Components

- **Sidebar menu:** cream table, photo thumbnail (122×161), uppercase Arial links, `menuhline.gif` 140×13 separators, badges at the bottom (Lush, DjVuLibre 140×49, Free Culture 88×31, hacker glider emblem).
- **Section bar:** grey full-width row, bold Arial heading, anchored with `<a name>` for in-page links (blog, bio, contact, students, press, teaching, talks, lenet, mnist, music, photos and more).
- **Right-floated thumbnails:** project images aligned right in the text (`align=right`, for example 128×96, 103×140).
- **Inline link lists:** social networks with handle and a one-line description each.

## Page Modules

- **Bio/photo:** photo thumbnail in the sidebar; affiliation paragraph (Meta, NYU Courant, NAE, NAS, ACM Turing Award) at the top of the main column; "Biography / CV / Portrait" section.
- **News:** "WHAT'S NEW" sidebar link; social network section with dated notes.
- **Publication list:** "PUBLICATIONS", arXiv and Google Scholar links in the sidebar; full list on a separate page (the scan flagged publication-list markup).
- **Software and data:** Lush, DjVu, LeNet, MNIST, NORB sections with figures.
- **Teaching and talks:** dedicated sections.
- **Students:** group section.
- **Awards:** "bragging" section with honors.
- **Contact:** contact section.
- **Hobbies:** music, photos, "fun" sections.

## Do's and Don'ts

- Do introduce every section with the same grey bar; it is the only navigation cue in a very long page.
- Do keep the sidebar narrow and cream.
- Don't add CSS frameworks or web fonts; the identity is the default serif plus Arial bars.
- Don't trim content to fit a viewport; this page scrolls by design.

## Surfaces

White page, cream sidebar, grey heading bars. Nothing floats or casts a shadow.

## Imagery

GIF wordmark, photo thumbnail, small project thumbnails and badges, research figures (NORB, LeNet).

## Layout

Two-column table: 140px sidebar plus fluid main column, roughly 30 stacked sections, about 490 links.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, text `#40556b`, link `#124a9c`, visited `#2c7aa4`, bar `#d8d8d8`, sidebar `#f4e8d1`.

1. "Build a section bar: a full-width row with background `#d8d8d8`, padding 4px, bold Arial 16px heading that is an anchor."
2. "Build a sidebar: 140px wide, background `#f4e8d1`, photo at top, uppercase Arial links stacked, a thin rule image between groups."
3. "Build body text: default serif 16px in `#40556b`, links `#124a9c`, visited `#2c7aa4`, small `#808080` timestamp in Arial."

## Similar Pages

Long-lived 1990s faculty pages (for example Aho in this batch); early web personal homepages.

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #40556b; --link: #124a9c; --link-visited: #2c7aa4;
  --bar: #d8d8d8; --sidebar: #f4e8d1; --bar-alert: #d04040; --meta: #808080;
  --font-body: 'Times New Roman', serif; --font-ui: Arial, Helvetica, sans-serif;
  --sidebar-width: 140px;
}
.section-bar { background: var(--bar); padding: 4px; font: bold 16px var(--font-ui); }
```

## Provenance

- **URL:** http://yann.lecun.com/
- **Person:** Yann LeCun, deep learning and computer vision.
- **Award:** ACM A.M. Turing Award 2018.
- **Selection reason:** Rule A, Turing Award 2018 laureate (awards.acm.org/turing); personal domain.
- **Template credit:** none; hand-written HTML.
- **Measurement method:** extract_style.py found no CSS, so colors were counted from HTML attributes in the source (29 `bgcolor="#d8d8d8"`, 39 tables, 29 images), plus one rendered viewport. Pixel sizes for `<font size>` values are the usual browser mapping (inferred).
