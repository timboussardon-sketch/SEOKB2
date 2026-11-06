#!/usr/bin/env python3
"""
Extracteur d'apprentissage — lit les transcripts Claude Code et sort les couples
LIVRAISON -> VERDICT de Tim.

Aucun LLM ici : 100 % déterministe, rejouable, versionnable.
La lecture est strictement en lecture seule sur ~/.claude/projects/.

Sortie : JSON sur stdout (ou --out fichier).
  {
    "fenetre": {...},
    "evenements": [ {ts, projet, session, verdict, message, artefacts[], commits[]}, ... ],
    "publications": [ {ts, projet, session, urls[], commande}, ... ],
    "stats": {...}
  }

Usage :
  apprentissage-extract.py                    # dernières 24 h
  apprentissage-extract.py --since 2026-09-01 --until 2026-09-11
  apprentissage-extract.py --all              # tout l'historique (passe rétroactive)
"""
import argparse, glob, json, os, re, sys
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

PROJECTS = os.path.expanduser("~/.claude/projects")
DOMAINES = os.path.expanduser("~/Code/seo-kb/wiki/apprentissage/domaines.txt")

# Extensions qui ne sont pas des pages : on ne suit pas leur performance.
RE_NON_PAGE = re.compile(r"(/(?:api|auth|oauth|callback)/|/_next/|\.(xml|json|pdf|png|jpe?g|svg|webp|ico|txt|csv|zip|mp4|css|js)($|\?))", re.I)


def domaines_mesurables():
    """Domaines dont on possède la donnée GSC. Hors de cette liste, une URL captée
    est une référence externe citée par l'agent, pas une publication de Tim."""
    try:
        with open(DOMAINES) as fh:
            return {l.strip() for l in fh if l.strip()}
    except OSError:
        return set()

# --- classification du verdict de Tim -------------------------------------
# L'ordre compte : on teste rejet, puis casse, puis validation, puis correction.
RE_REJET = re.compile(
    r"(^|[\s\.,!?'\"])(non|nan)\b"
    r"|\bpas (ça|ca|bon|du tout|comme ça|comme ca|ce que)\b"
    r"|\b(ça|ca) (va pas|ne va pas|marche pas|craint|le fait pas)\b"
    r"|\bc'?est (nul|moche|pas (bon|ça|ca)|faux|hors sujet)\b"
    r"|\b(refais|recommence|reprends tout|annule|retire|enlève|enleve|supprime)\b"
    r"|\bje t'?ai (dit|déjà dit|deja dit)\b"
    r"|\bjamais\b"
    r"|\bmauvais\b",
    re.I)
RE_CASSE = re.compile(
    r"\b(cass[ée]|casse tout|marche plus|ne marche pas|fonctionne pas|plante|erreur|bug|404|500|blanche?)\b",
    re.I)
RE_VALIDATION = re.compile(
    r"\b(parfait|nickel|excellent|génial|genial|impec|impeccable|ça marche|ca marche|"
    r"c'?est bon|c'?est (ça|ca)|valid[ée]|j'?aime|bien jou[ée]|banco)\b"
    r"|^\s*(go|ok go|top|super)\b"
    r"|\b(c'?est|trop) (top|super)\b",
    re.I)
RE_CORRECTION = re.compile(
    r"\b(change|modifie|remplace|mets|met |ajoute|déplace|deplace|plutôt|plutot|"
    r"il faut|tu dois|corrige|revois|refait|augmente|réduis|reduis)\b",
    re.I)

# --- bruit à ignorer dans les messages de Tim ------------------------------
RE_BRUIT = re.compile(r"^\s*(<|\[Request interrupted|/clear|/compact|continue$|ok$|oui$|merci)", re.I)

# --- publications ----------------------------------------------------------
RE_DEPLOY = re.compile(
    r"\b(netlify deploy|vercel (deploy|--prod)|npm run deploy|npm run publish|"
    r"wrangler (deploy|pages)|supabase functions deploy|gh-pages|firebase deploy)\b", re.I)
RE_URL = re.compile(r"https?://[^\s\)\"'<>\]]+", re.I)
RE_COMMIT = re.compile(r"git\s+commit[^\n]*?-m\s+[\"']([^\"']{4,200})", re.I)

IGNORE_URL = re.compile(r"(localhost|127\.0\.0\.1|github\.com|anthropic\.com|claude\.ai|"
                        r"google\.com|docs\.|npmjs\.com|stackoverflow|app\.netlify\.com|"
                        r"supabase\.com|\.netlify\.app/?$)", re.I)


def nettoie_url(u: str) -> str:
    """Retire la ponctuation et le balisage markdown collés à l'URL."""
    return u.rstrip(".,;:)>\"'`*_ ")


RE_BLOC_COLLE = re.compile(r"\n\s*(#{1,6}\s|```|\|\s|>\s)")


def tete(msg: str) -> str:
    """Le verdict de Tim est dans sa première phrase, pas dans le contenu qu'il colle
    derrière. On coupe au premier bloc collé (titre markdown, code, tableau, citation)
    et on plafonne à 300 caractères."""
    m = RE_BLOC_COLLE.search(msg)
    t = msg[: m.start()] if m else msg
    return t[:300]


def est_deploiement(cmd: str) -> bool:
    """Vraie commande de mise en ligne, pas une inspection qui la mentionne."""
    if "<<" in cmd or len(cmd) > 400:          # heredoc / script : on ne sait pas ce qui tourne
        return False
    for seg in re.split(r"&&|\|\||;|\n", cmd):
        seg = seg.strip()
        if not seg or re.match(r"^(grep|cat|which|echo|ls|head|tail|rg|sed|awk|#)\b", seg):
            continue
        if RE_DEPLOY.search(seg):
            return True
    return False


def classer(msg: str) -> str:
    """Retourne le verdict porté par un message de Tim."""
    t = tete(msg)
    if RE_CASSE.search(t):
        return "casse"
    if RE_REJET.search(t):
        return "rejet"
    # une validation s'annonce d'entrée de jeu ; au-delà, c'est une nouvelle consigne
    if RE_VALIDATION.search(t[:80]):
        return "validation"
    if RE_CORRECTION.search(t):
        return "correction"
    return "neutre"


def texte_user(d):
    """Extrait le texte réel d'un message user, ou None si ce n'est pas un vrai tour de Tim."""
    if d.get("type") != "user" or d.get("isMeta"):
        return None
    c = d.get("message", {}).get("content")
    if isinstance(c, str):
        txt = c
    elif isinstance(c, list):
        parts = []
        for b in c:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_result":   # retour d'outil, pas Tim
                return None
            if b.get("type") == "text":
                parts.append(b.get("text", ""))
        txt = "\n".join(parts)
    else:
        return None
    txt = txt.strip()
    if not txt or RE_BRUIT.match(txt):
        return None
    return txt


def parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def scan_fichier(path, projet, debut, fin, domaines):
    """Parcourt un transcript et rend (evenements, publications)."""
    evenements, publications = [], []
    en_attente = {"fichiers": [], "commits": [], "ts": None}
    session = os.path.basename(path)[:-6]

    try:
        fh = open(path, errors="ignore")
    except OSError:
        return evenements, publications

    with fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue

            ts = parse_ts(d.get("timestamp"))
            typ = d.get("type")

            # --- ce que l'agent a produit ---
            if typ == "assistant":
                for b in d.get("message", {}).get("content", []) or []:
                    if not isinstance(b, dict) or b.get("type") != "tool_use":
                        continue
                    nom, inp = b.get("name"), b.get("input") or {}
                    if nom in ("Write", "Edit", "NotebookEdit"):
                        fp = inp.get("file_path") or inp.get("notebook_path")
                        if fp and fp not in en_attente["fichiers"]:
                            en_attente["fichiers"].append(fp)
                            en_attente["ts"] = en_attente["ts"] or ts
                    elif nom == "Bash":
                        cmd = inp.get("command", "") or ""
                        m = RE_COMMIT.search(cmd)
                        if m:
                            en_attente["commits"].append(m.group(1)[:160])
                            en_attente["ts"] = en_attente["ts"] or ts
                        if (est_deploiement(cmd)) and debut <= (ts or debut) <= fin:
                            publications.append({
                                "ts": d.get("timestamp"), "projet": projet, "session": session,
                                "commande": cmd.strip()[:200], "urls": [],
                            })
                    # URLs annoncées par l'agent (page mise en ligne)
                # texte de l'assistant : on y pêche les URLs publiques
                for b in d.get("message", {}).get("content", []) or []:
                    if isinstance(b, dict) and b.get("type") == "text" and publications:
                        for u in RE_URL.findall(b.get("text", ""))[:5]:
                            u = nettoie_url(u)
                            if not u or IGNORE_URL.search(u) or RE_NON_PAGE.search(u):
                                continue
                            host = urlparse(u).netloc.replace("www.", "")
                            if domaines and host not in domaines:
                                continue
                            if u not in publications[-1]["urls"]:
                                publications[-1]["urls"].append(u)

            # --- le verdict de Tim ---
            else:
                msg = texte_user(d)
                if msg is None:
                    continue
                if en_attente["fichiers"] or en_attente["commits"]:
                    if ts and debut <= ts <= fin:
                        verdict = classer(msg)
                        evenements.append({
                            "ts": d.get("timestamp"),
                            "projet": projet,
                            "session": session,
                            "verdict": verdict,
                            "message": msg[:900],
                            "long": len(msg) > 900,
                            "artefacts": en_attente["fichiers"][:12],
                            "artefacts_total": len(en_attente["fichiers"]),
                            "commits": en_attente["commits"][:6],
                        })
                en_attente = {"fichiers": [], "commits": [], "ts": None}

    return evenements, publications


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", help="AAAA-MM-JJ inclus")
    ap.add_argument("--until", help="AAAA-MM-JJ inclus")
    ap.add_argument("--all", action="store_true", help="tout l'historique")
    ap.add_argument("--out", help="fichier de sortie (défaut: stdout)")
    ap.add_argument("--verdicts", default="rejet,casse,correction,validation",
                    help="verdicts à conserver (défaut: tout sauf neutre)")
    a = ap.parse_args()

    maintenant = datetime.now(timezone.utc)
    if a.all:
        debut, fin = datetime(2000, 1, 1, tzinfo=timezone.utc), maintenant
    elif a.since:
        debut = datetime.fromisoformat(a.since).replace(tzinfo=timezone.utc)
        fin = (datetime.fromisoformat(a.until).replace(tzinfo=timezone.utc) + timedelta(days=1)
               if a.until else maintenant)
    else:
        debut, fin = maintenant - timedelta(hours=24), maintenant

    gardes = {v.strip() for v in a.verdicts.split(",") if v.strip()}

    domaines = domaines_mesurables()
    evenements, publications = [], []
    fichiers = sorted(glob.glob(os.path.join(PROJECTS, "*", "*.jsonl")))
    lus = 0
    for path in fichiers:
        # filtre grossier par mtime pour ne pas ouvrir 2,5 Go inutilement
        if not a.all:
            try:
                mt = datetime.fromtimestamp(os.path.getmtime(path), timezone.utc)
            except OSError:
                continue
            if mt < debut - timedelta(days=1):
                continue
        projet = os.path.basename(os.path.dirname(path))
        e, p = scan_fichier(path, projet, debut, fin, domaines)
        evenements += e
        publications += p
        lus += 1

    evenements = [e for e in evenements if e["verdict"] in gardes]
    evenements.sort(key=lambda e: e["ts"] or "")
    publications.sort(key=lambda p: p["ts"] or "")

    stats = {"transcripts_lus": lus, "transcripts_total": len(fichiers),
             "evenements": len(evenements), "publications": len(publications)}
    for v in ("rejet", "casse", "correction", "validation", "neutre"):
        n = sum(1 for e in evenements if e["verdict"] == v)
        if n:
            stats[v] = n

    sortie = {
        "fenetre": {"debut": debut.isoformat(), "fin": fin.isoformat()},
        "genere_le": maintenant.isoformat(),
        "stats": stats,
        "evenements": evenements,
        "publications": publications,
    }
    txt = json.dumps(sortie, ensure_ascii=False, indent=2)
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "w") as f:
            f.write(txt)
        print(json.dumps(stats, ensure_ascii=False), file=sys.stderr)
    else:
        print(txt)


if __name__ == "__main__":
    main()
