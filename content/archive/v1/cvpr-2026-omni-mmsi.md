# Omni-MMSI Style Reference

> Slate ink on a Tailwind-white lab bench.

**Theme:** light

Measurements below come from the page's own CSS (static/css/index.css), its inline HTML styles and computed styles read in a rendered browser tab. Values are normalized to hex where the source used hex or rgb; roles are interpreted from where each token is applied.

## Overview

Omni-MMSI uses the 2025 refresh of the Academic Project Page Template: Bulma 0.9 underneath, with a Tailwind-flavoured variable layer on top (slate text, blue-600 accent, 12/16px radii, layered soft shadows). Everything is centred in a single narrow column. The title is set in Inter 800 at 48px, author names are blue-600 semibold, and four dark slate pill buttons (Paper, Presentation, Code, Dataset) sit under a light venue line. Sections alternate white and a barely tinted #f8fafc band. Section titles carry a short pink-to-coral gradient bar underneath, the template's one decorative flourish.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Slate Ink | #1e293b | --text-primary | Body text, h1, dark button fill |
| Blueprint Blue | #2563eb | --primary-color | Author links, button hover, scroll-to-top, copy-BibTeX button |
| Deep Blueprint | #1d4ed8 | --primary-hover | Hover state of blue elements |
| Fog Slate | #64748b | --text-secondary | Abstract body text, footer text, carousel captions |
| Mist Slate | #94a3b8 | --text-light | Icons inside the More Works list |
| Paper White | #ffffff | --background-primary | Page background |
| Frost Band | #f8fafc | --background-secondary | hero.is-light bands, footer |
| Ice Tile | #f1f5f9 | --background-accent | BibTeX pre block, venue pill |
| Hairline | #e2e8f0 | --border-color | Band borders, pre border, card borders |
| Sky Accent | #0ea5e9 | --accent-color | Declared, little visible use |
| Orchid to Coral | #f093fb to #f5576c | --gradient-accent | 60x3px bar under section titles, author-link underline |
| Copied Green | #10b981 | (literal) | Copy button success state |
| Award Red | #ef4444 | (literal) | publication-awards block (not used on this page) |
| Inline Blue | #3b82f6 | (inline style) | One inline highlighted span |

Bulma's own palette (#00d1b2 turquoise, #ffdd57 yellow, #3273dc link blue) dominates the raw frequency counts but is not visible on the rendered page.

## Tokens · Typography

- **Primary family**: Inter (Google Fonts), fallback "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif.
- **Mono**: browser monospace for BibTeX (SF Mono appears in the stack).
- **Weights**: 800 title, 700 section titles, 600 buttons and author links, 500 author block, 400 body.
- **Body**: 16px, line-height 1.6, antialiased.

| Role | Size | Weight | Color |
|---|---|---|---|
| Paper title (h1.is-1) | 48px | 800 | #1e293b, line-height 1.1 |
| Section title (h2.title.is-3) | 32px (2rem) | 700 | #1e293b |
| Subtitle / teaser caption | 20px | 400 | #4a4a4a |
| Author names | 20px | 600 | #2563eb |
| Abstract | 17.6px (1.1rem) | 400 | #64748b, line-height 1.8 |
| Button label | 16px | 600 | #ffffff |
| BibTeX | 14.4px (0.9rem) | 400 | #4a4a4a |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, pre, venue pill, images | 12px (--border-radius) |
| Video frame, banner, carousel item | 16px (--border-radius-lg) |
| Scroll-to-top | 50% |

- **Shadows**: md `0 4px 6px -1px rgb(0 0 0/.1), 0 2px 4px -2px rgb(0 0 0/.1)`; lg `0 10px 15px -3px …`; xl `0 20px 25px -5px …`. Buttons rest on md and lift to lg on hover.
- **Transition**: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); hover lifts translateY(-2px to -4px).
- **Layout**: Bulma container.is-max-desktop (960px, inferred from class), column is-four-fifths for text. hero-body padding 4rem 1.5rem; header 5rem 1.5rem 1.5rem.

## Components

- **Link button**: `a.external-link.button.is-normal.is-rounded.is-dark`, fill #1e293b, white 600 Inter 16px, radius 12px (overrides Bulma's pill), shadow-md; hover turns #2563eb and lifts 2px. Font Awesome / academicons glyph left of label.
- **Section title**: centred h2 32px/700 with a 60x3px gradient bar (#f093fb to #f5576c) centred below it.
- **Venue line**: plain centred text under authors (CVPR 2026); the template's grey pill style is available via .publication-venue (#64748b on #f1f5f9, 12px radius).
- **BibTeX**: header row with title and a blue (#2563eb) "Copy" button, 12px radius; pre on #f1f5f9 with #e2e8f0 border and shadow-sm, padding 1.5rem.
- **Carousel card**: white, 1px #e2e8f0 border, 16px radius, shadow-md, 1.5rem padding, hover lift 4px.
- **More Works dropdown**: fixed top-right pill (white, 2px #e2e8f0 border, 16px radius), opens a 400px list of related works.
- **Scroll-to-top**: fixed 50px blue circle bottom-right, appears after scroll.
- **Footer**: #f8fafc band, 1px top hairline, links #2563eb.

## Page Modules

- **Title/author block**: centred h1, nine author blocks with superscript affiliations, four universities on one line, venue text "CVPR 2026".
- **Link buttons**: Paper, Presentation, Code, Dataset (four dark slate buttons).
- **Teaser figure**: wide comparison diagram (prior studies vs Omni-MMSI) directly below buttons, with a 20px centred subtitle.
- **Abstract**: light band, justified slate-grey text in a four-fifths column.
- **Image carousel**: bulma-carousel with four items; captions still read "First image description." etc. (template placeholder).
- **Video presentation**: 16:9 YouTube iframe in a 16px-radius shadowed frame.
- **Second carousel and Poster**: sections titled "Another Carousel" and "Poster" retained from the template.
- **BibTeX**: copy-button block.
- **Absent**: results tables, comparison slider, 3D viewer, HF demo.

## Do's and Don'ts

- Do keep text in the slate scale (#1e293b, #64748b, #94a3b8) rather than pure black.
- Do use #2563eb only for interactive elements (author links, hover, copy, scroll-to-top).
- Do keep 12px radius on buttons even though Bulma's is-rounded class implies a pill.
- Don't surface Bulma's turquoise #00d1b2 or yellow #ffdd57; they ship in bulma.min.css but are unused.
- Don't leave template placeholder captions or section names in production.
- Don't add hard borders; separation comes from #f8fafc bands and soft shadows.

## Surfaces

White page, #f8fafc bands with #e2e8f0 hairlines top and bottom, #f1f5f9 tiles for code. Media cards float on layered shadows.

## Imagery

Paper figures (flat diagrams with coloured callouts) and video frames. Images get 12px radius plus shadow-md; banner/video 16px plus shadow-xl.

## Layout

Single centred column, about 960px, text at four-fifths width. Order: hero header, teaser, abstract band, carousel, video band, carousel, poster, BibTeX, footer. Rendered height about 2,200px at 1,009px wide.

## Agent Prompt Guide

Quick colors: text #1e293b, secondary #64748b, accent #2563eb, band #f8fafc, tile #f1f5f9, hairline #e2e8f0, title bar gradient #f093fb to #f5576c.

1. "Build a centred paper header: Inter 800 48px title in #1e293b, author names 20px/600 in #2563eb, then four buttons filled #1e293b, white 600 text, 12px radius, shadow `0 4px 6px -1px rgb(0 0 0/.1)`, turning #2563eb on hover with a 2px lift."
2. "Make a section title: centred 32px/700 Inter, followed by a 60x3px bar with linear-gradient(135deg,#f093fb,#f5576c), 2px radius."
3. "Create a BibTeX block: header row with a #2563eb Copy button (12px radius, white 600 0.9rem); pre on #f1f5f9 with 1px #e2e8f0 border, 12px radius, 1.5rem padding."

## Similar Pages

- CFG-Ctrl (CVPR 2026), same refreshed template and tokens.
- Other pages built on the 2025 Academic Project Page Template refresh.

## Quick Start

```css
:root {
  --primary-color: #2563eb;
  --primary-hover: #1d4ed8;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --text-light: #94a3b8;
  --background-primary: #ffffff;
  --background-secondary: #f8fafc;
  --background-accent: #f1f5f9;
  --border-color: #e2e8f0;
  --gradient-accent: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --border-radius: 12px;
  --border-radius-lg: 16px;
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --font-sans: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

## Provenance

- **URL**: https://sampson-lee.github.io/omni-mmsi-project-page/
- **Paper**: Omni-MMSI: Toward Identity-attributed Social Interaction Understanding (arXiv 2604.00267), Xinpeng Li et al.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states CVPR 2026 acceptance and links this page.
- **Template credit**: footer says the page uses the Academic Project Page Template, adapted from Nerfies.
- **Measurement method**: static HTML and CSS parsed by extract_style.py, page-local index.css read directly, and computed styles plus one reduced screenshot taken in a browser tab on 2026-10-27. Font sizes from computed style at about 1,000px viewport. No pixel colour sampling.
