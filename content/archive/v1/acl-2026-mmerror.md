# MMErroR Slate Exhibit — Style Reference

> A benchmark poster hung in a white gallery: logo-stamped title, a grey venue chip, and paper figures given room to breathe.

**Theme:** light

Measurements come from `static/css/index.css` (the Inter/slate revision of the Academic Project Page Template, extended with about 200 lines of page-specific rules), the HTML, and Bulma 0.9 underneath. Bulma's palette dominates the raw counts but is overridden. Roles are interpreted. One CSS rule hides most template sections, so the visible page is much shorter than the HTML.

## Overview

The page keeps the template's slate tokens and blue primary but strips the decoration: author links inherit text colour with the hover bar removed, the "More Works" dropdown is hidden, and a selector (`#main-content > section:not(:first-of-type):not(#Abstract):not(#overview):not(#statistics):not(#results):not(#BibTeX)`) hides the teaser video, the PDF-embed carousel, the task and taxonomy sections, the flow-figure iframe and the embedded arXiv PDF. What remains is a clean sequence: a title with a 48px logo and a fluid `clamp()` size, authors in fixed rows, a `#f1f5f9` "ACL 2026" chip, three slate buttons, then Abstract, Overview, Statistics and Experiment Results as "figure sections" with centered descriptions and figures capped at 70% width, ending in BibTeX.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Slate Ink | `#1e293b` | `--text-primary` | Title, body, dark buttons, figure-caption strong |
| Slate Secondary | `#64748b` | `--text-secondary` | Venue chip text, section descriptions, figure captions |
| Slate Light | `#94a3b8` | `--text-light` | Notes |
| Royal Blue | `#2563eb` | `--primary-color` | Button hover, copy button, footer links |
| Royal Deep | `#1d4ed8` | `--primary-hover` | Hover |
| Sky Accent | `#0ea5e9` | `--accent-color` | Declared accent |
| Gallery White | `#ffffff` | `--background-primary` | Page, `.figure-section` |
| Mist | `#f8fafc` | `--background-secondary` | `figure-section is-light` and `hero is-light` bands |
| Frost | `#f1f5f9` | `--background-accent` | Venue chip, code |
| Hairline | `#e2e8f0` | `--border-color` | Band borders, `pre` border |
| Underline Pink → Coral | `#f093fb` → `#f5576c` | `--gradient-accent` | 60×3px section-title underline |

## Tokens — Typography

- **Text:** `'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif` (Google Fonts 400–800). Substitute: system-ui.
- **Mono:** `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace`.
- **Base:** body 16px, line-height 1.6.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title | `clamp(2.4rem, 2.6vw + 1rem, 3.3rem)` | 800 | 1.1 | lines `nowrap`, logo line inline-flex, 0.35em gap |
| Section title (`title is-3`) | 1.5rem | 700 | inherit | gradient underline |
| Figure heading (`.paper-figure h3`) | 1.35rem (1.2rem mobile) | 700 | 1.3 | |
| Section description | 1.05rem | 400 | 1.7 | centered, max 780px, slate secondary |
| Figure description | 1rem | 400 | 1.7 | max 860px |
| Figure caption | 0.95rem | 400 | 1.65 | centered (left on mobile) |
| Venue chip | inherit | 600 | | slate secondary |
| BibTeX | 0.9rem mono | 400 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, venue chip, `pre` (`--border-radius`) | 12px |
| Video / banner (`--border-radius-lg`) | 16px |
| Paper figures | 0 (explicitly flat, no shadow) |

- **Shadows:** template Tailwind scale on buttons; figures have `box-shadow: none`.
- **Layout:** figure sections widen the container to 1180px; figures `max-width: 70%` with viewport-height caps (`min(53vh, 532px)`, flow figure `min(70%, 602px)`, wide figure `min(70%, 728px)`); `.figure-pair` is a 55fr/43fr grid at 70% width; `.paper-figure` 4rem bottom margin; body is a flex column with `#main-content { flex: 1 0 auto }` so the footer sits at the bottom.

## Components

- **Logo title.** 48px logo PNG with 12px left margin, inline with the first title line; each title line is a `nowrap` block so the break is fixed.
- **Author rows.** `.author-row` flex lines with 0.6rem gaps and `nowrap`; author links inherit colour, no underline animation.
- **Venue chip.** `.publication-venue`: `#f1f5f9`, `#64748b` 600 text, 0.5rem 1rem padding, 12px radius, inline-block, centered at `1rem auto 1.25rem`.
- **Dark button.** `#1e293b`, white 600, 12px radius, md shadow, hover `#2563eb` with 2px lift. Buttons: ArXiv, Dataset (HF), Code. A disabled variant (`aria-disabled="true"`) drops to 0.7 opacity.
- **Figure section.** Alternating white and `#f8fafc` (with `#e2e8f0` top/bottom borders), centered heading, a centered description paragraph, then flat figures and captions with bold lead-ins in ink.
- **BibTeX.** `#f1f5f9` `pre`, 1px border, 12px radius, copy button.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Logo plus fluid Inter 800 title, fixed author rows |
| Venue badge | Yes | Grey "ACL 2026" chip |
| Link buttons | ArXiv, Dataset (HF), Code | Slate buttons |
| Teaser video | In HTML but hidden by CSS | |
| Abstract | Yes | Mist band |
| Overview / statistics / results | Yes | Flat figure sections, 70% width |
| Carousel, PDF iframes, tasks, taxonomy, flow figure, embedded arXiv PDF | In HTML, hidden by CSS | |
| Tables / sliders / 3D / HF Space | No | |
| BibTeX | Yes | |
| Footer | Empty `footer` element | No template credit text |

## Do's and Don'ts

- Do give paper figures their own band with a one-paragraph description above them.
- Do cap figure height by viewport (`min(53vh, 532px)`) so tall figures fit a laptop screen.
- Do keep figures flat (no radius or shadow) when they are PDF-derived diagrams.
- Don't ship hidden sections you do not intend to show; here the teaser video and PDFs still download.
- Don't let author lines wrap unpredictably; the page fixes them in rows.

## Surfaces

White page and `#f8fafc` bands with hairline borders. No cards; figures sit directly on the band.

## Imagery

Static PNG figures in the visible sections; a poster-framed MP4 teaser, a `bulma-carousel`, and four PDF iframes exist but are hidden.

## Layout

Centered column, 1180px for figure sections, 70% figure width, two-figure grid for pairs that collapses to one column on mobile.

## Agent Prompt Guide

**Quick colors:** text `#1e293b`, secondary `#64748b`, band `#f8fafc`, chip `#f1f5f9`, border `#e2e8f0`, primary `#2563eb`.

1. "Make a grey venue chip: inline-block, `#f1f5f9` fill, `#64748b` 600 text, 0.5rem 1rem padding, 12px radius, centered under the authors."
2. "Build a figure section: alternating white / `#f8fafc` band with 1px `#e2e8f0` borders, 1180px container, centered 1.5rem/700 Inter heading, a 1.05rem slate-secondary description capped at 780px, then a flat figure at 70% width and max-height `min(53vh, 532px)` with a 0.95rem centered caption."
3. "Set a title with an inline 48px logo: title lines as `nowrap` blocks, font-size `clamp(2.4rem, 2.6vw + 1rem, 3.3rem)`, weight 800."

## Similar Pages

VC-Inspector, GanitLLM and BadScientist in this batch use the same Inter/slate template revision with more decoration.

## Quick Start

```css
:root {
  --primary-color: #2563eb; --primary-hover: #1d4ed8;
  --text-primary: #1e293b; --text-secondary: #64748b; --text-light: #94a3b8;
  --background-primary: #ffffff; --background-secondary: #f8fafc;
  --background-accent: #f1f5f9; --border-color: #e2e8f0;
  --border-radius: 12px; --border-radius-lg: 16px;
}
body { font: 16px/1.6 'Inter', 'Segoe UI', sans-serif; color: var(--text-primary); }
.figure-section .container { max-width: 1180px; }
.figure-media img { max-width: 70%; max-height: min(53vh, 532px); box-shadow: none; }
```

## Provenance

- **URL:** https://mmerror-benchmark.github.io/
- **Paper:** MMErroR: A Benchmark for Erroneous Reasoning in Vision-Language Models (arXiv 2601.03331), Yang Shi, Yifeng Xie et al. (Guangdong University of Technology, Hong Kong Baptist University, Sun Yat-sen University, Peking University).
- **Venue:** ACL 2026 (chip on the page).
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 Main; the project page is linked in the arXiv abstract.
- **Template credit:** not stated on the page (the footer is empty); the stylesheet is recognizably the Academic Project Page Template's Inter/slate revision.
- **Measurement method:** `extract_style.py`, a line diff of `index.css` against BadScientist's copy of the same template, and the HTML section order. Which sections are visible is deduced from the hiding selector, not observed; the rendered page was not viewed.
