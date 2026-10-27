# Pano3DComposer — Style Reference

> A tidy lab notebook with blue margin tabs, opened on a split panorama you can drag apart.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero, demo, abstract, figures and video grid), the 1440×900 and full-page screenshots, and the page's `static/css/index.css` plus two inline `<style>` blocks read directly (Bulma 0.9 underneath). Google Fonts serves only the 400 face of Google Sans and Noto Sans, so the 600 title and section headings and the 700 badge are browser-synthesized bolds. The inline `.publication-title { font-size: 2rem }` loses to Bulma's `.title.is-2`, so the title renders at 40px.

## Overview

The Nerfies/Bulma template made orderly with one blue accent. A plain white navbar centres six text links (Demo to BibTeX). The hero is centred: a solid #3273dc "CVPR 2026" pill, a two-line 40px Google Sans title in #363636, two Bulma-blue author links, a grey affiliation, and three dark #363636 rounded buttons. Instead of a teaser figure, the first section is an interactive demo: a 32px section heading with a 4px blue bar at the far left edge of the column, a grey lead sentence, two Bulma segmented button groups (scene and view selectors, active segment dark), and a 2:1 panorama comparison at the full 960px column where a white divider line splits the input panorama from the generated scene, each labelled with a small dark translucent tag. Below, the abstract sits in a pale blue (#f0f4ff) rounded panel with justified text, then method and result figures with 8px radii and soft shadows, centred grey captions with bold lead-ins, a 5-column grid of small rounded videos labelled "Scene 01…", a grey BibTeX block and the standard #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 79.0% plus #f4f5f5 2.3%, #fdffff 0.4%, #fffffc 0.4%; warm panorama tones #ad9268 7.1% and #b2a085 4.9% (the top of the comparison image); dark grey #696158 3.2% (title, buttons and segmented controls); light grey #cdcfd1 2.8% (segment borders, anti-aliasing). The blue badge and heading bar are too small to cluster.

Anatomy in DOM order (desktop 1440px; Bulma `.container.is-max-desktop` 960px at x=240):

1. **Navbar** (0–52px, not sticky): white, items centred from x=463; Demo, Abstract, Method, Results, Video Gallery, BibTeX in Noto Sans 16px/400 #4a4a4a, padding 8px 12px.
2. **Venue pill** (`.conference-badge`, y=100, 116×32): "CVPR 2026", white 16px/700 (synthesized), letter-spacing 1px, #3273dc fill, 20px radius, padding 4px 13.6px. Gap 12px.
3. **Title** (`h1.publication-title`, y=144, two lines, 90px): Google Sans 40px/600, line-height 45px, #363636, centred. Gap 24px.
4. **Authors** (y=258): Google Sans 20px/400, names #209cee, commas and superscripts #4a4a4a. Gap 6px.
5. **Affiliation** (y=299): Google Sans 16px #555555 with a superscript. Gap 33px.
6. **Buttons** (y=359, 40px tall, 5px apart): Paper, arXiv, Code; #363636 rounded, white 16px, icon left. The hero section ends at y=464.
7. **Demo heading** (`h2.section-title`, y=512): Noto Sans 32px/600, #363636, centred text with a 4px #3273dc left border at x=240 and 12px left padding. Gap 24px.
8. **Demo lead** (y=572): 16px #555555 centred, two lines. Gap 20px.
9. **Scene selector** (y=640) and **view selector** (y=690): Bulma `.buttons.has-addons` with `.button.is-small`, 30px tall, 12px system-sans text; active segment #363636 with white text, others white with 1px #dbdbdb borders; 2px outer radii.
10. **Comparison** (`.demo-compare`, y=748, 960×480, 2:1): 8px radius, input panorama on the left and generated render clipped from `--cut: 50%`, 2px white divider with a 4px dark glow, tags "Input panorama" / "Generated scene" (12.48px white on rgba(0,0,0,0.55), 4px radius, 8px from the corners). Its top 150px shows above the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Title Ink | #363636 | Bulma `$text-strong` | title, section headings, dark buttons, active segments |
| Body Grey | #4a4a4a | Bulma `$text` | body text, navbar links, abstract text, BibTeX text |
| Caption Grey | #555555 | (literal) | affiliation, demo lead, figure captions |
| Label Grey | #666666 | (literal) | video grid labels |
| Strong Ink | #222222 | (literal) | bold lead-ins in figure captions |
| Accent Blue | #3273dc | (literal) | venue pill fill, 4px section-heading bars |
| Author Blue | #209cee | hsl(204,86%,53%) | author links |
| Abstract Mist | #f0f4ff | (literal) | abstract panel |
| Segment Edge | #dbdbdb | Bulma border | inactive segmented buttons |
| Code Grey | #f5f5f5 | Bulma `pre` | BibTeX block |
| Footer Grey | #fafafa | Bulma footer | footer band |
| Tag Shade | rgba(0,0,0,0.55) | (literal) | demo image tags |

Declared but not visible: `.hero.teaser-section { background: #f5f7fa }` and Bulma `is-light` on two sections have no visible fill; the page is white throughout apart from the abstract panel.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display (title, authors) | 'Google Sans', sans-serif | Google Sans 400; 600 synthesized | Outfit |
| Body and headings | 'Noto Sans', sans-serif | Noto Sans 400; 600/700 synthesized | Noto Sans (load 600/700) |
| Segmented controls | Bulma `.button` system stack (BlinkMacSystemFont, Segoe UI, Roboto…) | Segoe UI on Windows | Inter |
| Mono | Bulma monospace | Consolas | JetBrains Mono |
| Icons | Font Awesome 5 (SVG), Academicons | Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `.title.is-2.publication-title` | 40px / 600 / 45px | #363636 |
| Venue pill | `.conference-badge` | 16px / 700, letter-spacing 1px | #ffffff |
| Authors | `.publication-authors` (`is-size-5`) | 20px / 400 / 30px | #209cee links |
| Affiliation | `.author-block` (`is-size-6`) | 16px / 400 | #555555 |
| Section heading | `.title.is-3.section-title` | 32px / 600 / 36px | #363636 |
| Body / abstract | `body`, `.abstract-box` | 16px / 400 / 24px, abstract justified | #4a4a4a |
| Demo lead | `.demo-lead` | 16px / 400 | #555555 |
| Figure caption | `.figure-caption` | 0.95rem = 15.2px / 400 / 1.5; lead-in bold #222222 | #555555 |
| Video label | `.video-grid-item p` | 0.78rem = 12.48px | #666666 |
| Demo tag | `.demo-tag` | 12.48px | #ffffff |
| Segmented button | `.button.is-small` | 12px / 400 | #363636 or #ffffff |
| BibTeX | `pre` | 14px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill | 20px | none | none |
| Link buttons | 290486px (Bulma rounded) | 1px transparent | none |
| Segmented buttons | 2px outer corners, square inner joins | 1px #dbdbdb (inactive) | none |
| Section heading | 0 | 4px #3273dc left | none |
| Comparison frame | 8px | none | none; divider 2px #ffffff with 0 0 4px rgba(0,0,0,0.5) |
| Demo tags | 4px | none | none |
| Abstract panel | 10px | none | none |
| Method figure | 8px | none | 0 4px 20px rgba(0,0,0,0.15) |
| Result figures | 8px | none | 0 4px 16px rgba(0,0,0,0.12) |
| Gallery videos | 6px | none | 0 2px 8px rgba(0,0,0,0.15) |
| BibTeX pre | 0 | none | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop`, 960px at x=240 (max-width 960px from 1024px up); sections padding 48px 24px.
- **Hero**: `.hero-body` default Bulma padding 48px 24px; badge 48px under the navbar; hero 52–464px.
- **Abstract**: column `is-four-fifths` (763px at x=338); panel padding 24px 32px; paragraphs 16px apart.
- **Figures**: full 960px; captions 12px below; `.result-figure` margin-bottom 32px.
- **Demo**: selectors 8px margin-bottom each plus 12px group spacing; comparison 20px below, `aspect-ratio: 2/1`.
- **Video gallery**: `grid-template-columns: repeat(5, 1fr)`, gap 10px (184px tiles at 1440, 3:2 videos), labels 4px below.
- **Footer**: #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | (100% − 960px)/2 | 16px | 40px | video grid 5 columns |
| 769–1023px | 24px (fluid container) | 16px | 40px | video grid 4 columns; navbar collapses to a burger below 1024px |
| ≤768px | 24px | 16px | 40px (Bulma keeps is-2) | video grid 2 columns; abstract column full width |

## Components

- **Venue pill** (`.conference-badge`): inline-block, #3273dc, white 16px bold, letter-spacing 1px, padding 4px 13.6px, 20px radius, 12px above the title.
- **Dark link button** (Bulma `.button.is-dark.is-rounded`): #363636, white 16px/400, 40px tall, padding 7px 20px, fully rounded, Font Awesome or Academicons icon left.
- **Accent-bar heading** (`h2.title.is-3.section-title`): full-width block, centred 32px/600 #363636 text, 4px solid #3273dc left border with 12px padding, 24px margin below. Because the heading spans the column, the bar sits at the column's left edge while the text stays centred.
- **Segmented selector** (Bulma `.buttons.has-addons` + `.button.is-small`): 30px tall, padding 5px 12px, 12px text; active segment `.is-dark` #363636 white; others white with 1px #dbdbdb; 2px radii on the outer ends only.
- **Panorama comparison** (`.demo-compare`): 2:1 frame, 8px radius, two stacked images with the second clipped by `clip-path: inset(0 0 0 var(--cut))`, an invisible full-size range input for dragging (cursor ew-resize), a 2px white divider with a dark glow, and corner tags.
- **Abstract panel** (`.abstract-box`): #f0f4ff, 10px radius, padding 24px 32px, justified 16px #4a4a4a with bold method names.
- **Shadowed figure** (`.result-figure img`, `.method-figure img`): 8px radius, soft shadow, centred 15.2px #555555 caption with a bold #222222 "Fig. N:" lead-in.
- **Video gallery tile**: 6px radius, 0 2px 8px rgba(0,0,0,0.15), 12.48px #666666 label beneath.
- **BibTeX**: Bulma `pre` on #f5f5f5, 14px, padding 17.5px 21px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | centred plain text links, not sticky |
| Venue badge | yes | solid blue pill above the title |
| Title / authors / affiliation | yes | centred Google Sans, Bulma-blue author links |
| Link buttons | yes | three dark rounded buttons |
| Interactive teaser | present but non-standard | the hero teaser is a drag-to-compare panorama demo with scene and view selectors |
| Abstract | yes | pale blue rounded panel |
| Method figure | yes | shadowed 960px figure with caption |
| Results | yes | two shadowed figures with captions |
| Results tables | absent from the source | results are figures only |
| Video gallery | yes | 5-column grid of small rounded videos |
| BibTeX | yes | grey Bulma pre |
| Footer | yes | Nerfies credit |

## Adapting to Other Content

- **More authors and affiliations**: keep the 20px Google Sans author line and the 16px #555555 affiliation line; let them wrap; numbered superscripts in #4a4a4a.
- **A results table**: Bulma `.table.is-fullwidth` inside the 960px container with 15px text, a 2px #363636 rule under the header, 1px #dbdbdb rows; highlight the best value with bold rather than colour; caption in 15.2px #555555 below.
- **A non-panorama comparison**: reuse `.demo-compare` with the image pair's own aspect ratio and keep the corner tags and segmented selectors.
- **More sections**: every heading uses the same blue-bar `.section-title`; alternate nothing else (no tinted bands).
- **News or a long list**: plain 16px #4a4a4a list inside the container, dates bold #363636; no cards.

## Do's and Don'ts

- Do keep #3273dc for the venue pill and heading bars only.
- Do keep figures white-framed with 8px radii and soft shadows.
- Do use Bulma segmented buttons for any selector rather than tabs.
- Don't load only the 400 weights if you want real bolds; request Google Sans and Noto Sans at 600 and 700.
- Don't add background bands; only the abstract is tinted.
- Don't left-align headings; the bar is the only off-centre element.

## Surfaces

White page and hero, one pale blue abstract panel, #f5f5f5 BibTeX, #fafafa footer.

## Imagery

Equirectangular interior panoramas (bedroom, studio loft, photo studio) with matching generated renders, a pastel colour-blocked method diagram, multi-row result grids, and short orbit videos of generated 3D scenes.

## Layout

Navbar; centred hero; Interactive Demo; Abstract; Method Overview; Results; Video Gallery; BibTeX; footer, all in a 960px column. About 5,100px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, caption #555555, accent #3273dc, authors #209cee, abstract panel #f0f4ff, segment border #dbdbdb, footer #fafafa.

1. "Build a centred hero in a 960px container: a venue pill (#3273dc, white 16px bold, letter-spacing 1px, padding 4px 13.6px, 20px radius), 12px gap, title Google Sans 40px/600 #363636 line-height 45px, authors Google Sans 20px with #209cee links, affiliation 16px #555555, then three #363636 fully rounded 40px buttons with white 16px labels and icons left."
2. "Create a section heading: full-width h2, Noto Sans 32px/600 #363636, text centred, border-left 4px solid #3273dc, padding-left 12px, margin-bottom 24px."
3. "Make a drag-to-compare image: container aspect-ratio 2/1, 8px radius, overflow hidden; two absolutely positioned images, the second clipped with clip-path inset(0 0 0 var(--cut)); a 2px #ffffff divider at var(--cut) with box-shadow 0 0 4px rgba(0,0,0,0.5); corner tags 12.48px white on rgba(0,0,0,0.55), 4px radius, padding 2px 8px."

## Similar Pages

- Nerfies/Bulma academic pages with a single accent colour added through badges and heading bars.
- 3D scene generation pages that lead with an interactive before/after viewer.

## Quick Start

```css
:root {
  --title: #363636;
  --text: #4a4a4a;
  --caption: #555555;
  --accent: #3273dc;
  --author: #209cee;
  --abstract-bg: #f0f4ff;
  --segment-border: #dbdbdb;
  --footer: #fafafa;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
body { font: 16px/1.5 var(--font-body); color: var(--text); background: #ffffff; }
.section-title { border-left: 4px solid var(--accent); padding-left: 0.75rem; margin-bottom: 1.5rem; }
.abstract-box { background: var(--abstract-bg); border-radius: 10px; padding: 1.5rem 2rem; }
```

## Provenance

- **URL**: https://qiuzidian.github.io/pano3dcomposer-page/
- **Paper**: Pano3DComposer: Feed-Forward Compositional 3D Scene Generation from Single Panoramic Image (arXiv 2603.05908), Zidian Qiu, Ancong Wu.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit**: footer says the site is built upon the Nerfies template.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and components, the 1440×900 and full-page screenshots, and `index.css` plus the inline styles read directly, on 2026-10-28.
