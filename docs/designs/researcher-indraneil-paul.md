# Ledger Green — Style Reference

> A well-kept lab notebook on cream paper: serif headlines, typewriter labels in small caps, and one bottle-green ink for every live link.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's two Astro stylesheets (`/_astro/CommandPalette.CXNvocbC.css` holds the globals and tokens, `/_astro/index.BDEYYKeZ.css` the section components) and probes of rendered elements. The page ships a dark theme behind a moon button (`:root[data-theme=dark]`); the render and this file describe the default light theme, with the dark values listed separately.

## Overview

A single-column personal page built with Astro, about 4,680px tall at 1440. The ground is warm cream #faf9f5, text is near-black #1a1a18, and one deep bottle green #004225 is the accent: bold underlined prose links, the "ip" brand tile, the active publication filter, the left bar of the availability box and the primary email button. Three variable fonts carry the character: Newsreader for the name, research-thread titles and paper titles; Source Sans 3 for prose; Source Code Pro for the nav, the role line, years, venues, chips and the large small-caps section eyebrows ("🔬 Research Interests", "📚 Publications"). The hero is a two-column grid (bio left, a 208px rounded photo right that stays sticky). Below it come numbered research threads with mono tag chips, a filterable publication list with a year gutter and right-aligned Abstract/PDF chips, a dated news feed and a contact block with two buttons. Rows are separated by 1px #e6e3db hairlines; there are no cards except the pale-green availability callout.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): cream family #faf9f5 / #faf9f6 / #fdfcf8 / #fbf9f3 / #fbf9f5 / #f8faf7 together 82.2%; pale green wash #edf0eb 9.7% (the availability box and the photo backdrop blended); warm gray #999691 8.2% (antialiased body text, the photo and the social row). The green #004225 occupies too little area to form its own cluster.

Anatomy in DOM order (content column `.wrap` max-width 920px with 40px side padding, so content runs x=300–1140):

1. **Sticky nav** (`header.nav`, 0–61px): background color-mix(in srgb, #faf9f5 92%, transparent) with `-webkit-backdrop-filter: saturate(1.4) blur(50px)`, 60px inner height, 1px bottom border transparent until the page scrolls (then #e6e3db). Left: 27px #004225 square "ip" tile (Source Code Pro 13.6px/600, white, 6px radius) plus "Indraneil Paul" in Newsreader 16.32px/600. Right: links About, Research, Publications, News, Contact in Source Code Pro 12.48px/600 #6b6b63, letter-spacing 0.02em, 22.4px apart (clamp gap at 1440); "CV" in #0a6b3d; then two 27×27px outlined buttons (moon icon, "⌘K"), white fill, 1px #d8d4c8 border, 6px radius, 16px gaps.
2. **Hero section** padding-top 72px (clamp(2.5rem, 7vw, 4.5rem)).
3. **Name** (`h1.name`, y=133, 49px tall): Newsreader 48px/600, line-height 1.02, letter-spacing -0.96px, #1a1a18, left aligned. Gap 8px.
4. **Role** (`p.role`, y=190): "PhD Researcher, Language Models & Code", Source Code Pro 13.6px/700, #6b6b63, letter-spacing 0.136px. Gap 25.6px (grid row gap).
5. **Bio** (`.bio`, y=238–606, width 588px): three justified paragraphs in Source Sans 3 17px/400, line-height 28.05px, #1a1a18, 16px apart. Links are 700 #004225 with a 1px #004225 underline drawn by a background gradient; key phrases are plain bold #1a1a18.
6. **Photo** (right column x=932, y=238, 208×208px): square crop, 14px radius, 1px #e6e3db border, shadow `0 20px 45px -24px #00422566`; `position: sticky; top: 5rem`. Below it, 13.6px gap, "📍 Berlin, Germany" in Source Code Pro 12px #6b6b63, centred.
7. **Availability box** (`.availability`, y=635, 588×128px, 28px below the bio): #edf3ee fill, 1px #dfeae1 border with a 3px #004225 left border, 6px radius, padding 15.2px 18.4px. Head "OPEN TO OPPORTUNITIES" in Source Code Pro 14.4px/700 all-small-caps #004225, letter-spacing 0.06em, led by an 8px pulsing #004225 dot; text 15.2px #1a1a18, line-height 25.08px, 6.4px below. Gap 32px.
8. **Social row** (`.socials`, y=795, centred): Scholar, GitHub, HuggingFace, LinkedIn; each a brand-colored icon (#4285f4, #24292f, #ff9d00, #0a66c2), 18.4px for Scholar, GitHub and LinkedIn and 20.8px for the HuggingFace logo (`.icon-logo`, 1.3rem), plus a 14.4px/700 small-caps label in #1a1a18, padding 6.4px 11.2px, 6px radius. Hero bottom padding 96px; the section ends at y=929.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Cream Paper | #faf9f5 | --bg | page background, nav background at 92% |
| Raised White | #ffffff | --bg-raised / --on-accent | theme and ⌘K buttons, text on green (brand tile, active filter, primary button) |
| Ink | #1a1a18 | --ink | body text, name, thread and paper titles, years, dates, venue labels, social labels |
| Muted Gray | #6b6b63 | --muted | nav links, role line, location, eyebrows, thread blurbs, author lines, chip text |
| Faint Gray | #8f8f86 | --faint | footer colophon |
| Hairline | #e6e3db | --rule | row borders of threads, publications and news, footer top border, photo border |
| Strong Rule | #d8d4c8 | --rule-strong | chip borders, button borders, theme/⌘K borders |
| Bottle Green | #004225 | --accent | prose links and their underline, brand tile, active filter chip, availability bar and head, primary button, hover color of chips and paper titles |
| Hover Green | #063d24 | --accent-hover | primary button hover fill |
| Bright Green | #0a6b3d | --accent-bright | "CV" nav link, focus outline |
| Green Wash | #edf3ee | --wash | availability box fill, chip and social hover fill, photo backdrop |
| Green Wash Strong | #dfeae1 | --wash-strong | availability box border, oral badge border |
| Crimson Badge | #a4132f on #fbe8eb, border #eebfc7 | --crimson-* | "UNDER REVIEW" badge |
| Blue Badge | #135a9e on #e9f1fb, border #bcd5f1 | --blue-* | "POSTER" badge |
| Gold Badge | #8a6a00 on #faf2d3, border #e6d18f | --gold-* | award badges |
| Dark Ground | #151916 | --bg (dark theme) | page background after the theme toggle |
| Dark Ink | #e6edf3 | --ink (dark theme) | text in dark theme |
| Dark Accent | #46c98d | --accent (dark theme) | accent in dark theme |

Social icons use brand colors as literals: Scholar #4285f4, GitHub #24292f, HuggingFace #ff9d00, LinkedIn #0a66c2.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (display) | "Newsreader Variable", ui-serif, Georgia, "Times New Roman", serif | Newsreader Variable 200–800 | Source Serif 4 |
| Sans (text) | "Source Sans 3 Variable", ui-sans-serif, system-ui, sans-serif | Source Sans 3 Variable 200–900 | Source Sans Pro |
| Mono (labels) | "Source Code Pro Variable", ui-monospace, SFMono-Regular, Menlo, monospace | Source Code Pro Variable 200–900 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1.name` | clamp(2.25rem, 6vw, 3rem) → 48px / 600 / 1.02, letter-spacing -0.02em | #1a1a18 |
| Section eyebrow | `.eyebrow` | Source Code Pro clamp(1.05rem, .72rem + 1.7vw, 1.8rem) → 28.8px / 600, small-caps, letter-spacing 0.1em (2.88px), emoji at 0.85em | #6b6b63 |
| Thread title | `h3.thread-title` | Newsreader 1.2rem = 19.2px / 600 / 1.15 | #1a1a18 |
| Paper title | `.pub-title a` | Newsreader 1.08rem = 17.28px / 600 / 1.3 | #1a1a18, hover #004225 |
| Body | `body` | Source Sans 3 1.0625rem = 17px / 400 / 1.65 | #1a1a18 |
| Prose link | `.prose a` | 17px / 700 | #004225 |
| Role line | `p.role` | Source Code Pro 0.85rem = 13.6px / 700 | #6b6b63 |
| Nav link | `.links a` | Source Code Pro 0.78rem = 12.48px / 600, letter-spacing 0.02em | #6b6b63 |
| Thread number | `.thread-no` | Source Code Pro 0.9rem = 14.4px / 700 | #1a1a18 |
| Year gutter | `.pub-year` | Source Code Pro 0.85rem = 13.6px / 700 | #1a1a18 |
| Author line | `.pub-authors` | 0.92rem = 14.72px / 400; own name 600 #1a1a18 | #6b6b63 |
| Venue | `.venue` | Source Code Pro 0.76rem = 12.16px / 400 | #1a1a18 |
| Badge | `.badge` | Source Code Pro 0.66rem = 10.56px, uppercase, letter-spacing 0.03em | per status |
| Chip | `.chip` | Source Code Pro 0.72rem = 11.52px / 500 / 1, letter-spacing 0.02em | #6b6b63 |
| News date | `.date` | Source Code Pro 0.78rem = 12.48px / 700 | #1a1a18 |
| News text | `.text` | 0.98rem = 15.68px / 400 | #1a1a18 |
| Social label | `.social-label` | 0.9rem = 14.4px / 700, small-caps, letter-spacing 0.03em | #1a1a18 |
| Footer | `.footer-inner` | Source Code Pro 0.74rem = 11.84px | #8f8f86 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Brand tile, nav buttons, social links, contact buttons, availability box | 6px (--radius) | buttons 1px #d8d4c8; box 1px #dfeae1 + 3px #004225 left | none |
| Hero photo | 14px (--radius-lg) | 1px #e6e3db | `0 20px 45px -24px #00422566` |
| Chips and filters | 999px | 1px #d8d4c8 (active: #004225) | none |
| Badges | 4px | 1px per status | none |
| Thread and publication rows | 0 | 1px #e6e3db top (last row also bottom) | none |
| News rows | 0 | 1px #e6e3db between rows only (`.item+.item` top border; none above the first or below the last) | none |
| Command palette panel | 14px | 1px #d8d4c8 | `0 1px 2px #1a1a180a, 0 12px 40px -12px #1a1a182e` |

The availability dot pulses with `box-shadow: 0 0 0 0 → 0 0 0 .5rem` in color-mix of the accent, every 2.6s.

## Layout Metrics

- **Container**: `.wrap { max-width: 57.5rem (920px); padding-inline: clamp(1.25rem, 5vw, 2.5rem) → 40px; margin-inline: auto }`, so text runs x=300–1140 (840px) at 1440.
- **Hero grid**: `grid-template-columns: minmax(0,1fr) minmax(0,13rem)` → 588px + 208px, gap 25.6px rows / 44px columns (clamp(1.75rem, 5vw, 2.75rem)). Hero padding 72px top, 96px bottom.
- **Section rhythm**: `--section-gap` clamp(3.75rem, 9vw, 6rem) = 96px; ordinary sections use `--section-gap-tight` = 62.4px top and bottom, and `.section + .section` drops the top padding, so adjacent sections sit 62.4px apart. A `<script type="module">` sits between Publications and News, so `#news` is not matched and keeps its 62.4px top padding; that gap is 124.8px. Eyebrow 48px tall with 24px margin below.
- **Threads**: grid 52px number gutter + 764px, gap 24px, padding 28px 0, blurb max-width 640px, chips 14.4px below the blurb with 6.4px gaps.
- **Publications**: filter row with 7.2px gaps and 32px bottom margin; rows grid 52px + 764px, gap 24px, padding 24px 0; Abstract/PDF/Slides chips pushed right with margin-left auto.
- **News**: rows grid 88px date + 728px text, gap 24px, padding 16px 0, hairline between rows.
- **Footer**: 1px #e6e3db top border, padding 40px 0 88px.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| >720px | 40px (5vw floor 20px) | 17px | 48px | two-column hero with sticky photo |
| ≤720px | 5vw | 17px | 6vw, 36px floor | hero stacks: photo first, centred at min(13rem, 55vw); name and role centred; socials in a 2-column grid |
| ≤640px | 5vw | 17px | 6vw | nav links hidden; brand name 15.68px |
| ≤560px | 5vw | 17px | 6vw | contact primary button full width |
| ≤520px | 20px floor | 17px | 36px | thread, publication and news rows stack (number/year/date above text) |

## Components

- **Brand tile** (`.brand-mark`): 27.2px square, #004225 fill, "ip" in Source Code Pro 13.6px/600 #ffffff, letter-spacing -0.03em, 6px radius; followed by the name in Newsreader 16.32px/600 with 9.6px gap.
- **Nav link**: Source Code Pro 12.48px/600 #6b6b63, padding 4px 0; hover turns #1a1a18 and a 1.5px #004225 underline scales in from the left at bottom -2px.
- **Section eyebrow** (`.eyebrow`): flex row, emoji at 0.85em with `filter: saturate(.85)`, then the title in Source Code Pro 28.8px/600 small-caps #6b6b63, letter-spacing 0.1em; 24px margin below; no rule under it.
- **Research thread** (`.thread`): 1px #e6e3db top border, padding 28px 0, grid 52px + 1fr; "01" in Source Code Pro 14.4px/700; title Newsreader 19.2px/600; blurb 17px #6b6b63 justified, max 640px, 8px below; a row of outlined mono chips naming the projects.
- **Chip** (`.chip`): Source Code Pro 11.52px/500 #6b6b63, padding 0.4em 0.7em (4.6px 8.1px), 1px #d8d4c8 border, 999px radius, transparent fill. Link chips hover to #004225 text, #004225 border and #edf3ee fill. Abstract/PDF/Slides chips carry a 1em leading line icon.
- **Filter chip**: the chip recipe as a button; active state #004225 fill, #004225 border, #ffffff text.
- **Publication row** (`.pub`): year gutter Source Code Pro 13.6px/700; Newsreader 17.28px/600 title whose 1.5px #004225 underline grows from 0 to 100% on hover while the text turns #004225; author line 14.72px #6b6b63 with the owner's name in 600 #1a1a18; meta row with mono venue (12.16px) plus an optional uppercase badge (10.56px, 4px radius, padding 1.6px 6.4px) and right-aligned link chips.
- **Availability callout**: #edf3ee fill, 1px #dfeae1 border, 3px #004225 left border, 6px radius, padding 15.2px 18.4px; small-caps green head with a pulsing 8px dot.
- **Social link** (`.social`): inline-flex, 7.2px gap, padding 6.4px 11.2px, 6px radius; icon 18.4px (1.15rem) in the brand color, 20.8px (1.3rem) for the HuggingFace `.icon-logo`; label 14.4px/700 small-caps. Hover: text turns the brand color, fill #edf3ee, translateY(-1px).
- **Contact buttons** (`.btn`): Source Code Pro 13.12px, padding 9.6px 16px, 6px radius, 1px #d8d4c8 border, #1a1a18 text; primary is #004225 fill with #ffffff text, hover #063d24. Outline hover: #004225 border and text on #edf3ee.
- **Command palette** (⌘K): 608px-wide white panel, 14px radius, the two-layer shadow above, mono prompt in #004225, grouped results with uppercase 10.56px #8f8f86 group labels.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav with brand tile | yes | translucent cream bar, mono links, theme and ⌘K buttons |
| Name / role / bio | yes | serif name, mono role, justified sans bio with green bold links |
| Photo | yes | 208px square, 14px radius, green-tinted soft shadow, sticky |
| Availability callout | yes | pale green box with 3px green bar |
| Social links | yes | brand-colored icons with small-caps labels |
| Research interests | yes | numbered threads with mono chips |
| Publications | yes | filter chips, year gutter, serif titles, status badges, right-aligned link chips |
| News | yes | 88px date gutter, hairline-separated rows |
| Contact | yes | muted lede and two mono buttons |
| Command palette | yes | ⌘K search overlay |
| Theme toggle | yes | dark palette #151916 / #e6edf3 / #46c98d |
| Teaching, talks, students | absent from the source | none |
| Footer | yes | mono colophon in #8f8f86 under a hairline |

## Adapting to Other Content

- **More co-authors**: keep the author line at 14.72px #6b6b63 and set the owner's name in 600 #1a1a18; let it wrap inside the 764px column.
- **Long publication lists**: keep the 52px year gutter (Source Code Pro 13.6px/700) and repeat the year on every row as the source does; add more filter chips rather than sub-headings.
- **A results or stats table**: hairline rows (1px #e6e3db), header in Source Code Pro 12.16px #6b6b63, cells 15.68px #1a1a18, best value 700 #004225. No fills.
- **Talks or teaching**: reuse the news row (88px mono date gutter, 15.68px text, hairline separators) under a new 28.8px small-caps eyebrow with an emoji.
- **Awards**: use the gold badge (#8a6a00 on #faf2d3, 1px #e6d18f, 4px radius) inside the publication meta row.

## Do's and Don'ts

- Do keep three families with fixed jobs: Newsreader for names and titles, Source Sans 3 for prose, Source Code Pro for every label, number, chip and date.
- Do use small caps (via `font-variant-caps`) for eyebrows, social labels and the availability head.
- Do separate rows with 1px #e6e3db hairlines only; keep chips outlined and transparent.
- Do reserve #004225 for links, the active filter, the brand tile, the primary button and the availability bar.
- Don't add cards, shadows or tinted panels beyond the one availability callout and the photo shadow.
- Don't center body text; only the social row and the location line are centred on desktop.
- Don't use pure black or pure white for the page; the ground is #faf9f5 and the ink #1a1a18.

## Surfaces

One flat cream ground (#faf9f5) under a 92% translucent blurred sticky nav. The only filled panel is the #edf3ee availability callout; white #ffffff appears on the small nav buttons and the command palette. Status badges bring small tinted fills (crimson, blue, gold).

## Imagery

One square portrait at 208px with a 14px radius and the green-tinted drop shadow `0 20px 45px -24px #00422566`. Everything else is text, emoji in eyebrows, and small line icons inside chips and social links. No paper thumbnails.

## Layout

A 920px column (840px of text) with a two-column hero, then full-width stacked sections each opened by a big small-caps eyebrow. Inside sections, a narrow left gutter (52px or 88px) holds numbers, years or dates and the text runs to the right, like a ledger.

## Agent Prompt Guide

Quick colors: page #faf9f5, ink #1a1a18, muted #6b6b63, hairline #e6e3db, chip border #d8d4c8, accent #004225, wash #edf3ee, faint #8f8f86.

1. "Build a two-column hero inside a 920px wrap with 40px padding: name in Newsreader 48px/600, letter-spacing -0.02em, #1a1a18; role line 8px below in Source Code Pro 13.6px/700 #6b6b63; justified Source Sans 3 17px/1.65 bio whose links are 700 #004225 with a 1px #004225 underline. Right column 208px: square photo, 14px radius, 1px #e6e3db border, box-shadow 0 20px 45px -24px #00422566, sticky at top 5rem."
2. "Make a publication list: each row has a 1px #e6e3db top border, padding 24px 0, grid 52px + 1fr with 24px gap. Year in Source Code Pro 13.6px/700 #1a1a18; title Newsreader 17.28px/600 whose 1.5px #004225 underline grows on hover; authors 14.72px #6b6b63 with own name 600 #1a1a18; meta row with Source Code Pro 12.16px venue and right-aligned outlined chips (11.52px/500 #6b6b63, 1px #d8d4c8, radius 999px, padding .4em .7em)."
3. "Create a section eyebrow and callout: eyebrow is an emoji plus Source Code Pro 28.8px/600 small-caps #6b6b63 with letter-spacing 0.1em and 24px bottom margin. Callout: #edf3ee fill, 1px #dfeae1 border, 3px #004225 left border, 6px radius, padding 15.2px 18.4px, head in 14.4px/700 all-small-caps #004225 with an 8px pulsing green dot."

## Similar Pages

- Astro or Eleventy academic homepages that pair a book serif with a code mono for labels.
- Ledger-style CVs with a narrow year gutter and hairline-separated rows.

## Quick Start

```css
:root {
  --bg: #faf9f5;
  --bg-raised: #ffffff;
  --ink: #1a1a18;
  --muted: #6b6b63;
  --faint: #8f8f86;
  --rule: #e6e3db;
  --rule-strong: #d8d4c8;
  --accent: #004225;
  --accent-bright: #0a6b3d;
  --wash: #edf3ee;
  --wash-strong: #dfeae1;
  --serif: "Newsreader", ui-serif, Georgia, serif;
  --sans: "Source Sans 3", ui-sans-serif, system-ui, sans-serif;
  --mono: "Source Code Pro", ui-monospace, Menlo, monospace;
  --measure: 57.5rem;
  --gutter: clamp(1.25rem, 5vw, 2.5rem);
  --section-gap: clamp(3.75rem, 9vw, 6rem);
  --radius: 6px;
  --radius-lg: 14px;
}
body { background: var(--bg); color: var(--ink); font: 400 1.0625rem/1.65 var(--sans); }
h1, h2, h3 { font-family: var(--serif); font-weight: 600; line-height: 1.15; letter-spacing: -.01em; }
[data-theme="dark"] { --bg: #151916; --ink: #e6edf3; --accent: #46c98d; }
```

## Provenance

- **URL**: https://ineil77.dev/
- **Person**: Indraneil Paul (PhD researcher, UKP Lab, TU Darmstadt); field: code generation with LLMs.
- **Venue / award**: ACL 2024 Outstanding Paper, first author of "IRCoder: Intermediate Representations Make Language Models Robust Multilingual Code Generators".
- **Selection reason**: Rule A; award listed at https://2024.aclweb.org/program/best_papers/ ; the GitHub iNeil77 blog field ineil77.github.io client-redirects to this domain.
- **Template credit**: custom Astro build; footer reads "Built with Astro, deployed on Cloudflare".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, the two `/_astro/*.css` files and `index.html`, and element probes, on 2026-10-28.
