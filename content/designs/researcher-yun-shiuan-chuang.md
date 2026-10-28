# Two-Weight Masthead — Style Reference

> A broadsheet masthead in two weights of the same face, followed by numbered questions on hairlines and a cool gray reading room for the papers.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's own `css/portfolio-2026.css` and `index.html`, and probes of rendered elements. No web font loads: the type is the operating system's UI face, so the fractional weights in the stylesheet (680, 670, 650, 460) are honoured exactly only where the OS face is variable (SF Pro on macOS, Segoe UI Variable on Windows 11); elsewhere they snap to the nearest available weight.

## Overview

A typographic single-column homepage, about 3,920px tall at 1440, white with near-black ink (#202428), a cool gray for secondary text (#626a72) and one muted denim link color (#1b5c91). A slim header (name left, four small gray links right) sits on a hairline. The hero sets the name in two weights of one family at 74.4px: "Yun-Shiuan" in 680 and "(Sean) Chuang" on a second line in 460, under a tiny uppercase eyebrow ("AI RESEARCH & ENGINEERING"), with a 600-weight role line, a gray intro paragraph, two arrow links and a 278×300px portrait with a 4px radius on the right. Each section opens with an uppercase eyebrow and a 48px/670 heading. Research questions are numbered rows (01, 02, 03) between 1px #d9dde0 hairlines. Publications sit in a full-width #f5f6f7 band as a two-column list: a 218px gutter for "year · venue" in small gray type and a column with an underlined denim title, a gray author line with the owner's name in bold ink, and italic venue details. A "Full publication list →" outlined button, a hairline background timeline and a gray footer band with a large "Contact" heading close the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff / #fafbfb / #fdffff / #fffffd 86.0%; light gray #d2d6d7 4.3% and #f1f2f3 2.0% (the hairlines and the portrait's sky); navy #2e364d 4.2% (the portrait's jacket and the heavy name type); mid gray #9ea4a9 3.6% (antialiased gray text and the photo).

Anatomy in DOM order (`.content-width { width: min(1050px, calc(100% - 48px)) }`, so content runs x=195–1245):

1. **Header** (`header.site-header`, 0–69px): 68px min-height row plus a 1px #d9dde0 bottom border. "Yun-Shiuan Chuang" 16px/650, letter-spacing -0.018em, #202428 at left; links Research, Publications, Background, Contact at 14.4px #626a72, 23px gaps, at right.
2. **Hero** (`section.hero`, 69–640px): grid minmax(0,1fr) 278px, gap clamp(45px, 9vw, 135px) = 129.6px, padding 92px 0, 1px #d9dde0 bottom border, `align-items: center`.
3. **Eyebrow** (y=161): "AI RESEARCH & ENGINEERING", 11.52px/650 uppercase, letter-spacing 0.09em, #626a72. Gap 14px.
4. **Name** (`h1`, y=194, two lines, 155px tall): clamp(3rem, 6vw, 4.65rem) → 74.4px, line-height 1.04, letter-spacing -0.032em; "Yun-Shiuan" weight 680, "(Sean) Chuang" weight 460, #202428. Gap 16px.
5. **Role** (`p.hero-role`, y=364): "Staff AI Research Scientist · PayPal AI Research", 17.28px/600 #202428. Gap 20px.
6. **Intro** (`p.hero-intro`, y=412, max 650px): 17.6px/400, line-height 1.62, #626a72. Gap 23px.
7. **Link row** (y=521): "Selected work ↓" and "Google Scholar ↗", 16px/600 #1b5c91, no underline, 20px apart.
8. **Portrait** (x=967, y=204): 278×300px (aspect 1/1.08), object-position center 31%, 4px radius, vertically centred against the text column.
9. **Research section** from y=640: padding 88px 0; eyebrow "RESEARCH" at y=728, then "LLM agents and human behavior" 48px/670 (y=760), then a 16.8px #626a72 paragraph (y=833) running past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (body background) | page, "Full publication list" button fill |
| Ink | #202428 | --text | name, headings, role line, site name, owner's name in author lists, resource links, skip link fill |
| Gray | #626a72 | --muted | eyebrows, nav links, intro and paragraphs, numbers, year/venue gutter, author lines, footer bottom |
| Light Band | #f5f6f7 | --light | publications band, footer band |
| Hairline | #d9dde0 | --rule | header border, hero bottom border, list rows, footer borders |
| Denim | #1b5c91 | --link | links, publication titles, link row, email, button border and text |
| Denim Hover | #0d3f68 | (literal) | link hover |
| Button Hover | #eaf1f7 | (literal) | "Full publication list" hover fill |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI (all text) | ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif | no web font loaded; the OS UI face (Segoe UI on Windows, SF Pro on macOS) | Inter (variable, to keep the 680/460 weights) |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.hero h1` / `.hero h1 span` | clamp(3rem, 6vw, 4.65rem) → 74.4px / 680 and 460 / 1.04, letter-spacing -0.032em | #202428 |
| Section heading | `.section-intro h2`, `.section-heading-row h2` | clamp(2rem, 3.7vw, 3rem) → 48px / 670 / 1.16, letter-spacing -0.032em | #202428 |
| Eyebrow | `.eyebrow` | 0.72rem = 11.52px / 650 uppercase, letter-spacing 0.09em | #626a72 |
| Site name | `.site-name` | 16px / 650, letter-spacing -0.018em | #202428 |
| Nav | `.nav-links a` | 0.9rem = 14.4px | #626a72 |
| Role | `.hero-role` | 1.08rem = 17.28px / 600 | #202428 |
| Intro | `.hero-intro` | 1.1rem = 17.6px / 400 / 1.62 | #626a72 |
| Section paragraph | `.section-intro > p:last-child` | 1.05rem = 16.8px | #626a72 |
| Body | `body` | 16px / 400 / 1.62 | #202428 |
| Row title | `.interest-list h3`, `.background-list h3` | 1.18rem = 18.88px / 650 / 1.35 | #202428 |
| Number / year / date | `.item-number`, `.publication-year`, `.background-date` | 0.78rem = 12.48px, tabular numerals | #626a72 |
| Publication title | `.publication h3 a` | 1.13rem = 18.08px / 650 / 1.38, underline 1px offset 3px | #1b5c91 |
| Author line | `.publication div > p` | 0.93rem = 14.88px; own name 700 #202428 | #626a72 |
| Button | `.full-publications-link` | 0.95rem = 15.2px / 650 | #1b5c91 |
| Footer bottom | `.footer-bottom` | 0.8rem = 12.8px | #626a72 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 4px | none | none |
| "Full publication list" button | 4px | 1px #1b5c91 | none |
| Header, hero, list rows | 0 | 1px #d9dde0 (bottom; lists also top) | none |
| Footer band | 0 | 1px #d9dde0 top; inner bottom row 1px #d9dde0 top | none |

## Layout Metrics

- **Container**: `.content-width { width: min(1050px, calc(100% - 48px)); margin-inline: auto }` → x=195–1245; the muted publications band and footer are full bleed with the same inner width.
- **Hero**: grid minmax(0,1fr) 278px, gap 129.6px (clamp(45px, 9vw, 135px)), padding 92px 0 → text column 642px.
- **Sections**: padding 88px 0; heading 17px above the paragraph; section intro max 760px.
- **Research rows**: list starts 54px below the intro with a top hairline; rows grid 64px + 1fr, gap 22px, padding 24px 0, bottom hairline; descriptions max 675px.
- **Publications**: list 47px below the heading row; rows grid 218px + 1fr, gap 28px, padding 23px 0; button 28px below, padding 12px 17px.
- **Background**: intro margin-bottom 45px; rows grid 160px + 1fr, gap 28px, padding 25px 0.
- **Footer**: padding-top 68px; main row padding-bottom 59px, flex space-between with 50px gap; bottom row padding 19px 0.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| >720px | 24px min (195px at 1440) | 16px | 74.4px | two-column hero; 64px / 218px / 160px gutters on lists |
| ≤720px | 18px, content max 600px | 16px | clamp(2.6rem, 12.8vw, 3.75rem) | hero one column with 38px gap and 60px padding; portrait min(278px, 75vw); sections 64px padding; list rows stack with 7px gap; nav links 12.8px with 14px gaps |
| ≤470px | 18px | 16px | 41.6px floor | third nav link (Background) hidden; nav gap 13px |

## Components

- **Eyebrow + heading**: 11.52px/650 uppercase #626a72 with 0.09em tracking, 14px above a 48px/670 #202428 heading with -0.032em tracking.
- **Two-weight name**: one h1 with a 680-weight first line and a 460-weight span on the next line, both 74.4px, line-height 1.04.
- **Numbered row** (`.interest-list article`): grid 64px + 1fr, gap 22px, padding 24px 0, 1px #d9dde0 bottom border (list top border too); "01" in 12.48px #626a72 tabular numerals with 3px top margin; 18.88px/650 title; #626a72 description, max 675px.
- **Publication row** (`.publication`): grid 218px + 1fr, gap 28px, padding 23px 0, hairline bottom; left "2026 · ACL (Industry Track)" in 12.48px #626a72; right an underlined 18.08px/650 #1b5c91 title with "↗", then a 14.88px #626a72 author/citation line with the owner in 700 #202428 and italic proceedings; optional "Code ↗" in 600 #202428.
- **Outlined button** (`.full-publications-link`): #ffffff fill, 1px #1b5c91 border, 4px radius, padding 12px 17px, 15.2px/650 #1b5c91; hover fill #eaf1f7.
- **Arrow links**: 16px/600 #1b5c91 without underline, followed by ↓ or ↗; underline at 4px offset on hover.
- **Footer**: #f5f6f7 band with a 48px "Contact" heading, a 16.8px/600 #1b5c91 email, a column of 14.88px links on the right, and a hairline bottom row with "© 2026" and "Back to top ↑" in 12.8px #626a72.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header | yes | hairline bar, bold name, small gray links |
| Hero with eyebrow and two-weight name | yes | 74.4px name, gray intro, arrow links, 278px portrait |
| Research questions | yes | numbered hairline rows |
| Selected publications | yes | #f5f6f7 band, 218px year/venue gutter, underlined denim titles |
| Full publication list link | yes | outlined button |
| Experience and education | yes | 160px date gutter, hairline rows |
| Contact | yes | footer band with large heading and email |
| News | absent from the source | none |
| Awards | present but non-standard | written into the publication gutter ("Best Paper Award; Computational Modeling Prize") |

## Adapting to Other Content

- **More co-authors**: keep the citation line at 14.88px #626a72 and bold only the owner's name (700 #202428).
- **Awards on papers**: write them into the 218px gutter after the venue, as the source does, in the same 12.48px #626a72; do not add badges.
- **News**: reuse the background row (160px date gutter, 25px padding, hairlines) in a new section with an eyebrow and a 48px heading.
- **A results table**: hairline rows (1px #d9dde0), 12.48px uppercase #626a72 headers with 0.09em tracking, 14.88px #202428 cells, best value 650.
- **Long publication lists**: keep a selected set on the #f5f6f7 band and link the rest with the outlined button.

## Do's and Don'ts

- Do set the name in two weights of the same face, heavy first line and light second line, at 74.4px with tight tracking.
- Do open every section with a small uppercase eyebrow over a 48px heading.
- Do structure lists as left-gutter grids separated by 1px #d9dde0 hairlines.
- Do keep #1b5c91 for links and titles only; everything else is ink or gray.
- Don't add cards, shadows or tag chips.
- Don't round anything beyond 4px.
- Don't tint sections other than the publications band and the footer.

## Surfaces

White page; one full-width #f5f6f7 band behind the publications and the same gray for the footer. No panels; separation is hairlines and 88px section padding.

## Imagery

A single 278×300px outdoor portrait (autumn hills behind) with a 4px radius. No paper figures or icons; arrows (↓ ↗ →) are text glyphs.

## Layout

A 1050px column. The hero is a two-column grid with a wide gap; every other section is a stacked eyebrow, heading and hairline list whose rows use a fixed left gutter (64px numbers, 218px year/venue, 160px dates).

## Agent Prompt Guide

Quick colors: page #ffffff, ink #202428, gray #626a72, hairline #d9dde0, band #f5f6f7, link #1b5c91, hover fill #eaf1f7.

1. "Build a hero in a 1050px container: grid minmax(0,1fr) 278px, gap 129.6px, padding 92px 0, 1px #d9dde0 bottom border, items centred. Eyebrow 11.52px/650 uppercase #626a72 with 0.09em tracking; name 74.4px, line-height 1.04, letter-spacing -0.032em, #202428, first line weight 680 and second line weight 460; role 17.28px/600; intro 17.6px #626a72; two 16px/600 #1b5c91 arrow links 20px apart. Portrait 278px wide at aspect 1/1.08 with 4px radius."
2. "Create numbered research rows: list with a 1px #d9dde0 top border, 54px below the section intro; each row grid 64px + 1fr, gap 22px, padding 24px 0, 1px #d9dde0 bottom border; number 12.48px #626a72 tabular; title 18.88px/650 #202428; description #626a72, max 675px."
3. "Make a publications band: full-width #f5f6f7 with padding 88px 0; inside a 1050px column, rows grid 218px + 1fr, gap 28px, padding 23px 0, hairline bottom. Left: '2026 · ACL' in 12.48px #626a72. Right: underlined 18.08px/650 #1b5c91 title, then 14.88px #626a72 citation with the owner's name 700 #202428. End with an outlined button: #ffffff, 1px #1b5c91, 4px radius, padding 12px 17px, 15.2px/650 #1b5c91, hover #eaf1f7."

## Similar Pages

- Editorial portfolio homepages that rely on system type, hairline lists and a single link color.
- Industry-researcher pages with a large two-weight name and a selected-publications band.

## Quick Start

```css
:root {
  --text: #202428;
  --muted: #626a72;
  --light: #f5f6f7;
  --rule: #d9dde0;
  --link: #1b5c91;
  --sans: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
body { margin: 0; color: var(--text); background: #ffffff; font: 16px/1.62 var(--sans); }
.content-width { width: min(1050px, calc(100% - 48px)); margin-inline: auto; }
.eyebrow { margin: 0 0 14px; color: var(--muted); font-size: .72rem; font-weight: 650; letter-spacing: .09em; text-transform: uppercase; }
h1, h2, h3 { letter-spacing: -.032em; }
.section { padding-block: 88px; }
```

## Provenance

- **URL**: https://yunshiuan.github.io/
- **Person**: Yun-Shiuan (Sean) Chuang (Staff AI Research Scientist, PayPal AI Research); field: computational cognitive science / social learning.
- **Venue / award**: CogSci 2024 Computational Modeling Prize (Higher-Level Cognition), first author of "The Delusional Hedge Algorithm as a Model of Human Learning from Diverse Opinions".
- **Selection reason**: Rule B(3); prize listed at https://cognitivesciencesociety.org/cogsci-2024/ ; personal github.io site.
- **Template credit**: none stated; hand-written `index.html` with `css/portfolio-2026.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, `portfolio-2026.css` and `index.html` read directly, and element probes, on 2026-10-28.
