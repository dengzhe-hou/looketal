# UniversalRAG Cobalt Brief — Style Reference

> A well-designed GitHub README printed as a briefing: Source Sans, one cobalt accent, a pale-blue TL;DR band running edge to edge.

**Theme:** light

Measurements come from the page's inline `<style>` block (tokens in `:root`, including font and weight variables) and the Google Fonts link for Source Sans 3 (300/400/600/700). Font Awesome 7.0.0 and Academicons 1.9.4 are self-hosted. Roles are interpreted.

## Overview

A framework-free page whose content sections are rendered Markdown (`.markdown-body`), giving it a README rhythm. A centered title block in Source Sans 3 600 is followed by a muted "ACL 2026 Oral" line, muted authors whose affiliation superscripts are colour-coded per institution (KAIST in vermilion `#d1432f`, DeepAuto.ai in blue `#2563eb`), and three white buttons with brand-coloured icons (PDF red, arXiv red, GitHub black). The TL;DR concept figure sits in a full-bleed `#eef2fb` band drawn with a `::before` that extends to the viewport edges. The abstract is a rounded `#f9fafb` card. Results flow as Markdown with figures; a four-slide case-study carousel sits in a bordered card with frosted arrow controls and a dark counter pill. BibTeX is a dark `#0f172a` block.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Cobalt | `#1f6feb` | `--accent` | Primary button fill, brand dot, author hover |
| Cobalt Glow | `rgba(31,111,235,0.22)` | (literal) | Primary button shadow |
| Night Ink | `#101827` | `--text` | Body and heading text |
| Abstract Ink | `#111827` | (literal) | Abstract paragraphs; also `#111827` copy and to-top buttons |
| Pewter | `#4b5563` | `--muted` | Venue line, authors, affiliations, footer |
| Label Grey | `#6b7280` | (literal) | TL;DR label, eyebrow |
| Hairline | `#e5e7eb` | `--border` | Card, slider, button, band borders |
| Briefing Blue | `#eef2fb` | `--tldr-bg` | Full-bleed TL;DR band |
| Card Mist | `#f9fafb` | (literal) | Abstract card |
| Media Grey | `#f3f4f6` | (literal) | Figure and slide-media backgrounds |
| Inline Code | `#f0f2f8` | (literal) | Markdown inline code |
| Night Code | `#0f172a` | (literal) | BibTeX `pre` |
| Code Text | `#e2e8f0` | (literal) | BibTeX text |
| KAIST Vermilion | `#d1432f` | `.affil-1` | Affiliation 1 marker |
| Affil Blue | `#2563eb` | `.affil-2` | Affiliation 2 marker |
| Affil Amber / Green | `#f59e0b` / `#10b981` | `.affil-3` / `.affil-4` | Defined, unused (two affiliations) |
| PDF Red | `#c62828` | `.btn.pdf i` | PDF icon |
| arXiv Red | `#b31b1b` | `.btn.arxiv i` | arXiv icon |
| GitHub Black | `#24292e` | `.btn.code i` | Code icon |
| Demo Sky | `#0ea5e9` | `.btn.demo i` | Defined, unused |
| Counter Pill | `rgba(17,24,39,0.8)` / `#f9fafb` | (literal) | Slide indicator fill / text |
| Frosted Control | `rgba(255,255,255,0.92)` | (literal) | Slider arrow buttons |
| Paper | `#ffffff` | `--bg` / `--card` | Page, cards, buttons |

## Tokens — Typography

- **Body and headings:** `"Source Sans 3", system-ui, -apple-system, "Segoe UI", sans-serif` through `--font-body` / `--font-heading`, weights 400 body and 600 headings. Substitute: Source Sans Pro.
- **Mono:** `--mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace`.
- **Base:** 17px, line-height 1.6.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Page title | `clamp(1.95rem, 3vw, 2.5rem)` | 600 | 1.25 | |
| Section heading (`h1.section-heading`, Markdown h1) | `clamp(1.7rem, 2.4vw, 2.05rem)` | 600 | | |
| Venue line | 1.5rem | 600 | | muted |
| Authors | 1.3rem | 400 | | muted, comma via `::after` |
| Affiliations | 1.2rem | 400 | 1.4 | `·` separators |
| Affiliation marker | 0.7em | 700 | 1 | coloured superscript |
| Body | 17px | 400 | 1.6 | |
| TL;DR lead / body | 1.05em | 400 | | max 780 / 820px |
| TL;DR label, eyebrow | 12px | 800 / 700 | | uppercase, 0.08em |
| Markdown h2 / h3 / h4 | 1.25 / 1.08 / 0.95rem | 600 | | |
| Note, footer | 14px | 400 | | muted |
| Slide counter, copy button | 13px / 12px | | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Cards, slider, TL;DR figure (`--radius`) | 14px |
| Figures, slider controls, to-top button | 12px |
| Buttons, BibTeX `pre`, slide counter | 10px |
| Brand dot, copy button | 8px |
| Inline code | 6px |

- **Shadows:** `--shadow: 0 12px 30px rgba(15,24,46,0.08)` on cards, figures and slider; hero buttons `0 10px 24px rgba(15,24,46,0.08)`; primary `0 10px 24px rgba(31,111,235,0.22)`; abstract card `0 10px 24px rgba(15,24,46,0.04)`; slider-control hover `0 12px 28px rgba(15,24,46,0.16)`.
- **Layout:** `.container` 1100px with 20px padding; abstract card 900px; TL;DR text 780–820px; sections 32px apart; title block margin 48px 0 36px.

## Components

- **Title block.** Centered h1, muted 1.5rem venue line, wrapped author row with colour-coded superscripts, affiliation row with middots, small equal-contribution note.
- **Icon button (`.btn`).** Inline-flex, gap 8px, 10px 14px padding, 10px radius, 700 text, white fill, 1px `#e5e7eb` border, soft shadow, 1px lift on hover; icon tinted by brand (`.pdf`, `.arxiv`, `.code`). Buttons: Paper, arXiv, Code.
- **TL;DR band.** Section with a `::before` spanning `calc(-50vw + 50%)` on both sides, `#eef2fb` fill and hairline top/bottom borders; holds the concept figure (14px radius, hairline border, shadow) and a caption with an `(a) (b) (c)` counter list.
- **Abstract card.** `#f9fafb`, 1px hairline, 14px radius, 18px padding, max 900px.
- **Case-study slider.** Bordered 14px card with shadow; one active slide at a time on a `#f3f4f6` media area, white caption with slide title; frosted 12px-radius prev/next buttons at mid-height; dark counter pill "1 / 4".
- **BibTeX.** `#0f172a` `pre`, `#e2e8f0` text, 10px radius, dark `#111827` copy button.
- **Back-to-top.** Dark `#111827` 12px-radius button that appears on scroll and lifts 2px on hover.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Source Sans 600, colour-coded affiliations |
| Venue badge | Text | Muted 1.5rem "ACL 2026 Oral" |
| Link buttons | Paper, arXiv, Code | White icon buttons |
| Teaser | Concept figure in TL;DR band | Full-bleed blue band |
| Abstract | Yes | Mist card |
| Method | "Why UniversalRAG?" Markdown section with figures | |
| Results | Markdown text and figures | |
| Carousel | Four case-study slides | Bordered slider card |
| Video / tables / 3D / HF demo | No | |
| BibTeX | Yes | Dark code block |
| Footer | CC BY-SA 4.0 licence note | Muted 14px |

## Do's and Don'ts

- Do drive fonts and weights from `:root` variables so the heading face can be swapped in one place.
- Do colour affiliation markers instead of using symbols, and keep authors muted so the markers read.
- Do tint button icons with each service's brand colour while the button stays white.
- Don't use the cobalt for large fills; the TL;DR band is a pale tint, not the accent.
- Don't break the README rhythm with cards everywhere; only the abstract and slider are carded.

## Surfaces

White page, full-bleed `#eef2fb` TL;DR band, `#f9fafb` abstract card, white slider card, dark code block.

## Imagery

Concept figure (WebP) and result figures with `#f3f4f6` backgrounds; four case-study images in the slider. No video.

## Layout

Centered 1100px container; text blocks capped at 780–900px. Under the mobile breakpoint the nav wraps and authors stack.

## Agent Prompt Guide

**Quick colors:** text `#101827`, muted `#4b5563`, border `#e5e7eb`, accent `#1f6feb`, TL;DR band `#eef2fb`, card `#f9fafb`, code `#0f172a`.

1. "Make a full-bleed TL;DR band inside a 1100px container: `::before` from `calc(-50vw + 50%)` on both sides, `#eef2fb` fill, 1px `#e5e7eb` top and bottom borders, an uppercase 12px/800 `#6b7280` label, then a 14px-radius figure with a hairline border and `0 12px 30px rgba(15,24,46,0.08)` shadow."
2. "Build white icon buttons: 10px 14px padding, 10px radius, 1px `#e5e7eb` border, 700 Source Sans 3 text, icons tinted `#c62828` (PDF), `#b31b1b` (arXiv), `#24292e` (GitHub)."
3. "Render author superscripts as 0.7em/700 coloured markers, one colour per institution (`#d1432f`, `#2563eb`), with author names in `#4b5563`."

## Similar Pages

VLN-NF (ACL 2026) in this batch shares the framework-free, card-and-shadow approach with a single blue accent; LaMI is the other ACL 2026 Oral.

## Quick Start

```css
:root {
  --bg: #ffffff; --card: #ffffff; --text: #101827; --muted: #4b5563;
  --accent: #1f6feb; --border: #e5e7eb; --tldr-bg: #eef2fb;
  --radius: 14px; --shadow: 0 12px 30px rgba(15, 24, 46, 0.08);
  --mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  --font-body: "Source Sans 3", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-heading: var(--font-body); --font-body-weight: 400; --font-heading-weight: 600;
}
body { font: var(--font-body-weight) 17px/1.6 var(--font-body); color: var(--text); background: var(--bg); }
```

## Provenance

- **URL:** https://universalrag.github.io/
- **Paper:** UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities (arXiv 2504.20734), Woongyeong Yeo, Kangsan Kim, Soyeong Jeong, Jinheon Baek, Sung Ju Hwang (KAIST, DeepAuto.ai).
- **Venue:** ACL 2026; the page states "ACL 2026 Oral" (BibTeX: ACL 2026 Volume 1 Long Papers, pages 3843–3871).
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 and links this page.
- **Template credit:** none named; footer gives a CC BY-SA 4.0 licence. Custom build.
- **Measurement method:** `extract_style.py` plus a read of the inline stylesheet and HTML. A sticky header/nav style is defined in CSS but no `<header>` element appears in the markup. The rendered page was not viewed.
