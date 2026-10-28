# WebMMU — Style Reference

> A product launch page for a dataset: a glossy violet book cover on the right, confetti shapes drifting behind, and every author worn as a name tag.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, the page's `style.css` (custom properties, an 8pt spacing scale, many animated hero shapes) and `index.html`, and a browser probe at 1440px of the hero badges, author and affiliation chips, buttons, cards, tables, tabs and BibTeX. The violet "WebMMU" cover card with its globe illustration is a 400×600 image (`img.hero-cover-image`), not CSS. Space Grotesk is declared as the display face but the hero title uses Inter; Space Grotesk renders only on the navbar wordmark, section titles and card titles. Tab and carousel buttons fall back to Arial because `button` does not inherit the page font.

## Overview

A light, startup-styled benchmark page. A sticky translucent white navbar (90% white with a 10px backdrop blur and a hairline) carries the "WebMMU" wordmark in steel blue and five text links. The hero sits on a faint #f8fafc → #f1f5f9 gradient strewn with about fifteen softly coloured, slowly floating shapes (circles, a square, triangle, diamond, hexagon, star, oval, cross, symbols). On the left: a light-blue "EMNLP 2025" label next to a blue-to-yellow gradient pill "Spotlight at MAR workshop @ CVPR 2025", a second pill "First Multilingual Benchmark for Web Agents", a 33.6px bold slate title, authors as tinted rounded chips with emoji affiliation markers, grey affiliation chips, a small legend, a long description and four glossy sky-to-steel gradient pill buttons. On the right, the violet cover image. Below, sections with centred Space Grotesk titles hold white rounded cards with hairline borders: an About card with a framed figure and an emoji-led feature list, three task cards, a dataset table, a tabbed sample explorer with a carousel, embedded Hugging Face viewers, results tables and figures, a dark BibTeX block and a dark slate footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): violet-blue #717fc5 19.7% (the cover image), #f5f8fb 19.4% and #f6f9fb 17.7% (hero gradient), #d1dce7 11.5% (chips, shapes and antialiased text), #f0f3f6 10.0%, #f4f7f8 9.4%, #fcfdfe 8.1%, #f6f8fb 4.2%.

Anatomy in DOM order (desktop 1440px):

1. **Navbar** (`nav.navbar`, sticky, 0–71px): rgba(255,255,255,0.9), `backdrop-filter: blur(10px)`, 1px #e2e8f0 bottom border, padding 16px 0; `.container` max 1300px, padding 0 40px. Wordmark "WebMMU" Space Grotesk 24px / 700 #2d6fa3 at x=110; links About … Results 16px / 500 #334155, padding 8px 12px, radius 8px, 24px gap; hover #2d6fa3 on rgba(59,130,246,0.1).
2. **Hero** (`section.hero.hero-blend`, 71–1105px): padding 32px 0 24px, background `linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%)`; `.hero-flex` (1300px at x=70) flex with a 56px gap, padding 24px 0 40px, min-height 520px.
3. **Meta row** (y=127): "EMNLP 2025" 17.6px / 600 #7db7ff, letter-spacing 0.03em; then the `.hero-multilingual-badge` pill "Spotlight at MAR workshop @ CVPR 2025": `linear-gradient(90deg, #e0f2fe 0%, #fef9c3 100%)`, 16.8px / 600 #2d6fa3, radius 16px, padding 3.7px 18.5px, shadow `0 1px 6px rgba(30,72,94,0.06)`. A second identical pill "🌐 First Multilingual Benchmark for Web Agents" sits on the next row (y≈197).
4. **Title** (`h1.hero-title`, y=266): Inter 33.6px / 700, line-height 1.15 (38.64px), #1e293b, left aligned, three lines within 800px, `text-shadow: 0 2px 8px rgba(30,72,94,0.06)`. Margin-bottom 16px.
5. **Author chips** (`.hero-authors-compact`, y=359, max 700px): 13 chips, 17.28px / 500 #1e293b, background rgba(59,130,246,0.07), radius 19px, padding 3.1px 16.4px, gaps 4.8px × 14.4px; emoji affiliation markers and ∗ † ‡ superscripts after each name; hover #e0e7ef.
6. **Affiliation chips** (`.hero-affiliations-compact`, y=520): 16.16px / 400 #64748b on rgba(100,116,139,0.10), radius 19.4px, padding 2.1px 13.7px, each with its emoji marker.
7. **Legend** (`.hero-authorship-legend`, y=596): 14.4px #64748b, "† Equal contribution (first authors)" and "‡ Equal contribution (second authors)".
8. **Description** (`.hero-description`, y=630): 17.28px / 400, line-height 27.65px, #334155, max 800px, eight lines; margin-bottom 28px.
9. **Buttons** (`.hero-buttons`, y=879, 50px tall): 📄 Paper, 💻 Code, 📥 Dataset, 🎥 Video Talk, 16px apart, min-width 140px; an italic "*Corresponding:" line with an underlined mail link follows below the fold.
10. **Cover** (`.hero-right`, x=948, y=127): 400×600 image, radius 16px, white background.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Steel Blue | #2d6fa3 | --primary-color | wordmark, badge text, nav hover, carousel buttons, button gradient end, task card hover border |
| Sky | #a3d8fd | (literal) | button gradient start |
| Light Blue | #7db7ff | (literal) | "EMNLP 2025" meta label |
| Slate | #1e293b | --secondary-color / --primary-dark | titles, author chips, table headers, active tabs, BibTeX block, footer |
| Text | #334155 | --text-color | body text, description, nav links, table cells |
| Muted | #64748b | --text-light | affiliations, legend, section subtitles, inactive tabs, task descriptions, sample text |
| Page | #f8fafc | --bg-color | page background, hero gradient start, table header cells |
| Hero End | #f1f5f9 | (literal) | hero gradient end |
| Border | #e2e8f0 | --border-color | navbar rule, card and figure borders, table row lines, tab bar border |
| White | #ffffff | --white | cards, tables, tab bar, sample cards, footer and BibTeX text |
| Badge Blue | #e0f2fe | (literal) | badge gradient start |
| Badge Yellow | #fef9c3 | (literal) | badge gradient end |
| Chip Tint | rgba(59,130,246,0.07) | (literal) | author chip fill; nav-link hover uses the same blue at 10% |
| Chip Hover | #e0e7ef | (literal) | author chip hover |
| Accent Violet | #8b5cf6 | --accent-color | violet floating circle (at 20%) |
| Cover Violet | #717fc5 | (image) | dominant tone of the cover image |

The custom properties also declare --accent-yellow #f6c544, --accent-orange #f6a13b, --accent-green #7ecb4a, --accent-teal #3bb6b6 and --accent-red #e45757; none of them is visible as a solid fill in the render, only the translucent floating shapes use similar hues.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif | Inter 400, 500, 600, 700 | Inter |
| Display | 'Space Grotesk', sans-serif | Space Grotesk 600, 700 | Space Grotesk |
| Buttons in tabs and carousel | browser default | Arial | Inter (set `font: inherit`) |
| Code | 'Monaco', 'Menlo', monospace | system fallback (Consolas on Windows) | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Hero title | `.hero-title` | 2.1rem = 33.6px / 700 / 1.15 | #1e293b |
| Meta label | `.hero-meta` | 1.1rem = 17.6px / 600, letter-spacing 0.03em | #7db7ff |
| Badge | `.hero-multilingual-badge` | 1.05rem = 16.8px / 600 | #2d6fa3 |
| Author chip | `.hero-authors-compact span` | 1.08rem = 17.28px / 500 / 1.5 | #1e293b |
| Affiliation chip | `.hero-affiliations-compact span` | 1.01rem = 16.16px / 400 / 1.4 | #64748b |
| Legend | `.hero-authorship-legend` | 0.9rem = 14.4px | #64748b |
| Description | `.hero-description` | 1.08rem = 17.28px / 400 / 1.6 | #334155 |
| Button | `.hero-btn` | 1.05rem = 16.8px / 600 | #ffffff |
| Wordmark | `.navbar-brand` | Space Grotesk 1.5rem = 24px / 700 | #2d6fa3 |
| Nav link | `.navbar-item` | 16px / 500 | #334155 |
| Section title | `.section-title` | Space Grotesk 2rem = 32px / 700, centred, margin-bottom 32px | #1e293b |
| Section subtitle | `.section-subtitle` | 1.1rem = 17.6px / 400 / 1.6, max 600px, centred | #64748b |
| Card title | `.card-title` | Space Grotesk 1.5rem = 24px / 600 | #1e293b |
| Task title | `.task-card h3` | Space Grotesk 1.25rem = 20px / 600 | #1e293b |
| Feature item | `.features-list li` | 1.1rem = 17.6px; `strong` 700 #1e293b | #334155 |
| Table | `.table th, td` | 16px; th 600 | th #1e293b, td #334155 |
| Tab | `.tab`, `.explore-tab` | Arial 1.3rem = 20.8px / 600 | active #ffffff, others #64748b |
| BibTeX | `.bibtex-block` | 0.9rem = 14.4px / 1.5 monospace | #ffffff on #1e293b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / background |
|---|---|---|---|
| Navbar | 0 | 1px solid #e2e8f0 bottom | rgba(255,255,255,0.9), `backdrop-filter: blur(10px)` |
| Hero buttons | 2em = 33.6px, padding 12px 28px | none | `linear-gradient(135deg, #a3d8fd 10%, #2d6fa3 90%)`; `0 2px 8px rgba(30, 41, 59, 0.08)`; hover gradient reversed `linear-gradient(135deg, #2d6fa3 10%, #a3d8fd 90%)` with `0 4px 16px rgba(30, 41, 59, 0.12)`; active solid #2d6fa3 |
| Hero badges | 16px | none | `linear-gradient(90deg, #e0f2fe 0%, #fef9c3 100%)`; `0 1px 6px rgba(30,72,94,0.06)` |
| Author chips | 1.1em = 19px | none | rgba(59,130,246,0.07); `0 1px 4px rgba(100,116,139,0.04)` |
| Affiliation chips | 1.2em = 19.4px | none | rgba(100,116,139,0.10); `0 1px 4px rgba(100,116,139,0.03)` |
| Cover image | 16px | none | none |
| Cards | 12px, padding 32px | 1px solid #e2e8f0 | `0 1px 3px rgba(0, 0, 0, 0.1)` |
| Task cards | 12px, padding 24px | 1px solid #e2e8f0; hover #2d6fa3 | `0 1px 3px rgba(0, 0, 0, 0.1)`; hover `translateY(-2px)` + `0 8px 16px rgba(0, 0, 0, 0.1)` |
| Framed figures (`.image`) | 12px | 1px solid #e2e8f0 | `0 4px 6px rgba(0, 0, 0, 0.1)` |
| Tables | 8px, overflow hidden | 1px #e2e8f0 row lines | `0 1px 3px rgba(0, 0, 0, 0.1)`; row hover rgba(59,130,246,0.05) |
| Tab bar | 12px, padding 12px | 1px solid #e2e8f0 | white, `0 1px 3px rgba(0, 0, 0, 0.1)`; active tab #1e293b with `0 4px 12px rgba(30, 41, 59, 0.2)` and `translateY(-1px)` |
| Carousel buttons | 50%, 44×44px | none | #2d6fa3, `0 1px 3px rgba(0, 0, 0, 0.1)` |
| Sample cards | 8px, padding 8px 8px 12px | none | white, `0 1px 3px rgba(0, 0, 0, 0.1)` |
| BibTeX block | 8px, padding 24px | none | #1e293b |
| Floating shapes | 50% for circles | none | translucent fills such as rgba(59, 130, 246, 0.25), rgba(139, 92, 246, 0.2), rgba(16, 185, 129, 0.2), rgba(245, 158, 11, 0.18), rgba(239, 68, 68, 0.18), rgba(236, 72, 153, 0.18); `float`, `float-reverse`, `float-wide` animations over 10–24s |

## Layout Metrics

- **Container**: `.container` max 1300px, padding 0 40px (content 1220px at x=110). Spacing follows an 8pt scale (4, 8, 12, 16 … 80px).
- **Hero**: section padding 32px 0 24px; `.hero-flex` 1300px at x=70, padding 24px 0 40px, gap 56px, min-height 520px; left column max 800px (min 400px), right column flexible (min 320px) centring the 400px cover.
- **Sections**: `.section` padding 40px 0 32px; titles margin-bottom 32px; subtitles max 600px centred with 32px below.
- **Cards**: 1220px wide, padding 32px, margin-bottom 32px; inner figures framed at 800px centred.
- **Task grid**: `repeat(auto-fit, minmax(320px, 1fr))`, gap 32px; three 385px cards.
- **Explorer**: tab bar with three equal 390px tabs (gap 12px); carousel with 44px buttons 8px inside each edge.
- **Footer**: #1e293b, padding 64px 0, margin-top 80px, centred white text.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1300px (1440 renders this) | 40px inside 1300px | 16px; description 17.28px | 33.6px | hero two columns |
| ≤1300px | 20px | same | 33.6px | hero left column and description lose the 800px cap |
| ≤900px | 20px | same | 24px | hero stacks (cover below text, max 90vw, radius 12px); buttons stack centred with 12px gap |
| ≤768px | 24px | same | 32px (this later rule overrides the 900px value) | nav links hidden behind a menu toggle; task grid 1 column; tabs stack; carousel buttons 36px |
| ≤600px | 24px | same | 32px | author and affiliation chips centred; meta row stacks |

## Components

- **Glossy gradient pill** (`.hero-btn`): inline-flex, gap 8px, padding 12px 28px, radius 33.6px, min-width 140px, `linear-gradient(135deg, #a3d8fd 10%, #2d6fa3 90%)`, #ffffff 16.8px / 600 Inter, leading emoji, `0 2px 8px rgba(30, 41, 59, 0.08)`; hover reverses the gradient and deepens the shadow; active solid #2d6fa3.
- **Gradient badge** (`.hero-multilingual-badge`): inline-block pill, `linear-gradient(90deg, #e0f2fe 0%, #fef9c3 100%)`, 16.8px / 600 #2d6fa3, radius 16px, padding 3.7px 18.5px, faint shadow; used for the workshop spotlight and the "first multilingual" claim.
- **Author name tag**: flex chip with rgba(59,130,246,0.07) fill, radius 19px, padding 3.1px 16.4px, 17.28px / 500 #1e293b, emoji affiliation marker and contribution symbol after the name; hover #e0e7ef.
- **Affiliation tag**: same shape in rgba(100,116,139,0.10) with 16.16px #64748b text and the emoji marker first.
- **White card**: #ffffff, 1px #e2e8f0, radius 12px, padding 32px, `0 1px 3px rgba(0, 0, 0, 0.1)`; Space Grotesk 24px / 600 card titles.
- **Feature list**: no bullets; each item 17.6px with an emoji and a 700 #1e293b run-in label, 8px vertical padding, separated by spacing only.
- **Task card**: white, 1px #e2e8f0, radius 12px, padding 24px; Space Grotesk 20px / 600 title, #64748b text; hover lifts 2px, border #2d6fa3.
- **Segmented tabs**: white bar (radius 12px, padding 12px, hairline, soft shadow) holding equal-width tabs at 20.8px / 600; active tab filled #1e293b with white text and a 0 4px 12px shadow.
- **Dark BibTeX**: #1e293b block, radius 8px, padding 24px, white 14.4px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky navbar | yes | translucent white with blur, steel-blue wordmark |
| Venue / highlight badges | yes | light-blue venue text plus blue-to-yellow gradient pills |
| Title | yes | 33.6px bold slate, left aligned |
| Authors / affiliations | yes | tinted name-tag chips with emoji markers |
| Link buttons | yes | four glossy gradient pills with emoji |
| Cover art | yes | 400×600 violet cover image with 16px radius |
| Animated background | yes | about fifteen translucent floating shapes in the hero |
| Abstract | present but non-standard | the hero description and the About card replace an Abstract heading |
| Task overview | yes | three white task cards |
| Dataset table | yes | rounded table with #f8fafc header |
| Sample explorer | yes | segmented tabs and a carousel with round steel-blue buttons |
| Embedded dataset viewer | yes | Hugging Face iframes inside cards |
| Results | yes | tables and framed figures |
| BibTeX | yes | dark slate block |
| Footer | yes | dark slate band with white text |

## Adapting to Other Content

- **Fewer authors**: keep the name-tag chips; with three to five names the chip row reads as a single line at 17.28px.
- **A results table**: use `.table` (16px cells, 16px padding, #f8fafc header with 600 #1e293b text, 1px #e2e8f0 rows, 8px radius, soft shadow) inside a white card; highlight the best value 700 #1e293b, not with colour.
- **No cover art**: let the left column span the hero, keep the floating shapes, and move the main figure into the About card as a framed 800px image.
- **News**: add more gradient badges in the meta row (one per announcement), each 16.8px / 600 #2d6fa3 on the blue-to-yellow pill.
- **More tasks or stats**: extend the task grid (auto-fit, min 320px) rather than adding new card styles.

## Do's and Don'ts

- Do wear authors and affiliations as rounded tinted chips with emoji markers.
- Do use the sky-to-steel 135deg gradient for every primary button.
- Do keep the hero background pale with translucent floating shapes behind the content.
- Do use Space Grotesk only for display titles and Inter for everything else.
- Don't make the chip tints opaque; they rely on 7–10% alpha over the pale gradient.
- Don't use saturated solid colours on cards; colour belongs to the cover image, badges and shapes.
- Don't let tab buttons fall back to Arial if rebuilding; set `font: inherit`.

## Surfaces

Page #f8fafc; hero gradient #f8fafc → #f1f5f9 with translucent shapes; translucent white navbar with blur; white cards, tables and tab bars with 1px #e2e8f0 borders and light shadows; dark #1e293b BibTeX and footer.

## Imagery

A violet-to-pink gradient cover with wavy lines, a globe, language glyphs (A, 文, अ) and browser-window icons; a colour-framed overview figure (green, blue and magenta panels); website screenshots and mockups in the sample carousel; Hugging Face dataset viewers. Emoji serve as icons on buttons, chips and features.

## Layout

Two-column hero (text left, cover right), then centred section titles over full-width white cards inside a 1300px container. About 10,200px tall at 1440 with the embedded viewers.

## Agent Prompt Guide

Quick colors: steel blue #2d6fa3, sky #a3d8fd, light blue #7db7ff, slate #1e293b, text #334155, muted #64748b, page #f8fafc, border #e2e8f0, badge #e0f2fe → #fef9c3.

1. "Build a two-column hero on linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%) with a 56px gap: left column (max 800px) with a 17.6px / 600 #7db7ff venue label, a pill badge (linear-gradient(90deg, #e0f2fe 0%, #fef9c3 100%), 16.8px / 600 #2d6fa3, radius 16px), an Inter 33.6px / 700 #1e293b title at line-height 1.15, author name tags (rgba(59,130,246,0.07), radius 19px, padding 3px 16px, 17.28px / 500 #1e293b) and a 17.28px #334155 description; right column a 400×600 cover image with a 16px radius."
2. "Make glossy pill buttons: padding 12px 28px, radius 2em, background linear-gradient(135deg, #a3d8fd 10%, #2d6fa3 90%), #ffffff 16.8px / 600 Inter with a leading emoji, box-shadow 0 2px 8px rgba(30, 41, 59, 0.08); hover reverses the gradient and uses 0 4px 16px rgba(30, 41, 59, 0.12)."
3. "Create a content section: padding 40px 0 32px; centred Space Grotesk 32px / 700 #1e293b title; 17.6px #64748b subtitle max 600px; a white card with 1px #e2e8f0 border, radius 12px, padding 32px, shadow 0 1px 3px rgba(0, 0, 0, 0.1); segmented tabs in a white bar where the active tab is #1e293b with white text."

## Similar Pages

- Benchmark pages styled like SaaS landing pages, with a cover image and animated background shapes.
- Multilingual or multimodal dataset pages that list authors as chips with emoji affiliation markers.

## Quick Start

```css
:root {
  --primary-color: #2d6fa3;
  --sky: #a3d8fd;
  --meta: #7db7ff;
  --secondary-color: #1e293b;
  --text-color: #334155;
  --text-light: #64748b;
  --bg-color: #f8fafc;
  --hero-end: #f1f5f9;
  --white: #ffffff;
  --border-color: #e2e8f0;
  --badge-a: #e0f2fe;
  --badge-b: #fef9c3;
  --accent-color: #8b5cf6;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-display: "Space Grotesk", sans-serif;
  --container-width: 1300px;
  --border-radius: 8px;
  --border-radius-lg: 12px;
  --border-radius-xl: 16px;
  --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

## Provenance

- **URL**: https://webmmu-paper.github.io/
- **Paper**: WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation (arXiv 2508.16763), Rabiul Awal and colleagues (ServiceNow, Mila, Université de Montréal, McGill, ÉTS, Polytechnique Montréal).
- **Venue**: EMNLP 2025; the page also notes a Spotlight at the MAR workshop at CVPR 2025.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: none stated; a custom build; footer reads "© 2025 WebMMU Benchmark. All rights reserved."
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, a browser probe at 1440px, and `style.css` and `index.html` read directly, on 2026-10-28.
