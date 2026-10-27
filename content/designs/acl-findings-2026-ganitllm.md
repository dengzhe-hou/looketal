# GanitLLM Emerald Ledger — Style Reference

> The slate project-page template re-inked in emerald, like a mathematics workbook with green answer keys.

**Theme:** light

Measurements come from `static/css/index.css` (the Inter/slate revision of the Academic Project Page Template, here with a recoloured `:root`), the page `<style>` block and inline styles. Bulma 0.9 sits underneath; its defaults dominate the extractor counts but are overridden. Roles are interpreted.

## Overview

Same author and same build as VC-Inspector, with the accent family swapped from blue to emerald: `--primary-color #10b981`, `--primary-hover #059669`, `--accent-color #34d399`, and all three template gradients rewritten in greens. Buttons, the copy-BibTeX button, nav active states and section-title underlines turn green, while author links were pinned back to royal blue `#2563eb` with a blue hover bar. The hero carries a gold "🔥 Accepted at ACL 2026 (Findings) 🔥" ribbon and the Bengali wordmark "গণিতLLM" above the title, set with Noto Sans Bengali. A narrow TL;DR band (`#475569` text, 800px max) introduces the four-card Key Results strip with emerald numbers. A single emerald gradient "highlight box" advertises the GANIT dataset with white link tiles.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Emerald | `#10b981` | `--primary-color` | Button hover, nav active, copy button, stat numbers, step circles, dataset link text |
| Deep Emerald | `#059669` | `--primary-hover` | Hover; gradient end |
| Mint | `#34d399` | `--accent-color` | Section-title underline start; scores in example cards |
| Green Wash | `#d1fae5` → `#a7f3d0` | `--gradient-subtle` | Subtle gradient; `#d1fae5` also used inline as row tint |
| Pale Mint | `#ecfdf5` | (inline) | Highlighted table rows |
| Forest Badge | `#065f46` | (page style) | Dark badge fill / green badge text |
| Royal Blue | `#2563eb` | (index.css literal) | Author links and their hover bar |
| Royal Deep | `#1d4ed8` | (index.css literal) | Author link hover |
| Slate Ink | `#1e293b` | `--text-primary` | Text, dark buttons, example-card ground |
| Slate Secondary | `#64748b` | `--text-secondary` | Abstract text, labels |
| TL;DR Slate | `#475569` | (inline) | TL;DR paragraph |
| Slate Light | `#94a3b8` | `--text-light` | Notes |
| Paper | `#ffffff` | `--background-primary` | Page |
| Mist | `#f8fafc` | `--background-secondary` | Light bands, stat cards |
| Frost | `#f1f5f9` | `--background-accent` | Venue chip, table header, code |
| Hairline | `#e2e8f0` | `--border-color` | Borders, table rules |
| Ribbon Gold | `#ffe082` / edge `#ffb300` / text `#b12a00` | (inline) | Acceptance ribbon |
| Venue Blue | `#1565c0` | (inline) | "ACL 2026 (Findings)" inside the ribbon |
| Loss Red | `#ef4444` | (inline) | Negative delta text |
| Caption Amber | `#fbbf24` | (page style) | Caption line in example cards |

## Tokens — Typography

- **Text:** `'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif` (Google Fonts 400–800). Substitute: system-ui.
- **Bengali:** `Noto Sans Bengali` for the wordmark and Bengali examples (inferred source: system or Google Fonts; no explicit link found in the stylesheet list).
- **Mono:** `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace`.
- **Base:** body 15px, line-height 1.6, with the same Bulma size overrides as VC-Inspector (`title is-1` 2.5rem, `is-size-5` 1.1rem, subtitle 1rem).

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title (`title is-1`) | 2.5rem | 800 | 1.1 | |
| Section title (`title is-3`) | 1.5rem | 700 | inherit | 60×3px mint→emerald underline |
| Authors (`is-size-5`) | 1.1rem (0.9rem mobile) | 500 | 1.5 | links 600 blue |
| TL;DR | 1.05rem | 400 | 1.6 | `#475569`, 800px |
| Abstract | 1rem | 400 | 1.7 | justified, slate secondary |
| Stat number / label | 2.5rem / 0.9rem | 800 / 400 | | emerald / grey |
| Highlight-box figures | 1.5rem / 0.8rem | 700 / 400 | | white on emerald, 0.9 opacity labels |
| Nav link | 0.85rem | 600 | | |
| BibTeX | 0.9rem mono | 400 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, cards, code, highlight box (`--border-radius`) | 12px |
| Banner, video, More Works button (`--border-radius-lg`) | 16px |
| Ribbon | 10px |
| Link tiles inside highlight box, nav links | 8px |
| Badges | 9999px |

- **Shadows:** template `--shadow-sm` to `--shadow-xl` (Tailwind values, e.g. md `0 4px 6px -1px rgb(0 0 0/.1), 0 2px 4px -2px rgb(0 0 0/.1)`).
- **Layout:** `container is-max-desktop` (960px); `section[id] { scroll-margin-top: 60px }` so anchors clear the sticky nav; hero-body padding 1em.

## Components

- **Wordmark title.** Bengali "গণিতLLM" set above "GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO" in Inter 800.
- **Acceptance ribbon.** `#ffe082` fill, 2px `#ffb300` border, 10px radius, `0 0 6px 1px #ffd54f70` glow, bold `#b12a00` text, 🔥 on both sides.
- **Dark button.** `#1e293b`, white 600 text, 12px radius, md shadow; hover to `#10b981` and lift 2px. Five buttons: Paper, Code, 🤗 Models, Dataset, arXiv.
- **Sticky nav and More Works.** Same glass bar and fixed dropdown as the template revision; active link in emerald on `#f1f5f9`.
- **Stat card.** `#f8fafc`, 1px `#e2e8f0`, 12px radius, emerald 2.5rem/800 numbers (+8 Bn-MGSM, 88% Bengali tokens, 79% fewer words, 3.8x faster convergence).
- **Highlight box.** `linear-gradient(135deg, #10b981 0%, #059669 100%)`, white text, 12px radius, 1.5rem padding; small stat pairs and a white block link (8px radius, emerald 600 text, 0.75rem padding) to the HF dataset.
- **Comparison table.** Slate rules, `#f1f5f9` header, highlighted rows in `#ecfdf5` / `#d1fae5`, green badges.
- **Example card.** `#1e293b` monospace card with amber caption and mint score lines.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Bengali wordmark plus Inter 800 title |
| Venue badge | Yes | Gold ribbon "ACL 2026 (Findings)" |
| Link buttons | Paper, Code, Models (HF), Dataset (HF), arXiv | Slate pills, emerald hover |
| TL;DR | Yes | Narrow slate band |
| Key results | Four stat cards | |
| Teaser figure | One teaser PNG with centered caption | |
| Abstract | Yes | Mist band |
| Method | Three numbered steps | Emerald step circles |
| Results tables | Five comparison tables | |
| Dataset callout | Emerald highlight box | |
| Examples | Two dark example cards | |
| Video / sliders / 3D / HF Space | No | |
| BibTeX | Yes | Copy button in emerald |

## Do's and Don'ts

- Do recolour by editing the `:root` primary/accent and the three gradients together; that is all this variant changes.
- Do reserve the emerald gradient box for the single dataset call-out.
- Do keep author links blue if you want them to read as hyperlinks against green UI.
- Don't let the gold ribbon and emerald box sit next to each other; the page separates them by the stat strip and teaser.
- Don't forget a Bengali-capable font for the wordmark and examples.

## Surfaces

White page, `#f8fafc` bands with `#e2e8f0` borders, white cards, one emerald gradient panel, dark slate example cards.

## Imagery

One teaser PNG and result figures. No video.

## Layout

Centered 960px column with Bulma columns for stat cards (`is-6`, `is-6-mobile`, `is-multiline`).

## Agent Prompt Guide

**Quick colors:** text `#1e293b`, secondary `#64748b`, band `#f8fafc`, border `#e2e8f0`, primary `#10b981`, hover `#059669`, accent `#34d399`, author links `#2563eb`.

1. "Recolour the slate project template to emerald: `--primary-color #10b981`, `--primary-hover #059669`, `--accent-color #34d399`, section underline `linear-gradient(135deg, #34d399, #10b981)`; keep author links `#2563eb`."
2. "Build a dataset call-out: `linear-gradient(135deg, #10b981, #059669)` panel, 12px radius, white text, three small 1.5rem/700 stats with 0.8rem labels at 0.9 opacity, and a full-width white link tile with `#10b981` 600 text and 8px radius."
3. "Set a bilingual wordmark: Bengali 'গণিতLLM' in Noto Sans Bengali above an Inter 800 English title."

## Similar Pages

VC-Inspector (same author, blue variant) is the direct sibling; MMErroR and BadScientist share the template revision.

## Quick Start

```css
:root {
  --primary-color: #10b981; --primary-hover: #059669; --accent-color: #34d399;
  --text-primary: #1e293b; --text-secondary: #64748b; --text-light: #94a3b8;
  --background-primary: #ffffff; --background-secondary: #f8fafc;
  --background-accent: #f1f5f9; --border-color: #e2e8f0;
  --gradient-primary: linear-gradient(135deg, #10b981 0%, #059669 100%);
  --gradient-accent: linear-gradient(135deg, #34d399 0%, #10b981 100%);
  --gradient-subtle: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  --border-radius: 12px; --border-radius-lg: 16px;
}
body { font: 15px/1.6 'Inter', 'Segoe UI', sans-serif; color: var(--text-primary); }
```

## Provenance

- **URL:** https://dipta007.github.io/GanitLLM/
- **Paper:** GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO (arXiv 2601.06767), Shubhashis Roy Dipta, Khairul Mahbub, Nadia Najjar (UMBC, UNC Charlotte).
- **Venue:** ACL 2026 Findings (ribbon reads "ACL 2026 (Findings)").
- **Selection reason:** the arXiv comment states acceptance at ACL 2026 Findings; the project page is linked in the arXiv abstract.
- **Template credit:** footer credits the Academic Project Page Template (eliahuhorwitz), CC BY-SA 4.0.
- **Measurement method:** `extract_style.py`, a line diff of this `index.css` against VC-Inspector's, and reading the page `<style>` and inline styles. The rendered page was not viewed; the Noto Sans Bengali source is not confirmed.
