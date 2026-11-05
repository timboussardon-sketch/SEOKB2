---
name: maillage-interne-gsc
description: |
  Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille. Pipeline en 5 étapes : récupérer GSC → diagnostiquer la structure (mères potentielles, sous-maillées, orphelines) → construire le plan de maillage avec règles Know→Do → prioriser par rang justifié → générer recommandations (page source, destination, ancre, contexte). Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "maillage interne", "liens internes", "cocon SEO", "pages orphelines", "GSC + structure de site", quand un fichier GSC est uploadé.
---

# Skill : maillage interne GSC

## Ce que tu donnes à Claude

- L'export Search Console « Pages » : URL, clics, impressions, CTR, position. Obligatoire.
- L'export « Requêtes » par page, si tu peux le sortir. Sans lui, Claude ne sait pas sur quoi chaque page se positionne.
- Une période de 3 à 6 mois.
- La liste de tes pages d'offre et de tes pages « Do » (outil, audit, contact, devis).
- Si tu as lancé le skill `maillage-systeme` avant, son crawl (`index.json`, `graph.json`) : les liens réels du site, que la GSC ne donne pas.

## Consigne pour le lancer

> voilà mon export GSC, construis le plan de maillage

> audite le maillage de monsite.fr à partir de ces exports Search Console

## Quand déclencher

Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille.

## Philosophie

> "Le maillage interne, c'est la puissance. Et ça part de tes mots-clés."

- Page mère = citée depuis des pages filles/petites-filles distinctes, liens du corps (repère interne : 5 ; c'est un repère de travail, pas un seuil de santé)
- Le maillage part de la stratégie de mots-clés → le cocon est la conséquence
- Priorité : transactionnel > décisionnel > informationnel
- Maillage par intention (Know → Do) en plus du maillage sémantique

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Pages : URL, Clics, Impressions, CTR, Position | Oui |
| Export GSC Requêtes par page | Recommandé |
| Période 3-6 mois | Recommandé |

## Pipeline (5 étapes)

1. **Récupérer les données GSC** : export Pages + Requêtes par URL
2. **Diagnostiquer la structure** :
   - Pages mères potentielles (impressions élevées, pos 4-15, requête transactionnelle)
   - Pages sous-maillées (bonne position mais CTR faible)
   - Pages orphelines (aucune thématique secondaire dans GSC)
3. **Construire le plan de maillage** : hiérarchie mère/fille/petite-fille + règles Know→Do
4. **Prioriser** : pas de score numérique. Une formule du type `(Impressions × 0.4) + (Potentiel position × 0.4) + (Business value × 0.2)` additionne des grandeurs non normalisées, les impressions écrasent le reste. Priorité justifiée, dans cet ordre : (a) page business prioritaire à fort déficit de maillage (forte en impressions, peu de liens entrants éditoriaux depuis des pages distinctes) ; (b) page en position 4-15 sur une requête transactionnelle que des liens entrants peuvent aider ; (c) page en forte baisse sur 90 jours contre 90 (tendance « en baisse ») ; (d) le reste. Chaque recommandation écrit la raison de son rang.
5. **Générer les recommandations** : page source + page destination + ancre + contexte + priorité

## Structure hiérarchique

```
Page Mère (mot-clé principal business)
├── Page Fille 1 (requête secondaire transactionnelle)
│   ├── Page Petite-Fille A (longue traîne / micro-intention)
│   └── Page Petite-Fille B
└── Page Fille 2
```

Règle Know → Do : chaque page Know doit pointer vers au moins 1 page Do thématiquement reliée.

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau.

Posture : tu es un consultant SEO senior qui transforme des données en décisions, pas un crawler qui récite ce qu'il trouve. Tu ne restitues pas toutes les anomalies : tu identifies les quelques phénomènes qui expliquent le mieux la situation du site. On doit pouvoir ouvrir le rapport et comprendre en moins de 30 secondes ce qui se passe, pourquoi, et ce qu'on fait maintenant.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque faible / moyen / élevé ; toute action à risque élevé (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist (requêtes, conversions, backlinks, intention, historique, rôle commercial de la page)
6. Ce que les données ne permettent pas de conclure (requêtes anonymisées, URL non inspectées, liens réels non crawlés, backlinks non analysés, conversions non disponibles), et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Repères pour remplir ces champs :

- Problème = dégrade probablement les performances ; opportunité = pourrait être amélioré.
- Confiance forte = plusieurs sources concordent (GSC, crawl, HTML) ; moyenne = signal incomplet ; faible = peu de données. Une recommandation lourde exige une confiance forte.
- Force du signal GSC par page : moins de 20 impressions = données insuffisantes ; 20 à 100 = signal faible ; 100 à 500 = exploitable ; 500 et plus = solide. Une page de moins de 30 jours sans impressions n'est pas un échec.
- Risque faible = maillage, navigation, title, Hn ; moyen = gros changement de contenu, canonical ; élevé = suppression, 301, fusion, changement massif d'URL.
- Pour prioriser, raisonne sur impact × confiance × poids business de la page × force du signal ÷ effort, sans jamais afficher ce calcul. Poids business : home, pages d'offre, service et tarifs en haut ; étude de cas ensuite ; guide, puis article de blog ; page légale presque nul.

Sur le périmètre de ce skill, le rapport tranche les pages fortes en impressions et sous-liées, tendance 28 jours contre 28 et 90 contre 90 par page stratégique (en hausse / stable / en baisse / nouvelle / données insuffisantes), les fortes baisses en premier.

Règles : chaque information est typée Fait (donnée observée), Hypothèse (interprétation) ou Action (recommandation), jamais une hypothèse écrite comme un fait ; un problème existe une seule fois, les observations qui parlent du même problème fusionnent ; une anomalie n'est pas une priorité par défaut ; une corrélation n'est pas une causalité ; peu de trafic n'est pas un problème en soi ; une orpheline n'est pas critique par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé (« les données GSC montrent », jamais « Google ne comprend pas »). Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution : aucun identifiant technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Partie détaillée du rapport : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Output obligatoire

Pour chaque action :
- Page source (intention Know/Do/Know+Do)
- Page destination + intention
- Nature du lien (sémantique ou intentionnel Know→Do)
- Ancre recommandée (jamais "cliquez ici")
- Contexte d'insertion
- Priorité (Haute/Moyenne/Faible)

## Ce que tu vérifies avant d'ajouter les liens

Claude propose, tu arbitres. Avant d'insérer un lien du plan :

- Lis le passage à voix haute sans le lien. Si la phrase boite, rejette le lien ou réécris la phrase ; ne force jamais une ancre.
- Insère par lot de 10 à 20 liens, pas tout le plan d'un coup. Commence par les rangs les plus hauts.
- Relance un crawl après l'insertion du lot (le script du skill `maillage-systeme` le fait) pour vérifier que les liens sont bien en place et comptés.
- Critère de fin de lot : zéro page d'offre orpheline. Tant qu'il en reste une, le lot suivant commence par elle.
- L'effet dans la GSC se lit sur plusieurs semaines, page par page, jamais le lendemain.

## Règles absolues

- Ne pas automatiser à 100% : le maillage part de la stratégie, pas des outils
- Ne pas mailler sans tenir compte de l'intention (sémantique ≠ intentionnel)
- Ne pas répéter la même ancre sur toutes les pages filles
- Une page mère se juge à ses citations depuis des pages distinctes, dans le corps (repère : 5) ; jamais un total brut qui mélange navigation et contexte

## Sauvegarde

Enregistre la sortie dans un fichier markdown daté dans ton dossier de projet (exemple : `2026-09-30-maillage-gsc-monsite.md`), rapport de pré-décision compris.
