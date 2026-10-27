# Dora Zhao — Style Reference

> A literary blog starter repainted in sage.

**Theme:** light

Measurements are normalized from the server-rendered Gatsby HTML and its inlined CSS; roles are interpreted. The base design tokens come from Gatsby's official blog starter, and the owner's overrides are noted where they replace them.

## Overview

The structure and type scale are gatsby-starter-blog: Merriweather serif for body, Montserrat for headings, a modular scale of rem sizes, and a 56rem wrapper. The owner kept those bones and changed the voice. Links drop the starter's #005b99 blue for a quiet sage (#6f8571) and gain a wavy underline on hover; the current nav item carries a permanent wavy underline. The home page is short: a right-aligned three-item nav (home, research, cv), a hero row with a 200px circular headshot beside a "Hi 👋, I'm Dora Zhao." greeting and a two-paragraph bio with bold research areas, bracketed contact links, then a "news" list in 14px with bold `[MM/YY]` dates, and an 11px "Last Updated" footer.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Sage Leaf | #6f8571 | `--link` (override) | All links on the page; wavy underline on hover |
| Slate Ink | #2e353f | `--color-text` | Body text |
| Slate Light | #4f5969 | `--color-text-light` | Secondary text |
| Heading Night | #1a202c | `--color-heading` | Headings |
| Starter Blue | #005b99 | `--color-primary` | Starter default; still applied to `.post-list-item h2`, not seen on the home page |
| Mist Accent | #d1dce5 | `--color-accent` | Starter accent (hr and borders) |
| Placeholder Olive | #282818 | none | Gatsby image placeholder behind the headshot while it loads |
| White | #ffffff | `.representative` | Background of representative images |

## Tokens — Typography

- **Body:** Merriweather (self-hosted by the starter), fallback `Georgia, Cambria, "Times New Roman", Times, serif`. Substitute: Source Serif 4.
- **Headings:** Montserrat (weights 200 to 900 self-hosted), fallback system sans. Substitute: Inter or Poppins.
- **Weights:** headings 900 from the starter (`--fontWeight-black`), body 400, `strong` bolder; hover on the selected nav item goes to 600.

| Level | Token | Size | Notes |
|---|---|---|---|
| Root | `--fontSize-root` | 16px | |
| h2 greeting | `--fontSize-5` | 2.074rem | Montserrat, letter-spacing -.025em, line-height 1.1 |
| h3 "news" | `--fontSize-4` | 1.728rem | lowercase heading text |
| h4 | `--fontSize-3` | 1.44rem | |
| Body | `--fontSize-1` | 1rem | Merriweather, line-height 1.625 on p |
| News item | `.news` | 14px | date in bold brackets |
| Footer | inline | 11px | "Last Updated: 9/2026" |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Circle | 100% | `.bio-avatar` headshot |
| Code | .3em | Prism code blocks (starter) |

- **Shadows:** none.
- **Layout max-width:** `--maxWidth-wrapper: var(--maxWidth-4xl)` = 56rem; wrapper padding `0.25rem 0.75rem`.
- **Spacing scale:** `--spacing-1` .25rem through `--spacing-32` 8rem; paragraphs end with `--spacing-8` (2rem).
- **Hero:** flex row, `margin-bottom: 2em`; profile picture `margin-right: 2.5em`; column layout on small screens.

## Components

- **Navbar.** Role: page navigation. Flex row aligned to the right, `gap: 3em`, `margin: 2em 0 0`; lowercase labels; `.selected` gets `text-decoration: wavy underline` and goes 600 on hover.
- **Hero.** Role: greeting and bio. Flex row with a 200 by 200px circular Gatsby image (AVIF and WebP sources) and a text column: Montserrat h2 greeting with emoji, serif bio, then bracketed links `[email] [github] [twitter]`.
- **Link.** Role: inline links. #6f8571, no underline; hover adds a wavy underline.
- **News item.** Role: dated update. `li.news` at 14px with no extra margin; `<strong>[06/26]</strong>` date prefix; list items indented 2em.
- **Footer.** Role: freshness note. `<hr>` then an 11px "Last Updated" span.

## Page Modules

- **Title/author block:** greeting h2 with the name, beside a round headshot.
- **Bio/photo:** two paragraphs naming advisors, fellowships and prior roles, with research areas in bold and key verbs in italics.
- **News:** short dated list.
- **Publication list:** on a separate "research" page (`.research` list styles exist in the CSS); not on the home page.
- **Link buttons:** bracketed text links for contact; CV in the nav.
- **Awards:** fellowships named inline in the bio.
- **Venue badges, BibTeX, teaser media:** not on the home page.

## Do's and Don'ts

- Do keep the serif body and sans headings pairing from the starter.
- Do use sage #6f8571 for every link and the wavy underline for hover and current page.
- Do keep news dates as bold bracketed `[MM/YY]`.
- Don't reintroduce the starter's #005b99 blue on visible elements.
- Don't capitalize nav labels or the "news" heading.
- Don't add cards or shadows; the page is typographic.

## Surfaces

One white surface. The headshot sits on a dark olive placeholder only while loading.

## Imagery

One circular headshot served through Gatsby Image at 200 and 400px widths.

## Layout

Centered 56rem wrapper. Hero is a horizontal flex row that becomes a centered column on small screens. Nav sits above the hero, right-aligned.

## Agent Prompt Guide

**Quick colors:** link #6f8571, text #2e353f, heading #1a202c, secondary #4f5969, background #ffffff.

1. "Build a right-aligned lowercase nav (home, research, cv) with 3em gaps; the current item has a wavy underline. Links are #6f8571 without underline and gain a wavy underline on hover."
2. "Create a hero row: 200px circular headshot with 2.5em right margin, then a Montserrat h2 greeting 'Hi 👋, I'm …' at 2.074rem and a Merriweather bio with bold research areas, followed by bracketed links [email] [github] [twitter]."
3. "Make a news list at 14px: each item starts with a bold bracketed date like [06/26], items indented 2em, no extra spacing."

## Similar Pages

- [Angelina Wang](https://angelina-wang.infosci.cornell.edu/), a fellow Princeton Visual AI Lab alum, for a Bootstrap take on a responsible-AI home page.
- [Akbir Khan](https://akbir.dev/) for another short bio-first page.

## Quick Start

```css
:root {
  --color-text: #2e353f;
  --color-text-light: #4f5969;
  --color-heading: #1a202c;
  --link: #6f8571;
  --color-accent: #d1dce5;
  --fontFamily-sans: Montserrat, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --fontFamily-serif: "Merriweather", "Georgia", Cambria, "Times New Roman", serif;
  --fontSize-1: 1rem; --fontSize-4: 1.728rem; --fontSize-5: 2.074rem;
  --maxWidth-wrapper: 56rem;
}
html { font-size: 16px; line-height: 1.5; }
body { color: var(--color-text); font-family: var(--fontFamily-serif); }
h1, h2, h3 { font-family: var(--fontFamily-sans); color: var(--color-heading); letter-spacing: -.025em; line-height: 1.1; }
a { color: var(--link); text-decoration: none; }
a:hover, .selected { text-decoration: wavy underline; }
.navbar { display: flex; justify-content: flex-end; gap: 3em; margin: 2em 0 0; }
.news { font-size: 14px; margin: 0; }
```

## Provenance

- **URL:** https://dorazhao99.github.io/
- **Venue/award:** ICML 2024 Best Paper (first author of "Position: Measure Dataset Diversity, Don't Just Claim It"), per https://icml.cc/virtual/2024/awards_detail
- **Selection reason:** Rule B; homepage taken from her GitHub profile link.
- **Template credit:** none stated on the page; tokens and font setup match Gatsby's official gatsby-starter-blog (generator: Gatsby 5.14.3).
- **Measurement method:** inlined CSS and server-rendered HTML read via `extract_style.py` and curl. Not rendered in a browser. The HTML `<title>` is empty, and the bio is wrapped in a nested `<body>` element; both are markup quirks, not style choices.
