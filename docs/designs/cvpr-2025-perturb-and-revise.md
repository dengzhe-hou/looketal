# Perturb-and-Revise Slate Header — Style Reference

> A slate-blue dusk banner with one yellow lamp lit, opening onto a row of quiet white cards.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 9,042px page, a 390px render, and the single inline `<style>` block in the page HTML (the page uses no framework; Font Awesome 6 is the only external CSS). No web text fonts load: everything is the system UI stack. Color share is measured on the first 1440×900 viewport.

## Overview

A self-contained, hand-written page. A 360px header runs a horizontal gradient from slate #2c3e50 to steel blue #4a6b8a, centring a 38.4px bold white title on one line, white author links with superscripts, pale grey affiliations, a yellow "CVPR 2025" with 1px letter-spacing and two translucent glass buttons (15% white fill, 30% white border, 5px radius). Below, on a #f8f9fa page, the abstract sits in a white 1000px card with an 8px radius and a soft shadow; then each result is its own white 800px card holding a wide comparison GIF (source, baselines, ours) that lifts 5px on hover. Section heads are 28.8px bold #2c3e50, centred. Thin 2px dividers fade from transparent through #3498db and back between groups. Method figures sit at 70% width with rounded corners and a shadow, captions in #555555. A white BibTeX box and a #f5f5f5 attribution band close the page.

## First Viewport

Color share (1440×900, 8-color quantize): slate #364d63 37.1% (the header gradient), page grey #f8f9fa 28.6% plus #f8f9f9 4.6% and #f8f9fb 1.4%, white #ffffff 22.1% (the abstract card), blue-grey #8092a3 4.0% (header edges and glass buttons), warm white #faf9f7 2.1%. The yellow venue line is under 1% but is the only saturated color on screen.

Anatomy in DOM order (`header` padding 40px 20px, centred, 360px tall, margin-bottom 40px):

1. **Title** — `h1`, 38.4px (2.4rem) / 700 / line-height 49.92px, #ffffff, one line at 1440 (y=40–90). Gap 30px.
2. **Authors** — `.authors` flex row, gap 20px, wrapping; `a.author` 19.2px / 400 #ffffff with superscripts; hover #3498db (y=120–154). Gap 15px.
3. **Affiliations** — `.affiliations` flex row, gap 20px, 16px / 400 #e0e0e0 (y=169–198). Gap 20px.
4. **Venue** — `.conference`, "CVPR 2025", 20.8px (1.3rem) / 500, letter-spacing 1px, #ffff00 (CSS `yellow`) (y=218–251). Gap 25px.
5. **Buttons** — `.buttons` flex, gap 15px: `a.button` "Paper" (fa-file-pdf) and "Code" (fa-github), 16px / 500 #ffffff, background rgba(255,255,255,0.15), 1px rgba(255,255,255,0.3) border, radius 5px, padding 8px 20px, icon then `&ensp;`; each 44px tall (y=276–320). Header ends at y=360. Gap 40px.
6. **Abstract card** — `.abstract`, #ffffff, max-width 1000px (x=220–1220), padding 25px, radius 8px, shadow `0 2px 4px rgba(0,0,0,0.1)`, y=400–774; `h2` "Abstract" 28.8px / 700 #2c3e50 centred at y=455 (30px top margin), paragraph 16px / 27.2px (1.7) #444444 left-aligned, 950px wide.
7. **Next head** — "3D Object Editing" h2 starts at y=813, cut by the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Slate | #2c3e50 | `header` gradient start, `h2` color | header left edge, all section heads |
| Steel Blue | #4a6b8a | `header` gradient end | header right edge |
| White | #ffffff | `h1`, `.author`, `.button` text, cards | title, authors, button labels, abstract and GIF cards, BibTeX box |
| Pale Grey | #e0e0e0 | `.affiliations` | affiliation line |
| Venue Yellow | #ffff00 | `.conference` (`yellow`) | "CVPR 2025" |
| Glass Fill | rgba(255,255,255,0.15) | `.button` | button fill (0.25 on hover) |
| Glass Edge | rgba(255,255,255,0.3) | `.button` border | button outline |
| Page Grey | #f8f9fa | `body`, `.main-container` | page background |
| Body Ink | #333333 | `body` color | general text |
| Abstract Ink | #444444 | `.abstract p` | abstract paragraph |
| Caption Ink | #555555 | `.figure-section p` | figure captions |
| Accent Blue | #3498db | `.section-divider` gradient, `.author:hover` | divider centre, author hover |
| Box Edge | #eeeeee | `.bibtex` border | BibTeX box outline |
| Band Grey | #f5f5f5 | `.attribution-banner` | attribution band |
| Credit Grey | #808080 | `.attribution-banner` (`grey`) | attribution text |
| Default Link | #0000ee | (browser default) | attribution links, unstyled and underlined |
| Header Slate | #364d63 | (screenshot) | dominant mid tone of the header gradient |

## Tokens — Typography

- **Sans:** `*` sets `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`; no web text fonts load, so it renders Segoe UI on Windows and San Francisco on macOS. Substitute: Inter.
- **Mono:** `.bibtex` uses the browser `monospace` at 14.4px.
- **Icons:** Font Awesome 6 (solid and brands).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `header h1` | 38.4px / 700 / 49.92px, #ffffff |
| Authors | `.authors .author` | 19.2px / 400 / 30.72px |
| Affiliations | `.affiliations` | 16px / 400 / 25.6px |
| Venue | `.conference` | 20.8px / 500, letter-spacing 1px |
| Buttons | `.button` | 16px / 500 / 25.6px |
| Section heads | `h2` | 28.8px / 700 / 46.08px, #2c3e50, centred, max-width 80% |
| Abstract | `.abstract p` | 16px / 400 / 27.2px, left |
| Captions | `.figure-section p` | 16px / 400 / 25.6px, #555555, centred, max-width 70% |
| BibTeX | `.bibtex` | 14.4px / 20.16px monospace |
| Attribution | `.attribution-banner` | 12.8px, letter-spacing 0.5px |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Abstract card | radius 8px, padding 25px, shadow `0 2px 4px rgba(0,0,0,0.1)`, no border |
| GIF card | radius 8px, `overflow: hidden`, same shadow; hover `translateY(-5px)` over 0.3s |
| Method figures | radius 8px, same shadow, 20px vertical margin |
| Buttons | radius 5px, 1px rgba(255,255,255,0.3) border, no shadow |
| BibTeX box | radius 5px, 1px #eeeeee border, padding 20px |
| Divider | 2px tall, 80% wide, `linear-gradient(to right, transparent, #3498db, transparent)`, margin 50px auto |
| Header | square, full bleed |

## Layout Metrics

- **Header:** full width, padding 40px 20px, 360px tall at 1440, margin-bottom 40px; internal gaps 30 / 15 / 20 / 25px (title → authors → affiliations → venue → buttons).
- **Content width:** `.abstract`, `.gif-section`, `.figure-section` max-width 1000px, centred (x=220 at 1440); section margin 40px auto.
- **GIF cards:** max-width 800px (x=320), stacked in a one-column grid with 30px gaps; three object-editing cards at 800×270.
- **Figures:** 70% of the 1000px section = 700px; captions also 70%.
- **Headings:** h2 max-width 80%, margin 30px auto 20px, padding-bottom 10px.
- **Dividers:** 80% of the viewport container (1152px at 1440), 50px above and below.
- **BibTeX:** 80% width, max 800px. **Attribution band:** padding 50px, margin-top 30px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >1040px | auto (centred 1000px) | 16px | 38.4px | one-line title, 800px GIF cards |
| 769–1040px | 20px header padding; cards touch the edges below 1000px | 16px | 38.4px | title wraps |
| ≤768px | 20px (header), 0 for cards | 16px | 38.4px | method figures widen to 90%; at 390 the title takes five lines (250px), authors wrap one per line, cards run edge to edge (390px) with no side margin |

## Components

- **Gradient header:** `linear-gradient(to right, #2c3e50, #4a6b8a)`, padding 40px 20px, all text centred and white except #e0e0e0 affiliations and the #ffff00 venue.
- **Glass button:** inline-flex, rgba(255,255,255,0.15) fill, 1px rgba(255,255,255,0.3) border, 5px radius, padding 8px 20px, 16px / 500 white, Font Awesome icon then an en space; hover fill rgba(255,255,255,0.25) over 0.3s.
- **White card:** #ffffff, 8px radius, `0 2px 4px rgba(0,0,0,0.1)`; for the abstract with 25px padding and a centred h2; for results with `overflow: hidden` and the GIF flush to the edges, lifting 5px on hover.
- **Fading divider:** 2px line, transparent → #3498db → transparent, 80% width.
- **Figure with caption:** 700px image with 8px radius and the card shadow, then a centred #555555 paragraph at 70% width.
- **BibTeX box:** white, 1px #eeeeee, 5px radius, padding 20px, 14.4px monospace, left-aligned, `pre-wrap`.
- **Attribution band:** #f5f5f5, padding 50px, 12.8px #808080 text with default blue underlined links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations / venue | Yes | white on the slate gradient, yellow venue |
| Link buttons | Yes | two glass buttons |
| Teaser | No (absent from the source) | the first result cards follow the abstract directly |
| Abstract | Yes | white card |
| Results | Yes | stacked GIF comparison cards (object, scene, Objaverse, fashion) |
| Method figures | Yes | Method Overview and Parameter Perturbation at 70% width |
| Real-scene results | Yes | tall comparison figure |
| Results table | No (absent from the source) | |
| BibTeX | Yes | white box under "Citation" |
| Footer | Yes | #f5f5f5 attribution band crediting the template to Susung Hong |

## Adapting to Other Content

- **More authors:** the flex row with 20px gaps wraps cleanly; past six names drop to 16px and keep superscripts.
- **Results table:** place it in a white card like the abstract (1000px, 25px padding, 8px radius, light shadow); header row #2c3e50 text on #f8f9fa, 1px #eeeeee row rules, best values bold.
- **Teaser video:** a white card at 800px with the video flush to the edges, directly under the header so the first screen has imagery.
- **Award:** reuse the `.conference` line, for example "CVPR 2025 · Highlight" in #ffff00; do not add a second accent.
- **News:** a white card with a short list, dates in #2c3e50 bold.

## Do's and Don'ts

- Do keep the header gradient horizontal from #2c3e50 to #4a6b8a and everything on it white, with yellow only for the venue.
- Do give every result its own white card at 800px with the same 8px radius and shadow.
- Do separate groups with the fading #3498db divider, not with background bands.
- Don't let cards touch the viewport edge on mobile; add a 16px side margin, which the source lacks.
- Don't leave footer links in browser-default #0000ee; colour them #3498db to match.
- Don't use heavier shadows; one soft `0 2px 4px` level is the whole system.

## Surfaces

Slate gradient header, #f8f9fa page, white cards (abstract, GIFs, BibTeX) with a single soft shadow, #f5f5f5 attribution band.

## Imagery

Wide comparison strips: a row of 3D objects (people, shoes) from five methods with serif column labels and an edit prompt underneath, polar-bear scene edits, landscape scenes with red-highlighted prompt words, and a soft diagram of parameter perturbation drawn as overlapping coloured discs.

## Layout

A full-width header, then a single centred column (1000px sections, 800px cards, 700px figures) on a light grey page. Rendered height about 9,000px.

## Agent Prompt Guide

Quick colors: header gradient #2c3e50 → #4a6b8a, title and authors #ffffff, affiliations #e0e0e0, venue #ffff00, page #f8f9fa, cards #ffffff, heads #2c3e50, abstract #444444, captions #555555, divider #3498db.

1. "Create a header: full width, background linear-gradient(to right, #2c3e50, #4a6b8a), padding 40px 20px, centred; a 38.4px bold white title, 19.2px white author links in a wrapping flex row with 20px gaps, 16px #e0e0e0 affiliations, a 20.8px weight-500 venue in #ffff00 with 1px letter-spacing, and glass buttons: rgba(255,255,255,0.15) fill, 1px rgba(255,255,255,0.3) border, 5px radius, padding 8px 20px, white 16px weight-500 text, hover fill rgba(255,255,255,0.25)."
2. "Put the abstract in a white card: max-width 1000px, padding 25px, 8px radius, shadow 0 2px 4px rgba(0,0,0,0.1), a centred 28.8px bold #2c3e50 heading and a left-aligned 16px #444444 paragraph with 1.7 line height, on a #f8f9fa page."
3. "Stack result cards: white, max-width 800px, 8px radius, overflow hidden, the same shadow, 30px apart, each holding a full-width comparison GIF; on hover translateY(-5px). Between groups add a 2px divider, 80% wide, linear-gradient(to right, transparent, #3498db, transparent), 50px margins."

## Similar Pages

- Hand-written single-file project pages with a gradient header and card-wrapped results.
- 3D editing project pages built around stacked comparison GIFs.

## Quick Start

```css
:root {
  --header-start: #2c3e50;
  --header-end: #4a6b8a;
  --on-header: #ffffff;
  --affiliation: #e0e0e0;
  --venue: #ffff00;
  --page: #f8f9fa;
  --card: #ffffff;
  --heading: #2c3e50;
  --text: #333333;
  --abstract: #444444;
  --caption: #555555;
  --accent: #3498db;
  --box-edge: #eeeeee;
  --band: #f5f5f5;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --title-size: 38.4px;
  --h2-size: 28.8px;
  --body-size: 16px;
  --radius-card: 8px;
  --radius-button: 5px;
  --shadow-card: 0 2px 4px rgba(0, 0, 0, 0.1);
  --section: 1000px;
  --card-width: 800px;
}
```

## Provenance

- **URL:** https://susunghong.github.io/Perturb-and-Revise
- **Paper:** Perturb-and-Revise: Flexible 3D Editing with Generative Trajectories (arXiv 2412.05279), Susung Hong, Johanna Karras, Ricardo Martin-Brualla, Ira Kemelmacher-Shlizerman (University of Washington, Google Research).
- **Venue:** CVPR 2025 (stated in the header).
- **Selection reason:** existing verified entry (entries.json).
- **Template credit:** the attribution band says the template was originally made by Susung Hong for this project.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, a 390px render, the inline `<style>` block and page HTML; 2026-10-28.
