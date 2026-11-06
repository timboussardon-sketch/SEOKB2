#!/usr/bin/env python3
"""
Liste les meilleures vidéos YouTube sur Claude + SEO du moment.
API YouTube Data v3, stdlib seule (pas de pip install).

Critère de tri : pertinence + fraîcheur (fenêtre récente), avec un léger
appoint de popularité pour départager. Score transparent, documenté plus bas.

Usage :
  python3 yt_best.py [--months 6] [--top 15] [--region FR] ["requête sup" ...]

Clé API : lue depuis $YOUTUBE_API_KEY, sinon ~/.config/youtube-api.env
(ligne YOUTUBE_API_KEY=AIza...).
"""
import sys, os, json, math, argparse, time, ssl
from datetime import datetime, timezone, timedelta
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

API = "https://www.googleapis.com/youtube/v3"

# Requêtes par défaut : Claude x SEO, FR + EN. Couvre Claude Code, Anthropic,
# usages SEO/GEO. On ratisse large, on dédoublonne ensuite.
DEFAULT_QUERIES = [
    "Claude SEO",
    "Claude AI SEO",
    "Claude Code SEO",
    "SEO avec Claude",
    "Claude pour le SEO",
    "Claude Anthropic SEO",
    "Claude AI for SEO",
    "Claude Code SEO automation",
    "Claude SEO content",
    "Claude GEO AI search",
]


def load_api_key():
    key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if key:
        return key
    path = os.path.expanduser("~/.config/youtube-api.env")
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                if k.strip() == "YOUTUBE_API_KEY":
                    return v.strip().strip('"').strip("'")
    sys.exit(
        "ERREUR : clé API YouTube introuvable.\n"
        "Crée ~/.config/youtube-api.env avec la ligne :\n"
        "  YOUTUBE_API_KEY=AIza...ta_cle...\n"
        "ou exporte YOUTUBE_API_KEY dans ton shell."
    )


def api_get(endpoint, params, retries=4):
    params = dict(params)
    url = f"{API}/{endpoint}?{urlencode(params)}"
    last_err = None
    for attempt in range(retries):
        try:
            with urlopen(url, timeout=30) as r:
                return json.loads(r.read().decode())
        except HTTPError as e:
            body = e.read().decode(errors="replace")
            msg = body
            try:
                msg = json.loads(body)["error"]["message"]
            except Exception:
                pass
            # 403/400 = clé/quota : inutile de retenter
            sys.exit(f"ERREUR API YouTube (HTTP {e.code}) sur {endpoint} : {msg}")
        except (URLError, ssl.SSLError, OSError) as e:
            # EOF SSL et coupures réseau sont intermittents : on retente
            last_err = e
            if attempt < retries - 1:
                time.sleep(1.5 * (attempt + 1))
                continue
    reason = getattr(last_err, "reason", last_err)
    sys.exit(f"ERREUR réseau sur {endpoint} (après {retries} tentatives) : {reason}")


def search(query, key, published_after, region, max_results=15):
    data = api_get("search", {
        "key": key,
        "q": query,
        "part": "snippet",
        "type": "video",
        "order": "relevance",
        "maxResults": max_results,
        "publishedAfter": published_after,
        "regionCode": region,
        "relevanceLanguage": "fr",
    })
    out = []
    for rank, item in enumerate(data.get("items", [])):
        vid = item["id"].get("videoId")
        if vid:
            out.append((vid, rank))
    return out


def fetch_details(video_ids, key):
    details = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        data = api_get("videos", {
            "key": key,
            "id": ",".join(batch),
            "part": "snippet,statistics,contentDetails",
        })
        for it in data.get("items", []):
            details[it["id"]] = it
    return details


def parse_duration(iso):
    # PT#H#M#S -> secondes
    if not iso or not iso.startswith("PT"):
        return 0
    num, total = "", 0
    for ch in iso[2:]:
        if ch.isdigit():
            num += ch
        else:
            n = int(num) if num else 0
            total += n * {"H": 3600, "M": 60, "S": 1}.get(ch, 0)
            num = ""
    return total


def fmt_duration(sec):
    if sec <= 0:
        return "?"
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fmt_views(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=6)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--region", default="FR")
    ap.add_argument("extra", nargs="*", help="requêtes supplémentaires")
    args = ap.parse_args()

    key = load_api_key()
    now = datetime.now(timezone.utc)
    window_days = max(1, args.months * 30)
    published_after = (now - timedelta(days=window_days)).strftime("%Y-%m-%dT%H:%M:%SZ")

    queries = DEFAULT_QUERIES + list(args.extra)

    # best_rank[vid] = meilleure position de pertinence vue sur l'ensemble des requêtes
    best_rank = {}
    hits = {}
    for q in queries:
        for vid, rank in search(q, key, published_after, args.region):
            hits[vid] = hits.get(vid, 0) + 1
            if vid not in best_rank or rank < best_rank[vid]:
                best_rank[vid] = rank

    if not best_rank:
        print("Aucune vidéo trouvée sur la fenêtre demandée. Élargis --months.")
        return

    details = fetch_details(list(best_rank), key)

    rows = []
    for vid, rank in best_rank.items():
        it = details.get(vid)
        if not it:
            continue
        sn = it["snippet"]
        st = it.get("statistics", {})
        views = int(st.get("viewCount", 0))
        published = sn.get("publishedAt", "")
        try:
            pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
            days_old = (now - pub_dt).days
        except Exception:
            days_old = window_days

        # --- Score transparent : pertinence + fraîcheur + appoint popularité ---
        relevance = 1.0 / (1 + rank)                      # rang 0 = 1.0, décroît
        relevance += 0.10 * (hits[vid] - 1)               # bonus si plusieurs requêtes la remontent
        recency = max(0.0, 1.0 - days_old / window_days)  # 1.0 = aujourd'hui, 0 = bord de fenêtre
        popularity = math.log10(views + 1) / 7.0          # ~1.0 vers 10M vues
        score = 0.45 * relevance + 0.40 * recency + 0.15 * popularity

        rows.append({
            "score": score,
            "title": sn.get("title", "").replace("|", "/"),
            "channel": sn.get("channelTitle", ""),
            "date": published[:10],
            "days_old": days_old,
            "views": views,
            "duration": fmt_duration(parse_duration(it.get("contentDetails", {}).get("duration", ""))),
            "url": f"https://www.youtube.com/watch?v={vid}",
            "description": (sn.get("description", "") or "")[:500],
            "tags": sn.get("tags", [])[:15],
        })

    rows.sort(key=lambda r: r["score"], reverse=True)
    rows = rows[:args.top]

    # Sortie markdown, prête à coller dans le chat
    theme = "Claude x SEO" if not args.extra else "veille search/IA (élargie)"
    print(f"# Meilleures vidéos YouTube — {theme}")
    print(f"_Fenêtre : {args.months} derniers mois · {len(best_rank)} candidates · "
          f"top {len(rows)} · tri pertinence + fraîcheur_\n")
    print("| # | Vidéo | Chaîne | Date | Vues | Durée | Lien |")
    print("|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        title = r["title"][:70]
        print(f"| {i} | {title} | {r['channel']} | {r['date']} | "
              f"{fmt_views(r['views'])} | {r['duration']} | {r['url']} |")

    # JSON brut en fin pour réusage éventuel par le skill
    print("\n<!-- JSON")
    print(json.dumps(rows, ensure_ascii=False))
    print("-->")


if __name__ == "__main__":
    main()
