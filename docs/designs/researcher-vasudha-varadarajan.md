# Night Sky Emerald — Style Reference

> A dusk photograph over a dark hillside, then a gallery wall of figure cards labelled in small mint capitals.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, `index.html` (a Hugo Blox Builder site with Tailwind utility classes and the emerald theme, `css/themes/emerald.min.css` plus `dist/wc.min.css`), and probes of rendered elements. Tailwind classes were resolved by probing the rendered elements rather than by reading the class names. The site defaults to dark (`data-wc-theme-default=dark`) and has a sun button for a light theme; this file describes the dark default.

## Overview

A long Hugo Blox homepage, about 11,850px tall at 1440, on near-black #17181c in Inter. A #27272a header bar carries the name at the far left, centred white 16px/600 nav links and search and theme icons at the right. The hero is a full-bleed photograph of a violet-blue night sky with a pink cloud over a black hill (the image is set with `background-size: cover; background-position: 50%` on a black fill). Over it, a centred two-column biography: left a 150px round avatar with an emoji badge, the first name in 30px/700, the role and affiliation, and a row of 24px social icons; right a slate-gray (#cbd5e1) bio with white underlined links, an outlined "Download CV" button and two lists (Interests, Education). Below, centred 30px/700 section titles introduce: a short "📚 My Research" statement in 20px prose; "Featured Publications" as a two-column grid of 16:9 figure cards with mint uppercase topic tags, white 18px/600 titles and gray dates; "Recent Publications" as a citation list with emerald CITE / URL links; "Recent & Upcoming Talks" as full-width 16:9 cards; "Teaching and Mentoring" and "Media" sections; and a small centred footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): the photograph dominates. Near-black #05060a / #020622 / #090a1a 33.7% (hill silhouette and the darkest sky); deep navy #13173f / #00002a 29.3%; violet #382a41 / #292047 25.9%; dusty mauve #7b5f7c 11.0% (the pink cloud band). The #27272a header is a small share of the top 72px; the emerald accent does not appear above the fold.

Anatomy in DOM order:

1. **Header** (`header.header`, 0–72px): #27272a, padding 12px 0, shadow `0 1px 3px 0 rgba(0,0,0,.1), 0 1px 2px -1px rgba(0,0,0,.1)`. Brand "Vasudha Varadarajan" at x=12, 20px/600 #ffffff. Nav links Bio, Publications, Awards, Experience, Talks, Media, Teaching and Mentoring: 16px/600 #ffffff, padding 12px 8px, about 32px apart, centred between x=357 and x=1201. Search (magnifier) and sun icons at x=1340 and x=1392.
2. **Hero section** (`section.blox-resume-biography-3`, 72–998px, padding 96px 0): background layer `.home-section-bg` with `background-color: #000; background-image: url(…pexels-qhung999-27200282…webp); background-size: cover; background-position: 50%; filter: brightness(1)`. Content row is flex, centred, gap 48px.
3. **Avatar** (x=296, y=238): 158px circle (150px image plus 4px #1f2937 padding ring), with a 40px black emoji badge 🧚🏽‍♀️ at its lower right (x=406, y=348) carrying shadow `0 10px 20px rgba(0,0,0,.04), 0 2px 6px rgba(0,0,0,.04), 0 0 1px rgba(255,255,255,.96)`.
4. **Name** (y=412, centred in the 256px left column): "Vasudha" 30px/700 #ffffff, 24px top margin, 8px below. Role "Postdoctoral Research Associate" 16px/600 #ffffff (y=456); "CMU LTI" 16px #ffffff (y=484).
5. **Social icons** (y=524): six 24px outline icons (email, X, GitHub, LinkedIn, Google Scholar, ORCID) in #f4f4f5, about 10px apart.
6. **Bio** (right column x=557, y=244, 650px wide): 16px/400, line-height 28px, #cbd5e1, 20px paragraph margins; links 500 #ffffff underlined. Second paragraph at y=544.
7. **Download CV** (y=620): inline-flex, #1f2937 fill, 1px #4b5563 border, 8px radius, padding 8px 16px, 14px/500 #9ca3af with a download icon.
8. **Interests / Education** (y=683): two-column grid, gap 16px; headings 20px/700 #d1d5db, 12px below; Interests is a disc list, Education rows have a 20px mortarboard icon, 16px #d1d5db degree and 14px school line. Hero ends at y=998.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Page Night | #17181c | (body, `dark:bg-hb-dark`) | page background below the hero |
| Header Zinc | #27272a | (header) | top bar |
| Black | #000000 | (hero bg fill) | hero fallback under the photo, emoji badge fill |
| Card Slate | #1f2937 | gray-800 | figure-card image wells, Download CV fill, avatar ring |
| Border Gray | #4b5563 | gray-600 | Download CV border |
| White | #ffffff | — | name, nav, brand, section titles, card titles, citation text, bio links |
| Bio Slate | #cbd5e1 | slate-300 | hero bio and "My Research" prose |
| Light Gray | #d1d5db | gray-300 | Interests and Education headings and lists |
| Muted Gray | #9ca3af | gray-400 | card dates and summaries, Download CV label |
| Icon White | #f4f4f5 | zinc-100 | social icons |
| Footer Gray | #e2e8f0 | slate-200 | footer lines |
| Mint | #6ee7b7 | primary-300 (emerald) | uppercase topic tags on cards |
| Emerald | #34d399 | primary-400 | CITE / URL links in the citation list |
| Title Highlight | linear-gradient(to right, #065f46, #064e3b) | primary-800 → primary-900 | hover underline band behind card titles |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | "Inter var", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", … | inter var 100–900 | Inter |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Section title | `.text-3xl.font-bold` | 30px / 700 / 36px, centred | #ffffff |
| Hero name | `.portrait-title .text-3xl` | 30px / 700 / 36px | #ffffff |
| Brand | `.navbar-brand` | 20px / 600 | #ffffff |
| Nav link | `.nav-link` | 16px / 600 / 24px | #ffffff |
| Hero role | `.portrait-title h3` | 16px / 600 | #ffffff |
| Hero bio | `.resume-biography p` | 16px / 400 / 28px; links 500 underline #ffffff | #cbd5e1 |
| Subheading | `.section-subheading` | 20px / 700 / 30px | #d1d5db |
| Research prose | `.blox-markdown .prose` (`lg:prose-xl`) | 20px / 400 / 36px | #cbd5e1 |
| Card tag | `.group span.uppercase` | 12px / 500 uppercase, letter-spacing 0.05em (0.6px) | #6ee7b7 |
| Card title | `.group h2` | 18px / 600 / 1.375, letter-spacing -0.025em | #ffffff |
| Card summary / date | `.line-clamp-3`, `time` | 14px / 400 / 21px | #9ca3af |
| Citation | `.pub-list-item` | 16px / 400 / 24px; title underlined, venue italic | #ffffff |
| Citation link | `.hb-attachment-link` | 16px / 700 uppercase | #34d399 |
| Button | Download CV | 14px / 500 | #9ca3af |
| Footer | `footer p` | 14px / 24px, centred | #e2e8f0 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Avatar | 9999px, 4px padding ring | none | none |
| Emoji badge | 100%, 40px | none | `0 10px 20px rgba(0,0,0,.04), 0 2px 6px rgba(0,0,0,.04), 0 0 1px rgba(255,255,255,.96)` |
| Figure card image well | 6px (`rounded-md`), overflow hidden | none | none; hover scale(1.05) |
| Download CV | 8px | 1px #4b5563 | none |
| Header | 0 | none | `0 1px 3px 0 rgba(0,0,0,.1), 0 1px 2px -1px rgba(0,0,0,.1)` |

## Layout Metrics

- **Sections**: every home section uses inline `padding: 6rem 0` (96px top and bottom) except Teaching and Mentoring (`padding: 0`); titles are centred in a `max-w-prose` column with 24px bottom margin.
- **Hero**: flex row, `justify-center gap-12` (48px); left column 256px (x=243–499), right column 650px (x=557–1207).
- **Card grids**: `.container px-8 xl:px-5 py-5 lg:py-8 max-w-screen-lg` → max 1024px with 20px side padding at 1440 (content x=228–1212) and 32px vertical padding; Featured Publications `md:grid-cols-2` with 40px gap (cards 472px wide, image 472×266px at 16:9); Talks `md:grid-cols-1` (984×554px images).
- **Card body**: tag 20px below the image; title 8px below; summary 8px below (clamped to 3 lines); date 12px below.
- **Citation list**: `max-w-3xl` column (768px, x=336–1104), 64px/80px top margin (`mt-16 sm:mt-20`), items 16px apart.
- **Footer**: 1280px container, 96px top margin, 14px centred lines.

| Breakpoint | Gutter | Body size | Section title | Grid change |
|---|---|---|---|---|
| ≥1280px (xl) | 20px card container padding | 16px | 30px | two-column featured cards, research prose 20px (`lg:prose-xl`) |
| 1024–1279px (lg) | 32px | 16px | 30px | same grids; card container py 32px |
| 768–1023px (md) | 32px | 16px | 30px | hero row stays side by side; featured cards 2 columns; research prose drops to the base prose size (16px) below lg |
| <768px | 32px | 16px | 30px | hero stacks (avatar column above bio); cards one column; nav collapses to a menu button |

## Components

- **Figure card** (`.group`): image well #1f2937, 6px radius, overflow hidden, 16:9 (`aspect-video`), image object-fill; hover scales the well 1.05. Below: mint 12px/500 uppercase tag line (#6ee7b7, 0.05em tracking), 18px/600 #ffffff title whose inline span grows a `linear-gradient(to right, #065f46, #064e3b)` band from `0px 10px` to `100% 10px` on card hover over 500ms, a 14px #9ca3af summary clamped to three lines, and a 14px #9ca3af date.
- **Citation item** (`.pub-list-item`): 16px #ffffff authors, year in parentheses, underlined title link, italic venue; a row of uppercase 16px/700 #34d399 links (CITE, URL) with 1em outline icons.
- **Outlined button** (Download CV): #1f2937 fill, 1px #4b5563 border, 8px radius, padding 8px 16px, 14px/500 #9ca3af, leading download icon.
- **Avatar with badge**: 150px circular photo in a 4px #1f2937 ring; 40px black circle with an emoji pinned to the lower right.
- **Nav link**: 16px/600 #ffffff, padding 12px 8px on the #27272a bar.
- **Section title**: 30px/700 #ffffff centred, optionally with a leading emoji (📚).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header with search and theme toggle | yes | #27272a bar, centred white links |
| Photo hero with biography | yes | full-bleed night-sky photo, avatar column + bio column |
| Interests / education | yes | two small lists inside the hero |
| Research statement | yes | centred 20px prose |
| Featured publications | yes | 2-column 16:9 figure cards with mint tags |
| Recent publications | yes | citation list with emerald CITE / URL links |
| Talks | yes | full-width 16:9 cards |
| Teaching and mentoring | yes | section with zero padding |
| Media | yes | cards with topic tags |
| News | absent from the source | none |
| Footer | yes | centred license and "Published with Hugo Blox Builder" lines |

## Adapting to Other Content

- **More featured papers**: keep the two-column card grid at 472px cards with 40px gaps; supply a 16:9 figure for every card so rows stay even.
- **Papers without figures**: use the citation-list item (16px #ffffff, underlined title, italic venue, #34d399 uppercase links) rather than an empty card.
- **A results table**: center it in the 768px `max-w-3xl` column, 14px #d1d5db cells on #17181c, 1px #4b5563 row rules, 12px/500 uppercase #6ee7b7 headers.
- **News**: reuse the citation-list rhythm (16px gaps) with a 14px #9ca3af date line above each item.
- **More authors**: let the citation author line wrap inside 768px; keep plain #ffffff with no bolding.

## Do's and Don'ts

- Do keep the hero as a full-bleed dark photograph with the biography directly on it; text stays white or #cbd5e1.
- Do use mint #6ee7b7 uppercase 12px tags as the only color on cards.
- Do give every card a 16:9 figure with a 6px radius.
- Do center section titles at 30px/700.
- Don't use light backgrounds below the hero; the page stays #17181c.
- Don't place emerald on large areas; it is for tags, citation links and the hover band.
- Don't add borders to cards; the image well and spacing define them.

## Surfaces

A #27272a header, a photographic hero over #000000, then a flat #17181c page. Card image wells are #1f2937. No panels, borders or shadows on content cards.

## Imagery

A wide landscape photo of a night sky (deep navy to violet with a pink cloud) over a black hill fills the hero. Featured publications and talks use paper figures (diagrams, plots, illustrations) on white, shown as 16:9 thumbnails. One circular portrait with an emoji badge.

## Layout

A full-bleed hero, then centred sections of decreasing width: a 650px prose column, a 1024px card grid (two columns), a 768px citation list, and full-width single-column talk cards. Generous 96px section padding.

## Agent Prompt Guide

Quick colors: page #17181c, header #27272a, card well #1f2937, text #ffffff, bio #cbd5e1, muted #9ca3af, tag #6ee7b7, link #34d399, button border #4b5563.

1. "Build a hero section with padding 96px 0 over a full-bleed photo (background-color #000000, background-size cover, background-position 50%). Center a flex row with a 48px gap: left a 256px column with a 150px round avatar in a 4px #1f2937 ring, a 30px/700 #ffffff first name, a 16px/600 role and 24px #f4f4f5 social icons; right a 650px column with 16px/28px #cbd5e1 bio text, 500-weight underlined #ffffff links, and an outlined button (#1f2937 fill, 1px #4b5563, 8px radius, padding 8px 16px, 14px/500 #9ca3af)."
2. "Make a featured-publications grid: max-width 1024px, two columns, 40px gap. Each card: a 16:9 image well (#1f2937, 6px radius, hover scale 1.05), then a 12px/500 uppercase #6ee7b7 tag line 20px below, an 18px/600 #ffffff title 8px below with a hover band linear-gradient(to right, #065f46, #064e3b) growing to 100% 10px, and a 14px #9ca3af date 12px below."
3. "Create a citation list in a 768px column on #17181c: each item 16px #ffffff authors, (year), an underlined title link, italic venue, then a row of 16px/700 uppercase #34d399 links (CITE, URL) with small outline icons; items 16px apart."

## Similar Pages

- Hugo Blox Builder (formerly Wowchemy / Hugo Academic) "resume biography" homepages using the dark theme with a hero background image.
- Dark academic portfolios that show publications as figure cards rather than text lists.

## Quick Start

```css
:root {
  --bg: #17181c;
  --header: #27272a;
  --card: #1f2937;
  --border: #4b5563;
  --text: #ffffff;
  --bio: #cbd5e1;
  --muted: #9ca3af;
  --tag: #6ee7b7;
  --link: #34d399;
  --font: "Inter var", Inter, ui-sans-serif, system-ui, sans-serif;
  --section-pad: 6rem;
  --card-radius: 6px;
}
body { margin: 0; background: var(--bg); color: var(--text); font: 16px/24px var(--font); }
.section-title { font-size: 30px; font-weight: 700; line-height: 36px; text-align: center; margin-bottom: 24px; }
.tag { font-size: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: .05em; color: var(--tag); }
```

## Provenance

- **URL**: https://vasevarad.github.io/
- **Person**: Vasudha Varadarajan (Postdoctoral Research Associate, CMU LTI); field: computational social science, psychology-oriented NLP.
- **Venue / award**: ACL 2023 Outstanding Paper, first author of "Transfer and Active Learning for Dissonance Detection".
- **Selection reason**: Rule A; award listed at https://2023.aclweb.org/program/best_papers/ ; homepage from the GitHub vasevarad blog field, and the page lists the paper.
- **Template credit**: Hugo Blox Builder (footer "Published with Hugo Blox Builder"), emerald theme; hero photo from Pexels (file name pexels-qhung999-27200282).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `index.html` read directly, and element probes of the Tailwind-styled elements, on 2026-10-28.
