# DESIGN.md tests (2026-10-28)

## Reconstruction test

An agent builds a page with different, fictional content using only one DESIGN.md. It is not allowed to see the original page. A blind judge then sees the original's screenshot and the builds made from pages of the same kind (3 project builds or 2 researcher builds) and picks the one that came from that original. An analyst compares the build with the live page and scores each dimension from 1 to 5. Five pages were tested, and the same pages and content were used both times. Hinton's page is not in the gallery, so its v2 file was written for the test only.

| Page | v1 overall | v2 overall | v2 palette / type / layout / components |
|---|---|---|---|
| cvpr-2026-autogaze | 3 | 4 | 5 / 4 / 4 / 4 |
| icml-2026-ssi-bench | 3 | 4 | 5 / 5 / 4 / 4 |
| acl-2025-gamebot | 2 | 4 | 5 / 4 / 4 / 4 |
| researcher-yoshua-bengio | 3 | 4 | 4 / 4 / 4 / 4 |
| researcher-geoffrey-hinton | 4 | 4 | 5 / 4 / 3 / 4 |
| mean | 3.0 | 4.0 | |

The blind match was 5/5 correct in both rounds, with high confidence in v2. Five pages is a small sample, and the scores come from model analysts, not people.

In v2 the analysts found remaining errors in 4 of the 5 files. Most were viewport-dependent values copied from base CSS rules, gradients described in words instead of quoted, and a misread chip count. Each was rechecked against a 1440 render. The gallery files for autogaze, ssi-bench and Bengio were corrected. The one gamebot item was rejected, because the render confirms the documented 32px. Some of the reported values were themselves off and were replaced by measured ones: the autogaze header padding is 72px, not 5vh. METHOD.md gained four rules from this round.

## Spot audit

An independent agent checked about 129 concrete claims in ten v2 files against fresh renders: zpressor, sparse-planning, smpo, ogbench, egoworld, semanticdraw, multimodal-distribution-matching, guidedog, Matt Deitke and Erik Wijmans. It found 4 wrong values, about 3%. Six files had no errors. Three of the four were values that a script or a later cascade rule changes at render time. All four were corrected.

Raw outputs are in the session scratchpad and are not kept in the repo.

## Spot audit, second round (2026-10-28)

After adding 100 project and researcher pages and 40 code READMEs, auditors checked 13 new files (10 pages, 3 READMEs) against the rendered page or the README source: 208 claims, 8 wrong (3.8%). All 8 were confirmed against the CSS, HTML, SVG or Markdown and corrected. Five concerned values that only hold for part of the page (a column split used in two of four sections, a border rule used by two of three lists, one icon larger than the others, a section gap changed by a script tag, a footer handle in a different color); three concerned README details (a third logo color, an autolinked email, a GIF count).

## Usability test with missing content (2026-11-02)

Four builders each got one DESIGN.md of a page type not tested before (a CHI project page, a TPAMI project page, a cognitive-science researcher page and a code README) and fictional content with modules removed on purpose: no video, no demo, no portrait. They could not see the original or render their work. One model reviewer, not blind, compared the builds with the live pages on the same 1 to 5 scale.

| Page | palette / type / layout / components | overall |
|---|---|---|
| chi-2026-hear-you-in-silence | 5 / 5 / 4 / 4 | 4 |
| tpami-2026-hermes | 5 / 5 / 4 / 5 | 5 |
| researcher-lionel-wong | 5 / 3 / 4 / 3 | 3 |
| readme-kuleshov-group-bd3lms | 5 / 5 / 4 / 4 | 4 |
| mean | | 4.0 |

All four could be published once real links, figures and a photo were added, and none overflowed at widths down to 360px. The README was first captured from a test page that lacked GitHub's `markdown-body` wrapper, so the reviewer scored a corrected render.

Two gaps came from the files. No file gave a font link, and some substitutes could not be loaded or had the wrong shape: the Lionel Wong file called a wide, heavy wordmark "compressed" and suggested Anton, which renders "lio wong" at 109px against the source's 140px. And most page files said what to do with more content but not with less, so the CHI builder rebuilt the header by guesswork and the Lionel Wong build lost its framed research box above the fold. README files already had such rules, and their builder followed one.

Changes made after the test:

- Every substitute now names one family that loads from Google Fonts, or a system font where the page renders one. Display faces were chosen with `tools/font_fit.py`, which measures the rendered width of the display line against the source (Dela Gothic One gives 147px for the Lionel Wong wordmark). Font text changed in 72 files.
- The Quick Start of 193 page files now opens with an `@import` of the Google Fonts families its stacks use, with the weights the source loads. All 157 distinct URLs returned 200. The other 37 pages use system fonts only. Stacks whose declared family cannot be loaded name the substitute right after it.
- 191 files gained one to three `**No ...**` rules in Adapting to Other Content (no teaser, no video, no portrait, no cards, no venue and so on), saying what takes the missing element's place and the size that results. Three were written by hand and 188 by agents from each file's First Viewport, Page Modules, Imagery and Do's and Don'ts, then checked by script for new colors and dashes and read in a sample. `tools/lint_design.py` now fails a file without such a rule.
- Wrong lines were corrected. The CHI blocks are 121px apart, set by a 1px `hr` with 60px margins; the file said 80px and the reviewer 40px, and a render settled it. The Hermes authors are dark when unlinked and have no commas. The Lionel Wong arrow rule now covers running text only. The shields.io named colors in `METHOD_README.md` are the values served today (`green` is #67ac09, not #97ca00).

The CHI and Lionel Wong builds were then redone with the same prompts and content, and a separate model reviewer, who was not told the earlier scores or what had changed, scored them. CHI stayed at 5 / 5 / 4 / 4, overall 4, though its header now keeps the source's two columns, title position, teaser and BibTeX panel. Lionel Wong rose to 5 / 4 / 4 / 4, overall 4: the wordmark now matches and the framed box is back in the first viewport. The rebuild notes found one new contradiction, between the publication-list rule and the new no-research-questions rule, which was fixed. These screenshots were taken after web fonts had loaded, since `tools/snap.py` captured one rebuild before its body font arrived.

Not changed: 20 light-theme rules still recommend best-value colors below 4.5:1 contrast on white (the CHI rebuilder again replaced #c97c5d), and the files were not shortened. Four pages and two rebuilds is a small sample, the scores come from models, and none of this shows whether people find the files useful.
