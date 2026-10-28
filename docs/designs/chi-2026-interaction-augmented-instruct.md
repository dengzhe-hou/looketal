# Interaction-Augmented Instruction — Style Reference

> A clean product landing page bolted onto a research database: a blue pill badge, a title that speaks in rust and moss, and below it a gray workbench of paradigm cards.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, a second capture of y=1850 to 3850 taken after a 6s wait, and the compiled Vue stylesheet (`index-DvRR6HMo.css`, scoped `data-v-*` rules) and bundle (`index-BWdjEOBy.js`) read directly. The page is a Vue single-page app: the white "paper promotion" header is static, and the gray lower half is an interactive browser of interaction paradigms that fetches its data after load. The pool full-page screenshot was taken before that data arrived and shows only a centred "Loading papers..." line (18px #666666 in a 400px-tall `.loading` box); the later render and capture show twelve paradigm cards, and the values below describe that loaded state.

## Overview

A long page (about 9,750px tall when loaded) in two zones. The top zone (`section.paper-promotion`, white, 1889px tall, 1px #e5e7eb bottom border) is a centred landing block: a small blue "ACM CHI 2026" pill at the top left, a two-line 32px bold title in #1f2937 with the words "Prompts" in rust #c04f17 and "Interactions" in moss #3c7c22, a row of five author names in blue #3b82f6 with tiny gray affiliations under each, a gray venue line and an amber "🏆 Best Paper Honorable Mention" line, a 1000px teaser figure in a white card with 12px radius, hairline border and soft shadow, an abstract in a pale slate (#f8fafc) bordered card, an 800px introduction video in the same card style, and a single blue "Paper (PDF)" button. The lower zone (`#f5f5f5`) starts with a full-width two-tab bar (Paradigm Analysis, Paper List) whose active tab has a 3px blue underline, a gray filter strip with two selects and a "Clear Filters" button, and then white paradigm cards, each with a gray header (title, name field, blue and purple italic tags, paper count), a 600px node-link diagram and a scrollable list of paper items.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 58.6% and near-whites #fafdfd 10.3%, #fffffd 1.5%, #fcffff 0.7%; pale blue #f2f8fc 9.0% and light slate #e1e8ec 8.6% (the teaser's tinted panels), gray-blue #98aab2 7.1% (teaser line work and text), cream #fcf9f1 4.0% (the teaser's peach panel A). The blue badge, author names and colored title words are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `.paper-promotion` padding 48px 40px 40px):

1. **Conference badge** (`.conference-badge`, x=40, y=48, 118×29): inline-flex, #3b82f6 fill, white 13px / 600 "ACM CHI 2026", padding 6px 16px, radius 20px, left aligned. Margin-bottom 20px.
2. **Title** (`h1.paper-title`, y=97, 83px tall, max 1000px centred): 32px / 700, line-height 1.3, #1f2937, two lines; spans `.highlight-prompts` #c04f17 and `.highlight-interactions` #3c7c22. Margin-bottom 28px.
3. **Authors** (`.authors-list`, y=208, 42px tall, max 1200px): flex wrap, centred, gap 20px 36px; each `.author-item` is a name (`a.author-name`, 18px / 600 #3b82f6) over an affiliation (`.author-affiliation`, 12px #6b7280, 2px above). The venue and award lines sit inside the same `.authors-section`, so the venue's 20px margin-top is the gap here; the section's 36px margin-bottom falls below the award.
4. **Venue** (`.venue-info`, y=270, 20px tall): "The ACM CHI Conference on Human Factors in Computing Systems (CHI'26)", 15px / 500 #4b5563, centred.
5. **Award** (`.award-info`, y=298): "🏆 Best Paper Honorable Mention", 15px / 600 #b45309, margin-top 8px.
6. **Teaser card** (`.teaser-section` max 1000px, `.teaser-container`, y=354 to 883): white, 1px #e5e7eb border, radius 12px, overflow hidden, box-shadow 0 4px 20px #00000014; image 998×527. Margin-bottom 32px.

Below the fold: the abstract card at y=915 (900px), the "Introduction Video" label at y=1257 and the video card at y=1290 (800×450), the Paper (PDF) button at y=1772, the tab bar at y=1889.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #1f2937 | (literal, gray-800) | title, header text |
| Body Gray | #333333 | (literal, `body`) | lower-zone text, paradigm titles, paper titles |
| Label Gray | #374151 | (literal, gray-700) | section labels (Abstract, Introduction Video), filter labels, description values |
| Copy Gray | #4b5563 | (literal, gray-600) | abstract text, venue line, Clear Filters hover |
| Meta Gray | #6b7280 | (literal, gray-500) | affiliations, inactive tab text, Clear Filters fill |
| Blue | #3b82f6 | (literal, blue-500) | badge, author names, PDF button, active tab text and underline, focus rings, paper-item hover border |
| Blue Hover | #2563eb | (literal, blue-600) | author and button hover |
| Rust | #c04f17 | (`.highlight-prompts`) | "Prompts" in the title |
| Moss | #3c7c22 | (`.highlight-interactions`) | "Interactions" in the title |
| Amber | #b45309 | (literal, amber-700) | award line |
| White | #ffffff | (literal) | header zone, cards, tab bar |
| Lower Gray | #f5f5f5 | (literal, `body`, `.app-main`) | page background below the header |
| Hairline | #e5e7eb | (literal) | header bottom border, card borders, tab bar border |
| Slate Tint | #f8fafc | (literal) | abstract card, tab hover |
| Panel Gray | #f8f9fa | (literal) | filter strip, paradigm card header, paper items |
| Panel Edge | #e9ecef | (literal) | filter strip and paper-item borders, paper-count chip |
| Card Edge | #e0e0e0 | (literal) | paradigm card and diagram borders |
| Diagram Ground | #fafafa | (literal) | diagram well |
| Field Fill | #f9fafb | (literal, gray-50) | read-only paradigm name field and description box |
| Select Edge | #d1d5db | (literal, gray-300) | filter select borders |
| Muted Text | #666666 | (literal) | paper meta, paper count, loading text |
| Timing Tag | #e3f2fd / #1565c0 / #bbdefb | (`.timing-label`) | fill / text / border of "Interaction Before Calling GenAI" tags |
| Resource Tag | #f3e5f5 / #7b1fa2 / #e1bee7 | (`.resource-label`) | fill / text / border of "Prompt-only" tags |
| Template Violet | #8b5cf6 | (`.template-info`) | italic "Paradigm 1" lines in paper items |
| Video Black | #000000 | (literal) | video card background |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif | no web font loaded; Segoe UI on Windows, SF Pro on macOS | Inter |
| Form controls | browser default for `button`/`select` | Arial (tab buttons and Clear Filters inherit no font) | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Badge | `.conference-badge` | 13px / 600 | white on #3b82f6 |
| Paper title | `.paper-title` (header) | 32px / 700 / 1.3 | #1f2937, highlights #c04f17 and #3c7c22 |
| Author name | `.author-name` | 18px / 600 | #3b82f6 |
| Affiliation | `.author-affiliation` | 12px / 400 | #6b7280 |
| Venue | `.venue-info` | 15px / 500 | #4b5563 |
| Award | `.award-info` | 15px / 600 | #b45309 |
| Section label | `.section-title` | 16px / 600, centred | #374151 |
| Abstract | `.abstract-text` | 14px / 1.8, justified | #4b5563 |
| PDF button | `.action-btn` | 15px / 600 | white |
| Tab | `.nav-tab` | 16px / 500 (Arial) | #6b7280; active #3b82f6 |
| Paradigm title | `.pattern-header h2` | 20px / 600 | #333333 |
| Tag | `.pattern-label` | 12px / 500 italic | tag colors above |
| List heading | `.pattern-papers h3` | 18px / 600 | #333333 |
| Paper title (list) | `.paper-title` (list) | 16px / 600 | #333333 |
| Paper meta | `.paper-meta` | 14px | #666666 |
| Description | `.description-display` | 14px / 1.5 | #374151 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Conference badge | 20px | none | none |
| Teaser card, video card | 12px, overflow hidden | 1px #e5e7eb | 0 4px 20px #00000014 |
| Abstract card | 12px | 1px #e5e7eb | none |
| PDF button | 8px | none | none; hover #2563eb, translateY(-1px), 0 4px 12px #3b82f64d |
| Tab bar | 0 | 1px #e5e7eb bottom; active tab 3px #3b82f6 underline | none |
| Filter strip | 8px | 1px #e9ecef | none |
| Selects | 4px | 1px #d1d5db; focus #3b82f6 with 0 0 0 2px #3b82f61a | none |
| Clear Filters | 4px | none | none |
| Paradigm card | 12px, overflow hidden | 1px #e0e0e0; header 1px #e0e0e0 bottom | none |
| Diagram well | 8px | 1px #e0e0e0 | none; node rects `filter: drop-shadow(0 2px 4px rgba(0,0,0,.1))` |
| Tags | 4px | 1px tag border | none |
| Paper items | 8px | 1px #e9ecef; hover 1px #3b82f6 | none |
| Paper-count chip | 4px | none | none |

## Layout Metrics

- **Header zone**: `.paper-promotion` padding 48px 40px 40px, white, 1px #e5e7eb bottom border; 1889px tall at 1440.
- **Header columns**: title max 1000px centred; authors max 1200px (x=120); teaser section max 1000px (x=220), margin-bottom 32px; abstract card max 900px (x=270), padding 24px 28px, margin-bottom 32px; video section max 800px (x=320), 16:9 (800×450), margin-bottom 32px; action buttons centred with 16px gap, margin-bottom 32px.
- **Tab bar**: full width, two `flex: 1` tabs of 720px, padding 16px 24px, 51px tall incl. border.
- **Lower zone**: `.pattern-analysis` max 1200px, padding 20px (cards 1160px from x=140); filter strip padding 16px 20px, gap 20px, margin-bottom 20px; cards 30px apart.
- **Paradigm card**: header padding 20px; content grid `600px 1fr` with 30px gap and 20px padding; diagram well 600×300 with 10px padding; paper list items padding 15px, 12px apart (scrollable lists 400px tall).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1024px | header 40px; lower 20px | 14px abstract, 16px UI | 32px | paradigm cards two columns (600px diagram + list) |
| ≤1024px | same | same | 32px | paradigm content one column, diagram max 600px centred; name fields 300px |
| ≤900px | header padding 32px 20px 30px | same | 24px | authors gap 14px 24px; names 14px; affiliations 11px |
| ≤768px | same | same | 24px | tabs padding 12px 16px, 14px; tab text 13px |
| ≤600px | same | abstract 13px | 20.8px | abstract card padding 16px 18px |
| ≤480px | same | same | 20.8px | tabs padding 10px 8px; tab text 12px |

## Components

- **Conference badge** (`.conference-badge`): inline-flex, gap 8px, #3b82f6, white 13px / 600, padding 6px 16px, radius 20px, top left of the header.
- **Two-color title**: 32px / 700 #1f2937 with the two key nouns colored #c04f17 and #3c7c22, matching the teaser's own color coding.
- **Author item**: centred column, 18px / 600 #3b82f6 name (hover #2563eb underlined) over a 12px #6b7280 affiliation; items in a wrapping row with 36px column gaps.
- **Media card** (`.teaser-container`, `.video-container`): white (video black), 1px #e5e7eb border, radius 12px, overflow hidden, shadow 0 4px 20px #00000014.
- **Abstract card** (`.abstract-section`): #f8fafc, 1px #e5e7eb border, radius 12px, padding 24px 28px; a centred 16px / 600 #374151 label, then 14px / 1.8 justified #4b5563 text.
- **Primary button** (`.action-btn.pdf-btn`): inline-flex, gap 10px, padding 12px 24px, radius 8px, #3b82f6, white 15px / 600, 18px document icon. Hover #2563eb, translateY(-1px), shadow 0 4px 12px #3b82f64d.
- **Tab bar** (`.nav-tabs`): white, full width, 1px #e5e7eb bottom border; tabs 16px / 500 #6b7280 with an icon, hover #f8fafc and #374151; active #3b82f6 with a 3px #3b82f6 bar along the bottom.
- **Filter strip** (`.filter-section`): #f8f9fa, 1px #e9ecef, radius 8px, padding 16px 20px; 14px / 600 #374151 labels; selects min 180px, 1px #d1d5db, radius 4px; "Clear Filters" #6b7280 fill, white 14px, radius 4px, hover #4b5563.
- **Paradigm card** (`.pattern-group`): white, 1px #e0e0e0, radius 12px; #f8f9fa header with "Paradigm P1" 20px / 600, a read-only name field (#f9fafb, 1px #e5e7eb, radius 6px, 16px / 500 #374151, 400px wide), italic 12px tags, and a #e9ecef "2 paper(s)" chip; body with a #fafafa diagram well and a list of #f8f9fa paper items (16px / 600 title, 14px #666666 meta, 12px italic #8b5cf6 template line).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue badge | yes | blue pill "ACM CHI 2026", top left |
| Title | yes | two-color highlighted 32px bold title |
| Authors / affiliations | yes | blue names over gray affiliations, one row |
| Venue / award | yes | gray venue line, amber award line |
| Teaser | yes | 1000px shadowed card |
| Abstract | yes | slate-tinted bordered card |
| Video | yes | 800px card with native controls |
| Link buttons | present but non-standard | a single blue "Paper (PDF)" button after the video |
| Interactive database | yes | tabbed paradigm browser with filters, diagrams and paper lists |
| Loading state | yes | "Loading papers..." centred in a 400px gray box until data arrives |
| BibTeX | absent from the source | none |
| Footer | absent from the source | the page ends with the last paradigm card |

## Adapting to Other Content

- **More authors**: keep author items in the wrapping centred row (36px column gap, 20px row gap); at 1200px about five items with long affiliations fit per row.
- **A results table**: put it in a white card like the paradigm cards (1px #e0e0e0, radius 12px) with a #f8f9fa header row in 14px / 600 #374151, 14px #333333 cells, 1px #e9ecef row rules, best values in #3b82f6 600.
- **Long publication or news lists**: reuse paper items: #f8f9fa rows, 1px #e9ecef, radius 8px, padding 15px, 12px apart, 16px / 600 titles with 14px #666666 meta and a #3b82f6 border on hover.
- **More links**: add `.action-btn`s next to the PDF button with 16px gaps; secondary links as white buttons with 1px #e5e7eb border and #374151 text.
- **A BibTeX block**: a card like the abstract (#f8fafc, 1px #e5e7eb, radius 12px, padding 24px 28px) with 13px monospace #4b5563, max 900px, above the tab bar.

## Do's and Don'ts

- Do keep the header white and the database zone #f5f5f5, separated by the 1px #e5e7eb rule and the tab bar.
- Do use #3b82f6 for every interactive accent: badge, author links, button, active tab.
- Do reserve #c04f17 and #3c7c22 for the two highlighted title words and the matching figure concepts.
- Do frame media in white 12px cards with the 8% 20px shadow.
- Don't ship the page without its data; the loading block alone reads as broken.
- Don't use more than one filled button in the header.
- Don't change the tag colors; blue is timing, purple is resource.

## Surfaces

White header with three framed cards (teaser, abstract on #f8fafc, video on black); a gray #f5f5f5 lower zone holding white paradigm cards with #f8f9fa headers and items, #fafafa diagram wells, and a #f8f9fa filter strip.

## Imagery

A large multi-panel teaser (peach motivation panel A with a cartoon person, blue IAI model diagram B, paradigm diagrams C, usage-scenario thumbnails D, a blue pyramid of Model, Paradigms and Interfaces), an introduction video with a title card that repeats the two-color title, and many small SVG node-link diagrams (H, I, A, T, Aug, G nodes with numbered blue edges).

## Layout

A centred landing block with columns that narrow as they go down (title 1000px, authors 1200px, teaser 1000px, abstract 900px, video 800px), then a full-width tab bar and a 1160px column of stacked paradigm cards with a 600px diagram beside each paper list.

## Agent Prompt Guide

Quick colors: header #ffffff, lower zone #f5f5f5, ink #1f2937, labels #374151, copy #4b5563, meta #6b7280, accent #3b82f6, highlights #c04f17 and #3c7c22, award #b45309, borders #e5e7eb.

1. "Build a white header with padding 48px 40px 40px: a left-aligned pill (#3b82f6, white 13px / 600, padding 6px 16px, radius 20px), then a centred 32px / 700 #1f2937 title (max 1000px, line-height 1.3) with one word in #c04f17 and one in #3c7c22; authors in a wrapping centred row (gap 20px 36px), names 18px / 600 #3b82f6 over 12px #6b7280 affiliations; venue 15px / 500 #4b5563; award 15px / 600 #b45309."
2. "Make media and abstract cards: teaser and video in white cards with 1px #e5e7eb border, radius 12px, box-shadow 0 4px 20px #00000014 (teaser 1000px, video 800px 16:9 on black); abstract card #f8fafc, 1px #e5e7eb, radius 12px, padding 24px 28px, 16px / 600 #374151 centred label, 14px / 1.8 justified #4b5563 text; one #3b82f6 button, padding 12px 24px, radius 8px, white 15px / 600, hover #2563eb."
3. "Create a tabbed database zone on #f5f5f5: a full-width white tab bar with two equal tabs (16px / 500 #6b7280, padding 16px 24px), active tab #3b82f6 with a 3px #3b82f6 bottom bar; a #f8f9fa filter strip (1px #e9ecef, radius 8px, padding 16px 20px); white cards (1px #e0e0e0, radius 12px) with #f8f9fa headers, 20px / 600 titles, italic 12px tags (#e3f2fd / #1565c0 and #f3e5f5 / #7b1fa2), a 600px #fafafa diagram well and #f8f9fa list items with radius 8px."

## Similar Pages

- Vue or React project pages that pair a paper landing block with a browsable design-space database.
- HCI taxonomy papers whose site is mostly an interactive catalogue of surveyed papers.

## Quick Start

```css
:root {
  --header-bg: #ffffff;
  --page-bg: #f5f5f5;
  --ink: #1f2937;
  --text: #333333;
  --label: #374151;
  --copy: #4b5563;
  --meta: #6b7280;
  --accent: #3b82f6;
  --accent-hover: #2563eb;
  --hl-prompts: #c04f17;
  --hl-interactions: #3c7c22;
  --award: #b45309;
  --border: #e5e7eb;
  --panel: #f8f9fa;
  --card-shadow: 0 4px 20px #00000014;
  --radius-card: 12px;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
```

## Provenance

- **URL**: https://interaction-augmented-instruction.github.io/
- **Paper**: Interaction-Augmented Instruction: Modeling the Synergy of Prompts and Interactions in Human-GenAI Collaboration (arXiv 2510.26069), Leixian Shen, Yifang Wang, Huamin Qu, Xing Xie, Haotian Li.
- **Venue**: CHI 2026, Best Paper Honorable Mention (as shown on the page).
- **Selection reason**: the arXiv comment states acceptance at CHI 2026; the project page is linked in the paper body (arXiv HTML).
- **Template credit**: none stated; a Vite-built Vue single-page app with scoped CSS.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of the header, cards, tabs, filters and paradigm cards, the pool 1440×900 and full-page screenshots, a later capture of y=1850 to 3850 with data loaded, and the compiled CSS and JS read directly, on 2026-10-28.
