# StreamSplat Pastel Glow — Style Reference

> A soft-launch SaaS page dipped in sunrise pastels, with a cyan-to-violet ribbon tying every accent together.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's `static/css/index.css`, and Bulma 0.9.4 from jsDelivr (loaded first and overridden by `index.css`). Google Sans 600 and Noto Sans 400/700 load, so the declared faces render; Noto Sans has no 600 file, so `font-weight: 600` headings render with the 700 face. Below-fold blocks use a `.fade-in` class that slides them up 30px as they scroll in. Color share is measured on the first viewport.

## Overview

The hero is a full-width pastel wash (ice blue to lilac to blush, at 135°) under a white Bulma navbar with a soft shadow. Centered on it: a gradient pill tag "🏆 ICLR 2026" (cyan #00b4d8 to violet #7209b7), a two-line Google Sans title whose first word "StreamSplat" carries the same gradient, sky-blue author links, grey affiliations, and three charcoal pill buttons (arXiv, Code, 💾 Checkpoints). Below, on white, a 912px teaser figure with 12px corners and a large soft shadow gently floats up and down. The rest of the page alternates white and #f8f9fb sections: an abstract card with a gradient left bar, four white icon feature cards with emoji, video comparisons with gradient dataset badges and scene pills, a method figure and numbered gradient-circle contributions, tabbed results with gradient-header tables, dashed "Future Directions" cards, and a dark Catppuccin-style BibTeX block.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 27.8% (navbar and lower page), lilac #f4ebf9 19.0%, periwinkle #ececfc 15.6% and ice #eaf2fd 11.5% (the hero gradient), mauve-grey #b9b0b7 13.2% (teaser photos), warm whites #f9f9f7 7.6% and #fffcf3 4.9% (teaser panels). The gradient tag, title word and charcoal buttons are each under 1%.

Anatomy in DOM order:

1. **Navbar** — `nav.navbar.is-white`, 52px, #ffffff, shadow `0 2px 12px rgba(0,0,0,0.06)`. Brand "StreamSplat" 17.6px / 700 with the cyan-violet gradient text at left; centered items Abstract, Videos, Method, Results, BibTeX in Noto Sans 16px #0a0a0a, padding 8px 12px; GitHub icon at the far right.
2. **Hero band** — `section.hero.hero-gradient-bg`, y=52–479, `linear-gradient(135deg, #f0f7ff 0%, #f5f0ff 50%, #fff0f5 100%)` plus two drifting 6% radial glows.
3. **Tag** — `span.tag.is-medium.is-rounded`, "🏆 ICLR 2026", Noto Sans 15.2px / 600 (700 face), #ffffff on `linear-gradient(135deg, #00b4d8, #7209b7)`, padding 8px 20px, pill (y=100–130). Gap 16px.
4. **Title** — `h1.title.is-2.publication-title`, Google Sans 40px / 600, line-height 1.25, #363636, centered on two lines; "StreamSplat" in gradient text (y=146–246). Margin-bottom 24px.
5. **Authors** — `.is-size-5.publication-authors`, 20px Noto Sans, links #209cee (`hsl(204,86%,53%)`), superscripts, margin-top 16px (y=276–303).
6. **Affiliations** — `.is-size-6.publication-authors`, 16px Noto Sans, #666666 (inline style), superscript numbers, one line, margin-top 8px (about y=318–342).
7. **Buttons** — three `a.external-link.button.is-dark.is-rounded`, 40px tall, #363636 fill, #ffffff Noto Sans 16px, padding 7px 20px, pill, 4px margins, icon left (y=391–431). Hero body bottom padding 32px.
8. **Teaser** — `img.teaser-image.floating`, 912×541px at y=505, radius 12px, shadow `0 8px 32px rgba(0,0,0,0.12)`, floating ±8px over 4s; caption "Figure 1. …" below in 14px grey with "StreamSplat" in gradient bold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Stream Cyan | #00b4d8 | gradient start | tag, title word, nav brand, section-title underline, active scene pill, active results tab, table header strip, contribution circles, "ours" row bar, footer icon hover, tab hover border and text |
| Splat Violet | #7209b7 | gradient end | same gradient as above; scrollbar thumb hover |
| Ice Wash | #f0f7ff | hero stop 0% | hero band left |
| Lilac Wash | #f5f0ff | hero stop 50% | hero band middle |
| Blush Wash | #fff0f5 | hero stop 100% | hero band right |
| Charcoal | #363636 | Bulma `$dark` / title | link buttons, title, section titles |
| Body Grey | #4a4a4a | Bulma body | body text, abstract |
| Heading Grey | #333333 | (literal) | feature-card and subsection headings, table header text, footer icons |
| Soft Grey | #666666 | (literal) | affiliations line, feature-card text, subsection descriptions, contribution text, inactive scene pill text |
| Caption Grey | #555555 | (literal) | video and figure captions |
| Sky Link | #209cee | Bulma link | author links |
| Alt Band | #f8f9fb | `.section-alt` | Key Features, Method, Quantitative Results, Future Directions bands |
| Caption Strip | #fafafa | (literal) | video captions, scene-pill bar, figure captions, table notes, footer |
| Pill Grey | #e8e8e8 | `.scene-pill` | inactive scene pills (hover #d0d0d0) |
| Rule Greys | #dddddd, #e9ecef, #eeeeee, #f0f0f0, #cccccc | (literals) | results-tab border, thead bottom rule (2px), scene-pill bar rule, table row rules, dashed future-card border |
| Table Head | #f8f9fa | `.results-table thead th` | table header row |
| Best Red | #dd0000 | `.best` | best value in tables (bold) |
| Ours Hover | #f8faff | row hover | table row hover |
| Code Night | #1e1e2e | `#BibTeX pre` | BibTeX block background |
| Code Lavender | #cdd6f4 | `#BibTeX pre` | BibTeX text, copy button text |
| DAVIS Orange | #f97316 → #ef4444 | `.dataset-badge.davis` | DAVIS badge gradient |
| RE10K Blue | #3b82f6 → #6366f1 | `.dataset-badge.re10k` | RE10K badge gradient |
| Tracking Green | #10b981 → #059669 | `.dataset-badge.tracking` | Tracking badge gradient |

Declared but not visible: `.publication-venue` (#f72585) and `.gradient-text-alt` (#7209b7 → #f72585) and `.speed-badge` are not used in the markup.

## Tokens — Typography

- **Headings:** `'Google Sans', sans-serif` on `.title.is-1/.is-2`, `.publication-title`, card headings and table header strips; renders Google Sans 600. Substitute: Product Sans or Outfit (similar round geometric caps).
- **Body:** `'Noto Sans', sans-serif`; renders Noto Sans 400 and 700. Section titles (`h2.title.is-3`, weight 600) render with the 700 face. Substitute: Open Sans.
- **Scene pills:** native `button` font (Segoe UI on Windows, SF on macOS), 13.6px / 500.
- **Code:** browser monospace, 14.08px, line-height 1.6.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px / 600 / 1.25 (Google Sans) |
| Section title | `h2.title.is-3` | 32px / 700 rendered / 1.125 (Noto Sans) |
| Sub-section title | `h2.title.is-4` | 24px / 700 rendered |
| Video subsection | `.video-subsection-title` | 20px / 600 |
| Card heading | `.feature-card h3` | 18.4px / 600 (Google Sans), #333333 |
| Authors | `.publication-authors` | 20px / 400 |
| Body | `body` / `.content` | 16px / 400 / 1.5 |
| Feature text | `.feature-card p` | 15.2px / 1.6, #666666 |
| Table | `.results-table` | 14.72px; header 14.08px / 600 |
| Tag | `.tag.is-medium` | 15.2px / 600 |
| Dataset badge | `.dataset-badge` | 12px / 700, uppercase, 0.5px tracking |
| Caption | `.figure-caption`, video caption | 14.4–14.7px, #555555 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link buttons, tag, results tabs | pill (9999px / 100px) |
| Teaser, video cards, result figures, scene-pill bar, BibTeX | 12px radius |
| Feature cards, abstract card, table containers, pipeline figure, future cards | 16px radius |
| Scene pills | 20px radius |
| Dataset badges | 6px radius |
| Shadows | teaser `0 8px 32px rgba(0,0,0,0.12)` (hover `0 12px 48px rgba(0,0,0,0.18)` with scale 1.01); cards `0 4px 20px rgba(0,0,0,0.06–0.08)`; feature hover `0 12px 40px rgba(0,0,0,0.12)` with lift 6px; table container `0 4px 24px rgba(0,0,0,0.08)` |
| Abstract card | white, padding 2rem 2.5rem, 4px left border painted with the cyan-violet gradient via `border-image` (that edge renders square) |
| Feature card border | 1px rgba(0,0,0,0.04) |
| Future card | 2px dashed #cccccc, pale ice-to-lilac fill |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px at ≥1024 (x=240–1200 at 1440); abstract column `is-four-fifths` (about 768px).
- **Hero:** navbar 52px; hero body padding 48px 24px 32px; band height 427px at 1440.
- **Sections:** padding 48px 24px; alternate sections #f8f9fb.
- **Teaser:** 95% of the column (912px), centered.
- **Feature cards:** Bulma columns, 4 × 228px with 12px gutters.
- **Video grid:** 2 columns, 24px gap; showcase videos 16:9 or 1764:1080.
- **Results:** tab row centered with 8px gaps, then a full-width table card.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px | 40px | 4 feature columns, 2-column video grid |
| 769–1023px | 24px (section padding) | 16px | 40px | none |
| ≤768px | 16px in the hero, 24px in sections | 16px | 24px (`!important`) | columns stack, video grid one column, navbar collapses to a burger, abstract padding 1.25rem 1.5rem, feature padding 1.5rem 1.25rem |

## Components

- **Gradient tag:** Bulma `.tag.is-medium.is-rounded`, `linear-gradient(135deg, #00b4d8, #7209b7)`, #ffffff 15.2px / 600, padding 8px 20px, leading emoji.
- **Charcoal pill button:** Bulma `.button.is-dark.is-rounded`, #363636, #ffffff 16px, padding 7px 20px, Font Awesome or emoji icon left; hover lifts 2px with `0 4px 15px rgba(0,0,0,0.15)`.
- **Floating teaser:** 12px radius, deep soft shadow, 4s float animation, hover scale 1.01 with a deeper shadow.
- **Abstract card:** white box, 16px radius on the right side, padding 2rem 2.5rem, `0 4px 24px rgba(0,0,0,0.06)`, gradient left bar; gradient-text product name and bold key terms inside.
- **Feature card:** white, 16px radius, padding 2rem 1.5rem, 1px rgba(0,0,0,0.04) border, 40px emoji icon (⚡ 📷 🌊 ♾️), Google Sans 18.4px heading #333333, 15.2px #666666 text, centered; hover lift 6px.
- **Dataset subsection title:** 20px / 600 #333333 row with a 12px uppercase gradient badge (DAVIS orange-red, RE10K blue-indigo, Tracking green) and a 15.2px #666666 description.
- **Scene switcher:** #fafafa bar with 12px top corners and a 1px #eeeeee bottom rule; pills #e8e8e8 with #666666 13.6px / 500 text, 20px radius; active pill gets the gradient, #ffffff text and `0 2px 8px rgba(114,9,183,0.25)`; video below with 12px bottom corners and a play-icon flash.
- **Contribution item:** 44px gradient circle with a white bold number and violet glow, then a Google Sans heading and #666666 text.
- **Results tabs:** pill buttons, 2px #dddddd border, white, #555555 14.7px / 600; hover border and text #00b4d8; active filled with the gradient.
- **Results table card:** white, 16px radius, shadow; a gradient header strip with Google Sans 17.6px / 600 white title; `thead` #f8f9fa with 2px #e9ecef rule; centered cells, #f0f0f0 row rules; best values bold #dd0000, second-best underlined; "ours" row washed with 8% cyan-violet and a 3px gradient bar; row hover #f8faff; #fafafa note strip.
- **BibTeX:** #1e1e2e block, #cdd6f4 text, 12px radius, padding 1.5rem, translucent copy button top right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | Yes | white Bulma navbar with gradient brand and centered anchors |
| Venue tag | Yes | gradient pill with trophy emoji |
| Title / authors / affiliations | Yes | Google Sans title with gradient product name |
| Link buttons | Yes | charcoal pills, including a Checkpoints link |
| Teaser | Yes | floating pipeline figure with caption |
| Abstract | Yes | white card with gradient left bar |
| Feature highlights | Yes | four emoji icon cards on a pale band |
| Video comparisons | Yes | dataset badges, scene pills, 2-up video cards |
| Method | Yes | pipeline figure plus numbered contributions, architecture in a `details` toggle |
| Qualitative results | Yes | tabbed figure cards with caption strips |
| Results tables (HTML) | Yes | tabbed gradient-header tables |
| Future work | Yes | three dashed placeholder cards |
| BibTeX | Yes | dark code block with copy button |
| Footer | Yes | #fafafa, icon links, Academic Project Page Template credit |

## Adapting to Other Content

- **More authors:** keep the 20px sky-blue links on one centered block; at three or more lines, drop to Bulma `is-size-5` (20px stays) and keep affiliations on their own 16px line.
- **Results table:** reuse the gradient-header table card; one table per tab, best in bold #dd0000, your row with the 8% gradient wash.
- **Long publication or news list:** a white card on the #f8f9fb band, each entry with a small gradient badge for the venue and a 15.2px #666666 description.
- **No video:** keep the dataset-badge subsection titles over image comparison cards with #fafafa caption strips.
- **Award or oral:** add it inside the gradient tag rather than as a second badge.

## Do's and Don'ts

- Do use the one cyan-to-violet gradient for every accent (tag, product name, active states, bars).
- Do keep link buttons charcoal and pill-shaped; color goes on tags and states, not on primary links.
- Do alternate white and #f8f9fb sections to pace the long page.
- Don't add more pastel hues to the chrome; dataset badges are the only other colors.
- Don't combine `border-image` with radius if you want a rounded accent bar; use a pseudo-element instead.
- Don't make the floating animation larger than 8px.

## Surfaces

Pastel gradient hero band; white page; #f8f9fb alternate bands; white cards with soft shadows; #fafafa caption strips and footer; one dark #1e1e2e code block.

## Imagery

A pipeline teaser with video frames and colored Gaussian blobs, side-by-side reconstruction videos (DAVIS, RE10K), 3D point-tracking videos, a method diagram, and paper figures in white cards.

## Layout

Navbar, pastel hero, then a 960px centered column through alternating bands. Rendered height about 9,200px.

## Agent Prompt Guide

Quick colors: gradient #00b4d8 → #7209b7, hero wash #f0f7ff → #f5f0ff → #fff0f5, title #363636, body #4a4a4a, headings #333333, muted #666666, author link #209cee, alt band #f8f9fb, strip #fafafa, code #1e1e2e / #cdd6f4.

1. "Build a pastel hero: full-width band with linear-gradient(135deg, #f0f7ff, #f5f0ff, #fff0f5); centered pill tag with linear-gradient(135deg, #00b4d8, #7209b7), #ffffff 15.2px/600 text, padding 8px 20px; a Google Sans 40px/600 title in #363636 whose product name uses the same gradient as text fill; 20px #209cee author links; three #363636 pill buttons with #ffffff 16px labels and padding 7px 20px."
2. "Create four feature cards in a row: #ffffff, 16px radius, padding 2rem 1.5rem, 1px rgba(0,0,0,0.04) border, box-shadow 0 4px 20px rgba(0,0,0,0.06); a 40px emoji, an 18.4px Google Sans 600 #333333 heading and 15.2px #666666 text, centered; hover translateY(-6px) and shadow 0 12px 40px rgba(0,0,0,0.12). Place them on a #f8f9fb band."
3. "Make a results table card: #ffffff, 16px radius, shadow 0 4px 24px rgba(0,0,0,0.08); header strip filled with linear-gradient(135deg, #00b4d8, #7209b7) and a #ffffff Google Sans 17.6px/600 title; thead #f8f9fa with #333333 14px/600 text; centered cells; best values bold #dd0000; row hover #f8faff."

## Similar Pages

- Academic Project Page Template (Nerfies-derived) pages that add a pastel hero and gradient accents.
- Modern "landing page" research sites with feature-card rows and tabbed result tables.

## Quick Start

```css
:root {
  --grad-a: #00b4d8;
  --grad-b: #7209b7;
  --gradient: linear-gradient(135deg, var(--grad-a), var(--grad-b));
  --hero-bg: linear-gradient(135deg, #f0f7ff 0%, #f5f0ff 50%, #fff0f5 100%);
  --title: #363636;
  --text: #4a4a4a;
  --heading: #333333;
  --muted: #666666;
  --link: #209cee;
  --band: #f8f9fb;
  --strip: #fafafa;
  --code-bg: #1e1e2e;
  --code-fg: #cdd6f4;
  --best: #dd0000;
  --font-heading: 'Google Sans', 'Outfit', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-card: 16px;
  --radius-media: 12px;
  --container: 960px;
}
```

## Provenance

- **URL:** https://streamsplat3d.github.io/
- **Paper:** StreamSplat: Towards Online Dynamic 3D Reconstruction from Uncalibrated Video Streams (arXiv 2506.08862), Zike Wu, Qi Yan, Xuanyu Yi, Lele Wang, Renjie Liao.
- **Venue:** ICLR 2026 (tag on the page).
- **Selection reason:** the arXiv comment reads "Accepted by ICLR 2026" and links the page; chosen for its pastel gradient hero, gradient wordmark, dark pill buttons, framed teaser, accent-bar abstract card, four icon feature cards and labeled scene toggles.
- **Template credit:** footer says the page was built using the Academic Project Page Template, adopted from the Nerfies project page.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `static/css/index.css`, page HTML; 2026-10-28.
