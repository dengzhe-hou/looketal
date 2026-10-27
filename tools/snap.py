"""Capture above-the-fold screenshots with headless Chrome and write webp thumbnails.

Usage: python -I -B snap.py OUT_DIR URLS_JSON [--workers 4] [--tall] [--wait MS]
URLS_JSON is a list of {"slug": ..., "url": ...}. For each slug writes OUT_DIR/<slug>.png (raw 1440x900),
OUT_DIR/<slug>.webp (1200x750) and OUT_DIR/<slug>.card.webp (640x400). Prints a JSON status list.
"""
import json
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 1440, 900
TALL = "--tall" in sys.argv
WAIT = "--timeout=" + (sys.argv[sys.argv.index("--wait") + 1] if "--wait" in sys.argv else "10000")


def run_chrome(url, png, out, wait_flag, size=(W, H)):
    with tempfile.TemporaryDirectory(dir=out, ignore_cleanup_errors=True) as prof:
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--mute-audio", "--no-first-run",
               "--no-default-browser-check", f"--user-data-dir={prof}", f"--window-size={size[0]},{size[1]}",
               wait_flag, "--force-device-scale-factor=1", f"--screenshot={png}", url]
        try:
            subprocess.run(cmd, capture_output=True, timeout=35)
            return True
        except subprocess.TimeoutExpired:
            return False


def shoot(item, out):
    png = out / f"{item['slug']}.png"
    # a wall-clock wait first: virtual time hangs on pages that stream video; it remains the fallback
    if not run_chrome(item["url"], png, out, WAIT) and not run_chrome(item["url"], png, out, "--virtual-time-budget=8000"):
        return {"slug": item["slug"], "ok": False, "error": "timeout"}
    if not png.exists():
        return {"slug": item["slug"], "ok": False, "error": "no screenshot"}
    im = Image.open(png).convert("RGB")
    im.resize((1200, 750), Image.LANCZOS).save(out / f"{item['slug']}.webp", "WEBP", quality=80)
    im.resize((640, 400), Image.LANCZOS).save(out / f"{item['slug']}.card.webp", "WEBP", quality=78)
    # a near-uniform frame usually means a blank page, a loader, or a bot wall
    if TALL:
        # taller window for judging what lies below the fold (100vh heroes stretch, so thumbnails stay on the 900px shot)
        tall = out / f"{item['slug']}.tall.png"
        if run_chrome(item["url"], tall, out, "--timeout=12000", (W, 2700)) and tall.exists():
            Image.open(tall).convert("RGB").resize((720, 1350), Image.LANCZOS).save(out / f"{item['slug']}.tall.webp", "WEBP", quality=72)
            tall.unlink()
    lo, hi = im.convert("L").getextrema()
    return {"slug": item["slug"], "ok": True, "blank": hi - lo < 16}


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    items = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(lambda it: shoot(it, out), items))
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
