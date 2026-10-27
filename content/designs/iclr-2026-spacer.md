# SPACeR Applied Blue Swiss — Style Reference

> A corporate research report in Swiss order: blue capitals spelling the name, mono bylines, and numbers that stand on black rules.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, and the page's own `static/css/style.css`, a documented token system ("Applied Intuition brand design system", adapted from the TerraZero report site). No CSS framework is loaded. Color share is measured on the first 1440×900 viewport.

## Overview

A white, left-aligned page in a 1280px frame. A frosted pill header floats 14px from the top with a black logo glyph and "SPACeR" at the left and grey 13px nav links at the right. The hero starts with a mono uppercase eyebrow led by a small black square ("APPLIED INTUITION · ICLR 2026"), then a 57.6px bold grotesk title in #111111 where the acronym and every initial letter that spells it (S, P, A, Ce, R) are Applied Blue #006cfa. A thin #e4e4e4 rule separates the title from a mono byline (names in ink, superscripts and separators grey), mono affiliations, and three small 8px-radius buttons (blue "arXiv", outlined "Paper" and "Blog"). Below, full-width sections alternate between white and #f6f7f9, separated by 1px #e4e4e4 rules; each opens with a black-square mono eyebrow and a 35.2px semibold heading. Body copy is XCharter serif, justified across the full 1232px width. Figures sit in 10px-radius bordered frames with a grey stage and a caption bar whose label is blue; the demo is a dark driving video. A three-column stat row (~50×, 10×, 65K) in blue display numbers stands on 2px black rules, and results tables use a 2px ink header rule and blue-wash row hover. The footer is a solid #111111 band.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 72.9% (plus #fdfdfd 3.0%, #fffffe 1.6%), mid grey #bebfc2 8.6% and pale grey #ebeced 4.3% (header pill shadow, rules, button borders, antialiased text), #fafafa 5.2%, slate #707c8c 4.4% (grey nav, byline and blended blue type). The blue title letters are a small share by area but the strongest colour on screen.

Anatomy in DOM order (wide frame x=80–1360; content x=104):

1. **Header pill** — `header.site-header` fixed, padding 14px 16px; `.header-pill` 1280px max, 60px tall, padding 0 22px; pseudo-element background rgba(255,255,255,0.72) with 14px blur, 1px rgba(17,17,17,0.07) border, 999px radius, shadow `0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07)`. Left: masked icon (1.15em, #111111) + "SPACeR" Applied Sans Display 16.8px / 700. Right: nav links Applied Sans Text 13.12px / 400, #767676, gap 24px; active link #111111 600.
2. **Eyebrow** — `p.eyebrow` at y=114: 0.5em black square, then "APPLIED INTUITION · ICLR 2026" in mono 13.76px, letter-spacing 0.16em, uppercase, #767676. Margin-bottom 16px.
3. **Title** — `h1` at y=152: Applied Sans Display 57.6px / 700 / 1.04, letter-spacing -0.02em, #111111, two lines in a 960px intro block; `span.accent` letters #006cfa. Margin-bottom 24px.
4. **Rule** — `.hero-meta` border-top 1px #e4e4e4, padding-top 24px.
5. **Byline** — `p.byline` at y=321: mono 13.12px / 1.7, #767676 with name links #111111 and superscript numbers.
6. **Affiliations** — `p.affil`: mono 11.52px, #767676, middot separators; a second line "* Work done during internship at Applied Intuition" (y=354–397).
7. **Buttons** — `.actions` (gap 0.7rem, margin-top 24px) at y=421: "arXiv" `btn-primary` (#006cfa fill, #ffffff text), "Paper" and "Blog" `btn` (#ffffff fill, 1px #e4e4e4 border, #111111 text); Applied Sans Text 13.12px / 600, padding 0.6em 1.05em, 8px radius, 39px tall. Hero ends at y=500 with a 1px #e4e4e4 rule.
8. **Abstract** — section padding 96px 0: eyebrow "ABSTRACT" at y=597, then `p.prose` XCharter 17px / 27.54px, justified and hyphenated, #111111, full 1232px width (y=635–910).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| White | #ffffff | `--white` | page, secondary buttons, figure frames |
| Ink | #111111 | `--ink` | title, headings, body text, eyebrow square, logo glyph, stat rules, table header rule, footer band |
| Applied Blue | #006cfa | `--blue` | title initials and acronym, primary button, links, stat numbers, figure and table labels, speed-control thumb |
| Blue Dark | #0052bd | `--blue-dark` | primary button hover |
| Grey | #767676 | `--gray` | nav links, eyebrows, byline, affiliations, stat captions, copyright |
| Line | #e4e4e4 | `--gray-line` | section dividers, hero rule, button borders, figure borders, table row rules |
| Soft Band | #f6f7f9 | `--gray-soft` | alternate section backgrounds, figure stage, segmented track, table group rows |
| Blue Wash | #eef4ff | `--blue-wash` | table row hover |
| Marker Wash | #e0ecff | `--blue-wash-2` | `mark.hl` underline swipe |
| Caption Ink | #333333 | (literal) | figcaption and table caption text |
| Lead Ink | #2a2a2a | (literal) | `.lead` paragraphs |
| Footer Text | #cfd3da | (literal) | footer body text on ink |
| Video Black | #0d1117 | (literal) | background behind three-up comparison videos |

## Tokens — Typography

- **Display:** declared `"Applied Sans Display", "Helvetica Neue", Arial, sans-serif` (vendored TTF, 600 and 700). Rendered: Applied Sans Display 600, 700. Substitute: Inter Display or Neue Haas Grotesk Display; for free use, Inter at 600/700 with -0.02em tracking.
- **UI sans:** declared `"Applied Sans Text", …` (400, 400i, 600, 600i). Rendered: Applied Sans Text 400, 600. Substitute: Inter.
- **Serif body:** declared `"XCharter", Georgia, "Times New Roman", serif` (vendored OTF). Rendered: XCharter 400, 400i. Substitute: Charis SIL or Bitstream Charter.
- **Mono:** declared `"SFMono-Regular", "JetBrains Mono", Menlo, Consolas, monospace`; no webfont, so it renders as the first installed face (Consolas on Windows, SF Mono or Menlo on macOS). Substitute: JetBrains Mono.
- **Math:** MathJax 3.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Title | `.hero h1` (`clamp(2.05rem, 5vw, 3.6rem)`) | 57.6px / 700 / 1.04, ls -0.02em |
| Section heading | `h2` (`--fs-h2` 2.2rem) | 35.2px / 600 / 1.12, ls -0.01em |
| Sub-heading | `h3` (`--fs-h3` 1.18rem) | 18.88px / 600 |
| Stat number | `.statline .stat-num` (`clamp(2rem, 4vw, 3rem)`) | 48px / 700 / 1, #006cfa |
| Lead | `.lead` | 20.8px / 1.5, #2a2a2a |
| Body | `body`, `.prose` | XCharter 17px (1.0625rem) / 1.62, justified with hyphenation |
| Eyebrow | `.eyebrow` | mono 13.76px (0.86rem), uppercase, ls 0.16em |
| Byline | `.byline` | mono 13.12px / 1.7 |
| Affiliations | `.affil` | mono 11.52px |
| Nav, buttons, captions, tables | `.nav a`, `.btn`, `figcaption`, `table.data` | Applied Sans Text 13.12px (0.82rem); buttons and labels 600 |
| Brand mark | `.brand-mark` | Display 16.8px / 700 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Spacing scale | 0.5rem, 1rem, 1.5rem, 2.5rem, 4rem, 6rem (`--space-1…6`) |
| Radius | 10px (`--radius`) on figures and video frames; 8px on buttons; 6px on legends; 999px on header pill and segmented control |
| Shadow | `--shadow`: `0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07)` on the header pill and speed thumb |
| Shadow lift (declared) | `0 2px 6px rgba(17,17,17,.06), 0 18px 48px rgba(0,108,250,.10)` |
| Section divider | 1px #e4e4e4 between consecutive sections |
| Stat rule | 2px #111111 top border on each stat cell, padding-top 0.6rem |
| Table rules | header bottom 2px #111111; rows 1px #e4e4e4 |
| Eyebrow marker | 0.5em solid #111111 square |

## Layout Metrics

- **Frame:** `.wide` max-width 1280px, padding-inline 24px (content 1232px, x=104–1336 at 1440). `.reading` 720px and `.bleed` `min(1680px, 96vw)` are also defined.
- **Hero:** padding-top 60 + 14 + 40 = 114px, padding-bottom 40px; intro block max 60rem (960px).
- **Sections:** padding-block 96px (6rem); every second content section on #f6f7f9; 1px #e4e4e4 between sections.
- **Body measure:** `.prose` has no max-width, so paragraphs run the full 1232px.
- **Figures:** `.figure` with 24px stage padding and caption padding 16px 24px; figure bands padding 64px.
- **Stat row:** `.statline` three equal columns, gap 16px, margin 24px 0.
- **Three-up comparisons:** `.threeup` three columns, gap 16px; centred italic serif row notes max 80ch.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1328px | (viewport − 1280)/2 + 24px | 17px | 57.6px | three-up and stat row at 3 columns |
| 861–1327px | 24px | 17px | 5vw | same grids |
| 821–860px | 24px | 17px | 5vw | stat row 2 columns |
| ≤820px | 24px | 17px | 5vw (min 32.8px) | header pill becomes two frosted 52px circles (brand, menu) with a full-screen overlay nav in 27px Display; sections padding 64px |
| ≤640px | 24px | 17px | 32.8px | three-up comparisons stack to 1 column |

## Components

- **Floating pill header:** fixed, 1280px max, 60px tall, frosted white (0.72) with 14px blur, 1px faint border, 999px radius, soft two-layer shadow; brand glyph + bold wordmark left, grey 13px links right, hover to ink without underline.
- **Eyebrow:** mono uppercase, 0.16em tracking, #767676, preceded by a 0.5em solid #111111 square.
- **Acronym title:** bold display title in ink with the acronym and each spelled initial in #006cfa.
- **Buttons:** 8px radius, padding 0.6em 1.05em, 13.12px / 600; default white with 1px #e4e4e4 border, hover border and text #006cfa; primary #006cfa fill, hover #0052bd; press moves 1px down.
- **Figure frame:** 1px #e4e4e4 border, 10px radius, #f6f7f9 stage with 24px padding, caption bar with 1px top rule, 13.12px #333333 text and a blue 600 label ("Demo.", "Figure 2.").
- **Stat row:** three cells, each a 2px #111111 top rule, a 48px bold #006cfa number (~50×, 10×, 65K) and a 13.12px grey caption.
- **Data table:** Applied Sans Text 13.12px, cells 0.55em 0.85em, numbers right aligned, header 600 over a 2px ink rule, 1px #e4e4e4 row rules, row hover #eef4ff, best row 600, mono uppercase group rows on #f6f7f9, caption below with a blue label.
- **Segmented speed control:** #f6f7f9 track with 1px border and 999px radius, a sliding #006cfa thumb with shadow, 13.12px / 600 options; active white, hover blue.
- **Marker highlight:** `mark.hl` with a #e0ecff swipe under the lower 44% of the text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Floating nav | Yes | frosted pill with brand glyph |
| Eyebrow (org · venue) | Yes | mono uppercase with black square |
| Title with blue initials | Yes | display bold, acronym letters #006cfa |
| Byline / affiliations | Yes | mono, grey with ink names |
| Link buttons | Yes | blue primary + two outlined |
| Teaser | Present but non-standard | none in the hero; the dark demo video opens section two |
| Abstract | Yes | full-width justified XCharter |
| Demo video | Yes | dark video in a bordered figure frame |
| Overview with stats | Yes | bullet list, stat row |
| Method / equations | Yes | MathJax display blocks |
| Results table | Yes | HTML `table.data` with blue-labelled caption |
| Comparisons | Yes | synchronized three-up videos with speed control |
| BibTeX | No (absent from the source) | |
| Footer | Yes | #111111 band with series links and mono copyright |

## Adapting to Other Content

- **No acronym:** colour only the product or method name in #006cfa; keep the rest of the title ink.
- **More authors:** the mono byline wraps naturally; keep names ink and separators grey, move notes to the affiliation line.
- **Long text:** constrain prose to `.reading` (720px) for essays; the full-width justified measure only works for one abstract paragraph.
- **More results tables:** reuse `table.data` with group rows for benchmark families; put the best row in 600 weight, never coloured fills.
- **News or updates:** an eyebrow "UPDATES" section with mono dates in #767676 and one-line entries in XCharter.
- **BibTeX:** add a figure frame whose stage holds mono 13px text, caption label "BibTeX." in blue.

## Do's and Don'ts

- Do use one brand blue for every accent: initials, primary button, labels, stat numbers.
- Do open every section with the black-square mono eyebrow.
- Do alternate white and #f6f7f9 sections with 1px #e4e4e4 seams instead of cards.
- Don't round buttons beyond 8px or figures beyond 10px; only the header and segmented control are pills.
- Don't let justified serif prose run 1232px wide for more than a paragraph.
- Don't introduce a second accent hue; status and emphasis use weight, not colour.

## Surfaces

White page and alternating #f6f7f9 bands; frosted white header; white figure frames with #f6f7f9 stages; a dark #0d1117 video area; solid #111111 footer.

## Imagery

Dark top-down driving simulations with green agent boxes and a white ego car, method diagrams, plots, and three-up synchronized comparison videos with small white legends.

## Layout

A 1280px frame, left-aligned hero, then full-width alternating sections with eyebrow, heading, prose, figure and table. Rendered height about 14,200px.

## Agent Prompt Guide

Quick colors: ink #111111, blue #006cfa (hover #0052bd), grey #767676, line #e4e4e4, band #f6f7f9, row hover #eef4ff, page #ffffff, footer text #cfd3da.

1. "Build a hero inside a 1280px frame with 24px padding: a mono uppercase eyebrow (13.76px, 0.16em tracking, #767676) led by a 0.5em #111111 square; a left-aligned 57.6px / 700 display title in #111111 with the acronym and its initials in #006cfa; a 1px #e4e4e4 rule; a mono 13.12px byline with ink names; then 8px-radius buttons: primary #006cfa with white text, secondary white with 1px #e4e4e4 border, both 13.12px / 600, padding 0.6em 1.05em."
2. "Add a stat row: three equal columns with 16px gap; each cell has a 2px solid #111111 top border, a 48px bold #006cfa number with -0.02em tracking, and a 13.12px #767676 caption."
3. "Style a results table: 13.12px sans, numbers right aligned, header 600 with a 2px #111111 bottom rule, body rows separated by 1px #e4e4e4, hover background #eef4ff, best row weight 600, caption below with a 600 #006cfa 'Table 1.' label."

## Similar Pages

- TerraZero and other Applied Intuition "Terra Series" research pages that share this token system.
- Swiss-style corporate research pages with eyebrow labels and stat rows (compare PA3FF in this collection for the editorial serif counterpart).

## Quick Start

```css
:root {
  --white: #ffffff;
  --ink: #111111;
  --blue: #006cfa;
  --blue-dark: #0052bd;
  --gray: #767676;
  --gray-line: #e4e4e4;
  --gray-soft: #f6f7f9;
  --blue-wash: #eef4ff;
  --blue-wash-2: #e0ecff;
  --font-display: "Inter Display", "Helvetica Neue", Arial, sans-serif;
  --font-sans: "Inter", "Helvetica Neue", Arial, sans-serif;
  --font-serif: "XCharter", "Charis SIL", Georgia, serif;
  --font-mono: "JetBrains Mono", Menlo, Consolas, monospace;
  --fs-title: clamp(2.05rem, 5vw, 3.6rem);
  --fs-h2: 2.2rem;
  --fs-body: 1.0625rem;
  --fs-meta: 0.82rem;
  --wide: 1280px;
  --radius: 10px;
}
```

## Provenance

- **URL:** https://terra-applied.github.io/SPACeR/
- **Paper:** SPACeR: Self-Play Anchoring with Centralized Reference Models (arXiv 2510.18060), Wei-Jer Chang et al.
- **Venue:** ICLR 2026 (stated on the page).
- **Selection reason:** arXiv comment states "Accepted at ICLR 2026"; project page linked in the comment (spacer-ai.github.io meta-refreshes to this URL).
- **Template credit:** the stylesheet header says it is the Applied Intuition brand design system adapted from the TerraZero technical-report site; brand fonts are the company's own and are vendored by the authors.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 screenshots (first viewport and tall), `static/css/style.css`, page HTML; 2026-10-28.
