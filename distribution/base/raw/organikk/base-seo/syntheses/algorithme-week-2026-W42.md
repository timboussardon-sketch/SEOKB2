---
type: synthese
title: "Algorithme : Récap semaine 42 (2026-10-12 au 2026-10-18)"
date: 2026-10-18
week: 2026-W42
tags: [synthese, algorithme, recap-hebdo, ia, seo, geo]
status: draft
sources_count: 2
---

# Récap semaine 42 : l'IA choisit à la place de l'acheteur, et vos statistiques ne le voient plus

> Synthèse des 2 revues de presse Algorithme entre le 2026-10-12 et le 2026-10-18. Seulement deux éditions (14 et 15/10) : [[ops/sante-automatisations]] (relevé du 2026-10-17) classe la revue de presse « en retard », dernière sortie le 15/10. Aucune édition les 12, 13, 16, 17 et 18/10. Les récaps W40 et W41 n'existent pas non plus (récap Algorithme « en panne » depuis le 2026-09-27). Ce récap ne couvre que neuf items : les ratios ci-dessous sont indicatifs.

## Tendance dominante

Les deux infos du jour se répondent. Le 14/10, Kevin Indig mesure que dans AI Mode, 74 % des acheteurs prennent le produit classé premier et que 64 % ne cliquent sur aucun lien (185 achats) ; côté ChatGPT, Profound compte 92,8 % de sessions d'achat sans clic vers un site (221 tâches). Le 15/10, on apprend que depuis GPT-6, ChatGPT ouvre une partie des liens sans `utm_source` : sur 500 pages suivies par Cedric Huesler (Adobe), −31 000 visites ChatGPT par jour, +26 000 visites « Direct ». La décision se prend dans la réponse, et le peu de clics qui reste devient moins traçable. La semaine W39 parlait déjà d'une mesure qui casse ; W42 ajoute que ce n'est plus Google seul qui la casse, c'est OpenAI aussi.

## Pilier dominant : IA, 67 % du volume (6/9)

Six items sur neuf relèvent de l'IA générative : les deux infos du jour, les publicités pharmaceutiques dans AI Mode, Discover en « concierge », Gemini 4 Argon, l'étude Lily Ray sur les pages « meilleurs X ». Trois relèvent du SEO classique : UGC Fresh Data Program, empoisonnement des SERP vues par les rank trackers, traitement des PDF. Le classement de Discover en IA est discutable (c'est un produit Google Search, l'item porte sur sa transformation en agent).

## Ce qui fait consensus

- **L'achat assisté par IA se fait sans visite du site.** Indig (64 % sans clic, 88 % gardent la liste courte telle quelle) et Profound (92,8 % de sessions sans clic, 3,2 % de vérification sur un autre site), 14/10. Deux études, deux moteurs, petits panels US, et Profound vend un outil de suivi des citations.
- **Le trafic ChatGPT n'a pas baissé, il a changé de ligne.** Huesler/Adobe (+26 000 « Direct » pour −31 000 ChatGPT, environ 5 000 visites/jour non retrouvées), Profound (réponses avec lien étiqueté : 98 % le 8/10, 66 % le 14/10), Dalin Degraff, 15/10. Profound apparaît dans les deux consensus de la semaine : ce n'est pas une source indépendante comptée deux fois.
- **Les rapports de positions de septembre-octobre ne sont pas fiables.** Étude Nozzle du 10/10 : 8,0 % de pages de résultats « empoisonnées » du 13/09 au 9/10, contre 0,17 % fin août (15/10). Prolonge directement le blocage des rank trackers rapporté le 21/09 (W39).

## Ce qui fait débat

Pas de désaccord notable entre experts nommés cette semaine. Une réserve de méthode : sur l'étude Lily Ray (83 % de non-recommandation quand une marque se classe première sur sa propre liste, contre 69 % en juin), les relais ne comptent pas de la même façon, et Tim signale ne pas avoir lu l'original (15/10). Ordre de grandeur, pas chiffre établi.

## Signaux faibles à surveiller

- **UGC Fresh Data Program** : cité une fois (14/10). Google ouvre aux forums et réseaux un canal d'indexation en quelques minutes, sous balisage DiscussionForumPosting ou SocialMediaPosting. À creuser : fiche entité dans `wiki/entities/`, et un test sur un client qui a une communauté active.
- **Publicités pharmaceutiques dans AI Overviews et AI Mode** : cité une fois (14/10), test US d'octobre confirmé à Adweek. Premier emplacement publicitaire documenté sur une catégorie YMYL dans les réponses IA de Google. À suivre avec les Sponsored Agents d'OpenAI (signal faible W39).
- **Discover en « concierge proactif »** : cité une fois (14/10), source : une offre d'emploi. Indice faible, mais il concerne les éditeurs qui vivent de Discover.

## Angles à creuser semaine prochaine

### Angle 1 : Votre rapport GEO s'est cassé le 9 octobre
**Pourquoi maintenant** : la ligne « ChatGPT » de Google Analytics a perdu une partie de son trafic au profit de « Direct » (Huesler, Profound, 15/10), et les rank trackers servent des SERP faussées depuis le 13/09 (Nozzle). Les deux preuves standard d'un accompagnement SEO/GEO sont touchées en même temps. Matière déjà dans l'édition du 15/10 : annotation du 9/10, champ « comment nous avez-vous connus », panel fixe de requêtes.
**Format suggéré** : post LinkedIn, puis méthode dans `wiki/methodes/` pour les reportings clients.

### Angle 2 : Deuxième dans la réponse de l'IA, c'est absent
**Pourquoi maintenant** : dans AI Mode, les rangs trois et plus se partagent 10 % des choix (Indig, 14/10). Rejoint l'angle 2 de W39 (fiche produit et paiement natif dans Gemini), non traité depuis.
**Format suggéré** : article.

---

## Index des éditions de la semaine

- [[raw/revue-de-presse/2026-10-14-revue-presse|2026-10-14]] : 74 % des acheteurs prennent le premier produit que l'IA leur propose
- [[raw/revue-de-presse/2026-10-15-revue-presse|2026-10-15]] : Votre trafic ChatGPT est peut-être passé en « Direct »

Récap précédent : [[syntheses/algorithme-week-2026-W39]].

---

*Récap auto-généré chaque dimanche soir à partir de `raw/revue-de-presse/`. Pour traiter les angles : ouvre wiki/queries/ et créé un brief, ou wiki/posts-linkedin/ pour un draft.*
