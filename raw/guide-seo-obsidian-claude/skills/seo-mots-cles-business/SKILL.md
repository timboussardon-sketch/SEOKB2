---
name: seo-mots-cles-business
description: |
  Audit des mots-clés business d'un site : pas un classement de requêtes par score, mais une lecture par intention. Regroupe les variantes orthographiques d'un même besoin, distingue les intentions déjà captées de celles qui manquent une page dédiée, diagnostique les pages business qui sous-performent, et dit explicitement non aux requêtes à fort volume mais hors offre. Décision par trois portes successives (correspond à l'offre, intention business, opportunité SEO démontrée) plutôt qu'un produit de notes subjectives affiché en score sur 10. Avec Search Console : les intentions captées et leur performance viennent de l'export. Sans Search Console : une procédure interne (Google Suggest, recherche web des intentions, verbatims clients, regroupement par intention, tri de ce qu'une IA absorbe sans clic, demande observée) alimente les mêmes sections.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "mots-clés business", "audit mots-clés business", "quelles intentions business le site capte", "quels mots-clés comptent", "priorise mes mots-clés Search Console", "sur quoi ce site devrait se battre", ou quand un audit SEO doit démarrer sans liste de requêtes business fournie.
---

# Skill : mots-clés business (par intention, pas par score)

## Ce que tu donnes à Claude

- **L'offre et le point de conversion** : ce que le site vend ou permet de faire, et l'action attendue (demande de devis, rendez-vous, achat, inscription, candidature, utilisation d'un outil).
- **La cible** : qui tu veux attirer (particuliers ou entreprises, taille, secteur, situation).
- **Le marché et la langue** : pays, langue des recherches, zone géographique si l'offre est locale.
- **Les URL des pages d'offre** : les pages qui vendent, pas tout le site.
- **L'export Search Console, si tu l'as** : onglets Requêtes et Pages, sur 3 à 6 mois (Performances > Exporter). Sans lui, le skill tourne quand même, avec une demande observée à la place des impressions.
- **Des verbatims clients, si tu en as** : notes ou transcriptions d'appels, emails, avis, questions reçues. Ils servent de signal de demande et de vocabulaire réel.

## Consigne pour le lancer

> Lance le skill seo-mots-cles-business sur [URL du site]. Mon offre : [ce que je vends], ma cible : [qui], mon point de conversion : [action attendue], marché : [pays, langue].

> Voici mon export Search Console (Requêtes + Pages, 6 mois) et mes pages d'offre : [URL]. Dis-moi sur quelles intentions mon site doit concentrer ses pages, lesquelles manquent, et lesquelles écarter.

## Quand déclencher

- Fournir la liste de requêtes business qui manque au démarrage d'un audit SEO
- Lire un historique Search Console business sans concevoir toute une architecture de pages
- Point de départ d'un call ou d'un audit : « sur quoi ce site devrait-il se battre en premier »

Ce skill part de ce que le site capte déjà et diagnostique. Il ne dessine pas une architecture neuve de pages satellites autour d'une page d'offre à partir d'un mot-clé seed.

## Doctrine

- **La question n'est pas « quelles requêtes rapportent le plus d'impressions » mais « sur quelles intentions capables de générer du business le site devrait-il concentrer ses pages, et lesquelles sont aujourd'hui absentes, mal ciblées ou sous-exploitées ».**
- **Les variantes orthographiques d'un même besoin sont regroupées** (accord singulier/pluriel, accent, ordre des mots : « générateur de mots clés gratuit », « générateur mots clés gratuit », « générateur mot clé gratuit » = un seul cluster). Les afficher séparément brouille la décision. L'objet de la ligne est l'intention, pas la requête Search Console brute.
- **Aucun score sur 10 affiché.** Un produit de trois notes subjectives (Proximité × Intention × Faisabilité) donne une impression de précision artificielle. La décision passe par trois portes successives, pas par une arithmétique.
- **Une requête à fort volume qui ne correspond pas réellement à l'offre doit pouvoir finir ÉCARTÉE.** Dire non au volume est une partie du livrable, pas un angle mort.
- Aucun volume inventé. Avec Search Console : impressions et positions viennent de l'export, avec leur période. Sans Search Console : demande observée en Faible / Moyenne / Forte avec ses signaux nommés (voir « Demande observée » plus bas), jamais un chiffre inventé.
- Les requêtes de marque (nom du site, variantes) sont exclues : ce ne sont pas des opportunités d'acquisition.
- **Search Console ne représente pas tout le marché.** Certaines requêtes sont anonymisées, les tableaux ne restituent pas toutes les lignes. L'absence d'une intention dans l'export ne suffit jamais à l'écarter : même avec Search Console, la recherche web ciblée des intentions non couvertes (section 2) tourne toujours.

## Branche avec ou sans Search Console

**Avec Search Console** : la section 1 (intentions déjà captées) et la section 3 (pages qui sous-performent) se remplissent depuis l'export (dimensions requête + page, 3 à 6 mois). La section 2 (opportunités sans page dédiée) s'appuie sur une recherche web des intentions probables non couvertes par le site, comparées au périmètre de l'export.

**Sans Search Console** : ne pas improviser de fausses impressions ni de fausses positions. Dérouler la procédure ci-dessous. Elle alimente les sections 1 et 2 : « intentions déjà captées » devient vide ou quasi vide (rien n'est mesuré), « opportunités sans page dédiée » porte l'essentiel du travail, avec la demande observée à la place des impressions.

### Procédure sans Search Console (5 temps)

**1. Collecter les formulations réelles.**
- Google Suggest : taper chaque terme de l'offre (et ses variantes « prix », « avis », « meilleur », « alternative », « [ville] ») et relever les suggestions. Compter les variantes qui contiennent le sujet.
- Recherche web des intentions : pour chaque offre, chercher comment les gens formulent le besoin et qui y répond déjà (pages d'offre d'autres sites, comparatifs, annuaires, forums). Relever les « Autres questions posées » quand elles apparaissent.
- Verbatims fournis par l'utilisateur : repérer les formulations qui reviennent dans les appels, emails, avis. Compter dans combien d'appels ou de messages chaque formulation apparaît.

**2. Regrouper par intention.** Un cluster = une intention = une page.
- Le vrai critère est le partage de résultats Google : si deux requêtes affichent le même top 10, c'est la même intention, donc une seule page. La ressemblance des mots ne suffit pas (« assurance auto pas chère » et « tarif assurance auto » peuvent avoir des résultats distincts).
- Sans vérification des résultats, regrouper par intention identique + même tête sémantique, et marquer le cluster « hypothèse, à valider sur les résultats Google ».
- Fusionner les variantes orthographiques strictes. Un mot-clé n'appartient qu'à un seul cluster. Un mot-clé orphelin reste seul, on ne le force pas dans un cluster.
- Pour chaque cluster : nom, intention dominante, requête pivot, requêtes secondaires. Une requête secondaire sert à repérer une sous-intention, pas à placer un title, un H2 ou une FAQ par défaut.
- Si un cluster recoupe une page existante du site, écrire « chevauchement potentiel à vérifier ». Le mot « cannibalisation » exige une preuve (mêmes requêtes sur plusieurs URL dans Search Console, ou résultats Google vérifiés).

**3. Trier ce qu'une IA absorbe sans clic.**
- Test : une réponse générique et non sourcée de trois phrases satisferait-elle la requête ? Oui, l'IA (AI Overviews, ChatGPT, Perplexity) y répond à la place du site. Non, il faut comparer, choisir ou vérifier avec du contexte propre : le clic a de bonnes chances de rester.
- Signaux d'absorption : « qu'est-ce que », « comment », « pourquoi », « définition de », un chiffre ou un fait unique et stable.
- Signaux de résistance : achat (acheter, prix, tarif, devis, abonnement, s'inscrire), comparaison (meilleur, top, vs, comparatif, alternative à, lequel choisir), évaluation (avis, test, retour d'expérience, fiable, arnaque), local ou immédiat (près de moi, [ville], en ligne, livraison), marque (nom d'outil + alternative, avis, prix).
- Écrire « probabilité de conserver un clic après réponse IA : forte / moyenne / faible », jamais une certitude, et toujours justifiée par le modificateur ou le test. Le volume ne dit rien du risque d'absorption : une requête définitionnelle à fort volume est la plus exposée.
- Une requête absorbée n'est pas abandonnée : elle peut valoir un travail de citation dans les réponses IA plutôt qu'une page pour le clic. Le dire.

**4. Isoler le décisionnel.**
- Une requête décisionnelle : la personne choisit, compare ou achète. Elle se repère à ses modificateurs, pas à son volume.
- Étages : achat (transformer maintenant), comparatif (choisir entre options, toi compris), local (achat + contrainte géographique), marque (connaît déjà un acteur), connaissance commerciale (« comment choisir un X », pré-décision à capter tôt).
- Chaque requête décisionnelle pointe vers une page avec offre et appel à l'action, sinon elle ne convertit pas. Une requête qui cite un autre site ou un autre outil se traite par une page comparative honnête, sans tromperie.
- Ne jamais classer décisionnelle une requête purement informationnelle pour gonfler la liste.

**5. Qualifier la demande observée** (section suivante), puis passer chaque cluster aux trois portes.

Si tu as aussi les skills `seo-clustering-mots-cles`, `seo-mots-cles-resistants-ia` ou `seo-mots-cles-decisionnels`, tu peux les lancer à la place des temps 2, 3 et 4 : leurs sorties alimentent les mêmes sections.

### Demande observée

« Pas de volume inventé » ne veut pas dire « aucun signal de demande ». Une requête à forte intention peut être cherchée par 5 personnes ou par 500. On n'écrit pas « volume = 320 », on écrit une demande observée Faible / Moyenne / Forte, toujours avec les signaux qui la fondent, nommés et affichés séparément.

| Signal | Faible | Moyen | Fort |
|---|---|---|---|
| Variantes Google Suggest contenant le sujet | 0 | 1 à 4 | 5 et plus |
| Impressions Search Console sur les requêtes du sujet (90 jours) | 0 | 1 à 19 | 20 et plus |
| Formulation présente dans les appels ou messages clients | 0 à 2 | 3 à 6 | 7 et plus |
| Sites spécialisés qui tiennent déjà la requête | 0 | 1 ou 2 | 3 et plus |

À ajouter quand ils sont disponibles, même barème : « Autres questions posées », suggestions YouTube, Google Trends sur 12 mois, Keyword Planner (alors le volume s'affiche, avec sa source).

- Un signal non mesuré s'écrit « non mesuré ».
- Les signaux ne s'additionnent pas en silence : 20 variantes Suggest peuvent venir de formulations très proches, et le nombre de sites présents mesure l'offre en place, pas la demande. Le niveau Faible / Moyenne / Forte est une lecture, les signaux restent visibles à côté.
- Seules les impressions Search Console prouvent qu'une requête est tapée et que le site y apparaît : « demande confirmée par la Search Console » à partir de 20 impressions, rien d'autre.
- Intention forte + aucun signal de demande = terrain vide : « demande à confirmer », mesure dans Search Console à 90 jours, jamais une priorité présentée comme acquise.
- Signaux de demande présents + intention faible = trafic sans demande commerciale : pas de page pour le clic.

## Les trois portes

Chaque intention ou cluster passe successivement les trois portes. Une porte fermée n'empêche pas d'examiner la suivante quand elle éclaire la décision, mais la décision finale suit la porte la plus contraignante.

**Porte 1 : correspond à l'offre ?** Oui / Non. Teste si l'intention colle réellement à ce que le site vend ou permet de faire, pas à un champ lexical proche. Non : écartée, les portes 2 et 3 ne sont pas notées.

**Porte 2 : intention business ?** Forte / Moyenne / Faible. Mesurée aux modificateurs de la requête ou du besoin exprimé (achat, comparaison, délégation, utilisation directe d'un outil), jamais au volume.

**Porte 3 : opportunité SEO démontrée ?** Déjà captée (une page existe et Google l'expose) / Nouvelle opportunité (la demande existe, aucune page n'y répond) / Non démontrée (rien ne prouve la demande sur ce point précis).

**Décision** (une valeur parmi) :

- **POUSSER** : déjà captée, offre et intention fortes. Consolider ce qui marche déjà.
- **CRÉER** : nouvelle opportunité, offre et intention fortes, aucune page n'y répond.
- **CONSOLIDER** : déjà captée mais sous-performe (la page existe, mauvaise position ou mauvais ciblage). Diagnostiquer avant de retravailler.
- **ÉCARTER** : porte 1 fermée, ou intention trop faible pour justifier l'effort.
- **À VALIDER** : porte 3 non démontrée. La demande ou les résultats Google doivent être vérifiés avant toute décision définitive.

## Pipeline (4 étapes)

### Étape 1 : lister et regrouper

Avec Search Console : toutes les requêtes non-marque (dimension requête, 3 à 6 mois), regroupées par intention business. Fusionner les variantes orthographiques strictes du même besoin, sommer leurs impressions et signaler la fusion, ne jamais l'omettre en silence. Sans Search Console : les clusters sortis de la procédure ci-dessus.

### Étape 2 : croiser avec les pages existantes

Pour chaque intention ou cluster : quelle page du site y répond aujourd'hui (si une existe), et avec quel signal (position, impressions avec Search Console ; sans elle, rien à afficher au-delà du diagnostic qualitatif).

### Étape 3 : passer les trois portes

Noter Porte 1 / Porte 2 / Porte 3 pour chaque intention ou cluster retenu à l'étape 1. Une requête à fort volume qui échoue à la porte 1 est documentée dans la section 4 (à ne pas poursuivre), pas supprimée en silence.

### Étape 4 : répartir dans les quatre sections et décider

Ranger chaque intention ou cluster dans une des quatre sections de sortie selon sa décision, puis écrire la synthèse « Ce qu'il faut faire » (3 actions maximum, chacune justifiée par la porte qui la motive).

## Sortie de pré-décision (obligatoire)

Format d'un rapport de consultant qui priorise, pas d'un outil qui récite : peu d'informations visibles, le raisonnement derrière. Chaque information est typée : fait observé, interprétation ou recommandation, et une interprétation n'est jamais présentée comme un fait. La conclusion n'est jamais plus catégorique que la couverture des données (« sur les 40 requêtes de l'export », pas « sur le site »). Pas de « low / medium / high » : Faible, Moyen, Élevé.

1. Diagnostic principal : une phrase (ex. « la demande existe sur N intentions, une seule dépasse le top 10 », ou l'inverse). Une conclusion en gras, deux lignes de démonstration.
2. Les chiffres à retenir : 3 à 5, chacun avec sa source et sa période.
3. Pas d'état Critique / À améliorer / Sain ici : ce skill priorise, il n'audite pas une dimension technique.
4. Les quatre sections de sortie ci-dessous.
5. Ce que les données ne permettent pas de conclure (ex. pas de volume Keyword Planner, pas de CPC, résultats Google examinés sur un échantillon restreint de recherches, demande observée sans Search Console = signal, pas une mesure).

Règles : aucun volume ni CPC inventé ; une requête corrompue dans l'export est signalée, jamais classée comme si elle était réelle ; jamais de score /10 affiché, les trois portes remplacent l'arithmétique ; une fusion de variantes est toujours signalée, jamais silencieuse ; aucune création de page recommandée par automatisme parce qu'un mot-clé n'a pas de page : vérifier d'abord s'il existe une URL, une intention proche ou un contenu réutilisable.

## Ce que le client lit

Le client doit comprendre ce que l'analyse change pour son activité, pas comment elle a été menée. Règles pour tout ce qui s'affiche dans le livrable :

- **Le dernier lien est obligatoire** : recherche → offre ou fonction concernée → résultat commercial recherché (candidature, rendez-vous, devis, contact qualifié) → ce qu'il reste à établir. « Correspond à l'offre : oui » ne suffit pas, il ne dit pas pourquoi investir sur cette recherche plutôt qu'une autre. Trois recherches ne remplissent pas la même fonction (vendre une offre, vendre une prestation, faire découvrir un outil) : ne pas les ranger sous une même « intention business ». Pour un outil gratuit, la question à poser au client avant toute priorité : cette page doit-elle seulement faire utiliser l'outil, ou aussi générer des demandes ?
- **Résultat SEO et résultat commercial restent distincts.** Impressions, positions, clics évaluent les apparitions des pages dans Google, pas leur contribution aux ventes. Sans candidatures, demandes ou ventes attribuées, l'écrire tel quel. Ne pas inventer un chiffre d'affaires potentiel ; dire quelle conversion on cherche et comment on saura que l'action a servi.
- **Un verdict en tête, pas une note.** Le livrable s'ouvre sur un diagnostic lisible en deux phrases (« Diagnostic partiel » quand les requêtes ou les conversions manquent). Pas de score sur 100 : il mélangerait la performance du site et la qualité du diagnostic, et une donnée manquante n'est pas une mauvaise performance. Pour chaque action, trois appréciations séparées : impact attendu, certitude du diagnostic, effort ; quand l'une est inconnue, l'écrire. Un indicateur de couverture n'a de sens qu'avec un dénominateur réel : les intentions prioritaires validées avec le client, pas les requêtes que Search Console accepte de montrer.
- **Ordre du livrable** : verdict → les décisions proposées (offre, action justifiée, résultat commercial à suivre) → ce que l'analyse ne permet pas de conclure → tableau recherche / offre / résultat commercial / reste à établir → les preuves, regroupées par opportunité ou par page (une page n'apparaît qu'une fois, pas dans quatre sections) → exclusions et vérifications en fin de document ou dans des blocs repliés.
- **Requêtes absentes de l'extraction.** Absentes ne veut pas dire anonymisées : distinguer limite d'extraction, filtrage et anonymisation. Si elles sont anonymisées, Google les retire aussi du tableau de l'interface : ne jamais écrire « lire les requêtes dans l'interface ». L'action est : établir pourquoi elles ne remontent pas ; si elles restent indisponibles, analyser le ciblage depuis le contenu de la page et les résultats Google sur les recherches visées. Ne jamais bloquer toute décision derrière ces données : dire lesquelles les attendent (fusion, 301, title réécrit pour une recherche précise) et lesquelles se prennent sur d'autres preuves (liens, rôle des pages, cohérence des chiffres).
- **Une position moyenne agrège** toutes les apparitions de la page sur le périmètre : position 5 ne veut pas dire cinquième sur la recherche commerciale visée. Des apparitions sans clic justifient de vérifier le ciblage ; elles ne démontrent ni que le title est en cause ni qu'une modification apportera des clics.
- **Les impressions comptent les affichages du site**, pas le volume du marché. La colonne des observations de résultats s'appelle « Ce que montrent les résultats Google » et renseigne le format et l'intention à examiner, pas la demande. Écrire : intention examinée, demande non quantifiée, rentabilité non établie. Trois recherches examinées ne couvrent pas les opportunités des offres : il faut une couverture par offre prioritaire.
- **Vocabulaire client.** Les trois portes, les étapes et les règles internes restent dans le fonctionnement, pas dans le texte. « Lecture par intention, pas par volume » → « nous retenons les recherches qui correspondent à vos offres et aux clients que vous voulez attirer » ; « intentions déjà captées » → « les recherches commerciales sur lesquelles votre site apparaît » (« captée » est exclu pour une recherche sans clic) ; « opportunités sans page exposée » → « les recherches à examiner pour vos pages existantes » ; « porte 1 fermée » → « cette recherche ne correspond pas à votre offre actuelle » ; « porte 3 non démontrée » → « les données ne suffisent pas encore pour recommander cette action » ; « exposée, jamais cliquée » → « 91 apparitions dans Google, aucun clic sur la période » ; « maillage, chiffres étayés, puis relire » → « vérifier les liens vers la page et les preuves présentées, puis préciser les modifications nécessaires ».
- **Une requête qui ressemble à un terme technique peut être un nom** (« 410gone » est aussi le nom d'une agence SEO) : vérifier avant d'écrire la raison d'une exclusion, même si la décision ne change pas.
- **Réconcilier les comptes** avant de livrer : le même nombre de pages sans requête partout, les impressions attribuées à la même unité (cluster ou requête) partout, une baisse toujours accompagnée de ses chiffres par période.

## Sortie obligatoire

Gabarit du livrable « Mots-clés business » (à assembler dans l'ordre client ci-dessus, les quatre sections deviennent les preuves).

```markdown
# Mots-clés business

L'analyse ne cherche pas les requêtes qui génèrent le plus d'impressions, mais celles qui sont les plus proches de l'offre et d'une décision d'utilisation ou d'achat.
Les variantes orthographiques correspondant à la même intention sont regroupées. Une requête n'est retenue comme opportunité que si elle correspond réellement à l'offre.

## 1. Les intentions business déjà captées

| Intention / cluster | Page actuelle | Impressions 6 mois | Position | Intention | Correspondance offre | État |
|---|---|---:|---:|---|---|---|

## 2. Les opportunités business sans page dédiée

| Intention | Demande observée | Correspondance avec l'offre | Page existante capable de répondre ? | Décision |
|---|---|---|---|---|

## 3. Les pages business qui sous-performent

| Page | Intention cible | Signal actuel | Diagnostic | Action |
|---|---|---|---|---|

## 4. Les requêtes à ne pas poursuivre

| Requête / intention | Pourquoi elle est écartée |
|---|---|

## Ce qu'il faut faire

1. [Action, justifiée par la porte qui la motive]
2. [Action]
3. [Action]

## Limites

- [recherche web faite sur N requêtes seulement / pas de dimension page dans l'export / demande observée sans Search Console = signal, pas une mesure / etc.]
```

Dans la section 2, la colonne « Demande observée » affiche le niveau et ses signaux nommés (ex. « Moyenne : 6 variantes Suggest, 4 appels, Search Console non disponible »).

## Garde-fous (non négociables)

- Jamais de score /10 affiché : les trois portes et la décision (POUSSER / CRÉER / CONSOLIDER / ÉCARTER / À VALIDER) remplacent l'arithmétique.
- Une fusion de variantes orthographiques est toujours explicite (quelles requêtes fusionnées, dans quel cluster), jamais une somme silencieuse.
- Sans Search Console, ne pas fabriquer d'impressions ni de position : dérouler la procédure sans Search Console et afficher une demande observée avec ses signaux.
- Une requête à fort volume mais hors offre finit explicitement dans la section 4, jamais retirée sans trace.
- La décision ne se pondère jamais à la main pour faire remonter une intention qu'on préférerait voir en tête : elle découle des trois portes.

## Suite

Pour les intentions en CRÉER : un brief de contenu par cluster, une fois les résultats Google vérifiés. Si une intention CRÉER révèle une famille de requêtes assez riche, elle peut justifier une page d'offre entourée de pages satellites décisionnelles.

## Sauvegarde

Enregistre la sortie dans un fichier markdown daté (`AAAA-MM-JJ-<site>-mots-cles-business.md`) dans ton dossier de projet.
