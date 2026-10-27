# DICE — Style Reference

> A quarterly journal on warm paper: Georgia headlines, a small-caps dateline and one plum ink for every link.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the author's site stylesheets `research-home.css` and `research-pages.css`. The page loads no web font; every text element renders in the system Georgia, and the only loaded fonts are MathJax's.

## Overview

A blog post on a personal academic site rather than a standalone project page. The site header is a 50px row inside an 864px frame: a "TZ" monogram, a hairline divider and "Tongtian Zhu" in 21px Georgia at the left, and Research / Blog / Talks at the right, with the current page underlined in plum. The article header is left-aligned: a small "← Writing" back link, a tiny tracked uppercase dateline ("2025 · ICLR · RESEARCH EXPLAINER"), a bold 38px Georgia title over two lines, the author list with the site owner in bold, and a row of text links separated by slashes. A hairline closes the header. The body is a 720px column on warm off-white (#faf9f7) in 17px Georgia at line-height 1.6: a contents list with bold plum section links and bulleted subsection links, the conference poster at full column width, an "Updates" note, then long sections with inline diagrams, italic centred captions, plum-ruled pull quotes on a pale mauve fill, numbered lists and MathJax. A gray BibTeX block and a small italic footer end the page. Plum (#794590) is the only accent.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): paper #faf9f7 82.3% plus near-identical #fcfcfa / #faf9f6 / #faf9f8 / #f8f9f9 / #fcf9f6 7.2%; text gray #827d85 5.5% (anti-aliased ink and plum); hairline gray #e4e1e5 5.0% (rules and the poster's gray band).

Anatomy in DOM order (desktop 1440px; site frame 864px at x=288, article header x=306, body column x=360–1080):

1. **Site header** (0–50px): row height 50px, padding 0 13px, 1px #cccbd0 bottom rule. Left: 31×30 monogram, 17px gap, 1px #cccbd0 vertical divider, 17px padding, "Tongtian Zhu" Georgia 21px/400 #101020. Right: Research, Blog, Talks in 15px #101020, 30px apart; "Blog" in #794590 with an underline offset 7px.
2. **Back link** (y=81): "← Writing", 13px #794590, margin-bottom 25px.
3. **Dateline** (y=124): "2025 · ICLR · RESEARCH EXPLAINER", Georgia 10px uppercase, letter-spacing 1.8px, #484653. Gap 8px.
4. **Title** (`.article-header h1`, y=146, two lines, 87px): Georgia 38px/700, line-height 1.15, letter-spacing -0.8px, #101020, max-width 760px, left-aligned. Gap 15px.
5. **Authors** (y=249): 14px #101020, "Tongtian Zhu" bold. Gap 15px.
6. **Link row** (y=283): Paper / Code / arXiv / Slides / Poster / Video · 中文 / Thread / Hugging Face, 14px #794590, 12px gaps with #484653 slashes.
7. **Header rule** (y≈324): padding-bottom 22px, 1px #cccbd0, margin-bottom 24px.
8. **Contents** (y=356): h2 "Contents" 28px/700; section links bold 17px #794590; subsection links 17px #794590 in a bulleted list indented 40px.
9. **Poster** (y≈799): the ICLR poster image at 720px width, starting near the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #faf9f7 | --paper | page background |
| Ink | #101020 | --ink | title, headings, body text, nav links, wordmark |
| Muted Ink | #484653 | --muted | dateline, slash separators, pull-quote text, BibTeX text, footer |
| Plum | #794590 | --accent | all links (back link, link row, contents, inline), current nav item, focus outline |
| Hairline | #cccbd0 | --line | header and footer rules, wordmark divider, article header rule, horizontal rules |
| Quote Mauve | #f1edf2 | (literal) | pull-quote and custom-box fill, BibTeX block |
| Quote Rule | #a18bad | (literal) | 2px left rule of pull quotes and custom boxes |
| Caption Gray | #666666 | (inline style) | figure captions |

Inline styles in the markup try to color some custom boxes yellow, blue or red; the stylesheet overrides them with `!important`, so every box renders in the mauve pair above.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | Georgia, 'Times New Roman', serif | system Georgia (no web font loaded) | Gelasio |
| Mono | browser monospace | Consolas / Courier New | IBM Plex Mono |
| Math | MathJax 3 CHTML | MJXTEX fonts loaded | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Article title | `.article-header h1` | 38px / 700 / 1.15, letter-spacing -0.8px | #101020 |
| Section heading | `.article-body h2` | 28px / 700 / 1.2, letter-spacing -0.5px, margin 32px 0 14px | #101020 |
| Subsection | `.article-body h3` | 21px / 700 / 1.3, margin 25px 0 12px | #101020 |
| Minor heading | `.article-body h4` | 18px / 700 | #101020 |
| Body | `.article-body` | 17px / 400 / 1.6 | #101020 |
| Dateline | `.eyebrow` | 10px / 400 uppercase, letter-spacing 1.8px | #484653 |
| Authors | `.article-header .authors` | 14px | #101020 |
| Link row | `.paper-links` | 14px / 1.3 | #794590 |
| Back link | `.back-link` | 13px | #794590 |
| Wordmark | `.wordmark` | 21px / 400 | #101020 |
| Nav | `.site-header nav a` | 15px | #101020 (current #794590) |
| Caption | inline-styled `<p>` under figures | 0.88em = 15px italic, centred, margin-top 0.5em | #666666 |
| Pull quote | `.article-body blockquote`, `.custom-box` | 17px / 400 (bold only where the source wraps text in `<strong>`) | #484653 |
| BibTeX | `.article-body pre` | 12px / 1.5 | #484653 |
| Footer | `.site-footer` | 12px italic | #484653 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pull quote / custom box | 0 | 2px #a18bad left only | none |
| BibTeX block | 0 | none | none |
| Header and footer | 0 | 1px #cccbd0 bottom / top | none |
| Figures, poster | 0 | none | none |
| Nav current item | 0 | underline, offset 7px | none |

Nothing on the page is rounded and nothing casts a shadow.

## Layout Metrics

- **Frame**: `.site-header, .site-footer, main { width: min(864px, calc(100% - 80px)); margin-inline: auto }` (x=288 at 1440).
- **Article**: `.article-page { padding: 28px 18px 32px }`; header block left-aligned at x=306; `.article-body { max-width: 720px; margin: auto }` centred inside the frame (x=360–1080), so the body sits 54px further in than the header.
- **Rhythm**: paragraphs margin 0 0 16px; h2 32px above and 14px below; h3 25px / 12px; list items 5px apart; `hr` 25px above and below.
- **Pull quotes**: padding 18px 22px, margin 20px 0.
- **Figures**: poster and wide figures fill 720px; small diagrams are centred at max-width 65% with an italic caption under them.
- **BibTeX**: padding 18px, horizontal scroll.
- **Footer**: padding 12px 17px 16px, 1px top rule, italic 12px, space-between.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >850px | (100% − 864px)/2, minimum 40px | 17px | 38px | header nav 30px gaps |
| ≤850px | 20px each side (frame 100% − 40px) | 17px | 38px | — |
| ≤620px | 18px each side; article page padding 24px 0 | 16px | 29px | header wraps (min-height 60px), wordmark 17px, nav 14px with 16px gaps and 40px tap targets; h2 25px, h3 20px; pull-quote padding 15px; footer stacks |

## Components

- **Site header**: 50px flex row, space-between, 1px #cccbd0 bottom rule; monogram image + divider + 21px Georgia name; text nav at 15px with the current page in #794590 and underlined (offset 7px).
- **Dateline kicker** (`.eyebrow`): Georgia 10px, uppercase, letter-spacing 1.8px, #484653, items joined by " · ".
- **Slash link row** (`.paper-links`): flex, gap 12px, 14px plum links; every link after the first is preceded by a #484653 "/" with 12px right margin. No buttons, no icons.
- **Contents list**: h2 "Contents", then each section as a bold 17px plum link paragraph and its subsections as a bulleted plum list.
- **Pull quote** (`blockquote`, `.custom-box`): no outer border except a 2px #a18bad left rule, fill #f1edf2, padding 18px 22px, text #484653 at 17px/400.
- **Figure with caption**: a centred wrapper (margin 1.5em 0) with the image at max-width 65% and an italic 15px #666666 caption 0.5em below, prefixed "Figure:"; these are inline styles in the post, not stylesheet rules.
- **Updates note**: h3 "Updates in progress. More coming soon!" followed by a dated line with a calendar emoji and a bold date.
- **BibTeX block** (`pre`): #f1edf2, padding 18px, 12px mono, #484653, square corners.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Personal site header | yes | monogram, name, three-link nav |
| Venue | present but non-standard | only in the dateline kicker ("2025 · ICLR · …") and on the poster |
| Title / authors | yes | left-aligned Georgia title, author line with owner in bold |
| Link buttons | present but non-standard | a slash-separated text link row instead of buttons |
| Table of contents | yes | in-body list of plum links |
| Teaser | present but non-standard | the conference poster image serves as the teaser |
| Abstract | absent from the source | the Background section opens the argument |
| Method / theory | yes | prose with MathJax and small diagrams |
| Pull quotes / callouts | yes | mauve boxes with a plum-gray left rule |
| Results tables | absent from the source | results are figures and prose |
| BibTeX | yes | mauve mono block |
| Footer | yes | italic small print over a hairline |

## Adapting to Other Content

- **A project page with buttons**: keep the slash link row; if more prominence is needed, set the row in 15px and add the venue to the dateline rather than introducing pills.
- **More authors and affiliations**: keep one 14px author line (owner bold) and add affiliations as a second 14px #484653 line; numbered superscripts in plum.
- **A results table**: Georgia 15px, header row 700 with a 1px #cccbd0 rule under it, no fills; mark the best value in bold, not in color.
- **Long publication or news lists**: use the site's writing-row pattern: 200×112.5px thumbnail plus a 9–10px uppercase kicker, a 24px title link in ink, and a 15px #484653 summary, separated by #cccbd0 hairlines.
- **A video**: embed at the full 720px column with an italic caption, no frame.

## Do's and Don'ts

- Do set everything in Georgia: one family, with size and weight doing the hierarchy.
- Do keep a single accent, plum #794590, for links and the current nav item.
- Do use the tiny tracked uppercase dateline above the title.
- Don't add rounded corners, shadows or buttons.
- Don't color callouts individually; all of them use #f1edf2 with a #a18bad rule.
- Don't centre the title block; it is left-aligned like a magazine article.

## Surfaces

One warm off-white surface (#faf9f7); pale mauve (#f1edf2) for pull quotes and code; hairlines (#cccbd0) for structure. Images blend into the paper.

## Imagery

The ICLR conference poster as a wide lead image, schematic diagrams of server-based versus decentralized learning in light pastel line art, theory figures and plots; captions in italic. No photography.

## Layout

Personal-site frame of 864px; left-aligned article header; a 720px reading column for contents, poster, Background, Main Results, Future Work and Citation; footer. Page height about 11,650px at 1440 wide.

## Agent Prompt Guide

Quick colors: paper #faf9f7, ink #101020, muted #484653, plum #794590, hairline #cccbd0, quote fill #f1edf2, quote rule #a18bad.

1. "Build an editorial article header on #faf9f7, left-aligned: back link '← Writing' 13px #794590; dateline Georgia 10px uppercase, letter-spacing 1.8px, #484653; title Georgia 38px/700, line-height 1.15, letter-spacing -0.8px, #101020, max-width 760px; authors 14px with the first author bold; then a 1px #cccbd0 rule with 22px padding above it."
2. "Make a slash-separated link row: flex, gap 12px, Georgia 14px links in #794590, each link after the first preceded by a '/' in #484653 with 12px right margin; no buttons or icons."
3. "Create a pull quote: background #f1edf2, 2px solid #a18bad left border only, padding 18px 22px, margin 20px 0, Georgia 17px text in #484653, square corners."

## Similar Pages

- Research explainers published as posts on a personal academic site, styled like a journal or magazine.
- Serif-only blog layouts with a single accent color and in-body contents lists.

## Quick Start

```css
:root {
  --paper: #faf9f7;
  --ink: #101020;
  --muted: #484653;
  --accent: #794590;
  --line: #cccbd0;
  --quote-bg: #f1edf2;
  --quote-rule: #a18bad;
  --serif: Georgia, 'Times New Roman', serif;
  --frame: min(864px, calc(100% - 80px));
  --measure: 720px;
}
body { background: var(--paper); color: var(--ink); font: 16px/1.4 var(--serif); }
.article-body { max-width: var(--measure); margin: auto; font-size: 17px; line-height: 1.6; }
```

## Provenance

- **URL**: https://raiden-zhu.github.io/blog/2025/DICE/
- **Paper**: DICE: Data Influence Cascade in Decentralized Learning (arXiv 2507.06931), Tongtian Zhu, Wenhao Li, Can Wang, Fengxiang He.
- **Venue**: ICLR 2025.
- **Selection reason**: the arXiv abstract links this page and the comment states acceptance at ICLR 2025.
- **Template credit**: the author's own site design (`research-home.css`, `research-pages.css`); no third-party template credited.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the site stylesheets and page HTML read directly, on 2026-10-28.
