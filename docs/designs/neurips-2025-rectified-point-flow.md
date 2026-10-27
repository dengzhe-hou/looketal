# Rectified Point Flow Indigo Cards — Style Reference

> A product launch for a research paper: a frosted card floating on a lavender haze, indigo pills glowing underneath like stage lights.

**Theme:** light

Measured from the rendered page at 1440×900 in headless Chrome (`computed_style.py`, screenshot and tall capture), then checked against `css/index-v5.css` (a Nerfies stylesheet extended with a card system), `css/pages.css` and Bulma 0.9. Where stylesheet and render disagree, the render is reported. Pixel values are at the 1440px viewport unless a breakpoint is named.

## Overview

A Nerfies/Bulma page rebuilt as a modern SaaS-style landing. The whole page sits in one `section.hero.is-landing` painted with a soft radial gradient (`#eef2ff` → `#ffffff` → `#f5f3ff`), with a blurred indigo circle bleeding in at the top right. The hero is a frosted white card (32px radius, faint indigo hairline, soft shadow) holding a 40px Google Sans title in Bulma charcoal, indigo author links, a letter-spaced "NeurIPS 2025 • Spotlight" badge, four indigo gradient pill buttons with deep coloured under-glow, and a one-line summary in an outlined 20px-radius box. Below, sections are introduced by navy headings with a 6px violet gradient bar at their left. An interactive point-cloud viewer sits in a large white rounded card with lavender pill tabs. In the capture, two of its three panels still show grey "Loading..." overlays. Figures are framed in 24px-radius white cards with long blue shadows. A dark navy BibTeX block and a plain white footer close the page. Document height is about 5,964px.

## First Viewport

Color share of the first 1440×900 viewport: `#ffffff` 24.3% (landing card and gradient centre), `#f2f5ff` 20.6% and `#eff1fd` 9.6% (lavender gradient edges), `#fcfcff` 10.6%, `#fefeff` 9.6%, `#f5f7ff` 9.4%, `#feffff` 8.2% (near-white gradient steps), `#acadd0` 7.7% (indigo glow beneath the buttons and the top-right blob).

Anatomy in DOM order (all centred inside the card):

1. Page backdrop `section.hero.is-landing`, full width and full page height, `radial-gradient(120% 120% at 20% 0%, #eef2ff 0%, #ffffff 55%, #f5f3ff 100%)`; `::before` blob 460px circle at top −160px / right −120px. `.hero-body` padding 72px 24px 56px.
2. Landing card `.landing-card`, 960px wide (x≈240), top y≈72, `rgba(255,255,255,0.92)` with `backdrop-filter: blur(10px)`, 32px radius, padding 48px 48px 40px. 
3. Title `h1.title.is-2.publication-title`, Google Sans 40px/600, `#363636`, line-height 45px, two lines (y=121 to 211). Gap about 28px.
4. Authors `.authors-list`, flex wrap with 1.5rem column gap, Noto Sans 17.28px/500, `#3730a3`; superscripts 0.75em `#6366f1`. Gap about 14px.
5. Affiliations `.authors-affiliations`, 15.2px `#475569`, and "(*equal contribution)" at 14.4px `#64748b` on the same row. Gap about 40px.
6. Badge `.conference-badge`: "NeurIPS 2025" and "Spotlight" in Noto Sans 16px/600, `#312e81`, letter-spacing 0.12em (1.92px), joined by a `•` in `rgba(79,70,229,0.65)`. Gap about 47px.
7. Buttons `.hero-links`, flex wrap, 14.4px gap: Paper, Code, 🤗 Model, Follow-up: Register Any Point; each 40px tall, min-width 140px. Gap about 32px.
8. Summary `.tldr-card`, max-width 720px (rendered about 600px), 20px radius, 1px `rgba(79,70,229,0.18)` border, padding 16px 24px; text 17.6px `#284065`, the bold phrase "poses from assembled shapes." in `#4338ca`. Card ends at y≈618.
9. About 80px of gradient, then the "Abstract" heading (24px/600 `#1e3a8a`, violet bar) at y=699 and the 16px abstract paragraph at y=750, which runs past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Lavender Mist | `#eef2ff` | `.hero.is-landing` gradient stop; `.controls-bar button` fill | Page backdrop top-left; viewer tab and control pills |
| Lilac Mist | `#f5f3ff` | `.hero.is-landing` gradient stop | Page backdrop bottom-right |
| Card White | `rgba(255,255,255,0.92)` | `.landing-card` | Hero card fill |
| Panel White | `rgba(255,255,255,0.88)` | `.gallery-hero .hero-body`, `.framework-hero .hero-body` | Viewer card fill |
| Indigo Deep | `#4338ca` | `.hero-links a` gradient start; `.tldr-card strong` | Pill buttons; bold phrase in the summary |
| Indigo | `#6366f1` | `.hero-links a` gradient end; `.section-title::before`; `sup` | Pill buttons; heading bar top; author superscripts |
| Violet | `#a855f7` | `.section-title::before` gradient end | Heading bar bottom |
| Indigo Glow | `rgba(79,70,229,0.85)` (`#4f46e5`) | `.hero-links a` box-shadow | Coloured under-glow of the pills; blob and badge bullet use the same hue at 0.25 and 0.65 |
| Author Indigo | `#3730a3` | `.authors-list .author a`; `.controls-bar button` | Author names; viewer tab labels |
| Badge Navy | `#312e81` | `.conference-badge` | "NeurIPS 2025 • Spotlight" |
| Heading Navy | `#1e3a8a` | `.section-title` | Abstract, Framework, Multi-part Shape Assembly and other section heads |
| Title Charcoal | `#363636` | Bulma `.title` | Paper title, `is-6` sub-heads, Concurrent Works head |
| Slate Ink | `#0f172a` | `body` color; `#BibTeX pre code` background | Body text; BibTeX block fill |
| Summary Ink | `#284065` | `.tldr-card`, `.assembled-subcaption` | Summary text, viewer sub-captions |
| Affiliation Slate | `#475569` | `.authors-affiliations` | Affiliation row |
| Note Slate | `#64748b` | `.authors-equal` | Equal-contribution note |
| Hairline Indigo | `rgba(99,102,241,0.15)` | `.landing-card` border | Hero card border; framed images use 0.18 |
| Hairline Slate | `rgba(148,163,184,0.25)` | `.gallery-hero .hero-body` border | Viewer card border; BibTeX border at 0.35 |
| Code Text | `#e2e8f0` | `#BibTeX pre code` | BibTeX text |
| Tab Hover | `#c7d2fe` | `.controls-bar button:hover` | Viewer pill hover fill (label `#1d4ed8`) |
| Active Ring | `#394b6c` | `.tab-button.active` | 1px border on the selected object tab |
| Loading Grey | `rgba(245,245,245,0.85)` | `.viewer .loading` | Overlay on viewer panels before the point cloud loads |
| Caption Grey | `#333333` | `.assembled-caption`, `.viewer .loading` | "Condition" / "Generation" viewer captions, "Loading..." text |
| Sky Shadow | `rgba(59,130,246,0.35)` (`#3b82f6`) | `.gallery-hero .hero-body` box-shadow | Long shadow under the viewer card |
| Page Base | `#f8fafc` | `body` background | Visible only below the landing section, behind the footer edge |

## Tokens — Typography

- **Declared:** `body { font-family: 'Noto Sans', sans-serif; line-height: 1.65 }`; `.publication-title` in `'Google Sans', sans-serif`. Viewer captions and controls use `sans-serif`, Arial or the system UI stack.
- **Rendered:** Google Sans 400 and Noto Sans 400 loaded; 500/600 weights are synthesized. MathJax fonts (MJXTEX) render the Framework formulas. Icons from the Font Awesome JS kit (SVG). Substitute for Google Sans: Outfit, whose round geometry and tight spacing match at 600.
- **Mono:** Bulma `monospace` in the BibTeX block.

| Role | Selector | Size | Weight | Line height | Colour |
|---|---|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px | 600 | 45px | `#363636` |
| Section head | `.title.is-4.section-title` | 24px | 600 | 27px | `#1e3a8a` |
| Sub-head | `h2.title.is-6` | 16px | 600 | 18px | `#363636`, left |
| Authors | `.authors-list` | 17.28px (1.08rem) | 500 | 28.5px | `#3730a3` |
| Affiliations | `.authors-affiliations` | 15.2px | 400 | 1.65 | `#475569` |
| Badge | `.conference-badge`, `.conference-name`, `.spotlight-tag` | 16px | 600 | 26.4px | `#312e81`, letter-spacing 0.12em |
| Pill label | `.hero-links .link-block a` | 16px (Bulma `is-normal`) | 600 | 24px | `#ffffff` |
| Summary | `.tldr-card` | 17.6px | 400 | 29px | `#284065` |
| Body | `body`, `p` | 16px | 400 | 26.4px | `#0f172a` |
| Viewer pills | `.gallery-hero .controls-bar button` | 13.6px | 600 | normal | `#3730a3`, system UI font |
| Viewer caption | `.assembled-caption` | 17.6px | 600 | 1.8 | `#333333` |
| BibTeX | `#BibTeX pre code` | 14px | 400 | 23.1px | `#e2e8f0` |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Landing card | 32px |
| Viewer and framework cards (`.gallery-hero .hero-body`) | 28px |
| Framed figures `.framed-image` | 24px |
| Summary box `.tldr-card` | 20px |
| BibTeX code, `.vis-card`, controls bar | 18px |
| Pill buttons, viewer pills, heading bar | 999px / Bulma `is-rounded` 290486px |
| Canvases in the interpolation sliders | 8px |
| Viewer panels | 6px |

- **Shadows:** landing card `0 10px 13px -12px rgba(15,23,42,0.15)`; pills `0 28px 50px -26px rgba(79,70,229,0.85)`, hover `0 30px 56px -26px rgba(79,70,229,0.95)`; viewer card `0 40px 90px -65px rgba(59,130,246,0.35)`; `.vis-card` `0 35px 70px -55px rgba(30,64,175,0.4)`; framed figures `0 45px 90px -65px rgba(30,58,138,0.7)`. All shadows are long and offset downward, so cards seem to float.
- **Borders:** 1px translucent indigo or slate hairlines on every card (see Tokens — Colors).
- **Motion:** pills lift `translateY(-3px)`; viewer pills lift 1px with fill `#c7d2fe`; both 0.2s ease-in-out.

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px at ≥1024px; content columns `is-five-fifths` (full width). The landing card is the full 960px; the viewer controls `.vis-card` is widened to 110% with −5% margin.
- **Hero:** `.hero.is-landing .hero-body` padding 72px 24px 56px; card padding 48px 48px 40px; `.landing-intro` stacks its children with a 24px gap.
- **Sections:** `.page-stack` margin-top 56px with a 56px gap; each `.section.soft-section` has 56px top and bottom padding, nudged by inline negative margins (−2rem, −6rem, −80px, −30px) to tighten the stack.
- **Viewer:** `.viewers-container` max 1050px, flex wrap, 20px gap, panels 320×320px; controls bar max 1030px with object tabs on the left and Rotate / Trajectories / Pause on the right.
- **Figures:** full column width inside `.framed-image`; interpolation sliders put three canvases in a row with 1rem gaps and a 400px-max range slider below.

| Breakpoint | Container | Card padding | Body size | Title size | Grid change |
|---|---|---|---|---|---|
| ≥1216px | 960px | 48px 48px 40px | 16px | 40px | viewer panels side by side |
| 1024–1215px | 960px | 44.8px 40px 35.2px | 16px | 40px | same |
| 769–1023px | fluid, 24px gutters | 44.8px 40px 35.2px; hero-body 56px 24px 48px; sections 48px | 16px | 40px | viewer panels wrap |
| 481–768px | fluid | 38.4px 28px 32px; page-stack gap 40px | 16px | 40px | Bulma columns stack; rotate controls drop below tabs at ≤670px |
| ≤480px | fluid | 16px 28px | 16px | 32px | badge stacks vertically, bullet hidden; pills 0.8rem; authors 0.85rem; canvases stack at ≤600px |

## Components

- **Landing card.** `rgba(255,255,255,0.92)` fill, `backdrop-filter: blur(10px)`, 32px radius, 1px `rgba(99,102,241,0.15)` border, shadow `0 10px 13px -12px rgba(15,23,42,0.15)`, padding 48px 48px 40px, all content centred.
- **Indigo pill.** `a.external-link.button.is-normal.is-rounded` inside `.hero-links`: `linear-gradient(135deg, #4338ca, #6366f1)`, no border, white 16px/600 label, icon left with 8px gap (Font Awesome `fa-file-pdf`, `fa-github`, the 🤗 emoji, an inverted SVG external-link icon), padding 13.6px 25.6px, min-width 140px, pill radius, glow `0 28px 50px -26px rgba(79,70,229,0.85)`; hover lifts 3px with a stronger glow; focus ring 2px `rgba(99,102,241,0.65)` offset 4px.
- **Venue badge.** Plain text, no fill: 16px/600 `#312e81`, letter-spacing 0.12em, with a `•` pseudo-element bullet in `rgba(79,70,229,0.65)` before "Spotlight".
- **Summary box.** `.tldr-card`: transparent fill, 1px `rgba(79,70,229,0.18)` border, 20px radius, padding 16px 24px, 17.6px `#284065`, key phrase bold in `#4338ca`.
- **Section head with bar.** `.section-title`: inline-flex, padding-left 22.4px, 24px/600 `#1e3a8a`; `::before` a 6px-wide full-height bar, 999px radius, `linear-gradient(180deg, #6366f1, #a855f7)`.
- **Viewer card.** `.gallery-hero .hero-body`: `rgba(255,255,255,0.88)`, 28px radius, padding 48px 40px, 1px `rgba(148,163,184,0.25)` border, shadow `0 40px 90px -65px rgba(59,130,246,0.35)`. Inside: "Condition" and "Generation" captions with outlined pill sub-captions, three 320px canvas panels, a centred note, then pill controls in `#eef2ff` with `#3730a3` 13.6px/600 labels, padding 8.8px 22.4px; the active tab adds a 1px `#394b6c` border.
- **Loading overlay.** `.viewer .loading`: `rgba(245,245,245,0.85)` full-panel overlay, `#333333` 17.6px "Loading..." text. It is visible in the capture on two panels, which leaves two large grey squares in the viewer.
- **Framed figure.** `img.framed-image`: white fill, 24px radius, 1px `rgba(99,102,241,0.18)` border, shadow `0 45px 90px -65px rgba(30,58,138,0.7)`.
- **BibTeX block.** `#BibTeX pre code`: `#0f172a` fill, `#e2e8f0` 14px monospace, 18px radius, padding 24px 28px, 1px `rgba(148,163,184,0.35)` border.
- **Footer.** Bulma `.footer` overridden to white with 32px top padding; small credit to Nerfies and a ClustrMaps widget.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / author block | Yes | Frosted landing card |
| Venue badge | Yes | Letter-spaced navy text with bullet ("NeurIPS 2025 • Spotlight") |
| Link buttons | Paper, Code, Model, Follow-up | Indigo gradient pills with glow |
| TL;DR | Yes | Outlined 20px-radius summary box |
| Abstract | Yes | Section head with violet bar, left-aligned text |
| Interactive 3D viewer | Yes, non-standard | Point-cloud canvases in a white card with pill tabs and rotate/trajectory/pause toggles |
| Method figure | Framework | Framed figure plus MathJax-typeset lead paragraph |
| Results | Multi-part assembly and pairwise registration figures; noise-space interpolation sliders | Framed figures, canvas sliders |
| Results table | Absent from the source | |
| Concurrent works | Yes | Left-aligned section with link list |
| BibTeX | Yes | Dark navy code block |
| Video, carousel | Absent (bulma-carousel is loaded but not used) | |

## Adapting to Other Content

- **More authors:** `.authors-list` is a flex-wrap row with 10.4px row gap and 24px column gap, so extra names wrap into centred rows inside the card without change.
- **More buttons:** pills already wrap with a 14.4px gap; keep every pill the same gradient and glow rather than introducing secondary colours.
- **A results table:** put it inside a white `.framed-image`-style card (24px radius, indigo hairline, long blue shadow), headers 16px/600 `#1e3a8a`, body 16px `#0f172a`, best values bold `#4338ca`.
- **Video galleries:** use 24px-radius framed tiles in a two- or three-column grid inside a `.gallery-hero` white card.
- **News:** a second outlined `.tldr-card` under the summary, left-aligned, with dates in `#4338ca` 600.

## Do's and Don'ts

- Do float everything on the lavender radial backdrop; never set a plain white page.
- Do keep one indigo family (`#4338ca`, `#6366f1`, `#3730a3`, `#312e81`, `#1e3a8a`) for every accent, plus violet `#a855f7` only in the heading bar.
- Do give cards 1px translucent hairlines and long, soft, downward shadows.
- Do mark every section head with the 6px gradient bar.
- Don't ship the viewer with panels still loading in the first screenful; preload or show a poster frame instead of the grey overlay.
- Don't use dark buttons; the only dark surface is the BibTeX block.

## Surfaces

Three levels: the lavender radial backdrop with blurred indigo and sky blobs; translucent white cards (0.92 for the hero, 0.88 for viewer and framework) with hairline borders; and one dark navy code surface. The summary box and badge have no fill.

## Imagery

Coloured point-cloud renders (furniture parts, scanned objects) in framework and result figures, interactive WebGL point clouds in the viewer, and three-canvas interpolation strips. Figures are white-background PNGs inside framed cards.

## Layout

A centred 960px column of stacked cards and sections on a full-page gradient. The viewer card is the only element wider than the column (its controls run at 110%).

## Agent Prompt Guide

Quick colors: backdrop `#eef2ff` → `#ffffff` → `#f5f3ff`, card `rgba(255,255,255,0.92)`, pills `#4338ca` → `#6366f1`, authors `#3730a3`, badge `#312e81`, headings `#1e3a8a` with bar `#6366f1` → `#a855f7`, text `#0f172a`, summary `#284065`, code `#0f172a` with `#e2e8f0` text.

1. "Create a landing card on a `radial-gradient(120% 120% at 20% 0%, #eef2ff 0%, #ffffff 55%, #f5f3ff 100%)` page: 960px wide, `rgba(255,255,255,0.92)`, 32px radius, 1px `rgba(99,102,241,0.15)` border, shadow `0 10px 13px -12px rgba(15,23,42,0.15)`, padding 48px 48px 40px; centred 40px/600 Google Sans title in `#363636`, 17.28px/500 author links in `#3730a3`, and a 16px/600 `#312e81` badge with 0.12em letter-spacing."
2. "Make pill buttons: `linear-gradient(135deg, #4338ca, #6366f1)`, white 16px/600 label with left icon, padding 13.6px 25.6px, min-width 140px, fully rounded, shadow `0 28px 50px -26px rgba(79,70,229,0.85)`; on hover translateY(-3px)."
3. "Style section heads: 24px/600 `#1e3a8a`, padding-left 22.4px, with a 6px-wide full-height rounded bar `linear-gradient(180deg, #6366f1, #a855f7)` as a `::before`."

## Similar Pages

Nerfies-derived Bulma pages share the skeleton, but this one replaces Bulma's flat look with glass cards and gradient pills. In this NeurIPS 2025 batch, Time-IMM uses colourful pills and a tinted abstract band in a similar modern idiom, and ThermalGen uses a tinted TL;DR callout.

## Quick Start

```css
:root {
  --backdrop: radial-gradient(120% 120% at 20% 0%, #eef2ff 0%, #ffffff 55%, #f5f3ff 100%);
  --card: rgba(255, 255, 255, 0.92);
  --card-border: rgba(99, 102, 241, 0.15);
  --card-shadow: 0 10px 13px -12px rgba(15, 23, 42, 0.15);
  --pill: linear-gradient(135deg, #4338ca, #6366f1);
  --pill-glow: 0 28px 50px -26px rgba(79, 70, 229, 0.85);
  --bar: linear-gradient(180deg, #6366f1, #a855f7);
  --title: #363636;
  --heading: #1e3a8a;
  --author: #3730a3;
  --badge: #312e81;
  --text: #0f172a;
  --summary: #284065;
  --code-text: #e2e8f0;
  --font-display: 'Google Sans', 'Outfit', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-card: 32px;
  --radius-panel: 28px;
  --radius-figure: 24px;
}
.section-title { position: relative; padding-left: 22.4px; color: var(--heading); }
.section-title::before { content: ""; position: absolute; left: 0; top: 0; width: 6px; height: 100%; border-radius: 999px; background: var(--bar); }
```

## Provenance

- **URL:** https://rectified-pointflow.github.io/
- **Paper:** Rectified Point Flow: Generic Point Cloud Pose Estimation (arXiv 2506.05282), Tao Sun, Liyuan Zhu, Shengyu Huang, Shuran Song, Iro Armeni (Stanford University, NVIDIA Research).
- **Venue:** NeurIPS 2025; the page badge reads "NeurIPS 2025 • Spotlight".
- **Selection reason:** existing entry; the arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer says the website template is based on Nerfies.
- **Evidence used:** `computed_style.py` render at 1440×900 with first-viewport color share, the 1440 screenshot and tall capture, `css/index-v5.css`, `css/pages.css` and the page markup. Captured 2026-10-28.
