# GeoV2V — Style Reference

> A night drive through a film festival lobby: ink-black walls, tight grotesk headlines that fade to gray halfway through, and one violet glow on whatever is "ours".

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the headings, tabs, table and cards), the 1440×900 shot and a full-page capture, and the page's own `styles.css` and `index.html`. The stylesheet is 3,500 lines and layers late overrides over early rules (the `h1` rule says clamp(60px, 7vw, 100px) but a final `.hero-cinema h1` rule sets 44px), so every size below was probed on the rendered element. The large "Change the view. Keep the dynamics." headline in the first viewport is burned into the film's poster frame, not HTML text.

## Overview

A single-column cinematic research page, 10,681px tall, on near-black #07090f with off-white #f0f3f5 text in the system UI face (Segoe UI on Windows). A thin 76px header carries a wordmark ("Geo" bold + "V2V" regular + a 6px violet dot), five 13px gray nav links and an outlined "Read the paper ↗" pill. The hero is compact and centred (tiny uppercase "ECCV 2026" label with a teal dot, a 44px title, a 13px gray subtitle) and hands the viewport to a 1129×636 film player with a frosted "Watch the film" pill. Below, every section opens with an 11px tracked uppercase label ("01 / THE DIFFERENCE IS TIME") and a heavy, tightly tracked two-tone headline whose second sentence is set in gray #a9acb8 ("A scene is more / than one moment."), with a 370px gray paragraph aligned to its baseline on the right. Content is a synced side-by-side video comparison with a segmented 1 m / 2 m / 4 m viewpoint switch, an animated image-formation illustration, a method band on a slightly lifted gradient, results videos behind pill tabs, a bar chart plus an 86px light-violet score, plain hairline tables, a numbered resource list and a BibTeX card. Violet (#baa7ff and lighter tints) marks "ours"; teal #78dce8 is the hover and focus color.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): near-black family #07090f / #06090f / #0a0c14 / #05070b / #080c13 / #070b12 together 75.4%; road gray #373e45 14.5% and sky gray-blue #a7b6c2 10.1%, both from the street footage in the film poster. Violet and teal cover too little area to form clusters.

Anatomy in DOM order (desktop 1440px):

1. **Header** (`header.site-header`, y 0–76): width min(1440px, 100% − 80px) → x 40–1400, flex space-between, 1px #ffffff0d bottom border. Wordmark `a.brand` at x=40: 24px, "Geo" weight 760 and "V2V" weight 400, letter-spacing -1.3px, #f0f3f5, followed by a 6px #baa7ff dot (margin 12px 0 0 3px). Nav centred at y=27: 13px/400 #b9bdc8, 32px gaps (Film, The idea, Method, Results, Resources). Right: `a.header-paper` 12px #f0f3f5, padding 8px 15px, 1px #ffffff25 border, 30px radius, an 18px "↗" 18px to the right of the label.
2. **Hero** (`section.hero.hero-cinema.wrap`, from y=76): padding-top 22px.
3. **Venue label** (`a.publication`, y=107): 10px uppercase, letter-spacing 0.14em (1.4px), line-height 1, #cac9d6, centred; a 5px #78dce8 dot 11px before "ECCV 2026", a 16px "↗" after. Margin-bottom 12px.
4. **Title** (`h1`, y=135, 48px box): "GeoV2V" 44px/650, line-height 1.08, letter-spacing -0.06em (-2.64px), #f0f3f5, centred, nowrap. Gap 10px.
5. **Subtitle** (`p.hero-description`, y=192): 13px/400, line-height 1.6, letter-spacing -0.02em, #aeb3c1, max 800px, centred. `.hero-copy` margin-bottom 20px.
6. **Film player** (`.feature-player`, y=233, 1129×636 at x=156): width min(100%, 1160px, (100svh − 265px) × 16/9), 16:9 video on #0c111b, 12px radius, 1px #8f80b53d border, shadow `0 24px 90px #0005`. The poster frame shows the two-tone tagline (white + violet) and two street clips.
7. **Play pill** (`button.feature-play`, centred at y=521, 172×59): #080b15df with `backdrop-filter: blur(12px)`, 1px #ffffff3d border, 50px radius, padding 11px 24px 11px 12px, shadow `0 5px 35px #0008`, 13px/550 #f5f3ff text; a 35px #f0eafc circle holds a #171023 "▶". Hover: background #222033ed, border #e0d5ff87, text white.
8. **Film meta row** (`.feature-bottom`, y=881): padding-top 12px; 9px #8692a8 text with 0.04em tracking ("THE RESEARCH FILM · 01:29 · 1080P · EN / 中文"), right link "Compare the views ↓" 10px #b0bcd1, hover #78dce8.

The "Chapters & downloads" disclosure and the "EXPLORE THE RESULT" comparison start just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink Night | #07090f | --bg | page background (body) |
| Panel | #10131b | --panel | video letterbox, showcase control bar (`.showcase-controls`) |
| Off-white | #f0f3f5 | --ink | title, section headlines, wordmark, resource titles, header paper pill text |
| Muted | #9a9fae | --muted | `.mono` metadata lines |
| Headline Gray | #a9acb8 | (literal, `em`) | second sentence of every two-tone h2 ("A different lane.", "one moment.") |
| Body Gray | #9ea7b9 | (literal) | 15px section intro paragraphs (`.section-heading > p`) |
| Subtitle Gray | #aeb3c1 | (literal) | hero subtitle |
| Nav Gray | #b9bdc8 | (literal) | header nav links |
| Label Gray | #a0a7b8 | (literal) | uppercase section labels (`.section-label`) |
| Line | #282c37 | --line | footer top border, resource list rules, result stage border, `.hero-principles` bottom rule |
| Teal | #78dce8 | --teal | venue dot, link and button hover text, focus outline (2px, offset 5px) |
| Violet | #baa7ff | --violet | wordmark dot, legend dots, accent words in the poster tagline |
| Lavender Score | #d4c5f7 | (literal) | 86px headline metric (`.metric-large`) |
| Ours Text | #ddcefb | (literal, `tr.ours td`) | GeoV2V row in tables |
| Ours Row | #a78ac910 | (literal, `tr.ours`) | GeoV2V table row background |
| Active Tab | #282339 | (literal) | selected pill tab background; text #f3f0ff, border #8e77bd55 |
| Tab Border | #343849 | (literal) | unselected pill tab border; text #a1a7b7 |
| Gold | #e5c29c | --gold | legend dots, "Illumination" label in the formation figure (rendered #dfc496) |
| Card | #10141f | (literal) | BibTeX card (`.citation`) |
| Table Rule | #222a39 | (literal) | td bottom borders; th bottom border #586171 |
| Table Head | #8c9aae | (literal) | th text |
| Table Cell | #b5bfd0 | (literal) | td text |
| Stage Dark | #0c0e14 | (literal) | results video stage (`.result-stage`) |
| Switch Track | #080a10 | (literal) | segmented 1/2/4 m switch track |
| Switch Selected | #333040 | (rendered) | selected offset button fill; its text #e9e0ff |
| Tab Hover Border | #a5a1bf | (literal) | pill tab hover border |
| Bar Gray | #455166 | (literal) | baseline bars in the metric chart |
| Bar Ours | #9b88c8 → #c4b3f1 | (literal gradient) | ours bar; ours bar row text #d6c7f4 |
| Figure Gradient | #121823 → #101119 | (literal gradient) | formation illustration background |
| Index Gray | #68758c | (literal) | resource numbers |
| Small Gray | #8391a9 | (literal) | resource sublines, release note |
| Credit Grays | #b1b8c8 / #868fa1 / #6e788b | (rendered) | credits paper title / affiliations / author notes |
| Caption Gray | #8b96aa | (literal) | table captions |
| Plus Gray | #8c94a9 | (literal) | disclosure "+" glyph |
| Code Gray | #91a1bd | (literal) | BibTeX text |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif | no web font loaded (`fonts_loaded` empty); Segoe UI on Windows, SF Pro on macOS | Inter |
| Mono | ui-monospace, SFMono-Regular, Menlo, monospace | system mono (Consolas on Windows) | JetBrains Mono |

Weights are fractional (550, 650, 760); with system fonts they snap to the nearest available face.

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Hero title | `.hero-cinema h1` | 44px / 650 / 1.08 / -0.06em | #f0f3f5 |
| Section headline | `h2` (idea, method, results, evidence, resources) | clamp(40px, 4.8vw, 70px) → 69.12px / 650 / 1.05 / -0.055em | #f0f3f5 + `em` #a9acb8 |
| Motivation headline | `.motivation-heading h2` | clamp(40px, 3.5vw, 50px) → 50px / 650 / 1.06 | same two-tone |
| Showcase headline | `.paired-heading h2` | clamp(30px, 3.2vw, 44px) → 44px / 650 / 1.12 / -0.048em | same two-tone |
| Section label | `.section-label` | 11px / 600 / 1.4 / 0.16em uppercase (9px inside `.paired-heading`) | #a0a7b8 |
| Section intro | `.section-heading > p` | 15px / 400 / 1.8 / -0.01em, max 370px | #9ea7b9 |
| Body | `body` | 16px / 400 / 1.6 | #f0f3f5 |
| Wordmark | `.brand` | 24px / 760 + 400 / -1.3px | #f0f3f5 |
| Nav | `.site-header nav` | 13px / 400 | #b9bdc8 |
| Pill tab | `.pill-tabs button` | 12px / 400, padding 10px 16px | #a1a7b7 |
| Resource title | `.resource-list b` | 18px / 500 / -0.025em | #f0f3f5 |
| Result caption title | `.result-caption h3` | 24px / 650 / -0.025em | #f0f3f5 |
| Headline metric | `.metric-large` | 86px / 400 / 1.1 / -0.065em, tabular | #d4c5f7 |
| Table | `table` / `th` / `td` | 12px tabular, th 10px/500 | th #8c9aae, td #b5bfd0 |
| BibTeX | `.citation pre` | mono 11px / 1.9 | #91a1bd |
| Footnotes, captions | `caption`, `footer p` | 10px | #8b96aa, #79869d |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Header paper pill, buttons | 30px | 1px #ffffff25 | none |
| Play pill | 50px | 1px #ffffff3d | `0 5px 35px #0008`, `backdrop-filter: blur(12px)` |
| Film player | 12px | 1px #8f80b53d | `0 24px 90px #0005` |
| Paired video frame | 12px 12px 0 0 | 1px #ffffff18, no bottom | none; 3px gap between panels on #040407 |
| Video overlay chips | 4px | 1px #ffffff28 | background #02050988, `backdrop-filter: blur(10px)` |
| Pill tabs | 40px | 1px #343849 | none |
| Offset segmented switch | 22px track, 40px buttons | 1px #ffffff13 track | track #080a10, padding 3px |
| Formation illustration | 13px | 1px #ffffff15 | background `linear-gradient(125deg, #121823, #101119)` |
| Result stage | 12px | 1px #282c37 | background #0c0e14 |
| Chapter buttons | 6px | 1px #293345 | background #0e1420 |
| BibTeX card | 10px | 1px #ffffff10 | background #10141f, padding 30px 35px |

## Layout Metrics

- **Container**: `.wrap { width: min(1280px, calc(100% - 100px)); margin: auto }` → x 80–1360 at 1440. The header is wider: min(1440px, 100% − 80px) → x 40–1400.
- **Hero**: padding-top 22px, no bottom padding; hero copy 115px tall plus 20px gap; film player width min(100%, 1160px, (100svh − 265px) × 16/9), which is 1129px at 1440×900.
- **Section rhythm**: `.section-space` padding 96px top, 22px bottom (late override of 140px); `.paired-showcase` 76px top; `.motivation-section` 92px top; `.method` margin-top 90px and padding 75px 0 85px, full-bleed with background `linear-gradient(#11141e8f, #0a0e1660)` and 1px #ffffff09 top and bottom borders; `.results` 85px top.
- **Section heading**: flex, space-between, align flex-end, gap 60px, margin-bottom 42px (28px in results); label margin-bottom 28px.
- **Paired showcase**: two 16:10-ish panels (aspect 832/480) side by side, 3px gap; control bar 67px tall, padding 13px 18px, 24px gap; `.hero-principles` row padding 27px 0 23px with 70px gaps and a 1px #282c37 bottom rule.
- **Credits**: centred block, padding 32px 0 12px; paper title 14px #b1b8c8 max 820px; affiliations 10px #868fa1; notes 10px #6e788b.
- **Formation figure**: grid 1.35fr 1fr 1fr 1fr, gap 18px, padding 12px 25px 0.
- **Resource list**: rows padding 25px 0, gap 32px, 1px #282c37 rules; numbers 11px mono #68758c.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1600px | wrap 1280px | 16px | 44px | hero padding-top 80px rule is overridden by the cinema hero (22px) |
| 1101–1599px (base) | 50px each side (100% − 100px) | 16px | 44px | h2 69.12px, section intro 370px |
| ≤1100px | 32px (100% − 64px); header 26px | 16px | 44px | h2 55px; nav gap 23px; metric 74px; intro 330px / 14px |
| ≤760px | 18px (100% − 36px) | 16px | 37px, line-height 1.08 | header 67px, nav hidden; h2 43px; showcase h2 clamp(26px, 6vw, 37px); chapter list 2 columns; metric 48px; section-space 78px top |

## Components

- **Wordmark**: "Geo" 24px/760 + "V2V" 24px/400, letter-spacing -1.3px, #f0f3f5, then a 6×6 #baa7ff circle with margin 12px 0 0 3px.
- **Outline pill link** (`.header-paper`): 12px #f0f3f5, padding 8px 15px, 1px #ffffff25 border, radius 30px, gap 18px before an 18px "↗". Hover text #78dce8.
- **Play pill** (`.feature-play`): absolutely centred on the film, #080b15df, blur(12px), 1px #ffffff3d, radius 50px, padding 11px 24px 11px 12px, 13px/550 #f5f3ff, 35px #f0eafc icon circle with a #171023 triangle; hover #222033ed fill, #e0d5ff87 border.
- **Two-tone headline**: h2 at 650 weight with negative tracking (-0.055em); first sentence #f0f3f5, second sentence wrapped in `em` (font-style normal) #a9acb8, usually on its own line; a 370px #9ea7b9 15px/1.8 paragraph sits right, bottom-aligned.
- **Segmented viewpoint switch** (`.offset-tabs`): track #080a10, 1px #ffffff13, radius 22px, padding 3px, gap 2px; buttons 12px #a1a7b7, padding 4px 16px, radius 40px; selected #333040 fill (rendered) with #e9e0ff text.
- **Pill tabs** (`.pill-tabs button`): 12px #a1a7b7, padding 10px 16px, 1px #343849, radius 40px; selected #282339 fill, #f3f0ff text, #8e77bd55 border; hover white text, #a5a1bf border.
- **Video overlay chip** (`.video-overlay`): 10px uppercase, 0.08em tracking, padding 5px 9px, #02050988 with blur(10px), 1px #ffffff28, radius 4px, at 16px from the bottom and 18px from the left.
- **Metric bar chart**: rows with gray #455166 bars (2px radius) and 10px mono numbers; the ours row uses `linear-gradient(90deg, #9b88c8, #c4b3f1)` and #d6c7f4 text; beside it the 86px #d4c5f7 score.
- **Table**: full width, collapse, tabular numerals, right-aligned except the first column; th 10px/500 #8c9aae, padding 13px 20px, 1px #586171 bottom; td 12px #b5bfd0, padding 11px 20px, 1px #222a39 bottom; best value underlined (offset 4px); ours row #a78ac910 with #ddcefb text; 10px #8b96aa caption above.
- **Disclosure** (`details summary`): 14px, padding 20px 0, a 22px weight-200 "+" in #8c94a9 that rotates 45° when open, between 1px #282c37 rules.
- **Resource row** (`.resource-list > a`): 11px mono number #68758c, 18px/500 title, 11px #8391a9 subline, 24px weight-200 arrow on the right; hover adds 15px side padding and #bbb0e209 fill.
- **BibTeX card** (`.citation`): #10141f, 1px #ffffff10, radius 10px, padding 30px 35px; 23px heading "Cite GeoV2V" with a "Copy BibTeX ⧉" text link right; mono 11px/1.9 #91a1bd.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky / site header | yes (static, not sticky) | 76px row with wordmark, centred nav, outline pill |
| Venue badge | yes | 10px uppercase label with teal dot, not a filled badge |
| Title / tagline | yes | 44px centred title, 13px gray subtitle |
| Teaser film | yes | 1129px 16:9 player with frosted play pill and chapters disclosure |
| Synced comparison | yes | two panels with overlay chips and 1/2/4 m segmented switch |
| Authors / affiliations | present but non-standard | placed after the comparison in a centred 10–14px credits block, not under the title |
| Abstract | absent from the source | replaced by two-tone section headlines with short intro paragraphs |
| Method figure | yes | animated formation illustration and an HTML architecture flow in a lifted full-bleed band |
| Results videos | yes | pill-tab switcher over a 12px-radius stage |
| Results tables | yes | hairline tables with underlined best values and a violet ours row, plus a bar chart and large score |
| Resources | yes | numbered list with arrows |
| BibTeX | yes | dark card with copy link |
| Footer | yes | wordmark, two 10px lines, Contact link, year in #56647d |

## Adapting to Other Content

- **More authors**: keep them in the centred credits block (14px title line, names in body size, 10px affiliations with 16px gaps); do not move them into the 44px hero, which stays three lines tall (title 48px box, 10px label, 13px subtitle).
- **A results table**: use the table recipe above at full container width (1280px); best value underlined, ours row #a78ac910 with #ddcefb text; never color cells.
- **Long publication or news lists**: use the resource-row recipe (11px mono index, 18px/500 title, 11px #8391a9 date or venue line, 25px vertical padding, #282c37 rules).
- **More sections**: open each with an 11px "0N / LABEL" line and a 69.12px two-tone h2 whose second sentence is #a9acb8; keep the 370px intro paragraph right-aligned.
- **A single headline number**: reuse the 86px/400 #d4c5f7 metric with a 10px mono footnote rather than a stat strip.

## Do's and Don'ts

- Do let video carry color; the chrome stays in near-black, grays and off-white.
- Do write headlines as two short sentences and gray out the second one.
- Do reserve violet tints for the method's own output (ours row, ours bar, selected tab, wordmark dot) and teal for hover and focus.
- Do keep labels tiny (9–11px) and widely tracked; scale contrast comes from 44–86px display sizes.
- Don't load a web font; the system face with fractional weights is part of the look.
- Don't use filled colored buttons; everything is outline pills, frosted pills or text links.
- Don't add drop shadows to cards; only the film player and the play pill cast shadows.

## Surfaces

Near-black page #07090f; panels #10131b and #0c0e14 for video stages; the method band adds a translucent gradient (`linear-gradient(#11141e8f, #0a0e1660)`) and faint #ffffff09 rules; the formation illustration sits on a 125° #121823 → #101119 gradient; the BibTeX card is #10141f. A faint radial violet halo (`radial-gradient(ellipse, #a38bfb0b, transparent 70%)`, 820×420px) sits behind the hero copy.

## Imagery

Real dashcam driving footage (Waymo, CARLA renders) in synchronized pairs, a research film with chapters, an animated line-art illustration of image formation (camera, rain sheet, lamp, wireframe person and box) in thin gray strokes with teal and gold labels, an HTML architecture flow of token blocks, and white-background paper figures inset in dark frames.

## Layout

Centred compact hero over a near-full-width film, then a 1280px column of left-aligned sections: headline left, short intro right, then one wide media module per section. Generous vertical spacing (76–96px section tops) and hairline rules separate sections; only the method section breaks out to full bleed.

## Agent Prompt Guide

Quick colors: page #07090f, panel #10131b, text #f0f3f5, headline gray #a9acb8, body gray #9ea7b9, label #a0a7b8, line #282c37, violet #baa7ff, teal #78dce8, score #d4c5f7.

1. "Build a dark header and hero: page #07090f; 76px header with a 24px wordmark (bold 760 + regular 400, letter-spacing -1.3px, #f0f3f5, 6px #baa7ff dot), centred 13px #b9bdc8 nav with 32px gaps, and an outline pill (12px, padding 8px 15px, 1px #ffffff25, radius 30px). Below, centred: a 10px uppercase label with 0.14em tracking in #cac9d6 and a 5px #78dce8 dot, a 44px/650 title with -0.06em tracking, a 13px #aeb3c1 subtitle, then a 16:9 video with 12px radius, 1px #8f80b53d border and box-shadow 0 24px 90px #0005."
2. "Make a section heading: an 11px/600 uppercase label, 0.16em tracking, #a0a7b8, 28px above a 69.12px/650 h2 with letter-spacing -0.055em and line-height 1.05; the second sentence in #a9acb8. On the right, bottom-aligned, a 370px paragraph at 15px/1.8 in #9ea7b9. Container 1280px, section padding-top 96px."
3. "Create a results table: width 100%, 12px tabular numerals, right-aligned except the first column; th 10px/500 #8c9aae with 13px 20px padding and a 1px #586171 bottom border; td #b5bfd0 with 11px 20px padding and 1px #222a39 rules; underline the best value with offset 4px; give the ours row background #a78ac910 and text #ddcefb."

## Similar Pages

- Product-launch style research pages with a film-first hero and segmented comparison controls.
- Dark editorial pages that use two-tone (white + gray) headlines as section openers.

## Quick Start

```css
:root {
  --bg: #07090f;
  --panel: #10131b;
  --ink: #f0f3f5;
  --muted: #9a9fae;
  --headline-gray: #a9acb8;
  --body-gray: #9ea7b9;
  --label: #a0a7b8;
  --line: #282c37;
  --teal: #78dce8;
  --violet: #baa7ff;
  --gold: #e5c29c;
  --score: #d4c5f7;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, monospace;
  --wrap: min(1280px, calc(100% - 100px));
  --h1: 44px;
  --h2: clamp(40px, 4.8vw, 70px);
  --track-tight: -0.055em;
  --radius-pill: 30px;
  --radius-media: 12px;
}
```

## Provenance

- **URL**: https://xiyuche.github.io/GeoV2V/
- **Paper**: GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation (arXiv 2610.25245), Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang.
- **Venue**: ECCV 2026 (LNCS 17012, pp. 656–673 per the resource list).
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a custom hand-built page (`styles.css`, `app.js`); footer reads "© 2026 GeoV2V authors".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of headings, tabs, table, cards and footer, the 1440×900 shot and a full-page capture, and the page's `styles.css` and `index.html` read directly, on 2026-10-28.
