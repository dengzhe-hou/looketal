# Snell Astro Bulma — Style Reference

> A Bulma 1.0 faculty card catalogue that dims itself when the room goes dark.

**Theme:** both

Measurements come from the static HTML and its single Astro-built stylesheet `/_astro/biography.jjZd2DSW.css` (698KB: the full Bulma 1.x build, Font Awesome, Academicons, and about 2KB of custom rules at the end). Bulma's palette variables (primary turquoise `hsl(171,100%,41%)`, info, success, warning, danger) are declared but unused by this page and are excluded. Bulma 1.x ships `prefers-color-scheme: dark` overrides, so the page follows the system theme with no toggle. Hex values for Bulma's HSL tokens are computed where noted. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Jake Snell's site is an Astro static build on stock Bulma 1.x. A transparent navbar (`.navbar{background:none}`) with 1.25rem items (About, Biography, Publications, Contact) sits over a two-column layout: a sticky left sidebar (`position: sticky; top: 48px`) in a `column is-4` with a 250x313 portrait at 12px radius, the name as `title` and three `subtitle` lines (Associate Research Scholar, Department of Computer Science, Princeton University), and a `column is-8` main area. The main area has About (with a bold "Incoming Assistant Professor, University of Cambridge" line), Research Interests (three numbered bold themes: Robustness, Reliability, Transparency), News, and Selected Publications. Each publication is a `columns is-mobile` row: a `column is-3` thumbnail and a flattened Bulma card (radius 0, no shadow, no padding) with a 1.25rem title, 1.25rem author subtitle, venue line, and icon-only PDF / Code / arXiv links that reveal a dark tooltip on hover.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Scheme White | `hsl(221,14%,100%)` = `#ffffff` | `--bulma-scheme-main` | Page background (light) |
| Scheme Night | `hsl(221,14%,9%)` (computed about `#14161a`) | `--bulma-scheme-main` (dark) | Page background under `prefers-color-scheme: dark` |
| Slate Text | `hsl(221,14%,29%)` (computed about `#404654`) | `--bulma-text` | Body text (light) |
| Slate Strong | `hsl(221,14%,21%)` (computed about `#2e333d`) | `--bulma-text-strong` | Titles (light) |
| Slate Weak | `hsl(221,14%,48%)` | `--bulma-text-weak` | Muted text |
| Mist Text | `hsl(221,14%,71%)` | `--bulma-text` (dark) | Body text in dark scheme |
| Link Blue | `rgb(46,103,211)` = `#2e67d3` | `--bulma-link` (`219deg 65% 50%`) | Links, icon links |
| Link On Scheme | `hsl(219,65%,40.4%)` / `60.4%` dark | `--bulma-link-text` | Link text tuned to scheme |
| Tooltip Graphite | `#363636` | (custom) | Tooltip background; arrow `#555` |
| Preprint Orange | `#F98506` | `.publication .box.preprint` | Declared venue box color |
| Conference Violet | `#3500ff` | `.publication .box.conference` | Declared venue box color |
| Journal Red | `#FF0000` | `.publication .box.journal` | Declared venue box color |
| Thesis Yellow | `#ffe40e` | `.publication .box.thesis` | Declared venue box color |

The four venue box colors are in the custom CSS but no `.box` element appears in the current home-page HTML, so they are dormant here.

## Tokens — Typography

- **Family:** `Inter, SF Pro, Segoe UI, Roboto, Oxygen, Ubuntu, Helvetica Neue, Helvetica, Arial, sans-serif` (`--bulma-family-primary`). Inter is not loaded as a web font, so it renders only if installed (inferred). Substitute: `Inter` via Google Fonts.
- **Mono:** `Inconsolata, Hack, SF Mono, Roboto Mono, Source Code Pro, Ubuntu Mono, monospace`.
- **Weights:** 400 body and subtitles, 800 titles (`--bulma-title-weight: extrabold`), 600 semibold available.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Name `title` | 2rem (`--bulma-size-3`) | 800 | 1.125 (Bulma) |
| Section title (About, News) | 2rem | 800 | 1.125 |
| Sidebar subtitle lines | 1.25rem | 400 | 1.25 |
| Publication title | 1.25rem (`size-5`) | 800 | 1.125 |
| Publication authors / venue | 1.25rem (`is-size-5`) | 400 | 1.5 |
| Navbar item | 1.25rem | 400 | 1.5 |
| Body | 1em | 400 | 1.5 |
| Tooltip | inherit | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Portrait | 12px |
| Bulma default control | .375rem |
| Bulma card (default) / publication card | .75rem / 0 |
| Tooltip | 6px |
| Rounded controls | 9999px |

- **Shadows:** none on content; publication cards override `--bulma-card-shadow: 0 0 0 0`. Bulma's default card shadow `0 .5em 1em -.125em hsla(...,.1), 0 0 0 1px hsla(...,.02)` is unused.
- **Layout max-width:** Bulma `.container` (1152px at widescreen, 1344px at fullhd, both in the CSS).
- **Section padding:** `section.main-content` padding 0 0 1.5rem; paragraphs margin-bottom .75rem; publication rows mb-4.
- **Sidebar:** sticky at 48px from the top.

## Components

- **Sidebar portrait.** 250x313, `border-radius: 12px`, centered above the title block.
- **Publication row.** `columns is-mobile`: `column is-3` WebP thumbnail (explicit width/height), `column` with a flat card.
- **Icon link with tooltip.** Font Awesome `fa-file-pdf`, `fa-code` or Academicons `ai-arxiv` at `fa-lg`; hover shows an 80px `#363636` tooltip with white text, 6px radius, fading in over .3s, with a 5px arrow.
- **Supplement link.** Plain text link with `ml-3` after the icons.
- **Navbar.** Bulma navbar with background removed and a burger toggle script for mobile.
- **Links.** Underline on hover (`a:hover{text-decoration:underline}`), except navbar and icons.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | Sticky sidebar portrait, title, subtitles |
| Research interests | Yes | Numbered bold themes with explanations |
| News | Yes | Dated lines ("Mar 2026: ...") |
| Publication list with thumbnails | Yes, six selected | Thumbnail plus flat card, icon links (PDF, Code, arXiv) |
| Biography / full publications / contact | Separate pages | Navbar |
| Awards | No section | |
| Dark mode | Automatic via Bulma `prefers-color-scheme` | No toggle |

## Do's and Don'ts

- Do keep Bulma's slate scheme and use only the link blue as an accent.
- Do flatten cards in lists (radius 0, no shadow, no padding) so rows read as text.
- Do keep the sidebar sticky so the name stays visible while scrolling papers.
- Don't apply Bulma's turquoise primary anywhere; it is never referenced.
- Don't replace icon links with text buttons; the tooltip pattern is part of the look.

## Surfaces

One surface: the scheme background (white or near-black). The tooltip is the only filled element.

## Imagery

Portrait and six publication thumbnails (600 to 711px wide sources, about 4:3 to 16:9) in WebP with lazy loading.

## Layout

Bulma container with `columns`: sidebar `is-4`, main `is-8`; publications as nested `is-mobile` columns so thumbnails stay beside text on phones. Navbar collapses to a burger.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff` (dark `hsl(221,14%,9%)`), text `hsl(221,14%,29%)`, strong `hsl(221,14%,21%)`, link `#2e67d3`, tooltip `#363636`.

1. "Build a sticky left sidebar (top 48px) with a 250x313 portrait at 12px radius, a 2rem weight-800 name, and three 1.25rem subtitle lines in Bulma slate."
2. "Make a publication row: 25% thumbnail column, then a flat text block with a 1.25rem/800 title, a 1.25rem/400 author line, venue, and icon links that show a `#363636` tooltip on hover."
3. "Use Bulma 1.x defaults so the page follows `prefers-color-scheme`, with the link hue at 219deg 65% 50%."

## Similar Pages

Bulma-based academic pages; most in this collection are Nerfies project pages on Bulma 0.9, whereas this is Bulma 1.x with automatic dark mode. The Aditi Raghunathan page shares the venue-color tag idea.

## Quick Start

```css
:root {
  --bulma-scheme-h: 221;
  --bulma-scheme-s: 14%;
  --bulma-text-l: 29%;
  --bulma-text-strong-l: 21%;
  --bulma-link-h: 219deg;
  --bulma-link-s: 65%;
  --bulma-link-l: 50%;
  --bulma-family-primary: Inter, "SF Pro", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --bulma-radius: .375rem;
  --portrait-radius: 12px;
  --tooltip-bg: #363636;
}
.publication .card { --bulma-card-radius: 0; --bulma-card-shadow: 0 0 0 0; --bulma-card-content-padding: 0; }
```

## Provenance

- **URL:** https://jakesnell.com/
- **Person:** Jake C. Snell, uncertainty quantification and Bayesian ML
- **Venue / award:** ICML 2025 Outstanding Paper (Conformal Prediction as Bayesian Quadrature, first author)
- **Selection reason:** Rule B, first author of an ICML 2025 Outstanding Paper (https://icml.cc/virtual/2025/awards_detail); homepage from his GitHub profile link.
- **Template credit:** none credited; Astro static site (`/_astro/` hashed assets) on Bulma 1.x with Font Awesome and Academicons.
- **Measurement method:** `extract_style.py` returned mostly Bulma variable references, so the stylesheet was read for Bulma's scheme, text and link variables and the custom rules at its end. Hex equivalents of HSL tokens marked "computed" are my conversions. Whether Inter renders and how dark mode looks were not checked in a browser.
