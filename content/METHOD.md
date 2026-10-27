# How a Look et al. DESIGN.md is written (v2, 2026-10-28)

v2 follows a reconstruction test on 5 v1 files (blind matching 5/5 correct; similarity 2–4 of 5). The test showed that most errors came from reading CSS without checking what the page actually renders, and that builders lacked header anatomy and layout metrics. v2 fixes both.

## Evidence, in order of authority

1. **Rendered page**: `tools/computed_style.py URL --png SHOT.png` gives computed styles of key elements, the first-viewport anatomy in DOM order, the fonts that really loaded, the widest content container, and the first-viewport color share. The screenshot (`tools/snap.py`, 1440×900) is looked at directly.
2. **Page stylesheet and markup**: to cite selectors, find hover/responsive rules, and explain what the render shows.
3. **`tools/extract_style.py`**: declaration frequency counts; useful for finding the page's own palette, but it includes framework defaults.

When CSS and the render disagree, the render wins. A spot audit of ten v2 files (about 129 claims, 4 wrong) found that three of the four errors were values a script or a later cascade rule changes at render time (inline-sized sliders, a label rule overridden inside one block, a heading inside a link). Before writing a value taken from a stylesheet rule, probe one rendered instance of that exact element. A rule that is declared but not visible (overridden, covered, or unused) is not a token; mention it only under "Declared but not visible" if it matters.

## Rules

- Every token row names the rendered element(s) it applies to, e.g. `#2c3e50 — paper title (h1.title), section titles`.
- Write "inferred" only when CSS, DOM and render cannot settle the value. Never for values a selector or utility class determines (`py-3` is 1rem, `h1.h4` renders at h4 size).
- Fonts: report the declared stack and what actually renders (from `fonts_loaded`). Give one substitute, chosen for matching proportions.
- Describe components as recipes (exact colors, size, weight, padding, radius, border, shadow, icon set and side, hover), not adjectives.
- One property gets one value across the file. The Agent Prompt Guide and Quick Start reuse values from the token tables. Check for contradictions before finishing.
- Separate "absent from the source" from "present but non-standard" in Page Modules.
- Sizes are what renders at 1440. Where a media query changes a value, give the base value and each override separately (the v2 test found a 240px rule that renders 110px at 1440).
- Quote gradient, shadow and filter declarations literally; give positions as coordinates, never as words like "lower right".
- Check that the anatomy y-positions add up from the listed paddings and margins; name every wrapper padding that contributes.
- Every "Adapting to Other Content" rule states the size it produces at 1440 and must not contradict Imagery or Do's and Don'ts.

## Required sections (in order)

1. `# <Style name> — Style Reference`, `> mood line`, `**Theme:**`, a one-paragraph measurement note.
2. `## Overview` — what the page looks like as rendered.
3. `## First Viewport` — color share by area (from the tool), then the anatomy in DOM order: each line (logo, title, authors, affiliations, venue, buttons, teaser…) with font size / weight / color / alignment and the vertical gap to the next item.
4. `## Tokens — Colors` — Name | Value | Token | Applies to (rendered elements).
5. `## Tokens — Typography` — families (declared vs rendered, substitute), type scale with the selector for each role.
6. `## Tokens — Spacing & Shapes` — radius, shadows, borders.
7. `## Layout Metrics` — container width formula, hero padding, section padding, gaps, figure/video widths, and a breakpoint table (breakpoint → gutter, body size, title size, grid change).
8. `## Components` — recipes.
9. `## Page Modules` — table: module | present | how it is styled.
10. `## Adapting to Other Content` — how this style handles content the source lacks (more authors, a results table, long publication lists, news).
11. `## Do's and Don'ts`, `## Surfaces`, `## Imagery`, `## Layout`.
12. `## Agent Prompt Guide` — quick color reference and 3 component prompts using only values from the tables above.
13. `## Similar Pages`, `## Quick Start` (CSS custom properties), `## Provenance` (URL, venue/award, selection reason, template credit, evidence used, date).
