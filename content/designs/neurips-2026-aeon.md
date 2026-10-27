# AEON Night and Day — Style Reference

> An observatory almanac: small-caps serif wordmark on midnight navy, then pale day plates.

**Theme:** both (dark hero and dark gallery section, light content sections)

Values come from the single stylesheet `static/css/aeon.css`, which defines two complete token sets: one scoped to `.sec--night` and the top bar, one to every other `.sec`. Fonts are self-hosted OFL files. Roles are interpreted. Rendered output was not viewed.

## Overview

AEON (Tsinghua group of Yu-Shen Liu) is the most typographically deliberate page in this batch. The hero is a night section on `#0B1430` with a faint amber radial glow, a 14px amber venue line "NeurIPS 2026", a huge Spectral SC Light wordmark "Aeon" (92–160px, line-height .8), a Spectral Light subtitle, a Schibsted Grotesk lede and author list with hairline underlines, and four outline pill buttons (Paper, arXiv, Code, BibTeX). To the right sits a live world viewer (canvas, 4D Gaussian renders) with a vertical thumbnail picker and a time scrubber whose thumb is a thin amber bar. The following Abstract, Method and Results sections switch to the day token set (`#F2F4F8` ground, `#10172B` text, darker amber `#9A5B0E`), with white plates for figures and a paradigm comparison table whose "ours" row is tinted amber. A second night section hosts the generated-worlds gallery; BibTeX returns to day.

## Tokens — Colors

**Night set (`.sec--night`, `.topbar`, dialogs)**

| Name | Value | Token | Role |
|---|---|---|---|
| Midnight | `#0B1430` | `--bg` | Night section and `html` background |
| Deep Midnight | `#070D20` | `--bg-deep` | Explainer stage, code |
| Starlight | `#EEF2FA` | `--fg` | Primary text |
| Haze | `#C5CFE3` | `--fg-soft`, `--p2` | Body paragraphs, second series |
| Dusk Gray | `#8D9AB8` | `--muted` | Affiliations, captions |
| Lantern Amber | `#F0B054` | `--accent`, `--p1` | Venue, superscripts, hover, focus, scrubber |
| Sky Series | `#7FB8F0` | `--p3` | Third data series |
| Night Line | `rgba(197,207,227,.14)` / `.30` | `--line` / `--line-strong` | Rules, button borders |

**Day set (all other `.sec`)**

| Name | Value | Token | Role |
|---|---|---|---|
| Daylight Ground | `#F2F4F8` | `--bg` | Content sections |
| Day Deep | `#E7EBF2` | `--bg-deep` | BibTeX pre, explainer stage |
| Day Ink | `#10172B` | `--fg` | Headings and primary text |
| Day Soft | `#2E3852` | `--fg-soft` | Body paragraphs |
| Day Muted | `#5C6682` | `--muted`, `--p2` | Captions, table heads |
| Burnt Amber | `#9A5B0E` | `--accent` | Accent on light ground |
| Copper Series | `#B9700F` | `--p1` | First data series |
| Cobalt Series | `#2F6FB8` | `--p3` | Third data series |
| Plate White | `#FFFFFF` | `--plate` | Figure plates |
| Day Line | `rgba(16,23,43,.10)` / `.24` | `--line` / `--line-strong` | Rules, borders |
| Ours Tint | `rgba(240,176,84,.16)` (night `.085`) | `--ours-bg` | Highlighted table row |

## Tokens — Typography

- **Mark:** `Spectral SC` 300 (wordmark, top-bar mark). Substitute: Cormorant SC.
- **Display:** `Spectral` 300/400/600 with italics (h2, h3, subtitle, all `<i>`). Substitute: Georgia.
- **UI / body:** `Schibsted Grotesk` 400/500/600. Substitute: system-ui, Inter.
- **Mono:** ui-monospace, "SF Mono", Menlo, Consolas.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Wordmark | `clamp(92px, 11.4vw, 160px)` | 300 SC | .8 | .012em, -.045em left margin |
| Subtitle | `clamp(24px, 2.35vw, 32px)` | 300 | 1.18 | |
| h2 | `clamp(32px, 4.2vw, 46px)` | 300 | | |
| h3 | `clamp(22px, 2.3vw, 26px)` | 400 | | |
| Top-bar mark | 25px | 300 SC | 1 | |
| Body | 17px (16px ≤720px) | 400 | 1.62 (1.7 in sections) | `text-wrap: pretty` |
| Authors | 16px | 400 | | hairline underline |
| Buttons | 14.5px | 500 | 1 | |
| Venue, affiliation, captions | 14–14.5px | 500 / 400 | 1.55 | venue .02em |
| Table head | 13px | 500 | 1.3 | |
| BibTeX | 12.5px | 400 | 1.75 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, copy button | 999px |
| Plates, explainer stage, BibTeX pre | 8px |
| Skip link, small controls | 6px / 4px / 3px |
| Picker thumbnails | inferred square with focus ring |

- **Shadows:** viewer stage `0 40px 90px -40px rgba(0,0,0,.75)`; picker selection is a double ring `0 0 0 1.5px var(--bg), 0 0 0 3px var(--accent)`. Content is otherwise flat.
- **Layout:** `--col` 960px, `--col-full` 1240px (top bar, hero grid), `--pad clamp(20px, 4vw, 40px)`.
- **Rhythm:** `--sec-space clamp(64px, 7.5vw, 104px)`; consecutive day sections collapse top padding to 8px.

## Components

- **Top bar.** 56px, transparent until scrolled, then `color-mix(bg 84%)` with a bottom line; small-caps mark appears on scroll; links 26px apart, hidden under 720px.
- **Venue line.** 14px/500 amber text, no badge.
- **Button (`.btn`).** 40px tall pill, 1px `--line-strong` border, transparent fill, 17px stroked icon, 500 weight; hover turns border and text amber. An `is-soon` variant appends "soon".
- **World viewer.** Canvas stage sized `clamp(300px, min(58vh, 40vw), 448px)`, eight-thumbnail vertical picker, viewer-mode segmented buttons (pressed = inverted fg/bg), amber bar scrubber.
- **Plate.** White figure plate, 8px radius, `clamp(10px, 1.6vw, 22px)` padding, 14.5px muted caption with bold soft-ink lead.
- **Paradigm table.** UI font, 15px 12px cells, 13px muted header over a strong line, check/cross glyphs via `data-yes`/`data-no`, amber-tinted ours row.
- **BibTeX.** `--bg-deep` pre, 1px line, 8px radius, with a pill "copy" button that turns amber on hover.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Giant small-caps wordmark, serif subtitle, grotesk authors |
| Venue badge | Amber text line | |
| Link buttons | Paper (PDF), arXiv, Code, BibTeX anchor | Outline pills |
| Teaser | Interactive 4D world viewer in hero | |
| Abstract | Day section | |
| Method figure | Plate plus draggable explainer SVG | |
| Results | Paradigm comparison table and figures | |
| Interactive 3D | Hero viewer and night "Generated worlds" gallery with dialogs | |
| Sliders | Time scrubber and explainer drag | |
| BibTeX | Yes | Deep panel with copy pill |
| Acknowledgements | No | |

## Do's and Don'ts

- Do switch whole token sets per section rather than recoloring components.
- Do use the lighter amber `#F0B054` on night and the darker `#9A5B0E` on day.
- Do keep headings in Spectral Light; weight comes from size, not boldness.
- Don't fill buttons; they are outlines in both modes.
- Don't add drop shadows to day content; only the viewer floats.

## Surfaces

Midnight hero and gallery, daylight content sections, white plates, deep panels for code and explainer.

## Imagery

Live canvas renders of generated 4D worlds, thumbnail pickers, white-plated method and results figures, an interactive SVG explainer.

## Layout

Hero is a two-column grid (text left, viewer and picker right) at 1240px, collapsing to one column under 1020px. Content columns are 960px.

## Agent Prompt Guide

**Quick colors:** night bg `#0B1430`, night fg `#EEF2FA`, night accent `#F0B054`; day bg `#F2F4F8`, day fg `#10172B`, day soft `#2E3852`, day muted `#5C6682`, day accent `#9A5B0E`, plate `#FFFFFF`.

1. "Make a night hero on `#0B1430`: 14px/500 amber `#F0B054` venue line, a Spectral SC weight-300 wordmark at `clamp(92px,11.4vw,160px)` with line-height .8, and a Spectral Light 32px subtitle in `#EEF2FA`."
2. "Create outline pill buttons 40px tall: 1px `rgba(197,207,227,.30)` border, transparent fill, Schibsted Grotesk 14.5px/500, 17px stroke icons; hover turns border and text amber."
3. "Build a comparison table on `#F2F4F8`: 13px/500 `#5C6682` headers above a `rgba(16,23,43,.24)` rule, 15px 12px centered cells, ours row tinted `rgba(240,176,84,.16)`."

## Similar Pages

Editorial magazine-style project pages with dual light/dark sections; OmniUE in this collection also opens on a dark hero, though with a sans display face.

## Quick Start

```css
.sec--night { --bg: #0B1430; --bg-deep: #070D20; --fg: #EEF2FA; --fg-soft: #C5CFE3;
  --muted: #8D9AB8; --line: rgba(197,207,227,.14); --line-strong: rgba(197,207,227,.30);
  --accent: #F0B054; --ours-bg: rgba(240,176,84,.085); }
.sec:not(.sec--night) { --bg: #F2F4F8; --bg-deep: #E7EBF2; --fg: #10172B; --fg-soft: #2E3852;
  --muted: #5C6682; --line: rgba(16,23,43,.10); --line-strong: rgba(16,23,43,.24);
  --accent: #9A5B0E; --ours-bg: rgba(240,176,84,.16); --plate: #FFFFFF; }
:root {
  --font-mark: "Spectral SC", "Spectral", Georgia, serif;
  --font-display: "Spectral", Georgia, serif;
  --font-ui: "Schibsted Grotesk", system-ui, -apple-system, "Segoe UI", sans-serif;
  --body-size: 17px; --body-lh: 1.62; --col: 960px; --col-full: 1240px;
  --pad: clamp(20px, 4vw, 40px); --sec-space: clamp(64px, 7.5vw, 104px);
}
```

## Provenance

- **URL:** https://weiqi-zhang.github.io/AEON/
- **Paper:** AEON: Unifying Video and 3D World Models (arXiv 2610.28631), Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** none; custom page with self-hosted OFL fonts.
- **Measurement method:** static HTML and `aeon.css` parsed with `extract_style.py` and read directly; both token sets taken verbatim from the CSS. Not viewed in a browser, so the viewer's look is described from CSS, not from a render.
