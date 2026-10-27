# Rectified Point Flow — Style Reference

> Indigo glass card floating on a pale periwinkle haze.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.9 plus the page's `css/index-v5.css` and `css/pages.css`, TwentyTwenty and jQuery UI) and roles are interpreted from selectors and one rendered look. Bulma's default palette (`#00d1b2`, `#ffdd57`, `#3273dc`) appears in frequency counts but the page overrides it with its own indigo system, so those values are excluded.

## Overview

A Nerfies skeleton re-dressed as a modern landing page. The body sits on `#f8fafc` with slate text `#0f172a`. The hero (`.hero.is-landing`) uses a radial gradient from `#eef2ff` through white to `#f5f3ff`, with two blurred circular glows (indigo top-right, sky bottom-left). Inside it a frosted white `.landing-card` (rgba white .92, 32px radius, backdrop blur) holds the Google Sans title, indigo author links, a letter-spaced "NEURIPS 2025 • SPOTLIGHT" badge and four gradient-indigo pill buttons with deep glow shadows. Section titles get a 6px vertical indigo-to-violet bar at the left. Figures sit in 24px-radius frames; BibTeX is a dark navy code card.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Snow Slate | `#f8fafc` | — | Body background |
| Midnight Slate | `#0f172a` | — | Body text, BibTeX card background |
| Periwinkle Dawn | `#eef2ff` | — | Hero gradient start |
| Lilac Dusk | `#f5f3ff` | — | Hero gradient end |
| Paper White | `#ffffff` | — | Landing card, figure frames, footer |
| Indigo Ink | `#3730a3` | — | Author links |
| Indigo Core | `#6366f1` | — | Superscripts, button gradient end, title bar |
| Indigo Deep | `#4338ca` | — | Button gradient start, TL;DR emphasis |
| Royal Navy | `#1e3a8a` | — | Section title text |
| Venue Indigo | `#312e81` | — | Conference badge text |
| Violet Tail | `#a855f7` | — | Section bar gradient end |
| Slate 800 | `#1e293b` | — | Authors block |
| Slate 600 | `#475569` | — | Affiliations |
| Slate 500 | `#64748b` | — | Equal-contribution note |
| TL;DR Navy | `#284065` | — | TL;DR card text |
| Code Mist | `#e2e8f0` | — | BibTeX text on dark card |

## Tokens — Typography

- **Title family:** Google Sans on `.publication-title` and titles. Substitute: Inter.
- **Body family:** Noto Sans, line-height 1.65.
- **Weights:** 600 buttons and badge, 500 author list, 400 body.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Paper title (`.title.is-2`) | 2.5rem (2rem on mobile) | 600 | Two lines, centered |
| Section title (`.section-title`, `.title.is-4`) | 1.5rem | 600 | `#1e3a8a`, left bar |
| Authors | 1.08rem | 500 | Flex-wrap, gap .65rem 1.5rem |
| Affiliations | 0.95rem | 400 | `#475569` |
| Conference badge | 1rem, letter-spacing 0.08–0.12em | 600 | `#312e81` |
| TL;DR card | 1.1rem | 400 | `#284065` |
| Button | 1.1rem | 600 | White |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Landing card | 32px |
| Content panels | 28px |
| Figure frame (`.framed-image`) | 24px |
| TL;DR card | 20px |
| BibTeX card | 18px |
| Buttons, glows, section bar | 999px |
| Tab buttons | 16px |

- **Shadows:** button `0 28px 50px -26px rgba(79,70,229,.85)` (hover `0 30px 56px -26px rgba(79,70,229,.95)`); landing card `0 10px 13px -12px rgba(15,23,42,.15)`; figure frame `0 45px 90px -65px rgba(30,58,138,.7)`; panels `0 42px 90px -68px rgba(79,70,229,.28)`.
- **Hero padding:** 4.5rem 1.5rem 3.5rem; card padding 3rem 3rem 2.5rem.
- **Layout width:** Bulma `.container.is-max-desktop` (960px, inferred) with media rows up to 1030–1050px.

## Components

- **Gradient pill button** (`.link-block a`): `linear-gradient(135deg, #4338ca, #6366f1)`, white text and icons (images inverted), min-width 140px, padding .85rem 1.6rem, pill radius, indigo glow; hover lifts 3px. Labels: Paper, Code, 🤗 Model, "Follow-up: Register Any Point".
- **Conference badge:** text-only, centered, `NeurIPS 2025` plus a `•`-prefixed `Spotlight` tag (dot `rgba(79,70,229,.65)`).
- **TL;DR card:** max-width 720px, 20px radius, 1px `rgba(79,70,229,.18)` border, highlighted phrase in indigo.
- **Section title:** inline-flex with 1.4rem left padding and a 6px pill bar `linear-gradient(180deg, #6366f1, #a855f7)`.
- **Framed figure:** white, 24px radius, 1px `rgba(99,102,241,.18)` border, long soft navy shadow.
- **BibTeX:** `pre code` on `#0f172a`, text `#e2e8f0`, 18px radius, padding 1.5rem 1.75rem.
- **Viewer tabs:** white chips, 1px `#bbb`, 16px radius, active border `#394b6c`.

## Page Modules

- **Title/author block:** inside the frosted landing card; equal-contribution and affiliation notes (Stanford, NVIDIA Research).
- **Venue badge:** "NeurIPS 2025 • Spotlight" letter-spaced text badge.
- **Link buttons:** Paper, Code, 🤗 Model, follow-up project link.
- **Teaser:** gallery hero below the card (pulled up with −6rem margin).
- **Abstract:** section with left-bar title.
- **Method figure:** "Framework" / "How it works" framed figure.
- **Interactive 3D:** three-canvas point-cloud viewers with rotate controls and tab buttons ("Please make sure hardware acceleration is enabled"), plus noise-space interpolation sliders (jQuery UI).
- **Image-comparison slider:** TwentyTwenty CSS loaded.
- **Results:** multi-part assembly, pairwise registration, generalization carousels; no HTML tables.
- **Concurrent Works** list and **BibTeX** dark card.

## Do's and Don'ts

- Do keep every accent in the indigo family (`#4338ca`, `#6366f1`, `#3730a3`, `#1e3a8a`).
- Do use long, negative-spread shadows that read as glow rather than drop shadow.
- Do frame figures in white with large radii.
- Don't use Bulma's dark `#363636` buttons; they are replaced by the gradient pill.
- Don't add saturated colors outside indigo/violet/sky.
- Don't shrink radii below 16px on cards.

## Surfaces

Three layers: `#f8fafc` page, translucent white cards (0.88–0.92 alpha, blur) with faint slate or indigo borders, and the dark `#0f172a` code card as the single inverted surface.

## Imagery

Rendered point clouds and mesh parts on white, assembly sequences, interactive WebGL canvases. Logos for affiliations are absent; emphasis is on 3D renders.

## Layout

Centered landing card, then stacked `.soft-section` blocks (padding 3.5rem top/bottom) with left-aligned titles and centered media; canvases stack vertically under 600px.

## Agent Prompt Guide

**Quick colors:** page `#f8fafc`, text `#0f172a`, card white, primary gradient `#4338ca → #6366f1`, links `#3730a3`, section titles `#1e3a8a`, bar `#6366f1 → #a855f7`, code card `#0f172a` / `#e2e8f0`.

1. "Build a landing hero: radial gradient `#eef2ff → #ffffff → #f5f3ff` with two blurred circular glows, holding a frosted white card (rgba(255,255,255,.92), 32px radius, 1px rgba(99,102,241,.15) border) containing a Google Sans title and indigo author links."
2. "Make gradient pill buttons: `linear-gradient(135deg,#4338ca,#6366f1)`, white 600-weight text, padding .85rem 1.6rem, shadow `0 28px 50px -26px rgba(79,70,229,.85)`, hover translateY(-3px)."
3. "Create a section title with a 6px vertical pill bar on its left, gradient `#6366f1 → #a855f7`, text `#1e3a8a`."

## Similar Pages

Nerfies-based pages that have been restyled with Tailwind-like indigo tokens; compare NoisyGRPO (slate re-skin) in this batch.

## Quick Start

```css
:root {
  --page: #f8fafc;
  --text: #0f172a;
  --card: rgba(255, 255, 255, 0.92);
  --indigo-deep: #4338ca;
  --indigo: #6366f1;
  --indigo-ink: #3730a3;
  --title-navy: #1e3a8a;
  --violet: #a855f7;
  --muted: #475569;
  --btn-grad: linear-gradient(135deg, #4338ca, #6366f1);
  --btn-glow: 0 28px 50px -26px rgba(79, 70, 229, 0.85);
  --radius-card: 32px;
  --radius-frame: 24px;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL:** https://rectified-pointflow.github.io/
- **Paper:** Rectified Point Flow: Generic Point Cloud Pose Estimation (arXiv 2506.05282), Tao Sun et al., Stanford / NVIDIA Research.
- **Venue:** NeurIPS 2025. The page itself labels it "NeurIPS 2025 • Spotlight"; the batch metadata lists NeurIPS 2025 without the Spotlight tag.
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer says "Website template based on Nerfies and licensed under CC-BY-SA-4.0".
- **Measurement method:** `extract_style.py` counts, manual reading of `index-v5.css` and `pages.css` and the HTML, one rendered screenshot of the hero. WebGL viewers and sliders were not exercised.
