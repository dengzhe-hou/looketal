# Faculty Dashboard — Style Reference

> A department noticeboard turned into a tidy dashboard: one white panel ruled into hero, news strip, research column and a sidebar of stat tiles, framed by royal-blue bars.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's stylesheets (`css/main.css` from the beautiful-jekyll theme, overridden by `css/homepage-redesign.css`) and `index.html`, plus probes of rendered elements. Several sizes declared in `homepage-redesign.css` lose to the more specific `.academic-home p` / `.academic-home a` rules (15px); the tables give what renders, and the stylesheet value is noted where it differs.

## Overview

A beautiful-jekyll site restyled as a single dashboard panel, about 2,490px tall at 1440. A fixed royal-blue navbar (#3c58ad) with centred white uppercase links sits above a light gray page (#f7f7f5). All content lives in one white panel (max 1180px, 1px #d8d8d2 border, 10px radius) set in Plus Jakarta Sans. The panel is divided by 1px #d8d8d2 rules into: a hero (34px/800 name, two role lines, a 15px summary, a row of outlined button pills with one filled #1f65ab primary, and a centred 140px portrait card on the right); a full-width news strip with uppercase dates; and a two-column body. The main column holds "Research at a glance" (five themed blocks, each with a 17px/800 title, a 14px paragraph and pale-blue tag chips) and "Highlighted papers and projects" (hairline-separated rows). The 250px sidebar holds "Impact" stat tiles (2×2, beige #f3f2ed, 20px/800 numbers), an "Experience" timeline list with right-aligned years, and a pale-blue "Join the lab" call-to-action box with a filled button. A #1f65ab footer band with white circular social icons closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white panel #ffffff / #fffffe / #feffff 54.1%; page grays #f8f8f6 / #f4f5f4 / #f8f5f2 26.4% (the #f7f7f5 margins and the beige impact tiles); royal blue #445ca4 11.1% (the navbar); light gray #d1d2d4 8.4% (panel borders, rules and antialiased text).

Anatomy in DOM order (Bootstrap `.container` width min(1180px, 100% − 32px) with 15px padding; the panel runs x=145–1295):

1. **Fixed navbar** (`nav.navbar-custom`, 0–91px): #3c58ad, padding 20px 15px 20px 0, 1px #eaeaea bottom border. Centred links DIRECTOR, GROUP, RESEARCH, PUBLICATIONS, TALKS, AWARDS, FUNDING, OPENING in Open Sans 13px/800 uppercase, letter-spacing 0.6px, #ffffff, padding 15px; hover #f2be42.
2. **Panel** top edge at y=104 on the #f7f7f5 page.
3. **Hero** (`section.hero-panel`, y=105–506): grid minmax(0,1fr) 190px, gap 34px, padding 42px 32px 34px.
4. **Name** (`h1`, y=147, 38px tall): Plus Jakarta Sans 34px/800, line-height 1.12, #1e1e1e. Gap 8px.
5. **Role lines** (`.hero-role`, y=193 and 218): 15px/500, line-height 1.65, #343434, 2px apart. Gap 18px.
6. **Summary** (`.hero-summary`, y=261–410, max-width 645px): 15px/400, line-height 1.65, #333735 (the stylesheet's 16px/1.72 is overridden). Gap 22px.
7. **Action pills** (`.hero-actions`, y=431, 41px tall, 8px gaps): "Google Scholar" filled #1f65ab with #ffffff text; "Publications", "Group", "CV", "Email" white with 1px #bfc3c8 border and #064f99 text; all 15px, padding 7px 12px, 8px radius.
8. **Portrait card** (right column, centred): 140×161px photo (aspect 1/1.15), 1px #d8d8d2 border, 10px radius, at x=1097, y=147; 9px below, "Kai-Wei Chang" 13px/700 #1e1e1e, address lines 13px #5f625f, line-height 1.45; then Email · LinkedIn · Twitter / X in 12px/700 #064f99, 8px gaps.
9. **News strip** (y=506–666): 1px #d8d8d2 top rule, padding 22px 32px 24px; "NEWS" label (15px/800 uppercase, letter-spacing 0.08em, #74736e); rows grid 74px + 1fr, gap 14px, 10px between rows; date 12px/800 uppercase #6b6b66; text 14px #333735 with links 800 #0d5ea8.
10. **Content grid** from y=666: main column (898px, padding 28px 32px 30px, 1px #d8d8d2 right border) and 250px sidebar (padding 28px 24px 30px). "RESEARCH AT A GLANCE" label at y=694, first block title at y=737; "IMPACT" tiles begin at y=731.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Page Gray | #f7f7f5 | (literal, body) | page background around the panel |
| Panel White | #ffffff | --surface | panel, secondary action pills, footer icon circles |
| Royal Blue | #3c58ad | (literal, `.navbar-custom`) | fixed navbar |
| Action Blue | #1f65ab | --accent | primary pill, "View opportunities" button, footer band |
| Action Blue Hover | #174f88 | (literal) | primary hover, link hover |
| Link Navy | #064f99 | (literal) | secondary pill text, portrait-card links, callout text and label |
| News Link | #0d5ea8 | (literal) | bold links in news rows |
| Tag Blue | #1260a6 on #e7f1ff | --accent-soft | research tag chips; #e7f1ff also fills the callout box and pill hover |
| Callout Border | #82b7ed | (literal) | "Join the lab" box border |
| Pill Border | #bfc3c8 | (literal) | secondary pill border |
| Rule | #d8d8d2 | --border | panel border, section rules, column divider, list separators, portrait border |
| Tile Beige | #f3f2ed | --surface-soft | impact stat tiles |
| Ink | #1e1e1e | --text | name, block titles, stat numbers, list text |
| Body Ink | #333735 | (literal) | hero summary, news text |
| Paragraph Gray | #3f4444 | (literal) | research paragraphs, highlight descriptions |
| Muted | #5f625f | --muted | portrait address lines, experience years |
| Label Gray | #74736e | (literal) | section labels |
| Date Gray | #6b6b66 | (literal) | news dates |
| Nav Hover Gold | #f2be42 | (literal) | navbar link hover |
| Stat Caption | #373a38 | (literal) | impact tile captions |
| Pill Hover Border | #8eb8e6 | (literal) | secondary pill hover border |
| Tag Hover | #d7e9ff | (literal) | tag chip hover fill |
| Tile Hover | #eef6ff | (literal) | impact tile hover fill |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Panel text | "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif | Plus Jakarta Sans 400, 500, 700, 800 | Manrope |
| Navbar / footer copyright | 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif | Open Sans 400, 800 | Open Sans |
| Theme base (footer "Theme by") | 'Lora', 'Times New Roman', serif | Lora 400, 700 | Lora |
| Icons | FontAwesome 4.7 | FontAwesome | Font Awesome 4.7 |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.academic-home h1` | 34px / 800 / 1.12 | #1e1e1e |
| Block title | `.academic-home h3` | 17px / 800 / 1.35 | #1e1e1e |
| Section label | `.section-label` | 15px / 800 uppercase, letter-spacing 0.08em (declared 12px, overridden) | #74736e |
| Callout label | `.callout-card .section-label` | 13px / 800 uppercase, letter-spacing 0.08em | #064f99 |
| Role line | `.hero-role` | 15px / 500 / 1.65 | #343434 |
| Summary | `.hero-summary` | 15px / 400 / 1.65 (declared 16px/1.72, overridden) | #333735 |
| Action pill | `.action-pill` | 15px / 400 (declared 14px, overridden) | #064f99 or #ffffff |
| News date | `.news-item span` | 12px / 800 uppercase, letter-spacing 0.03em | #6b6b66 |
| News text | `.news-item p` | 14px / 400 / 1.55; links 800 #0d5ea8 | #333735 |
| Research paragraph | `.project-item p` | 14px / 400 / 1.55 | #3f4444 |
| Tag chip | `.project-links a` | 12px / 700 / 1.2 | #1260a6 |
| Highlight title / note | `.highlight-list strong` / `span` | 14px / 700 / 1.35 and 13px / 400 / 1.5 | #1e1e1e / #3f4444 |
| Stat number | `.impact-value` | 20px / 800 / 1.1 | #1e1e1e |
| Stat caption | `.impact-card p` | 12px / 400 / 1.35 | #373a38 |
| Experience row | `.award-list li` | 13px / 400 / 1.4; year #5f625f | #1e1e1e |
| Portrait name / lines | `.hero-card-body p` | 13px / 700 and 400, line-height 1.45 | #1e1e1e / #5f625f |
| Navbar link | `.navbar-custom .nav li a` | Open Sans 13px / 800 uppercase, letter-spacing 0.6px | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Panel | 10px | 1px #d8d8d2 | none |
| Portrait | 10px | 1px #d8d8d2 | none |
| Action pills, CTA button | 8px | pills 1px #bfc3c8 (primary 1px #1f65ab) | none |
| Impact tiles | 8px | none, #f3f2ed fill, padding 10px, min-height 80px | none; hover #eef6ff and translateY(-1px) |
| Tag chips | 4px | none, #e7f1ff fill, padding 4px 7px | none |
| Callout box | 10px | 1px #82b7ed on #e7f1ff, padding 16px | none |
| Section rules | 0 | 1px #d8d8d2 between hero, news and content; column divider on the main column's right | none |
| List rows (research, highlights, experience) | 0 | 1px #d8d8d2 bottom | none |

## Layout Metrics

- **Container**: `.container:has(.academic-home) { width: min(1180px, calc(100% - 32px)) }` with Bootstrap's 15px padding → panel 1150px at x=145–1295.
- **Hero**: grid minmax(0,1fr) 190px, gap 34px, padding 42px 32px 34px; copy max 650px.
- **News strip**: padding 22px 32px 24px; rows grid 74px + 1fr, gap 14px, row gap 10px.
- **Content grid**: minmax(0,1fr) 250px; main column padding 28px 32px 30px with 1px right border; sidebar padding 28px 24px 30px; side cards 24px apart; content sections 28px apart.
- **Research blocks**: padding 16px 0 15px (first 8px top), 1px bottom rule; tags 9px below the paragraph, 7px gaps.
- **Impact grid**: 2 columns, 8px gap, 12px below the label; tiles 97px wide at 1440.
- **Footer**: #1f65ab band, 30px top margin, padding 50px 0; 48px white circular icons, copyright Open Sans 16px.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| ≥992px | 32px inside the panel | 15px | 34px | hero two columns; main + 250px sidebar |
| ≤991px | 32px | 15px | 34px | hero and content grid collapse to one column; portrait card left-aligned; sidebar gains a top rule |
| ≤767px | 22px | 15px | 30px | panel loses side borders and radius; news dates stack above text; navbar collapses to the theme's hamburger |

## Components

- **Action pill**: inline-flex, 15px Plus Jakarta Sans, padding 7px 12px, 8px radius; secondary #ffffff with 1px #bfc3c8 border and #064f99 text, hover #e7f1ff fill with #8eb8e6 border; primary #1f65ab fill and border with #ffffff text, hover #174f88.
- **Portrait card**: centred column 190px wide; 140px photo at 1/1.15 aspect, 1px #d8d8d2, 10px radius; name 13px/700; two 13px #5f625f lines; a row of 12px/700 #064f99 text links.
- **Section label**: 15px/800 uppercase, 0.08em tracking, #74736e, 12px below; used for News, Research at a glance, Impact, Experience, Highlighted papers.
- **Research block**: 17px/800 #1e1e1e title, 5px gap, 14px/1.55 #3f4444 paragraph, then tag chips (#e7f1ff fill, #1260a6 12px/700, 4px radius, padding 4px 7px; hover #d7e9ff), separated by 1px #d8d8d2.
- **Highlight row**: block link, padding 12px 0, 1px #d8d8d2 bottom; 14px/700 title over a 13px #3f4444 note.
- **Impact tile**: #f3f2ed, 8px radius, padding 10px, min-height 80px; number 20px/800 #1e1e1e, caption 12px #373a38; hover #eef6ff and lift 1px.
- **Experience row**: flex space-between, 13px #1e1e1e role and #5f625f years, padding 8px 0, 1px #d8d8d2 bottom.
- **Call-to-action box**: #e7f1ff fill, 1px #82b7ed border, 10px radius, padding 16px; label 13px/800 uppercase #064f99; text 13px #064f99; button "View opportunities" #1f65ab fill, #ffffff 15px/800, padding 8px 12px, 8px radius, 12px top margin.
- **Navbar**: #3c58ad bar, centred Open Sans 13px/800 uppercase white links; hover gold #f2be42.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed navbar | yes | royal-blue bar, centred uppercase links |
| Name, roles, summary | yes | 34px/800 name, 15px text |
| Action buttons | yes | outlined pills plus one filled primary |
| Portrait card with contact | yes | 140px framed photo, centred lines and links |
| News | yes | ruled strip with uppercase dates |
| Research themes | yes | five blocks with tag chips |
| Highlighted papers | yes | hairline list of title + note |
| Impact stats | yes | 2×2 beige tiles |
| Experience timeline | yes | ruled list with right-aligned years |
| Join-the-lab call to action | yes | pale-blue box with filled button |
| Full publication list | present but non-standard | a separate page; the homepage shows only highlights |
| Footer | yes | #1f65ab band, white circle icons, theme credit |

## Adapting to Other Content

- **More stats**: keep the 2-column impact grid in the 250px sidebar (97px tiles); add rows of tiles rather than widening them.
- **A results table**: place it in the main column with 1px #d8d8d2 row rules, 12px/800 uppercase #74736e headers and 14px #333735 cells; mark the best value in 800 #0d5ea8.
- **Long publication lists**: reuse the highlight row (14px/700 title, 13px note, 12px padding, hairline) and add the tag-chip row for links.
- **More news**: keep the 74px date column and 10px row gap; cap the strip at about five rows and link the rest.
- **Students or group members**: use the impact-tile recipe (beige #f3f2ed, 8px radius) for each person with a 13px/700 name and a 12px caption.

## Do's and Don'ts

- Do keep everything inside one white panel with 1px #d8d8d2 rules dividing hero, news and content.
- Do use 800 weight for names, titles, labels and stat numbers, and 400 for prose.
- Do reserve filled #1f65ab for one primary action per block (Google Scholar, View opportunities).
- Do use #e7f1ff chips for project tags and the call-to-action box only.
- Don't add drop shadows; separation comes from rules and fills.
- Don't let the sidebar grow past 250px.
- Don't mix the Lora theme serif into the panel; it survives only in the footer credit.

## Surfaces

A #f7f7f5 page with a single #ffffff panel bordered 1px #d8d8d2 and rounded 10px. Inside, beige #f3f2ed stat tiles and a #e7f1ff call-to-action box are the only filled areas. Two saturated bands frame the page: the #3c58ad navbar and the #1f65ab footer.

## Imagery

One framed portrait (140×161px, 10px radius, 1px border). No paper thumbnails. Footer social icons are FontAwesome glyphs inside 48px white circles.

## Layout

A 1150px panel: full-width hero (copy + 190px portrait column), a full-width news strip, then a two-column body (fluid main column and a 250px sidebar separated by a vertical rule). It reads like a dashboard: labels, tiles and lists rather than long prose.

## Agent Prompt Guide

Quick colors: page #f7f7f5, panel #ffffff, rule #d8d8d2, ink #1e1e1e, paragraph #3f4444, label #74736e, action #1f65ab, link #064f99, tag #1260a6 on #e7f1ff, tile #f3f2ed, navbar #3c58ad.

1. "Build a dashboard panel: max 1180px, #ffffff, 1px #d8d8d2 border, 10px radius, Plus Jakarta Sans. Hero grid minmax(0,1fr) 190px, gap 34px, padding 42px 32px 34px: name 34px/800 #1e1e1e, two 15px/500 #343434 role lines, a 15px/1.65 #333735 summary, then pills (15px, padding 7px 12px, 8px radius; primary #1f65ab with #ffffff text; others #ffffff with 1px #bfc3c8 border and #064f99 text). Right: centred 140px portrait with 1px #d8d8d2 border and 10px radius."
2. "Make a research block list: section label 15px/800 uppercase, letter-spacing .08em, #74736e; each block has a 17px/800 #1e1e1e title, a 14px/1.55 #3f4444 paragraph and tag chips (#e7f1ff fill, #1260a6 12px/700, 4px radius, padding 4px 7px, 7px gaps), padding 16px 0 15px with a 1px #d8d8d2 bottom rule."
3. "Create a 250px sidebar: 'IMPACT' label, a 2-column grid of tiles (#f3f2ed, 8px radius, padding 10px, min-height 80px, number 20px/800 #1e1e1e, caption 12px #373a38, hover #eef6ff); then a call-to-action box (#e7f1ff, 1px #82b7ed border, 10px radius, padding 16px, 13px #064f99 text, button #1f65ab with #ffffff 15px/800 text and 8px radius)."

## Similar Pages

- beautiful-jekyll faculty sites restyled with a modern sans and a dashboard panel.
- Lab-director homepages that combine a stat-tile sidebar with research-theme blocks and a recruiting call to action.

## Quick Start

```css
:root {
  --page: #f7f7f5;
  --surface: #ffffff;
  --surface-soft: #f3f2ed;
  --border: #d8d8d2;
  --text: #1e1e1e;
  --muted: #5f625f;
  --label: #74736e;
  --accent: #1f65ab;
  --accent-hover: #174f88;
  --link: #064f99;
  --accent-soft: #e7f1ff;
  --nav: #3c58ad;
  --font: "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif;
}
body { background: var(--page); }
.panel { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; font-family: var(--font); color: var(--text); max-width: 1180px; margin: 0 auto 24px; overflow: hidden; }
.panel p, .panel a { font-size: 15px; line-height: 1.65; }
```

## Provenance

- **URL**: http://web.cs.ucla.edu/~kwchang/
- **Person**: Kai-Wei Chang (Professor, UCLA Computer Science); field: fairness and bias in NLP.
- **Venue / award**: ACL 2023 Outstanding Paper, last author of "The Tail Wagging the Dog: Dataset Construction Biases of Social Bias Benchmarks".
- **Selection reason**: Rule A; award listed at https://2023.aclweb.org/program/best_papers/ ; the Semantic Scholar/GitHub homepage kwchang.net redirects here.
- **Template credit**: beautiful-jekyll (footer "Theme by beautiful-jekyll"), restyled by `css/homepage-redesign.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `main.css`, `homepage-redesign.css` and `index.html` read directly, and element probes, on 2026-10-28.
