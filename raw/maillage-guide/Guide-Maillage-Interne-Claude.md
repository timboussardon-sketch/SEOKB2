---
type: source
source_type: note
title: "Guide : Le maillage interne avec Claude"
aliases: [guide maillage, maillage-interne-claude]
tags: [guide, maillage-interne, claude, skills, lead-magnet, organikk]
created: 2026-08-13
updated: 2026-08-13
sources: 0
confidence: high
status: published
---

# Guide « Le maillage interne avec Claude »

Guide Organikk publié le 2026-08-13, format identique aux autres guides (Geist, papier crème, A4).

Fichiers dans ce dossier : `maillage-interne-claude.html` (copie) et `maillage-interne-claude.pdf`.
**Source canonique : `~/Code/organikk-next/public/guides/maillage-interne-claude.html`.** Toute modification se fait là-bas, puis on recopie ici. Carte publique : organikk.co/guides (teinte lilac, 5e guide).

Post X de lancement (draft, non publié) : `raw/articles/posts-linkedin/post-x-guide-maillage-interne-claude.md`.

## Structure du guide (11 chapitres + FAQ)

1. Le maillage interne est un système. Les 3 signaux d'un lien (topique, intention, autorité), l'ancre comme promesse, la dilution du PageRank en 1/N, Know→Do avant Know→Know, pas de « Voir aussi ».
2. Les deux skills à installer. `maillage-systeme` (sans GSC) et `maillage-interne-gsc` (avec data), quand déclencher lequel, installation.
3. Le workflow de A à Z. 8 étapes, chacune avec livrable + critère de passage. Une demi-journée pour un site de 50-100 pages. Box « où ça bloque en vrai » : à l'étape 6 (validation lien par lien).
4. Préparer la donnée. La règle du contexte léger (index + graphe, jamais 50 pages dans le chat), 3 situations : crawl sitemap / exports GSC / liste planifiée. Exclusion des liens de gabarit (≥ 80 % des pages).
5. L'architecture en piliers. Classification Know-Simple / Know / Do, 3 à 5 piliers (≥ 3 articles + mot-clé business central + hub naturel), hub = article le plus stratégique, jamais une catégorie. Hiérarchie mère/fille/petite-fille côté GSC.
6. L'audit du graphe. Orphelines (0 entrant), dead-ends (0 sortant), hubs sous-maillés (< 5 entrants), pages Do sous-maillées en tête de gravité. La profondeur de clic n'est pas un critère.
7. Les ancres. Exact (1 max par cible) / partial (60-70 %) / sémantique. Les 5 critères, le test à voix haute, densité 2-5 liens / 1000 mots, FAQ = source d'ancres.
8. Prioriser et dérouler. Ordre : hub→satellites, Know→Do, cross-pillar, orphelines. Score sans GSC (poids d'intention) et avec GSC (impressions × 0.4 + potentiel position × 0.4 + business × 0.2). Format complet par lien : passage rédigé + 3 ancres + justification.
9. Gouvernance et cas particuliers. Checklist à chaque publication (3 entrants, 3 sortants, 1 Do, 1 cross-pillar). Site neuf, refonte, pSEO 300-500+ pages (signal de données, ex. cooccurrence sur 13 622 pages lexique, jamais d'agent page par page).
10. Les 7 règles non négociables.
11. Les deux SKILL.md complets, prêts à copier (versions nettoyées des boucles internes et chemins vault).

+ FAQ (densité, position des liens, gros sites, plugins de maillage auto, délais d'effet) + Aller plus loin (CTA Qadence + accompagnement 1:1).

## Warning d'ouverture (ajout demandé par Tim le 2026-08-13)

Encart « ⚠ À lire avant de commencer » dans l'introduction : sans système SEO (vault Obsidian / dossier de contexte, cf. guide De 0 à 1), la méthode perd beaucoup en efficacité et produit des erreurs (hubs génériques, ancres plausibles non alignées stratégie, mauvais pilier, liens vers des pages inexistantes). Minimum viable avant l'étape 1 : offre + 3-5 mots-clés piliers + liste des pages Do.
Illustré par un schéma SVG type graphe Obsidian : « Claude sans contexte » (pages isolées, lien pointillé rouge vers une page « ? ») vs « Claude + ton système » (nœud vault orange relié à doctrine, mots-clés, pages Do, data GSC, articles, secteur).

## Règles de production appliquées (réutilisables sur les prochains guides)

- Format = celui de `de-0-a-1-seo-claude.html` : CSS reprise à l'identique, cover, sommaire, ch-kicker/ch-title/ch-lead, boxes sombres (tim / rule / cta), diagrammes ASCII à la place de fausses captures, print A4.
- PDF généré par Chrome headless (`--headless --no-pdf-header-footer --print-to-pdf`) depuis le HTML.
- Nouvelle teinte de couverture ajoutée dans `src/app/guides/page.tsx` : `lilac` (les 4 existantes étaient prises).
- Les SKILL.md publiés sont nettoyés : pas de phase apprentissage/boucle, pas de chemins internes du vault.
- Chiffres méthode uniquement (pas de stats externes à sourcer) : 1 exact match, 60-70 % partial, 2-5 liens/1000 mots, hub ≥ 5, mère active = 10, seuil pSEO 300-500.
