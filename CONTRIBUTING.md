# Contributing to Look et al.

Look et al. is maintained by one person, and every issue and pull request is read by hand. There are four ways to help.

## Suggest a page

Know a paper project page, researcher homepage or code README whose design is worth studying? [Suggest it](https://github.com/dengzhe-hou/Looketal/issues/new?template=suggest-page.yml). Your own page is welcome too.

Suggestions join the candidate pool for the next update and are judged the same way as every other entry: by visual design only, from screenshots (see "How entries were chosen" in the [README](README.md)). Not every suggestion will be added, and a page that is not added says nothing about the research behind it. Project pages should belong to a paper accepted at a conference or journal; workshop papers are not included.

## Report a wrong value

If a DESIGN.md gives a color, size, font or rule that the live page does not show, [report it](https://github.com/dengzhe-hou/Looketal/issues/new?template=correction.yml) with the style page, the line, and what the page actually shows. A screenshot or the CSS rule helps. Corrections are checked against a fresh render of the page before they go in, since the render is what a DESIGN.md describes.

## Translations

The site interface is in English, Japanese and Simplified Chinese (`tools/i18n.py`, `tools/i18n_about.py` and `data/i18n/`). DESIGN.md files stay in English so that people and coding agents read one text. Fixes to the Japanese and Chinese text are welcome as an issue or a pull request.

## Code

Fixes to the site and the tools are welcome as pull requests. Before opening one, run:

```bash
python -I -B tools/lint_design.py content/designs/*.md
python -I -B tools/build_site.py
```

Commit the rebuilt `docs/` folder with your change, because GitHub Pages serves it directly. For larger changes, such as a new feature or a new kind of entry, please open an issue first.

## Removal

If you are an author and want your page or screenshot removed or corrected, use the [removal form](https://github.com/dengzhe-hou/Looketal/issues/new?template=removal.yml). These requests are handled first.

## License

By contributing you agree that code is released under the MIT license and content (DESIGN.md files, data and site text) under CC BY-NC 4.0, as described in the [README](README.md#license-and-citation). Please do not submit screenshots or text you do not have the right to share.
