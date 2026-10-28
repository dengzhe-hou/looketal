# ICDG — Style Reference

> A lab handbook printed on two paper stocks: grey and white bands take turns, blue-ruled callouts hold the key numbers, and charcoal pills point to the paper.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css` read with `index.html`. Bulma 0.9 (Nerfies template) sits underneath and wins several declarations; the render is reported where it differs from the custom sheet: the navbar is fixed (custom `position: static` loses to `.navbar.is-fixed-top`), the venue line is rgba(0,0,0,0.9) at 20px (custom #64748b at 1.55rem loses to `.hero.is-light .subtitle` and `is-size-5 !important`), the authors are 20px (custom 1.3rem loses to `is-size-5`), and the hero body padding is 24px (custom 4rem top loses to `.hero.is-small .hero-body`). There is no dark mode.

## Overview

A long (11,903px) results-and-method page built on the Nerfies/Bulma base with a few custom touches. A fixed 53px white navbar (95% opaque, 1px #e2e8f0 bottom rule) lists nine section anchors in grey #4a4a4a with "Back to top" at the left and a GitHub icon at the right. The hero is a flat light-grey #f5f5f5 band with a centred 40px Google Sans title in rgba(0,0,0,0.7), blue #0e78be author names on two lines, affiliations, a bold venue line and five charcoal pill buttons with white icons. The Abstract sits on white in two half columns: justified 20px text on the left and a square looping video (10px radius) with a centred caption on the right. Sections then alternate between white and #f5f5f5 bands (Setting, Method, Results, Efficiency, Bad Data → Online RL, Analysis, Scaling, BibTeX). Key statements are set in blue-bordered callouts with a faint blue wash; figures are captioned in slate #64748b; task names appear as Bulma's red-on-grey inline code. Body text is slate #1e293b.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): light grey #f5f5f5 37.0% (the hero band), white #ffffff 35.6% plus near-whites #fafafa 2.2% (navbar and Abstract section); mid grey #8e8f90 17.5% (anti-aliased title, venue and justified abstract text, the dark buttons); cool tint #f1f5f6 5.4% and #f5f6f7 0.9% (the video frame edges). The blue author names and the video's colors are too small to form clusters.

Anatomy in DOM order (desktop 1440px, everything centred in a 960px `.container.is-max-desktop`, x=240–1200):

1. **Fixed navbar** (`nav.navbar.is-fixed-top`, 0–53px): rgba(255,255,255,0.95), 1px #e2e8f0 bottom border; items Noto Sans 16px #4a4a4a, padding 8px 12px, 52px tall; "Back to top" at x=0, anchors from x=300 to 1210, GitHub icon at x=1400.
2. **Hero band** (`section.hero.is-light.is-small.top-hero`, 0–479px): #f5f5f5; `.hero-body` margin-top 80px and padding 24px, so the title column starts at y=104 (Bulma `.columns` -12px margin and `.column` 12px padding cancel).
3. **Title** (`h1.publication-title`, y=104, 92px tall): Google Sans 40px/600 (`2.5rem !important`), line-height 1.15, letter-spacing -0.8px (-0.02em), rgba(0,0,0,0.7), two lines in a 714px three-quarter column; margin-bottom 24px.
4. **Authors** (`.publication-authors`, y=220, 75px): Google Sans 20px, line-height 30px, names #0e78be (hsl(204,86%,40%), underline on hover), comma-separated with superscripts, two lines 5.6px apart.
5. **Affiliations** (y=303, 8px below): 20px rgba(0,0,0,0.7) with superscripts.
6. **Venue** (`p.publication-venue`, y=347, 9.6px below): "Transactions on Machine Learning Research (TMLR), 2026", Noto Sans 20px/600, rgba(0,0,0,0.9).
7. **Buttons** (`.publication-links`, y=415, 40px tall): in a `column is-12 mt-4` (16px margin + 12px padding below the column above); Paper (PDF), arXiv, OpenReview, Journal/Publisher Site, Code; gap 10.4px. The hero ends at y=479 (455 + 24px padding).
8. **Abstract** (`section.section`, white, padding 48px 24px; h2 at y=527): "Abstract" Noto Sans 32px/600 #363636, margin-bottom 32px; two `column is-half` (492px with 12px padding): text at x=240, y=595, Noto Sans 20px, line-height 30px, #1e293b, justified; video at x=732, y=603, 468×468px.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Ink | #1e293b | (body) | body text, abstract, callout text, list items |
| White | #ffffff | (literal) | Abstract and alternate section backgrounds, button text and icons |
| Navbar White | rgba(255,255,255,0.95) | (literal) | fixed navbar background |
| Light Grey | #f5f5f5 | (Bulma `is-light`, `has-background-light`) | hero band, every second section band, BibTeX `pre`, inline `code` background |
| Title Ink | rgba(0,0,0,0.7) | (Bulma `.hero.is-light .title`) | paper title, affiliations |
| Venue Ink | rgba(0,0,0,0.9) | (Bulma `.hero.is-light .subtitle`) | venue line |
| Heading Grey | #363636 | (Bulma `.title`, `strong`, `is-dark`) | h2, h3, bold text in callouts, pill button fill |
| Nav Grey | #4a4a4a | (Bulma `.navbar-item`, `pre`) | navbar links, BibTeX text |
| Author Blue | #0e78be | hsl(204, 86%, 40%) | author names, active nav item |
| Callout Blue | #1086d5 | hsl(204, 86%, 45%) | 4px callout left border |
| Callout Wash | rgba(59,130,246,0.06) | (literal) | callout gradient start |
| Link Blue | #3273dc | (Bulma link) | links inside text and callouts |
| Caption Slate | #64748b | (literal) | figure captions |
| Rule | #e2e8f0 | (literal) | navbar bottom border, task-image borders |
| Code Red | #da1039 | (Bulma `code`) | inline task names (IIWA, Box, PickPlace) |
| Footer Grey | #fafafa | (Bulma `.footer`) | footer background |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors | 'Google Sans', sans-serif | Google Sans 400; 600 is synthesised bold | Outfit |
| Body / headings | 'Noto Sans', sans-serif | Noto Sans 400; 600/700 synthesised | Open Sans |
| Code | monospace | system monospace (Consolas on Windows) | IBM Plex Mono |
| Icons | Font Awesome 5 (SVG), Academicons | inline SVG; Academicons 400 for arXiv | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.publication-title` | 40px / 600 / 1.15, letter-spacing -0.02em | rgba(0,0,0,0.7) |
| Section title | `h2.title.is-3.section-heading` | 32px / 600 / 1.125, letter-spacing -0.01em, margin-bottom 32px | #363636 |
| Subsection | `h3.title.is-4` | 24px / 600 / 1.125 | #363636 |
| Authors | `.publication-authors` | Google Sans 20px / 400 / 1.5 | #0e78be names |
| Venue | `.publication-venue` | Noto Sans 20px / 600 / 1.25 | rgba(0,0,0,0.9) |
| Abstract / callout / list | `.content.is-size-5 p`, `.callout-new`, `.pipeline-steps li` | 20px / 400 / 1.5 | #1e293b |
| Abstract caption | `.has-text-centered.is-size-6` | 16px / 400 / 1.5 | #1e293b |
| Figure caption | `.figure-caption` | 16.8px (1.05rem) / 400 / 1.45 | #64748b |
| Inline code | `code` | 14.7px, padding 3.675px 7.35px | #da1039 on #f5f5f5 |
| Button | `.button.is-rounded.is-dark` | 16px / 400 | #ffffff |
| Navbar item | `.navbar-item` | 16px / 400 | #4a4a4a |
| BibTeX | `pre` | 14px / 1.5 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill buttons | 290486px (Bulma `is-rounded`) | 1px transparent | none |
| Callout | 0 8px 8px 0 | 4px solid #1086d5 left | none |
| Abstract video | 10px | none | none |
| Task images (`.compo-grid img`) | 8px | 1px #e2e8f0 | none |
| Navbar | 0 | 1px #e2e8f0 bottom | none |
| BibTeX `pre` | 0 | none | none |
| Inline code | 0 | none | none |

## Layout Metrics

- **Container**: `.container.is-max-desktop` → 960px at x=240 (Bulma's desktop max for this class).
- **Hero**: 479px tall; hero body margin-top 80px (clears the fixed navbar), padding 24px; title column `is-three-quarters` (714px text width); title→authors 24px, authors→affiliations 8px, affiliations→venue 9.6px, venue→buttons 40px (column padding 12 + `mt-4` 16 + column padding 12).
- **Sections**: `.section` padding 48px 24px (Bulma); section title margin-bottom 32px; bands alternate white and #f5f5f5.
- **Abstract**: two `is-half` columns of 492px including 12px padding → 468px text and 468px video, 24px apart.
- **Callout**: full 960px, padding 16px 20px, margin 20px 0 24px.
- **Task grid** (`.compo-grid`): `repeat(auto-fit, minmax(140px, 1fr))`, gap 12px → four 231px images (two empty tracks remain at 0px).
- **Figures**: full 960px width with captions 8px below.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px (incl. 1440) | 960px container | 16px (content 20px) | 40px | navbar items inline; two-column abstract |
| 769–1023px | 24px section padding, container fluid | 16px | 40px | columns stay side by side |
| ≤768px | 24px | 16px | 40px (fixed by `!important`) | navbar collapses to a burger; Bulma columns stack (abstract text above video); hero body padding-top 2rem declared but still 24px from Bulma |

## Components

- **Pill button** (`.button.is-rounded.is-dark`): #363636 fill, white Noto Sans 16px, padding 7px 20px, fully rounded, 40px tall; a 24px white icon box (file-pdf, X/arXiv via Academicons, file, book, GitHub) with -9px left and 4px right margin. Bulma hover darkens the fill.
- **Fixed navbar**: 53px, rgba(255,255,255,0.95), 1px #e2e8f0 bottom; text-only anchors 16px #4a4a4a with 8px 12px padding; a script adds `.is-active-nav` to the item for the visible section, which turns it #0e78be (no item is active at load).
- **Callout** (`.callout-new`): `border-left: 4px solid hsl(204, 86%, 45%)`, `background: linear-gradient(90deg, rgba(59,130,246,0.06), transparent)`, padding 16px 20px, radius 0 8px 8px 0; 20px #1e293b text with bold #363636 numbers and #3273dc links.
- **Task image row** (`.compo-grid`): square simulator renders with 8px radius and 1px #e2e8f0 border; caption below with a "(a)" label and red inline-code task names, 16.8px #64748b.
- **Figure + caption**: full-width image, caption 16.8px #64748b, line-height 1.45, centred, 8px above.
- **Step list** (`.pipeline-steps`): unbulleted list, 20px items 16px apart.
- **BibTeX**: Bulma `pre` on #f5f5f5, padding 17.5px 21px, 14px #4a4a4a.
- **Footer**: #fafafa, centred corresponding-author line and Nerfies credit.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed section navbar | yes | white translucent bar with nine anchors and a GitHub icon |
| Title / authors / affiliations / venue | yes | centred on a #f5f5f5 hero, blue names |
| Link buttons | yes | five charcoal pills with white icons |
| Abstract | yes | two columns: justified 20px text beside a square video |
| Teaser video | yes | 468px looping video with 10px radius and a centred caption |
| Callouts | yes | blue left-ruled boxes with a faint blue wash |
| Figures | yes | full-width figures with slate captions, task image grids |
| Results tables | present but non-standard | results appear as figure images, no HTML tables |
| Method steps | yes | unbulleted step list |
| BibTeX | yes | plain grey `pre` |
| Footer | yes | #fafafa footer with credit |
| Dark mode | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep the 20px Google Sans author block in the 714px column; it wraps to a third line with 5.6px between lines.
- **More buttons**: add `.button.is-rounded.is-dark` pills to the flex row (gap 10.4px, wrapping, centred).
- **An HTML results table**: place it on a white or #f5f5f5 band at 960px; header 16px/600 #363636 with a 1px #e2e8f0 bottom rule, body 16px #1e293b, best values bold; caption below in 16.8px #64748b.
- **Key takeaways or news**: one `.callout-new` per item (4px #1086d5 left border, blue wash, 16px 20px padding) with the date or number in bold #363636.
- **More sections**: alternate the band color (white, then #f5f5f5) and add an anchor to the navbar.

## Do's and Don'ts

- Do alternate white and #f5f5f5 section bands; this is the page's main rhythm.
- Do put the most important sentence of each section in a blue-ruled callout.
- Do keep buttons charcoal pills with white icons.
- Do set long text at 20px with 1.5 line-height; it is justified in the abstract.
- Don't add color fills to sections; blue appears only in names, links and the callout rule.
- Don't round figures beyond 8–10px or add shadows.
- Don't rely on the custom sheet's venue color (#64748b); the rendered venue is near-black.

## Surfaces

Flat bands: a #f5f5f5 hero, then alternating #ffffff and #f5f5f5 sections, a translucent white fixed navbar and a #fafafa footer. Callouts add a left-to-right blue wash; nothing else is tinted.

## Imagery

Simulator renders of robot arms (IIWA, Jaco, Panda, Kinova3) at a table with coloured objects, square thumbnails and wide montages; a square looping video of many task tiles with an "EXPERT DATA" stamp; plots and diagrams as images. Images use 8–10px radii and thin #e2e8f0 borders.

## Layout

A centred 960px column under a fixed navbar. Hero band → Abstract (two columns) → Setting (callout, four-up task grid, task-indicator diagram, montages) → Method (callouts and step lists) → Results, Efficiency, Bad Data, Analysis, Scaling → BibTeX → footer, each section a full-width band with 48px vertical padding.

## Agent Prompt Guide

Quick colors: text #1e293b, headings #363636, page bands #ffffff and #f5f5f5, author blue #0e78be, callout rule #1086d5, link #3273dc, captions #64748b, rule #e2e8f0.

1. "Build a fixed 53px navbar with background rgba(255,255,255,0.95) and a 1px #e2e8f0 bottom border; text-only anchors in Noto Sans 16px #4a4a4a with 8px 12px padding; the active one #0e78be. Below it a #f5f5f5 hero with a centred Google Sans 40px/600 title (line-height 1.15, letter-spacing -0.02em, rgba(0,0,0,0.7)), 20px authors in #0e78be, a 20px/600 venue line, and #363636 pill buttons (padding 7px 20px, fully rounded, white text and icons, gap 10.4px)."
2. "Make a callout: border-left 4px solid #1086d5, background linear-gradient(90deg, rgba(59,130,246,0.06), transparent), padding 16px 20px, border-radius 0 8px 8px 0, 20px #1e293b text with key numbers in bold #363636."
3. "Lay out a section band (padding 48px 24px, alternating #ffffff and #f5f5f5) with a centred 32px/600 #363636 title 32px above the content, a four-up grid of 231px square images (gap 12px, radius 8px, 1px #e2e8f0) and 16.8px #64748b captions."

## Similar Pages

- Nerfies-template pages extended with a fixed section navbar and alternating grey/white section bands.
- Robot-learning project pages that pair a justified abstract with a looping video and use callouts for key numbers.

## Quick Start

```css
:root {
  --ink: #1e293b;
  --heading: #363636;
  --band: #f5f5f5;
  --white: #ffffff;
  --nav-text: #4a4a4a;
  --author: #0e78be;
  --callout: #1086d5;
  --link: #3273dc;
  --caption: #64748b;
  --rule: #e2e8f0;
  --code: #da1039;
  --font-title: "Google Sans", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --container: 960px;
  --section-pad: 48px 24px;
}
```

## Provenance

- **URL**: https://anhquanpham.github.io/iterative-comp-rl-generation/
- **Paper**: Iterative Compositional Data Generation for Robot Control, Anh-Quan Pham, Marcel Hussing, Shubhankar P. Patankar, Dani S. Bassett, Jorge Mendez-Mendez, Eric Eaton (University of Pennsylvania; Stony Brook University).
- **Venue**: TMLR 2026 (OpenReview cASorO1kiy, May 2026).
- **Selection reason**: linked from the jmlr.org/tmlr/papers accepted list; curl returned 200 text/html.
- **Template credit**: footer reads "Website adapted from" the Nerfies template; Bulma 0.9, Font Awesome 5, Academicons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the hero, authors, buttons, sections, callouts, task grid, captions, video, list, BibTeX and footer, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
