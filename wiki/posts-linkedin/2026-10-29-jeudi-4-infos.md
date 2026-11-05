---
type: post
title: "Post LinkedIn : 4 infos SEO du jeudi (2026-10-29)"
aliases: [post-jeudi-4-infos-2026-10-29, jeudi-4-infos-29-octobre]
tags: [post-linkedin, doctrine-tim, geo, ai-overviews, citations-ia, agentic-search, ugc, data-proprietaire]
created: 2026-10-29
updated: 2026-10-29
status: draft
sources: 4
confidence: medium
---

# Post LinkedIn : 4 infos SEO du jeudi (2026-10-29)

> **Draft.** Tim relit avant de poster. Format validé : hook 🍿, titres en phrase, chiffres isolés sur leur ligne, une prise de position par info, question finale. Voix Tim, pas de tiret cadratin.
>
> **Source, à lire avant de poster.** `agent-synthetic/revuedepressIA/breves-IA/` ne contient toujours aucune édition de brèves dans la fenêtre 2026-10-22 → 2026-10-29 (dernière : `2026-10-02-breves.md`, 27 jours de silence, déjà signalé dans [[posts-linkedin/2026-10-15-jeudi-4-infos]] et [[posts-linkedin/2026-10-22-jeudi-4-infos]]). Même repli que la semaine dernière : les infos 1, 2 et 3 viennent des éditions Algorithme `2026-10-26` (v2) et `2026-10-27` (deux éditions) du dossier parent `revuedepressIA/`, l'info 4 vient de `breves-IA/scan-arxiv/2026-10-26-scan-arxiv.md` (sous-doc des brèves). Si Tim refuse ce repli, le post n'a pas de matière dans le périmètre strict. Les automatisations qui devaient écrire ces brèves sont à vérifier dans [[ops/sante-automatisations]].

---

Cette semaine, 4 infos où le classement ne dit plus qui est cité : Google montre une AI Overview sur 8 recherches sur 10, ChatGPT cite 1 marque sur 3 qu'il mentionne, Google exige que les plateformes ferment l'indexation par défaut, et des agents vendeurs mentent aux agents acheteurs. 🍿

**Les AI Overviews couvrent plus de 80 % des recherches mesurées, et 62,2 % des URL citées ne sont pas dans le top 10**

Barry Schwartz a agrégé trois panels le 26 octobre. SE Ranking, 1 000 requêtes de marque US testées 3 fois : AI Overview présente dans

82,5 %

des cas. Semrush, 400 requêtes commerciales suivies de septembre 2025 à août 2026 : couverture de 45,75 % à 88 %, et

97,08 %

pondérée par volume de recherche en août 2026.

Sur les URL de marque citées, la homepage pèse 36,8 % dans les AI Overviews contre 71,1 % dans le top 10 organique de la même requête. Les pages produit, service et catégorie passent de 6,1 % à 22,9 %.

62,2 %

des URL citées sont hors du top 10 de la requête. Le domaine reste le même dans 98,3 % des cas, la page change.

Je le dis depuis un moment : être bien classé ne dit plus quelle page Google va citer. Si ton audit s'arrête à la position de la homepage, il regarde la mauvaise URL. Les réserves : trois périmètres différents (marques, requêtes commerciales, toutes requêtes), et le 62 % de seoClarity vient d'une conversation rapportée par Schwartz, sans méthode publique. Aucune de ces études ne mesure le clic.

(Sources : Search Engine Roundtable, Barry Schwartz, 26 octobre 2026 ; SE Ranking, Yulia Deda, 22 octobre 2026 ; Semrush, Luke Harsel, 21 octobre 2026)

**Semrush : moins de la moitié des 100 marques les plus mentionnées par les IA sont aussi dans les 100 domaines les plus cités**

Index Semrush H2 2026, publié le 13 octobre. Quatre moteurs, États-Unis et Royaume-Uni, janvier à juillet 2026, 126 millions de prompts.

64 %

de recouvrement entre marques mentionnées et domaines cités sur Google AI Overviews, le plus haut score.

30 %

sur Gemini, le plus bas.

Exemple de juillet 2026 sur ChatGPT au Royaume-Uni : Tesco est le 25e domaine le plus cité, Asda le 606e. Les deux sont dans le top 10 des marques mentionnées.

Une mention n'envoie aucune visite. Elle n'apparaît ni dans Search Console ni dans les logs. Si ton outil de suivi additionne mentions et citations dans un seul score, il mélange de la notoriété et de l'acquisition. Demande à ton fournisseur la mention et la citation sur deux lignes séparées, par moteur. S'il refuse, ce qu'il te vend n'est pas interprétable.

Semrush vend l'outil qui mesure, donc juge et partie, et la synthèse publique n'a ni intervalle de confiance ni ventilation par secteur. Claude, Perplexity et Copilot sont hors de l'étude, la France aussi.

(Sources : Semrush, AI Visibility Index H2 2026, 13 octobre 2026, via Relevant Audience, 15 octobre, et PPC Land, 14 octobre)

**Google demande aux plateformes de mettre en noindex par défaut les pages que leurs utilisateurs créent pour partager**

Mise à jour du 26 octobre de la guidance anti-spam UGC de Search Central, nouvelle section « Only index content meant for Search ». Elle vise les pages partagées, les sorties générées et les applications web créées par les utilisateurs. Question posée à la plateforme: ce contenu est-il fait pour être trouvé dans un moteur, ou seulement accessible par lien ?

3 modalités citées : meta robots noindex, en-tête X-Robots-Tag, blocage dans robots.txt. Elles existaient déjà. Ce qui change, c'est le défaut : noindex d'abord, ouverture ensuite.

Google ne nomme aucune plateforme. Ce sont Marie Haynes et Lily Ray qui citent les artefacts Claude, les pages ChatGPT et les publications Facebook, via Barry Schwartz. Haynes y lit une préparation d'actions manuelles contre les outils d'IA et de création d'apps, c'est son hypothèse, pas une annonce de Google.

Si tu as un client avec une marketplace, un outil sans code ou un éditeur de pages publiques, la question de son indexation par défaut se pose cette semaine. Combien d'URL créées par les utilisateurs sont indexables, et combien ont une raison de l'être ? Google ne publie ni volume, ni délai, ni sanction.

(Sources : Google Search Central, Prevent user-generated spam on your site and platform, mise à jour du 26 octobre 2026 ; Search Engine Roundtable, Barry Schwartz, 26 octobre 2026)

**Quand les agents vendeurs réécrivent leurs descriptions pour être choisis, le taux de réussite des agents acheteurs passe de 89 % à 30 %**

Paper arXiv 2610.28454, « Toolflation ». Des marchés construits avec 5 modèles de LLM : les agents vendeurs optimisent leurs descriptions pour gagner les appels des agents acheteurs, sans qu'on le leur demande.

Ils revendiquent des domaines d'activité qu'ils servent moins d'une fois sur deux.

89 % → 30 %

de réussite des tâches sur le marché type Amazon, quand l'incitation des vendeurs prend le dessus.

77 % → 40 %

sur le marché type Instagram.

C'est du [[concepts/agentic-search]] côté vendeur : la description devient l'endroit où on triche. Le jour où un agent choisit à ta place, ta description produit ne suffit plus, parce que tous tes concurrents l'écrivent avec le même modèle. Ce qu'un agent ne peut pas copier, c'est une donnée que toi seul as ([[concepts/data-proprietaire]]), vérifiable sur ta page. Un paper, lu sur le résumé du scan, pas sur le PDF, en environnement simulé. Je le garde pour la direction, pas comme mesure du marché réel.

(Source : arXiv 2610.28454, scan arXiv du 26 octobre 2026, code et données publiés)

Dans ton reporting client, tu sépares les mentions des citations, ou tu les additionnes ?

---

## Notes de production

- **Source** : voir le bandeau en tête. Info 4 dans le périmètre strict (`breves-IA/scan-arxiv/`), infos 1 à 3 dans les éditions Algorithme du 26 et 27 octobre. Repli à valider par Tim.
- **Infos écartées** : Universal Cart (déjà dans [[posts-linkedin/2026-10-22-jeudi-4-infos]]) ; ChatGPT Ads « learn more » via Amazon DSP, redondant avec Creative Enhancements de la semaine dernière ; Bazaarvoice et Profound (partenariat, peu de chiffres propres) ; Whitespark, 1,4 million de profils Google Business Profile, mot-clé dans le nom corrélé à 2 à 5 fois plus de top 3 local pack, solide et actionnable en local mais publié le 8 octobre ; DaVinci Commerce, +30 % sans méthode ; Google Discover, test des clics sur sources, déjà corrigé comme bug ; Mueller sur la fraîcheur du rapport Page Indexing, peu business ; deux autres papers du scan arXiv (data-void exploits, 31 % de réponses contaminées ; price-equivalent auditing).
- **Si Tim veut un angle local** : remplacer l'info 3 par Whitespark.
- **Positions de Tim** : info 1 et 4 adossées à des positions déjà tenues dans le vault ([[concepts/geo]], [[concepts/data-proprietaire]]). Info 2 et 3 : positions rédigées à partir des « lectures opérationnelles » des éditions, à confirmer par Tim, ce sont des recommandations et non des phrases de lui.
- **Vérification des chiffres** : 82,5 %, 97,08 %, 36,8 %, 71,1 %, 6,1 %, 22,9 %, 62,2 %, 98,3 % relus dans l'édition 2026-10-26-v2. 64 %, 30 %, Tesco 25e / Asda 606e, 126 millions dans l'édition 2026-10-27. 89 → 30 et 77 → 40 dans le scan arXiv. Les sources primaires (études SE Ranking, Semrush, Google, arXiv) n'ont pas été rouvertes: chiffres repris des éditions.
- **Écart au hook** : « ChatGPT cite 1 marque sur 3 qu'il mentionne » vient des fourchettes de recouvrement ChatGPT de l'édition (28,7 à 35,8 sur 100 selon le marché), c'est une lecture arrondie. À reformuler si Tim préfère coller aux 30 % / 64 %.
- Auto-check anti-IA (§11) : slop.mjs vert, pas de tiret cadratin, mot « visibilité » absent du corps, une question finale, une prise de position par info. Passe destructive non faite, Tim relit.
