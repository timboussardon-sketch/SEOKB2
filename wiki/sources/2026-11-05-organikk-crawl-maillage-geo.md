---
type: source
source_type: test-terrain
title: "Organikk : crawl structurel et contrôles des pages GEO"
aliases: []
tags: [geo, maillage, organikk]
created: 2026-11-05
updated: 2026-11-05
sources: 1
confidence: high
status: stable
---

# Collecte du 5 novembre 2026

Script exécuté : `python3 /Users/timothee/.claude/skills/maillage-systeme/scripts/crawl_graph.py https://organikk.co/sitemap.xml -o wiki/maillage/2026-11-05-organikk-questions-geo-data`.

Résultat : 49 pages parcourues, aucune erreur remontée. Preuves : `index.json` et `graph.json` dans ce dossier. Le parseur exclut nav/header/footer/aside, les liens internes à la même page et les couples ancre/cible de gabarit répétés. Entrants = pages sources distinctes ; sortants bruts du script = occurrences de liens, pas cibles distinctes. Le plan du site est inclus par le parseur mais n'est pas une preuve éditoriale thématique.

L’outil `/outils/questions-geo` reçoit 68 occurrences hors corps éditorial, toutes libellées « Générateur de questions IA », et aucun entrant éditorial dans le périmètre du sitemap. Aucun sortant éditorial détecté depuis l’outil. `/consultant-geo` reçoit trois sources classées in-body : plan du site (« Consultant GEO »), consultant SEO Lyon (« référencement dans les IA génératives »), skills SEO (« être citée »). Soit deux sources de contenu en excluant le plan du site.

Contrôle GET complémentaire : les huit pages du lot (sources + destinations) répondent 200 sans redirection. Les meta robots contiennent index/follow et les canonicals correspondent aux URL demandées. Détail `access-checks.json` ; copies HTML dans `html/`. X-Robots-Tag et indexation réelle Google non contrôlés. Le script ne conserve pas le statut HTTP ni les redirections de toutes les pages : ne pas généraliser le contrôle complémentaire au site entier.

Le sitemap ne couvre pas forcément toutes les URL. Liens injectés après JavaScript non mesurés. Aucune GSC, conversion, autorité ou performance IA mesurée. Les passages des pages retenues ont été lus séparément par trois agents (trois sources maximum chacun).

Voir [[maillage/2026-11-05-organikk-questions-geo]] et [[maillage/2026-11-05-organikk-questions-geo-structurel-decision]].
