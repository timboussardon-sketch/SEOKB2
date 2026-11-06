---
name: seo-page-etude-originale
description: "Rédige une page d'étude sur data first-party. « étude originale », « publie notre data »."
---

# Skill — Page d'étude originale (data first-party, citable IA)

## Quand utiliser ce skill

Rédige une page d'étude originale fondée sur de la data FIRST-PARTY (logs, GSC, data clients anonymisée), le format le plus cité par les moteurs génératifs parce que la donnée n'existe nulle part ailleurs. Cible les requêtes "étude [sujet]", "[sujet] data", "selon une étude [sujet]". Méthodologie honnête (échantillon réel, période, limites), faits séparés des interprétations, jamais de résultat inventé ni d'échantillon gonflé. Le système rédige, il n'hallucine jamais.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "étude originale", "page étude", "étude sur [sujet]", "[sujet] data", "étude first-party", "publie notre data", "étude propriétaire", "transforme nos logs en étude", ou quand il veut une page-étude citable par les IA à partir de notre data.

Diffère de `seo-page-statistiques` (agrège des chiffres externes) et `seo-page-benchmark` (compare des options). Ici LA donnée est produite par nous.

## Quand déclencher
Transformer de la data propriétaire en étude publiable, conçue pour devenir LA source primaire que l'IA cite. C'est la page phare (peu nombreuses, profondes), pas du pSEO de masse. Rédigée par le système, jamais hallucinée.

## Posture
Une étude originale tient par sa méthodologie. La data est à nous, donc la crédibilité repose sur l'honnêteté du protocole : échantillon réel, période réelle, limites assumées. Un fait n'est pas une interprétation : on sépare les deux (cf. boucle `agent-synthetic`).

## Règle anti-hallucination (non négociable)
1. Aucun résultat inventé. Le chiffre publié est celui que la data dit, point.
2. Échantillon (n) et période RÉELS, jamais gonflés. Si n est petit, on le dit et on nuance.
3. Faits ≠ interprétations : le fait est sourcé sur la data, l'interprétation est marquée comme telle.
4. Tout chiffre de contexte externe suit les règles de `seo-page-statistiques` (source primaire datée, sinon `[À SOURCER]`).
5. La rédaction ne suffit pas : chaque résultat passe la **Vérification** ci-dessous (traçabilité à la data brute + anonymisation), pas une simple relecture.

## Sources autorisées
1. **Data first-party de Tim (le cœur)** : logs Fusionn (`seo-kb/raw/fusionn/`), GSC sur 20+ propriétés (export `admin-gsc-export` + secret dédié), data clients anonymisée. Cf. mémoire `project_etudes_originales` (pilote logs Fusionn, études dans `raw/etudes-seo/`).
2. **Recoupement externe** pour contextualiser le finding (sources primaires datées uniquement).
- **Interdits** : data clients non anonymisée, échantillon non vérifiable, résultat extrapolé présenté comme mesuré.

## Pipeline (5 étapes)
1. **Cadrer** : la question d'étude + la requête-ancre ("étude [sujet]") + la data disponible pour y répondre. Si on n'a pas la data, on ne fait pas l'étude (on bascule sur `seo-page-statistiques`).
2. **Analyser** la data : extraire les findings, noter n, période, méthode de calcul.
3. **Vérifier** : recouper, tester la solidité (cf. skill `breves-factcheck` pour l'esprit adversarial), séparer faits et interprétations.
4. **Rédiger** selon le modèle, finding chiffré dans le titre.
5. **Auto-check anti-hallucination** + limites explicites + score GEO.

## Modèle de page
```
H1 : Étude : [le finding chiffré, énoncé sec]   (ex. "Étude : le CTR chute de N% quand un AI Overview apparaît")

## En résumé
Le finding principal en 2-3 phrases + la méthode en une ligne (n, période, source de la data).

## Méthodologie
Échantillon (n réel), période, origine de la data, méthode de calcul, périmètre. Honnête sur les limites de représentativité.

## Résultats
### [Finding 1]  (H2 par résultat)
Le chiffre + sa visualisation (table/graphe) + interprétation CLAIREMENT séparée du fait.
### [Finding 2]
...

## Limites
Ce que l'étude ne dit pas. Obligatoire : c'est ce qui rend l'étude crédible pour un humain et pour l'IA.

## Contre-analyse (la lecture inverse, obligatoire)
Distincte des limites : on attaque son propre finding. Quelle autre lecture de la même data ? Quelles études disent l'inverse ? Le résultat tient-il hors de notre périmètre ? Conclure nuancé, jamais en absolu.

## Ce que ça implique
Lecture actionnable, sans surinterpréter au-delà de la data.

## Données et sources
Lien vers la data si publiable (ou méthode de reproduction), sources de contexte datées.
```

## Optimisation GEO
- Le finding chiffré dans le H1 et le title : c'est ce que l'IA cite.
- Answer-first : "En résumé" porte le résultat extractible.
- Surprise élevée : une donnée que personne d'autre n'a = forte mémorisation par les modèles (`concepts/surprise-gap`).
- Grounding maximal : méthodologie + limites = signal de fiabilité.
- Schema.org : `Dataset` + `ScholarlyArticle` / `Article`, `dateModified`.
- Bloc Données et sources obligatoire.

## Vérification (obligatoire, passe séparée du rédacteur)
La data est à nous, donc la garantie n'est pas « la source existe » mais « le résultat trace bien à la data brute et n'expose personne ».
1. **Traçabilité** : chaque chiffre publié renvoie à l'extrait de data exact (requête, fichier, colonne) qui le produit. Un résultat qu'on ne peut pas rejouer sur la data brute est retiré.
2. **Honnêteté du protocole** : n et période confirmés sur la data réelle, jamais arrondis vers le haut ni extrapolés. Si n est petit, c'est dit dans la méthodologie et les limites.
3. **Faits vs interprétations** : chaque ligne du corps est étiquetée fait (tracé data) ou interprétation (lecture). Pas de mélange.
4. **Chiffres de contexte externes** : passent la Vérification de `seo-page-statistiques` (fetch de la source primaire).
5. **Anonymisation (bloquant)** : aucune donnée client identifiante. Vérifier qu'aucun nom de site, URL, requête de marque ou volume isolé ne permet de réidentifier un client sans accord. Cf. `feedback_dpa_anonymisation_dashboards`.

## Gate de publication (seuils, non optionnel)
Avant « publiable », idéalement par une passe adversariale distincte :
1. **`breves-factcheck`** sur les findings : chaque résultat tient l'examen adversarial (la data dit-elle vraiment ça ? une autre lecture la contredit-elle ?). Tout Contredit ou non traçable est retiré.
2. **`seo-geo-audit`** : Surprise élevée (la donnée est inédite, c'est l'atout) et Grounding maximal (méthodologie + limites présentes). Section Limites obligatoire, sinon non publiable.
3. **`anti-ai-writing`** : prose, pas de survente au-delà de la data.
4. **Contre-analyse présente** : le finding est confronté à sa lecture inverse et aux études contraires. Sans elle, refus de la gate.
Sortie : statut explicite + liste des findings avec leur trace data et leur verdict. **Relecture humaine finale obligatoire, surtout sur l'anonymisation et l'accord client.**

## Sauvegarde
Page draft markdown dans le dossier du projet (`seo-kb/raw/etudes-seo/` pour le brouillon de travail, page publiable dans le repo concerné). Relecture humaine obligatoire avant publication, surtout sur l'anonymisation.

## Concepts liés
`surprise-gap` · `data-proprietaire` · `grounding-score` · `information-gain` · `anti-ai-writing` · skills `deep-research`, `breves-factcheck`, `seo-geo-audit` · mémoire `project_etudes_originales`
