# DAWN — Style Reference

> A frosted lab clipboard floating over a sky-and-teal haze, with a pulsing acceptance badge clipped to the top.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero, summary cards, pipeline strip, abstract and demo cards), the 1440×900 and full-page screenshots, and the page's three inline `<style>` blocks and inline element styles read directly. Fonts load from Google Fonts: IBM Plex Sans 400–700 and Space Grotesk 700 (the declared 500 face is never used). Many demo elements carry old inline colours (#4A90E2, #fff, #f8f9ff) that attribute-selector rules in the stylesheet override with `!important`; the overridden values are what render and what is listed below.

## Overview

The whole page is one large frosted card. Behind it, two 40vmax blurred blobs drift slowly (sky blue at the top left, teal at the bottom right, 30% opacity) on white. The card is 1240px wide, white at 74% with a 12px backdrop blur, a 24px radius, a faint slate hairline and a soft drop shadow. Inside, everything is centred. The title is two-tone: "Pixel Motion Diffusion" in a sky → teal → cyan gradient and "is What We Need for Robot Control" in near-black #0f172a, both in Space Grotesk 48px bold with tight tracking. Below sit a gradient "DAWN" acronym, an author panel (pale sky tint, 14px radius) with sky-blue author links, an italic grey affiliation and a teal "*Equal contribution" pill, then a glowing sky-gradient "ACCEPTED · CVPR 2026" capsule that gently bobs. Three coloured pill buttons follow: arXiv red Paper, GitHub charcoal Code and blue Videos, each with a white circular icon badge. The teaser figure, a one-line TL;DR, three left-aligned component cards (sky-blue titles), a numbered three-step process strip and a sky-tinted abstract panel complete the first part. The demo section uses white frosted cards with a sky-tinted "Task Goal:" header bar and monospace goal chips over wide videos.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 47.4% plus #fdfefe 12.4%, #fffffc 1.1%, #fffeff 0.3% (card and page); sky haze #f7fbfd 12.7% and #eff9fc 9.8% (the blurred blob and the author panel tint); teaser figure greens and greys #dae0d4 8.4%; text and figure darks #72777b 7.9%. The coloured buttons and gradient title are too small to cluster.

Anatomy in DOM order (desktop 1440px; card 1240px at x=100, inner content 1164px at x=138):

1. **Page card** (`.container`, y=40 to the page end): rgba(255,255,255,0.74), backdrop blur 12px, 24px radius, 1px rgba(15,23,42,0.1), shadow 0 14px 36px -14px rgba(15,23,42,0.28), padding 35.2px 36.8px 44.8px.
2. **Title** (`h1`, y=108, two lines, 122px): Space Grotesk 48px/700, letter-spacing -1.92px (-0.04em), #0f172a; the lead phrase is `.langtomo-highlight` gradient text (#0ea5e9 → #0d9488 → #06b6d4) with 4px side padding. Gap 20px.
3. **Acronym** (`h2`, y=250): "DAWN" IBM Plex Sans 24px/700 in the same gradient. Gap 20px.
4. **Author panel** (`.authors`, y=302–443, 920px at x=260): rgba(14,165,233,0.05) fill, 1px rgba(14,165,233,0.16), 14px radius, padding 14.4px 16px. Names IBM Plex Sans 17.6px/500 #0ea5e9, separators #1e293b; affiliation 17.6px italic #475569 at y=358; "*Equal contribution" pill at y=395: 13.76px/600 #0f766e on rgba(13,148,136,0.12), 1px rgba(13,148,136,0.3), 999px radius, padding 4.16px 11.52px. Gap 20px.
5. **Venue capsule** (`.venue-pill`, y=463, 228×45): IBM Plex Sans 18.24px/800 #f8fdff, text-shadow 0 1px 1px rgba(0,0,0,0.24), gradient 115° #0284c7 → #0ea5e9 → #22d3ee, 1px rgba(2,132,199,0.42), 999px radius, padding 9.28px 19.52px, shadow 0 16px 32px -18px rgba(2,132,199,0.8); a `::before` "ACCEPTED" chip (11.5px/700 uppercase, rgba(255,255,255,0.24) fill, 1px rgba(255,255,255,0.44)); a 2px up-and-down `badgePulse` animation. Gap 24px.
6. **Buttons** (y=532, 45px tall, 12.8px gaps): Paper #b31b1b, Code #24292e, Videos #4a90e2; white 16px/500, 999px radius, 1px rgba(255,255,255,0.2), shadow 0 10px 24px -16px rgba(15,23,42,0.45); icon in a 24px white circle (Paper, Videos) or a white GitHub SVG (Code), 8px gap. Gap 35px.
7. **Teaser** (`.teaser-figure img`, y=612, 980×441 at x=230): 8px radius, 1px rgba(15,23,42,0.1), shadow 0 20px 40px -28px rgba(15,23,42,0.65); its top 288px is above the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Ink | #0f172a | --text-primary | title, section headings, pipeline step labels, task-goal chips |
| Slate | #1e293b | --text-secondary | author separators, abstract text, card text, TL;DR |
| Muted Slate | #475569 | --text-muted | affiliation |
| Sky | #0ea5e9 | --accent-blue | author links, summary card titles, "Task Goal:" labels, gradient start, panel tints |
| Teal | #0d9488 | --accent-teal | gradient middle, contribution pill tint, author link hover |
| Cyan | #06b6d4 | --accent-cyan | gradient end |
| Deep Teal | #0f766e | (literal) | contribution pill text |
| Deep Sky | #0284c7 | (literal) | venue capsule gradient start and border |
| Bright Cyan | #22d3ee | (literal) | venue capsule gradient end |
| arXiv Red | #b31b1b | (inline) | Paper button |
| GitHub Charcoal | #24292e | (inline) | Code button |
| Video Blue | #4a90e2 | (inline) | Videos button |
| Glass | rgba(255,255,255,0.74) | --glass-bg | page card, demo cards |
| Glass Edge | rgba(15,23,42,0.1) | --glass-border | card, summary card, teaser borders |
| Sky Tint | rgba(14,165,233,0.06) | (literal) | pipeline strip fill (author panel 0.05, abstract 0.04, task header 0.08) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Space Grotesk', IBM Plex Sans… | Space Grotesk 700 | Sora |
| Body | 'IBM Plex Sans', system-ui, -apple-system, sans-serif | IBM Plex Sans 400, 500, 600, 700 | Source Sans 3 |
| Task chips | inline 'Courier New', monospace | Courier New | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1` | 3rem = 48px / 700, letter-spacing -0.04em | #0f172a with gradient lead phrase |
| Acronym | `h2` (first) | 24px / 700 | gradient |
| Section heading | `h2[style*="color: #4A90E2"]` | 2rem = 32px / 700 Space Grotesk, letter-spacing -0.02em | #0f172a |
| Subsection heading | `h3[style*="color: #4A90E2"]` | 1.72rem = 27.52px / 700 Space Grotesk | #0f172a |
| Abstract heading | `.abstract h2` | 24px / 700 Space Grotesk | #0f172a |
| Authors | `.authors` | 1.1rem = 17.6px / 400, links 500 / 1.6 | #0ea5e9 links |
| Venue capsule | `.venue-pill` | 1.14rem = 18.24px / 800 | #f8fdff |
| Buttons | `.paper-button` | 16px / 500 | #ffffff |
| Summary card title | `.summary-card h3` | 16px / 700 | #0ea5e9 |
| Summary card text | `.summary-card p` | 0.93rem = 14.88px / 400 / 1.55 | #1e293b |
| Pipeline step | `.pipeline-step` | 0.9rem = 14.4px / 1.5; label 14.72px / 700 | #1e293b, label #0f172a |
| Abstract | `.abstract p` | 1.1rem = 17.6px / 400 / 1.8, justified | #1e293b |
| Task goal | demo header `p` | 20px / 500 | #0ea5e9; chip #0f172a Courier New |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Page card | 24px | 1px rgba(15,23,42,0.1) | 0 14px 36px -14px rgba(15,23,42,0.28) |
| Author panel | 14px | 1px rgba(14,165,233,0.16) | none |
| Contribution pill | 999px | 1px rgba(13,148,136,0.3) | none |
| Venue capsule | 999px | 1px rgba(2,132,199,0.42) | 0 16px 32px -18px rgba(2,132,199,0.8) |
| Buttons | 999px | 1px rgba(255,255,255,0.2) | 0 10px 24px -16px rgba(15,23,42,0.45) |
| Teaser image | 8px | 1px rgba(15,23,42,0.1) | 0 20px 40px -28px rgba(15,23,42,0.65) |
| Summary cards | 14px | 1px rgba(15,23,42,0.1) | 0 10px 26px -22px rgba(15,23,42,0.45) |
| Pipeline strip | 14px | 1px rgba(14,165,233,0.22) | none |
| Abstract panel | 16px | 1px rgba(14,165,233,0.16) | none |
| Demo cards | 12px | 1px rgba(15,23,42,0.1) | 0 14px 36px -14px rgba(15,23,42,0.28) |
| Task-goal chip | 4px | 1px rgba(15,23,42,0.14) | none |
| Demo videos | 8px | 1px rgba(14,165,233,0.14) | 0 10px 28px -16px rgba(15,23,42,0.5); hover lifts 2px |

## Layout Metrics

- **Page card**: `max-width: min(1240px, 95%)`, centred (x=100 at 1440), inside `.content-section` padding 40px 0 48px; inner width 1164px.
- **Measures**: author panel 920px; teaser, summary grid, pipeline strip and abstract 980px (x=230); hero lede 74ch.
- **Rhythm**: buttons margin 24px 0 35.2px; summary grid margin 25.6px auto 16px; pipeline strip 16px below; abstract margin 32px auto, padding 22.4px 24px.
- **Grids**: summary cards 3 columns, gap 13.6px (318px each); pipeline steps 3 columns, gap 12px.
- **Demo cards**: 1068px wide with a 66px tinted header (padding 19.2px, 1px rgba(14,165,233,0.2) bottom rule) and a 10px-padded video grid; sections 48px apart.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1305px | (100% − 1240px)/2 | 16px | 48px | summary and pipeline 3 columns |
| ≤1305px | 2.5% each side (card 95%) | 16px | 48px | — |
| ≤768px | 2.5%; card padding 24px 16px | 16px | 35.2px | summary cards and pipeline steps stack to one column; venue capsule 16px; demo rows stack with vertical arrows |

## Components

- **Frosted page card**: everything sits on one `.container` card, rgba(255,255,255,0.74), blur(12px), 24px radius, slate hairline, soft shadow; the drifting body blobs show through as a faint sky and teal wash.
- **Gradient phrase** (`.langtomo-highlight`): `background: linear-gradient(90deg, #0ea5e9, #0d9488, #06b6d4)` clipped to text, 600 weight, 4px side padding; a 2px gradient underline wipes in on hover.
- **Author panel** (`.authors`): sky tint 0.05, 1px sky 0.16, 14px radius, centred 17.6px text, links 500 sky with teal underline on hover; affiliation italic #475569; teal contribution pill beneath.
- **Venue capsule** (`.venue-pill`): see First Viewport; it carries its own "ACCEPTED" mini chip and a slow 2px bob.
- **Brand-coloured button** (`.paper-button`): 999px pill, padding 9.6px 24px, 16px/500 white, brand fill (#b31b1b, #24292e, #4a90e2), 1px rgba(255,255,255,0.2), soft dark shadow, icon in a 24px white circle; hover lifts 1px and brightens 5%.
- **Summary card** (`.summary-card`): rgba(255,255,255,0.75), 1px rgba(15,23,42,0.1), 14px radius, padding 15.2px 16px, left-aligned; 16px/700 #0ea5e9 title, 14.88px #1e293b text.
- **Process strip** (`.pipeline-strip`): sky-tinted 14px-radius band with three left-aligned steps; bold "1. Inputs" style labels in #0f172a and 14.4px #1e293b descriptions.
- **Abstract panel** (`.abstract`): sky tint 0.04, 1px sky 0.16, 16px radius, justified 17.6px/1.8 #1e293b text, bold acronym letters, italic 500 emphasis.
- **Demo card**: frosted 12px-radius card; header band rgba(14,165,233,0.08) with "Task Goal:" in 20px/500 #0ea5e9 and the goal in a Courier New chip (rgba(15,23,42,0.06), 1px rgba(15,23,42,0.14), 4px radius); videos below with 8px radius and sky hairlines.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | absent from the source | no navbar; a separate videos.html is linked from a button |
| Title / acronym | yes | two-tone Space Grotesk title, gradient acronym |
| Authors / affiliation | yes | tinted panel with contribution pill |
| Venue | yes | animated gradient "ACCEPTED · CVPR 2026" capsule |
| Link buttons | yes | three brand-coloured pills |
| Teaser | yes | wide method figure with a TL;DR line under it |
| Component cards | yes | three summary cards |
| Process strip | yes | numbered three-step band |
| Abstract | yes | sky-tinted panel |
| Demonstrations | yes | frosted demo cards with task-goal headers and wide videos (bimanual, real world, CALVIN) |
| Results tables | absent from the source | a `.results-section` table style exists only in a mobile rule; no table is rendered |
| BibTeX | absent from the source | none on the page |
| Footer | absent from the source | the card ends the page |

## Adapting to Other Content

- **More authors**: the author panel wraps inside its 920px measure; keep names 17.6px/500 sky and add affiliations as more italic #475569 lines.
- **A results table**: put it inside a summary-card shell at 980px: 14px radius, 1px rgba(15,23,42,0.1); header 14.72px/700 #0f172a on rgba(14,165,233,0.06); body 14.88px #1e293b; best values bold #0d9488.
- **More components**: extend the summary grid in threes; keep the sky title colour.
- **BibTeX or news**: a 980px panel styled like the abstract (sky tint 0.04, 16px radius) with 14px IBM Plex Mono text.
- **A navbar**: if one is needed, make it a frosted strip in the same glass recipe (rgba(255,255,255,0.74), blur 12px, 1px rgba(15,23,42,0.1)) and keep links #0f172a with sky hover.

## Do's and Don'ts

- Do keep the whole page inside one frosted 24px-radius card over the drifting sky and teal blobs.
- Do set titles in Space Grotesk 700 with negative tracking and body in IBM Plex Sans.
- Do use the sky → teal → cyan gradient only on the lead phrase, acronym and venue capsule.
- Don't use flat Bulma buttons; buttons are brand-coloured 999px pills with white icon circles.
- Don't leave inline legacy colours (#4A90E2 headings, #fff cards) unstyled; the stylesheet maps them to slate ink and glass.
- Don't add hard section dividers; tinted panels and cards separate content.

## Surfaces

White page with two blurred colour blobs, one large frosted card, pale sky-tinted panels (author block, pipeline strip, abstract, demo headers), white summary and demo cards.

## Imagery

A colour-coded method diagram (yellow observation box, orange dashed model box, green and pink modules) beside a photo of a robot arm, then wide three-panel demo videos (RGB, predicted pixel motion as orange dot fields, overlay) and CALVIN simulation clips.

## Layout

One centred card: title block, buttons, teaser with TL;DR, summary cards, process strip, abstract, Demonstrations (bimanual, real world, CALVIN). About 6,780px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: ink #0f172a, text #1e293b, muted #475569, sky #0ea5e9, teal #0d9488, cyan #06b6d4, capsule #0284c7 → #22d3ee, buttons #b31b1b / #24292e / #4a90e2, glass rgba(255,255,255,0.74).

1. "Wrap the page in a frosted card: max-width min(1240px, 95%), margin 0 auto, padding 35.2px 36.8px 44.8px, background rgba(255,255,255,0.74), backdrop-filter blur(12px), border 1px solid rgba(15,23,42,0.1), radius 24px, box-shadow 0 14px 36px -14px rgba(15,23,42,0.28). Title Space Grotesk 48px/700, letter-spacing -0.04em, #0f172a, with the lead phrase as gradient text linear-gradient(90deg, #0ea5e9, #0d9488, #06b6d4)."
2. "Make a venue capsule: inline-flex, gap 8.8px, padding 9.28px 19.52px, 999px radius, IBM Plex Sans 18.24px/800 #f8fdff, background linear-gradient(115deg, #0284c7, #0ea5e9 40%, #22d3ee 90%), 1px rgba(2,132,199,0.42) border, box-shadow 0 16px 32px -18px rgba(2,132,199,0.8), with a ::before 'ACCEPTED' chip in rgba(255,255,255,0.24) and a slow 2px vertical bob."
3. "Build three summary cards in a 3-column grid with 13.6px gaps, max-width 980px: each rgba(255,255,255,0.75), 1px rgba(15,23,42,0.1), 14px radius, padding 15.2px 16px, left-aligned; title IBM Plex Sans 16px/700 #0ea5e9; text 14.88px/1.55 #1e293b."

## Similar Pages

- Single-card "glass" project pages with gradient titles and brand-coloured link pills.
- Robot-learning pages that pair a method figure with task-goal video cards.

## Quick Start

```css
:root {
  --bg-primary: #ffffff;
  --text-primary: #0f172a;
  --text-secondary: #1e293b;
  --text-muted: #475569;
  --accent-blue: #0ea5e9;
  --accent-teal: #0d9488;
  --accent-cyan: #06b6d4;
  --gradient-text: linear-gradient(90deg, #0ea5e9, #0d9488, #06b6d4);
  --glass-bg: rgba(255, 255, 255, 0.74);
  --glass-border: rgba(15, 23, 42, 0.1);
  --glass-shadow: 0 14px 36px -14px rgba(15, 23, 42, 0.28);
  --font-main: 'IBM Plex Sans', system-ui, -apple-system, sans-serif;
  --font-display: 'Space Grotesk', 'IBM Plex Sans', sans-serif;
}
body { margin: 0; font-family: var(--font-main); color: var(--text-primary); background: var(--bg-primary); }
.container { max-width: min(1240px, 95%); margin: 0 auto; text-align: center; background: var(--glass-bg); backdrop-filter: blur(12px); border: 1px solid var(--glass-border); border-radius: 24px; box-shadow: var(--glass-shadow); }
```

## Provenance

- **URL**: https://eronguyen.me/DAWN/ (the arXiv link https://eronguyen.github.io/DAWN redirects here)
- **Paper**: Pixel Motion Diffusion is What We Need for Robot Control (arXiv 2509.22652), E-Ro Nguyen, Yichi Zhang, Kanchana Ranasinghe, Xiang Li, Michael S. Ryoo.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states acceptance at CVPR 2026 and links the project page.
- **Template credit**: none credited; a hand-written page with inline styles (the gradient class name `langtomo-highlight` suggests reuse from the authors' earlier LangToMo page).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and components, the 1440×900 and full-page screenshots, and the inline styles read directly, on 2026-10-28.
