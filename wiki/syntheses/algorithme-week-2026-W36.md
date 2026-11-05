---
type: synthese
title: Algorithme — Récap semaine 36 (2026-08-30 au 2026-09-05)
date: 2026-09-06
week: 2026-W36
tags: [synthese, algorithme, recap-hebdo, ia, seo, geo, seo-local]
status: draft
sources_count: 3
---

# Récap semaine 36 — Personne ne vous a demandé la permission

> Synthèse des 3 revues de presse Algorithme entre le 2026-08-30 et le 2026-09-05. Trois éditions seulement sur la fenêtre de 7 jours (30/08, 01/09, 03/09) : la synthèse s'appuie sur ce volume réduit, sans compléter par de l'invention. L'édition du 30/08 n'avait pas été couverte par le récap W35, elle entre ici.

## Tendance dominante

Cette semaine, quatre intermédiaires ont changé les règles sans prévenir les sites qui en dépendent. ChatGPT a modifié sa mécanique de découpage de requête le 8 août, et Reddit a perdu 86 % de ses citations sans avoir touché à une ligne (édition du 30/08). Google Maps a retiré le bouton d'appel de 80 % de ses blocs de trois fiches, et les appels vers les commerces baissent (01/09 et 03/09). Rank Math s'est créé un accès administrateur sur 4 millions de sites WordPress, et l'a envoyé à sa maison mère avant de demander quoi que ce soit (03/09). Cloudflare, lui, ferme par défaut : à partir du 15 septembre, les robots IA sont bloqués sur toute page avec pub de tout nouveau domaine (03/09). Le fil commun : l'affichage, l'accès et la citation se décident chez un tiers, et ce tiers ne consulte pas le site. Les résumés IA apparaissent dans les trois éditions, mais ce n'est plus l'histoire principale. L'histoire, c'est que la mécanique du moteur compte plus que la qualité de la page, et que cette mécanique change un mardi.

## Pilier dominant : IA — 58 % du volume (7/12)

Sept items sur douze touchent à l'IA, mais presque aucun ne parle de contenu généré. Le sujet, c'est l'IA comme intermédiaire d'accès : qui cite (ChatGPT, fan-out), qui lit (robots bloqués par Cloudflare), qui paie (Universal Commerce Protocol via Google Pay), qui entre dans l'admin (agent Rank Math), qui reçoit les données de clics Google en Europe (assistants IA éligibles au programme DMA). Le SEO classique pèse 33 % (4/12) et se concentre sur le local : Google Maps occupe deux éditions sur trois. Le pilier contenu ne tient qu'avec l'étude listicles de Kevin Indig (1/12), mais c'est la seule étude de la semaine avec un vrai volume (60 000 requêtes).

## Ce qui fait consensus

- **Le point de contact local sort du site et du téléphone** — confirmé par l'étude sur 3 075 résultats Google Maps (Programming Insider, 01/09 : bouton d'appel survivant dans une recherche sur cinq) et par GMBapi, Sterling Sky et Jepto (Search Engine Land, 03/09 : appels -11,9 %, clics vers le site -12,5 %, itinéraires +21,1 % entre T2 2025 et T2 2026). Deux sources, deux méthodes, même direction : le client compare sur Maps et se déplace sans passer par vous.
- **Ce qui s'affiche dépend de la mécanique du moteur, pas de la page** — confirmé par Promptwatch (30/08 : Reddit passe de 3,83 % à 0,52 % de citations ChatGPT sans changement côté Reddit, l'opérateur site: passant de 0,37 % à 16,8 % des sous-requêtes) et par Search Engine Roundtable (01/09 : articles du WSJ, du NYT et de CNN invisibles une heure le 28/08 alors que la Search Console les donnait indexés).
- **Le résumé IA ne remplace pas les résultats classiques, il les recouvre** — confirmé par Growth Memo (01/09 : un résumé IA au-dessus de 83,7 % des SERP à listicles, 93,4 % en B2B, et le listicle garde le top 10 en dessous) et par Search Engine Land (03/09 : les encarts locaux générés par l'IA affichent deux établissements au lieu de trois, sans bouton d'appel, et 32 % du nombre d'établissements distincts de l'encart classique). Le résultat classique reste, mais avec moins de place et moins de boutons.
- **Retirer les résumés IA rend le clic, et le mode IA seul fait baisser la confiance** — confirmé par l'expérience contrôlée arXiv 2608.18352 sur 1 100 personnes (01/09) et, en creux, par Google lui-même : le bouton « source préférée » doublerait le taux de clic (Search Central, 30/08), ce qui suppose un taux de clic par défaut assez bas pour valoir un badge. Une seule source expérimentale, donc consensus à confirmer sur la durée.

## Ce qui fait débat

- **Pourquoi Reddit a chuté** — Explainx et TechCrunch relaient le blocage robots.txt du 20 août. Promptwatch date la chute du 14 au 17 août et le changement de fan-out du 8 août. Tim's take (30/08) : le calendrier tranche, le blocage est postérieur à la chute de trois jours, la cause est le [[concepts/query-fan-out]] qui a changé de préférence de source, et Reddit n'y est pour rien.
- **Rank Math « lecture seule » contre Sybre Waaijer « accès administrateur »** — Rank Math parle de droits hérités et d'identifiants jamais conservés. Waaijer et The Repository rappellent qu'un mot de passe d'application WordPress hérite de tous les droits du compte qui le crée. Tim's take (03/09) : la lecture seule est une promesse côté Rank Math, pas un verrou côté WordPress.
- **Combien d'appels perdus sur Google Maps** — les retours terrain de l'édition du 01/09 donnent -20 à -40 %, jusqu'à -50 à -70 % en urgence, sans méthode publiée. GMBapi mesure -11,9 % sur un an (03/09). Un facteur trois à six entre les chiffres. Tim's take : à trancher, les deux premiers chiffres n'ont pas de méthode, le troisième est le seul mesuré.

## Signaux faibles à surveiller

- **Google livre ses données de clics aux moteurs et assistants IA européens** (Search Central, 03/09) — cité une fois, mais c'est structurel : contrats le 17 septembre, échantillons le 16 novembre, seuil à 50 000 utilisateurs mensuels, assistants IA éligibles s'ils correspondent à la définition d'un moteur. Vos positions Google en Europe alimentent les réponses de ChatGPT et Perplexity demain. À creuser : suivre la liste des signataires le 17/09 et créer une page entité sur le programme de licence DMA.
- **Le bouton « source préférée » de Google** (Search Central, Techwyse, 30/08) — cité une fois, deux lignes de HTML, badge visible dans les AI Overviews et [[entities/google-ai-mode]] depuis le 27 mai, taux de clic doublé selon Google. Seuls les domaines et sous-domaines racines sont éligibles. À creuser : le poser sur organikk.co cette semaine et mesurer, et vérifier si Substack laisse l'insérer sur algorithme.substack.com.
- **L'expérience arXiv 2608.18352** (01/09) — première mesure avec groupe témoin de l'effet des résumés IA sur le clic et la confiance. Cité une fois, mais c'est l'argument à opposer aux clients qui pensent que la perte de clic se compense par une meilleure expérience. À creuser : fiche source dans le wiki avant que l'étude soit reprise partout.
- **L'Universal Commerce Protocol** (Google Developers Blog, 30/08) — mode d'emploi technique de l'achat depuis une conversation IA, paiement Google Pay, vingt entreprises rejointes. Prolonge la réservation d'hôtel du récap W35 : l'agent capture le point de paiement, et la liste de lancement est déjà faite de dominants.

## Angles à creuser semaine prochaine

### Angle 1 : Reddit n'a rien changé et a perdu 86 % : ce n'est pas votre page qui décide, c'est le fan-out
**Pourquoi maintenant** : Promptwatch fournit la première chronologie précise d'un effondrement de citations expliqué par un changement de mécanique de requête, pas par le site. Et la licence de données DMA (03/09) va caler les assistants IA européens sur les clics Google dès novembre : la mécanique de source des moteurs va encore bouger. Tim tient déjà le concept ([[concepts/query-fan-out]], « ce que j'appelle le fan-out ») et la doctrine (« une citation IA n'est pas une métrique de business », depuis l'édition du 12 juin). Personne n'a encore relié les deux pour un lectorat non technique.
**Format suggéré** : article organikk ou post LinkedIn long, plus mise à jour de [[concepts/query-fan-out]] avec le cas Reddit et les chiffres Promptwatch.

### Angle 2 : Votre plugin SEO a un agent. Qui tient les clés ?
**Pourquoi maintenant** : Rank Math annonce que son agent de support est « la première brique » d'agents qui agiront sur le site. Matt Mullenweg demande un audit obligatoire. Cloudflare choisit le défaut inverse le 15 septembre. L'UCP fait payer un agent avec des moyens déjà enregistrés. Tim construit des agents SEO avec Claude tous les jours et sait exactement ce qu'il exige d'eux : permissions une par une, expiration, révocation en un clic. C'est l'inversion d'expertise : celui qui fabrique des agents explique pourquoi il refuse ceux qui ne demandent pas.
**Format suggéré** : post LinkedIn (checklist « ouvre Utilisateurs, Profil, Mots de passe d'application ») puis article, à relier à [[concepts/agentic-search]].

---

## Index des éditions de la semaine

- [[2026-08-30-revue-presse|2026-08-30]] — Reddit perd 86 % de ses citations ChatGPT, pour une raison différente de celle qu'on raconte
- [[2026-09-01-revue-presse|2026-09-01]] — 55 % des tops 10 Google sont encore des listicles
- [[2026-09-03-revue-presse|2026-09-03]] — 4 millions de sites : le plugin SEO qui s'est créé un accès admin sans demander

---

*Récap auto-généré chaque dimanche soir à partir de `raw/revue-de-presse/`. Pour traiter les angles : ouvre wiki/queries/ et créé un brief, ou wiki/posts-linkedin/ pour un draft.*
