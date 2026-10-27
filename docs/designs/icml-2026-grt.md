# GRT Kinetic Title Blue — Style Reference

> A one-file lab page where the title itself is a looping video.

**Theme:** light

Values come from the single inline `<style>` block of a framework-free HTML file (no external CSS). Measurements are normalized; roles are interpreted from usage.

## Overview

The GRT page replaces the usual text title with an autoplaying, muted, looping title-motion video (the real `<h1>` is visually hidden for accessibility), followed by a bold subtitle, a blue "ICML 2026" h2, and two names. Below the hero sit five slate-gray capsule buttons that turn electric blue `#1f71f6` and lift 3px on hover. A compact comparison table with green ticks and red crosses opens the content, followed by a glowing amber dataset badge, then alternating `#fafbfc` and white full-bleed bands for Method Insight, Dataset Gallery, Results Gallery and BibTeX. One blue does all the accent work: links, h2s, table headers, gallery-arrow hover.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Reciprocity Blue | `#1f71f6` | (literal) | Links, h2 (including venue), table header text, button hover fill, arrow hover |
| Ours Blue | `#1463d8` | `.ours td` | "Ours" row text, bold |
| Ours Wash | `#f6fbff` | `.ours td` | "Ours" row fill |
| Header Wash | `#f3f7ff` | `th` | Table header fill |
| Slate Capsule | `#4a5568` | `.button` | Button fill and border |
| Headline Ink | `#1a1a1a` | `h1`, `.title-subtitle` | Subtitle and section titles |
| Body Ink | `#333333` | `body` | Body text, table cells, BibTeX |
| Prose Gray | `#555555` | `.contributors`, `.description` | Names, descriptions, captions |
| Muted Slate | `#667085` / `#4b5563` | `.media-label`, `.sample-count` | Media labels, counters |
| Tick Green | `#2f855a` | `.yes` | ✓ marks, weight 800 |
| Cross Red | `#b94a48` | `.no` | ✗ marks, weight 800 |
| Band Paper | `#fafbfc` | method, dataset, BibTeX sections | Alternating band |
| Media Mint | `#f4f7f6` | video backgrounds | Letterbox behind videos |
| Rule Gray | `#e5e7eb` | table | Table wrapper border and row rules |
| Amber Badge | `#fff7eb` / `#ffd7a3` / `#8a5518` | `--badge-*` on `.resource-masks` | Dataset badge fill, border, text; hover border `#e78e1e` |
| Blue Badge | `#eef5ff` / `#c5dafa` / `#275a9b` | `--badge-*` on `.inline-badge` | Inline resource badge |
| Badge Default | `#f1f6ff` / `#c7daf4` / `#355f92` | fallbacks | Default badge colors |

## Tokens — Typography

- **Sans (everything):** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`. No web font. Substitute: Inter.
- **Mono:** `"SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace` for BibTeX.
- Unusual weights: 750 (subtitle) and 800 (ticks, `.gradient-text`).

| Role | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| h1 (section titles) | 2.8rem (2rem ≤768px) | 700 | 1.2 | justified with centered last line |
| `.title-center` section titles | 2.5rem | 700 | | centered |
| Subtitle | 2.05rem (1.55rem ≤768px) | 750 | 1.18 | max 980px |
| h2 / venue | 1.6rem (1.35rem ≤768px) | 600 | | blue |
| Description | 1.2rem | 400 | 1.7 | gray, max 1080px |
| Contributors | 1.1rem | 400 | 1.8 | |
| Section note | 1.05rem | 400 | 1.65 | |
| Buttons | 0.95rem | 600 | | |
| Table | 0.96rem (0.72rem ≤768px) | 400 / header 700 | | |
| BibTeX | 0.92rem | 400 | 1.55 | `white-space: pre` |
| Media label | 0.8rem | 700 | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 50px |
| Resource badges, video toggle | 999px |
| BibTeX wrapper | 12px |
| Table wrapper | 10px |
| Method video, placeholders | 6px |
| Gallery video | 5px |
| Gallery arrows | 50% |

- **Shadows:** buttons `0 4px 15px rgba(0,0,0,.1)` → hover `0 8px 25px rgba(0,0,0,.15)`; table `0 5px 18px rgba(0,0,0,.07)`; BibTeX `0 4px 15px rgba(0,0,0,.08)`; badges pulse with a `badgeGlow` keyframe (3.8s) that grows a 6px ring, disabled under `prefers-reduced-motion`.
- **Layout:** `main` and `.section-content` max 1200px with 20px padding; title video `min(900px, 96vw)`; result card and method grid 980px; sample browser 1120px; BibTeX 1040px; section padding 72-80px vertical.

## Components

- **Title-motion hero.** Visually hidden h1, then a transparent-background looping MP4 as the visible title, the bold subtitle, a blue venue h2 and names in `#555`.
- **Capsule button.** Fixed 128px wide, padding 14px 28px, `#4a5568` fill and border, white 0.95rem/600 label, 18px icon, 50px radius. Hover: blue fill and border, translateY(-3px), deeper shadow. Buttons without `href` drop to 0.72 opacity.
- **Comparison table.** White, 10px-radius wrapper with a soft shadow, `#f3f7ff` header with blue 700 text, `#e5e7eb` rules, ✓/✗ in green/red 800, "Ours" row in `#f6fbff` with `#1463d8` bold text.
- **Resource badge.** 38px-high pill with icon, label and a trailing `↗`, colored by `--badge-*` variables (amber for the masks dataset), slow glow pulse, lifts 2px on hover.
- **Gallery control.** Two 32px round arrows (`#d9e2ec` border, white) around a bold sample counter; arrow hover turns blue. Slides fade and shift 18px.
- **Method video.** Wide 40:11 video on `#f4f7f6` with a 34px round translucent play/pause toggle at top-right.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Video title, subtitle, venue h2, names |
| Venue badge | "ICML 2026" h2 | Blue text, no chip |
| Link buttons | Paper, Code, Demo (Colab), Gallery, BibTeX | Slate capsules |
| Teaser | Comparison table plus description directly under buttons | |
| Abstract | No labeled abstract; a description paragraph | |
| Method | "Method Insight" band | Wide videos with captions |
| Dataset | "Dataset Gallery" with HF masks badge (~300K Kinetics-GRT masks) | Amber badge, 3-up / 2-up video grids |
| Results | "Results Gallery" | Paged video browser |
| BibTeX | Yes | White card on `#fafbfc` band |
| Acknowledgements / footer | No footer element | |

## Do's and Don'ts

- Do keep a single blue for links, headings and hovers; badges are the only place for amber.
- Do make buttons a fixed width so the row reads as a set.
- Do alternate `#fafbfc` and white bands per section.
- Don't render the h1 as text when the motion title is present; keep it visually hidden.
- Don't skip the reduced-motion rule when copying the badge glow.

## Surfaces

White hero, alternating `#fafbfc` / white full-bleed bands, white cards for table and BibTeX, mint-gray video letterboxes.

## Imagery

Stereoscopic video pairs and masks, shown in 3-up and 2-up grids; the title is a motion graphic.

## Layout

Single 1200px column with full-bleed band backgrounds built from `100vw` and negative margins. Grids collapse to one column at 768px, where table cells wrap and shrink to 0.72rem.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#fafbfc`, ink `#333333`, headline `#1a1a1a`, gray `#555555`, accent `#1f71f6`, button `#4a5568`, yes `#2f855a`, no `#b94a48`.

1. "Make a row of fixed 128px capsule links: `#4a5568` fill, white 0.95rem/600 label with an 18px icon, 50px radius, shadow `0 4px 15px rgba(0,0,0,.1)`; on hover fill `#1f71f6` and lift 3px."
2. "Build a feature comparison table with ✓ in `#2f855a` and ✗ in `#b94a48` at weight 800, a `#f3f7ff` header with `#1f71f6` 700 text, and the 'Ours' row in `#f6fbff` with `#1463d8` bold text."
3. "Create a resource badge pill: 38px high, `#fff7eb` fill, `#ffd7a3` border, `#8a5518` 0.84rem/700 label with a trailing ↗ and a slow glowing ring animation that stops under reduced motion."

## Similar Pages

Single-file custom pages from the same lab family (Visual AI Lab, HKU); TapSampling in this collection is another framework-free 2026 page.

## Quick Start

```css
:root {
  --accent: #1f71f6; --accent-strong: #1463d8; --accent-wash: #f3f7ff;
  --ink: #333333; --headline: #1a1a1a; --muted: #555555;
  --button: #4a5568; --band: #fafbfc; --rule: #e5e7eb; --video-bg: #f4f7f6;
  --yes: #2f855a; --no: #b94a48;
  --badge-bg: #fff7eb; --badge-border: #ffd7a3; --badge-fg: #8a5518;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  --container: 1200px;
}
body { font-family: var(--font-sans); color: var(--ink); line-height: 1.6; background: #fff; }
```

## Provenance

- **URL:** https://visual-ai.github.io/grt/
- **Paper:** Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation (arXiv 2607.05354), Jingyi Lu and Kai Han.
- **Venue:** ICML 2026 (h2 in the hero).
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit:** none; hand-written single HTML file with no footer.
- **Measurement method:** `extract_style.py` on static HTML plus manual reading of the inline style block. Rendered page not viewed; the title-motion video and badge animation are described from CSS and markup only.
