# Nagarajan Fell Type Study — Style Reference

> An antiquarian's study at night: letterpress serif on dark walnut, tan brass trim.

**Theme:** both

Measurements come from the static HTML of `/home/index.html` (the root URL is a meta refresh to it) and its stylesheets `/stylesheets/style.css` (66KB), `syntax.css` and `responsive.css`, plus Google Fonts and Font Awesome 6.5.1 / Academicons. The extractor's top text colors (`#f8f8f2`, `#e6db74`, `#ae81ff`, `#66d9ef`, `#f92672`) come from the Monokai `syntax.css` for blog code blocks and are excluded. Default theme is dark: the script reads `localStorage.getItem('theme') || 'dark'`. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Vaishnavh Nagarajan's page is a personal site set almost entirely in `IM Fell Great Primer`, a digitised 17th-century English roman, on a near-black brown ground `#1f1a12`. A right-aligned nav sits on a 1px white bottom rule, with his name pinned top-left as a Futura uppercase logo tracked 0.25em. A moon / sun button toggles to a parchment light theme (`#fdf5e6` ground, umber `#663925` highlights). The profile section pairs a photo column with an intro (Research Scientist, Google DeepMind; e-mail; pronouns; resume) and a row of icon links. Section headings ("research interests", "selected publications") switch to Futura small caps, lowercase, 0.16em tracking, 20px, in tan `#D2B48C` with a hairline under them. Papers are listed with an 800-weight Fell title, a grey conference line, and highlighted words in tan; three featured papers use `.paper-card` rows with a 240px thumbnail. Sketch images get a grayscale high-contrast "scanner" filter, inverted in dark mode.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Walnut Night | `#1f1a12` | `--background-color` (dark) | Default page background |
| Candle White | `#eeeeee` | `--text-color` (dark) | Body, headings, paper titles in dark mode |
| Brass Tan | `#D2B48C` | `--highlight-color` / `--hr-color` (dark) | Section headings, `.myhighlight`, rules, tooltip border |
| Ash Grey | `#cccccc` | `--conference-color` (dark) | Venue line |
| Nav Rule | `#ffffff` | `--nav-border-color` (dark) | Nav and heading underline |
| Terracotta Link | `#B86A50` | `--link-color` (both) | Links |
| Parchment | `#fdf5e6` | `--background-color` (light) | Light theme background |
| Iron Gall | `#303030` | `--text-color` (light) | Light theme body |
| Umber | `#663925` | `--highlight-color` (light) | Light theme headings, rules, highlights |
| Press Black | `#000000` | `--papertitle-color` (light) | Light theme paper titles |
| Venue Grey | `#636363` | `--conference-color` (light) | Light theme venue line |
| Heading Grey | `#444444` | `--heading-color` (light) | Light theme paragraphs and headings |
| Blockquote Dusk | `#252525` | `--blockquote-background` (dark) | Quote blocks |
| Strong Cream | `#ffffee` | `--em-strong-bg` | Emphasised strong background |

## Tokens — Typography

- **Body and titles:** `IM Fell Great Primer`, "OfflineAcademic", serif (Google Fonts). Substitute: `EB Garamond` (also loaded) or `IM Fell English`.
- **Headings and logo:** `Futura`, "Helvetica Neue", sans-serif (system font, not loaded). Substitute: `Jost` (loaded in one of the font requests) or `Century Gothic`.
- **Loaded but decorative or unused on home:** Instrument Serif, Pacifico, Roboto Slab, Ewert, Fredericka the Great, Jacques Francois Shadow, IM Fell SC variants, Libre Caslon Text.
- **Weights:** 400 body, 800 paper titles, 400 Futura headings.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Logo (name) | 20px (16px mobile) | 400 | Futura, uppercase, 0.25em tracking |
| Section heading `.subheading` | 20px | 400 | Futura, small caps, lowercase, 0.16em tracking |
| Main page text `--main-page-fontsize` | 18px | 400 | Fell |
| Paper title `.papertitle` | 18px | 800 | Fell |
| Venue `.conference` | 18px | 400 | Fell, grey |
| Highlight `.myhighlight` | 18px | 700 | Fell, tan / umber |
| Blog name | 24px italic | 800 | Fell |
| Base body | 14px / 20px | 400 | Fell |
| Blog body `--dynamic-font-size` | 17px (user adjustable) | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Paper thumbnail | 4px |
| Small UI (buttons, code) | 3px |
| Sketch frame image | 0 |
| Pill toggles | 42px |

- **Shadows:** thumbnails `0 2px 4px rgba(0,0,0,.05)`; floating controls `0 2px 8px rgba(0,0,0,.2)` and `0 4px 8px rgba(0,0,0,.2)`.
- **Layout max-width:** content up to 1200px; text blocks at 600px; profile image max 200px on mobile.
- **Paper card:** flex, 25px gap, 40px bottom margin, thumbnail column fixed at 240px; stacks under the mobile breakpoint with 10px gap.
- **Heading rhythm:** `.subheading` margin 3rem top, 1.5rem bottom, 8px padding above a 1px rule.

## Components

- **Nav bar.** Full-width flex, right-aligned links (`.link`, padding 15px 0, margin 2px 25px, no underline), 1px bottom rule in `--nav-border-color`, absolute-positioned Futura logo at top-left; column layout on mobile.
- **Theme toggle.** Font Awesome moon / sun icon button, stores choice in `localStorage`, also resets the Disqus thread theme.
- **Section heading.** Futura small caps, tan or umber, hairline below.
- **Paper entry.** Fell 800 title in candle white or black, venue line in grey, author highlights in tan / umber 700.
- **Paper card.** 240px thumbnail with 1px faint border and 4px radius beside the text block.
- **Sketch frame.** Image in a 1px highlight-color border, filtered `grayscale(1) contrast(1.8) brightness(1.1)`, plus `invert(0.9)` in dark mode.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | Photo column, intro text, icon row (Twitter, Scholar, Semantic Scholar, LinkedIn) |
| Research interests | Yes | Prose with highlighted phrases |
| Publication list with thumbnails | Yes, 17 titles; 3 featured cards with thumbnails | Fell titles, grey venues |
| Talks / blog | Separate pages in nav | |
| News | No | |
| Awards | Mentioned in prose (ICML 2025 Outstanding Paper, NeurIPS 2019 Outstanding New Directions) | |
| Contact | E-mail in intro | |
| Dark mode toggle | Yes, dark by default | |

## Do's and Don'ts

- Do set all reading text in IM Fell and all structural labels in a geometric sans with wide tracking.
- Do keep dark mode as the default and make the light mode parchment, not white.
- Do use one warm accent family (tan / umber) for headings and highlights, terracotta for links.
- Don't load the Monokai code colors into page chrome; they belong to blog code blocks only.
- Don't round sketch images; the scanner look depends on hard edges.

## Surfaces

Dark: walnut `#1f1a12` page, `#252525` quotes, `#202020` code. Light: parchment `#fdf5e6`, `#f9f9f9` quotes, `#39382e` code.

## Imagery

One portrait, three paper thumbnails, and sketch-style illustrations processed to monochrome with CSS filters.

## Layout

Single column under a full-width nav; the profile section is a two-column flex (image, text) that centers and stacks on mobile. Floating font-size controls appear on blog pages.

## Agent Prompt Guide

**Quick colors:** dark bg `#1f1a12`, dark text `#eeeeee`, tan `#D2B48C`, link `#B86A50`; light bg `#fdf5e6`, light text `#303030`, umber `#663925`.

1. "Write a section heading in Futura 20px weight 400, small caps, lowercase, 0.16em letter-spacing, color `#D2B48C`, 3rem above, with a 1px rule 8px below."
2. "List a paper: IM Fell Great Primer 18px weight 800 title in `#eee`, venue line 18px in `#ccc`, and the author's name highlighted 700 in `#D2B48C`, on `#1f1a12`."
3. "Add a theme toggle that swaps to a parchment light mode: bg `#fdf5e6`, text `#303030`, highlights `#663925`, links stay `#B86A50`."

## Similar Pages

Personal sites with period typography; the Junyang Lin page in this batch shares the serif-led editorial approach in a bright register.

## Quick Start

```css
:root {
  --background-color: #1f1a12;
  --text-color: #eee;
  --highlight-color: #D2B48C;
  --link-color: #B86A50;
  --conference-color: #ccc;
  --nav-border-color: #ffffff;
  --main-page-fontsize: 18px;
  --font-body: "IM Fell Great Primer", "EB Garamond", serif;
  --font-label: Futura, "Jost", "Helvetica Neue", sans-serif;
}
[data-theme="light"] {
  --background-color: #fdf5e6;
  --text-color: #303030;
  --highlight-color: #663925;
  --conference-color: #636363;
  --nav-border-color: black;
}
```

## Provenance

- **URL:** https://vaishnavh.github.io/ (meta refresh to https://vaishnavh.github.io/home/index.html)
- **Person:** Vaishnavh Nagarajan, deep learning theory
- **Venue / award:** ICML 2025 Outstanding Paper (Roll the dice & look before you leap, first author)
- **Selection reason:** Rule B, first author of an ICML 2025 Outstanding Paper (https://icml.cc/virtual/2025/awards_detail).
- **Template credit:** none credited; custom stylesheet (comments in `style.css` are personal notes). The original Jekyll-era structure (`stylesheets/syntax.css`, `responsive.css`) suggests a forked minimal theme (inferred).
- **Measurement method:** the root returned only a meta refresh, so `extract_style.py` was rerun on `/home/index.html`; `style.css` was fetched and its `:root` and `[data-theme="light"]` blocks read directly. Futura availability and the rendered default theme were not checked in a browser.
