---
type: query
title: "Template d'audit d'opportunité mot-clé pour la prospection Fusionn"
aliases: [audit-mot-cle-fusionn, template-prospection-mot-cle, keyword-opportunity-audit]
tags: [fusionn, prospection, mots-cles, micro-intentions, score-business]
created: 2026-09-14
updated: 2026-09-14
sources: 4
confidence: high
status: stable
---

# Template d'audit d'opportunité mot-clé pour la prospection Fusionn

## Décision

Le livrable prend un mot-clé et l'organise en trois tableaux : mots-clés avec volume/CPC, micro-intentions et objections avec preuves attendues. Le format sert d'audit-cadeau en relance sans ajouter de verdict ou de recommandation non demandée.

Le template exécutable est stocké dans `Code/prospection/modele-audit-mot-cle-fusionn.md`. Il contient la trame prospect, la méthode interne, un exemple « freelance SEO » et un prompt avec contrat JSON.

## Entrées minimales

Le mot-clé de départ ne suffit pas. Le meilleur mot-clé dépend de trois données business : l'offre vendue, le client recherché et la conversion attendue. L'URL du prospect et sa liste de pages servent ensuite à vérifier le content gap. Sans ces éléments, l'agent retourne les champs manquants et ne produit aucun gagnant.

Les données de demande restent facultatives pour une première hypothèse. Leur absence réduit la confiance. Aucun volume, CPC, trafic ou niveau de concurrence ne peut être inventé, conformément à [[sources/2026-01-15-organikk-mots-cles-seo-2026]].

## Calcul retenu

Le template reprend le Score Business déjà présent dans Fusionn :

`intention d'achat × 45 % + proximité à l'offre × 35 % + faisabilité × 20 %`

La faisabilité reste vide sans lecture de la SERP. Le `business_score` reste alors vide lui aussi. Le score fondé sur les deux facteurs disponibles s'appelle `strategic_score` et se normalise sur 100 : `(intention × 0,45 + proximité × 0,35) ÷ 0,80`. Il ne doit jamais être présenté comme une mesure de demande. Cette séparation corrige la faille de scoring identifiée dans [[syntheses/audit-doctrine-2026]] : un proxy LLM ne remplace pas une donnée de marché.

Le nombre de suggestions Google sert à corroborer une formulation. Il ne donne aucun point. Les données GSC, Keyword Planner et Suggest portent leur source, leur date, leur zone et leur langue.

## Séquence de production

L'agent génère 50 à 100 candidats en interne, puis livre 15 à 30 requêtes mesurées. Il regroupe les synonymes qui servent la même décision dans 8 à 12 micro-intentions. Il produit enfin 10 objections B2B minimum, chacune avec un verbatim précis et une preuve atomique attendue. Les verbatims non issus d'entretiens réels restent explicitement des hypothèses.

Le document visible conserve uniquement le titre, les métadonnées de mesure et trois tableaux :

1. mots-clés, volume, CPC et concurrence Ads ;
2. micro-intentions, requêtes représentatives, étape et décision ;
3. priorité, objection, verbatim prospect et preuve atomique attendue.

## Exemple « freelance SEO »

L'exemple sur `consultant SEO` contient 28 requêtes mesurées dans une extraction Google Ads homogène, 10 micro-intentions et 10 objections. Il reprend les tokens réels de Fusionn et transforme les lignes en cartes sur mobile pour supprimer le défilement horizontal.

Cette discipline garde l'audit utile sans transformer une déduction plausible en fait. Elle suit aussi la thèse de [[sources/2026-09-08-algorithme-ne-plus-vendre-audit-seo]] : l'actif commercial durable est le système capable de régénérer ce diagnostic, pas le PDF isolé.

## Pages liées

[[concepts/know-simple-know-do]] · [[concepts/mots-cles-actionnels]] · [[concepts/data-proprietaire]] · [[concepts/tabou-visibilite]] · [[entities/fusionn-io]]
