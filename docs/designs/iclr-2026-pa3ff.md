# PA3FF Terracotta Editorial — Style Reference

> A design-annual spread on warm paper: Fraunces headlines, rust italics, and a faded robot drifting behind the masthead.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, and the page's own inline `<style>` block (about 800 lines, with CSS custom properties), layered over a local Bulma build. The authors' variables are reported where the render confirms them. Color share is measured on the first 1440×900 viewport.

## Overview

A custom editorial theme on top of Bulma. The page background is warm paper #faf8f3 with a 22px dot grid and a faint noise grain. A frosted pill navigation floats at the top in lowercase IBM Plex Mono. The hero is left aligned: a mono uppercase meta line with a pulsing rust dot ("PA3FF — PART-AWARE 3D FEATURE FIELD — ICLR 2026"), then a 70.4px Fraunces headline at light weight 380 with the second half in rust #c2410c italics, authors in Plex Sans with rust superscripts, mono affiliations, a black "Accepted to ICLR 2026" pill with a green dot, and three square mono buttons (one solid ink, two ghost). A greyed photo of the robot fills the right half of the hero and fades into the paper. Each section has a two-column layout: a mono "§ 01 ABSTRACT" marker in the left quarter, and on the right a 48px Fraunces headline sentence with a rust italic phrase, then prose, figure plates with mono labels, numbered contribution lists, hairline-grid metric cards, and black insight boxes with amber kickers. Sections alternate between paper and a tinted #f3efe6 band; the footer is a solid ink colophon.

## First Viewport

Color share (1440×900, 8-color quantize): the screen is almost all warm neutrals: #eeece7 35.8%, #d8d4cf 18.4%, #dddbd7 13.1%, #eae8e3 11.4%, #e4e1dd 10.5%, #f0efea 5.4% (paper plus the faded robot photo on the right), and a warm taupe #ac9c94 5.2% from the photo's wood tones. Ink type and rust italics are each under 1% by area, yet they carry the screen.

Anatomy in DOM order (Bulma `container is-max-desktop`, 960px, x=240):

1. **Floating nav** — `nav.navbar-float`, fixed 20px from the top, centred, 551×51, rgba(250,248,243,0.82) with 14px backdrop blur, 1px rgba(15,17,21,0.08) border, 9999px radius, soft shadow. Links: IBM Plex Mono 13.12px / 500, lowercase, #4a4d55, padding 8px 15.2px, pill hover rgba(15,17,21,0.06); "code" and "paper" carry small icons.
2. **Meta line** — `.hero-meta` at y=176: 6px #c2410c dot with a pulsing ring, "PA3FF — PART-AWARE 3D FEATURE FIELD" in Plex Mono 11.52px / 400, letter-spacing 0.12em, uppercase, #4a4d55; a 40px #e3dccd rule; "ICLR 2026". Margin-bottom 28px.
3. **Headline** — `h1.publication-title`, Fraunces 70.4px / 380 / line-height 1.02, letter-spacing -0.025em, #0f1115, max-width 18ch (743px), left aligned, four lines (y=223–510); "Generalizable Articulated Object Manipulation" in `<em>`: italic, weight 360, #c2410c. Margin-bottom 28px.
4. **Authors** — `.publication-authors`, Plex Sans 16px / 400 / 1.75, #0f1115; first three names bold 600; superscripts 600 #c2410c; wraps at 44rem.
5. **Affiliations** — `.author-affil`, Plex Mono 11.52px, letter-spacing 0.06em, #4a4d55, rust superscripts, separated by middots.
6. **Notes** — `.author-note`, Plex Mono 10.88px uppercase, letter-spacing 0.08em, #7c7f87: "* Equal contribution · † Corresponding author".
7. **Venue pill** — `.venue-badge` at y≈740: #0f1115 fill, #faf8f3 Plex Mono 12.48px text, padding 0.45rem 0.9rem, 999px radius, 6px #22c55e dot. Gap 36px.
8. **Buttons** — `.publication-links` (gap 0.6rem) at y=807: "READ PAPER →" solid #0f1115 with #faf8f3 text; "VIEW CODE" and "WATCH DEMO" ghost (transparent, #0f1115 text); all Plex Mono 12.48px / 500 uppercase, letter-spacing 0.06em, height 2.6rem (42px), padding 0 20px, 1px #0f1115 border, square corners.
9. **Hero photo** — `.hero-face`, absolute right 52% of the hero, robot photo at 0.55 opacity, grayscale 0.15, faded by a left-to-right paper gradient. Hero bottom at y=978 with a 1px #e3dccd rule.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #faf8f3 | `--paper` | page background, hero, button text on ink, nav glass tint |
| Paper Tint | #f3efe6 | `--paper-tint` | alternate section bands (§ 02, § 05, § 07), callout fill, tag fill |
| Ink | #0f1115 | `--ink` | headlines, body text, solid button, venue pill, insight boxes, footer |
| Muted | #4a4d55 | `--text-muted` | nav links, meta line, affiliations, section markers, pillar text |
| Light | #7c7f87 | `--text-light` | author notes, figure-plate labels |
| Terracotta | #c2410c | `--primary` | italic headline phrases, links, superscripts, § numbers, figure labels, list numerals, button hover fill |
| Terracotta Dark | #9a330a | `--primary-dark` | link hover, accent metric card hover |
| Rule Soft | #e3dccd | `--rule-soft` | hairlines, hero bottom border, grid gaps, figure-plate border, meta rule |
| Rule | #2a2d33 | `--rule` | footer top border |
| Surface | #ffffff | `--bg-surface` | figure plates, metric cards, pillars, video cards |
| Amber | #fbbf24 | (literal) | insight-box kicker, bold numbers in insights and the positive compare column |
| Live Green | #22c55e | (literal) | dot in the venue pill |
| Teal | #0f766e | `--secondary` | secondary tag text in the generalization table |
| Photo Taupe | #ac9c94 | (image) | warm tone of the faded hero photo |

## Tokens — Typography

- **Display:** declared `'Fraunces', ui-serif, Georgia, 'Times New Roman', serif` with `font-variation-settings` ("opsz" 96–144, "SOFT" 20–80). Rendered: Fraunces variable 300–900 (Google Fonts). Substitute: Newsreader (variable, similar optical sizing).
- **Body:** declared `'IBM Plex Sans', system-ui, …`. Rendered: IBM Plex Sans 400 and 600. Substitute: Inter.
- **Mono:** declared `'IBM Plex Mono', ui-monospace, …`. Rendered: IBM Plex Mono 400, 500, 600. Substitute: JetBrains Mono.
- **Icons:** Font Awesome 6.4, Academicons.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Hero headline | `.publication-title` (`clamp(2.4rem, 5.4vw, 4.4rem)`) | 70.4px / 380 / 1.02, ls -0.025em; `em` 360 italic |
| Section headline | `.section-title` (`clamp(2rem, 3.6vw, 3rem)`) | 48px / 380 / 1.05, ls -0.02em, max 28ch |
| Metric number | `.result-card .metric` | Fraunces 54.4px (3.4rem) / 400 / 1 |
| Insight sentence | `.insight p` | Fraunces 21.6px / 360 italic / 1.4 |
| Pillar / callout heads | `.pillar h4`, `.callout h5` | Fraunces 21.6px / 19.2px, 420 italic |
| Footer title | `.footer h4` | Fraunces 32px / 400 |
| Prose | `.prose` | Plex Sans 16.8px (1.05rem) / 400 / 1.75, max 68ch |
| Body | `body` | Plex Sans 16px / 400 / 1.65 |
| Figure caption | `.figure-caption` | Plex Sans 15.2px / 1.6 |
| Section marker | `.section-index` | Plex Mono 11.52px uppercase, ls 0.18em; `.num` 600 #c2410c |
| Buttons | `.publication-links .button` | Plex Mono 12.48px / 500 uppercase, ls 0.06em |
| Nav | `.navbar-float a` | Plex Mono 13.12px / 500 lowercase |
| Labels | `.figure-plate::before`, `.fc-label`, `.video-caption` | Plex Mono 9.9–11.5px uppercase, ls 0.08–0.2em |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons, cards, plates, tables | radius 0 (square) |
| Nav, venue pill | radius 9999px / 999px |
| Radius scale (declared) | 4px, 6px, 10px (`--radius-sm/md/lg`), barely used |
| Shadow small | `0 1px 2px 0 rgba(15,17,21,0.06)` on figure plates |
| Shadow medium | `0 2px 6px -2px rgba(15,17,21,0.08), 0 8px 24px -12px rgba(15,17,21,0.08)` on the nav |
| Shadow large | `0 12px 32px -8px rgba(15,17,21,0.12), 0 24px 48px -16px rgba(15,17,21,0.10)` on plate and video hover |
| Button hover | `transform: translate(-2px,-2px)`, `box-shadow: 4px 4px 0 #0f1115`, fill #c2410c |
| Hairline grids | 1px gap on #e3dccd background with a 1px #e3dccd border (metrics, pillars, videos) |
| Callout | left border 2px #c2410c, padding 1.5rem 1.5rem 1.5rem 2.75rem, vertical rotated kicker |
| Body texture | dot grid `radial-gradient(rgba(15,17,21,0.045) 1px, transparent 1px)` at 22px, noise overlay at 0.35 opacity |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px max at ≥1024px (x=240–1200 at 1440).
- **Hero:** padding 8rem top (128px) / 5rem bottom (80px); content left aligned; title capped at 18ch; photo covers the right 52%.
- **Sections:** `.section` padding 96px 24px; Bulma `columns` with `column is-3` (marker, 240px) and `column is-9` (content, 714px at x=486).
- **Section headline:** margin-bottom 44px; prose max 68ch.
- **Figure plate:** padding 20px inside a 1px #e3dccd border on #ffffff; caption grid `80px 1fr` with a 20px gap.
- **Grids:** `.results-grid` and `.pillar-grid` 3 equal columns; `.compare-grid` 2 columns; `.video-grid` `repeat(auto-fill, minmax(280px, 1fr))`.
- **Footer:** padding 80px 24px on #0f1115.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px (prose 16.8px) | 70.4px | marker column + 9-column content |
| 901–1023px | 24px | 16px | 5.4vw (49–55px) | same split, container fluid |
| 769–900px | 20px | 16px | 5.4vw | section padding 64px 20px; metrics, pillars, compare stack to 1 column; caption label above body; hero photo full width at 0.18 opacity |
| ≤768px | 20px | 16px | 36px (2.25rem) | hero padding 96px / 48px; Bulma columns stack (marker above headline); nav max 94% wide, scrolls horizontally |

## Components

- **Floating pill nav:** fixed, centred, translucent paper with 14px blur, 9999px radius, 1px faint border, medium shadow; lowercase mono links in #4a4d55 that gain a 6% ink pill on hover.
- **Meta line:** mono uppercase kicker with a 6px rust dot pulsing via a 4px → 8px ring, a 40px #e3dccd rule, then the venue.
- **Editorial headline:** Fraunces light 380, tight negative tracking, with one clause set as rust italic `em`.
- **Square mono button:** height 2.6rem, padding 0 1.25rem, 1px #0f1115 border, Plex Mono 12.48px uppercase; solid variant #0f1115 / #faf8f3, ghost variant transparent / #0f1115; hover fills #c2410c, shifts up-left 2px and drops a hard 4px ink shadow (ghost hover fills ink instead).
- **Section marker:** "§ 01" in rust 600 mono plus the label in muted mono, letter-spacing 0.18em, in the left quarter column.
- **Figure plate:** #ffffff, 1px #e3dccd border, 20px padding, small shadow, a mono "FIG. 01 — FRAMEWORK" label pinned top-left; on hover large shadow and image scales 1.015. Caption below in a two-column grid with a rust mono "FIGURE 01" label.
- **Numbered list:** `.contrib-list` items separated by #e3dccd hairlines, rust mono "01", "02" numerals at the left, 56px text indent, inside a callout with a vertical rotated kicker "KEY CONTRIBUTIONS".
- **Metric card:** white cell in a 1px hairline grid, 2rem 1.5rem padding, Fraunces 54.4px number above a mono uppercase label; a 2px top bar turns rust on hover; accent variant is ink with paper text.
- **Insight box:** #0f1115 block, amber #fbbf24 mono kicker, Fraunces italic 21.6px sentence with bold numbers in Plex Sans amber.
- **Video card:** in a 1px hairline grid; mono uppercase caption bar with a rust "→" that slides 4px on hover; card scales 1.02 with a large shadow.
- **Underline tabs:** mono uppercase tabs, active tab ink with a 2px #c2410c underline.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Floating nav | Yes | frosted pill, mono lowercase links |
| Meta kicker + venue | Yes | mono line with pulsing dot; black venue pill |
| Title / authors / affiliations | Yes | left-aligned Fraunces headline, mono affiliations |
| Link buttons | Yes | square mono buttons, one solid two ghost |
| Hero imagery | Present but non-standard | faded robot photo behind the right half, no teaser figure |
| Abstract | Yes | § 01 with headline sentence and prose |
| Overview figure + contributions | Yes | figure plate, numbered list in a callout |
| Method | Yes | pillars grid and figure plates |
| Comparison | Yes | two-column compare grid (white vs ink) |
| Results | Yes | metric cards, tabs, figure plates, generalization table with tags |
| Demo videos | Yes | hairline video grid with mono captions |
| Applications | Yes | figures on a tinted band |
| BibTeX | No (absent from the source) | |
| Footer | Yes | ink colophon with Fraunces title |

## Adapting to Other Content

- **More authors:** keep them inline in Plex Sans 16px with rust superscripts; bold only equal-first authors; let the block wrap at 44rem.
- **Results table:** use the `.gen-table` recipe: no outer border, rows separated by 1px #e3dccd, Plex Sans 15.2px cells, mono tag chips (#f3efe6 fill, 1px #e3dccd border, rust text) for categories, best numbers bold #0f1115.
- **News:** a `.contrib-list`-style list where the numeral is replaced by a mono date in #c2410c.
- **BibTeX:** add a § section with a #ffffff figure-plate box holding Plex Mono 13px text and a mono "BIBTEX" plate label.
- **Without a hero photo:** keep the left-aligned headline and let the dot-grid paper show; do not centre the hero.

## Do's and Don'ts

- Do open every section with a single headline sentence in Fraunces, one clause in rust italic.
- Do keep corners square except the nav and venue pill.
- Do set all labels, markers and buttons in uppercase Plex Mono with generous tracking.
- Do alternate paper and #f3efe6 bands rather than adding cards with shadows.
- Don't use rust for large fills; it is for italics, numerals and hover.
- Don't add more than one accent beyond rust; amber appears only inside ink insight boxes.
- Don't centre body sections; the left marker column is part of the rhythm.

## Surfaces

Warm paper #faf8f3 with a 22px dot grid and grain; tinted #f3efe6 bands for alternate sections; #ffffff plates and cards on hairline grids; solid #0f1115 for insight boxes, the positive comparison column and the footer.

## Imagery

A faded photograph of a robot arm behind the hero; white-plated research figures (feature-field visualisations, bar charts, pipeline diagrams); real-world manipulation videos in a hairline grid.

## Layout

Left-aligned editorial hero with a photo on the right, then 960px sections split 3/9 between a section marker and content. Rendered height about 9,700px.

## Agent Prompt Guide

Quick colors: paper #faf8f3, tint #f3efe6, ink #0f1115, muted #4a4d55, light #7c7f87, rust #c2410c (hover #9a330a), hairline #e3dccd, surface #ffffff, amber #fbbf24, live dot #22c55e.

1. "Build a hero on #faf8f3 with a 22px dot grid: a mono uppercase kicker (IBM Plex Mono 11.52px, letter-spacing 0.12em, #4a4d55) led by a 6px #c2410c dot; a left-aligned Fraunces headline at 70.4px, weight 380, line-height 1.02, letter-spacing -0.025em, max 18ch, #0f1115, with the second clause in italic #c2410c; then a #0f1115 pill reading 'Accepted to …' with a #22c55e dot."
2. "Create square mono buttons: height 2.6rem, padding 0 1.25rem, 1px solid #0f1115, IBM Plex Mono 12.48px / 500 uppercase, letter-spacing 0.06em; primary filled #0f1115 with #faf8f3 text, others transparent; on hover fill #c2410c, translate(-2px,-2px) and box-shadow 4px 4px 0 #0f1115."
3. "Lay out a section: padding 96px 24px in a 960px container; left quarter shows '§ 03' in #c2410c Plex Mono 600 beside a muted uppercase label; right three quarters hold a 48px Fraunces headline (weight 380, one italic #c2410c phrase), then a figure plate: #ffffff, 1px #e3dccd border, 20px padding, mono label top-left in #7c7f87."

## Similar Pages

- Editorial-style research pages that use a variable serif display with mono metadata (for example, SPACeR in this collection for the Swiss counterpart).
- Magazine-like project pages with section numbering and a left marker column.

## Quick Start

```css
:root {
  --paper: #faf8f3;
  --paper-tint: #f3efe6;
  --ink: #0f1115;
  --muted: #4a4d55;
  --light: #7c7f87;
  --primary: #c2410c;
  --primary-dark: #9a330a;
  --rule-soft: #e3dccd;
  --surface: #ffffff;
  --amber: #fbbf24;
  --live: #22c55e;
  --font-display: 'Fraunces', Georgia, serif;
  --font-body: 'IBM Plex Sans', system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --title-size: clamp(2.4rem, 5.4vw, 4.4rem);
  --section-title-size: clamp(2rem, 3.6vw, 3rem);
  --container: 960px;
}
```

## Provenance

- **URL:** https://pa3ff.github.io/
- **Paper:** Learning Part-Aware Dense 3D Feature Field for Generalizable Articulated Object Manipulation (arXiv 2602.14193), Yue Chen et al.
- **Venue:** ICLR 2026 (stated on the page).
- **Selection reason:** existing verified entry; arXiv 2602.14193 comment: Accept to ICLR 2026, project page https://pa3ff.github.io.
- **Template credit:** none stated; custom inline theme over Bulma.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 screenshots (first viewport and tall), the page's inline style block and HTML; 2026-10-28.
