# Idan Attias — Style Reference

> A night-mode IDE where the sidebar never scrolls away.

**Theme:** both (dark by default, light on toggle)

Measurements are normalized from the static HTML and its inline `<style>` block (about 13 KB); roles are interpreted. The `<body>` ships with `class="dark-mode"`, and a script keeps dark unless the visitor saved "light", so dark is the first impression.

## Overview

A hand-built two-column page. On the left, a fixed 340px charcoal sidebar (#22252a) holds a 150px circular photo with a faint white ring, the name, a grey subtitle, Font Awesome social icons and a vertical section menu. On the right, the content column (max 1100px, padding 4rem 6rem) runs About, News, Publications, Mentoring, Teaching and Contact. Section titles are uppercase with 1.5px tracking and a 2px bottom rule. The publication area has a sticky row of pill filters (Preprints, Conferences, Journals) and 41 entries separated by dashed rules; awards appear as small red-tinted tags such as "ICML 2024 Best Paper Award • Oral Presentation". A round floating button bottom-right switches themes. The palette is Tailwind-like slate with a single blue accent (#58a6ff in dark, #2563eb in light) and a rose red for highlights.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Charcoal Rail | #22252a | `--sidebar-bg` | Sidebar, theme button, email box, dark filter pills |
| Rail White | #ffffff | `--sidebar-text` | Sidebar name and hovered icons |
| Rail Grey | #9ca3af | `--sidebar-sub` | Sidebar subtitle, icons, menu links |
| Midnight Panel | #1a1d20 | `--content-bg` (dark) | Content background in dark mode |
| Frost Text | #f1f5f9 | `--text-main` (dark) | Main text in dark mode |
| Slate Muted | #94a3b8 | `--text-muted` (dark) | Dates, venues, links row in dark |
| Slate Border | #334155 | `--border` (dark) | Rules and pill borders in dark |
| Deep Well | #111416 | `--light-bg` (dark) | Inset background in dark |
| Signal Blue | #58a6ff | `--accent` (dark) | Accent in dark: links, filter hover, type marker |
| Venue Sky | #60a5fa | none | Venue links in dark mode |
| Rose Alert | #f87171 | none | Dark-mode award tag text, news highlights, announcement |
| Rose Wash | rgba(248,113,113,0.15) | none | Dark-mode award tag background |
| Paper White | #ffffff | `--content-bg` (light) | Content background in light mode |
| Midnight Blue Ink | #2c3e50 | `--text-main` (light) | Main text in light |
| Slate 500 | #64748b | `--text-muted` (light) | Muted text in light |
| Slate 200 | #e2e8f0 | `--border` (light) | Rules in light |
| Slate 50 | #f8fafc | `--light-bg` (light) | Filter pill background in light |
| Royal Blue | #2563eb | `--accent` (light) | Accent in light |
| Inline Azure | #3686ff | none | `a.inline-link` in light |
| Title Ink | #0f172a | none | Publication title and announcement text in light |
| Crimson Tag | #b91c1c on rgba(185,28,28,0.08) | none | Award tag in light |
| Terminal Cyan | #38bdf8 | none | Monospace email box text |

## Tokens — Typography

- **Primary:** system stack `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`. No web fonts. Substitute: Inter.
- **Mono:** `"Courier New", Courier, monospace` for the email box.
- **Icons:** Font Awesome 6.4.2 from cdnjs.
- **Weights:** 500 for dates and link rows, 600 for name, titles and filters, 700 for section titles.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Name | `.sidebar h1` | 1.75rem | | 600, letter-spacing -0.5px |
| Section | h2 | 1.35rem | | 700, uppercase, letter-spacing 1.5px, 2px bottom rule |
| Pub group | `.pub-type` | 1.15rem | | 700, 4px left accent bar |
| Paper title | `.pub-title` | 1.05rem | 1.5 | 600 |
| Body | p | 1.05rem | 1.75 | |
| News | `.news-row` | 1.05rem | 1.6 | date 0.95rem in a 100px column |
| Venue | `.pub-venue` | 0.95rem | | italic, muted |
| Links | `.pub-links a` | 0.9rem | | 500, muted, accent on hover |
| Tag / filter | `.pub-award`, `.pub-filter-link` | 0.85rem | | 600; filters uppercase, 0.5px tracking |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Tag | 4px | Award tags |
| Box | 6px | Email box |
| Pill | 20px | Publication filter links |
| Circle | 50% | Profile photo, floating theme button |

- **Shadows:** `0 4px 12px rgba(0,0,0,0.15)` on the floating theme button only.
- **Layout:** `body { display: grid; grid-template-columns: 340px 1fr; }`; content `max-width: 1100px; padding: 4rem 6rem`.
- **Rhythm:** sections `margin-bottom: 4rem`; pub entries `margin-bottom: 1.15rem; padding-bottom: 1.15rem` with a dashed border.

## Components

- **Fixed sidebar.** Role: identity and section nav. 340px, full height, `padding: 4rem 2rem`, centered column; photo 150px round with `border: 3px solid rgba(255,255,255,0.1)`; menu links grey turning white on hover.
- **Section title.** Role: h2 for each section. Uppercase, 1.5px tracking, 2px `--border` bottom rule, 1.5rem space below.
- **News row.** Role: dated update. Flex row with a 100px muted date column; links in accent; bold text in rose in dark mode.
- **Sticky filter bar.** Role: jump between publication groups. `position: sticky` on the content background, 1px bottom rule; pill links 0.85rem uppercase, 1px border, 20px radius, fill with accent on hover and lift 1px.
- **Publication group header.** Role: Preprints, Conferences, Journals. 1.15rem bold with `border-left: 4px solid var(--accent); padding-left: .75rem`.
- **Publication entry.** Role: one paper. Title (600, links without underline until hover), authors, a meta row with italic venue and an award tag, then a muted links row ("Arxiv").
- **Award tag.** Role: Spotlight, Oral, Best Paper. 0.85rem 600, padding .15rem .5rem, 4px radius, crimson on a faint red wash in light; rose on a rose wash in dark.
- **Email box.** Role: contact. Charcoal block, cyan Courier text, 1rem padding, 6px radius.
- **Theme button.** Role: switch theme. Fixed bottom-right, 3.5rem round, charcoal fill, Font Awesome sun or moon icon, scale 1.05 on hover.

## Page Modules

- **Title/author block:** sidebar photo, name, subtitle and social icons.
- **Bio/photo:** About section with inline links in azure.
- **News:** dated rows with a highlighted announcement style.
- **Publication list:** 41 text entries grouped by type with a sticky filter bar; no thumbnails.
- **Venue badge:** venue is italic text; distinctions are red award tags.
- **Link buttons:** plain text links under each entry.
- **Mentoring, teaching:** dedicated sections.
- **Contact:** email box plus contact rows.
- **BibTeX, teaser media, demos:** not present.

## Do's and Don'ts

- Do keep the sidebar fixed and charcoal in both themes; only the content column changes.
- Do use uppercase tracked section titles with a 2px rule.
- Do show distinctions as small tinted tags in red, never in the accent blue.
- Don't use more than one accent blue per theme.
- Don't add thumbnails; entries are dense text with dashed separators.
- Don't drop the sticky filter bar if the list stays long.

## Surfaces

Charcoal sidebar, a content panel that is #1a1d20 in dark and white in light, slate-tinted pills, and a charcoal email box. No cards or elevation beyond the floating button.

## Imagery

One round profile photo; Font Awesome icons for social links and the theme button.

## Layout

Grid of 340px fixed sidebar plus fluid content. Under 960px the sidebar becomes a full-width static header, the menu turns into a centered wrapped row, news rows stack, and the filter bar becomes a three-column grid of small pills.

## Agent Prompt Guide

**Quick colors:** sidebar #22252a / #9ca3af; dark content #1a1d20, text #f1f5f9, muted #94a3b8, border #334155, accent #58a6ff, award #f87171; light content #ffffff, text #2c3e50, muted #64748b, border #e2e8f0, accent #2563eb, award #b91c1c.

1. "Build a fixed 340px left sidebar in #22252a: 150px round photo with a 3px rgba(255,255,255,.1) ring, 1.75rem 600 name, #9ca3af subtitle, a row of icon links, and a vertical menu whose grey links turn white on hover."
2. "Create a sticky publication filter bar: pill links 0.85rem 600 uppercase with .5px tracking, padding .4rem 1rem, 1px border, 20px radius; on hover fill with the accent and lift 1px."
3. "Make a publication entry with a dashed bottom rule: 1.05rem 600 title, author line, a meta row with an italic muted venue and a small award tag (0.85rem 600, 4px radius, #b91c1c on rgba(185,28,28,.08)), then a muted 0.9rem 'Arxiv' link."

## Similar Pages

- [David Novotny](https://d-novotny.github.io/) for another fixed-sidebar researcher page.
- [Daniel Roy](https://danroy.org/), his co-author on the ICML 2024 Best Paper, for a very different take on a theory group page.

## Quick Start

```css
:root {
  --sidebar-bg: #22252a; --sidebar-text: #ffffff; --sidebar-sub: #9ca3af;
  --content-bg: #ffffff; --text-main: #2c3e50; --text-muted: #64748b;
  --accent: #2563eb; --border: #e2e8f0; --light-bg: #f8fafc;
}
body.dark-mode {
  --content-bg: #1a1d20; --text-main: #f1f5f9; --text-muted: #94a3b8;
  --border: #334155; --light-bg: #111416; --accent: #58a6ff;
}
body { display: grid; grid-template-columns: 340px 1fr; min-height: 100vh; color: var(--text-main); background: var(--content-bg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
.sidebar { position: fixed; width: 340px; height: 100vh; padding: 4rem 2rem; background: var(--sidebar-bg); color: var(--sidebar-text); text-align: center; }
.content-container { grid-column: 2; padding: 4rem 6rem; max-width: 1100px; }
h2 { font-size: 1.35rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; border-bottom: 2px solid var(--border); padding-bottom: .5rem; }
.pub-award { color: #b91c1c; background: rgba(185,28,28,.08); font: 600 .85rem/1.5 inherit; padding: .15rem .5rem; border-radius: 4px; }
```

## Provenance

- **URL:** https://www.idanattias.com/
- **Venue/award:** ICML 2024 Best Paper (first author of "Information Complexity of Stochastic Convex Optimization"), per https://icml.cc/virtual/2024/awards_detail
- **Selection reason:** Rule B.
- **Template credit:** none; hand-written HTML and CSS with Font Awesome 6.4.2.
- **Measurement method:** all tokens read from the inline style block and HTML via `extract_style.py` and curl. Not rendered in a browser. Light-mode publication title links have no explicit color rule, so they likely fall back to the browser default blue (inferred).
