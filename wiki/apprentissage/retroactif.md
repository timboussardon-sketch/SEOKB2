---
type: apprentissage
title: Apprentissage rétroactif — 445 sessions
date: 2026-09-11
tags: [apprentissage, boucle, verdicts, retroactif]
status: auto-generated
sources: 445
confidence: high
---

# Apprentissage rétroactif — tout l'historique

> Passe unique du 2026-09-11 sur les 445 transcripts Claude Code (2026-05-03 → 2026-09-10).
> Extraction déterministe : `.claude/bin/apprentissage-extract.py --all`.
> **191 rejets ou casses, 76 validations, 194 corrections, 149 publications.**
>
> Tous les verbatims sont bruts, jamais reformulés. Un thème n'entre ici que si Tim l'a
> exprimé au moins deux fois sur des chantiers différents.

## Ce que le corpus dit d'abord

Sur 461 verdicts, **41 % sont des rejets ou des casses, 16 % des validations**. L'écart n'est
pas un taux d'échec : Tim parle quand quelque chose ne va pas et se tait quand c'est bon. Le
silence après une livraison compte donc comme acceptation, sinon le système n'apprend que des
échecs.

## Thèmes classés par occurrences

### 1. Rendu visuel refusé sur le premier jet — 16 occurrences

> « non horrible, fait un truc qui défile »
> « [Image #27] non ca cest horrible ! améliorer et propose 5 variantes de Ancré »
> « non cest horrible, l'ux est horrible et je ne veux plus d'icone dans la slide barre »
> « le rond au centre cest moche »
> « null a chier, recommence de zero »

Un visuel proposé seul est refusé environ une fois sur trois. Ce n'est pas un problème de goût,
c'est un problème de format de livraison : une proposition unique ne laisse rien à choisir.

**Règle** : ne jamais livrer une seule proposition visuelle. Voir le thème 3.

### 2. Correction partielle refusée — 10 occurrences

> « non pas deux correction, tu dois tout réécrire »
> « ca va pas. oublie tout et genenere moi 10 nouveaux favicon »
> « annule ca on repart sur super maillage »
> « on annule » (deux fois)
> « Non faut non dark mode et clair. et on annule leffet 3D, on repart de 0 sur le design »

Quand la direction est fausse, retoucher aggrave. Tim demande la reprise complète, pas le
rattrapage.

**Règle** : si un rejet porte sur la direction et non sur un détail, reprendre à zéro et le
dire, au lieu d'ajuster l'existant.

### 3. Plusieurs variantes avant de choisir — 6 occurrences

> « propose 3 hero en local, des trucs cools et incroybale, et je valide »
> « non ca va pas, propose 3 variante en local »
> « Je sais pas ca fait bizarre, propose 3 maniere de présenter logo et organikk en local et je valide »
> « améliorer et propose 5 variantes de Ancré »
> « oublie tout et genenere moi 10 nouveaux favicon »

**Règle** : toute demande visuelle (hero, logo, section, animation, favicon) se livre en 3 à 5
variantes montrées en local, jamais en une seule version posée dans le code.

### 4. Lien ou bouton mort — 8 occurrences

> « toute la partie compte ne fonctionne pas, je clic sur du vide »
> « les liens ne fonctionne pas »
> « Le hero est cassé, et le bouton réservé ne fait rien »
> « lorsque je clic sur worpdress j'ai Page not found »
> « WordPress répond 404 »

**Règle** : avant de rendre une page, cliquer chaque lien et chaque bouton ajoutés. Un élément
d'interface sans destination ne se livre pas.

### 5. Chiffre affiché non recalculé — 6 occurrences

> « gagner cest 237 + 790 non ? »
> « 93% pur timothée ? cest beaucoup non ? »
> « cigartette par pacquet cest 20 ou 10 non ? »
> « [Image #4] question, bizarre non ? croissance mais impression qui chute ? »
> « ok mais par rapport aux premierers sheet, il est différent il y a plus de page non ? »

Tim recalcule systématiquement. La forme du rejet est toujours la même : une question en
« non ? » posée sur un nombre.

**Règle** : tout nombre affiché se recalcule depuis la source avant livraison, et l'unité comme
la période s'écrivent à côté.

### 6. Déploiement sans validation locale — 5 occurrences

> « NON NE DEPLOY PAS, MONTRE EN LOCAL »
> « commit MAIS NE PUBLIE PAS jamais, car ce nest pas pret »
> « cest null tu ne mets pas ca en ligne, on garde ce qu'on avait »
> « non tu dois mettre ca sur organikk.co pas https://organikk-landing.netlify.app »
> « ok, mais propose moi en local des simulations 3D »

Déjà en mémoire, et pourtant cinq rechutes sur la période. Une règle qui rechute est le signal
le plus fort du registre.

### 7. Régression sur une fonction qui marchait — 3 occurrences

> « ATTEND mais ça a sauté !!! j'ai plus de stats, mon compte nest plus connecté !! »
> « mais tu as tout cassé où est le rapport ? où est le bouton pour lancer ? »
> « verifie que tout fonctionne et que rien nest cassé »

Coût très supérieur aux autres thèmes : chaque occurrence casse un chemin déjà validé.

**Règle** : après toute modification d'un parcours existant (connexion, rapport, lancement),
rejouer ce parcours avant de rendre.

### 8. Aplat de couleur et mode sombre — 4 occurrences

> « il faut du décoloré, ou dégradé et grainy et noisy. Jamais de oculeur pleine »
> « fond blanc et garder le vert, jamais de site en dark »
> « Non tu fais theme claire DA seocity »
> « Non faire plein on retire le dégradé mais on laisse gainy et noisy »

### 9. Page de test mise en ligne indexable — 3 occurrences

> « ajoute ca en non indexe sur organikk et pas dans le sitemap »
> « tu vas deploy les pages audit sur organikk.co en non indexe ni dans le sitemap ni dans le robot »
> « et deployer les deux non index et non site map »

**Règle** : toute page déployée qui n'est pas destinée à la recherche part en `noindex`, hors
sitemap, et bloquée au robot. Trois consignes, pas une.

### 10. Version mobile non pensée — 2 occurrences

> « mais la version mobile, reponsive ca va pas du otut, tu dois penser la version mobile seule »
> « ok sur mobile ca va pas du otut, tu dois créé une version du live pour mobile »

### 11. Vocabulaire interne servi au lecteur — 3 occurrences

> « regle : le lecteur ne connait pas notre vault, ne connait pas notre corpus, il est néophyte »
> « le has ? mais le fueur ne sait pas ce que cest, tu parles comme un scientifique la »
> « non mais la tu parle comme une IA, tu dois respecter ce que je t'ai donné »

## Candidats sérieux au durcissement

Les thèmes à trois occurrences ou plus qui ne sont **pas** encore une règle vérifiable :

| Thème | Occ. | Forme de durcissement possible |
|---|---|---|
| `variantes-avant-choix` | 7 | contrainte de livraison dans les skills visuels (`logo`, `creation-da`, `organikk-site`) |
| `correction-partielle-refusee` | 10 | question posée à Tim au moment du rejet : détail ou direction ? |
| `lien-ou-bouton-mort` | 8 | check automatique des ancres et handlers ajoutés avant de rendre |
| `chiffre-non-verifie` | 6 | recalcul obligatoire depuis la source, unité et période affichées |
| `noindex-hors-sitemap` | 3 | check au déploiement d'une page hors recherche |
| `regression-sur-existant` | 3 | rejouer le parcours modifié avant de rendre |

Aucun de ces durcissements n'est appliqué automatiquement. Ils sont proposés en revue hebdo,
Tim tranche.

Pages liées : [[corrections-recurrentes]] · [[hypotheses]] · [[preuves/index]] · [[apprentissage/preuves-auto]]
