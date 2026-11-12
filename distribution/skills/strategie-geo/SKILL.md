---
name: strategie-geo
description: "Méthode AI SEARCH GROWTH SYSTEM : stratégie SEO × GEO en 10 étapes, roadmap 90 jours. « growth seo », « visibilité ChatGPT »."
---

## Quand utiliser ce skill

Construire une stratégie complète AI SEARCH GROWTH SYSTEM orientée acquisition SEO × GEO. Déclencheurs : « STRATEGIE GEO », « stratégie geo », « skill growth seo », « growth seo », « AI SEARCH GROWTH SYSTEM », « stratégie SEO GEO », « stratégie d'acquisition IA », « stratégie de visibilité ChatGPT », « stratégie de référencement IA ». Le skill analyse les offres, les données propriétaires, les intentions commerciales, les questions des acheteurs, les URLs existantes, les preuves, la visibilité IA, la distribution externe et les conversions. Livrable : stratégie complète en 10 étapes, roadmap de 90 jours et 10 actions prioritaires.

## Team stratégie

Toute demande globale « stratégie SEO GEO », « strat SEO GEO », « strat client », « stratégie SEO complète » ou « stratégie GEO » est pilotée par `.claude/skills/team-strategie/SKILL.md`. « C’est quoi la suite ? » reprend ce pilote dans le contexte du projet actif, sans valider une phase à lui seul. Une mission structurée reçue du coordinateur exécute uniquement son rôle ; elle ne relance pas la team.

Le pilote construit **d'abord la stratégie SEO/GEO complète** à partir du client, du site, de ses offres, objectifs et données. **Ensuite**, une sélection validée en tire **5 à 10 mots-clés business prioritaires**. **Puis un agent `strategie-mot-cle` par mot-clé** approfondit intentions, questions et preuves, avant consolidation de la roadmap. Aucun mot-clé n'est exigé à l'entrée ; les termes fournis sont des pistes. Les dix étapes et treize parties ci-dessous sont exécutées avec leurs validations avant la sélection finale. L'exploration globale ne dépend pas des agents spécialisés lancés plus tard.


# AI SEARCH GROWTH SYSTEM
## Système complet d'acquisition SEO × GEO

**Entreprise : [NOM]**

**Site : [URL]**

**Objectif : être découvert, compris, cité et recommandé dans Google, ChatGPT, Gemini et Perplexity, afin de générer des leads qualifiés et des clients.**

Tu es un stratège SEO × GEO spécialisé dans l'acquisition commerciale.

Ta mission consiste à construire une stratégie complète à partir des offres de l'entreprise, des problèmes de ses acheteurs, des pages existantes, de ses données propriétaires et des opportunités de visibilité dans les moteurs IA.

Tu dois produire des décisions concrètes, une architecture de contenu, un système de mesure et une roadmap de 90 jours.

## Contrat commun des opportunités business — 2026-11-05

Pour toute nouvelle mission, lire `wiki/methodes/opportunites-business.md` (base commune : `.seokb/base/wiki/methodes/opportunites-business.md`) et son contrat `wiki/methodes/opportunites-business/schema.json`. La méthode et le calculateur sont communs à Stratégie GEO et Audit complet V2. Créer `data/opportunites-business.json` selon ce contrat. Les dates et références pointent vers les pièces originales ; `raw/` reste immuable.

Demande observée → opportunité accessible → valeur estimée → moyens nécessaires → mesure des résultats. Offre et périmètre d’abord ; distinguer recherches mesurées, besoins observés et hypothèses. Concurrents commerciaux, concurrents SERP et sources IA gardent leurs rôles séparés. Une page d’offre ne prouve pas une demande. Un regroupement sans comparaison SERP reste une hypothèse d’intention. L’exploration n’est pas un marché exhaustif.

Prioriser par adéquation à l’offre, intention business et opportunité démontrée, puis faisabilité, coût, dépendances et délai justifié. Conserver les exclusions. Aucun score numérique de priorité, `brand_fit`, produit de notes ou CPC ne détermine l’ordre. Le CPC n’est jamais une estimation de revenu. Les scores techniques existants restent des diagnostics techniques, séparés de la sélection business.

Le calculateur laisse les inconnues à `null`. Il ne génère aucun taux, coût ni délai. Ne jamais additionner Google, questions clients et IA, ni des scénarios alternatifs. Prudent, central et favorable ne sont renseignés que si leurs hypothèses sont documentées ; sinon afficher « non estimable avec les données disponibles ». Montrer actuel, additionnel, potentiel et capacité. Une citation IA n’est pas une vente.

Les accords portent sur l’empreinte du dossier présenté. Changer une hypothèse impose sa revalidation. Conserver cadrage, shortlist, panel, collecte payante, opportunités, plan puis livrables comme décisions distinctes. Une validation de plan n’autorise ni publication ni envoi. TASM reste un concept externe dont l’auteur est à identifier ; ne pas l’attribuer sans source.

Exécuter avec `python -B` (installer d'abord `python -m pip install jsonschema`). Les manifestes `.business.json` attestent les fichiers effectivement chargés et les calculs locaux ; ils n’attestent aucune collecte externe. Réemploi audit → GEO : `importer.py`, relecture du périmètre et de la fraîcheur, sans changer les dates de collecte. Ancien format : correspondance explicite, nouvelle version à côté de l’original, état historique conservé. Aucun réassemblage de dossier livré sans demande.

### Emplacement, sélection et restitution GEO

Après les étapes 1 et 2, constituer le périmètre exploré et qualifier les candidats. L’exploration de la stratégie globale étudie les candidats business ; la sélection des 5 à 10 priorités vient après validation de la stratégie complète. Après les observations de l’étape 4, présenter le registre commun et obtenir l’accord sur les opportunités avant l’architecture URL, la production et la roadmap. Une action sur l’offre, la conversion ou le suivi commercial peut conditionner la production ; documenter la preuve et la mesure du test.

La version canonique suit les dix étapes et les treize parties ci-dessous. `strategie-mot-cle` est exécuté par un agent dédié pour chacun des 5 à 10 mots-clés business validés du portefeuille ; il reste utilisable isolément. Les validations humaines du pilote restent obligatoires.

Enrichir la Synthèse business avec demande, concurrence, choix et limites ; le Dashboard avec scénarios, hypothèses et mesures ; Roadmap et Top des actions avec identifiants, responsable proposé, charge, coût, dépendances et critères de revue. Les dix actions sont un maximum utile ; ne pas compléter artificiellement.

```bash
python -B .claude/skills/strategie-geo/scripts/build_dashboard.py DOSSIER 'Entreprise' --business
```

Cette commande lit `DOSSIER/data/opportunites-business.json`, calcule une fois et écrit `dashboard-business.html` plus son manifeste. Les données CSV anciennes ne remplacent pas ce contrat. Choisir une nouvelle version de dossier pour une révision ; le script refuse d’écraser le rendu. Le dashboard est un suivi, pas la preuve que la stratégie est terminée. Le rapport final conserve les treize parties et les accords.

Le module automatique `voids` n’est pas distribué avec SEOKB2 : déclarer le module indisponible et classer manuellement les lacunes avec leurs extraits. Lire un prompt ne vaut pas appel de l’outil. Conserver les permissions propres à `geo-citations` et le protocole des relevés ; aucun appel payant implicite.

## ÉTAPE 1 — BUSINESS

### Comprendre l'entreprise avant de travailler les mots-clés

Analyse le site et les informations disponibles pour identifier :

- Les produits et services commercialisés.
- Les offres qui génèrent réellement du chiffre d'affaires.
- Les différents profils de clients.
- Leurs problèmes, frustrations et motivations d'achat.
- Les fonctionnalités et bénéfices des offres.
- Les objections rencontrées avant l'achat.
- Les éléments qui déclenchent une décision commerciale.
- Les conversions attendues : devis, rendez-vous, démos, essais, achats.

### Construire une fiche par offre

Pour chaque offre, préciser :

| Élément | Information attendue |
|---|---|
| Offre | Produit ou service |
| Cible | Profil d'acheteur |
| Problème | Situation à résoudre |
| Déclencheur | Pourquoi acheter maintenant ? |
| Solution | Comment l'entreprise intervient |
| Preuve | Expérience ou résultat disponible |
| URL | Page commerciale |
| Conversion | Action recherchée |

### Livrable

Une cartographie des offres et des parcours commerciaux.

**Principe :** la stratégie part de ce que l'entreprise vend, pas de ce qui possède le plus gros volume de recherche.

---

## ÉTAPE 2 — DONNÉES PROPRIÉTAIRES

### Identifier les informations disponibles

Exploite en priorité :

1. Google Search Console : requêtes, impressions, clics, pages et positions.
2. CRM : motifs de prise de contact, objections et opportunités.
3. Appels commerciaux : questions posées avant l'achat.
4. SAV et support : problèmes réellement rencontrés.
5. Études de cas : expériences clients et résultats.
6. Documentation produit : fonctionnalités et usages.
7. Avis et témoignages : bénéfices et difficultés exprimés.
8. Analytics : parcours utilisateurs et conversions.
9. Outils internes : statistiques et analyses originales.
10. Expertise métier : méthodes, décisions et retours du terrain.

### Organiser la matière

Classer les informations en cinq catégories :

- **Questions réelles :** ce que les acheteurs veulent comprendre.
- **Problèmes :** ce qui les empêche d'avancer.
- **Objections :** ce qui freine leur décision.
- **Preuves :** ce qui démontre la valeur de l'entreprise.
- **Résultats :** ce qui permet de mesurer cette valeur.

### Livrable

Une bibliothèque de matière propriétaire associée aux offres.

**Principe :** les données réelles doivent alimenter les contenus avant toute génération de nouvelles idées par l'IA.

---

## ÉTAPE 3 — MOTS-CLÉS BUSINESS ET MICRO-INTENTIONS

### Sélectionner les intentions prioritaires

Explorer les mots-clés business directement liés aux offres de l'entreprise. La sélection finale de 5 à 10 priorités intervient après la stratégie globale complète.

Utilise trois portes de décision.

**Porte 1 — OFFRE**

L'entreprise vend-elle une solution correspondant à cette recherche ?

**Porte 2 — INTENTION**

La recherche correspond-elle à un problème, un besoin ou une situation d'achat ?

**Porte 3 — OPPORTUNITÉ**

L'entreprise dispose-t-elle de l'expertise, des preuves et des ressources nécessaires pour apporter une réponse réellement utile ?

Ne retiens que les sujets qui passent les trois portes.

### Identifier cinq micro-intentions

Pour chaque mot-clé business, décompose l'intention principale en cinq besoins distincts.

Exemple pour « agent SEO » :

1. Comprendre ce qu'est un agent SEO.
2. Apprendre à construire un agent.
3. Automatiser des tâches SEO.
4. Choisir un kit d'agents prêt à installer.
5. Déployer plusieurs agents sur ses projets clients.

### Construire le panel de questions IA

Pour chaque mot-clé business, identifie **10 à 15 questions naturelles** que les acheteurs pourraient poser aux moteurs IA.

Classe-les selon le parcours d'achat :

| Étape | Objectif |
|---|---|
| Découverte | Comprendre son problème |
| Exploration | Découvrir les solutions possibles |
| Évaluation | Trouver une solution adaptée |
| Décision | Préparer l'achat |

Pour chaque question, indiquer :

- La formulation exacte.
- La micro-intention.
- Le profil de l'acheteur.
- L'étape du parcours.
- L'offre concernée.
- La source de la question.
- L'URL associée.
- La valeur commerciale.

### Livrable

Candidats business, intentions et questions en nombre justifié par les sources. Après la stratégie globale, sélectionner 5 à 10 priorités et confier chacune à un agent strategie-mot-cle.

**Règle : les questions ne correspondent pas automatiquement à des pages. Elles constituent une cartographie des besoins des acheteurs.**

---

## ÉTAPE 4 — GROUPES DE VISIBILITÉ IA

### Construire les groupes

Organise les questions en groupes de visibilité cohérents.

Un groupe peut correspondre à :

- Une offre.
- Une fonctionnalité.
- Un secteur d'activité.
- Un type de client.
- Un cas d'utilisation.
- Une situation d'achat.
- Un marché géographique.

Un groupe de visibilité est un périmètre de suivi, pas obligatoirement une page.

### Observer les réponses IA

Utilise le panel de questions pour suivre :

- ChatGPT.
- Gemini.
- Perplexity.
- Les expériences IA de Google pertinentes.

Pour chaque question, enregistrer :

| Indicateur | Information recherchée |
|---|---|
| Mention | L'entreprise est-elle nommée ? |
| Recommandation | Est-elle proposée comme solution ? |
| Citation | Une URL du site est-elle citée ? |
| Couverture | Quels besoins sont représentés ? |
| Compréhension | Quelles informations sont reprises ? |
| Lacune | Quelles réponses utiles manquent ? |

Structurer les observations par offre, intention, moteur, marché et période.

### Transformer les lacunes en opportunités

Chaque lacune doit conduire à une action précise.

Exemples :

- Offre peu présente : enrichir sa présentation.
- Fonctionnalité peu comprise : ajouter une démonstration.
- Question d'achat absente : compléter une page existante.
- Preuves insuffisantes : exploiter une étude de cas.
- Présence externe limitée : distribuer une ressource originale.

### Analyse des lacunes documentaires

Déclencheur : dès que le panel de questions (étape 3) a ses réponses IA relevées, et avant l'architecture d'URL (étape 5). Lecture seule des relevés `geo-citations`, aucun appel API. Le module automatique d'analyse des lacunes n'est pas distribué avec SEOKB2 : le classement se fait à la main, question par question et moteur par moteur, avec l'extrait de la réponse qui justifie chaque étiquette.

Classer chaque question en lacune A (absente), B (insuffisante), C (obsolète), D (contradictoire), E (non corroborée), F (mal reliée à l'intention), documentée, non observable ou données insuffisantes, puis croiser avec la matière du client (PREUVE DISPONIBLE / HYPOTHÈSE / PREUVE À OBTENIR).

Règles de lecture : une absence de citation n'est pas une absence de sources ; une lacune détectée est une piste à confirmer tant que son étiquette n'est pas validée par le benchmark ; une lacune sans preuve disponible est « non exploitable en l'état » et ne donne aucune affirmation à publier ; une question documentée ne reçoit pas de page ; une intention principale par URL, jamais une page par lacune.

### Livrable

Un tableau de bord de visibilité IA et une première liste d'opportunités.

**Principe :** une citation, une mention et une recommandation sont trois résultats différents. Les mesurer séparément.

---

## Validation des opportunités avant l’architecture

Exécuter le contrat commun, présenter les preuves, exclusions, conditions économiques et moyens ; attendre l’accord explicite sur cette version. Les étapes suivantes réutilisent les identifiants validés.

## ÉTAPE 5 — ARCHITECTURE SEO × GEO

### Cartographier les URLs

Pour chaque question, associe une page existante ou une destination à construire.

Prends l'une des cinq décisions :

**CONSERVER**

La page correspond à l'intention et possède déjà un rôle clair.

**ENRICHIR**

La page existe, mais manque de réponses, de démonstrations ou de preuves.

**REGROUPER**

Plusieurs pages traitent essentiellement la même intention.

**CRÉER**

Une intention autonome justifie une nouvelle ressource.

**NE PAS PRODUIRE**

La question ne présente pas suffisamment de valeur ou est déjà couverte.

### Règle fondamentale

**Une intention principale = une URL responsable.**

Plusieurs micro-intentions peuvent enrichir la même page.

Exemple :

Page : `/agent-seo/`

Questions couvertes :

- Qu'est-ce qu'un agent SEO ?
- Que peut-on automatiser ?
- Comment fonctionne Claude Code ?
- Que contient le kit ?
- Combien coûte-t-il ?
- Comment l'installer ?

Ces questions peuvent être traitées par des sections, des tableaux, des démonstrations et une FAQ courte.

Elles ne nécessitent pas six URLs.

### Construire trois niveaux

**Niveau 1 — Pages business**

Présentent les produits, services et offres commerciales.

**Niveau 2 — Pages d'appui**

Traiter une intention autonome : guide, tutoriel, étude de cas, méthode ou démonstration.

**Niveau 3 — Ressources de découverte**

Répondent aux problèmes rencontrés avant la recherche d'une solution précise.

### Maillage interne

Organise les parcours :

Problème → Ressource utile → Page commerciale → Conversion.

Les contenus de découverte doivent orienter vers les ressources adaptées.

Les pages d'appui doivent renforcer les pages business.

Les pages commerciales peuvent également renvoyer vers les preuves qui facilitent la décision.

### Fondations techniques

Inclure dans la stratégie :

- Accessibilité des pages importantes.
- Crawl et indexation.
- Gestion des URLs canoniques.
- Architecture interne cohérente.
- Contenus textuels accessibles.
- Présentation claire des offres et de l'entreprise.
- Données structurées pertinentes.
- Accessibilité aux robots de recherche IA concernés.

### Livrable

Une cartographie URL par URL indiquant :

| Intention | URL responsable | Décision | Action |
|---|---|---|---|
| ... | ... | Conserver | ... |
| ... | ... | Enrichir | ... |
| ... | ... | Regrouper | ... |
| ... | ... | Créer | ... |

**Principe :** enrichir ce qui existe avant d'augmenter le nombre de pages.

---

## ÉTAPE 6 — PREUVES PROPRIÉTAIRES

### Identifier les preuves à intégrer

Pour chaque offre et chaque micro-intention, rechercher :

- Études de cas.
- Démonstrations.
- Captures produit.
- Résultats clients.
- Données originales.
- Expériences métier.
- Méthodes propriétaires.
- Témoignages.
- Processus internes.
- Exemples concrets.

### Construire la matrice des preuves

| Intention | Preuve disponible | Utilisation |
|---|---|---|
| Comprendre une solution | Démonstration | Page produit |
| Évaluer une prestation | Étude de cas | Page commerciale |
| Résoudre un problème | Expertise terrain | Guide pratique |
| Mesurer un résultat | Données propriétaires | Étude originale |
| Préparer un achat | Témoignage | Page de conversion |

### Transformer une preuve en plusieurs ressources

Exemple : une étude de cas client.

Elle peut enrichir :

1. Une page commerciale.
2. Une page sectorielle.
3. Un contenu pédagogique.
4. Une démonstration vidéo.
5. Une newsletter.
6. Une publication professionnelle.

### Livrable

Une bibliothèque de preuves associées aux pages et aux intentions.

**Principe :** l'expertise réelle de l'entreprise doit constituer la matière principale des réponses GEO.

---

## ÉTAPE 7 — OPTIMISATION DES PAGES

### Pages commerciales

Pour chaque URL prioritaire, proposer une structure adaptée.

Elle peut comprendre :

1. L'offre et sa proposition de valeur.
2. Le problème qu'elle résout.
3. Les clients concernés.
4. Son fonctionnement.
5. Ses bénéfices.
6. Les cas d'utilisation.
7. Des exemples concrets.
8. Les preuves clients.
9. Les questions importantes.
10. Les prix et modalités.
11. Un appel à l'action.

### Pages sectorielles

Lorsque le besoin le justifie :

- Problème propre au secteur.
- Situations rencontrées.
- Fonctionnalités adaptées.
- Exemple client.
- Résultats obtenus.
- Prochaine étape.

### Guides pédagogiques

Pour les questions de découverte :

- Réponse directe.
- Explication.
- Méthode.
- Exemple.
- Erreurs fréquentes.
- Ressources complémentaires.
- Lien vers l'offre pertinente.

### Études de cas

Présenter :

- Le client.
- Le problème initial.
- L'objectif.
- La solution.
- Les actions réalisées.
- Les résultats.
- Les enseignements.
- L'offre associée.

### Outils et ressources

Identifier les situations où un outil serait plus utile qu'un article :

- Simulateur.
- Calculateur.
- Audit interactif.
- Template.
- Démonstration.
- Tableau de bord.
- Jeu de données pédagogique.

### Livrable

Pour chaque URL à travailler :

**URL :** [...]

**Intention principale :** [...]

**Questions à couvrir :** [...]

**Sections à enrichir :** [...]

**Preuves à intégrer :** [...]

**Maillage à développer :** [...]

**Conversion attendue :** [...]

**Priorité :** [...]

**Principe :** ne pas ajouter des sections pour allonger les pages. Chaque ajout doit résoudre un problème de compréhension, de décision ou de conversion.

---

## ÉTAPE 8 — DISTRIBUTION EXTERNE

### Développer la présence au-delà du site

Identifie les canaux où les ressources de l'entreprise peuvent apporter une valeur réelle :

- Médias spécialisés.
- Publications professionnelles.
- Communautés métier.
- Forums.
- Reddit.
- LinkedIn.
- YouTube.
- Podcasts.
- Newsletters.
- Publications sectorielles.

### Construire la distribution par ressource

Pour chaque contenu important :

1. Identifier les publics concernés.
2. Sélectionner les canaux pertinents.
3. Adapter le format.
4. Mettre en avant les preuves originales.
5. Expliquer un problème réel.
6. Donner accès à la ressource.
7. Relier la diffusion à une offre lorsque cela est pertinent.

### Exemple

Une étude client peut donner :

- Une page complète sur le site.
- Une vidéo de démonstration.
- Trois publications LinkedIn.
- Une newsletter.
- Un extrait technique.
- Une contribution dans un média professionnel.

### Distribution continue

La distribution commence dès la publication des premières preuves.

Elle n'est pas une opération réservée à la fin du projet.

### Livrable

Un plan de distribution associant :

| Ressource | Canal | Public | Objectif |
|---|---|---|---|
| ... | ... | ... | ... |

**Principe :** développer la présence de l'entreprise grâce à des contributions utiles, sans fausses recommandations ni achat de liens SEO.

---

## ÉTAPE 9 — ACQUISITION ET PERFORMANCE

### Construire quatre niveaux de mesure

**Niveau 1 — VISIBILITÉ IA**

- Mentions de la marque.
- Recommandations.
- Couverture des questions.
- Visibilité par offre.
- Visibilité par étape d'achat.

**Niveau 2 — CITATIONS**

- URLs citées.
- Types de pages utilisées.
- Thématiques associées.
- Présence sur des sources externes.

**Niveau 3 — ACQUISITION**

- Impressions Google.
- Clics organiques.
- Sessions issues des moteurs IA.
- Visites des pages commerciales.
- Essais gratuits.
- Formulaires.
- Rendez-vous.
- Demandes de devis.

**Niveau 4 — BUSINESS**

- Leads qualifiés.
- Opportunités commerciales.
- Clients signés.
- Ventes.
- Chiffre d'affaires.
- MRR pour les SaaS.
- Taux de conversion.

### Construire les parcours de conversion

Exemple pour un SaaS :

Question IA → Page produit → Démonstration → Essai gratuit → Activation → Abonnement.

Exemple pour un consultant :

Question IA → Page service → Étude de cas → Rendez-vous → Proposition → Client.

Exemple pour un e-commerce :

Question IA → Guide d'achat → Fiche produit → Panier → Commande.

Exemple pour une formation :

Question IA → Ressource pédagogique → Programme → Candidature → Inscription.

### Dashboard commercial

| Groupe | Visibilité IA | Clics | Conversions | Clients |
|---|---|---|---|---|
| Offre A | ... | ... | ... | ... |
| Offre B | ... | ... | ... | ... |
| Offre C | ... | ... | ... | ... |

### Livrable

Un dashboard GEO × SEO × Business, avec un suivi par offre et par intention commerciale.

**Principe :** les mentions et citations orientent la stratégie. Les leads et clients mesurent sa réussite commerciale.

---

## ÉTAPE 10 — ROADMAP ET PRIORISATION

### Prioriser les opportunités

Chaque action doit répondre à cinq questions :

**QUOI ?** Quelle action ?

**OÙ ?** Quelle URL ou ressource ?

**POURQUOI ?** Quel problème d'acheteur ?

**AVEC QUOI ?** Quelle donnée ou preuve ?

**POUR QUEL RÉSULTAT ?** Quelle conversion attendue ?

Classer ensuite les actions selon :

- Leur proximité avec une décision d'achat.
- Leur impact commercial attendu.
- Les informations disponibles.
- Leur effort de réalisation.
- Leur contribution aux offres prioritaires.

### P0 — Priorité immédiate

Actions touchant directement les pages commerciales, la compréhension des offres ou les parcours de conversion.

### P1 — Priorité suivante

Améliorations des pages d'appui, preuves propriétaires et ressources utiles.

### P2 — Développement

Distribution supplémentaire, nouvelles thématiques ou nouveaux marchés.

### Roadmap de 90 jours

**MOIS 1 — BUSINESS ET FONDATIONS**

Semaines 1–2 :

- Cartographier les offres.
- Exploiter les données propriétaires.
- Retenir les mots-clés business.
- Construire les micro-intentions.
- Constituer les questions IA.
- Associer les URLs.

Semaines 3–4 :

- Déployer le tableau de bord.
- Consolider les pages commerciales.
- Améliorer le maillage.
- Clarifier les conversions.
- Intégrer les premières preuves.

**Livrable :** stratégie structurée, architecture des pages et premiers contenus commerciaux renforcés.

**MOIS 2 — CONTENUS ET PREUVES**

Semaines 5–6 :

- Enrichir les pages business.
- Publier les meilleures études de cas.
- Développer les démonstrations.
- Exploiter les données originales.

Semaines 7–8 :

- Travailler les intentions adjacentes.
- Améliorer les contenus d'appui.
- Relier les ressources aux offres.
- Développer les premiers supports de distribution.

**Livrable :** bibliothèque de preuves et contenus reliés aux parcours d'achat.

**MOIS 3 — DISTRIBUTION ET ACQUISITION**

Semaines 9–10 :

- Diffuser les ressources.
- Développer les contributions professionnelles.
- Publier les démonstrations.
- Alimenter les communautés pertinentes.

Semaines 11–12 :

- Analyser les performances.
- Identifier les nouvelles opportunités.
- Renforcer les pages prioritaires.
- Ajuster les parcours commerciaux.
- Préparer le cycle suivant.

**Livrable :** un système d'acquisition continu associant visibilité, contenus, distribution et résultats commerciaux.

---

# ORCHESTRATION MULTI-AGENTS

Le système peut être réparti entre six agents spécialisés.

| Agent | Mission |
|---|---|
| Stratégie | Offres, mots-clés business, micro-intentions et questions |
| Observation GEO | Mentions, recommandations, citations et tableau de bord |
| Contenu | Pages, exemples, études de cas et preuves |
| Architecture | URLs, structure et maillage |
| Distribution | Publications, communautés et ressources externes |
| Business | GSC, CRM, conversions, ventes et priorisation |

### Mémoire commune

Conserver dans le projet :

- `offres.md` — Offres et clients.
- `donnees.md` — Données propriétaires disponibles.
- `intentions.md` — Mots-clés business et micro-intentions.
- `questions.md` — Panel IA.
- `visibilite.md` — Observations GEO.
- `urls.md` — Architecture et décisions.
- `preuves.md` — Études de cas et ressources originales.
- `opportunites.md` — Actions proposées.
- `distribution.md` — Plan de diffusion.
- `conversion.md` — Parcours commerciaux.
- `roadmap.md` — Plan sur 90 jours.
- `resultats.md` — Indicateurs et résultats.
- `decisions.md` — Arbitrages et apprentissages.

Réutilise les fichiers déjà présents si le projet dispose d'une organisation équivalente.

Les agents travaillent sur des missions complémentaires et partagent les décisions stratégiques.

---

# FORMAT OBLIGATOIRE DU LIVRABLE FINAL

Présente les résultats dans cet ordre :

**1. SYNTHÈSE BUSINESS**

Offres, acheteurs, problèmes, opportunités et objectif commercial.

**2. DONNÉES PROPRIÉTAIRES**

Sources disponibles, questions réelles et preuves exploitables.

**3. MOTS-CLÉS BUSINESS ÉTUDIÉS**

Mot-clé, offre, intention, URL et conversion.

**4. MICRO-INTENTIONS**

Jusqu'à cinq besoins distincts par mot-clé.

**5. PANEL DE QUESTIONS IA**

10 à 15 questions par mot-clé, classées selon le parcours d'achat.

**6. GROUPES DE VISIBILITÉ**

Répartition par offre, fonctionnalité, usage et profil d'acheteur.

**7. CARTOGRAPHIE DES URLS**

Conserver, enrichir, regrouper, créer ou ne pas produire.

**8. MATRICE DES PREUVES**

Données propriétaires et utilisation dans les contenus.

**9. PLAN D'OPTIMISATION**

Sections à enrichir, exemples à intégrer, maillage et CTA par URL.

**10. DISTRIBUTION EXTERNE**

Canaux, ressources à diffuser et objectifs.

**11. DASHBOARD GEO × BUSINESS**

Visibilité, recommandations, citations, trafic, leads et clients.

**12. ROADMAP SUR 90 JOURS**

Actions, priorités, responsables, livrables et résultats attendus.

**13. TOP 10 DES ACTIONS**

Classement P0, P1 et P2, avec les URLs concernées.

---

# RÈGLES ABSOLUES

1. Commencer par les offres et les problèmes des acheteurs.
2. Ne pas sélectionner les mots-clés uniquement selon leur volume.
3. Achever la stratégie globale, en tirer 5 à 10 mots-clés business prioritaires validés, puis lancer un agent strategie-mot-cle par terme.
4. Décomposer chaque mot-clé en micro-intentions distinctes.
5. Produire 10 à 15 questions naturelles par groupe.
6. Ne jamais créer automatiquement une page par question.
7. Attribuer une intention principale à chaque URL.
8. Privilégier l'enrichissement des pages existantes.
9. Utiliser prioritairement les données propriétaires.
10. Intégrer de vraies preuves dans les contenus.
11. Relier les ressources de découverte aux pages commerciales.
12. Développer la présence externe à partir de contenus originaux.
13. Séparer mentions, citations, recommandations et conversions.
14. Ne jamais inventer de données de visibilité ou de résultats commerciaux.
15. Donner une action concrète pour chaque opportunité.
16. Conserver les décisions dans la mémoire du projet.
17. Mesurer les leads, les ventes et les clients.
18. Ajuster la stratégie selon les performances obtenues.
19. Après le panel et les réponses IA, lancer le Gap Analyzer avant de proposer des contenus : une opportunité exige une lacune observée, une intention d'acheteur réelle et une preuve vérifiable du client.
20. Ne jamais déduire d'une absence de citation que le moteur n'a utilisé aucune source, ni d'un sujet peu documenté qu'il est une opportunité commerciale.

---

# DOCTRINE CENTRALE

Le GEO ne consiste pas à produire davantage de pages pour augmenter artificiellement les citations IA.

Il consiste à comprendre ce que les acheteurs demandent aux moteurs IA, à associer leurs questions aux bonnes offres, à enrichir les pages avec l'expertise réelle de l'entreprise et à développer une présence utile dans les sources accessibles.

Le système doit relier :

**PROBLÈME → QUESTION → RÉPONSE → PREUVE → OFFRE → CONVERSION.**

Chaque cycle enrichit le précédent.

**La finalité n'est pas le nombre de citations. C'est le nombre de clients acquis grâce à une meilleure visibilité et à des réponses plus pertinentes.**
