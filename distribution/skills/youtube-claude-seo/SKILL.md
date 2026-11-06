---
name: youtube-claude-seo
description: "Meilleures vidéos YouTube récentes sur Claude et le SEO, avec leurs angles. « meilleures vidéos Claude SEO »."
---

# Skill : Veille vidéos YouTube — Claude x SEO

## Quand utiliser ce skill

Liste les meilleures vidéos YouTube du moment sur Claude appliqué au SEO (Claude, Claude Code, Anthropic x référencement / GEO / content). Tape l'API YouTube Data v3 via un script Python stdlib (pas de pip install), filtre sur une fenêtre récente (6 mois par défaut), dédoublonne, classe par pertinence + fraîcheur avec un léger appoint de popularité, et sort un tableau prêt à scanner dans le chat : titre, chaîne, date, vues, durée, lien. Puis extrait les ANGLES/hooks qui reviennent (à partir des titres + descriptions) : clusters d'angles nommés, patterns de titre réutilisables, et ce qui ne marche pas.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "meilleures vidéos Claude SEO", "vidéos YouTube Claude SEO", "/youtube-claude-seo", "qu'est-ce qui sort sur YouTube sur Claude et le SEO", "trouve-moi des vidéos sur Claude pour le SEO", "veille YouTube Claude SEO", "top vidéos Claude SEO du moment", "quels titres / angles marchent sur YouTube sur Claude SEO".

## Quand déclencher

- Tim demande les meilleures vidéos YouTube sur Claude appliqué au SEO (ou variantes).
- Veille ponctuelle ou récurrente (branchable via `/schedule`).
- Tim veut élargir un thème précis (ex : Claude Code + pSEO) en passant une requête supplémentaire.

## Pré-requis : clé API

Clé API YouTube Data v3 (Google Cloud Console, projet de Tim). Le script la lit dans cet ordre :

1. variable d'env `YOUTUBE_API_KEY` ;
2. sinon `~/.config/youtube-api.env`, ligne `YOUTUBE_API_KEY=AIza...`.

Si la clé manque, le script s'arrête avec le mode d'emploi exact. Le fichier `~/.config/youtube-api.env` n'est jamais commité (hors du repo). Pour le créer une fois :

```bash
echo 'YOUTUBE_API_KEY=AIza...colle_ta_cle...' > ~/.config/youtube-api.env
chmod 600 ~/.config/youtube-api.env
```

Quota : l'API offre 10 000 unités/jour. Un run = ~10 appels `search` (100 unités chacun) + 1-2 appels `videos` (1 unité) ≈ 1 000 unités. Une dizaine de runs/jour sans souci.

## Comment lancer

```bash
python3 .claude/skills/youtube-claude-seo/yt_best.py
```

Options :

```bash
# Fenêtre 3 mois, top 10
python3 .claude/skills/youtube-claude-seo/yt_best.py --months 3 --top 10

# Cibler une zone et ajouter des requêtes sur mesure
python3 .claude/skills/youtube-claude-seo/yt_best.py --region US "Claude Code pSEO" "Anthropic SEO workflow"
```

| Option | Défaut | Effet |
|---|---|---|
| `--months` | 6 | Fenêtre de fraîcheur (`publishedAfter`) |
| `--top` | 15 | Nombre de vidéos retournées |
| `--region` | FR | `regionCode` YouTube |
| `extra` (positionnels) | — | Requêtes ajoutées aux requêtes par défaut |

## Ce que fait le script

```
1. Charge la clé API (env ou ~/.config/youtube-api.env)
        ↓
2. search.list sur ~10 requêtes Claude x SEO (FR + EN), fenêtre récente, order=relevance
        ↓
3. Dédoublonne par videoId, garde la meilleure position de pertinence + le nb de requêtes qui la remontent
        ↓
4. videos.list (batch 50) pour vues, durée, date exacte
        ↓
5. Score = 0.45 pertinence + 0.40 fraîcheur + 0.15 popularité, tri décroissant
        ↓
6. Tableau markdown dans le chat (+ JSON brut en commentaire, avec description + tags, pour l'extraction d'angles)
```

Réseau : `api_get` retente 4 fois (backoff) sur EOF SSL / coupures réseau intermittentes avant d'abandonner. Sur une erreur HTTP (clé invalide, quota), il s'arrête net sans retenter.

### Le score (transparent, pas une boîte noire)

- **Pertinence** : `1/(1+rang)` sur la meilleure position renvoyée par YouTube, + 0,10 par requête supplémentaire qui remonte la vidéo.
- **Fraîcheur** : `1 - âge/fenêtre` (une vidéo d'aujourd'hui = 1,0 ; au bord de la fenêtre = 0).
- **Popularité** : `log10(vues)/7`, plafonne vers 10M vues. Léger appoint, jamais le critère dominant (sinon on remonte toujours les mêmes grosses chaînes).

Pour changer la pondération ou les requêtes par défaut, éditer le haut de `yt_best.py` (`DEFAULT_QUERIES`) et la section score.

## Restitution attendue

Deux livrables, dans cet ordre :

### 1. Le tableau (titres + perfs)

Présenter le tableau markdown tel quel dans le chat. Ajouter une ligne de tête sur les plus gros signaux de perf (vues hautes indépendamment de la fraîcheur, format/durée qui sort du lot).

### 2. Les angles extraits (OBLIGATOIRE)

Le script sort `description` (500 car.) et `tags` dans le JSON de fin : c'est la matière première. Lire le JSON, pas seulement le tableau, puis **clusteriser les angles/hooks qui reviennent** sur l'ensemble des vidéos. Pour chaque angle :
- le **nommer** (ex : « promesse de résultat chiffré + Steal This », « contrarian / pattern interrupt », « pour ta stack précise CMS nommé », « bascule SEO→GEO », « build a skill », « autorité / appel aux pros ») ;
- donner **2-3 titres réels** du run qui l'illustrent (citation exacte, jamais paraphrasé) ;
- expliciter le **pattern de titre** réutilisable (la structure, pas juste l'exemple) ;
- si pertinent, signaler le **hook récurrent dans les descriptions** (formule qui revient mot pour mot).

Finir par **ce qui NE marche pas** : repérer dans le bas du classement / les faibles vues les titres tièdes purement descriptifs (pas de chiffre, pas de tension, pas de stack nommée) et le dire en une ligne.

Les angles ne sont pas une liste figée : ils émergent du run. Ceux ci-dessus sont les clusters observés au 2026-06, à confirmer ou faire évoluer selon ce que remonte l'API.

### Garde-fous

- Ne pas inventer de chiffres : tout vient de l'API. Si une vidéo a 0 vue affichée, c'est l'API qui le dit (vidéo très récente ou stats masquées).
- Citer les titres **exactement** comme l'API les renvoie (ce sont des données, pas du copy à reformuler).
- Terminer par 1-2 vidéos à regarder en priorité selon le sujet du moment de Tim.

## Limites assumées

- L'API classe sur du texte (titre, description, tags), pas sur le contenu réel de la vidéo. Une vidéo bien titrée mais creuse peut remonter. Le tri fait le gros du tri, l'œil de Tim tranche.
- `relevanceLanguage=fr` + `regionCode` orientent sans garantir : des vidéos EN remontent, c'est voulu (le meilleur contenu Claude x SEO est souvent anglophone).
- Pas de transcription ni de résumé de vidéo ici. Si besoin d'un résumé, enchaîner avec un fetch manuel de la page/transcript.
