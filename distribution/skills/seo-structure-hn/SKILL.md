---
name: seo-structure-hn
description: "Audit des Hn (H1 à H6) de tout un site, 8 contrôles. « audit Hn », « audit structure Hn », « vérifie mes H1/H2 »."
---

# Skill — Audit structurel Hn

## Quand utiliser ce skill

Audit structurel Hn (H1 à H6) d'un site : extrait l'arborescence de titres de chaque URL et applique 8 contrôles (H1 unique et présent, hiérarchie sans saut de niveau, H1 vs intention GSC, H2 vs micro-intentions GSC, Hn génériques bannis, Hn sur-optimisés, Passage Ranking — chaque H2 lisible comme une réponse autonome, pages sans structure). Le périmètre suit le sitemap complet du site, pas un échantillon arbitraire. Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit structure Hn", "audit Hn", "vérifie mes H1/H2", "structure de titres", "mes pages ont-elles un bon Hn", "audit structurel", ou quand il fournit une liste d'URLs / un sitemap en demandant un diagnostic de structure éditoriale.

Formalise la Phase 3 (« Audit structurel — architecture Hn ») du workflow d'audit complet (`audit-complet-v2/workflow-audit.md`), qui n'avait jusqu'ici qu'un prompt sans skill dédié. Invocable seul, ou comme brique de `audit-complet-v2`.

## Quand déclencher

- Audit ponctuel de la structure éditoriale d'un site (avant call commercial, après une refonte, après une migration de CMS)
- Brique de la Phase 3 du workflow `audit-complet-v2`
- Diagnostic d'un cluster de pages qui ne rankent pas malgré un contenu réel (le Hn peut être la cause structurante)

Diffère de `seo-brief-contenu` (qui construit un Hn cible AVANT rédaction) : ici on audite un Hn qui EXISTE déjà.

Diffère de `seo-contenu-pertinence` (qui audite la réponse du contenu : intention et format, questions sans réponse, crédibilité, valeur propre, title / meta) : ici on audite la charpente seule. Dans `audit-complet-v2`, les deux se chaînent dans l'onglet « Contenu et pertinence », ce skill en sous-contrôle (depuis le 28/09/2026, l'onglet s'appelait « Structure des titres » avant).

## Doctrine

- La structure Hn est la colonne vertébrale du Passage Ranking. Un Hn cassé rend un bon contenu invisible.
- On ne compare jamais un Hn à un idéal abstrait : on le compare aux requêtes GSC réelles de la page (H1 vs intention primaire, H2 vs micro-intentions en position 4-20).
- Des Hn identiques mot pour mot sur plusieurs pages d'un même cluster sont un **signal d'examen**, pas une anomalie en soi : plusieurs pages peuvent légitimement partager « Fonctionnement », « Tarifs », « Conditions ». Ce qu'on juge, c'est la différenciation des réponses et des intentions derrière les intitulés, pas les intitulés seuls. Un cluster à intitulés identiques ET à zéro impression GSC renforce le signal ; il ne prouve pas la cause.
- Le nombre de mots seul n'est jamais un problème Hn.
- **Une convention éditoriale n'est pas un problème SEO critique**. Les huit contrôles produisent des observations ; la gravité ne découle jamais automatiquement de l'observation. L'ordre des headings n'est pas une exigence de classement chez Google, leur organisation sémantique sert d'abord l'accessibilité, et il n'existe pas de nombre idéal de headings. La question qui donne la gravité : **le titre principal et l'organisation permettent-ils de comprendre clairement la page ?** Un « Conclusion » est un choix éditorial faible selon le standard de l'utilisateur ; ce n'est pas, pour cette seule raison, un frein SEO démontré.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Sitemap.xml complet du site, ou liste exhaustive des URLs (le périmètre suit le site, pas un échantillon de 50) | Oui |
| Export GSC (positions, impressions par page et par requête) | Recommandé — sans lui, le contrôle 3 et 4 (H1/H2 vs intention) ne peuvent pas tourner, à documenter en limite |
| Accès HTML des pages (`curl` terminal, ou Chrome en Cowork) | Oui |

Minimum viable : liste d'URLs + accès HTML. Sans GSC, le skill audite la structure seule (contrôles 1, 2, 5, 6, 7, 8) et documente les contrôles 3/4 comme non testables.

## Pipeline (3 étapes)

### Étape 1 — Extraire l'arborescence Hn

Pour chaque URL du périmètre, extraire H1 → H6 dans l'ordre du document, plus `<title>` et meta description.

- Terminal : `curl -sL -A "Mozilla/5.0" {URL} | grep -oE '<h[1-6][^>]*>.*?</h[1-6]>'` (puis nettoyer le texte des balises)
- Cowork : Chrome lit les headings du DOM rendu (utile si le Hn n'existe qu'après hydratation JS)

**Garde-fou rendu** (reformulé le 28/09/2026) : si le HTML récupéré par `curl` est identique (même taille en octets, même title) à celui d'une autre URL du site (typiquement la home), ne pas noter la page sur les 8 contrôles comme si son Hn était réel, et ne PAS conclure « pré-rendu cassé ». Un HTML initial commun ne le démontre pas : certaines applications servent un HTML initial sans contenu principal puis le génèrent en JavaScript, et Google indexe le HTML rendu. La sortie est « Suspicion de dépendance au rendu ou de problème de pré-rendu : vérifier avant de conclure », et la vérification suit le protocole de rendu de `indexation-check` (HTML initial → DOM rendu → version vue par Google). Lire alors les Hn dans le DOM rendu.

### Étape 2 — Appliquer les 8 contrôles

Les huit contrôles relèvent des observations. Aucune ne porte de gravité par défaut : la gravité se décide ensuite, page par page, sur la question « le titre principal et l'organisation permettent-ils de comprendre clairement la page ? », croisée avec le rôle business de la page.

1. **H1 unique et présent** — relever 0 H1 ou plusieurs H1. Un H1 absent sur une page business dont rien d'autre ne dit le sujet pèse ; un second H1 sur un bloc visuel qui n'ambiguïse pas la page ne pèse pas.
2. **Hiérarchie sans saut de niveau** — relever un H1 → H3 sans H2. L'ordre des headings n'est pas une exigence de classement : le saut devient un défaut seulement s'il rend la page moins compréhensible.
3. **H1 vs intention** — le H1 répond-il à la requête principale GSC de la page, ou est-ce un H1 générique / le nom du site / un slogan ? Nécessite GSC.
4. **H2 vs micro-intentions** — les H2 couvrent-ils les requêtes GSC où la page est en position 4-20 (signal « Google la trouve pertinente mais incomplète ») ? Nécessite GSC.
5. **Hn génériques** — relever « Introduction », « Conclusion », « Pour aller plus loin », « En résumé ». Signal d'un contenu faible ou écrit sans matière propre selon le standard éditorial de l'utilisateur ; pas un frein SEO démontré pour cette seule raison. La gravité vient de ce que le H2 cache : s'il coiffe une réponse réelle, il se réécrit en P3 ; s'il coiffe du vide, c'est `seo-contenu-pertinence` qui porte le défaut.
6. **Hn sur-optimisés** — le mot-clé exact répété identique dans chaque Hn = sur-optimisation.
7. **Passage Ranking** — chaque H2 doit pouvoir se lire comme une réponse autonome, extractible en featured snippet ou citable par un LLM sans le reste de la page.
8. **Templating inter-pages** — sur un cluster de pages similaires (satellites, fiches produit, pages ville), comparer les Hn entre pages : des intitulés identiques mot pour mot sur plus de 2 pages (hors H1) ouvrent un **examen**, pas un défaut. « Fonctionnement », « Tarifs », « Conditions » partagés par dix fiches sont normaux si les réponses dessous diffèrent. L'examen porte sur la différenciation des réponses et des intentions (lire deux pages du cluster côte à côte, ou renvoyer vers `seo-contenu-pertinence`, contrôle 4 « valeur propre »). C'est un contrôle inter-pages, pas un contrôle par page.

### Étape 3 — Croiser

- Pages business (requêtes Phase 0 du workflow d'audit, ou fournies par l'utilisateur) avec un Hn cassé ou hors-sujet → priorité haute.
- Recouper avec les données GSC : un cluster de pages au contrôle 8 (intitulés identiques) et à zéro impression GSC renforce le signal d'examen ; c'est une corrélation à écrire comme telle, pas une cause démontrée.
- Ne jamais conclure à une cannibalisation depuis le seul Hn : un Hn différencié entre deux pages proches n'élimine pas un conflit de requêtes (à vérifier côté GSC, skill `seo-cannibalisation`), et un Hn similaire n'en prouve pas un (à vérifier aussi).

## Sortie de pré-décision (obligatoire)

Ce skill est une brique de `audit-complet-v2` (workflow `audit-complet-v2/workflow-audit.md`, Phase 3) et peut aussi tourner seul. Sa sortie de pré-décision suit le même format que les autres skills d'audit — `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/audit/YYYY-MM-DD-slug-structure-hn.md` en usage autonome, ou intégré à l'annexe Phase 3 en usage via `audit-complet-v2`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel (pages business touchées, corrélation GSC), jamais sur le nombre d'anomalies ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque Faible / Moyen / Élevé ; toute action qui implique une réécriture à l'échelle d'un cluster porte « À valider avant déploiement »
6. Ce que les données ne permettent pas de conclure, et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Règles : chaque information est typée FACT, HYPOTHESIS ou ACTION, jamais une hypothèse écrite comme un fait ; un problème existe une seule fois (ID), les observations qui parlent du même problème fusionnent ; le contrôle 8 (templating) ne se déclare qu'à partir de 2 pages comparées, jamais sur une page isolée ; jamais de recommandation automatique de réécriture en masse sans échantillon validé par l'utilisateur d'abord ; Google n'est jamais anthropomorphisé ; phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution : aucun ID technique ni mot anglais dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème Hn détecté sur les URL inspectées », pas « Sain » si l'échantillon est partiel) ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

## Sortie obligatoire

```markdown
# Audit structure Hn — {domaine} — {date}

## Tableau par URL

| URL | H1 ok | Hiérarchie ok | H1↔intention | H2↔requêtes GSC | Hn génériques | Templating | Verdict |
|---|---|---|---|---|---|---|---|

## Observations à examiner en tête (gravité justifiée, jamais automatique)

- {page business dont le titre principal et l'organisation ne permettent pas de comprendre la page : H1 absent sans autre repère, H1 hors-sujet, structure absente ; suspicion de dépendance au rendu à vérifier}
- Pour chacune : observation prouvée → conséquence justifiée sur la compréhension de la page → bénéfice attendu de la correction

## Recommandations Hn par page prioritaire

Le H1/H2 cible précis, jamais « revoir la structure ».

## Limites

- {contrôles non testables (pas de GSC), échantillon vs périmètre complet}
```

## Garde-fous (NON-NÉGOCIABLES)

- Le périmètre suit le sitemap complet du site, pas un plafond arbitraire de 50 URLs — un site à 800 pages s'audite en 800, en priorisant si le budget tokens l'exige (pages GSC + business d'abord, cf. Phase 3 du workflow).
- Ne jamais recommander une réécriture Hn à l'échelle d'un cluster sans échantillon validé d'abord.
- Ne jamais déclarer une cannibalisation depuis le seul Hn : renvoyer vers `seo-cannibalisation` pour la confirmation GSC.
- Lecture seule. Pas de modification du site.

## Enchaînement workflow

En amont : `indexation-check` (une page non indexée n'a pas besoin d'un Hn parfait en priorité). En aval : `seo-cannibalisation` (un Hn qui se chevauche entre 2 pages est un signal à vérifier, pas une preuve), `seo-brief-contenu` (les réécritures Hn recommandées ici se briefent avec ce skill avant rédaction), `maillage-systeme` (un cluster templé en Hn est souvent aussi sous-maillé — vérifier la corrélation).

## Sauvegarde

Output dans `wiki/audit/YYYY-MM-DD-slug-structure-hn.md` en usage autonome selon hook §7 AGENTS.md ; intégré à l'annexe Phase 3 du rapport `audit-complet-v2` sinon.

## Concepts liés

`passage-ranking` · `surprise-gap` · `grounding-score` · `fully-meets`
