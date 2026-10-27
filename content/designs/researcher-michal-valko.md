# Michal Valko — Style Reference

> A research cockpit in a paper frame: a steel-blue title strip, a dashed sidebar of links and student faces, and a grid of colour-keyed research cards humming beside dense 9px news.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share, and pixel samples of the screenshot for the image-drawn title strip), the 1440×900 and full-page screenshots, and the site's `/luky.min.css` (its own `:root` palette) plus three inline `<style>` blocks (selected work, upcoming talks, students) read directly. No web font loads: text renders in the system UI stack (Segoe UI in this Windows render) and headings in Georgia. The root font size is `smaller` (13.33px), so the page is set small and every em value below is relative to that.

## Overview

A 1000px white sheet centred on a warm grey #e7e6e6 ground, framed by drop-shadow edge images and topped by a 30px steel-blue gradient strip carrying "Michal Valko" in small white Georgia with wide tracking. Inside, a narrow left sidebar holds the navigation as a stack of block links with a 1px dashed black right edge (the active "Intro" is a #2c5aa0 bar with white 600 text), a tiny grey "Advisory" link, a 9px email, a row of brand-coloured social icons, a portrait, three institutional logos and a vertical rail of 50px student photos with 8px first names. The main column opens with a handwritten-signature image of the name, the Chinese name in 600, a justified 13.33px intro in #444444 with teal #00778a links (each external link carries a small arrow icon), an italic keyword line and identity links. Georgia 18.67px/600 navy #1e3a5f section headings each have a 4px blue-to-navy bar at the left. News is a block of 9px lines with a grey "News:" label and a red "new" flag. The Bio is justified prose followed by three small white CV cards with emoji icons. "Selected work" is a two-column grid of six cards with 13px corners, each keyed to its own accent (blue, teal, violet) through a top bar, an uppercase label, a year pill, a tinted blob behind the illustration and a faint ghost numeral. Below come an upcoming-talks table, contact cards, current-student cards and a dense grid of past-student cards with colour-coded role badges (PhD blue, Postdoc pink, Visiting and Mentoring amber, Master green).

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #e7e6e6 38.4% (ground either side of the sheet), #ffffff 37.3% (sheet), #bbc4cb 12.7% (small dense text, icons and sidebar photos), #f2f4f5 4.5% and #e0eaec 2.4% (card washes and borders), #fdfdfd 3.5%. The title strip samples at about #7aa7d4 (an image, not a CSS color), and the teal links and #2c5aa0 active tab are each under 1%.

Anatomy in DOM order (desktop 1440px; sheet `#lt` 1000px at x=220; sidebar from x=247; main column `#content` x=368–1180):

1. **Title strip** (`header`/`#supertoplt`, y=0–30, image `covlttp.png`): pale steel-blue gradient; `h1.nadpis` "Michal Valko" at y=39 in Georgia 12.67px/500, letter-spacing 1.52px (0.12em), #ffffff with a 0 1px 2px rgba(0,0,0,0.3) text shadow. Gap about 30px.
2. **Sidebar nav** (`#menu .menulink a`, x=247, y=84–237, 94px wide, 17px rows): 13.33px, #00778a, 1px dashed #000000 right border; active "Intro" #ffffff 600 on #2c5aa0. Then "Advisory" 9px #808080, a 9px email link, and a 20px row of social icons in brand colors.
3. **Sidebar media** (y≈330 onward): portrait about 75px wide, three institution logos at 40px, then 50×50 student photos with 8px #64748b first names, stacked to the fold.
4. **Name line** (main column, y=84–120): a 164×33 handwritten-name image, the Chinese name `span.chinese-name` 16.67px/600 #444444, then the intro sentence at 13.33px #444444, justified, with teal external links. Gap about 14px.
5. **Keywords and identity links** (y≈150 and 177): italic 13.33px keyword line; `.identity-links` at 12px with "·" separators.
6. **News heading** (`h2`, y=208): Georgia 18.67px/600, line-height 1.3, #1e3a5f, padding-left 18.67px with the 4px gradient bar, plus an orange RSS icon.
7. **News lines** (`.news-feed .note`, from y≈232): 9px (xx-small); "News" label #999999, "new" flag #cc3333, text #444444; "All news" link below.
8. **Bio** (`h2` y=436, paragraph from y≈465): 13.33px #444444 justified, one bold key phrase; CV cards at y≈565; Selected work header at y=742 and the first cards at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ground | #e7e6e6 | --background-color | page background around the sheet |
| Sheet | #ffffff | --bg-white | main sheet, CV cards, talks list |
| Text | #444444 | --text-color | body, intro, bio, news text |
| Teal Link | #00778a | --primary-color | links, sidebar nav links, identity links |
| Periwinkle Hover | #8282ff | --primary-hover | link hover |
| Heading Navy | #1e3a5f | --text-dark | section headings, student names, contact titles, CV card labels |
| Work Ink | #17385f | --work-ink | "Selected work" heading and card titles |
| Active Tab | #2c5aa0 | (literal) | active sidebar item, focus outlines |
| Nav Hover | #d1e2fe | (literal) | sidebar link hover fill (border #294763) |
| Bar Blue | #3b82f6 | --blue-primary | top of the heading bar gradient, student link color |
| New Red | #cc3333 | --highlight-color | "new" flag in news |
| News Label | #999999 | (literal) | "News:" label |
| Muted Slate | #64748b | --text-light | student first names, talk dates, contact details, meta text |
| Medium Slate | #475569 | --text-medium | talk subtitles |
| Card Edge | #e2e8f0 | --border | CV, contact, student and talks borders |
| Card Wash | #f8fafc | --bg-light | end of the student and contact card gradients |
| Work Card Edge | #d9e2ea | (literal) | selected-work card border |
| Work Muted | #667b91 | --work-muted | selected-work kicker text |
| Work Text | #40546a | (literal) | selected-work card descriptions |
| Accent Blue | #367cc6 | --accent (card 1) | label, top bar and blob of the first work card (cards 4: #497fc1) |
| Accent Teal | #238f8b | --accent (card 2) | second work card accent (card 5: #2d9296) |
| Accent Violet | #755bab | --accent (card 3) | third work card accent (card 6: #8562b0) |
| PhD Badge | #bfdbfe | --blue-light | PhD badge (gradient from #dbeafe), text #1e40af |
| Postdoc Badge | #fce7f3 | --pink-light | Postdoc badge, text #9f1239 |
| Amber Badge | #fef3c7 | --yellow-light | Visiting and Mentoring badges and award highlight, text #92400e |
| Master Badge | #d1fae5 | --green-light | Master badge, text #065f46 |
| Advisory Grey | #808080 | (gray) | "Advisory" link |
| Dashed Edge | #000000 | (literal) | dashed sidebar border, nav hover text |
| Nav Hover Edge | #294763 | (literal) | sidebar link border on hover |
| Trail Grey | #61768c | (literal) | selected-work trail line |
| Pill Grey | #677b90 | (literal) | selected-work year pill text |
| Work Rule | #e4ebf1 | (literal) | underline of the selected-work header |
| Work Shadow | rgba(25,53,79,0.035) | (literal) | resting and hover shadows of selected-work cards (hover at 0.11) |

Declared but not visible on this page: the table, purple and red badge palettes, `--header-bg` black (covered by the strip image), and the press-card grid styles used on the Press page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (body, nav, cards) | system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif | no web font; system UI (Segoe UI here) | Inter |
| Serif (headings, strip, ghost numerals) | Georgia, "Times New Roman", Times, serif | Georgia (system) | Gelasio |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Strip title | `h1.nadpis` | 0.95em = 12.67px / 500 Georgia, letter-spacing 0.12em | #ffffff |
| Section heading | `h2` | 1.4em = 18.67px / 600 Georgia / 1.3 | #1e3a5f |
| Selected work heading | `.selected-work-header h2` | 18.67px / 600 Georgia, letter-spacing -0.022em | #17385f |
| Sub-heading | `h3` | 1.1em = 14.67px / 600 (system) | #1e3a5f |
| Body | `html` | smaller = 13.33px / 400 / normal, justified | #444444 |
| Sidebar nav | `#menu .menulink a` | 13.33px / 400 (active 600) | #00778a (active #ffffff) |
| News line | `.note` | xx-small = 9px / 400 | #444444; label #999999; flag #cc3333 |
| Chinese name | `.chinese-name` | 1.25em = 16.67px / 600 | #444444 |
| Identity links | `.identity-links` | 0.9em = 12px | #00778a |
| Work label | `.selected-work-label` | 0.66em / 750, uppercase, letter-spacing 0.11em | card accent |
| Work title | `.selected-work-card > strong` | 1.08em / 700 / 1.16 | #17385f |
| Work description | `.selected-work-description` | 0.79em / 400 / 1.38 | #40546a |
| Work trail | `.selected-work-trail` | 0.665em / 600 / 1.38 | #61768c |
| Student badge | `.student-badge` (compact) | 0.65em / 600 | per badge |
| Student first name | `.sidebar-student span` | 8px / 400 | #64748b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Sheet | 0 | none (edge shadow images) | image shadow at left and right |
| Section heading bar | 2px | 4px wide, 70% tall, gradient #3b82f6 → #1e3a5f | none |
| Sidebar nav link | 0 | right 1px dashed #000000 | none |
| CV card | 8px | 1px #e2e8f0 | hover 0 4px 12px rgba(0,0,0,0.08) |
| Selected work card | 13px | 1px #d9e2ea (hover accent at 0.34) | 0 2px 7px rgba(25,53,79,0.035); hover 0 13px 28px rgba(25,53,79,0.11) |
| Year pill | 999px | 1px accent at 0.19 | none |
| Talks list | 9px | 1px #e2e8f0, rows split by 1px #e2e8f0 | none |
| Contact and student cards | 12px (compact 8px) | 1px #e2e8f0 | 0 2px 8px rgba(0,0,0,0.04) |
| Student badge | 12px (compact 6px) | none | none |

## Layout Metrics

- **Sheet**: `#lt` width 80%, min-width 62em, max-width 75em (1000px at the 13.33px root), centred at x=220 on 1440; min-height 1350px; background edge images left and right.
- **Strip**: 30px tall image band across the sheet; footer closes with a matching `covltdn.png` strip.
- **Sidebar**: `#menu` float left, padding 1em 0 0 2em; nav links block-level, about 94px wide, 17px rows.
- **Main column**: `#content` padding 1em 3em 0 2em, overflow hidden; 812px wide at x=368.
- **Headings**: h2 margin 0.8em 0 0.4em, padding-left 1em; h3 margin 2em 0 1em.
- **CV cards**: flex, gap 0.8em, padding 0.5em 1em.
- **Selected work**: margin 2.05em 0 1.4em; header padding 0 0 0.72em 1.12em with a 1px #e4ebf1 underline; grid 2 columns, gap 0.72em; card padding 0.9em 0.98em 0.82em, inner grid text + visual (min 122px, 33%).
- **Talks**: rows grid minmax(112px, 0.7fr) 2.3fr, gap 0.8em, padding 0.7em 0.85em.
- **Students**: current students grid minmax(200px, 1fr), gap 0.6em; past students compact grid minmax(180px, 1fr), gap 0.4em.
- **Page height**: 2,850px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1024px | sheet 1000px centred on #e7e6e6 | 13.33px | h2 18.67px | sidebar + main column; work grid 2 columns |
| ≤1024px | sheet 95% wide; content padding 1em 1.5em | 13.33px | 18.67px | as above |
| ≤768px | full width, no frame images | 13.33px | h2 1.2em (16px) | strip centred; sidebar becomes a sticky horizontal #f8fafc bar with rounded 4px links; sidebar photos hidden, a centred row of 32px student photos and an 80px round portrait header appear; students one column |
| ≤760px | — | 13.33px | 16px | selected-work grid one column |
| ≤600px | — | 13.33px | 16px | talk rows stack date over title |
| ≤480px | content padding 0.8em | 13.33px | h2 1.1em | nav links 0.8em |

## Components

- **Dashed sidebar nav**: block links in #00778a with a 1px dashed #000000 right border; hover #000000 text on #d1e2fe with a #294763 border; active #ffffff 600 on #2c5aa0.
- **Section heading with bar**: Georgia 18.67px/600 #1e3a5f, padding-left 1em, and an absolutely positioned 4px × 70% bar with a #3b82f6 → #1e3a5f vertical gradient and 2px radius.
- **News block**: 9px lines, each "News:" in #999999, a #cc3333 "new" flag, a sentence and optional teal link with an external-link icon; line-height tightened to 0.95.
- **External and PDF links**: `a[href^="https://"]` gets a 13px right padding with an `external.png` arrow; `a[href$=".pdf"]` gets a `pdf.png` icon.
- **CV card**: #ffffff, 1px #e2e8f0, 8px radius, padding 0.5em 1em, emoji icon plus 600 #1e3a5f label; hover translateY(-2px) and 0 4px 12px rgba(0,0,0,0.08).
- **Selected work card**: 13px radius, 1px #d9e2ea, background radial accent glow at the top-right over a white-to-wash linear gradient; a 3px accent bar across the top (inset 1em each side); meta row with an uppercase accent label and a 999px year pill (#677b90 text on rgba(255,255,255,0.7)); 1.08em #17385f title, 0.79em #40546a description, a 0.665em/600 #61768c trail line above a hairline; illustration on the right over a rotated organic accent blob; ghost numeral "01"–"06" in Georgia 700 at 0.045 alpha. Hover: translateY(-4px), accent border, 0 13px 28px rgba(25,53,79,0.11).
- **Talks table**: white rounded box (9px, 1px #e2e8f0), rows with a 0.82em/600 #64748b date and a title plus #475569 subtitle and #64748b location.
- **Student card**: white-to-#f8fafc gradient, 1px #e2e8f0, 12px radius (8px compact), name 600 #1e3a5f with link and paper icons, a role badge (PhD #1e40af on #bfdbfe, Postdoc #9f1239 on #fce7f3, Visiting/Mentoring #92400e on #fef3c7, Master #065f46 on #d1fae5), years and institutions in #64748b, "→ next position"; hover lifts 2–4px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title strip | yes | image gradient with small white Georgia name |
| Sidebar nav, socials, portrait, logos | yes | dashed-edge link stack and brand icons |
| Student portrait rail | yes | 50px photos with 8px names in the sidebar |
| Intro and identity links | yes | handwritten-name image, justified intro |
| News | yes | 9px feed with red "new" flags |
| Bio and CV links | yes | justified prose and three small cards |
| Selected work | yes | six colour-keyed cards in a 2-column grid |
| Upcoming talks | yes | bordered two-column table |
| Contact | yes | three gradient cards |
| Current and past students | yes | badge-coded card grids |
| Publication list | absent from the source | lives on the Publications page |
| Footer | present but non-standard | only the closing frame image strip |

## Adapting to Other Content

- **Long publication lists**: keep them on a separate page as the site does; on the home page, surface them as selected-work cards with an accent each, never more than six.
- **More news**: the 9px feed scales, but keep it to about eight lines and link "All news".
- **More students**: the compact grid (minmax 180px) absorbs dozens; keep the badge colours fixed per role.
- **Awards**: use the amber `.student-highlight` style (#92400e on #fef3c7, 8px radius) inline after a name or title.
- **Talks**: add rows to the talks table; past talks go to the Talks page.

## Do's and Don'ts

- Do keep the page inside a 1000px framed white sheet on #e7e6e6.
- Do use Georgia only for headings, the strip title and ghost numerals; everything else is system UI at 13.33px or smaller.
- Do key each selected-work card to one accent (blue, teal or violet) used for its top bar, label, pill border and blob.
- Do keep role badges colour-coded consistently across all student grids.
- Don't let links turn anything but periwinkle #8282ff on hover.
- Don't drop the dashed sidebar edge; it is the page's signature line.

## Surfaces

Warm grey ground, a framed white sheet with image-drawn edges and a steel-blue strip, white and #f8fafc-washed cards with #e2e8f0 hairlines, and tinted gradient cards in the selected-work grid.

## Imagery

A small portrait, institutional logos (ENS, Inria, a maths lab), circular-cropped student photos, a cartoon dog-on-a-wagon mascot at the top right, product logos (Gemini, LLaMA) and pastel diagram illustrations inside the work cards.

## Layout

Strip, then sidebar beside a main column: intro, News, Bio and CV cards, Selected work, Coming up, Contact, Current Students, Past Students and Postdocs. About 2,850px tall at 1440.

## Agent Prompt Guide

Quick colors: ground #e7e6e6, sheet #ffffff, text #444444, links #00778a (hover #8282ff), headings #1e3a5f, work ink #17385f, active tab #2c5aa0, new flag #cc3333, card edge #e2e8f0, work card edge #d9e2ea, accents #367cc6 / #238f8b / #755bab.

1. "Build a framed sheet: html font-size smaller (13.33px), system-ui, #444444 on #e7e6e6; a 1000px white sheet centred; a sidebar floated left with block nav links in #00778a, a 1px dashed #000000 right border, hover #d1e2fe, active #ffffff 600 on #2c5aa0; the main column padded 1em 3em 0 2em with justified text."
2. "Make a section heading: Georgia 18.67px/600 #1e3a5f, padding-left 1em, with a ::before bar 4px wide and 70% tall, vertically centred, linear-gradient(180deg, #3b82f6, #1e3a5f), radius 2px."
3. "Create a selected-work card grid: two columns, gap 0.72em; each card radius 13px, 1px solid #d9e2ea, background a radial accent glow at 96% 4% over linear-gradient(145deg, #ffffff 62%, a pale wash), box-shadow 0 2px 7px rgba(25,53,79,0.035); a 3px accent bar at the top; an uppercase 750-weight accent label with 0.11em tracking and a 999px year pill; a #17385f title, #40546a description and #61768c trail line; illustration at right; hover translateY(-4px) with 0 13px 28px rgba(25,53,79,0.11). Accents #367cc6, #238f8b, #755bab in turn."

## Similar Pages

- Long-lived hand-built academic sites that have been modernised piece by piece (old framed layout, new card modules).
- RL and bandits researcher pages that showcase many students.

## Quick Start

```css
:root {
  --primary-color: #00778a;
  --primary-hover: #8282ff;
  --text-color: #444444;
  --background-color: #e7e6e6;
  --text-dark: #1e3a5f;
  --blue-primary: #3b82f6;
  --border: #e2e8f0;
  --bg-light: #f8fafc;
  --highlight-color: #cc3333;
}
html { font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; font-size: smaller; text-align: justify; background: var(--background-color); color: var(--text-color); }
#lt { width: 80%; min-width: 62em; max-width: 75em; margin: 0 auto; background: #ffffff; }
a { color: var(--primary-color); text-decoration: none; } a:hover { color: var(--primary-hover); }
h2 { font: 600 1.4em/1.3 Georgia, 'Times New Roman', serif; color: var(--text-dark); padding-left: 1em; position: relative; }
div#menu .menulink a { display: block; border-right: 1px dashed #000000; }
div#menu .menulink a.active { color: #ffffff; background: #2c5aa0; font-weight: 600; }
```

## Provenance

- **URL**: https://misovalko.github.io/
- **Person**: Michal Valko (reinforcement learning, bandits).
- **Venue / award**: ICML 2023 Outstanding Paper, "Adapting to game trees in zero-sum imperfect information games".
- **Selection reason**: Rule B (last author); announcement https://icml.cc/virtual/2023/awards_detail.
- **Template credit**: none; a long-maintained hand-built site (`luky.min.css`) with inline module styles.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), pixel samples of the 1440×900 screenshot for the strip image, the full-page screenshot, and `luky.min.css`, the inline `<style>` blocks and the markup read directly, on 2026-10-28.
