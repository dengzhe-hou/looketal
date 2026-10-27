# Bengio · Aurora Mist Editorial — Style Reference

> A think-tank homepage under a teal and lime morning haze.

**Theme:** light

Measurements are normalized from the page HTML and its aggregated Drupal theme CSS (`yoshuabengio_v1`); roles are interpreted from markup and one rendered viewport. Drupal admin-toolbar variables (`--manager-*`) in the scan belong to the CMS back end and are excluded.

## Overview

Yoshua Bengio's site is a professionally built Drupal theme, closer to a policy institute than a lab page. The page sits on a warm grey `#E6E6E2`; the hero is a large serif statement ("A.M. Turing Award Recipient and most-cited AI researcher") in FlechaBronzeaM, dark teal `#0B404D`, regular weight, floating over a soft aurora wash of cyan and lime. Navigation is minimal: name wordmark left, three uppercase links right (Research, Blog, FR). Below, news and blog posts run in a Swiper carousel of cards, two YouTube embeds feature talks, and a contact footer lists media inquiries and Mila's address. Links are teal `#2393A7` with a 1px underline drawn as a border.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Fog Linen | `#e6e6e2` | `--bg` | Body background |
| Chalk | `#f2f2f0` | `--surface` | Main buttons, light panels |
| White | `#ffffff` | `--card` | Message panels, cards |
| Abyss Teal | `#0b404d` | `--heading` | Serif headings; green-theme button fill |
| Lagoon Link | `#2393a7` | `--link` | Content links and their underline, pill outlines |
| Glacier Cyan | `#3eb9c6` | `--grad-a` | Button hover gradient start, aurora tone |
| Spring Lime | `#cbe18b` | `--grad-b` | Button hover gradient end, aurora tone |
| Ink | `#000000` | `--text` | Body text, nav |
| Charcoal | `#333333` | `--text-soft` | Secondary text |

## Tokens — Typography

- **Display:** FlechaBronzeaM (self-hosted woff2; substitute: a narrow high-contrast serif such as Newsreader or Fraunces at 400) for h1–h5, weight normal, line-height 1.1.
- **Body/UI:** Funnel Sans (self-hosted, Light to ExtraBold, italic; substitute: Inter or Funnel Sans from Google Fonts).

| Role | Size | Weight | Line height |
|---|---|---|---|
| Hero statement | 70–100px (full-view node headers) | 400 | 1.1 |
| Section heading | 30px | 400 | 1.1 |
| Card title | 22–24px | 500–600 | 1.15 |
| Body | 18px (most common) | 400 | normal |
| Nav, labels | 14px uppercase | 500 | 1 |
| Load-more pill | 18px uppercase | 500 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Main button | 0 (square) |
| Load-more pill | 9999px |
| Message panel | 25px |
| Avatar / round icons | 100% |
| Spinner | 100% |

Main button padding 20px 40px; load-more padding 10px 35px. Shadows are rare: one `0 0 15px 5px rgba(0,0,0,.1)`. Content max width 1585px; text blocks narrower (500px, 60%). Page top padding 160px under a fixed header (`scroll-padding-top:130px`).

## Components

- **Header:** wordmark "Yoshua Bengio" in serif at left, uppercase sans links at right, transparent over the hero.
- **Hero statement:** multi-line serif headline in `#0B404D` on the aurora wash, left-offset.
- **Main button:** square, `#f2f2f0` fill, black text; hover fades in a `-90deg` gradient `#3eb9c6 → #cbe18b`. Green variant: `#0B404D` fill, `#f2f2f0` text.
- **Load-more pill:** transparent, 1px `#2393A7` border, 9999px radius, uppercase 18px.
- **News card carousel:** Swiper slides with image, headline and source link.
- **Video embeds:** two YouTube iframes (talks).
- **Contact footer:** media inquiries address, assistant contact, Mila postal address, social links (LinkedIn, X, Bluesky).

## Page Modules

- **Bio/photo:** short positioning statement in the hero; full bio on linked pages.
- **News:** carousel of press and blog items (FT, TIME, UN Security Council speech, International AI Safety Report).
- **Publication list:** not on the home page; under "Research".
- **Awards:** Turing Award stated in the hero headline.
- **Talks:** embedded YouTube videos.
- **Contact:** structured footer with media and office contacts.
- **Language switch:** EN / FR toggle in the nav.

## Do's and Don'ts

- Do set every heading in the serif at regular weight and dark teal.
- Do keep the background warm grey, not white.
- Don't round the main buttons; only the load-more control is a pill.
- Don't use the lime and cyan as flat fills; they appear as gradients and haze.

## Surfaces

Warm grey page, chalk panels, white message cards, and the aurora hero as the only atmospheric layer.

## Imagery

Abstract gradient haze in the hero, editorial press photos in cards, video thumbnails. No paper figures on the home page.

## Layout

Wide (up to 1585px) editorial grid, fixed header, large hero, horizontal carousel rows.

## Agent Prompt Guide

Quick colors: bg `#e6e6e2`, surface `#f2f2f0`, heading `#0b404d`, link `#2393a7`, gradient `#3eb9c6 → #cbe18b`, text `#000000`.

1. "Build a hero statement: serif (FlechaBronzeaM or Fraunces 400) at 70px/1.1 in `#0b404d` over a blurred radial wash of `#3eb9c6` and `#cbe18b` on `#e6e6e2`."
2. "Build a main button: square corners, padding 20px 40px, `#f2f2f0` fill, black Funnel Sans text; on hover fade in `linear-gradient(-90deg,#3eb9c6,#cbe18b)`."
3. "Build a load-more pill: transparent, 1px solid `#2393a7`, radius 9999px, padding 10px 35px, uppercase 18px weight 500."

## Similar Pages

Institute and foundation sites (Mila, LawZero) rather than academic templates.

## Quick Start

```css
:root {
  --bg: #e6e6e2; --surface: #f2f2f0; --card: #ffffff;
  --heading: #0b404d; --link: #2393a7; --text: #000000;
  --grad: linear-gradient(-90deg, #3eb9c6, #cbe18b);
  --radius-pill: 9999px; --radius-panel: 25px;
  --font-display: 'FlechaBronzeaM', 'Fraunces', serif;
  --font-body: 'Funnel Sans', 'Inter', sans-serif;
  --max-width: 1585px;
}
```

## Provenance

- **URL:** https://yoshuabengio.org/en
- **Person:** Yoshua Bengio, deep learning.
- **Award:** ACM A.M. Turing Award 2018.
- **Selection reason:** Rule A, Turing Award 2018 laureate (awards.acm.org/turing); personal domain.
- **Template credit:** custom Drupal theme `yoshuabengio_v1`; no designer credit found in the footer.
- **Measurement method:** extract_style.py scan plus targeted reading of the aggregated theme CSS (about 263 KB) for body, heading, link and button rules, and one rendered viewport. A cookie-consent banner covered part of the first viewport; it was not interacted with. The aurora wash is described from the render; its source (image or CSS) was not traced.
