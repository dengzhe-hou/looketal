# Yejin Choi Charcoal Matte — Style Reference

> A white press sheet pinned to a charcoal studio wall, annotated in red and green pen.

**Theme:** light

Measurements come from the static HTML and its one working stylesheet, `choi.css`. The page also links `bootstrap.min.css` and two Google Fonts files at relative paths (`./css`, `./css(1)`), but all three return HTTP 404 today, so Bootstrap contributes nothing and the Monoton / Permanent Marker classes fall back. Colors are taken from `choi.css` and `<font color>` attributes. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Yejin Choi's page is a single long document on a 1000px-wide body whose background is near-black `rgb(30,30,30)`. Inside, a `.container` with 4em side margins holds a white `.content` panel padded 2ex, so the reading sheet floats on a charcoal mat. The header is a table: a right-aligned 200px portrait (with a tiny italic photo credit), the name, the endowed chair title, a green "MacArthur" link, and the Stanford address in `<font size="2">`. Below it, h3 sections run in order: News, Awards, Recognition, Research Interests, Recent Talks, Recent Preprints, Recent Publications (2016 to 2026), Selected Publications (2011 to 2015), Full List, Teaching, xlab, Short Bio and Personal. Lists use a custom GIF bullet (`ul.emlist`). The main inline accents are `<font color="red">` (39 uses, for awards and keynote labels) and `<font color="green">` (50 uses, for honours and highlighted names), plus a few `#306EFF` blue spans.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Studio Charcoal | `rgb(30,30,30)` / `#1e1e1e` | `--mat` | `body` background around the sheet |
| Press White | `rgb(255,255,255)` | `--surface` | `.content` panel |
| Sheet Ink | `rgb(0,0,0)` | `--text` | Body text |
| Ink Blue | `rgb(0,51,160)` / `#0033a0` | `--link` | `a:link` and `a:visited`, no underline |
| Hover Brick | `rgb(154,0,0)` / `#9a0000` | `--link-hover` | `a:hover` |
| Red Pen | `red` (`#ff0000`) | `--mark-award` | Award names, keynote labels, "Best Paper" lines |
| Green Pen | `green` (`#008000`) | `--mark-honour` | MacArthur link, highlighted honours and names |
| Signal Blue | `#306EFF` | `--mark-alt` | Five emphasised spans |
| NVIDIA Green | `#76b900` | `--mark-employer` | One (commented-out) NVIDIA mention |
| Caption Grey | `grey` | `--caption` | Photo credit, `size="1"` |
| Nav Paper | `rgb(250,250,245)` | `--panel` | `div.publicationnav` sidebar box (declared) |

## Tokens — Typography

- **Body:** `font: normal 90% Candara, Constantia, Avenir Next, Palatino, Cambria, Times`. Candara is a Windows ClearType humanist sans; on macOS it falls to Avenir Next, elsewhere to Palatino or Times (inferred). Substitute: `Candara` then `Avenir Next`, or `Nunito Sans`.
- **Display flourishes:** `.vcremph` asks for Monoton 500 and `.swagemph` for Permanent Marker, but their font files 404, so both render in `monospace` / `cursive` fallbacks (inferred).
- **Weights:** 400 body, `<b>` for paper short names ("HieraSuite:", "SurfDesign:").

| Role | Size | Weight | Notes |
|---|---|---|---|
| Base | 90% of browser default (about 14.4px, inferred) | 400 | Candara stack |
| Table cells | 90% of base (`TD{font-size:90%}`) | 400 | Header table |
| h3 section | browser h3 (inferred about 1.17em) | bold | Ends with a colon ("News:") |
| Address block | `<font size="2">` | 400 | |
| Photo caption | `xx-small`, italic | 400 | Right-floated |
| Name | `<font size="5">` (inferred) | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Everything | 0 |

- **Shadows:** none.
- **Layout width:** `body { width: 1000px; margin: 0 auto }`; `.container` margin `1em 4em`; `.content` padding 2ex, `min-width: 80ex`.
- **Lists:** `ul` margin-left 5ex, right 5ex, padding-left 0; `ul.publicationlist > li` margin-top 1em; publication items separated by `<br><br>`.
- **Paragraph indents:** `p.indent` 5ex both sides.

## Components

- **Header table.** Name, title lines, coloured honour link, address, and a `width="200" align="right"` portrait; a second 90px "mosaic-brain" image floats right.
- **News line.** Starts with "- ", accent label in red or green, then a link, with an 18px TV icon before video links.
- **Award line.** Indented with `&nbsp;` runs, red award label, venue as a link.
- **Publication item.** `<ui>` inside `ul.emlist`: linked title (bold short name), author list, venue line, blank line. Bullet is `bullet.gif`.
- **Links.** Ink blue, never underlined, brick red on hover.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes, portrait plus "Short Bio" paragraph at the end | Right-floated image |
| Contact | Office, phone, e-mail | `size="2"` lines |
| News | Yes, about 25 items | Dash bullets, red / green labels |
| Awards / recognition | Yes | Red labels, indented lines |
| Talks | Yes (2020 to 2026) | Link list with TV icons |
| Publication list | Yes, preprints plus 2011 to 2026 | GIF-bullet list, no thumbnails, title links to arXiv |
| Teaching / lab (xlab) | Yes | Short lists |
| Personal | "Scuba!" | |

## Do's and Don'ts

- Do keep the white sheet narrow on a charcoal mat; the contrast frames the page.
- Do use red and green text only as short labels, never for whole lines.
- Do keep links un-underlined deep blue with a brick hover.
- Don't rely on the Bootstrap or Google Font links; they are dead and the page works without them.
- Don't add thumbnails or cards; the list is meant to read as a typed CV.

## Surfaces

Two: charcoal `#1e1e1e` outside, white inside. The optional `publicationnav` box would add `rgb(250,250,245)` with a 1px border.

## Imagery

One portrait (200px), one small decorative brain mosaic (90px), and 18px TV icons. No figures.

## Layout

Fixed 1000px centered body, inner white panel, one column of sections in source order. Not responsive.

## Agent Prompt Guide

**Quick colors:** mat `#1e1e1e`, sheet `#ffffff`, text `#000000`, link `#0033a0`, hover `#9a0000`, award label `red`, honour label `green`.

1. "Make a 1000px body on `#1e1e1e` with an inner white panel (side margins 4em, padding 2ex); Candara 90% body text."
2. "Write a news line: leading '- ', a short `red` label, then an un-underlined `#0033a0` link that turns `#9a0000` on hover."
3. "List publications with a small GIF bullet: linked title with bold short name, author line, venue line, then an empty line."

## Similar Pages

Long-running NLP faculty pages that grew in place (one file, coloured font tags, decade-spanning lists). The Barto and Dongarra pages in this batch share the font-tag accent habit.

## Quick Start

```css
:root {
  --mat: rgb(30,30,30);
  --surface: #ffffff;
  --text: #000000;
  --link: rgb(0,51,160);
  --link-hover: rgb(154,0,0);
  --mark-award: red;
  --mark-honour: green;
  --font: Candara, Constantia, "Avenir Next", Palatino, Cambria, Times, serif;
}
body { background: var(--mat); width: 1000px; margin: 0 auto; font: normal 90% var(--font); }
.content { background: var(--surface); padding: 2ex; }
a { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); }
```

## Provenance

- **URL:** https://yejinc.github.io/
- **Person:** Yejin Choi, NLP and commonsense reasoning
- **Venue / award:** NeurIPS 2025 Best Paper (Artificial Hivemind, last author)
- **Selection reason:** Rule B, last author of a NeurIPS 2025 Best Paper (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/).
- **Template credit:** none; hand-written HTML with a personal `choi.css`. The linked `bootstrap.min.css` and Google Fonts files return 404.
- **Measurement method:** `extract_style.py` failed to load the two 404 stylesheets and found almost nothing. `choi.css` was fetched separately and `<font>` attributes were counted in the HTML. Effective font fallback and pixel sizes are inferred; the rendered page was not viewed.
