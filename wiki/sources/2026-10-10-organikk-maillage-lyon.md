---
type: source
source_type: test-terrain
title: "Organikk : crawl du maillage après publication de Consultant SEO Lyon"
created: 2026-10-10
updated: 2026-10-10
tags: [organikk, maillage, seo, lyon]
sources: 3
confidence: high
status: stable
---

# Organikk : maillage de la nouvelle page Lyon

## Collecte

FACT : Le script officiel `/Users/timothee/.claude/skills/maillage-systeme/scripts/crawl_graph.py` a parcouru les 32 URL du sitemap public le 10 octobre 2026. Il a extrait 742 occurrences de liens internes, dont 60 retenues comme éditoriales, sans erreur de récupération. Ce périmètre ne représente pas toutes les pages accessibles du site.

Fichiers conservés : `wiki/maillage/data/2026-10-10-organikk/index.json`, `graph.json`, `targets.json`, `classification.json`, `releve-complementaire.json`.

## Constats ciblés

FACT : `/consultant-seo-lyon/` reçoit un lien éditorial depuis une seule page source distincte : `/consultant-seo-geo-lyon/`, ancre « consultant SEO à Lyon ». Elle ne contient aucun lien éditorial vers une autre URL interne dans le graphe. Les liens `#contact` sont des déplacements dans la même page et ne comptent pas comme sorties.

FACT : Des liens hors contenu vers la nouvelle page existent depuis 25 URL sources du crawl. Le relevé HTML complémentaire les situe dans le footer. Ils sont séparés du comptage éditorial. La nouvelle page est accessible depuis l’accueil par son footer.

FACT : `/consultant-seo-geo-lyon/` reçoit une source classée éditoriale par le script : `/plan-du-site/`. C’est une liste utilitaire ; ce comptage ne constitue pas une recommandation contextuelle dans un paragraphe commercial.

FACT : `/accompagnement-seo-geo/` et `/consultant-geo/` ne reçoivent aucune source éditoriale dans le périmètre des 32 URL. Leurs liens de gabarit restent comptés séparément.

## Accessibilité et proximité des pages

FACT : Le contrôle complémentaire de huit URL finales avec slash a obtenu HTTP 200, un canonical vers chacune d’elles et aucune directive noindex dans les métas robots ou l’en-tête X-Robots-Tag. Les huit objets figurent dans `targets.json`. Ce contrôle ne prouve pas leur indexation dans Google.

FACT : Les H1 complets, relus dans le HTML, sont « Consultant SEO à Lyon pour les entreprises B2B » et « Consultant SEO Lyon pour les entreprises B2B ». Le parser du script officiel tronque certains H1 comportant des spans ; `targets.json` sert de preuve pour les titres complets.

FACT : La cible `/etudes-de-cas/appart-hotel/` affiche le H1 « +30 % de réservation en direct ». La nouvelle page indique que ses chiffres SEO ne permettent pas seuls d’attribuer une hausse des réservations. Le relevé ne permet pas de rapprocher les périodes ni d’établir l’attribution du chiffre de la cible.

## Limites

La collecte du sitemap ne développe pas récursivement toutes les cibles découvertes. `/tarifs/` et `/etudes-de-cas/appart-hotel/` ont été contrôlées en complément ; leurs compteurs entrants tirés du graphe restent partiels. Les pages `/systeme-seo/` et `/audit/` figurent dans des liens mais ne sont pas couvertes par ce crawl du sitemap. Aucun état global du site n’est déduit de ces absences.

Le relevé Search Console du 5 octobre précède la publication de la nouvelle page. Il ne permet ni de mesurer son trafic ni de confirmer une cannibalisation après sa mise en ligne. Voir [[audit/2026-10-05-organikk-mots-cles-business]].

Analyse : [[maillage/2026-10-10-organikk-lyon-structurel-decision]]. Plan : [[maillage/2026-10-10-organikk-lyon]].

## Contrôle après publication

FACT : Après le déploiement `6ac9fdb02212dca4cebe0bd8`, le même script a parcouru les 32 URL sans erreur : 747 occurrences de liens internes, dont 65 éditoriales. La page demandée reçoit quatre sources éditoriales distinctes et possède deux destinations éditoriales. Les cinq liens préparés sont présents. Données : `wiki/maillage/data/2026-10-10-organikk-apres/graph.json`, `index.json` et `validation.json`. Aucun effet sur les positions ou les demandes n’est établi par ce contrôle.
