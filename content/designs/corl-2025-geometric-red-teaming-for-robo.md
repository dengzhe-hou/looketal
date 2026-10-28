# GRT Red-Team Dossier — Style Reference

> A tidy test report with one red stamp: an apricot "Oral Presentation" pill, green author names, and a framed specimen sheet of nominal objects beside their broken twins.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the title, badge, author block, teaser figure, abstract, simulation table, video galleries and prompt explorer, the 1440×900 and full-page screenshots, and the page's `static/css/index.css`, Bulma 0.9, a long inline `<style>` block and `index.html`. The inline block declares several values that lose the cascade to Bulma; the rendered values are listed and the losing declarations are noted. The stock render tool timed out on this page's slow load event; the same script was rerun with a tolerant load wait.

## Overview

A long academic page (about 10,500px tall) in a classic Bulma/Nerfies frame, retuned with an inline "global rhythm" stylesheet that tightens sections to almost no padding. On white, a centred two-line title in heavy Google Sans (#363636), a grey-and-charcoal venue line, a small apricot pill reading "Oral Presentation • 5.7% acceptance" in red, green (#00b803) author names with superscripts, a black affiliation line and two dark pill buttons. The teaser is a single framed image (1px #dbdbdb border, 6px radius, Bulma box shadow) whose own header shows a red hacker icon and the title in a monospace face with "Red-Teaming" in dark red; below that header sits a grid of object photos and robot frames labelled Nominal, Successful Grasp, CrashShape and Failure. Sections follow with large justified text (20px abstract), uppercase centred headings (SYSTEM OVERVIEW, VLM PROMPTING STRATEGY, SIMULATION DEMOS), a bordered video table, an interactive VLM prompt explorer with selects and boxed tabs, and long real-world galleries of portrait videos with thumbnail strips and green or red outcome dots.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #faf9f8 / #fffffd / #fdffff together 67.6%; photo greys #8e8b89 10.5%, #4b4848 8.6%, #bfc1b7 8.6% and #e2dedb 4.7% (the object and robot photographs in the teaser grid). The green names and the red badge are too small to form clusters.

Anatomy in DOM order (desktop 1440px, everything centred in a 960px column at x=240):

1. **Hero body** (`.hero .hero-body`, from y=0): no navbar; inline rule `padding: clamp(1rem, 3vw, 2rem) 0 1rem` renders 32px 0 16px.
2. **Title** (`h1.title.is-1.publication-title`, y=32, 110px tall): Google Sans 48px/800 (synthesized from the 400 face), line-height 1.15 (55.2px), letter-spacing −0.02em (−0.96px), #363636, two lines. The inline `font-size: clamp(2rem, 5.2vw, 3.6rem)` loses to Bulma's `.title.is-1` (3rem). Margin-bottom 24px.
3. **Venue** (`h3.title.is-4.conference-authors`, y=166): "Conference on Robot Learning (CoRL) 2025", Google Sans 24px/600 (Bulma `is-4` beats the inline clamp), letter-spacing −0.36px; the h3 colour is #6b7280 but the text is a link forced to #292929. Gap 24px + 8px.
4. **Oral badge** (`.badge-pill`, y=226, 259×29): "Oral Presentation • 5.7% acceptance", Myriad Pro 16px/700, line-height 1, #c81717 on #fff6ee, 1px #fee7db border, padding 5.6px 9.6px, radius 9999px. Gap 4px.
5. **Authors** (`.publication-authors`, y=259): Myriad Pro 20px/400 (line-height 30px); names in #00b803 (the `index.css` `!important` beats the inline `color: inherit`), superscripts and commas in #222222; † marks equal advising. Hover adds a 1px dotted #bbbbbb underline.
6. **Affiliations** (y=298): "¹Robotics Institute, Carnegie Mellon University | ²National Institute of Standards and Technology", 20px #222222. Gap 4px.
7. **Advising note** (y=337): "( † indicates equal advising)", 20px #222222.
8. **Buttons** (y=387, 40px tall): arXiv and Code, Bulma dark pills, margin 4px 4.8px. Hero ends at y=459.
9. **Teaser figure** (`.png-image-display-section figure img`, y=479, 960×488): section padding 4px, figure margin 16px; 1px #dbdbdb border, radius 6px, shadow `0 2px 3px rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.1)`; the fold cuts it.

Arithmetic check: 0 + 32 = 32; 32 + 110 + 24 = 166; 166 + 28 + 24 = 218; 218 + 8 = 226; 226 + 29 + 4 = 259; 259 + 35 + 4 = 298; 298 + 35 + 4 ≈ 337; 337 + 35 + 12 (column padding) + 4 (button margin) ≈ 387; 387 + 40 + 4 + 12 + 16 = 459; 459 + 4 + 16 = 479.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (Bulma) | page, table, boxed tab panel |
| Ink | #222222 | --ink | body text, abstract, affiliations, author superscripts |
| Title Ink | #363636 | (Bulma `$grey-darker`) | title, section headings, table text, dark button fill |
| Venue Ink | #292929 | (`hsl(0, 0%, 16%)`) | venue link text |
| Venue Muted | #6b7280 | --muted | venue h3 colour (visible only on non-link text) |
| Author Green | #00b803 | (`hsl(121, 100%, 36%)`) | author names |
| Badge Red | #c81717 | (literal, `.badge-pill`) | oral badge text |
| Badge Cream | #fff6ee | (literal) | oral badge fill |
| Badge Border | #fee7db | (literal) | oral badge 1px border |
| Frame Grey | #dbdbdb | (Bulma `$grey-lighter`) | teaser and figure borders, table cell borders, selects, prompt windows |
| Prompt Fill | #f9f9f9 | (literal) | scrollable VLM prompt windows |
| Tab Blue | #3273dc | (Bulma `$link`) | active boxed tab text, active gallery thumbnail border |
| Player Grey | #363636 | (literal, `.lead-video-player-wrapper`) | portrait video frame fill |
| Thumb Dark | #2b2b2b | (literal) | gallery thumbnail fill |
| Success Green | #28a745 | (literal) | success outcome dot |
| Failure Red | #dc3545 | (literal) | failure outcome dot |
| Code Grey | #f5f5f5 | (Bulma `pre`) | BibTeX outer block |
| Footer | #fafafa | (Bulma `.footer`) | footer band |

Declared but not visible: `--accent: #1f6feb` in the inline `:root` is not used by any probed element.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / venue | "Google Sans", system-ui, -apple-system, Segoe UI, Roboto, "Noto Sans", sans-serif | Google Sans 400; 600 and 800 synthesized | Product Sans / Outfit |
| Body | "Myriad-Pro", "Open Sans", sans-serif (`myriad_pro.css`, self-hosted) | Myriad-Pro and Open Sans 400 loaded; Myriad Pro renders | Open Sans |
| Code | monospace; highlight.js GitHub theme | Consolas on Windows | Source Code Pro |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 800 / 55.2px, letter-spacing −0.96px | #363636 |
| Venue | `h3.title.is-4.conference-authors a` | 24px / 600 / 27.6px, letter-spacing −0.36px | #292929 |
| Oral badge | `.badge-pill` | 16px / 700 / 1 | #c81717 |
| Authors / affiliations | `.publication-authors` (`is-size-5`) | 20px / 400 / 30px | names #00b803, rest #222222 |
| Section heading | `h2.title.is-3` | 32px / 600 / 36.8px, letter-spacing −0.48px, uppercase in overview sections | #363636 |
| Sub-heading | `h3.title.is-4` | 24px / 600 / 27.6px | #363636 |
| Panel heading | `h4` | 20px / 600 / 23px | #363636 |
| Abstract | `.content.has-text-justified p` | 20px / 400 / 30px, justified | #222222 |
| Caption / body | `.content p` in figure sections | 16px / 400 / 24px, justified | #222222 |
| Table | `.table` cells | 16px / 400; headers 700 | #363636 |
| Button | `.button.is-normal` | 16px / 400 | #ffffff |
| Prompt text | `.scrollable-prompt-window pre` | 0.8rem = 12.8px | #363636 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Oral badge | 9999px | 1px #fee7db | none |
| Link buttons | 290486px (pill) | 1px transparent | none |
| Teaser and overview figures | 6px | 1px #dbdbdb | `0 2px 3px rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.1)` |
| Simulation table | 0 | 1px #dbdbdb cells, padding 4px 8px | none |
| Portrait lead video | 15px | none | none; fill #363636 |
| Gallery thumbnails | 8px (120×70) | 3px transparent; hover #dbdbdb; active #3273dc | outcome dot `0 1px 3px rgba(0,0,0,0.4)` |
| Prompt window | 4px | 1px #dbdbdb | none |
| Selects | 4px | 1px #dbdbdb | none |
| Boxed tabs | 4px 4px 0 0 | 1px #dbdbdb, open bottom on the active tab | none |

## Layout Metrics

- **Column**: `.container.is-max-desktop` 960px at x=240 for the hero, teaser, abstract and figures; the footer container is 1344px.
- **Section rhythm**: inline `.section { padding-top/bottom: clamp(0.25rem, 0.25vw, 0.25rem) }` = 4px, with Bulma helpers `pt-2`/`pb-2` (8px) or `py-4` (16px) on some sections; side padding stays 24px. Figures keep `margin: 1rem auto !important` (16px). Sections therefore sit only 8–32px apart; spacing comes from the headings.
- **Hero**: padding 32px 0 16px; 459px tall.
- **Simulation table**: full 960px, four 240px columns (`table-layout: fixed`), videos 223px wide inside cells.
- **Real-world galleries**: centred 180×320 portrait lead player, 12px below it a wrapped strip of 120×70 thumbnails 8px apart; scenarios 24px apart (`margin-bottom: 1.5rem`).
- **BibTeX**: outer `pre` 1152px at x=144 with an inner highlight.js `code` panel (#ffffff, padding 14px).
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px (1440 render) | 960px column centred | 16px (abstract 20px) | 48px | 4-column table, centred galleries |
| 769–1023px | 24px section padding, fluid column | 16px | 48px | hero padding 3vw (about 23–31px) |
| ≤768px | 24px | 16px | 48px (Bulma `is-1` has no mobile override) | Bulma columns stack; the table keeps 4 fixed columns and scrolls in `.table-container` |
| ≤533px | 24px | 16px | 48px | hero padding hits the 1rem (16px) floor |

## Components

- **Oral badge** (`.badge-pill`): inline-flex, gap 0.4em, #fff6ee fill, 1px #fee7db border, #c81717 text 16px/700, line-height 1, padding 5.6px 9.6px, radius 9999px, 8px top margin. Placed between the venue line and the authors.
- **Green author line**: Myriad Pro 20px, names #00b803 with numeric superscripts, separated by commas; hover shows a 1px dotted #bbbbbb underline.
- **Dark pill button** (Bulma `.button.is-dark.is-rounded`): #363636, #ffffff 16px text, 40px tall, padding 7px 20px, icon left (Academicons arXiv, Font Awesome GitHub).
- **Framed figure** (`figure.image img`): 1px #dbdbdb border, radius 6px, `0 2px 3px rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.1)`, max-height 80vh, centred with 16px margins.
- **Uppercase section heading**: Myriad Pro 32px/600 #363636, letter-spacing −0.48px, `text-transform: uppercase`, 9.6px below it the figure.
- **Video table**: Bulma `.table.is-bordered.is-striped.is-narrow.is-hoverable.is-fullwidth`, header row 700 #363636, first column labels (Nominal Objects / CrashShapes), looping videos in cells.
- **Gallery picker**: 180×320 portrait player (radius 15px, #363636) above a strip of 120×70 thumbnails (radius 8px, #2b2b2b, 3px border; hover #dbdbdb and scale 1.05; active #3273dc), each with a 24px outcome dot at the bottom right in #28a745 or #dc3545 with a white Font Awesome icon.
- **VLM prompt explorer**: full-width Bulma selects (40px, 1px #dbdbdb, radius 4px), boxed tabs (active text #3273dc on white), #f9f9f9 scroll windows (max-height 280px, padding 0.75em, 12.8px text) and thumbnails with a #3273dc active border and glow `0 0 5px #3273dc`.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | absent from the source | the page opens directly with the title |
| Title / venue | yes | heavy Google Sans title, grey-black venue line |
| Award / oral badge | yes | apricot pill with red text |
| Authors / affiliations | yes | green names, black affiliation line |
| Link buttons | yes | two dark pills |
| Teaser | yes | one framed image with its own monospace header and a labelled photo grid |
| Abstract | yes | 20px justified paragraph |
| Method figure | yes | framed overview diagram with a justified caption |
| Simulation demos | yes | bordered table of looping videos |
| Interactive explorer | yes | selects, boxed tabs, scroll windows |
| Real-world galleries | yes | portrait player plus thumbnail strip with outcome dots |
| Acknowledgement / BibTeX / footer | yes | short section, highlight.js BibTeX, #fafafa footer |
| Results table (numbers) | absent from the source | the only table holds videos |

## Adapting to Other Content

- **More authors**: keep the 20px Myriad Pro line with #00b803 names; at 960px it holds about seven names, so a longer list wraps to more lines above the single affiliation line.
- **A results table**: reuse the Bulma table classes already on the page (bordered, striped, narrow, hoverable, full width) at 960px with 16px #363636 text, 700 headers and 1px #dbdbdb borders; put best values in bold, not in green or red.
- **More awards**: add another `.badge-pill` next to the first (same #fff6ee / #fee7db / #c81717 recipe), separated by 8px.
- **More galleries**: repeat the lead-player-plus-strip pattern; keep outcome dots strictly #28a745 for success and #dc3545 for failure.
- **Long publication or news lists**: 16px justified paragraphs under a 32px uppercase heading, dates in 700 #363636; no cards.

## Do's and Don'ts

- Do keep one warm accent, the apricot oral pill, and let the green names be the only other colour in the header.
- Do frame every static figure with the 1px #dbdbdb border, 6px radius and Bulma's two-layer shadow.
- Do keep section padding tight (4–16px) and let headings carry the separation.
- Do set the abstract larger (20px) than the rest of the body text.
- Don't fill buttons with colour; they stay #363636.
- Don't use the red and green outcome colours outside the result indicators.
- Don't rely on the inline clamp sizes for the title and venue; Bulma's `is-1` and `is-4` sizes are what render.

## Surfaces

Plain white throughout; framed figures with soft two-layer shadows; #f9f9f9 prompt windows; dark #363636 and #2b2b2b frames for videos; #f5f5f5 BibTeX and #fafafa footer.

## Imagery

Photographs of hand tools, bottles and connectors next to their deformed "CrashShape" counterparts; Franka arm and UFactory gripper frames on grey cloth; simulation renders on checkered floors; a pastel four-panel system diagram (yellow, green, red, orange); portrait phone videos of real-robot insertion trials.

## Layout

Centred 960px column for everything except the footer. Very compact vertical rhythm. Galleries are centred stacks; the simulation table is the only grid.

## Agent Prompt Guide

Quick colors: page #ffffff, text #222222, title #363636, venue #292929, authors #00b803, badge text #c81717, badge fill #fff6ee, badge border #fee7db, frames #dbdbdb, tab blue #3273dc, success #28a745, failure #dc3545.

1. "Build a centred 960px header with padding 32px 0 16px: Google Sans 48px/800 #363636 title, line-height 1.15, letter-spacing -0.02em; a 24px/600 #292929 venue line; an oral pill (#fff6ee fill, 1px #fee7db border, #c81717 16px/700 text, padding 5.6px 9.6px, radius 9999px); Myriad Pro 20px authors with #00b803 names and #222222 superscripts; two #363636 pill buttons 40px tall."
2. "Frame figures: 1px #dbdbdb border, radius 6px, box-shadow 0 2px 3px rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.1), 16px vertical margin; section headings Myriad Pro 32px/600 #363636 uppercase, letter-spacing -0.48px; captions 16px/24px #222222 justified."
3. "Make a result gallery: a 180×320 portrait video in a #363636 frame with radius 15px, then a centred strip of 120×70 thumbnails (radius 8px, #2b2b2b, 3px transparent border, hover #dbdbdb and scale 1.05, active #3273dc) 8px apart, each with a 24px round outcome dot in #28a745 or #dc3545 at bottom right."

## Similar Pages

- CMU robotics pages built from the ArticuBot / Eureka template (credited in the footer), which descend from Nerfies.
- Robustness and red-teaming pages that pair nominal objects with failure-inducing variants in a labelled grid.

## Quick Start

```css
:root {
  --ink: #222222;
  --title: #363636;
  --muted: #6b7280;
  --author: #00b803;
  --badge-text: #c81717;
  --badge-bg: #fff6ee;
  --badge-border: #fee7db;
  --frame: #dbdbdb;
  --tab: #3273dc;
  --success: #28a745;
  --failure: #dc3545;
  --font-title: "Google Sans", system-ui, sans-serif;
  --font-body: "Myriad-Pro", "Open Sans", sans-serif;
}
.badge-pill { display: inline-flex; gap: .4em; border: 1px solid var(--badge-border); background: var(--badge-bg); color: var(--badge-text); font-weight: 700; font-size: 1rem; line-height: 1; padding: .35rem .6rem; border-radius: 9999px; }
figure.image img { border: 1px solid var(--frame); border-radius: 6px; box-shadow: 0 2px 3px rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.1); }
```

## Provenance

- **URL**: https://georedteam.github.io/
- **Paper**: Geometric Red-Teaming for Robotic Manipulation (arXiv 2509.12379), Divyam Goel, Yufei Wang, Tiancheng Wu, Helen Qiao, Pavel Piliptchak, David Held, Zackory Erickson (Carnegie Mellon University, NIST).
- **Venue**: CoRL 2025, Oral Presentation (5.7% acceptance, per the page).
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 (Oral) and the abstract links this project page.
- **Template credit**: footer reads "Website template borrowed from ArticuBot and Eureka" (Bulma 0.9, Font Awesome, Academicons, highlight.js GitHub theme).
- **Evidence used**: computed-style render at 1440×900 (computed styles, anatomy, fonts_loaded, color share) via the same script with a tolerant load wait, selector probes at 1440, the 1440×900 and full-page screenshots, and `static/css/index.css`, the inline `<style>` block and `index.html` read directly, on 2026-10-28.
