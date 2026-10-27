# CHAI Film Slate — Style Reference

> A festival programme printed on cool paper: Garamond headlines, typewriter tags, and a black screening room just past the title.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, scrolled captures of the full 13,924px page, and the page's single inline `<style>` block (about 1,060 lines with CSS custom properties); there is no framework. Color share is measured on the first 1440×900 viewport.

## Overview

A carefully art-directed, magazine-like page. A sticky, frosted nav carries a Garamond "CHAI" wordmark with a tiny gold "CVPR '26" tag, eight muted section links split by hairlines and a black "Code" button. The hero is centred on a cool off-white (#f7f7f9): a two-part mono badge (pale gold "★ CVPR 2026 HIGHLIGHT" joined to solid gold "TOP 3%"), a muted Garamond tagline, a 57.6px EB Garamond semibold headline, a short DM Sans subtitle with bold key numbers, blue author links among grey names, and two rows of mono buttons: four solid black (Paper, Code, Dataset, HuggingFace) and two outlined with small coloured status pills. Directly below, a white "hook" band poses the problem in one paragraph and plays a black 1036px video grid (Ours with a teal frame and green tick against Wan2.7, Veo3, Kling V3, Seedance2). The body follows a strict rhythm: a blue mono eyebrow ("1 SPECIFICATION"), a 38.4px Garamond title, a muted lead, then figures, numbered white cards, red-versus-blue "Prior Work / Ours" illustrations, a results table with a pale blue "Ours" row, a blue-ruled "Key Findings" box, and a dark BibTeX block.

## First Viewport

Color share (1440×900, 8-color quantize): paper #f7f7f9 68.3% (plus near-identical #f7f7fa 5.1%, #f8f7f9 3.2%, #f4f7f7 2.8%), near-white #fcfcfd 8.1% (nav frost and the hook band's top edge), warm grey #edebe7 7.2% (outline buttons, badge and hairlines), taupe #7f7d77 5.2% (muted text and the black buttons at this quantization). The gold badge, black buttons and blue links are each small in area.

Anatomy in DOM order (nav and content share `.container` max-width 1100px with 32px padding, so content runs x=202–1238):

1. **Nav** — `nav.topnav`, sticky, 57px tall, rgba(247,247,249,0.88) with `backdrop-filter: saturate(180%) blur(10px)`, 1px #d9d5cf bottom border. Left: "CHAI" EB Garamond 18.4px / 600 #1a1a1a plus `.topnav__brand-tag` "CVPR '26" (Roboto Mono 9.92px / 700 uppercase, #8a6700 on #ffefbe, 1px #8a6700 border, 3px radius). Right: links DM Sans 13.12px / 500 #6b6560, padding 5.9px 9.84px, 5px radius, 1px #d9d5cf dividers between them; `a.nav-cta` "Code" #ffffff on #1a1a1a. Gap 48px.
2. **Badge pair** — `.hero__badges` inline-flex, 6px radius with `overflow: hidden`; `.hero__badge--award` Roboto Mono 14.72px / 700 uppercase, letter-spacing 0.06em, #8a6700 on #ffefbe with a star icon; `.hero__badge--top` #ffffff on #c9961a, letter-spacing 0.08em; padding 8.8px 17.7px; 340×42px at x=550, y=105. Gap 19px.
3. **Tagline** — `.hero__tagline`, EB Garamond 28.8px / 400 / 37.44px, #6b6560, max-width 720px, two lines (y=166–241). Gap 13px.
4. **Title** — `h1`, EB Garamond 57.6px / 600 / 66.24px, #1a1a1a, max-width 900px, two lines (y=254–386). Gap 26px.
5. **Subtitle** — `.hero__subtitle`, DM Sans 16.8px / 400 / 26.88px, #6b6560 with `b` in #1a1a1a / 600, max-width 680px (y=412–493). Gap 38px.
6. **Authors** — `.hero__authors`, DM Sans 15.2px / 27.36px #6b6560, max-width 800px; linked names #006af3 at weight 400 (y=531–592). Gap 7px.
7. **Affiliations** — `.hero__affiliations`, 13.12px #6b6560 (y=599–624). Gap 33px.
8. **Buttons** — `.hero__links` flex-wrap, gap 12.8px. Row 1: four `a` Roboto Mono 16px / 700 #ffffff on #1a1a1a, padding 9.6px 20.8px, 6px radius, SVG icon left, 51px tall (y=657–708). Row 2: two `a.outline` transparent with 1px #999999 border and #1a1a1a text, icon at 50% opacity, each with a `.btn-pill` (10.88px mono uppercase: #9b6100 on #fcefcc "RELEASING MAY 2026", #0e6b34 on #dcf2e4 "NEURIPS'25 SPOTLIGHT · TOP 3%"), y=733–781. Hero ends at y=846 with a 1px #d9d5cf rule.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Cool Paper | #f7f7f9 | `--bg` | page and hero background, nav frost base |
| Panel Mist | #edf0f4 | `--bg-alt` | "Why CHAI?" band, table header cells, related-pointer cards, nav link hover |
| White | #ffffff | (literal) | hook band, key-point cards, table body, highlight box, collab card, button text |
| Ink | #1a1a1a | `--text`, `--bg-dark` | headlines, body, black buttons, nav "Code", BibTeX block |
| Muted Taupe | #6b6560 | `--text-muted` | tagline, subtitle, authors, affiliations, leads, captions, nav links, footer |
| Link Blue | #006af3 | `a` color (literal) | author links, section eyebrows, key-point numerals, highlight-box rule, best values and "Ours" row figures |
| Deep Blue | #004194 | `--accent` | link hover, outline button hover text |
| Primary Hover | #004493 | `.hero__links a:hover` | black button hover fill |
| Blue Wash | #eff6ff | `--accent-light` | key-point illustration tiles, "Ours" table row |
| Hairline | #d9d5cf | `--border` | section rules, nav border and dividers, card and table borders |
| Outline Grey | #999999 | `.hero__links a.outline` | outline button border |
| Gold Ink | #8a6700 | `.hero__badge--award`, `.topnav__brand-tag` | award badge text, nav tag text and border |
| Gold Cream | #ffefbe | same | award badge and nav tag fill |
| Gold | #c9961a | `.hero__badge--top` | "TOP 3%" badge fill |
| Soon Amber | #9b6100 | `.btn-pill--soon` | "RELEASING" pill text (fill #fcefcc) |
| Soon Cream | #fcefcc | `.btn-pill--soon` | "RELEASING" pill fill |
| Award Green | #0e6b34 | `.btn-pill--award`, `.pill` | spotlight pill text (fill #dcf2e4) |
| Award Mint | #dcf2e4 | same | spotlight pill fill |
| Check Green | #16833b | `.table-wrap .check` | ✓ marks |
| Cross Red | #c0392b | `.table-wrap .cross` | ✗ marks |
| Code Sand | #e0ddd8 | `.bibtex-block` | BibTeX text on #1a1a1a |
| Emphasis Grey | #333333 | `.collab-card .emphasis`, nav-cta hover | collab statement, "Code" hover fill |
| Video Black | #000000 | `.hero-video` | hook video frame background |

## Tokens — Typography

- **Display serif:** `'EB Garamond', Georgia, serif` (Google Fonts, variable 400–800 rendered) for the wordmark, tagline, h1, section titles, sub-headings, key-point numerals and h3s. Substitute: Cormorant Garamond at one weight heavier.
- **Sans:** `--sans: 'DM Sans', system-ui, sans-serif` (variable 300–700 with optical sizes, rendered) for body, nav, leads and tables; the body has `letter-spacing: -0.02em`. Substitute: Inter.
- **Mono:** `--mono: 'Roboto Mono', 'JetBrains Mono', monospace` (Google Fonts request is 400/500/600; the rendered faces are 400 and 600, so every `font-weight: 700` mono label renders with the 600 face) for badges, buttons, eyebrows, pills and BibTeX. Substitute: JetBrains Mono.
- **Declared but not visible:** `--serif: 'Instrument Serif'` is defined and requested from Google Fonts but no visible element uses it.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Wordmark | `.topnav__brand` | 18.4px / 600, EB Garamond |
| Nav links | `.topnav__links a` | clamp(0.7rem, 1.15vw, 0.82rem) = 13.12px / 500 |
| Badges | `.hero__badge` | clamp(0.65rem, 2.6vw, 0.92rem) = 14.72px / 700 mono uppercase |
| Tagline | `.hero__tagline` | clamp(1.1rem, 2.5vw, 1.8rem) = 28.8px / 400 / 1.3 |
| Title | `.hero h1` | clamp(2.2rem, 5vw, 3.6rem) = 57.6px / 600 / 1.15 |
| Subtitle | `.hero__subtitle` | 16.8px / 400 / 1.6 |
| Authors | `.hero__authors` | 15.2px / 400 / 1.8 |
| Hero buttons | `.hero__links a` | 16px / 700 mono |
| Eyebrow | `.section-label` | 11.52px / 700 mono uppercase, letter-spacing 0.1em, #006af3 |
| Section title | `.section-title` | clamp(1.6rem, 3.5vw, 2.4rem) = 38.4px / 500 / 1.2, EB Garamond |
| Lead | `.section-lead` | 16.8px / 400 / 1.7, #6b6560 |
| Card numeral / title | `.key-point__num`, `.key-point h3` | 32px / 400 and 20px / 600, EB Garamond |
| Card text | `.key-point p` | 14.4px / 1.6, #6b6560 |
| Caption | `.fig-block__caption` | 13.6px / 400, "Figure N." bold #1a1a1a |
| Table | `.table-wrap table`, `th` | 13.12px; header 12.48px / 600 uppercase |
| BibTeX | `.bibtex-block` | 12.48px mono, #e0ddd8 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Black / outline buttons | radius 6px, padding 0.6em 1.3em, outline 1px #999999, no shadow |
| Badge pair | radius 6px on the group, `overflow: hidden`, shadow `0 1px 0 rgba(0,0,0,0.03)` |
| Nav tag, pills | radius 3px (pills), 4px (`.pill`) |
| Key-point, stat and collab cards | radius 10px, 1px #d9d5cf border, padding 24px (collab 32px 35px), no shadow |
| Illustration tile | radius 8px, #eff6ff |
| Figures | radius 8px; bordered variant 1px #d9d5cf |
| Hook video | radius 10px, 1px #d9d5cf border, #000000 fill |
| Table | wrapper radius 8px, 1px #d9d5cf, row rules 1px #d9d5cf |
| Highlight box | radius 0 8px 8px 0, 3px #006af3 left border, padding 24px 28.8px |
| BibTeX block | radius 8px, padding 24px, copy button 4px radius on rgba(255,255,255,0.1) |
| Sections | 1px #d9d5cf bottom rule; no shadows anywhere except the lightbox |

## Layout Metrics

- **Container:** `.container` max-width 1100px, padding 0 2rem, so content is 1036px (x=202–1238 at 1440).
- **Hero:** padding 48px 0 64px; text measures 720px (tagline), 900px (title), 680px (subtitle), 800px (authors).
- **Sections:** padding 72px 0 (4.5rem), each closed by a 1px #d9d5cf rule; hook band padding 56px 0 64px on #ffffff; "Why CHAI?" band on #edf0f4.
- **Hook:** lead max-width 760px, video 1036×583 with 32px top margin.
- **Key points:** 4-column grid of 241px cards (24px gaps) with 191×110 illustration tiles.
- **Figures:** `.fig-block` margin 40px 0, images at the full 1036px; two-column variant `1fr 1fr`.
- **Table:** 1036px, header two rows; "Ours" row on #eff6ff.
- **BibTeX:** 1036px dark block; footer padding 40px 0, centred 13.12px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >1000px | 32px | 16px | 5vw capped at 57.6px (cap from 1152px) | key points four across |
| 821–1000px | 32px | 16px | 5vw (41–50px) | key points two across |
| 769–820px | 32px (nav 19.2px) | 16px | 5vw (38.5–41px) | nav collapses to a hamburger dropdown |
| 601–768px | 32px | 16px | 35.2–38.4px (5vw, floor 2.2rem) | `.two-col` stacks |
| ≤600px | 19.2px | 16px | 35.2px | sections padding 48px; hero buttons 42px tall at 14px, two per row, outline buttons full width; all media corners forced to 4px; carousels fill the width |
| ≤480px | 19.2px | 16px | 35.2px | key points one per row |

## Components

- **Frosted sticky nav:** rgba(247,247,249,0.88) with saturate-and-blur backdrop, 1px #d9d5cf bottom border; links #6b6560 13.12px / 500 with 1px hairline separators, hover #1a1a1a on #edf0f4; black "Code" CTA, hover #333333.
- **Split award badge:** two mono uppercase segments in one 6px-radius pill: #8a6700 on #ffefbe with a star, then #ffffff on #c9961a.
- **Mono black button:** Roboto Mono 16px / 700, #ffffff on #1a1a1a, padding 0.6em 1.3em, 6px radius, icon left with 0.7em gap; hover fill #004493.
- **Outline button with status pill:** transparent, 1px #999999, #1a1a1a label, icon at 50% opacity, a 10.88px mono pill inside (amber #9b6100 on #fcefcc, green #0e6b34 on #dcf2e4); hover border #006af3, text #004194, fill #ffffff, icon to full opacity.
- **Section header stack:** blue mono eyebrow with a number ("2 OVERSIGHT"), 38.4px Garamond title, 16.8px muted lead with bold dark phrases.
- **Numbered key-point card:** white, 1px #d9d5cf, 10px radius, padding 24px; a #eff6ff tile with a blue line icon, a 32px Garamond numeral in #006af3, a 20px Garamond title and 14.4px muted text.
- **Results table:** wrapper 1px #d9d5cf with 8px radius; uppercase header on #edf0f4; ✓ #16833b, ✗ #c0392b; "Ours" row on #eff6ff with figures in #006af3 and best values bold.
- **Key findings box:** white, 3px #006af3 left rule, 0 8px 8px 0 radius, mono "Key Findings" title and a muted bullet list with bold dark claims.
- **Related pointer:** #edf0f4 card, 10px radius, white 6px-radius icon tile in #006af3, Garamond title and an optional green pill.
- **Dark BibTeX:** #1a1a1a, #e0ddd8 12.48px mono, 8px radius, translucent "Copy" button top right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky section nav | Yes | frosted bar with wordmark and venue tag |
| Award badge | Yes | split gold mono badge |
| Tagline / title / subtitle | Yes | Garamond tagline and headline, DM Sans subtitle |
| Authors / affiliations | Yes | muted text with blue linked names |
| Link buttons | Yes | four black mono buttons, two outline buttons with pills |
| Hook / teaser video | Yes | white band, one paragraph, black comparison video |
| Overview cards | Yes | four numbered key-point cards |
| Problem / solution illustrations | Yes | red "Prior Work" and blue "Ours" illustrated panels as figures |
| Results table | Yes | HTML table with "Ours" row |
| Key findings | Yes | blue-ruled box |
| Example carousels | Yes | horizontal scrolling cards with mono labels |
| Ecosystem / collaboration | Yes | pointer cards and a collab card |
| Comparison with prior work | Yes | "Why CHAI?" band on #edf0f4 |
| BibTeX | Yes | dark block with copy button |
| Footer | Yes | centred "© 2026 · Zhiqiu Lin" |

## Adapting to Other Content

- **More authors:** the 800px author paragraph wraps naturally at 1.8 line height; link only the names that have pages, as the source does.
- **Fewer badges:** a single-segment badge in #ffefbe / #8a6700 works; keep the gold reserved for awards.
- **More results:** add tables in `.table-wrap`; keep "Ours" as the last row on #eff6ff and best values bold #006af3.
- **News or updates:** a section with a mono eyebrow "NEWS" and a list of rows, each date as a `.btn-pill`-style tag.
- **Long publication lists:** related-pointer cards in a two-column grid on #edf0f4, each with an icon tile and a pill for the venue.
- **No video:** keep the white hook band and put the key comparison figure there; the first scroll should still show a result.

## Do's and Don'ts

- Do pair three voices consistently: EB Garamond for headlines and numerals, DM Sans for prose, Roboto Mono for every label, badge and button.
- Do open every section with a numbered blue mono eyebrow, a Garamond title and a muted lead.
- Do keep surfaces flat: hairline borders (#d9d5cf) and 10px radii, no drop shadows.
- Don't introduce new accent hues; blue #006af3 is the only link and data colour, gold only marks awards.
- Don't centre body sections; only the hero is centred, content below is left-aligned in the 1036px column.
- Don't put the comparison video in the hero; it belongs to the white hook band right after it.

## Surfaces

Cool off-white #f7f7f9 page and hero, white hook band and cards, #edf0f4 for the comparison band, table headers and pointer cards, #eff6ff for illustration tiles and the "Ours" row, #1a1a1a for buttons and BibTeX. Separation is by 1px #d9d5cf rules.

## Imagery

A black video grid of cinematic generations with teal "Ours" frames and green ticks, flat line icons on pale blue tiles, illustrated problem/solution panels with red and blue headers and cartoon people, a colour-coded taxonomy tree, screenshots of annotation tools, and frame-and-caption carousels set in mono.

## Layout

A centred hero, then left-aligned sections in a 1036px column with consistent 72px padding and hairline separators; one full-width white band and one #edf0f4 band break the rhythm. Rendered height about 13,900px.

## Agent Prompt Guide

Quick colors: page #f7f7f9, ink #1a1a1a, muted #6b6560, link and data #006af3 (hover #004194), hairline #d9d5cf, panel #edf0f4, blue wash #eff6ff, award gold #8a6700 on #ffefbe with #c9961a.

1. "Create a hero on #f7f7f9, centred: a split badge (Roboto Mono 14.72px bold uppercase, #8a6700 on #ffefbe joined to #ffffff on #c9961a, 6px radius on the pair), a 28.8px EB Garamond tagline in #6b6560, a 57.6px EB Garamond weight-600 title in #1a1a1a with line-height 1.15, a 16.8px DM Sans subtitle in #6b6560 with bold #1a1a1a numbers, then Roboto Mono 16px bold buttons, #ffffff on #1a1a1a, 6px radius, padding 0.6em 1.3em, hover #004493."
2. "Start each section with a Roboto Mono 11.52px bold uppercase eyebrow in #006af3 with 0.1em letter-spacing ('1 SPECIFICATION'), a 38.4px EB Garamond weight-500 title, and a 16.8px DM Sans lead in #6b6560; sections padded 72px 0 and closed by a 1px #d9d5cf rule, content in a 1100px container with 32px padding."
3. "Build four key-point cards in a grid: #ffffff, 1px #d9d5cf border, 10px radius, padding 24px; inside a #eff6ff tile with a blue line icon, a 32px EB Garamond numeral in #006af3, a 20px EB Garamond weight-600 title, and 14.4px #6b6560 text."

## Similar Pages

- Editorial research landing pages that mix a serif display face with mono labels (product-launch style).
- Video-language and camera-motion benchmark pages from the same group (CameraBench).

## Quick Start

```css
:root {
  --bg: #f7f7f9;
  --bg-alt: #edf0f4;
  --bg-dark: #1a1a1a;
  --text: #1a1a1a;
  --text-muted: #6b6560;
  --link: #006af3;
  --accent: #004194;
  --accent-light: #eff6ff;
  --border: #d9d5cf;
  --gold-ink: #8a6700;
  --gold-cream: #ffefbe;
  --gold: #c9961a;
  --display: 'EB Garamond', Georgia, serif;
  --sans: 'DM Sans', system-ui, sans-serif;
  --mono: 'Roboto Mono', 'JetBrains Mono', monospace;
  --max-w: 1100px;
  --title-size: 57.6px;
  --section-title: 38.4px;
  --body-size: 16px;
  --radius-button: 6px;
  --radius-card: 10px;
}
```

## Provenance

- **URL:** https://linzhiqiu.github.io/papers/chai/
- **Paper:** CHAI: Building a Precise Video Language with Human–AI Oversight (arXiv 2604.21718), Zhiqiu Lin et al., Carnegie Mellon University and Harvard University.
- **Venue:** CVPR 2026, Highlight (badge on the page reads "CVPR 2026 HIGHLIGHT · TOP 3%").
- **Selection reason:** arXiv 2604.21718 comment states acceptance at CVPR 2026 ("CVPR 2026 Highlight. Project page: ..."); project page linked in the comment.
- **Template credit:** none stated; hand-written single-file CSS.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, the inline `<style>` block and page HTML; 2026-10-28.
