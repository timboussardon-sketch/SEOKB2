#!/usr/bin/env python3
"""Read-only Search Console audit for a manually triggered GitHub Actions run."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
from urllib.parse import quote, urlparse

SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
ROW_LIMIT = 25_000


def period(end: dt.date, days: int) -> tuple[str, str]:
    return ((end - dt.timedelta(days=days - 1)).isoformat(), end.isoformat())


def fetch(session: object, site: str, start: str, end: str,
          dimensions: list[str] | None = None) -> list[dict]:
    url = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        f"{quote(site, safe='')}/searchAnalytics/query"
    )
    body = {"startDate": start, "endDate": end, "type": "web"}
    if dimensions:
        body["dimensions"] = dimensions
        body["rowLimit"] = ROW_LIMIT
    rows: list[dict] = []
    while True:
        if dimensions:
            body["startRow"] = len(rows)
        response = session.post(url, json=body, timeout=90)
        if getattr(response, "status_code", 200) == 403:
            raise PermissionError(
                f"GSC refuse la lecture de {site} (403). Ajouter le compte de service "
                "comme utilisateur restreint de cette propriété Search Console."
            )
        response.raise_for_status()
        batch = response.json().get("rows", [])
        rows.extend(batch)
        if not dimensions or len(batch) < ROW_LIMIT:
            return rows
        if len(rows) >= 50_000:
            raise RuntimeError("Plus de 50 000 lignes GSC : audit incomplet, arrêt sans rapport.")


def clicks(row: dict) -> int:
    return int(row.get("clicks", 0))


def impressions(row: dict) -> int:
    return int(row.get("impressions", 0))


def page_map(rows: list[dict]) -> dict[str, dict]:
    return {row["keys"][0]: row for row in rows if row.get("keys")}


def table(rows: list[tuple[str, dict, dict]], limit: int = 5) -> list[str]:
    lines = ["| Page | Clics période | Clics avant | Écart | Impressions période | Position moyenne |",
             "|---|---:|---:|---:|---:|---:|"]
    for url, now, before in rows[:limit]:
        safe_url = url.replace("|", "%7C")
        now_clicks = str(clicks(now)) if now else "—"
        before_clicks = str(clicks(before)) if before else "—"
        delta = f"{clicks(now) - clicks(before):+d}" if now and before else "—"
        pos = f"{float(now.get('position', 0)):.1f}" if impressions(now) else "—"
        lines.append(
            f"| {safe_url} | {now_clicks} | {before_clicks} | {delta} | "
            f"{impressions(now) if now else '—'} | {pos} |"
        )
    if not rows:
        lines.append("| Aucune ligne répondant au filtre | — | — | — | — | — |")
    return lines


def report(site: str, start: str, end: str, prior_start: str, prior_end: str,
           current_total: dict, prior_total: dict,
           current_pages: list[dict], prior_pages: list[dict]) -> str:
    current = page_map(current_pages)
    prior = page_map(prior_pages)
    all_pages = set(current) | set(prior)
    pairs = [(url, current.get(url, {}), prior.get(url, {})) for url in all_pages]
    declines = sorted(
        (p for p in pairs if p[1] and p[2] and clicks(p[2]) >= 5
         and clicks(p[1]) < clicks(p[2])),
        key=lambda p: (clicks(p[1]) - clicks(p[2]), p[0]),
    )
    candidates = sorted(
        (p for p in pairs if impressions(p[1]) >= 100
         and 3 <= float(p[1].get("position", 0)) <= 12),
        key=lambda p: (-impressions(p[1]), p[0]),
    )
    fetched = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Audit GSC ponctuel", "",
        f"Source : API Google Search Console, propriété `{site}`, type `web`, extraction {fetched}.",
        f"Période observée : {start} au {end}. Comparaison : {prior_start} au {prior_end}.",
        "Les clics et impressions du site viennent d'une requête sans dimension. "
        "Les tableaux de pages proviennent de requêtes avec dimension `page`.", "",
        "## Mesure du site", "",
        "| Mesure | Période | Avant | Écart |", "|---|---:|---:|---:|",
        f"| Clics | {clicks(current_total)} | {clicks(prior_total)} | "
        f"{clicks(current_total) - clicks(prior_total):+d} |",
        f"| Impressions | {impressions(current_total)} | {impressions(prior_total)} | "
        f"{impressions(current_total) - impressions(prior_total):+d} |", "",
        "## Pages en recul à examiner", "",
        "Filtre de tri : au moins 5 clics sur la période précédente et moins de clics "
        "sur la période récente. Ce tableau ne démontre aucune cause.", "",
        *table(declines), "",
        "## Pages avec impressions et position 3–12", "",
        "Filtre de tri : au moins 100 impressions et position moyenne entre 3 et 12 "
        "sur la période récente. Ce sont des candidates à examiner, sans décision automatique.", "",
        *table(candidates), "",
        "## Limites", "",
        f"{len(current_pages)} lignes page reçues pour la période récente et "
        f"{len(prior_pages)} pour la précédente. Les lignes GSC peuvent être limitées "
        "ou anonymisées ; leur somme ne remplace pas le total du site. "
        "Les périodes n'ajustent pas la saisonnalité et cet audit ne mesure ni conversions "
        "ni causes de variation. Aucun changement de page n'est exécuté.", "",
    ]
    return "\n".join(lines)


def main() -> None:
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import service_account

    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="sc-domain:organikk.co")
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--end-date", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if not 7 <= args.days <= 90:
        parser.error("--days doit être compris entre 7 et 90")
    valid_domain = re.fullmatch(r"sc-domain:[A-Za-z0-9.-]+", args.site)
    parsed_site = urlparse(args.site)
    valid_prefix = (
        parsed_site.scheme == "https" and bool(parsed_site.netloc)
        and not any(char.isspace() for char in args.site)
    )
    if not (valid_domain or valid_prefix):
        parser.error("--site doit être une propriété GSC sc-domain: ou https:// valide")
    end_date = (dt.date.fromisoformat(args.end_date) if args.end_date
                else dt.date.today() - dt.timedelta(days=3))
    if end_date > dt.date.today() - dt.timedelta(days=2):
        parser.error("--end-date doit laisser au moins 2 jours de délai GSC")
    start, end = period(end_date, args.days)
    prior_start, prior_end = period(
        dt.date.fromisoformat(start) - dt.timedelta(days=1), args.days
    )
    credential_json = os.environ.get("GSC_SERVICE_ACCOUNT_JSON")
    credential_file = os.environ.get("GSC_SERVICE_ACCOUNT_FILE")
    if credential_json:
        credentials = service_account.Credentials.from_service_account_info(
            json.loads(credential_json), scopes=[SCOPE]
        )
    elif credential_file and Path(credential_file).is_file():
        credentials = service_account.Credentials.from_service_account_file(
            credential_file, scopes=[SCOPE]
        )
    else:
        parser.error("GSC_SERVICE_ACCOUNT_JSON ou GSC_SERVICE_ACCOUNT_FILE absent")
    session = AuthorizedSession(credentials)
    current_total = fetch(session, args.site, start, end)
    prior_total = fetch(session, args.site, prior_start, prior_end)
    if not current_total or not prior_total:
        raise RuntimeError(
            "Aucun total GSC sur l'une des périodes : vérifier la propriété et les dates. "
            "Aucun zéro n'est inféré d'une réponse vide."
        )
    current_pages = fetch(session, args.site, start, end, ["page"])
    prior_pages = fetch(session, args.site, prior_start, prior_end, ["page"])
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report(
        args.site, start, end, prior_start, prior_end,
        current_total[0] if current_total else {},
        prior_total[0] if prior_total else {}, current_pages, prior_pages,
    ), encoding="utf-8")
    print(f"Rapport écrit : {output}")


if __name__ == "__main__":
    main()
