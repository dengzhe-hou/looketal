# Eysenbach al-folio Orange — Style Reference

> A stock al-folio lab page wearing Princeton orange.

**Theme:** light

Measurements come from the static HTML and its linked CSS: Bootstrap 4.6.1, MDBootstrap 4.20.0, bootstrap-table, Font Awesome 6.5.2, Academicons 1.9.1, the GitHub Pygments theme, Google Fonts (Roboto, Roboto Slab, Material Icons) and the site's compiled `/assets/css/main.css`. The extractor's frequency lists are dominated by Bootstrap and MDB defaults (`#007bff`, `#ff3547`, `#00c851`, Material shadows); those are filtered out here, and only values reached by the page's own markup are kept. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Benjamin Eysenbach's site is the al-folio Jekyll theme with its theme color changed from the default purple to Princeton orange `#e87a0d` (light mode; the compiled CSS keeps al-folio's `#2698ba` for dark mode, but this page ships no theme toggle). A fixed top navbar (95% opacity white, 1px divider bottom border, with a reading progress bar) lists about, lab, hiring, teaching, talks/podcasts and publications. The about page opens with "**Benjamin** Eysenbach" (first name bold), a one-line title at Princeton, affiliation links, and a right-floated headshot at 30% width with `z-depth-1 rounded` and an address block under it. Prose with GitHub emoji images follows, then a borderless news table, then "selected publications" grouped by year (2025 back to 2019) with 29 entries, each with a 200px max preview thumbnail, bold title, author line, italic periodical, outlined PDF / Code / Website buttons and Altmetric / Dimensions badges. The footer is a sticky-bottom copyright line with "Last updated".

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Princeton Orange | `#e87a0d` | `--global-theme-color` | Links, hover, abbr venue badge fill, award outline |
| Orange Wash | `rgba(232,122,13,0.05)` | `--global-code-bg-color` | Inline code background |
| Page White | `#ffffff` | `--global-bg-color` | Body and navbar background |
| Ink Black | `#000000` | `--global-text-color` | Body text, outlined button text and border |
| Light Grey | `#828282` | `--global-text-color-light` | Secondary text, periodical lines |
| Divider | `rgba(0,0,0,.1)` | `--global-divider-color` | Navbar bottom and footer top borders |
| Hover White | `#ffffff` | `--global-hover-text-color` | Text on orange hover |
| Footer Charcoal | `#1c1c1d` | `--global-footer-bg-color` | Declared footer background (al-folio default) |
| Muted Note | `#aaa` | (inline) | Repeated `style="color:#aaa;"` notes in publications |

Callout block colors (`--global-tip-block #42b983`, warning `#e7c000`, danger `#c00`) are declared by al-folio but unused on this page.

## Tokens — Typography

- **Family:** Roboto (Google Fonts, 300/400/500/700), with Bootstrap's `-apple-system` system stack as fallback; Roboto Slab and Material Icons are loaded but not prominent. Substitute: `Roboto` or `Inter`.
- **Mono:** `SFMono-Regular`, Menlo, monospace (Bootstrap).
- **Weights in use:** 300 (most frequent, al-folio light headings), 400 body, bold first name and publication titles (`font-weight: bolder`).

| Role | Size | Weight | Notes |
|---|---|---|---|
| Page title `.post-title` | Bootstrap h1 2.5rem (inferred) | 300, first name bold | |
| Section h2 (news, selected publications, years) | Bootstrap h2 2rem (inferred) | 300 | Lowercase labels |
| Body | 1rem | 400 | line-height 1.5 |
| Publication title | 1rem | bolder | |
| Author / periodical | .875rem to 1rem (inferred) | 400 | Periodical italic, light grey |
| Button `btn-sm` | .875rem | 400 | Outlined |
| Footer | .9rem | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, inputs (Bootstrap) | .25rem |
| Headshot and previews (`rounded`) | .25rem |
| abbr badge | 0 (square block) |

- **Shadows:** `z-depth-1` on the headshot and previews, `0 2px 5px 0 rgba(0,0,0,.16), 0 2px 10px 0 rgba(0,0,0,.12)` (MDB); link buttons use `z-depth-0` (no shadow). Navbar has `box-shadow: none`.
- **Layout max-width:** Bootstrap `.container` (1140px at xl, inferred); publication rows split `col-sm-2` preview / `col-sm-8` text.
- **Body padding:** 70px bottom for the sticky footer; footer padding 40px top and bottom.

## Components

- **Navbar.** Fixed top, white at 0.95 opacity, 1px `rgba(0,0,0,.1)` bottom border, no shadow; active item marked "(current)".
- **Profile.** `.profile.float-right` at 30% width, headshot with `img-fluid z-depth-1 rounded`, centered address lines below.
- **News table.** `table table-sm table-borderless` inside `table-responsive`: date column then one-line items with emoji.
- **Publication row.** Preview image (min 80px, max 200px, `z-depth-1 rounded`), bold title, author list, italic `periodical` (two per entry), then `.links` buttons.
- **Link button.** `btn btn-sm z-depth-0`, 1px solid black border, black text, padding `.25rem 1rem`; hover fills with the theme color (al-folio behaviour, inferred).
- **Venue abbr.** `.abbr abbr` block in `#e87a0d` with white text, padding 0 1rem (al-folio).
- **Footer.** Sticky-bottom, 1px top divider, `.9rem`, copyright plus last-updated date.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | Right-floated 30% headshot with address |
| News | Yes | Borderless small table |
| Publication list with thumbnails | Yes, 29 selected entries by year | al-folio bibliography rows |
| Link buttons | PDF, Code, Website | Outlined black small buttons |
| Metrics badges | Altmetric and Dimensions | Embedded third-party badges |
| Lab / hiring / teaching / talks | Separate pages | Nav items |
| Math rendering | MathJax 3.2 loaded | |
| Awards | Not on home page | |

## Do's and Don'ts

- Do keep al-folio's white canvas and change only `--global-theme-color` for identity.
- Do keep link buttons outlined black and thumbnails at most 200px.
- Do write section labels in lowercase light-weight headings.
- Don't let Bootstrap's blue `#007bff` or MDB's colored buttons leak into content.
- Don't add a second accent; orange carries every interactive state.

## Surfaces

White page, white navbar at 95% opacity, and a faint orange wash for inline code. The footer is plain white here with a divider (the declared `#1c1c1d` footer background is not applied by this layout, inferred).

## Imagery

29 publication preview images served through `responsive-img-srcset` (WebP srcsets), a headshot, and 20px GitHub emoji images in prose.

## Layout

Bootstrap container, single column with a floated profile on the about block; publications as `row` with 2/8 column split. Navbar collapses to a toggle on small screens.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#000000`, light text `#828282`, theme `#e87a0d`, divider `rgba(0,0,0,.1)`.

1. "Create an al-folio style publication row: 200px max preview with .25rem radius and a soft Material shadow, bold title, author line, italic grey venue, then outlined black `btn-sm` buttons 'PDF', 'Code', 'Website'."
2. "Make a fixed white navbar at 0.95 opacity with a 1px `rgba(0,0,0,.1)` bottom border, lowercase Roboto links, hover `#e87a0d`."
3. "Add a venue abbreviation block: `#e87a0d` background, white text, padding 0 1rem, no radius, left of the title."

## Similar Pages

Any al-folio site (alshedivat.github.io/al-folio). Within this collection, al-folio pages differ mainly by `--global-theme-color`.

## Quick Start

```css
:root {
  --global-bg-color: #fff;
  --global-code-bg-color: rgba(232,122,13,0.05);
  --global-text-color: #000;
  --global-text-color-light: #828282;
  --global-theme-color: #e87a0d;
  --global-hover-color: #e87a0d;
  --global-hover-text-color: #fff;
  --global-divider-color: rgba(0,0,0,.1);
  --font: Roboto, -apple-system, "Segoe UI", sans-serif;
  --radius: .25rem;
}
```

## Provenance

- **URL:** https://ben-eysenbach.github.io/
- **Person:** Benjamin Eysenbach, reinforcement learning
- **Venue / award:** NeurIPS 2025 Best Paper (1000 Layer Networks for Self-Supervised RL, last author)
- **Selection reason:** Rule B, last author of a NeurIPS 2025 Best Paper (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/).
- **Template credit:** al-folio Jekyll theme (identified from `--global-*` variables, `z-depth` classes, progress bar script and bibliography markup; the footer carries no theme credit). Bootstrap 4.6.1 and MDBootstrap 4.20.0.
- **Measurement method:** `extract_style.py` over HTML and five stylesheets, then `main.css` was read for the `:root` block and component rules. Bootstrap heading sizes and container width are inferred from framework defaults. The rendered page was not viewed.
