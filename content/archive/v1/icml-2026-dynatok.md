# DynaTok — Style Reference

> Google-blue lab memo on white, with a faint three-color dawn behind the title.

**Theme:** light

Measurements are normalized from the single inline `<style>` block (about 7.7 KB, no framework, no external CSS) and roles are interpreted from selectors and one rendered look. All values below come directly from the page's `:root` tokens and rules.

## Overview

DynaTok is a hand-written, framework-free page with a tight token set. The hero is centered with a soft background built from three radial gradients (Google blue `rgba(26,115,232,.06)`, coral `rgba(231,111,81,.05)`, teal `rgba(42,106,115,.05)`). A letter-spaced uppercase "ICML 2026" in `#1a73e8` sits under a Google Sans Display title. Buttons are white pills with hairline borders that turn blue on hover; a disabled "Code (soon)" pill and a coral "Page under construction" notice show work in progress. Content sections alternate white and `#f6f9fc`, headings carry a 3px blue left rule, and figures sit in white 18px-radius cards with 12px inner image radius.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg`, `--surface` | Page, cards, buttons |
| Ice Tint | `#f6f9fc` | `--bg-tint` | Alternate sections, disabled button, copy button |
| Hairline | `#e2e6eb` | `--hairline` | Card and button borders, footer rule |
| Graphite | `#1f2937` | `--text` | Title, body, author names |
| Slate Muted | `#5f6b7a` | `--text-muted` | Affiliations, TL;DR, captions |
| Slate Faint | `#8b95a2` | `--text-faint` | Footer, disabled text |
| Google Blue | `#1a73e8` | `--accent` | Venue, superscripts, hover, heading rule, abstract name |
| Blue Wash | `#e8f0fe` | `--accent-soft` | Copy-button hover |
| Deep Teal | `#2a6a73` | `--teal` | Hero glow (5% alpha) |
| Coral | `#e76f51` | `--coral` | Construction notice text; hero glow |

## Tokens — Typography

- **Family:** Google Sans Display, then Inter (both from Google Fonts), then system stack. Substitute: Inter.
- **Mono:** JetBrains Mono for BibTeX.
- **Weights:** 700 title and venue, 600 section heads and buttons, 500 authors.

| Level | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| Title (`h1`) | clamp(26px, 3.4vw, 38px) | 700 | 1.12 | letter-spacing −0.025em |
| Venue (`.venue`) | 25px (14px mobile) | 700 | — | uppercase, 0.08em tracking, blue |
| Section head (`h2`) | clamp(19px, 2vw, 23px) | 600 | 1.15 | −0.015em, 3px blue left border |
| Authors | 18px (16px mobile) | 500 | — | gap 6px 24px |
| Affiliations | 15px | 400 | — | muted |
| Body / abstract | 16px | 400 | 1.7 | justified, hyphens auto |
| Figure caption | 15px | 400 | 1.65 | left-aligned |
| Button | 14.5px | 600 | — | — |
| BibTeX | 13.5px | 400 | 1.75 | JetBrains Mono |
| Copy button | 11px | 600 | — | uppercase, 0.08em |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Cards (teaser, figures, BibTeX) | 18px (`--radius`) |
| Images inside cards | 12px (`--radius-sm`) |
| Buttons, construction notice | 999px |
| Copy button | 8px |

- **Shadows:** `--shadow-sm: 0 1px 2px rgba(20,30,50,.04), 0 1px 3px rgba(20,30,50,.06)`; `--shadow-md: 0 4px 16px rgba(20,30,50,.06), 0 2px 4px rgba(20,30,50,.04)`.
- **Layout width:** `--max-w: 900px`, container padding 0 28px (20px mobile); teaser figure max 600px; TL;DR 780px; abstract 760px.
- **Section padding:** 38px vertical (56px on mobile); hero 48px 0 32px.

## Components

- **Pill button** (`.btn`): white, 1px `#e2e6eb`, 999px, padding 12px 22px, 14.5px/600, `--shadow-sm`, 15px stroke SVG icon; hover border and text `#1a73e8`, lift 1px, `--shadow-md`. Disabled: `#8b95a2` on `#f6f9fc`, no shadow, "soon" note.
- **Construction notice:** inline pill, coral text on `rgba(231,111,81,.08)` with `rgba(231,111,81,.22)` border.
- **Section head:** 3px solid blue left border, 13px left padding.
- **Figure card** (`.exp-figure`): white, hairline border, 18px radius, 12px padding, `--shadow-sm`; caption 15px muted with bold lead.
- **BibTeX card:** white, hairline, 18px radius, padding 24px 28px; absolute copy button top-right (uppercase 11px, `#f6f9fc`, hover blue wash).
- **Footer:** centered 13.5px faint text, links with dotted underline.

## Page Modules

- **Title/author block:** six authors with blue superscripts (TU Munich, Google, Munich Center for Machine Learning).
- **Venue badge:** uppercase letter-spaced "ICML 2026" text in blue.
- **Link buttons:** Preprint, Code (disabled, "soon"), BibTeX (anchor).
- **Teaser:** method overview figure in a card, max 600px, followed by a centered TL;DR with blue bold emphasis.
- **Abstract:** justified, product name in bold blue.
- **Method, Results, Canonical Space Analysis:** figure cards with left-aligned captions on tinted sections.
- **BibTeX:** card with copy button.
- **Not present:** video, sliders, 3D viewer, HF demo, results tables, acknowledgements.

## Do's and Don'ts

- Do keep one accent (Google blue) and use coral only for status notices.
- Do put every figure in a white card with an inner image radius smaller than the card radius.
- Do alternate white and `#f6f9fc` sections instead of drawing dividers.
- Don't use heavy shadows; the two shadow tokens are nearly invisible.
- Don't center figure captions; they are left-aligned.
- Don't introduce a second display font.

## Surfaces

White page, `#f6f9fc` tinted sections, white hairline cards with very light shadows. The hero background is a barely visible three-color radial wash.

## Imagery

Clean diagram-style method figures (point-cloud sequence to tokens), qualitative 4D reconstructions, analysis plots.

## Layout

Single 900px column, centered hero and teaser, left-anchored section heads, stacked figure cards.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, tint `#f6f9fc`, hairline `#e2e6eb`, text `#1f2937`, muted `#5f6b7a`, faint `#8b95a2`, accent `#1a73e8`, accent-soft `#e8f0fe`, coral `#e76f51`.

1. "Build a centered hero with three faint radial gradients (blue, coral, teal at 5–6% alpha), a Google Sans Display title clamp(26px,3.4vw,38px)/700, and an uppercase letter-spaced 'ICML 2026' in `#1a73e8` at 25px."
2. "Make white pill buttons (1px `#e2e6eb`, 999px radius, 12px 22px padding, tiny shadow) that turn their border and text `#1a73e8` on hover, plus a disabled variant on `#f6f9fc`."
3. "Create a figure card: white, 1px `#e2e6eb`, 18px radius, 12px padding, image radius 12px, left-aligned 15px muted caption with a bold lead phrase."

## Similar Pages

Other hand-built single-file pages with Google Sans Display and a token block, e.g. IDLM in this batch (also custom, but serif-free and purple accent).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --bg-tint: #f6f9fc;
  --surface: #ffffff;
  --hairline: #e2e6eb;
  --text: #1f2937;
  --text-muted: #5f6b7a;
  --text-faint: #8b95a2;
  --accent: #1a73e8;
  --accent-soft: #e8f0fe;
  --teal: #2a6a73;
  --coral: #e76f51;
  --max-w: 900px;
  --radius: 18px;
  --radius-sm: 12px;
  --shadow-sm: 0 1px 2px rgba(20,30,50,.04), 0 1px 3px rgba(20,30,50,.06);
  --shadow-md: 0 4px 16px rgba(20,30,50,.06), 0 2px 4px rgba(20,30,50,.04);
  --font: 'Google Sans Display', 'Inter', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
}
```

## Provenance

- **URL:** https://wrchen530.github.io/dynatok/
- **Paper:** DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds (arXiv 2606.12189), Weirong Chen et al., TU Munich / Google / MCML.
- **Venue:** ICML 2026, stated on the page and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links the project page.
- **Template credit:** footer reads "Page template adapted for DynaTok · ICML 2026"; no upstream template named.
- **Measurement method:** `extract_style.py` counts plus full reading of the inline style block, one rendered screenshot. The page was marked "under construction" at capture time.
