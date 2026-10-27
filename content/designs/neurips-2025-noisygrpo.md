# NoisyGRPO — Style Reference

> Slate-and-Inter conference handout, polished with Tailwind-era shadows.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.9 base plus the page's `static/css/index.css`) and roles are interpreted from selectors and one rendered look. Bulma's unused palette (turquoise `#00d1b2`, yellow `#ffdd57`, info `#3298dc`) appears in frequency counts but not on the page and is excluded.

## Overview

NoisyGRPO uses the newer "modernized" Academic Project Page Template: the Nerfies/Bulma skeleton re-skinned with a slate design-token layer (`--text-primary: #1e293b`, `--primary-color: #2563eb`), Inter everywhere, 12px/16px radii and Tailwind-style layered shadows. The hero is white and centered; author names are blue links with a pink-to-red gradient underline on hover; link buttons are near-black slate pills that turn blue and lift 2px on hover. Section headings carry a 60px gradient bar centered beneath them. Content is mostly static figures (19 `img`, no inline video) arranged in Bulma carousels, plus a copy-to-clipboard BibTeX block.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Chalk White | `#ffffff` | `--background-primary` | Page background, hero |
| Slate Mist | `#f8fafc` | `--background-secondary` | `.hero.is-light` bands, footer |
| Slate Wash | `#f1f5f9` | `--background-accent` | Venue chip, `pre`/`code` background |
| Hairline Slate | `#e2e8f0` | `--border-color` | Band borders, `pre` border |
| Ink Slate | `#1e293b` | `--text-primary` | Titles, body, dark button fill |
| Pewter | `#64748b` | `--text-secondary` | Justified abstract text, footer icons |
| Fog | `#94a3b8` | `--text-light` | Light meta text |
| Signal Blue | `#2563eb` | `--primary-color` | Author links, button hover, copy button |
| Deep Signal | `#1d4ed8` | `--primary-hover` | Hover state of blue elements |
| Sky Accent | `#0ea5e9` | `--accent-color` | Declared accent (sparse use) |
| Award Red | `#ef4444` | — | `.publication-awards` text and left rule |
| Copied Green | `#10b981` | — | Copy-BibTeX "copied" state |
| Orchid→Coral | `#f093fb → #f5576c` | `--gradient-accent` | Heading underline bar, author hover underline |
| Indigo→Plum | `#667eea → #764ba2` | `--gradient-primary` | Declared, not visibly used |

## Tokens — Typography

- **Primary family:** Inter (Google Fonts), stack `'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif`. Substitute: system-ui.
- **Mono:** `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace` for BibTeX.
- **Weights:** 800 title, 700 section titles, 600 buttons and author links, 500 author block, 400 body.
- **Body:** 16px, line-height 1.6; abstract `.content.has-text-justified` 1.1rem / 1.8.

| Level | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| Paper title (`.title.is-1`) | 3rem (2rem under 480px) | 800 | 1.1 | `#1e293b`, margin-bottom 2rem |
| Section title (`.title.is-3`) | 2rem | 700 | 1.125 | Gradient bar 60×3px below |
| Authors (`.is-size-5`) | 1.25rem | 500/600 | 1.5 | Links blue |
| Body / abstract | 1.1rem | 400 | 1.8 | Pewter color |
| Code / BibTeX | 0.9rem | 400 | — | Mono stack |
| Buttons | 1rem (Bulma `is-normal`) | 600 | — | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, venue chip, `pre`, copy button | 12px (`--border-radius`) |
| Banner image/video, carousel cards | 16px (`--border-radius-lg`) |
| Gradient underline bar | 2px |
| Scroll-to-top | 50% |

- **Shadows:** `--shadow-sm 0 1px 2px 0 rgb(0 0 0/.05)`; `--shadow-md 0 4px 6px -1px rgb(0 0 0/.1), 0 2px 4px -2px rgb(0 0 0/.1)`; `--shadow-lg 0 10px 15px -3px …`; `--shadow-xl 0 20px 25px -5px …`.
- **Hero padding:** `.hero-body` 4rem 1.5rem; publication header 6rem 1.5rem 4rem.
- **Layout width:** Bulma `.container.is-max-desktop` (960px, inferred from Bulma default); figures constrained inline to `max-width: 50%`–`60%`.
- **Motion:** `all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`; hover lifts of −2px/−3px.

## Components

- **Link button** (`.button.is-dark.is-rounded`): fill `#1e293b`, white text, 600 weight, radius 12px (overrides Bulma pill), `--shadow-md`; hover fill `#2563eb`, translateY(−2px), `--shadow-lg`. Labels: Paper, Code, arXiv, 🤗 Model.
- **Author link:** `#2563eb`, 600, no underline; hover `#1d4ed8` with a 2px gradient underline growing from 0 to 100% width.
- **Venue chip** (`.publication-venue`): `#64748b` on `#f1f5f9`, 600, padding 0.5rem 1rem, radius 12px. On this page the venue sits as plain text "NeurIPS 2025" under the affiliations.
- **Section heading:** centered `.title.is-3` with `::after` bar 60×3px, `--gradient-accent`.
- **Light band:** `.hero.is-light` `#f8fafc` with 1px `#e2e8f0` top and bottom borders, used for the abstract.
- **BibTeX block:** `pre` on `#f1f5f9`, 1px `#e2e8f0`, radius 12px, padding 1.5rem, `--shadow-sm`; header row with blue `.copy-bibtex-btn` (padding 0.75rem 1rem, 0.9rem) that turns `#10b981` when copied.
- **Scroll-to-top:** fixed 50px blue circle, bottom/right 2rem, `--shadow-lg`.

## Page Modules

- **Title/author block:** centered Inter 800 title, blue author links with superscript affiliations, three-line affiliation block, venue line "NeurIPS 2025".
- **Venue badge:** plain text line (the template's chip style exists but is not used as a badge here).
- **Link buttons:** Paper (PDF icon), Code (GitHub), arXiv (academicons), 🤗 Model.
- **Teaser:** template teaser section is commented out; page goes straight to the abstract band.
- **Abstract:** light band, justified, Pewter text.
- **Motivation / method figures:** static images at 50–60% width, with `h2.subtitle` captions above.
- **Results:** result tables are embedded as images inside `.results-carousel` (no HTML `<table>`).
- **Video Presentation** heading present; no `<video>` or iframe found in static HTML.
- **BibTeX:** copy-button header, mono block.
- **Not present:** comparison slider, 3D viewer, HF Space demo, acknowledgements section. "More works" dropdown is commented out.

## Do's and Don'ts

- Do keep everything in Inter; let weight (800/700/600) carry hierarchy.
- Do use slate neutrals (`#1e293b`, `#64748b`) rather than Bulma's `#363636`/`#4a4a4a`.
- Do keep buttons dark slate at rest and blue only on hover.
- Don't reintroduce Bulma's full pill radius; this skin uses 12px.
- Don't use the purple `--gradient-primary` for chrome; only the orchid-coral accent gradient is visible.
- Don't add colored section backgrounds beyond `#f8fafc`.

## Surfaces

Two levels: white page and `#f8fafc` bands with hairline borders. Elevation comes from Tailwind-style shadows on buttons, banner media and the BibTeX block, never from color fills.

## Imagery

Wide paper figures (pipeline diagram, benchmark plots, qualitative visualizations) on white, rendered at 50–60% column width. No video loops; no decorative imagery.

## Layout

Single centered column inside `.container.is-max-desktop`; sections separated by `.hero.is-small` blocks. Carousels hold multiple result images per section.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f8fafc`, wash `#f1f5f9`, border `#e2e8f0`, text `#1e293b`, muted `#64748b`, primary `#2563eb`, hover `#1d4ed8`, accent gradient `#f093fb → #f5576c`.

1. "Build a centered paper hero in Inter: 3rem/800 title in `#1e293b`, blue `#2563eb` author links with superscripts, venue line, and four dark-slate link buttons (radius 12px, `0 4px 6px -1px rgb(0 0 0/.1)` shadow) that turn `#2563eb` and lift 2px on hover."
2. "Create a section heading: centered 2rem/700 Inter text with a 60×3px gradient bar (`#f093fb → #f5576c`) beneath it, radius 2px."
3. "Make a BibTeX card: `#f1f5f9` background, 1px `#e2e8f0` border, 12px radius, 1.5rem padding, mono 0.9rem text, and a blue copy button that turns `#10b981` after copying."

## Similar Pages

Other pages built on the 2025 modernized Academic Project Page Template (Inter + slate tokens); classic Nerfies pages share the skeleton but not the skin.

## Quick Start

```css
:root {
  --primary-color: #2563eb;
  --primary-hover: #1d4ed8;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --text-light: #94a3b8;
  --background-primary: #ffffff;
  --background-secondary: #f8fafc;
  --background-accent: #f1f5f9;
  --border-color: #e2e8f0;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --border-radius: 12px;
  --border-radius-lg: 16px;
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --font-sans: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

## Provenance

- **URL:** https://artanic30.github.io/project_pages/NoisyGRPO/
- **Paper:** NoisyGRPO: Incentivizing Multimodal CoT Reasoning via Noise Injection and Bayesian Estimation (arXiv 2510.21122), Longtian Qiu et al., ShanghaiTech University.
- **Venue:** NeurIPS 2025 (stated on the page and in the arXiv comment).
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer says "built using the Academic Project Page Template which was adopted from the Nerfies project page".
- **Measurement method:** `extract_style.py` frequency counts plus manual reading of `static/css/index.css` and the HTML; one rendered screenshot of the hero at desktop width. Hover states and the 480px breakpoint come from CSS, not from interaction.
