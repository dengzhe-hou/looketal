"""Read what a page actually renders: computed styles of key elements, first-viewport anatomy, fonts that
really loaded, and the color share of the first viewport. Uses headless Chrome over the DevTools protocol.

Usage: python -I -B computed_style.py URL [--port 9333] [--png SCREENSHOT.png]  -> JSON on stdout
The optional screenshot (from snap.py, 1440x900) is used for the color-share measurement.
"""
import base64
import json
import os
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

JS = r"""
(async () => {
  await new Promise(r => setTimeout(r, 2500));
  const cs = el => getComputedStyle(el);
  const pick = el => { const s = cs(el), r = el.getBoundingClientRect();
    return { tag: el.tagName.toLowerCase(), cls: (el.className && el.className.baseVal === undefined ? el.className : '').toString().slice(0, 80),
      text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60),
      box: [Math.round(r.x), Math.round(r.y + scrollY), Math.round(r.width), Math.round(r.height)],
      color: s.color, bg: s.backgroundColor, bgImage: s.backgroundImage === 'none' ? '' : s.backgroundImage.slice(0, 160),
      font: s.fontFamily.slice(0, 80), size: s.fontSize, weight: s.fontWeight, lh: s.lineHeight, ls: s.letterSpacing,
      tt: s.textTransform, align: s.textAlign, radius: s.borderRadius, border: s.borderTopWidth !== '0px' ? `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}` : '',
      shadow: s.boxShadow === 'none' ? '' : s.boxShadow.slice(0, 120), pad: s.padding, margin: s.margin, maxw: s.maxWidth, pos: s.position }; };
  const vis = el => { const r = el.getBoundingClientRect(), s = cs(el); return r.width > 4 && r.height > 4 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05; };
  const all = sel => [...document.querySelectorAll(sel)].filter(vis);
  const first = (sel, n = 3) => all(sel).slice(0, n).map(pick);
  // first viewport anatomy: visible leaf-ish blocks in the top 900px, in DOM order
  const anatomy = [];
  for (const el of document.body.querySelectorAll('h1,h2,h3,h4,p,a,button,img,video,iframe,canvas,span,li,figure,pre,table,nav,header')) {
    const r = el.getBoundingClientRect();
    if (!vis(el) || r.top + scrollY > 900 || r.bottom < 0) continue;
    if (el.closest('a,button') && el.closest('a,button') !== el) continue;
    if (['span', 'li'].includes(el.tagName.toLowerCase()) && el.children.length) continue;
    anatomy.push(pick(el));
    if (anatomy.length >= 45) break;
  }
  // widest centered content container
  let container = null, best = 0;
  for (const el of document.body.querySelectorAll('div,main,section,article')) {
    const s = cs(el), r = el.getBoundingClientRect();
    if (!vis(el) || s.maxWidth === 'none' || !s.maxWidth.endsWith('px')) continue;
    if (r.width > best && r.width < innerWidth - 20) { best = r.width; container = el; }
  }
  const fonts = [...document.fonts].filter(f => f.status === 'loaded').map(f => `${f.family.replace(/"/g, '')} ${f.weight}${f.style === 'italic' ? 'i' : ''}`);
  const counts = {}; for (const t of ['h1','h2','h3','h4','section','table','video','pre','figure','iframe','canvas']) counts[t] = document.querySelectorAll(t).length;
  return JSON.stringify({
    url: location.href, title: document.title, viewport: [innerWidth, innerHeight], doc_height: document.documentElement.scrollHeight,
    html: pick(document.documentElement), body: pick(document.body), container: container && pick(container),
    headings: { h1: first('h1', 3), h2: first('h2', 4), h3: first('h3', 3) },
    links_buttons: first('a.button, .button, button, a.btn, .btn, a[class*="link"]', 6), nav: first('nav, header', 2),
    sections: first('section', 8), tables: first('table', 2), th: first('th', 2), td: first('td', 2), pre: first('pre, code', 2),
    footer: first('footer', 1), anatomy, fonts_loaded: [...new Set(fonts)].slice(0, 20), counts });
})()
"""


def ws_connect(url):
    host, rest = url[len("ws://"):].split("/", 1)
    h, p = host.split(":")
    s = socket.create_connection((h, int(p)), timeout=60)
    key = base64.b64encode(os.urandom(16)).decode()
    s.sendall((f"GET /{rest} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
               f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
    buf = b""
    while b"\r\n\r\n" not in buf:
        buf += s.recv(4096)
    if b" 101 " not in buf.split(b"\r\n", 1)[0]:
        raise RuntimeError(f"websocket upgrade failed: {buf[:200]!r}")
    return s


def ws_send(s, text):
    data = text.encode()
    head = bytes([0x81])
    n = len(data)
    head += bytes([0x80 | n]) if n < 126 else (bytes([0x80 | 126]) + struct.pack(">H", n) if n < 65536 else bytes([0x80 | 127]) + struct.pack(">Q", n))
    mask = os.urandom(4)
    s.sendall(head + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))


def recv_exact(s, n):
    out = b""
    while len(out) < n:
        chunk = s.recv(n - len(out))
        if not chunk:
            raise RuntimeError("websocket closed")
        out += chunk
    return out


def ws_recv(s):
    msg = b""
    while True:
        b1, b2 = recv_exact(s, 2)
        n = b2 & 0x7F
        if n == 126:
            n = struct.unpack(">H", recv_exact(s, 2))[0]
        elif n == 127:
            n = struct.unpack(">Q", recv_exact(s, 8))[0]
        msg += recv_exact(s, n)
        if b1 & 0x80:
            return msg.decode("utf-8", "replace")


def color_share(png, k=8):
    from PIL import Image
    im = Image.open(png).convert("RGB").resize((360, 225))
    q = im.quantize(colors=k, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    counts = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in counts)
    return [{"hex": "#%02x%02x%02x" % tuple(pal[i * 3:i * 3 + 3]), "share": round(c / total, 3)} for c, i in counts]


def main():
    url = sys.argv[1]
    port = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 9333
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
            page = next(t for t in targets if t["type"] == "page")
            s = ws_connect(page["webSocketDebuggerUrl"])
            ws_send(s, json.dumps({"id": 1, "method": "Page.enable"}))
            ws_send(s, json.dumps({"id": 2, "method": "Emulation.setDeviceMetricsOverride",
                                   "params": {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False}}))
            ws_send(s, json.dumps({"id": 3, "method": "Page.navigate", "params": {"url": url}}))
            deadline = time.time() + 40
            while time.time() < deadline:
                m = json.loads(ws_recv(s))
                if m.get("method") == "Page.loadEventFired":
                    break
            ws_send(s, json.dumps({"id": 4, "method": "Runtime.evaluate", "params": {"expression": JS, "awaitPromise": True, "returnByValue": True}}))
            while True:
                m = json.loads(ws_recv(s))
                if m.get("id") == 4:
                    break
            res = m["result"]["result"]
            if "value" not in res:
                raise RuntimeError(f"evaluate failed: {json.dumps(m)[:400]}")
            out = json.loads(res["value"])
        finally:
            proc.kill()
            proc.wait()
    if "--png" in sys.argv:
        out["first_viewport_color_share"] = color_share(sys.argv[sys.argv.index("--png") + 1])
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
