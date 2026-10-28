# Material Ledger — Style Reference

> A tidy Google-gray notebook: ink links on faint blue underlines, mint pills, and every paper stacked on one hairline.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's single stylesheet `/assets/css/site.css` (its header comment says the visual language is modelled on wenhaochai.com, with Google GM2 grays and blue) and `index.html`, plus probes of rendered elements. Light theme only.

## Overview

A white single-family page, about 3,740px tall at 1440, set entirely in self-hosted Hanken Grotesk. Text is Google gray #202124 / #3c4043 / #5f6368 and the accent is Google blue #1a73e8. Running-text links stay ink-colored on a 1px translucent blue line and sweep a 2px blue line in on hover. The hero is a two-column grid: left a 290px square photo with 8px radius, a five-icon dock (email, scholar, GitHub, X, LinkedIn) and two affiliation rows with 32px logos (Johns Hopkins, Meta FAIR); right the 46px/600 name and an 18px bio. Then "News" as a dated log with a fade-out mask and a mint "Show 5 earlier entries" pill, "Selected Publications" as text-only rows separated by #e8eaed hairlines with blue action links (TL;DR⌄, Paper, Project, Code…), and "Awards & Honors" in the same log style. Award names render as pale-blue highlight chips (#0b57d0 on #e8f0fe).

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fdffff / #fffffe / #f8fafe / #f6f6f5 together 85.4%; gray #b2b3b1 6.9% and dark gray #74736f 3.8% (the photo's lake and shore, icons and antialiased text); warm beige #dddbcc 3.9% (the photo's sky and stones). The blue accent and the link lines cover too little area to form a cluster.

Anatomy in DOM order (`.page` and `.topbar-inner` max-width 1180px with a clamp(20px, 4vw, 56px) gutter = 56px, so content runs x=186–1254):

1. **Top bar** (`header.topbar`, 0–73px, static): #ffffff, 72px inner height, 1px #e8eaed bottom border. Brand: 24px "CJ" logo image then "Chuanyang Jin" 20px/600, letter-spacing -0.01em, #202124, 10px gap. Nav right: Home, Publications, Life at 16px/600, 28px apart, padding 6px 0; current item #202124 with a 2px #1a73e8 bottom border; others #3c4043.
2. **Hero section** padding-top 72px (clamp(40px, 6vw, 72px)); grid columns 290px + 1fr, column gap 86.4px (clamp(32px, 6vw, 88px)).
3. **Photo** (left, y=145): 290×290px square, 8px radius, #f8f9fa placeholder, object-fit cover. Gap 14px.
4. **Icon dock** (y=449): 5 equal 40px-tall cells, 2px gaps, 17px icons in #5f6368; hover #202124 on #f1f3f4 with 8px radius. Gap 28px.
5. **Affiliations** (y=517): two rows 14px apart, each a 32px contain-fitted logo, 14px gap, name 15px/600 #202124 over role 13px #5f6368 (line-height 1.35).
6. **Name** (right column x=562, y=145, 51px tall): 46px/600 (clamp(34px, 4.6vw, 46px)), line-height 1.1, letter-spacing -0.015em, #202124. Gap 24px.
7. **Bio** (y=220–597, max-width 660px): three paragraphs, 18px/400, line-height 1.6, #3c4043, 16px apart. Links are #202124 with padding 0 1px and two background lines: `linear-gradient(#1a73e8, #1a73e8)` sized 0 2px and `linear-gradient(rgba(26,115,232,.35), rgba(26,115,232,.35))` sized 100% 1px, both at 0 100%. "reason about" and "learn from human interaction" open floating research cards.
8. **News** section padding-top 96px (clamp(56px, 8vw, 96px)); title "News" at y=707, 24px above the first log row (y=767).

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | --paper | page, top bar, peek cards |
| Paper 2 | #f8f9fa | --paper-2 | photo placeholder, project thumbnails, code blocks |
| Paper 3 | #f1f3f4 | --paper-3 | dock hover fill, segmented-control track |
| Ink | #202124 | --ink | name, section titles, paper titles, own name in author lists, link text, current nav item, affiliation names |
| Ink 2 | #3c4043 | --ink-2 | bio, news and award text, venue lines, other nav items |
| Ink 3 | #5f6368 | --ink-3 | dates, author lists, legend note, affiliation roles, dock icons, footer |
| Rule | #dadce0 | --rule | scrollbar thumb, mobile nav panel border |
| Hairline | #e8eaed | --rule-2 | top-bar border, publication separators, year dividers in logs, footer rule, abstract left bar |
| Google Blue | #1a73e8 | --accent | link hover color and 2px sweep line, action links (TL;DR, Paper, Code, All publications), current-nav underline, peek-card bullets |
| Blue Hover | #1967d2 | --accent-hover | action-link and nav hover |
| Link Line | rgba(26,115,232,0.35) | --link-line | resting 1px underline of running-text links |
| Mint | #d3e3fd | --mint | "Show earlier entries" pill, skip link |
| Mint Hover | #c2d7fb | --mint-2 | pill hover, text selection |
| Mint Ink | #041e49 | --mint-ink | pill text |
| Tint | #e8f0fe | --tint | award highlight chip fill |
| Tint Ink | #0b57d0 | --tint-ink | award highlight chip text |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Hanken Grotesk', 'Helvetica Neue', Arial, sans-serif | Hanken Grotesk 400–700 (self-hosted variable) | Hanken Grotesk via Google Fonts, else Manrope |
| Mono | ui-monospace, Menlo, Consolas, monospace | system mono (code only on sub-pages) | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.hero-name` | clamp(34px, 4.6vw, 46px) → 46px / 600 / 1.1, letter-spacing -0.015em | #202124 |
| Section title | `.sec-title` | clamp(25px, 2.4vw, 30px) → 30px / 600 / 1.2, letter-spacing -0.01em | #202124 |
| Paper title | `.pub-title` | 20px / 600 / 1.25, letter-spacing -0.01em | #202124 |
| Brand | `.brand` | 20px / 600 / 1.55, letter-spacing -0.01em | #202124 |
| Nav | `.nav a` | 16px / 600 / 1.55 | #3c4043 (current #202124) |
| Bio | `.hero-bio` | 18px / 400 / 1.6 | #3c4043 |
| Body | `body` | 16px / 400 / 1.55 | #202124 |
| Log row | `.log > li` | 16px / 400 / 1.6 | #3c4043 |
| Log date | `.news-date` | 14px / 500 / 25.6px, tabular numerals | #5f6368 |
| Authors | `.pub-authors` | 15px / 400 / 1.55; own name 600 #202124 | #5f6368 |
| Venue | `.pub-venue` | 15px / 500 / 1.55 | #3c4043 |
| Action link | `.pub-links a`, `.sec-more`, `.pub-tldr` | 15px / 600 | #1a73e8 |
| Legend note | `.pub-note` | 14px / 400 / 1.5 | #5f6368 |
| Affiliation | `.aff b` / `.aff span` | 15px / 600 and 13px / 400, line-height 1.35 | #202124 / #5f6368 |
| Pill | `.pill` | 15px / 600 | #041e49 |
| Award chip | `.award` | inherits size (16px in logs), 600 | #0b57d0 |
| Footer | `.foot` | 14px / 1.55 | #5f6368 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Photo, dock cells, project thumbnails, code blocks | 8px | none (thumbnails 1px #e8eaed) | none |
| Award chip | 4px, padding 1px 6px | none | none |
| Pill, skip link, segmented control | 50px | none | none |
| Peek card | 12px | 1px #e8eaed | `0 1px 2px rgba(60, 64, 67, 0.1), 0 10px 28px rgba(60, 64, 67, 0.16)` |
| Publication rows | 0 | 1px #e8eaed bottom | none |
| Log year divider | 0 | 1px #e8eaed top, 8px margin above, 18px padding | none |
| Mobile nav panel | 0 | 1px #dadce0 bottom | `0 12px 24px rgba(32, 33, 36, 0.08)` |

The collapsed news list fades its last 30px with `mask-image: linear-gradient(to bottom, #000 calc(100% - var(--log-peek)), transparent)` where `--log-peek: 30px`.

## Layout Metrics

- **Container**: `.page { max-width: 1180px; margin: 0 auto; padding: 0 clamp(20px, 4vw, 56px) }` → 1068px content at x=186–1254.
- **Hero grid**: `grid-template-columns: clamp(220px, 25vw, 290px) minmax(0, 1fr)` → 290px + 691.6px, `column-gap: clamp(32px, 6vw, 88px)` → 86.4px; bio max-width 660px.
- **Section rhythm**: `.journal { padding-top: clamp(56px, 8vw, 96px) }` → 96px between sections; hero 72px; the last section adds 80px bottom padding. Section head margin-bottom 24px, title and "All publications" link baseline-aligned with space-between.
- **Logs** (news, awards): each row padding 10px 0 10px 116px, the date absolutely positioned at left 0 in a 96px column at top 11px; no row separators except a 1px #e8eaed rule where the year changes. Collapsed list shows six rows, then the pill 16px below.
- **Publications**: text-only rows, padding 24px 0, 1px #e8eaed bottom border; title 6px above authors; venue 2px below authors; action links 10px below with gaps 6px 18px.
- **Footer**: hairline row inside the 1180px container, padding-top 24px, bottom padding 40px, 14px #5f6368, space-between.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| >1000px | 56px | 16px (bio 18px) | 46px | two-column hero; nav gap 28px |
| ≤1000px | 4vw | 16px | 4.6vw | nav gap 20px, nav links 15px |
| ≤860px | 4vw | 16px | 4.6vw, 34px floor | hero becomes avatar (88–128px) beside the name, dock across, bio below; affiliations hidden |
| ≤800px | 4vw | 16px | 34px | top bar 60px, brand 18px; nav turns into a burger drop-down panel |
| ≤600px | 20px floor | 15px log rows (bio 17px) | 34px | log date column 76px with 88px indent; paper titles 18px; project cards stack |
| ≤377px | 20px | 15px | max(26px, 9vw) | name scales with width |

## Components

- **Running-text link**: color #202124, padding 0 1px; resting `background-size: 0 2px, 100% 1px` of a #1a73e8 line over a rgba(26,115,232,.35) line at the baseline; hover turns the text #1a73e8 and sweeps the 2px line to 100% in 0.28s `cubic-bezier(0.2, 0.7, 0.3, 1)`.
- **Action link** (`.pub-links a`, `.sec-more`): 15px/600 #1a73e8, no resting underline, first letter uppercased; hover #1967d2 with a 2px currentColor line sweeping in.
- **TL;DR toggle**: first item in each link row, 15px/600 #1a73e8 with a 0.82em chevron that rotates 180° when open; opens an abstract with a 2px #e8eaed left border, 13px left padding, 16px/1.6 #3c4043, max-width 760px.
- **Award chip** (`.award`): #e8f0fe fill, #0b57d0 text 600, 4px radius, padding 1px 6px, inline inside sentences and venue lines.
- **Pill** (`.pill`): #d3e3fd fill, #041e49 15px/600 text, padding 8px 16px, 50px radius, no border; hover #c2d7fb; active scale(0.96).
- **Icon dock**: five 40px-tall cells sharing the 290px photo width, 2px gaps, 17px #5f6368 icons, 8px radius hover fill #f1f3f4.
- **Affiliation row**: 32px logo, 14px gap, two-line label (15px/600 #202124 over 13px #5f6368).
- **Peek card**: absolutely positioned under the bio link, width min(500px, 100%), #ffffff, 1px #e8eaed, 12px radius, padding 14px 18px 12px, the two-layer shadow above; 14px/600 head and 15px bullet rows with 5px #1a73e8 dots.
- **Log row**: 116px left indent with the 14px/500 #5f6368 date hung in it; 16px #3c4043 text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top bar | yes | static white bar, logo + name, three nav items with blue current underline |
| Photo + icon dock + affiliations | yes | 290px rounded photo, 5-icon dock, two logo rows |
| Bio with research cards | yes | 18px text, blue-line links, two links open floating cards |
| News | yes | dated log, collapsed with a fade mask and a mint pill |
| Selected publications | yes | text-only rows, highlight chips, TL;DR abstracts, blue action links |
| Awards & honors | yes | same log layout as news |
| Publication thumbnails | absent from the source | rows are text only |
| Life / photo gallery | present but non-standard | separate page (nav "Life"); the stylesheet defines a 4-column photo grid with a lightbox |
| Footer | yes | one hairline row, 14px muted text |

## Adapting to Other Content

- **More co-authors**: let `.pub-authors` wrap at 15px #5f6368 across the full 1068px width; keep own name 600 #202124 and the `*`/`†` markers explained in the 14px legend line.
- **A results table**: use the stylesheet's prose table (15px tabular numerals, 13px/600 header over a 1px #3c4043 rule, cells with 1px #e8eaed bottom borders, padding 10px 14px 10px 0); mark the best value with the #e8f0fe/#0b57d0 award chip.
- **Long publication lists**: keep the text-only rows and add the source's Selected / All segmented control (#f1f3f4 track, 50px radius, pressed segment #d3e3fd with an inset 1px #0b57d0 ring).
- **Long news**: keep the collapsed log (about six rows visible, 30px mask fade) and the mint pill; insert year dividers (1px #e8eaed, 18px padding-top).
- **Talks or service**: reuse the log row with the date column; for icon lists use the 40px left indent with a 20px emoji, as the source's misc list does.

## Do's and Don'ts

- Do use one family (Hanken Grotesk) and build hierarchy with 600 weight and size only.
- Do keep link text ink-colored with the translucent blue underline; reserve solid #1a73e8 text for action links.
- Do separate publication rows with 1px #e8eaed hairlines and nothing else.
- Do use the #e8f0fe/#0b57d0 chip for awards and orals, inline in the sentence.
- Don't add thumbnails or cards to publication rows.
- Don't use rules between news rows except at year changes.
- Don't introduce a second accent; mint is a tint of the same blue family.

## Surfaces

Plain #ffffff throughout, with #f8f9fa and #f1f3f4 only as placeholders and hover fills. The only elevated surface is the peek card with its soft two-layer shadow. Mint #d3e3fd fills the pill.

## Imagery

One 290px square outdoor portrait with an 8px radius, two 32px institution logos, and 17px monochrome social icons. Publications carry no images; emoji (🔍, ⭐, 📈) appear inline in venue lines.

## Layout

A 1068px column. The hero is a 290px sidebar (photo, dock, affiliations) beside a wide text column; every section after it is full width with a left-aligned 30px title and an optional right-aligned action link on the same baseline. Logs hang their dates in a 116px left indent.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #202124, ink-2 #3c4043, ink-3 #5f6368, hairline #e8eaed, accent #1a73e8, mint #d3e3fd, tint #e8f0fe on #0b57d0.

1. "Build a hero grid inside a 1180px container with 56px gutters and 72px top padding: columns 290px and 1fr, column gap 86.4px. Left: 290px square photo with 8px radius; 14px below, a 5-cell icon dock (40px tall, 17px #5f6368 icons, hover #f1f3f4); 28px below, affiliation rows (32px logo, 15px/600 #202124 name over 13px #5f6368 role). Right: Hanken Grotesk 46px/600 name, letter-spacing -0.015em, 24px above an 18px/1.6 #3c4043 bio."
2. "Style running-text links as #202124 with background-image linear-gradient(#1a73e8, #1a73e8), linear-gradient(rgba(26,115,232,.35), rgba(26,115,232,.35)) at 0 100%, sizes 0 2px and 100% 1px; on hover text #1a73e8 and the first size goes to 100% 2px over 0.28s."
3. "Create a publication row: padding 24px 0, 1px #e8eaed bottom border; title 20px/600 #202124; authors 15px #5f6368 with own name 600 #202124; venue 15px/500 #3c4043 with an inline award chip (#e8f0fe fill, #0b57d0 600 text, 4px radius, padding 1px 6px); a link row 10px below of 15px/600 #1a73e8 links with 18px gaps, starting with a 'TL;DR⌄' toggle."

## Similar Pages

- wenhaochai.com, which the stylesheet names as its model.
- Google Material–flavoured academic homepages with GM2 grays, a single blue accent and text-only publication lists.

## Quick Start

```css
:root {
  --paper: #ffffff;
  --paper-2: #f8f9fa;
  --paper-3: #f1f3f4;
  --ink: #202124;
  --ink-2: #3c4043;
  --ink-3: #5f6368;
  --rule-2: #e8eaed;
  --accent: #1a73e8;
  --accent-hover: #1967d2;
  --link-line: rgba(26, 115, 232, 0.35);
  --mint: #d3e3fd;
  --mint-ink: #041e49;
  --tint: #e8f0fe;
  --tint-ink: #0b57d0;
  --font-sans: "Hanken Grotesk", "Helvetica Neue", Arial, sans-serif;
  --max: 1180px;
  --gutter: clamp(20px, 4vw, 56px);
}
body { margin: 0; background: var(--paper); color: var(--ink); font: 16px/1.55 var(--font-sans); }
```

## Provenance

- **URL**: https://chuanyangjin.com/
- **Person**: Chuanyang Jin (PhD student, Johns Hopkins University); field: machine theory of mind, multimodal reasoning.
- **Venue / award**: ACL 2024 Outstanding Paper, first author of "MMToM-QA: Multimodal Theory of Mind Question Answering".
- **Selection reason**: Rule A; award listed at https://2024.aclweb.org/program/best_papers/ ; homepage from Semantic Scholar and GitHub chuanyangjin.
- **Template credit**: hand-written stylesheet; its header states the visual language is modelled on wenhaochai.com. Hanken Grotesk is self-hosted under the SIL Open Font License.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `site.css` and `index.html` read directly, and element probes, on 2026-10-28.
