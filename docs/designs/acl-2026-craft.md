# Blueprint Docs Console — Style Reference

> A tidy product manual in pale blueprint blue, where every stage wears its own colored edge.

**Theme:** both

Measured on 2026-10-28 from a headless Chrome render at 1440×900 in light mode (computed styles of the top bar, segmented control, hero, buttons, section heads, abstract, code blocks and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's single inline `<style>` block and HTML. The page also defines a full dark palette (via `prefers-color-scheme: dark` and a ◐ toggle); the dark values below come from that CSS, since the render is light. Positions are document coordinates at 1440px wide.

## Overview

CRAFT is a single-file, hand-built page that behaves like product documentation. A sticky translucent top bar holds a serif "CRAFT" wordmark, a Demo/Paper segmented switch (Paper active by default, a live retrieval explorer behind Demo), two grey text links and a theme toggle. The compact hero sits on a pale blue diagonal gradient: a solid blue "ACL 2026" pill, a 36.8px Source Serif 4 bold title with "CRAFT" in blue, an italic serif tagline, Inter authors and affiliations, and a row of 8px-radius buttons (gold "Try the Demo", blue "Paper (ACL)", six white outlined). Below, on a #f3f7fd page, sections open with a blue uppercase eyebrow and a 23.2px serif heading, separated by 1px #cfdcee rules. The overview is a serif paragraph with a 4px gold left bar; the pipeline is a three-card grid whose cards carry 4px blue, gold and violet left edges; the framework figure sits in a rounded, softly shadowed frame; install and BibTeX are dark navy code blocks.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): page blue-white #f3f7fd 43.8%, hero gradient #edf5fe 24.0%, hero gradient #f0f7ff 9.7%, slate grey #c3ccd7 8.1% (text anti-aliasing and rules), #f4f7fd 7.0%, #f7fafe 4.0%, remainder under 3%. Accents are small: the blue pill and primary button (#2f6fd0), the gold demo button and abstract bar (#eab308).

Anatomy in DOM order (y = top of element box):

1. **Top bar** (`header.topbar`), y 0, 1440×58 plus a 1px #cfdcee bottom border, background `color-mix(#f3f7fd 86%, transparent)` with 10px backdrop blur; inner row max-width 1080px (x 180–1260), padding 9.6px 19.2px, gap 16px.
2. **Wordmark** (`.brand`), x 199, "CRAFT" in Source Serif 4 18.4px/700, #2f6fd0.
3. **Segmented control** (`.segmented`), x 296, a #eaf2fc track with 1px #cfdcee border, radius 9.6px, padding 3px; buttons Inter 14.72px/700, padding 6.4px 18.4px, radius 7.2px; inactive "Demo" #5a6b82, active "Paper" #ffffff on #2f6fd0 with shadow 0 1px 4px rgba(23,45,80,0.1).
4. **Right links**: "GitHub" and "Paper" (`a.ghost`) Inter 13.6px/600 #5a6b82, then a 34×34 theme toggle (#ffffff, 1px #cfdcee, radius 8px). Hero begins at y 59.
5. **Venue pill** (`.venue`), y about 97, "ACL 2026", Inter 11.52px/700, uppercase, letter-spacing 0.08em, #ffffff on #2f6fd0, radius 999px, padding 4.5px 13.6px. Gap 14.4px.
6. **Title** (`.hero h1`), y 140, max-width 780px, two lines, Source Serif 4 36.8px/700, line-height 44.2px, #16233a with "CRAFT" in #2f6fd0, centered. Gap 8px.
7. **Tagline** (`.tag`), y 236, Source Serif 4 italic 16.32px, #5a6b82, max-width 560px. Gap 16px.
8. **Authors** (`.authors`), y 278, Inter 14.4px #33445e, first two names bold #16233a. Gap 3px.
9. **Affiliations** (`.affil`), y 304, Inter 12.48px #5a6b82, joined by " · ". Gap 18px.
10. **Button row** (`.btn-row`), y 342, nine buttons 43px tall, gap 9.6px, centered (x 215–1226): gold "Try the Demo" (#eab308 fill, #3a2c05 text), blue "Paper (ACL)" (#2f6fd0 fill, white text), then white outlined "Paper PDF", "Slides", "Poster", "arXiv", "Datasets", "Code"; 15px line icons on the left. Hero ends at y 417 with a 1px #cfdcee border.
11. **Section start**: eyebrow "OVERVIEW" (y about 451) and h2 "What CRAFT is" (y 474), then the gold-barred abstract at y 534.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Page | #f3f7fd | `--page-bg` | Page background, top bar glass base |
| Hero A / B / C | #e8f0fd → #eef6ff → #f4f8fe | `--hero-a/b/c` | Hero `linear-gradient(160deg, …)` |
| Surface | #ffffff | `--surface` | Outlined buttons, feature cards, theme toggle, demo panels |
| Surface Soft | #eaf2fc | `--surface-soft` | Segmented control track, inline `code` background, table headers, demo panel heads |
| Ink | #16233a | `--ink` | Title, section headings, card titles, outlined button text |
| Body | #33445e | `--body` | Authors, abstract, lead text, card text |
| Muted | #5a6b82 | `--muted` | Tagline, affiliations, top-bar links, inactive segment, captions, footer |
| Blue | #2f6fd0 | `--blue` | Wordmark, "CRAFT" in the title, venue pill, active segment, primary button, eyebrows, links, abstract bold, stage-1 card edge |
| Blue Dark | #1e4fa0 | `--blue-dk` | Primary button hover |
| Gold Bright | #eab308 | `--gold-bright` (`--brand-gold`) | "Try the Demo" button, abstract left bar, stage-2 card edge, flow arrows |
| Gold Text | #b7860b | `--gold` | Stage-2 card label, "best" highlights in results text |
| Gold Button Text | #3a2c05 | `.btn-gold` | Text on the gold button |
| Violet | #6d4bd6 | `--brand-violet` (`--purple`) | Stage-3 card edge and label |
| Green | #1f9d57 | `--green` | Benefit numbers in the demo explainer |
| Border | #cfdcee | `--border` | Top bar and hero bottom borders, section dividers, card and button borders, footer rule |
| Border Soft | #e2ecf8 | `--border-soft` | Stripes in table glyphs (demo) |
| Code | #16233a | `--code-bg` | Install and BibTeX code block background |
| Code Text | #dbe6c9 | `--code-fg` | Code block text (comments #93a2b8) |
| Dark Page | #0e141d | dark `--page-bg` | Page background in dark mode |
| Dark Surface | #161e2a | dark `--surface` | Cards and buttons in dark mode |
| Dark Ink | #e7eef8 | dark `--ink` | Headings in dark mode |
| Dark Blue | #6ea8fe | dark `--blue` | Accent in dark mode |

Declared but not visible: `--brand-blue` #2f7fe0, `--brand-navy` #1e3a5f and `--brand-teal` #2e9bb0 are palette notes lifted from the paper figure and are not applied to any element.

## Tokens — Typography

- **Headings and prose**: declared `'Source Serif 4', serif` for `h1–h4`, the tagline and the abstract, from Google Fonts (400, 600, 700, 400 italic). Rendered: Source Serif 4 400, 400i, 700 (`fonts_loaded`). Substitute: Source Serif Pro (same design, earlier release).
- **UI and body**: declared `'Inter', sans-serif` (Google Fonts 400–800). Rendered: Inter 400, 600, 700. Card titles (`h4`) are reset to Inter.
- **Buttons quirk**: `.btn` sets no font family, so the `<button>` "Try the Demo" renders in the browser default Arial while the `<a>` buttons inherit Inter.
- **Mono**: `'SFMono-Regular', 'Consolas', monospace` for code blocks (system font).

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `.hero h1` | 36.8px / 44.2px (`clamp(1.5rem, 3.6vw, 2.3rem)`) | 700 serif | #16233a, "CRAFT" #2f6fd0 |
| Section heading | `.h-sec` | 23.2px / 27.8px | 700 serif | #16233a |
| Wordmark | `.brand` | 18.4px | 700 serif | #2f6fd0 |
| Tagline | `.hero .tag` | 16.32px / 26.1px | 400 italic serif | #5a6b82 |
| Abstract | `.abstract` | 16px / 28px (1.75) | 400 serif | #33445e |
| Card title | `.fcard h4` | 16px | 700 Inter | #16233a |
| Body | `body` | 16px / 25.6px | 400 | #16233a |
| Lead | `.lead` | 15.68px | 400 | #33445e |
| Segment button | `.seg-btn` | 14.72px | 700 | #5a6b82 / #ffffff |
| Authors | `.authors` | 14.4px / 23px | 400 (names 700) | #33445e |
| Button | `.btn` | 14.08px / 22.5px | 600 | per variant |
| Card text | `.fcard p` | 13.6px / 1.5 | 400 | #33445e |
| Code | `.code` | 13.12px / 22.3px | 400 mono | #dbe6c9 |
| Caption, footer | `.cap`, `footer` | 13.12px | 400 (caption italic) | #5a6b82 |
| Affiliations | `.affil` | 12.48px | 400 | #5a6b82 |
| Eyebrow | `.eyebrow` | 11.84px, uppercase, 0.09em | 700 | #2f6fd0 |
| Venue pill | `.venue` | 11.52px, uppercase, 0.08em | 700 | #ffffff |
| Card label | `.fcard .k` | 11.2px, uppercase, 0.08em | 700 | #2f6fd0 / #b7860b / #6d4bd6 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons (`.btn`) | 8px | 2px solid (gold #eab308, blue #2f6fd0, outline #cfdcee) | none |
| Segmented track / segment | 9.6px / 7.2px | 1px #cfdcee / none | active segment 0 1px 4px rgba(23,45,80,0.1) |
| Venue pill | 999px | none | none |
| Feature card (`.fcard`) | 11.2px | 1px #cfdcee, 4px left color bar (`::before`) | none |
| Framework figure (`.fig`) | 12px | 1px #cfdcee | 0 4px 22px rgba(23,45,80,0.1) |
| Code block (`.code`) | 11.2px | none | none |
| Demo panels (`.play`, `.hiw`) | 16px | 1px #cfdcee | 0 8px 30px rgba(23,45,80,0.1) |
| Abstract | 0 | 4px solid #eab308 left | none |
| Divider (`hr.divider`) | 0 | 1px #cfdcee top, margin 38.4px 0 | none |
| Theme toggle | 8px | 1px #cfdcee | none |

## Layout Metrics

- **Container**: `main` and `.topbar-inner` max-width 1080px centered with 19.2px side padding, so content spans x 199–1241 (1042px).
- **Hero**: full-width gradient band, padding 38.4px 19.2px 32px, centered; title max-width 780px, tagline 560px.
- **Main**: padding 32px 19.2px 48px. Sections are separated by `hr.divider` (38.4px above and below), not by padding blocks.
- **Abstract**: max-width 68ch (575px), 20.8px left padding inside the gold bar, 32px top margin.
- **Card grids**: `.grid-3` three equal columns and `.grid-2` two columns, gap 14.4px; card padding 17.6px 18.4px. `.mt-lg` adds 32px above.
- **Figure**: `.fig.wide` full container width (1042px), margin 19.2px auto; centered italic caption.
- **Code blocks**: full width, padding 17.6px 20.8px, 12.8px top margin. Rendered height about 4,050px at 1440px (Paper panel).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1081px | 19.2px inside a 1080px container | 16px | 36.8px | three-card and two-card grids |
| 721–1080px | 19.2px | 16px | 3.6vw (26–36.8px) | grids unchanged; button row wraps |
| ≤720px | 19.2px | 16px | 24px minimum | `.grid-3` and `.grid-2` become one column; demo explainer stacks |

## Components

- **Segmented Demo/Paper switch**: inline-flex track #eaf2fc with 1px #cfdcee border, 9.6px radius, 3px padding, 2px gap; segments Inter 14.72px/700, padding 6.4px 18.4px, 7.2px radius, inactive #5a6b82 (hover #16233a), active #ffffff on #2f6fd0. A delayed gold hint bubble (#eab308, #3a2c05 text) can point visitors to Demo.
- **Hero button**: inline-flex, gap 6.4px, padding 8px 17.6px, 8px radius, 2px border, Inter 14.08px/600, 15px line icon left. Variants: gold (#eab308 fill and border, #3a2c05 text, hover brightness 1.05); primary (#2f6fd0, white text, hover #1e4fa0); outline (#ffffff fill, #cfdcee border, #16233a text, hover border and text #2f6fd0).
- **Venue pill**: solid #2f6fd0, white 11.52px/700 uppercase text, 999px radius.
- **Section head**: eyebrow 11.84px/700 uppercase #2f6fd0 (5.6px below), then a 23.2px Source Serif 4 bold h2.
- **Gold-bar abstract**: Source Serif 4 16px/1.75 #33445e, 4px solid #eab308 left border, 20.8px left padding, bold terms in #2f6fd0.
- **Stage card**: #ffffff, 1px #cfdcee border, 11.2px radius, padding 17.6px 18.4px, a 4px full-height left bar (#2f6fd0, #eab308 or #6d4bd6); uppercase label 11.2px/700 in the stage color ("STAGE 1 · SPARSE"), Inter 16px bold title, 13.6px #33445e text. A second row uses emoji icons (22.4px) instead of labels.
- **Framed figure**: image with 12px radius, 1px #cfdcee border and 0 4px 22px rgba(23,45,80,0.1) shadow; italic centered 13.12px #5a6b82 caption.
- **Code block**: #16233a background, #dbe6c9 text, mono 13.12px/1.7, 11.2px radius, padding 17.6px 20.8px; the BibTeX block has a "Copy" chip top right (rgba(255,255,255,0.1) fill, 1px rgba(255,255,255,0.16) border).
- **Footer**: centered 13.12px #5a6b82 links row above a 1px #cfdcee rule, padding 32px 19.2px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky top bar | yes | wordmark, segmented switch, text links, theme toggle |
| Venue badge | yes | solid blue pill |
| Title, tagline, authors | yes | centered serif title with blue acronym |
| Link buttons | yes | nine 8px-radius buttons, gold, blue and outlined |
| Abstract / overview | yes | serif paragraph with gold left bar |
| Method cards | yes | three stage cards with colored left edges, three feature cards |
| Pipeline figure | yes | full-width framed image |
| Datasets | yes | two cards plus a lead and an install code block |
| Interactive demo | yes | separate "Demo" panel with a search box, stage flow and result cards |
| Results table | present but non-standard | styles exist (`.rtable`) but the Paper panel shows results only in prose; the demo shows per-query mini-tables |
| Stat tiles | present but non-standard | `.tiles` styles exist for the demo; not on the Paper panel |
| BibTeX | yes | dark code block with Copy button |
| Videos | absent from the source | none |
| Footer | yes | centered link row |

## Adapting to Other Content

- **More authors**: keep a single centered Inter 14.4px line that wraps, bold the equal-contribution names, and keep affiliations on one 12.48px line below.
- **A results table**: use the declared `.rtable`: 14.08px Inter, header row #eaf2fc with 700 #33445e labels and a 2px #cfdcee bottom rule, 1px #cfdcee row rules, tabular numerals; the best row tinted 13% gold over white with a 3px #eab308 inset left edge and its first cell in #2f6fd0.
- **Headline numbers**: use `.tiles`: auto-fit cards min 150px, white, 1px #cfdcee, 11.2px radius, value 27.2px/800 Inter in #2f6fd0 (gold #b7860b for the featured tile with a 3px gold inset), label 12.16px #5a6b82.
- **Videos**: frame like `.fig` (12px radius, 1px #cfdcee, soft blue shadow) with an italic centered caption.
- **Long publication lists or news**: stacked white cards with a colored 4px left edge per category and an uppercase 11.2px label.
- **Dark mode**: swap to #0e141d page, #161e2a surfaces, #e7eef8 ink and #6ea8fe blue; keep the gold accent.

## Do's and Don'ts

- Do color-code the stages consistently: blue, gold, violet, as 4px left edges and matching labels.
- Do keep headings in Source Serif 4 and every control in Inter.
- Do separate sections with a 1px #cfdcee rule and an uppercase blue eyebrow.
- Do give the one call to action (the demo) the gold fill; the paper link is blue, the rest outlined.
- Don't use large radii; controls stay at 7–8px and cards at 11–12px.
- Don't add shadows to static cards; only figures and demo panels float.
- Don't make headings large; the title is 36.8px and section heads 23.2px.

## Surfaces

The page is #f3f7fd; the hero is a 160° gradient from #e8f0fd to #f4f8fe with a bottom border; cards and buttons are white with #cfdcee borders; code blocks are deep navy #16233a; the segmented track and table headers use #eaf2fc. Dark mode mirrors this on #0e141d and #161e2a.

## Imagery

One large paper figure of the framework: hand-drawn table stacks, magnifier icons, blue arrows, Gemini logos and star-topped "top-k" tables, boxed in black outlines with dashed stage regions. Emoji icons (🔍 📋 ✂) head the feature cards. A Hugging Face badge sits inline in the dataset text.

## Layout

A single 1042px column under a full-width hero band. Prose stays near 68ch on the left; card grids and the figure use the full width. Sections follow eyebrow, heading, content, divider, with a second "Demo" panel swapped in by the segmented control instead of a separate page.

## Agent Prompt Guide

Quick colors: page #f3f7fd, surface #ffffff, soft #eaf2fc, ink #16233a, body #33445e, muted #5a6b82, blue #2f6fd0, gold #eab308, violet #6d4bd6, border #cfdcee, code #16233a.

1. "Build a compact centered hero on a linear-gradient(160deg, #e8f0fd, #eef6ff 55%, #f4f8fe) band with a 1px #cfdcee bottom border: a #2f6fd0 pill with 'ACL 2026' in white 11.52px/700 uppercase Inter; a Source Serif 4 36.8px/700 #16233a title with the acronym in #2f6fd0; an italic 16.32px #5a6b82 tagline; Inter 14.4px #33445e authors; then a row of 8px-radius buttons with 2px borders: gold #eab308 with #3a2c05 text, blue #2f6fd0 with white text, the rest #ffffff with #cfdcee borders and #16233a text."
2. "Create three stage cards in a 3-column grid with 14.4px gaps: white, 1px #cfdcee border, 11.2px radius, padding 17.6px 18.4px, a 4px full-height left bar in #2f6fd0, #eab308 and #6d4bd6 respectively; an uppercase 11.2px/700 label in the stage color, an Inter 16px bold #16233a title, and 13.6px #33445e text."
3. "Add a dark code block: background #16233a, text #dbe6c9, SFMono 13.12px with line-height 1.7, 11.2px radius, padding 17.6px 20.8px, with a small 'Copy' chip at top right."

## Similar Pages

- Developer documentation and product landing pages (Docusaurus or Stripe-docs-like) adapted to a paper.
- Project pages that pair a static paper view with an in-page interactive demo.

## Quick Start

```css
:root {
  --page-bg: #f3f7fd;
  --surface: #ffffff;
  --surface-soft: #eaf2fc;
  --ink: #16233a;
  --body: #33445e;
  --muted: #5a6b82;
  --blue: #2f6fd0;
  --blue-dk: #1e4fa0;
  --gold-bright: #eab308;
  --gold: #b7860b;
  --purple: #6d4bd6;
  --border: #cfdcee;
  --code-bg: #16233a;
  --code-fg: #dbe6c9;
  --shadow: rgba(23, 45, 80, 0.10);
  --max-w: 1080px;
  --font-sans: 'Inter', sans-serif;
  --font-serif: 'Source Serif 4', serif;
}
@media (prefers-color-scheme: dark) {
  :root { --page-bg: #0e141d; --surface: #161e2a; --ink: #e7eef8; --blue: #6ea8fe; }
}
```

## Provenance

- **URL**: https://coral-lab-asu.github.io/CRAFT/
- **Paper**: CRAFT: Training-Free Cascaded Retrieval for Tabular QA (arXiv 2505.14984), Adarsh Singh, Kushal Raj Bhandari, Jianxi Gao, Soham Dan, Vivek Gupta (Arizona State University, Rensselaer Polytechnic Institute, Microsoft).
- **Venue**: ACL 2026 Main.
- **Selection reason**: arXiv 2505.14984 comment states acceptance at ACL 2026 Main ("ACL 2026 Mains"); project page linked in the abstract. Chosen for its product-documentation style: sticky nav with a Demo/Paper toggle, color-coded three-stage cards, a bar-quoted overview and a framed pipeline figure.
- **Template credit**: none; the CSS notes that the palette was lifted from the paper's pipeline figure.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 (light) with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture, the inline `<style>` block and HTML. Date 2026-10-28.
