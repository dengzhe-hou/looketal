"""Render the 1200x630 link-preview image to tools/assets/og.jpg with headless Chrome.

Usage: python -I -B tools/og_card.py
Counts come from data/catalog.json; the thumbnails are the first cards of the home page wall.
"""
import json
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
THUMBS = ["acl-2026-progresslm", "acl-2026-craft", "acl-2026-figma", "cvpr-2026-archon", "chi-2026-lingoq",
          "acl-2026-unleashing-spatial-reasoning", "chi-2026-collaposer", "acl-2025-cosyn", "acl-2025-gamebot"]


def html():
    n = Counter(r["kind"] for r in json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8")))
    cards = "".join(f'<img src="{(ROOT / "content" / "shots" / f"{s}.card.webp").as_uri()}">' for s in THUMBS)
    return f"""<!doctype html><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0}} html,body{{width:1200px;height:630px;overflow:hidden;background:#fbfaf7;color:#1b1a17}}
.text{{position:absolute;left:64px;top:64px;bottom:60px;width:560px;display:flex;flex-direction:column}}
.mark{{width:64px;height:64px;border-radius:50%;background:#1b1a17;color:#fbfaf7;display:flex;align-items:center;justify-content:center;
font:italic 500 21px/0.92 Newsreader,serif;text-align:center}}
h1{{font:500 104px/1 Newsreader,serif;letter-spacing:-.025em;margin-top:44px;white-space:nowrap}}
p{{font:400 33px/1.26 Newsreader,serif;color:#3a3833;margin-top:24px}}
.meta{{margin-top:auto;font:400 19px/1.6 Inter,sans-serif;color:#6b675f;white-space:nowrap}} .meta b{{font-weight:500;color:#1b1a17}}
.wall{{position:absolute;left:680px;top:-44px;width:760px;display:grid;grid-template-columns:repeat(3,300px);gap:20px;transform:rotate(-4deg);transform-origin:0 0}}
.wall img{{width:300px;height:188px;object-fit:cover;object-position:top;border-radius:10px;border:1px solid rgba(27,26,23,.12);box-shadow:0 8px 24px rgba(0,0,0,.08)}}
</style>
<div class="wall">{cards}</div>
<div class="text"><div class="mark">et<br>al.</div><h1>Look et al.</h1>
<p>A design library of academic web pages for humans and AI agents</p>
<div class="meta"><b>{n['project']}</b> project pages &nbsp; <b>{n['researcher']}</b> researcher homepages &nbsp; <b>{n['readme']}</b> code READMEs<br>looketal.com</div></div>"""


def main():
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        src, png = Path(tmp) / "og.html", Path(tmp) / "og.png"
        src.write_text(html(), encoding="utf-8")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                        f"--user-data-dir={Path(tmp) / 'p'}", "--window-size=1200,630", "--virtual-time-budget=12000",
                        "--force-device-scale-factor=1", f"--screenshot={png}", src.as_uri()], capture_output=True, timeout=60, check=True)
        im = Image.open(png).convert("RGB")
        assert im.size == (1200, 630), im.size
        im.save(ROOT / "tools" / "assets" / "og.jpg", "JPEG", quality=88, optimize=True)


if __name__ == "__main__":
    main()
