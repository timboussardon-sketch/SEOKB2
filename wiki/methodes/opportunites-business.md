---
type: methode
title: Opportunités business — méthode commune Audit et GEO
aliases: [opportunites-business-contrat-phase-b]
tags: [seo, geo, business, calcul, methode]
created: 2026-11-05
updated: 2026-11-05
sources: 2
confidence: high
status: stable
---

# Opportunités business — méthode commune Audit et GEO

Contrat économique `0.1.0`, validé par Tim après la livraison de phase B le 5 novembre 2026. L’intégration `business-v1` ajoute les adaptateurs et rendus sans changer les formules. Son installation est tracée par le manifeste de déploiement ; la présence de cette méthode seule ne prouve pas le chargement d’un workflow.

Les résultats et limites des vérifications sont dans [[queries/2026-11-05-opportunites-business-phase-b]] et [[sources/2026-11-05-opportunites-business-phase-b-verification]]. Aucun résultat de test fictif n’est une prévision pour un client.

## 1. Ce que produit le contrat

Le dossier conserve les offres et le périmètre, les besoins, les mesures, les concurrents observés, les groupes de requêtes, les opportunités et leurs actions. Les scénarios économiques et les panels de visibilité restent des objets distincts.

Le flux suit : demande observée → opportunité accessible → valeur estimée → moyens nécessaires → mesure des résultats. Une étape dont les données manquent reste ouverte. La présence dans une liste de requêtes, une SERP ou une réponse IA ne donne pas automatiquement accès aux étapes économiques.

Le calculateur vérifie les types, références, unités, horizons et formules. Le consultant vérifie les sources, les interprétations et la pertinence commerciale. Tim conserve les choix et les validations. [[moc/doctrine-seo-reference]]

## 2. Identifier le périmètre

`offers` décrit l’offre annoncée, son objectif commercial, la conversion recherchée et les contraintes connues. `scopes` précise les offres couvertes, segments, pays et langues. Une priorité déclarée par le dirigeant conserve sa source ; une priorité déduite du site reste une hypothèse.

`explored_need_ids` conserve tous les besoins examinés. `retained_opportunity_ids` identifie les opportunités proposées pour le cycle. Le choix initial des cinq mots-clés de GEO reste une règle de son point d’entrée ; le contrat commun peut conserver une exploration plus large. Le tri d’Audit conserve sa propre couverture documentaire.

Une capacité commerciale désigne le nombre de clients livrables sur l’horizon. Une capacité de production désigne les heures disponibles par semaine. Le contrat ne convertit jamais automatiquement des points ou des catégories d’effort en heures.

## 3. Conserver la provenance

Chaque source a un identifiant, un type, une URL ou un chemin, la date de collecte, la date du document si connue, un emplacement précis dans la source et des limites. L’empreinte du fichier local est conservée lorsqu’elle existe. Une collecte réutilisée garde sa date d’origine ; la date de consultation de l’archive n’est pas une nouvelle date de mesure.

Chaque valeur numérique figure dans `metrics` avec quantité, unité, canal, périmètre, période, source, emplacement et justification. Les quantités sont explicites : recherches mensuelles, impressions GSC, clics GSC, sessions, taux de qualification, transformation, revenu par client, coût variable par client, investissement ou capacité. Le CPC n’est pas un paramètre économique de ce modèle.

| Statut de donnée | Condition |
|---|---|
| `observed` | Valeur lue dans une source identifiée, avec son périmètre et sa période |
| `estimated` | Estimation d’un fournisseur ou calcul documenté ; origine et limites explicites |
| `hypothesis` | Valeur proposée, auteur et justification requis ; à modifier ou valider |
| `unavailable` | Valeur `null`, motif d’absence conservé |

Une valeur zéro est admise avec sa provenance. Elle ne remplace jamais une valeur inconnue. Un export Keyword Planner sans fenêtre de moyenne connue conserve cette limite ; sa date de relevé ne devient pas la période économique d’un scénario.

La validation structurelle ne prouve pas qu’une source affirme réellement la valeur : cette relecture reste humaine. Le calculateur n’ouvre pas les pages externes, n’interroge aucun fournisseur et n’invente aucun paramètre manquant.

## 4. Demande, concurrence et regroupements

`needs.kind` distingue recherche mesurée, besoin observé et hypothèse. Une recherche déclarée mesurée doit référencer une mesure de recherche disponible. Les mots d’un prospect gardent leur formulation, leur extrait, leur attribution et leur contexte.

`actors.roles` distingue concurrent commercial, concurrent SERP, source citée par une IA et entreprise étudiée. Chaque rôle est justifié par des sources et des URL. La visibilité ne démontre ni les ventes ni la part de marché d’un acteur.

`groups.method` accepte une normalisation de variantes, une hypothèse d’intention ou une comparaison SERP. Un regroupement SERP exige une liste de résultats pour chaque besoin, les sources, la date, le moteur, le pays, la langue, l’appareil, la profondeur et la règle de comparaison. Le calculateur retire uniquement les fragments d’URL pour comparer les résultats ; il ne fusionne pas des paramètres ni des domaines au jugé.

La sortie donne les URL communes et le nombre de résultats réellement relevés de chaque côté. Elle ne convertit pas un recouvrement en validation d’intention. Le statut humain reste séparé. Un regroupement sémantique sans relevé conserve `intent_hypothesis`, même si ses termes se ressemblent.

## 5. Sélectionner les opportunités

Une fiche `opportunities` relie offre, périmètre, besoins, sources, acteurs, URL, actions, scénarios et mesure de résultat. Les trois portes portent chacune un statut et une justification : adéquation à l’offre, intention business, opportunité démontrée.

`retain` exige trois portes satisfaites et étayées. `investigate` conserve une piste qui manque de preuves. `defer` reporte une opportunité selon ses conditions ; `exclude` conserve la raison d’exclusion. Le rang est un ordre proposé, accompagné de `priority_reason`, jamais une note calculée.

Les actions couvrent page existante, nouvelle page, preuve, distribution, offre, conversion, suivi commercial, investigation et technique. Elles conservent un responsable proposé, des dépendances, des références de coût et d’effort et leur validation. Une correction technique peut exister sans gain commercial attribué.

Le validateur refuse une dépendance inconnue ou circulaire. Il refuse une date planifiée sans capacité positive et sans source de cette date. Le calculateur n’assigne aucune date. Avec une capacité inconnue, il affiche `capacity_unknown` ; avec zéro, `no_capacity`. Les responsables, charges et coûts inconnus restent vides.

## 6. Scénarios économiques

Les paramètres sont des références aux métriques, pas des nombres recopiés dans chaque rendu. Chaque scénario donne son périmètre, sa devise, son horizon, sa convention de revenu, sa définition des coûts, la justification du transfert des taux historiques et les actions conditionnantes.

Le coût d’investissement est le montant additionnel total de l’horizon, issu d’un devis, d’une mesure ou d’une hypothèse documentée. Sa source détaille les charges initiales et récurrentes, internes et externes. Cette version ne produit pas un devis à partir de catégories d’effort. Le coût de livraison est séparé ; le validateur refuse un investissement déclaré comme l’incluant déjà.

### Acquisition seule

Le paramètre de trafic est un nombre de sessions **additionnelles** sur l’horizon.

```text
Leads qualifiés additionnels = sessions additionnelles × taux de qualification
Clients additionnels potentiels = leads additionnels × taux de transformation
CA additionnel potentiel = clients additionnels × revenu par nouveau client sur l’horizon
Coût variable additionnel = clients additionnels × coût variable de livraison par client
Contribution avant investissement = CA additionnel − coût variable additionnel
Contribution après investissement = contribution avant investissement − investissement additionnel
```

Le modèle ne déduit pas des sessions d’un volume Google. Une hypothèse de trafic doit être renseignée et justifiée en amont. Aucun taux de clic par défaut n’est fourni ; les clics GSC, les sessions analytics et les citations IA gardent des quantités distinctes.

### Trafic et conversion modifiés

`full_funnel` compare un état actuel et un état futur sur des durées comparables. Les périodes restent identifiées et la saisonnalité doit être discutée dans la justification. Le trafic futur représente cette fois le total envisagé.

```text
Clients actuels calculés = trafic actuel × qualification actuelle × transformation actuelle
Clients futurs calculés = trafic futur × qualification future × transformation future
Variation de clients = clients futurs − clients actuels
Variation de CA = CA futur − CA actuel
Variation de contribution = contribution future − contribution actuelle
Contribution additionnelle après investissement = variation de contribution − investissement additionnel
```

Chaque étage est calculé séparément. Des clients calculés à partir de taux restent des estimations, même lorsque les paramètres viennent de mesures. Les taux futurs conditionnés à une relance commerciale ou à un changement de formulaire ne sont pas attribués au seul SEO. Une variation négative est conservée.

### Potentiel et capacité de livraison

`future_potential` montre la projection avant la contrainte de livraison. `future_deliverable` utilise le minimum entre clients potentiels et capacité renseignée. En acquisition seule, cette capacité correspond aux clients additionnels ; en comparaison complète, elle correspond aux clients totaux. La sortie rappelle cette convention.

Si la capacité est inconnue, le potentiel peut rester calculable, tandis que le résultat sous capacité reste `null`. La demande non servie est affichée séparément. Une capacité nulle est respectée. Les actions encore non réalisées apparaissent dans `conditional_on_action_ids` : le calcul ne démontre pas qu’une opportunité est déjà accessible.

### Étages incomplets et unités

Un revenu par client doit porter sur l’horizon du scénario. Une valeur vie client à horizon indéfini ne peut pas être utilisée comme revenu mensuel. Une devise différente, un trafic futur hors période, un taux supérieur à un ou des périodes actuelles/futures de durées différentes sont refusés. Les changements de cohorte, de segment et les délais de maturation restent à examiner avant de réutiliser un taux.

Si les coûts manquent, le CA peut être calculé sans contribution. Si la conversion manque, ni clients ni revenu ne sont estimés. Une multiplication comportant une inconnue reste inconnue, même si un autre facteur vaut zéro. Le message est « non estimable avec les données disponibles », avec les paramètres manquants.

Les valeurs sont calculées avec `Decimal`, précision de travail de quarante chiffres. Les résultats JSON les sérialisent sous forme de chaînes décimales ; `null` reste `null`. Les nombres de clients potentiels peuvent être fractionnaires : ce sont des valeurs attendues. L’aperçu arrondit les montants monétaires à deux décimales ; le JSON garde les valeurs non arrondies.

Prudent, central et favorable sont des jeux distincts de paramètres justifiés. Aucun multiplicateur standard ne les génère. Les scénarios n’ont aucun total automatique, y compris lorsqu’ils concernent plusieurs actions ou canaux.

## 7. Dédupliquer sans masquer les limites

Une métrique agrégée possède une `counting_key` représentant l’unité de mesure fournisseur ou l’unité observée. Deux variantes qui partagent cette clé sont comptées une seule fois, à condition que valeur, période, périmètre, quantité et unité concordent.

Plusieurs clés ne sont additionnées que si leur indépendance est documentée. Un chevauchement inconnu, une valeur absente, un conflit entre mesures identiques, une clé absente ou un mélange de canaux produit un résultat indisponible avec sa raison. Les taux et valeurs par client ne sont jamais additionnés.

Des totaux par groupes GSC qui partagent des requêtes ne suffisent pas à obtenir un total unique : il faut revenir aux lignes élémentaires ou laisser le total absent. Pour plusieurs actions sur la même demande, produire un scénario conjoint. La déduplication entre canaux repose sur une règle d’attribution documentée ; ce module ne crée pas d’identité client fictive.

## 8. Mesurer la visibilité

Un panel définit questions exactes, moteur, modèle connu, mode de collecte, pays, langue, appareil, période, répétitions prévues et acteurs suivis. Chaque réponse ou relevé a un identifiant, sa date, une source, un statut valide ou échec et des détections explicites. Une mention positive exige un extrait ; une citation exige aussi une URL. Une recommandation explicite implique une mention ; elle n’est pas déduite de la seule présence du nom.

Les calculs sont faits par question et par moteur :

```text
Taux de mention = réponses positives / réponses valides effectivement évaluées pour la mention
Taux de citation = réponses avec citation / réponses valides effectivement évaluées pour la citation
Taux de recommandation = recommandations explicites / réponses valides évaluées pour ce critère
Part de voix sur le panel = paires marque-réponse / paires acteur-réponse pour les acteurs suivis
```

Les détections inconnues sont exclues du dénominateur du critère et comptées explicitement. Les erreurs sont exclues ; les runs manquants restent visibles. Pour la part de voix, seules les réponses où tous les acteurs suivis ont été évalués entrent dans le calcul. Une paire acteur-réponse est comptée une fois.

Une SERP utilise la profondeur contrôlée et une URL avec position dans cette profondeur pour établir la présence. Elle ne reçoit pas de recommandation IA. Aucun résultat de panel n’entre dans une formule de trafic ou de revenu.

Les panels IA sous le protocole habituel de trente relevés valides par question et moteur sont signalés. Le calcul descriptif d’un petit échantillon n’atteste pas sa représentativité. Les autorisations de coût et les validations de panel du workflow GEO restent requises en phase C. Aucun relevé payant n’est lancé ici.

## 9. Accords humains et suivi

Une validation conserve statut, auteur, date, message et empreinte du contenu. Le statut `approved` seul est refusé. L’empreinte couvre le dossier entier, en excluant les métadonnées d’approbation elles-mêmes. Si une donnée change, les accords portant sur l’ancienne empreinte deviennent effectivement `needs_revision` ; leur texte historique reste intact.

Ce choix est volontairement strict pour la première version : une modification locale peut faire réexaminer plusieurs accords. Une granularité plus fine nécessiterait un graphe de dépendances validé. Le calculateur ne signe aucun accord et n’exécute aucune action.

Après validation, toute modification de formule impose une nouvelle version de méthode et de calculateur, avec les nouvelles empreintes. La version de méthode appartient au contenu approuvé ; elle ne se remplace pas silencieusement.

Chaque opportunité conserve indicateur, formule, baseline, source, responsable, date de revue, attribution et critères de poursuite, révision et arrêt. Les résultats observés alimenteront [[preuves/index]] ; les nouvelles dépenses restent des propositions à arbitrer. Vérifier [[ops/sante-automatisations]] avant de transformer une absence de collecte en conclusion commerciale.

## 10. Commandes et fichiers

Depuis la racine de seo-kb, utiliser l’interpréteur `.venv/bin/python`, où `jsonschema 4.25.1` est disponible. Le Python système ne possède pas cette dépendance. Aucun paquet n’a été installé pendant cette phase.

```bash
.venv/bin/python -B wiki/methodes/opportunites-business/valider.py DOSSIER.json
.venv/bin/python -B wiki/methodes/opportunites-business/calculer.py DOSSIER.json --output NOUVEAU-RESULTAT.json
.venv/bin/python -B wiki/methodes/opportunites-business/rendu.py NOUVEAU-RESULTAT.json --audience audit --output NOUVEL-APERCU.md
.venv/bin/python -B wiki/methodes/opportunites-business/rendu.py NOUVEAU-RESULTAT.json --audience geo --output AUTRE-APERCU.md
.venv/bin/python -B wiki/methodes/opportunites-business/tests/run_checks.py NOUVEAU-DOSSIER-DE-VERIFICATION
```

Les sorties existantes ne sont pas écrasées. Les commandes refusent l’écriture dans `raw/` et dans le fichier d’entrée. Le calcul préserve les paramètres, les sources et les empreintes du code chargé. Le résultat commun alimente les deux aperçus, qui n’effectuent aucun calcul métier.

## 11. Compatibilité et limites

Les nouvelles missions utilisent `integration.py` pour charger et calculer une fois le contrat, produire les blocs HTML et inscrire les chemins et empreintes réellement chargés. Les anciens dossiers sans marqueur `business-v1` gardent leur chaîne historique. Un ancien JSON n’est jamais transformé implicitement.

`importer.py SOURCE --review REVUE.json --output NOUVEAU-DOSSIER` réutilise les octets du contrat et préserve ses sources et dates. La revue précise auteur, date, justification, `source_sha256`, `scope_compatible: true`, et `freshness: current_for_scope | retained_with_limits`. Un périmètre incompatible appelle un nouveau cadrage. Pour un JSON historique, ajouter `--contract CONTRAT-RELUE.json --mapping CORRESPONDANCES.json` : une correspondance `{metric_id, pointer, rationale}` par valeur disponible non hypothétique. Les accords historiques restent dans la copie originale ; aucune approbation transférée par l’adaptation.

Pour les rendus, lire [[methodes/opportunites-business-integration]]. La méthode ne lance aucun collecteur. Les scénarios fictifs des tests restent hors des dossiers clients.

Le contrat ne vérifie pas automatiquement la véracité des extraits, la causalité d’un gain, la qualité statistique des taux ni la complétude d’un marché. Il ne détermine pas les coûts, ne collecte pas le CRM et ne prédit pas un délai de résultat. Ces limites restent affichées dans les livrables concernés.

TASM n’est pas repris comme concept propriétaire. L’auteur du post d’origine reste à identifier avant toute réutilisation attribuée.
