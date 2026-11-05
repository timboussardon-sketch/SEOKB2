#!/usr/bin/env python3
"""Étape 0 du skill maillage-systeme : ingestion déterministe d'un site.

Entrée  : une URL de sitemap (ou une URL de base, on tente /sitemap.xml).
Sortie  : index.json (une ligne légère par page) + graph.json (tous les liens
          internes avec leur ancre, leur passage d'ancrage, in-body ou non) + un résumé sur stdout.

Aucune dépendance externe (stdlib uniquement). Aucun LLM : le graphe est exact.

Usage :
  python3 crawl_graph.py https://exemple.com/sitemap.xml -o ./maillage-data
  python3 crawl_graph.py https://exemple.com --limit 50 --delay 0.3
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, urlunsplit

UA = "Mozilla/5.0 (compatible; maillage-systeme/1.0; audit maillage interne)"
# Zones dont les liens ne comptent pas comme liens éditoriaux in-body
CHROME_TAGS = {"nav", "header", "footer", "aside"}
# Blocs de texte : le paragraphe autour d'un lien sert à juger ce lien sur son
# contexte et non sur le seul titre de la cible.
BLOCK_TAGS = {"p", "li", "td", "th", "blockquote", "dd", "dt", "figcaption",
              "h1", "h2", "h3", "h4", "h5", "h6", "section", "article", "div"}
PASSAGE_MAX = 400
# Un bloc qui n'est qu'une suite d'ancres (carrousel de logos, liste de liens)
# ressemble à du contexte sans en être. En dessous de ce nombre de caractères de
# prose hors ancres, on n'attribue pas de passage : le lien s'évalue alors sur
# le titre de la cible, et le rapport porte la limite au lieu d'un faux contexte.
PROSE_MIN = 40
# Second signal : un carrousel de logos concatène ses libellés sans espace
# (« Client AClient BClient C… »). Le compte de mots l'écarte là où la
# longueur seule le laisse passer.
PROSE_MOTS_MIN = 10
TRACKING_PARAMS = re.compile(r"^(utm_|fbclid|gclid|ref$)")


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def sitemap_urls(sitemap_url):
    """Retourne toutes les URLs de pages du sitemap (gère les sitemap index)."""
    xml = fetch(sitemap_url)
    root = ET.fromstring(xml.encode())
    ns = {"sm": root.tag.split("}")[0].strip("{")} if "}" in root.tag else {}
    tag = lambda name: f"sm:{name}" if ns else name
    urls = []
    if root.tag.endswith("sitemapindex"):
        for loc in root.iterfind(f".//{tag('sitemap')}/{tag('loc')}", ns):
            urls.extend(sitemap_urls(loc.text.strip()))
    else:
        for loc in root.iterfind(f".//{tag('url')}/{tag('loc')}", ns):
            urls.append(loc.text.strip())
    return urls


def normalize(url, base):
    """URL absolue, sans fragment, sans params de tracking, sans slash final."""
    absolute = urljoin(base, url)
    parts = urlsplit(absolute)
    if parts.scheme not in ("http", "https"):
        return None
    query = "&".join(
        p for p in parts.query.split("&") if p and not TRACKING_PARAMS.match(p)
    )
    path = parts.path.rstrip("/") or "/"
    host = parts.netloc.lower().removeprefix("www.")
    return urlunsplit((parts.scheme, host, path, query, ""))


class PageParser(HTMLParser):
    """Extrait titre, meta description, h1 et liens (avec zone in-body ou non)."""

    def __init__(self, base_url):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title = ""
        self.description = ""
        self.h1 = ""
        self.links = []  # (href, anchor_text, in_body, passage)
        self._block_parts = []      # texte du bloc courant
        self._block_anchor_len = 0  # part de ce texte occupée par des ancres
        self._pending = []          # index des liens ouverts dans ce bloc
        self._chrome_depth = 0
        self._in_title = False
        self._in_h1 = False
        self._current_link = None  # [href, [text_parts], in_body]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in BLOCK_TAGS:
            self._fermer_bloc()
        if tag in CHROME_TAGS:
            self._chrome_depth += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "meta" and attrs.get("name", "").lower() == "description":
            self.description = (attrs.get("content") or "").strip()
        elif tag == "a" and attrs.get("href"):
            self._current_link = [attrs["href"], [], self._chrome_depth == 0]

    def _fermer_bloc(self):
        """Attribue le texte du bloc aux liens qu'il contient, puis repart à vide."""
        texte = re.sub(r"\s+", " ", "".join(self._block_parts)).strip()
        prose = len(texte) - self._block_anchor_len
        if texte and prose >= PROSE_MIN and len(texte.split()) >= PROSE_MOTS_MIN:
            for i in self._pending:
                if not self.links[i][3]:
                    self.links[i][3] = texte[:PASSAGE_MAX]
        self._block_parts = []
        self._block_anchor_len = 0
        self._pending = []

    def close(self):
        super().close()
        self._fermer_bloc()

    def handle_endtag(self, tag):
        if tag in BLOCK_TAGS:
            self._fermer_bloc()
        if tag in CHROME_TAGS and self._chrome_depth > 0:
            self._chrome_depth -= 1
        elif tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "a" and self._current_link:
            href, parts, in_body = self._current_link
            anchor = re.sub(r"\s+", " ", "".join(parts)).strip()
            self.links.append([href, anchor, in_body, ""])
            self._block_anchor_len += len(anchor)
            self._pending.append(len(self.links) - 1)
            self._current_link = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1 and not self.h1.strip():
            self.h1 += data
        if self._current_link:
            self._current_link[1].append(data)
        self._block_parts.append(data)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sitemap", help="URL du sitemap.xml ou URL de base du site")
    ap.add_argument("-o", "--out", default=".", help="dossier de sortie")
    ap.add_argument("--limit", type=int, default=0, help="max de pages (0 = tout)")
    ap.add_argument("--delay", type=float, default=0.2, help="pause entre requêtes (s)")
    args = ap.parse_args()

    sitemap = args.sitemap
    if not sitemap.endswith(".xml"):
        sitemap = sitemap.rstrip("/") + "/sitemap.xml"

    pages = sitemap_urls(sitemap)
    if args.limit:
        pages = pages[: args.limit]
    site_host = urlsplit(pages[0]).netloc.lower().removeprefix("www.")
    known = {normalize(u, u) for u in pages}

    index, edges, errors = {}, [], []
    for i, url in enumerate(pages, 1):
        page_key = normalize(url, url)
        try:
            html = fetch(url)
        except Exception as e:
            errors.append({"url": url, "error": str(e)})
            print(f"[{i}/{len(pages)}] ERREUR {url} : {e}", file=sys.stderr)
            continue
        parser = PageParser(url)
        try:
            parser.feed(html)
            parser.close()
        except Exception as e:
            errors.append({"url": url, "error": f"parse: {e}"})
            continue
        for href, anchor, in_body, passage in parser.links:
            target = normalize(href, url)
            if not target or urlsplit(target).netloc != site_host:
                continue
            if target == page_key:
                continue
            edges.append(
                {
                    "source": page_key,
                    "target": target,
                    "anchor": anchor,
                    "in_body": in_body,
                    "passage": passage,
                    "target_in_sitemap": target in known,
                }
            )
        index[page_key] = {
            "url": page_key,
            "title": re.sub(r"\s+", " ", parser.title).strip(),
            "h1": re.sub(r"\s+", " ", parser.h1).strip(),
            "description": parser.description,
            "inbound_in_body": 0,
            "outbound_in_body": 0,
        }
        print(f"[{i}/{len(pages)}] {page_key}", file=sys.stderr)
        if args.delay:
            time.sleep(args.delay)

    # Un même couple (cible, ancre) présent sur la quasi-totalité des pages
    # est un lien de gabarit (menu/footer non sémantique), pas un lien éditorial
    from collections import defaultdict

    pair_sources = defaultdict(set)
    for e in edges:
        if e["in_body"]:
            pair_sources[(e["target"], e["anchor"])].add(e["source"])
    sitewide_threshold = max(3, int(len(index) * 0.8))
    for e in edges:
        e["sitewide"] = (
            e["in_body"]
            and len(pair_sources[(e["target"], e["anchor"])]) >= sitewide_threshold
        )

    # Compteurs sur les liens in-body non sitewide uniquement (nav/footer et
    # liens de gabarit ne comptent pas comme maillage éditorial dans la méthode)
    for e in edges:
        if not e["in_body"] or e["sitewide"]:
            continue
        if e["source"] in index:
            index[e["source"]]["outbound_in_body"] += 1
        if e["target"] in index:
            index[e["target"]]["inbound_in_body"] += 1

    orphans = [u for u, p in index.items() if p["inbound_in_body"] == 0]
    dead_ends = [u for u, p in index.items() if p["outbound_in_body"] == 0]

    import os

    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "index.json"), "w") as f:
        json.dump(
            {
                "site": site_host,
                "crawled": len(index),
                "errors": errors,
                "orphans": orphans,
                "dead_ends": dead_ends,
                "pages": list(index.values()),
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    with open(os.path.join(args.out, "graph.json"), "w") as f:
        json.dump(edges, f, ensure_ascii=False, indent=2)

    in_body_edges = sum(1 for e in edges if e["in_body"] and not e["sitewide"])
    sitewide_edges = sum(1 for e in edges if e["sitewide"])
    print(
        f"\n{len(index)} pages crawlées, {len(edges)} liens internes "
        f"({in_body_edges} éditoriaux, {sitewide_edges} de gabarit), "
        f"{len(orphans)} orphelines, "
        f"{len(dead_ends)} dead-ends, {len(errors)} erreurs.\n"
        f"Sorties : {args.out}/index.json et {args.out}/graph.json"
    )


if __name__ == "__main__":
    main()
