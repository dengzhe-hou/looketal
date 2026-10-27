# Warm Paper Garamond Folio — Style Reference

> A quiet researcher's folio on warm paper: Garamond headings, teal small labels and hairline-ruled entries.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the sticky header, brand, nav, portrait, hero name, lead, buttons, section kickers and headings, theme and work entries, featured essay and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the site's own `assets/css/site.css` (about 11.5 KB) with its HTML. Positions are document coordinates at 1440px wide.

## Overview

Junyang Lin's homepage is a hand-written Jekyll-style site on a warm off-white ground (#f7f5f0) with near-black text, a muted grey for prose and one deep teal accent (#1d5c63). A translucent sticky header holds a 40px Cormorant Garamond wordmark and five tracked uppercase links. The hero pairs a 192×240 rounded portrait with a bold 59.52px Source Sans 3 name (the only heavy sans display on the page), a grey "Independent researcher" line, a lead sentence, a summary and three 44px pill buttons (teal "Read research", outlined "Browse writing" and "Contact"). Sections follow with a 64px rhythm: a small teal uppercase kicker, a 40px Garamond heading, then content. "About" is a 672px statement; "Research" is three numbered themes ("01", "02", "03") under hairline rules with 30.4px Garamond questions; "Selected work" is a two-column grid of ruled entries with a meta line, a Garamond title, grey text and small outlined pill links; "Writing" features one essay; "Contact" closes with pill links. No shadows, no fills beyond the teal button.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): warm paper #f7f5f0 79.4%, light warm grey #e8e6e2 7.4% (rules and the portrait's sky), mid grey #8a8c8a 4.4% (text anti-aliasing), #f9f7f2 3.8%, #f7f5ef 2.8%, remainder under 2%. Teal #1d5c63 appears only in the primary button and the "ABOUT" kicker; the portrait is the one photographic patch.

Anatomy in DOM order (y = top of element box):

1. **Sticky header** (`header.site-header`), y 0, 1440×77 including a 1px #e7e2d8 bottom border, background rgba(247,245,240,0.92) with 10px blur; inner row `min(100% - 2rem, 68rem)` (x 176–1264), min-height 76px, space-between.
2. **Wordmark** (`a.site-brand`), x 176, "Junyang Lin", Cormorant Garamond 40px/600, letter-spacing 0.02em, #171717.
3. **Nav** (`nav.site-nav--desktop`), right, five links "ABOUT … CONTACT", Source Sans 3 13.44px/700 uppercase, letter-spacing 0.12em, #5f5f5f, gap 19.2px; hover #1d5c63. Main top padding 40px.
4. **Portrait** (`.portrait-frame img`), x 144, y 158, 192×240 (4:5), radius 8px, backing #eae5db, vertically centered with the text column; gap 32px to the text.
5. **Name** (`h1.hero__name`), x 368, y 117, "Junyang Lin", Source Sans 3 59.52px/700, line-height 101.2px (inherits 1.7), #171717, left. Gap 6px.
6. **Eyebrow** (`p.hero__eyebrow`), y 224, "Independent researcher", 16px/600 #5f5f5f. Gap 14px.
7. **Lead** (`p.hero__lead`), y 265, 17.6px/400 #5f5f5f, max-width 672px. Gap 18px.
8. **Summary** (`p.hero__summary`), y 313, two lines, 16.32px #5f5f5f. Gap 20px.
9. **Buttons** (`.hero__actions`), y 388, three pills 50px tall, gap 12.8px: "Read research" (#1d5c63 fill and border, #ffffff text), "Browse writing" and "Contact" (transparent, 1px #d8d1c3 border, #171717 text); Source Sans 3 15.2px/700, padding 11.2px 16px.
10. **Hero rule**: the hero ends with 8px padding and a 1px #e7e2d8 bottom border (about y 456) spanning x 144–1296. Gap 64px.
11. **About section** (`section.content-section`), y 512: teal kicker "ABOUT" 12.8px/700, 0.14em, #1d5c63; 12px below, "About" in Cormorant Garamond 40px/600; then a 19.2px #171717 lede and 16px #5f5f5f paragraphs at 672px.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #f7f5f0 | `--bg` | Page background, header glass base |
| Surface | #ffffff | `--surface` | Mobile menu button and panel (not visible on desktop) |
| Text | #171717 | `--text` | Wordmark, name, headings, statement lede, secondary button text |
| Muted | #5f5f5f | `--muted` | Nav links, eyebrow, lead and summary, paragraphs, meta lines, footer |
| Line | #e7e2d8 | `--line` | Header bottom border, hero rule, footer top border, work-link pill borders |
| Line Strong | #d8d1c3 | `--line-strong` | Secondary button borders, theme and work entry top rules, featured essay rule |
| Teal | #1d5c63 | `--accent` | Primary button, section kickers, theme numbers, text links ("Full publication list", "All essays", "Read the essay"), hover color for nav and pills |
| Teal Hover | #174c51 | `.button--primary:hover` | Primary button hover fill |
| Teal Soft | #eef5f5 | `--accent-soft` | Tag pills (`.tag-list span`) |
| Portrait Backing | #eae5db | `.portrait-frame` | Background behind the portrait |

## Tokens — Typography

- **Display serif**: declared `"Cormorant Garamond", Georgia, serif` for the wordmark, section headings, theme and work titles, featured essay title. Rendered: Cormorant Garamond 600 only (`fonts_loaded`). Substitute: EB Garamond 600 (a little wider; reduce size by about 5%).
- **Sans**: declared `"Source Sans 3", -apple-system, BlinkMacSystemFont, sans-serif` for everything else, including the hero name (the `.hero__name` class is not in the serif list). Rendered: Source Sans 3 400, 600, 700. Substitute: Source Sans Pro.
- **Body letter-spacing**: 0.01em on everything; nav and kickers tracked wider.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Hero name | `.hero__name` | 59.52px (`clamp(2.8rem, 2.1rem + 1.8vw, 4.1rem)`) / 1.7 | 700 sans | #171717 |
| Wordmark | `.site-brand` | 40px / 1.7, 0.02em | 600 serif | #171717 |
| Section heading | `.section-heading h2` | 40px / 1.05 | 600 serif | #171717 |
| Featured essay title | `.featured-writing h3` | 38.4px / 1.05 | 600 serif | #171717 |
| Theme and work title | `.theme-card h3`, `.work-card h3` | 30.4px / 1.05 | 600 serif | #171717 |
| Statement lede | `.statement__lede` | 19.2px / 1.7 | 400 | #171717 |
| Hero lead | `.hero__lead` | 17.6px / 1.7 | 400 | #5f5f5f |
| Hero summary | `.hero__summary` | 16.32px | 400 | #5f5f5f |
| Body | `body`, `.statement p`, `.theme-card p` | 16px / 27.2px (1.7), 0.01em | 400 | #5f5f5f |
| Eyebrow, text links | `.hero__eyebrow`, `.text-link` | 16px | 600 / 700 | #5f5f5f / #1d5c63 |
| Button | `.button` | 15.2px | 700 | #ffffff / #171717 |
| Work meta | `.work-card__meta` | 14.4px | 600 | #5f5f5f |
| Theme number | `.theme-card__index` | 13.6px, 0.14em | 700 | #1d5c63 |
| Nav link | `.site-nav a` | 13.44px uppercase, 0.12em | 700 | #5f5f5f |
| Section kicker | `.section-kicker` | 12.8px uppercase, 0.14em | 700 | #1d5c63 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero buttons | 999px | 1px #1d5c63 (primary) or #d8d1c3 | none |
| Work and contact link pills | 999px | 1px #e7e2d8; hover #1d5c63 | none |
| Portrait | 8px | none | none |
| Theme, work, featured entries | 0 | 1px #d8d1c3 top rule only | none |
| Header, hero, footer | 0 | 1px #e7e2d8 bottom or top | none |
| Mobile menu panel | 0 | 1px #e7e2d8 | 0 12px 28px rgba(20,20,20,0.08) |

The desktop page has no shadows and no filled cards.

## Layout Metrics

- **Container**: home `.page-shell` is `min(100% - 2rem, 72rem)`, 1152px at 1440 (x 144–1296); header and footer use 68rem (1088px, x 176–1264), so the wordmark sits 32px inside the content edge.
- **Main**: padding 40px 0 64px.
- **Hero**: grid `12rem minmax(0, 1fr)`, gap 32px, centered vertically; text column max 640px; copy max 672px; buttons 20px above, gap 12.8px; 8px bottom padding then a rule.
- **Sections**: 64px top margin each; kicker 12px above the heading; heading block 28px below; statement 672px wide.
- **Research**: three equal columns, gap 24px; each entry has 16px top padding under a 1px #d8d1c3 rule; title 11.2px above text.
- **Selected work**: two equal columns, gap 17.6px 24px; entries 21.6px top padding under a rule; links 13.6px above, gap 8.8px; heading row split with "Full publication list" right-aligned.
- **Featured essay**: max-width 768px. **Footer**: 80px top margin, padding 22.4px 0 41.6px, 15.2px text.
- Rendered height about 3,240px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >980px | 144px at 1440 (container 1152px) | 16px | 59.52px name, 40px headings | portrait column 192px; themes 3-up; work 2-up |
| 761–980px | 16px each side | 16px | about 51–56px (fluid) | portrait column 160px; themes and work go one column |
| 561–760px | 10px each side | 16px | 44.8px minimum | desktop nav replaced by a round menu button with a white drop-down panel; hero stacks, portrait max 144px; split headings and footer stack |
| ≤560px | 10px | 16px | 44.8px | main top padding 24px; buttons and pill links become full-width grid items |

## Components

- **Teal pill button**: inline-flex, min-height 44px, padding 11.2px 16px, 999px radius, Source Sans 3 15.2px/700; primary #1d5c63 fill and border with #ffffff text, hover #174c51; secondary and ghost transparent with 1px #d8d1c3 border and #171717 text, hover border and text #1d5c63.
- **Section kicker + heading**: uppercase 12.8px/700 teal label with 0.14em tracking, then a 40px Cormorant Garamond 600 heading at line-height 1.05; split variant puts a 16px/700 teal text link at the right.
- **Numbered theme entry**: 1px #d8d1c3 top rule, 16px padding, teal "01" at 13.6px/700 with 0.14em tracking, a 30.4px Garamond question, 16px #5f5f5f paragraph.
- **Work entry**: 1px #d8d1c3 top rule, 21.6px top padding; meta "2025 · Technical Report" 14.4px/600 #5f5f5f; 30.4px Garamond title; grey description; small pill links (1px #e7e2d8, padding 8.8px 12.8px, min-height 40px, no fill).
- **Featured essay**: max 768px, ruled top, meta "Latest essay · March 26, 2026", 38.4px Garamond title, grey summary, teal "Read the essay" link.
- **Sticky header**: rgba(247,245,240,0.92) with 10px blur, Garamond wordmark left, tracked uppercase grey links right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header | yes | Garamond wordmark, uppercase nav |
| Portrait and name | yes | rounded 4:5 photo, bold sans name |
| Hero actions | yes | three pills, one teal |
| About statement | yes | 672px lede and paragraphs |
| Research themes | yes | three numbered ruled columns |
| Selected work | yes | two-column ruled entries with pill links |
| Writing | yes | one featured essay and an "All essays" link |
| Contact | yes | short text and pill links |
| News | absent from the source | none on the home page |
| Stats, awards | absent from the source | none |
| Footer | yes | one ruled line, copyright left, note right |

## Adapting to Other Content

- **News**: a ruled list in the 672px statement width, each item with a 14.4px/600 #5f5f5f date meta line and a 16px #5f5f5f sentence; teal links.
- **Long publication lists**: extend the two-column work grid or switch to one column per year with a Garamond 30.4px year heading; keep meta line, title, description, pill links.
- **Awards**: use the numbered theme entry with the award name as the Garamond title and the year as the teal index.
- **A project page**: Garamond 40px title, teal uppercase venue kicker, grey lead at 17.6px, three pills; figures full width with the 8px portrait radius.
- **Tags**: the declared `.tag-list` pills (#eef5f5 fill, #1d5c63 text, 14.08px/600, 999px radius).

## Do's and Don'ts

- Do keep one accent, #1d5c63, for kickers, numbers, links and the primary button.
- Do separate entries with 1px #d8d1c3 rules and generous top padding instead of cards.
- Do set headings in Cormorant Garamond 600 and keep body text grey #5f5f5f.
- Do keep line lengths near 672px for prose.
- Don't add shadows or filled cards on desktop.
- Don't use more than one filled button per row.
- Don't switch the background to pure white; the warm #f7f5f0 is the identity.

## Surfaces

One surface: warm paper #f7f5f0. Hairlines in #e7e2d8 and #d8d1c3 do all the structuring. White appears only in the mobile menu; the portrait has a #eae5db backing.

## Imagery

A single casual portrait photo in a 4:5 frame with 8px corners. No figures, logos or icons on the home page.

## Layout

A 1152px shell: a two-column hero (portrait and text), then left-aligned sections with kicker and heading, a 672px statement, a three-column theme row, a two-column work grid, a 768px featured essay and a short contact block. Rendered height about 3,240px.

## Agent Prompt Guide

Quick colors: paper #f7f5f0, text #171717, muted #5f5f5f, line #e7e2d8, strong line #d8d1c3, teal #1d5c63 (hover #174c51), teal soft #eef5f5.

1. "Build a hero on #f7f5f0: a 192×240 portrait with 8px radius on the left, 32px gap, then a Source Sans 3 59.52px/700 #171717 name, a 16px/600 #5f5f5f 'Independent researcher' line, a 17.6px #5f5f5f lead, a 16.32px #5f5f5f summary, and three 44px pills 12.8px apart: #1d5c63 with white 15.2px/700 text, then two transparent ones with 1px #d8d1c3 borders and #171717 text; close with a 1px #e7e2d8 rule."
2. "Create a section: a 12.8px/700 uppercase #1d5c63 kicker with 0.14em tracking, 12px below a Cormorant Garamond 40px/600 #171717 heading at line-height 1.05, then three equal columns 24px apart, each with a 1px #d8d1c3 top rule, 16px padding, a teal '01' index, a 30.4px Garamond question and a 16px #5f5f5f paragraph."
3. "Add a selected-work grid: two columns, each entry under a 1px #d8d1c3 rule with 21.6px top padding, a 14.4px/600 #5f5f5f meta line, a 30.4px Garamond title, a 16px #5f5f5f description and pill links with a 1px #e7e2d8 border, 999px radius, no fill, hover #1d5c63."

## Similar Pages

- Minimal editorial academic homepages with a serif display face on warm paper and one muted accent.
- Personal sites styled like a writer's portfolio (essays plus selected work).

## Quick Start

```css
:root {
  --bg: #f7f5f0;
  --surface: #ffffff;
  --text: #171717;
  --muted: #5f5f5f;
  --line: #e7e2d8;
  --line-strong: #d8d1c3;
  --accent: #1d5c63;
  --accent-soft: #eef5f5;
  --max-width: 68rem;
  --copy-width: 42rem;
  --header-height: 4.75rem;
  --font-serif: "Cormorant Garamond", Georgia, serif;
  --font-sans: "Source Sans 3", -apple-system, BlinkMacSystemFont, sans-serif;
}
body { background: var(--bg); color: var(--text); font: 16px/1.7 var(--font-sans); letter-spacing: 0.01em; }
```

## Provenance

- **URL**: https://justinlin610.github.io/
- **Person**: Junyang Lin (independent researcher, per the page).
- **Venue / award**: NeurIPS 2025 Best Paper, as last author of "Gated Attention for Large Language Models" (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/).
- **Selection reason**: rule B, existing entry kept unchanged; chosen for editorial serif on a warm off-white ground with uppercase eyebrows, numbered research themes and a two-column selected-work grid with excellent hierarchy and measure.
- **Template credit**: none stated; custom stylesheet.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture, `assets/css/site.css` and `index.html`. Date 2026-10-28.
