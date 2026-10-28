# Think Before You Move — Style Reference

> A clean lab notebook with two highlighters: amber marks what the model thinks, blue marks what it does, and everything else is ink on white.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles, loaded fonts, first-viewport color share, DOM anatomy), the 1440×900 and full-page screenshots, a second in-browser probe of below-the-fold elements (TL;DR, stat cards, callout, findings, method, tables, BibTeX), and the page's own `static/css/index.css`, `static/js/index.js` and `index.html` read directly. The probe browser had a 15px scrollbar, so its x positions sit 7px left of the tool's; x positions below are the tool's (content column starts at x=174). Section-nav highlighting (`a.active`) is set by an IntersectionObserver only after scrolling, so no link is active in the first-viewport render; the full-page screenshot shows "Overview" active.

## Overview

A long (16,137px) single-column project page in the system UI font (Segoe UI on Windows) on white, built from bands that alternate between #ffffff and a pale cool gray #f6f7f9, each with 76px vertical padding. The ink is near-black #141821 for headings and buttons and slate #2c323d for body text. Two semantic accents carry the paper's idea and recur in every module: amber (#e0a722 bars, #9a6a06 text on #fcf3dd) for "reasoning", and blue (#4a78c2 bars, #2f5a9e text on #e8eef8) for "execution". A third pair, blue #245fc2 and orange #c2410c, colors keywords inside motion prompts, and green #17803d marks "ours". The hero is centred: a cream venue pill, a 52px/800 title with a 62px robot mascot inline, a 31.2px subtitle line, authors, affiliations, then near-black pill buttons. Below it sit four square motion videos with prompt captions, a gray TL;DR band with highlighted tokens and four stat cards, the abstract, a two-column motivation block with an amber callout, findings cards, a method equation with an animated token stream, tabbed video comparisons, white tables with a green "ours" row, a user-study bar chart, a gallery and a dark BibTeX block.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 85.3%, #cbcccd 4.5% (video frame borders, gray mannequins and antialiased text), #fbf9f6 2.6% (venue pill and the beige mannequin renders), #5d5c64 2.5% (dark text and the three filled buttons, blended), #f0f1f2 2.4% (nav bottom rule, ghost button, clip borders), #fdfdfe 1.9%, #feffff 0.7%, #fffffe 0.1%. Amber, blue and orange cover too little area to form clusters.

Anatomy in DOM order (1440px, hero centred):

1. **Sticky section nav** (`nav.topnav`, 0–57px): rgba(255,255,255,0.92) with `backdrop-filter: saturate(160%) blur(10px)` and a 1px #e3e6eb bottom border; inner `.wrap` is a 56px flex row, gap 18px. Left: 28×28 mascot icon plus "LMR" 17px/800, letter-spacing 0.34px, #141821, at x=174, y=14. Right (margin-left auto): ten links from x=400 to x=1266, 14.08px/400 #586070, padding 6px 10px, radius 8px, 2px apart. Hover and active: #141821 on #f6f7f9; active adds weight 650.
2. **Hero** (`header.hero`, 57–547px): padding 60px 0 26px, transparent (white page shows), text-align center.
3. **Venue pill** (`.venue-badge`, y=117, 154×38): "IEEE TPAMI 2026", 14.4px/750, letter-spacing 0.432px, #9a6a06 on #fcf3dd, 1px #efd7a2 border, padding 6px 16px, radius 999px. Gap 20px (title margin-top).
4. **Title** (`h1.title`, y=175, 1000px wide at x=220, 108px tall): first line "Think Before You Move:" 52px/800, line-height 58.24px, letter-spacing -1.3px, #141821, preceded by a 62×62 mascot image (`.title-logo`, 1.2em, vertical-align -0.26em, x=388, y=176). Second line `.title-sub` at y=248: "Latent Motion Reasoning for Text-to-Motion Generation", 31.2px/650 (0.6em), letter-spacing -0.374px, #2c323d, margin-top 9.36px. Gap 24px (authors margin-top; the title's 8px bottom margin collapses into it).
5. **Authors** (`p.authors`, y=307, 920px max at x=260, two lines, 57px): 17.28px/400, line-height 28.5px, #141821; each name in a nowrap span with superscript markers (1,* and 1,† style). Gap 8px.
6. **Affiliations** (`p.affils`, y=372, 52px): flex-wrap centred, gap 2px 20px, 15.2px #586070, two rows. Gap 6px.
7. **Notes** (`p.notes`, y=430): "*Equal contribution   †Corresponding author", 13.6px #868d99. Its 13.6px bottom margin collapses into the 24px top margin of the button row.
8. **Link buttons** (`.links`, y=476, 45px tall): Paper, arXiv, Code as filled pills (98px wide each) and BibTeX as a ghost pill (110px), 10px gap, x=503–937. Hero padding-bottom 26px ends the hero at 547.
9. **Teaser** (`section.teaser`, from 547, padding 14px 0 60px): four 260px-wide square clips at x=174, 452, 729, 1007 (18px gap), y=561–821, each a 1px #e3e6eb framed white box with a looping mannequin video; prompt captions start at y=831 (10px below) and run past the fold. The teaser caption line sits at y=915.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #141821 | --ink | title, h2–h4, author names, nav brand, filled buttons and selected tabs (fill and border), stat values, table headers, prompt lines, callout text |
| Body Slate | #2c323d | --body | body text, title subtitle line, clip prompt captions |
| Muted Slate | #586070 | --muted | nav links, affiliations, lead paragraphs, stat labels, figure captions, teaser caption, unselected tabs, card text, reference rows in tables |
| Faint Gray | #868d99 | --faint | notes line, stat detail, table group labels, table notes, clip-head small text, footer |
| Hairline | #e3e6eb | --line | nav bottom rule, ghost button border, clip frames, stat cards, cards, table wrap, details, footer top rule |
| Paper | #ffffff | --bg | page, hero, plain bands, cards, clip boxes, table wraps |
| Alt Band | #f6f7f9 | --bg-alt | alternating sections (TL;DR, Findings, Comparisons, Latent vs. Language, Gallery), nav hover/active fill, ghost hover |
| Reasoning Amber | #e0a722 | --reason | callout left bar, reasoning tokens in the stream, 3px underline under the reasoning term in the equation, legend dot |
| Reasoning Ink | #9a6a06 | --reason-ink | venue pill text, eyebrow labels, `.mark-r` text, equation "Reasoning · System 2" label |
| Reasoning Soft | #fcf3dd | --reason-soft | venue pill fill, `.mark-r` highlight, callout fill |
| Venue Border | #efd7a2 | (literal, `.venue-badge`) | 1px venue pill border |
| Execution Blue | #4a78c2 | --exec | execution tokens, equation execution underline, user-study bar fill, focus outline |
| Execution Ink | #2f5a9e | --exec-ink | links, `.mark-e` text, finding tags, equation "Execution · System 1" label |
| Execution Soft | #e8eef8 | --exec-soft | `.mark-e` highlight, finding tag fill |
| Keyword Blue | #245fc2 | --kw1 | `em.k1` keywords in prompts |
| Keyword Orange | #c2410c | --kw2 | `em.k2` keywords in prompts |
| Ours Green | #17803d | --ok | 2px frame and head label of "LMR (ours)" clips, ✓ verdicts |
| Ours Soft | #ebf6ef | --ok-soft | table row for LMR |
| Bad Red | #c2412f | --bad | ✗ verdicts under baseline clips |
| Button Hover | #2e3544 | (literal, `.btn:hover`) | filled button hover |
| Table Head | #fafbfc | (literal) | `thead th` fill |
| Group Row | #fcfcfd | (literal) | `tr.group th` fill |
| Row Rule | #eef0f3 | (literal) | 1px bottom rule between table rows |
| Dashed Gray | #c9ced6 | (literal) | dashed border of the "text prompt" chip in the stream, tab hover border |
| Bar Track | #e9ecf1 | (literal) | user-study bar track |
| Bar Midline | #8f97a3 | (literal) | 2px dashed 50% line on bar tracks |
| Code Night | #111722 | (literal, `.bib pre`) | BibTeX block |
| Code Text | #e6e8ec | (literal) | BibTeX text and copy button text |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "PingFang SC", "Microsoft YaHei", sans-serif | no web text font; the OS UI face renders (Segoe UI on Windows, SF Pro on macOS) | Inter |
| Code | ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace | system monospace (Consolas on Windows) | JetBrains Mono |
| Equation | "Cambria Math", Cambria, "Times New Roman", serif | system Cambria Math | STIX Two Math |
| Icons | Font Awesome (SVG via JS) and Academicons | Academicons 400 is the only loaded webfont; Font Awesome replaces `<i>` with inline SVG | — |

Root size is 16px, so rem values resolve against 16px while body text is 17px.

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title` | clamp(2.1rem, 4.6vw, 3.25rem) → 52px / 800 / 1.12, letter-spacing -0.025em | #141821 |
| Title subtitle | `.title-sub` | 0.6em → 31.2px / 650 / 1.12, letter-spacing -0.012em | #2c323d |
| Section heading | `h2` | clamp(1.65rem, 2.8vw, 2.15rem) → 34.4px / 750 / 1.25, letter-spacing -0.015em | #141821 |
| Abstract heading | `.abstract-title` | 1.35rem → 21.6px / 750 | #141821 |
| Subsection | `h3` | 1.28rem → 20.48px / 700 / 1.25, margin-top 2.6rem | #141821 |
| Card / table sub-heading | `h4` | 1.02rem → 16.32px / 700 | #141821 |
| Eyebrow | `.eyebrow` | 0.78rem → 12.48px / 700 uppercase, letter-spacing 0.1em | #9a6a06 |
| Body | `body` | 17px / 400 / 1.65 | #2c323d |
| Lead | `.lead` | 1.08rem → 17.28px / 400 | #586070 |
| TL;DR sentence | `.tldr` | clamp(1.12rem, 1.8vw, 1.3rem) → 20.8px / 400 / 1.6 | #141821 |
| Token highlight | `.mark-r`, `.mark-e` | inherits 20.8px / 650 | #9a6a06 / #2f5a9e |
| Venue pill | `.venue-badge` | 0.9rem → 14.4px / 750, letter-spacing 0.03em | #9a6a06 |
| Authors | `.authors` | 1.08rem → 17.28px / 400 | #141821 |
| Affiliations | `.affils` | 0.95rem → 15.2px | #586070 |
| Notes | `.notes` | 0.85rem → 13.6px | #868d99 |
| Button | `.btn` | 0.95rem → 15.2px / 650 | #ffffff on #141821; ghost #141821 |
| Nav link | `.topnav-links a` | 0.88rem → 14.08px / 400 | #586070 |
| Stat value | `.stat-value` | 2rem → 32px / 800 / 1.1, letter-spacing -0.02em | #141821 |
| Stat label | `.stat-label` | 0.88rem → 14.08px / 1.4 | #586070 |
| Stat detail | `.stat-detail` | 0.82rem → 13.12px, tabular numbers | #868d99 |
| Finding tag | `.finding-tag` | 0.8rem → 12.8px / 700 | #2f5a9e |
| Figure caption | `.figure figcaption` | 0.9rem → 14.4px / 1.55 | #586070 |
| Clip prompt | `.clip-prompt` | 0.92rem → 14.72px / 1.45 | #2c323d, keywords 650 in #245fc2 / #c2410c |
| Clip head | `.clip-head` | 0.95rem → 15.2px / 700; small line 0.76rem / 500 | #141821; small #868d99 |
| Verdict | `.verdict` | 0.86rem → 13.76px; `.ok` 650 | #c2412f / #17803d |
| Prompt line | `.prompt-line` | 1.04rem → 16.64px italic | #141821 |
| Tab | `.tab-list [role=tab]` | 0.9rem → 14.4px | #586070; selected #ffffff |
| Table | `table.res` | 0.9rem → 14.4px, tabular numbers; head 700 | head #141821, body inherits #2c323d |
| Table group label | `tr.group th` | 0.72rem → 11.52px / 700 uppercase, letter-spacing 0.08em | #868d99 |
| Equation | `.eq` | 1.4rem → 22.4px Cambria Math; labels 0.72rem / 700 uppercase | #141821 |
| BibTeX | `.bib pre` | 0.86rem → 13.76px / 1.65 monospace | #e6e8ec |
| Footer | `.footer` | 0.85rem → 13.6px | #868d99 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill, buttons, tabs, replay button, finding tags | 999px | pill 1px #efd7a2; button 1px #141821; ghost and tabs 1px #e3e6eb; tags none | none |
| Nav links | 8px | none | none |
| Stat cards, cards, clip frames, table wrap, stream box, details, finding figures, BibTeX | 12px (`--radius`) | 1px #e3e6eb (BibTeX none) | none |
| Figure images | 10px | none | none |
| Callout | 0 10px 10px 0 | 4px #e0a722 left bar only | none |
| Token highlights | 4px | none | none |
| Stream tokens | 5px, 22×22px | none | none |
| Copy button | 8px | 1px rgba(255,255,255,0.22) | none |
| "Ours" clip frame | 12px | 2px #17803d | none |

The page uses no box shadows anywhere; depth comes from the 1px #e3e6eb hairline and the white-on-#f6f7f9 band contrast. The only blur is the nav's backdrop filter.

## Layout Metrics

- **Container**: `.wrap { max-width: 1140px; margin: 0 auto; padding: 0 24px }`, so the content column is 1092px from x=174 to x=1266 at 1440. `.narrow` (BibTeX) is 860px, giving an 812px code block at x=314.
- **Hero**: padding 60px 0 26px under the 57px nav, rendered 490px tall (57–547). Title max 1000px; authors and affiliations max 920px; buttons row margin-top 24px.
- **Teaser**: padding 14px 0 60px; `.grid.cols-4` with 18px gap gives 260px clips; caption max 760px, margin-top 20px.
- **Section rhythm**: every `.block` has padding 76px 0, and bands alternate #f6f7f9 / #ffffff, so each section edge is a color change with 152px of space across it. Eyebrow margin-bottom 8px; h2 margin-bottom 0.55em (18.92px); `.lead` and `.abstract` max 860px and 900px.
- **TL;DR band**: `.tldr` max 920px; `.stats` is `repeat(4, minmax(0,1fr))` with 14px gap and margin 30px 0 48px, giving 263px cards 146px tall.
- **Motivation split**: `.split` is `minmax(0,1fr) minmax(0,1.08fr)` with 48px gap and centred items, so text gets 502px (x=174) and the figure 542px (x=724). `.split--top` aligns to the top with a 36px gap.
- **Findings**: `.finding` margin-top 44px; figure card padding 16px, margin-top 18px, full 1092px.
- **Method**: `.eq` margin 26px 0 6px; `.stream` max 920px centred, padding 20px 22px 16px, margin-top 30px; `.cards` three columns, 18px gap, margin-top 28px.
- **Video grids**: `.grid` gap 18px, `.cols-2` to `.cols-5`; clips are 1:1 with `object-fit: contain`; `.pair` max 760px; `.clip--wide` max 460px.
- **Tables**: `.table-wrap` full width (1092px) or `.narrow-table` 860px; cells padding 8px 12px.
- **Footer**: padding 34px 0 46px, 1px #e3e6eb top border.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >960px (base) | 24px inside 1140px | 17px | 52px (cap reached from 1131px; 4.6vw below) | stats 4 columns, splits 2 columns, cards 3, clips 4 |
| ≤960px | 24px | 17px | 4.6vw → 44.2px at 960 | splits and cards → 1 column (split gap 28px); stats → 2; `.cols-3/4/5` → 2; diversity → 3; user study → 1 |
| ≤640px | 16px | 16px | 2.1rem floor → 33.6px | block padding 52px; hero padding-top 40px; nav brand hidden, links scroll horizontally; grid gap 12px; stat value 25.6px; abstract left-aligned |

## Components

- **Venue pill** (`.venue-badge`): inline-block, #fcf3dd fill, 1px #efd7a2 border, radius 999px, padding 6px 16px, 14.4px/750 #9a6a06, letter-spacing 0.03em. No shadow, no animation.
- **Filled button** (`.btn`): inline-flex with 8px gap, padding 9px 18px, #141821 fill and 1px #141821 border, radius 999px, 15.2px/650 #ffffff, leading 1em Font Awesome / Academicons icon on the left (file-pdf, arXiv glyph, GitHub). Hover: fill #2e3544, no underline.
- **Ghost button** (`.btn--ghost`): same shape, #ffffff fill, 1px #e3e6eb border, #141821 text, quote-right icon. Hover fill #f6f7f9.
- **Section nav**: sticky 56px bar, rgba(255,255,255,0.92) with saturate(160%) blur(10px), 1px #e3e6eb bottom border; brand left, links right-aligned, 14.08px #586070, padding 6px 10px, radius 8px; hover and active #141821 on #f6f7f9, active weight 650. `scroll-padding-top: 72px` keeps anchored headings clear of the bar.
- **Eyebrow**: 12.48px/700 uppercase, letter-spacing 0.1em, #9a6a06, 8px above every section h2 ("TL;DR", "MOTIVATION", "ANALYSIS", "METHOD", "QUALITATIVE RESULTS"...).
- **Token highlight** (`.mark-r` / `.mark-e`): inline span, padding 0 0.25em, radius 4px, weight 650; amber #9a6a06 on #fcf3dd for "reasoning tokens", blue #2f5a9e on #e8eef8 for "execution tokens".
- **Stat card** (`.stat`): #ffffff on the #f6f7f9 band, 1px #e3e6eb, radius 12px, padding 18px 20px; value 32px/800 #141821 (e.g. "−71%"), label 14.08px #586070 8px below, detail 13.12px #868d99 tabular numbers 4px below ("0.141 → 0.040"). No accent color on the numbers.
- **Callout** (`.callout`): #fcf3dd fill, 4px #e0a722 left border, radius 0 10px 10px 0, padding 16px 20px, #141821 text with a bold lead-in ("The question behind the design:") and italic key terms; margin-top 8px.
- **Figure** (`.figure`): image full width, radius 10px, white background; caption 14.4px/1.55 #586070, 12px below, starting with a bold sentence.
- **Finding** (`.finding`): blue pill tag (12.8px/700 #2f5a9e on #e8eef8, padding 3px 10px, "Takeaway 1 · Knowledge capacity"), h3 with no top margin, text max 900px, then a white figure card (1px #e3e6eb, radius 12px, padding 16px).
- **Equation strip** (`.eq`): centred flex row of Cambria Math 22.4px terms; the execution term has a 3px #4a78c2 underline and the reasoning term a 3px #e0a722 underline, each with a 0.72rem/700 uppercase label beneath in #2f5a9e or #9a6a06.
- **Token stream** (`.stream`): white card, 1px #e3e6eb, radius 12px, padding 20px 22px 16px; a dashed #c9ced6 italic "text prompt" chip, then rows of 22px squares (radius 5px) in #e0a722 (reasoning) and #4a78c2 (execution) that light from 16% opacity at scale 0.8 to full as the script plays; legend with 10px dots in 14.08px #868d99, the active phase in #141821/650.
- **Card** (`.card`): white, 1px #e3e6eb, radius 12px, padding 20px 22px; h4 16.32px/700, text 15.04px #586070.
- **Motion clip** (`.clip`): optional head (15.2px/700 #141821 with a 12.16px/500 #868d99 sub-line), a 1:1 white box with 1px #e3e6eb and radius 12px holding a muted looping video (autoplay when in view), then a 14.72px #2c323d prompt or a 13.76px verdict ("✗ ..." #c2412f, "✓ ..." #17803d 650). "Ours" clips get a 2px #17803d frame and green head.
- **Tabs** (`.tab-list`): centred pill buttons, padding 7px 15px, 1px #e3e6eb, radius 999px, 14.4px #586070 on #ffffff; hover #141821 text with #c9ced6 border; selected #ffffff on #141821. Optional group labels 11.52px/700 uppercase #868d99.
- **Results table** (`table.res` in `.table-wrap`): white wrap, 1px #e3e6eb, radius 12px, horizontal scroll; header row #fafbfc 700 #141821; cells 8px 12px, centred, nowrap, 1px #eef0f3 rules; group rows #fcfcfd with 11.52px uppercase #868d99 labels; LMR row #ebf6ef fill, 650 #141821; confidence intervals at 0.72em #868d99; best values bold, second underlined (1.5px, offset 3px).
- **User-study bar**: grid 96px label / track / 44px value; track 14px tall, #e9ecf1, radius 999px, with a 2px dashed #8f97a3 line at 50%; fill #4a78c2; value 700 #141821 tabular.
- **Paper figure toggle** (`details.paperfig`): white, 1px #e3e6eb, radius 12px, padding 12px 18px; summary 650 #141821.
- **BibTeX** (`.bib`): #111722 pre, radius 12px, padding 22px 24px, 13.76px monospace #e6e8ec; copy button top-right (12px inset), padding 5px 12px, 1px rgba(255,255,255,0.22) border, rgba(255,255,255,0.08) fill, radius 8px, copy icon, hover fill rgba(255,255,255,0.16).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky section nav | yes | translucent white bar, mascot + "LMR" brand, ten anchor links with gray pill hover |
| Venue badge | yes | cream amber pill "IEEE TPAMI 2026" |
| Title / authors / affiliations | yes | centred, 52px title with inline mascot and 31.2px subtitle line, muted affiliation row, faint notes |
| Link buttons | yes | three near-black pills and one ghost pill with icons |
| Teaser | yes | four square motion videos with keyword-colored prompt captions and a muted caption line |
| TL;DR | yes | eyebrow plus 20.8px sentence with amber and blue token highlights, on the gray band |
| Stats | yes | four white stat cards, black numbers |
| Abstract | present but non-standard | no section of its own; a 21.6px heading and justified 900px text share the TL;DR band below the stats |
| Motivation | yes | two-column split, amber callout under the text, captioned diagram on the right |
| Findings | yes | blue takeaway tags and white figure cards |
| Method | yes | equation strip with colored underlines, animated token stream, three cards, figure |
| Video comparisons | yes | tabbed prompts, 4-up clips with model heads and ✗/✓ verdicts, green frame for ours |
| Results tables | yes | twelve tables in white rounded wraps, tabbed by dataset, green "ours" row |
| User study | yes | horizontal bar charts with a dashed 50% line |
| Gallery | yes | more clip grids, streaming long-term and diversity sub-blocks in a split |
| BibTeX | yes | dark code block with ghost copy button |
| Footer | yes | centred faint line with the title and venue, top hairline |
| Theme toggle, news, publication list, acknowledgements | absent from the source | none |

## Adapting to Other Content

- **More authors**: keep `.authors` at 17.28px in the 920px block with nowrap name spans; a third line adds 28.5px and pushes everything down; keep the 15.2px #586070 affiliation flex row with 20px column gaps.
- **More stats**: keep four per row at 1440 (263px cards); a fifth goes on a new row rather than shrinking cards. Numbers stay 32px/800 #141821, never amber or blue.
- **A long publication or news list**: put it in a `.block` band, each item a `.card` row (white, 1px #e3e6eb, radius 12px, padding 20px 22px) with the date as a finding-style tag (12.8px/700 #2f5a9e on #e8eef8).
- **Extra results tables**: follow `table.res` exactly; mark the proposed method with the #ebf6ef row, not with amber.
- **Content with no "reasoning vs. execution" pair**: keep amber as the page accent (eyebrows, venue pill, callouts) and drop the blue highlights, keeping blue only for links and data bars.

## Do's and Don'ts

- Do alternate #ffffff and #f6f7f9 bands with 76px padding; that change is the section divider.
- Do keep amber and blue tied to meaning (reasoning and execution) across text highlights, tokens, equation underlines and tags.
- Do use near-black #141821 for primary buttons and selected tabs; the accents never fill a button.
- Do frame every video, card and table with 1px #e3e6eb and a 12px radius.
- Don't add shadows; the page has none.
- Don't load a text web font; the system UI face is part of the look.
- Don't color stat numbers; they are black 32px/800 with muted labels.
- Don't use orange #c2410c or keyword blue #245fc2 outside prompt keywords.

## Surfaces

White page (#ffffff) with full-width #f6f7f9 bands for every other section; white cards, stat cards, clip boxes and table wraps sit on both. Cream #fcf3dd appears in the venue pill, callout and reasoning highlights; pale blue #e8eef8 in execution highlights and finding tags; pale green #ebf6ef only on the LMR table rows. The single dark surface is the #111722 BibTeX block near the end.

## Imagery

57 short looping videos of a beige SMPL-style mannequin on white, shown in 1:1 framed boxes with `object-fit: contain`, so the figure is small inside wide white space. Paper figures (architecture diagrams, token-space analyses) are wide raster images with 10px radii and bold-led captions. A small robot mascot (lmr_icon.png) appears in the nav (28px) and before the title (62px). Icons are Font Awesome SVGs and the Academicons arXiv glyph.

## Layout

Centred hero and teaser, then a 1092px left-aligned column inside alternating full-width bands: TL;DR and stats, motivation split (502px text, 542px figure), findings, method, comparisons, benchmarks, latent-vs-language ablation, ablations, gallery and BibTeX. Generous 76px band padding and consistent 12px-radius cards give a calm, magazine-like rhythm.

## Agent Prompt Guide

Quick colors: page #ffffff, band #f6f7f9, ink #141821, body #2c323d, muted #586070, faint #868d99, hairline #e3e6eb, reasoning #e0a722 / #9a6a06 / #fcf3dd, execution #4a78c2 / #2f5a9e / #e8eef8, ours #17803d / #ebf6ef.

1. "Build a centred light hero under a 56px sticky nav (rgba(255,255,255,0.92), backdrop-filter saturate(160%) blur(10px), 1px #e3e6eb bottom border, links 14.08px #586070 padding 6px 10px radius 8px). Hero padding 60px 0 26px. Venue pill: #fcf3dd fill, 1px #efd7a2 border, 14.4px/750 #9a6a06, padding 6px 16px, radius 999px. Title 52px/800 #141821, letter-spacing -0.025em, line-height 1.12, with a 31.2px/650 #2c323d subtitle line. Authors 17.28px #141821, affiliations 15.2px #586070. Buttons: padding 9px 18px, radius 999px, #141821 fill, 15.2px/650 #ffffff with a left icon; ghost variant #ffffff with 1px #e3e6eb."
2. "Make a TL;DR band: #f6f7f9 background, padding 76px 0; eyebrow 12.48px/700 uppercase, letter-spacing 0.1em, #9a6a06; sentence 20.8px #141821 line-height 1.6, max 920px, with inline highlights (padding 0 0.25em, radius 4px, weight 650) #9a6a06 on #fcf3dd and #2f5a9e on #e8eef8. Below, four stat cards in a 14px-gap grid: #ffffff, 1px #e3e6eb, radius 12px, padding 18px 20px, value 32px/800 #141821, label 14.08px #586070, detail 13.12px #868d99."
3. "Create a results table: wrapper #ffffff with 1px #e3e6eb border and 12px radius; 14.4px tabular cells padding 8px 12px with 1px #eef0f3 rules; header row #fafbfc 700 #141821; group rows #fcfcfd 11.52px/700 uppercase #868d99; the proposed method's row #ebf6ef, weight 650."

## Similar Pages

- Modern hand-built project pages with a sticky section nav, alternating light gray bands and white rounded cards, in the style of recent generative-model and robotics pages.
- Pages that use paired semantic accent colors to encode the method's two components across text, diagrams and animations.

## Quick Start

```css
:root {
  --ink: #141821;
  --body: #2c323d;
  --muted: #586070;
  --faint: #868d99;
  --line: #e3e6eb;
  --bg: #ffffff;
  --bg-alt: #f6f7f9;
  --reason: #e0a722;
  --reason-ink: #9a6a06;
  --reason-soft: #fcf3dd;
  --exec: #4a78c2;
  --exec-ink: #2f5a9e;
  --exec-soft: #e8eef8;
  --ok: #17803d;
  --ok-soft: #ebf6ef;
  --bad: #c2412f;
  --kw1: #245fc2;
  --kw2: #c2410c;
  --radius: 12px;
  --wrap: 1140px;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
body { font: 17px/1.65 var(--font); color: var(--body); background: var(--bg); }
.wrap { max-width: var(--wrap); margin: 0 auto; padding: 0 24px; }
.block { padding: 76px 0; }
.block--alt { background: var(--bg-alt); }
```

## Provenance

- **URL**: https://chenhaoqcdyq.github.io/LMR/
- **Paper**: Think Before You Move: Latent Motion Reasoning for Text-to-Motion Generation (arXiv 2512.24100), Yijie Qian, Juncheng Wang, Yuxiang Feng, Chao Xu, Wang Lu, Yang Liu, Baigui Sun, Yiqiang Chen, Yong Liu, Shujun Wang.
- **Venue**: IEEE TPAMI 2026 (venue pill, page title and BibTeX `journal` field; the late-December 2025 arXiv comment says "Accepted to TPAMI").
- **Selection reason**: rich and polished; sticky section nav, a venue pill, a captioned motion gallery, a TL;DR band with highlighted tokens and stat cards, then a two-column motivation section with a tinted callout, with strong rhythm throughout.
- **Template credit**: none stated; a custom build (`static/css/index.css`, `static/js/index.js`) with Font Awesome and Academicons; footer reads the title and "IEEE TPAMI 2026".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, anatomy), the 1440×900 and full-page screenshots, an in-browser computed-style probe of below-the-fold elements, and `index.css`, `index.js` and `index.html` read directly, on 2026-10-28.
