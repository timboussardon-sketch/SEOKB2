# -*- coding: utf-8 -*-
"""Cartes de score pour l'onglet Vitesse (Tim, 29/09/2026 : « tu dois faire des cards de scores vitesse »).
Réutilise les classes .kpis / .kpi de la coque, dans un conteneur .dashwrap."""
import html as _h

ICO = '<span class="ico-rond"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6a8 8 0 0 0-8 8h4a4 4 0 0 1 8 0h4a8 8 0 0 0-8-8z"/><path d="M12 14l3.5-3.5"/></svg></span>'

def _c(score):
    return "vert" if score >= 90 else ("orange" if score >= 50 else "rouge")

def _s(x):
    return f"{x:.2f}".replace(".", ",") + " s"

def carte(titre, n, l, src, couleur, aide=""):
    return (f'<div class="card kpi {couleur}">{ICO}<span class="t">{titre}</span>'
            f'<b class="n">{n}{aide}</b><span class="l">{l}</span><span class="src">{src}</span></div>')

def cartes_terrain(mobile=None, desktop=None, note=""):
    """mobile / desktop : dict lcp (s), inp (ms ou None), cls (float). None = non mesuré."""
    out = ['<div class="dashwrap"><div class="kpis">']
    if not mobile:
        out.append(carte("Chez vos visiteurs réels", "n. d.", "Google ne publie aucune donnée pour ce site",
                         "trop peu de visiteurs mesurés · expérience réelle non évaluée", "bleu"))
    else:
        lcp = mobile["lcp"]; out.append(carte("Affichage chez vos visiteurs · mobile", _s(lcp),
            "bon sous 2,5 s" if lcp <= 2.5 else ("à améliorer, entre 2,5 et 4 s" if lcp <= 4 else "lent, au-dessus de 4 s"),
            (f"ordinateur {_s(desktop['lcp'])} · " if desktop else "") + "75e percentile, 28 jours, tout le site", _c(95 if lcp <= 2.5 else 70 if lcp <= 4 else 30)))
        inp = mobile.get("inp")
        out.append(carte("Réactivité · mobile", f"{inp} ms" if inp is not None else "n. d.",
            ("bon sous 200 ms" if inp is not None and inp <= 200 else ("à améliorer" if inp is not None else "pas assez d'interactions enregistrées")),
            (f"ordinateur {desktop['inp']} ms" if desktop and desktop.get("inp") is not None else "mesure non disponible sur ordinateur"),
            _c(95 if inp is not None and inp <= 200 else (70 if inp is not None else 60))))
        cls = mobile["cls"]
        out.append(carte("Stabilité de la mise en page · mobile", f"{cls:.2f}".replace(".", ","),
            "bon sous 0,1" if cls < 0.1 else "à améliorer",
            (f"ordinateur {desktop['cls']:.2f}".replace(".", ",") if desktop else "") , _c(95 if cls < 0.1 else 70)))
    out.append("</div>" + (f'<p class="note">{note}</p>' if note else "") + "</div>")
    return "".join(out)

def cartes_pages(pages, principal="google"):
    """pages : liste de dict path, google_m (score, lcp), google_d (score, lcp) ou None, local (score, lcp), ttfb (ms), bloque (str).
    principal : « google » (score PSI mobile en gros chiffre) ou « local » (Lighthouse depuis mon poste)."""
    out = ['<div class="dashwrap"><div class="kpis">']
    for p in pages:
        sc, lcp = p["google_m"] if principal == "google" and p.get("google_m") else p["local"]
        src = []
        if principal == "google":
            if p.get("google_d"): src.append(f"ordinateur {p['google_d'][0]} · {_s(p['google_d'][1])}")
            if p.get("local"): src.append(f"mon poste {p['local'][0]} · {_s(p['local'][1])}")
        else:
            if p.get("google_m"): src.append(f"test Google {p['google_m'][0]} · {_s(p['google_m'][1])}")
        if p.get("ttfb") is not None: src.append("traitement serveur " + (f"{p['ttfb']/1000:.1f} s".replace(".", ",") if p["ttfb"] >= 1000 else f"{p['ttfb']} ms"))
        if p.get("bloque"): src.append(p["bloque"])
        out.append(carte(f'<code>{_h.escape(p["path"])}</code>', str(sc),
                         f"contenu principal affiché en {_s(lcp)} · mobile, " + ("test Google" if principal == "google" and p.get("google_m") else "depuis mon poste"),
                         " · ".join(src), _c(sc)))
    out.append("</div></div>")
    return "".join(out)

# ── lecture automatique des mesures d'un dossier d'audit ─────────────────────
import json as _json, hashlib as _hl, os as _os

def charge_mesures(dossier, bloque=None):
    """Lit pages5.txt, lh/, psi/ du dossier. Renvoie (terrain_mobile, terrain_desktop, pages) prêts pour cartes_terrain / cartes_pages.
    bloque : dict path -> texte « ce qui bloque »."""
    bloque = bloque or {}
    pages = []; tm = td = None
    for u in [l.strip() for l in open(_os.path.join(dossier, "pages5.txt")) if l.strip()]:
        h = _hl.md5(u.encode()).hexdigest(); path = "/" + u.split("/", 3)[3] if u.count("/") >= 3 else "/"
        d = {"path": path or "/", "bloque": bloque.get(path or "/", "")}
        try:
            lh = _json.load(open(_os.path.join(dossier, f"lh/{h}.json"))); a = lh["audits"]
            d["local"] = (round(lh["categories"]["performance"]["score"] * 100), a["largest-contentful-paint"]["numericValue"] / 1000)
            d["ttfb"] = round(a["server-response-time"]["numericValue"])
        except Exception: pass
        for s in ("mobile", "desktop"):
            try:
                p = _json.load(open(_os.path.join(dossier, f"psi/{h}-{s}.json"))); lr = p["lighthouseResult"]
                d["google_m" if s == "mobile" else "google_d"] = (round(lr["categories"]["performance"]["score"] * 100), lr["audits"]["largest-contentful-paint"]["numericValue"] / 1000)
                oe = p.get("originLoadingExperience", {}).get("metrics") or p.get("loadingExperience", {}).get("metrics")
                if oe and (s == "mobile" and tm is None or s == "desktop" and td is None):
                    m = {"lcp": (oe.get("LARGEST_CONTENTFUL_PAINT_MS", {}).get("percentile") or 0) / 1000,
                         "inp": oe.get("INTERACTION_TO_NEXT_PAINT", {}).get("percentile"),
                         "cls": (oe.get("CUMULATIVE_LAYOUT_SHIFT_SCORE", {}).get("percentile") or 0) / 100}
                    if s == "mobile": tm = m
                    else: td = m
            except Exception: pass
        pages.append(d)
    return tm, td, pages

def resume_mesures(pages):
    """min/max des LCP Google mobile et local, pour les phrases."""
    g = [p["google_m"][1] for p in pages if p.get("google_m")]; l = [p["local"][1] for p in pages if p.get("local")]
    gs = [p["google_m"][0] for p in pages if p.get("google_m")]
    f = lambda x: f"{x:.1f}".replace(".", ",")
    return {"g_min": f(min(g)) if g else "n. d.", "g_max": f(max(g)) if g else "n. d.", "l_min": f(min(l)) if l else "n. d.", "l_max": f(max(l)) if l else "n. d.",
            "gs_min": min(gs) if gs else "n. d.", "gs_max": max(gs) if gs else "n. d.", "n_g": len(g), "sup4_g": sum(1 for x in g if x > 4), "sup4_l": sum(1 for x in l if x > 4)}

# ── tableau « ce que Google lit de chaque page » : code initial vs rendu Chrome ─
import re as _re, html as _html

def _main_text(b):
    m = _re.search(r"<main[^>]*>(.*?)</main>", b, _re.S | _re.I); body = m.group(1) if m else (_re.search(r"<body[^>]*>(.*?)</body>", b, _re.S | _re.I) or _re.search(r"(.*)", b, _re.S)).group(1)
    body = _re.sub(r"<(script|style|nav|footer|header|noscript|svg)[^>]*>.*?</\1>", "", body, flags=_re.S | _re.I)
    return _re.sub(r"\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", " ", body))).strip()

def _links(b):
    m = _re.search(r"<main[^>]*>(.*?)</main>", b, _re.S | _re.I); body = m.group(1) if m else b
    body = _re.sub(r"<(nav|footer|header)[^>]*>.*?</\1>", "", body, flags=_re.S | _re.I)
    return {_re.sub(r"[?#].*$", "", h).rstrip("/") for h in _re.findall(r'<a[^>]+href=["\']([^"\'#][^"\']*)', body, _re.I) if not h.startswith(("mailto", "tel", "javascript"))}

def _meta(b):
    t = _re.search(r"<title[^>]*>(.*?)</title>", b, _re.S | _re.I); c = _re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', b) or _re.search(r'href=["\']([^"\']+)["\'][^>]*rel=["\']canonical', b)
    r = _re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']*)', b, _re.I)
    return (_html.unescape(t.group(1).strip()) if t else None, c.group(1) if c else None, r.group(1) if r else None)

def table_rendu(dossier):
    rows = []; diff = []; note = "Rien ne change après JavaScript sur ces cinq pages."
    for u in [l.strip() for l in open(_os.path.join(dossier, "pages5.txt")) if l.strip()]:
        h = _hl.md5(u.encode()).hexdigest(); f = _os.path.join(dossier, "html", _re.sub(r"[^a-z0-9]+", "-", u.lower()).strip("-") + ".html")
        path = "/" + u.split("/", 3)[3] if u.count("/") >= 3 else "/"
        try:
            ini = open(f, encoding="utf-8", errors="ignore").read(); dom = open(_os.path.join(dossier, f"dom/{h}.html"), encoding="utf-8", errors="ignore").read()
        except Exception:
            rows.append(f'<tr><td class="mono">{path or "/"}</td><td colspan="5">rendu non disponible</td></tr>'); continue
        if len(dom) < 2000:
            rows.append(f'<tr><td class="mono">{path or "/"}</td><td colspan="5">le rendu Chrome a échoué</td></tr>'); continue
        ti, td = _main_text(ini), _main_text(dom); li, ld = _links(ini), _links(dom); mi, md = _meta(ini), _meta(dom)
        wi, wd = len(ti.split()), len(td.split())
        texte = f"identique ({wi} mots)" if abs(wi - wd) <= max(5, wi * 0.05) else f"différent : {wi} mots avant, {wd} après"
        liens = f"identiques ({len(li)})" if li == ld else f"différents : {len(li)} avant, {len(ld)} après"
        if wi < 50 and wd > 200: texte = f"le texte n'existe qu'après JavaScript : {wi} mot(s) avant, {wd} après"; note = "Sur au moins une page, le contenu principal n'est présent qu'après exécution du JavaScript : Google doit rendre la page pour le lire."
        elif "différent" in texte or "différents" in liens or mi[0] != md[0]:
            diff.append(path or "/")
        rows.append(f'<tr><td class="mono">{path or "/"}</td><td>{texte}</td><td>{liens}</td><td>{"identique" if mi[0]==md[0] else "différent"}</td><td>{"identiques" if mi[2]==md[2] else "différentes"}</td><td>{"identique" if mi[1]==md[1] else "différente"}</td></tr>')
    if diff and note.startswith("Rien"): note = "Le JavaScript modifie le texte, les liens ou le titre sur : " + ", ".join(diff) + ". Google peut lire deux versions de ces pages ; la version rendue est celle qu'il garde, dans un second temps."
    return ('<p>J\'ai comparé le code envoyé par le serveur et la page une fois le JavaScript exécuté : texte principal, destination de chaque lien du texte, titre, directives, adresse de référence.</p>'
            '<div class="tablewrap"><table><thead><tr><th>Page</th><th>Texte principal</th><th>Liens du texte</th><th>Titre</th><th>Directives</th><th>Adresse de référence</th></tr></thead><tbody>' + "".join(rows) + '</tbody></table></div><p class="note">' + note + '</p>')

# ── mini-cartes de résumé et graphiques par onglet (Tim, 29/09/2026) ───────
_TON = {"vert": "vert", "orange": "orange", "rouge": "rouge", "bleu": "bleu", "gris": "gris"}

def minis(items):
    """items : liste de (valeur, phrase en mots de client, ton vert|orange|rouge|bleu|gris). 3 ou 4 cartes en tête d'onglet."""
    h = ['<div class="minis">']
    for v, l, t in items:
        h.append(f'<div class="mini {_TON.get(t, "gris")}"><b>{v}</b><span>{l}</span></div>')
    return "".join(h) + "</div>"

def _fmt(v):
    if isinstance(v, float): return f"{v:.1f}".replace(".", ",")
    return f"{v:,}".replace(",", " ") if isinstance(v, int) else str(v)

def barres(titre, rows, unite="", maxi=None, seuil=None, seuil_label="", note="", ton=None):
    """Graphique en barres horizontales. rows : liste de (libellé, valeur, ton) ; ton par barre ou fonction ton(valeur).
    seuil : valeur de repère tracée en pointillé (ex. 2,5 s)."""
    vals = [r[1] for r in rows if isinstance(r[1], (int, float))]
    m = maxi or (max(vals + ([seuil] if seuil else [])) if vals else 1) or 1
    h = [f'<div class="graf"><h4>{titre}</h4>']
    for lab, v, t in rows:
        tt = (ton(v) if callable(ton) else (t or "bleu")) if isinstance(v, (int, float)) else "gris"
        w = max(2, min(100, round(100 * v / m))) if isinstance(v, (int, float)) else 0
        # accord : « 0 lien », « 1 mot » (unité au pluriel par défaut ; « ms », « s », « Ko » ne bougent pas)
        u = unite[:-1] if isinstance(v, (int, float)) and abs(v) < 2 and len(unite) > 3 and unite.endswith("s") and " " not in unite else unite
        val = (_fmt(v) + (" " + u if u else "")) if isinstance(v, (int, float)) else str(v)
        h.append(f'<div class="graf-row"><span class="lbl">{lab}</span><span class="bar"><i class="{tt}" style="width:{w}%"></i>' + (f'<em class="seuil" style="left:{min(100, round(100 * seuil / m))}%"></em>' if seuil else "") + f'</span><span class="val">{val}</span></div>')
    if seuil: h.append(f'<p class="graf-note"><em class="seuil-l"></em> {seuil_label or "repère : " + _fmt(seuil) + " " + unite}' + (f" · {note}" if note else "") + "</p>")
    elif note: h.append(f'<p class="graf-note">{note}</p>')
    return "".join(h) + "</div>"

def pile(titre, segments, note=""):
    """Barre empilée : segments = liste de (libellé, valeur, ton). Montre une répartition (liens du menu / du texte, pages par famille…)."""
    tot = sum(v for _, v, _ in segments) or 1
    h = [f'<div class="graf"><h4>{titre}</h4><div class="pile">']
    for lab, v, t in segments:
        h.append(f'<i class="{t}" style="width:{max(1, round(100 * v / tot))}%" title="{lab} : {_fmt(v)}"></i>')
    h.append('</div><div class="pile-leg">')
    for lab, v, t in segments:
        h.append(f'<span><i class="{t}"></i>{lab} <b>{_fmt(v)}</b> ({round(100 * v / tot)} %)</span>')
    h.append("</div>" + (f'<p class="graf-note">{note}</p>' if note else "") + "</div>")
    return "".join(h)

def grille(titre, cols, rows, note=""):
    """Deux graphiques côte à côte ou plus : cols = liste de HTML (barres/pile). rows non utilisé."""
    return f'<div class="grafs">' + "".join(cols) + "</div>"

CSS_MINIS = """
/* ── mini-cartes et graphiques par onglet ── */
.minis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:18px 0 26px}
.mini{position:relative;overflow:hidden;isolation:isolate;border:0;border-radius:16px;padding:16px 18px;display:flex;flex-direction:column;gap:5px;color:#fff;background:linear-gradient(160deg,#2f4fe0 0%,#2f4fe0 45%,#7fa0ff 100%);box-shadow:0 10px 24px -14px rgba(33,55,157,.55)}
.mini::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;opacity:.32;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='3' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");background-size:260px 260px}
.mini b{font-size:24px;font-weight:700;letter-spacing:-.03em;line-height:1.1;color:#fff}
.mini span{font-size:13px;line-height:1.35;color:rgba(255,255,255,.88)}
.mini span::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:7px;vertical-align:1px;background:rgba(255,255,255,.45)}
.mini.vert span::before{background:#5fd48a}.mini.orange span::before{background:#ffc45c}.mini.rouge span::before{background:#ff7a6a}.mini.bleu span::before{background:#cfe0ff}.mini.gris span::before{background:rgba(255,255,255,.5)}
.graf{background:#fff;border:1px solid #e8e6e6;border-radius:16px;padding:16px 18px 12px;margin:14px 0 22px}
.grafs{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:14px 0 22px}
.grafs .graf{margin:0}
.graf h4{margin:0 0 12px;font-size:14px;font-weight:600;color:#2b2b30;background:none;-webkit-text-fill-color:initial}
.graf-row{display:grid;grid-template-columns:minmax(90px,34%) 1fr 74px;align-items:center;gap:10px;margin:6px 0;font-size:13px}
.graf-row .lbl{color:#6f6f78;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-family:'Geist Mono',ui-monospace,monospace;font-size:12px}
.graf-row .bar{position:relative;height:14px;background:#f3f5fb;border-radius:7px;overflow:visible}
.graf-row .bar i{display:block;height:100%;border-radius:7px;min-width:3px}
.graf-row .bar i.vert{background:#3f9a63}.graf-row .bar i.orange{background:#d99a2b}.graf-row .bar i.rouge{background:#cf4a3c}.graf-row .bar i.bleu{background:#2f4fe0}.graf-row .bar i.gris{background:#b9b9c2}.graf-row .bar i.tint{background:#aebcf3}
.graf-row .bar .seuil{position:absolute;top:-4px;bottom:-4px;border-left:2px dashed #9a9aa3}
.graf-row .val{text-align:right;font-family:'Geist Mono',ui-monospace,monospace;font-size:12px;color:#2b2b30;white-space:nowrap}
.graf-note{margin:10px 0 0;font-size:12.5px;color:#6f6f78}
.graf-note .seuil-l{display:inline-block;width:14px;border-top:2px dashed #9a9aa3;vertical-align:middle;margin-right:4px}
.pile{display:flex;height:18px;border-radius:9px;overflow:hidden;background:#f3f5fb}
.pile i{display:block;height:100%}
.pile i.vert{background:#3f9a63}.pile i.orange{background:#d99a2b}.pile i.rouge{background:#cf4a3c}.pile i.bleu{background:#2f4fe0}.pile i.gris{background:#b9b9c2}.pile i.tint{background:#aebcf3}
.pile-leg{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:10px;font-size:12.5px;color:#6f6f78}
.pile-leg i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:middle}
.pile-leg i.vert{background:#3f9a63}.pile-leg i.orange{background:#d99a2b}.pile-leg i.rouge{background:#cf4a3c}.pile-leg i.bleu{background:#2f4fe0}.pile-leg i.gris{background:#b9b9c2}.pile-leg i.tint{background:#aebcf3}
.pile-leg b{color:#2b2b30}
.markdown .minis+h3,.markdown .graf+h3{margin-top:28px}
p .tag,li .tag{display:inline-block;font-size:10.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;padding:2px 7px;border-radius:6px;background:#e8eeff;color:#1e2eba;margin-right:6px;vertical-align:middle;line-height:1.5}
.minis,.graf,.grafs{font-family:'Geist',system-ui,-apple-system,sans-serif}
.graf h4{text-transform:none;letter-spacing:0;font-size:14px}
.kchat .markdown .graf-note,.kchat .markdown .graf p{font-size:12.5px;line-height:1.45;margin:10px 0 0;color:#6f6f78}
.kchat .markdown .minis{margin:18px 0 26px}
/* ── aération : des paragraphes, pas des pavés (Tim, 29/09/2026) ──
   Les onglets 2 à 7 vivent dans .dashwrap, pas dans .markdown : viser les deux. */
.kchat .markdown p,.dashwrap>p,.dashwrap .card>p{margin-top:26px!important}
.dashwrap .card-head .sous{margin-top:8px!important}
.dashwrap>h2{margin-bottom:0!important}
.dashwrap>h3,.kchat .markdown h3{margin-top:60px!important;margin-bottom:0!important}
.dashwrap>h4,.kchat .markdown h4{margin-top:48px!important;margin-bottom:0!important}
.dashwrap>ol,.dashwrap>ul,.kchat .markdown ol,.kchat .markdown ul{margin-top:22px!important}
.dashwrap li,.kchat .markdown li{margin-top:12px!important;line-height:1.75}
.dashwrap>.tablewrap,.dashwrap>table,.kchat .markdown .tablewrap{margin-top:26px!important}
.dashwrap details.repli,.kchat .markdown details.repli{margin-top:44px!important}
.dashwrap .minis,.kchat .markdown .minis{margin:26px 0 26px!important}
.dashwrap>.graf,.dashwrap>.grafs{margin-top:26px!important}
.dashwrap .card .note{margin-top:22px!important}
.dashwrap .card .card-head+.note{margin-top:16px!important}
.dashwrap .graf .graf-note{margin-top:12px!important}
@media (max-width:640px){.graf-row{grid-template-columns:1fr;gap:4px}.graf-row .val{text-align:left}}
"""

def graf_vitesse(pages, seuil=2.5):
    """Barres d'affichage (LCP) dans le test Google, mobile, page par page, repère 2,5 s. pages : sortie de charge_mesures."""
    rows = []
    for p in pages:
        g = p.get("google_m"); v = (g[1] if g else None)
        rows.append((p["path"], round(v, 2) if v is not None else "n. d.", None))
    ton = lambda v: "vert" if v <= seuil else ("orange" if v <= 4 else "rouge")
    return barres("Temps d'affichage de l'élément principal, test Google (mobile)", rows, "s", seuil=seuil, seuil_label="repère Google : 2,5 s", ton=ton)

def graf_vitesse_poste(pages, seuil=2.5):
    rows = []
    for p in pages:
        l = p.get("local"); v = (l[1] if l else None)
        rows.append((p["path"], round(v, 2) if v is not None else "n. d.", None))
    ton = lambda v: "vert" if v <= seuil else ("orange" if v <= 4 else "rouge")
    return barres("Même mesure depuis mon poste (Lighthouse, mobile simulé)", rows, "s", seuil=seuil, seuil_label="repère Google : 2,5 s", ton=ton)

def graf_volumes(dossier, n=8):
    """Barres des recherches par mois des premiers mots-clés du top 20 (top20_rows.json écrit par top20.py)."""
    import json as _j
    f = _os.path.join(dossier, "top20_rows.json")
    if not _os.path.exists(f): return ""
    rows = _j.load(open(f, encoding="utf-8"))
    rows = sorted(rows, key=lambda r: -(r.get("vol") or 0))[:n]
    return barres("Recherches par mois sur Google (Keyword Planner) : les plus demandées du top 20", [(r["kw"], r.get("vol") or 0, "bleu" if r.get("n", 0) >= 8 else "tint") for r in rows], "", note="en bleu foncé, les mots-clés notés 8 ou plus ; en bleu pâle, les autres")
