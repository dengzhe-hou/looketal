# Time-IMM Slate Pills — Style Reference

> A tidy SaaS changelog for a dataset: heavy slate headline, a row of candy-coloured pills, and soft grey cards that never raise their voice.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against `static/css/index.css` (the Academic Project Page Template stylesheet with a Tailwind-like token layer), Bulma 0.9 and inline styles in `index.html`. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

A Bulma page from Eliahu Horwitz's Academic Project Page Template, restyled with a slate and blue token set and Inter throughout. The hero is white: a heavy 48px/800 slate title over three lines, bold blue author links, affiliations, a correspondence e-mail, and a row of five 12px-radius buttons. Paper, Code and arXiv are slate `#1e293b` with soft shadows, Dataset is Bulma info blue `#3298dc`, and SlidesLive is Bulma danger pink `#f14668`. A fixed "More Works" dropdown button floats in the top-right corner. A rounded, shadowed poster thumbnail with a centred caption serves as the teaser. The abstract sits in a pale `#f8fafc` band with hairline top and bottom borders, under a heading with a short pink-to-coral gradient underline, in justified grey text. Dataset, benchmark and results figures are shown in white 16px-radius carousel cards, followed by an embedded PDF poster, a BibTeX block with a blue Copy button and a pale footer. Document height is about 5,313px.

## First Viewport

Color share of the first 1440×900 viewport: `#ffffff` 80.1% (page and hero), `#b2b0c0` 5.3% (blue taxonomy wedges in the teaser), `#524a59` 3.9% (dark figure text and buttons), `#d7dee6` 3.6% (pale blue figure panels), `#fae2c1` 3.5% (yellow figure wedges and panels), `#fbfafa` 2.9%, `#fffffd` 0.5%, `#fdffff` 0.2%.

Anatomy in DOM order (centred in a 960px column):

1. "More Works" button, `position: fixed` at top 32px / right 32px (168×45px at x=1240), white, 2px `#e2e8f0` border, 16px radius, Inter 14.4px/600 `#1e293b`, flask icon left and chevron right, md shadow.
2. Hero `section.hero` with `.hero-body` padding 64px 24px; title `h1.title.is-1.publication-title`, Inter 48px/800, `#1e293b`, line-height 52.8px, three lines (y=64 to 222). Gap 32px plus Bulma spacing (about 40px).
3. Authors, two rows, Inter 20px/600, `#2563eb`, line-height 32px, superscripts and commas in `#1e293b`. Gap about 22px.
4. Affiliations, two lines of `span.author-block`, 16px/400 `#1e293b`; then "* Correspondence:" with the e-mail link in `#3273dc` (y≈406). Gap about 16px.
5. Buttons row, `.link-block a` with 8px 4px margins, each 40px tall at y=450: Paper, Code (slate), Dataset (`#3298dc`), arXiv (slate), SlidesLive (`#f14668`). Hero ends at y=574.
6. Teaser `section.hero.teaser`, `.hero-body` padding 32px 24px 64px: poster thumbnail 730×547px at y=606, max-width 80%, 10px radius, shadow `0 2px 10px rgba(0,0,0,0.1)`; it crosses the fold. The caption `h2.subtitle` (20px `#4a4a4a`) follows at y=1177.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Ink | `#1e293b` | `--text-primary` | Title, body text, affiliations; Paper, Code, arXiv button fill; BibTeX text |
| Royal Blue | `#2563eb` | `--primary-color` | Author names, Copy button, slate-button hover fill, footer links, focus rings |
| Royal Blue Hover | `#1d4ed8` | `--primary-hover` | Author link hover, Copy hover |
| Info Blue | `#3298dc` | Bulma `.is-info` | Dataset button |
| Danger Pink | `#f14668` | Bulma `.is-danger` | SlidesLive button |
| Accent Pink | `#f093fb` → `#f5576c` | `--gradient-accent` | 60×3px underline under section `title is-3` headings; author-link hover underline |
| Muted Slate | `#64748b` | `--text-secondary` | Abstract text, carousel captions, footer text |
| Mist | `#f8fafc` | `--background-secondary` | Abstract and Poster bands, footer |
| Code Mist | `#f1f5f9` | `--background-accent` | BibTeX `pre` and `code` fill |
| Hairline | `#e2e8f0` | `--border-color` | Band top/bottom borders, card borders, More Works border, `pre` border |
| Bulma Title Grey | `rgba(0,0,0,0.7)` | Bulma `.hero.is-light .title` | "Abstract" and "Poster" headings inside light bands |
| Bulma Charcoal | `#363636` | Bulma `.title` | "Time-IMM Dataset", "IMM-TSF Benchmark Library" headings |
| Subtitle Grey | `#4a4a4a` | Bulma `.subtitle` | Teaser caption and section subtitles |
| Mail Blue | `#3273dc` | Bulma `a` | Correspondence e-mail link |
| Copied Green | `#10b981` | `.copy-bibtex-btn.copied` | Copy button after click |

## Tokens — Typography

- **Declared:** `body { font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif; line-height: 1.6 }`; `.publication-title`, `.publication-authors`, `.title.is-3` force `'Inter', sans-serif`. Code uses `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace`.
- **Rendered:** Inter 400, 500, 600, 700, 800 loaded; Academicons and the Font Awesome JS kit for icons. BibTeX renders in Cascadia Code on Windows (first available in the mono stack). Substitute for Inter: Geist or Manrope at the same weights.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px | 800 | 52.8px | `#1e293b` |
| Band heading | `h2.title.is-3` | 32px | 700 | 36px | `rgba(0,0,0,0.7)` in light bands, pink bar below |
| Section heading | `h1.title.has-text-centered` | 32px | 600 | 36px | `#363636` |
| Section subtitle | `h2.subtitle` | 20px | 400 | 25px | `#4a4a4a` |
| Carousel caption | `.results-carousel .subtitle` | 16px | 500 | 20px | `#64748b` |
| Authors | `.publication-authors a` | 20px | 600 | 32px | `#2563eb` |
| Body, affiliations | `body` | 16px | 400 | 25.6px | `#1e293b` |
| Abstract | `.content.has-text-justified` | 17.6px | 400 | 31.7px | `#64748b`, justified |
| Buttons | `.button` | 16px | 600 | 24px | `#ffffff` |
| More Works | `.more-works-btn` | 14.4px | 600 | normal | `#1e293b` |
| BibTeX | `pre`, `code` | 14.4px | 400 | 23px | `#1e293b` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, `pre`, Copy button | 12px (`--border-radius`, forced over Bulma's `is-rounded`) |
| Carousel cards, More Works button and dropdown | 16px (`--border-radius-lg`) |
| Teaser thumbnail | 10px (inline) |
| Carousel images | 8px (inline; the stylesheet's 12px is overridden) |
| Section underline bar | 2px |

- **Shadows:** `--shadow-sm` `0 1px 2px 0 rgb(0 0 0 / 0.05)` (`pre`); `--shadow-md` `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)` (slate buttons, cards, More Works); `--shadow-lg` on hover; teaser `0 2px 10px rgba(0,0,0,0.1)`. Dataset and SlidesLive buttons have no shadow.
- **Borders:** 1px `#e2e8f0` on light bands (top and bottom), cards, `pre`, footer top; 2px `#e2e8f0` on More Works; 2px transparent on coloured buttons.
- **Motion:** `--transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`; buttons and cards lift 2–4px on hover and slate buttons turn `#2563eb`; author links grow a 2px gradient underline; every `.hero` and `.section` fades up 30px over 0.6s on load.

## Layout Metrics

- **Containers:** hero, teaser, abstract and BibTeX use `.container.is-max-desktop` (960px at ≥1024px); the abstract column is `is-four-fifths` (about 763px). Dataset, benchmark and results carousels use a plain `.container` (1344px at 1440px).
- **Hero:** `.hero-body` 64px 24px; teaser `.hero-body` 32px 24px 64px.
- **Bands:** `.section.hero.is-light` with Bulma `.section` padding 48px 24px; carousel sections `.hero.is-small` (24px vertical padding); `hr` separators inside the carousel section with 48px margins.
- **Carousel cards:** `.results-carousel .item` margin 16px, padding 24px, images at max-width 35% centred, caption below.
- **Poster:** `iframe` 100% wide, 550px tall inside a light band.

| Breakpoint | Container | Hero padding | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1408px | 960px / 1344px | 64px 24px | 16px | 48px | carousels full width |
| 1025–1407px | 960px / 1152px | 64px 24px | 16px | 48px | same |
| 769–1024px | fluid | 48px 32px | 16px | 48px | same |
| 481–768px | fluid | 32px 16px | 16px (abstract 16px) | 40px, line-height 1.2 | buttons 14px with 12px 16px padding; More Works moves to bottom-right; carousel cards 16px padding |
| ≤480px | fluid | 24px 12px | 16px | 32px | each button full width on its own line; More Works fixed at bottom |

## Components

- **Slate button.** `.external-link.button.is-normal.is-rounded.is-dark`: `#1e293b` fill, white 16px/600 label, Font Awesome or Academicons icon left, padding 7px 20px, 12px radius, no border, `--shadow-md`; hover fill `#2563eb`, lift 2px, `--shadow-lg`.
- **Colour button.** Same shape with Bulma `.is-info` (`#3298dc`, Dataset, database icon) or `.is-danger` (`#f14668`, SlidesLive, play icon), 2px transparent border, no shadow.
- **More Works dropdown.** Fixed top-right white button (2px `#e2e8f0`, 16px radius, padding 12px 20px, 14.4px/600) opening a 400px white panel (16px radius, xl shadow) of related works; chevron rotates 180° when open.
- **Teaser poster.** Thumbnail at 80% max width, 10px radius, `0 2px 10px rgba(0,0,0,0.1)`, centred 20px `#4a4a4a` caption 16px below.
- **Light band.** `section.hero.is-light`: `#f8fafc`, 1px `#e2e8f0` top and bottom borders.
- **Band heading.** `h2.title.is-3` 32px/700, 16px bottom padding, `::after` 60×3px bar `linear-gradient(135deg, #f093fb 0%, #f5576c 100%)`, 2px radius, centred.
- **Carousel card.** bulma-carousel `.item`: white, 1px `#e2e8f0`, 16px radius, 24px padding, md shadow, lifts 4px on hover; image at 35% width with 8px radius; 16px/500 `#64748b` caption; round white Bulma arrows on the edges; pagination dots `#2563eb`, active `#1d4ed8` scaled 1.2.
- **BibTeX block.** Header row with "BibTeX" title and a `#2563eb` Copy button (white 14.4px/600, padding 12px 16px, 12px radius; turns `#10b981` reading "Copied!"); `pre` `#f1f5f9`, 1px `#e2e8f0`, 12px radius, 24px padding, sm shadow.
- **Footer.** `#f8fafc`, 1px `#e2e8f0` top border, padding 48px 24px, `#64748b` text crediting the Academic Project Page Template, links `#2563eb`.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | White hero, 800-weight slate title, blue authors, correspondence e-mail |
| Venue badge | Absent from the hero (the `.publication-venue` chip is defined in CSS but not used); the venue appears only in the BibTeX | |
| Link buttons | Paper, Code, Dataset, arXiv, SlidesLive | Slate, info-blue and danger-pink 12px-radius buttons |
| Related works | Yes, non-standard | Fixed "More Works" dropdown |
| Teaser | Yes | Shadowed poster thumbnail with caption |
| Abstract | Yes | Light band, gradient underline heading, justified grey text |
| Dataset / benchmark / results | Yes | Three carousels of white figure cards separated by `hr` |
| Results table | Absent (results are carousel images) | |
| Poster | Yes | Embedded PDF `iframe` in a light band |
| BibTeX | Yes | Copy button and rounded `pre` |
| Footer | Yes | Light band with template credit |
| Video, sliders, 3D | Absent from the source | |

## Adapting to Other Content

- **More authors:** the authors block wraps in centred rows of 20px/600 `#2563eb`; keep affiliations as separate `span.author-block` lines below.
- **More buttons:** use slate `is-dark` for paper and code links and keep at most two Bulma colour buttons for special resources (data, talk), as here.
- **Venue:** use the stylesheet's own `.publication-venue` chip (`#f1f5f9` fill, `#64748b` 600 text, padding 8px 16px, 12px radius) under the authors; it is defined but unused.
- **A results table:** put it inside a white card (1px `#e2e8f0`, 16px radius, 24px padding, md shadow) in a plain section; header 600 `#1e293b` on `#f1f5f9`, rows with 1px `#e2e8f0` rules, best scores in `#2563eb` 600.
- **News:** a light `#f8fafc` band with a `title is-3` heading and a list of 16px items with dates in `#2563eb` 600.

## Do's and Don'ts

- Do keep the hero white and let the heavy slate title and the button row carry it.
- Do mark band headings with the 60×3px pink-coral gradient bar; it is the page's only gradient.
- Do wrap figures in white bordered cards with md shadows.
- Do keep body and abstract text in muted slate `#64748b`, titles in `#1e293b`.
- Don't mix more than two non-slate button colours.
- Don't leave Bulma's default title colours inside light bands if you want the slate palette to be consistent; here they render as `rgba(0,0,0,0.7)` and `#363636`.

## Surfaces

White page and hero; `#f8fafc` bands with hairline borders for Abstract, Poster and footer; white bordered cards in the carousels; a `#f1f5f9` code block. No dark surfaces apart from slate buttons.

## Imagery

A poster-style teaser combining a sunburst taxonomy of irregularity types (blue, yellow and red wedges) with small time-series panels; dataset taxonomy, benchmark-library diagrams and result charts in carousels; a full PDF poster embed.

## Layout

Centred 960px column for hero, abstract and BibTeX; carousels widen to the 1344px container. Sections stack as white blocks and light bands.

## Agent Prompt Guide

Quick colors: text `#1e293b`, muted `#64748b`, blue `#2563eb` (hover `#1d4ed8`), info `#3298dc`, danger `#f14668`, accent bar `#f093fb` → `#f5576c`, band `#f8fafc`, code `#f1f5f9`, hairline `#e2e8f0`.

1. "Create a white hero: centred Inter 48px/800 title in `#1e293b` with line-height 1.1, 20px/600 author links in `#2563eb` that grow a 2px `linear-gradient(135deg, #f093fb 0%, #f5576c 100%)` underline on hover, 16px affiliations, and a row of 40px-tall buttons with 12px radius."
2. "Make buttons: slate `#1e293b` fill, white 16px/600 label with left icon, padding 7px 20px, 12px radius, shadow `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)`, hover fill `#2563eb` and 2px lift; plus colour variants `#3298dc` and `#f14668` without shadow."
3. "Build a light band: `#f8fafc` with 1px `#e2e8f0` top and bottom borders, 48px 24px padding, a centred 32px/700 heading with a 60×3px `linear-gradient(135deg, #f093fb 0%, #f5576c 100%)` bar below, and justified 17.6px `#64748b` text at line-height 1.8."

## Similar Pages

Other pages on Eliahu Horwitz's Academic Project Page Template share the skeleton and the "More Works" dropdown; this one keeps the template's modern token layer intact. In this NeurIPS 2025 batch, Rectified Point Flow and EgoGazeVQA share the card-and-shadow idiom.

## Quick Start

```css
:root {
  --primary-color: #2563eb;
  --primary-hover: #1d4ed8;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --background-primary: #ffffff;
  --background-secondary: #f8fafc;
  --background-accent: #f1f5f9;
  --border-color: #e2e8f0;
  --info: #3298dc;
  --danger: #f14668;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --border-radius: 12px;
  --border-radius-lg: 16px;
  --font: 'Inter', 'Segoe UI', -apple-system, sans-serif;
}
.title.is-3::after { content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 60px; height: 3px; background: var(--gradient-accent); border-radius: 2px; }
```

## Provenance

- **URL:** https://blacksnail789521.github.io/time-imm-project-page/
- **Paper:** Time-IMM: A Dataset and Benchmark for Irregular Multimodal Multivariate Time Series (arXiv 2506.10412), Ching Chang, Jeehyun Hwang, Yidan Shi, Haixin Wang, Wen-Chih Peng, Tien-Fu Chen, Wei Wang (UCLA, National Yang Ming Chiao Tung University).
- **Venue:** NeurIPS 2025, Datasets and Benchmarks Track (not shown in the hero).
- **Selection reason:** the arXiv comment states acceptance at NeurIPS 2025 (Datasets and Benchmarks Track); the project page is linked in the abstract.
- **Template credit:** footer credits the Academic Project Page Template (Eliahu Horwitz), adopted from Nerfies.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, `static/css/index.css`, Bulma defaults and inline styles. Captured 2026-10-28.
