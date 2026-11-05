---
type: synthese
title: "Algorithme : Récap semaine 38 (2026-09-14 au 2026-09-20)"
date: 2026-09-20
week: 2026-W38
tags: [synthese, algorithme, recap-hebdo, ia, seo, geo]
status: draft
sources_count: 4
---

# Récap semaine 38 : Google devient l'intermédiaire qui paie, filtre et cite à votre place

> Synthèse des 4 revues de presse Algorithme entre le 2026-09-14 et le 2026-09-18. Quatre éditions sur la fenêtre de 7 jours (14, 16, 17, 18/09) : le 15 et le 19-20 n'ont pas produit d'édition, la synthèse s'appuie sur ce volume réduit sans compléter par de l'invention. [[ops/sante-automatisations]] confirme que la revue de presse est à jour (dernière édition le 18/09, cadence 1 j) : l'absence du 15 et du week-end n'est pas une panne.

## Tendance dominante

Cette semaine, Google a construit trois pièces d'une même infrastructure : un rapport Search Console qui compte les impressions IA sans les clics (14/09), un module qui paie certains éditeurs pour leur contribution aux réponses IA sans publier la formule (16/09), et un classement qui montre que ses résumés citent d'abord YouTube et Reddit plutôt que les sites eux-mêmes (17/09). Le fil commun : Google mesure, rémunère et cite à travers ses propres critères, sans les rendre publics et souvent sans faire passer l'utilisateur par votre site. En parallèle, Cloudflare a activé le 15/09 le blocage par défaut des robots d'entraînement IA, avec un risque documenté de bloquer Googlebot par erreur (18/09), la même semaine où les données Cloudflare Radar montrent que les robots de réponse (OAI-SearchBot, Claude-User) passent presque toujours, contrairement aux robots d'entraînement (GPTBot, ClaudeBot), bloqués deux fois sur trois. Le crawl ne vaut plus rien, la citation commence à valoir quelque chose : c'est la thèse que Tim répète depuis mi-juillet, et cette semaine l'aligne sur trois sources indépendantes.

## Pilier dominant : SEO, 55 % du volume (11/20)

Onze items sur vingt relèvent du SEO classique (volatilité d'algo, données Search Console, positions, outils de suivi), neuf de l'IA (résumés, robots, publicité conversationnelle). Mais la frontière s'efface : la quasi-totalité des items SEO de la semaine sont des ricochets de l'IA générative. La volatilité d'algo du 4 au 13 septembre, l'absence de données Google Business Profile, la fusion des positions dans un bloc IA (Mueller) sont tous des effets de second ordre d'une infrastructure de recherche en cours de refonte, pas des mises à jour de pertinence au sens classique.

## Ce qui fait consensus

- **Les robots d'entraînement IA sont bloqués par défaut, les robots de réponse passent.** Confirmé par Cloudflare Radar sur 4 223 fichiers robots.txt (16/09 et détaillé le 18/09) : GPTBot bloqué 2,33 fois pour 1 fois autorisé contre 0,94 pour OAI-SearchBot ; ClaudeBot à 2,39 contre parité pour Claude-User ; Applebot-Extended à 3,24 contre Applebot majoritairement autorisé. Le même chiffre revient à deux jours d'intervalle, avec le risque ajouté le 18/09 : Cloudflare range Googlebot dans les robots à usages multiples, ce que Google conteste.
- **Le mouvement d'algo du 4 septembre a été annulé le 13.** Rapporté indépendamment par Barry Schwartz/Search Engine Roundtable (16/09 et 18/09) et par Glenn Gabe (18/09, « retours complets sur des sites qui avaient décroché »). Une nouvelle secousse a suivi le 15. Google n'a rien confirmé.
- **La mesure de clic est en train de se déconnecter du reporting IA.** Trois sources distinctes le montrent sous trois angles : le rapport « IA générative » de Search Console donne des impressions mais ni clics ni position (14/09, Search Engine Journal) ; John Mueller confirme que tous les liens d'un bloc IA héritent de la même position (17/09, Search Engine Roundtable) ; Ahrefs isole un -23,1 % de CTR sur les sites très exposés aux résumés IA avec un vrai groupe témoin (14/09).

## Ce qui fait débat

- **L'ampleur de la perte de trafic liée aux résumés IA.** Ahrefs (médiane -5,7 % de CTR sur 963 domaines, avec groupe témoin) contre mind Media (-19 % de fréquentation web sur 20 éditeurs Top 50 ACPM, en excluant le témoin), l'ACPM contestant formellement ce second chiffre. Deux méthodologies, un mois d'août brouillé par la mise à jour anti-spam du 18 au 21 août (14/09).
- **Qui a raison sur la classification de Googlebot.** Cloudflare le range parmi les robots à usages multiples (indexation + entraînement), bloquable donc par erreur si on coche « bloquer l'entraînement ». Google conteste et renvoie vers Google-Extended, un jeton séparé (18/09). Pas de tiers pour trancher cette semaine.
- **LinkedIn comme source de citation IA en B2B.** Tim défend cette thèse depuis avril, mais le classement Ahrefs le place à 0,6 % des citations, dix-neuvième sur cinquante (17/09). Tim le signale lui-même comme gênant plutôt que de l'ignorer : un classement tous sujets écrase une plateforme B2B, et Ahrefs ne mesure que Google, pas les autres moteurs.

## Signaux faibles à surveiller

- **Le programme AI contribution de Google.** Cité une seule fois (16/09, Digiday) mais c'est le premier mécanisme de paiement construit autour de la contribution à une réponse IA plutôt qu'autour du clic. Formule non publiée, montants qualifiés de « peanuts » par les éditeurs participants. À creuser : dès que d'autres éditeurs confirment des montants, ça mérite une fiche entity/concept séparée.
- **Sponsored Agents d'OpenAI.** Cité une seule fois (17/09) : une publicité dans ChatGPT qui ouvre une conversation avec un agent payé par la marque avant de renvoyer vers le site. Test US avec Newegg, Best Buy, Lowe's, VistaPrint. Structurellement, c'est la première pub conversationnelle documentée dans un moteur de réponse.
- **Onze jours sans données sur les fiches Google Business Profile en septembre.** Cité une seule fois (18/09), résolu depuis, mais un signal d'instabilité côté reporting local à surveiller si ça se reproduit.

## Angles à creuser semaine prochaine

### Angle 1 : Google vous paie pour une réponse dont il ne publie pas la formule
**Pourquoi maintenant** : le programme AI contribution est confirmé (16/09) au moment même où Ahrefs montre que 60 % des citations IA de Google vont à des plateformes tierces (YouTube, Reddit, réseaux sociaux, 17/09). Si Google paie « à la valeur » sans formule publique, la seule protection est la donnée que le modèle ne peut pas fabriquer seul : la thèse que Tim défend depuis le printemps, avec une preuve fraîche à l'appui.
**Format suggéré** : article ou post LinkedIn.

### Angle 2 : bloquer l'entraînement IA peut vous couper de Google, vérifiez avant de cocher
**Pourquoi maintenant** : la bascule Cloudflare du 15/09 touche tous les comptes gratuits et nouveaux domaines, et le risque de confondre Googlebot avec un robot d'entraînement est documenté noir sur blanc par Cloudflare elle-même (18/09), pendant que Google conteste cette classification. C'est un angle actionnable immédiat : un audit en cinq minutes (vérifier le réglage Cloudflare + le statut Googlebot) évite une perte de trafic invisible.
**Format suggéré** : post LinkedIn ou quick-win.

---

## Index des éditions de la semaine

- [[raw/revue-de-presse/2026-09-14-revue-presse|2026-09-14]] : Deux mois de résumés IA en France, les chiffres ne sont pas d'accord
- [[raw/revue-de-presse/2026-09-16-revue-presse|2026-09-16]] : Google a commencé à payer votre contenu. Sans dire comment il calcule.
- [[raw/revue-de-presse/2026-09-17-revue-presse|2026-09-17]] : L'IA de Google cite YouTube et Reddit avant de vous citer
- [[raw/revue-de-presse/2026-09-18-revue-presse|2026-09-18]] : Le bouton qui vous protège de l'IA peut vous sortir de Google

---

*Récap auto-généré chaque dimanche soir à partir de `raw/revue-de-presse/`. Pour traiter les angles : ouvre wiki/queries/ et créé un brief, ou wiki/posts-linkedin/ pour un draft.*
