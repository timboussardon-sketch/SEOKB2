---
type: doctrine
title: "Agent avocats : prospection pilotée par objectif"
aliases: [agent avocats, agent prospection avocats]
date: 2026-10-01
updated: 2026-10-22
tags: [agents, prospection, avocats, geo, claude-api, visibilite-ia]
status: living-doc
sources: 1
---

# Agent avocats : prospection pilotée par objectif

Je donne un nombre à l'agent : « 30 avocats en droit du travail à Lyon, côté employeurs, avec un email prêt à relire ». Il cherche des cabinets, les qualifie, mesure leur présence dans les réponses de Claude, audite le site de ceux qui n'y figurent pas, liste des requêtes et rédige un brouillon. Il recommence la recherche tant que le nombre n'est pas atteint. S'il s'arrête avant, il écrit pourquoi.

Code : `~/Code/prospection/agent-avocats/`, copié dans cette base sous `agent-prospect/` (82 fichiers, sans clé ni donnée de cabinet). Fiche source et instantané du code : [[raw/agents/agent-avocats/README]]. Autres agents : [[agents/ia-employe]], [[entities/qadence-seo-agent]].

## État au 1er octobre 2026

67 tests passent sur une base PostgreSQL locale.

L'agent n'envoie aucun email. Il s'arrête au brouillon relu et approuvé.

## Les boucles

| Boucle | Elle s'arrête quand |
|---|---|
| Campagne | le nombre visé est atteint, ou une limite est touchée : tours de découverte, résultats, deux tours sans nouveau candidat, budget |
| Découverte | la formulation du tour a rendu ses candidats ; le tour suivant change de formulation |
| Qualification | le cabinet est qualifié, rejeté avec un motif, ou envoyé en revue |
| Enrichissement | une adresse publiée est trouvée, ou 10 pages du site sont lues |
| Présence IA | 15 réponses valides sont réunies (5 questions, 3 fois chacune), ou chaque créneau a été tenté 3 fois |
| Mots-clés | 20 requêtes sont retenues, ou 2 tours sont faits |
| Email | toutes les phrases passent le contrôle, ou 2 réécritures ont échoué |

Motifs de rejet : hors zone, autre pratique, autre clientèle, pas de site exploitable, doublon, site qui refuse l'exploration, opposition enregistrée.

## Règles codées

- Une adresse email vient d'une page du cabinet. L'agent n'en compose aucune avec un nom.
- Un site qui répond 403 ou dont le robots.txt interdit l'exploration est abandonné.
- Une erreur, un refus ou une réponse vide ne compte jamais comme une absence. Avec moins de 15 réponses valides, le verdict est « non concluant ».
- Le nom du cabinet n'entre jamais dans les questions de mesure. La correspondance se fait après, sur les réponses déjà produites.
- Chaque extrait cité par le modèle est recherché mot pour mot dans la page. Absent, il est jeté.
- Volume, CPC, difficulté et position restent vides.
- Une liste de 13 requêtes reste à 13.
- Dans l'email, une phrase sans preuve est réécrite seule. Les mots « invisible », « jamais », « vous perdez » et toute mention de position ou de trafic sont refusés.
- Plusieurs avocats d'un même cabinet donnent un seul prospect.
- Chaque appel réserve son coût avant de partir. Un modèle sans tarif connu suspend la campagne.

Je garde trois décisions : l'approbation du brouillon, les cas ambigus, l'audit d'un cabinet déjà cité par l'IA ([[concepts/dette-cognitive]]).

## Essai réel du 1er octobre 2026

Commande : droit du travail, Lyon, clientèle entreprise, 2 prospects avec email prêt, 2 tours de découverte au plus.

| Mesure | Résultat |
|---|---|
| Cabinets trouvés | 5 |
| Prêt à relire | 1, renvoyé en revue le soir même après durcissement du contrôle de l'email |
| En revue humaine | 4 |
| Réponses de mesure valides | 15 sur 15, après 2 erreurs relancées |
| Requêtes retenues pour le cabinet prêt | 20 |
| Pages auditées | 20 |
| Coût engagé | 4,23 $ |
| dont mesure de présence | 2,71 $ pour 17 appels |
| dont qualification | 0,74 $ pour 5 cabinets |
| dont découverte | 0,53 $ pour 2 tours |
| Statut final | « Objectif non atteint : nombre maximal de tours de découverte atteint (2). Cible 2, atteints 1, 4 en attente de revue humaine. » |

Les 4 revues : 2 sites qui ne disent pas à qui ils s'adressent, 1 coupure réseau pendant la qualification, 1 cabinet cité par Claude sans que l'avocat soit nommé.

Une question de mesure coûte 0,16 $ en moyenne. Les 15 réponses servent à tous les cabinets d'un même segment (pratique, clientèle, ville) : leur coût se divise par le nombre de cabinets testés.

## Défauts relevés pendant l'essai

Le premier brouillon écrivait « j'ai regardé comment le site se positionne » sur deux requêtes. Aucune position n'est mesurée. Le contrôle l'avait laissé passer, il le refuse depuis.

Le brouillon a évité la phrase « non observé dans les 15 réponses » et a écrit « je peux vous indiquer quels cabinets y sont cités ». Le contrôle l'acceptait. Depuis, le code écrit lui-même le constat (nombre, date, mode) et refuse un email où il manque.

Une coupure réseau était classée « erreur inconnue », donc sans relance. Elle est retentée depuis, 3 essais au plus.

Un prospect est resté bloqué après un redémarrage du worker : l'ancien process tenait encore son verrou. Le job est maintenant reprogrammé.

Deux cabinets sont partis en revue pour « clientèle non établie ». Leurs sites la donnent : « pour une clientèle d'entreprises et de dirigeants » pour l'un, « nous intervenons majoritairement auprès des employeurs » pour l'autre. L'extraction les a ratés. La cause n'est pas connue : les extraits écartés n'étaient pas journalisés, ils le sont depuis.

Après l'arrêt du worker en plein appel, 0,29 $ sont restés réservés. Ils passent en « non confirmé » et restent comptés. Sur 4,23 $ engagés, 2,92 $ sont recalculés depuis l'usage rapporté et 1,31 $ ont une issue inconnue.

Les recherches remontent surtout des annuaires (justifit, juritravail, barreau). L'agent les écarte et garde les sites de cabinets : 5 sur deux tours.

## Relance du 2 octobre 2026

J'ai relancé les dossiers en revue après correction du code.

| Cabinet | Avant | Après |
|---|---|---|
| 1 | brouillon refusé (position inventée) | prêt à relire |
| 2 | clientèle non établie | prêt à relire, 20 requêtes |
| 3 | clientèle non établie | prêt à relire, 0 requête : aucune prestation avec page dédiée relevée |
| 4 | coupure réseau | archivé : Claude le cite déjà |
| 5 | cabinet cité sans l'avocat | toujours en revue |

Statut : « Objectif atteint : 3 / 2. » Engagé : 5,62 $, dont 3,83 $ recalculés depuis l'usage rapporté et 1,79 $ d'issue inconnue.

À la première lecture, le modèle avait rendu zéro clientèle et zéro prestation pour un site qui écrit « auprès des employeurs » en page d'accueil. L'extraction tourne depuis à effort élevé.

Un objet de 81 caractères et un email de 89 mots partaient en revue sans correction possible. Le brouillon est maintenant rédigé à nouveau avec la liste des défauts, deux fois au plus.

## Claude par API, ChatGPT à la main

La mesure automatique passe par l'API Claude avec recherche web. Elle ne dit rien de ChatGPT.

Pour ChatGPT, je pose moi-même les 5 questions dans ChatGPT et je colle les réponses dans l'écran « Saisir des réponses de ChatGPT » de la campagne. L'agent recalcule les verdicts sur ces réponses et rédige à nouveau les emails. L'email ne nomme ChatGPT que dans ce cas.

L'email suit mon message type du 2 octobre 2026. Le texte est fixe, le code y place le nom du cabinet, la pratique relevée sur son site, la ville, le nombre de réponses, l'IA interrogée, deux requêtes et le nombre de pages du pré-audit. Aucun appel au modèle pour la rédaction.

Constat : « Premier constat : sur 5 recherches effectuées dans ChatGPT pour trouver un cabinet accompagnant les entreprises et dirigeants, [cabinet] n'a été cité aucune fois. »

## Mesure par un modèle d'OpenAI, sans moi

Aucune clé OpenAI sur ma machine. L'agent passe par Codex, l'outil en ligne de commande d'OpenAI connecté à mon compte ChatGPT : un modèle d'OpenAI (gpt-6-astra) avec recherche web, sans coût à l'appel. Ce n'est pas l'interface ChatGPT. L'email écrit « un modèle d'OpenAI, l'éditeur de ChatGPT ».

Essai du 2 octobre sur les 5 cabinets, 5 questions, 5 réponses valides :

- 2 cabinets cités par le modèle d'OpenAI sont archivés. L'un d'eux n'apparaissait dans aucune des 15 réponses de Claude.
- 2 cabinets non cités ont un email prêt à relire.
- 1 cabinet reste en revue : cité sans que l'avocat soit nommé.

## Deux requêtes vérifiées par cabinet

L'agent choisit deux requêtes : intention business, puis spécialité et clientèle visées, ville, deux groupes différents. Il pose chacune telle quelle à l'IA et cherche le site et le nom du cabinet dans la réponse. L'email écrit « votre site est cité » ou « votre site n'est pas cité » d'après ce relevé. Sans relevé valide, la ligne ne dit rien.

Sur l'essai, un cabinet absent des 5 réponses générales est cité sur l'une de ses deux requêtes. L'email le dit.

## En service depuis le 2 octobre 2026

Objectif : des contrats de prestation SEO signés avec des avocats spécialisés.

L'agent tourne par launchd. En semaine, il envoie 10 emails par Resend, de tim@organikk.co, entre 9 h et 17 h (Paris). Il approuve seul les emails au contrôle factuel vert. Les réponses arrivent sur ma boîte Gmail. Il m'envoie un rapport à 18 h.

Découverte et analyse passent par `claude -p` sur mon forfait Max, la mesure par Codex.

Cibles en rotation : immobilier et construction, droit du travail, URSSAF, dommage corporel, à Lyon.

Détail et prochaines étapes : `~/Code/prospection/agent-avocats/ROADMAP.md`.

## Incidents du 2 octobre 2026

Postgres ne démarrait pas sous launchd : « postmaster became multithreaded during startup », faute de locale. Le worker tournait en boucle sur ECONNREFUSED. Corrigé par `LC_ALL` dans `scripts/service.sh` (commit 8bc46ef).

La campagne du matin (immobilier et construction) est bloquée : `claude -p` a répondu « Not logged in ». Testé à 13 h sous launchd : il répond. Elle reste bloquée, 7 prospects prêts dedans, parce qu'une seule campagne de mission tourne à la fois.

Un envoi (Equipage avocats) a échoué sur une erreur DNS chez Resend et n'était jamais retenté. L'agent retente désormais les échecs réseau, jamais les refus de Resend.

## Message type v3 et réglages du 2 octobre 2026 (après-midi)

Texte de Tim, mot pour mot, avec les 5 requêtes testées entre parenthèses (`src/prompts/email-template.ts`). Il part seulement si : segment entreprise, mesure par Codex ou relevé ChatGPT, cabinet absent des réponses, chacune des 5 questions couverte par une réponse valide, pré-audit préparé.

Conséquence : les missions ne ciblent plus que droit du travail et URSSAF. Immobilier-construction (clientèle mixte) et dommage corporel (particuliers) rendent la phrase « cabinets qui accompagnent les entreprises et dirigeants » fausse.

Réglages : 20 envois par jour, 15 min d'écart, 10 villes (Lyon, Paris, Marseille, Toulouse, Bordeaux, Lille, Nantes, Strasbourg, Montpellier, Rennes).

Blocage trouvé : dix verrous tenus épuisaient le pool de connexions, plus rien n'avançait après 13 h 34. Les verrous ont désormais leur pool (commit 9a4c328).

Adresses : celle du cabinet dans ses mentions légales, ou sur un second domaine au même nom, n'est plus écartée (2 récupérées sur 6).

## Adresses nominatives seulement (12 octobre 2026)

Règle de Tim du 9 octobre : « adresse professionnelle nominative, interdit juste contact + nom cabinet ».

Avant la correction : 250 emails envoyés, dont 107 à contact@ et 34 à cabinet@, avocats@, info@, accueil@ ou secretariat@. Aucune réponse.

Une adresse part seulement si sa partie locale porte le nom ou le prénom d'un avocat connu du cabinet, sans mot de boîte partagée. Sans avocat reconnu, elle est refusée. Le contrôle s'applique à la sélection, à l'approbation, à l'envoi, à la relance et au calcul du stock (commit 92d79e1). L'adresse de l'avocat visé passe avant celles de ses confrères. Les adresses sourcées hors site (barreau, inventaire) restent candidates.

Le contrôle de doublon comptait l'inventaire DRAFT du 10 octobre comme un suivi en cours : 59 des 100 prioritaires étaient rejetés à tort. Un inventaire jamais lancé ne compte plus.

Les 100 prioritaires du 10 octobre tournent en 18 campagnes, une par ville (Paris 51, Lyon 13, Nantes 8…), mesure Codex, sans découverte. 35 restent écartés comme doublons réels : 28 cabinets déjà cités par l'IA lors d'une mission précédente, 7 en revue ou prêts ailleurs.

Le 12 octobre au matin, 9 envois sur 11 ont échoué en « Unable to fetch data. The request could not be resolved ». Cause : Node 22 abandonne chaque tentative IPv6/IPv4 après 250 ms. Délai porté à 2 s dans `scripts/service.sh` (commit dbcb5e6). Deux emails sont partis avant la correction, dont un à contact@berenguer-avocat.fr.

À 10 h 05, l'inventaire nominatif de 131 cabinets est lancé de la même façon (33 campagnes). 59 cabinets figurent dans les deux lots : les deux campagnes se sont rejetées mutuellement comme doublons. Les 59 sont gardés dans le lot des 100 prioritaires et écartés de l'inventaire, qui garde 71 cabinets à analyser. Le contrôle de doublon ne tranche pas entre deux campagnes lancées en même temps sur le même cabinet : il les rejette toutes les deux.

## État des envois au 22 octobre 2026

Le relevé local de Courrier du 22 octobre à 12:00:46 UTC contient 512 lignes d'envoi avec une date de premier envoi et un identifiant fournisseur. Le code de l'agent utilise Resend pour ces envois. Ce constat corrige les deux points obsolètes ci-dessous : Resend a bien été utilisé pour la prospection, et des emails sont partis. La politique actuelle de Resend exclut toutefois explicitement la prospection non sollicitée ; le constat historique ne vaut pas autorisation d'usage futur. Voir [[projets/courrier/lot-50-avocats]].

## À trancher

- L'ancien plan « brouillon Gmail envoyé à la main » était une piste du 2 octobre, dépassée par les envois Resend constatés ci-dessus. Choisir le transport des prochains messages en tenant compte des conditions du fournisseur.
- [MATIÈRE MANQUANTE] Taux de réponse : à calculer depuis les réponses réellement relevées.
- [MATIÈRE MANQUANTE] Rendement de la découverte au-delà de 2 tours.

## Lancer

```bash
cd ~/Code/prospection/agent-avocats
npm run db:start
npm run build && npm start     # http://localhost:3456
npm run worker                 # second terminal
```

Le mode simulation tourne sans clé : cabinets, sites et réponses fictifs, coût nul.
