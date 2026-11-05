#!/usr/bin/env python3
"""Projection régénérable des publications dont la mise en ligne est prouvée.

Le registre historique est une liste de candidats, jamais une preuve. Une capture
HTTP datée et conservée séparément doit attester chaque URL et sa date. Le hash
empêche qu'une capture modifiée continue de justifier une publication.
"""
import argparse
import hashlib
import json
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

VAULT = Path(__file__).resolve().parents[2]
REGISTRE = VAULT / "wiki/apprentissage/publications.jsonl"
VERIFIEES = VAULT / "wiki/apprentissage/publications-verifiees.json"
REFUSEES = VAULT / "wiki/apprentissage/publications-refusees.json"


class PageMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = None
        self.published = None

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if tag == "link" and props.get("rel", "").lower() == "canonical":
            self.canonical = props.get("href")
        if tag == "meta" and props.get("property", "").lower() == "article:published_time":
            self.published = props.get("content")


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def capture_page(url, vault=VAULT):
    """Capture HTTP à faire au moment de la publication, sans suivre les redirects."""
    key = canonical(url)
    domains = (Path(vault) / "wiki/apprentissage/domaines.txt").read_text().splitlines()
    if not key or urlsplit(key).hostname not in domains:
        raise ValueError("URL hors des propriétés GSC ou non éditoriale")
    opener = build_opener(NoRedirect)
    with opener.open(Request(url, headers={"User-Agent": "seo-kb-evidence/1.0"}), timeout=10) as response:
        if response.status != 200:
            raise ValueError("réponse HTTP différente de 200")
        html = response.read(2_000_001)
        if len(html) > 2_000_000:
            raise ValueError("page trop volumineuse")
    parser = PageMetadata()
    parser.feed(html.decode("utf-8", errors="replace"))
    if canonical(parser.canonical or "") != key or not parser.published:
        raise ValueError("canonique ou article:published_time manquant")
    published = date.fromisoformat(parser.published[:10]).isoformat()
    captured = datetime.now().astimezone().isoformat()
    if not date.fromisoformat(published) <= date.fromisoformat(captured[:10]) <= date.fromisoformat(published) + timedelta(days=1):
        raise ValueError("capture trop tardive pour attester la date de publication")
    record = {"url": url, "canonical": parser.canonical, "status": 200,
              "captured_at": captured, "published_at": published}
    raw = (json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    digest = hashlib.sha256(raw).hexdigest()
    directory = Path(vault) / "wiki/apprentissage/captures"
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{digest}.json"
    path.write_bytes(raw)
    return {"publie": published, "url": url,
            "evidence": {"path": str(path.relative_to(vault)), "sha256": digest}}


def canonical(url):
    try:
        p = urlsplit(url)
        if p.scheme != "https" or not p.hostname or p.username or p.password:
            return None
        host = p.hostname.lower().removeprefix("www.")
        path = p.path.rstrip("/") or "/"
        if p.query or p.fragment or path == "/":
            return None
        if any(part in {"auth", "oauth", "callback", "api", "app", "app2"}
               for part in path.lower().split("/")):
            return None
        return urlunsplit(("https", host, path, "", ""))
    except ValueError:
        return None


def validate(url, published, evidence, vault=VAULT):
    key = canonical(url)
    if key is None:
        return None, "URL non éditoriale ou non canonique"
    try:
        day = date.fromisoformat(published)
    except (TypeError, ValueError):
        return None, "date de publication invalide"
    if not isinstance(evidence, dict) or not evidence.get("path") or not evidence.get("sha256"):
        return None, "preuve de mise en ligne absente"
    root = (Path(vault) / "wiki/apprentissage/captures").resolve()
    path = (Path(vault) / evidence["path"]).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        return None, "preuve hors périmètre ou introuvable"
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != evidence["sha256"]:
        return None, "preuve modifiée depuis son référencement"
    try:
        capture = json.loads(raw)
        captured = datetime.fromisoformat(capture["captured_at"].replace("Z", "+00:00")).date()
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return None, "capture illisible ou non datée"
    if (capture.get("status") != 200 or canonical(capture.get("url", "")) != key
            or canonical(capture.get("canonical", "")) != key):
        return None, "URL, canonique ou statut HTTP contradictoire"
    if capture.get("published_at") != published or not day <= captured <= day + timedelta(days=1):
        return None, "date de mise en ligne non attestée par la capture"
    return {"source_reference": str(path.relative_to(Path(vault).resolve())), "sha256": digest,
            "captured_at": capture["captured_at"], "status": 200}, None


def project(registry=REGISTRE, vault=VAULT):
    accepted, rejected, seen = [], [], set()
    for line_no, line in enumerate(Path(registry).read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            rejected.append({"line": line_no, "reason": "JSON invalide"})
            continue
        for url in row.get("urls", []):
            published = row.get("publie")
            key = canonical(url)
            event_id = hashlib.sha256(f"{published}|{key or url}".encode()).hexdigest()[:20]
            origin = f"wiki/apprentissage/publications.jsonl#L{line_no}"
            if (published, key or url) in seen:
                rejected.append({"event_id": event_id, "source_reference": origin,
                                 "reason": "doublon sur rejeu"})
                continue
            seen.add((published, key or url))
            evidence = row.get("evidence", {}).get(url) if isinstance(row.get("evidence"), dict) else None
            proof, reason = validate(url, published, evidence, vault)
            if reason:
                rejected.append({"event_id": event_id, "source_reference": origin,
                                 "reason": reason})
                continue
            accepted.append({"event_id": event_id, "url": url, "publie": published,
                             "site_id": urlsplit(url).hostname.lower().removeprefix("www."),
                             "source_reference": origin, "evidence": proof})
    return {"verified": accepted, "rejected": rejected,
            "stats": {"verified": len(accepted), "rejected": len(rejected),
                      "duplicates": sum(r.get("reason") == "doublon sur rejeu" for r in rejected)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", help="URL publique à capturer immédiatement après publication")
    ap.add_argument("--registre", default=str(REGISTRE))
    ap.add_argument("--verified", default=str(VERIFIEES))
    ap.add_argument("--rejected", default=str(REFUSEES))
    args = ap.parse_args()
    if args.capture:
        print(json.dumps(capture_page(args.capture), ensure_ascii=False, indent=2))
        return
    result = project(args.registre)
    for path, data in ((args.verified, result["verified"]),
                       (args.rejected, {"events": result["rejected"], "stats": result["stats"]})):
        Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["stats"], ensure_ascii=False))


if __name__ == "__main__":
    main()
