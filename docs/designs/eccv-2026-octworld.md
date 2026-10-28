# OctWorld — Style Reference

> A magazine cover shot at dusk: full-bleed footage, a huge light grotesk headline anchored to the bottom edge, and one coral underline that signs it.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, section heads, gallery cards, method media, abstract and citation), the 1440×900 shot and a full-page capture, and the page's own `styles.css` and `index.html`. The hero background is a rotating set of generated videos that cross-fade (1600ms), so the scene behind the title differs between captures (a concrete underpass in the 1440×900 shot, a Japanese interior in the full-page capture).

## Overview

A dark, cinematic page (8,954px) on #050505 with a faint 48px grid of white hairlines (2.3% white) across the whole body. A 58px sticky header holds the Microsoft logo with a 14px/600 "OctWorld: an open source research project." wordmark and five DM Mono uppercase links. The hero is a full-viewport video (842px at 900px tall) darkened by a vertical gradient; everything is left-aligned and pushed to the bottom: a mono eyebrow with a 22px coral dash, a three-line 79.2px Manrope 400 title whose first word "OctWorld:" carries a thick coral underline, 13px author names with cyan mono superscripts, 10px mono affiliations and two square outlined mono buttons. Below, sections are separated by #262626 rules with 120px padding; each has a mono "01 / VISUAL OVERVIEW" index with the same coral dash and a 48.96px light Manrope headline. Content is video-heavy: two 960px method videos with mono status chips and a pulsing cyan dot, a 2-column gallery of rounded video cards with coral "Generated Video" badges and pill "SHOW 3D MAP" toggles, a 17px gray abstract, a white-framed training-pipeline figure, a BibTeX block on #0b0b0b and a mono footer with Microsoft legal links.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): video footage tones #6f6d6b 17.4%, #524f44 15.2%, #5e594f 12.0%, #423e35 10.2% and #a09f9a 7.6% (concrete, sky and water); near-blacks #050505 13.9% (header), #100f0e 11.7% and #292927 12.0% (the darkened lower hero). Coral and cyan cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px, left-aligned at x=28):

1. **Sticky header** (`header.site-header`, 0–58px): rgba(5,5,5,0.88) with `backdrop-filter: blur(16px)`, 1px #262626 bottom border, padding 0 28px. Left: 30px Microsoft logo + 9px gap + "OctWorld: an open source research project." Manrope 14px/600 #f2f1ec. Right: DM Mono 11px uppercase #8b8b84 links with 26px gaps (Overview, Gallery, Abstract, Method, Citation); hover #ff6b57.
2. **Hero** (`section.intro`, y 58–900): min-height calc(100svh − 58px); video `object-fit: cover` with `filter: saturate(1.02) contrast(1.04) brightness(0.78)`; shade `linear-gradient(180deg, rgba(5, 5, 5, 0.34) 0%, rgba(5, 5, 5, 0.18) 38%, rgba(5, 5, 5, 0.9) 100%)` plus a 48px grid of rgba(255,255,255,0.025) lines. Content column width min(1720px, 100% − 56px), flex column justified to the bottom, padding 16vh 0 9vh (144px / 81px).
3. **Eyebrow** (`p.eyebrow`, y=379): DM Mono 11px uppercase #c4c4bd, a 22×1px #ff6b57 dash and 10px gap before the text. Gap 22px.
4. **Title** (`h1`, y=415, 242px, three lines): Manrope 79.2px/400, line-height 1.02, letter-spacing 0, #f2f1ec, max 1400px, `text-shadow: 0 2px 24px rgba(0, 0, 0, 0.46)`. "OctWorld:" is underlined in #ff6b57 at 0.07em thickness, offset 0.09em. Gap 42px.
5. **Authors** (`.author-list`, y=699): Manrope 13px #e3e2dc, gaps 6px 22px, `text-shadow: 0 1px 12px rgba(0, 0, 0, 0.72)`; superscripts DM Mono 8.45px #58c8c4. Gap 18px.
6. **Affiliations** (`p.affiliations`, y=735): DM Mono 10px/1.8 #b8b8b1 with cyan superscripts. Gap 28px.
7. **Buttons** (`.paper-links a`, y=781, 38px tall, 10px gap): "READ RESEARCH PAPER" and "CODE", DM Mono 10px uppercase #f2f1ec, padding 0 14px, 1px rgba(242,241,236,0.42) border, rgba(5,5,5,0.46) fill with `backdrop-filter: blur(10px)`, square corners, 16px line icon left (document, GitHub mark). Hover: border #ff6b57, fill rgba(255,107,87,0.12), text #ff6b57. Hero bottom padding 81px ends at y=900.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Black | #050505 | --background | body, hero base, scene card backgrounds |
| Surface | #0b0b0b | --surface | BibTeX block |
| Surface Raised | #121212 | --surface-raised | copy button |
| Line | #262626 | --line | header rule, section top rules, method media and figure borders, footer rule |
| Muted | #8b8b84 | --muted | nav links, gallery notes, group headings, footer text |
| Paper Text | #f2f1ec | --text | title, headings, wordmark, button text |
| Coral | #ff6b57 | --accent | title underline, eyebrow and section-index dashes, group numbers, nav and button hover, video badges, copy hover |
| Cyan | #58c8c4 | --cyan | author superscripts, live status dots (with a 10px glow at 72%) |
| Eyebrow Gray | #c4c4bd | (literal) | eyebrow and section-index text |
| Author Gray | #e3e2dc | (literal) | author names |
| Affiliation Gray | #b8b8b1 | (literal) | affiliations |
| Abstract Gray | #bdbdb6 | (literal) | abstract paragraphs |
| Body Gray | #a5a59e | (literal) | method card text and figure caption; `strong` #deddd7 |
| Code Gray | #c7c7c0 | (literal) | BibTeX text |
| Status Gray | #b6b6af | (literal) | media status chips |
| Instruction Gray | #777770 | (literal) | gallery group instructions |
| Grid Line | rgba(255,255,255,0.023) | (literal) | 48px background grid on body (0.025 inside the hero shade) |
| Coral Wash | rgba(255,107,87,0.24) | (literal) | "Generated Video" badge fill (border at 0.42) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / text | "Manrope", sans-serif (self-hosted TTF) | Manrope 400, 500, 600 | Manrope |
| Mono | "DM Mono", monospace (self-hosted TTF) | DM Mono 400 | DM Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `h1` | clamp(42px, 5.5vw, 92px) → 79.2px / 400 / 1.02 | #f2f1ec |
| Section headline | `.section-heading h2` | clamp(31px, 3.4vw, 60px) → 48.96px / 400 / 1.07, max 880px (gallery 760px) | #f2f1ec |
| Eyebrow, section index | `.eyebrow`, `.section-index` | DM Mono 11px / 400 uppercase | #c4c4bd |
| Wordmark | `.wordmark` | 14px / 600 | #f2f1ec |
| Nav | `.site-header nav` | DM Mono 11px uppercase | #8b8b84 |
| Authors | `.author-list` | 13px / 400 | #e3e2dc |
| Affiliations | `.affiliations` | DM Mono 10px / 1.8 | #b8b8b1 |
| Button | `.paper-links a` | DM Mono 10px uppercase | #f2f1ec |
| Method card title | `.method-card h3` | 18px / 500 | #f2f1ec |
| Method text, figure caption | `.method-card p`, `.method-figure figcaption` | 14px / 1.7–1.72 | #a5a59e |
| Gallery group title | `.gallery-group-heading h3` | 20px / 500 | #f2f1ec |
| Group number | `.gallery-group-heading p` | DM Mono 9px uppercase | #ff6b57 |
| Abstract | `.abstract-copy` | 17px / 1.82 | #bdbdb6, terms 500 #f2f1ec |
| Video badge | `.video-mode-badge` | Manrope 10px / 600 / 1.4 | #ffffff |
| Status chip, map toggle | `.media-status`, `.map-toggle` | DM Mono 9px uppercase | #b6b6af / white |
| BibTeX | `pre` | DM Mono 12px / 1.8 | #c7c7c0 |
| Footer | `footer` | DM Mono 11px / 1.7 | #8b8b84 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Hero buttons | 0 | 1px rgba(242,241,236,0.42) | `backdrop-filter: blur(10px)` |
| Method media, figure frame, citation block | 0 | 1px #262626 | none; figure frame is white #ffffff |
| Scene cards | 8px | none | overflow hidden |
| Video badge | 2px | 1px rgba(255,107,87,0.42) | `backdrop-filter: blur(6px)` |
| Map toggle | 9999px | 1px rgba(255,255,255,0.3) | rgba(0,0,0,0.48) fill, `backdrop-filter: blur(4px)` |
| Map inset (when shown) | 0 | 1px rgba(255,255,255,0.48), 3px padding | `0 8px 26px rgba(0, 0, 0, 0.5)` |
| Play toggle, copy button | 50% (30px / 34px) | 1px rgba(255,255,255,0.3) / 1px #262626 | play fades in on hover |
| Map expand button | 2px, 26px | 1px rgba(255,255,255,0.36) | rgba(0,0,0,0.74) fill |
| Status dot | 50%, 6px | none | `0 0 10px rgba(88, 200, 196, 0.72)` |

## Layout Metrics

- **Shell**: `.section-shell, footer { width: min(1720px, calc(100% - 56px)) }` → x 28–1412 (1384px) at 1440; the gallery heading and groups narrow to min(1152px, 100% − 56px) → x 144–1296.
- **Hero**: min-height calc(100svh − 58px) = 842px; content padding 16vh 0 9vh; title block ends 81px above the fold.
- **Sections**: padding 120px 0 with a 1px #262626 top rule; section heading grid minmax(180px, .7fr) / minmax(0, 2.3fr) → index at x=28, h2 at x=351; heading margin-bottom 56px.
- **Method**: grid width min(960px, 100%) centred (x 240–1200), gap 64px; media 16:9 (960×540); titles 22px below media; method figure 80% wide (1107px) with 76px bottom margin, caption 22px below.
- **Gallery**: groups 96px apart; group heading grid 48px / 1fr / auto with 18px bottom padding; scene grid 2 columns, gap 24px → 564px cards (317px tall).
- **Abstract and citation**: 80% of the shell (1107px at x=166); BibTeX padding 28px 72px 28px 28px.
- **Footer**: padding 30px 0 46px, 1px #262626 top, brand left and legal links right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 28px | 16px | 79.2px (5.5vw) | heading grid 0.7fr / 2.3fr; 2-column gallery |
| ≥1673px | 28px, shell capped at 1720px | 16px | 92px cap | none |
| ≤900px | 14px (min(100% − 28px, 720px)) | 16px | 5.5vw, e.g. 49.5px at 900 | header wraps (padding 10px 14px, nav gap 14px); sections 84px; heading grids stack; method figure, abstract and citation 100%; abstract 15px; footer stacks |
| ≤763px | same | 16px | 42px floor | none |
| ≤560px | same | 16px | 38px | two nav links hidden; gallery 1 column; map toggle collapses to a 30px icon; group title 17px; BibTeX 10px |

## Components

- **Mono eyebrow / section index**: flex row, 10px gap, a 22×1px #ff6b57 rule then DM Mono 11px uppercase #c4c4bd text; 22px below to the headline.
- **Underlined title word**: the first `span` of the h1 is #f2f1ec with `text-decoration: underline`, color #ff6b57, thickness 0.07em, offset 0.09em.
- **Glass button** (`.paper-links a`): min-height 38px, padding 0 14px, 9px gap to a 16px stroked icon (1.5px), DM Mono 10px uppercase #f2f1ec, 1px rgba(242,241,236,0.42) border, rgba(5,5,5,0.46) fill with blur(10px), square; hover border #ff6b57, rgba(255,107,87,0.12) fill, #ff6b57 text.
- **Method media**: 16:9 black box with 1px #262626 border; bottom-left status chip (padding 7px 9px, rgba(0,0,0,0.74), DM Mono 9px uppercase #b6b6af) led by a 6px #58c8c4 dot with glow.
- **Scene card** (`.scene-pair`): 8px radius, #050505, a 16:9 video; top-left badge "Generated Video" (Manrope 10px/600 white on rgba(255,107,87,0.24), 1px rgba(255,107,87,0.42), 2px radius, padding 4px 8px, blur(6px)); bottom-left pill "SHOW 3D MAP" (30px tall, padding 0 11px, DM Mono 9px uppercase, 1px rgba(255,255,255,0.3), rgba(0,0,0,0.48), radius 9999px, 13px map icon). The map opens as a 32%-wide inset at top-right 12px with a 3px black mat and can expand to fill the card.
- **Gallery group heading**: grid 48px / 1fr / auto; coral DM Mono 9px number, Manrope 20px/500 #f2f1ec title, an 11px/1.55 mono #777770 instruction line, a muted count on the right.
- **Citation block**: #0b0b0b, 1px #262626, 80% width; DM Mono 12px/1.8 #c7c7c0; 34px round copy button at top/right 16px (#121212, 1px #262626, #8b8b84 icon; hover #ff6b57).
- **Footer**: Microsoft logo and "OCTWORLD · RESEARCH PROJECT" left; underlined legal links (offset 3px, gaps 8px 24px) and "© 2026 Microsoft" right in DM Mono 11px #8b8b84; hover #ff6b57.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header | yes | blurred black bar with logo wordmark and mono nav |
| Full-bleed video hero | yes | rotating generated videos under a dark gradient and grid |
| Title / authors / affiliations | yes | bottom-anchored, left-aligned over the video |
| Link buttons | yes | two square glass buttons with mono labels |
| Venue badge | absent from the source | no ECCV mention in the hero; the eyebrow reads "Long-range generative world modeling" |
| Method videos | yes | two 960px 16:9 players with status chips |
| Gallery | yes | three groups of 2-column video cards with coral badges and 3D-map toggles |
| Abstract | yes | 17px gray paragraphs at 80% width |
| Method figure | yes | white-framed training pipeline figure with caption |
| Results table | absent from the source | results are shown only as videos |
| BibTeX | yes | dark block with round copy button |
| Footer | yes | mono corporate footer with legal links |

## Adapting to Other Content

- **More authors**: keep the flex-wrap row at 13px with gaps 6px 22px; it stays bottom-anchored, so extra lines push the title up rather than the buttons down.
- **A results table**: place it in the 960px method column inside a 1px #262626 frame on #0b0b0b; header DM Mono 11px uppercase #8b8b84, cells Manrope 14px #a5a59e with 1px #262626 rules, best values 500 #f2f1ec with a 1px #ff6b57 underline. Keep corners square.
- **Long publication or news lists**: use the gallery-group-heading pattern per item: coral DM Mono 9px index, 20px/500 title, 11px mono #777770 line for venue or date, with 1px #262626 rules between items.
- **A venue badge**: put it in the eyebrow slot (DM Mono 11px uppercase #c4c4bd with the 22px coral dash) instead of adding a filled badge.
- **Image results instead of video**: use the 8px-radius scene card with the same coral badge and 24px grid gap.

## Do's and Don'ts

- Do anchor the hero text to the bottom of a full-bleed, darkened media background.
- Do set every label, nav item, button and code line in DM Mono uppercase at 9–11px.
- Do use coral #ff6b57 only for marks: the title underline, 22px dashes, group numbers, badges and hover states.
- Do keep the 48px hairline grid on the black ground.
- Don't use bold display weights; the title and headlines are Manrope 400.
- Don't round the hero buttons or the media frames; only scene cards (8px) and pills are rounded.
- Don't introduce light sections; the only white surface is the frame of the pipeline figure.

## Surfaces

Black #050505 with a 48px rgba(255,255,255,0.023) grid; the hero adds a darkening gradient over video; #0b0b0b for the citation block and #121212 for the copy button; translucent black chips and pills over video with backdrop blur; one white frame around the method figure.

## Imagery

Long generated camera walk-throughs of real and synthetic scenes (interiors, gardens, pools, streets) as autoplaying video, inset point-cloud and octree map renders, a dark system-workflow diagram with orange highlights, and a white paper figure of the training pipeline.

## Layout

A bottom-anchored cover hero, then wide sections on a 1384px shell with a two-column heading grid (index left, headline right), media centred at 960px or 1152px, and generous 120px section padding with hairline separators.

## Agent Prompt Guide

Quick colors: black #050505, surface #0b0b0b, line #262626, text #f2f1ec, muted #8b8b84, eyebrow #c4c4bd, body gray #a5a59e, coral #ff6b57, cyan #58c8c4.

1. "Build a full-bleed video hero: min-height calc(100svh − 58px), video object-fit cover with filter saturate(1.02) contrast(1.04) brightness(0.78), overlay linear-gradient(180deg, rgba(5, 5, 5, 0.34) 0%, rgba(5, 5, 5, 0.18) 38%, rgba(5, 5, 5, 0.9) 100%). Content left-aligned at 28px, justified to the bottom with padding 16vh 0 9vh: DM Mono 11px uppercase #c4c4bd eyebrow led by a 22×1px #ff6b57 rule, a Manrope 400 title at clamp(42px, 5.5vw, 92px) with line-height 1.02 and its first word underlined in #ff6b57 (thickness 0.07em, offset 0.09em), 13px #e3e2dc authors with #58c8c4 mono superscripts."
2. "Make glass buttons: min-height 38px, padding 0 14px, DM Mono 10px uppercase #f2f1ec, 1px rgba(242,241,236,0.42) border, rgba(5,5,5,0.46) background with backdrop-filter blur(10px), square corners, 16px stroked icon; hover border and text #ff6b57 with rgba(255,107,87,0.12) fill."
3. "Create a video gallery card: 8px radius on #050505, 16:9 video; top-left badge Manrope 10px/600 white on rgba(255,107,87,0.24) with a 1px rgba(255,107,87,0.42) border and 2px radius; bottom-left pill 30px tall, DM Mono 9px uppercase, 1px rgba(255,255,255,0.3) border, rgba(0,0,0,0.48) fill, radius 9999px. Two columns, 24px gap, inside a 1152px column."

## Similar Pages

- Corporate-lab research pages with a full-bleed video cover and mono labeling.
- World-model and video-generation pages that present results as large autoplaying video grids.

## Quick Start

```css
:root {
  --background: #050505;
  --surface: #0b0b0b;
  --surface-raised: #121212;
  --line: #262626;
  --muted: #8b8b84;
  --text: #f2f1ec;
  --accent: #ff6b57;
  --cyan: #58c8c4;
  --display: "Manrope", sans-serif;
  --mono: "DM Mono", monospace;
  --shell: min(1720px, calc(100% - 56px));
}
body {
  background:
    linear-gradient(rgba(255, 255, 255, 0.023) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.023) 1px, transparent 1px),
    var(--background);
  background-size: 48px 48px;
}
```

## Provenance

- **URL**: https://microsoft.github.io/OctWorld/
- **Paper**: OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping (arXiv 2609.03919), Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang (USTC, Microsoft Research Asia, Tsinghua University).
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a custom build hosted under Microsoft's GitHub Pages with self-hosted Manrope and DM Mono; footer reads "© 2026 Microsoft".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, section heads, gallery cards, method media, abstract, citation and footer, the 1440×900 shot and a full-page capture, and the page's `styles.css` and `index.html` read directly, on 2026-10-28.
