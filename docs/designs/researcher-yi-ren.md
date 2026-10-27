# Yi Ren Navy Rail — Style Reference

> A navy chart-room rail beside a clean logbook of topic-coded papers.

**Theme:** light

Measurements come from the static HTML, its inline `<style>` block (the author's overrides) and the linked `w3.css`. W3.CSS framework colors (its `w3-black`, `w3-grey` and button palette) are excluded except where the markup uses them. All hex values below appear in the inline style block or in `<font color>` attributes. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Yi (Joshua) Ren's page is the W3.CSS fixed-sidebar portfolio layout, restyled. The body is `w3-content` capped at 1000px. A 175px fixed left sidebar in deep navy `#0b2545` shows "YI REN" in bold and a scroll-synced section nav (Home, News, Topics, Talks, Publications) in pale steel `#c3cfdd`, with a 3px left marker bar that turns `#4d9bf0` on the active item. The main column (margin-left 175px) opens with a square photo (60% width, max 240px, 14px radius, `0 6px 20px rgba(0,0,0,.18)` shadow) that swaps to a second photo on hover, the h1 "Yi (Joshua) Ren" at 2.4em, and a bio paragraph (Oxford OATML postdoc, UBC Ph.D.). Contact and affiliation links are pills underlined in a random hue reshuffled on every load (`hsl(h, 58%, 55%)`). Sections use inline-block h2 headings underlined 3px navy. News and Talks run on a timeline rule (3px `#c9d1d9` left border, bold navy dates). Publications have topic filter buttons (All, Learning dynamics, RL, Iterated learning, Other) with colored dots, starred featured papers, and venue names as rounded badges.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Page White | `#ffffff` | `--bg` | Body background |
| Body Ink | `#222222` | `--text` | Body text |
| Harbor Navy | `#0b2545` | `--navy` | Sidebar, mobile header, h2 underline, dates, active filter |
| Steel Nav | `#c3cfdd` | `--nav-text` | Sidebar links |
| Active Marker | `#4d9bf0` | `--nav-active` | 3px bar on active nav item |
| Link Blue | `#1772d0` | `--link` | All content links; dynamics topic |
| Hover Amber | `#f09228` | `--link-hover` | Content link hover |
| Star Gold | `#e0a92a` | `--star` | Featured-paper star and note |
| Rule Grey | `#c9d1d9` | `--rule` | Timeline and publication left borders |
| Pill Line | `#d6dde6` | `--pill-line` | Filter button border, home link underline default |
| Venue Wash | `#eaf1fa` | `--venue-bg` | Default venue badge |
| Conference Wash | `#cfdff3` | `--venue-conf` | Conference venue badge |
| Workshop Wash | `#f0f4f9` | `--venue-workshop` | Workshop badge (text `#4a6283`) |
| Preprint Sand | `#efede8` | `--venue-preprint` | Preprint badge (text `#6b6258`) |
| RL Teal | `#0f9d8f` | `--topic-rl` | RL topic border and dot |
| IL Violet | `#7b5ea7` | `--topic-il` | Iterated learning topic |
| Other Slate | `#9aa5b1` | `--topic-other` | Other topic |
| Filter Ink | `#44515f` | `--filter-text` | Filter button text |
| Note Grey | `#6b7684` | `--note` | `.pub-note` text |
| Accent Fonts | `#0492C2`, `#1338BE`, `#48AAAD`, `#DC143C` | (font tags) | Inline colored phrases in the bio |

## Tokens — Typography

- **Family:** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif` for body, all headings, `.w3-wide` and sidebar links. Substitute: `Inter`.
- **Mono:** `Consolas` / monospace (W3.CSS code).
- **Weights:** 400 body, 700 dates, venue badges and filter buttons; bold sidebar name.

| Role | Size | Weight | Notes |
|---|---|---|---|
| h1 name | 2.4em (overrides W3 36px) | 400 (W3 default, inferred) | margin-top 22px |
| h2 section | 30px (W3.CSS h2) | 400 | inline-block, 3px navy underline, 6px padding below |
| Topic h3 | 19px | 400 | Navy |
| Body | 15px (W3.CSS base) | 400 | line-height 1.5 |
| Home pill link | 14px | 400 | `#3d4753`, 2px colored underline |
| Filter button | 13px | 700 | Pill |
| Pub note | 12px | 400 | Grey |
| Venue badge | 0.9em | 700 | Navy text |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Profile photo | 14px |
| Filter buttons | 16px |
| Venue badge | 10px |
| Topic dots | 50% |

- **Shadows:** profile photo `0 6px 20px rgba(0,0,0,0.18)`; W3.CSS card shadows exist but are not used on content.
- **Layout max-width:** body 1000px (`w3-content`), sidebar 175px fixed, main `margin-left: 175px`; publication tables capped at 600px.
- **List rhythm:** publication items padding `2px 0 2px 28px`, 18px apart; timeline items `2px 0 2px 14px`, 14px apart.

## Components

- **Sidebar nav.** Navy panel, links `#c3cfdd`; hover background `rgba(255,255,255,0.08)` and white text; active `rgba(255,255,255,0.10)` with a `#4d9bf0` 3px left bar; nav separated by a `rgba(255,255,255,0.14)` top rule.
- **Home photo.** Square crop (aspect-ratio 1, `object-fit: cover`), 14px radius, deep shadow, hover image swap.
- **Rainbow link pills.** Inline links with a 2px bottom border colored by evenly spaced random hues (58% saturation, 55% lightness), hover to `#1772d0`.
- **Section heading.** Inline-block h2 with a 3px `#0b2545` underline, 20px bottom margin.
- **Timeline list.** No bullets, 3px `#c9d1d9` left rule, bold navy date then text.
- **Publication item.** Left border colored by `data-topic`, optional gold star, venue in a `<em>` rounded badge (`#eaf1fa`, 1px 8px padding).
- **Topic filter.** White pill buttons with 1px `#d6dde6` border and a colored 8px dot; hover blue; active fills navy with white text.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | Square shadowed photo with hover swap, h1 name, rainbow pills |
| News | Yes | Timeline list |
| Research topics | Yes (Learning dynamics, forgetting, iterated learning) | Navy h3 sub-headings |
| Talks | Yes | Timeline list, YouTube links |
| Publication list | Yes, topic-filterable, no thumbnails | Colored left borders, venue badges, stars |
| Notes / TA | Yes | List |
| Awards | No separate section | |
| Contact | Pills under the name | |

## Do's and Don'ts

- Do anchor the page with a narrow navy rail and keep the content on white.
- Do color-code publications by topic on the left border and repeat the color in the filter dots.
- Do keep one link blue and one amber hover across all content.
- Don't use W3.CSS default black for the sidebar; it is overridden to `#0b2545`.
- Don't fill publication rows with backgrounds; the colored rule alone carries the topic.

## Surfaces

White main area and a navy sidebar; small tinted badge washes (`#eaf1fa`, `#cfdff3`, `#f0f4f9`, `#efede8`).

## Imagery

One profile photo with a hover swap, plus a StatCounter pixel. No paper thumbnails.

## Layout

W3.CSS fixed sidebar (`w3-sidebar w3-collapse`, 175px) and a 1000px max content column; on small screens the sidebar becomes a toggled overlay under a navy top header (margin-top 83px for content).

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#222222`, navy `#0b2545`, link `#1772d0`, hover `#f09228`, rule `#c9d1d9`, star `#e0a92a`, topics `#1772d0` / `#0f9d8f` / `#7b5ea7` / `#9aa5b1`.

1. "Build a 175px fixed sidebar in `#0b2545` with links in `#c3cfdd`; the active link gets a `rgba(255,255,255,.10)` background and a 3px `#4d9bf0` left bar."
2. "List publications with a 3px left border colored by topic, padding-left 28px, a gold ★ for featured items, and the venue as a bold navy badge on `#eaf1fa` with 10px radius."
3. "Add topic filter pills: white, 1px `#d6dde6` border, 16px radius, 13px/700 `#44515f` text with an 8px colored dot; active state navy fill with white text."

## Similar Pages

W3Schools' sidebar portfolio template adopted by many ML students; the Liwei Jiang page in this batch shares the navy plus gold accent logic.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #222222;
  --navy: #0b2545;
  --nav-text: #c3cfdd;
  --nav-active: #4d9bf0;
  --link: #1772d0;
  --link-hover: #f09228;
  --rule: #c9d1d9;
  --star: #e0a92a;
  --topic-dynamics: #1772d0;
  --topic-rl: #0f9d8f;
  --topic-il: #7b5ea7;
  --topic-other: #9aa5b1;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, "PingFang SC", sans-serif;
  --sidebar: 175px;
  --content: 1000px;
}
```

## Provenance

- **URL:** https://joshua-ren.github.io/
- **Person:** Yi (Joshua) Ren, learning dynamics and LLM finetuning
- **Venue / award:** ICLR 2025 Outstanding Paper (Learning Dynamics of LLM Finetuning, first author)
- **Selection reason:** Rule B, first author of an ICLR 2025 Outstanding Paper (https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/); homepage from the GitHub profile of the paper's code account Joshua-Ren.
- **Template credit:** W3.CSS sidebar layout (`w3-content`, `w3-sidebar`, `w3_open()` / `w3_close()` functions); no footer credit.
- **Measurement method:** `extract_style.py` on HTML plus `w3.css`, then the inline style block was read in full for roles. W3.CSS base sizes (15px body, 30px h2, 24px h3) were read from `w3.css`. The rendered page was not viewed.
