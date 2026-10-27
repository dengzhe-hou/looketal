# VC-Inspector Slate Console — Style Reference

> A product-analytics landing page wearing a lab coat: slate type, royal-blue hover, a gold "Accepted" ribbon, and terminal cards that grade captions.

**Theme:** light

Measurements come from `static/css/index.css` (the 2025 Inter/Tailwind-slate revision of the Academic Project Page Template, with tokens in `:root`), a page-level `<style>` block, and inline styles. Bulma 0.9 is still loaded underneath; its palette (`#00d1b2`, `#3273dc` …) tops the frequency counts but is overridden and does not appear. Roles are interpreted.

## Overview

The page uses the modern template's slate token set (`#1e293b` text, `#64748b` secondary, `#f8fafc` / `#f1f5f9` surfaces, `#e2e8f0` borders) with Inter 400–800 at a 15px base. The author added a sticky glass section nav (Abstract · Problem · Method · Results · Models · Examples · BibTeX), a fixed "More Works" dropdown top-right, a gold acceptance ribbon, a four-card Key Results strip in bright blue `#3b82f6`, and seven dark `#1e293b` "example" cards whose caption, score and explanation are coloured amber, mint and coral. Section titles keep the template's 60×3px underline in a pink-to-coral gradient, which is the only warm hue in the chrome. Buttons are slate pills that turn royal blue `#2563eb` and lift 2px on hover.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Slate Ink | `#1e293b` | `--text-primary` | Body text, title, dark buttons, example-card ground |
| Slate Secondary | `#64748b` | `--text-secondary` / `--secondary-color` | Justified abstract text, nav links, labels |
| Slate Light | `#94a3b8` | `--text-light` | Equal-contribution note, example sub-labels |
| Royal Blue | `#2563eb` | `--primary-color` | Author links, button hover, nav active, copy button, table links |
| Royal Deep | `#1d4ed8` | `--primary-hover` | Hover state; highlight-box gradient end |
| Signal Blue | `#3b82f6` | (page style) | Stat numbers, step circles, pipeline arrows, highlight-box start |
| Sky Accent | `#0ea5e9` | `--accent-color` | Declared accent |
| Paper | `#ffffff` | `--background-primary` | Page |
| Mist | `#f8fafc` | `--background-secondary` | `hero is-light` bands, stat cards, footer |
| Frost | `#f1f5f9` | `--background-accent` | Venue chip, nav hover, table header, code |
| Hairline | `#e2e8f0` | `--border-color` | Band borders, card borders, table rules |
| Ribbon Gold | `#ffe082` | (inline) | Acceptance ribbon fill |
| Ribbon Amber Edge | `#ffb300` | (inline) | Ribbon 2px border; glow `#ffd54f70` |
| Ember | `#b12a00` | (inline) | Ribbon text |
| Venue Blue | `#1565c0` | (inline) | "ACL 2026 (Main)" span inside the ribbon |
| Underline Pink → Coral | `#f093fb` → `#f5576c` | `--gradient-accent` | Section-title underline, author-link hover bar |
| Caption Amber | `#fbbf24` | (page style) | Caption line in example cards |
| Score Mint | `#34d399` | (page style) | Score in example cards |
| Error Coral | `#f87171` | (page style) | Explanation line in example cards |
| Badge Blue | `#dbeafe` / `#1e40af` | `.badge-blue` | Model-size badges |
| Badge Green | `#d1fae5` / `#065f46` | `.badge-green` | Badge variant |
| Badge Orange | `#ffedd5` / `#c2410c` | `.badge-orange` | Badge variant |
| Card Divider | `#475569` | (inline) | `hr` inside dark example cards |

## Tokens — Typography

- **All text:** `'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif`, Google Fonts weights 400–800. Substitute: system-ui.
- **Mono:** `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace`; example cards use generic `monospace`.
- **Base:** `body { font-size: 15px; line-height: 1.6 }` with Bulma sizes overridden.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title (`title is-1`) | 2.5rem | 800 | 1.1 | `#1e293b`, 2rem bottom margin |
| Section title (`title is-3`) | 1.5rem | 700 | inherit | 60×3px gradient underline |
| `is-size-5` / `title is-5` | 1.1rem | 600 (title) | | authors, sub-heads |
| `is-size-4` / `title is-4` | 1.25rem | | | |
| Subtitle | 1rem | 500 in carousels | | |
| Abstract (`has-text-justified`) | 1rem | 400 | 1.7 | `#64748b` |
| Stat number | 2.5rem (1.8rem mobile) | 800 | | `#3b82f6` |
| Stat label | 0.9rem | 400 | | `#64748b` |
| Nav link | 0.85rem (0.75rem mobile) | 600 | | |
| Badge | 0.8rem | 500 | | pill |
| BibTeX | 0.9rem mono | 400 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, venue chip, cards, code (`--border-radius`) | 12px |
| Banner, video, carousel items, More Works button (`--border-radius-lg`) | 16px |
| Ribbon | 10px |
| Nav link | 8px |
| Badges | 9999px |
| Step number | 50% |

- **Shadows:** `--shadow-sm 0 1px 2px 0 rgb(0 0 0/.05)`, `--shadow-md 0 4px 6px -1px rgb(0 0 0/.1), 0 2px 4px -2px rgb(0 0 0/.1)`, `--shadow-lg 0 10px 15px -3px …`, `--shadow-xl 0 20px 25px -5px …`.
- **Motion:** `--transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`; buttons and images lift 2px on hover.
- **Layout:** `container is-max-desktop` (960px); nav inner 960px; hero-body padding 2em.

## Components

- **Sticky section nav.** Fixed bar hidden at `top: -60px`, slides to 0 when scrolled; `rgba(255,255,255,0.95)` with 10px backdrop blur, 1px bottom border; centered 0.85rem/600 links that get a `#f1f5f9` chip and blue text on hover/active. Hidden under 768px.
- **More Works dropdown.** Fixed top-right white button, 2px `#e2e8f0` border, 16px radius, md shadow; lists the author's other pages with a venue tag each.
- **Acceptance ribbon.** Inline-block, `#ffe082` fill, `#b12a00` bold text, 2px `#ffb300` border, 10px radius, `0 0 6px 1px #ffd54f70` glow, 1px tracking, 🔥 emoji on both sides, venue span in `#1565c0`.
- **Dark button.** `button is-dark` becomes `#1e293b`, no border, white 600 text, 12px radius, md shadow; hover to `#2563eb`, lift 2px, lg shadow. Five buttons: Paper, Code, 🤗 Models, Dataset, arXiv.
- **Stat card.** `#f8fafc`, 1px `#e2e8f0`, 12px radius, 1.5rem padding, centered 2.5rem/800 blue number over a grey label; four in a `columns is-multiline` row.
- **Example card.** `#1e293b` ground, `#e2e8f0` monospace text, 12px radius, 1.5rem padding; caption line `#fbbf24`, 1.5rem bold score `#34d399`, explanation `#f87171`; `hr` in `#475569`.
- **Comparison table.** Full width, 0.75rem 1rem cells, `#e2e8f0` row rules, `#f1f5f9` header at 600, row hover `#f8fafc`, horizontal scroll wrapper.
- **BibTeX.** `#f1f5f9` `pre`, 1px border, 12px radius, 1.5rem padding, header row with a blue "Copy" button that turns green `#10b981` when copied.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Inter 800 title, blue author links with gradient hover bar |
| Venue badge | Yes | Gold "🔥 Accepted at ACL 2026 (Main) 🔥" ribbon |
| Link buttons | Paper, Code, Models (HF), Dataset (HF), arXiv | Slate pills, blue hover |
| Key results strip | Yes | Four stat cards (42.6 τ VATEX-Eval, 63.4 τ Flickr8K-Expert, 3B/7B, 0.30s) |
| Teaser figure | Two teaser PNGs with a centered caption | |
| Abstract | Yes | Mist band, justified slate-secondary text |
| Problem / method | Side-by-side failure examples, three numbered method steps, pipeline box | |
| Results tables | Five comparison tables | Slate table style |
| Model cards | Badges for 3B/7B models | Blue/green/orange pills |
| Examples | Seven dark example cards | |
| Video / sliders / 3D / HF Space | No | |
| BibTeX | Yes | With copy button |
| Footer | Template credit, CC BY-SA 4.0, statcounter | Mist band |

## Do's and Don'ts

- Do keep chrome in slate neutrals and let blue mark interaction only.
- Do use the dark example card for model outputs; colour-code caption, score and explanation consistently.
- Do keep the sticky nav to one row of section anchors.
- Don't mix the gold ribbon with other badges in the hero; it is the only warm block.
- Don't leave Bulma's own `is-primary` turquoise anywhere; everything is re-tokenized.

## Surfaces

White page, `#f8fafc` light bands bordered top and bottom by `#e2e8f0`, white cards with soft shadows, dark slate example cards, mist footer.

## Imagery

Two teaser PNGs, a method figure and result charts. No video.

## Layout

Centered 960px column. Stat cards and examples use Bulma columns (`is-6`, `is-6-mobile`). The nav and More Works button are fixed overlays.

## Agent Prompt Guide

**Quick colors:** text `#1e293b`, secondary `#64748b`, page `#ffffff`, band `#f8fafc`, chip `#f1f5f9`, border `#e2e8f0`, primary `#2563eb`, stat blue `#3b82f6`.

1. "Create a gold acceptance ribbon: inline-block, `#ffe082` fill, 2px `#ffb300` border, 10px radius, `0 0 6px 1px #ffd54f70` glow, bold `#b12a00` text with 1px tracking, the venue name in `#1565c0`, flanked by 🔥."
2. "Build a stat card row: four cards, `#f8fafc` fill, 1px `#e2e8f0` border, 12px radius, centered 2.5rem/800 `#3b82f6` number over a 0.9rem `#64748b` label."
3. "Make a dark evaluation card: `#1e293b`, 12px radius, 1.5rem padding, monospace `#e2e8f0` text, caption line in `#fbbf24`, a 1.5rem bold score in `#34d399`, and the explanation in `#f87171`."

## Similar Pages

GanitLLM (same author, emerald variant), MMErroR and BadScientist in this batch share the same Inter/slate template revision.

## Quick Start

```css
:root {
  --primary-color: #2563eb; --primary-hover: #1d4ed8; --accent-color: #0ea5e9;
  --text-primary: #1e293b; --text-secondary: #64748b; --text-light: #94a3b8;
  --background-primary: #ffffff; --background-secondary: #f8fafc;
  --background-accent: #f1f5f9; --border-color: #e2e8f0;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --border-radius: 12px; --border-radius-lg: 16px;
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
body { font: 15px/1.6 'Inter', 'Segoe UI', sans-serif; color: var(--text-primary); }
```

## Provenance

- **URL:** https://dipta007.github.io/VC-Inspector/
- **Paper:** VC-Inspector: Advancing Reference-free Evaluation of Video Captions with Factual Analysis (arXiv 2509.16538), Shubhashis Roy Dipta, Tz-Ying Wu, Subarna Tripathi (UMBC, Intel).
- **Venue:** ACL 2026 (Main), shown in the gold ribbon.
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 (Main); the project page is linked in the arXiv abstract.
- **Template credit:** footer credits the Academic Project Page Template (eliahuhorwitz); the Inter/slate token layer is that template's newer revision, with page-level additions by the author.
- **Measurement method:** `extract_style.py`, then manual reading of `index.css`, the page `<style>` block and inline styles. The rendered page was not viewed; the sticky-nav reveal is inferred from CSS (`top: -60px` → `.visible`), not observed.
