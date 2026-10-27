# VLN-NF Navy Wayfinder — Style Reference

> A clean signage system in a modern museum: soft white cards, pill-shaped signposts, one navy arrow that says go.

**Theme:** light

Measurements come from the single inline `<style>` block (no framework, no external CSS). Colors are declared in `:root` or as literals; roles are interpreted from markup.

## Overview

A compact, hand-built page in a SaaS-documentation idiom. The background is a 260px vertical wash from `#f9fbff` into white. The hero is centered: a navy-on-ice "ACL 2026" eyebrow pill, an 800-weight title with tight -0.04em tracking and fluid size, authors, muted affiliations and notes, one solid navy pill button (arXiv), a muted availability note ("Code and data links will be added here once they are public."), then a row of quick-nav pills. Content sits in 18px-radius white cards with a 1px `#e5e7eb` border and a wide, faint `0 14px 40px rgba(15,23,42,0.08)` shadow. Three highlight cards sit in a grid under the teaser. BibTeX is a dark `#0f172a` block with a pill copy button.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Wayfinder Navy | `#2f4b8f` | `--accent` | Eyebrow text, primary button fill and border, quick-nav hover text |
| Ice Wash | `#eef3ff` | `--accent-soft` | Eyebrow fill, quick-nav hover fill |
| Ice Edge | `#dbe7ff` | (literal) | Quick-nav hover border |
| Graphite | `#1f2937` | `--text` | Body text |
| Author Ink | `#111827` | (literal) | Author line |
| Slate Muted | `#64748b` | `--muted` | Affiliations, notes, availability, captions, footer, card body |
| Hairline | `#e5e7eb` | `--line` | Card and button borders |
| Hover Edge | `#cbd5e1` | (literal) | Button and copy-button hover border |
| Figure Edge | `#edf2f7` | (literal) | 1px border on figure images |
| Dawn Wash | `#f9fbff` | (literal) | Top of the body gradient |
| Soft Ground | `#f7f9fc` | `--bg-soft` | Declared soft background |
| Card White | `#ffffff` | `--bg` / `--card` | Cards, buttons, page |
| Night Code | `#0f172a` | (literal) | BibTeX background |
| Moon Text | `#e5eefc` | (literal) | BibTeX text |
| Card Shadow | `rgba(15,23,42,0.08)` | `--shadow` | Card shadow colour |

## Tokens — Typography

- **Text:** `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`. No web font is linked, so Inter appears only if installed; otherwise system-ui (inferred).
- **Mono:** `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.
- **Weights:** 800 title, 700 eyebrow, buttons and section titles.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title | `clamp(2.15rem, 4vw, 3.6rem)` | 800 | 1.12 | letter-spacing -0.04em |
| Eyebrow pill | 0.94rem | 700 | 1.65 | 0.01em tracking |
| Authors | 1.05rem | 400 | 1.65 | max-width 980px |
| Affiliations / notes / availability | 0.98 / 0.96 / 0.95rem | 400 | 1.65 | muted |
| Section title | 1.9rem | bold (h2) | 1.65 | -0.03em, centered |
| Section subtitle | 1rem | 400 | 1.65 | muted, max 860px |
| Highlight card h3 | 1.08rem | bold | | -0.01em |
| Card body / quick-nav | 0.96rem | 400 | | |
| Caption | 0.95rem | 400 | | muted |
| BibTeX | 0.93rem mono | 400 | 1.55 | |
| Footer | 0.92rem | 400 | | muted |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Section / figure / highlight / BibTeX cards (`--radius`) | 18px |
| Figure images, `pre` | 14px |
| Eyebrow, buttons, quick-nav, copy button | 999px |

- **Shadows:** cards `0 14px 40px rgba(15,23,42,0.08)`; buttons `0 3px 12px rgba(15,23,42,0.04)`, hover `0 10px 24px rgba(15,23,42,0.08)` with a 1px lift; copy button hover `0 8px 18px rgba(15,23,42,0.06)`.
- **Layout:** `--maxw` 1120px via `width: min(calc(100% - 32px), var(--maxw))`; `.narrow` 920px; hero padding 56px 0 26px; sections 18px 0 20px; card padding 28px (22px mobile); figure-card 18px.

## Components

- **Eyebrow pill.** Inline-flex, 8px 14px padding, 999px radius, `#eef3ff` fill, `#2f4b8f` 700 text: "ACL 2026".
- **Button.** Min-height 46px, 0 18px padding, 999px radius, white fill, 1px `#e5e7eb` border, 700 text, small shadow; `.primary` fills navy with white text. Only one button (arXiv) is present.
- **Quick-nav.** Centered pill links (Abstract · Overview · Method · BibTeX), muted 0.96rem; hover turns them into ice-wash pills with navy text.
- **Section card.** White, 1px hairline, 18px radius, wide soft shadow, 28px padding.
- **Figure card.** Same shell, 18px padding; image 14px radius with a `#edf2f7` border; muted caption ("Figure 1. …").
- **Highlight grid.** Three equal cards (one column under 900px) with a 1.08rem h3 and muted body: false-premise VLN, evidence-grounded evaluation, ROAM.
- **BibTeX card.** Header row with title and a pill copy button; dark `#0f172a` `pre` with `#e5eefc` text, 14px radius.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered, symbol superscripts († ‡) |
| Venue badge | Yes | Ice-wash eyebrow pill "ACL 2026" |
| Link buttons | arXiv only | Navy primary pill; note says code and data will follow |
| Section nav | Quick-nav pills | |
| Teaser figure | Yes | Figure card under the abstract |
| Abstract | Yes | Section card |
| Highlights | Three-card grid | |
| Method figure | Yes | Figure card (two-up grid available) |
| Results tables / video / sliders / 3D / HF demo | No | |
| BibTeX | Yes | Dark code card with copy |
| Footer | "Lightweight static project page for GitHub Pages." | Muted |

## Do's and Don'ts

- Do use the navy only on the eyebrow, the primary button and hover states.
- Do keep every content block in the same 18px white card with the same shadow.
- Do state plainly when code or data are not yet public, as this page does under the buttons.
- Don't add a second accent hue; status is carried by fill (navy vs white), not colour.
- Don't rely on Inter without linking it.

## Surfaces

Body gradient `#f9fbff` → `#ffffff` over the first 260px, then white. White bordered cards, one dark code card.

## Imagery

Two static figures (teaser and method). No video.

## Layout

1120px max container with 16px gutters, centered hero and section titles, 3-column highlight grid and 2-column figure grid that stack under 900px.

## Agent Prompt Guide

**Quick colors:** text `#1f2937`, muted `#64748b`, line `#e5e7eb`, accent `#2f4b8f`, accent-soft `#eef3ff`, code `#0f172a`, page wash `#f9fbff`.

1. "Create a venue eyebrow pill: inline-flex, 8px 14px padding, 999px radius, `#eef3ff` fill, `#2f4b8f` 0.94rem/700 text, 18px below it an 800-weight title at `clamp(2.15rem, 4vw, 3.6rem)` with -0.04em tracking."
2. "Make a content card: white, 1px `#e5e7eb` border, 18px radius, `0 14px 40px rgba(15,23,42,0.08)` shadow, 28px padding."
3. "Build a BibTeX card: header row with a 'BibTeX' title and a white pill copy button (1px `#e5e7eb`, 40px min-height, 700), then a `#0f172a` `pre` with `#e5eefc` 0.93rem mono text and 14px radius."

## Similar Pages

UniversalRAG (ACL 2026) in this batch is the other card-and-pill, framework-free page with a single blue accent.

## Quick Start

```css
:root {
  --bg: #ffffff; --bg-soft: #f7f9fc; --card: #ffffff;
  --text: #1f2937; --muted: #64748b; --line: #e5e7eb;
  --accent: #2f4b8f; --accent-soft: #eef3ff;
  --shadow: 0 14px 40px rgba(15, 23, 42, 0.08);
  --radius: 18px; --maxw: 1120px;
}
body { font-family: Inter, ui-sans-serif, system-ui, sans-serif; line-height: 1.65;
  color: var(--text); background: linear-gradient(180deg, #f9fbff 0px, #ffffff 260px); }
```

## Provenance

- **URL:** https://vln-nf.github.io/
- **Paper:** VLN-NF: Feasibility-Aware Vision-and-Language Navigation with False-Premise Instructions (arXiv 2604.10533), Hung-Ting Su, Ting-Jun Wang, Jia-Fong Yeh, Min Sun, Winston H. Hsu (National Taiwan University, National Tsing Hua University).
- **Venue:** ACL 2026 (eyebrow pill; page title prefixed "[ACL 2026]").
- **Selection reason:** the arXiv comment states ACL 2026 camera ready; the project page is linked in the arXiv abstract.
- **Template credit:** none; footer reads "Lightweight static project page for GitHub Pages."
- **Measurement method:** `extract_style.py` and a full read of the inline stylesheet. The rendered page was not viewed, so the effective font (Inter vs system fallback) is not confirmed.
