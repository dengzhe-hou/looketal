# Scholar's Ledger — Style Reference

> A white sheet laid on a slate desk: a sidebar of credentials, slate-gray cards of research and repositories, and a dotted timeline of honours with crimson highlights.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's own `/assets/css/main.css` (a Jekyll site, its header reads "Modern academic style, Jekyll-driven") and `index.html`, plus probes of rendered elements. The page is in Simplified Chinese; the system sans stack renders Segoe UI for Latin text and Microsoft YaHei for Chinese on Windows.

## Overview

A Chinese-language academic homepage, about 3,290px tall at 1440. The page is a 1200px white sheet (#ffffff) with a soft shadow, centred on a pale slate ground (#f7f8fa). A sticky translucent header carries the name 邱锡鹏 in 24px/700, a muted affiliation line with a blue "OpenMOSS" link, and a small tab-style nav (首页, 学生, 研究方向与代表性论文, English) whose current item sits on a #f7f8fa pill. Below, a 260px left sidebar (rounded portrait, small uppercase section labels with hairlines, team link, icon links, two book covers, address) runs beside the main column. The main column opens with a muted subtitle and bio paragraphs where project names are set in crimson #b91c1c, then a warm amber recruiting callout with a "招生中" badge. Sections follow, each titled with a 19.2px/600 heading that has a 1px rule and a short 40×2px dark underline: research topic cards (3-up, #f7f8fa fills), open-source project cards with mono repo tiles and amber star counts, and dotted vertical timelines for awards, teaching awards and service, ending with a dashed course list and a centred footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff / #fdfefe / #fafafb / #fffffe / #fffefd 53.7% (the sheet and header); slate ground and card fills #f7f8fa 25.8% (side margins x=0–120 and 1320–1440, topic cards); pale #f5f9f9 8.9% (the portrait's sky and the callout); warm gray #cbc7bf 11.6% (the portrait's trees, the callout border and book covers blended). Blue links and crimson highlights are too small to form a cluster.

Anatomy in DOM order (`.page` max-width 1200px, x=120–1320; sidebar 260px; main column padding 2rem 2.25rem 3rem, so main content runs x=416–1284):

1. **Sticky header** (`header.site-header`, 0–87px): background rgba(255, 255, 255, 0.92) with `backdrop-filter: saturate(150%) blur(6px)`, padding 24px 32px 20px, 1px #e2e6ec bottom border. Name "邱锡鹏" 24px/700 #0f172a; role line 14.4px #64748b with "OpenMOSS" in #1d4ed8; nav right (x=934–1288) at 14.72px, items padding 4.8px 11.2px, 4px radius, 4px gaps; current "首页" 600 #0f172a on #f7f8fa, others #64748b.
2. **Sidebar** (`aside.sidebar`, x=120–380 from y=87): #ffffff, 1px #e2e6ec right border, padding 32px 24px.
3. **Portrait** (x=144, y=119): 211×280px, 8px radius, shadow `0 1px 2px rgba(15, 23, 42, 0.04)`, 16px below.
4. **Sidebar sections** (from y=415): labels 团队主页, 链接, 著作, 联系方式 at 12.48px/700 uppercase, letter-spacing 0.08em, #64748b, with a 1px #d8dde4 bottom rule (padding 6.4px) and 11.2px margin below; link rows 15.2px #1f2937 with 16.8px #64748b icon glyphs, padding 5.6px 0; book covers block 211×100px; book title 14.72px/600 #0f172a; contact 13.76px #64748b.
5. **Hero** (`section.hero`, x=416, y=119, padding 8px 0 24px): subtitle (y=127) 16.8px #64748b; bio paragraphs (y=172 and 213) 16.32px, line-height 1.75, #1f2937, 12px margins; `.hl` names (MOSS, NEX, FastNLP, FudanNLP) 600 #b91c1c.
6. **Recruiting callout** (y=330, 868×89px): `background: linear-gradient(180deg, #fdf6ec 0%, #fbf2e3 100%)`, 1px #e8d8b3 border, 8px radius, padding 13.6px 17.6px, flex with 16px gap; badge "招生中" 12px/700 #ffffff on #b45309, 999px radius, padding 3.2px 8.8px; text 15.2px #6b4019; links 600 #92400e. 32px below.
7. **Research heading** (`h2`, y=451): 19.2px/600 #0f172a, padding-bottom 8px, 1px #d8dde4 bottom border with a 40×2px #0f172a bar at its left end (`h2::before`). Intro sentence 16px #1f2937.
8. **Topic cards** (y=550): `repeat(auto-fit, minmax(220px, 1fr))` → three 280px columns, 13.6px gap; first row visible, second row from y≈670.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Sheet White | #ffffff | --c-bg | page sheet, header (at 92%), sidebar, project cards, footer |
| Slate Ground | #f7f8fa | --c-surface | body background, topic cards, repo tiles, current-nav pill, nav hover |
| Badge Gray | #eef1f5 | --c-surface-2 | project-card badges ("LLM Series", "Textbook") |
| Border | #e2e6ec | --c-border | header and sidebar borders, card and tile borders, footer top border, dashed course separators |
| Rule | #d8dde4 | --c-rule | h2 rules, sidebar label rules, timeline spine |
| Text | #1f2937 | --c-text | body text, sidebar links |
| Muted | #64748b | --c-muted | subtitle, nav, sidebar labels, card descriptions, years, timeline dot rings, footer |
| Heading | #0f172a | --c-heading | name, h2 and its 2px underline bar, card titles, repo names |
| Link Blue | #1d4ed8 | --c-link | links, "GitHub Org →", card hover border |
| Link Hover | #1e3a8a | --c-link-h | link hover |
| Crimson | #b91c1c | --c-accent | `.hl` highlights in bio and award names |
| Amber Badge | #b45309 | (literal) | "招生中" badge fill, star-total text |
| Callout Top / Bottom | #fdf6ec → #fbf2e3 | (literal) | recruiting callout gradient |
| Callout Border | #e8d8b3 | (literal) | recruiting callout border |
| Callout Text | #6b4019 | (literal) | recruiting text |
| Callout Link | #92400e | (literal) | recruiting links |
| Star Amber | #f59e0b | (literal) | star icons; also rgba(245, 158, 11, 0.12) star-total pill fill |
| Shadow | rgba(15, 23, 42, 0.06) | --shadow-md | sheet shadow `0 4px 16px` |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (all text) | -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Source Han Sans CN", "Noto Sans CJK SC", "Helvetica Neue", Helvetica, Arial, sans-serif | no web font; Segoe UI for Latin and Microsoft YaHei for Chinese on Windows (PingFang SC on macOS) | Noto Sans SC |
| Mono | ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace | system mono (Consolas on Windows) | JetBrains Mono |
| Icons | icomoon | icomoon (loaded) | — |
| Serif (declared for `.hero__title`, unused on this page) | "Source Serif Pro", "Source Serif 4", "Noto Serif SC", … | not rendered | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.site-header__name` | 1.5rem = 24px / 700, letter-spacing -0.01em | #0f172a |
| Section heading | `.layout-content h2` | 1.2rem = 19.2px / 600 / 1.7, letter-spacing -0.01em | #0f172a |
| Sidebar label | `.sidebar h2` | 0.78rem = 12.48px / 700 uppercase, letter-spacing 0.08em | #64748b |
| Body | `body` | 16px / 400 / 1.7 | #1f2937 |
| Hero subtitle | `.hero__subtitle` | 1.05rem = 16.8px | #64748b |
| Hero bio | `.hero__bio` | 1.02rem = 16.32px / 1.75 | #1f2937 |
| Nav | `.site-nav` | 0.92rem = 14.72px; current 600 | #64748b / #0f172a |
| Topic title / desc | `.topic-card__title` / `__desc` | 15.68px / 600 and 14.08px / 1.6 | #0f172a / #64748b |
| Project name | `.project-card__name` | 16.32px / 700 | #0f172a |
| Project badge | `.project-card__badge` | 11.52px / 600, letter-spacing 0.02em | #64748b |
| Repo name | `.repo-name` | mono 13.12px / 600 | #0f172a |
| Timeline row | `.list-academic > li` | 15.36px / 1.7 | #1f2937 |
| Timeline year | `.list-academic .year` | 14.08px / 600, tabular numerals | #64748b |
| Footer | `.site-footer` | 13.76px, centred | #64748b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Page sheet | 0 | none | `0 4px 16px rgba(15, 23, 42, 0.06)` |
| Portrait | 8px | none | `0 1px 2px rgba(15, 23, 42, 0.04)` |
| Topic, project cards, callout | 8px | 1px #e2e6ec (callout 1px #e8d8b3) | none; project hover `0 1px 2px rgba(15, 23, 42, 0.04)` |
| Repo tiles, nav items, book cover | 4px | tiles 1px #e2e6ec | none |
| Badges, star pill | 999px | none | none |
| Section heading | 0 | 1px #d8dde4 bottom + 40×2px #0f172a bar | none |
| Timeline | 0 | 2px #d8dde4 left spine; 8px dots with 2px #64748b ring on #ffffff (hover #1d4ed8) | none |
| Course rows | 0 | 1px dashed #e2e6ec bottom | none |

## Layout Metrics

- **Sheet**: `.page { max-width: 1200px; margin: 0 auto }` → x=120–1320 on #f7f8fa; flex column with min-height 100vh.
- **Columns**: `@media (min-width: 880px) .layout-with-sidebar { grid-template-columns: 260px 1fr }`; sidebar padding 32px 24px; content padding 32px 36px 48px → main content 868px at x=416–1284.
- **Header**: sticky, padding 24px 32px 20px, 87px tall.
- **Sections**: `.section { margin: 2rem 0 }` (32px); h2 margin 32px 0 13.6px with 8px padding-bottom.
- **Topic grid**: auto-fit minmax(220px, 1fr), gap 13.6px → 3 × 280px; card padding 13.6px 16px.
- **Project grid**: 3 columns ≥720px, gap 13.6px, the feature card spans all three; card padding 14.4px 16px; repo tiles in an auto-fit minmax(240px, 1fr) grid with 5.6px gaps, padding 6.4px 9.6px.
- **Timeline lists**: 2px left spine; rows grid 64px year + 1fr, gap 16px, padding 8.8px 0 8.8px 20px; dot at left -5px, top 17.6px.
- **Footer**: 1px #e2e6ec top border, padding 20px 32px, centred.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| ≥880px | 36px main padding | 16px | 24px | 260px sidebar + main column |
| <880px | 36px | 16px | 24px | sidebar moves above content as a 140px photo + info grid with a bottom border |
| <720px | 36px | 16px | 24px | project cards one column |
| ≤640px | 20px | 16px | 24px | content padding 24px 20px 32px; tables 13.76px |
| ≤540px | 20px | 16px | 24px | callout stacks badge above text |
| ≤520px | 20px | 16px | 24px | timeline rows stack year above text (year 13.12px) |
| ≤480px | 20px | 16px | 24px | sidebar becomes one column |

## Components

- **Section heading** (`h2`): 19.2px/600 #0f172a, 8px padding-bottom, 1px #d8dde4 bottom border, plus a 40×2px #0f172a bar (`h2::before`, radius 1px) sitting on the left end of the rule. Optional star-total pill to the right (12.48px/600 #b45309 on rgba(245, 158, 11, 0.12), 999px radius, padding 1.6px 8px, star in #f59e0b).
- **Topic card**: #f7f8fa, 1px #e2e6ec, 8px radius, padding 13.6px 16px; 15.68px/600 #0f172a title, 4.8px gap, 14.08px #64748b description. Hover: border #1d4ed8, translateY(-1px).
- **Project card**: #ffffff, 1px #e2e6ec, 8px radius, padding 14.4px 16px; head row with 16.32px/700 name, a #eef1f5 pill badge (11.52px/600 #64748b) and a right-aligned 13.6px/600 #1d4ed8 "GitHub Org →"; 14.08px #64748b description; repo tiles (#f7f8fa, 1px #e2e6ec, 4px radius, mono 13.12px/600 name, star count with a 12px #f59e0b star). Hover: border #1d4ed8, lift 1px, faint shadow.
- **Recruiting callout**: amber gradient box (#fdf6ec → #fbf2e3), 1px #e8d8b3, 8px radius, padding 13.6px 17.6px; #b45309 pill badge with white 12px/700 text; #6b4019 text with 600 #92400e links followed by "→".
- **Timeline list**: 2px #d8dde4 spine; each row has an 8px white dot with a 2px #64748b ring, a 64px year column (14.08px/600 #64748b, tabular numerals) and 15.36px text; highlighted award names in 600 #b91c1c; paper titles as #1d4ed8 links.
- **Sidebar label**: 12.48px/700 uppercase #64748b, 0.08em tracking, 1px #d8dde4 rule below.
- **Nav tab**: 14.72px, padding 4.8px 11.2px, 4px radius; current 600 #0f172a on #f7f8fa; hover the same fill.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header with tab nav | yes | translucent white, blurred, current tab on slate pill |
| Sidebar profile | yes | portrait, labelled link groups, book covers, address |
| Bio with highlights | yes | crimson 600 project names |
| Recruiting callout | yes | amber gradient box with "招生中" badge |
| Research topics | yes | 3-up slate cards |
| Open-source projects | yes | feature card + three cards, mono repo tiles with star counts |
| Academic awards | yes | dotted timeline |
| Teaching awards, service | yes | dotted timelines (service grouped by sub-headings) |
| Courses | yes | dashed-separator list |
| Publications | present but non-standard | on a separate page; the homepage shows award papers inside the timeline |
| Footer | yes | centred muted line |

## Adapting to Other Content

- **Publications**: use the stylesheet's `.pub-list` timeline (same 2px spine and dots, 64px year column) with 600 #0f172a titles, 14.72px #64748b author lines, and 14.08px #1d4ed8 links; abstracts open in #f7f8fa boxes with a 3px #1d4ed8 left border.
- **A results table**: use the content table recipe (14.88px, cells padding 10.4px 14.4px, 1px #e2e6ec row rules, header on #f7f8fa with a 2px #d8dde4 bottom border, row hover #f7f8fa).
- **News**: reuse the timeline rows with dates in the 64px column.
- **Students**: the stylesheet's student groups use small colored labels (amber #fef3c7/#92400e for PhD, indigo #e0e7ff/#3730a3 for MS); keep them to the students page.
- **English version**: keep the same layout; Latin text renders in Segoe UI and the uppercase sidebar labels gain their full 0.08em tracking.

## Do's and Don'ts

- Do keep the white sheet on #f7f8fa with only the 0 4px 16px 6% shadow.
- Do mark every section heading with the 1px rule plus the 40×2px dark bar.
- Do reserve crimson #b91c1c for highlighted names and awards, blue #1d4ed8 for links, and amber for recruiting and stars.
- Do use dotted timelines for awards, teaching and service.
- Don't load a web font; the system CJK stack is part of the look.
- Don't round cards beyond 8px or add heavy shadows.
- Don't use the crimson for links.

## Surfaces

A #f7f8fa ground with a centred #ffffff sheet. Inside, #f7f8fa fills topic cards and repo tiles, #ffffff fills project cards, and a single amber gradient panel carries the recruiting message. The sticky header is white at 92% with a blur.

## Imagery

A 211×280px outdoor portrait with an 8px radius in the sidebar, and two small textbook cover images. No paper figures; icons are icomoon glyphs and small amber star SVGs.

## Layout

A 1200px sheet split into a 260px sidebar and an 868px content column. Content stacks sections with 32px margins: callout, topic grid, project grid, then several timelines. Dense but orderly, like an annotated CV.

## Agent Prompt Guide

Quick colors: ground #f7f8fa, sheet #ffffff, text #1f2937, heading #0f172a, muted #64748b, border #e2e6ec, rule #d8dde4, link #1d4ed8, highlight #b91c1c, amber #b45309.

1. "Build a 1200px #ffffff sheet centred on #f7f8fa with box-shadow 0 4px 16px rgba(15,23,42,.06). Sticky header: rgba(255,255,255,.92), backdrop-filter saturate(150%) blur(6px), padding 24px 32px 20px, 1px #e2e6ec bottom border; name 24px/700 #0f172a, muted 14.4px role line, tab nav (14.72px, padding 4.8px 11.2px, 4px radius, current 600 #0f172a on #f7f8fa). Body grid 260px sidebar (1px #e2e6ec right border, padding 32px 24px) + content with padding 32px 36px 48px."
2. "Style section headings: 19.2px/600 #0f172a, padding-bottom 8px, border-bottom 1px solid #d8dde4, and a ::before bar 40px × 2px #0f172a at bottom -1px left 0. Topic cards in a repeat(auto-fit, minmax(220px, 1fr)) grid with 13.6px gap: #f7f8fa, 1px #e2e6ec, 8px radius, padding 13.6px 16px, 15.68px/600 title and 14.08px #64748b text; hover border #1d4ed8."
3. "Create a timeline list: 2px solid #d8dde4 left border; rows grid 64px + 1fr, gap 16px, padding 8.8px 0 8.8px 20px; an 8px #ffffff dot with a 2px #64748b ring at left -5px; year 14.08px/600 #64748b tabular; text 15.36px #1f2937 with award names in 600 #b91c1c and paper titles as #1d4ed8 links."

## Similar Pages

- Chinese faculty homepages built on Jekyll with a sidebar profile and timeline sections.
- Lab-leader pages that showcase open-source repositories with live GitHub star counts.

## Quick Start

```css
:root {
  --c-bg: #ffffff;
  --c-surface: #f7f8fa;
  --c-surface-2: #eef1f5;
  --c-border: #e2e6ec;
  --c-rule: #d8dde4;
  --c-text: #1f2937;
  --c-muted: #64748b;
  --c-heading: #0f172a;
  --c-link: #1d4ed8;
  --c-link-h: #1e3a8a;
  --c-accent: #b91c1c;
  --f-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", Arial, sans-serif;
  --radius: 8px;
}
body { margin: 0; font: 16px/1.7 var(--f-sans); color: var(--c-text); background: var(--c-surface); }
.page { max-width: 1200px; margin: 0 auto; background: var(--c-bg); box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06); }
h2 { font-size: 1.2rem; font-weight: 600; color: var(--c-heading); padding-bottom: .5rem; border-bottom: 1px solid var(--c-rule); position: relative; }
h2::before { content: ""; position: absolute; left: 0; bottom: -1px; width: 2.5rem; height: 2px; background: var(--c-heading); }
```

## Provenance

- **URL**: https://xpqiu.github.io/
- **Person**: Xipeng Qiu (邱锡鹏), Professor, Fudan University; field: large language models.
- **Venue / award**: ACL 2024 Outstanding Paper, last author of "L-Eval: Instituting Standardized Evaluation for Long Context Language Models".
- **Selection reason**: Rule A; award listed at https://2024.aclweb.org/program/best_papers/ ; homepage from Semantic Scholar and GitHub xpqiu.
- **Template credit**: custom Jekyll site; the stylesheet header reads "Xipeng Qiu — Academic Homepage, Modern academic style, Jekyll-driven".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `main.css` and `index.html` read directly, and element probes, on 2026-10-28.
