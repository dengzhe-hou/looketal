# Akbir Khan — Style Reference

> An index card pinned in a greenhouse.

**Theme:** both (follows `prefers-color-scheme`)

Measurements are normalized from the static HTML and `style.css`; roles are interpreted. The page is tiny, so nearly every rule is accounted for.

## Overview

A single 650px column in the system UI font, warm off-white background, and plain CSS `green` links. The whole home page is a lowercase title with a seedling emoji ("akbir khan 🌱"), a 220px photo with 4px radius, three short paragraphs (AI safety researcher, PhD with Tim Rocktäschel, the debate paper's ICML 2024 Best Paper, earlier work), and a flex row of seven nav links underlined by a 1px dark border: blog, github, scholar, last.fm, discogs, resume, thesis. In dark mode the page turns #333 with white text and mint-green links (#6fffa3). There is no publication list, no news and no section headings on the home page; the blog carries the rest.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Porcelain | #fafafa | `--bg` | Light background |
| Graphite | #333333 | `--text` | Light text; nav underline; dark-mode background |
| Garden Green | `green` (#008000) | `--link` | Light links (underlined, 2px offset); blog post h1 |
| Mint Glow | #6fffa3 | `--link-dark` | Dark-mode links |
| White | #ffffff | `--text-dark` | Dark-mode text |
| Ash | #666666 | `--muted` | Post dates, meta, captions, back link |
| Fog | #aaaaaa | `--muted-dark` | Muted text in dark mode |
| Code Cloud | #f5f5f5 | `--code-bg` | Code blocks (light) |
| Code Slate | #555555 | `--code-bg-dark` | Code blocks (dark); blockquote text in light |
| Quote Rule | #dddddd | `--quote-rule` | 3px blockquote left border |

## Tokens — Typography

- **Primary:** `system-ui, -apple-system, sans-serif`. No web fonts. Substitute: Inter if a fixed face is needed.
- **Mono:** `ui-monospace, monospace` for code in posts.
- **Weights:** 600 for all headings; 400 body.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Title | h1 | 1.5rem | 1.6 | 600, lowercase text, emoji suffix |
| h2 | h2 | 1.25rem | | 600, 2rem top margin |
| h3 | h3 | 1.1rem | | 600, 1.5rem top margin |
| Body | body | browser 16px (inferred) | 1.6 | |
| Meta | `.post-date`, `article .meta`, code block | 0.9rem | | #666 |
| Caption | figcaption | 0.85rem | | #666 |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Photo | 4px | Profile image, code blocks |
| Inline code | 3px | `article p code` |

- **Shadows:** none.
- **Layout max-width:** `body { max-width: 650px; margin: 0 auto; padding: 2rem 1rem; }` (1rem padding under 480px).
- **Rhythm:** paragraphs 1rem bottom margin; nav `margin-top: 2rem; gap: 1rem` (0.75rem on phones).

## Components

- **Title.** Role: identity. Lowercase name with an emoji, 1.5rem, weight 600.
- **Profile photo.** Role: portrait. `max-width: 220px; border-radius: 4px; margin-bottom: 1rem`.
- **Inline link.** Role: references in prose. `green`, underlined with `text-underline-offset: 2px`; hover drops opacity to 0.7.
- **Nav row.** Role: outbound links. Flex-wrapped row, links without text underline but with `border-bottom: 1px solid #333` and 0.25rem vertical padding.
- **Blog list (blog page).** Role: posts index. Unstyled list, 0.75rem between items, date in #666 at 0.9rem after the title.
- **Article (blog page).** Role: post body. Green h1, gray meta line, images full-width with 1.5rem margins, 3px #ddd blockquote rule.

## Page Modules

- **Title/author block:** lowercase name plus photo.
- **Bio/photo:** three short paragraphs; the debate paper link and its award are mentioned inline.
- **Awards:** only the inline ICML 2024 Best Paper mention.
- **Link buttons:** none; links to scholar, resume and thesis sit in the nav row.
- **Publication list, news, venue badges, BibTeX, media:** not on the home page.
- **Blog:** separate section with its own list and article styles in the same stylesheet.

## Do's and Don'ts

- Do keep everything lowercase and short; the home page is under a screen tall.
- Do use the named CSS color `green` in light mode and #6fffa3 in dark mode.
- Do underline nav links with a border rather than text-decoration.
- Don't add headings or sections to the home page.
- Don't load web fonts; the system UI stack is the choice.
- Don't add shadows or cards.

## Surfaces

Single flat surface: #fafafa in light, #333 in dark. Code blocks are the only inset surface.

## Imagery

One portrait photo. The seedling emoji in the title acts as the only ornament.

## Layout

Single 650px centered column with 2rem by 1rem padding. Nav wraps on narrow screens.

## Agent Prompt Guide

**Quick colors:** light bg #fafafa, text #333, link green (#008000); dark bg #333, text #fff, link #6fffa3; muted #666.

1. "Build a minimal home page: 650px centered column, system-ui font, line-height 1.6, background #fafafa, text #333. Lowercase h1 at 1.5rem weight 600 with an emoji, a 220px photo with 4px radius, then three short paragraphs."
2. "Create a link row: flex-wrapped, 1rem gap, 2rem top margin; each link in green with no text underline but a 1px solid #333 bottom border and 0.25rem vertical padding; hover sets opacity 0.7."
3. "Add a dark mode via prefers-color-scheme: background #333, text #fff, links #6fffa3, muted text #aaa, code backgrounds #555."

## Similar Pages

- [Zekun Shi](https://zekun-shi.github.io/) for another minimal text-first home page with a theme switch.
- [Dora Zhao](https://dorazhao99.github.io/) for a short bio-first page.

## Quick Start

```css
:root {
  --bg: #fafafa;
  --text: #333333;
  --link: green;
  --muted: #666666;
  --code-bg: #f5f5f5;
  --font: system-ui, -apple-system, sans-serif;
  --content-max: 650px;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #333333; --text: #ffffff; --link: #6fffa3; --muted: #aaaaaa; --code-bg: #555555; }
}
* { box-sizing: border-box; }
body { font-family: var(--font); max-width: var(--content-max); margin: 0 auto; padding: 2rem 1rem; line-height: 1.6; color: var(--text); background: var(--bg); }
a { color: var(--link); text-decoration: underline; text-underline-offset: 2px; }
a:hover { opacity: .7; }
nav { margin-top: 2rem; display: flex; flex-wrap: wrap; gap: 1rem; }
nav a { text-decoration: none; padding: .25rem 0; border-bottom: 1px solid #333; }
```

## Provenance

- **URL:** https://akbir.dev/
- **Venue/award:** ICML 2024 Best Paper (first author of "Debating with More Persuasive LLMs Leads to More Truthful Answers"), per https://icml.cc/virtual/2024/awards_detail
- **Selection reason:** Rule B; homepage taken from his GitHub profile link.
- **Template credit:** none; hand-written HTML and CSS.
- **Measurement method:** the whole stylesheet and HTML were read via `extract_style.py` and curl. Not rendered in a browser. Note that the nav border stays #333 in dark mode, where it matches the background, so in dark mode those links likely lose their visible underline (inferred from CSS).
