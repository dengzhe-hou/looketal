# Dusk Gradient Distill — Style Reference

> A violet-to-ember dusk poster up top, then a plain Distill reading room below.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the hero headings, award pill, intro paragraph, icon list, buttons, teaser image, author list and article headings, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's `static/css/style.css` with the Distill v2 template it loads (`distill_template.v2.js`). Positions are document coordinates at 1440px wide. The stylesheet asks for `font-family: Charter` with no fallback and loads no Charter webfont, so on this Windows render every text element fell back to the browser default serif (Times New Roman); on macOS, where Charter is installed, the page shows Charter.

## Overview

ProgressLM is a Distill-template article with a custom poster-like hero. The hero is a full-width diagonal gradient from near-black violet through purple to burnt orange. On the left half, a 52.8px bold italic title "ProgressLM:" and a 32px bold subtitle are set in peach (#feae6f); a translucent pill reads "🏆 ACL 2026 Oral Presentation"; a justified cream paragraph introduces the work, followed by three line-icon feature items with yellow bold lead-ins, and four dark-grey rounded buttons with Font Awesome icons. On the right half sits a square illustrated teaser (a child imagining an elephant entering a fridge, in purple night tones). Below the hero, the page switches to white: a centered author list, a red-edged announcement box, a large method figure with a long Distill caption, a justified abstract, a row of five pale-blue "jump to section" buttons, and long Distill sections with big bold serif headings and justified body text.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): deep purple #521673 18.8%, violet-black #1c0f35 15.2%, white #fffefe 13.9% (the page below the hero), plum #3a1255 13.5%, tan #b38267 11.2% (orange end of the gradient and the illustration's skin tones), midnight #0b051c 10.9%, rose #873857 9.4% (gradient transition), dusk violet #3e2e56 7.1%. The hero gradient fills about 85% of the viewport.

Anatomy in DOM order (y = top of element box):

1. **Hero band** (`.header-wrapper`), y 0 to about 767, background `linear-gradient(-235deg, #1a0b2e 10%, #671b8d 55%, #bd5703 80%, #f97212d2 100%)`. Inner `.header-container` is a flex row, max-width 1600px, padding 50px, content and image `space-between`, vertically centered.
2. **Title** (`.header-content h1 > i`), x 50, y 50, "ProgressLM:", 52.8px/700 italic, line-height 63.4px, #feae6f, left. Gap 3px (subtitle has -24px top margin).
3. **Subtitle** (`.header-content h2`), y 116, two lines, 32px/700, line-height 38.4px, #feae6f. Gap 16px.
4. **Award pill** (`.hero-award`), y about 210, inline-flex, "🏆 ACL 2026 Oral Presentation", 16.8px/700 #fff7d4, background rgba(255,247,212,0.12), 1px rgba(254,174,111,0.55) border, radius 999px, padding 6.4px 12px. Gap about 13px.
5. **Intro paragraph** (`.header-container p`), y 261, 650px wide, 19.2px/400, line-height 25.6px, justified, #fff7d4; the key phrase bold italic in #ffe099. Gap 19px.
6. **Feature list** (`.icon-container`), y about 400–600, three items each with a 30px white line icon on the left (16px gap) and 16px text, lead-in bold #ffe099.
7. **Buttons** (`.button-container`), y 642, four 50px buttons: "Paper", "Code (100+ ⭐)", "Dataset", "Model", 16px/700 #ffffff on #24292f, 2px rgba(255,255,255,0.35) border, radius 20px, padding 10px 20px, margin 5px 2px; Font Awesome or Hugging Face icons on the left.
8. **Teaser image** (`img.teaser-image`), right column, x 773, y 81, 585×585 square, no frame or radius.
9. **Author list** (`p.author-list`), y 805 on white, centered, names 20.35px/400 #000000 with superscripts; affiliations below; "*Equal Contribution" in #999999.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Dusk Black | #1a0b2e | gradient stop 10% | Hero gradient, top-left corner |
| Violet | #671b8d | gradient stop 55% | Hero gradient middle |
| Ember | #bd5703 | gradient stop 80% | Hero gradient, orange zone |
| Flame | #f97212 | gradient stop 100% (82% alpha) | Hero gradient, bottom-right corner |
| Peach | #feae6f | `.header-container`, `.header-content h1, h2` | Hero title and subtitle |
| Cream | #fff7d4 | `.header-content` | Hero paragraph, feature text, award pill text |
| Butter | #ffe099 | `.header-content strong` | Bold lead-ins in the hero |
| Button Grey | #24292f | `a.button.dark-button` | Hero buttons |
| Button Hover Blue | #0969da | `.dark-button:hover` | Hero button hover fill |
| White | #ffffff | page | Article background, button text |
| Article Ink | rgba(0,0,0,0.8) | Distill `d-article` | Section headings and body text |
| Author Black | #000000 | `.author-link` | Author and affiliation names (hover #007bff) |
| Notice Text | #333333 | `.presentation-details` | Announcement details text |
| Note Grey | #999999 | `.author-note` | "*Equal Contribution" |
| Notice Fill | #fff8f8 | `.presentation-notice` | Announcement box background |
| Notice Red | #b91c1c | `.presentation-notice` | 5px left border of the announcement box |
| Notice Title | #991b1b | `.presentation-title` | Announcement title text |
| Jump Fill | #edf7ff | `.icon-link` | Section jump buttons (hover #dceeff) |
| Jump Blue | #508af6 | `.icon-link` | 4px left border of jump buttons, 1px border at 45% |
| Jump Ink | #253247 | `.icon-link` | Jump button text |

Declared but not visible: the default `.button` style (#fff0ce fill, rgba(255,193,7,0.5) border, hover #eab682) is overridden on every hero button by `.dark-button`.

## Tokens — Typography

- **Everything**: declared `font-family: Charter` on `body` with no fallback and no `@font-face`. Rendered here: the browser default serif, Times New Roman (`fonts_loaded` lists only Font Awesome 5 Free and Brands). On macOS and iOS it renders as system Charter. Substitute: Charis SIL (a free Charter derivative with the same proportions), which would make the page look as intended everywhere.
- **Icons**: Font Awesome 5 (Free 900 and Brands 400) for button icons; academicons loaded.
- **Math**: MathJax 3 and KaTeX 0.10.2 are both loaded.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Hero title | `.header-content h1` (italic via `<i>`) | 52.8px (3.3em) / 63.4px | 700 italic | #feae6f |
| Section title | `d-article h1.text` | 33.92px / 28.8px | 700 | rgba(0,0,0,0.8) |
| Hero subtitle | `.header-content h2` | 32px (2em) / 38.4px | 700 | #feae6f |
| Subsection | `d-article h2.text` | 30.53px / 38.2px, 16px bottom padding | 600 | rgba(0,0,0,0.8) |
| Author names | `.author-link` | 20.35px | 400 | #000000 |
| Hero paragraph | `.header-container p` | 19.2px / 25.6px, justified | 400 | #fff7d4 |
| Sub-subsection | `d-article h3.text` | 19.2px / 26.9px | 700 | rgba(0,0,0,0.8) |
| Article body | `d-article p` | 16.96px / 28.8px, justified | 400 | rgba(0,0,0,0.8) |
| Award pill | `.hero-award` | 16.8px | 700 | #fff7d4 |
| Hero button | `.dark-button` | 16px | 700 | #ffffff |
| Feature text | `.icon-item div` | 16px | 400 (lead-in 700) | #fff7d4 / #ffe099 |
| Announcement title | `.presentation-title` | 18.4px | 700 | #991b1b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero button | 20px | 2px solid rgba(255,255,255,0.35) | none |
| Award pill | 999px | 1px solid rgba(254,174,111,0.55) | none |
| Teaser image | 0 | none | none |
| Announcement box | 8px | 1px rgba(153,27,27,0.22), 5px #b91c1c left | none |
| Section jump button | 8px | 1px rgba(80,138,246,0.45), 4px #508af6 left | none |
| Collapsible blocks | 4px (flat bottom when open) | none | none; fill hsla(206,95%,20%,0.2) |

## Layout Metrics

- **Hero**: `.header-container` max-width 1600px, centered, padding 50px (16px with 32px top under 768px); at ≥600px a flex row with `.header-content` at `calc(50% - 20px)` (650px at 1440) and the image column at the same width, image `max-width: 90%` (585px).
- **Byline**: centered author list, padding 5.6px 16px 8px.
- **Article**: the Distill grid places text in a column about 1056px wide starting near x 227 at 1440px; figures use the same column or wider; headings sit flush with text. Section h1 margins 17px top, 34px bottom.
- **Jump row**: five `.icon-link` buttons in a flex row (wrapping to full width on phones), padding 10.4px 12px, icons 1.8em tall.
- **Rendered height** about 12,800px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | Distill grid margins | 16.96px | 52.8px | hero two columns; article on the wide Distill grid |
| 768–1023px | Distill grid margins | 16px | 52.8px | hero two columns; narrower article |
| 600–767px | 16px hero padding | 16px | 52.8px | jump buttons full width; hero still a row |
| <600px | 16px | 16px | 48px (3em) | hero stacks, centered text, image below; subtitle 27.2px |

## Components

- **Award pill**: inline-flex, gap 7.2px, padding 6.4px 12px, radius 999px, background rgba(255,247,212,0.12), 1px rgba(254,174,111,0.55) border, 16.8px/700 #fff7d4, trophy emoji at 1.1em.
- **Dark hero button**: inline-block, padding 10px 20px, margin 5px 2px, radius 20px, #24292f fill, 2px rgba(255,255,255,0.35) border, 16px/700 white, icon left; hover fill #0969da.
- **Icon feature item**: flex row, 30px white SVG line icon with 16px right margin, text 16px #fff7d4 with a bold #ffe099 lead-in and colon.
- **Announcement box**: #fff8f8 fill, 1px rgba(153,27,27,0.22) border with a 5px #b91c1c left edge, 8px radius, padding 16px 20px; centered 18.4px bold #991b1b title framed by emoji, 16px #333333 details.
- **Section jump button**: #edf7ff fill, 1px rgba(80,138,246,0.45) border, 4px #508af6 left edge, 8px radius, padding 10.4px 12px, #253247 text with an icon; hover #dceeff and a full #508af6 border. A pale bar below reads "Click to jump to each section."
- **Distill section heading**: bold serif h1 at 33.92px, rgba(0,0,0,0.8), above a thin full-width rule; h2 at 30.53px/600 with a 1px rgba(0,0,0,0.1) underline and 16px padding.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Gradient hero | yes | violet-to-orange band, text left, image right |
| Venue / award | yes | translucent pill "ACL 2026 Oral Presentation" |
| Title and subtitle | yes | peach serif, italic title |
| Contribution list | yes | three icon items in the hero |
| Link buttons | yes | four dark rounded buttons |
| Teaser | yes | square illustration, unframed |
| Authors and affiliations | present but non-standard | placed below the hero on white, not in it |
| Announcement | yes | red-edged notice box |
| Method figure | yes | full-width figure with long Distill caption |
| Abstract | yes | justified paragraph without a heading |
| Section jump nav | yes | five pale-blue buttons |
| Results figures and tables | yes | figures and Distill tables inside sections |
| Distill table of contents | present but non-standard | styled `d-contents` sidebar rules exist |
| BibTeX | yes | Distill appendix block |
| Videos | absent from the source | none |

## Adapting to Other Content

- **More authors**: keep them below the hero in the centered 20.35px list; the hero stays reserved for title, pill, pitch and buttons.
- **A results table**: use the Distill table with 1px rgba(0,0,0,0.1) rules; the page also defines a 3px #000 `.bold-divider` row to separate model groups.
- **Videos**: swap the teaser image for a square video in the hero's right column at `max-width: 90%`, unframed.
- **More contributions**: add icon items in the hero; past four, move them below into the article.
- **Long publication lists or news**: use the red-edged notice box for one announcement only; put dated items as a plain Distill list.
- **Font**: specify `Charter, "Charis SIL", Georgia, serif` so non-Apple viewers do not fall back to Times.

## Do's and Don'ts

- Do keep the hero gradient angle (-235deg) and its four stops; it is the page's identity.
- Do set hero type in peach #feae6f and cream #fff7d4 with butter #ffe099 for emphasis, never pure white.
- Do keep buttons dark (#24292f) with a translucent white border so they read on both purple and orange.
- Do leave the article plain Distill: white, serif, justified, rgba(0,0,0,0.8) ink.
- Don't frame or round the teaser illustration.
- Don't add more accent hues below the hero beyond the notice red and the jump-button blue.
- Don't rely on Charter without a fallback.

## Surfaces

A full-bleed gradient hero, then white for everything else. Inset surfaces are the #fff8f8 notice, #edf7ff jump buttons and Distill's light grey figure shading (hsl(0,0%,97%) in `.shaded-figure`).

## Imagery

A painterly square illustration in deep purples (a child dreaming of an elephant entering a refrigerator), matching the hero gradient. Below, paper figures: robot-arm frame sequences with progress percentages, reasoning traces with orange and blue highlights, charts and tables. White line icons in the hero.

## Layout

A two-column hero (text 650px left, image right) spanning up to 1600px, followed by a single Distill article column about 1056px wide with justified text, full-column figures and long captions. Rendered height about 12,800px.

## Agent Prompt Guide

Quick colors: gradient #1a0b2e → #671b8d → #bd5703 → #f97212, peach #feae6f, cream #fff7d4, butter #ffe099, button #24292f (hover #0969da), article ink rgba(0,0,0,0.8), notice #fff8f8 / #b91c1c, jump #edf7ff / #508af6.

1. "Build a two-column hero on linear-gradient(-235deg, #1a0b2e 10%, #671b8d 55%, #bd5703 80%, #f97212d2 100%) with 50px padding: left half a 52.8px bold italic serif title in #feae6f, a 32px bold #feae6f subtitle, a pill 'ACL 2026 Oral Presentation' (16.8px/700 #fff7d4, background rgba(255,247,212,0.12), 1px rgba(254,174,111,0.55) border, radius 999px), and a justified 19.2px #fff7d4 paragraph with #ffe099 bold emphasis; right half a square unframed illustration."
2. "Add hero buttons: #24292f fill, 2px solid rgba(255,255,255,0.35) border, 20px radius, padding 10px 20px, 16px bold white serif text with a Font Awesome icon on the left; hover fill #0969da."
3. "Add a row of section jump buttons on white: #edf7ff fill, 1px rgba(80,138,246,0.45) border with a 4px #508af6 left edge, 8px radius, padding 10.4px 12px, #253247 text and a small line icon; hover #dceeff."

## Similar Pages

- Distill-template project pages (Cambrian, MMVP-style) that add a colored hero.
- Pages with a split hero: pitch and buttons left, square teaser right.

## Quick Start

```css
:root {
  --hero-gradient: linear-gradient(-235deg, #1a0b2e 10%, #671b8d 55%, #bd5703 80%, #f97212d2 100%);
  --hero-title: #feae6f;
  --hero-text: #fff7d4;
  --hero-strong: #ffe099;
  --button-bg: #24292f;
  --button-hover: #0969da;
  --article-ink: rgba(0, 0, 0, 0.8);
  --notice-bg: #fff8f8;
  --notice-edge: #b91c1c;
  --jump-bg: #edf7ff;
  --jump-edge: #508af6;
  --font: Charter, "Charis SIL", Georgia, serif;
}
```

## Provenance

- **URL**: https://progresslm.github.io/ProgressLM/
- **Paper**: PROGRESSLM: Towards Progress Reasoning in Vision-Language Models (arXiv 2601.15224), Jianshu Zhang, Chengxuan Qian et al. (Northwestern University, University of California, Santa Barbara).
- **Venue**: ACL 2026 (oral presentation, per the page).
- **Selection reason**: arXiv 2601.15224 comment states acceptance at ACL 2026 ("ACL 2026 Camera Ready Version"); project page linked in the abstract. Chosen for its bold purple-to-orange gradient hero with an illustrated image and icon feature list; the body below switches to default serif and gets text-heavy.
- **Template credit**: Distill (distill.pub template v2) for the article body.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture, `static/css/style.css` and `index.html`. Date 2026-10-28.
