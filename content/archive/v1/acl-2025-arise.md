# ARise · Black Banner Readme — Style Reference

> A GitHub README that put on a black header and walked onto the web.

**Theme:** light

Measurements are normalized from the page's single inline `<style>` block (no external CSS, no framework); roles are interpreted from markup and one rendered viewport. Every color listed appears in that block.

## Overview

ARise is hand-written HTML of about 9 KB: Arial throughout, a near-black `#1a1a1a` header band holding the title, a one-line tagline and two small white buttons (Code, Paper), then authors and affiliations on an off-white `#f9f9f9` page body capped at 900px. Sections are introduced by emoji `h2`s (🧠 Abstract, 🚀 Key Features, 🔍 Method, 📊 Experimental Results, 📄 Citation). Figures get an 8px radius and a soft drop shadow with italic grey captions; key points sit in a pale blue callout with a 4px blue left rule. A matching black footer closes the page.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Ink Banner | `#1a1a1a` | `--band` | Header and footer background |
| Banner White | `#ffffff` (`white`) | `--band-fg` | Header and footer text, button fill |
| Porcelain | `#f9f9f9` | `--bg` | Body background |
| Graphite | `#333333` | `--text` | Body text |
| Near Black | `#111111` | `--heading` | h1–h3 in the body |
| Cobalt Link | `#007acc` | `--link` | Links and callout rule |
| Caption Grey | `#555555` | `--caption` | Figure captions |
| Code Linen | `#eeeeee` | `--code-bg` | `pre` background |
| Callout Ice | `#f0f7ff` | `--callout-bg` | `.highlight` box |

## Tokens — Typography

- **Family:** Arial, sans-serif for everything; `monospace` for code.
- No web fonts are loaded.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Title (`h1`, in banner) | 2em (browser default, inferred) | 700 | 1.6 |
| Section heading (`h2`) | 1.5em (browser default, inferred) | 700 | 1.6 |
| Sub-heading (`h3`) | 1.17em (inferred) | 700 | 1.6 |
| Body | 16px (inferred) | 400 | 1.6 |
| Captions | 0.9em italic (scan) | 400 | 1.6 |
| Footnotes, emails | 0.8em | 400 | 1.6 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Figures | 8px |
| Banner buttons | 4px |
| Callout | 0 (left rule only) |

Shadows: figures `0 4px 12px rgba(0,0,0,0.1)`. Spacing: header padding 2rem 1rem; `main` padding 2rem, max-width 900px, centered; sections margin-bottom 3rem; `pre` padding 1rem; callout padding 1rem, margin 1rem 0; footer padding 1rem, margin-top 3rem.

## Components

- **Black banner:** full-width `#1a1a1a`, centered white title, small tagline, two white buttons with black text.
- **Emoji heading:** left-aligned `h2` with one leading emoji, `#111`.
- **Figure:** `img.figure` max-width 100%, 8px radius, soft shadow, 1.5rem vertical margin; `.figure-caption` centered italic `#555`.
- **Callout:** `.highlight` `#f0f7ff` fill, 4px solid `#007acc` left border.
- **Code / citation:** `pre` on `#eeeeee`, 1rem padding, horizontal scroll.
- **Footer:** black band, "© 2025 OpenCausaLab, Shanghai AI Laboratory".

## Page Modules

- **Title/author block:** title and tagline inside the banner; authors with numbered affiliations and corresponding-author emails below, centered.
- **Venue badge:** none on the page.
- **Link buttons:** Code, Paper (white on black).
- **Teaser:** none.
- **Abstract:** "🧠 Abstract".
- **Method figure:** "🔍 Method: ARise Pipeline".
- **Results:** "📊 Experimental Results" with two figure subsections (baselines, large reasoning models); no HTML tables.
- **BibTeX:** "📄 Citation" in a `pre`.
- **Footer:** lab copyright line.

## Do's and Don'ts

- Do frame the page top and bottom with the same black band.
- Do keep one blue (`#007acc`) for links and the callout rule only.
- Don't add a framework or web font; Arial and browser defaults are the style.
- Don't center body text; only the banner, author block and captions are centered.

## Surfaces

Black band, off-white page, lighter grey code blocks, ice-blue callouts. Figures float with one soft shadow.

## Imagery

Pipeline diagram and result charts exported from the paper, each in the rounded-shadow frame.

## Layout

Single 900px column, 2rem padding, generous 3rem gaps between sections.

## Agent Prompt Guide

Quick colors: band `#1a1a1a`, bg `#f9f9f9`, text `#333`, heading `#111`, link `#007acc`, callout `#f0f7ff`, code `#eee`.

1. "Build a black header band: `#1a1a1a`, padding 2rem 1rem, centered white Arial title, small tagline, two white 4px-radius buttons."
2. "Build a callout: background `#f0f7ff`, padding 1rem, 4px solid `#007acc` left border, Arial 16px/1.6 `#333`."
3. "Build a figure: max-width 100%, radius 8px, shadow `0 4px 12px rgba(0,0,0,.1)`, centered italic caption `#555` at .9em."

## Similar Pages

Markdown-rendered GitHub READMEs; minimal single-file lab project pages.

## Quick Start

```css
:root {
  --band: #1a1a1a; --bg: #f9f9f9; --text: #333; --heading: #111;
  --link: #007acc; --caption: #555; --code-bg: #eee; --callout: #f0f7ff;
  --radius-fig: 8px; --shadow-fig: 0 4px 12px rgba(0,0,0,0.1);
  --font: Arial, sans-serif; --max-width: 900px;
}
body { font-family: var(--font); line-height: 1.6; background: var(--bg); color: var(--text); margin: 0; }
```

## Provenance

- **URL:** https://opencausalab.github.io/ARise/
- **Paper:** ARise: Towards Knowledge-Augmented Reasoning via Risk-Adaptive Search (arXiv 2504.10893), Yize Zhang et al.
- **Venue:** ACL 2025.
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and links this page.
- **Template credit:** none; custom single-file HTML with a footer naming OpenCausaLab, Shanghai AI Laboratory.
- **Measurement method:** the complete inline style block was read directly, plus the extract_style.py scan and one rendered viewport. Heading and body sizes are browser defaults because the CSS does not set them (marked inferred).
