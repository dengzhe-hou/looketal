# DIMO — Style Reference

> A night sky of latent space that opens onto white paper: a blue-violet-pink spectrum traces the title, the trajectories and a single hairline across the top.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, viewport screenshots taken after scrolling to y=900, 1700, 3100, 3900, 4600 and 5300, and the page's own `css/style.css`, `fonts/fonts.css` and `index.html`. The stored full-page screenshot is not usable for the body: its capture stretches the `min-height: 100svh` hero to the whole canvas, so the body sections were checked on the scrolled viewport shots instead. Videos in the Applications section load lazily, so section y-positions grow after load (the render measured the page at 5,934px). "Theme: both" here means a dark hero over a light body, not a theme toggle.

## Overview

A two-part page. The first screen is a full-height dark "latent space" hero (#0b0e14) lit by three soft radial glows (violet top-right, pink bottom-right, blue left), with a 3px spectrum hairline at the very top. On the left, a mono pill eyebrow "● ICCV 2025 HIGHLIGHT", a large Space Grotesk wordmark "DIMO", a three-line subtitle whose first and last lines are filled with the blue → violet → pink spectrum, an italic Newsreader serif lede, authors, mono affiliations and ghost pill buttons. On the right, an animated inline SVG: a single-image node, a glowing violet manifold labelled "LATENT SPACE Z", and trajectories that decode into five dancing stick figures. Below the hero the page turns into a light paper body: sections alternate white and #f5f6f8 with no rules, each opened by a mono kicker with a 22px spectrum dash and a 34.4px Space Grotesk title; prose is set in Newsreader serif, captions in Space Mono; media sit in 14px-radius frames; the BibTeX block is a dark #0b0e14 panel; the footer is two mono lines. A fixed side "trajectory" nav appears only on screens wider than 1480px.

## First Viewport

Color share (quantized 1440×900 shot): the whole viewport is dark: #0b0e14 38.4%, violet-tinted #141320 35.0%, #2c2a42 11.6% (the violet glow and manifold), #0e0f17 9.8%, plus #0b0f16, #080b11, #0b0e13 and #090e16 at 0.2–2.6%. Spectrum text and white type are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `.container` content box x=234 to 1206; copy column x=234 to 803, figure column x=843 to 1206):

1. **Spectrum hairline** (`body::before`, y=0–3): 3px `linear-gradient(90deg, #3b82f6, #8b5cf6, #ff5c8a)` across the full width.
2. **Hero** (`header.hero`, y=3–903): min-height 100vh, flex, content vertically centred; `.hero__inner` padding 56px 0; grid 1.22fr / 0.78fr with a 40px gap.
3. **Eyebrow pill** (y=129, 38px tall): Space Mono 13.12px uppercase, letter-spacing 0.18em, #f4f6fa; padding 7px 14px 7px 12px; 1px rgba(255,255,255,0.12) border; rgba(255,255,255,0.04) fill; 999px radius; a 7px #ff5c8a dot with `box-shadow: 0 0 12px var(--pink)`; "HIGHLIGHT" 700 filled with `linear-gradient(90deg, var(--violet), var(--pink))`. Gap 22px.
4. **Wordmark** (`.hero__name`, y=189): "DIMO" Space Grotesk 82.8px/700, line-height 0.95, letter-spacing -0.045em, #f4f6fa. Gap 14.9px (0.18em).
5. **Subtitle lines** (y=283, 333, 383): 45.26px/700, line-height 1.1, letter-spacing -0.03em; "Diverse 3D Motion" and "Arbitrary Objects" clipped to the spectrum gradient, "Generation for" in #f4f6fa. Title block ends at y=432; gap 22px.
6. **Lede** (y=454–524): Newsreader 24px italic, line-height 1.45, #f4f6fa, max 34rem. Gap 30px.
7. **Authors** (y=554): Inter 14.72px, line-height 1.7, #f4f6fa, each name with a 1px rgba(255,255,255,0.12) bottom border (hover #ff5c8a). Gap 6px.
8. **Affiliations** (y=588–637): Space Mono 13.12px #9aa3b2, two lines (affiliations, corresponding-author note). Gap 30px.
9. **Buttons** (`nav.links`, y=667): arXiv, Poster, YouTube, Code in row one; "Latest Work: UniMate" (spectrum-tinted) wraps to row two at y=727; each 50px tall, gaps 10px.
10. **Hero figure** (right column, centred at y≈380): inline SVG, `transform: translateX(34px) scale(1.18)` from the right centre, so it reaches past the container edge to about x=1240. Labels in Space Mono 13px uppercase #aeb6c4 ("SINGLE IMAGE", "LATENT SPACE Z", "DIVERSE MOTIONS"; "DECODE" in #c9b6f0).

The first light section starts at y=903, exactly at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Space | #0b0e14 | --space | hero background, html background, BibTeX panel |
| On Space | #f4f6fa | --on-space | hero type, button text, BibTeX code, SVG origin strokes and joints |
| On Space Mute | #9aa3b2 | --on-space-mute | hero affiliations |
| Dark Hairline | rgba(255,255,255,0.12) | --hairline-dark | eyebrow and button borders, author underlines, BibTeX border |
| Paper | #ffffff | --paper | body background, white sections, side-nav node fill |
| Paper 2 | #f5f6f8 | --paper-2 | alternating sections (`.section--alt`), media backgrounds |
| Ink | #0e1320 | --ink | section titles, bold prose, caption bold, footer links |
| Prose | #2b3340 | (literal, `.prose p`) | serif paragraphs |
| Mute | #6b7280 | --mute | kickers, captions, footer text, side-nav labels |
| Line | #e6e8ec | --line | media borders, footer top rule, side-nav track |
| Blue | #3b82f6 | --blue | spectrum start (title words, hairline, kicker dash), blue glow |
| Violet | #8b5cf6 | --violet | spectrum middle, body links, focus outline, violet glow, Latest Work border |
| Pink | #ff5c8a | --pink | spectrum end, eyebrow dot, author hover underline, pink glow |
| Label Gray | #aeb6c4 | (literal, SVG) | hero figure labels |
| Decode Lilac | #c9b6f0 | (literal, SVG) | "DECODE" label in the hero figure |
| Manifold Grid | rgba(190,198,224,0.24) | (literal, SVG) | grid lines on the hero manifold; the dashed encode line uses rgba(174,182,196,0.45) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | "Space Grotesk", system-ui, sans-serif | Space Grotesk 700 (self-hosted) | Archivo |
| Body / UI | "Inter", system-ui, sans-serif | Inter 400, 600 | Inter |
| Serif (lede, prose) | "Newsreader", Georgia, "Times New Roman", serif | Newsreader 400, 400 italic, 600 | Source Serif 4 |
| Mono (labels, captions, code) | "Space Mono", ui-monospace, monospace | Space Mono 400, 700 | IBM Plex Mono |
| Icons | Font Awesome 4.7, Academicons | FontAwesome, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark | `.hero__title .hero__name` | 1.5em of 55.2px = 82.8px / 700 / 0.95, letter-spacing -0.045em | #f4f6fa |
| Hero subtitle | `.hero__title .word`, `.hero__plain` | 0.82em = 45.26px / 700 / 1.1, letter-spacing -0.03em | spectrum gradient / #f4f6fa |
| Hero title base | `.hero__title` | clamp(2.3rem, 4.4vw, 3.45rem) → 55.2px | — |
| Lede | `.hero__lede` | clamp(1.2rem, 1.9vw, 1.5rem) → 24px / 400 italic / 1.45, Newsreader | #f4f6fa |
| Eyebrow | `.hero__eyebrow` | 0.82rem = 13.12px Space Mono, uppercase, letter-spacing 0.18em | #f4f6fa |
| Authors | `.hero__authors` | 0.92rem = 14.72px / 400 / 1.7 | #f4f6fa |
| Affiliations | `.hero__affil` | 13.12px Space Mono / 1.7 | #9aa3b2 |
| Button | `.btn` | 0.95rem = 15.2px / 600 | #f4f6fa |
| Section title | `.section-title` | clamp(1.6rem, 3.2vw, 2.15rem) → 34.4px / 700 / 1.1, letter-spacing -0.02em | #0e1320 |
| Kicker | `.kicker` | 0.78rem = 12.48px Space Mono, uppercase, letter-spacing 0.2em | #6b7280 |
| Prose | `.prose p` | 1.18rem = 20.06px / 400 / 1.72, Newsreader | #2b3340, bold 600 #0e1320 |
| Body | `body` | 17px / 400 / 1.7, Inter | #0e1320 |
| Caption | `.caption` | 0.95rem = 15.2px Space Mono / 1.6, letter-spacing 0.02em | #6b7280, bold #0e1320 |
| BibTeX | `.cite code` | 0.82rem = 13.12px Space Mono / 1.7 | #f4f6fa |
| Footer | `.footer p` | 12.48px Space Mono, letter-spacing 0.06em | #6b7280 |
| Side-nav label | `.sidenav__label` | 11.5px Space Mono, uppercase, letter-spacing 0.13em | #6b7280; active #0e1320 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Eyebrow, buttons | 999px | 1px rgba(255,255,255,0.12) | none; Latest Work `0 0 18px color-mix(in srgb, var(--violet) 16%, transparent)` |
| Media frames (video, figures, YouTube embed) | 14px | 1px #e6e8ec | `0 1px 2px rgba(14, 19, 32, 0.04)`; hover `0 18px 40px rgba(14, 19, 32, 0.12)` with translateY(-3px) |
| BibTeX panel | 14px | 1px rgba(255,255,255,0.12) | none |
| Eyebrow dot | 50%, 7px | none | `0 0 12px var(--pink)` |
| Side-nav node | 50%, 11px | 2px #e6e8ec | `0 0 0 5px var(--paper)`; active `0 0 0 5px var(--paper), 0 0 12px rgba(139, 92, 246, 0.45)` |
| Kicker dash | 0 | 22×2px spectrum bar | none |
| Footer | 0 | 1px #e6e8ec top | none |

SVG glow filters in the hero figure: latent points `drop-shadow(0 0 7px var(--violet))`, keypoints `drop-shadow(0 0 6px currentColor)`, bones and heads `drop-shadow(0 0 4px currentColor)`.

## Layout Metrics

- **Container**: `.container { max-width: 1020px; margin: 0 auto; padding: 0 24px }` → content box x=234 to 1206 (972px) at 1440.
- **Hero**: min-height 100vh (100svh); background quoted literally: `radial-gradient(900px 520px at 78% 12%, rgba(139, 92, 246, 0.22), transparent 60%), radial-gradient(700px 480px at 96% 90%, rgba(255, 92, 138, 0.16), transparent 60%), radial-gradient(700px 520px at 4% 20%, rgba(59, 130, 246, 0.16), transparent 60%), var(--space)`. Inner grid 1.22fr / 0.78fr (≈569px / 363px), gap 40px, padding 56px 0; content block y=129 to 777, centred in the 900px hero.
- **Sections**: padding 52px 0; kicker margin-bottom 10px; title margin-bottom 24px; alternating white and #f5f6f8 is the only separator.
- **Media**: full container width (972px); a caption followed by another media block gets a 40px gap; figures margin-bottom 22px.
- **BibTeX**: padding 26px 28px, full container width.
- **Footer**: padding 36px 0 56px, 1px #e6e8ec top border.
- **Side nav**: fixed, vertically centred, right edge 88px left of the content column (`left: calc((100vw - 1020px) / 2 - 88px)`, translated -100%); items 11px apart.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1480px | 24px inside 1020px | 17px | 55.2px base (wordmark 82.8px) | side "trajectory" nav shown after scrolling past the hero |
| ≤1480px | same | 17px | same | side nav hidden (this includes 1440) |
| ≤1255px | same | 17px | 4.4vw (e.g. 45px at 1024) | — |
| ≤860px | same | 17px | 4.4vw, floor 36.8px | hero becomes one column, gap 36px, padding 72px 0 64px; figure moves below the copy, max 520px, no transform |
| ≤520px | same | 17px | 36.8px | buttons padding 10px 16px, 14.4px text; link gap 9px |

## Components

- **Eyebrow pill** (`.hero__eyebrow`): inline-flex, gap 9px, padding 7px 14px 7px 12px, 999px radius, rgba(255,255,255,0.04) fill, 1px rgba(255,255,255,0.12) border, Space Mono 13.12px uppercase with 0.18em tracking; leading 7px #ff5c8a glowing dot; the highlighted word clipped to `linear-gradient(90deg, var(--violet), var(--pink))`.
- **Spectrum title words** (`.hero__title .word`): `background: var(--spectrum); background-clip: text; color: transparent; width: fit-content`, one phrase per line so the gradient spans each phrase.
- **Ghost button** (`.btn`): inline-flex, gap 9px, padding 11px 17px, 999px radius, rgba(255,255,255,0.04) fill, 1px rgba(255,255,255,0.12) border, Inter 15.2px/600 #f4f6fa, Font Awesome / Academicons icon left. Hover: translateY(-2px), fill rgba(255,255,255,0.1), border rgba(255,255,255,0.28).
- **Latest Work button** (`.btn--latest`): same shape; border `color-mix(in srgb, var(--violet) 62%, transparent)`; background `linear-gradient(105deg, color-mix(in srgb, var(--blue) 14%, transparent), color-mix(in srgb, var(--pink) 14%, transparent))`; glow `0 0 18px color-mix(in srgb, var(--violet) 16%, transparent)`; hover raises both mixes to 22% and the border to pink at 78%.
- **Kicker** (`.kicker`): flex, gap 12px, Space Mono 12.48px uppercase, 0.2em tracking, #6b7280, preceded by a 22×2px spectrum dash ("— DEMO VIDEO", "— METHOD · PIPELINE").
- **Section title**: Space Grotesk 34.4px/700, -0.02em, #0e1320; the Poster section colors "Highlight" with the violet-to-pink gradient.
- **Media frame** (`.media`): 14px radius, 1px #e6e8ec, #f5f6f8 background, tiny shadow; hover lift 3px with a larger soft shadow. YouTube embeds use `.media--embed` with a 16:9 aspect ratio.
- **Caption** (`.caption`): Space Mono 15.2px, line-height 1.6, #6b7280, 14px top margin, bold lead-in in #0e1320.
- **BibTeX panel** (`pre.cite`): #0b0e14, 14px radius, 1px rgba(255,255,255,0.12), padding 26px 28px, Space Mono 13.12px #f4f6fa, no wrap.
- **Side trajectory nav**: 2px #e6e8ec track with a `linear-gradient(180deg, var(--blue), var(--violet), var(--pink))` progress fill; 11px nodes (white, 2px #e6e8ec ring); active node filled `linear-gradient(135deg, var(--blue), var(--pink))`, scaled 1.18 with a violet glow; mono uppercase labels.
- **Hero figure**: animated inline SVG; violet manifold with a glow and a faint grid (`rgba(190, 198, 224, 0.24)` lines), dashed encode line `rgba(174, 182, 196, 0.45)`, colored trajectories at 0.55 opacity, five stick figures (wave, walk, kick, jump, punch) animated with CSS keyframes; reduced-motion freezes them in a pose.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Full-screen dark hero | yes | #0b0e14 with three radial glows and a spectrum hairline |
| Venue / award badge | yes | mono eyebrow pill with glowing pink dot, "HIGHLIGHT" in gradient |
| Title / authors / affiliations | yes | left-aligned; wordmark plus spectrum subtitle; mono affiliations |
| Lede / TL;DR | yes | italic Newsreader 24px sentence |
| Link buttons | yes | ghost pills; one gradient-tinted "Latest Work" pill |
| Hero illustration | yes | animated SVG latent-space diagram |
| Demo video | yes | YouTube embed in a 14px frame |
| Applications videos | yes | autoplay videos in frames with mono captions |
| Abstract | yes | teaser figure then Newsreader prose |
| Method | yes | pipeline figure plus prose on a #f5f6f8 band |
| Poster | yes | poster image in a frame |
| BibTeX | yes | dark #0b0e14 panel |
| Results tables | absent from the source | — |
| Side navigation | present but non-standard | fixed vertical trajectory rail, only above 1480px |
| Footer | yes | two Space Mono lines under a 1px rule |

## Adapting to Other Content

- **More authors**: keep them on 14.72px Inter lines in the 569px copy column; past six names let them wrap to a second line and keep the mono affiliation block below.
- **A results table**: place it in a `.media`-style frame (14px radius, 1px #e6e8ec, white) at 972px; header in Space Mono 12.48px uppercase #6b7280, body Inter 15.2px #0e1320, rules 1px #e6e8ec, best values 600 #8b5cf6. Use a mono caption below.
- **Long publication or news lists**: use rows of Space Mono 12.48px dates (#6b7280) and Inter 17px titles (#0e1320) separated by 1px #e6e8ec rules inside a light section, with a kicker on top.
- **More sections**: alternate white and #f5f6f8; never add borders between them.
- **A light-only page**: the hero is the identity; if it must go, keep the 3px spectrum hairline and the kicker dashes so the spectrum survives.

## Do's and Don'ts

- Do keep the spectrum (#3b82f6 → #8b5cf6 → #ff5c8a) to horizontal runs: title words, the top hairline and kicker dashes.
- Do pair four faces by role: Space Grotesk for display, Newsreader for reading, Inter for UI, Space Mono for labels and captions.
- Do let the hero fill the first screen and keep its type left-aligned beside the figure.
- Do separate body sections only by alternating #ffffff and #f5f6f8.
- Don't use the spectrum as a background fill for large areas; the Latest Work button's 14% tint is the most it gets.
- Don't add rules or cards between body sections.
- Don't set prose in Inter; body paragraphs are serif.

## Surfaces

Dark hero #0b0e14 with radial glows; translucent ghost controls at 4% white; light body in white and #f5f6f8 bands; media frames on #f5f6f8 with 1px #e6e8ec borders; one dark #0b0e14 BibTeX panel that echoes the hero.

## Imagery

A custom animated SVG of a latent manifold and glowing stick figures in the hero; in the body, a YouTube demo with white-background 3D renders, autoplaying videos of object motions, pipeline and teaser figures with colorful 3D characters, and the conference poster.

## Layout

A centred 1020px column throughout. The hero is a two-column grid (copy left, figure right, figure pushed slightly beyond the container); every body section is one column with a kicker, title, media and prose stacked at 52px vertical padding.

## Agent Prompt Guide

Quick colors: space #0b0e14, on-space #f4f6fa, on-space mute #9aa3b2, paper #ffffff, paper 2 #f5f6f8, ink #0e1320, prose #2b3340, mute #6b7280, line #e6e8ec, spectrum #3b82f6 → #8b5cf6 → #ff5c8a.

1. "Build a full-height dark hero: background radial-gradient(900px 520px at 78% 12%, rgba(139,92,246,0.22), transparent 60%), radial-gradient(700px 480px at 96% 90%, rgba(255,92,138,0.16), transparent 60%), radial-gradient(700px 520px at 4% 20%, rgba(59,130,246,0.16), transparent 60%), #0b0e14; a 3px linear-gradient(90deg, #3b82f6, #8b5cf6, #ff5c8a) hairline at the top. Left column: a Space Mono 13.12px uppercase eyebrow pill (rgba(255,255,255,0.04) fill, 1px rgba(255,255,255,0.12) border, 7px #ff5c8a dot); 'DIMO' in Space Grotesk 82.8px/700, letter-spacing -0.045em, #f4f6fa; subtitle lines 45.26px/700 with the key phrases clipped to the spectrum gradient; italic Newsreader 24px lede."
2. "Make ghost pill buttons: padding 11px 17px, radius 999px, rgba(255,255,255,0.04) fill, 1px rgba(255,255,255,0.12) border, Inter 15.2px/600 #f4f6fa with a left icon; hover translateY(-2px), fill rgba(255,255,255,0.1), border rgba(255,255,255,0.28)."
3. "Create light body sections: padding 52px 0, alternating #ffffff and #f5f6f8; a Space Mono 12.48px uppercase #6b7280 kicker with a 22×2px spectrum dash; a 34.4px/700 Space Grotesk title in #0e1320; media in 14px-radius frames with 1px #e6e8ec borders; prose in Newsreader 20.06px/1.72 #2b3340; captions in Space Mono 15.2px #6b7280; BibTeX in a #0b0e14 panel with Space Mono 13.12px #f4f6fa."

## Similar Pages

- Product-launch-style research pages that open with a full-screen dark hero and an animated diagram, then switch to a light reading body.
- Pages that set prose in a serif and labels in a mono face under a geometric display face.

## Quick Start

```css
:root {
  --space: #0b0e14;
  --on-space: #f4f6fa;
  --on-space-mute: #9aa3b2;
  --hairline-dark: rgba(255, 255, 255, 0.12);
  --paper: #ffffff;
  --paper-2: #f5f6f8;
  --ink: #0e1320;
  --mute: #6b7280;
  --line: #e6e8ec;
  --blue: #3b82f6;
  --violet: #8b5cf6;
  --pink: #ff5c8a;
  --spectrum: linear-gradient(90deg, var(--blue), var(--violet), var(--pink));
  --radius: 14px;
  --container: 1020px;
  --display: "Space Grotesk", system-ui, sans-serif;
  --body: "Inter", system-ui, sans-serif;
  --serif: "Newsreader", Georgia, "Times New Roman", serif;
  --mono: "Space Mono", ui-monospace, monospace;
}
```

## Provenance

- **URL**: https://linzhanmou.com/dimo/
- **Paper**: DIMO: Diverse 3D Motion Generation for Arbitrary Objects (arXiv 2511.07409), Linzhan Mou, Jiahui Lei, Chen Wang, Lingjie Liu, Kostas Daniilidis (University of Pennsylvania; Archimedes, Athena RC).
- **Venue**: ICCV 2025 (Highlight, as stated on the page).
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: none; the stylesheet header says it is loaded by this page alone, with one first-party script (`js/nav.js`).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 screenshot, six scrolled viewport screenshots of the body, and `style.css`, `fonts.css` and `index.html` read directly, on 2026-10-28.
