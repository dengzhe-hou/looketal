# Hinton · Steel-Blue Card Grid — Style Reference

> A tidy faculty noticeboard pinned to a steel-blue wall.

**Theme:** light

Measurements are normalized from the page HTML, its inline `<style>` block, the shared `css/styles.css`, and Bootstrap 5.3.0 from cdnjs; roles are interpreted from markup and one rendered viewport. Bootstrap's full palette is in the scan; only colors the custom CSS or used classes set are listed.

## Overview

Geoffrey Hinton's university page is a Bootstrap 5.3 directory: a white header with his name, a bright blue book pre-order banner, then a 3-column grid of white cards on a steel-blue `#7997b9` background. Each card has an icon and a semibold title underlined by a short 2rem navy bar, followed by a plain list of grey links (Scientific Publications, Teaching, Media Appearances, Amusing Odds & Ends, Speaking Requests, Media Requests, About Me, Students, Contact). Cards rise 3px on hover. Several items open `<dialog>` popups instead of new pages. There are no images on the index.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Steel Wall | `#7997b9` | `--bg-color` | Main background behind cards |
| Navy Primary | `#2e446e` | `--bs-primary` | Card-title underline bar, icons, hover links, section titles |
| Card White | `#ffffff` | `--card` | Cards, header, popups |
| Footer Mist | `#f8f9fa` | `--footer` | Footer and body background below it |
| Banner Blue | `#1a73e8` | `--banner-color` | Book pre-order banner |
| Banner Hover | `#d7e6ff` | `--banner-link-hover` | Banner link hover |
| Link Grey | `#6c757d` | `--text-muted` | Card link lists, close button |
| Popup Text | `#495057` | `--text-popup` | Popup body text |
| Name Ink | `#212529` | `--text` | Body and item names |
| Hairline | `#dee2e6` | `--border` | Header bottom border |
| Overlay | `rgba(0,0,0,0.5)` | `--overlay` | Popup backdrop |

## Tokens — Typography

- **Family:** Inter (substitute system UI stack: -apple-system, Segoe UI, Roboto) for everything.
- **Icons:** Bootstrap Icons 1.11.1.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Name in header | 1.25rem (inferred, Bootstrap `h5`-scale) | 600 | 1.2 |
| Card title | 1.25rem | 600 | 1.2 |
| Section title (subpages) | 1.5rem | 600 | 1.2 |
| Card links | 1rem | 400 | 1.5 |
| Item year, thesis | 0.9rem | 400 / italic | 1.5 |
| Popup title | 1.25rem | 600 | 1.2 |
| Banner | 1rem | 600 | 1.5 |
| Mobile card title | 0.9rem → 0.7rem | 600 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Cards | var(--bs-border-radius) = 0.375rem (Bootstrap 5.3 default, inferred) |
| Popup content, list items | 0.5rem |
| Popup links | 0.25rem |
| Title underline bar | 0 |

Shadows: card hover `0 .5rem 1rem rgba(0,0,0,.15)`; list items `0 0.125rem 0.25rem rgba(0,0,0,0.075)`. Spacing: card body padding-block 0.75rem; card-title padding-bottom 0.75rem; grid gutter `g-4` (1.5rem). Popups max-width 400px (wide 600 / 800px). Container: Bootstrap `.container` (1320px at xxl).

## Components

- **Header:** white bar, name left, `#dee2e6` bottom border.
- **Book banner:** full-width `#1a73e8` strip, white 600-weight text with underlined links.
- **Grid card:** white card, title row with Bootstrap icon in `#2e446e`, 2rem × 2px navy underline bar, grey link list without bullets; translateY(-3px) on hover.
- **Popup:** `<dialog>` as a full-screen 50% black overlay with a centered white panel, close button top right.
- **Item list (subpages):** white rounded rows with item name in navy and year in grey.

## Page Modules

- **Bio/photo:** "About Me" card linking a brief biography; no photo on the index.
- **News:** the book banner acts as the single news item.
- **Publication list:** "Scientific Publications" card linking a full reverse-chronological list with topic filter.
- **Teaching:** Coursera course and archived university courses.
- **Media:** appearances (video, print, podcasts) and media request form.
- **Students:** card with information for prospective students.
- **Contact:** email card.
- **Awards:** on a separate page, not on the index.

## Do's and Don'ts

- Do keep every card identical in structure: icon, title, short navy bar, grey links.
- Do let the steel-blue wall show between cards.
- Don't add images or color to cards; navy is the only accent inside them.
- Don't link out where a short popup will do.

## Surfaces

Steel-blue wall, white cards with hover shadow, white header, light grey footer, dark overlay for popups.

## Imagery

None on the index; icons only.

## Layout

3 × 3 card grid on desktop, collapsing to compact icon tiles (`col-4`, centered icons at 2rem) on mobile.

## Agent Prompt Guide

Quick colors: wall `#7997b9`, card `#ffffff`, primary `#2e446e`, link grey `#6c757d`, banner `#1a73e8`, footer `#f8f9fa`.

1. "Build a directory card: white, Bootstrap radius, title Inter 1.25rem/600 with a `#2e446e` icon and a 2rem × 2px `#2e446e` underline bar; list of `#6c757d` links that turn navy on hover; lift 3px with `0 .5rem 1rem rgba(0,0,0,.15)`."
2. "Build an announcement banner: `#1a73e8`, white 600-weight text, underlined white links, hover `#d7e6ff`, padding .75rem 0."
3. "Build a popup: dialog filling the viewport with `rgba(0,0,0,.5)`, centered white panel radius .5rem, padding 1.5rem, max-width 400px."

## Similar Pages

University faculty pages rebuilt with Bootstrap card grids.

## Quick Start

```css
:root {
  --bs-primary: #2e446e; --bg-color: #7997b9;
  --card: #ffffff; --footer: #f8f9fa; --banner: #1a73e8;
  --muted: #6c757d; --text: #212529; --border: #dee2e6;
  --shadow-hover: 0 .5rem 1rem rgba(0,0,0,.15);
  --font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
body { font-family: var(--font); background: var(--bg-color); }
```

## Provenance

- **URL:** https://www.cs.toronto.edu/~hinton/
- **Person:** Geoffrey Hinton, deep learning.
- **Award:** ACM A.M. Turing Award 2018.
- **Selection reason:** Rule A, Turing Award 2018 laureate (awards.acm.org/turing); self-maintained university page.
- **Template credit:** none; footer names a webmaster (Patrick Yung Kang Lee) and "© 2025-2026 Geoffrey Hinton".
- **Measurement method:** extract_style.py scan, full reading of the inline style block and the first part of `css/styles.css` (which sets `--bg-color:#7997b9` and Inter), one rendered viewport. The steel-blue background matches the render.
