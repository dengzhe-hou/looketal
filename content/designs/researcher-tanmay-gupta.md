# Pico Journey Timeline — Style Reference

> A clean résumé pinned to a corkboard rail: blue ring markers running down a grey thread beside an oval portrait.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport color share and DOM boxes from `tools/computed_style.py`, plus a selector probe of the nav, columns, timeline pseudo-elements, award rows and footer), the 1440×900 and full-page screenshots, and the page's inline `<style>` blocks and `/assets/styles.css` read directly. The page is a FastHTML app on Pico CSS (`@picocss/pico@latest`) plus flexboxgrid 6.3.1 and Font Awesome 6.5. No web font loads (`fonts_loaded` is empty); the system-ui stack renders as Segoe UI on the Windows capture. `html { color-scheme: light dark }` lets Pico switch to its dark palette under `prefers-color-scheme: dark`; the capture and every value below are the light scheme.

## Overview

A two-column profile under a sticky centred header. The header is a white band, full viewport width, with a 1px rgba(0,0,0,0.08) bottom border: the name "Tanmay Gupta" in system sans 32px/700 #373c44, a 16px tagline "Building multimodal AI that acts" in 62% black, and a row of four 19.2px links (Home, Updates, Research, Blog) separated by "|" bars at 60% opacity, the current page underlined. Below, a 1200px Pico container splits 5/1/6 with flexboxgrid. The left column holds a large oval portrait (the photo at 80% width with `border-radius: 50%`, so it renders as a 393×532 ellipse), then "About me", an email in a grey `code` pill, a slash-separated social row, an Awards list and a Service list whose rows are separated by 12% black hairlines. The right column is the distinctive part: "Professional Journey", a vertical timeline with a 2px #cccccc rail and 12px white dots ringed 3px in #007acc; each event has a blue date line, a 24px/700 role "@ organisation" heading, a 17.6px paragraph and square-bulleted project links. Links are Pico azure #0172ad with a half-opacity underline. A centred, 85%-opacity footer ends the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 75.2%, plus near-whites #fafafa 2.1%, #fffffe 0.8%, #fdffff 0.6%; dark #262321 7.1% (text and the dark photo background); greys #d1d3d7 6.3% and #e9ebee 4.5% (photo shirt, rail, hairlines); warm grey #8c7f7a 3.4% (skin and fence in the photo). Blue appears only in dates, dots and links, under 1%.

Anatomy in DOM order (desktop 1440px; `main.container` x=120, 1200px wide, padding-top 16px):

1. **Sticky header** (`nav.site-nav`, y=16, 131px tall, full 1440px via `margin: 0 calc(50% - 50vw)`): white, padding 8px 0, border-bottom 1px rgba(0,0,0,0.08), flex column centred.
2. **Name** (`.site-nav__brand strong`, y=20): system sans 32px/700, line-height 1.1, #373c44, centred. Gap 4px.
3. **Tagline** (`.site-nav__tagline`, y=67): 16px/400, line-height 1.1, rgba(0,0,0,0.62), centred, margin-top 8px. Gap 9px.
4. **Nav links** (`.site-nav__links a.contrast`, y=94): 19.2px/400 #181c25, padding 8px with -8px margin, 4px radius; "|" separators (`li.site-nav__sep`, opacity 0.6, padding 16px 8px); Home underlined. Header ends at y=147; gap 24px.
5. **Left column, portrait** (`.col-sm-5 img`, x=169, y=219): 393×532px ellipse (width 80%, `border-radius: 50%`), centred in the 507px column after two `<br>`s. Gap 48px.
6. **Left column, "About me"** (`h2`, y=799): 28px/700, line-height 1.15, #373c44, margin-bottom 16px; paragraph 17.6px/400, line-height 26.4px, #373c44, with #0172ad links. Continues below the fold.
7. **Right column, "Professional Journey"** (`.col-sm-6 h2`, x=728, y=171): same h2 recipe, top-aligned with the column. Gap 32px.
8. **Timeline** (`.timeline`, y=235): first event date "2026 - Present" 16px #007acc at y=235, dot at x=744; role heading `h3` 24px/700 #424751 at y=264; paragraph 17.6px at y=308; next event 40px later at y=453.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Text | #373c44 | Pico --pico-color (rgb 55,60,68) | body text, h2 section titles, name, award rows |
| Heading Slate | #424751 | Pico h3 colour | timeline role headings (`h3`) |
| Nav Ink | #181c25 | Pico --pico-contrast | header nav links (`a.contrast`) |
| Muted Tagline | rgba(0,0,0,0.62) | (literal) | header tagline |
| Azure Link | #0172ad | Pico --pico-primary | inline links, footer link; underline rgba(1,114,173,0.5) |
| Timeline Blue | #007acc | (literal) | `.date` text, timeline dot ring |
| Rail Grey | #cccccc | (literal) | timeline vertical rail (`.timeline::before`) |
| Paper | #ffffff | Pico background | page, sticky header, timeline dot fill |
| Hairline | rgba(0,0,0,0.12) | --award-divider-color | award and service row dividers |
| Nav Border | rgba(0,0,0,0.08) | --nav-border | header bottom border |
| Code Wash | #f3f5f7 | Pico --pico-code-background-color | email `code` pill |
| Code Text | #646b79 | Pico --pico-code-color | email `code` text |

Declared but not visible: `.tag` (purple), `.award` (gold #6b5200 on rgba(197,157,11,0.14)), `.venue` (neutral grey) badges, `.grouplink` (teal) and `.callout` (blue left border) are defined in the inline style for other pages (research, updates) and do not render on the home page. The `.codehilite` code-block colours belong to blog posts.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | system-ui, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, Helvetica, Arial, sans-serif (Pico) | none loaded; system font (Segoe UI on Windows, SF Pro on macOS) | Inter |
| Mono | ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace (Pico) | system mono (Consolas on Windows) | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.site-nav__brand strong` | 32px / 700 / 1.1, centred | #373c44 |
| Tagline | `.site-nav__tagline` | 16px / 400 / 1.1, centred | rgba(0,0,0,0.62) |
| Nav link | `.site-nav__links a` | 19.2px (inline 1.2em) / 400 / 1 | #181c25 |
| Section title | `h2` | 28px / 700 / 1.15 (32.2px) | #373c44 |
| Role heading | `.timeline-event h3` | 24px / 700 / 1.175 (28.2px) | #424751 |
| Date | `.date` | 16px / 400 / 1.5 | #007acc |
| Paragraph | `p[style="font-size: 1.1em"]` | 17.6px / 400 / 1.5 (26.4px) | #373c44 |
| List item | `.timeline-event li` | 16px / 400 / 1.5, square bullets | #373c44 |
| Award title | award row first `div` | 16px / 600 / 1.5 | #373c44 |
| Award detail | award row second `div` | 15.2px (0.95em) / 400 | #373c44 |
| Code | `code` | 15.4px / 400 mono | #646b79 on #f3f5f7 |
| Footer | `footer` | 16px, small line 13.33px, centred, opacity 0.85 | #373c44 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 50% (ellipse, image is not square) | none | none |
| Timeline dot | 50% (12px) | 3px #007acc | none |
| Timeline rail | 0 | 2px wide #cccccc fill | none |
| Nav link hit area | 4px | none | none |
| Code pill | 4px | none | none |
| Award / service row | 0 | 1px rgba(0,0,0,0.12) bottom | none |
| Sticky header | 0 | 1px rgba(0,0,0,0.08) bottom | none |

## Layout Metrics

- **Container**: Pico `main.container`, max-width 1200px at 1440 (x=120), padding 16px 0. Pico steps the container at its breakpoints (510px ≥576, 700px ≥768, 950px ≥1024, 1200px ≥1280, 1450px ≥1536).
- **Header**: sticky top 0, full viewport width, padding 8px 0, inner flex column centred with 0.1rem gap; links row gap 0.35rem; `scroll-padding-top: 80px` for anchors.
- **Columns**: flexboxgrid `.row` (margin 0 -8px) with `.col-sm-5` (41.67%, 507px), an empty `.col-sm-1` spacer (8.33%) and `.col-sm-6` (50%, 608px); column padding 0 8px. Columns start 24px under the header.
- **Portrait**: 80% of the left column, centred with auto margins, preceded and followed by two `<br>`s.
- **Left-column sections**: separated by `<br><br>`; h2 margin-bottom 16px; award rows padding 8px 0.
- **Timeline**: `.timeline` margin 32px 0, padding-left 32px; rail at left 20.8px (1.3rem), from 6.4px below the top to the bottom, 2px wide; each `.timeline-event` padding-left 32px, margin-bottom 40px; dot at left -16px, top 6.4px; `.date` margin-bottom 4.8px; h3 margin-bottom 16px.
- **Footer**: padding 32px 0 24px, centred, opacity 0.85.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| <576px | 16px (Pico container padding) | 16px (paragraphs 17.6px) | name 32px, h2 28px | single column; nav links shrink to 0.9em with 0.1rem gap and separators at 0.5 opacity (≤480px) |
| 576–767px | auto (container 510px) | 16px | same | single column |
| ≥768px | auto (container 700, 950, 1200, 1450px by step) | 16px | same | flexboxgrid `col-sm` activates: 5 / 1 / 6 split |

## Components

- **Sticky name header**: full-bleed white band, padding 8px 0, 1px rgba(0,0,0,0.08) bottom border; centred name 32px/700 #373c44, tagline 16px rgba(0,0,0,0.62) 8px below, then nav links 19.2px #181c25 with "|" separators at 0.6 opacity; current link underlined. No icons.
- **Oval portrait**: a portrait-format photo at 80% column width with `border-radius: 50%`, giving an ellipse; no border, no shadow.
- **Timeline event**: rail 2px #cccccc; dot 12px circle, white fill, 3px #007acc ring, aligned with the date's first line; date 16px #007acc; role "Title @ Org" 24px/700 #424751; description 17.6px/1.5; optional square-bullet list of project links (#0172ad) with one-line explanations; 40px between events.
- **Award row**: block with padding 8px 0 and a 1px rgba(0,0,0,0.12) bottom rule; 16px/600 title line, then a 15.2px detail line "CVPR 2023 Best Paper | arXiv" with the source as a link.
- **Contact lines**: "Email:" followed by an obfuscated address in a Pico `code` pill (#f3f5f7, #646b79, 4px radius, padding 6px); "Social:" followed by slash-separated text links in a flex row with 10px gaps.
- **Link**: #0172ad, underline in rgba(1,114,173,0.5); Pico darkens to its primary-hover on hover.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name / tagline header | yes | sticky centred white band |
| Navigation | yes | four text links with bar separators |
| Portrait | yes | large ellipse at the top of the left column |
| About / bio | yes | h2 plus two 17.6px paragraphs |
| Contact and social | yes | code pill email, slash-separated links |
| Awards | yes | hairline-separated two-line rows |
| Service | yes | same row recipe as awards |
| Career timeline | yes | right column, rail with ringed dots |
| Selected projects | present but non-standard | square-bullet links inside timeline events |
| Publication list | absent from the source | lives on the separate Research page |
| News | absent from the source | lives on the separate Updates page |
| Footer | yes | centred copyright and "Made with FastHTML" at 0.85 opacity |

## Adapting to Other Content

- **Long publication lists**: keep them out of the timeline; add an h2 "Publications" in the left column using the award-row recipe (16px/600 title, 15.2px venue line, 12% hairline), or a separate page as the source does.
- **News**: use the timeline recipe with the date as the `.date` line and a one-line paragraph instead of an h3, so news reads as a second rail.
- **More roles**: the rail stretches with content; keep 40px between events and one h3 per role.
- **Venue or award badges**: the inline style already defines `.venue` (rgba(17,24,39,0.06) fill, 1px rgba(17,24,39,0.14), 6px radius, 13.6px/600) and `.award` (gold); use them after a paper title rather than adding new colours.
- **A results table**: use Pico's default table (hairline rows) inside the right column; do not add fills.

## Do's and Don'ts

- Do keep the 5 / 1 / 6 split so the timeline column is visibly wider than the profile column.
- Do keep blue (#007acc) for dates and dot rings only; links stay Pico azure #0172ad.
- Do keep section separation to `<br>` spacing and 12% hairlines; no cards.
- Don't crop the portrait into a circle; the ellipse from a portrait photo is part of the look.
- Don't put the nav in a bar with a background colour; it is white with a hairline.
- Don't use more than one rail; everything chronological goes on the right.

## Surfaces

One white surface. The sticky header is the same white with a hairline beneath; the only filled element is the grey code pill.

## Imagery

A single large black-and-white-background portrait, cropped by the ellipse. No project thumbnails, logos or icons on the home page.

## Layout

Sticky centred header, then a two-column flexboxgrid row inside a 1200px Pico container: profile, about, contact, awards and service on the left; a long career timeline on the right that runs past the left column's end. About 2638px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: text #373c44, role heading #424751, nav #181c25, link #0172ad, date and dot #007acc, rail #cccccc, hairline rgba(0,0,0,0.12), header border rgba(0,0,0,0.08), code #646b79 on #f3f5f7, page #ffffff.

1. "Build a sticky centred header: full-width white band, padding 8px 0, border-bottom 1px rgba(0,0,0,0.08); name in system-ui 32px/700 #373c44; tagline 16px rgba(0,0,0,0.62) 8px below; nav links 19.2px #181c25 separated by '|' at 0.6 opacity, current link underlined."
2. "Make a career timeline: container padding-left 32px with a 2px #cccccc rail at left 20.8px; each event padding-left 32px, margin-bottom 40px, with a 12px circle (white fill, 3px #007acc ring) at left -16px, top 6.4px; date 16px #007acc; role heading 24px/700 #424751 'Title @ Org'; paragraph 17.6px/1.5 #373c44; square-bullet project links in #0172ad."
3. "Make award rows: each block padding 8px 0 with a 1px rgba(0,0,0,0.12) bottom border; first line 16px/600 #373c44, second line 15.2px with the venue and award text followed by '| arXiv' as a #0172ad link."

## Similar Pages

- Pico CSS / FastHTML personal sites.
- Résumé-style researcher pages that put industry roles on a vertical timeline.

## Quick Start

```css
:root {
  --text: #373c44;
  --heading: #424751;
  --nav: #181c25;
  --link: #0172ad;
  --accent: #007acc;
  --rail: #cccccc;
  --hairline: rgba(0, 0, 0, 0.12);
  --nav-border: rgba(0, 0, 0, 0.08);
  --font-sans: system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
body { font: 400 16px/1.5 var(--font-sans); color: var(--text); background: #ffffff; }
.site-nav { position: sticky; top: 0; background: #ffffff; border-bottom: 1px solid var(--nav-border); padding: 8px 0; text-align: center; }
.timeline { position: relative; margin: 32px 0; padding-left: 32px; }
.timeline::before { content: ""; position: absolute; top: 6.4px; bottom: 0; left: 20.8px; width: 2px; background: var(--rail); }
.timeline-event { position: relative; padding-left: 32px; margin-bottom: 40px; }
.timeline-event::before { content: ""; position: absolute; top: 6.4px; left: -16px; width: 12px; height: 12px; background: #ffffff; border: 3px solid var(--accent); border-radius: 50%; box-sizing: border-box; }
.date { color: var(--accent); margin-bottom: 4.8px; }
```

## Provenance

- **URL**: https://tanmaygupta.info/
- **Person**: Tanmay Gupta (vision-language, visual reasoning agents).
- **Venue / award**: CVPR 2023 Best Paper, "Visual Programming: Compositional visual reasoning without training" (first author). https://cvpr.thecvf.com/Conferences/2023/BestPaperAwards
- **Selection reason**: award rule (first/last author); chosen for the two-column layout with a "Professional Journey" vertical timeline beside the profile and awards.
- **Template credit**: footer says "Made with FastHTML"; styling is Pico CSS with flexboxgrid and custom inline rules.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, DOM boxes), a selector probe of header, columns, timeline pseudo-elements, award rows and footer, the 1440×900 and full-page screenshots, and the inline styles and `/assets/styles.css` read directly, on 2026-10-28.
