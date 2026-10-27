# Yaodong Yang — Style Reference

> A university press catalogue printed on warm linen paper.

**Theme:** light (with a dark ink footer)

Measurements are normalized from the static HTML and the bundled Astro stylesheet (`/_astro/venue.BgGY0H-3.css`); roles are interpreted. Tokens below come from the site's own `:root` block. The default page is Chinese (`lang="zh-CN"`) with an `/en/` toggle in the nav.

## Overview

The most designed page in this batch. Built with Astro 6, it sets a cream paper background (#f5f1e8) dusted with a 24px dot grid, a sticky translucent nav with a backdrop blur, and an editorial type trio: Fraunces serif for display, Inter (with Noto Sans SC for Chinese) for text, and JetBrains Mono for every piece of metadata. Peking University cardinal (#8c1515) is the single brand accent; five muted topic colors (navy, moss, umber, ochre, plum) tag research areas across news, publications and recruiting cards. Section heads are huge serif words (clamp 40 to 64px) led by a small red square and closed by a hairline rule. Publications are a three-column grid with a 64px square "mini-thumb" tile printed with the venue acronym and tinted by topic, then title, authors and a mono meta row with venue chip and oral or spotlight badges.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Linen | #f5f1e8 | `--bg` | Page background (with dot grid) |
| Linen Shade | #ebe5d4 | `--bg-2` | Neutral mini-thumb fill |
| Card White | #ffffff | `--card` | Cards and role chips |
| Press Ink | #0a0a0a | `--ink` | Headings and titles; footer background |
| Ink Two | #1f1f1f | `--ink-2` | Body copy, nav links |
| Pencil Grey | #6b6b6b | `--muted` | Authors, sub-labels, venue chip fill |
| Rule | #d9d4c5 | `--rule` | Section rules, nav border, mini-thumb border |
| Soft Rule | #e5e1d4 | `--rule-soft` | Divider between publication rows |
| PKU Cardinal | #8c1515 | `--pku` / `--accent` | Brand accent: section square, CTA, oral badge, corresponding-author mark |
| Cardinal Dusk | #5e0e0e | `--pku-dark` | CTA hover |
| Cardinal Blush | #f1dada | `--pku-soft` | Featured mini-thumb |
| Old Gold | #b8860b | `--gold` | Spotlight badge |
| Topic Navy | #1e3a5f | topic 02 | Embodied RL tag, talk tag |
| Topic Moss | #2d5016 | topic 03 | Multi-agent RL tag |
| Topic Umber | #6b4423 | topic 04 | Agentic RL tag |
| Topic Ochre | #6b5014 | ai4sci | AI for science tag, preprint badge text |
| Topic Plum | #4a2c5a | topic 05 | Fifth research topic accent |
| Nav Glass | #f5f1e8e0 | none | Sticky nav fill with `backdrop-filter: saturate(180%) blur(14px)` |

## Tokens — Typography

- **Display:** Fraunces (opsz 9 to 144, 400 to 600, italic 400/500), fallback Georgia. Substitute: Newsreader or Source Serif 4.
- **Text:** Inter 300 to 800 with Noto Sans SC 300 to 700, fallback `system-ui, sans-serif`.
- **Mono:** JetBrains Mono 400 to 600, fallback `ui-monospace`. Used 79 times in the CSS: chips, badges, meta rows, footer, nav CTA.
- **Weights:** 500 and 600 dominate; 700 for strong marks; Fraunces h1 at 400.

| Level | Element | Size | Line height | Notes |
|---|---|---|---|---|
| Hero name | h1 | clamp(40px, 5.2vw, 76px) | 1.02 | Fraunces 400, letter-spacing -.03em; `.cn` sub-line at .28em Inter 300 |
| Section | `.sec-head h2` | clamp(40px, 5vw, 64px) | 1 | Fraunces 500, -.035em, red 10px square before |
| Card name | `.card-name` | 1.25rem | 1.1 | Fraunces 600 |
| Paper title | `.pub .title` | 1.05rem | 1.4 | Inter 600 |
| Body | body | 16px | 1.6 | html at .98rem |
| Authors | `.pub .authors` | .88rem | 1.5 | #6b6b6b, own name bold with dotted cardinal underline |
| Meta | `.pub .meta-row`, chips | .72rem | 1 | JetBrains Mono |
| Micro label | badges, `.card-sub` | .66 to .68rem | | uppercase, letter-spacing .05 to .14em |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Hairline | 2px | small tags |
| Tight | 3px | Nav CTA, nav toggle |
| Small | 4px | misc |
| Logo card | 8px | Partner logo tiles |
| Pill | 999px | rounded chips |
| Circle | 50% | Portrait frame, avatars |
| Square | 0 | Venue chip, badges, mini-thumbs, role chips |

- **Shadows:** `0 12px 28px -16px #0000002e` and `0 20px 40px -20px #00000026` on cards; red glow `0 4px 14px -6px #8c151573` on the nav CTA.
- **Layout max-width:** `.wrap` 1140px with 40px side padding (20px on phones); `.wrap-sm` 980px; prose blocks 680 to 720px.
- **Rhythm:** section head `margin-bottom: 56px; padding-bottom: 20px`; publication rows `padding: 22px 0; gap: 24px`.

## Components

- **Sticky nav.** Role: site navigation and language switch. 68px tall (56px on phones), translucent linen with blur, 1px rule below. Links 0.88rem with an animated 1px cardinal underline on hover; a mono uppercase CTA in solid cardinal with 3px radius.
- **Role chip.** Role: positions in the hero. JetBrains Mono .72rem, 1px ink border, white fill, 6px 11px padding; `.red` variant is solid cardinal; linked chips invert to ink on hover.
- **Key-value badges.** Role: hero facts. Mono .72rem; key uppercase in muted grey, value in ink or cardinal; row sits above a 1px rule.
- **Section head.** Role: h2 with Chinese subtitle. Fraunces display word, 10px cardinal square before it, muted `.cn` subtitle at half size, hairline bottom rule.
- **Publication row.** Role: one paper. Grid `80px 1fr auto` (48px on phones); 64px mini-thumb square with venue acronym in mono, tinted by topic; title in Inter 600 with corresponding-author mark in cardinal; authors in muted grey; mono meta row with venue chip (white on #6b6b6b, 3px 9px) and badges (oral cardinal, spotlight gold, preprint ochre on #efe6d0).
- **Partner card.** Role: industry links. Logo tile 128 by 76px on white at 70% opacity with 8px radius, serif name, mono uppercase sub-line, warm gradient glow on hover.
- **Footer.** Role: contact. Full-bleed ink (#0a0a0a) with linen text, 80px top and 60px bottom padding, mono counters.

## Page Modules

- **Title/author block:** serif name with Chinese and English, role chips, key-value badges, circular portrait in a dark gradient frame.
- **News:** card grid with cover images and colored tags (talk tag in navy).
- **Research directions:** five topic cards, each with its own accent color.
- **Awards:** dedicated section.
- **Team / students:** "团队培养" section.
- **Publication list:** grouped list with venue-acronym tiles instead of thumbnails, venue chips, oral and spotlight badges; links to arXiv, code, datasets.
- **Academic service and CV timeline:** text sections.
- **Recruiting:** "欢迎一起钻研" section with direction cards (top border in topic color) and a getting-started guide.
- **Contact:** dark footer.
- **BibTeX, teaser video, interactive demos:** not present on the home page.

## Do's and Don'ts

- Do keep one brand red and use the five topic colors only as tags and tile tints.
- Do set all metadata (venues, dates, counts, chips) in JetBrains Mono at about .7rem.
- Do lead every section with a big Fraunces word and the small red square.
- Don't round the venue chips or badges; they are square-cornered print labels.
- Don't use photos as paper thumbnails; the tile with the venue acronym is the system.
- Don't drop the dot-grid texture or the linen tone; a white background loses the catalogue feel.

## Surfaces

Linen page with a faint 1px dot grid every 24px; white cards with long soft shadows; translucent blurred nav; one solid ink footer.

## Imagery

Circular portrait, PKU logo mark in the nav, partner logos in rounded tiles, press and news cover images. Publication "thumbnails" are typographic tiles, not images.

## Layout

1140px centered wrapper with grids that step from four columns to two to one. Publication rows are three-column grids that drop the trailing column on phones. Footer uses a `1.5fr 1fr 1fr 1fr` grid.

## Agent Prompt Guide

**Quick colors:** bg #f5f1e8, ink #0a0a0a, body #1f1f1f, muted #6b6b6b, rule #d9d4c5, accent #8c1515, gold #b8860b, topics #1e3a5f #2d5016 #6b4423 #6b5014 #4a2c5a.

1. "Build a section head: Fraunces 500 at clamp(40px, 5vw, 64px), letter-spacing -.035em, preceded by a 10px #8c1515 square; a muted Inter subtitle at half size beside it; 1px #d9d4c5 rule below; 56px space after."
2. "Create a publication row: grid 80px / 1fr / auto with 24px gap and a #e5e1d4 bottom rule. Left a 64px square tile with the venue acronym in JetBrains Mono .68rem 600, tinted by topic (e.g. #dce3ee bg with #1e3a5f text). Middle: Inter 600 1.05rem title, .88rem #6b6b6b authors with the owner bolded over a dotted red underline, and a mono .72rem row with a square venue chip (white on #6b6b6b) and an uppercase 'ORAL' badge on #8c1515."
3. "Make a sticky nav: 68px tall, background #f5f1e8e0 with backdrop blur 14px, 1px #d9d4c5 bottom rule, links .88rem #1f1f1f with a sliding 1px #8c1515 underline, and a mono uppercase CTA button in #8c1515 with 3px radius and a red glow shadow."

## Similar Pages

- [Idan Attias](https://www.idanattias.com/) for another custom component-based researcher page with filters and badges.
- [Daniel Roy](https://danroy.org/) for an older take on a display-name header.

## Quick Start

```css
:root {
  --bg: #f5f1e8; --bg-2: #ebe5d4; --card: #ffffff;
  --ink: #0a0a0a; --ink-2: #1f1f1f; --muted: #6b6b6b;
  --rule: #d9d4c5; --rule-soft: #e5e1d4;
  --pku: #8c1515; --pku-dark: #5e0e0e; --pku-soft: #f1dada; --gold: #b8860b;
  --sans: "Inter", "Noto Sans SC", system-ui, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, monospace;
  --serif: "Fraunces", Georgia, serif;
}
body {
  background: var(--bg); color: var(--ink); font: 16px/1.6 var(--sans);
  background-image: radial-gradient(circle at 1px 1px, rgba(10,10,10,.035) 1px, transparent 0);
  background-size: 24px 24px;
}
.wrap { max-width: 1140px; margin: 0 auto; padding: 0 40px; }
h1 { font-family: var(--serif); font-weight: 400; font-size: clamp(40px, 5.2vw, 76px); line-height: 1.02; letter-spacing: -.03em; }
.pub .venue { font-family: var(--mono); font-size: .72rem; color: #fff; background: var(--muted); padding: 3px 9px; }
```

## Provenance

- **URL:** https://yangyaodong.com/
- **Venue/award:** ACL 2025 Best Paper (last author of "Language Models Resist Alignment"), per https://2025.aclweb.org/program/awards/
- **Selection reason:** Rule B.
- **Template credit:** none; custom Astro v6.1.9 site (generator meta tag).
- **Measurement method:** tokens copied from the site's `:root` and component rules in the bundled CSS, plus the static HTML, via `extract_style.py` and curl. The page was not viewed in a browser, so hover effects and the dark footer's look are described from CSS. Only the Chinese default page was measured; `/en/` was not checked.
