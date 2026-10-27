# AutoGaze — Style Reference

> A linen-bound field journal: light Figtree on parchment, hairline-underlined names and brass-edged notes.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the header, abstract, highlight boxes, tables and the scroll-in navbar), the 1440×900 and full-page screenshots plus a mid-page capture, and the authors' customized Clarity stylesheet `assets/stylesheets/main_free.css` and `assets/scripts/navbar.js` read directly. The stylesheet's @import requests Figtree ital,wght 300–900, but only 300–700 (upright and italic) load because nothing on the page uses 800 or 900; Fira Code 400 also loads; everything renders in Figtree except code. Several template values are overridden later in the same stylesheet (body 20px rather than 17px at this width, title 37px rather than 32px, chips 13px/500 rather than 0.7em/700), and the render values are the ones used below.

## Overview

AutoGaze is a blog-style long read on Shikun Liu's Clarity template, made warm. The header block fades from parchment #f1e6d2 to white and holds a centred three-line title in Figtree 37px at weight 500, warm graphite #353535. Below it, three centred rows of author names in 20px light (300) black with a 0.5px underline, then an italic 18px line of affiliations and contribution notes, then four small uppercase link chips (Paper, Code, Models/Data/Benchmark, Demo) on a 5% black wash with Font Awesome icons on the right. The abstract follows in 20px/300 with 600-weight key phrases. The body is a single 909px reading column at 1440: 26px/600 section headings, light 20px paragraphs, a cream key-claim box with a brass outline, cream pill-shaped inline highlights, wide figures, Flickity carousels with brass-ringed arrows, an image-comparison slider, a Fira Code quickstart block and a results table with warm banded rows. Sections are divided by faint 15%-black hairlines. Once the reader scrolls, a frosted white navbar slides down from the top. Links are black with a hairline underline that thickens and turns walnut on hover.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): the parchment gradient in seven steps, #fcfaf5 15.1%, #f5edde 14.9%, #f1e7d5 13.5%, #f8f3e9 12.7%, #faf6ee 12.7%, #f6f0e4 12.2%, #f2ead9 12.0% (together 93%); text grey #bdb9b1 7.0% (anti-aliased #353535 type and chips). There is no image above the fold.

Anatomy in DOM order (desktop 1440px; header padding 54px top and 265px each side, so the column is 909px at x=265; inside it `.blog-intro` adds 72px top and bottom, so the title starts at y=54+72=126):

1. **Scroll navbar** (`nav.nav-container`, fixed): hidden above the viewport (translateY(-100%)) until scrolling; see Components.
2. **Title** (`#first-content h1.title`, y=126, three lines, 156px incl. 12px padding): Figtree 37px/500, line-height 1.3, #353535, centred, manual line breaks. Gap 60px.
3. **Authors** (`.author-list`, y=342, 382, 421): flex-wrap, centred, gaps 1vh 2vw (9px 28.8px), side margins 7vw; names Figtree 20px/300 #000000 with a 0.5px underline offset 1px; symbol superscripts at 0.55em. Gap 49px.
4. **Affiliations and notes** (`p.author`, y=494, two blocks side by side): Figtree 18px/400 italic #353535, padding 4px 0 10px. Gap 44px.
5. **Link chips** (`.info`, y=574, 38px tall, 8px gaps, centred): four chips, PAPER / CODE / MODELS, DATA, BENCHMARK (one chip) / DEMO; see Components. Gap 50px.
6. **Abstract** (`p.abstract`, y=662, x=294, 881px wide): Figtree 20px/300, line-height 1.6 (32px), #353535, bold phrases 600; indented 28.8px by `.abstract-column` padding. A second paragraph introduces HLVid at y=896; the gradient header ends at y=1057.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Graphite | #353535 | (literal) | title, headings, body text, abstract, chip labels, affiliations |
| Ink Link | #000000 | --link-brown | author names, inline links (0.5px underline), navbar text |
| Walnut | #775223 | --link-brown-hover | link hover colour |
| Parchment | #f1e6d2 | --gradient-start | top of the header gradient (to #ffffff) |
| Cream Note | #fdf4e9 | (literal) | key-claim highlight box fill, carousel arrow hover fill |
| Brass | #e1b76e | (literal) | highlight box border, carousel arrow border |
| Deep Brass | #d4a054 | (literal) | carousel arrow hover border |
| Pill Cream | #fcf6f0 | (literal) | inline highlight span fill |
| Pill Edge | #e3caac | (literal) | inline highlight span border (hover #e5a945 on #fef2df) |
| Chip Wash | rgba(0,0,0,0.05) | (inline style) | link chip background |
| Table Rule | #ececec | (literal) | results-table cell borders |
| Band Tan | #f8edd8 | (literal) | `.gradient-dark` results rows |
| Band Cream | #fdf9f1 | (literal) | `.gradient-medium` results rows |
| Header Grey | #666667 | (literal) | table header text |
| Rule Grey | #c6c6c6 | (literal) | code-block border, table separator rows |
| Code Paper | #fafafa | (literal) | code block fill, footer |

Declared but not visible: `.results-table tr.highlight-row td { font-weight: 800 }` (no row on the page has that class, and Figtree 800 never loads); the template's green link colours (#598864, hover #7baa86) and the #ececec chip base are overridden by `--link-brown` and the inline rgba(0,0,0,0.05) background.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | "Figtree", serif / sans-serif (Google Fonts @import) | Figtree 300, 400, 500, 600, 700 and italics | Outfit |
| Mono | "Fira Code", monospace | Fira Code 400 | JetBrains Mono |
| Icons | Font Awesome 6.6 Free | Font Awesome 6 Free 900 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `#first-content h1.title` | 37px / 500 / 1.3, centred | #353535 |
| Section heading | `div.container.blog h1` | 26px / 600 / 1.2, padding 24px 0 | #353535 |
| Subheading | `h2` | 20px / 600 / 1.2, padding 12px 0 | #353535 |
| Body | `p.text` | 20px / 300 / 1.46 (29.2px) | #353535 |
| Abstract | `#first-content p.abstract` | 20px / 300 / 1.6 | #353535 |
| Authors | `.author-list .author-item a` | 20px / 300 / 1.4 | #000000 |
| Affiliations | `p.author` | 18px / 400 italic / 1.2 | #353535 |
| Link chip | `.button.icon` | 0.65em = 13px / 500, uppercase, letter-spacing 0.075em | #353535 |
| Caption | `p.caption` | 85% = 17px / 400 / 1.4; bold 600 | #353535 |
| Inline link | `a` | inherits, weight 400, underline 0.5px | #000000 |
| Table header | `.results-table thead th` | 15px / 600 (first row), 14px below | #666667 |
| Table cell | `.results-table td` | 14px / 400; first column 500 | #353535 |
| Code | `pre code` | 15px / 300 Fira Code | #000000 (highlight.js foundation colours) |
| Navbar title | `.nav-title` | 16px / 600 | #000000 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link chips | 10px | none | none |
| Highlight box | 16px | 1px #e1b76e | none |
| Inline highlight span | 16px | 1px #e3caac | none |
| Carousel arrows | 50% (35px) | 1px #e1b76e | none |
| Code block | 10px | 1px #c6c6c6 | none |
| Results table | last-row corners 12px | 1px #ececec cells, no outer side borders | none |
| Scroll navbar | 0; links 6px | none | 0 2px 10px rgba(0,0,0,0.1) |
| Section divider | 0 | 1px rgba(0,0,0,0.15) top | none |

## Layout Metrics

- **Column**: every `.container.blog.main` uses `padding: 18px 18.4275vw` at 1200–1599px, giving a 909px column at 1440 (x=265); direct children are capped at `max-width: 1200px`.
- **Header**: `#first-content` padding-top 54px (6vh), same side padding, background linear-gradient(180deg, #f1e6d2, #ffffff); ends at 1057px. The inner `.blog-intro` has `padding: 4.5rem 0 !important` (72px top and bottom, main_free.css line 1752), which overrides the template's 5vh rules at every breakpoint.
- **Title block**: title margin-bottom 3.75rem (60px); author list margin 0 7vw; `.info` margin 2.25rem auto; abstract column padding-left 2vw.
- **Sections**: blocks containing an `hr.section-divider` get 3rem padding top and bottom; paragraphs padding 1.125rem 0; highlight box padding 1em 2em (20px 40px), margin 1.125rem auto.
- **Figures**: images and videos at 100% of the column; OOD carousel cells padded 0 50px for the arrows.
- **Scroll navbar**: fixed, full width, padding 12px 30px, slides in on scroll.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≤768px | 9.171vw | 16px | 37px (h1 22px, h2 18px) | two-column figures stack; chips take two per row; abstract column gets a top rule |
| 769–991px | 9.685vw | 17px | 37px (h1 22px) | — |
| 992–1199px | 15.342vw | 18px | 37px (h1 22px) | chips 0.6em |
| 1200–1599px | 18.4275vw | 20px | 37px (h1 26px, h2 20px) | — |
| 1600–1999px | 21.513vw | 22px | 37px (h1 32px, h2 23px) | — |
| ≥2000px | 25.627vw (27.684vw ≥2400, 35.912vw ≥3200) | 20px (23px ≥2400) | 37px | — |

## Components

- **Link chip** (`a.button.icon`): inline-flex, background rgba(0,0,0,0.05) (inline style), 10px radius, padding 9.75px 13px, Figtree 13px/500 uppercase, letter-spacing 0.975px, #353535, Font Awesome 6 Free solid icon (weight 900) on the right at 1.2em with 7.8px left padding, glyphs `fa-solid fa-book-open` (Paper), `fa-code` (Code), `fa-database` (Models, Data, Benchmark), `fa-laptop-code` (Demo); hover opacity 0.8, active 0.5. 8px gaps, centred.
- **Hairline link**: #000000, underline 0.5px thick, offset 1px, weight 400; hover #775223 and 1.5px thick.
- **Key-claim box** (`p.text.highlight-box`): #fdf4e9, 1px #e1b76e, 16px radius, padding 20px 40px, 20px/300 text with the opening sentence in 600.
- **Inline highlight** (`span.inline-highlight`): #fcf6f0 pill, 1px #e3caac, 16px radius, padding 0.03em 0.4em; hover (or when the linked figure region is hovered) #fef2df with #e5a945.
- **Flickity carousel**: 35px circular arrows, rgba(255,255,255,0.9), 1px #e1b76e border; hover #fdf4e9 fill and #d4a054 border; grey #c6c6c6 dots.
- **Results table** (`.results-table`): full column width, collapsed, 1px #ececec cell borders without outer sides; headers 15px/600 #666667 centred (first column left); body 14px centred, first column 500 left; row bands #f8edd8 (dark), #fdf9f1 (medium), #ffffff (light); best numbers in `strong` at 700; separator rows 1.5px #c6c6c6.
- **Code block**: `pre code` on #fafafa, 1px #c6c6c6, 10px radius, Fira Code 15px/300, padding 13.5px 21.6px, highlight.js "foundation" theme.
- **Scroll navbar** (`.nav-container`, injected by navbar.js): fixed, rgba(255,255,255,0.5) with blur(10px), shadow 0 2px 10px rgba(0,0,0,0.1); left a ☰ table-of-contents toggle and "AutoGaze" 16px/600, then the current section name in grey italic; right four links with icons left, 13px/500 labels, padding 8px 10px, 6px radius.
- **Footer**: #fafafa band, padding 36px 0, italic Clarity credit.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | centred, light weight, underlined black names, italic notes |
| Venue | absent from the source | no CVPR line on the page |
| Link chips | yes | four uppercase chips with right-side icons |
| Abstract | yes | two light paragraphs inside the gradient header |
| Quickstart code | yes | Fira Code block after a section heading |
| Teaser video | yes | autoplay video near the top of the body |
| Method figures | yes | full-width diagrams with linked inline highlights |
| Qualitative carousels | yes | Flickity with brass-ringed arrows |
| Image comparison | yes | `img-comparison-slider` web component |
| Efficiency results | yes | carousels of plots under h2 questions |
| Results table | yes | warm banded HTML table (HLVid benchmark) |
| Section dividers | yes | 15% black hairlines |
| Scroll navbar | yes | frosted bar that slides in |
| BibTeX | yes | code block near the end |
| Footer | yes | #fafafa band with template credit |

## Adapting to Other Content

- **More authors**: the `.author-list` flex-wrap takes any number of names at 20px/300 with 28.8px gaps; keep affiliations as one italic 18px line below.
- **A venue line**: add it as a fifth uppercase chip-style label (13px/500, letter-spacing 0.075em) without the wash, or as an italic 18px line above the chips; do not add colour.
- **Larger results tables**: reuse `.results-table` banding (#f8edd8 for the method group, #fdf9f1 for strong baselines, white for the rest) and 700 (`strong`) for your own best numbers; wrap in `.table-wrapper` for horizontal scroll on phones.
- **Long publication or news lists**: use 20px/300 paragraphs with a 600-weight date, separated by `hr.section-divider` hairlines.
- **More emphasis boxes**: use at most one `.highlight-box` per section; use inline pills for smaller emphasis.

## Do's and Don'ts

- Do keep text #353535 at weight 300; headings only go to 500–600.
- Do keep brass (#e1b76e) and cream (#fdf4e9) for emphasis surfaces and carousel controls.
- Do keep links black with a hairline underline; walnut #775223 only on hover.
- Don't use filled colour buttons; chips are a 5% black wash with uppercase micro type.
- Don't set side gutters in px; they scale in vw steps.
- Don't put the header gradient anywhere else; the body stays white.

## Surfaces

Parchment-to-white header, white body, cream highlight box and pills, warm banded table rows, #fafafa code and footer, frosted scroll navbar.

## Imagery

Video frames with gaze-patch overlays, efficiency plots in orange and green, architecture diagrams with brass and grey blocks, a qualitative video carousel, an HLVid benchmark section. Figures run full column width and open in a lightbox.

## Layout

A single reading column (909px at 1440) with vw-based gutters: gradient header, quickstart, introduction, architecture, qualitative results, generalization, efficiency, HLVid benchmark with table, BibTeX, footer. About 11,165px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: text #353535, link #000000 with hover #775223, header gradient #f1e6d2 → #ffffff, highlight #fdf4e9 with #e1b76e, inline pill #fcf6f0 with #e3caac, chip rgba(0,0,0,0.05), table rule #ececec, code #fafafa.

1. "Build a parchment header: background linear-gradient(180deg, #f1e6d2, #ffffff), padding 54px 18.4275vw 0, with an inner wrapper padded 72px 0; title Figtree 37px/500, line-height 1.3, #353535, centred, margin-bottom 60px; authors in a centred flex-wrap with gaps 9px 28.8px, Figtree 20px/300 #000000 with a 0.5px underline offset 1px; affiliations Figtree 18px italic #353535."
2. "Make link chips: inline-flex, background rgba(0,0,0,0.05), 10px radius, padding 9.75px 13px, Figtree 13px/500 uppercase, letter-spacing 0.975px, #353535, icon on the right with 7.8px left padding; 8px gaps; hover opacity 0.8."
3. "Create a key-claim callout: paragraph in Figtree 20px/300 #353535 with a 600-weight lead sentence, background #fdf4e9, 1px solid #e1b76e, 16px radius, padding 20px 40px, margin 18px auto."

## Similar Pages

- Clarity template pages by Shikun Liu.
- Long-form, blog-style research pages with a single wide reading column and minimal colour.

## Quick Start

```css
:root {
  --text: #353535;
  --link-brown: #000000;
  --link-brown-hover: #775223;
  --gradient-start: #f1e6d2;
  --gradient-end: #ffffff;
  --highlight-bg: #fdf4e9;
  --highlight-border: #e1b76e;
  --pill-bg: #fcf6f0;
  --pill-border: #e3caac;
  --chip-bg: rgba(0, 0, 0, 0.05);
  --rule: #ececec;
  --code-bg: #fafafa;
  --font-sans: 'Figtree', sans-serif;
  --font-mono: 'Fira Code', monospace;
}
p, li { font: 300 20px/1.46 var(--font-sans); color: var(--text); }
.container.blog.main { padding: 18px 18.4275vw; }
a { color: var(--link-brown); text-decoration: underline; text-decoration-thickness: 0.5px; text-underline-offset: 1px; }
```

## Provenance

- **URL**: https://autogaze.github.io/
- **Paper**: Attend Before Attention: Efficient and Scalable Video Understanding via Autoregressive Gazing (arXiv 2603.12254), Baifeng Shi et al.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment reads "CVPR 2026. Project page: https://autogaze.github.io/".
- **Template credit**: footer says the site is built on the Clarity Template designed by Shikun Liu.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of the header and body components, the 1440×900 and full-page screenshots, a mid-page capture showing the scroll navbar, and `main_free.css` and `navbar.js` read directly, on 2026-10-28. v2 rewrite: v1 values for body size (18px), chip size (11.7px) and title weight were CSS readings that the render contradicts.
