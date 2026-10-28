# MOCHI — Style Reference

> A clean exhibition label: a single 900px column, steel-blue initials in the title, small navy pills, and quiet uppercase heads ruled in gray.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), two further probes of rendered elements (title spans, venue, section heads, dividers, carousel controls, footer), the 1440×900 and tall screenshots, and the page's shared `../project_style.css` and `../../css/carousel.css`. The page body is built at load time by `project.js` from a YAML file, so the static `index.html` holds almost no content; every value here was read from the rendered DOM. Section heads render in capitals because the source text is uppercase, while the CSS only sets `text-transform: capitalize`.

## Overview

A minimal, well-aligned page on near-white #fdfdfd with near-black #111111 text in Inter. There is no navigation bar: the page opens directly with a centred 28px bold title whose acronym initials are coloured steel blue #4e86c4 ("MOCHI", "Mo", "C", "H", "I"), followed by three navy #2c4a8a author links separated by em-spaces, a one-line affiliation, a bold "SIGGRAPH 2026 (Journal Track)" line and four small navy pill buttons. Everything sits in a single 900px column. The teaser is a bright, white-ground render of colour-coded characters carrying furniture, with a justified caption that colours "soft pink", "skyblue", "pink" and "blue" to match the figures. Sections ("ABSTRACT", "RESULTS", "APPLICATIONS") are 18.4px bold gray heads with a 1px #d0d0d0 rule beneath, then justified 15px text and large 16:9 carousel videos with small arrow-and-dot controls. A two-column footer with "CONTACT" and "INFO" lists closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): near-white family #fdfdfd / #fffffe / #fefdfc / #fbfefe / #fdfdfe / #fefdfd together 69.1%; warm light gray #ebeae7 19.1% (the floor and walls of the teaser render); silver #b1b1b3 11.8% (furniture, shadows and text blended). The navy buttons and blue initials are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `.home-wrapper` 960px at x=240 with 30px padding, content x=270 to 1170):

1. **Page top**: `.page-content` padding-top 45px; no header or nav.
2. **Title** (`#title`, y=65, 78px, two lines): Inter 28px/700 (rendered from the 600 file), line-height 1.4, letter-spacing -0.01cm (-0.378px), #111111, centred; acronym initials in `<span style="color:#4E86C4">`. Gap 5.6px + 20.7px.
3. **Authors** (`.author-wrapper`, y=164): 18px, links Inter 600 #2c4a8a with two em-spaces between names, no underline.
4. **Affiliation** (`#aff`, y=195): 17px/400 #111111, margin 10.2px 0 5.1px.
5. **Venue** (`.pub-source-wrapper`, y=234): 19px, inner `<b>` 700 #111111, margin 19px 0. Gap 14.4px.
6. **Buttons** (`.links-row`, y=276, 33px tall, gap 18px): arXiv, PDF, Video, Code as `button.link-button` inside links: #2c4a8a fill, white 15px text in the browser's default button face (Arial), radius 20px, padding 8px 13px, no border; hover #203767. Gap 30px.
7. **Teaser** (y=339): a 900×377 image with no frame, radius or shadow.
8. **Caption** (y=730): 14.5px/1.5 #000000, justified, with bold-italic "noisy" and "clean" and coloured words rgb(248,176,185), rgb(160,210,236), rgb(227,112,140), rgb(111,155,210).
9. **Abstract head** (y=834): "ABSTRACT" 18.4px/700 #464646, letter-spacing 0.5px, then a 1px #d0d0d0 rule at y=866 with 14px below.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #fdfdfd | (literal, `body`) | page background |
| Ink | #111111 | (literal, `body`) | title, affiliation, venue, body defaults |
| Text | #1e1e21 | (literal) | abstract, section text, application subtitles |
| Head Gray | #464646 | (literal) | section heads (ABSTRACT, RESULTS, APPLICATIONS) |
| Steel Blue | #4e86c4 | (inline) | acronym initials in the title |
| Navy | #2c4a8a | (literal) | author links, all links, link buttons, footer email, icons |
| Navy Hover | #203767 | (literal) | link button hover |
| Rule Gray | #d0d0d0 | (literal) | section dividers |
| Footer Line | #e8e8e8 | (literal) | footer top border |
| Footer Head | #444552 | (literal) | footer list heads (CONTACT, INFO) |
| Code Well | #eeeeee | (literal) | BibTeX code background |
| Soft Pink / Sky Blue | #f8b0b9 / #a0d2ec | (inline) | caption words for the noisy input colours |
| Pink / Blue | #e3708c / #6f9bd2 | (inline) | caption words for the clean output colours |
| Control Gray | #555555 / #cccccc / #888888 | (literal) | active dot and clip labels / inactive dots / carousel arrows |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Body / headings | 'Inter', sans-serif | Inter 400, 600 (700 requests render with the 600 file) | Inter |
| Buttons | none set on `button` | browser default button face, Arial on Windows | Arial |
| Footer heads | "Roboto", sans-serif | Roboto not loaded; falls back to the system sans | Roboto |
| Code | Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title-wrapper #title` | 28px / 700 / 1.4, letter-spacing -0.378px | #111111, initials #4e86c4 |
| Authors | `.author-wrapper a` | 18px / 600 | #2c4a8a |
| Affiliation | `.author-wrapper #aff` | 17px / 400 | #111111 |
| Venue | `.pub-source-wrapper b` | 19px / 700 | #111111 |
| Section head | `.page-section-title` | 1.15em = 18.4px / 700, letter-spacing 0.5px | #464646 |
| Application subtitle | `.app-subtitle` | 1.05em = 16.8px / 600, letter-spacing 0.2px | #1e1e21 |
| Body text | `#abstract`, `.section-text` | 15px / 1.6, justified | #1e1e21 |
| Teaser caption | `.teaser-caption` | 14.5px / 400 / 1.5, justified | #000000 |
| Link button | `.link-button` | 15px / 400 | #ffffff |
| Clip label | `.compare-video-label`, `.grid2col-header` | 0.85em / 600 | #555555 |
| Footer head | `.footer-ui` | 15px / 700 / 1.6 | #444552 |
| BibTeX | `pre code` | 13.5px / 1.5 | #111111 on #eeeeee |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 20px | none | none |
| Carousels | 3px (overflow hidden) | none | none |
| Carousel dots | 50%, 8px | none | none |
| Teaser, videos | 0 | none | none |
| Section divider | — | 1px #d0d0d0 top, margin 0 0 14px | none |
| Footer | — | 1px #e8e8e8 top | none |
| BibTeX code | 0 | none | none; padding 10px |

## Layout Metrics

- **Container**: `.home-wrapper { max-width: calc(940px - 40px); padding: 0 30px }` renders 960px wide at x=240, content 900px (x=270 to 1170); the footer `.site-wrapper` is 940px max with 30px padding.
- **Header block**: page padding-top 45px; title margin-bottom 0.2em; author block margin-top 1.15em, bottom 0.4em; venue margin 19px 0; links row margin 0.9em 0 0.3em; teaser 30px below the buttons.
- **Sections**: `.page-section` margin-top 60px; head margin-bottom 10px; rule then 14px; text blocks margin-bottom 14px; application subtitles margin 28px 0 10px.
- **Media**: videos 100% wide at 16:9 (900×506); carousel controls row padding 10px 0 4px, gap 14px, dots 7px apart; two-up comparisons use 8px gaps.
- **Footer**: padding 30px 0, two lists (Contact left, Info right), 15px/1.6.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >800px | 30px | 15px | 28px | section text justified |
| 601–800px | 30px | 15px | 28px | teaser wrapper gets 30px side margins; section layouts stack |
| ≤600px | 30px | 15px | 24px | authors 16px, affiliation 15px, code 12px; two-up comparison grids stack and their headers hide |

## Components

- **Acronym title**: centred Inter 28px/700 in #111111, with the letters that spell the acronym coloured #4e86c4 via inline spans.
- **Author line**: 18px Inter 600 #2c4a8a links separated by two em-spaces, no underline; affiliation on its own line at 17px.
- **Navy pill button** (`.link-button`): #2c4a8a, white 15px text, radius 20px, padding 8px 13px, no border, 33px tall; hover #203767; four in a centred row with 18px gaps.
- **Ruled section head**: 18.4px/700 #464646 uppercase-text head with 0.5px tracking, 10px gap, then a full-width 1px #d0d0d0 rule and 14px space.
- **Video carousel**: 900px 16:9 autoplay videos in a 3px-radius clip, sliding 0.5s; below, gray ← → arrows (19.2px/700 #888888, hover #111111) around 8px dots (#cccccc, active #555555).
- **Colour-keyed caption**: justified 14.5px caption where colour names are written in the matching figure colour.
- **Footer**: 1px #e8e8e8 top rule, two lists with 15px/700 #444552 heads and a bold navy email link.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | absent from the source | no top bar or side nav |
| Title / authors / affiliation | yes | centred, steel-blue acronym initials, navy author links |
| Venue badge | present but non-standard | a bold 19px text line, not a pill |
| Link buttons | yes | four small navy pills |
| Teaser + caption | yes | frameless 900px render with a colour-keyed justified caption |
| Abstract | yes | ruled uppercase head, justified 15px text |
| Results carousels | yes | 16:9 video carousels with arrow-and-dot controls |
| Applications | yes | subsections with 16.8px/600 subtitles and videos |
| Video embed | yes | a 16:9 iframe |
| Results tables | absent from the source | results are videos |
| BibTeX | yes | #eeeeee code block |
| Footer | yes | contact and info lists |

## Adapting to Other Content

- **More authors**: keep 18px/600 navy links with em-space separators; when the line wraps, keep affiliations on a separate 17px line with superscript numbers.
- **A results table**: place it in the 900px column under a ruled head; 15px Inter, header 600 #464646, 1px #d0d0d0 rules, best value 600 #2c4a8a.
- **Long publication or news lists**: use 15px/1.6 rows with a 600 #2c4a8a date, separated by the same 1px #d0d0d0 rule, under an 18.4px head.
- **More results**: add another carousel with the same gray arrow-and-dot controls rather than a grid; keep videos at full column width.

## Do's and Don'ts

- Do keep a single 900px column and centre only the header block.
- Do colour only the acronym initials in the title; everything else in the header stays #111111 or navy.
- Do use the ruled uppercase section head for every section.
- Do let colour words in captions match the figure colours.
- Don't add frames, radii or shadows to the teaser and videos.
- Don't enlarge the buttons; they are small 15px navy pills.
- Don't introduce a second accent beyond navy and the steel-blue initials.

## Surfaces

Near-white #fdfdfd throughout, with no bands or cards; the only fills are the navy buttons and the #eeeeee BibTeX well; separation comes from 1px #d0d0d0 rules and the #e8e8e8 footer line.

## Imagery

Clean, bright renders of mannequin-like characters in pastel pink, blue, green and yellow clothing carrying and rotating furniture in white interiors, with orange and green callout boxes for noisy input and generated hands. Videos are 16:9 with large overlay text ("Input: Noisy MHOI Data", "4 Participants Rotating an Object").

## Layout

A centred header block, a full-column teaser, then Abstract, Results (two carousels), Applications (subsections with videos), video embed and BibTeX, each starting 60px below the last, then the footer. About 5,800px tall.

## Agent Prompt Guide

Quick colors: page #fdfdfd, ink #111111, text #1e1e21, head #464646, navy #2c4a8a (hover #203767), initials #4e86c4, rule #d0d0d0, footer line #e8e8e8.

1. "Build a centred header in a 900px column with 45px top padding: Inter 28px/700 title, line-height 1.4, letter-spacing -0.378px, #111111, with the acronym letters coloured #4e86c4; authors 18px/600 #2c4a8a separated by two em-spaces; affiliation 17px; venue 19px bold; then four pill buttons (#2c4a8a, white 15px, radius 20px, padding 8px 13px, gap 18px; hover #203767)."
2. "Make a ruled section head: Inter 18.4px/700 #464646, letter-spacing 0.5px, uppercase text, margin-bottom 10px, then a 1px #d0d0d0 rule with 14px below; body 15px/1.6 #1e1e21, justified."
3. "Create a video carousel: full-width 16:9 videos in a 3px-radius clip sliding over 0.5s; controls centred below with 14px gaps: arrows 19.2px/700 #888888 (hover #111111) and 8px round dots #cccccc, active #555555."

## Similar Pages

- Minimal single-column project pages from character-animation labs, built from a shared stylesheet and YAML content.
- Pages that colour the acronym letters inside the title instead of using a separate wordmark.

## Quick Start

```css
:root {
  --bg: #fdfdfd;
  --ink: #111111;
  --text: #1e1e21;
  --head: #464646;
  --navy: #2c4a8a;
  --navy-hover: #203767;
  --initials: #4e86c4;
  --rule: #d0d0d0;
  --footer-line: #e8e8e8;
  --code-bg: #eeeeee;
  --font: 'Inter', sans-serif;
  --column: 900px;
  --section-gap: 60px;
}
```

## Provenance

- **URL**: https://jiyewise.github.io/projects/MOCHI/
- **Paper**: MOCHI: Motion Enhancement of Collaborative Human-object Interactions (arXiv 2606.18243), Jiye Lee, Yonghun Choi, Jungdam Won (Seoul National University).
- **Venue**: SIGGRAPH 2026 (Journal Track), ACM TOG.
- **Selection reason**: the arXiv comment lists the venue as SIGGRAPH 2026 (ACM TOG) without an explicit acceptance word and links this project page.
- **Template credit**: none stated; the author's own shared `project_style.css` and `carousel.css`, with content loaded from YAML by `project.js`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), two additional computed-style probes, the 1440×900 and tall screenshots, and the two stylesheets read directly, on 2026-10-28.
