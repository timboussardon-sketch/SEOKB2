---
type: methode
title: "Faire un audit complet avec Claude, étape par étape"
tags: [audit, seo, process, claude, organikk]
created: 2026-09-24
updated: 2026-09-24
sources: 1
confidence: high
status: stable
---

## Nouvelles missions : opportunités business

Le contrat [[methodes/opportunites-business]] et le branchement [[methodes/opportunites-business-integration]] complètent cette référence pour `business-v1`. Ils remplacent les scores numériques de priorité business, les valeurs économiques par défaut et le calendrier sans capacité. Les diagnostics techniques et leur profondeur restent conservés. La synthèse des opportunités suit le contexte et le périmètre ; trois opportunités visibles, détail repliable. La collecte historique ne devient jamais un marché exhaustif.

Les méthodes et commandes ci-dessous décrivent aussi des dossiers historiques. Pour une nouvelle mission, utiliser les points d’entrée canoniques du contrat ; préserver les anciens livrables. Distinguer les requêtes mesurées, les besoins observés et les hypothèses ; ne pas additionner demande Google, questions et citations IA.


> Le process d'un audit complet, de la demande reçue au livrable montré.
> Écrit le 24/09/2026, à partir de l'audit d'artisansmart.fr, le premier passé
> par cette chaîne. Les durées sont celles mesurées ce jour-là.

## En résumé (à lire en premier)

Un audit se fait en 8 étapes. Trois d'entre elles tournent en parallèle.

Le cadre ne s'improvise jamais. Le skill `audit-complet` route vers le workflow de la base, tu le suis.

Quatre relevés alimentent tout : le moteur d'audit Organikk, un crawl maison, Jev, PageSpeed Insights.

Le moteur public s'arrête à 50 pages. Pour un audit client, tu relances sans ce plafond.

Le crawl maison suit les liens. C'est le seul qui voit les pages absentes du sitemap.

Sans Search Console, quatre phases du workflow tombent. Tu le dis dans le livrable, tu ne combles pas.

Le rapport rédigé part dans `seo-kb/wiki/audit/`. Le livrable HTML sort de `~/Code/audits-clients/_modele/build.py`.

Tu montres en local. Tu attends la validation. Rien ne part au client avant.

Compte 25 minutes de relevés pour un site de 400 pages, le reste est de la lecture.

## 1. La demande arrive

Une adresse déposée sur `organikk.co/audit` atterrit dans le store Netlify `audit-demandes`.

`GET /api/audit-vitrine` donne les sites et les dates, jamais les emails.

`GET /api/audit-demandes?key=…` donne la liste complète, avec les adresses.

La page annonce 48 heures. Le compteur part de la date de dépôt.

## 2. Ouvrir le cadre

Invoque `audit-complet`. Il ne contient pas la méthode, il route vers `seo-kb/raw/bootcamp4/workflow-audit-bootcamp4.md`.

Lis les 9 phases avant de lancer quoi que ce soit.

Ne décide jamais toi-même des critères, de la priorisation ou du format de sortie.

## 3. Lancer les relevés

Trois scripts partent en même temps, depuis `~/Code/audits-clients/_modele/`.

| Script | Ce qu'il produit | Durée mesurée |
|---|---|---|
| `audit-complet.py` | le moteur Organikk sans plafond, six dimensions, page par page | 154 s sur 266 pages |
| `crawl.py` | sitemap plus les liens découverts, 392 URL sur artisansmart | 3 min |
| `psi.py` | PageSpeed mobile sur 55 pages, plus le terrain CrUX | 5 min |

`jev-toutes.py` suit, sur toutes les pages du crawl : 388 notées sur artisansmart.

Le moteur tourne sur une base isolée dans le scratchpad. Ta base de travail n'est pas touchée.

## 4. Vérifier ce qui est mesurable

Sans accès à la Search Console, le positionnement, les gains rapides, la cannibalisation chiffrée et la passe data du maillage ne se tiennent pas.

Écris-le dans le livrable, section « ce que les données ne permettent pas de conclure ».

Une page « non testée » n'est pas une page « non indexée ». Les deux mots ne se remplacent pas.

## 5. Croiser les quatre relevés

Le moteur voit les pages du sitemap. Le crawl maison voit celles qui n'y sont pas.

Sur artisansmart, l'écart valait le diagnostic principal : 123 pages en `noindex` et hors sitemap, invisibles pour le moteur seul.

Jev donne l'intention d'achat page par page. Sur artisansmart, les 122 pages retenues hors de l'index sont notées 75 sur 100, les 57 ouvertes 74.

PageSpeed donne le laboratoire, CrUX donne le terrain. Les deux ne disent pas la même chose, et l'écart est une information.

## 6. Écrire le rapport

Le rapport rédigé va dans `seo-kb/wiki/audit/AAAA-MM-JJ-slug.md`.

Il suit le format de sortie du skill : diagnostic en une phrase, quatre chiffres, état par zone, trois problèmes, plan des 30 jours, opportunités, limites.

Jamais de score sur 10. Jamais d'effort en heures. Faible, moyen, élevé.

Aucune action proposée sur une page dont les requêtes ne sont pas connues.

Passe `redaction-anti-ia` avant de montrer quoi que ce soit.

## 7. Générer le livrable

```
AUDIT_DATA=<dossier des relevés> python3 ~/Code/audits-clients/_modele/build.py
```

Sortie : un tableau de bord en accueil, chiffres cliquables, et une page par analyse.

Onze pages au total. Le filigrane `organikk.co` est posé sur le fond, pas sur les cartes.

Sers le dossier sur un port libre et vérifie que la page s'affiche. Un build qui passe ne prouve pas qu'une page se dessine.

## 8. Montrer et committer

Donne le lien local. Attends la validation avant tout envoi.

Committe le rapport dans `seo-kb`. Ne pousse pas sans demande.

## Les cinq pièges déjà payés

**L'échantillon de 50 pages ment.** Sur artisansmart, il donnait une orientation de 42 sur 100. Le site entier est à 61 : l'échantillon penchait vers les pages d'aide.

**PageSpeed se mesure sur les URL du sitemap, slash compris.** Une URL tapée sans le slash final déclenche un 301 que PageSpeed facture 800 ms en « Avoid multiple page redirects ». Ce sont tes chiffres, pas ceux du site.

**Les temps de réponse mesurés depuis Lyon sont pollués.** Mesure un site témoin au même moment. Le jour de l'audit, organikk.co répondait en 1,4 s depuis le même poste. Seul le temps de réponse de terrain de CrUX est publiable.

**« Non testé » se vérifie avant de s'écrire.** La cannibalisation se mesure sur le contenu : même mot-clé visé, H1 qui se recouvrent. Ce qui demande la Search Console, c'est son coût, pas son existence.

**Un site lent ralentit sous ton crawl.** Six requêtes de front sur un serveur partagé multiplient les temps par trois. Ne teste jamais un site pendant qu'un audit tourne dessus.

## Sources

- Workflow : [[raw/bootcamp4/workflow-audit-bootcamp4]]
- Premier audit passé par cette chaîne : [[audit/2026-09-24-artisansmart-fr]]
- Format de restitution : [[audit/2026-09-22-organikk-co]]
- Scripts et modèle de livrable : `~/Code/audits-clients/_modele/README.md`
