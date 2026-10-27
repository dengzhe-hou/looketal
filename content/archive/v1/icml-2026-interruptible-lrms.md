# Are Large Reasoning Models Interruptible? — Style Reference

> A Bulma explainer with branded buttons and three color-coded failure modes.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.7.4 from cdnjs plus the page's `static/css/index.css` and `interactive_visualizer.css`, about 108 KB of own CSS) and roles are interpreted from selectors and one rendered look. Bulma's defaults (`#00d1b2`, `#3273dc`, `#209cee`) appear in frequency counts; only those visibly used are listed.

## Overview

The page starts from the Academic Project Page Template but grows into a long-form explainer. The hero places a round mascot logo (which tilts and scales on hover) beside the Google Sans title. Below it are authors, "Accepted at ICML 2026" in bold, and three brand-colored pill buttons (arXiv `#f14668`, Dataset `#ffce4b`, Code `#171515`). A bold lede and a three-column "failure modes" row (Reasoning Leakage, Panic, Self-doubt) lead into a chart selector with a dark active segment. A fixed floating table of contents sits at the left on wide screens. Each failure mode has an interactive trace visualizer with its own color family: violet for leakage, green for panic, and orange for the third. Slate `#0f172a` is the strong text color throughout.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | — | Page, cards |
| Bulma Smoke | `#f5f5f5` | — | Light bands, `pre` |
| Midnight Slate | `#0f172a` | — | Lede, card titles, strong text (23 uses) |
| Slate 800 | `#1e293b` | — | TOC title, active TOC link |
| Slate 500 | `#64748b` | — | TOC links, muted text |
| Gray 600 | `#4b5563` | — | Chart intro text |
| Gray 500 | `#6b7280` | — | Uppercase small labels |
| Ink 900 | `#111827` | — | Active chart-selector segment, failure items |
| arXiv Rose | `#f14668` | `.button--arxiv` | arXiv button |
| GitHub Black | `#171515` | `.button--github` | Code button |
| Dataset Gold | `#ffce4b` | `.button--dataset` | Dataset button (text `#1f2937`) |
| Action Blue | `#2563eb` | — | Example buttons, focus ring |
| Action Blue Hover | `#1d4ed8` | — | Hover; also `.hero-pill` text |
| Pill Wash | `#eff6ff` | — | `.hero-pill` background |
| TOC Blue | `#3b82f6` | — | TOC hover text and 10–15% alpha highlight |
| Leakage Violet | `#7c3aed` / `#faf5ff` | — | Leakage visualizer header, answer rule, wash |
| Panic Green | `#16a34a` / `#ecfdf5` | — | Panic visualizer header, wash |
| Ember Orange | `#ea580c` / `#fff7ed` | — | Third visualizer palette (inferred: Self-doubt) |
| Sky Answer | `#0284c7` / `#e0f2fe` | — | Final-answer callout rule and wash |
| Error Red | `#ff0000` | inline | Inline emphasis in text (3 uses) |

## Tokens — Typography

- **Title family:** Google Sans (`.publication-title`). Substitute: Inter.
- **Body family:** Noto Sans; Inter appears in visualizer UI (`'Inter', Arial, sans-serif`).
- **Mono:** JetBrains Mono / Fira Code for reasoning traces and inline code.
- **Weights:** 600 dominant (58 declarations), 700 for badges and titles.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Paper title (`.title.is-1`) | 3rem | 600 | Beside 180px logo |
| Section title (`.title.is-3`/`.is-4`) | 2rem / 1.5rem | 600 | Centered |
| TL;DR lede (`.tldr-lede`) | 1.13rem | 600 | line-height 1.45, `#0f172a` |
| Failure title | 1rem | 600 | `#0f172a` |
| Visualizer headings | 0.95–1.05rem | 600 | — |
| TOC title | 0.85rem | 700 | uppercase, 0.05em |
| Pills / small labels | 0.75–0.85rem | 600–700 | uppercase badges 0.08em |
| Inline code | 0.92em | 400 | mono |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| CTA buttons, pills, chart selector, badges | 999px |
| Hero TL;DR card, hero chart, read-more cards | 18px |
| Floating TOC, chart images, visualizer panels | 12px |
| TOC links, inline code | 6px |

- **Shadows:** CTA `0 6px 16px rgba(0,0,0,.08)` → hover `0 12px 20px rgba(0,0,0,.12)`; hero card `0 12px 28px rgba(17,24,39,.12)`; panels `0 18px 40px rgba(15,23,42,.12)`; badge `0 8px 18px rgba(17,24,39,.16)`.
- **Layout width:** Bulma `.container.is-max-desktop`; wider visualizer containers at 1280px and 1400px.

## Components

- **Brand CTA button** (`.cta-group .button`): inline-flex, gap .5rem, pill, 600; brand background per service; hover lift 2px.
- **Hero logo:** max-width 180px, hover `scale(1.1) rotate(5deg)` with tooltip.
- **Chart selector:** pill track `#f3f4f6`, padding .4rem; segments transparent, active `#111827` with white text.
- **Hero pill:** `#eff6ff` background, `#1d4ed8` text, 0.85rem/600.
- **TL;DR badge:** `#1f2937` pill, white uppercase 0.75rem, 0.08em tracking.
- **Floating TOC:** fixed left 2%, top 60%, white 98% with blur, 1px `rgba(0,0,0,.1)`, 12px radius; links `#64748b`, hover blue wash, active bold with 15% blue; hidden on narrow screens.
- **Trace visualizer:** gradient header (`#7c3aed → #5b21b6` or `#16a34a → #047857`), tinted question area, answer callouts with 4px left rules.
- **Read-more card:** 155° gradient from `rgba(241,245,249,.85)` to white, 18px radius, soft shadow.

## Page Modules

- **Title/author block:** logo + title, six authors (UC Berkeley), equal-contribution note, "Accepted at ICML 2026".
- **Venue badge:** bold text line, not a chip.
- **Link buttons:** arXiv, Dataset (Hugging Face), Code; plus "View full dataset on Hugging Face" further down.
- **Teaser:** lede, three failure-mode columns, then an interactive chart with a model selector.
- **Sections:** Problem Setup, #1 Hard Interrupt, #2 Speedup, #3 Info Update, Conclusion with takeaways.
- **Results:** interactive charts and trace visualizers instead of HTML tables; teaser video present.
- **Acknowledgment** section and **BibTeX**.
- **Not present:** 3D viewer, image-comparison slider, HF Space embed.

## Do's and Don'ts

- Do give each failure mode a stable color family and reuse it in every visualizer.
- Do use service brand colors for the three CTA buttons only.
- Do keep strong text in `#0f172a` and secondary text in slate grays.
- Don't use the brand rose or gold anywhere except their buttons.
- Don't show the floating TOC on mobile.
- Don't rely on pure `#ff0000` inline text for emphasis in new sections; it clashes with the slate palette.

## Surfaces

White page with `#f5f5f5` Bulma bands; elevated white cards with 12–18px radii; tinted visualizer panels (violet, green, orange washes); one dark segment for the active chart tab.

## Imagery

Mascot logo, line charts of accuracy versus interruption point, model reasoning traces rendered as text, simple icons.

## Layout

Centered column with a fixed left TOC on desktop; sections anchored by id; wide interactive blocks break out to 1280–1400px.

## Agent Prompt Guide

**Quick colors:** text `#0f172a`, muted `#64748b`, arXiv `#f14668`, code `#171515`, dataset `#ffce4b`, action `#2563eb`, leakage `#7c3aed`, panic `#16a34a`, third mode `#ea580c`.

1. "Build three pill CTA buttons with brand fills (arXiv `#f14668`, Dataset `#ffce4b` with dark text, Code `#171515`), 600 weight, shadow `0 6px 16px rgba(0,0,0,.08)`, lift 2px on hover."
2. "Create a fixed left floating TOC: white 98% with blur, 1px rgba(0,0,0,.1) border, 12px radius, uppercase 0.85rem title, `#64748b` links with blue-wash hover and bold active state."
3. "Make a reasoning-trace panel with a `linear-gradient(135deg,#7c3aed,#5b21b6)` header, `#faf5ff` body, and a final-answer block with a 4px `#7c3aed` left rule."

## Similar Pages

Academic Project Page Template derivatives that add custom interactive explainers; NoisyGRPO in this batch shares the template lineage but stays static.

## Quick Start

```css
:root {
  --text-strong: #0f172a;
  --text: #1e293b;
  --muted: #64748b;
  --btn-arxiv: #f14668;
  --btn-github: #171515;
  --btn-dataset: #ffce4b;
  --action: #2563eb;
  --action-hover: #1d4ed8;
  --leakage: #7c3aed;
  --leakage-wash: #faf5ff;
  --panic: #16a34a;
  --panic-wash: #ecfdf5;
  --ember: #ea580c;
  --ember-wash: #fff7ed;
  --radius-card: 18px;
  --radius-panel: 12px;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
}
```

## Provenance

- **URL:** https://dynamic-lm.github.io/
- **Paper:** Are Large Reasoning Models Interruptible? (arXiv 2510.11713), Tsung-Han Wu et al., UC Berkeley.
- **Venue:** ICML 2026, stated on the page ("Accepted at ICML 2026") and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links the project page.
- **Template credit:** footer says "built using the Academic Project Page Template which was adopted from the Nerfies project page".
- **Measurement method:** `extract_style.py` counts, manual reading of `index.css` and `interactive_visualizer.css` selectors, one rendered screenshot. The orange palette's assignment to the Self-doubt visualizer is inferred from color counts, not confirmed by interaction.
