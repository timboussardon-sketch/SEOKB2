---
type: query
title: "SEO City comme référencier de sites : ce que l'idée change, ce qui tient, ce qui manque"
aliases: [seo-city-referencier, referencier-sites-seocity, seo-city-classement-produit]
tags: [seocity, produit, gsc, data-proprietaire, acquisition, agences, marketplace]
created: 2026-10-15
updated: 2026-10-15
sources: 5
confidence: medium
status: draft
---

# SEO City comme référencier de sites

Idée de Tim, 15 octobre 2026 : « SEO City pourrait devenir un référencier de sites que les agences viennent consulter. Le produit devient le classement. On branche son site et les agences, freelances viennent voir la performance. »

Matière : `~/Code/gsc-simcity` (README, `classement.js`, pages `classement.html`, `freelances.html`, `consultant.html`), [[decisions/0002-score-sante-site]], [[concepts/score-sante-ville-seocity]], [[methodes/playbook-acquisition-organikk]], [[reflexions/vendre-le-systeme]].

## 1. Ce que l'idée inverse

Aujourd'hui le propriétaire branche sa GSC pour regarder sa propre ville. L'audience, c'est lui.

Demain il la branche pour être vu. L'audience devient ceux qui le démarchent : agences, freelances, acheteurs de sites.

SEO City contient déjà les trois briques, dans l'autre sens :

| Brique existante | Ce qu'elle fait | Ce que le référencier en fait |
|---|---|---|
| `classement.html` | Top 50 des villes construites, score 75 % développement + 25 % rendement sur clics 28 j, podium | Devient le produit, pas l'accueil |
| `freelances.html` | « La base des freelances SEO · ville, spécialité, TJM » : l'offre est listée, les sites consultent | Se retourne : les sites sont listés, l'offre consulte |
| `consultant.html` (prototype local) | Fiche consultant avec « Sites gérés (publics) », trophées de portefeuille | Reste : c'est la preuve côté prestataire |

Donc ce n'est pas un pivot. C'est la deuxième face d'une place de marché dont la première face est déjà en ligne.

## 2. L'argument qui n'existe nulle part ailleurs

La donnée est déclarée par le site lui-même, depuis sa GSC. Pas estimée par un crawler.

Similarweb, Semrush Traffic Analytics et Ahrefs vendent des extrapolations. Une agence qui lit un vrai historique de clics et de positions avant un premier call, personne ne lui offre ça aujourd'hui.

L'analogie la plus proche n'est pas Similarweb, c'est le mouvement « open startup » : des entreprises qui publient leur revenu réel comme acte marketing. Ici, des sites qui publient leur Search Console. [MATIÈRE MANQUANTE : aucun comparable dans le coffre, à documenter.]

## 3. Ce que le coffre a déjà tranché, et qui pèse

**La donnée appartient à ses propriétaires.** [[decisions/0002-score-sante-site]], 27 août : l'usage des ~45 villes d'autres comptes comme corpus a été laissé non tranché pour cette raison, et le corpus limité aux 17 sites de Tim. Le référencier répond à la question : le propriétaire choisit d'apparaître. Sans opt-in explicite, l'idée contredit l'ADR.

**Un score de tendance détruit la confiance.** Même ADR : le score SEO City note la tendance, oscille, et a été écarté pour un tableau de bord client. Un classement public a le même défaut en pire. Le classement actuel (log des clics 28 j) récompense les gros sites et bouge au bruit. Le référencier a besoin du score d'état de [[concepts/score-sante-site]], ou d'aucun score du tout : les chiffres bruts datés suffisent à une agence.

**Le corpus n'est pas figé.** Ajouter un site déplace la note des autres. Dans un classement c'est normal, mais chaque édition doit être datée pour que « 14e au 1er octobre » reste vrai.

## 4. La question qui décide : pourquoi un site accepte d'être listé

Un site qui monte veut se montrer. Un site qui baisse n'a aucune raison de brancher sa GSC pour que tout le monde le voie.

Trois raisons possibles de s'inscrire, et elles ne donnent pas le même produit :

1. **Vitrine.** Le site est fier de ses chiffres. Biais vers les gagnants. Produit : un palmarès. Ce qu'une agence en tire : une liste de sites qui ont du trafic à perdre, donc à défendre.
2. **Preuve pour un prestataire.** Le consultant montre les sites qu'il gère. C'est `consultant.html`. Le site n'a pas choisi, c'est le prestataire qui expose.
3. **Appel d'offres.** Le site se liste parce qu'il cherche quelqu'un. Il coche « ouvert aux propositions ».

La troisième est la seule qui rende le référencier payant côté agences. [[methodes/playbook-acquisition-organikk]] : le seul cas outbound documenté qui fonctionne filtre sa liste sur un signal d'achat, 9 à 11 % de réponse contre 4 à 5 % sans. Un site qui a branché sa vraie GSC et coché « je cherche un prestataire », c'est le signal d'achat le plus propre qui existe en SEO.

Donc le produit n'est pas un classement. Le classement est l'appât. Le produit est une base de sites qualifiés par leur vraie donnée, avec une intention déclarée.

## 5. Qui paie

Deux modèles, pas compatibles au départ :

| Modèle | Qui paie | Comparable | Ce qui le porte |
|---|---|---|---|
| Vitrine | Le site listé | Clutch, Sortlist (inversé) | Vanité, badge, backlink |
| Base de prospection | L'agence qui consulte | Base de leads qualifiés | Le coût actuel d'un lead cold : CPL email 225 $, SEO 206 $ (Sopro 2025 via playbook) |

Le second est cohérent avec ce qu'Organikk sait déjà de la cible : 143 agences SEO/web 5-20 salariés contactées du 13 au 15 octobre, 1 réponse, et Tim le 15 : « c'est la bonne cible, le bon message ». Leur douleur est la prospection sans signal. Le message « voici des sites qui ont branché leur GSC et cherchent un prestataire » est une autre proposition que « voici mon système SEO ».

Prix acceptable côté agence : [MATIÈRE MANQUANTE].

## 6. Le problème de démarrage

Place de marché à deux faces, donc problème de l'œuf et de la poule.

Côté sites : ~45 villes construites au 27 août (ADR-0002), dont 17 de Tim. Un référencier à 45 entrées n'intéresse aucune agence. Il faut la masse avant la demande.

Ce qui joue pour : la première ville est gratuite (`prix.html`, 0 € puis 19 €/mois). Chaque ville construite est un site potentiellement listable. L'acquisition côté sites existe déjà, c'est le jeu.

Côté agences : l'outbound en cours est exactement la cible. Il peut servir de sondage avant de construire quoi que ce soit.

## 7. Ce qu'un site en déclin fait au produit

Si l'état « déclin » est public, un site qui décroche se désinscrit. Churn garanti côté offre.

Si l'état « déclin » est visible par les agences avec le consentement du site, c'est le lead le plus chaud de la base.

Le propriétaire doit choisir ce qu'il expose : chiffres bruts, score, état, intention. Pas de réglage par défaut qui expose.

## 8. À vérifier avant de coder

- Conditions d'utilisation de l'API Search Console sur l'affichage public de données d'un tiers, même consenti. [MATIÈRE MANQUANTE : non vérifié.]
- Segmentation nécessaire pour qu'une agence s'en serve : secteur, pays, ville, taille, CMS. `freelances.html` a déjà ville et spécialité côté offre, le schéma miroir côté sites n'existe pas.

## 9. Le test le moins cher

Pas de référencier à construire pour savoir si l'idée tient.

Côté sites : un interrupteur sur la page ville, « visible dans l'annuaire des sites » et « ouvert aux propositions ». Compter combien de propriétaires le cochent en 30 jours sur les villes existantes et les nouvelles.

Côté agences : une question dans les prochains lots outbound, ou aux répondants (Flash Design) : « si vous aviez accès à des sites qui ont publié leur Search Console et cherchent un prestataire, vous paieriez ? ». Une réponse vaut plus que le reste de cette note.

Les deux chiffres décident. Sans eux, l'idée reste une idée.

## Ce qui n'est pas tranché

- Pivot de SEO City ou produit à côté sous un autre nom.
- Place du classement actuel (podium, score log) : il contredit le besoin d'une agence, qui veut filtrer, pas un top 50.
- Articulation avec [[concepts/score-sante-site]] et son corpus versionné, jamais finalisé (page `draft`, `sources: 0`, cinquième semaine en [[revue-hebdo/2026-W39]]).
