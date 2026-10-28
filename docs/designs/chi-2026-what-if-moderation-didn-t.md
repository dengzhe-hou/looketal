# DIY-MOD — Style Reference

> A quiet reading room with a purple ribbon on the lectern: slate sans headlines, Garamond prose, and one warm amber note pinned to the wall.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `style.css` and `index.html` read directly (several inline `style` attributes override the stylesheet, and those were probed on the rendered elements). The footer credits the Nerfies template, but the page is a rewrite: there is no Bulma, and all styling comes from `style.css`.

## Overview

A short, centred single-column page (about 5,260px tall) on pure white inside a 1000px container. The hero stacks a two-line bold slate title (#2c3e50, Noto Sans 35.2px), an EB Garamond venue line in gray, three purple award lines with Font Awesome medal and trophy icons, two author names each followed by a 40px round photo, a navy University of Michigan logo plate, and four near-black pill buttons. The teaser is a large annotated system figure set in a white card with a soft shadow and a centred Garamond caption. Below, sections are introduced by centred 25.6px slate headings with a 1px gray rule under them: Abstract (Garamond text in a #f8f9fa rounded block), System Demo (a 900px video with 12px radius), an interactive Transformation Palette (an amber explainer box, an Image/Text segmented toggle, underline tabs, option buttons and blue/green metric bars), a pipeline figure, pastel expandable finding cards in a 2-column grid, a gray BibTeX block and a centred gray footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 73.3%, plus near-whites #fafafa 3.2%, #fffffd 1.1%, #fdffff 0.2%; warm photo tones from the teaser #847267 6.8%, #362926 6.5%, #e9dfd0 3.6%; gray #b7b5b0 5.2% (teaser line art and text). Slate, purple and the pill buttons are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `.container` max-width 1000px with 20px side padding, so content runs x=220 to 1220; `header.hero` padding 32px 0 48px, everything centred):

1. **Title** (`h1`, y=64, 84px tall): two lines, Noto Sans 35.2px (2.2rem) / 700, line-height 1.2, #2c3e50. Margin 32px top, 17.6px bottom.
2. **Venue line** (y=166, 29px tall): "ACM CHI Conference on Human Factors in Computing Systems (CHI 2026)", EB Garamond 18.4px / 400, #555555 (inline style). Margin-bottom 16px.
3. **Award lines** (`.awards-section`, y=212 to 298): three lines 16px / 600 #663399, each with a Font Awesome icon (medal, trophy, trophy) 8px before the text; flex column with 4.8px gaps. Margin-bottom 24px.
4. **Authors** (`.authors`, y=322, 40px tall): two `.author-block`s 19.2px apart; name 19.2px / 600 #333333, then a 40px circular photo 4.8px to its right with shadow 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24). Margin 16px top, 8px bottom.
5. **Institution logo** (y=371, 196×30): University of Michigan image (navy plate, maize block M), radius 8px.
6. **Buttons** (`.publication-links`, y=432, 37px tall): arXiv, Poster, Code, Video; 9.6px gaps; margin-top 24px.
7. **Teaser card** (`.hero-teaser`, y=510 to 1108): white, radius 8px, shadow 0 4px 6px rgba(0,0,0,0.1), margin 40px 0; image 1000×433, then caption in EB Garamond 16px #666666 centred with 32px side padding, 12.8px above and 24px below.

The Abstract heading follows at y=1244 (hero padding-bottom 48px plus the h2's 48px top margin, collapsed with the card margin).

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | --bg-color | page background, teaser card, video frame, transformation explorer card, active toggle button |
| Slate | #2c3e50 | --primary-color | title, section headings, active category tab and underline, active option button fill, card titles, explainer lead |
| Ink | #333333 | --text-color | body text, author names, abstract text |
| Award Purple | #663399 | --purple-award | award lines and their icons |
| Pill Black | #363636 | (literal, `.link-block a.button`) | link pill fill |
| Pill Hover | #555555 | (literal) | link pill hover fill; venue line text; filter label; explainer list items |
| Caption Gray | #666666 | (literal) | teaser and pipeline captions, demo caption |
| Mist | #f8f9fa | --secondary-bg | abstract block, filter-context gradient start |
| Code Gray | #f4f4f4 | (literal) | BibTeX block, visual box |
| Rule | #e1e4e8 | --border-color | h2 underline rule, BibTeX border, segmented-toggle track |
| Hairline | #eeeeee | (literal) | borders of video, explorer card, pipeline image, metrics box |
| Link Blue | #3498db | --accent-color | text links, first metric bar fill, quote bar in finding cards |
| Link Hover | #2980b9 | (literal) | text link hover |
| Metric Green | #2ecc71 | (literal) | direction arrows and the second metric bar |
| Amber Cream | #fff9f0 | (literal) | trade-off explainer box, third finding card |
| Amber Edge | #feeacb | (literal) | border of the explainer box and third finding card |
| Footer Gray | #999999 | (literal) | footer text |
| Tab Gray | #888888 | (literal) | inactive category tabs |
| Chevron Gray | #777777 | (literal) | finding-card chevrons, examples note |
| Button Edge | #dddddd | (literal) | option button border |
| Button Hover | #f5f5f5 | (literal) | option button hover fill |
| Bar Track | #e0e0e0 | (literal) | metric bar track |
| Card pastels | #f3f8ff / #dae8fc, #f0fff4 / #d5ebd5, #fbf5ff / #eedafe | (literal, `.card-color-1/2/4`) | fill / border of the blue, green and purple finding cards |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (UI, headings) | 'Noto Sans', sans-serif | Noto Sans 400, 400 italic, 500, 600, 700 (Google Fonts) | Open Sans |
| Serif (reading) | 'EB Garamond', serif | EB Garamond 400, 400 italic, 600 | Cormorant Garamond |
| Code | browser monospace | system monospace (Consolas on Windows) | IBM Plex Mono |
| Icons | Font Awesome 6.4.0, Academicons | FA 6 Free 900, FA 6 Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | 35.2px / 700 / 1.2 | #2c3e50 |
| Section heading | `h2` | 25.6px / 600 / 1.2, centred, 1px #e1e4e8 rule, padding-bottom 8px | #2c3e50 |
| Venue line | inline-styled `div` | EB Garamond 18.4px / 400 | #555555 |
| Award line | `.award-line` | 16px / 600 | #663399 |
| Author name | `.author-name` | 19.2px / 600 | #333333 |
| Body paragraph | `p` | 16.8px / 400 / 1.6 | #333333 |
| Abstract | `.abstract-content p` | EB Garamond 16.8px / 1.8, justified | #333333 |
| Teaser caption | inline-styled `p` | EB Garamond 16px / 1.6, centred | #666666 |
| Demo caption | `.demo-caption` | EB Garamond 16px italic | #666666 |
| Link pill | `.link-block a.button` | 15.2px / 600 | white |
| Category tab | `.category-tab` | 16px / 600 | #888888; active #2c3e50 |
| Explainer list | `.tradeoff-dimensions li` | 15.2px; terms bold #2c3e50 | #555555 |
| Card title | `.card-title` | 16.8px / 600 | #2c3e50 |
| BibTeX | `pre` | 14.4px / 1.6 monospace | #333333 |
| Footer | `footer p` | 16.8px; template credit 12.8px #bbbbbb | #999999 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link pills | 9999px | none | none; hover fill #555555 |
| Author photos | 50% (40px) | none | 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24) |
| Institution logo | 8px | none | none |
| Teaser card | 8px | none | 0 4px 6px rgba(0,0,0,0.1) |
| Abstract block | 8px | none | none |
| Demo video | 12px | 1px #eeeeee | 0 4px 6px rgba(0,0,0,0.1) |
| Trade-off explainer | 8px | 1px #feeacb | none |
| Explorer card | 12px | 1px #eeeeee | 0 4px 6px rgba(0,0,0,0.1) |
| Segmented toggle | 999px track, 999px buttons | none | active button 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24) |
| Option buttons | 6px | 1px #dddddd; active 1px #2c3e50 | none |
| Metrics box / visual box | 8px | metrics 1px #eeeeee | none |
| Metric bars | 4px, 8px tall | none | none |
| Finding cards | 12px | 1px pastel edge | 0 2px 4px rgba(0,0,0,0.05); hover 0 4px 6px rgba(0,0,0,0.1), translateY(-2px) |
| BibTeX | 8px | 1px #e1e4e8 | none |

## Layout Metrics

- **Container**: `.container { max-width: 1000px; margin: 0 auto; padding: 0 20px }`; at 1440 the content box is 1000px wide from x=220.
- **Hero**: `header.hero` padding 32px 0 48px; rendered from y=0 to 1196 including the teaser card.
- **Section rhythm**: each `h2` has margin 48px top, 12.8px bottom and an 8px bottom padding above its rule; sections themselves carry no padding.
- **Teaser**: `.hero-teaser` width 100% (max 1100px, so 1000px here), margin 40px auto.
- **Abstract**: block padding 32px 48px, so the text measures 904px.
- **Video**: max 900px (rendered 902px with borders), centred, margin 32px 0 around the demo container.
- **Explorer**: filter-context strip padding 24px 128px with background linear-gradient(135deg, #f8f9fa 0%, #fff 100%); main area padding 4px 32px 32px; result row is a 3:2 flex split (visual box : metrics box) with a 32px gap.
- **Findings grid**: two columns 1fr 1fr, gap 24px, margin 32px 0 (cards 488px wide).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >800px (base) | 20px | 16.8px paragraphs | 35.2px | findings 2 columns; explorer visual and metrics side by side |
| ≤800px | 20px | 16.8px | 35.2px | abstract padding 24px; findings 1 column; explorer stacks (sidebar, result area column, gap 16px); filter strip padding 16px 24px; tabs gap 12.8px, 14.4px |
| ≤480px | 20px | 16.8px | 35.2px | filter strip 12.8px 16px; tabs 13.6px; option buttons 13.6px, padding 5.6px 9.6px; metric labels 12.8px |

## Components

- **Link pill** (`.link-block a.button`): inline-flex, #363636 fill, white 15.2px / 600 Noto Sans, padding 6.4px 16px, radius 9999px, icon (academicons arXiv, FA file-image, FA GitHub, FA YouTube) on the left with a 6.4px gap. Hover: #555555, 0.2s.
- **Award line** (`.award-line`): 16px / 600 #663399, Font Awesome solid medal or trophy 8px before the text, one award per line, centred, 4.8px apart.
- **Author block**: name 19.2px / 600 #333333 followed by a 40px circular photo (object-fit cover) with the two-layer small shadow; blocks 19.2px apart.
- **Teaser card** (`.hero-teaser`): white, radius 8px, overflow hidden, shadow 0 4px 6px rgba(0,0,0,0.1); full-width image then a centred EB Garamond 16px #666666 caption with bold (a)–(d) markers.
- **Section heading** (`h2`): centred 25.6px / 600 #2c3e50 with a full-width 1px #e1e4e8 rule 8px below the text.
- **Abstract block** (`.abstract-content`): #f8f9fa, radius 8px, padding 32px 48px, EB Garamond 16.8px / 1.8 justified #333333, bold system name.
- **Trade-off explainer** (`.tradeoff-explainer`): #fff9f0 fill, 1px #feeacb border, radius 8px, padding 19.2px 24px; lead sentence 16.8px / 600 #2c3e50; list of three dimensions at 15.2px #555555 with bold #2c3e50 terms.
- **Segmented toggle** (`.mode-toggle`): #e1e4e8 track, radius 999px, padding 4px, gap 4px; buttons padding 6.4px 19.2px, 600, #555555; active white with #2c3e50 text and the small two-layer shadow.
- **Underline tabs** (`.category-tab`): 16px / 600 #888888, padding-bottom 8px, 2px transparent underline over a 2px #eeeeee track; active #2c3e50 with a 2px #2c3e50 underline.
- **Option button** (`.tradeoff-btn`): white, 1px #dddddd, radius 6px, padding 8px 16px, Noto Sans 500; hover #f5f5f5; active #2c3e50 fill, white text.
- **Metric bar**: label row 13.6px / 600 #555555 with a green arrow; 8px #e0e0e0 track, radius 4px; fill #3498db or #2ecc71 animating width over 0.6s.
- **Finding card** (`.expand-card`): pastel fill and border, radius 12px, shadow 0 2px 4px rgba(0,0,0,0.05); header padding 19.2px with a rgba(255,255,255,0.4) wash, 16.8px / 600 #2c3e50 title and a #777777 chevron that rotates 180° when open; body slides open to 19.2px padding.
- **BibTeX** (`pre`): #f4f4f4, 1px #e1e4e8 border, radius 8px, padding 24px, 14.4px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title | yes | two-line bold slate sans, centred |
| Venue line | yes | gray EB Garamond line under the title |
| Awards | yes | three purple lines with medal and trophy icons |
| Authors with photos | yes | name plus 40px round photo, two authors |
| Affiliation | present but non-standard | a University of Michigan logo image instead of text |
| Link buttons | yes | four near-black pills |
| Teaser + caption | yes | white shadowed card with Garamond caption |
| Abstract | yes | tinted Garamond block |
| Video | yes | 900px rounded video with italic caption |
| Interactive explorer | yes | amber explainer, segmented toggle, tabs, option buttons, metric bars |
| Findings / future work | yes | pastel expandable cards, 2 columns |
| Results tables | absent from the source | results are cards and the explorer |
| BibTeX | yes | gray pre block |
| Footer | yes | centred gray text with template credit |

## Adapting to Other Content

- **More authors**: keep the name-plus-photo blocks in one centred flex row with 19.2px gaps; at 1000px about four blocks fit per line, then they wrap. Add text affiliations under the logo in EB Garamond 16px #666666 if there is more than one institution.
- **A results table**: put it in a card like the explorer (white, 1px #eeeeee, radius 12px, shadow 0 4px 6px rgba(0,0,0,0.1)); header 16px / 600 #2c3e50 on #f8f9fa, cells 15.2px #333333, best values bold #2c3e50; numbers in Noto Sans, not Garamond.
- **Long publication or news lists**: use the explainer box (#fff9f0, 1px #feeacb, radius 8px, padding 19.2px 24px) with dates bold #2c3e50 and entries at 15.2px #555555.
- **More awards**: one `.award-line` per award in #663399; keep them stacked rather than inline.
- **More findings**: continue the 2-column pastel grid (488px cards at 1440), cycling blue, green, amber and purple.

## Do's and Don'ts

- Do pair Noto Sans for headings and UI with EB Garamond for captions, abstract and the venue line.
- Do keep every heading centred with the thin #e1e4e8 rule beneath it.
- Do use #663399 only for awards, and #2c3e50 for headings and active states.
- Do keep the pills near-black (#363636), not blue.
- Don't use a colored hero band; the hero is white.
- Don't make the abstract sans; it is the serif reading block.
- Don't add heavy shadows; the deepest is 0 4px 6px rgba(0,0,0,0.1).

## Surfaces

All white, with three tints: #f8f9fa for the abstract, #fff9f0 for the explainer, pastel fills for finding cards. Raised elements (teaser card, video, explorer) get the single 0 4px 6px rgba(0,0,0,0.1) shadow; the BibTeX block is flat gray with a hairline.

## Imagery

An annotated system diagram (filter panel, Reddit-style feed posts, transformed images, yellow lettered markers, a blue "Modified by DIY-MOD" badge) as the teaser; a demo screen recording; transformation examples (blurred, occluded, inpainted and painterly food photos) in the explorer; a grayscale pipeline figure with 1px #eeeeee border and 8px radius; two small round author photos.

## Layout

One centred 1000px column throughout: hero, full-width teaser card, then sections separated only by headings with 48px top margins. Interactive and card content stays inside the column; the only two-column layout is the findings grid.

## Agent Prompt Guide

Quick colors: background #ffffff, text #333333, headings #2c3e50, awards #663399, pills #363636, abstract block #f8f9fa, callout #fff9f0 with #feeacb edge, rules #e1e4e8, links #3498db.

1. "Build a centred white hero in a 1000px column: title Noto Sans 35.2px / 700 #2c3e50, line-height 1.2; venue line EB Garamond 18.4px #555555; three award lines 16px / 600 #663399 with Font Awesome trophy icons; author names 19.2px / 600 #333333 each followed by a 40px round photo; then pills with #363636 fill, white 15.2px / 600 text, padding 6.4px 16px, radius 9999px, hover #555555."
2. "Make a section: centred h2 25.6px / 600 #2c3e50 with a 1px #e1e4e8 rule 8px below, margin-top 48px. Abstract in a #f8f9fa block, radius 8px, padding 32px 48px, EB Garamond 16.8px / 1.8 justified #333333."
3. "Create a callout and cards: callout #fff9f0, 1px #feeacb border, radius 8px, padding 19.2px 24px, bold #2c3e50 lead; finding cards in a 2-column grid with 24px gap, radius 12px, pastel fill #f3f8ff with 1px #dae8fc edge, shadow 0 2px 4px rgba(0,0,0,0.05), header padding 19.2px with a 16.8px / 600 #2c3e50 title."

## Similar Pages

- Nerfies-derived project pages rewritten without Bulma, with centred headings and pill buttons.
- HCI pages that set the abstract and captions in a Garamond serif under sans headings.

## Quick Start

```css
:root {
  --bg-color: #ffffff;
  --text-color: #333333;
  --primary-color: #2c3e50;
  --accent-color: #3498db;
  --purple-award: #663399;
  --secondary-bg: #f8f9fa;
  --border-color: #e1e4e8;
  --pill: #363636;
  --callout-bg: #fff9f0;
  --callout-edge: #feeacb;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --font-sans: 'Noto Sans', sans-serif;
  --font-serif: 'EB Garamond', serif;
  --container: 1000px;
}
```

## Provenance

- **URL**: https://rayhan.io/diymod/
- **Paper**: What If Moderation Didn't Mean Suppression? A Case for Personalized Content Transformation (arXiv 2509.22861), Rayhan Rashed, Farnaz Jahanbakhsh.
- **Venue**: CHI 2026; the page lists Best Paper Honorable Mention, Best Poster Award (Michigan HCAI 2025) and Best Application of AI (Michigan AI Symposium 2025).
- **Selection reason**: the arXiv comment states acceptance at CHI 2026; the project page is the homepage of the paper's code repository (UMichHCI/diymod) linked in the paper body.
- **Template credit**: footer reads "Website template based on Nerfies"; the CSS is a custom `style.css` without Bulma.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of hero lines, abstract, explorer controls and cards, the 1440×900 and full-page screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
