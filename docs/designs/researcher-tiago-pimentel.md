# Ink Slate Profile — Style Reference

> A quiet night-mode dossier: slate ground, Inter text, pink monospace dates down the margin and a few soft tinted award pills.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), the 1440×900 and full-page screenshots, and the site's `redesign.css` and markup read directly. An inline script sets `data-theme` to `localStorage.theme` or, when nothing is stored, to `dark`, so first-time visitors always get the dark palette; the sun button switches to light. Inter 400/500, IBM Plex Mono 400/500 and the Tabler icon font load. Hairlines are declared 0.5px and compute to 1px at device-pixel-ratio 1.

## Overview

A two-column homepage on slate #131519. A sticky translucent top bar holds "Tiago Pimentel" in 16px Inter 500 at left and News / Publications / Blog / CV in 14px #aeb6c0 plus a 32px square theme button with an 8px radius on the right. Below, a 1080px grid puts a 256px sticky profile column on the left: a 152px circular photo with a hairline ring, a 27px weight-500 name, "Postdoctoral Researcher / ETH Zürich" and a 15px #aeb6c0 bio, then five 19px Tabler icons each in its own colour (magenta scholar cap, blue GitHub, orange LinkedIn, gold X, periwinkle mail). The right column, separated by a vertical hairline, has a 13px #838b96 "News" label and rows with pink #ee82b8 IBM Plex Mono dates on the left and 15px muted text on the right, then "Selected publications" with the year in pink mono and the venue acronym in grey mono in a 72px aside, a 15.5px #e8eaed title, 13.5px authors with the owner's name in white 500, and tinted award pills (blue "Spotlight", gold "SAC highlights award", magenta "Best paper award"). A centred footer closes with a "•‿•" face and Scholar · GitHub · Email.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): slate #131519 70.7% plus #121318 8.0%, #1b1c20 7.9%, #16151a 2.3%, #13151a 1.7%; grey #58575b 8.7% (anti-aliased text, hairlines and the photo). Pink dates and the coloured icons are too thin to form clusters.

Anatomy in DOM order (desktop 1440px; nav and grid 1080px at x=180 with 24px padding, content 1032px at x=204):

1. **Top bar** (`nav.nav`, sticky, 61px tall): background `color-mix(in srgb, #131519 88%, transparent)` with `backdrop-filter: saturate(140%) blur(8px)`, 1px rgba(255,255,255,0.12) bottom rule; name 16px / 500, letter-spacing -0.2px, #e8eaed at x=204; links 14px #aeb6c0, 20px apart; theme button 32×32, 1px rgba(255,255,255,0.22) border, 8px radius, sun icon #aeb6c0. Gap 48px (grid padding-top).
2. **Photo** (`.profile-photo`, y=109, 152×152): circle, 1px rgba(255,255,255,0.22) ring. Gap 19px.
3. **Name** (`h1.profile-name`, y=280): Inter 27px / 500 / 30px, letter-spacing -0.6px, #e8eaed. Gap 7px.
4. **Role** (`.hero-role`, two lines): 15px #aeb6c0. Gap 13px.
5. **Bio** (`.profile-bio p`, y=381): 15px / 1.66 (24.9px), #aeb6c0, 256px wide. Gap 16px.
6. **Social icons** (y=696): 19px Tabler glyphs, 18px apart, colours #dc267f, #547fef, #fe6100, #f2c25a, #9aa6f0.
7. **News label** (`h2.section-label`, x=517, y=117): 13px / 400, #838b96. The main column starts at x=489 with a 1px rgba(255,255,255,0.12) left rule and 28px padding. Gap 6px plus 8px.
8. **News rows** (y=147–423): 1px top rules, 11px vertical padding; date 13px IBM Plex Mono 500 #ee82b8 in a 72px column; text 15px / 1.55 #aeb6c0, 18px gap. Gap 34px.
9. **Selected publications** (label y=457, first row y=489): aside year 13px mono 500 #ee82b8 and acronym 12.5px mono #838b96; title 15.5px #e8eaed; authors 13.5px #aeb6c0; badges below. The fold falls on the fourth paper.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate | #131519 | `--bg` (dark) | page background, nav tint base |
| Slate Soft | #1b1e23 | `--bg-soft` (dark) | code blocks, post outline and excerpt boxes |
| Text | #e8eaed | `--text` (dark) | nav name, profile name, publication titles, owner's name in author lists |
| Muted | #aeb6c0 | `--text-muted` (dark) | nav links, role, bio, news text, authors, theme icon |
| Faint | #838b96 | `--text-faint` (dark) | section labels, venue acronyms, footer |
| Hairline | rgba(255,255,255,0.12) | `--border` (dark) | nav bottom rule, row rules, main-column left rule, footer rule |
| Strong Hairline | rgba(255,255,255,0.22) | `--border-strong` (dark) | photo ring, theme button border |
| Pink | #ee82b8 | `--accent` (dark) | news dates, publication years, links, focus ring |
| Spotlight Pill | #9bb6f7 on rgba(84,127,239,0.15) | `.badge.blue` | "Spotlight" |
| Award Gold Pill | #f2c25a on rgba(255,176,0,0.22) | `.badge.gold` | "SAC highlights award"; also the X icon |
| Best Paper Pill | #f08bbb on rgba(220,38,127,0.14) | `.badge.magenta` | "Best paper award" |
| Scholar Magenta | #dc267f | `.soc-magenta` | Google Scholar icon |
| GitHub Blue | #547fef | `.soc-blue` | GitHub icon |
| LinkedIn Orange | #fe6100 | `.soc-orange` (dark) | LinkedIn icon |
| Mail Periwinkle | #9aa6f0 | `.soc-navy` (dark) | email icon |
| Light Paper | #ffffff | `--bg` (light) | background in light mode |
| Light Text | #1b1d21 | `--text` (light) | text in light mode |
| Light Muted | #474d56 | `--text-muted` (light) | muted text in light mode |
| Light Faint | #6b727c | `--text-faint` (light) | labels in light mode |
| Raspberry | #c71f73 | `--accent` (light) | dates, years, links in light mode |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans | 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif | Inter 400, 500 | Inter (Google Fonts) |
| Mono | 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace | IBM Plex Mono 400, 500 | JetBrains Mono |
| Icons | tabler-icons 3.24.0 | tabler-icons 400 | Lucide |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Base | `body` | 16px / 400 / 1.7 | #e8eaed |
| Nav name | `.nav-name` | 16px / 500, letter-spacing -0.2px | #e8eaed |
| Nav links | `.nav-links a` | 14px / 400 | #aeb6c0; hover #e8eaed |
| Profile name | `.profile-name` | 27px / 500 / 1.12, letter-spacing -0.6px | #e8eaed |
| Role | `.hero-role` | 15px / 400 | #aeb6c0 |
| Bio | `.profile-bio` | 15px / 400 / 1.66 | #aeb6c0 |
| Section label | `.section-label` | 13px / 400 | #838b96 |
| News date | `.news-date` | IBM Plex Mono 13px / 500 | #ee82b8 |
| News text | `.news-text` | 15px / 400 / 1.55 | #aeb6c0 |
| Pub year | `.pub-year` | IBM Plex Mono 13px / 500 | #ee82b8 |
| Venue acronym | `.pub-acr` | IBM Plex Mono 12.5px / 400 | #838b96 |
| Pub title | `.pub-title` | 15.5px / 400 / 1.42 | #e8eaed; hover #ee82b8 |
| Authors | `.pub-authors` | 13.5px / 400 / 1.5; owner 500 #e8eaed | #aeb6c0 |
| Badge | `.badge` | 12px / 400 / 1.5 | per colour |
| Footer | `.footer` | 13px / 400 | #838b96 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Profile photo | 50% | 0.5px rgba(255,255,255,0.22) | none |
| Theme button | 8px | 0.5px rgba(255,255,255,0.22); hover border #838b96 | none |
| Badge | 8px | none | none |
| News / publication rows | 0 | 0.5px rgba(255,255,255,0.12) top | none |
| Main column | 0 | 0.5px rgba(255,255,255,0.12) left | none |
| Code / outline boxes | 12px | 0.5px rgba(255,255,255,0.12) | none |
| Focus ring | 3px | 2px solid #ee82b8, offset 3px | none |

## Layout Metrics

- **Container**: `.wrap-wide, .nav-inner-wide, .footer-wide { max-width: 1080px }`, padding 0 24px; inner pages use 760px (`--maxw`).
- **Nav**: padding 14px 24px, links gap 20px; sticky with blur.
- **Home grid**: `grid-template-columns: 256px 1fr; column-gap: 28px; padding: 48px 0 0`; profile `position: sticky; top: 84px`; main column `border-left` hairline and `padding-left: 28px` (main text 719px at x=517).
- **Profile**: photo 152px; name margin-top 19px; role margin 7px 0 13px; social margin-top 16px, gap 18px.
- **News**: margin-top 8px; rows `display: flex; gap: 18px; padding: 11px 0`; date column 72px.
- **Publications**: section margin-top 34px; rows padding 14px 0, aside 72px, gap 18px; authors margin-top 3px; award row margin-top 6px.
- **Footer**: max 760px centred, padding 28px 24px 48px, hairline top rule, flex space-between.
- **Page height**: 1,407px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >860px | (100% − 1080px)/2 + 24px | 16px (bio 15px) | 27px | 256px sticky profile + main with left rule |
| 621–860px | 24px | 16px | 24px | single column, gap 28px, padding-top 34px; photo 112px; profile not sticky; no left rule |
| 421–620px | 24px | 16px | 24px | nav links 13.5px, gap 12px, "News" link hidden; news date column 78px |
| ≤420px | 18px in the nav | 16px | 24px | nav name 15px, links 13px, gap 11px |

## Components

- **Glass top bar**: sticky, 88% slate with 8px blur and 140% saturation, hairline bottom border; text links without underlines; square 32px theme toggle with a hairline border and 8px radius.
- **Profile column**: circular 152px photo with a hairline ring, 27px name, two-line role, 15px muted bio, row of five coloured 19px icons that lift 2px on hover (0.12s).
- **Date-keyed row**: flex row with a 72px mono column (pink, weight 500) and the content on the right, 18px gap, 11px (news) or 14px (publications) vertical padding, hairline top rule.
- **Publication aside**: year in pink mono 13px / 500 above a grey mono 12.5px venue acronym ("ICML", "NeurIPS", "ACL").
- **Award pill**: 12px text, padding 2px 9px, 8px radius, no border, a translucent tint of the hue behind a lighter text of the same hue (blue, gold, magenta; orange, navy and grey also defined).
- **Footer**: centred 760px strip, "•‿•" on the left, "Scholar · GitHub · Email" on the right, 13px #838b96.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | yes | sticky blurred bar with theme toggle |
| Portrait | yes | 152px circle |
| Bio | yes | 15px muted paragraph in the sticky sidebar |
| Social links | yes | five coloured icons |
| News | yes | date-keyed rows with pink mono dates |
| Publications | yes | selected papers with year / venue aside |
| Awards | yes | tinted pills under the paper |
| Dark / light toggle | yes | sun button; dark by default |
| Teaser images | absent from the source | none |
| Footer | yes | small centred strip |

## Adapting to Other Content

- **Long publication lists**: use the publications-page pattern already in the CSS: `.year-group` with a 46px pink mono year label (14px / 500) on the left and papers on the right, hairlines between groups.
- **More news**: keep 72px mono dates; for long lists show five and link "See all" in 14px #ee82b8.
- **Talks and service**: CV pattern, a 150px pink mono heading column beside 15px muted list items with `strong` in #e8eaed.
- **Code or BibTeX**: #1b1e23 box with a hairline border, 12px radius, 12.5px mono.
- **Light mode**: swap to #ffffff, #1b1d21, #474d56, #6b727c and accent #c71f73; badge text darkens (for example #a01055 on magenta).

## Do's and Don'ts

- Do keep dates and years in IBM Plex Mono 500 pink; it is the page's signature rhythm.
- Do separate everything with 0.5px hairlines rather than boxes.
- Do keep award pills tinted and borderless, one hue per award type.
- Don't use bold for titles; publication titles are weight 400 and only the owner's name is 500.
- Don't drop the vertical hairline between sidebar and main column on desktop.
- Don't add thumbnails; this is a text-only, list-driven layout.

## Surfaces

Slate #131519 everywhere; the nav is the same colour at 88% with blur; #1b1e23 for code and outline boxes on inner pages; translucent tints behind badges.

## Imagery

One circular selfie-style portrait on a rooftop at dusk; otherwise only coloured line icons.

## Layout

Sticky nav; two-column grid (sticky profile | News and Selected publications); footer. About 1,407px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: background #131519, soft #1b1e23, text #e8eaed, muted #aeb6c0, faint #838b96, hairline rgba(255,255,255,0.12), strong hairline rgba(255,255,255,0.22), accent #ee82b8; pills blue #9bb6f7, gold #f2c25a, magenta #f08bbb.

1. "Build a sticky top bar on #131519 at 88% with backdrop blur 8px and a 0.5px rgba(255,255,255,0.12) bottom rule; inner 1080px with 24px padding; left 'Name' in Inter 16px 500 #e8eaed letter-spacing -0.2px; right 14px #aeb6c0 links 20px apart and a 32px square theme button with an 8px radius and a 0.5px rgba(255,255,255,0.22) border."
2. "Make a home grid 256px + 1fr with 28px gap and 48px top padding: a sticky profile (top 84px) with a 152px round photo ringed by 0.5px rgba(255,255,255,0.22), 27px Inter 500 name with -0.6px tracking, 15px #aeb6c0 role and bio, and 19px coloured icons 18px apart; the main column has a 0.5px rgba(255,255,255,0.12) left border and 28px padding."
3. "Make date-keyed rows: flex with 18px gap and a hairline top rule; left a 72px column in IBM Plex Mono 13px 500 #ee82b8 (year) with a 12.5px #838b96 venue acronym beneath; right a 15.5px #e8eaed title, 13.5px #aeb6c0 authors with the owner in 500 #e8eaed, and a pill (12px, padding 2px 9px, radius 8px) such as #f08bbb on rgba(220,38,127,0.14) for 'Best paper award'."

## Similar Pages

- Minimal dark researcher homepages with a sticky profile sidebar.
- Linear-style personal sites using Inter with monospace metadata.

## Quick Start

```css
:root, [data-theme="dark"] {
  --bg: #131519; --bg-soft: #1b1e23; --text: #e8eaed; --text-muted: #aeb6c0; --text-faint: #838b96;
  --border: rgba(255,255,255,0.12); --border-strong: rgba(255,255,255,0.22); --accent: #ee82b8;
  --font-sans: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'IBM Plex Mono', ui-monospace, Menlo, monospace;
}
[data-theme="light"] { --bg: #ffffff; --text: #1b1d21; --text-muted: #474d56; --text-faint: #6b727c; --accent: #c71f73; }
body { margin: 0; background: var(--bg); color: var(--text); font: 16px/1.7 var(--font-sans); }
a { color: var(--accent); text-decoration: none; }
.home-grid { display: grid; grid-template-columns: 256px 1fr; column-gap: 28px; padding-top: 48px; }
.home-main { border-left: 0.5px solid var(--border); padding-left: 28px; }
.news-item, .pub { display: flex; gap: 18px; border-top: 0.5px solid var(--border); }
.news-date, .pub-year { flex: 0 0 72px; font: 500 13px var(--font-mono); color: var(--accent); }
.badge { font-size: 12px; padding: 2px 9px; border-radius: 8px; }
```

## Provenance

- **URL**: https://tpimentelms.github.io/
- **Person**: Tiago Pimentel, NLP, information theory and interpretability.
- **Award**: ACL 2024 Best Paper, "Causal Estimation of Memorisation Profiles" (last author). https://2024.aclweb.org/program/best_papers/
- **Selection reason**: award rule (first or last author); chosen for the crisp dark two-column layout with a sticky profile column, date-keyed news and tagged award pills.
- **Template credit**: the stylesheet header says it is a self-contained redesign that no longer uses Minimal Mistakes.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `redesign.css` and the inline theme script read directly, on 2026-10-28.
