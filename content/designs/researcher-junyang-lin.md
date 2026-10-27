# Junyang Lin Linen Essay — Style Reference

> A quiet literary quarterly printed on warm linen, with one teal ribbon marker.

**Theme:** light

Measurements come from the static HTML and its single custom stylesheet `/assets/css/site.css` (11.5KB), plus Font Awesome for icons. All colors are declared by the author as `:root` variables or literals; there is no CSS framework to filter. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Junyang Lin's home page reads like an editorial site rather than a CV. A sticky translucent linen header (`rgba(247,245,240,0.92)` with a 10px backdrop blur) carries a Cormorant Garamond wordmark and small uppercase tracked nav links (About, Research, Selected Work, Writing, Contact). The hero is a two-column grid: a 12rem portrait in a 4:5 frame with 0.5rem radius, then a large serif name (`clamp(2.8rem … 4.1rem)`), a muted eyebrow ("Independent researcher"), a 1.1rem lead, and three pill buttons, the first filled deep teal. Sections below each open with a teal uppercase kicker and a serif h2: About (a statement column), Research (three numbered theme cards asking questions), Selected work (a two-column grid of six papers: Qwen3, Qwen3-VL, Qwen3-Coder, GSPO, Gated Attention, Qwen-Image), Writing, and Contact with pill social links. Separation is done with hairline top borders, not boxes or shadows.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Linen | `#f7f5f0` | `--bg` | Page background; header at 92% alpha |
| Paper | `#ffffff` | `--surface` | Mobile nav panel and summary button |
| Press Black | `#171717` | `--text` | Headings and strong copy |
| Graphite | `#5f5f5f` | `--muted` | Body copy, lead, nav links, meta |
| Hairline Sand | `#e7e2d8` | `--line` | Header and footer borders, link pill borders |
| Seam Sand | `#d8d1c3` | `--line-strong` | Card top rules, secondary button border |
| Deep Teal | `#1d5c63` | `--accent` | Primary button, kickers, text links, hovers |
| Teal Shade | `#174c51` | (literal) | Primary button hover |
| Teal Wash | `#eef5f5` | `--accent-soft` | Tag pill background |
| Frame Oat | `#eae5db` | (literal) | Portrait frame background |
| Code Oat | `#f0ece3` | (literal) | Inline code background (writing pages) |
| Night Slate | `#1f2328` | (literal) | `pre` background; text `#f7f4ee` |

## Tokens — Typography

- **Display:** `Cormorant Garamond`, Georgia, serif, weights 600 (headings) and 700 available. Google Fonts.
- **Body / UI:** `Source Sans 3`, -apple-system, BlinkMacSystemFont, sans-serif, weights 400 to 700. Google Fonts.
- **Mono:** `SFMono-Regular`, Consolas, `Liberation Mono`, Menlo, monospace.
- **Body rhythm:** line-height 1.7, letter-spacing 0.01em; articles at 1.1rem / 1.85.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Hero name | `clamp(2.8rem, 2.1rem + 1.8vw, 4.1rem)` | 600 | Serif, line-height 1.05 |
| Brand wordmark | `clamp(2rem, 1.7rem + 0.9vw, 2.5rem)` | 600 | Serif, 0.02em tracking |
| Section h2 | `clamp(2rem, 1.6rem + 1vw, 2.6rem)` | 600 | Serif |
| Featured writing h3 | 2.4rem | 600 | Serif |
| Theme / work card h3 | 1.9rem | 600 | Serif |
| Lead | 1.1rem | 400 | Muted, max 42rem |
| Button | 0.95rem | 700 | Sans |
| Meta line | 0.9rem | 600 | Muted |
| Tag | 0.88rem | 600 | Teal on teal wash |
| Nav link | 0.84rem | 700 | Uppercase, 0.12em tracking |
| Kicker | 0.8rem | 700 | Uppercase, 0.14em tracking, teal |
| Meta label `dt` | 0.78rem | 700 | Uppercase, 0.12em |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, link pills, tags, mobile menu button | 999px |
| Portrait frame | 0.5rem |
| `pre` | 0.6rem |
| Inline code | 0.2rem |

- **Shadows:** only the mobile nav panel, `0 12px 28px rgba(20,20,20,0.08)`.
- **Layout max-width:** `--max-width: 68rem`; the home page shell widens to 72rem; copy column `--copy-width: 42rem`; hero content 40rem; articles 46rem.
- **Section rhythm:** `.content-section` margin-top 4rem; main padding `2.5rem 0 4rem`; footer margin-top 5rem.
- **Header height:** 4.75rem, also used for `scroll-margin-top`.

## Components

- **Primary button.** Pill, min-height 2.75rem, padding `0.7rem 1rem`, `#1d5c63` fill and border, white 0.95rem/700 text, hover `#174c51`.
- **Secondary / ghost button.** Transparent, `#d8d1c3` border, `#171717` text; hover turns border and text teal.
- **Theme card.** No box: a 1px `#d8d1c3` top rule, 1rem top padding, a teal tracked index number, serif 1.9rem question title, muted paragraph. Three across, one column under 980px.
- **Work card.** Same top-rule treatment, meta line, serif title, summary, and a row of outlined pill links (min-height 2.5rem, 1px `#e7e2d8`, teal on hover).
- **Section kicker.** Teal uppercase 0.8rem label above each serif h2.
- **Sticky header.** Linen at 92% alpha with blur, 1px bottom hairline; collapses to a `<details>` hamburger under 760px.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | 4:5 portrait, serif name, lead, three pill CTAs |
| Research themes | Yes, three questions | Numbered top-rule cards |
| Publication list | Selected work, six entries | Two-column top-rule cards with pill links (Paper / arXiv / Code) |
| Writing | Yes | Featured writing block, link to blog |
| News | No | |
| Awards | No | |
| Contact | Yes | Pill social links (GitHub, X, LinkedIn, Scholar, e-mail) |

## Do's and Don'ts

- Do pair a large Cormorant Garamond heading with small tracked uppercase sans labels.
- Do separate content with 1px sand top rules instead of cards or shadows.
- Do reserve the teal for one filled button, kickers and links.
- Don't use pure white as the page background; the warmth of `#f7f5f0` carries the look.
- Don't add publication thumbnails or badges; the page is text-led.

## Surfaces

Linen page, white only for the mobile menu, oat for the portrait frame and inline code, dark slate for code blocks.

## Imagery

One portrait, cropped 4:5 with `object-fit: cover`. Icons are Font Awesome and inline SVG at 16px.

## Layout

Centered 72rem shell. Hero grid `12rem 1fr` with 2rem gap (10rem under 980px, stacked under 760px). Theme grid three columns, work grid two columns, both single column under 980px. Buttons go full width under 560px.

## Agent Prompt Guide

**Quick colors:** bg `#f7f5f0`, text `#171717`, muted `#5f5f5f`, line `#e7e2d8`, strong line `#d8d1c3`, accent `#1d5c63`, accent soft `#eef5f5`.

1. "Create a hero: 12rem 4:5 portrait with 0.5rem radius on `#eae5db`, then a Cormorant Garamond 600 name at `clamp(2.8rem,2.1rem+1.8vw,4.1rem)`, a 1.1rem muted lead, and a filled `#1d5c63` pill button beside two outlined pills."
2. "Build three research theme cards with no background: 1px `#d8d1c3` top border, teal tracked index '01', serif 1.9rem question title, muted body."
3. "Add a section kicker: 0.8rem Source Sans 3 weight 700, uppercase, 0.14em tracking, color `#1d5c63`, 0.75rem above a serif h2."

## Similar Pages

Editorial personal sites built on hand-written CSS with a serif display face (for example Stripe Press-like typography). The Vaishnavh Nagarajan page in this batch also leans on serif display type but in a darker, antique register.

## Quick Start

```css
:root {
  --bg: #f7f5f0;
  --surface: #ffffff;
  --text: #171717;
  --muted: #5f5f5f;
  --line: #e7e2d8;
  --line-strong: #d8d1c3;
  --accent: #1d5c63;
  --accent-soft: #eef5f5;
  --max-width: 68rem;
  --copy-width: 42rem;
  --header-height: 4.75rem;
  --font-display: "Cormorant Garamond", Georgia, serif;
  --font-body: "Source Sans 3", -apple-system, sans-serif;
  --radius-pill: 999px;
}
```

## Provenance

- **URL:** https://justinlin610.github.io/
- **Person:** Junyang Lin, large language models (Qwen)
- **Venue / award:** NeurIPS 2025 Best Paper (Gated Attention for LLMs, last author)
- **Selection reason:** Rule B, last author of a NeurIPS 2025 Best Paper (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/); homepage taken from his GitHub profile link.
- **Template credit:** none credited; custom `site.css` with BEM-style class names. Footer reads only the copyright line.
- **Measurement method:** `extract_style.py` on HTML plus `site.css`, then the stylesheet was read in full to assign roles and breakpoints. All hex values are from the source. Rendered font loading and actual clamp outputs were not checked in a browser.
