# ECAD Zinc Launch — Style Reference

> A product keynote on zinc paper: one electric-blue key, a slide deck for a hero, and a plot you can poke.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, and the page's own `ecad/static/css/index.css` (its `:root` token block, hover rules and media queries). The heading face Satoshi (Fontshare) and JetBrains Mono (Google Fonts) load; the body face Geist is declared but never loaded, so body text renders in the `system-ui` fallback (Segoe UI on Windows, San Francisco on macOS). The embedded teaser deck had not finished painting in the 1440×900 snap (it shows as a pale blur), so its contents are described from the tall screenshot. Color share is measured on that first viewport.

## Overview

The page reads like a small product launch. A zinc-white canvas (#fafafa) carries a flat electric-blue venue badge in mono caps, a tight black Satoshi Black title with negative tracking, grey system-UI author and affiliation lines, and three square-cornered mono buttons, of which only "Paper" is filled blue. Directly under them sits a 1100px embedded slide player: a white stage with a frosted glass-tile image in the upper right, a blue mono "INTRODUCING" kicker, a huge black "ECAD" wordmark, the subtitle with "Caching" underlined in blue, a mono "ICLR 2026 · UNIVERSITY OF MARYLAND" line, and a control strip with "01 / 13 · title", a boxed blue PAUSE button and a thin blue progress bar. Below, an italic grey caption, an 800px abstract with the full acronym set as a blue highlight chip, and an interactive Plotly Pareto explorer in a white bordered frame with blue corner brackets and a "Hover to Explore" side panel. Everything has 2px corners; blue (#2563eb) is the only hue in the chrome.

## First Viewport

Color share (1440×900, 8-color quantize): zinc canvas #fafafa 62.1%, pale deck placeholder #f6f7f8 26.5% and #f9fafa 6.2%, blue-grey blur #d9dce2 3.4%, near-white #fdfdfd 1.2%. The blue badge and Paper button and the black title are each under 1%. With the deck loaded, its white stage, black "ECAD" wordmark and the cool glass-tile photo take the 1100×682 block instead.

Anatomy in DOM order (x is centered on 720):

1. **Venue badge** — `.iclr-badge span`, "ACCEPTED AT ICLR 2026" ("ICLR 2026" in `strong`), JetBrains Mono 11.2px / 500, uppercase, letter-spacing 0.06em, #ffffff on #2563eb, padding 0.3rem 0.85rem, radius 2px, centered (y≈19–46). Gap to title about 36px (badge wrapper bottom padding 4px plus hero top padding 32px).
2. **Title** — `header.hero h1`, Satoshi 38.4px / 900, line-height 40.32px (1.05), letter-spacing −1.536px (−0.04em), #18181b, centered on two lines inside the 900px hero (y=82–163). Margin-bottom 16px.
3. **Authors** — `p.authors`, 18.4px system-UI, #71717a for the commas, names are `a` at weight 500 in #18181b (y=178–207). Gap 4px.
4. **Affiliation** — `p.affiliation`, "University of Maryland, College Park", 14px, #71717a (y=212–234). Gap 16px.
5. **Buttons** — `nav.links`, three `a[role=button]` 88/88/81×33px, 8px gap (y=250–283): Paper filled #2563eb with #ffffff text; arXiv and Code transparent with #71717a text and 1px #e4e4e7 border. Font JetBrains Mono 10.88px / 500, padding 6.72px 15.2px, radius 2px, Font Awesome icon left. Hero bottom padding 24px.
6. **Teaser deck** — `section.teaser .teaser-player iframe`, 1100px wide (x=170–1270) at y=307, 682px tall at 1440 (16:9 stage plus a 70px chapter strip).
7. **Caption** — `.teaser .caption`, 14px italic, #71717a, centered, max-width 800px, line-height 1.7, "ECAD" in #2563eb bold; 24px below the deck (just below the fold).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Zinc Canvas | #fafafa | `--bg` | `body` background, `details` summaries, baseline table rows, BibTeX `pre` |
| Ink Zinc | #18181b | `--text` | title, section headings, author names, `strong`, table body first columns |
| Muted Zinc | #71717a | `--muted` | paragraphs (`p` default), authors line, affiliation, outline button text, table headers and numbers, captions |
| Hairline | #e4e4e7 | `--border` | outline buttons, explorer frame, table wrappers, row rules, footer top rule, `pre` border |
| Surface | #ffffff | `--surface` | explorer frame, table wrappers, button hover fill |
| Electric Blue | #2563eb | `--accent` | venue badge, Paper button, links, acronym chip, explorer corner brackets, "ours" row bar, best values, deck kicker and progress bar |
| Deep Blue | #1d4ed8 | (literal) | Paper button hover fill and border |
| Blue Wash | rgba(37, 99, 235, 0.06) | `--accent-dim` | "ours" table rows, summary hover |
| Selection Blue | #dbeafe | `--accent-light` | text selection highlight |

Declared but not visible: `--success` #22c55e and `--success-light` #f0fdf4 have no rendered use in the first 2,700px.

## Tokens — Typography

- **Headings:** declared `'Satoshi', system-ui, sans-serif`; renders Satoshi 700 and 900 (both loaded from Fontshare). Substitute: General Sans or Manrope ExtraBold, which keep the compact geometric width.
- **Body:** declared `'Geist', system-ui, sans-serif`; Geist is not loaded, so it renders as Segoe UI (Windows) or SF Pro (macOS). Substitute that keeps the rendered look: Inter. If you want what the author intended, load Geist.
- **Mono:** declared `'JetBrains Mono', 'Geist Mono', monospace`; renders JetBrains Mono 400/500. Used for badge, buttons, table headers, code. Substitute: IBM Plex Mono.
- The scale is fluid (`clamp()`); values below are what renders at 1440.

| Role | Selector | Size / weight / line-height / tracking |
|---|---|---|
| Paper title | `.hero h1` (`--text-3xl`) | 38.4px / 900 / 1.05 / −0.04em |
| Section heading | `section h2` (`--text-2xl`) | 30.4px / 900 / 1.2 / −0.03em |
| Sub-heading | `h3` (`--text-xl`) | 22.4px / 700 / 1.2 / −0.02em |
| Small heading | `.key-findings h3` | 18.4px / 700 |
| Authors | `.hero .authors` (`--text-lg`) | 18.4px / 400, names 500 |
| Body / abstract | `p` (`--text-base`), `.abstract-section p` | 16px / 400 / 1.6 (abstract 1.75) |
| Affiliation, teaser caption | `--text-sm` | 14px |
| Small caption | `.caption` (`--text-xs`) | 13px italic |
| Venue badge | `.iclr-badge span` | mono 11.2px / 500 / uppercase / 0.06em |
| Buttons | `.hero .links a[role=button]` | mono 10.88px / 500 / 0.02em |
| Table header | `th` | mono 10px / 500 / uppercase / 0.8px |
| Table cell | `td` | 12.8px / 500 |
| Code | `pre` | mono 13px / 400 / 1.6 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Radius (badge, buttons, explorer, tables, `pre`) | 2px everywhere in the chrome |
| Images | 8px radius (`img` default) |
| Explorer frame | 1px #e4e4e7 border, shadow `0 2px 12px rgba(24,24,27,0.06)`, 12×12px L-brackets of 2px #2563eb at top-left and bottom-right (offset −2px) |
| Outline button | 1px #e4e4e7; hover border #71717a, fill #ffffff, text #18181b, `translateY(-1px)` |
| "Ours" table row | fill rgba(37,99,235,0.06), first cell `inset 3px 0 0 #2563eb` |
| Baseline row | fill #fafafa, first cell `inset 3px 0 0 #e4e4e7` |
| Key findings box | #fafafa fill, 1px #e4e4e7 border, 3px #2563eb left border, radius 0 2px 2px 0 |
| Spacing scale | 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px (`--space-xs` … `--space-4xl`) |

## Layout Metrics

- **Container:** `main.container-fluid` max-width 1200px, padding 0 40px, centered; inner measure 1120px (x=160–1280 at 1440).
- **Nested widths:** hero 900px, teaser 1100px (x=170–1270), abstract 800px (x=320–1120), explorer and results full 1120px.
- **Hero padding:** 32px top, 24px bottom; title 16px below; affiliation 16px above the buttons.
- **Section rhythm:** `section` margin-bottom 48px; teaser and explorer 64px; `h2` margin-bottom 24px.
- **Explorer:** grid `1fr 380px`, height 740px; plot padding 8px; Plotly modebar restyled as a bordered white strip.
- **Footer:** border-top 1px #e4e4e7, padding 64px 16px 32px, margin-top 32px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1267px | (viewport − 1120)/2 | 16px | 38.4px | explorer two columns |
| 1001–1266px | (viewport − 1120)/2, reaching 40px at 1200px and below | 16px | 35.2–38.3px (fluid) | none |
| 901–1000px | 40px | 16px | 34–35.2px | explorer stacks, plot 500px tall, panel gets a top rule |
| 769–900px | 40px | 16px | 32.4–34px | 2-col, 3-col and method grids become one column |
| 481–768px | 16px | 15.5–16px | 29–32.4px | hero buttons stack, each up to 180px wide; table cells padding 4px 8px |
| ≤480px | 16px | 15–15.5px | 24px (h2 20.8px) | badge 9.6px; plot 360px tall |

## Components

- **Venue badge:** inline-block, JetBrains Mono 11.2px / 500 uppercase, letter-spacing 0.06em, #ffffff on #2563eb, padding 0.3rem 0.85rem, 2px radius, no border or shadow; venue name in bold.
- **Primary button:** first `a[role=button]`, #2563eb fill and border, #ffffff mono 10.88px / 500 label, padding 0.42rem 0.95rem, 2px radius, icon left with 0.5em gap; hover #1d4ed8.
- **Outline button:** transparent, 1px #e4e4e7 border, #71717a label, same type and padding; hover border #71717a, fill #ffffff, label #18181b, lifts 1px.
- **Slide-deck teaser:** iframe player, white stage, cool frosted glass-tile image fading in from the top right; left-aligned mono blue kicker "INTRODUCING" (letter-spaced), a huge black Satoshi "ECAD", a one-line subtitle with a blue underline under one word, a hairline rule, grey author names, and a blue mono caps venue line. Control strip under the stage: mono "01 / 13 · title" left, prev/next arrows, a boxed blue "PAUSE" chip and a fullscreen icon right, and a 2px blue progress bar.
- **Acronym chip:** `.ecad-acronym`, inline #2563eb highlight with #ffffff bold text, padding 0.1em 0.4em, 2px radius, `box-decoration-break: clone` so it wraps cleanly.
- **Pareto explorer:** white frame, 1px #e4e4e7, 2px radius, soft shadow, blue L-shaped corner brackets; Plotly scatter left (blue circles for ECAD schedules, thin colored lines for baselines, black cross for "Unaccelerated"), 380px side panel right with a grey circled-plus icon, "Hover to Explore" in bold and a muted hint.
- **Collapsible table:** `details.table-section` inside a white bordered wrapper (hover border #71717a); summary bar #fafafa, Satoshi 700 16px, mono ">" marker, hover rgba(37,99,235,0.06).
- **Results table:** mono 10px uppercase #71717a headers, 12.8px cells, 1px #e4e4e7 row rules, first two columns in the body font and #18181b; "ours" rows blue-washed with a 3px blue inset bar; best values bold #2563eb; row hover rgba(37,99,235,0.06).
- **Key findings:** #fafafa box with 3px blue left edge, its `h3` set as a white bordered tab inside.
- **BibTeX:** `pre` on #fafafa, 1px #e4e4e7, 2px radius, padding 16px, JetBrains Mono 13px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue badge | Yes | flat blue mono caps chip above the title |
| Title / authors / affiliation | Yes | centered, Satoshi Black title, grey system-UI lines |
| Link buttons | Yes | three square mono buttons, first filled blue |
| Teaser | Present but non-standard | an embedded 13-slide autoplaying deck instead of an image or video |
| TL;DR caption | Yes | italic 14px grey line under the deck |
| Abstract | Yes | 800px column, acronym as a blue highlight chip |
| Interactive figure | Yes | Plotly Pareto explorer with hover panel |
| Method figure | Yes | `method-grid` 1.2fr / 1fr with "Key Components" list |
| Results tables (HTML) | Yes | collapsible bordered tables with "ours" rows tinted |
| Key findings callout | Yes | blue-edged box |
| Qualitative results | Yes | image grids (2- and 3-column) |
| BibTeX | Yes | mono `pre` |
| Footer | Yes | hairline rule, mono outline buttons, CC BY-SA license line |
| Navigation bar | No (absent from the source) | |
| Video | No (absent from the source) | the deck plays the role of motion |

## Adapting to Other Content

- **More authors:** keep one centered 18.4px line with names at weight 500 #18181b and commas in #71717a; let it wrap; put affiliations with superscript numbers on the 14px #71717a line.
- **Results table:** reuse the collapsible table recipe; mono uppercase headers, a 3px blue inset bar and 6% blue wash on your method's row, best numbers bold #2563eb, second-best underlined rather than adding a second color.
- **Long publication or news list:** a 1120px list with 1px #e4e4e7 rules between items, dates in JetBrains Mono 10.88px #71717a on the left, titles in Satoshi 700 #18181b.
- **No slide deck:** use a 1100px figure with 8px radius in the teaser slot and keep the italic caption; do not add a shadow to it.
- **Extra links (Video, Data, Demo):** add more outline mono buttons; keep exactly one filled blue primary.

## Do's and Don'ts

- Do keep blue as the only chroma in the chrome; everything else is zinc greys.
- Do keep corners at 2px on every control and container; only images get 8px.
- Do set the title in a heavy geometric face with negative tracking.
- Do load Geist (or name Inter) explicitly; the source falls back to system-ui without it.
- Don't give more than one button a fill.
- Don't use drop shadows beyond the single soft one on the explorer frame.
- Don't color body paragraphs black; the muted #71717a is the body voice, with #18181b reserved for `strong` and headings.

## Surfaces

One zinc-white canvas (#fafafa) with white (#ffffff) bordered frames for interactive and tabular content; #fafafa summary bars and code blocks; no tinted bands or dark sections. The teaser deck is a white stage inside the canvas.

## Imagery

A slide deck with a frosted blue-grey glass-tile photo; a Plotly scatter with blue ECAD points; method diagrams; generated image grids (PixArt and FLUX samples) on white; caching schedule heatmaps that open in a lightbox.

## Layout

Single centered column with stepped widths (900 hero, 1100 teaser, 800 abstract, 1120 content), generous 48–64px section gaps. Rendered height about 9,250px.

## Agent Prompt Guide

Quick colors: canvas #fafafa, text #18181b, muted #71717a, hairline #e4e4e7, surface #ffffff, accent #2563eb, accent hover #1d4ed8, accent wash rgba(37,99,235,0.06).

1. "Build a hero on #fafafa: a centered JetBrains Mono 11.2px/500 uppercase badge (letter-spacing 0.06em, #ffffff on #2563eb, padding 0.3rem 0.85rem, 2px radius); then a Satoshi 38.4px/900 title with −0.04em tracking and 1.05 line-height in #18181b; authors at 18.4px with names #18181b weight 500; affiliation 14px #71717a; three mono 10.88px buttons, 2px radius, padding 0.42rem 0.95rem, the first filled #2563eb (hover #1d4ed8), the others transparent with 1px #e4e4e7 border and #71717a text."
2. "Create an interactive chart frame: white #ffffff box, 1px #e4e4e7 border, 2px radius, box-shadow 0 2px 12px rgba(24,24,27,0.06), grid 1fr 380px at 740px height, with 12px L-shaped 2px #2563eb corner brackets at top-left and bottom-right."
3. "Style a results table: header cells JetBrains Mono 10px/500 uppercase, letter-spacing 0.8px, #71717a; body 12.8px; 1px #e4e4e7 row rules; our row filled rgba(37,99,235,0.06) with an inset 3px #2563eb bar on the first cell; best values bold #2563eb."

## Similar Pages

- The author's own site (aniaggarwal.com), whose design system this page states it matches.
- Product-launch style research pages that embed a slide deck or keynote player as the teaser.

## Quick Start

```css
:root {
  --bg: #fafafa;
  --text: #18181b;
  --muted: #71717a;
  --border: #e4e4e7;
  --surface: #ffffff;
  --accent: #2563eb;
  --accent-hover: #1d4ed8;
  --accent-dim: rgba(37, 99, 235, 0.06);
  --accent-light: #dbeafe;
  --font-heading: 'Satoshi', 'General Sans', sans-serif;
  --font-body: 'Geist', 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', 'IBM Plex Mono', monospace;
  --radius: 2px;
  --title-size: 38.4px;
  --h2-size: 30.4px;
  --body-size: 16px;
  --container: 1200px;
  --gutter: 40px;
}
```

## Provenance

- **URL:** https://research.aniaggarwal.com/ecad
- **Paper:** Evolutionary Caching to Accelerate Your Off-the-Shelf Diffusion Model (arXiv 2506.15682), Anirud Aggarwal, Abhinav Shrivastava, Matthew Gwilliam.
- **Venue:** ICLR 2026 (badge on the page: "Accepted at ICLR 2026").
- **Selection reason:** the arXiv comment states acceptance at ICLR 2026 and links this page; chosen for its embedded slide-deck hero, mono kickers and interactive Pareto plot with a hover panel.
- **Template credit:** none stated; the stylesheet header says it matches the aniaggarwal.com design system (Satoshi, Geist, JetBrains Mono, electric blue).
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `ecad/static/css/index.css`, page HTML; 2026-10-28.
