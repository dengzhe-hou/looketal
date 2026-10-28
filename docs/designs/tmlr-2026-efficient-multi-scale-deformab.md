# Efficient MSDA — Style Reference

> A journal offprint set by a careful compositor: serif prose in a 34em measure, italic notes in the left margin, and one thin red rule to say where the article begins.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own Nuxt stylesheet `_nuxt/entry.DzMFe2QY.css` and `index.html`. The site ships a dark scheme (class `scheme-dark` on `<html>`, switched by a cog button in the footer through `scheme.js`); the default render is light and the dark values are listed separately. All numbers below are what renders at 1440 unless a breakpoint is named.

## Overview

A short (3,728px) article-style project page that reads like a typeset journal paper rather than a web landing page. White ground, near-black ink #181b1b, and a single brick red #c52023 used sparingly: the "EFFICIENT-MSDA" kicker and its 2px rule, list numerals, inline links and the `pip`/`@article` tokens in code. Prose is Source Serif 4; all apparatus (labels, buttons, rails, navigation) is Figtree, mostly in uppercase or all-small-caps with wide tracking. The layout is a three-column grid inside a 1150px sheet: a 160px right-aligned left rail (site name, venue, date, then italic margin notes), a 612px text column, and a free right column that holds a fixed "On this page" list. Sections are introduced by a full-width 1px black rule broken by an all-small-caps heading in the rail ("—— SUMMARY ————"). There are no figures, videos or tables; the page is pure typography plus two light-grey code exhibits.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 84.6%, plus near-white #fcfbfb / #fffffd / #fdffff 2.5%; anti-aliased text greys #bfbbbb 4.6%, #d7d8d7 3.2%, #909091 2.8%; #f0f1f1 2.2%. Red #c52023 is present (kicker, rule, numerals, link) but too small to form a cluster.

Anatomy in DOM order (desktop 1440px). `.paper` is 1150px wide with 24px padding (content x=169–1271); `main.paper-main` adds 16px top padding, so content starts at y=40.

1. **Left rail masthead** (`.title-topbar.fill-text`, x=169–329, y=40, 21px tall): "RESEARCH.KHWS.IO", Figtree 11.2px/750 uppercase, letter-spacing 1.12px, #181b1b, right-aligned, with a 2px solid #181b1b bottom border; margin-bottom 17.6px.
2. **Venue block** (`a.venue`, y=78): "TMLR" 16.16px/650 #181b1b, then "Transactions on Machine Learning Research" 12.62px/400, right-aligned, wraps to two lines; date "September 2026" (`time`) at y=160, 12.62px #48504f.
3. **Kicker** (`.title-topbar.fill-theme`, x=370–982, y=40, 21px): "EFFICIENT-MSDA" 11.2px/750 uppercase, letter-spacing 1.12px, #c52023, 2px solid #c52023 bottom border across the full 612px column; margin-bottom 17.6px.
4. **Title** (`h1`, y=78, 75px tall): Source Serif 4 34.2px/600, line-height 37.62px (1.1), letter-spacing -0.171px, #181b1b, left-aligned, two lines; margin-bottom 25.65px, then the author list's 7.2px top margin.
5. **Author** (y=186): "Kurt H.W. Stolle" Figtree 19.08px/420 #181b1b; affiliation "Eindhoven University of Technology" 15.84px/420 at y=213. Block is 48px tall; 24px to the buttons.
6. **Link buttons** (`.title-actions nav`, y=258, 29px tall): PAPER (filled), GITHUB and REVIEWS (outlined), 12px apart. Bottom of the header is y=287.
7. **Lede** (`.plain-summary p`, y=301): Source Serif 4 20.88px/400, line-height 30.9px, #181b1b, five lines to y=455. The section starts 96px below the header minus its -81.6px pull-up margin (287 + 96 − 81.6 = 301).
8. **Findings** (y=482, 25.6px below): "FINDINGS" label 11.2px/750 uppercase #48504f, then an ordered list (y=506–846) whose numerals are Figtree 14.32px/650 #c52023, right-aligned in a 35.2px gutter; each item is a 600-weight serif lead, an em-dash in muted grey, and a 400-weight serif detail at 18.36px/26.6px.
9. **Library note** (y=871): "LIBRARY" label, then one serif sentence with two red underlined links; the block ends at y=948.
10. **Right rail** (`nav.rail-nav.rail-nav-fixed`, fixed, x=1023, top 96px): "ON THIS PAGE" 11.2px/750 #48504f, then SUMMARY / LIBRARY / CITATION in 14.04px/700 uppercase, letter-spacing 0.84px, #181b1b with a dotted #9aa1a0 underline, rows 24px tall.

The first section rule ("SUMMARY") sits below the fold at y=1053.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | --paper | page background, rail and sticky rail-title backgrounds, text on filled buttons |
| Ink | #181b1b | --ink-900 | body text, h1, h3, rail titles, author, venue, masthead and its 2px rule, section rules, button fill and outline, footer top border, footer handle |
| Rail Ink | #475252 | --text-rail (hsl 178 7.2% 30%) | left-rail margin notes, venue/date block wrapper, "Citation downloads" label |
| Muted | #48504f | --ink-600 / --text-muted | "FINDINGS"/"LIBRARY"/"ON THIS PAGE" labels, date, code-shell language label, footer text, em-dash after list leads |
| Dotted Rule | #9aa1a0 | --ink-300 | dotted underline of right-rail links, code punctuation |
| Brick Red | #c52023 | --red-500 / --link | kicker text and its 2px rule, list numerals, inline links, `pip` and `@article` code tokens |
| Red Hover | #a51a1d | --red-600 | inline link hover |
| Link Underline | rgba(197,32,35,0.42) | --link-underline | 1px underline under inline links |
| Exhibit Grey | #f5f7f6 (rendered color(srgb .9627 .9667 .9653)) | --surface-exhibit = color-mix(ink-100 34%, paper) | code-shell background (pip install, BibTeX) |
| Hover Wash | #f6f7f7 | --ink-025 / --button-line-hover-bg | outline and quiet button hover fill |
| Button Hover | #2b3130 | --ink-700 / --button-bg-hover | filled button hover fill and border |
| Paper Off | #fcfcfc | --paper-off | rail note boxes at ≤520px |
| Hairline | #e3e6e5 | --ink-100 | disabled button border, exhibit caption rule |
| Dark Paper | #121515 | --paper (dark, hsl 178 7.2% 7.8%) | page background in dark scheme |
| Dark Ink | #eaeeed | --ink-900 (dark) | text in dark scheme |
| Dark Red | #e8595b | --red-500 (dark) | accent in dark scheme |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / apparatus | "Figtree", "Figtree Fallback: sans-serif", "Nunito Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif | Figtree 300–900 (variable) | Nunito Sans |
| Prose / headings | "Source Serif 4", "Source Serif 4 Fallback: serif", "Source Serif Pro", Georgia, serif | Source Serif 4 200–900 roman and italic (variable) | Source Serif Pro |
| Code | "Source Code Pro", "Source Code Pro Fallback: monospace", "Fira Code", monospace | Source Code Pro 200–900 | IBM Plex Mono |

The body enables oldstyle, proportional numerals, discretionary ligatures and slashed zero (`font-variant-numeric: ordinal oldstyle-nums proportional-nums stacked-fractions slashed-zero`); figures in prose sit below cap height.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title-block h1` | 34.2px (1.9em) / 600 / 1.1, letter-spacing -0.005em, `font-variant-caps: titling-caps` | #181b1b |
| Section head (rail) | `h2.rail-title` | 24.64px (1.54rem) / 450 / 1.18, letter-spacing 2.464px (0.1em), `all-small-caps`, right-aligned | #181b1b |
| Subsection | `.paper-block h3` | Source Serif 4 21.6px / 600 / 1.1; margin 0 0 9.72px | #181b1b |
| Lede | `.plain-summary p` | Source Serif 4 20.88px / 400 / 30.9px | #181b1b |
| Body prose | `.paper-block p`, `.contributions li` | Source Serif 4 18.36px / 400 / 27.54px (lists 26.62px) | #181b1b |
| Finding lead | `.contributions li strong` | Source Serif 4 18.36px / 600, followed by " — " in 400 #48504f | #181b1b |
| List numeral | `ol li::before` | Figtree 14.32px / 650, right-aligned in 35.2px | #c52023 |
| Margin note | `.margin-note:not(.title-aside) p` | Source Serif 4 16.07px / 400 italic / 23.15px, right-aligned; `strong` stays italic 600 | #475252 |
| Mini label | `.label-mini`, `.rail-nav-label`, `.code-shell-lang` | Figtree 11.2px (0.7rem) / 750, uppercase, letter-spacing 1.12px | #48504f |
| Kicker / masthead | `.title-topbar a` | 11.2px / 750 uppercase, letter-spacing 1.12px | kicker #c52023, masthead #181b1b |
| Author name | `.author-name a` | Figtree 19.08px / 420 / 24.8px | #181b1b |
| Affiliation | `.author-affiliation a` | Figtree 15.84px / 420 / 21.38px | #181b1b |
| Button (small) | `.button.button-sm` | Figtree 12.96px / 650 / 1, uppercase, letter-spacing 1.296px | per variant |
| Right-rail link | `.rail-nav a` | Figtree 14.04px / 700 / 17.55px, uppercase, letter-spacing 0.84px | #181b1b |
| Inline link | `p a` | inherits serif, 600, underline 1px rgba(197,32,35,.42), offset 0.16em | #c52023 |
| Code | `.code-shell > code.listing` | Source Code Pro 15.48px / 430 / 24px | #181b1b |
| Footer | `.site-footer` | Figtree 15.12px / 400; handle (`.site-footer-handle` and its link) 15.88px / 800 all-small-caps | text, links, copyright #48504f; handle #181b1b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons (all variants) | 999vh (renders 8991px, full pill) | 1px solid #181b1b; quiet variant transparent | none; focus ring 0 0 0 3px hsl(178 7.2% 20% / 26%) |
| Kicker | 0 | 2px solid #c52023 bottom | none |
| Masthead | 0 | 2px solid #181b1b bottom | none |
| Section rule | 0 | 1px solid #181b1b top (`.section-head-line`) | none |
| Code shell | 0 | none | none |
| Footer | 0 | 1px solid #181b1b top | none |
| Rail-title fade | 0 | none | `::after` 28.8px strip, `linear-gradient(rgb(255, 255, 255), rgba(255, 255, 255, 0))` |

Base spacing unit `--spacing: 1.5rem` (24px). The page uses no shadows and no rounded boxes besides the pills.

## Layout Metrics

- **Sheet**: `.paper { max-width: 1150px; margin: 0 auto; padding: 24px }` → x=145–1295, content 169–1271 (1102px). From 1600px up `--measure-max` drops to 980px.
- **Grid**: every `.paper-section` is `display: grid; grid-template-columns: 160px minmax(0, 34em) 1fr; column-gap: 40.8px` → rail 169–329, text 370–982 (612px = 34em at 18px), free column 1023–1271 (248px).
- **Vertical rhythm**: `main.paper-main` is a grid with `gap: 96px` (4×spacing) and padding 16px 0 192px; the lede section is pulled up by `margin-top: calc(-96px + .9rem)` = -81.6px so it reads as part of the header.
- **Section head**: a full-width grid row (1102px) holding a 39px rule, the right-aligned rail title, and a 633px rule across the text column; margin-bottom 38.4px (1.8rem + .6rem). The rail title is `position: sticky` with a white background and a 28.8px white-to-transparent fade below.
- **Right rail**: `nav.rail-nav-fixed` is `position: fixed; top: 96px; width: 160px`, its `left` set from the script variable `--right-rail-left` (renders x=1023).
- **Code shell**: bleeds 12.8px into both gutters (`margin: 48px -12.8px; padding: 12.8px`), so it renders 638px wide at x=357.
- **Footer**: margin-top 96px, padding-top 16px, three-column grid 160px / 1fr / auto.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1600px | 24px | 18px | 34.2px | sheet max-width 980px |
| 1200–1599px (incl. 1440) | 24px | 18px | 34.2px | rail column 10rem = 160px |
| <1200px | 24px | 18px | 34.2px | rail column 12rem = 216px |
| ≤760px | 24px | 18px | 34.2px | footer single column, copyright left |
| ≤520px | 0 (`.paper-main` padding 0) | 18px | 34.2px | grid becomes block; section heads become a plain 1px top rule with a left-aligned title; rail notes become #fcfcfc boxes with a 1px #e3e6e5 border and a 3px red left border |

## Components

- **Kicker rule** (`.title-topbar.fill-theme`): full text-column width, Figtree 11.2px/750 uppercase, letter-spacing 1.12px, #c52023, `border-bottom: 2px solid #c52023`, margin-bottom 17.6px. The rail twin (`.fill-text`) uses #181b1b for both text and rule and is right-aligned.
- **Filled pill button** (`.button.button-sm`): #181b1b fill, 1px #181b1b border, white Figtree 12.96px/650 uppercase text, letter-spacing 1.296px, padding 6.86px 14.43px, radius 999vh, renders 29px tall. Hover: fill and border #2b3130; active: #000 and translateY(1px).
- **Outline pill button** (`.button-outline`): transparent fill, 1px #181b1b border, #181b1b text; hover fill #f6f7f7 and text #000. A "quiet" variant has a transparent border (the COPY button).
- **Section head**: 1px #181b1b rule split around an all-small-caps Figtree 24.64px/450 title (letter-spacing 2.464px) that is right-aligned in the 160px rail, 20px clear of the rule on its left; the title sticks while its section scrolls.
- **Numbered findings** (`.contributions ol`): items margin-left 35.2px; numeral in `::before`, Figtree 14.32px/650 #c52023, right-aligned with 12.2px right padding; bold serif lead, grey em-dash, serif detail; 10.1px between items.
- **Margin note** (`.margin-note`): right-aligned italic Source Serif 4 16.07px/23.15px #475252 in the 160px rail, aligned with the paragraph it glosses; bold terms stay italic at 600; links inside are #c52023.
- **Inline link** (`p a`): #c52023 600, 1px underline rgba(197,32,35,.42) offset 0.16em; hover #a51a1d with a 2px currentColor underline.
- **Right-rail contents** (`.rail-nav-fixed`): "ON THIS PAGE" mini label, then uppercase 14.04px/700 links with dotted #9aa1a0 underline, 2.7px row gap; hover or `aria-current` turns text and underline #c52023.
- **Code shell** (`.code-shell`): #f5f7f6 block, no radius, 12.8px padding; header row with "SHELL"/"BIBTEX" mini label left and a quiet COPY pill right; code Source Code Pro 15.48px/430, line-height 1.55, lead token #c52023 520, field names 500, punctuation #9aa1a0.
- **Citation downloads** (rail of Citation section): italic serif label "Citation downloads" 16.8px #475252, then right-aligned outline pills BIBTEX / RIS / ENDNOTE / PLAIN TEXT at 12.31px.
- **Footer**: 1px #181b1b top rule, handle "research.khws.io" 15.88px/800 all-small-caps in #181b1b, muted #48504f links, a cog scheme switch, copyright right-aligned.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Masthead / site name | yes | 11.2px uppercase with 2px black rule, top of left rail |
| Venue and date | yes | right-aligned rail block, "TMLR" 650 over full name and date |
| Title / author / affiliation | yes | serif title, sans author, single author, no superscripts |
| Link buttons | yes | one filled and two outlined uppercase pills, no icons |
| TL;DR / lede | yes | 20.88px serif paragraph directly under the buttons |
| Key findings | yes | numbered list with red numerals and bold serif leads |
| Table of contents | yes | fixed right-rail "On this page" list |
| Abstract | present but non-standard | no "Abstract" heading; the lede and the Summary section replace it |
| Margin notes | yes | italic serif glosses in the left rail |
| Teaser / figures / video | absent from the source | no images at all |
| Results tables | absent from the source | findings are given as prose with numbers |
| Code install snippet | yes | grey code shell with SHELL label and COPY button |
| BibTeX | yes | same code shell, plus download pills in the rail |
| Dark scheme | yes | footer cog toggles `scheme-dark` |
| Footer | yes | ruled, three-column |

## Adapting to Other Content

- **More authors**: keep `.author-list` as a flex row (gap 16.2px 43.2px); each author is a 19.08px/420 name over a 15.84px affiliation, so four authors fit per line in the 612px column. Use red Figtree 0.72em superscript numerals for shared affiliations, matching the `.affiliations li::before` rule.
- **A results table**: place it in the text column on the #f5f7f6 exhibit surface with 12.8px padding; header row in Figtree 11.2px/750 uppercase #48504f, cells in Source Code Pro 15.48px with tabular numerals, best values in 600 weight #181b1b (not red); caption below in Figtree 15.84px (.88em) #48504f above a 1px #e3e6e5 rule, led by a red 9.9px (.62rem) uppercase "TABLE 1" label as in `.exhibit-num`.
- **Figures**: full 612px column width, caption Figtree 16.2px (.9em) / 600 #181b1b; put any gloss in a margin note instead of a long caption.
- **Long publication or news lists**: use the findings list pattern (red Figtree numerals or dates in the 35.2px gutter, serif bold lead, grey em-dash, serif detail) rather than cards.
- **More sections**: each new section gets the ruled all-small-caps rail head and a right-rail link; keep the 96px gap between sections.

## Do's and Don'ts

- Do keep red #c52023 for the kicker, numerals and links only; headings and buttons stay #181b1b.
- Do set prose in Source Serif 4 and everything that is navigation or metadata in Figtree uppercase or small caps with 0.06–0.1em tracking.
- Do put glosses, venue and date in the right-aligned 160px left rail.
- Do keep buttons as small uppercase pills, one filled and the rest outlined.
- Don't add cards, shadows, colored bands or rounded panels; separation comes from 1px rules and 96px gaps.
- Don't widen the text column beyond 34em (612px).
- Don't center anything; every block is left-aligned in its column, and rail content is right-aligned.

## Surfaces

One white sheet (#ffffff) with no section bands. The only tinted surface is the code shell (#f5f7f6) that bleeds 12.8px past the text column. Sticky rail titles carry a white background and a white-to-transparent fade so scrolling text slides under them.

## Imagery

None. The page has no teaser, figures or video; all evidence is prose with figures in oldstyle numerals. A reproduction should not invent imagery; if a figure is unavoidable, render it at the 612px text width on white with a Figtree caption.

## Layout

A 1150px sheet split into a 160px rail, a 612px serif column and a 248px free column with a fixed contents list. The header block, lede and findings form the first screen; then three ruled sections (Summary, Library, Citation) separated by 96px, and a ruled footer.

## Agent Prompt Guide

Quick colors: paper #ffffff, ink #181b1b, rail notes #475252, muted labels #48504f, accent #c52023, dotted rule #9aa1a0, exhibit #f5f7f6.

1. "Build an article header in a 3-column grid (160px | 612px | 1fr, column-gap 40.8px) inside a 1150px sheet with 24px padding. Left rail, right-aligned: 'RESEARCH.KHWS.IO' in Figtree 11.2px/750 uppercase, letter-spacing 1.12px, #181b1b, 2px #181b1b bottom border; below it the venue in 16.16px/650 and the date in 12.62px #48504f. Text column: kicker in the same 11.2px style but #c52023 with a 2px #c52023 bottom border across 612px, then a Source Serif 4 34.2px/600 title (line-height 1.1, letter-spacing -0.005em), author 19.08px/420, affiliation 15.84px/420."
2. "Make link buttons: uppercase Figtree 12.96px/650 pills, letter-spacing 1.296px, padding 6.86px 14.43px, radius 999vh, 1px #181b1b border. First one filled #181b1b with white text, the rest transparent with #181b1b text; hover fill #f6f7f7 for outlined ones. 12px apart."
3. "Create a section head: a full-width row with a 1px #181b1b rule interrupted by an all-small-caps Figtree 24.64px/450 title (letter-spacing 0.1em) right-aligned in the 160px left rail, 20px clear of the rule; 38.4px below it, start Source Serif 4 prose at 18.36px/1.5 #181b1b, and put italic 16.07px #475252 margin notes right-aligned in the rail next to the paragraphs they explain."

## Similar Pages

- Hand-built "paper as article" project pages that use a margin rail and serif prose, in the Tufte CSS / Distill tradition.
- Personal research sites built on a single Nuxt template where each paper page reuses the same masthead, kicker and ruled section heads.

## Quick Start

```css
:root {
  --paper: #ffffff;
  --ink: #181b1b;
  --rail: #475252;
  --muted: #48504f;
  --dotted: #9aa1a0;
  --accent: #c52023;
  --accent-hover: #a51a1d;
  --exhibit: #f5f7f6;
  --font-sans: "Figtree", "Nunito Sans", -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-serif: "Source Serif 4", "Source Serif Pro", Georgia, serif;
  --font-mono: "Source Code Pro", "Fira Code", monospace;
  --body: 18px;
  --measure: 34em;
  --rail-width: 160px;
  --rail-gap: 40.8px;
  --sheet: 1150px;
  --section-gap: 96px;
  --radius-pill: 999vh;
}
.scheme-dark {
  --paper: #121515;
  --ink: #eaeeed;
  --accent: #e8595b;
}
```

## Provenance

- **URL**: https://research.khws.io/efficient-msda/
- **Paper**: Efficient Multi-Scale Deformable Attention on GPUs, Kurt H. W. Stolle (Eindhoven University of Technology).
- **Venue**: TMLR 2026 (OpenReview Q4jZ7zKNKx, September 2026).
- **Selection reason**: linked from the jmlr.org/tmlr/papers accepted list; curl returned 200 text/html.
- **Template credit**: none stated; a custom Nuxt site (`research.khws.io`) with Iconify Lucide icons; footer reads "© 2026 Kurt H.W. Stolle. All Rights Reserved".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the kicker, numerals (`::before`), section rules, rail-title `::after`, margin notes and buttons, the 1440×900 and full-page screenshots, and `entry.DzMFe2QY.css` and `index.html` read directly, on 2026-10-28.
