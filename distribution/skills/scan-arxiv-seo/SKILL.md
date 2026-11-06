---
name: scan-arxiv-seo
description: "Scan arXiv des publications utiles au SEO et au GEO. « lance le scan arxiv », « nouvelles études SEO »."
---

# Scan arXiv SEO/GEO/AEO — `/scan-arxiv-seo`

## Quand utiliser ce skill

Scan hebdomadaire arXiv des publications académiques qui comptent réellement pour le SEO, le GEO (Generative Engine Optimization), l'AEO et le ranking dans les moteurs génératifs — un sous-doc du système brèves (agent-synthetic/revuedepressIA/breves-IA/scan-arxiv/), au même titre que factcheck/.

TOUJOURS utiliser ce skill quand Tim dit : "/scan-arxiv-seo", "lance le scan arxiv", "check les nouvelles études SEO sur arxiv", "des nouveautés arxiv sur le GEO", "scan de littérature SEO/GEO", "quoi de neuf sur arxiv niveau search", "études académiques SEO récentes", ou quand le cron hebdo `com.tim.scan-arxiv` se déclenche.

## Mission

Repérer, dans la littérature académique publiée sur arXiv, les papers qui changent réellement la pratique ou la doctrine SEO/GEO/AEO de Tim — pas une liste exhaustive de tout ce qui contient le mot "search". Sous-doc du système brèves : même famille que `breves-IA/factcheck/`, même logique (draft, jamais envoyé, git commité).

**arXiv n'est pas un gisement "SEO"** : quasi personne n'y publie sous ce terme. Le gisement pertinent est cs.IR/cs.CL — ranking, retrieval, moteurs génératifs, citation de marques par les LLM, manipulation du search augmenté par IA. Le scoring (Étape 2) fait le tri.

## Zéro hallucination (non négociable)

- **Jamais de paper, d'ID arXiv, d'auteur ou de chiffre sorti de mémoire.** Tout candidat vient du JSON produit par `arxiv-fetch.py` (Étape 1).
- Un ID arXiv cité doit être vérifiable sur `arxiv.org/abs/<id>`.
- Un chiffre cité doit être retrouvé dans l'abstract réel (ou le PDF si approfondi), jamais déduit de mémoire.
- En cas de doute sur un chiffre ou une conclusion : score `Fiabilité source` bas, ou pas de fiche.

## Non-complétion

Produire uniquement ce que les abstracts réels permettent d'écrire. Si aucun candidat ne passe le seuil de score, le rapport le dit explicitement et s'arrête là. Ne jamais forcer une fiche sous le seuil pour remplir.

---

## Étape 1 — Collecte déterministe (obligatoire, jamais remplacée par une recherche manuelle ou WebSearch)

```bash
# Collecter via les outils web disponibles ; le fetcher personnel de Tim est absent.
```

Le script interroge l'API officielle arXiv, déduplique contre tout ID déjà présent dans `raw/papers/`, `raw/etudes-seo/`, `wiki/sources/`, filtre par fraîcheur. `--days 8` par défaut pour une cadence hebdomadaire (couvre la semaine + marge). Si le dernier rapport `breves-IA/scan-arxiv/*.md` date de plus de 8 jours (cron sauté), élargir `--days` pour couvrir le trou.

Si `candidates_count` est 0, passer directement à la clôture (non-complétion).

## Étape 2 — Scoring déterministe (5 axes, /10 chacun, /50 total)

Pour **chaque candidat** du JSON, noter sur la base du titre + abstract réels :

| Axe | Question |
|---|---|
| **Nouveauté** /10 | Le finding ou la méthode apporte-t-il quelque chose que le vault ne sait pas déjà (grep `wiki/concepts/`, `wiki/sources/` avant de noter) ? Un paper qui répète un finding déjà ingéré perd des points, même s'il l'étend un peu. |
| **Impact SEO/GEO** /10 | Change-t-il la pratique ou la doctrine d'un consultant SEO/GEO senior ? |
| **Solidité méthodologique** /10 | Taille d'échantillon, contrôles, institution(s) identifiable(s), réplicabilité, venue (conférence/journal vs préprint seul). |
| **Actionnabilité** /10 | Conséquence concrète exploitable en conseil, prospection ou production de contenu — pas juste "intéressant à savoir". |
| **Fiabilité de la source** /10 | Auteurs et institution identifiables, préprint isolé vs accepté quelque part, cohérence interne de l'abstract. |

**Total /50. Seuil de rétention : 30/50.** Sous 30, le candidat est écarté (le dire en une ligne dans le rapport, pas de fiche développée). Au-dessus de 30, cap à **7 fiches par édition** — au-delà, garder les 7 mieux notées, les autres attendent l'édition suivante (ils resteront candidats : non ingérés au JSON = pas dédupliqués).

Afficher le score total sur chaque fiche retenue (`Score : 37/50`), pas le détail des 5 sous-notes (bruit inutile pour Tim) sauf demande explicite.

## Étape 3 — Approfondir les candidats retenus

Pour chaque candidat ≥ 30/50 : lire l'abstract en entier (déjà dans le JSON). Si un chiffre clé du rapport a besoin d'être vérifié au-delà de l'abstract, WebFetch sur `abs_url` (voire le PDF). Ne jamais résumer au-delà de ce que le texte dit.

## Étape 4 — Écrire le rapport hebdomadaire (sous-doc de brèves)

**Fichier** : `agent-synthetic/revuedepressIA/breves-IA/scan-arxiv/YYYY-MM-DD-scan-arxiv.md` (suffixer `-v2` si le fichier du jour existe déjà, même convention que `breves-IA/`).

```markdown
# Scan ArXiv SEO/GEO — {YYYY-MM-DD}

*Scan hebdomadaire de la littérature arXiv pertinente SEO/GEO/AEO. Collecte déterministe (API arXiv) + scoring /50. Aucun envoi, sous-doc de brèves.*

## Verdict de la semaine

2-4 phrases : tendance de fond, combien de candidats examinés / retenus, le fil qui relie les papers gardés si un fil existe.

## Études retenues

### {N}. {Titre vulgarisé qui porte l'angle} — `Score : XX/50`

**Source** : https://arxiv.org/abs/{id}
**Signal** : 🟢 Opportunité / 🟡 À surveiller / 🔴 Menace
**Impact business en 1 ligne** : ...

Résumé factuel (méthode, chiffres, findings) — 4 à 6 phrases.

**Lien avec la doctrine du vault** : connexion à un concept/entity existant si elle est réelle (citer `[[concepts/...]]` — ce fichier vit hors du wiki mais la référence reste utile pour un futur ingest), sinon l'omettre.

---

(jusqu'à 7 fiches, classées par score décroissant)

## Écartés

Une ligne par candidat sous le seuil ou hors périmètre : `- {id} — {titre court} (score XX/50 ou hors-scope)`. Pas de développement.

## Candidats à ingestion complète

Si un ou plusieurs papers retenus méritent le traitement complet du vault (fiche `raw/papers/` + synthèse `wiki/sources/` avec wikilinks concepts/entities, format du scan du 2026-04-15) : le signaler ici, ne jamais l'exécuter automatiquement dans ce skill. `raw/` et `wiki/` restent un ingest décidé par Tim (§6.1 AGENTS.md).

## Candidat INFO DU JOUR newsletter Algorithme

Oui/Non + lequel + angle possible, si un sujet est assez fort (même logique que `breves-quotidiennes`).
```

## Étape 5 — Clôture

Commit du dossier `breves-IA/scan-arxiv/` uniquement (jamais push automatique — règle absolue committer-pas-pousser). Rapport court à Tim : N candidats examinés, N retenus (scores), fichier écrit, candidats à ingestion complète le cas échéant.

Si 0 candidat ou tout sous le seuil : ne pas écrire de rapport vide inutile — un message court suffit ("Scan du {période} : N candidats examinés, aucun au-dessus de 30/50. Rien écrit.").

## Ingestion complète dans le vault (raw/papers/ + wiki/sources/) — séparée, sur demande

Ce skill ne le fait jamais seul en automatique. Quand Tim demande d'ingérer un paper du rapport hebdo dans le vault (doctrine complète avec wikilinks concepts/entities), suivre le format déjà établi par `raw/papers/scan-arxiv-2026-04-15.md` / `wiki/sources/2026-04-15-scan-arxiv-15-avril.md` (et `raw/papers/scan-arxiv-2026-09-25.md` / `wiki/sources/2026-09-25-scan-arxiv-25-septembre.md`) : frontmatter complet, sections par étude, `VERDICT`, `Apports à la KB`, `Limites`, `Pages liées`. Suivre le workflow §6.1 AGENTS.md (log + index.md).

## Cadence

Déclenchement manuel dans SEOKB2. Aucun cron fourni. Utiliser la recherche web disponible et consigner les URLs, dates, résumés et limites de collecte.

## Dédoublonnage

Garanti par `arxiv-fetch.py` (Étape 1) sur l'ID arXiv, contre `raw/papers/`, `raw/etudes-seo/`, `wiki/sources/`. Un paper déjà ingéré en doctrine complète ne revient jamais dans un rapport hebdo suivant.
