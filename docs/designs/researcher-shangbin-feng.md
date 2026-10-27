# Shangbin Feng — Style Reference

> A research statement that reads like a well-edited op-ed: system sans in one narrow column, a diagram tucked into the argument, and four blue verbs carrying the agenda.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the site's `/assets/css/site.css` (its own five `:root` tokens) and markup read directly. No web font is loaded (`fonts_loaded` is empty): the stack starts with -apple-system and BlinkMacSystemFont, so it renders in San Francisco on Apple devices and, in this Windows render, in Segoe UI.

## Overview

A single 720px text column on white, centred in a 760px `main` with 20px padding. The header is a flex row: on the left "Shangbin Feng" in 34px/600 near-black #1a1a1a with slight negative tracking, a link line (CV · Email · Scholar · GitHub · X) in blue #1f4fb0 separated by grey middots, a pale #f5f7fb callout with a 3px blue left bar announcing the job market, and a two-line bio; on the right a 200px square portrait with no rounding. Sections open with 19px/600 headings over a full-width 1px #e3e3e3 rule. The research section is the centrepiece: a 360px concept figure floats right beside the first paragraphs, bold phrases mark the key terms, and four paragraphs begin with a bold blue stage verb (Train, Align, Adapt, Deploy) followed by linked paper names in parentheses. Honors are a short bulleted list; selected publications are a numbered-style plain list at 16px with a bold title line, authors with the owner bold and underlined, a grey venue, red #b3261e award notes, and small blue "paper" and "code" links. A two-column mentee list and a grey "Last updated" footer close the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 78.7% (page), #c5c6c7 5.9% and #e6e8e9 3.4% (anti-aliased text and the heading rule), #9b8e80 4.1% (portrait), #f1f5f5 3.6% (the figure's pale teal panel), #f9fafb 2.8% (the #f5f7fb callout). Blue #1f4fb0 covers under 1%.

Anatomy in DOM order (desktop 1440px; `main` 760px at x=340, padding 48px 20px 40px, text x=360–1080):

1. **Name** (`header .who h1`, y=48): 34px/600, line-height 1.6 (54.4px), letter-spacing -0.34px, #1a1a1a. Gap 4px.
2. **Link line** (`p.links`, y=106): 17px/400 #1f4fb0 links; each link after the first is preceded by a #5f6368 "·" with 9px side margins. Gap 18px.
3. **Market callout** (`p.market`, y=152, 488px wide): 17px/400 #1a1a1a on #f5f7fb, padding 10px 14px, border-left 3px #1f4fb0, no radius. Gap 14px.
4. **Bio** (`p`, y=213): 17px/400, line-height 1.6, #1a1a1a, link #1f4fb0.
5. **Portrait** (`header img`, x=880, y=54): 200×200, object-fit cover, margin-top 6px, no radius; 32px gap from the text column. Header ends at y=308; gap 36px.
6. **Section heading** (`h2`, y=344): 19px/600 #1a1a1a, padding-bottom 6px, border-bottom 1px #e3e3e3 across 720px. Gap 12px.
7. **Concept figure** (`figure.side`, floated right, x=720, y=398): 360px wide, margin 4px 0 10px 24px, image only, no caption or border.
8. **Research paragraphs** (`p`, y=394 onward): 17px/1.6 #1a1a1a, wrapping at 336px beside the figure, with 600-weight key terms; the "Train" stage paragraph starts at y=804 with a `span.stage` in 600 #1f4fb0.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Text | #1a1a1a | --text | name, headings, body, publication titles |
| Link Blue | #1f4fb0 | --link | links, stage verbs (Train / Align / Adapt / Deploy), callout bar |
| Muted | #5f6368 | --muted | link-line middots, venue lines, note line, mentee destinations, footer |
| Rule | #e3e3e3 | --rule | section heading underline, footer top border |
| Tint | #f5f7fb | --tint | job-market callout background |
| Author Grey | #333333 | (literal) | author lines |
| Award Red | #b3261e | (literal) | award and impact notes in publications (e.g. "Senior Area Chair Award, Oral") |
| White | #ffffff | (literal) | page |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif | no web font; system UI face (Segoe UI in this Windows render, San Francisco on macOS) | Inter |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1` | 34px / 600 / 1.6, letter-spacing -0.01em | #1a1a1a |
| Section heading | `h2` | 19px / 600 / 1.6, rule below | #1a1a1a |
| Body | `body`, `p` | 17px / 400 / 1.6 | #1a1a1a |
| Key term | `strong` | 17px / 700 | #1a1a1a |
| Stage verb | `.stage` | 17px / 600 | #1f4fb0 |
| Link line | `.links a` | 17px / 400 | #1f4fb0 |
| Publication item | `ol.pubs li` | 16px / 400 / 1.5 | #1a1a1a |
| Publication title | `.title` | 16px / 600 | #1a1a1a |
| Authors | `.authors` | 16px / 400; own name `.me` 600 underlined (offset 2px) | #333333 |
| Venue | `.venue` | 16px / 400 | #5f6368 |
| Award / impact | `.award`, `.impact` | 16px / 600 | #b3261e |
| Paper / code links | `.pubs a` | 15px / 400, margin-right 8px | #1f4fb0 |
| Note | `.note` | 15px / 400 | #5f6368 |
| Mentees | `ul.mentees` | 16px; destination `.now` 14px | #1a1a1a; #5f6368 |
| Footer | `footer` | 14px / 400 | #5f6368 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 0 | none | none |
| Market callout | 0 | left 3px #1f4fb0 | none |
| Section heading | 0 | bottom 1px #e3e3e3 | none |
| Concept figure | 0 | none | none |
| Footer | 0 | top 1px #e3e3e3 | none |

## Layout Metrics

- **Column**: `main` max-width 760px, margin 0 auto, padding 48px 20px 40px; text 720px wide (x=360–1080 at 1440).
- **Header**: flex, gap 32px, align flex-start; text column flex 1 (488px), portrait 200×200.
- **Paragraphs**: margin 0 0 14px.
- **Section headings**: margin 36px 0 12px, padding-bottom 6px; `h2 { clear: both }` ends any float.
- **Side figure**: float right, 360px wide, margin 4px 0 10px 24px; full figures (`figure`) margin 22px 0 at 100%.
- **Lists**: pillars no bullets, 8px apart; honors bullets with 20px indent, 3px apart; publications no markers, 14px apart; mentees in 2 columns with a 32px gap.
- **Footer**: margin-top 40px, padding-top 12px. Page height 3,558px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >600px | auto margins around 760px, 20px padding | 17px | 34px | portrait right of the name block; figure floats right at 360px |
| ≤600px | 16px (main padding 28px 16px 32px) | 16px | 28px | header becomes column-reverse (140px portrait above the name); figure unfloats to 100% (max 380px) centred; mentees one column |

## Components

- **Link line**: plain #1f4fb0 text links on one line, separated by "·" in #5f6368 with 9px margins inserted by `a + a::before`; underline on hover only.
- **Callout bar** (`p.market`): #f5f7fb fill, 3px #1f4fb0 left border, padding 10px 14px, square corners, normal 17px text.
- **Section heading**: 19px/600 #1a1a1a with a 1px #e3e3e3 rule 6px below, 36px above.
- **Floated concept figure**: 360px image floated right with 24px left margin, no frame or caption, so the opening paragraphs wrap beside it.
- **Stage paragraph**: opens with a 600-weight #1f4fb0 verb (`span.stage`), then a sentence, then linked paper names in parentheses separated by commas.
- **Publication entry** (`ol.pubs li`): line 1 a 600 title; line 2 authors in #333333 with the owner 600 and underlined; line 3 venue in #5f6368, an optional 600 #b3261e award or impact note (outlet names italic in the same red), then 15px #1f4fb0 "paper" and "code" links kept together with `white-space: nowrap`.
- **Mentee list**: two CSS columns of names, each followed by a 14px #5f6368 "→ destination".
- **Footer**: 14px #5f6368 "Last updated October 2026." above a 1px #e3e3e3 rule.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name, links, bio, portrait | yes | flex header with square photo |
| Job-market notice | yes | tinted callout with a blue left bar |
| Research narrative with figure | yes | floated concept diagram and bold blue stage verbs |
| Honors and awards | yes | short bulleted list |
| Selected publications | yes | plain text list with red award notes |
| Mentoring | yes | two-column list with destinations |
| News | absent from the source | — |
| Navigation bar | absent from the source | — |
| Footer | yes | last-updated line on a hairline |

## Adapting to Other Content

- **Long publication lists**: keep the three-line entry and the 14px spacing; add year subheadings in the 19px/600 heading style only when the list exceeds about 20 items, and link the rest via the `.note` line.
- **News**: add a section with a plain list where each item starts with a 600-weight date; do not tint it, the callout bar is reserved for one announcement.
- **More research threads**: add stage paragraphs, each with one blue 600 verb; keep at most one floated figure per section.
- **Wide figures**: use a plain `figure` at 100% of the 720px column with 22px vertical margins.
- **Talks**: reuse the publication entry with venue and date on the grey line.

## Do's and Don'ts

- Do keep a single 720px column and let the figure float inside it.
- Do use #1f4fb0 for both links and the four stage verbs, and #b3261e only for awards.
- Do keep corners square everywhere (portrait, callout, figure).
- Don't add cards, backgrounds or shadows to publications; they are text.
- Don't load a web font; the system UI stack is part of the look.
- Don't use more than one tinted callout.

## Surfaces

All white, with one #f5f7fb callout and hairline #e3e3e3 rules under headings and above the footer.

## Imagery

A square headshot and one concept diagram (closed vs open AI against modular AI through participation, with coloured cubes and people icons on a pale teal panel). No thumbnails in the publication list.

## Layout

Header, research narrative, honors, selected publications, mentoring, footer, all in one column. About 3,558px tall at 1440.

## Agent Prompt Guide

Quick colors: text #1a1a1a, links and stage verbs #1f4fb0, muted #5f6368, authors #333333, award #b3261e, rule #e3e3e3, callout #f5f7fb, page #ffffff.

1. "Build a header: flex row with 32px gap inside a 760px main (padding 48px 20px 40px); left column with the name in the system UI stack at 34px/600, letter-spacing -0.01em, #1a1a1a; a link line in 17px #1f4fb0 with '·' separators in #5f6368 and 9px margins; a callout p with background #f5f7fb, border-left 3px solid #1f4fb0, padding 10px 14px; right a 200×200 square portrait, object-fit cover."
2. "Make a research section: h2 19px/600 #1a1a1a with padding-bottom 6px and border-bottom 1px solid #e3e3e3, margin 36px 0 12px; a 360px figure floated right with margin 4px 0 10px 24px; paragraphs 17px/1.6 #1a1a1a with 700 key terms; stage paragraphs that open with a 600-weight #1f4fb0 verb."
3. "Create a publication list: no markers, 16px/1.5, 14px between items; title 600 #1a1a1a; authors #333333 with the owner 600 and underlined (offset 2px); venue #5f6368, an optional 600 #b3261e award note, then 15px #1f4fb0 'paper' and 'code' links with 8px right margin."

## Similar Pages

- Single-column NLP PhD homepages written as a research statement rather than a CV.
- System-font academic pages with a floated concept figure.

## Quick Start

```css
:root {
  --text: #1a1a1a;
  --muted: #5f6368;
  --link: #1f4fb0;
  --rule: #e3e3e3;
  --tint: #f5f7fb;
  --award: #b3261e;
}
body { margin: 0; background: #ffffff; color: var(--text); font: 400 17px/1.6 -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif; }
main { max-width: 760px; margin: 0 auto; padding: 48px 20px 40px; }
a { color: var(--link); text-decoration: none; }
h2 { font-size: 19px; font-weight: 600; margin: 36px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--rule); clear: both; }
.market { background: var(--tint); border-left: 3px solid var(--link); padding: 10px 14px; }
.stage { font-weight: 600; color: var(--link); }
```

## Provenance

- **URL**: https://bunsenfeng.github.io/
- **Person**: Shangbin Feng (NLP, multi-LLM collaboration, social NLP).
- **Venue / award**: ACL 2023 Best Paper, "From Pretraining Data to Language Models to Downstream Tasks".
- **Selection reason**: award rule (first/last author). https://2023.aclweb.org/program/best_papers/
- **Template credit**: none; hand-written HTML with a short custom stylesheet.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `/assets/css/site.css` and the markup read directly, on 2026-10-28.
