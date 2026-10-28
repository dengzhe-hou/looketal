"""Render GitHub READMEs to local HTML pages, the way github.com shows them, for screenshots and for writers.

Usage: python -I -B tools/readme_render.py OUT_DIR ITEMS_JSON
ITEMS_JSON is a list of {"slug", "repo", "readme_path"}. For each item writes OUT_DIR/<slug>.readme.html
(GitHub's own rendered HTML from the API, in github-markdown-css light, inside a 920px frame, the README
column width on a 1440px-wide repository page) and OUT_DIR/<slug>.readme.md (the raw Markdown). Prints {"slug", "ok", "url"} per item; url is the
file:// address to pass to snap.py. Needs the gh CLI.
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path, PurePosixPath

CSS = "https://cdn.jsdelivr.net/npm/github-markdown-css@5.8.1/github-markdown-light.min.css"
PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><base href="{base}">
<link rel="stylesheet" href="{css}"><style>
body {{ margin: 0; background: #ffffff; }}
.frame {{ max-width: 920px; margin: 24px auto; border: 1px solid #d1d9e0; border-radius: 6px; }}
.bar {{ font: 600 14px/20px -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif; color: #1f2328;
  padding: 8px 16px; border-bottom: 1px solid #d1d9e0; }}
.markdown-body {{ padding: 32px; }}
.markdown-body .anchor {{ display: none; }}  /* github.com shows heading links only on hover */
</style><title>{repo}</title></head><body><div class="frame"><div class="bar">{path}</div>{html}</div></body></html>"""


def gh(args):
    r = subprocess.run(["gh", "api", *args], capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def render(item, out):
    repo, path = item["repo"], item.get("readme_path", "README.md")
    html = gh([f"repos/{repo}/readme", "-H", "Accept: application/vnd.github.html"])
    raw = gh([f"repos/{repo}/readme", "-H", "Accept: application/vnd.github.raw"])
    if html is None or raw is None:
        return {"slug": item["slug"], "ok": False, "url": ""}
    folder = str(PurePosixPath(path).parent)
    # relative image paths in the README resolve against the README's folder on the default branch
    base = f"https://github.com/{repo}/raw/HEAD/" + ("" if folder == "." else folder + "/")
    f = out / f"{item['slug']}.readme.html"
    f.write_text(PAGE.format(base=base, css=CSS, repo=repo, path=path, html=html), encoding="utf-8")
    (out / f"{item['slug']}.readme.md").write_text(raw, encoding="utf-8")
    return {"slug": item["slug"], "ok": True, "url": f.resolve().as_uri()}


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    items = json.load(open(sys.argv[2], encoding="utf-8"))
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(lambda x: render(x, out), items))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
