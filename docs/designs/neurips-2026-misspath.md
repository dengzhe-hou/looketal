# MissPath-FM — Style Reference

> A well-set lab notebook in violet ink: heavy Inter headlines, serif section claims, and every number, tab and badge stamped in the same deep indigo.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, a second live render scrolled through the Method and Results sections, and the page's own `assets/styles.css`, `assets/site.js` and `index.html`. The stylesheet defines its palette as custom properties on `:root`, so most token names below are the page's own. The green and blue in the first-viewport color share belong to the teaser figure image, not to the CSS.

## Overview

A white, hand-built single page (about 9,000px tall) with no navigation bar. The hero is centred: a small filled indigo eyebrow tag "MISSPATH-FM", a two-line 49.6px/800 Inter title whose first half ("Flow Matching with Structured Priors") is indigo #3d2f9a and second half near-black #142030, a slate subtitle sentence, a pale lavender "NeurIPS 2026" pill with a green status dot, one underlined author, a muted affiliation line, and three pale lavender pill buttons with inline SVG icons. A 1120px teaser figure card with a violet-tinted 70px shadow follows. Below, sections alternate white and a faint lavender wash (#f8f7fd fading to white) with thin lavender rules. Each section opens with an uppercase indigo kicker and a large 44.8px Noto Serif headline, a deliberate serif-on-sans contrast. Content is built from cards: two-column claim cards, three method cards with indigo, amber and green top bars, a dark #17142b code card, four big-number metric cards, and white table cards whose tables mark "Ours" in a lavender column with bold indigo numbers. A dark BibTeX card with a translucent copy button closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fdffff / #fffffe / #fbfffc 69.4%; teaser-image greens #e8f5ea 12.5%, #f4f9f7 4.1% and gray-green #dbe5e2 7.1% (the pale green panels inside the figure PNG); #797d94 7.0% (anti-aliased ink, indigo title text and figure line art). The indigo #3d2f9a fills too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px, hero centred in `.hero-inner`, 1060px wide at x=190):

1. **Eyebrow tag** (`p.eyebrow`, y=62–94): "MISSPATH-FM", 15.2px/800 uppercase, letter-spacing 0.08em, #ffffff on #3d2f9a, padding 3px 12px, radius 6px. Gap 12px.
2. **Title** (`h1`, y=106–219): 49.6px/800, line-height 1.14, `text-wrap: balance`, max 1000px, two lines; `h1 span` (line 1) #3d2f9a, rest #142030. Gap 18px.
3. **Subtitle** (`p.subtitle`, y=237–323): 18.4px/400, line-height 1.55, #334155, max 820px, three balanced lines. Gap 17px.
4. **Venue pill** (`span.venue-badge`, y=340–375): "NeurIPS 2026", 13.76px/800 #3d2f9a on #f1effb, 1px #c9c0ee border, padding 5px 14px, radius 999px, min-height 34px; 7px #2b9c70 dot 8px before the text. Gap 24px.
5. **Author** (`p.author-list`, y=399–428): 16.48px/500; link #4433b0 with an rgba(68,51,176,.35) underline at 3px offset. Gap 12px.
6. **Affiliation** (`p.affiliations`, y=440–464): 13.76px/400 #5a6779, line-height 1.72. Gap 24px.
7. **Buttons** (`.button-row`, y=488–528): Paper, Code, BibTeX; 40px tall, 10px apart, 15px SVG icon left. Hero ends 20px below (padding-bottom 20px).
8. **Teaser** (`figure.teaser`, y=566–1321): 1120px card at x=160 (teaser section padding 18px 0 42px), image inset 14px, caption 15.36px #5a6779 with a bold #142030 lead. The fold cuts through the figure.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | --bg | page background, cards, figure cards, inactive tab buttons |
| Ink | #142030 | --ink | body color, title line 2, h2 serif headlines, h3, table body text, caption leads |
| Slate | #334155 | (literal) | hero subtitle, prose paragraphs (`.prose p`) |
| Author Ink | #243047 | (literal) | `.authors` block color |
| Equation Ink | #1e2e44 | (literal) | `.equation` text in equation panels |
| Muted | #5a6779 | --muted | affiliation, section notes, figcaptions, card body text, table headers, metric labels, footer |
| Line | #e0dcf3 | --line | card and figure borders, table header rule, footer top border; at 75% for `.section-soft` top and bottom rules |
| Row Line | #edf2f4 | (literal) | 1px bottom border of table rows |
| Tint 25 | #f8f7fd | --tint-25 | top of the `.section-soft` gradient (to #ffffff) |
| Tint 50 | #f1effb | --tint-50 | venue pill, buttons, equation panels, callouts, author-link hover |
| Tint 100 | #e6e2f8 | --tint-100 | button hover fill; `theme-color` meta |
| Tint 200 | #c9c0ee | --tint-200 | venue pill and button borders, tab borders, equation-panel border, code-card label text |
| Ours Lavender | #efecfb | --ours-bg | "Ours" table column and row background |
| Indigo | #3d2f9a | --accent-700 | eyebrow fill, title line 1, kickers, venue and button text, active tab fill, method card 1 h3, metric numbers, "Ours" numbers, equation labels, callout strong, footer links |
| Violet | #5b4bc4 | --accent-500 | method card 1 top bar, callout left bar, button and venue hover border, button shadow (9%) |
| Link | #4433b0 | --link | author link, inline links |
| Link Hover | #2b1f7a | --link-hover | link hover color |
| Green | #2b9c70 | --green-500 | venue pill dot, method card 3 top bar and h3 |
| Amber | #b5761f | --amber-500 | method card 2 top bar and h3 |
| Night Card | #17142b | (literal) | code card and BibTeX card background |
| Night Text | #efedfb | (literal) | code and BibTeX text |
| Comment Lilac | #8f88b8 | (literal) | code comments (`.code-card .c`) |
| Callout Ink | #2b2747 | (literal) | callout body text |
| Card Shadow | rgba(61,47,154,0.12) | --shadow | teaser, wide figures, code and BibTeX cards (0 24px 70px) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif | Inter 400, 500, 600, 700, 800 (Google Fonts) | Roboto |
| Section headlines | "Noto Serif", Georgia, "Times New Roman", serif | Noto Serif 700 (500 requested, not used) | Source Serif 4 |
| Code | "JetBrains Mono", "SFMono-Regular", Consolas, Menlo, monospace | JetBrains Mono 400 | Fira Code |
| Math | KaTeX 0.16.11 auto-render | KaTeX_Main, KaTeX_Math, KaTeX_AMS, KaTeX_Caligraphic, KaTeX_Size1, KaTeX_Size2 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | clamp(1.9rem, 4vw, 3.1rem) → 49.6px / 800 / 1.14 | #142030, `h1 span` #3d2f9a |
| Eyebrow tag | `.eyebrow` | 0.95rem = 15.2px / 800 uppercase, letter-spacing 0.08em | #ffffff on #3d2f9a |
| Subtitle | `.subtitle` | clamp(1rem, 2vw, 1.15rem) → 18.4px / 400 / 1.55 | #334155 |
| Venue pill | `.venue-badge` | 0.86rem = 13.76px / 800 | #3d2f9a |
| Author | `.author-list` | 1.03rem = 16.48px / 500 / 1.75 | link #4433b0 |
| Affiliation | `.affiliations` | 0.86rem = 13.76px / 400 / 1.72 | #5a6779 |
| Button | `.button` | 0.9rem = 14.4px / 700 | #3d2f9a |
| Section kicker | `.section-kicker` | 0.8rem = 12.8px / 800 uppercase, letter-spacing 0.06em | #3d2f9a |
| Section headline | `h2` | clamp(1.8rem, 3.4vw, 2.8rem) → 44.8px / 700 / 1.14, Noto Serif | #142030 |
| Subhead | `.subhead` (h3) | 1.3rem = 20.8px / 700 | #3d2f9a |
| Card title | `h3` | 1.12rem = 17.92px / 700 / 1.28 | #142030 (method cards #3d2f9a, #b5761f, #2b9c70) |
| Body / prose | `body`, `.prose p` | 16px / 1.68; prose 1.04rem = 16.64px | #142030; prose #334155 |
| Section note | `.section-note` | 1.02rem = 16.32px / 1.6 | #5a6779 |
| Metric number | `.metric-card strong` | clamp(2rem, 4vw, 2.8rem) → 44.8px / 700 / 1, tabular | #3d2f9a |
| Metric label | `.metric-card > span` | 0.93rem = 14.88px / 600 / 1.4 | #5a6779 |
| Table body | `table.results td` | 0.9rem = 14.4px, tabular, right-aligned | #142030 |
| Table header | `table.results thead th` | 0.82rem = 13.12px / 700 | #5a6779 |
| Caption | `figcaption` | 0.96rem = 15.36px / 1.55 | #5a6779, `strong` #142030 |
| Code | `.code-card pre` | 0.84rem = 13.44px / 1.6 | #efedfb |
| Equation label | `.equation-label` | 0.82rem = 13.12px / 900 uppercase, letter-spacing 0.05em | #3d2f9a |
| Footer | `.footer` | 0.9rem = 14.4px | #5a6779, links #3d2f9a 700 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Eyebrow tag | 6px | none | none |
| Venue pill, buttons, tab buttons | 999px | 1px #c9c0ee | buttons 0 8px 24px rgba(91,75,196,.09); pill and tabs none |
| Teaser and wide figures | 10px | 1px #e0dcf3 | 0 24px 70px rgba(61,47,154,.12) |
| Claim, method and metric cards | 10px | 1px #e0dcf3; method cards add a 3px top bar | 0 18px 44px rgba(61,47,154,.07) |
| Table cards | 10px | 1px #e0dcf3 | 0 18px 44px rgba(61,47,154,.06) |
| Equation panel | 10px | 1px #c9c0ee | none |
| Callout | 0 10px 10px 0 | left 4px #5b4bc4 | none |
| Code card, BibTeX card | 10px | none | 0 24px 70px rgba(61,47,154,.12) |
| Copy button | 8px | 1px rgba(255,255,255,.18) | none |
| Soft sections | 0 | top and bottom 1px rgba(224,220,243,.75) | none |

## Layout Metrics

- **Containers**: `.container { width: min(1120px, calc(100% - 36px)) }` (x=160 at 1440); `.hero-inner` uses min(1060px, calc(100% - 36px)). Title max 1000px, subtitle 820px, authors 940px, section headings 780px, section notes 760px.
- **Hero**: padding 62px 0 20px, rendered 548px tall; teaser section padding 18px 0 42px; teaser image padding 14px 14px 0, caption padding 16px 22px 20px.
- **Section rhythm**: `.section` padding 76px 0; section heading block margin-bottom 32px; `.subhead` margin 52px 0 18px; cards and panels 22px apart (`margin-top: 22px`).
- **Grids**: Abstract uses `.text-grid` (0.9fr / 1.35fr, gap 54px → 426px headline column and 640px prose column); claim cards `.two-up` 2 columns, gap 18px; method cards 3 columns, gap 18px, padding 22px; metric cards 4 columns (2 at the browser-pane width shown in the live render), gap 18px; `.split-figure` 1fr/1fr, gap 22px. Tables scroll horizontally inside `.table-scroll`, `white-space: nowrap`.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1240px | 160px at 1440 (1120px container) | 16px | 49.6px | full grids; h2 44.8px |
| ≤1240px | 1120px container until 1156px, then 18px each side | 16px | 4vw (≈40px at 1000) | h2 3.4vw below 1318px |
| ≤960px | 18px | 16px | 4vw | metric grid 2 columns; split figure and equation rows 1 column |
| ≤760px | 18px | 16px | 30.4px floor | hero padding-top 44px; section padding 56px; text-grid, claim and method grids 1 column (gap 18px, text-grid 24px); h2 28.8px floor; footer stacks |
| ≤520px | 16px | 16px | 30.4px | metric grid 1 column; card padding 16px; buttons 38px tall, padding 0 12px, 13.12px; figcaption 14.72px |

## Components

- **Eyebrow tag** (`.eyebrow`): inline-block, #3d2f9a fill, white 15.2px/800 uppercase text, letter-spacing 0.08em, padding 3px 12px, radius 6px.
- **Venue pill** (`.venue-badge`): inline-flex, min-height 34px, padding 5px 14px, #f1effb fill, 1px #c9c0ee border, radius 999px, 13.76px/800 #3d2f9a; `::before` 7px #2b9c70 circle with 8px right margin. Hover: border #5b4bc4.
- **Link button** (`.button`): inline-flex, min-height 40px, padding 0 18px, gap 8px, #f1effb fill, 1px #c9c0ee border, radius 999px, 14.4px/700 #3d2f9a, inline 15px SVG icon left (file, GitHub, "E" glyph), shadow 0 8px 24px rgba(91,75,196,.09). Hover: fill #e6e2f8, border #5b4bc4, translateY(-1px), 160ms ease-out.
- **Section header**: kicker 12.8px/800 uppercase #3d2f9a, letter-spacing 0.06em, 12px below it a 44.8px/700 Noto Serif headline in #142030 with balanced wrapping, then an optional 16.32px #5a6779 note 14px below.
- **Figure card** (`.teaser`, `.wide-figure`): white, 1px #e0dcf3, radius 10px, shadow 0 24px 70px rgba(61,47,154,.12); image padded 14px 14px 0 and opens full size on click (zoom-in cursor); caption 15.36px #5a6779 with bold #142030 lead.
- **Claim card** (`.claim-card`): white, 1px #e0dcf3, radius 10px, padding 22px, shadow 0 18px 44px rgba(61,47,154,.07); index label 16px/900 #3d2f9a, 16px gap, then 17.92px/700 h3 and 15.36px #5a6779 text.
- **Method card** (`.method-flow article`): claim-card recipe plus a 3px top border, coloured per card #5b4bc4, #b5761f, #2b9c70 with h3 in #3d2f9a, #b5761f, #2b9c70.
- **Equation panel** (`.equation-panel`): #f1effb, 1px #c9c0ee, radius 10px, padding 18px 20px; label 13.12px/900 uppercase #3d2f9a; KaTeX at 16.8px #1e2e44.
- **Code card** (`.code-card`): #17142b, radius 10px, card shadow; header strip 13.12px/800 uppercase #c9c0ee, padding 12px 20px, 1px rgba(255,255,255,.1) bottom rule; JetBrains Mono 13.44px/1.6 #efedfb, comments #8f88b8, padding 16px 20px.
- **Metric card** (`.metric-card`): claim-card recipe; number 44.8px/700 #3d2f9a, line-height 1, tabular figures; label 14.88px/600 #5a6779, 10px below.
- **Table card with tabs**: white, 1px #e0dcf3, radius 10px, padding 18px 20px 14px, shadow 0 18px 44px rgba(61,47,154,.06). Dataset tabs are 999px pills (padding 5px 14px, 13.6px/700, 1px #c9c0ee, white with #3d2f9a text; selected #3d2f9a fill, white text) switched by `site.js`. Table 14.4px tabular, cells 7px 10px, rows ruled 1px #edf2f4, header 13.12px/700 #5a6779 over a 1.5px #e0dcf3 rule; "Ours" column or row #efecfb with #3d2f9a 700–800 text; best values 800, second best underlined at 3px offset; note below 13.76px #5a6779.
- **Callout** (`.callout`): #f1effb, 4px #5b4bc4 left bar, radius 0 10px 10px 0, padding 14px 18px, #2b2747 text, bold lead #3d2f9a.
- **BibTeX card** (`.bibtex-card`): #17142b, radius 10px, card shadow, `pre` padding 60px 22px 22px, 13.76px JetBrains Mono #efedfb; "Copy BibTeX" button top-right 14px in, min-height 34px, padding 0 12px, rgba(255,255,255,.1) fill, 1px rgba(255,255,255,.18) border, radius 8px, 13.6px/700 white; hover fill rgba(255,255,255,.18); label flips to "Copied" for 1.4s.
- **Footer** (`.footer`): 1px #e0dcf3 top border, padding 28px 0, flex row with 14.4px #5a6779 text left and a "Back to top" link right in #3d2f9a 700.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation bar | absent from the source | no nav; the footer has a "Back to top" link |
| Eyebrow / acronym tag | yes | filled indigo uppercase tag above the title |
| Title / subtitle | yes | two-tone 800-weight Inter title, slate one-paragraph subtitle |
| Venue badge | yes | lavender pill with a green dot |
| Authors / affiliations | yes | single underlined author, muted affiliation |
| Link buttons | yes | lavender pills with inline SVG icons |
| Teaser figure | yes | 1120px shadowed card with caption |
| Abstract | yes | two-column split: kicker and serif claim headline left, prose right |
| Method | yes | three colour-coded cards, equation panel, dark pseudo-code card |
| Key numbers | yes | four big-number metric cards |
| Results tables | yes | white table cards, dataset tabs, lavender "Ours" column |
| Qualitative figures | yes | wide figure cards and a figure/table split |
| Video | absent from the source | none |
| BibTeX | yes | dark card with copy button |
| Footer | yes | thin rule, muted line, back-to-top link |

## Adapting to Other Content

- **More authors**: keep `.author-list` at 16.48px/500 and put each author in `.author-line` (block on desktop, inline below 760px); use #5a6779 superscripts and add affiliations as further 13.76px #5a6779 lines.
- **Long publication or news lists**: use claim cards in a single column (white, 1px #e0dcf3, radius 10px, padding 22px) with the date as the 16px/900 #3d2f9a index label.
- **More results**: add table cards with the same tabs; mark the proposed method only with #efecfb background and #3d2f9a bold text, and keep best/second as bold/underline rather than colour.
- **More stats**: extend the 4-column metric grid; it drops to 2 columns at 960px and 1 at 520px.
- **A video**: place it in a `.wide-figure` card (white, 1px #e0dcf3, radius 10px, card shadow) with a figcaption.

## Do's and Don'ts

- Do set every section headline in Noto Serif 700 and everything else in Inter; the serif/sans switch is the page's signature.
- Do use #3d2f9a for all emphasis: kickers, numbers, active tabs, "Ours" cells and title line 1.
- Do keep amber #b5761f and green #2b9c70 to the second and third method cards and the venue dot.
- Do give cards and figures the violet-tinted shadow, not a gray one.
- Don't add a top navigation bar; the hero starts 62px from the top of the page.
- Don't fill buttons with solid indigo; they stay #f1effb pills with indigo text. Solid #3d2f9a is for the eyebrow tag and the selected tab only.
- Don't use dark surfaces except the #17142b code and BibTeX cards.

## Surfaces

White page (#ffffff) with alternating `.section-soft` bands: linear-gradient(180deg, #f8f7fd, #ffffff) between 1px rgba(224,220,243,.75) rules. White cards with 1px #e0dcf3 borders and violet-tinted shadows sit on both. Lavender inset surfaces (#f1effb) for equation panels, callouts, buttons and the venue pill; #efecfb for "Ours" table cells. Two dark inset cards (#17142b) for code and BibTeX.

## Imagery

Clean vector-style diagrams exported as WebP: the teaser framework figure with pale green panels, blue/orange heatmap grids and hand-drawn-style arrows; line plots of time series with shaded gaps and uncertainty bands; velocity-field magnitude panels. Images sit on white inside bordered, shadowed cards and open full size on click.

## Layout

Centred hero, full-width teaser card, then six sections in a 1120px container: Abstract (two-column split), The bottleneck (equation panel and two claim cards), Method (three cards, equation panel, code card), Results (metric cards, tabbed tables, figures, callout), Why it works (figure/table split and a wide figure), Citation. Generous 76px section padding and 22px card gaps give an airy, report-like rhythm.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #142030, slate #334155, muted #5a6779, indigo #3d2f9a, violet #5b4bc4, lavender fill #f1effb, lavender border #c9c0ee, line #e0dcf3, ours #efecfb, green #2b9c70, amber #b5761f, dark card #17142b.

1. "Build a centred hero on #ffffff with padding 62px 0 20px: an inline #3d2f9a tag with 15.2px/800 uppercase white text (letter-spacing 0.08em, padding 3px 12px, radius 6px); a 49.6px/800 Inter title, line-height 1.14, first phrase #3d2f9a and rest #142030; an 18.4px #334155 subtitle (max 820px); a venue pill (#f1effb, 1px #c9c0ee, radius 999px, 13.76px/800 #3d2f9a, 7px #2b9c70 dot); then 40px-tall link pills (#f1effb, 1px #c9c0ee, 14.4px/700 #3d2f9a, shadow 0 8px 24px rgba(91,75,196,.09); hover #e6e2f8 with #5b4bc4 border)."
2. "Create a section header and metric row: 12.8px/800 uppercase #3d2f9a kicker, 44.8px/700 Noto Serif #142030 headline, 16.32px #5a6779 note. Below, a 4-column grid (gap 18px) of white cards (1px #e0dcf3, radius 10px, padding 22px, shadow 0 18px 44px rgba(61,47,154,.07)) each with a 44.8px/700 #3d2f9a number and a 14.88px/600 #5a6779 label."
3. "Make a results table card: white, 1px #e0dcf3, radius 10px, padding 18px 20px 14px. Pill tabs 13.6px/700 (selected #3d2f9a fill with white text, others white with #3d2f9a text and 1px #c9c0ee). Table 14.4px tabular, cells 7px 10px, rows ruled 1px #edf2f4, header 13.12px/700 #5a6779; the 'Ours' column on #efecfb with bold #3d2f9a numbers."

## Similar Pages

- Hand-built single-author ML project pages with design tokens in `:root`, a serif section headline over sans body, and card-based results.
- Light lavender-accented pages that mark the proposed method with a tinted table column instead of colour-coded cells.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --ink: #142030;
  --muted: #5a6779;
  --line: #e0dcf3;
  --tint-25: #f8f7fd;
  --tint-50: #f1effb;
  --tint-100: #e6e2f8;
  --tint-200: #c9c0ee;
  --accent-500: #5b4bc4;
  --accent-700: #3d2f9a;
  --link: #4433b0;
  --green-500: #2b9c70;
  --amber-500: #b5761f;
  --ours-bg: #efecfb;
  --night: #17142b;
  --shadow: 0 24px 70px rgba(61, 47, 154, 0.12);
  --radius: 10px;
  --maxw: 1120px;
  --font-sans: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-serif: "Noto Serif", Georgia, "Times New Roman", serif;
  --font-mono: "JetBrains Mono", "SFMono-Regular", Consolas, Menlo, monospace;
}
```

## Provenance

- **URL**: https://zgp110.github.io/misspath-fm/
- **Paper**: MissPath-FM: Flow Matching with Structured Priors for Partially Observed Time Series (arXiv 2610.17715), Genpei Zhang.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv 2610.17715 comment states acceptance at NeurIPS 2026 and links this project page.
- **Template credit**: none stated; a custom static page (own `styles.css` and `site.js`, Google Fonts, KaTeX 0.16.11). Footer: "Page content released under CC BY-SA 4.0".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, a live render scrolled through Method and Results, and the page's `styles.css`, `site.js` and `index.html` read directly, on 2026-10-28.
