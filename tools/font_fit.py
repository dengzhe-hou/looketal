"""Compare substitute fonts against what a page renders: same text, size, weight and tracking, measured width.

Usage: python -I -B tools/font_fit.py URL "CSS selector" "Candidate A,Candidate B" [--port 9334]  -> JSON on stdout
Candidates are Google Fonts families. A ratio of 1.0 means the display line keeps the source's width.
"""
import json
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from computed_style import CHROME, ws_connect, ws_recv, ws_send

JS = r"""
(async (sel, cands) => {
  await new Promise(r => setTimeout(r, 2500));
  await document.fonts.ready;
  const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el); return r.width > 4 && r.height > 4 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const el = [...document.querySelectorAll(sel)].find(e => vis(e) && e.innerText && e.innerText.trim());
  if (!el) return JSON.stringify({ error: 'no visible match for ' + sel });
  const s = getComputedStyle(el), text = el.innerText.trim().replace(/\s+/g, ' ').slice(0, 80);
  const width = family => { const span = document.createElement('span'); span.textContent = text;
    span.style.cssText = `position:absolute;left:0;top:-9999px;white-space:nowrap;font-family:${family};font-size:${s.fontSize};font-weight:${s.fontWeight};font-style:${s.fontStyle};letter-spacing:${s.letterSpacing};text-transform:${s.textTransform}`;
    document.body.appendChild(span); const w = span.getBoundingClientRect().width; span.remove(); return w; };
  const source = width(s.fontFamily), out = {};
  const link = href => new Promise(res => { const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = href; l.onload = () => res(true); l.onerror = () => res(false); document.head.appendChild(l); });
  for (const c of cands) {
    const q = c.replace(/ /g, '+');
    if (!await link(`https://fonts.googleapis.com/css2?family=${q}:wght@${s.fontWeight}&display=block`) && !await link(`https://fonts.googleapis.com/css2?family=${q}&display=block`)) { out[c] = 'not on Google Fonts'; continue; }
    await document.fonts.load(`${s.fontWeight} ${s.fontSize} "${c}"`, text);
    out[c] = +(width(`"${c}", monospace`) / source).toFixed(3);
  }
  const loaded = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, ''));
  return JSON.stringify({ text, declared: s.fontFamily.slice(0, 80), size: s.fontSize, weight: s.fontWeight, letter_spacing: s.letterSpacing,
    source_width: +source.toFixed(1), ratio: out, fonts_loaded: [...new Set(loaded)].slice(0, 12) });
})
"""


def fit(url, selector, candidates, port=9334):
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as prof:
        proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--mute-audio", "--no-first-run",
                                 f"--remote-debugging-port={port}", f"--user-data-dir={prof}", "--window-size=1440,900", "about:blank"],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            for _ in range(50):
                try:
                    targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2))
                    break
                except OSError:
                    time.sleep(0.2)
            s = ws_connect(next(t for t in targets if t["type"] == "page")["webSocketDebuggerUrl"])
            ws_send(s, json.dumps({"id": 1, "method": "Page.enable"}))
            ws_send(s, json.dumps({"id": 2, "method": "Page.setBypassCSP", "params": {"enabled": True}}))
            ws_send(s, json.dumps({"id": 3, "method": "Page.navigate", "params": {"url": url}}))
            s.settimeout(60)
            while json.loads(ws_recv(s)).get("method") != "Page.loadEventFired":
                pass
            expr = f"{JS}({json.dumps(selector)}, {json.dumps(candidates)})"
            ws_send(s, json.dumps({"id": 4, "method": "Runtime.evaluate", "params": {"expression": expr, "awaitPromise": True, "returnByValue": True}}))
            while True:
                m = json.loads(ws_recv(s))
                if m.get("id") == 4:
                    return json.loads(m["result"]["result"]["value"])
        finally:
            proc.kill()


if __name__ == "__main__":
    port = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 9334
    print(json.dumps(fit(sys.argv[1], sys.argv[2], [c.strip() for c in sys.argv[3].split(",")], port), ensure_ascii=False, indent=1))
