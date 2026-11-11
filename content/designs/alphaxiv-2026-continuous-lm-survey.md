# Continuous LM Survey Map — Style Reference

> A transit map pinned under a scholarly masthead, with a navy Newsreader title and violet italic words above a wall of pastel model cards strung along an indigo timeline track, and an abstract whose first sentence condenses out of noise.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (`tools/computed_style.py`, computed styles, platform fonts per node, first-viewport color share), full-page captures at 1440, 768 and 375, width probes at 1024 and 1280, a scrolled 1440 viewport with the contents rail showing and the abstract slider set to t = 0.45, a tooltip probe on the LangFlow card, a legend-filter probe, forced-hover probes, and a dark-scheme render (`prefers-color-scheme: dark`, which `theme.js` turns into `data-theme="dark"`). The stylesheet `site.css` and the scripts `theme.js`, `site.js`, `abstract.js` and `timeline.js` were fetched with curl. The page is hand-written HTML with one stylesheet built on CSS custom properties; the timeline is an inline SVG generated from the survey's TikZ figure. Newsreader and JetBrains Mono load from Google Fonts as variable fonts, and Inter is self-hosted (`assets/fonts/inter-latin.woff2`).

## Overview

A single 980px reading column on white, 2,847px tall at 1440, with a 34px theme toggle in the top right corner and no navbar. The hero is a two-line centred title in navy Newsreader at 46px, with "Continuous" and "Language Models" in violet #4f4bd6 italics. Four underlined violet author names sit on one line with grey superscripts, then a line of grey JetBrains Mono email addresses and three university logos (Penn, KAIST, University of Amsterdam). Below a lilac hairline, a numbered "Contents" list with a navy left rule sits beside three bracketed resource links, each over a small preview card: a GitHub repository card with an indigo bottom bar, a looping video of the paper map with a sky-blue bottom bar, and a stacked paper cover with pastel offset sheets. The first viewport ends in the top of a 1020px interactive timeline that bleeds 20px past the column on each side: two black-framed panels of 92 small pastel rounded cards (models above, image and video foundations below) hung on a navy axis with indigo year chips, a lavender "Continuous LM winter" band, dashed teal adaptation arrows and orange and blue corner dots. Further down are an abstract card with a rainbow top bar and a scrubbable denoising sentence, a collapsible survey table of contents, a dated news list, and a pale teal BibTeX box. Sections are divided only by 1px lilac rules.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 73.4%; lilac grey #d9d9e6 7.5% (timeline card outlines, rules and logo strokes anti-aliased together); mid lavender #a5a5c9 5.3% (title, links and card text); pale lavender #f6f4f8 4.9% (winter band and card fills); pale blue #e8ecf3 4.7% (one-hot, binary and month-chip fills); near-whites #fcfcfd 2.6%, #fdffff 1.1%, #fffffe 0.5%. The violet italics and indigo year chips are too small to form their own clusters.

Anatomy in DOM order. `.wrap` is `width: min(980px, calc(100% - 400px))` at ≥1280px, so the column runs x=230–1210; `.hero` adds 64px top padding.

1. **Theme toggle** (`button.theme-toggle`, absolute): 34×34px at x=1392, y=14; white, 1.5px #c4c1f3 border declared (renders 1px at 1×), radius 6px, 16px moon icon stroked #4f4bd6 at width 2.
2. **Title** (`h1.paper-title`, two `span`s set to block): Newsreader 46px / 52.9px, letter-spacing −0.9px, #1d1b5e, centred. Line 1 "A Survey on *Continuous* Diffusion" is weight 500 at y=64, x=397–1043; line 2 "and Flow *Language Models*" is weight 400 with a 5px top margin, y=122, x=470–970. The `em` words are italic 500 #4f4bd6. Gap 22px.
3. **Authors** (`p.author-row`, flex-wrap, gap 3px 22px): y=197, 35.7px line; names Newsreader 21px / 400 #4f4bd6, underlined 1px #c9c6fb with a 3px offset; superscripts 13.65px (0.65em) #626074 with 2px left margin. Row spans x=425–1014. Gap 4px.
4. **Emails** (`p.author-emails`, gap 2px 18px): y=236.5, JetBrains Mono 12px / 19.2px #626074, four addresses x=351–1089. Gap 20px.
5. **Affiliations** (`div.affiliations`, gap 14px 34px, `align-items: center`): y=276–328, three linked logos with a 10px JetBrains Mono #626074 superscript before each: Penn 109×40, KAIST seal 52×52, University of Amsterdam wordmark 210×24. Gap 26px.
6. **Directory rule and grid** (`div.project-directory`): 1px #c4c1f3 top border at y=354, padding 22px 0 12px, grid `0.72fr 1.6fr` with a 38px gap (292px and 650px).
   - **Contents** (`nav.project-contents`): h2 "Contents" Newsreader 23px / 600 #1d1b5e at y=377, 15px below it an `ol` with a 1px #1d1b5e left border and 20px left padding; four links Newsreader 19px / 28.5px #4f4bd6 underlined #c9c6fb with a 4px offset, 10px apart, y=430–578.
   - **Resources** (`div.project-resources`, grid `1.15fr 1.4fr 0.9fr`, gap 26px 24px, x=560–1210): bracketed labels "[GitHub Collection]", "[Explore the Map]", "[Read Survey]" in Newsreader 22px / 28.6px #4f4bd6 with a 1px dotted bottom border, at y=377; 12px below, the preview cards at y=418: repository card 200×162, map video card 244×156, paper cover 112×144.
7. **Timeline figure** (`figure.hero-figure.timeline-figure`, margin 30px −20px 0): starts at y=622, 1020px wide (x=210–1230); the italic "Continuous Language Models" heading at y=622 and the top panel from y=644 fill the rest of the viewport. The figure is 529px tall, ending at y=1152 after its caption.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | `--paper`, `--card` | page, repository and map cards, abstract box, toggle, play button, unchecked mode segments, tooltip, survey preview card |
| Ink | #23222e | `--ink` | body text, news text, subsection rows, tooltip body |
| Navy | #1d1b5e | `--navy` | title, h2 headings, Contents heading, survey rows, BibTeX code, t readout, mode labels, repository name, tooltip name, Contents left rules, toast and skip-link fill |
| Accent | #4f4bd6 | `--accent` | title italics, author links, contents links, resource labels, toggle and play icons, survey chevrons, "Read the full abstract", copy icon, email and footer link hover |
| Accent Strong | #24208f | `--accent-strong`, `--tl-navy` | link hover, links inside the abstract, tooltip link text; timeline axis, card labels, ticks and winter label |
| Accent Soft | #c9c6fb | `--accent-soft` | link underlines, mask glyphs in the Masked mode |
| Ink Soft | #3a3950 | `--ink-soft` | abstract paragraphs |
| Muted | #626074 | `--muted` | author and logo superscripts, emails, figure caption, section notes, footer, repository owner and caption, subsection numbers |
| Rule | #c4c1f3 | `--rule` | section top borders, directory rule, footer rule, toggle, play and mode-group borders, survey preview border, tooltip border, paper-sheet borders |
| Line | #e4e3ef | `--line` | repository and map card borders, news separators, compact contents pill border |
| Indigo | #6b67ee | `--indigo`, `.tl-year rect` | repository card bottom bar and language dot, abstract bar start, slider accent, checked mode segment, news dates, year chips, current-section bar in the rail |
| Lavender | #9793f8 | `--lavender` | abstract bar at 30%, noise candidates in the denoising sentence |
| Sky | #50b2d7 | `--sky` | map card bottom bar, abstract bar at 60% |
| Mint | #60c7ab | `--mint` | abstract bar end |
| Abstract Line | #d9d6fb | `--abstract-line` | abstract box border, abstract link underlines |
| Denoise Top | #f7f6fe | `--denoise-top` | top of the denoising block's vertical gradient |
| Surface | #f6f5fe | `--surface` | play and mode hover, expanded full abstract, tooltip tags, inline code in notes |
| Tint | #f3f2ff | `--tint` | toggle hover, legend hover |
| Tint 2 | #eae9fe | `--tint-2` | pressed legend entry |
| Tint Mint | #e5faf3 | `--tint-mint` | back sheet behind the paper cover (offset 10px) |
| Tint Lilac | #f9f0ff | `--tint-lilac` | middle sheet behind the paper cover (offset 5px) |
| Frame | #b9b6ea | `--frame` | paper cover border |
| Cite Background | #e1f2f6 | `--cite-bg` | BibTeX box; also the one-hot card fill |
| Cite Line | #56a3b4 | `--cite-line`, `--tl-arrow` | BibTeX box border, dashed timeline arrows, one-hot card outline |
| Cite Hover | #cbe6ed | `--cite-hover` | copy button hover |
| Tint Sky | #eef7fb | `--tint-sky` | month chips on the axis |
| Month Ink | #716faa | `--tl-month-ink` | month chip text |
| Panel Frame | #111111 | `--tl-frame` | 1.27-unit outline of both timeline panels |
| Panel Ink | #000000 | `--tl-ink` | timeline panel headings, legend text |
| Stem | #9a9ab8 | `--tl-stem` | thin stems from cards to the axis |
| Winter | #9180c7 | `.tl-winter` at fill-opacity 0.1 | "Continuous LM winter" band; also the vocabulary card outline |
| Few-step | #0072b2 | `--tl-few` | square corner marks for few-step / flow-map papers, linked arrows on hover |
| Guidance | #d55e00 | `--tl-guide` | round corner dots for guidance papers |
| Vocabulary | #eae7fb | `.f-vocabulary` | card fill (outline #9180c7) |
| Contextual | #e4f1e7 / #6a9a78 | `.f-contextual` | card fill / outline |
| Compressed | #fff1d6 / #bd9656 | `.f-compressed` | card fill / outline |
| Binary | #e4ecfb / #658fc4 | `.f-binary` | card fill / outline |
| Simplex | #f8e2ed / #bb7297 | `.f-simplex` | card fill / outline |
| Spherical | #f9e9de / #c28b62 | `.f-sphere` | card fill / outline |
| Foundation | #9a95bb | `.f-foundation` | white cards in the image and video panel, outline |
| Neutral | #8b8b9a | `.f-neutral` | white neutral cards, outline |
| Focus | #2c84ff | `--blue` | 3px focus outline, offset 4px |
| Dark Paper | #0f0e22 | dark `--paper` | page background in dark theme, toast text |
| Dark Card | #1a1938 | dark `--card`, `--tl-panel` | cards, abstract box, timeline panels, toggle in dark theme |
| Dark Surface | #171633 | dark `--surface` | hover fills in dark theme |
| Dark Ink | #d6d5ee | dark `--ink` | body text in dark theme |
| Dark Ink Soft | #c4c3e2 | dark `--ink-soft` | abstract paragraphs in dark theme |
| Dark Navy | #c8c6ff | dark `--navy` | title, headings and code in dark theme |
| Dark Accent | #aeacff | dark `--accent` | links and icons in dark theme |
| Dark Accent Strong | #dcdaff | dark `--accent-strong` | link hover in dark theme |
| Dark Muted | #9a98c4 | dark `--muted` | notes, caption, emails in dark theme |
| Dark Rule | #3c3a6e | dark `--rule`, `--abstract-line` | section rules and box borders in dark theme |
| Dark Line | #2a2950 | dark `--line` | card borders and news separators in dark theme |
| Dark Denoise Top | #1f1d44 | dark `--denoise-top` | denoising gradient top in dark theme |
| Dark Cite | #13283a / #50b2d7 | dark `--cite-bg` / `--cite-line` | BibTeX box fill / border in dark theme |
| Dark Panel Frame | #6b6994 | dark `--tl-frame` | timeline panel outlines in dark theme |
| Dark Panel Ink | #e4e3f7 | dark `--tl-ink` | timeline headings and legend in dark theme |
| Dark TL Navy | #d4d2ff | dark `--tl-navy` | timeline axis and card labels in dark theme |
| Dark Card Fill | #39345d | `color-mix(in srgb, var(--tl-line) 26%, var(--tl-panel))` | vocabulary card fill in dark theme (each family mixes its own outline color) |

## Tokens — Typography

| Family | Declared | Rendered (platform fonts) | Substitute |
|---|---|---|---|
| Serif (body, title, headings) | `--serif`: 'Newsreader', Georgia, 'Times New Roman', serif; `body { font: 18px/1.65 var(--serif) }` | Newsreader, an optical-size variable serif from Google Fonts (`ital,opsz,wght` 6..72, 300..700), `font-optical-sizing: auto`; rendered weights 400, 500, 600 roman and 500, 600 italic | none needed (load Newsreader from Google Fonts) |
| Mono (emails, controls, dates, BibTeX) | `--mono`: 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace | JetBrains Mono (variable 400..700 from Google Fonts); rendered 400, 500, 600 | none needed (load JetBrains Mono) |
| Sans (timeline, repository card, footer, tooltip) | `--sans`: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif | Inter, self-hosted variable woff2 (300..700); rendered 400, 500, 600 | Inter from Google Fonts (same family) |

`fonts_loaded`: JetBrains Mono 400–700, Newsreader 300–700 and 300–700 italic, Inter 300–700. Because every rendered family is itself on Google Fonts, no `font_fit.py` comparison was needed.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title line 1 | `.paper-title > span` | 46px / 500 / 52.9px, letter-spacing −0.9px, centred | #1d1b5e |
| Title line 2 | `.paper-title .title-sub` | 46px / 400 / 52.9px, margin-top 5px | #1d1b5e |
| Title italics | `.paper-title em` | 46px / 500 italic | #4f4bd6 |
| Author names | `.author-row a` | 21px / 400 / 35.7px, underline 1px #c9c6fb, offset 3px | #4f4bd6 |
| Author superscripts | `.author-row sup` | 13.65px (0.65em) / 400, line-height 0 | #626074 |
| Emails | `.author-emails a` | JetBrains Mono 12px / 400 / 19.2px | #626074 |
| Logo numbers | `.institution sup` | JetBrains Mono 10px / 1 | #626074 |
| Contents heading | `.project-contents h2` | 23px / 600 / 37.95px | #1d1b5e |
| Contents links | `.project-contents a` | 19px / 400 / 28.5px, underline #c9c6fb, offset 4px | #4f4bd6 |
| Resource labels | `.resource-label` | 22px / 400 / 28.6px, 1px dotted bottom border | #4f4bd6 |
| Repository owner | `.repository-owner` | JetBrains Mono 10px / 14px | #626074 |
| Repository name | `.repository-preview strong` | Inter 15px / 600 / 18.75px, letter-spacing −0.3px | #1d1b5e |
| Repository caption | `.repository-caption` | Inter 10px / 15px | #626074 |
| Repository language | `.repository-language` | JetBrains Mono 9px / 12.6px, 7px #6b67ee dot | #626074 |
| Timeline panel heading | `.tl-heading` | Newsreader 16px / 600 italic | #000000 |
| Winter label | `.tl-winter-label` | Newsreader 14px / 600 italic | #24208f |
| Card label | `.tl-label` | Inter 10.2px / 500 (viewBox units, 1.054× at 1440) | #24208f |
| Year chip | `.tl-year text` | Inter 10.2px / 700 | #ffffff on #6b67ee |
| Month chip | `.tl-month text` | Inter 10.2px / 500 italic | #716faa on #eef7fb |
| Legend | `.tl-legend text` | Inter 11.4px / 400 | #000000 |
| Figure caption | `.hero-figure figcaption` | 16px / 400 / 24.8px | #626074 |
| Section heading | `h2.section-heading` | 32px / 600 / 40px, letter-spacing −0.55px | #1d1b5e |
| Section note | `.section-note` | 16px / 400 / 26.4px | #626074 |
| Denoising sentence | `.denoise-text` | 27px / 400 / 37.8px, letter-spacing −0.2px | #1d1b5e |
| Time readout | `.denoise-t` | JetBrains Mono 12px / 500, tabular numbers | #1d1b5e |
| Mode segment | `.denoise-modes span` | JetBrains Mono 12px / 500 / 14.4px | #1d1b5e, #ffffff when checked |
| Abstract paragraphs | `.abstract-copy p` | 18px / 400 / 29.7px | #3a3950 |
| Full-abstract toggle | `.abstract-full summary` | JetBrains Mono 12px / 500 / 21.6px | #4f4bd6 |
| Survey row | `.stoc summary`, `.stoc-row` | 20px / 400 / 29px | #1d1b5e |
| Survey subsection | `.stoc-sub` | 17px / 400 / 24.65px; third level 16px | #23222e; third level #626074 |
| News date | `.news-list time` | JetBrains Mono 12px / 600 / 19.2px | #6b67ee |
| News text | `.news-list p` | 18px / 400 / 29.7px | #23222e |
| BibTeX | `.citation-box pre` | JetBrains Mono 13px / 21.45px, pre-wrap | #1d1b5e |
| Footer | `footer` | Inter 12px / 400 / 19.2px | #626074 |
| Tooltip name / title / meta | `.tl-tip strong`, `.tip-title`, `.tip-meta` | Newsreader 17px / 600; Newsreader 14px / 19.6px; Inter 11.5px | #1d1b5e; #23222e; #626074 |
| Rail links | `.contents-list a` | 15px / 400, 42px rows; current 600 | #4f4bd6; current #1d1b5e |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Theme toggle | 6px | 1.5px solid #c4c1f3 declared, 1px at 1× | none |
| Repository card | 0 | 1px #e4e3ef, bottom 4px #6b67ee | `0 2px 8px #1d1b5e08`; hover `0 6px 18px #1d1b5e14` and translateY(−2px) |
| Map card | 0 | 1px #e4e3ef, bottom 4px #50b2d7 | same as the repository card |
| Paper cover | 0 | 1px #b9b6ea | `0 1px 4px #1d1b5e26`; two `::before`/`::after` sheets with 1px #c4c1f3 borders and `0 1px 3px #1d1b5e16`, offset 5px and 10px |
| Timeline card | rx 1.81 (viewBox units) | 0.91 outline in the family color; 1.9 on hover | hover `drop-shadow(0 2px 3px #1d1b5e33)` |
| Year chip | square | none | none |
| Abstract box | 8px (overflow hidden) | 1px #d9d6fb | none; 5px `linear-gradient(90deg, var(--indigo), var(--lavender) 30%, var(--sky) 60%, var(--mint))` bar on top |
| Play button | 50% | 1px #c4c1f3 | none |
| Mode group | 6px | 1px #c4c1f3, 1px dividers | none |
| Expanded full abstract | 6px | none | none |
| Survey preview card | 6px | 1px #c4c1f3 | none |
| Tooltip | 6px | 1px #c4c1f3, top 3px in the card's family color | `0 10px 28px #1d1b5e24` |
| Tooltip link | 5px | 1px #c4c1f3 | none |
| BibTeX box | 6px | 1px #56a3b4 | none |
| Copy button | 0 | none | none |
| Toast | 7px | none | none |
| Compact contents pill (<1280px) | 24px | 1px #e4e3ef | `0 3px 16px #1d1b5e14` |

## Layout Metrics

- **Container**: `.wrap { width: min(980px, calc(100% - 64px)) }`, overridden at ≥1280px to `min(980px, calc(100% - 400px))` and at ≤760px to `calc(100% - 32px)`. At 1440 the column is 980px at x=230–1210.
- **Hero**: padding-top 64px. Title 64–175 (52.9 + 5 + 52.9), margin 22px → authors 197–232.7, 4px → emails 236.5–255.7, 20px → logos 275.7–327.7, 26px → directory rule 353.7, 22px padding → contents and resources at 376.7, directory bottom 592.4 (12px padding), 30px → figure 622.4–1151.8.
- **Directory grid**: `0.72fr 1.6fr`, gap 38px → 292 + 650px. Resources grid `1.15fr 1.4fr 0.9fr`, gap 26px 24px → 200.5, 244.1 and 157px columns; label to card gap 12px.
- **Timeline figure**: `width: calc(100% + 40px); margin: 30px -20px 0`, so 1020px at x=210. The SVG has `viewBox="0 0 968 444"` and `min-width: 880px`; it renders 1020×468 (scale 1.054). Top panel 1008×168 at y=644, axis at about y=826, bottom panel 1008×172 at y=842, winter band x=503–718 across both panels, legend rows at y=1046 and 1068 (four family columns at x=210, 381, 565, 825 and the two marker keys at x=1066). Caption 12px below the SVG with 20px inline padding, so its text lines up with the column.
- **Sections**: `.text-section, .bibtex-section { padding-block: 30px; border-top: 1px solid var(--rule) }`; the first one has a 36px top margin (abstract at 1187.8). Heading 40px tall with 18px bottom margin. Abstract 1187.8–1667.7, Survey Contents 1667.7–2200.1, News 2200.1–2415.5, BibTeX 2415.5–2775, footer 2775–2847.
- **Abstract box**: 980×361 at y=1277; denoising block padding 24px 30px 18px (sentence box 918px, two lines at 1440), controls row `flex-wrap`, gap 10px 16px (play 34px, readout 62px, slider 494px, mode group 286×30); copy padding 4px 30px 18px, paragraphs 12px apart.
- **Survey list**: `.stoc > ol` width 56% (549px) with a 1px #1d1b5e left border and 20px padding; nine 41px rows (6px padding), seven with a 20px chevron at the right end (x=759); subsections indent 28px and run 31px per row. The hover preview card is `clamp(300px, 38vw, 380px)` wide, placed 28px right of the list (x=807); for the last three rows it opens upward.
- **News**: grid `130px 1fr`, gap 18px, 12px vertical padding, 1px #e4e3ef separators.
- **BibTeX box**: full column, padding 22px 52px 22px 22px, copy button 36×36 at top 8px, right 8px.
- **Contents rail** (≥1280px): fixed, `left: max(12px, calc((100vw - 980px) / 2 - 204px))` (26px at 1440), 164px wide, vertically centred; appears once `scrollY > 120`. Heading 20px / 600 #1d1b5e, list with a 1px #1d1b5e left border and 12px padding, links in 42px rows, the current one 600 #1d1b5e with a 3px #6b67ee bar 14px left of it.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1380px (incl. 1440) | (viewport − 980)/2, 230px at 1440 | 18px | 46px | contents beside resources; figure bleeds 20px; side rail |
| 1280–1379px | 200px | 18px | 46px | column shrinks (880px at 1280); rail at 12px |
| 1001–1279px | max(32px, (viewport − 980)/2), 32px at 1024 | 18px | 46px | rail becomes a bottom-left "Contents" pill (44px tall, radius 24px, 20px from the edges) |
| 901–1000px | 32px | 18px | 46px | figure stops bleeding (100% width); timeline scrolls sideways below 880px plus padding |
| 761–900px | 32px | 18px | 46px | directory stacks; resources capped at 560px and left-aligned; survey list full width, previews open inline |
| 521–760px | 16px | 18px | 30px | hero padding 40px; authors 19px; h2 27px; sentence 22px; news dates above text |
| ≤520px | 16px | 18px | 26px | resources 2 columns with GitHub and Map spanning both; labels 20px; BibTeX padding 48px 16px 16px, 12px code |

No width from 375 to 1440 scrolls the page sideways (scrollWidth equals the viewport); only the timeline scroller does (912px of content in a 375px box).

## Components

- **Bracketed resource link**: a centred flex column; a Newsreader 22px #4f4bd6 label in square brackets with a 1px dotted bottom border (solid and #24208f on hover), 12px above a preview card. The repository card is white with a 1px #e4e3ef border and a 4px #6b67ee bottom bar, padding 14px 15px 10px, a 25px GitHub mark, a 10px mono owner line, a 15px / 600 Inter repository name broken over two lines, a 10px Inter caption and a 9px mono "Awesome list" tag after a 7px #6b67ee dot; it lifts 2px on hover. The map card is the same frame with a #50b2d7 bar around a muted looping video (paused under reduced motion). The paper cover is a 112px-wide image with a #b9b6ea border and two pastel sheets (#f9f0ff at 5px, #e5faf3 at 10px) behind it.
- **Timeline card**: SVG rect, rx 1.81, family fill with a 0.91 outline of the family color, an Inter 10.2px / 500 #24208f label shrunk to fit 54 units; optional 6px orange #d55e00 dot or blue #0072b2 square on the top right corner. Hover or focus thickens the outline to 1.9 with a navy-tinted drop shadow, fades unrelated arrows to 0.22 and draws linked ones in #0072b2 at width 2.
- **Timeline tooltip**: 300px max, white, 1px #c4c1f3 border with a 3px top border in the card's family color, radius 6px, padding 10px 13px 11px, shadow `0 10px 28px #1d1b5e24`; Newsreader 17px / 600 name, 14px paper title, 11.5px #626074 author and date lines, then pill links ("arXiv ↗", "alphaXiv ↗", "Code ↗") 25px tall with 1px #c4c1f3 borders, radius 5px, #24208f text, #f6f5fe hover.
- **Legend entry**: 19.6×10.9 swatch in the family fill and outline, Inter 11.4px #000000 label; clicking toggles `aria-pressed`, fills the hit area #eae9fe with a #6b67ee outline and dims every non-matching card to 0.16 opacity.
- **Denoising abstract**: white box, 8px radius, 1px #d9d6fb border, 5px rainbow top bar. The first sentence plays once over 4s when 60% of it is visible: in Continuous mode each word fades from 0.24 opacity while three overlapping candidate words fade out; Masked mode shows ▒ glyphs in #c9c6fb that resolve word by word; Autoregressive reveals words left to right. Controls: a 34px round play button (1px #c4c1f3, #4f4bd6 triangle, #f6f5fe hover), "t = 1.00" in 12px mono, a native range slider with `accent-color` #6b67ee, and a three-part segmented control (1px #c4c1f3, radius 6px, padding 7px 11px, checked #6b67ee with white text).
- **Survey table of contents**: `details` rows in Newsreader 20px #1d1b5e with tabular numbers and a #4f4bd6 chevron that turns 180° when open; hover turns the row #4f4bd6 and, for five sections, shows a 380px white figure card with a 1px #c4c1f3 border and 8px padding beside the list.
- **News row**: 130px JetBrains Mono 12px / 600 #6b67ee date column, Newsreader 18px text, violet underlined links, 1px #e4e3ef separators.
- **BibTeX box**: #e1f2f6 fill, 1px #56a3b4 border, radius 6px, JetBrains Mono 13px #1d1b5e code that wraps; a borderless 36px copy button with a 22px outline icon in #4f4bd6 (hover #cbe6ed); a #1d1b5e toast "BibTeX copied" in 13px Inter white, radius 7px, padding 12px 22px, 25px from the bottom, for 3s.
- **Theme toggle**: 34px square, radius 6px, #c4c1f3 border, white fill (#f3f2ff on hover), moon icon in light mode and sun icon in dark mode; the choice is stored under `clm-theme` and otherwise follows the system setting.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | No (absent from the source) | a fixed contents rail appears after scrolling instead |
| Title / authors / affiliations | Yes | navy two-line serif title with violet italics, underlined violet names, mono emails, three logos |
| Link buttons | Present but non-standard | three bracketed serif labels over preview cards (repository card, map video, paper cover) |
| Venue badge | No (absent from the source) | the survey is an alphaXiv preprint; only the BibTeX and news mention alphaXiv |
| Contents | Yes | numbered list with a navy left rule in the hero, plus the scroll-aware rail |
| Teaser | Present but non-standard | the interactive SVG timeline of 92 models, full bleed of the column |
| Abstract | Yes | rainbow-barred card with the scrubbable denoising sentence and a collapsible full abstract |
| Method / results figures | No (absent from the source) | figures only appear as hover previews in the survey contents |
| Paper outline | Yes | collapsible survey table of contents with figure previews |
| Video | Present but non-standard | a muted looping map preview inside the resource card |
| News | Yes | dated two-column list |
| BibTeX | Yes | pale teal box with an icon copy button and toast |
| Footer | Yes | Inter 12px line, title and year on the left, "Paper list on GitHub" on the right |

## Adapting to Other Content

- **More authors**: keep the centred flex-wrap row with 22px column gaps and 21px names; at 1440 the 760px author block wraps after about four names, adding 35.7px per line, and the emails wrap the same way at 19.2px per line.
- **More affiliations**: add logos to the centred row with 34px gaps and 14px row gaps; keep them 40px tall (seals 52px) and number each with the 10px mono superscript.
- **A results table**: put it in a `.text-section` under its own 32px heading, in the 980px column; use Inter 12px or JetBrains Mono 12px for numbers on white with 1px #e4e3ef row rules, matching the news separators.
- **Long publication or news lists**: extend the news grid (130px date column, 18px gap, 1px #e4e3ef separators), newest first.
- **No timeline figure**: drop the 1020px figure; the hero then ends at y=592 and the abstract section starts at y=628 (36px margin). If a static teaser exists, place it in the same `calc(100% + 40px)` bleed with a 16px #626074 caption 14px below.
- **No interactive abstract**: keep the box (1px #d9d6fb, radius 8px, 5px rainbow bar) and start the copy with the first paragraph; the box loses the 168px denoising block and its text starts 10px below the box's top edge (1px border + 5px bar + 4px padding), at x=261 and 918px wide at 1440.
- **No resource previews**: keep the bracketed 22px labels in a row to the right of Contents without cards; the directory stays 239px tall because the 202px Contents list sets its height, so the figure does not move.
- **No logos**: write affiliations as one 16px #626074 Newsreader line under the emails, 20px below them, with the same 1, 2, 3 mono superscripts.

## Do's and Don'ts

- Do keep one navy (#1d1b5e) for headings and one violet (#4f4bd6) for links and the italic title words; hover darkens links to #24208f.
- Do keep the three-family split: Newsreader for reading and headings, JetBrains Mono for small technical text (emails, dates, controls, code), Inter only inside the timeline, repository card, tooltip and footer.
- Do keep the timeline's colors tied to its legend; each representation family has one fill and one outline, and the tooltip's top border repeats that outline.
- Do divide sections with 1px #c4c1f3 rules and 30px padding, not bands.
- Don't put the theme toggle where the title can reach it on phones; at 375px the 34px toggle covers 7px of the end of "Diffusion".
- Don't use #6b67ee for 12px text you need readable; the news dates reach 4.38:1 on white and 4.34:1 on #0f0e22.
- Don't add shadows to the reading surfaces; only the preview cards, tooltip, toast and contents pill carry them.

## Surfaces

White page; white preview cards with #e4e3ef borders and colored 4px bottom bars; a white abstract box with a #f7f6fe → white vertical wash behind the sentence; #f6f5fe for the expanded abstract; a #e1f2f6 BibTeX box; white timeline panels framed in #111111 with a 10% #9180c7 winter band. In the dark theme the page is #0f0e22, cards and timeline panels #1a1938, rules #3c3a6e, text #d6d5ee, headings #c8c6ff, links #aeacff, the BibTeX box #13283a with a #50b2d7 border, and timeline card fills mix 26% of each outline color into the panel (#39345d for vocabulary). The university logos and GitHub mark are flattened by `filter: brightness(0) invert(.88)`, so the Penn shield and KAIST seal become pale grey silhouettes; the map video and paper cover stay as light images on the dark page.

## Imagery

No photographs. The signature graphic is the inline SVG timeline with pastel rounded cards, dashed teal arrows and colored corner marks. The other images are the three university logos (SVG), a GitHub mark, a looping screen recording of the paper map (light page, scattered blue nodes) and the first page of the survey PDF as a cover thumbnail. The survey contents show figure thumbnails from the paper on hover.

## Layout

Centred 980px column: title, authors, emails and logos centred; a two-column directory (Contents list and three resource previews) under a lilac rule; a 1020px timeline figure with legend and caption; then left-aligned sections (Abstract card, Survey Contents list at 56% width, News, BibTeX) each opened by a 1px rule; a two-ended Inter footer. A fixed contents rail sits in the left margin at ≥1280px. Rendered height 2,847px at 1440.

## Agent Prompt Guide

Quick colors: page #ffffff, text #23222e, headings #1d1b5e, links and italics #4f4bd6, hover #24208f, underline #c9c6fb, muted #626074, rules #c4c1f3, card borders #e4e3ef, indigo #6b67ee, abstract bar #6b67ee → #9793f8 → #50b2d7 → #60c7ab, BibTeX #e1f2f6 with #56a3b4. Dark theme page #0f0e22, cards #1a1938, text #d6d5ee, headings #c8c6ff, links #aeacff.

1. "Build a centred hero in a 980px column: a two-line Newsreader title at 46px with −0.9px letter-spacing in #1d1b5e, first line weight 500 and second line 400, with two phrases set in italic 500 #4f4bd6; 22px below, author names in Newsreader 21px #4f4bd6 underlined 1px #c9c6fb with 3px offset, 22px apart, with 13.65px #626074 superscripts; then JetBrains Mono 12px #626074 emails 18px apart, and a row of 40px logos 34px apart."
2. "Make an abstract card: white, 1px #d9d6fb border, radius 8px, overflow hidden, with a 5px top bar `linear-gradient(90deg, #6b67ee, #9793f8 30%, #50b2d7 60%, #60c7ab)`; inside, a 27px Newsreader #1d1b5e sentence over a #f7f6fe → #ffffff wash with padding 24px 30px 18px; a control row with a 34px round play button (1px #c4c1f3 border, #4f4bd6 icon), a 12px / 500 JetBrains Mono 't = 1.00' readout, a range slider with accent #6b67ee, and a segmented control of three 12px mono options with 1px #c4c1f3 borders, radius 6px, padding 7px 11px, the checked one #6b67ee with white text; then 18px / 29.7px #3a3950 paragraphs."
3. "Make a resource preview: a Newsreader 22px #4f4bd6 label in square brackets with a 1px dotted bottom border, 12px above a white card with a 1px #e4e3ef border, a 4px #6b67ee bottom border and shadow 0 2px 8px #1d1b5e08, padding 14px 15px 10px, holding a 25px GitHub mark, a 10px JetBrains Mono #626074 owner line, a 15px / 600 Inter #1d1b5e repository name and a 10px Inter caption; on hover it lifts 2px with shadow 0 6px 18px #1d1b5e14."

## Similar Pages

- The site's own paper map at `map/`, which the "[Explore the Map]" card previews, and the blog whose palette the dark theme says it reuses; their styling was not checked here.
- Survey and awesome-list landing pages that pair a curated GitHub paper list with an interactive timeline of models.

## Quick Start

```css
@import url("https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,500;1,6..72,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap");
:root {
  --paper: #ffffff;
  --ink: #23222e;
  --ink-soft: #3a3950;
  --navy: #1d1b5e;
  --accent: #4f4bd6;
  --accent-strong: #24208f;
  --accent-soft: #c9c6fb;
  --muted: #626074;
  --rule: #c4c1f3;
  --line: #e4e3ef;
  --indigo: #6b67ee;
  --lavender: #9793f8;
  --sky: #50b2d7;
  --mint: #60c7ab;
  --surface: #f6f5fe;
  --abstract-line: #d9d6fb;
  --cite-bg: #e1f2f6;
  --cite-line: #56a3b4;
  --serif: "Newsreader", Georgia, "Times New Roman", serif;
  --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  --mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
  --column: 980px;
  --title-size: 46px;
  --heading-size: 32px;
  --body: 18px;
  --radius-box: 8px;
  --radius-small: 6px;
  --bar: linear-gradient(90deg, #6b67ee, #9793f8 30%, #50b2d7 60%, #60c7ab);
}
:root[data-theme="dark"] {
  --paper: #0f0e22;
  --ink: #d6d5ee;
  --ink-soft: #c4c3e2;
  --navy: #c8c6ff;
  --accent: #aeacff;
  --accent-strong: #dcdaff;
  --muted: #9a98c4;
  --rule: #3c3a6e;
  --line: #2a2950;
  --surface: #171633;
  --abstract-line: #3c3a6e;
  --cite-bg: #13283a;
  --cite-line: #50b2d7;
}
```

## Provenance

- **URL:** https://continuous-lm.github.io/
- **Paper:** A Survey on Continuous Diffusion and Flow Language Models, Sophia Tang, Chanhyuk Lee, Floor Eijkelboom, Jinwoo Kim (University of Pennsylvania, KAIST, University of Amsterdam). Paper list: github.com/sophtang/Awesome-Continuous-Language-Models.
- **Venue:** a survey preprint posted on alphaXiv on 2026-11-09 (the page's news list; BibTeX `@article` with publisher alphaXiv, year 2026, URL alphaxiv.org/abs/2611.continuous-diffusion-flow-language-models). It has not been accepted at a venue.
- **Selection reason:** added on the maintainer's suggestion (2026-11-12), outside the two-round design selection. The page is for a survey preprint on alphaXiv, so it falls outside the gallery's venue rules and was not judged in the design rounds.
- **Template credit:** none stated; hand-written HTML with one `site.css` built on CSS custom properties ("Palette taken from the survey figures"), three small scripts, and a timeline SVG generated by the authors' `scripts/build_timeline.py` from the survey's TikZ figure.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share; the 1440×900 and 1440×2700 captures; full-page captures at 1440, 768 and 375; DevTools probes of computed styles, platform fonts, forced hover states, the scrolled contents rail, the slider at t = 0.45, a timeline tooltip and a legend filter, widths 375–1440 and the dark theme; `site.css`, `theme.js`, `site.js`, `abstract.js` and `timeline.js` via curl; 2026-11-12.
