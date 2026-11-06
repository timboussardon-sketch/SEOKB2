# -*- coding: utf-8 -*-
"""Réduit les 26 Mo de relevés d'un audit à une synthèse de quelques kilo-octets.

    python3 digest.py <dossier du site>

Écrit <dossier>/digest.md. Aucun agent ne doit ouvrir lh/, psi/, maillage/ ni
crawl-initial.json : un rapport Lighthouse pèse 800 Ko, soit ~220 000 jetons.
Tout passe par ici.
"""
import json, glob, os, sys, hashlib, collections

def _lire(f):
    try: return json.load(open(f, encoding="utf-8"))
    except Exception: return None

def digest(d):
    out = []
    host = ""
    pages = [l.strip() for l in open(os.path.join(d, "pages5.txt"), encoding="utf-8") if l.strip()]
    if pages: host = pages[0].split("/")[2]
    out.append(f"# Relevé de {host}\n")

    crawl = _lire(os.path.join(d, "crawl-initial.json")) or []
    if crawl:
        codes = collections.Counter(str(p.get("code")) for p in crawl)
        noindex = [p["url"] for p in crawl if "noindex" in (str(p.get("robots") or "") + str(p.get("x_robots") or "")).lower()]
        sans_desc = [p["url"] for p in crawl if not p.get("meta")]
        h1 = collections.Counter(sum(1 for n, _ in (p.get("hn") or []) if n == 1) for p in crawl)
        sauts = [p["url"] for p in crawl
                 if any(b - a > 1 for (a, _), (b, __) in zip(p.get("hn") or [], (p.get("hn") or [])[1:]))]
        mots = sorted(((p.get("words_main") or 0), p["url"]) for p in crawl)
        titres = collections.Counter(p.get("title") for p in crawl if p.get("title"))
        dup = [(t, n) for t, n in titres.items() if n > 1]
        out.append(f"## Pages relevées : {len(crawl)}")
        out.append(f"- codes : {dict(codes)}")
        out.append(f"- interdites à Google : {len(noindex)} {noindex[:5]}")
        out.append(f"- sans description : {len(sans_desc)} {sans_desc[:5]}")
        out.append(f"- nombre de H1 par page : {dict(h1)}")
        out.append(f"- sauts de niveau dans les titres : {len(sauts)} {sauts[:5]}")
        out.append(f"- pages les plus courtes : {mots[:5]}")
        out.append(f"- pages les plus longues : {mots[-3:]}")
        out.append(f"- titres partagés : {len(dup)} {dup[:5]}")
        hors = [p["url"] for p in crawl if p.get("canonical") and p["canonical"].rstrip("/") != p["url"].rstrip("/")]
        out.append(f"- adresse de référence différente de la page : {len(hors)} {hors[:5]}")
        out.append(f"- pages redirigées : {sum(1 for p in crawl if p.get('redirects'))}")
        out.append(f"- versions de langue déclarées : {sum(1 for p in crawl if p.get('hreflang'))}\n")

    sm = os.path.join(d, "sitemap-urls.txt")
    if os.path.exists(sm):
        n = sum(1 for _ in open(sm, encoding="utf-8"))
        fam = collections.Counter(l.strip().replace(f"https://{host}/", "").split("/")[0] for l in open(sm, encoding="utf-8") if l.strip())
        out.append(f"## Sitemap : {n} adresses")
        out.append(f"- familles : {dict(fam.most_common(10))}\n")

    s4 = os.path.join(d, "soft404.txt")
    if os.path.exists(s4):
        out.append("## Fausses adresses")
        for l in open(s4, encoding="utf-8"):
            p = l.strip().split("|")
            if len(p) > 2: out.append(f"- {p[0]} → code {p[1]}")
        out.append("")

    g = _lire(os.path.join(d, "maillage", "graph.json"))
    if g:
        e = g if isinstance(g, list) else g.get("edges") or g.get("links") or []
        corps = [x for x in e if x.get("in_body")]
        entrants = collections.Counter(x["target"] for x in corps)
        out.append(f"## Liens internes : {len(e)} au total, {len(corps)} dans le texte")
        out.append(f"- les plus reliés : {entrants.most_common(8)}")
        cibles = set(x["target"] for x in corps)
        toutes = set(x["source"] for x in e) | set(x["target"] for x in e)
        out.append(f"- sans lien dans le texte : {len(toutes - cibles)}\n")

    lignes = []
    for f in sorted(glob.glob(os.path.join(d, "lh", "*.json"))):
        j = _lire(f)
        if not j or "audits" not in j: continue
        a = j["audits"]
        u = j.get("finalDisplayedUrl", "").replace(f"https://{host}", "") or "/"
        try:
            lcp = a["largest-contentful-paint"]["numericValue"] / 1000
            srt = a["server-response-time"]["numericValue"]
            ph = {}
            det = a.get("lcp-breakdown-insight", {}).get("details", {})
            for it in det.get("items", []):
                for r in it.get("items", []):
                    if r.get("phase"): ph[r["phase"]] = round(r.get("duration") or 0)
            lignes.append(f"- {u} : affichage {lcp:.2f} s, traitement serveur {round(srt)} ms, phases {ph}")
        except Exception: pass
    if lignes:
        out.append("## Depuis mon poste (Lighthouse, mobile)")
        out += lignes + [""]

    lignes, crux = [], None
    for f in sorted(glob.glob(os.path.join(d, "psi", "*-mobile.json"))):
        j = _lire(f)
        if not j or "lighthouseResult" not in j: continue
        lr = j["lighthouseResult"]; a = lr["audits"]
        u = lr.get("finalDisplayedUrl", "").replace(f"https://{host}", "") or "/"
        sc = int(lr["categories"]["performance"]["score"] * 100)
        lignes.append(f"- {u} : {a['largest-contentful-paint']['numericValue']/1000:.2f} s, score {sc}")
        if j.get("loadingExperience", {}).get("metrics"): crux = j["loadingExperience"]["metrics"]
    if lignes:
        out.append("## Test Google (PageSpeed, mobile)")
        out += lignes
        out.append(f"- visiteurs réels : {'oui, ' + str({k: v.get('percentile') for k, v in crux.items()}) if crux else 'Google ne publie rien pour ce site'}\n")

    pl = _lire(os.path.join(d, "planner.json"))
    if pl:
        ex = sorted(pl.get("exacts", {}).items(), key=lambda x: -(x[1].get("volume") or 0))
        out.append("## Keyword Planner, recherches par mois")
        for k, v in ex[:25]:
            out.append(f"- {v.get('volume') or 0} · {v.get('competition') or ''} · {k}")
        out.append("")

    for f in ("serp.txt", "accept-language.txt"):
        p = os.path.join(d, f)
        if os.path.exists(p):
            out.append(f"## {f}")
            out.append(open(p, encoding="utf-8").read().strip()[:2000] + "\n")

    return "\n".join(out)

if __name__ == "__main__":
    d = sys.argv[1]
    t = digest(d)
    open(os.path.join(d, "digest.md"), "w", encoding="utf-8").write(t)
    brut = sum(os.path.getsize(f) for p in ("lh", "psi", "maillage") for f in glob.glob(os.path.join(d, p, "*")))
    print(f"digest.md écrit : {len(t)/1024:.1f} Ko, à partir de {brut/1024/1024:.1f} Mo de relevés")
