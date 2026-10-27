# Arena Gradient Bulma — Style Reference

> A tidy game-arena scoreboard: a mascot crest over a navy title, then cool grey-blue gradient bands holding news cards and violet-headed score tables.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the title, author links, venue tag, buttons, section headings, tables, sections and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot, a full-height 1440×9000 headless capture for the task and leaderboard sections, and the page's own `static/css/index.css` (heavily customised) over Bulma 0.9 from the Academic Project Page Template. Positions are document coordinates at 1440px wide.

## Overview

GAMEBoT is an Academic Project Page Template build with a large custom stylesheet. The first viewport is white: a 200px "GAMEBOT ARENA" mascot logo with a soft drop shadow, the paper title in Google Sans 40px bold navy (#2c3e50) with a 60×4px violet gradient underline, blue (#209cee) author links, a grey affiliation line, a pale blue "ACL 2025 Main Conference" tag, and three dark (#363636) rounded buttons with icons. A diagonal grey-to-blue gradient band (#f5f7fa → #c3cfe2) then holds "Latest News & Updates": a pale blue rounded notification panel with two white news cards (outlined blue and green "Watch Battle Replay" buttons), a pale yellow results panel with two compact match tables whose headers carry a #667eea → #764ba2 violet gradient and whose winning row is tinted green, and a pale green key-finding box. Every 40px section title gets the same violet underline. The task section alternates white and light grey gradient rows, each pairing a text column (navy task title, justified slate description, a left-ruled "Required Abilities" chip) with a 340px game video framed by a 12px radius, a 2px border and a large shadow. A sortable leaderboard table with a violet gradient header, 15px radius and zebra rows closes the page above a #fafafa template footer.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 66.5%, news band grey-blue #dfe5ef 10.1%, notification pale blue #f3f8fc 6.0%, band light end #f0f3f7 5.6%, mid grey #8c95a1 5.4% (text, logo and button pixels), band mid #e9eff6 4.5%, remainder under 2%. The hero is white even though `.hero` declares a purple gradient: the white `.hero-body` covers it.

Anatomy in DOM order (y = top of element box):

1. **Logo** (`.publication-logo img`), y 48, 200×200, centered, `drop-shadow(0 10px 20px rgba(0,0,0,.2))`. Gap 6px.
2. **Title** (`h1.title.is-2.publication-title`), y 254, one line, Google Sans 40px/45px weight 700, #2c3e50, centered, text-shadow 0 2px 4px rgba(0,0,0,.1); a 60×4px gradient bar (#667eea → #764ba2, 2px radius) sits 10px below the box. Gap 39px.
3. **Authors** (`.publication-authors a`), y 338, Google Sans 20px/30px weight 400, #209cee links, comma separators and superscript numbers in #4a4a4a. Gap about 32px.
4. **Affiliations** (`.publication-authors .author-block`), y about 402, Google Sans 20px/30px, #4a4a4a, centered. Gap about 44px.
5. **Venue tag** (`span.tag.is-large.is-info.is-light`), y 476, 281×40, Noto Sans 20px, #1d72aa on #eef6fc, 4px radius, padding 0 15px. Gap 73px.
6. **Link buttons** (`a.external-link.button.is-normal.is-rounded.is-dark`), y 589, three pills 100–107px wide, 40px tall, 20px apart: #363636 fill, white Noto Sans 16px/500, letter-spacing 0.3px, padding 7px 20px, Font Awesome PDF and GitHub icons and the Academicons arXiv icon on the left, shadow 0 4px 6px rgba(0,0,0,.1). The hero ends at y 694.
7. **News band** (`section.section.is-light`), y 694, gradient 135deg #f5f7fa → #c3cfe2, padding 48px 24px; heading "🚀 Latest News & Updates" y 742, Noto Sans 40px/45px 700 #363636, centered with the violet underline. Gap 52px.
8. **News panel** (`.notification.is-info.is-light`), starts about y 820, 955px wide (four-fifths column), #eef6fc fill, 15px radius, shadow 0 8px 25px rgba(0,0,0,.1); its `h4` at y 839 is 24px/600 #1d72aa and the intro paragraph 16px/24px #1d72aa. The fold cuts through the panel.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Title Navy | #2c3e50 | `.hero-body .title`, `.task-title` | Paper title, task titles |
| Heading Ink | #363636 | Bulma `.title`, `.is-dark` | Section titles, dark link buttons, table cell text |
| Body Grey | #4a4a4a | Bulma body | Body copy, affiliations, author separators |
| Slate | #5a6c7d | `.task-description` | Task descriptions |
| Author Blue | #209cee | `.publication-authors a` | Author names |
| Violet Start | #667eea | gradient start, `.task-abilities` | Title underlines, table headers, abilities chip border and text |
| Violet End | #764ba2 | gradient end | Title underlines, table headers |
| Info Text | #1d72aa | Bulma `is-info is-light` | Venue tag text, news panel heading and text |
| Info Wash | #eef6fc | Bulma `is-info is-light` | Venue tag fill, news panel fill |
| Info Blue | #3298dc | Bulma `is-info` | Connect4 outlined button, "Connect4 Matches" label, card icon |
| Success Green | #48c774 | Bulma `is-success` | Checkers outlined button, "Checkers Matches" label, card icon |
| Win Row | #d4edda | `.has-background-success-light` | Highlighted winning table row |
| Win Rule | #28a745 | same | 4px left border of the winning row |
| Win Text | #155724 | `.has-text-success` | Winning score |
| Warning Wash | #fffbeb | Bulma `is-warning is-light` | "Latest Evaluation Results" panel fill |
| Warning Border | #ffeaa7 | `.notification.is-warning.is-light` | 1px border of that panel |
| Success Wash | #effaf3 | Bulma `is-success is-light` | "Key Finding" box fill |
| Success Text | #257942 | Bulma `is-success is-light` | "Key Finding" box text |
| Band Light | #f5f7fa | `.section.is-light` gradient start | News band |
| Band Blue | #c3cfe2 | `.section.is-light` gradient end | News band |
| Grey Band Start | #f8f9fa | task rows, leaderboard section, even table rows, video caption | Alternating task rows, leaderboard band, zebra rows |
| Grey Band End | #e9ecef | gradient end | Alternating task rows, leaderboard band; caption border |
| Frame Grey | #e0e6ed | `.task-video`, `#leaderboardTable` | Video border, leaderboard border and row rules, section hairlines |
| Caption Grey | #6c757d | `.video-caption` | Italic video captions |
| Model Brown | #574848 | `.model-name` | Model names in the leaderboard |
| Footer Wash | #fafafa | Bulma `.footer` | Footer band |
| Card Edge | #e8f4fd | `.notification.is-info.is-light .card` | 1px news-card border; abilities chip gradient end |
| Cell Rule | #f0f0f0 | `.notification .table td` | 1px bottom rule in match tables |
| Header Hover A | #5a6fd8 | `#leaderboardTable th:hover` | Leaderboard header gradient start on hover |
| Header Hover B | #6a4190 | `#leaderboardTable th:hover` | Leaderboard header gradient end on hover |
| White | #ffffff | page, cards | Hero, news cards, tables, odd task rows |

Declared but not visible: `.hero` sets `linear-gradient(135deg, #667eea, #764ba2)` with a grain pattern, but the white `.hero-body` covers it completely; `.publication-awards` (#ff3860) is unused.

## Tokens — Typography

- **Title and authors**: declared `'Google Sans', sans-serif` (`.publication-title`, `.publication-authors`). Rendered: Google Sans 400 only (`fonts_loaded`), so the 700 title is synthesized bold. Substitute: Figtree, close in width and roundness.
- **Everything else**: declared `'Noto Sans', sans-serif` on `body`. Rendered: Noto Sans 400 only, so the 600/700 headings are synthesized. Substitute: Noto Sans with real 600/700 weights.
- **Icons**: Font Awesome 5 (solid, brands) and Academicons.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 40px / 45px | 700 | #2c3e50 |
| Section title | `h2.title.is-2` | 40px / 45px | 700 | #363636 |
| Task title | `h2.title.is-3.task-title` | 32px / 36px, letter-spacing 0.5px | 700 | #2c3e50 |
| News heading | `h4.title.is-4` | 24px / 27px | 600 | #1d72aa |
| Authors, affiliations | `.publication-authors` (`is-size-5`) | 20px / 30px | 400 | #209cee / #4a4a4a |
| Venue tag | `.tag.is-large` | 20px / 30px | 400 | #1d72aa |
| Task description | `h2.subtitle.is-5.task-description` | 20px, line-height 1.8 | 400 | #5a6c7d, justified |
| Body | `body`, `.content p` | 16px / 24px | 400 | #4a4a4a |
| Buttons | `.button` | 16px / 24px, letter-spacing 0.3px | 500 | white or variant color |
| Table header | `.notification .table th` | 12.8px / 19.2px, uppercase, letter-spacing 0.5px | 600 | white |
| Table cell | `.notification .table td` | 13.6px / 20.4px | 400 | #363636 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link button | 290486px (pill) | 1px transparent | 0 4px 6px rgba(0,0,0,.1); hover 0 6px 12px rgba(0,0,0,.15) and translateY(-2px) |
| Outlined card button | 8px | 1px solid #3298dc or #48c774 | none |
| Venue tag | 4px | none | none |
| News panel | 15px | none | 0 8px 25px rgba(0,0,0,.1) |
| News card | 12px | 1px solid #e8f4fd | 0 4px 15px rgba(0,0,0,.08); hover 0 8px 25px rgba(0,0,0,.12) and translateY(-3px) |
| Results panel | 12px | 1px solid #ffeaa7 | none |
| Match table container | 8px | none | 0 2px 8px rgba(0,0,0,.1) |
| Task video | 12px | 2px solid #e0e6ed (hover #667eea) | 0 8px 25px rgba(0,0,0,.15); hover scale 1.02 |
| Video caption | 6px | 1px solid #e9ecef | none |
| Abilities chip | 8px | 4px solid #667eea on the left | none |
| Leaderboard table | 15px | 1px solid #e0e6ed | 0 8px 25px rgba(0,0,0,.1) |
| Title underline | 2px | none | none; 60×4px gradient bar |

## Layout Metrics

- **Containers**: hero and news use `.container.is-max-desktop` forced to 1200px (`!important`); the four-fifths column inside is 955px (x 242–1197). The task and leaderboard sections use the plain Bulma `.container`, 1344px at ≥1408px (x 48–1392).
- **Hero**: `.hero-body` padding 48px 24px; logo 200px; title margin-bottom 32px; authors margin-bottom 32px; links block margin-top 32px.
- **Sections**: `.section` padding 48px 24px. Section titles get margin-bottom 32px plus the underline 10px below the box.
- **News cards**: two `column is-6` cards in the 955px panel, 12px column padding.
- **Task rows**: `.task-section` padding 32px 0, alternating white and #f8f9fa → #e9ecef rows inset 24px from the page edge by the section padding; text column `is-4 is-offset-2` (about 448px), video column `is-6`, sides swap every row; video 340×340.
- **Leaderboard**: full 1344px container, 11 columns, header padding 20px 15px, cells 18px 15px.
- **Footer**: Bulma footer padding 48px 24px 96px, content in an `is-8` column.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | 1200px hero box, 1344px task container | 16px | 40px | as described |
| 1216–1407px | `.container` 1152px | 16px | 40px | same |
| 1024–1215px | `.container` 960px | 16px | 40px | same |
| 769–1023px | fluid; 24px section padding | 16px | 40px | columns side by side |
| ≤768px | `is-max-desktop` 95%; `.hero-body` padding 32px 16px; task container padding 0 8px | 16px | 40px | task columns stack; abilities chip 14.4px with 8px 12px padding |

## Components

- **Dark pill button**: `a.button.is-rounded.is-dark`, #363636 fill, white Noto Sans 16px/500, letter-spacing 0.3px, padding 7px 20px, height 40px, icon left (Font Awesome or Academicons), shadow 0 4px 6px rgba(0,0,0,.1); hover lifts 2px with shadow 0 6px 12px rgba(0,0,0,.15), 0.3s ease.
- **Venue tag**: `span.tag.is-large.is-info.is-light`, #eef6fc fill, #1d72aa 20px text, 4px radius, 40px tall, padding 0 15px.
- **Section title with underline**: 40px/45px 700 centered, margin-bottom 32px, `::after` 60×4px bar, `linear-gradient(135deg, #667eea, #764ba2)`, 2px radius, 10px below the text box, centered.
- **News card**: white `.card`, 12px radius, 1px #e8f4fd border, shadow 0 4px 15px rgba(0,0,0,.08); a 2x Font Awesome icon left (#3298dc or #48c774), 20px title and 16px subtitle right, a paragraph, and a full-width outlined button (8px radius, colored border and text, play icon left). Hover lifts 3px.
- **Match table**: Bulma `table.is-small.is-striped` inside an 8px-radius container with shadow 0 2px 8px rgba(0,0,0,.1); header row violet gradient with white uppercase 12.8px/600 text, padding 12px 8px; cells 13.6px, padding 10px 8px, 1px #f0f0f0 bottom rule; winner row #d4edda with a 4px #28a745 left border and bold #155724 score.
- **Task row**: two columns, vertically centered; navy 32px task title (hover reveals a 3px violet bar on its left), 20px justified #5a6c7d description with line-height 1.8, then the abilities chip (gradient #f8f9fa → #e8f4fd, 4px #667eea left border, 8px radius, padding 12px 16px, bold dark text); video opposite with an italic #6c757d caption in a #f8f9fa 6px-radius box.
- **Leaderboard table**: 15px radius, 1px #e0e6ed border, shadow 0 8px 25px rgba(0,0,0,.1); violet gradient header (hover #5a6fd8 → #6a4190) with white uppercase 600 labels; cells padding 18px 15px, 1px #e0e6ed rules, even rows #f8f9fa, model names #574848 600; click-to-sort headers.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logo | yes | 200px mascot crest with drop shadow and hover lift |
| Title, authors, affiliations | yes | Google Sans, navy title, blue author links |
| Venue badge | yes | pale blue Bulma tag |
| Link buttons | yes | three dark pills with icons |
| News | yes | gradient band, info panel, two cards, results panel, key-finding box |
| Results tables | yes | compact match tables and a full sortable leaderboard |
| Introduction | yes | 955px justified text with a bulleted list |
| Task gallery | yes | eight alternating text and video rows |
| Interactive demo | yes | SVG negotiation game in the Task 8 row |
| Teaser figure, abstract heading | absent from the source | the Introduction replaces the abstract |
| BibTeX | absent from the source | |
| Footer | yes | Bulma #fafafa template credit |

## Adapting to Other Content

- **More authors**: keep the centered 20px Google Sans line and let it wrap; affiliations stay on their own line below with superscript numbers.
- **A results table**: use the leaderboard recipe (violet gradient header, white uppercase 600 labels, 18px 15px cell padding, #f8f9fa zebra, 15px radius container) and tint the best row #d4edda with a 4px #28a745 left border.
- **News**: add more `.card`s to the info panel two per row; keep one panel per band.
- **Long publication lists**: a white 12px-radius card per item with a 20px navy title and a 16px #4a4a4a venue line, two per row.
- **More tasks or examples**: continue the alternating rows, swapping the video side each time, and reuse the abilities chip for any one-line takeaway.
- **A BibTeX block**: a white band with a section title and underline, then a `pre` on #f8f9fa with a 1px #e0e6ed border and 12px radius.

## Do's and Don'ts

- Do give every section title the 60×4px violet gradient underline.
- Do keep violet (#667eea → #764ba2) for decoration and table headers only; links stay #209cee and buttons #363636.
- Do frame media with 12px radius, a 2px #e0e6ed border and a soft large shadow.
- Do alternate white and #f8f9fa → #e9ecef rows for long repeated content.
- Don't rely on the declared purple hero; the rendered hero is white.
- Don't add hard borders to cards; they use a near-invisible #e8f4fd edge and shadow.
- Don't mix more than three Bulma notification tints (info, warning, success) in one panel.

## Surfaces

White hero, a diagonal #f5f7fa → #c3cfe2 news band, panels in Bulma light tints (#eef6fc, #fffbeb, #effaf3), white cards with soft shadows, alternating white and #f8f9fa → #e9ecef task rows, a #f8f9fa → #e9ecef leaderboard band, and a #fafafa footer. Bands are separated by 1px gradient hairlines fading from transparent through #e0e6ed.

## Imagery

A cartoon mascot crest (two robots dueling over a game board) as the logo, then square gameplay videos of Atari-style and board games (Othello in green, Pong in brown, Surround in red, Checkers in tan) and an SVG negotiation widget, each framed at 340px with rounded corners and shadows. Emoji prefix the news headings.

## Layout

A centered 1200px hero and news column (955px content), then full-width alternating task rows in a 1344px container with text and video columns that swap sides, then a full-width leaderboard. Rendered height is about 9,000px at 1440px.

## Agent Prompt Guide

Quick colors: title #2c3e50, headings #363636, body #4a4a4a, authors #209cee, accent gradient #667eea → #764ba2, info tint #eef6fc with #1d72aa text, band #f5f7fa → #c3cfe2, rows #f8f9fa → #e9ecef, frame #e0e6ed.

1. "Build a white hero, padding 48px 24px, centered: a 200px logo with drop-shadow(0 10px 20px rgba(0,0,0,.2)); a Google Sans 40px/45px bold #2c3e50 title with a centered 60×4px bar in linear-gradient(135deg, #667eea, #764ba2) 10px below; 20px #209cee author links; a 20px #4a4a4a affiliation line; a 40px-tall #eef6fc tag with #1d72aa text and 4px radius; three #363636 pill buttons, white 16px/500 text, padding 7px 20px, icon left, shadow 0 4px 6px rgba(0,0,0,.1), hover lift 2px."
2. "Create a news band: background linear-gradient(135deg, #f5f7fa, #c3cfe2), padding 48px 24px; a 955px #eef6fc panel with 15px radius and shadow 0 8px 25px rgba(0,0,0,.1); inside, two white cards (12px radius, 1px #e8f4fd border, shadow 0 4px 15px rgba(0,0,0,.08)) each with an icon, a title, a paragraph and a full-width outlined button (8px radius, #3298dc or #48c774)."
3. "Make a leaderboard table: 1px #e0e6ed border, 15px radius, shadow 0 8px 25px rgba(0,0,0,.1); header in linear-gradient(135deg, #667eea, #764ba2), white uppercase 600 labels with 0.5px letter-spacing, padding 20px 15px; cells padding 18px 15px with 1px #e0e6ed bottom rules, even rows #f8f9fa, model names #574848 weight 600."

## Similar Pages

- Academic Project Page Template (eliahuhorwitz) builds with a custom gradient layer over Bulma.
- Benchmark pages that combine a news panel and a sortable leaderboard (arena-style evaluation sites).

## Quick Start

```css
:root {
  --title: #2c3e50;
  --heading: #363636;
  --text: #4a4a4a;
  --muted: #5a6c7d;
  --author: #209cee;
  --accent-a: #667eea;
  --accent-b: #764ba2;
  --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --info-bg: #eef6fc;
  --info-text: #1d72aa;
  --band: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  --row: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  --frame: #e0e6ed;
  --font-title: 'Google Sans', Figtree, sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-card: 12px;
  --radius-panel: 15px;
  --shadow-panel: 0 8px 25px rgba(0,0,0,.1);
}
```

## Provenance

- **URL**: https://visual-ai.github.io/gamebot/
- **Paper**: GAMEBoT: Transparent Assessment of LLM Reasoning in Games (arXiv 2412.13602), Wenye Lin, Jonathan Roberts, Yunhan Yang, Samuel Albanie, Zongqing Lu, Kai Han.
- **Venue**: ACL 2025 (Main Conference).
- **Selection reason**: existing verified entry; the arXiv 2412.13602 comment states ACL 2025 and the project page is linked in the abstract. Chosen for the custom logo, the venue pill, accent underlines under section titles, the gradient news band with cards, and score tables with highlighted rows.
- **Template credit**: footer credits the Academic Project Page Template (eliahuhorwitz), adopted from Nerfies.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot, a 1440×9000 headless capture, `static/css/index.css`, `static/css/bargaining.css` and the HTML. Date 2026-10-28.
