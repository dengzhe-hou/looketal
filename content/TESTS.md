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
