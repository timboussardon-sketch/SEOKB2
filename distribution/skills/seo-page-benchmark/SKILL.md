---
name: seo-page-benchmark
description: "Rédige une page de benchmark chiffré et sourcé, citable par les IA. « page benchmark », « [A] vs [B] »."
---

# Skill — Page de benchmark chiffré (citable IA)

## Quand utiliser ce skill

Rédige une page de benchmark chiffré conçue pour être CITÉE par les moteurs génératifs. Cible les requêtes "[A] vs [B]", "benchmark [catégorie]", "[métrique] moyen par [secteur]". Le cœur est un tableau comparatif où chaque cellule chiffrée porte sa source (spec officielle ou mesure first-party). Jamais de claim marketing repris sans vérification, jamais de chiffre inventé. Verdict par cas d'usage, pas de "meilleur" absolu. Le système rédige, il n'hallucine jamais.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "page benchmark", "benchmark [catégorie]", "comparatif chiffré", "[A] vs [B]", "[métrique] moyen par secteur", "tableau comparatif sourcé", "crée un benchmark", ou quand il veut une page de comparaison citable par les IA.

Diffère de `seo-page-statistiques` (chiffres sur un sujet) et de `seo-page-etude-originale` (data first-party). Ici on COMPARE des options sur des métriques mesurées.

## Quand déclencher
Construire une page de comparaison quantifiée qui devient la source que l'IA cite pour "X vs Y" ou "la moyenne de [métrique]". Format actualité : datée, mise à jour quand les valeurs bougent. Rédigée par le système, jamais hallucinée.

## Posture
Un benchmark est un protocole de mesure, pas un avis. Chaque valeur du tableau est une donnée sourcée. Pas de "meilleur" absolu : un verdict par cas d'usage. Tout chiffre sans source = `[À SOURCER]`.

## Règle anti-hallucination (non négociable)
1. Chaque métrique de chaque ligne = une source : spec officielle de l'acteur, mesure first-party documentée, ou organisme de test reconnu. URL + date.
2. Jamais reprendre un claim marketing ("le plus rapide", "le plus précis") sans le vérifier ou le sourcer comme déclaratif.
3. Si une valeur manque → `[À SOURCER]` dans la cellule, jamais d'estimation déguisée en fait.
4. La rédaction ne suffit pas : chaque cellule passe la **Vérification des sources** ci-dessous (fetch réel), pas une simple relecture.

## Sources autorisées
1. **Sites officiels des acteurs comparés** pour les specs (cf. `feedback_marque-b_sources_sites_marques` : specs depuis les sites officiels, jamais de revendeurs/agrégateurs).
2. **Mesures first-party** : tests réels avec protocole documenté (l'angle le plus citable et le plus différenciant).
3. **Médias / labos de test reconnus** en repli, datés.
- **Interdits** : revendeurs, agrégateurs, comparateurs affiliés, claims non vérifiables, data tierce reprise sans citation.

### Règle de nommage
- Contenu éditorial (site de Tim, blog) : nommer les acteurs comparés est permis, avec source pour chaque valeur.
- Copy client / Fusionn : suivre `feedback_pas_de_marques_directories_seo` et `feedback_pas_de_mot_concurrent` (formulations génériques, data chiffrée sans attribution nominative). Adapter selon le contexte de publication.

## Pipeline (5 étapes)
1. **Cadrer** : la catégorie comparée, les options retenues, les métriques mesurables, la requête-ancre.
2. **Collecter** les valeurs (specs officielles + mesures first-party) via WebSearch/WebFetch. Logger source + date par cellule.
3. **Définir le protocole** : comment chaque métrique est mesurée (sinon le tableau n'est pas crédible pour l'IA).
4. **Rédiger** selon le modèle, verdict par cas d'usage.
5. **Auto-check anti-hallucination** + score GEO (extractibilité du tableau, fraîcheur).

## Modèle de page
```
H1 : Benchmark [catégorie] [année]   (ou : [A] vs [B] : le comparatif chiffré [année])

[Intro answer-first] : le verdict en une phrase (ex. "Sur la métrique X, A devance B de N ; sur Y, l'inverse.")

## Le comparatif en un tableau
| Option | Métrique 1 | Métrique 2 | Métrique 3 | ... |
|--------|-----------|-----------|-----------|-----|
| A      | valeur (source) | ... | ... |
| B      | ... |
(chaque cellule = valeur + source ; [À SOURCER] si manquante)

## [Critère 1]  (H2 par métrique, analyse courte sourcée)
## [Critère 2]
...

## Méthodologie
Comment chaque métrique a été mesurée, sources des specs, date du relevé.

## Quel choix selon le cas
Verdict par usage / profil, pas de "meilleur" universel.

## Où ce verdict ne tient pas (contre-analyse, obligatoire)
Les cas où le classement s'inverse, les limites du protocole de mesure, les critiques des sources, le contexte où l'option « perdante » gagne. Un benchmark sans son envers est un parti pris.

## FAQ
"quelle est la moyenne de [métrique]", "A ou B pour [cas]" : réponse 1-2 phrases sourcée.

## Sources
Liste complète : acteur, document, date, URL, date de consultation.
```

## Optimisation GEO
- Le tableau en premier : c'est l'objet le plus extractible par les IA.
- Verdict answer-first dès l'intro.
- Fraîcheur : année dans H1/title, `dateModified` à jour.
- Schema.org : `Table` / `Dataset`, `Article` + citations.
- Bloc Sources obligatoire.

## Vérification des sources (obligatoire, passe séparée du rédacteur)
Le tableau ne vaut que si chaque cellule est vérifiée mécaniquement. Idéalement par un agent de vérification distinct.
1. **Inventaire** : chaque cellule chiffrée du tableau avec sa source annoncée (URL spec officielle ou protocole de mesure first-party).
2. **Fetch obligatoire** : `WebFetch` la page officielle de l'acteur et confirmer la valeur. URL non fetchée = source nulle (anti-URL fabriquée).
3. **Source primaire exigée** : spec depuis le site officiel de l'acteur ou mesure first-party documentée, jamais un revendeur ni un comparateur affilié. Un claim marketing non vérifiable est marqué comme déclaratif, pas comme fait.
4. **Verdict par cellule** : Vérifié / Fragile / Non vérifiable → `[À SOURCER]` dans la cellule si non Vérifié.
5. **Blocage** : tableau non « prêt » tant que chaque cellule n'est pas Vérifié ou explicitement `[À SOURCER]`. La méthodologie doit décrire comment chaque métrique a été mesurée.

## Gate de publication (seuils, non optionnel)
Avant « publiable », trois contrôles, idéalement par une passe adversariale distincte :
1. **`seo-geo-audit`** : aucun rouge sur Grounding ni Freshness, Surprise non « médiocre ». Sous le seuil → réécriture.
2. **`breves-factcheck`** : verdict adversarial par cellule/claim (Confirmé / Fragile / Non vérifiable / Contredit) ; tout Contredit retiré.
3. **`anti-ai-writing`** + verdict par cas d'usage (jamais de « meilleur » absolu non justifié).
4. **Contre-analyse présente et sourcée** : les cas où le verdict s'inverse et les limites de mesure. Sans elle, refus de la gate.
Respecter la règle de nommage selon le contexte de publication (éditorial vs copy client). Sortie : statut explicite + table des cellules avec verdict et source. **Relecture humaine finale obligatoire.**

## Sauvegarde
Page draft markdown dans le dossier du projet. Jamais publier sans relecture des sources.

## Concepts liés
`grounding-score` · `information-gain` · `surprise-gap` · `data-proprietaire` · `anti-ai-writing` · skill `seo-geo-audit`
