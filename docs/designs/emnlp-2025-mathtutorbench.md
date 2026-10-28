# MathTutorBench — Style Reference

> A university report card in ETH navy: petrol eyebrows, a sortable gradebook, and every best mark inked in bold blue.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, and the single inline `<style>` block of `index.html`, which declares the ETH Zurich corporate palette as custom properties. No web font loads (`fonts_loaded` is empty); the system UI stack renders (Segoe UI in the Windows render). Button borders are declared 1.5px but compute to 1px at device pixel ratio 1.

## Overview

A white, single-column benchmark site with a 49px sticky top bar (navy wordmark "MathTutorBench" with "Bench" in a lighter blue, a grey affiliation line, six section links on the right). The centred hero is pure type: a 48px / 800 navy title, a 19.2px soft-ink subtitle, a petrol venue line and five pill buttons (two filled ETH blue, three outlined). Below, every section is a 1020px block separated by a 1px #e4e7ec rule and opens with a tracked uppercase petrol eyebrow (RESULTS, FINDINGS, BENCHMARK, USAGE, CONTRIBUTE, PEOPLE, REFERENCE) above an 800-weight heading. The leaderboard is a scrollable, sortable table in a rounded frame with a pale-blue header, a sticky model column, NEW tags in petrol and bold-blue best scores. Findings sit in two columns with bordered figures; How it works uses pale-blue feature tiles; Quick Start uses dark navy code blocks and a petrol callout.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 82.3%, pale blue #ecf1f7 4.4% (table header), light grey #d7dde2 4.0% (rules and table lines), #fcfdfd 3.0%, slate #7a94ae 2.7% (antialiased navy text and filled buttons), #f8f9f9 2.2%, #feffff 1.2%, #fffffe 0.1%.

Anatomy in DOM order (desktop 1440px):

1. **Sticky top bar** (`nav.topbar`, 0–49px): white with a 1px #e4e7ec bottom border; inner row max 1020px (x=210), padding 10.4px 20px, flex, baseline aligned, gap 16px. Wordmark 16.32px / 800 #08407e, letter-spacing -0.16px, "Bench" in #215caf; affiliation "ETH Zurich · ETH AI Center" 12.48px #6f6f6f; links (Leaderboard … Citation) 13.76px / 500 #4a4a4a, gap 17.6px, pushed right.
2. **Hero** (`header.hero`, 49–415px): max 860px, padding 64px 20px 40px, centred text.
3. **Title** (`h1`, y=113): 48px / 800, line-height 79.2px, letter-spacing -0.96px, #08407e. Margin-bottom 6.4px.
4. **Subtitle** (`p.subtitle`, y=198): 19.2px / 400, line-height 31.68px, #4a4a4a, max 704px, two lines. Margin-bottom 22.4px.
5. **Venue** (`p.venue`, y=284): "EMNLP 2025 (Main Conference)", 14.72px / 700 #007894. Margin-bottom 25.6px.
6. **Buttons** (`.btns`, y=334, 41px tall): five pills with 8.8px gaps, centred: 📄 Paper and 💻 Code filled, ACL Anthology, 🤗 Reward Model and 🤗 Dataset outlined. Then the 40px hero bottom padding.
7. **First section** (`section.section`, from y=415, no top border on the first one): padding 44px 20px; eyebrow "RESULTS" at y=459, h2 "Leaderboard" at y=484, intro paragraph at y=544, the table frame from y=614, running below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| ETH Blue | #215caf | --eth-blue | filled buttons, ghost-button text and border, "Bench" in the wordmark, links, sorted column header, best scores (`td.best`), nav hover |
| ETH Blue Dark | #08407e | --eth-blue-dark | hero title, wordmark, table header text, feature-tile titles, button hover fill |
| Blue 10 | #e9eff7 | --eth-blue-10 | table header background, feature tiles, inline code background, ghost-button hover |
| Blue 20 | #d3dfee | --eth-blue-20 | 2px bottom border under the table header |
| Petrol | #007894 | --eth-petrol | venue line, section eyebrows, NEW tags, callout left bar, team superscripts |
| Petrol 10 | #e5f1f4 | --eth-petrol-10 | callout background |
| ETH Gray | #6f6f6f | --eth-gray | affiliation line, table notes, figure notes, footer, inline code text |
| Ink | #222222 | --ink | body base colour, h2, h3, model names, strong, team names |
| Ink Soft | #4a4a4a | --ink-soft | paragraphs, subtitle, nav links, table cells |
| Line | #e4e7ec | --line | top-bar border, section rules, table frame and row lines, figure borders, footer rule |
| Code Navy | #0f2036 | --code-bg | `pre` code blocks |
| Code Ink | #dce7f5 | --code-ink | text in code blocks |
| Row Hover | #f6f9fd | (literal) | table row hover |
| Paper | #ffffff | (body) | page, top bar, ghost buttons, table cells |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif | no web font; Segoe UI in this render (SF Pro on macOS) | Inter |
| Code | ui-monospace, SFMono-Regular, Menlo, Consolas, monospace | system monospace (Consolas on Windows) | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Hero title | `.hero h1` | clamp(2rem, 5vw, 3rem) → 48px / 800 / 1.65, letter-spacing -0.02em | #08407e |
| Subtitle | `.hero .subtitle` | clamp(1rem, 2vw, 1.2rem) → 19.2px / 400 / 1.65 | #4a4a4a |
| Venue | `.hero .venue` | 0.92rem = 14.72px / 700 | #007894 |
| Wordmark | `.wordmark` | 1.02rem = 16.32px / 800, letter-spacing -0.01em | #08407e, span #215caf |
| Nav link | `.topbar-links a` | 0.86rem = 13.76px / 500 | #4a4a4a |
| Eyebrow | `.kicker` | 0.78rem = 12.48px / 800 uppercase, letter-spacing 0.12em | #007894 |
| Section heading | `h2` | 1.65rem = 26.4px / 800, letter-spacing -0.015em | #222222 |
| Subheading | `h3` | 1.08rem = 17.28px / 700, margin 1.9rem 0 0.6rem | #222222 |
| Body | `p, li` | 16px / 400 / 26.4px | #4a4a4a |
| Button | `.btn` | 0.88rem = 14.08px / 600 | #ffffff on #215caf; ghost #215caf |
| Table | `table` | 0.87rem = 13.92px; th 700; model column 600; best 800 | th #08407e, cells #4a4a4a |
| NEW tag | `.tag-new` | 0.64rem = 10.24px / 800, letter-spacing 0.05em | #ffffff on #007894 |
| Notes | `.table-note`, `.fignote` | 0.82rem = 13.12px | #6f6f6f |
| Code block | `pre` | 0.82rem = 13.12px / 1.65 | #dce7f5 on #0f2036 |
| Inline code | `code` | 0.88em | #6f6f6f in table notes on #e9eff7 |
| Footer | `footer` | 0.85rem = 13.6px | #6f6f6f |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 999px | 1px (declared 1.5px) solid #215caf | none; hover fill #08407e (ghost: #e9eff7) |
| NEW tag | 999px, padding 0.8px 7.2px | none | none |
| Table frame (`.table-wrap`) | 8px | 1px solid #e4e7ec | none; first column `box-shadow: inset -1px 0 0 #e4e7ec` |
| Figures (`.figure img`) | 8px | 1px solid #e4e7ec | none |
| Feature tiles | 8px, padding 15.2px 17.6px | none | none |
| Callout | 0 8px 8px 0, padding 13.6px 17.6px | 4px solid #007894 on the left | none |
| Code block | 8px, padding 16px 20px | none | none |
| Inline code | 4px, padding 0.1em 0.35em | none | none |
| Sections, top bar, footer | 0 | 1px solid #e4e7ec rules | none |

## Layout Metrics

- **Container**: `.section { max-width: 1020px; margin: 0 auto; padding: 2.75rem 1.25rem }` = 44px 20px, so content is 980px wide from x=230. The top-bar inner row uses the same 1020px. The hero is narrower: max 860px, padding 64px 20px 40px.
- **Section rhythm**: each section has 44px top and bottom padding and a 1px #e4e7ec top rule (none on the first), so rules sit 88px from the previous content. Eyebrow margin-bottom 4.8px; h2 margin-bottom 16px.
- **Leaderboard**: `.table-wrap` 980px wide with horizontal scroll; the table renders 1806px wide (white-space: nowrap); header cells padding 10.4px 12px, body cells 8px 12px; model column sticky at left 0.
- **Findings**: `.two-col` grid 1fr 1fr, gap 32px (two 474px columns).
- **Feature tiles**: `.features` grid repeat(auto-fit, minmax(220px, 1fr)), gap 14.4px.
- **Figures**: centred, max-width 100%; `.figure.narrow img` max 430px.
- **Footer**: 1px top rule, padding 36px 16px 44px, centred.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥960px (1440 renders this) | 20px inside 1020px | 16px | 48px | two-col findings |
| <960px | 20px | 16px | 5vw (e.g. 40px at 800px) down to 32px at ≤640px | subtitle follows 2vw, floor 16px |
| ≤800px | 20px | 16px | 40px | `.two-col` → 1 column |
| any width | — | — | — | nav links wrap (flex-wrap); feature tiles reflow by auto-fit |

## Components

- **Filled pill button** (`.btn`): inline-flex, gap 6.4px, padding 8px 16.8px, radius 999px, 14.08px / 600, #ffffff on #215caf, 1px #215caf border, emoji as the leading icon. Hover: fill and border #08407e, no underline, transition background 0.15s.
- **Ghost pill button** (`.btn.ghost`): same shape, #ffffff fill, #215caf text and border; hover fill #e9eff7.
- **Eyebrow + heading** (`.kicker` + `h2`): 12.48px / 800 uppercase petrol #007894 with 0.12em tracking, 4.8px above a 26.4px / 800 #222222 heading with -0.015em tracking.
- **Sortable leaderboard**: frame 1px #e4e7ec, radius 8px, overflow-x auto. Header #e9eff7 with #08407e 700 text, 2px #d3dfee bottom border, sticky; hover turns text #215caf; the sorted header turns #215caf and shows a ▼ at 0.7em. Body cells white, centred, #4a4a4a, 1px #e4e7ec row lines; row hover #f6f9fd. The model column is left aligned, 600 #222222, sticky with an inset right hairline. Best score per column: `td.best` 800 #215caf.
- **NEW tag** (`.tag-new`): 10.24px / 800, letter-spacing 0.05em, #ffffff on #007894, radius 999px, padding 0.8px 7.2px, 7.2px left margin after a model name.
- **Feature tile** (`.features li`): #e9eff7, radius 8px, padding 15.2px 17.6px, 14.4px text; bold title on its own line in #08407e.
- **Callout** (`.callout`): #e5f1f4, 4px #007894 left bar, radius 0 8px 8px 0, padding 13.6px 17.6px, 14.4px #4a4a4a text, emoji lead.
- **Code block** (`pre`): #0f2036 background, #dce7f5 text, radius 8px, padding 16px 20px, 13.12px monospace, line-height 1.65.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky top bar | yes | white, hairline bottom border, navy wordmark, six text links |
| Title / subtitle / venue | yes | centred navy 48px title, soft-ink subtitle, petrol venue |
| Link buttons | yes | two filled and three ghost pills with emoji |
| Authors in the hero | present but non-standard | no author line in the hero; names appear in the PEOPLE section near the end as a flex list of 600-weight names with petrol superscripts |
| Leaderboard | yes | sortable, scrollable table with sticky first column, NEW tags and bold-blue best scores |
| Findings | yes | two columns of h3 + text + bordered figures with grey notes |
| Method overview | yes | narrow figure and pale-blue feature tiles |
| Quick start / usage | yes | numbered steps, parameter lists, dark navy code blocks, petrol callout |
| Submission instructions | yes | CONTRIBUTE section in the same section style |
| Abstract | absent from the source | the subtitle and section intros replace it |
| Video / teaser image | absent from the source | — |
| BibTeX | yes | REFERENCE section with a navy code block |
| Footer | yes | centred grey 13.6px line with hairline rule |

## Adapting to Other Content

- **A teaser figure**: place it in a section directly after the hero using `.figure` (centred, 1px #e4e7ec border, 8px radius) at up to 980px wide, with a 13.12px #6f6f6f `.fignote`.
- **Authors in the hero**: add a centred line under the subtitle at 16px / 600 #222222 with #007894 superscripts, matching the PEOPLE section, and keep affiliations at 13.6px #6f6f6f.
- **More results tables**: reuse the leaderboard frame; mark best values only with 800 #215caf, never with a background fill.
- **News or publication lists**: a section with a petrol eyebrow ("NEWS") and a list of 16px #4a4a4a items, each date as 600 #222222; separate entries with 1px #e4e7ec lines rather than cards.
- **More stats**: use feature tiles (#e9eff7, 8px radius) with the number as the bold #08407e title.

## Do's and Don'ts

- Do open every section with a petrol uppercase eyebrow over an 800-weight heading.
- Do keep blue for action and emphasis (#215caf) and navy (#08407e) for identity (title, wordmark, table header).
- Do separate sections with a single 1px #e4e7ec rule and 44px padding.
- Do keep the hero type-only and centred.
- Don't load a web font; the system UI stack is the face.
- Don't add shadows; frames are 1px hairlines with 8px radii.
- Don't fill best scores with colour; bold blue text is the highlight.

## Surfaces

White page and white top bar; pale blue #e9eff7 for the table header, feature tiles and inline code; pale petrol #e5f1f4 for the callout; dark navy #0f2036 for code blocks. No gradients or shadows anywhere.

## Imagery

Plots exported from the paper (a scatter of models coloured by a blue scale, a multi-series radar chart) and a method diagram, each in a 1px hairline frame with 8px radius and a small grey note underneath. Emoji serve as button and callout icons.

## Layout

Sticky bar, centred type hero, then seven stacked 1020px sections divided by hairlines; the findings section splits into two equal columns. About 6,200px tall.

## Agent Prompt Guide

Quick colors: blue #215caf, navy #08407e, petrol #007894, pale blue #e9eff7, header rule #d3dfee, ink #222222, soft ink #4a4a4a, gray #6f6f6f, line #e4e7ec, code #0f2036 / #dce7f5.

1. "Build a centred hero (max 860px, padding 64px 20px 40px): title 48px / 800 #08407e with -0.02em tracking; subtitle 19.2px #4a4a4a max 704px; venue 14.72px / 700 #007894; a row of pills 8.8px apart: filled (#215caf fill, #ffffff 14.08px / 600 text, padding 8px 16.8px, radius 999px, hover #08407e) and ghost (#ffffff fill, #215caf text and 1px border, hover #e9eff7)."
2. "Make a section: max-width 1020px, padding 44px 20px, 1px #e4e7ec top border; eyebrow 12.48px / 800 uppercase #007894 with 0.12em letter-spacing; h2 26.4px / 800 #222222; body 16px #4a4a4a at line-height 1.65."
3. "Create a sortable leaderboard: wrapper with 1px #e4e7ec border, 8px radius, horizontal scroll; header #e9eff7 with #08407e 700 text and a 2px #d3dfee bottom border; cells centred #4a4a4a with 1px #e4e7ec row lines and #f6f9fd hover; sticky first column 600 #222222; best values 800 #215caf; NEW tags 10.24px / 800 #ffffff on #007894 pills."

## Similar Pages

- Hand-built benchmark sites that use a university corporate palette with a sortable leaderboard.
- Pages organised as eyebrow-labelled sections (RESULTS, FINDINGS, USAGE) like product documentation.

## Quick Start

```css
:root {
  --eth-blue: #215caf;
  --eth-blue-dark: #08407e;
  --eth-blue-10: #e9eff7;
  --eth-blue-20: #d3dfee;
  --eth-petrol: #007894;
  --eth-petrol-10: #e5f1f4;
  --eth-gray: #6f6f6f;
  --ink: #222222;
  --ink-soft: #4a4a4a;
  --line: #e4e7ec;
  --code-bg: #0f2036;
  --code-ink: #dce7f5;
  --font-ui: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --radius: 8px;
  --content-max: 1020px;
}
```

## Provenance

- **URL**: https://eth-lre.github.io/mathtutorbench/
- **Paper**: MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors (arXiv 2502.18940), Jakub Macina, Nico Daheim and colleagues (ETH Zurich, ETH AI Center).
- **Venue**: EMNLP 2025 (Main Conference).
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: none stated; a custom single-file build whose CSS comment names the ETH Zurich corporate palette.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and the inline stylesheet and markup of `index.html` read directly, on 2026-10-28.
