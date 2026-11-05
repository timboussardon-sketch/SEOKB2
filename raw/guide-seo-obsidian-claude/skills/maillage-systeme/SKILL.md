---
name: maillage-systeme
description: >
  Maillage interne stratégique d'un site (blog, catalogue, doc) : architecture en piliers,
  classification hub/satellite, sélection d'ancres avec diversification entrante,
  détection des pages orphelines et dead-end, audit complet du graphe interne. Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

  Complémentaire au skill maillage-interne-gsc qui exploite la donnée Search Console.
  Celui-ci raisonne sur la structure éditoriale et le contenu, sans dépendre de la GSC.
  Utilisable dès la phase de cadrage d'un nouveau site, avant qu'aucune donnée
  comportementale ne soit disponible.

  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : architecture de maillage,
  piliers de blog, hub et satellite, ancres internes, anchor text, choix d'ancre, audit
  maillage interne, orphan pages, pages dead-end, link equity, structurer le maillage
  d'un nouveau site, mailler un blog avant lancement, plan de cocon, ou uploade
  une liste d'articles/URLs et veut un plan de maillage complet.
---

# Skill : maillage interne, architecture, ancres et audit

## Ce que tu donnes à Claude

- L'URL du site (ou de son sitemap.xml) si le site est en ligne : Claude lance le script de crawl fourni dans `scripts/` et travaille sur le graphe réel.
- Sinon, la liste de tes articles : titre, slug, catégorie, extrait, mot-clé visé. Le contenu intégral (markdown ou HTML) si tu l'as.
- Tes 3 à 5 mots-clés piliers, ceux de ton métier.
- Tes pages d'offre et tes pages « Do » : outil, audit, contact, devis, démo. Ce sont elles que le maillage doit servir en premier.

## Consigne pour le lancer

> audite le maillage de monsite.fr

> voilà la liste de mes articles, construis l'architecture en piliers et le plan de liens

## Rôle

Construire et auditer le graphe de liens internes d'un site à partir du contenu existant ou planifié, sans dépendre de la Search Console. Le skill produit trois livrables : une **architecture en piliers**, un **plan d'ancres diversifiées** par lien, et un **rapport d'audit** des trous structurels.

L'objectif n'est pas de générer des liens à la chaîne. C'est de construire un graphe où chaque lien est justifié par trois signaux : topique, intention et autorité.

---

## Réflexion appliquée

- Le maillage interne est **un système, pas une passe**. Trois axes simultanés : topique, intention, autorité.
- Une ancre, ce n'est pas un mot-clé. C'est **une promesse de continuité** entre deux pages, lue par Google, par les LLM (en vecteur), et par l'humain (en désir de cliquer).
- **5 ancres possibles vers la même page = 5 ancres différentes.** Un seul exact match. Le reste est partial / sémantique / contextuel long.
- **Test à voix haute** : si la phrase tombe juste sans le lien, l'ancre est bien intégrée. Si elle clopine, l'ancre est plaquée.
- **Le maillage Know→Do passe avant le maillage Know→Know.** Une page qui explique un concept doit toujours pointer vers la page qui permet de l'exécuter (outil, audit, démo).
- **Pas de "Voir aussi" en bas d'article.** Le contexte de lien est dilué. Liens contextuels in-body uniquement.
- **Une page mère n'est pas un titre de catégorie.** C'est l'article le plus stratégique du pilier, celui qui définit le vocabulaire et reçoit le plus de liens internes.
- **Le cross-pillar pollination compte autant que le maillage intra-cluster.** 1 lien sortant sur N doit pointer vers un autre pilier pour éviter la siloïsation.

---

## Données requises

| Source | Description | Obligatoire |
|--------|-------------|-------------|
| Liste des URLs/articles | Titre, slug, catégorie, excerpt, mots-clés cibles | Oui |
| Contenu intégral (markdown ou HTML) | Pour détecter les opportunités contextuelles | Recommandé |
| Mots-clés piliers (3-5) | Le vocabulaire métier business du client | Recommandé |
| Pages "Do" identifiées | URLs des outils, audits, formulaires, simulateurs | Recommandé |

**Minimum viable** : la liste des articles avec titre + excerpt + mots-clés. Sans le contenu intégral, le skill produit l'architecture mais pas les ancres précises.

---

## Étape 0 : ingestion (site existant en ligne)

**Règle de contexte : le contenu intégral du site n'entre JAMAIS d'un bloc dans le contexte principal.** La qualité de raisonnement d'un LLM se dégrade quand la fenêtre se remplit ; charger 50+ pages HTML avant de raisonner produit un plan médiocre. Le contexte principal ne travaille que sur l'index.

Si le site est en ligne avec un sitemap, lancer le script d'ingestion AVANT toute lecture de page. Il est livré avec ce skill, dans `scripts/crawl_graph.py` :

```bash
python3 ~/.claude/skills/maillage-systeme/scripts/crawl_graph.py https://site.com/sitemap.xml -o ./maillage-data
```

Si le skill est installé ailleurs, lancer le script depuis son propre dossier : `python3 <dossier-du-skill>/scripts/crawl_graph.py ...`. Options utiles : `--limit 50` pour un premier passage sur 50 pages, `--delay 0.3` pour espacer les requêtes. Une URL de base sans `.xml` est complétée en `/sitemap.xml`.

Le script (stdlib Python 3 uniquement, zéro dépendance, zéro token) produit :

- **`index.json`** : une ligne légère par page : URL, title, H1, meta description, compteurs inbound/outbound éditoriaux, listes des orphelines et dead-ends. C'est le SEUL fichier chargé dans le contexte principal.
- **`graph.json`** : tous les liens internes avec leur ancre exacte et le paragraphe qui les porte (`passage`), marqués `in_body` (hors nav/header/footer/aside) et `sitewide` (même couple cible+ancre présent sur ≥ 80 % des pages = lien de gabarit, exclu du comptage éditorial même si le HTML n'est pas sémantique).

Les compteurs `inbound_in_body` / `outbound_in_body` de `index.json` comptent des liens, pas des pages sources. Pour le comptage par pages sources distinctes (étape 4), le recalculer depuis `graph.json`.

Répartition du travail ensuite :

1. **Étapes 1-4 et 6-7** raisonnent sur `index.json` + les compteurs de `graph.json`. Pas de lecture de contenu.
2. **Étape 5 (ancres précises)** : déléguer à des sous-agents quand l'environnement le permet. Chaque sous-agent lit 2-3 pages sources maximum, propose les passages et ancres, seul le résultat remonte au contexte principal.
3. Les ancres existantes vers une cible (pour la diversification) se lisent dans `graph.json`, jamais en re-crawlant.

Si le site n'est pas en ligne (contenu planifié, markdown local), sauter cette étape : la liste fournie par l'utilisateur fait office d'index, et la cartographie étape 4 se fait par parsing des fichiers locaux (grep des liens, pas lecture intégrale en contexte).

---

## Raisonnement de l'agent (étapes obligatoires)

L'agent DOIT suivre ces étapes **dans l'ordre** avant de répondre.

### Étape 1 : classifier chaque page en intention

Pour chaque article, déterminer son intention dominante :

| Intention | Description | Exemples de signaux |
|-----------|-------------|---------------------|
| **Know-Simple** | Définition courte, réponse directe | titre commence par "Qu'est-ce que", "C'est quoi" |
| **Know** | Guide approfondi, méthode, comparatif | titre "Comment", "Pourquoi", "Guide" |
| **Do** | Outil, simulateur, formulaire, démo | URL contient `/outils/`, `/audit`, `/contact` |

Une page peut avoir une intention dominante + une intention secondaire. Noter les deux.

### Étape 2 : identifier les piliers

Regrouper les articles par cohérence sémantique (pas par catégorie technique). **Repère interne : 3 à 5 piliers** pour un blog de taille moyenne. C'est un repère de travail, pas une condition de bonne santé SEO : un site à deux offres a deux piliers, un catalogue en a plus. Les quotas de ce skill sont tous des repères internes, jamais des conditions universelles ; Google recommande des liens utiles, contextualisés et explorables, sans nombre idéal.

Critères pour qu'un cluster forme un vrai pilier :
- Au moins 3 articles dans le cluster
- Un mot-clé business central qui revient dans tous les titres ou excerpts
- Une page-hub naturelle : l'article le plus complet ou le plus stratégique du cluster

Si un cluster a moins de 3 articles, il devient un **sous-cluster** d'un pilier existant, pas un pilier indépendant.

### Étape 3 : désigner le hub de chaque pilier

Pour chaque pilier, identifier la page-hub :
- Article le plus complet (ou prévu pour l'être)
- Recouvre les concepts secondaires des autres articles du pilier
- Idéalement : positionné sur le mot-clé pilier exact

Le hub reçoit des liens entrants depuis tous les satellites. Le hub redistribue vers les satellites via des liens contextuels (pas une liste).

### Étape 4 : cartographier les liens existants

Si l'étape 0 a tourné, cette cartographie est DÉJÀ dans `index.json` (compteurs) et `graph.json` (détail des ancres) : la lire, pas la refaire. Sinon, pour chaque article, lister :
- **Inbound links** : combien d'articles pointent vers lui ?
- **Outbound links** : vers combien d'articles pointe-t-il ?

(La profondeur de clic n'est PAS un critère : on ne la mesure pas, on ne la corrige pas.)

**Comment on compte** (un total de liens n'a pas la même signification selon l'origine et le rôle) : `graph.json` sépare déjà `in_body` et `sitewide`. Le comptage éditorial retient les liens du corps, depuis des **pages sources distinctes** (dix liens depuis une même page = une source), vers des **cibles pertinentes et accessibles** (pas une page en noindex, en redirection ou hors sujet). Les liens de navigation, pied de page et barre latérale se comptent à part et ne font ni orpheline ni hub à eux seuls. Chaque chiffre du rapport dit quel comptage il utilise.

Détecter les observations :
- **Orphan pages** : 0 lien entrant éditorial (une orpheline n'est pas critique par défaut : une page légale orpheline n'est pas un problème)
- **Dead-end pages** : 0 lien sortant éditorial
- **Hub sous-maillé** : repère interne, moins de 5 entrants depuis des satellites distincts ; à lire avec la taille du pilier, pas comme un seuil

### Étape 5 : sélectionner les ancres pour chaque lien proposé

Pour chaque lien `Source → Cible` à créer, produire **3 propositions d'ancres** classées :

1. **Exact match** (1 max par cible, sur la première mention) : reproduit le mot-clé pilier exact de la cible
2. **Partial match** (60-70% des liens entrants vers une cible) : variation autour du mot-clé pilier
3. **Sémantique étendue** : reformule la promesse de la cible sans utiliser le mot-clé

Pour chaque ancre, vérifier les 5 critères :

| Critère | Question à se poser |
|---------|---------------------|
| Promesse de la cible | L'ancre reflète-t-elle ce que l'utilisateur va trouver, pas le titre H1 ? |
| Phrase porteuse | La phrase reste-t-elle fluide à voix haute sans le lien ? |
| Diversification | Cette ancre est-elle déjà utilisée vers la même cible depuis une autre page ? |
| Position | L'ancre porte-t-elle le verbe d'action ou le substantif central, pas un mot de liaison ? |
| Link context | Les 5 mots avant/après parlent-ils du sujet de la cible ? |

Si une ancre rate un critère, la rejeter.

### Étape 6 : prioriser les liens à créer

Pas de score numérique. Une formule du type `(impressions × poids_intention) + (gain_authority × 0.4)` mélange des grandeurs sans normalisation : quelques milliers d'impressions écrasent tout le reste, et cette passe, annoncée indépendante de la GSC, en dépendrait quand même. La priorité se justifie depuis les dimensions déjà relevées, dans cet ordre, et chaque lien proposé porte sa justification écrite :

1. **La cible est une page business prioritaire** (désignée par l'utilisateur) et elle est orpheline ou sous-maillée.
2. **Le lien oriente Know → Do** vers une page qui permet d'agir (outil, audit, contact).
3. **Le lien manque entre un hub et un satellite** du même pilier (le cocon ne tourne pas sans lui).
4. **Le lien répare une orpheline ou une impasse** hors pages business.
5. **Le lien relie deux piliers** (un par pilier au moins, sur une passerelle conceptuelle réelle).

Deux liens au même rang se départagent par l'intention de la cible (Do avant Know-décisionnel avant Know avant Know-Simple), puis, **seulement si la GSC est disponible**, par l'exposition réelle de la cible (impressions). Sans GSC, cette passe reste complète : le départage s'arrête à l'intention. C'est le fonctionnement par défaut, pas un cas particulier.

### Étape 7 : vérifier les règles de conservation

Avant de finaliser le plan, valider. Les chiffres sont des repères internes de travail, pas des conditions de santé SEO : on explique un écart, on ne le corrige pas mécaniquement.
- Aucune page business orpheline restante (une page légale ou utilitaire orpheline peut le rester, en le disant)
- Aucune page business en impasse (repère : ≥ 2 liens sortants éditoriaux)
- Chaque hub reçoit des liens depuis des satellites distincts (repère : 5)
- Aucune cible ne reçoit la même ancre 2 fois
- Densité lisible (repère : 2 à 5 liens éditoriaux pour 1000 mots) ; au-delà, vérifier que chaque lien reste utile en contexte, pas retirer pour atteindre un nombre

**NE PAS répondre avant d'avoir complété chaque étape.**

---

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau.

Posture : tu es un consultant SEO senior qui transforme des données en décisions, pas un crawler qui récite ce qu'il trouve. Tu ne restitues pas toutes les anomalies : tu identifies les quelques phénomènes qui expliquent le mieux la situation du site. On doit pouvoir ouvrir le rapport et comprendre en moins de 30 secondes ce qui se passe, pourquoi, et ce qu'on fait maintenant.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque faible / moyen / élevé ; toute action à risque élevé (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist (requêtes, conversions, backlinks, intention, historique, rôle commercial de la page)
6. Ce que les données ne permettent pas de conclure (requêtes anonymisées, URL non inspectées, backlinks non analysés, conversions non disponibles), et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Repères pour remplir ces champs :

- Problème = dégrade probablement les performances ; opportunité = pourrait être amélioré.
- Confiance forte = plusieurs sources concordent (crawl, GSC, HTML) ; moyenne = signal incomplet ; faible = peu de données. Une recommandation lourde exige une confiance forte.
- Risque faible = maillage, navigation, title, Hn ; moyen = gros changement de contenu, canonical ; élevé = suppression, 301, fusion, changement massif d'URL.
- Pour prioriser, raisonne sur impact × confiance × poids business de la page ÷ effort, sans jamais afficher ce calcul. Poids business : home, pages d'offre, service et tarifs en haut ; étude de cas ensuite ; guide, puis article de blog ; page légale presque nul.

Sur le périmètre de ce skill, le rapport tranche l'architecture : orphelines et impasses pondérées par le type de page (une orpheline n'est pas critique par défaut, une page légale orpheline n'est pas un problème ; peu de trafic n'est pas un problème en soi), pages commerciales sous-liées regroupées en un seul problème avec les URL en preuves.

Règles : chaque information est typée Fait (donnée observée), Hypothèse (interprétation) ou Action (recommandation), jamais une hypothèse écrite comme un fait ; un problème existe une seule fois, les observations qui parlent du même problème fusionnent (quatre pages orphelines = un problème « pages commerciales insuffisamment intégrées au maillage ») ; une anomalie n'est pas une priorité par défaut ; une corrélation n'est pas une causalité ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé (« les données montrent », jamais « Google ne comprend pas »). Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution : aucun identifiant technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Partie détaillée du rapport : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Format de sortie OBLIGATOIRE

### Bloc 1 : architecture détectée

```
PILIER 1 : [Nom thématique] (mot-clé pilier : "...")
├── HUB : [titre article + slug]
├── Satellite : [titre + slug] (intention : Know)
├── Satellite : [titre + slug] (intention : Know)
└── Satellite : [titre + slug] (intention : Do)

PILIER 2 : [Nom]
...
```

### Bloc 2 : audit du graphe existant

Tableau :

| Article | Inbound | Outbound | Statut |
|---------|---------|----------|--------|
| ... | 3 | 4 | OK |
| ... | 0 | 2 | **ORPHELINE** |
| ... | 5 | 0 | **DEAD-END** |

### Bloc 3 : plan de liens à créer (priorisé)

Pour chaque lien proposé :

```
PRIORITÉ : HAUTE | Rang : 1 (cible business prioritaire, orpheline)
─────────────────────────────────
SOURCE     : [titre article source] (Know)
CIBLE      : [titre article cible] (Do)
PILIER     : Cross-pillar (Pilier 1 → Pilier 3)
NATURE     : Know → Do (orientation funnel)

PASSAGE PROPOSÉ :
"[Phrase complète où insérer le lien, en montrant les mots avant/après]"

ANCRES PROPOSÉES (choisir 1) :
  [exact]    "mot-clé pilier exact"
  [partial]  "variation naturelle du mot-clé"
  [sémant.]  "reformulation de la promesse cible"

JUSTIFICATION : [1 phrase sur pourquoi ce lien crée de la valeur]
```

### Bloc 4 : règles de gouvernance

Une checklist finale à suivre à chaque nouvelle publication :

- [ ] Le nouvel article reçoit des liens entrants depuis des articles existants distincts (repère : 3)
- [ ] Le nouvel article contient des liens sortants utiles vers des articles existants (repère : 3)
- [ ] Au moins 1 lien sortant pointe vers une page Do
- [ ] Au moins 1 lien sortant pointe vers un autre pilier (cross-pollination)
- [ ] Aucune ancre exacte n'est dupliquée vers la même cible
- [ ] Tous les liens sont in-body, aucun en bloc "Voir aussi"

---

## Ce que tu vérifies avant d'ajouter les liens

Claude propose, tu arbitres. Avant d'insérer un lien du plan :

- Lis le passage à voix haute sans le lien. Si la phrase boite, rejette le lien ou réécris la phrase ; ne force jamais une ancre.
- Insère par lot de 10 à 20 liens, pas les 60 d'un coup. Commence par le haut du plan.
- Relance le crawl (étape 0) après l'insertion du lot, et compare les compteurs avec le crawl précédent.
- Critère de fin de lot : zéro page d'offre orpheline. Tant qu'il en reste une, le lot suivant commence par elle.

---

## Points de vigilance

- **Ne pas tout automatiser.** Le skill propose, l'humain décide. Une ancre forcée détruit le naturel d'un texte.
- **Le contexte vaut plus que l'ancre.** Une ancre parfaite dans une phrase qui parle d'autre chose = lien faible. Réécris la phrase.
- **Le hub n'est pas figé.** Si un nouveau satellite devient plus complet que le hub historique, on bascule le hub. La structure suit le contenu, pas l'inverse.
- **Cross-pillar ≠ liens hors-sujet.** Le pont entre deux piliers doit reposer sur une vraie passerelle conceptuelle (pas "j'avais besoin d'un lien").
- **Ne jamais lier vers la home depuis le contenu.** La home a déjà tout le PageRank, elle n'en a pas besoin. Garde le jus pour les pages business.
- **Les FAQ sont une mine d'ancres.** Chaque réponse de FAQ qui mentionne un sous-sujet déjà traité doit lier. Densité haute, contexte naturel.
- **Densité : un repère, pas un plafond.** Au-delà de 5 liens éditoriaux pour 1000 mots, relire chaque lien pour vérifier qu'il reste utile et contextualisé. Le modèle « chaque ancre pèse 1/N » est un raisonnement de PageRank interne, pas une règle publiée par Google : il sert à réfléchir, pas à trancher.

---

## Cas particulier : site sans donnée GSC

Ce n'est plus un cas particulier : cette passe ne dépend pas de la GSC par construction (voir Étape 6). Sans GSC :
- Étape 4 (cartographie inbound/outbound) se fait via l'étape 0 (script) si le site est en ligne, sinon par parsing du contenu local (markdown/HTML)
- Étape 6 s'arrête au départage par intention ; l'exposition GSC ne s'ajoute que quand `maillage-interne-gsc` tourne derrière
- Le plan reste valable, ajusté avec la GSC dès que la donnée arrive

---

## Cas particulier : refonte de site existant

Si le site existe et a ≥ 6 mois de GSC :
- Chaîner ce skill avec **maillage-interne-gsc** : ce skill définit l'architecture, l'autre injecte la donnée comportementale
- Identifier les pages qui rankent déjà sur le pilier et les promouvoir hub si pertinent
- Préserver les liens existants qui marchent (pas de refonte aveugle)

---

## Cas particulier : pages générées en masse depuis une table de données

Ce skill raisonne par lecture et jugement éditorial (étapes 1-7). Ce raisonnement suppose un nombre de pages qu'un agent peut encore comparer entre elles de façon cohérente. Il ne tient plus au-delà de quelques centaines de pages issues d'un même gabarit.

**Détection** : si un lot de pages partage la même route/le même template et provient d'une table de données (pSEO : un mot de lexique, une fiche produit, un lieu, une entité par ligne), et que ce lot dépasse **300-500 instances**, NE PAS appliquer les étapes 1-7 à ce lot. Le pilier de ces pages est déjà donné par le template lui-même : il n'y a rien à clusteriser.

**Ce qui remplace le raisonnement agent à cette échelle** : un signal de données réel et vérifiable, calculé une fois pour tout le lot, jamais un agent qui juge page par page. Par ordre de préférence :
1. **Relation déjà présente dans la donnée** (cooccurrence, attribut partagé, référence croisée, clé étrangère). C'est le signal le plus fiable : il est vérifiable, pas juste "sémantiquement proche". Exemple : sur un lexique de plus de 13 000 pages (une par mot), les "mots liés" de chaque page sortent d'un comptage de cooccurrence dans le corpus source, pas d'un embedding ni d'un agent.
2. **Embedding + kNN**, seulement si aucune relation de données n'existe pour rapprocher les instances entre elles.

Dans les deux cas, l'agent n'intervient qu'en amont (pour définir la règle : quel signal, combien de liens, quel format de rendu), jamais par page. Le rendu est un bloc templaté (type "Mots liés"), pas un lien in-body : la règle "pas de Voir aussi" de ce skill vise le contenu éditorial écrit à la main, elle ne s'applique pas à un gabarit généré à grande échelle où aucune prose organique n'existe pour y glisser un lien contextuel.

Si le lot reste sous le seuil (quelques dizaines à ~300 pages), les étapes 1-7 s'appliquent normalement : à cette échelle, le jugement éditorial reste fiable et moins coûteux à mettre en place qu'un pipeline de données dédié.

---

## Sauvegarde

Enregistre la sortie dans un fichier markdown daté dans ton dossier de projet (exemple : `2026-09-30-maillage-monsite.md`), rapport de pré-décision compris. Garde à côté le dossier `maillage-data/` du crawl : il sert de point de comparaison au crawl suivant.

---

## Rappels méthode

> "Le maillage interne, c'est un système, pas une passe."
> "5 liens entrants vers la même page = 5 ancres différentes. Un seul exact match."
> "Test à voix haute : si la phrase tombe juste sans le lien, l'ancre est bonne."
> "Une page Know doit toujours pointer vers une page Do."
> "Pas de Voir aussi. Liens in-body uniquement."
> "Un hub n'est pas une catégorie. C'est l'article le plus stratégique du pilier."
> "Le contexte des 5 mots avant/après l'ancre vaut plus que l'ancre elle-même."
