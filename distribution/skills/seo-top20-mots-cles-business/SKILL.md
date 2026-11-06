---
name: seo-top20-mots-cles-business
description: "Audit des mots-clés business d'un site par intention, méthode des trois portes. « mots-clés business », « audit mots-clés business »."
---

# Skill — Mots-clés business (par intention, pas par score)

## Quand utiliser ce skill

Audit des mots-clés business d'un site : pas un classement de requêtes par score, mais une lecture par intention. Regroupe les variantes orthographiques d'un même besoin, distingue les intentions déjà captées de celles qui manquent une page dédiée, diagnostique les pages business qui sous-performent, et dit explicitement non aux requêtes à fort volume mais hors offre. Décision par trois portes successives (correspond à l'offre, intention business, opportunité SEO démontrée) plutôt qu'un produit de notes subjectives affiché en score sur 10. Avec Search Console : les intentions captées et leur performance viennent de GSC. Sans Search Console : la chaîne `seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-resistants-ia` → `seo-mots-cles-decisionnels` → `seo-modeles-pseo` tourne à la place, et alimente les mêmes sections. Comble l'input "requêtes business principales" de la Phase 0 du workflow `audit-complet-v2` quand l'utilisateur ne le fournit pas.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "mots-clés business", "audit mots-clés business", "quelles intentions business le site capte", "quels mots-clés qui comptent", "priorise mes mots-clés GSC", "sur quoi ce site devrait se battre", ou quand la Phase 0 d'un audit doit démarrer sans liste de requêtes business fournie.

## Quand déclencher

- Combler l'input manquant de la Phase 0 du workflow `audit-complet-v2` (`audit-complet-v2/workflow-audit.md`) quand l'utilisateur n'a pas fourni de liste de requêtes business
- Lire un historique GSC business sans passer par l'architecture complète de `seo-modeles-pseo`
- Point de départ d'un call ou d'un audit : « sur quoi ce site devrait-il se battre en premier »

Diffère de `seo-modeles-pseo` (qui conçoit des pages Spokes autour d'une Money Page à partir d'un mot-clé seed, architecture complète) : ici on part de ce que le site capte déjà et on diagnostique, on ne dessine pas une architecture neuve.

## Doctrine 

- **La question n'est pas « quelles requêtes rapportent le plus d'impressions » mais « sur quelles intentions capables de générer du business le site devrait-il concentrer ses pages, et lesquelles sont aujourd'hui absentes, mal ciblées ou sous-exploitées ».**
- **Les variantes orthographiques d'un même besoin sont regroupées** (accord singulier/pluriel, accent, ordre des mots — ex. « générateur de mots clés gratuit », « générateur mots clés gratuit », « générateur mot clé gratuit » = un seul cluster). Les afficher séparément brouille la décision. Ceci remplace l'ancienne doctrine de ce skill (variantes non fusionnées) : ici l'objet de la ligne est l'intention, pas la requête Search Console brute.
- **Aucun score sur 10 affiché.** Un produit de trois notes subjectives (Proximité × Intention × Faisabilité) donne une impression de précision artificielle. La décision passe par trois portes successives, pas par une arithmétique.
- **Une requête à fort volume qui ne correspond pas réellement à l'offre doit pouvoir finir ÉCARTÉE.** Dire non au volume est une partie du livrable, pas un angle mort.
- Aucun volume inventé. Avec GSC : impressions et positions viennent de Search Console, avec leur période. Sans GSC : demande observée en Faible / Moyenne / Forte avec ses signaux nommés (Suggest, calls, acteurs), jamais un chiffre inventé — méthode `audit-complet-v2/demande-observee.md`.
- Les requêtes de marque (nom du site, variantes) sont exclues : ce ne sont pas des opportunités d'acquisition.
- **GSC ne représente pas tout le marché**. Certaines requêtes sont anonymisées, les tableaux ne restituent pas toutes les lignes. L'absence d'une intention dans l'export ne suffit jamais à l'écarter : même avec GSC, la recherche web ciblée des intentions non couvertes (section 2) tourne toujours, elle n'est pas réservée au cas sans GSC.

## Branche GSC / sans GSC

**Avec Search Console** (l'input GSC est disponible) : la section 1 (intentions déjà captées) et la section 3 (pages qui sous-performent) se remplissent depuis GSC (dimension `query` + `page`, 3 à 6 mois). La section 2 (opportunités sans page dédiée) s'appuie sur une recherche web des intentions probables non couvertes par le site, comparées au périmètre GSC existant.

**Sans Search Console** : ne pas improviser un repli GSC-like. Lancer la chaîne complète des skills mots-clés, dans cet ordre (cf. le workflow mots-clés complet (onglet Mots-clés du dashboard), étapes 4-5-7-8-10) :

1. `seo-recherche-mots-cles` — liste brute qualifiée à partir du seed / de l'offre
2. `seo-clustering-mots-cles` — regroupe en clusters d'intention (remplace le regroupement de variantes GSC ci-dessus quand il n'y a pas de GSC)
3. `seo-mots-cles-resistants-ia` — écarte ce qu'une IA générative absorbe déjà sans clic
4. `seo-mots-cles-decisionnels` — isole les requêtes Do (achat, comparaison, délégation)
5. `seo-modeles-pseo` — génère les requêtes Ultra Business par intention et les classe en catégories de Spoke

Les clusters qui sortent de cette chaîne alimentent directement les sections 1 et 2 de ce skill : « intentions déjà captées » devient vide ou quasi vide (rien n'est mesuré sans GSC), « opportunités sans page dédiée » porte l'essentiel du travail, avec la demande observée (Faible/Moyenne/Forte) à la place des impressions.

## Les trois portes (remplace le score /10)

Chaque intention ou cluster passe successivement les trois portes. Une porte fermée n'empêche pas d'examiner la suivante quand elle éclaire la décision, mais la décision finale suit la porte la plus contraignante.

**Porte 1 — Correspond à l'offre ?** Oui / Non. Teste si l'intention colle réellement à ce que le site vend ou permet de faire, pas à un champ lexical proche. Non → écartée, la porte 2 et 3 ne sont pas notées.

**Porte 2 — Intention business ?** Forte / Moyenne / Faible. Mesurée aux modificateurs de la requête ou du besoin exprimé (achat, comparaison, délégation, utilisation directe d'un outil) — jamais au volume.

**Porte 3 — Opportunité SEO démontrée ?** Déjà captée (une page existe et Google l'expose) / Nouvelle opportunité (la demande existe, aucune page n'y répond) / Non démontrée (rien ne prouve la demande sur ce point précis).

**Décision** (une valeur parmi) :

- **POUSSER** — déjà captée, offre et intention fortes : consolider ce qui marche déjà.
- **CRÉER** — nouvelle opportunité, offre et intention fortes, aucune page n'y répond.
- **CONSOLIDER** — déjà captée mais sous-performe (page existe, mauvaise position ou mauvais ciblage) : diagnostiquer avant de retravailler.
- **ÉCARTER** — porte 1 fermée, ou intention trop faible pour justifier l'effort.
- **À VALIDER** — porte 3 non démontrée : la demande ou la SERP doit être vérifiée avant toute décision définitive.

## Pipeline (4 étapes)

### Étape 1 — Lister et regrouper

Avec GSC : toutes les requêtes non-marque (dimension `query`, 3-6 mois), regroupées par intention business (fusionner les variantes orthographiques strictes du même besoin — sommer leurs impressions et signaler la fusion, ne jamais l'omettre en silence). Sans GSC : les clusters sortis de la chaîne `seo-recherche-mots-cles` → `seo-clustering-mots-cles`.

### Étape 2 — Croiser avec les pages existantes

Pour chaque intention/cluster : quelle page du site y répond aujourd'hui (si une existe), et avec quel signal (position, impressions avec GSC ; rien à afficher sans GSC au-delà du diagnostic qualitatif).

### Étape 3 — Passer les trois portes

Noter Porte 1 / Porte 2 / Porte 3 pour chaque intention/cluster retenu à l'étape 1. Une requête à fort volume qui échoue Porte 1 est documentée dans la section 4 (à ne pas poursuivre), pas silencieusement supprimée.

### Étape 4 — Répartir dans les quatre sections et décider

Ranger chaque intention/cluster dans une des quatre sections de sortie ci-dessous selon sa décision, puis écrire la synthèse « Ce qu'il faut faire » (3 actions maximum, chacune justifiée par la porte qui la motive).

## Sortie de pré-décision (obligatoire)

Suit le format standard des skills d'audit — `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). En usage autonome : `wiki/audit/YYYY-MM-DD-slug-mots-cles-business.md`. En usage via `audit-complet-v2` : nourrit directement la Phase 0.

1. Diagnostic principal : une phrase (ex. « la demande existe sur N intentions, une seule dépasse le top 10 » ou l'inverse).
2. Les chiffres à retenir : 3 à 5.
3. Pas d'état Critique/À améliorer/Sain ici, ce skill priorise, il n'audite pas une dimension technique.
4. Les quatre sections de sortie ci-dessous.
5. Ce que les données ne permettent pas de conclure (ex. pas de volume Keyword Planner, pas de CPC, SERP jugée sur un échantillon de recherche web restreint, demande observée sans GSC = signal, pas une mesure).

Règles : aucun volume ni CPC inventé ; une requête corrompue dans l'export est signalée, jamais classée comme si elle était réelle ; jamais de score /10 affiché, les trois portes remplacent l'arithmétique ; une fusion de variantes est toujours signalée, jamais silencieuse.

## Ce que le client lit 

Le client doit comprendre ce que l'analyse change pour son activité, pas comment elle a été menée. Règles pour tout ce qui s'affiche dans l'onglet :

- **Le dernier lien est obligatoire** : recherche → offre ou fonction concernée → résultat commercial recherché (candidature, rendez-vous, devis, contact qualifié) → ce qu'il reste à établir. « Correspond à l'offre : oui » ne suffit pas, il ne dit pas pourquoi investir sur cette recherche plutôt qu'une autre. Trois recherches ne remplissent pas la même fonction (vendre une offre, vendre une prestation, faire découvrir un outil) : ne pas les ranger sous une même « intention business ». Pour un outil gratuit, la question à poser au client avant toute priorité : cette page doit-elle seulement faire utiliser l'outil, ou aussi générer des demandes ?
- **Résultat SEO et résultat commercial restent distincts.** Impressions, positions, clics évaluent les apparitions des pages dans Google, pas leur contribution aux ventes. Sans candidatures, demandes ou ventes attribuées, l'écrire tel quel. Ne pas inventer un chiffre d'affaires potentiel ; dire quelle conversion on cherche et comment on saura que l'action a servi.
- **Un verdict en tête, pas une note.** L'onglet s'ouvre sur un diagnostic lisible en deux phrases (« Diagnostic partiel » quand les requêtes ou les conversions manquent). Pas de score sur 100 sur cet onglet : il mélangerait la performance du site et la qualité du diagnostic, et une donnée manquante n'est pas une mauvaise performance. Pour chaque action, trois appréciations séparées : impact attendu, certitude du diagnostic, effort ; quand l'une est inconnue, l'écrire. Un indicateur de couverture n'a de sens qu'avec un dénominateur réel : les intentions prioritaires validées avec le client, pas les requêtes que Search Console accepte de montrer.
- **Ordre de l'onglet** : verdict → les décisions proposées (offre, action justifiée, résultat commercial à suivre) → ce que l'analyse ne permet pas de conclure → tableau recherche / offre / résultat commercial / reste à établir → les preuves, regroupées par opportunité ou par page (une page n'apparaît qu'une fois, pas dans quatre sections) → exclusions et vérifications dans des blocs repliés.
- **Requêtes absentes de l'extraction.** Absentes ne veut pas dire anonymisées : distinguer limite d'extraction, filtrage et anonymisation. Si elles sont anonymisées, Google les retire aussi du tableau de l'interface : ne jamais écrire « lire les requêtes dans l'interface ». L'action est : établir pourquoi elles ne remontent pas ; si elles restent indisponibles, analyser le ciblage depuis le contenu de la page et les résultats Google sur les recherches visées. Ne jamais bloquer toute décision derrière ces données : dire lesquelles les attendent (fusion, 301, title réécrit pour une recherche précise) et lesquelles se prennent sur d'autres preuves (liens, rôle des pages, cohérence des chiffres).
- **Une position moyenne agrège** toutes les apparitions de la page sur le périmètre : position 5 ne veut pas dire cinquième sur la recherche commerciale visée. Des apparitions sans clic justifient de vérifier le ciblage ; elles ne démontrent ni que le title est en cause ni qu'une modification apportera des clics.
- **Les impressions comptent les affichages du site**, pas le volume du marché. La colonne des observations de SERP s'appelle « Ce que montrent les résultats Google » et renseigne le format et l'intention à examiner, pas la demande. Écrire : intention examinée, demande non quantifiée, rentabilité non établie. Trois recherches examinées ne couvrent pas les opportunités des offres : il faut une couverture par offre prioritaire.
- **Vocabulaire client.** Les trois portes, les phases et les règles internes restent dans le fonctionnement, pas dans le texte. « Lecture par intention, pas par volume » → « nous retenons les recherches qui correspondent à vos offres et aux clients que vous voulez attirer » ; « intentions déjà captées » → « les recherches commerciales sur lesquelles votre site apparaît » (« captée » est exclu pour une recherche sans clic) ; « opportunités sans page exposée » → « les recherches à examiner pour vos pages existantes » ; « porte 1 fermée » → « cette recherche ne correspond pas à votre offre actuelle » ; « porte 3 non démontrée » → « les données ne suffisent pas encore pour recommander cette action » ; « exposée, jamais cliquée » → « 91 apparitions dans Google, aucun clic sur la période » ; « maillage, chiffres étayés, puis relire » → « vérifier les liens vers la page et les preuves présentées, puis préciser les modifications nécessaires ».
- **Une requête qui ressemble à un terme technique peut être un nom** (« 410gone » est aussi une agence SEO) : vérifier avant d'écrire la raison d'une exclusion, même si la décision ne change pas.
- **Réconcilier les comptes** avant publication : le même nombre de pages sans requête partout, les impressions attribuées à la même unité (cluster ou requête) partout, une baisse toujours accompagnée de ses chiffres par période.

## Sortie obligatoire

Gabarit de l'onglet Mots-clés business.

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

- [recherche web faite sur N requêtes seulement / pas de GSC page dimension / demande observée sans GSC = signal, pas une mesure / etc.]
```

## Garde-fous (NON-NÉGOCIABLES)

- Jamais de score /10 affiché : les trois portes et la décision (POUSSER/CRÉER/CONSOLIDER/ÉCARTER/À VALIDER) remplacent l'arithmétique.
- Une fusion de variantes orthographiques est toujours explicite (quelles requêtes fusionnées, dans quel cluster), jamais une somme silencieuse.
- Sans GSC, ne pas fabriquer d'impressions ni de position : lancer la chaîne des 5 skills et afficher une demande observée qualitative.
- Une requête à fort volume mais hors offre finit explicitement dans la section 4, jamais retirée sans trace.
- La décision ne se pondère jamais à la main pour faire remonter une intention que l'utilisateur préférerait voir en tête, elle découle des trois portes.

## Enchaînement workflow

Avec GSC en amont : export ou accès Search Console. Sans GSC en amont : `seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-resistants-ia` → `seo-mots-cles-decisionnels` → `seo-modeles-pseo`. En aval : Phase 0 du workflow `audit-complet-v2` ; `seo-brief-contenu` pour les intentions en CRÉER ; `seo-modeles-pseo` si une intention CRÉER révèle une famille assez riche pour mériter une architecture Money Page + Spokes complète.

## Sauvegarde

Output dans `wiki/audit/YYYY-MM-DD-slug-mots-cles-business.md` selon hook §7 AGENTS.md.

## Concepts liés

`grounding-score` · `surprise-gap` · `pseo` · `funnel` · `demande-observee`

## Vérification finale (obligatoire)

Avant de présenter le livrable comme terminé : lancer `verificateur-livrable` avec les 6 sections de le skill `verification-livrable` (demande de tous les skills utilisés, livrables, sources, contraintes). Corriger les ❌, relancer le vérificateur sur la nouvelle version, recopier le dernier tableau dans la réponse. Un hook refuse la fin de la réponse tant que ce n'est pas fait.
