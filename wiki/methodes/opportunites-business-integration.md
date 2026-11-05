---
type: methode
title: Branchement des opportunités business dans Audit V2 et Stratégie GEO
aliases: [opportunites-business-integration]
tags: [seo, geo, business, workflow]
created: 2026-11-05
updated: 2026-11-05
sources: 2
confidence: high
status: draft
---

# Branchement des opportunités business

Le contrat économique validé reste `0.1.0`. L’intégration est nommée `business-v1`. Elle charge [[methodes/opportunites-business]], puis produit un résultat partagé. La proposition et son périmètre sont conservés dans [[queries/2026-11-05-opportunites-business-geo-audit-proposition]]. La livraison de branchement est [[queries/2026-11-05-opportunites-business-phase-c]].

## Entrée et résultat communs

Chaque nouvelle mission fournit `data/opportunites-business.json`. Les champs sont définis par `wiki/methodes/opportunites-business/schema.json`. Le validateur refuse une entrée incohérente. `integration.load_bundle(path)` valide et calcule une seule fois ; le bundle alimente contexte, synthèse, moyens, mesure et détails. Aucun bloc HTML ne recalcule un scénario.

Les paramètres économiques restent modifiables dans ce fichier. Les valeurs absentes restent nulles. Les accords portent sur son empreinte ; une modification rend les accords concernés à réviser. Les scénarios alternatifs ne sont pas totalisés. Le code ne collecte aucune donnée externe.

## Audit complet V2

Le module de vues conserve ses vues techniques et ajoute ces déclarations :

```python
BUSINESS_CONTRACT = 'business-v1'
BUSINESS_INPUT = 'data/opportunites-business.json'
GEO_CONTRACT = 'geo-business-v1'
GEO_STATE = 'pending'
```

L’assembleur canonique est `~/.claude/skills/audit-complet-v2/assemble.py`. Utiliser `~/Code/seo-kb/.venv/bin/python -B`, puis les arguments habituels : site, module de vues, **nouvelle sortie HTML**.

Le contexte est affiché en V[0] et au début du Résumé V[1], pour que le lecteur arrivant directement sur le résumé le voie avant les opportunités. La synthèse business suit, puis le diagnostic technique existant. V[8] reçoit moyens et suivi. Les vues V[2] à V[7] restent conservées ; les nouvelles recommandations y citent l’opportunité dans les données lorsqu’un lien est démontré.

`GEO_STATE='pending'` crée un onglet clairement en attente, sans contenu donnant l’impression d’une stratégie complète. `complete` exige un dossier business actuellement approuvé et les treize titres canoniques dans l’ordre. Ce contrôle de forme ne remplace pas la relecture des contenus ni les validations de panel, de plan et de textes conservées dans `etat.json`.

Le raccourci `_modele/v2/assemble.py ... --business` route vers l’assembleur canonique. Sans cette option, le modèle historique reste inchangé. `top20.build(site, business_input=path)` remplace le tableau scoré par les décisions communes. Le mode historique sans paramètre reste réservé aux anciens dossiers.

Le rapport Markdown est assemblé par `rapport.py CONTRAT --body RAPPORT-SOURCE.md --audience audit --output NOUVEAU-RAPPORT.md`. Le rapport source contient `<!-- business-context -->`, puis `<!-- business-summary -->`, avant son analyse technique. Les marqueurs uniques sont contrôlés ; les autres sections restent intactes. Le rapport reçoit le même manifeste de calcul que le dashboard.

Pour V[7], utiliser le marqueur `<!-- business-opportunities -->` : l’assembleur y insère le bundle déjà calculé. L’adaptateur autonome top20 sert aux exports séparés, sans le rappeler depuis le module de vues.

## Stratégie GEO

Le point d’entrée Codex charge le pilote canonique global à dix étapes et treize parties. Les missions mot-clé ne sont plus automatiquement déclenchées par le pilote. Cadrage, shortlist, panel, coût éventuel de collecte, bilan des observations, opportunités, plan puis production gardent leurs validations.

Après cadrage et collecte, qualifier le périmètre exploré. Après les observations, obtenir l’accord sur les opportunités avant architecture et production. Le cycle retenu peut être plus restreint que l’exploration. Une condition commerciale démontrée peut passer avant le contenu.

```bash
~/Code/seo-kb/.venv/bin/python -B ~/.claude/skills/strategie-geo/scripts/build_dashboard.py DOSSIER 'Entreprise' --business
```

Cette commande écrit `dashboard-business.html` et son manifeste. Les onglets Synthèse, Demande et concurrence, Moyens et suivi et Visibilité IA utilisent le bundle commun. Pages, Preuves et Autorité conservent les CSV existants comme mémoire éditoriale ; ils ne calculent aucune valeur commerciale. Sans `--business`, le rendu historique reste disponible pour les anciens dossiers.

## Suivi et réemploi

`roadmap.py --business CONTRAT --output NOUVEAU-SUIVI --previous ANCIEN-SUIVI` produit un état sans calendrier ajouté. L’état historique complet, y compris les actions sorties du périmètre, reste dans `legacy_snapshot`. Un statut historique fait ou bloqué doit être réconcilié avec le contrat avant sortie. Aucun statut terminé n’est remis silencieusement à faire.

L’assembleur utilise le bundle déjà chargé pour le rendu des moyens. Les dates explicitement renseignées exigent source et capacité positive ; aucune date de résultat SEO n’est déduite. Les critères de poursuite, révision et arrêt restent ceux de chaque opportunité.

`importer.py` copie un contrat Audit vers GEO à l’identique après relecture du périmètre et de la fraîcheur. La revue ne rajeunit aucune collecte. Pour les anciens JSON, un contrat relu et des correspondances explicites sont exigés. Le dossier source est copié intégralement dans `original.json` ; les accords historiques restent archivés, pas transférés. L’import ne signe aucune validation.

## Preuve d’exécution et retour arrière

Chaque sortie nouvelle reçoit un fichier `.business.json` avec version, chemins et empreintes chargés, empreinte d’entrée, résultat et empreinte du HTML. Les entrées et sorties existantes ne sont pas écrasées en mode business. Les fichiers sources et les anciens HTML ne sont jamais migrés automatiquement.

Le paquet d’installation contient les fichiers avant/après, les empreintes et les destinations exactes. Son contrôle préalable refuse une installation si une cible a changé depuis la préparation. Le retour arrière restaure les fichiers existants sauvegardés et déplace les nouveaux fichiers dans une archive, sans supprimer les données de mission. Le paquet de phase C ne s’installe pas lui-même.

`SEO_BUSINESS_ROOT` et `SEO_AUDIT_ASSEMBLER` servent aux vérifications isolées ; les chemins par défaut sont les chemins canoniques ci-dessus. Le manifeste révèle les chemins réellement utilisés. Aucun outil tiers appelé ne doit être déduit de ces chemins.
