(() => {
  const D = window.LOOKETAL;
  const U = D.ui, AS = D.assets;  // UI strings for this language; prefix for shared assets (docs/assets)
  const fmt = (s, o) => s.replace(/\{(\w+)\}/g, (_, k) => o[k]);
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function toast(msg) {
    let t = document.querySelector(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; document.body.append(t); }
    t.textContent = msg; t.classList.add("on"); setTimeout(() => t.classList.remove("on"), 1300);
  }
  async function copy(text) {
    try { await navigator.clipboard.writeText(text); toast(U.copied); } catch { toast(U.copy_failed); }
  }

  // theme: auto (follows the OS) -> light -> dark; remembered per browser when storage is available
  const themes = ["auto", "light", "dark"];
  const applyTheme = t => { if (t === "auto") document.documentElement.removeAttribute("data-theme"); else document.documentElement.setAttribute("data-theme", t);
    const b = $("theme"); if (b) b.textContent = `${U.theme}: ${U["theme_" + t]}`; };
  let theme = "auto";
  try { theme = localStorage.getItem("looketal-theme") || "auto"; } catch {}
  applyTheme(theme);
  if ($("theme")) $("theme").onclick = () => { theme = themes[(themes.indexOf(theme) + 1) % 3]; applyTheme(theme);
    try { localStorage.setItem("looketal-theme", theme); } catch {} };

  const strip = e => `<div class="strip">${e.palette.slice(0, 6).map(p => `<em style="background:${esc(p.hex)}"></em>`).join("")}</div>`;
  function specimen(e) {
    const [bg, text, accent] = e.specimen;
    const pills = (e.kind === "project" ? ["Paper", "Code", "Video"] : e.kind === "readme" ? ["Install", "Usage", "Cite"] : ["CV", "Scholar", "Email"])
      .map(t => `<i style="background:${esc(accent)}">${t}</i>`).join("");
    const font = e.fonts[0] ? `'${esc(e.fonts[0])}',` : "";
    return `<div class="spec" style="background:${esc(bg)};color:${esc(text)};font-family:${font}system-ui,sans-serif" aria-hidden="true">
      <b class="aa">Aa</b><span style="color:${esc(accent)}">${esc(e.fonts[0] || "system font")}</span><div class="pills">${pills}</div>${strip(e)}</div>`;
  }
  const thumb = e => e.shot ? `<div class="shot"${e.tall ? ` data-tall="${AS}assets/shots/${esc(e.slug)}.tall.webp"` : ""}><img src="${AS}assets/shots/${esc(e.slug)}.card.webp" alt="" loading="lazy" width="640" height="400">${strip(e)}</div>` : specimen(e);
  function card(e) {
    const meta = e.kind === "project" ? e.venue : `${e.kind === "readme" ? U.readme : U.researcher} · ${e.venue}`;
    return `<a class="card" href="s/${esc(e.slug)}.html">${thumb(e)}<div class="cbody"><div class="meta">${esc(meta)}</div>
      <div class="name">${esc(e.title)}</div><div class="mood">${esc(e.mood)}</div></div></a>`;
  }

  // hover preview: on first hover a card fetches the tall capture, which then scrolls inside the card
  document.addEventListener("pointerover", ev => {
    const box = ev.target.closest && ev.target.closest(".shot[data-tall]");
    if (!box || box.querySelector("img.tall")) return;
    const im = new Image(); im.className = "tall"; im.alt = ""; im.decoding = "async";
    im.onload = () => requestAnimationFrame(() => im.classList.add("ready"));
    im.src = box.dataset.tall; box.prepend(im);
  });

  // language links keep the current filters and anchor
  document.querySelectorAll(".langs a").forEach(a => { a.href += location.search + location.hash; });

  // ---- browse page ----
  if ($("grid") && $("filters")) {
    const P = new URLSearchParams(location.search);
    const st = { q: (P.get("q") || "").toLowerCase(), kind: P.get("kind") || "", conf: P.get("conf") || "", year: P.get("year") || "",
      tpl: P.get("tpl") || "", theme: P.get("theme") || "", collection: P.get("collection") || "",
      mods: new Set(P.getAll("module")) };
    const uniq = (f, s) => [...new Set(D.entries.map(f).filter(Boolean))].sort(s);
    uniq(e => e.conf).forEach(v => $("conf").add(new Option(v, v)));
    uniq(e => e.year, (a, b) => b - a).forEach(v => $("year").add(new Option(v, v)));
    uniq(e => e.template_group).forEach(v => $("tpl").add(new Option(v, v)));
    const counts = {};
    D.entries.forEach(e => e.modules.forEach(m => counts[m] = (counts[m] || 0) + 1));
    Object.keys(counts).sort((a, b) => counts[b] - counts[a]).forEach(m => {
      const b = document.createElement("button"); b.className = "chip"; b.innerHTML = `${esc(U.mods[m] || m)} <span>${counts[m]}</span>`;
      b.setAttribute("aria-pressed", st.mods.has(m));
      b.onclick = () => { st.mods.has(m) ? st.mods.delete(m) : st.mods.add(m); b.setAttribute("aria-pressed", st.mods.has(m)); render(); };
      $("mods").append(b);
    });
    $("q").value = P.get("q") || "";
    for (const k of ["conf", "year", "tpl", "theme"]) $(k).value = st[k];
    const syncSeg = () => [...$("kind").children].forEach(x => x.setAttribute("aria-pressed", x.dataset.v === st.kind));
    syncSeg();
    const inColl = st.collection && D.collections[st.collection] ? new Set(D.collections[st.collection]) : null;

    function match(e) {
      if (inColl && !inColl.has(e.slug)) return false;
      if (st.kind && e.kind !== st.kind) return false;
      if (st.conf && e.conf !== st.conf) return false;
      if (st.year && String(e.year) !== st.year) return false;
      if (st.tpl && e.template_group !== st.tpl) return false;
      if (st.theme && e.theme !== st.theme) return false;
      for (const m of st.mods) if (!e.modules.includes(m)) return false;
      if (st.q) {
        const h = [e.title, e.person, e.field, e.mood, e.venue, e.template, e.style_name, e.fonts.join(" ")].join(" ").toLowerCase();
        if (h.includes(st.q)) { e._rank = 0; return true; }
        const t = window.LOOKETAL_TEXT && window.LOOKETAL_TEXT[e.slug];
        if (t && t.includes(st.q)) { e._rank = 1; return true; }
        return false;
      }
      e._rank = 0;
      return true;
    }
    function writeUrl() {
      const p = new URLSearchParams();
      for (const k of ["kind", "conf", "year", "tpl", "theme", "collection"]) if (st[k]) p.set(k, st[k]);
      if (st.q) p.set("q", st.q);
      st.mods.forEach(m => p.append("module", m));
      history.replaceState(null, "", "?" + p.toString());
    }
    function render() {
      const list = D.entries.filter(match).sort((a, b) => a._rank - b._rank);
      const title = inColl ? D.collectionTitles[st.collection]
        : st.kind === "project" ? U.nav_project : st.kind === "researcher" ? U.nav_researcher : st.kind === "readme" ? U.nav_readme : U.nav_all;
      $("btitle").textContent = title;
      $("bcount").textContent = fmt(U.count, { n: list.length, total: D.entries.length }) +
        (st.q ? (window.LOOKETAL_TEXT ? U.searching : U.loading_index) : "");
      $("grid").innerHTML = list.length ? list.map(card).join("") : `<div class="empty">${esc(U.no_match)}</div>`;
      document.querySelectorAll('.side nav a').forEach(a => {
        const h = a.getAttribute("href");
        const k = h.includes("kind=project") ? "project" : h.includes("kind=researcher") ? "researcher" : h.includes("kind=readme") ? "readme" : h === "browse.html" ? "all" : null;
        if (k) a.toggleAttribute("aria-current", (st.kind || "all") === k && !inColl);
      });
      writeUrl();
    }
    let textLoading = false;
    function needText() {
      if (window.LOOKETAL_TEXT || textLoading || !st.q) return;
      textLoading = true;
      const sc = document.createElement("script"); sc.src = AS + "assets/search.js"; sc.onload = render; document.body.append(sc);
    }
    $("q").oninput = ev => { st.q = ev.target.value.trim().toLowerCase(); needText(); render(); };
    needText();
    for (const k of ["conf", "year", "tpl", "theme"]) $(k).onchange = ev => { st[k] = ev.target.value; render(); };
    $("kind").onclick = ev => { const b = ev.target.closest("button"); if (!b) return; st.kind = b.dataset.v; syncSeg(); render(); };
    render();
  }

  // ---- style page ----
  const dataEl = document.getElementById("style-data");
  if (dataEl) {
    const S = JSON.parse(dataEl.textContent);
    document.querySelectorAll(".mdx[data-block]").forEach(el => {
      const src = S.blocks[el.dataset.block] || "";
      el.innerHTML = window.marked ? marked.parse(src) : `<p>${esc(src)}</p>`;
    });
    let tab = "md", mode = "extended";
    const body = $("pbody");
    const text = () => tab === "md" ? (mode === "compact" ? S.compact : S.md) : tab === "css" ? S.css : tab === "tw" ? S.tw : S.tokens;
    const show = () => { body.textContent = text() || U.not_available; $("mode").style.visibility = tab === "md" ? "visible" : "hidden"; };
    document.querySelector(".ptabs").onclick = ev => {
      const b = ev.target.closest("button"); if (!b) return; tab = b.dataset.tab;
      document.querySelectorAll(".ptabs button").forEach(x => x.setAttribute("aria-selected", x === b)); show();
    };
    $("mode").onclick = ev => {
      const b = ev.target.closest("button"); if (!b) return; mode = b.dataset.v;
      [...$("mode").children].forEach(x => x.setAttribute("aria-pressed", x === b)); show();
    };
    $("pcopy").onclick = () => copy(text());
    document.querySelectorAll(".sw[data-copy]").forEach(b => b.onclick = () => copy(b.dataset.copy));
    show();
  }
})();
