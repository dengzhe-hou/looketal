# VIST3A Slate Mosaic — Style Reference

> A gallery wall of tiny generated worlds, hung under crisp slate type and a single pink tick.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, the page's `static/css/index.css` (a Tailwind-like token block layered over Bulma) and an inline `<style>` block for the 3D viewer thumbnails. Inter 400–800 loads from Google Fonts, so declared and rendered faces match. Where Bulma and `index.css` disagree, the render is reported: section titles inside `.hero.is-light` bands render at rgba(0,0,0,0.7) from Bulma, not the declared #1e293b. Color share is measured on the first viewport.

## Overview

A white page with no navigation bar. The header is a centered stack: a heavy three-line Inter ExtraBold title in slate (#1e293b), an "ICLR 2026 (Oral)" line in the same weight, blue author names at 20px / 600, an affiliation line, and two compact slate buttons (Paper, GitHub) with 12px corners and a soft shadow. The teaser is the hero of the page: a 912px square-cornered video showing an 8-column mosaic of generated 3D scenes (sofas, coastlines, a golden retriever, a red hydrant, cakes, masks) playing at once. A plain caption and a pale-blue bold TL;DR strip follow. Lower sections sit on #f8fafc bands with hairline rules top and bottom, each headed by a centered 32px bold title with a 60px pink-to-coral gradient underline, then justified slate-grey text with bold key phrases, interactive 3D Gaussian splat viewers with thumbnail pickers, a baseline comparison carousel, a poster and a BibTeX block.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 74.6%, dark slate #181c22 7.4% (title text and dark mosaic tiles), brown #633b2f 5.5% and taupe #94867c 5.5% (interior scenes in the mosaic), blue-grey #bcc5cf 3.6%, cream #f0e8dd 2.0%. Author blue and button slate are each under 1%.

Anatomy in DOM order (centered on x=720; hero body padding 64px 24px; column 960px):

1. **Title** — `h1.title.is-1.publication-title`, Inter 48px / 800, line-height 1.1, #1e293b, centered, three lines (y=64–222). Margin-bottom 32px.
2. **Venue** — `h1.title.is-4.publication-title`, "ICLR 2026 (Oral)", Inter 24px / 800, #1e293b (y=254–280). Margin-bottom 32px; authors start 40px below.
3. **Authors** — `.is-size-5.publication-authors a`, Inter 20px / 600, #2563eb, superscripts in #1e293b, two centered lines, line-height 1.6 (y=320–380).
4. **Affiliations** — second `.is-size-5.publication-authors`, "ETH Zurich¹, Google²", 20px / 400, #1e293b (about y=410–440). Margin-bottom 24px.
5. **Buttons** — two `a.external-link.button.is-dark`, 40px tall, #1e293b fill, #ffffff Inter 16px / 600, padding 7px 20px, 12px radius, margins 8px 4px, shadow `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`, icon left (y=488–528).
6. **Teaser video** — `section.hero.teaser video`, 912×684px at y=644 (x=264–1176), square corners, no shadow; an 8-column grid of generated scenes with native controls. Teaser body padding 32px top, 64px bottom.
7. **Caption** — `h2.subtitle`, 20px / 400, #4a4a4a, centered (y=1335). Margin-bottom 24px.
8. **TL;DR** — `h2.subtitle.has-background-info-light.has-text-weight-bold.p-3`, 20px / 700, #0a0a0a on #eef6fc, padding 12px, centered, square corners (y=1384–1458).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | `--background-primary` | page, comparison section, thumbnail buttons |
| Slate Ink | #1e293b | `--text-primary` | title, venue, affiliations, buttons fill, code text |
| Royal Blue | #2563eb | `--primary-color` | author links, button hover fill, copy button, scroll-to-top button, footer links, loader |
| Deep Blue | #1d4ed8 | `--primary-hover` | author link hover, copy button hover |
| Slate Grey | #64748b | `--text-secondary` | justified body text, footer text |
| Mist Band | #f8fafc | `--background-secondary` | `.hero.is-light` section bands, footer |
| Slate Rule | #e2e8f0 | `--border-color` | band top and bottom hairlines, `pre` border, footer top rule |
| Code Fog | #f1f5f9 | `--background-accent` | BibTeX `pre` and `code` |
| Info Ice | #eef6fc | Bulma `has-background-info-light` | TL;DR strips |
| Bulma Black | #0a0a0a | Bulma `has-text-black` | TL;DR text |
| Caption Grey | #4a4a4a | Bulma `.subtitle` | teaser and viewer captions |
| Band Title | rgba(0,0,0,0.7) | Bulma `.hero.is-light .title` | section titles and h3s inside light bands |
| Orchid | #f093fb | `--gradient-accent` start | section-title underline, author hover underline |
| Coral | #f5576c | `--gradient-accent` end | section-title underline, author hover underline |
| Thumb Rule | #dddddd | inline `.ply-thumb` | viewer thumbnail border |
| Thumb Label | #333333 | inline `.ply-thumb span` | thumbnail captions |
| Loader Grey | #bbbbbb | inline `.loader` | spinner ring (top segment #2563eb) |
| Copied Green | #10b981 | `.copy-bibtex-btn.copied` | copy button after click |

Declared but not visible: `--gradient-primary` (#667eea → #764ba2), `--gradient-subtle`, `--accent-color` #0ea5e9 and the `.publication-awards` red style are not used on the page.

## Tokens — Typography

- **Family:** declared `'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif`; renders Inter 400, 500, 600, 700, 800. Substitute: Geist or SF Pro Display.
- **Code:** declared `'SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', monospace`; renders the first one installed (Cascadia Code or Consolas on Windows, SF Mono on macOS). Substitute: JetBrains Mono.
- **Thumbnail labels:** 12px #333333 in the native button font.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `.title.is-1.publication-title` | 48px / 800 / 1.1 |
| Venue line | `.title.is-4.publication-title` | 24px / 800 / 1.1 |
| Section title | `.title.is-3` | 32px / 700 / 1.125, padding-bottom 16px, gradient tick |
| Sub-heading | `h3.title.is-5` | 20px / 600, margin 32px 0 16px |
| Authors | `.publication-authors a` | 20px / 600 |
| Affiliations | `.publication-authors` | 20px / 400 |
| Caption / TL;DR | `h2.subtitle` | 20px / 400 (TL;DR 700) |
| Body (justified) | `.content.has-text-justified` | 17.6px / 400 / 1.8, #64748b |
| Base | `body` | 16px / 1.6 |
| Button | `.button` | 16px / 600 |
| Code | `pre` | 14.4px / 1.6 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons, copy button, `pre` | 12px radius (`--border-radius`) |
| Thumbnails | 8px radius, 1px #dddddd border, 8px padding; image inside 6px radius, 16:10 |
| Teaser video and figures | square corners, no shadow |
| Section-title tick | 60×3px, 2px radius, `linear-gradient(135deg, #f093fb, #f5576c)`, centered under the title |
| Author hover | 2px gradient underline grows from 0 to 100% width |
| Shadows | `--shadow-sm` 0 1px 2px rgba(0,0,0,0.05) on `pre`; `--shadow-md` on buttons; `--shadow-lg` on button hover; thumbnail hover 0 4px 12px rgba(0,0,0,0.08) |
| Band edges | 1px #e2e8f0 top and bottom |

## Layout Metrics

- **Container:** Bulma `.container.is-max-desktop`, 960px (x=240–1200 at 1440); text columns `is-four-fifths` (768px, x=336–1104).
- **Hero:** `.hero-body` padding 64px 24px (4rem 1.5rem); teaser body 32px top, 64px bottom.
- **Bands:** `section.section.hero.is-light`, padding 48px 24px, 1px #e2e8f0 rules.
- **Teaser:** 912px wide (95% of the column), 4:3.
- **Viewer gallery:** CSS grid `repeat(auto-fill, minmax(120px, 1fr))`, 10px gap, under a canvas viewer.
- **Section title spacing:** 32px below the title (including the 16px tick padding).

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | (viewport − 960)/2 | 16px (justified 17.6px) | 48px | four-fifths text column |
| 769–1023px | 32px (hero body 3rem 2rem) | 16px | 48px | none |
| 481–768px | 16px (hero body 2rem 1rem) | 16px | 48px | Bulma columns stack; text column full width |
| ≤480px | 12px (hero body 1.5rem 0.75rem) | 16px | 32px (`!important`) | thumbnails reflow to 2–3 per row |

## Components

- **Slate button:** Bulma `.button.is-dark` overridden: #1e293b fill, no border, #ffffff Inter 16px / 600, padding 7px 20px, 12px radius, `--shadow-md`; hover fill #2563eb, lift 2px, `--shadow-lg`; active returns to 0.
- **Mosaic teaser:** one autoplaying video, 912px, square corners, showing a grid of rendered 3DGS scenes; native video controls visible.
- **TL;DR strip:** 20px bold #0a0a0a on #eef6fc, 12px padding, centered, square corners; reused under each viewer section.
- **Section title:** centered 32px / 700, 16px bottom padding, a 60×3px orchid-to-coral gradient tick centered at the bottom.
- **Justified prose:** 17.6px, line-height 1.8, #64748b, `strong` phrases in heavier slate; bullet lists with bold lead phrases.
- **3D viewer picker:** canvas viewer above a grid of white 120px+ thumbnail buttons (1px #dddddd, 8px radius, 16:10 image with 6px radius, 12px #333333 label); hover adds a soft shadow, active nudges down 1px; a 14px spinning loader ring (#bbbbbb with #2563eb top) while loading.
- **Comparison carousel:** Bulma carousel forced to one slide at a time, white section.
- **BibTeX:** header row with a #2563eb copy button (12px radius, padding 0.75rem 1rem, 14.4px / 600, turns #10b981 with "Copied!"), `pre` on #f1f5f9 with 1px #e2e8f0 border and 12px radius.
- **Scroll-to-top:** fixed 50px #2563eb circle, bottom-right, appears after scrolling.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors / affiliations | Yes | centered Inter stack, blue authors |
| Link buttons | Yes | two slate 12px-radius buttons |
| Teaser | Yes | full-column mosaic video of generated scenes |
| TL;DR | Yes | pale-blue bold strip (repeated per section) |
| Method summary | Yes | figure, "Core Innovation" and "Why This Matters" sub-heads with bullet lists |
| Interactive 3D viewer | Yes | 3DGS and pointmap viewers with thumbnail pickers |
| Comparison | Yes | carousel of baseline renders |
| Video presentation | Yes | section with embedded video |
| Poster | Yes | poster section |
| BibTeX | Yes | copy button plus pale `pre` |
| Results table (HTML) | No (absent from the source) | |
| Navigation bar | No (absent from the source) | |
| Footer | Yes | #f8fafc band with Academic Project Page Template credit |

## Adapting to Other Content

- **More authors:** keep 20px / 600 blue names wrapping on centered lines with 8px right margins; a third line is fine at this size.
- **Results table:** place it in a #f8fafc band under a gradient-tick title; white table with 1px #e2e8f0 rules, slate #1e293b headers at 600, #64748b cells, your row in #eef6fc.
- **Long publication or news list:** justified 17.6px #64748b entries with bold slate lead phrases, separated by 1px #e2e8f0 rules inside a band.
- **No mosaic:** a single teaser video or image at 912px, square corners, followed by the same caption and TL;DR strip.
- **Award line:** add it to the venue line in parentheses as the source does ("Oral"), not as a badge.

## Do's and Don'ts

- Do keep the chrome slate and white and let the generated imagery supply the color.
- Do mark every section title with the same 60px gradient tick.
- Do reuse the pale-blue TL;DR strip as the one-line takeaway under each interactive block.
- Don't round or shadow the teaser video; its hard edges read as a gallery wall.
- Don't introduce the unused purple gradient tokens; pink-to-coral is the only accent gradient on display.
- Don't rely on Bulma's light-hero title color if you want slate titles; set it explicitly.

## Surfaces

White header and teaser; #f8fafc bands with #e2e8f0 hairlines for method and viewers; a white band for comparisons; #f1f5f9 code; #eef6fc TL;DR strips; #f8fafc footer.

## Imagery

A dense mosaic of generated 3D scenes (indoor, landscape, objects, animals), a two-panel method diagram with blue and orange blocks, interactive Gaussian splat renders and pointmaps, baseline comparison renders.

## Layout

Centered 960px column; header and teaser on white, then alternating light bands. Rendered height about 7,050px.

## Agent Prompt Guide

Quick colors: text #1e293b, link #2563eb (hover #1d4ed8), body grey #64748b, band #f8fafc, rule #e2e8f0, code #f1f5f9, TL;DR #eef6fc with #0a0a0a text, accent tick #f093fb → #f5576c.

1. "Build a header: centered Inter 48px/800 title in #1e293b with line-height 1.1; a 24px/800 venue line; authors as 20px/600 #2563eb links; affiliations 20px #1e293b; two buttons with #1e293b fill, #ffffff 16px/600 text, padding 7px 20px, 12px radius and box-shadow 0 4px 6px -1px rgba(0,0,0,0.1), hover fill #2563eb with translateY(-2px)."
2. "Create a section band: background #f8fafc with 1px #e2e8f0 top and bottom borders, padding 48px 24px; centered 32px/700 title with 16px bottom padding and a centered 60×3px linear-gradient(135deg, #f093fb, #f5576c) tick; then justified 17.6px text in #64748b at line-height 1.8."
3. "Add a TL;DR strip: 20px bold #0a0a0a text, centered, background #eef6fc, padding 12px, square corners, directly under a 912px square-cornered teaser video and a 20px #4a4a4a caption."

## Similar Pages

- Academic Project Page Template pages with a Tailwind-style token override layered on Bulma.
- Text-to-3D and video-generation pages that open with a results mosaic instead of a method figure.

## Quick Start

```css
:root {
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --primary-color: #2563eb;
  --primary-hover: #1d4ed8;
  --background-primary: #ffffff;
  --background-secondary: #f8fafc;
  --background-accent: #f1f5f9;
  --border-color: #e2e8f0;
  --tldr-bg: #eef6fc;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --border-radius: 12px;
  --font: 'Inter', 'Segoe UI', sans-serif;
  --title-size: 48px;
  --body-size: 16px;
  --container: 960px;
}
```

## Provenance

- **URL:** https://gohyojun15.github.io/VIST3A/
- **Paper:** Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator (VIST3A, arXiv 2510.13454), Hyojun Go, Dominik Narnhofer, Goutam Bhat, Prune Truong, Federico Tombari, Konrad Schindler.
- **Venue:** ICLR 2026, Oral (stated under the title).
- **Selection reason:** the arXiv comment reads "ICLR 2026 (Oral)" and links the page; chosen for its dense mosaic teaser, TL;DR callout, light tinted method section and accent underlines under headings.
- **Template credit:** footer says the page was built using the Academic Project Page Template, adopted from Nerfies.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `static/css/index.css`, inline style block, page HTML; 2026-10-28.
