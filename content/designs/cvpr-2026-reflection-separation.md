# Reflection Separation Ink Pill — Style Reference

> A quiet off-white lab notebook where every control is an ink-black pill.

**Theme:** light

Values come from one 15 KB inline `<style>` block, Bulma 0.9.4 (jsDelivr) and Font Awesome 6.5 (cdnjs). Bulma's palette (`#485fc7` link etc.) inflates the raw counts but is overridden almost everywhere, so the table lists the page's own values. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

This page uses Bulma only as a reset and writes its own design system on top. The root font size is 18px (17px under 640px), the family is Inter with `cv11` and ligatures on, and the canvas is an off-white `#fafafa` with slate body text `#3a3f44`. Headings are near-black `#0f1419` at weight 800 with negative tracking. Every control is a pill: the uppercase "CVPR 2026" venue badge, the white outline link buttons that flip to ink on hover, and the example/layer/method tabs whose active state is solid `#0f1419`. The hero teaser and the "Visual Comparison" section use 14 custom drag sliders (`.comparison-frame`, 3:2, 10px radius) with a 34px white knob, `‹ ›` glyph and frosted dark labels; each slider can switch between transmission (T) and reflection (R) layers. The method figure has pulsing brick-red hotspots (`rgba(192,57,43,0.85)`) that swap the image for a JetBrains Mono pseudocode panel with butter-yellow highlights. Sections fade up on scroll (`.reveal`).

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Notebook Off-White | `#fafafa` | (literal) | Page, hero, content and footer background |
| Card White | `#fff` | (literal) | Buttons, tabs, venue badge, pre, pseudocode panel |
| Ink | `#0f1419` | (literal) | Title, section titles, active tab, button hover fill |
| Slate Body | `#3a3f44` | (literal) | Body text |
| Prose Gray | `#4a4a4a` | (literal) | `.section-text` |
| Detail Gray | `#444` / `#555` | (literal) | Authors, venue badge text, inactive tab text |
| Caption Gray | `#888` | (literal) | Figure and teaser captions |
| Faint Gray | `#777` / `#999` | (literal) | Affiliations, row labels, footer text |
| Hairline | `#e3e3e3` | (literal) | Venue badge, pre and pseudocode borders |
| Pill Border | `#d8d8d8` | (literal) | Button and tab borders |
| Author Blue | `#2563eb` | (literal) | Author links |
| Author Blue Deep | `#1d4ed8` | (literal) | Author link hover and dashed underline |
| Footer Link | `#3274D8` | (literal) | Footer link |
| Hotspot Brick | `rgba(192,57,43,0.85)` / `#c0392b` | (literal) | Method hotspots, hint emphasis |
| Pseudocode Butter | `#ffeec8` | (literal) | Algorithm line highlight |
| Selection Blush | `#ffd2cc` | (literal) | `::selection` |
| Inline Rose | `#f5c1ba` | (inline) | Highlighted term in text |
| Inline Apricot | `#fbe2c1` | (inline) | Highlighted term in text |
| Slider Mat | `#111` | (literal) | Comparison frame background |
| Label Glass | `rgba(15,20,25,0.7)` | (literal) | Slider labels with 8px blur |

## Tokens — Typography

- **Sans:** Inter 400 to 800 (Google Fonts), fallbacks `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto`. `font-feature-settings: 'kern', 'liga', 'cv11'`.
- **Mono:** JetBrains Mono 400/500 for pseudocode and BibTeX.
- **Root:** `html { font-size: 18px }`, 17px under 640px.

| Role | Size (rem of 18px) | Weight | Tracking / line height |
|---|---|---|---|
| Publication title | 2.5rem (1.75rem ≤640px, 1.6rem ≤768px) | 800 | -0.022em / 1.2 |
| Section title | 2rem (1.5rem mobile) | 800 | -0.018em |
| Subsection title | 1.35rem | 700 | -0.01em |
| Authors | 1.05rem | 500 | |
| Section text | 1.02rem | 400 | / 1.75 |
| Abstract | 0.95rem, justified, max 780px | 400 | / 1.75 |
| Affiliations | 0.92rem | 400 | |
| Buttons | 0.9rem | 600 | 0.01em |
| Figure caption | 0.88rem italic | 400 | |
| Venue badge | 0.85rem uppercase | 600 | 0.06em |
| BibTeX | 0.82rem mono | 400 | / 1.6 |
| Tabs | 0.85rem (example) / 0.8rem (comparison) | 600 | |
| Pseudocode | 0.78rem mono | 400 | / 1.6 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, tabs, venue badge, slider labels, back button | 999px |
| Figures | 12px |
| Comparison frame, pre, pseudocode panel | 10px |
| Slider knob, hotspots | 50% |

**Shadows:** button rest `0 1px 2px rgba(0,0,0,0.03)`, hover `0 4px 10px rgba(0,0,0,0.12)` with `translateY(-1px)`; comparison frame `0 2px 8px rgba(0,0,0,0.06), 0 0 0 1px rgba(0,0,0,0.04)`; knob `0 2px 6px rgba(0,0,0,0.35)`.

**Widths:** hero inner 1100px; section inner 960px; teaser stack 820px; teaser intro 720px; authors 56rem. Hero padding `4rem 2rem 1.5rem`; sections `1.5rem`.

## Components

- **Venue badge:** inline-block pill, white, 1px `#e3e3e3`, `0.25rem 0.9rem` padding, uppercase `#555`.
- **Link button (`.pub-btn`):** white pill, 1px `#d8d8d8`, `0.55rem 1.15rem`, 0.9rem/600 `#1a1a1a`; hover fills `#0f1419` with white text. Buttons: Paper (arXiv), Code (GitHub), 🤗 Models (Hugging Face).
- **Tabs (`.ex-tab`, `.comp-tab`):** white pills, active solid ink with `0 1px 3px rgba(0,0,0,0.15)`.
- **Comparison slider:** 3:2 frame on `#111`, `clip-path` reveal driven by `--pos`, 2px white divider, 34px knob with `‹ ›`, frosted labels bottom-left and bottom-right.
- **Method hotspot:** 12px brick-red dot, white 1.5px ring, 2.4s pulse; click shows detail text beside a smaller figure or a pseudocode panel.
- **BibTeX:** white pre, 1px `#e3e3e3`, 10px radius, 1.25rem padding, JetBrains Mono.
- **Footer:** `#fafafa`, 1px `#ddd` top rule, 0.85rem `#999` text, APPT credit.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | 800-weight ink title with rotating logo on hover |
| Venue badge | Yes | Uppercase pill "CVPR 2026" |
| Link buttons | Yes | Paper, Code, 🤗 Models; white outline pills |
| Teaser | Yes | Example tabs plus comparison sliders, italic intro |
| Abstract | Yes | 780px justified |
| Method figure | Yes | Architecture with clickable hotspots, method tabs, pseudocode mode |
| Results | Yes | "Visual Comparison" sliders with T/R layer tabs; "Quantitative Comparison" panes |
| Image comparison slider | Yes | 14 custom sliders |
| Interactive 3D / HF demo | Partial | Hugging Face model link, no embedded demo |
| BibTeX | Yes | White bordered pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do make every interactive control the same pill with the same ink active state.
- Do keep the canvas `#fafafa` and reserve pure white for controls and code.
- Do limit warm color to the method hotspots and small inline highlights.
- Don't use Bulma's default blue for anything except author links (`#2563eb`).
- Don't let the `.reveal` fade-in hide content when script fails; the class starts at opacity 0 until `.is-visible` is added.

## Surfaces

One continuous off-white surface; white pills and code panels float on it; dark `#111` mats behind slider images.

## Imagery

45 `<img>` tags: before/after pairs for sliders, an architecture figure, quantitative figures. No video.

## Layout

960px reading column inside 1100px hero; sliders capped at 820px in the teaser; controls centered in wrapping flex rows.

## Agent Prompt Guide

**Quick colors:** bg `#fafafa`, card `#fff`, ink `#0f1419`, body `#3a3f44`, caption `#888`, hairline `#e3e3e3`, pill border `#d8d8d8`, author `#2563eb`, hotspot `#c0392b`.

1. "Create an uppercase venue pill: white, 1px `#e3e3e3`, 999px radius, 0.85rem/600 `#555`, letter-spacing 0.06em."
2. "Build a before/after slider: 3:2 frame, 10px radius, `#111` mat, top image clipped with `inset(0 calc(100% - var(--pos)) 0 0)`, 2px white divider, 34px white circular knob showing '‹ ›', frosted `rgba(15,20,25,0.7)` labels at the bottom corners."
3. "Make link buttons as white outline pills (`#d8d8d8`) with 0.9rem/600 text that invert to `#0f1419` fill and white text on hover, lifting 1px."

## Similar Pages

Modern hand-tuned project pages that keep the APPT credit but replace its look; in this collection PR-IQA also restyles APPT with tokens, though with amber accents.

## Quick Start

```css
:root {
  --bg: #fafafa; --card: #fff; --ink: #0f1419; --text: #3a3f44;
  --prose: #4a4a4a; --caption: #888; --hairline: #e3e3e3; --pill-border: #d8d8d8;
  --author: #2563eb; --author-hover: #1d4ed8; --hotspot: #c0392b;
  --hilite: #ffeec8; --selection: #ffd2cc; --mat: #111;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", SFMono-Regular, Menlo, monospace;
  --radius-pill: 999px; --radius-figure: 12px; --radius-frame: 10px;
  --section: 960px; --hero: 1100px;
}
html { font-size: 18px; }
```

## Provenance

- **URL:** https://brian90709.github.io/diff-reflection-separation/
- **Paper:** Reflection Separation from a Single Image via Joint Latent Diffusion (arXiv 2606.04107), Zheng-Hui Huang et al.
- **Venue:** CVPR 2026 (venue badge).
- **Selection reason:** arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit:** footer credits the Academic Project Page Template, but the styling is almost entirely custom.
- **Measurement method:** `extract_style.py` plus a full manual read of the inline style block. Rendered page not viewed.
