# BadScientist Red-Flag Bulletin — Style Reference

> A conference bulletin board with two red notices pinned under the title: the award and the venue.

**Theme:** light

Measurements come from `static/css/index.css` (the Inter/slate revision of the Academic Project Page Template, near-stock), Bulma v0.9.1 and the HTML. Bulma's palette tops the extractor counts but only its danger red and neutrals are used here. Roles are interpreted.

## Overview

A near-default copy of the modern template: slate tokens, pink-to-coral section underlines, slate pill buttons that turn royal blue on hover, `#f8fafc` light bands. The page's own signal is two lines under the affiliations, both in Bulma `has-text-danger` semibold at `is-size-5`: "🏆 Agents4Science 2025 Best Paper Award" and "ACL 2026 Main Conference". The body is a sequence of white sections, each a 1.5rem title over a full-width PNG of a paper table or figure followed by explanatory prose, closing with an embedded PDF of the paper and BibTeX. One quirk: the stylesheet asks for Inter but the HTML links Google Sans / Noto Sans / Castoro instead, so text renders in the fallback `'Segoe UI'` / system sans unless Inter is installed locally.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Red Flag | `#f14668` (Bulma 0.9.1 `$danger`, inferred from version) | `.has-text-danger` | Award line and venue line |
| Slate Ink | `#1e293b` | `--text-primary` | Title, text, dark buttons |
| Slate Secondary | `#64748b` | `--text-secondary` | Abstract, captions |
| Slate Light | `#94a3b8` | `--text-light` | Equal-contribution note style |
| Bulma Grey | `#7a7a7a` (Bulma `$grey`, inferred) | `.has-text-grey` | "† Equal Contribution" line |
| Royal Blue | `#2563eb` | `--primary-color` | Author links, button hover, copy button |
| Royal Deep | `#1d4ed8` | `--primary-hover` | Hover |
| Paper | `#ffffff` | `--background-primary` | Page, most sections |
| Mist | `#f8fafc` | `--background-secondary` | Abstract band, footer |
| Frost | `#f1f5f9` | `--background-accent` | Code, venue chip token |
| Hairline | `#e2e8f0` | `--border-color` | Band borders, `pre` border |
| Underline Pink → Coral | `#f093fb` → `#f5576c` | `--gradient-accent` | 60×3px section-title underline, author hover bar |

## Tokens — Typography

- **Declared:** `'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif`.
- **Actually loaded:** Google Fonts `Google Sans|Noto Sans|Castoro`, none of which the stylesheet names, so the effective face is Segoe UI / system sans (inferred).
- **Mono:** `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace`.
- **Base:** body 16px, line-height 1.6; Bulma's own size scale is not overridden in this copy.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title (`title is-1`) | 3rem (Bulma) | 800 | 1.1 | |
| Section title (`title is-3`) | 1.5rem | 700 | inherit | gradient underline |
| Authors / award / venue (`is-size-5`) | 1.25rem | 500 / 600 | 1.5 | award and venue in red |
| Equal-contribution (`is-size-6`) | 1rem | 400 | | Bulma grey |
| Abstract | 1rem | 400 | 1.7 | justified, slate secondary |
| BibTeX | 0.9rem mono | 400 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, `pre` (`--border-radius`) | 12px |
| Video, banner (`--border-radius-lg`) | 16px |
| Section images (`.publication-body img`) | 12px (template rule, inferred to apply) |

- **Shadows:** template Tailwind scale (md on buttons, xl on banners).
- **Layout:** Bulma `container is-max-desktop` and `column is-four-fifths`; hero-body padding 4rem 1.5rem in this copy.

## Components

- **Title block.** Inter 800 title, six authors with † and suit-symbol superscripts (♠ ♢), one affiliation line.
- **Notice lines.** Two separate `div.is-size-5.has-text-weight-semibold.has-text-danger`, each with `margin-top: 0.5rem`; the award line carries a 🏆 emoji. No pill, no background.
- **Dark button.** `#1e293b`, white 600, 12px radius, md shadow, hover `#2563eb` with 2px lift. Buttons: arXiv, Paper (anchor to the embedded PDF), Code.
- **Figure-as-table section.** `title is-3` heading, full-width PNG of a paper table (Main Results, Concern–Acceptance Conflict, Mitigation), then justified prose with inline math-style subscripts.
- **Embedded paper.** `iframe` of the PDF, width 100%, height 550px.
- **BibTeX.** `#f1f5f9` `pre` with copy button.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered |
| Venue badge | Text line | Red "ACL 2026 Main Conference" |
| Award | Yes | Red "🏆 Agents4Science 2025 Best Paper Award" |
| Link buttons | arXiv, Paper, Code | Slate buttons |
| Teaser | No video; framework figure first after abstract | |
| Abstract | Yes | Mist band |
| Method figure | BadScientist Framework | Full-width PNG |
| Results | Tables and histograms as PNGs | White sections |
| Carousels / video | Template placeholders present only inside HTML comments | |
| PDF viewer | Yes | 550px iframe |
| BibTeX | Yes | |

## Do's and Don'ts

- Do put award and venue on separate lines in the same weight so neither outranks the other.
- Do load the font your stylesheet names; this page's Inter declaration is not backed by a font link.
- Do present results tables as tables (HTML) if you want them searchable; this page uses screenshots.
- Don't add a pill badge on top of the red lines; the plain coloured text is the style.
- Don't leave template placeholder carousels uncommented (this page correctly comments them out).

## Surfaces

White page with one `#f8fafc` abstract band and a mist footer. Flat sections, images carry the visual weight.

## Imagery

Framework diagram, table screenshots, score histograms, an embedded PDF. No video.

## Layout

Centered single column, four-fifths width for text and images.

## Agent Prompt Guide

**Quick colors:** text `#1e293b`, secondary `#64748b`, band `#f8fafc`, border `#e2e8f0`, primary `#2563eb`, notice red `#f14668`.

1. "Under the affiliations, add two centered 1.25rem semibold lines in `#f14668`, 0.5rem apart: '🏆 <Award name>' and '<Venue> Main Conference'."
2. "Make a results section: 1.5rem/700 heading with a 60×3px `linear-gradient(135deg, #f093fb, #f5576c)` underline, a full-width figure with 12px radius, then justified 1rem `#64748b` prose."
3. "Embed the paper PDF in a 100%-wide, 550px-tall iframe under a plain 'Paper' heading, followed by a `#f1f5f9` BibTeX block with a copy button."

## Similar Pages

VC-Inspector, GanitLLM and MMErroR in this batch share the template revision; Perturb-and-Revise is the other University of Washington page in the batch.

## Quick Start

```css
:root {
  --primary-color: #2563eb; --primary-hover: #1d4ed8;
  --text-primary: #1e293b; --text-secondary: #64748b; --text-light: #94a3b8;
  --background-primary: #ffffff; --background-secondary: #f8fafc;
  --background-accent: #f1f5f9; --border-color: #e2e8f0;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --notice-red: #f14668; --border-radius: 12px; --border-radius-lg: 16px;
}
body { font: 16px/1.6 'Inter', 'Segoe UI', sans-serif; color: var(--text-primary); }
.notice { color: var(--notice-red); font-weight: 600; font-size: 1.25rem; margin-top: .5rem; }
```

## Provenance

- **URL:** https://bad-scientist.github.io/
- **Paper:** BadScientist: Can a Research Agent Write Convincing but Unsound Papers that Fool LLM Reviewers? (arXiv 2510.18003), Fengqing Jiang, Yichen Feng, Yuetai Li, Luyao Niu, Basel Alomair, Radha Poovendran (University of Washington, KACST).
- **Venue / award:** ACL 2026 Main Conference; the page also states an Agents4Science 2025 Best Paper Award.
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 and links this page.
- **Template credit:** footer credits the Academic Project Page Template (eliahuhorwitz).
- **Measurement method:** `extract_style.py`, a diff of `index.css` against VC-Inspector's copy, and the HTML. The red and grey hex values are Bulma 0.9.1 defaults inferred from the version banner in `bulma.min.css`, not read from this page. The rendered page was not viewed, so the effective font is inferred from the missing Inter link.
