# Nicholas Carlini — Style Reference

> A serif essay with a projector on every other paragraph.

**Theme:** light

Measurements are normalized from the static HTML and its large inline `<style>` block (about 11 KB, no external CSS); roles are interpreted. One web font, Lora, is self-hosted and preloaded.

## Overview

A writer's homepage. A white top bar with a soft shadow carries the name in small caps with wide tracking on the left and small-caps nav (Main, Papers, Talks, Code, Writing) on the right, each link drawing a 2px red underline from the left on hover. Below, a near-white page holds one boxed column (60em max, 5px radius, faint 12px shadow) set in Lora at 14pt with a generous 170% line height. A light grey contact card floats right with a 300px photo (5% radius), name, role, obfuscated email and two links. The bio is long-form prose with superscript footnote numbers linking each best-paper award. "Selected Recent Work" then alternates 480 by 270px videos, floated left and right, with paragraphs about each talk or project. Links are a deep red (#a02020), and the few buttons are maroon blocks. Footnotes are hover popovers.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Oxblood | #a02020 | `--link` | Links |
| Ember Red | #c03030 | `--link-hover` | Link hover |
| Underline Coral | #cc4444 | `--underline` | 2px animated underline in nav and contact links |
| Maroon Button | #663333 | `--button` | `a.button` fill |
| Maroon Hover | #884444 | `--button-hover` | `a.button` hover fill |
| Page Ivory | #fefefe | `--bg` | Body background |
| Card White | #ffffff | `--surface` | Top bar, main box, footnote popover |
| Contact Mist | #f8f8f8 | `--surface-2` | Contact card, left tab menu |
| Text Ink | #222222 | `--text` | Body text |
| Hairline | #d0d0d0 | `--rule` | Top bar bottom border, contact card right and bottom border |
| Header Rule | #dddddd | `--rule-2` | 2px rule under `div.header` |
| Divider Grey | #aaaaaa | `--rule-3` | Publication separators on mobile, footnote border |
| Award Butter | #ffffbb | `--award` | `span.award` highlight |
| Bar Black | #000000 | none | Mobile hamburger bars, button border |

## Tokens — Typography

- **Primary:** Lora 400 (self-hosted `lora.woff2`, `font-display: optional`), fallback `sans`. Substitute: Lora from Google Fonts or Source Serif 4.
- **Mono:** `monospace` inline, for example around `printf`.
- **Weights:** 400 throughout; bold for awards, `span.me`, and the active left-nav item.
- **Variants:** small caps for the site title, nav and left nav.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Site title | `div.title` | 150% | | small caps, letter-spacing .15em |
| Nav | `div.links` | 120% | | small caps |
| Page header | `div.header` | 2em | 100% | 2px #ddd bottom rule |
| Section label | `span.header` | 1.5em | 100% | "Selected Recent Work" |
| h2 | h2 | 1.5em | | weight normal |
| Body | `div.inner` | 14pt | 170% | |
| Card heading | `div.righthead` | 24px | | |
| Footnote mark | `span.footnote > a` | .7em | 100% | superscript |
| Mobile menu | `div.menu` | 12pt | | |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Popover | 2px | Footnote content |
| Mobile menu | .2em | Dropdown |
| Button | .25em | `a.button` |
| Award | 3px | `span.award` |
| Card | 4px | Contact card |
| Box | 5px | Main box |
| Photo | 5% | Portrait |
| Tab | 10px 10px 0 0 | `div.menu` tabs; left nav uses 10px 0 0 10px |

- **Shadows:** top bar `0 0 12px rgba(0,0,0,.1)`; main box `0 0 12px rgba(0,0,0,0.05)`; contact card `0 0 6px rgba(0,0,0,0.1)`; footnote `0 2px 10px 2px rgba(0,0,0,.25)`.
- **Layout max-width:** `div.outer` and `div.top` 60em, centered; container `padding: 1.5em 1em 0`.
- **Contact column:** `div.rightouter { width: 18em; float: right; }`, card width 16em.

## Components

- **Top bar.** Role: identity and nav. Full-width white strip, 1em vertical padding, 1px #d0d0d0 bottom border, 12px shadow; title left in small caps, nav right in small caps.
- **Fancy link.** Role: nav and contact links. Inside `div.fancy`, links get a `::before` 2px #cc4444 bar that scales from 0 to .99 on hover over 0.3s.
- **Main box.** Role: page body. White, 1em padding, 5px radius, faint 12px shadow.
- **Contact card.** Role: photo and contact. #f8f8f8 panel, 10px padding, 4px radius, right and bottom 1px #d0d0d0 borders, small shadow; 300px square photo with 5% radius; centered name, "Research Scientist, Anthropic", obfuscated email, GitHub and Scholar.
- **Video feature.** Role: a talk or project. `div.video` 480 by 270px `<video controls>` with a poster image, or a YouTube iframe, floated left or right beside its paragraph; on phones it becomes a full-width 60% padding-top responsive box.
- **Footnote popover.** Role: asides. Superscript link; hovering shows a fixed white popover with #aaa border and a strong shadow after a 1s delay.
- **Award highlight.** Role: mark best papers on the papers page. `span.award` bold on #ffffbb with 3px radius.
- **Button.** Role: occasional calls to action. White text on #663333, 1px black border, .25em radius, hover #884444 with a 0.5s transition.

## Page Modules

- **Title/author block:** top bar with small-caps name; contact card with photo, role and links.
- **Bio/photo:** long prose bio, awards cited with numbered superscript links to each paper.
- **Teaser media:** "Selected Recent Work" with nine videos and embeds (talks at Black Hat, ICML workshops, USENIX, CRYPTO, CAMLIS, a JavaScript game).
- **Publication list, talks, code, writing:** separate pages in the nav; the shared CSS holds publication rules (flex entries, abstract toggles via hidden checkboxes or radios, award highlight).
- **Link buttons:** text links and occasional maroon buttons.
- **News, venue badges, BibTeX block:** not on the home page.

## Do's and Don'ts

- Do set all text in one serif at 14pt with 170% leading; the page reads like an essay.
- Do cite awards with superscript footnote links instead of badges.
- Do alternate media left and right of the paragraph that explains it.
- Don't use more than the red link family for accents; the rest is white and grey.
- Don't sharpen the shadows; every elevation is a faint 6 to 12px blur.
- Don't put the photo in the header; it lives in the floated contact card (and in a centered block on phones).

## Surfaces

Ivory page, a white shadowed top bar, a white shadowed main box, a light grey contact card, and white footnote popovers. Three subtle elevation levels.

## Imagery

A 300px portrait, video poster frames, and embedded talk videos. No icons beyond the CSS hamburger.

## Layout

Centered 60em column with the contact card floated right at 18em. Under 40em the right column hides, a centered contact block appears at the top, the nav collapses into a checkbox-driven dropdown, and videos become full width. A fixed left section nav slides in beside the column on wide screens (hidden under 80em).

## Agent Prompt Guide

**Quick colors:** bg #fefefe, surface #ffffff, card #f8f8f8, text #222, link #a02020, hover #c03030, underline #cc4444, button #663333, award #ffffbb, rules #d0d0d0 / #ddd.

1. "Build a top bar: full-width white strip with a 1px #d0d0d0 bottom border and box-shadow 0 0 12px rgba(0,0,0,.1). Left, the name in small caps at 150% with .15em letter-spacing; right, small-caps nav links in #a02020 that draw a 2px #cc4444 underline from the left on hover."
2. "Create a floated contact card 16em wide: background #f8f8f8, 10px padding, 4px radius, right and bottom 1px #d0d0d0 borders, shadow 0 0 6px rgba(0,0,0,.1); 300px square photo with 5% radius, centered name, role, obfuscated email, and two links."
3. "Make a feature row: a 480 by 270px video with poster, floated left, beside a Lora 14pt paragraph with 170% line height describing the talk; the next feature floats right."

## Similar Pages

- [Florian Tramèr](https://www.floriantramer.com/), his co-author on the ICML 2024 Best Paper, for a card layout with a recorded-talks grid.
- [Danica J. Sutherland](https://djsutherland.ml/) for another serif-set researcher page.

## Quick Start

```css
:root {
  --bg: #fefefe; --surface: #ffffff; --surface-2: #f8f8f8;
  --text: #222222;
  --link: #a02020; --link-hover: #c03030; --underline: #cc4444;
  --button: #663333; --button-hover: #884444;
  --rule: #d0d0d0; --award: #ffffbb;
  --font: "Lora", serif;
  --content-max: 60em;
}
body { background: var(--bg); font-family: var(--font); line-height: 170%; margin: 0; text-rendering: optimizeLegibility; }
div.outer, div.top { max-width: var(--content-max); margin: 0 auto; }
div.topouter { background: var(--surface); border-bottom: 1px solid var(--rule); box-shadow: 0 0 12px rgba(0,0,0,.1); padding: 1em 0; }
div.boxed { background: var(--surface); border-radius: 5px; padding: 1em; box-shadow: 0 0 12px rgba(0,0,0,.05); }
div.inner { font-size: 14pt; color: var(--text); }
a { color: var(--link); text-decoration: none; } a:hover { color: var(--link-hover); }
div.fancy a { position: relative; }
div.fancy a::before { content: ""; position: absolute; left: 0; bottom: 0; width: 100%; height: 2px; background: var(--underline); transform: scaleX(0); transition: transform .3s ease; }
div.fancy a:hover::before { transform: scaleX(.99); }
```

## Provenance

- **URL:** https://nicholas.carlini.com/
- **Venue/award:** ICML 2024 Best Paper, twice: last author of the DP position paper and first author of "Stealing part of a production language model", per https://icml.cc/virtual/2024/awards_detail
- **Selection reason:** Rule B; homepage taken from his GitHub profile link.
- **Template credit:** none; hand-written HTML with inline CSS.
- **Measurement method:** all values read from the inline style block and HTML via `extract_style.py` and curl. Not rendered in a browser. The `font-family: "lora", sans` fallback names a generic family that browsers do not recognize, so if Lora fails to load the browser default font is used (inferred).
