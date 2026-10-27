# Liwei Jiang Navy Ledger — Style Reference

> A tidy navy research ledger with a signature in brush script and a gold trophy stamp.

**Theme:** light

Measurements come from the page's single 44KB inline `<style>` block and the HTML (no external CSS, no framework). Values below are declared by the author in `:root` variables and component rules; nothing is a framework default. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Liwei Jiang's page is a hand-built single-file site in a 1100px container. A sticky white nav sits flush under the top edge with a 2px `#2b6cb0` border on three sides and 12px bottom corners. The header is a two-column grid: a 160px square photo with 8px radius and a deep shadow, then the name set in Kaushan Script (brush script) next to the Chinese name in Ma Shan Zheng, a muted title line with "NVIDIA" in NVIDIA green `#76b900`, and an affiliation line painted with a navy-to-sky gradient clipped to text. Below come interest tags as soft blue "keycap" pills with a hard 3px bottom shadow, News with dated items and slanted uppercase badges, a year-grouped Publications list of white cards, an Awards list with a gold gradient trophy icon, Grants, Education and Experience, Teaching and Services, and a personal quote with a large yellow Georgia quote mark. The palette is Chakra-UI-like navy and blue with gold and red accents.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Harbor Navy | `#1a365d` | `--primary-color` | h1/h2, publication titles, news dates, tag text |
| Seaboard Blue | `#2b6cb0` | `--secondary-color` | Nav border, venue text, h3 sub-headings |
| Signal Blue | `#3182ce` | `--accent-color` | Paper link button outline and text |
| Sky Blue | `#4299e1` | (literal) | Gradient end of affiliation text, badge fills |
| Slate Ink | `#2d3748` | `--text-color` | Body text |
| Slate Grey | `#4a5568` | `--dark-gray` | Title line, tooltips |
| Mist | `#f7fafc` | `--light-gray` | Photo placeholder background |
| Hairline | `#e2e8f0` | `--border-color` | Card hover border |
| Card Edge | `#eef1f5` | (literal) | Publication card border |
| Keycap Frost | `#f5faff` to `#eef5fd` | (literal gradient) | Interest tags and social buttons |
| Keycap Shadow | `#ccdcec` | (literal) | 3px bottom edge of tags |
| Trophy Gold | `#ffcc00` | `--yellow-color` | Year headers, trophy icon, quote mark, "upcoming" badge |
| Badge Umber | `#5b4500` | (literal) | Text on gold badges |
| Award Red | `#ff2600` | `--red-color` | `.paper-award` text |
| Ember Orange | `#ff5c00` | `--orange-color` | Accent variable (declared) |
| NVIDIA Green | `#76b900` | (literal) | Global `a` color (weight 600) and the "NVIDIA" employer word |
| Highlighter | `#e4eefb` | (literal) | `.topic-hl` underline-highlight gradient |

## Tokens — Typography

- **Body:** `'Avenir Next', -webkit-system-fallback, 'Segoe UI', Roboto, sans-serif`. Substitute: `Nunito Sans` or `Inter`.
- **Name (English):** `Kaushan Script`, cursive, weight 400 (Google Fonts). Commented alternatives are Parisienne, Dancing Script, Great Vibes and Playfair Display, all still loaded.
- **Name (Chinese):** `Ma Shan Zheng`, cursive.
- **Quote mark:** Georgia, serif, 2.4rem.
- **Weights in use:** 400, 500 (most frequent), 550, 600, 700.

| Role | Size | Weight | Line height |
|---|---|---|---|
| h1 | 2.8rem | 400 | 1.6 (body) |
| h2 section (and name block) | 2.2rem | 400 | 1.6 |
| h3 sub-heading | 1.3rem | 400 | 1.6 |
| Year header | 1.2rem | 700 | 1.6 |
| Title line | 1.15rem | 500 | 1.6 |
| Publication title | 1rem | 600 | 1.3 |
| Publication meta | 0.9rem | 500 | 1.5 |
| Interest tag / social button | 0.88rem | 500 | 1.5 |
| Paper link button | 0.8rem | 400 | 1.5 |
| News badge / tooltip | 0.62rem | 700 / 500 | 1.4 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Publication card, profile photo | 8px |
| Nav bottom corners | 0 0 12px 12px |
| Interest tag, social button | 20px |
| Tooltip | 99px |
| Paper link button | 3px |
| Dots / avatars | 50% |

- **Shadows:** card `0 1px 4px rgba(26,54,93,0.05)`, card hover `0 4px 12px rgba(26,54,93,0.08)` with `translateY(-2px)`; keycap tags `0 3px 0 #ccdcec, 0 4px 8px rgba(0,0,0,0.06)`, pressed/active keycap `0 3px 0 #1a365d, 0 4px 8px rgba(0,0,0,0.15)`; photo `0 4px 16px rgba(0,0,0,0.15)`.
- **Layout max-width:** `.container` 1100px, padding `0.75rem 2rem 2rem`; a second wrapper at 1060px.
- **Card padding:** `0.85rem 1rem`, gap `0.7rem` between cards.

## Components

- **Sticky nav.** White, padding `0.85rem 2rem`, 2px `#2b6cb0` border with no top, 12px bottom radius, negative 1rem side margins so it overhangs the container.
- **Gradient affiliation.** `linear-gradient(135deg, #1a365d 0%, #2b6cb0 60%, #4299e1 100%)` clipped to text, 1rem weight 500.
- **Interest keycap.** Inline-flex pill, padding `0.32rem 0.8rem`, frost gradient, hard 3px `#ccdcec` drop.
- **Publication card.** White, 1px `#eef1f5` border, 8px radius, soft navy shadow, lift on hover. Title navy 600, venue `#2b6cb0` 500, award text red 700.
- **Paper link button.** `#3182ce` text, 1px `#3182ce` border, 3px radius, `0.15rem 0.5rem` padding, 0.8rem.
- **News badge.** Uppercase 0.62rem 700 label with a clipped-polygon slant; "upcoming" uses a gold gradient with `#5b4500` text.
- **Trophy.** SVG mask filled with `linear-gradient(135deg, #f6a800, #ffcc00, #ffe566)`, 1.7em square, left of each award.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | 160px square photo, script-font name, gradient affiliation |
| Interests | Yes | Keycap pills |
| News | Yes | Bold navy dates, slanted badges |
| Publication list | Yes, about 53 entries grouped by year | White cards, outlined link buttons (Paper, arXiv, Code, Data, HF) |
| Awards / grants | Yes | Trophy icon list; year and venue columns |
| Education & experience | Yes | Institution h3 with blue sub-headings |
| Talks / teaching / mentoring | Yes | Dated lists |
| Contact / social | Yes | Frost pill buttons |

## Do's and Don'ts

- Do anchor everything in the navy / blue ramp and keep gold for awards and year markers.
- Do give tags a tactile keycap edge rather than a blur shadow.
- Do keep publication cards light (1px border, near-invisible shadow) and lift them on hover.
- Don't use the script face beyond the name.
- Don't spread NVIDIA green beyond links and the employer word; it competes with navy.

## Surfaces

White page and white cards separated by `#eef1f5` borders; frost-blue gradients for pills; gold only as an accent fill.

## Imagery

One profile photo. Publications have no thumbnails. Icons are inline SVG masks (trophy) and emoji.

## Layout

Centered 1100px column: sticky nav, two-column header grid (`auto 1fr`, 2.5rem gap), then full-width stacked sections. Lists are flex rows with wrap.

## Agent Prompt Guide

**Quick colors:** text `#2d3748`, headings `#1a365d`, secondary `#2b6cb0`, link buttons `#3182ce`, gold `#ffcc00`, award red `#ff2600`, card border `#eef1f5`.

1. "Build a publication card: white, 1px `#eef1f5` border, 8px radius, shadow `0 1px 4px rgba(26,54,93,.05)`, navy 1rem/600 title, `#2b6cb0` venue, outlined 3px-radius link chips in `#3182ce`."
2. "Make interest tags as keycaps: 20px radius, gradient `#f5faff` to `#eef5fd`, shadow `0 3px 0 #ccdcec, 0 4px 8px rgba(0,0,0,.06)`, navy 0.88rem/500 text."
3. "Create a sticky nav: white, 2px `#2b6cb0` border on left, right and bottom only, 12px bottom radius, padding `0.85rem 2rem`."

## Similar Pages

Hand-rolled single-file academic sites with a Chakra / Tailwind-like navy palette; the Joshua Ren page in this batch uses a similar navy-plus-gold accent logic.

## Quick Start

```css
:root {
  --primary-color: #1a365d;
  --secondary-color: #2b6cb0;
  --accent-color: #3182ce;
  --text-color: #2d3748;
  --light-gray: #f7fafc;
  --border-color: #e2e8f0;
  --dark-gray: #4a5568;
  --yellow-color: #ffcc00;
  --orange-color: #ff5c00;
  --red-color: #ff2600;
  --font-body: 'Avenir Next', 'Segoe UI', Roboto, sans-serif;
  --font-name: 'Kaushan Script', cursive;
  --container: 1100px;
  --radius-card: 8px;
  --radius-pill: 20px;
}
```

## Provenance

- **URL:** https://liweijiang.github.io/
- **Person:** Liwei Jiang, NLP, LLM pluralism and safety
- **Venue / award:** NeurIPS 2025 Best Paper (Artificial Hivemind, first author)
- **Selection reason:** Rule B, first author of a NeurIPS 2025 Best Paper (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/).
- **Template credit:** none found; hand-written single HTML file with inline CSS and Google Fonts.
- **Measurement method:** `extract_style.py` parsed the inline style block; selectors were then read directly to assign roles. All hex values appear in the source. Font fallbacks (Avenir Next is not on Google Fonts) and rendered sizes were not checked in a browser.
