# Plex Mono Zine — Style Reference

> A developer's zine on off-white paper: everything in IBM Plex Mono, emoji for signposts, blue links on dashed underlines.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share and DOM boxes from `tools/computed_style.py`, plus a selector probe of the nav, masthead, avatar, rules, news list and footer), the 1440×900 and full-page screenshots, and the Astro build stylesheet `/_astro/_slug_.L531v-GM.css`, the component `<style>` and the theme script in `index.html` read directly. IBM Plex Mono 400, 600 and 700 load (500 is requested but unused here); headings set to 800 render as synthetic bold on the 700 file. The site has a light and a dark palette: an inline script picks `data-theme` from localStorage or `prefers-color-scheme`, and a moon/sun button toggles it. The capture and the values below are the light theme unless marked dark. The page is 1449px tall at 1440 wide.

## Overview

A narrow, calm home page set entirely in IBM Plex Mono on #fdfdfd. A top bar holds "Nikhila Ravi" in 20px/700 on the left and five nav links on the right, each prefixed by a colour emoji (🧠 Research, 🎤 Talks, 📰 Press, ✍️ Writing, 🌱 Projects), then a moon icon button; a 1px #ece9e9 line runs under it. The masthead is a flex row: a 250px circular portrait (a round cut-out PNG) and, 30px to its right, the name in 32px heavy mono, a 15px/1.7 grey (#555555) bio paragraph with #0066cc links underlined by a dashed line 4px below the text, and a row of five 22px grey social glyphs that rotate and turn blue on hover. A hairline rule follows, then "📢 Updates" as a 24px/600 heading and a disc-bulleted news list in 16px/1.75 near-black #282728 with "(link)" links. The footer, set off by a full-width hairline, centres the social icons, a 14px "Design inspired by …" credit and a 13px copyright. Generous white space and no colour besides the link blue and the emoji.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): paper #fdfdfd 74.6% plus #fffffe 6.1%, #fdfdfc 2.8%, #fcfdfe 0.9%, #fefdfd 0.6%, #fdfdfe 0.4%; light grey #eaecee 9.4% (anti-aliased mono text, rules, photo highlights); mid grey #838286 5.2% (bio text, icons, dark photo background). The blue links, the portrait's blue sweater and the emoji are each under 1%.

Anatomy in DOM order (desktop 1440px; `.head-container` and `.body-container` max-width 950px with 24px padding, content x=269, 902px wide):

1. **Top bar** (`nav.top-nav`, y=0, 86px tall): flex, space-between, padding 24px 0, border-bottom 1px #ece9e9.
2. **Site title** (`a.site-title`, x=269, y=24): IBM Plex Mono 20px/700, #282728, no underline; hover #0066cc.
3. **Nav links** (`a.nav-link`, y=29, from x=570): 15px/400 #282728, emoji prefix, gaps 24px; hover #0066cc; active page #0066cc with a wavy underline offset 6px.
4. **Theme toggle** (`button.theme-toggle`, x=1135, y=25): 36×36px, padding 8px, 8px radius, 20px moon icon; hover fill #e6e6e6. Bar ends at y=86.
5. **Masthead** (`section.masthead`, y=86, padding 48px 0 32px): flex row, items centred, gap 30px.
6. **Portrait** (`.site-avatar img`, x=269, y=202): 250×250px; the image itself is a circular cut-out (CSS radius 6px does not show).
7. **Name** (`h1.site-name`, x=549, y=134): 32px/800 (rendered bold), line-height 1.3, #282728, margin-bottom 16px.
8. **Bio** (`p.site-description`, y=192): 15px/400, line-height 1.7 (25.5px), #555555; links #0066cc, dashed underline, offset 4px. Gap 23px.
9. **Social icons** (`.social-icons`, y=492): five 28px boxes with 22px SVG glyphs (Google Scholar cap, GitHub, LinkedIn, X, mail), gap 16px, #555555. Masthead ends at y=552.
10. **Rule** (`hr`, y=576): 1px #ece9e9, margin-top 24px.
11. **Updates heading** (`.updates-section h2`, y=601): 24px/600, line-height 1.3, #282728, "📢" emoji prefix, margin 24px 0.
12. **News list** (`ul.news-list`, y=656): disc bullets, padding-left 24px; items 16px/400, line-height 1.75 (28px), #282728, padding-left 5.6px, 3.2px apart; "(link)" anchors #0066cc.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #fdfdfd | --background | page background |
| Ink | #282728 | --text-color | site title, nav links, name, headings, news items |
| Soft Ink | #555555 | --text-light | bio paragraph, social icons, footer credit and copyright |
| Link Blue | #0066cc | --link-color | inline links (dashed underline), hover colour of title, nav and icons, active nav link |
| Muted | #e6e6e6 | --muted | theme-toggle hover fill, code background on posts |
| Hairline | #ece9e9 | --border | top-bar bottom rule, `hr`, footer top rule |
| Dark Paper | #1a1a2e | --background (dark) | page background in dark theme |
| Dark Ink | #eaedf3 | --text-color (dark) | text in dark theme |
| Dark Soft Ink | #a0a3b1 | --text-light (dark) | secondary text in dark theme |
| Violet Link | #a855f7 | --link-color (dark) | links in dark theme |
| Dark Hairline | #3d3d5c | --border (dark) | rules in dark theme |
| Dark Muted | #2d2d44 | --muted (dark) | toggle hover in dark theme |

Declared but not visible on the home page: `.award-highlight` (#1565c0 on rgba(33,150,243,0.15)), `.oral-highlight` (#1976d2) and `.top-paper-highlight` (#7b1fa2) chips and the `.research-item` layout belong to the Research page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Mono (everything) | IBM Plex Mono, monospace (Google Fonts 400, 500, 600, 700) | IBM Plex Mono 400, 600, 700 | JetBrains Mono |
| Emoji | system emoji font | Segoe UI Emoji in the Windows capture | Noto Color Emoji |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Site title | `.site-title` | 20px / 700 | #282728 |
| Nav link | `.nav-link` | 15px / 400 / 1.85 | #282728 |
| Name | `.site-name` | 32px / 800 (renders as 700) / 1.3 | #282728 |
| Bio | `.site-description` | 15px / 400 / 1.7 | #555555 |
| Section heading | `h2` | 24px / 600 / 1.3 | #282728 |
| Body | `body` | 16px / 400 / 1.85 | #282728 |
| News item | `.news-list li` | 16px / 400 / 1.75 | #282728 |
| Link | `a` | inherits, dashed underline offset 4px; hover solid | #0066cc |
| Footer credit | `.footer-attribution` | 14px / 400 / 1.6, centred | #555555 |
| Copyright | `.footer-copyright` | 13px / 400, centred | #555555 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | circular cut-out image (CSS 6px) | none | none |
| Theme toggle | 8px | none | none |
| Top bar | 0 | 1px #ece9e9 bottom | none |
| Section rule | 0 | 1px #ece9e9 top | none |
| Footer | 0 | 1px #ece9e9 top (full width) | none |

## Layout Metrics

- **Container**: `.head-container` and `.body-container`, max-width 950px, padding 0 24px, centred (902px content at x=269 when the viewport is 1440).
- **Top bar**: padding 24px 0, nav gap 24px.
- **Masthead**: padding 48px 0 32px, flex row, align-items center, gap 30px; avatar column 250px fixed; text column flex 1 (622px).
- **Sections**: `hr` margin 24px 0 0; updates h2 margin 24px 0 (1em), other h2 2.5em top and 1em bottom; lists margin 16px 0, padding-left 24px, items 3.2px apart.
- **Footer**: full width, border-top, padding 32px 0, pushed to the bottom by a min-height 100vh flex wrapper; inner 950px centred; social row centred.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≤480px | 32px | 16px; news 14px | name 24px, bio 14px | — |
| ≤768px | 32px | 16px; news 15px/1.65 | name 28px, h2 20px | nav links hidden behind a hamburger that opens a 280px slide-in menu; masthead stacks and centres; avatar 170px; social icons centred |
| >768px | 24px | 16px | name 32px, h2 24px | masthead row, inline nav |

## Components

- **Emoji nav**: right-aligned row of 15px mono links, each "emoji + word", 24px gaps, #282728; hover #0066cc; current page #0066cc with a wavy underline offset 6px; followed by a 36px icon button (moon in light, sun in dark) with an 8px-radius #e6e6e6 hover fill.
- **Dashed link**: #0066cc, `text-decoration: underline dashed`, offset 4px; hover turns the underline solid.
- **Masthead**: 250px circular portrait left, 30px gap, then a heavy 32px mono name, a 15px/1.7 #555555 bio and a row of 22px grey SVG social icons (gap 16px) that rotate 8° and scale 1.1 to #0066cc on hover.
- **Emoji section heading**: 24px/600 mono heading with a leading emoji ("📢 Updates"), no underline.
- **News list**: disc bullets, 16px/1.75 sentences, trailing "(link)" anchors in #0066cc.
- **Footer**: full-width 1px #ece9e9 top rule, centred icon row, a 14px "Design inspired by …" line with three links and a 13px copyright.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Site title / nav | yes | mono title left, emoji links right, theme toggle |
| Portrait | yes | 250px circle beside the bio |
| Bio | yes | 15px grey mono paragraph |
| Social links | yes | 22px grey SVG icons, in the masthead and the footer |
| Updates / news | yes | disc list under an emoji heading |
| Publications | absent from the source | on the separate Research page |
| Talks / press / writing / projects | absent from the source | separate pages linked from the nav |
| Dark mode | yes | toggle plus `prefers-color-scheme` default |
| Footer | yes | centred icons, design credits, copyright |

## Adapting to Other Content

- **Publications**: use the site's own Research-page recipe: a flex row with a 280×160px media box on the left (4px radius) and a text column with an 18px/600 title, 15px #555555 author list (own name 700 #282728), 15px italic venue and slash-separated #0066cc links; award chips 14px/500, 4px radius, padding 3px 10px, #1565c0 on rgba(33,150,243,0.15).
- **More authors**: the 15px author list wraps freely; keep the own name bold and dark.
- **A results table**: mono 14px, 1px #ece9e9 row rules, #282728 text, header 600; no fills.
- **Long news lists**: keep disc bullets and 1.75 leading; add a bold 600 date at the start of each item rather than a separate column.
- **More sections**: each gets an emoji-prefixed 24px/600 h2 and an `hr` before it.

## Do's and Don'ts

- Do set everything, including headings and nav, in IBM Plex Mono.
- Do use one emoji per nav item and section heading as the only decoration.
- Do keep links #0066cc with dashed underlines offset 4px.
- Do keep both palettes in sync through the CSS variables.
- Don't add cards, shadows or coloured backgrounds; separation is hairlines and white space.
- Don't let the text column grow past 950px.

## Surfaces

Off-white #fdfdfd paper with #ece9e9 hairlines in light mode; deep indigo #1a1a2e with #3d3d5c hairlines in dark mode. No panels or cards.

## Imagery

One circular colour portrait; colour emoji as signposts; monochrome SVG social icons.

## Layout

A 950px column: top bar, two-column masthead (portrait + bio), a rule, an updates list, then a full-width footer pinned to the bottom of the viewport. About 1449px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: paper #fdfdfd, text #282728, secondary #555555, link #0066cc, hairline #ece9e9, hover fill #e6e6e6; dark theme #1a1a2e, #eaedf3, #a0a3b1, link #a855f7, hairline #3d3d5c.

1. "Make a top bar in IBM Plex Mono: 950px container with 24px side padding, flex space-between, padding 24px 0, 1px #ece9e9 bottom border; title 20px/700 #282728; right-side links 15px #282728 each prefixed with an emoji, 24px gaps, hover #0066cc, active #0066cc with a wavy underline offset 6px; a 36px moon icon button with 8px radius and #e6e6e6 hover."
2. "Build a masthead: flex row, align-items center, gap 30px, padding 48px 0 32px; a 250px circular portrait; text column with the name in IBM Plex Mono 32px heavy #282728, a 15px/1.7 #555555 bio with #0066cc links underlined dashed at 4px offset, and five 22px #555555 social icons 16px apart that rotate 8° and turn #0066cc on hover."
3. "Add an updates section: a 1px #ece9e9 rule, then '📢 Updates' in 24px/600 #282728, then a disc list with 24px left padding, items 16px/1.75 #282728 ending in '(link)' anchors in #0066cc."

## Similar Pages

- Monospace developer-style personal sites (the footer credits Peter Steinberger, Andrea Coravos and Jon Barron as inspiration).
- Astro-built researcher pages with a light/dark toggle.

## Quick Start

```css
:root { --background: #fdfdfd; --text-color: #282728; --text-light: #555555; --link-color: #0066cc; --muted: #e6e6e6; --border: #ece9e9; }
[data-theme="dark"] { --background: #1a1a2e; --text-color: #eaedf3; --text-light: #a0a3b1; --link-color: #a855f7; --muted: #2d2d44; --border: #3d3d5c; }
body { background: var(--background); color: var(--text-color); font: 400 16px/1.85 "IBM Plex Mono", monospace; margin: 0; }
.head-container, .body-container { max-width: 950px; margin: 0 auto; padding: 0 24px; }
.top-nav { display: flex; justify-content: space-between; align-items: center; padding: 24px 0; border-bottom: 1px solid var(--border); }
a { color: var(--link-color); text-decoration: underline dashed; text-underline-offset: 4px; }
a:hover { text-decoration-style: solid; }
.site-description { color: var(--text-light); font-size: 15px; line-height: 1.7; }
```

## Provenance

- **URL**: https://www.nikhilaravi.com/
- **Person**: Nikhila Ravi (computer vision, segmentation, 3D).
- **Venue / award**: ICLR 2025 Outstanding Paper Honorable Mention, "SAM 2: Segment Anything in Images and Videos" (first author). https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/
- **Selection reason**: award rule (first/last author); chosen for the monospace type, emoji nav icons and circular portrait.
- **Template credit**: Astro build; footer says "Design inspired by Peter Steinberger, Andrea Coravos, and Jon Barron".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, DOM boxes), a selector probe of nav, masthead, rules, news and footer, the 1440×900 and full-page screenshots, and the Astro stylesheet, component style and theme script read directly, on 2026-10-28.
