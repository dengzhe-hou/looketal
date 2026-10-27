# Peking Crimson Broadsheet — Style Reference

> A cream newsprint dossier stamped in Peking crimson, with typewriter labels and a serif masthead.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the sticky nav, hero heading, role chips, avatar, lede paragraphs, badge row, link buttons, sections, news cards and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the site's two Astro stylesheets (`venue.*.css`, `Recruit.*.css`) with the HTML. The default Chinese version was measured (`html[lang=zh-CN]`). Positions are document coordinates at 1440px wide.

## Overview

Yaodong Yang's homepage is a fully art-directed Astro site in a cream (#f5f1e8) ground with a 24px dot grid, ink-black (#0a0a0a) type and a single accent, Peking University crimson (#8c1515). A sticky translucent nav carries the PKU seal and name, plain Chinese section links with a crimson underline on hover, a crimson "招聘中 →" recruiting button and an outlined EN / 中文 switch. The hero opens with a huge 74.88px serif name (杨耀东), a light Inter romanized line, two square-cornered mono chips (one crimson, one outlined), a round portrait with a cream ring, four justified paragraphs with crimson bold highlights, a mono key-value badge row and square mono link buttons. Below come a beige stats band with 48px serif numerals and italic crimson plus signs, two partner cards, then long sections ("新闻", "研究方向", "获奖", "团队培养", "论文发表"…) introduced by 64px serif headings with a small crimson square, news as white cards with a crimson left edge and a faint star, and a black footer.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): cream #f5f1e8 53.2%, dusty rose-grey #b59f98 12.3% (crimson text anti-aliasing and the portrait), beige #efeae1 10.1% (dot grid and rules), cream variants #f6f1e8 8.3%, #f5f1e7 7.7%, #f7f3ea 6.2%, remainder under 2%. Crimson appears in the recruiting button, the first chip and dozens of bold phrases; black in the name and the primary link button.

Anatomy in DOM order (y = top of element box, content x 190–1250):

1. **Sticky nav** (`nav.top`), y 0, 1440×69 including a 1px #d9d4c5 bottom border, background rgba(245,241,232,0.88) with saturate(180%) blur(14px); inner `.wrap` 68px tall, flex, gap 24px.
2. **Brand** (`a.brand`), x 190: a 32px PKU seal image and "杨耀东" in PingFang SC / Microsoft YaHei 18.4px/600 #0a0a0a.
3. **Nav links**, centered group, Inter 14.08px/400 #1f1f1f, gap 22px; hover #8c1515 with a 1px crimson underline that scales in from the left.
4. **Recruit button** (`a.nav-cta`), "招聘中 →", JetBrains Mono 11.52px/600 uppercase, letter-spacing 0.05em, white on #8c1515, radius 3px, padding 6px 12px, shadow 0 4px 14px -6px rgba(140,21,21,0.45); then **language switch** (`a.lang`) mono 11.52px, 1px #0a0a0a border, padding 5px 10px. Hero top padding 90px.
5. **Name** (`.hero h1`), y 159, "杨耀东", 74.88px (`clamp(40px, 5.2vw, 76px)`), weight 400 with the given name at 500, line-height 1.02, letter-spacing -0.03em, #0a0a0a, left, no wrap. Gap 14px.
6. **Romanized line** (`h1 .cn`), y 249, "Yaodong Yang · 博雅青年学者", Inter 300 at 0.28em (20.97px), #6b6b6b, letter-spacing 0.04em. Gap 32px.
7. **Role chips** (`.title-stack`), y 303, gap 10px: crimson chip (#8c1515 fill, white mono 11.52px/500, padding 6px 11px, square corners) and a linked outlined chip (#ffffff, 1px #0a0a0a border, "↗" at 55% opacity; hover fills black).
8. **Portrait** (`a.hero-avatar`), x 1102, y 159, 148px circle with a cream 6px ring and a 1px #d9d4c5 outer ring, shadow 0 18px 32px -18px rgba(0,0,0,0.25); hover shows a crimson overlay "↓ 下载照片". Gap 32px to the lede.
9. **Lede** (`.hero .role p`), y 367, four justified paragraphs, Inter 15.2px/1.68, #1f1f1f, 14px apart; bold runs 600 #8c1515, italics #0a0a0a for journal names.
10. **Badge row** (`.hero .badges`), y about 830, 1px #d9d4c5 top rule with 28px padding: mono key-value pairs, keys 10.88px uppercase #6b6b6b, values 11.52px/600 #8c1515, separated by #d9d4c5 dots. The fold cuts here.
11. **Link buttons** (`.hero .links`), y 896: "→ Google Scholar" primary (#0a0a0a fill, white mono 11.84px, padding 9px 14px), then "DBLP", "对齐小组", "联系方式" (#ffffff, 1px #d9d4c5 border, #0a0a0a text); square corners; hover crimson fill.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Cream | #f5f1e8 | `--bg` | Page background (with a 24px rgba(10,10,10,0.035) dot grid), nav glass, awards and résumé sections, footer text |
| Beige | #ebe5d4 | `--bg-2` | Stats band, team section, mini-thumb fills |
| Card White | #ffffff | `--card` | Outlined chips, link buttons, news cards, filter bar |
| Ink | #0a0a0a | `--ink` | Name, headings, stat numerals, primary link button fill, footer background, venue tags |
| Ink 2 | #1f1f1f | `--ink-2` | Nav links, lede paragraphs, body text |
| Muted | #6b6b6b | `--muted` | Romanized name, badge keys, stat labels, news dates and summaries |
| Rule | #d9d4c5 | `--rule` | Nav bottom border, section-head underline, card borders, link-button borders, badge dots, avatar outer ring |
| Rule Soft | #e5e1d4 | `--rule-soft` | Paper-note tag fill |
| PKU Crimson | #8c1515 | `--pku` | Recruit button, first role chip, bold lede highlights, heading squares, plus signs in stats, news left edges and stamps, link hover fills |
| PKU Dark | #5e0e0e | `--pku-dark` | Hover state of crimson buttons, avatar gradient end |
| PKU Soft | #f1dada | `--pku-soft` | Hero eyebrow fill, featured mini-thumb fill |
| Gold | #b8860b | `--gold` | Media tags and spotlight paper notes |
| Talk Navy | #1e3a5f | `.tag-talk` | Talk tags in news, embodied thumbnails text |
| Warm Partner | #7c2d12 | `.accent-warm .card-name` | 灵初智能 partner card name (card glow #fff7ed → #fef3c7) |
| Cool Partner | #1e1b4b | `.accent-cool .card-name` | 逆矩阵科技 partner card name (card glow #eef2ff → #dbeafe) |

## Tokens — Typography

- **Display serif**: declared `"Fraunces", Georgia, serif` for the name, section headings, stat numerals, news and topic titles. Rendered: Fraunces 400, 500, 600 and italics (`fonts_loaded`). Fraunces has no CJK glyphs, so the Chinese characters in the name and headings fall back to the system serif (a Song style on this Windows render). Substitute: Newsreader for Latin, paired with Noto Serif SC for the Chinese, which matches the render's serif CJK.
- **Sans**: declared `"Inter", "Noto Sans SC", system-ui, sans-serif`. Rendered: Inter 300–700 and Noto Sans SC 300–700 for Chinese body text.
- **Mono**: `"JetBrains Mono", ui-monospace, monospace` for chips, buttons, labels, dates, tags (400–600 loaded).
- **Brand**: `"PingFang SC", "Microsoft YaHei", "Source Han Sans SC", "Noto Sans SC"` for the nav name.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Name | `.hero h1` | 74.88px / 1.02, -0.03em | 400 (given name 500) | #0a0a0a |
| Section heading | `.sec-head h2` | 64px (`clamp(40px, 5vw, 64px)`) / 1, -0.035em | 500 | #0a0a0a |
| Stat numeral | `.stat .n` | 48px / 1, -0.03em, lining | 500 (plus sign 400 italic #8c1515) | #0a0a0a |
| Featured news title | `.news-featured h3` | 27.2px / 1.2, -0.015em | 500 | #0a0a0a |
| Topic title | `.topic h3` | 24.8px / 1.1 | 500 | #0a0a0a |
| Romanized name | `.hero h1 .cn` | 20.97px (0.28em), 0.04em | 300 | #6b6b6b |
| Partner name | `.partner-card .card-name` | 20px | 600 | #7c2d12 / #1e1b4b |
| Brand | `nav.top .brand` | 18.4px | 600 | #0a0a0a |
| Body | `body` | 16px / 1.6 | 400 | #0a0a0a |
| News item | `.news-grid .item p` | 15.68px / 1.55 | 400 | #1f1f1f |
| Lede | `.hero .role` | 15.2px / 1.68, justified | 400 (bold 600 #8c1515) | #1f1f1f |
| Nav link | `.nav-links a` | 14.08px | 400 | #1f1f1f |
| Link button | `.hero .links a` | 11.84px mono | 400 | #ffffff / #0a0a0a |
| Chip, nav CTA, stat label | `.chip-role`, `.nav-cta`, `.stat .label` | 11.52px mono (CTA and labels uppercase) | 500 / 600 / 400 | per element |
| News stamp | `.news-featured .stamp` | 11.2px mono, uppercase, 0.18em | 600 | #8c1515 |
| Badge key | `.badge-kv .k` | 10.88px mono, uppercase, 0.08em | 400 | #6b6b6b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Role chips, link buttons, news cards, stat band | 0 | chips 1px #0a0a0a or #8c1515; buttons 1px #d9d4c5; cards 1px #d9d4c5 with 3px #8c1515 left | none |
| Nav CTA, nav toggle | 3px | 1px #8c1515 / #d9d4c5 | CTA 0 4px 14px -6px rgba(140,21,21,0.45) |
| Section-head square | 0 | none (10×10px #8c1515 block) | none |
| Portrait | 50% | none | 0 0 0 6px #f5f1e8, 0 0 0 7px #d9d4c5, 0 18px 32px -18px rgba(0,0,0,0.25) |
| Partner card logo tile | 8px | none | 0 2px 8px -3px rgba(0,0,0,0.12) |
| Hero eyebrow, mark | 2px | none | none |

Corners are square almost everywhere; only the portrait, logo tiles and the CTA are rounded.

## Layout Metrics

- **Container**: `.wrap` max-width 1140px, padding 0 40px, so content spans x 190–1250 (1060px). `.wrap-sm` is 980px.
- **Nav**: 68px tall, sticky, gap 24px.
- **Hero**: padding 90px 0 60px; avatar 148px top right beside the name; chips 32px below the name block; lede 1060px wide, justified; badges 36px below with 28px padding over a rule; links 20px below, gap 10px.
- **Stats band**: full width #ebe5d4 between 1px #d9d4c5 rules; 4 equal columns, padding 36px top and bottom, cells 24px side padding with 1px left dividers.
- **Sections**: padding 96px 0; `.sec-head` has a 1px #d9d4c5 bottom rule, 20px padding, 56px margin below.
- **News**: featured cards in a 2-column grid; each card padding 36px 44px, 48px bottom margin; dated list as a 140px / 1fr grid with 24px row and 40px column gaps.
- **Footer**: #0a0a0a, padding 80px 0 60px. Rendered height about 20,750px at 1440px (long publication list).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >960px | 40px inside a 1140px wrap | 16px | 74.88px name, 64px headings | as described |
| ≤960px | 40px | 16px | 5.2vw name (49.9px at 960) | nav links move into a toggle drop-down; stats 2×2 without dividers; topics, press, service, footer, publications and CV grids go single column; featured news one column |
| ≤820px | 40px | 16px | fluid, name may wrap | hero top reverses (portrait above the name), portrait 120px |
| ≤640px | 20px (nav 16px, 56px tall) | 16px | `clamp(30px, 9vw, 48px)` name, `clamp(32px, 9vw, 48px)` headings | hero padding 48px 0 36px, portrait 96px; sections 56px; stat numerals 35.2px |

## Components

- **Crimson CTA**: inline-flex, JetBrains Mono 11.52px/600 uppercase 0.05em, white on #8c1515, 1px #8c1515 border, 3px radius, padding 6px 12px, soft crimson drop shadow; hover #5e0e0e and translateY(-1px), the arrow slides 3px right.
- **Role chip**: mono 11.52px/500, padding 6px 11px, square corners; red variant #8c1515 fill with white text; outlined variant #ffffff with 1px #0a0a0a border and a faded "↗"; hover fills #0a0a0a.
- **Square link button**: mono 11.84px, padding 9px 14px, 1px #d9d4c5 border on #ffffff, #0a0a0a text; primary black fill with an arrow; hover crimson fill and white text.
- **Badge row**: mono key-value pairs on one line over a 1px #d9d4c5 rule, keys small uppercase #6b6b6b, values #8c1515 600, separated by #d9d4c5 middle dots.
- **Stat cell**: Fraunces 48px/500 numeral with an italic #8c1515 "+" or "#", a mono 11.52px uppercase #6b6b6b label 10px below and a 13.12px #6b6b6b sub-line; 1px #d9d4c5 left divider.
- **Section head**: Fraunces 64px/500 heading preceded by a 10×10 #8c1515 square, an optional 0.5em #6b6b6b subtitle, over a full-width 1px #d9d4c5 rule.
- **Featured news card**: #ffffff, 1px #d9d4c5 border with a 3px #8c1515 left edge, padding 36px 44px, a 112px "★" in #8c1515 at 8% opacity top right; stamp line (24px crimson rule, mono 11.2px uppercase "★ 头条新闻 · 2026 年 10 月"), 27.2px Fraunces title, 15.2px #6b6b6b summary, mono 12.48px crimson links with 30% underlines.
- **Footer**: #0a0a0a band, #f5f1e8 text, columns of address and site navigation.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav with CTA | yes | cream glass, crimson recruit button, language switch |
| Name masthead and portrait | yes | 74.88px serif name, round portrait right |
| Role chips | yes | square mono chips |
| Bio | yes | four justified paragraphs with crimson highlights |
| Badge row and links | yes | mono key-values, square buttons |
| Stats strip | yes | beige band, four serif numerals |
| Partner cards | yes | two gradient-glow cards with logos |
| News | yes | featured cards plus a dated list with venue tags |
| Research topics | yes | numbered topic cards |
| Awards | yes | year-led rows with rules |
| Students | yes | beige section with honors |
| Publications | yes | keyword orbit, filter bar, list with mini-thumbs |
| Service and CV | yes | lists and a timeline |
| Footer | yes | black band |

## Adapting to Other Content

- **A project page**: keep the masthead pattern: Fraunces title at 74.88px left, a crimson venue chip and an outlined code chip, a justified lede, and the square mono link buttons.
- **A results table**: square-cornered table on #ffffff with a 1px #d9d4c5 border, mono 11.52px uppercase headers in #6b6b6b, Inter body, best values 600 #8c1515.
- **Long publication lists**: reuse the list with 64px mini-thumbs, black mono venue tags, crimson oral tags and gold spotlight tags; keep the filter bar.
- **More news**: featured cards for the top items, then the 140px date column list with "·" crimson bullets.
- **An English version**: the CSS switches the given-name `.em` to italic crimson for Latin names; keep that.

## Do's and Don'ts

- Do keep one accent: #8c1515 for emphasis, CTAs, markers and highlights; gold and navy only in small tags.
- Do pair a big Fraunces display with JetBrains Mono labels and Inter text.
- Do keep corners square on chips, buttons, cards and tables.
- Do use the cream ground with the dot grid and beige bands for rhythm.
- Don't use pure white as the page background; white is reserved for cards and buttons.
- Don't round buttons into pills.
- Don't bold whole sentences; highlight short phrases in crimson 600.

## Surfaces

Cream #f5f1e8 with a 24px dot grid; beige #ebe5d4 bands for stats and team; white #ffffff cards with #d9d4c5 borders; tinted partner cards with soft radial glows; a black #0a0a0a footer.

## Imagery

One round portrait photo, the PKU seal in the nav, two partner logos in rounded tiles, small square mini-thumbs coded by topic color in the publication list, and a large faint star watermark in featured news. No large figures.

## Layout

A 1140px wrap with left-aligned editorial blocks: masthead and portrait, a four-column stats band, two-column card grids, a dated two-column news list and long single-column lists. Sections alternate cream and beige and are each headed by a ruled masthead heading. Rendered height about 20,750px.

## Agent Prompt Guide

Quick colors: cream #f5f1e8, beige #ebe5d4, card #ffffff, ink #0a0a0a, ink-2 #1f1f1f, muted #6b6b6b, rule #d9d4c5, crimson #8c1515 (hover #5e0e0e).

1. "Build a masthead on #f5f1e8 with a 24px rgba(10,10,10,0.035) dot grid: a Fraunces 74.88px weight-400 name in #0a0a0a with -0.03em tracking and line-height 1.02; beneath it an Inter 300 line at 0.28em in #6b6b6b; then two square mono chips (JetBrains Mono 11.52px/500, padding 6px 11px), the first #8c1515 with white text, the second #ffffff with a 1px #0a0a0a border; a 148px round portrait on the right with box-shadow 0 0 0 6px #f5f1e8, 0 0 0 7px #d9d4c5."
2. "Add a stats band: full width #ebe5d4 between 1px #d9d4c5 rules, four columns with 36px vertical padding and 1px #d9d4c5 dividers; each a Fraunces 48px/500 #0a0a0a numeral with an italic #8c1515 '+', a JetBrains Mono 11.52px uppercase #6b6b6b label and a 13.12px #6b6b6b sub-line."
3. "Add a featured news card: #ffffff with a 1px #d9d4c5 border and a 3px #8c1515 left border, padding 36px 44px, a faint #8c1515 star at 8% opacity top right, a mono 11.2px uppercase #8c1515 date stamp after a 24px crimson rule, a 27.2px Fraunces title and a 15.2px #6b6b6b summary."

## Similar Pages

- Editorial academic homepages built with Astro or Next that use a newsprint palette and a university accent color.
- Stanford-cardinal-style personal sites (a similar crimson) with serif mastheads.

## Quick Start

```css
:root {
  --bg: #f5f1e8;
  --bg-2: #ebe5d4;
  --card: #ffffff;
  --ink: #0a0a0a;
  --ink-2: #1f1f1f;
  --muted: #6b6b6b;
  --rule: #d9d4c5;
  --rule-soft: #e5e1d4;
  --pku: #8c1515;
  --pku-dark: #5e0e0e;
  --pku-soft: #f1dada;
  --gold: #b8860b;
  --sans: "Inter", "Noto Sans SC", system-ui, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, monospace;
  --serif: "Fraunces", Georgia, serif;
}
body { background: var(--bg) radial-gradient(circle at 1px 1px, rgba(10,10,10,.035) 1px, transparent 0) 0 0 / 24px 24px; }
```

## Provenance

- **URL**: https://yangyaodong.com/
- **Person**: 杨耀东 Yaodong Yang, Peking University Institute for Artificial Intelligence (博雅青年学者).
- **Venue / award**: ACL 2025 Best Paper, as last author of "Language Models Resist Alignment" (https://2025.aclweb.org/program/awards/).
- **Selection reason**: existing verified entry, kept unchanged; chosen as a fully art-directed page with bilingual serif display type, a crimson accent, a stats strip and editorial news cards.
- **Template credit**: none stated; custom Astro build.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture, the two Astro CSS bundles and `index.html`. Date 2026-10-28.
