---
name: maillage-systeme
description: Audite et construit le maillage interne d'un site sans Search Console. Déclencheurs : "audite le maillage", "pages orphelines", "plan de maillage".
---

# Maillage interne

## Ce que tu donnes à Claude

- L'URL du sitemap, ou la liste des articles (titre, slug, mot-clé visé).
- Tes 3 à 5 mots-clés piliers.
- Tes pages d'offre : audit, contact, devis, outil.

## Consigne

> Audite le maillage de monsite.fr. Mes pages d'offre : [URL].

## Étape 0 : crawl

```bash
python3 ~/.claude/skills/maillage-systeme/scripts/crawl_graph.py https://monsite.fr/sitemap.xml -o ./maillage-data
```

Seul `index.json` entre dans la conversation.

Un lien présent sur 80 % des pages ou plus est un lien de gabarit. Il ne compte pas.

## Étapes

1. Classe chaque page : Know ou Do.
2. Regroupe en piliers de 3 pages minimum, avec un hub chacun.
3. Compte les liens du corps par pages sources distinctes. Repère orphelines et impasses.
4. Pour chaque lien à créer : passage et 3 ancres (exacte, partielle, sémantique).
5. Classe par rang :
   - page d'offre orpheline ;
   - lien Know vers Do ;
   - hub vers satellite ;
   - orpheline hors offre ;
   - lien entre piliers.

## Critères d'une ancre

- Elle dit ce que la cible promet.
- La phrase reste fluide sans le lien.
- Elle n'est pas déjà utilisée vers la même cible.
- Les 5 mots autour parlent du sujet de la cible.

Un critère raté : l'ancre est rejetée.

## Sortie

- Piliers et hubs.
- Tableau : page, entrants, sortants, statut.
- Plan de liens : source, cible, passage, ancres, justification.
- Diagnostic en une phrase, 3 actions P1 maximum.
- Ce que les données ne permettent pas de conclure.

## Avant d'ajouter les liens

- Lis chaque passage à voix haute sans le lien. S'il boite, rejette le lien.
- Insère par lots de 10 à 20.
- Relance le crawl après chaque lot.
- Critère de fin : zéro page d'offre orpheline.

## Règles

- Aucun score numérique.
- Une page légale orpheline n'est pas un problème.
- Liens dans le texte, jamais en « Voir aussi ».
- Jamais de lien vers l'accueil depuis le contenu.

Enregistre la sortie dans `AAAA-MM-JJ-<site>-maillage.md`.
