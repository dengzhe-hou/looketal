# LaMI Inkwell Ledger — Style Reference

> A well-kept lab ledger: serif headings, one bottle of deep-sea blue ink, and results ruled into neat tables.

**Theme:** light

Measurements come from `static/style.css` (a hand-written stylesheet whose header calls it "Clean Academic Style") and the Google Fonts link (Noto Sans 300–700 with italic, Noto Serif 400/600 with italic). All values are literals; roles are interpreted.

## Overview

A framework-free page with a classic paper-page structure: centered hero (serif title, bold "ACL 2026 Oral" line, authors in blue, outline buttons), then sections alternating white and `#f8f9fa`: TL;DR, Abstract, Method, Results, Qualitative Analysis, BibTeX. Headings are Noto Serif, body Noto Sans at 16px with a generous 1.7 line height. A single ink colour, `#1a5276`, carries links, authors, buttons and the highlighted table row tint family. Results are three real HTML tables with a `#f0f2f4` header, uppercase group-header rows and a pale-blue "ours" row. Qualitative examples are left-ruled callouts coded green (success), blue (robustness) and red (failure). The method text colour-codes frozen (`#2e86c1`) and trainable (`#d68910`) modules to match the figure.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Deep-Sea Ink | `#1a5276` | (literal) | Links, author names, button text/border, button hover fill, copy-button hover |
| Frozen Blue | `#2e86c1` | `.color-frozen` | Frozen-module text; robustness callout rule |
| Trainable Amber | `#d68910` | `.color-trainable` | Trainable-module text |
| Success Green | `#27ae60` / `#f6fdf8` | `.example.success` | Success callout rule / fill |
| Robustness Wash | `#f5fafd` | `.example.robustness` | Robustness callout fill |
| Failure Red | `#c0392b` / `#fdf6f5` | `.example.failure` | Failure callout rule / fill |
| Highlight Row | `#eef5fb` / `#d4e4ef` | `tr.highlight` | "Ours" row fill / row rule |
| Heading Black | `#1a1a1a` | (literal) | h1–h4 |
| Body Ink | `#2c2c2c` | (literal) | Body text |
| Prose Grey | `#333333` | (literal) | TL;DR, abstract, venue line, BibTeX code |
| Method Grey | `#444444` | (literal) | Section descriptions, method text |
| Caption Grey | `#555555` | (literal) | Affiliations, captions, example question |
| Group Grey | `#666666` | (literal) | Table group headers, copy button |
| Note Grey | `#777777` / `#888888` | (literal) | Table notes / equal contribution, footer |
| Credit Grey | `#aaaaaa` | `.template-credit` | Template credit line |
| Table Head | `#f0f2f4` | (literal) | `thead th` fill |
| Band Grey | `#f8f9fa` | `.section-gray` | Alternating section fill |
| Code Ground | `#f5f6f8` | `.bibtex-container` | BibTeX fill |
| Rules | `#cccccc` / `#dddddd` / `#e8e8e8` / `#eaeaea` | (literal) | Table header rule, BibTeX border, method-point border, row rules and footer rule |
| Paper | `#ffffff` | (literal) | Page, hero, buttons, method cards |

## Tokens — Typography

- **Headings:** `'Noto Serif', 'Georgia', serif`, 600 (title 700). Substitute: Source Serif 4.
- **Body / UI:** `'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`. Method-point and example h3/h4 switch back to Noto Sans.
- **Mono:** `'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', monospace`.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title | 2.25rem (1.55rem ≤768px, 1.3rem ≤480px) | 700 | 1.3 | serif |
| Venue line | 1.05rem | strong | 1.7 | `#333` |
| h2 | 1.65rem | 600 | 1.7 | serif, centered |
| h3 / table title | 1.15 / 1.12rem | 600 | | |
| Authors | 1.1rem | 500 links | 1.8 | comma via `::after` |
| Body | 16px | 400 | 1.7 | |
| Abstract | 1rem | 400 | 1.8 | left |
| TL;DR | 1.02rem | 400 | 1.75 | |
| Section description / method | 0.97rem | 400 | 1.7 | max 760px |
| Affiliations | 0.92rem | 400 | | |
| Button | 0.9rem | 500 | | |
| Table body / header | 0.9 / 0.88rem | 400 / 600 | | `nowrap` |
| Group header row | 0.84rem | 600 | | uppercase, 0.03em |
| BibTeX | 0.84rem mono | 400 | 1.6 | |
| Equal contribution / table note | 0.82rem | 400 italic / 400 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, teaser and method images, copy button | 4px |
| Method points, example callouts, BibTeX container | 6px |

- **Shadows:** none anywhere.
- **Layout:** `.container` 980px with 24px padding; `.container-narrow` 780px; teaser image max 620px; captions max 700px; sections 56px vertical (40px mobile); hero 72px 24px 40px.

## Components

- **Hero.** Serif title, bold venue line, authors with comma separators drawn by `::after`, affiliations, italic equal-contribution note, then buttons.
- **Outline button (`.btn`).** Inline-flex, gap 7px, 9px 20px padding, 0.9rem/500 `#1a5276` text, white fill, 1.5px `#1a5276` border, 4px radius; hover inverts to ink fill with white text. Four buttons: Paper (PDF), ArXiv, Code, BibTeX (anchor). Under 480px they stack, max 220px wide.
- **Method points.** Two-column grid (32px gap) of white cards with a 1px `#e8e8e8` border, 6px radius, 24px padding.
- **Results table.** Full width, collapse, `#f0f2f4` header with a 2px `#ccc` bottom rule, `#eaeaea` row rules, uppercase grey group-header rows, a 1.5px backbone separator, and a `#eef5fb` highlighted row; table note in 0.82rem `#777`.
- **Example callout.** 22px 26px padding, 6px radius, 4px left border: green on `#f6fdf8`, blue on `#f5fafd`, red on `#fdf6f5`; italic question line.
- **BibTeX.** `#f5f6f8` container, 1px `#ddd`, 6px radius, absolute copy button top-right (1px `#ccc`, hover to ink).

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Serif, centered |
| Venue badge | Text | Bold "ACL 2026 Oral" |
| Link buttons | Paper, ArXiv, Code, BibTeX | Outline ink buttons |
| TL;DR | Yes | White section |
| Abstract | Yes | Grey band |
| Method figure | Yes | Full-width image plus two method-point cards |
| Results tables | Three HTML tables | Ruled, highlighted row |
| Qualitative examples | Success / robustness / failure | Left-ruled callouts |
| Video / sliders / 3D / HF demo | No | |
| BibTeX | Yes | Light code block with copy |
| Footer | Maintainer contact line | Muted, ink link |

## Do's and Don'ts

- Do keep a single ink colour for every interactive element.
- Do colour-code module types in prose to match the method figure.
- Do write results as HTML tables with a highlighted row instead of screenshots.
- Don't add shadows; separation comes from rules and grey bands.
- Don't mix more than three callout colours; each maps to one example type.

## Surfaces

White and `#f8f9fa` bands, white bordered cards for method points, tinted callouts, a light grey code block.

## Imagery

One teaser image (max 620px) and one method figure. No video.

## Layout

Centered 980px column with a 780px narrow variant for text. Two-column method grid collapses under 768px.

## Agent Prompt Guide

**Quick colors:** ink `#1a5276`, heading `#1a1a1a`, body `#2c2c2c`, band `#f8f9fa`, table head `#f0f2f4`, highlight `#eef5fb`, rule `#eaeaea`.

1. "Make outline buttons: 9px 20px padding, 0.9rem/500 `#1a5276` text, white fill, 1.5px `#1a5276` border, 4px radius, icon gap 7px; on hover fill `#1a5276` and turn the text white."
2. "Build a results table: `#f0f2f4` header with 600 0.88rem labels and a 2px `#ccc` bottom rule, 1px `#eaeaea` row rules, uppercase 0.84rem `#666` group-header rows, and the proposed method's row filled `#eef5fb`."
3. "Create three qualitative callouts with 4px left borders and 6px radius: success `#27ae60` on `#f6fdf8`, robustness `#2e86c1` on `#f5fafd`, failure `#c0392b` on `#fdf6f5`."

## Similar Pages

GuideDog (ACL 2026) in this batch is the other serif-led, framework-free page; UniversalRAG and LaMI are both ACL 2026 Oral papers.

## Quick Start

```css
:root {
  --ink: #1a5276; --heading: #1a1a1a; --text: #2c2c2c; --muted: #555555;
  --band: #f8f9fa; --table-head: #f0f2f4; --row-hl: #eef5fb; --rule: #eaeaea;
  --code-bg: #f5f6f8; --frozen: #2e86c1; --trainable: #d68910;
  --font-head: 'Noto Serif', Georgia, serif;
  --font-body: 'Noto Sans', -apple-system, 'Segoe UI', sans-serif;
  --container: 980px; --radius: 4px; --radius-card: 6px;
}
body { font: 16px/1.7 var(--font-body); color: var(--text); }
h1, h2, h3, h4 { font-family: var(--font-head); color: var(--heading); }
```

## Provenance

- **URL:** https://guyyariv.github.io/LaMI/
- **Paper:** LaMI: Augmenting Large Language Models via Late Multi-Image Fusion (arXiv 2406.13621), Guy Yariv, Idan Schwartz, Yossi Adi, Sagie Benaim (The Hebrew University of Jerusalem, Bar-Ilan University).
- **Venue:** ACL 2026; the page states "ACL 2026 Oral".
- **Selection reason:** the arXiv comment states acceptance at ACL 2026; the project page is linked in the arXiv abstract.
- **Template credit:** none visible; the stylesheet defines a `.template-credit` class but the footer only has a maintainer line. Custom build.
- **Measurement method:** `extract_style.py` plus a full read of `static/style.css`. The rendered page was not viewed. The footer's contact link points to `#`.
