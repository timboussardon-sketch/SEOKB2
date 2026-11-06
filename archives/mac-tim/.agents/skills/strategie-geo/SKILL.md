---
name: strategie-geo
description: >-
  Construire ou réviser une stratégie d’acquisition SEO et recherche IA avec le
  framework AI Search Growth System : offres, questions d’acheteurs, observations
  des moteurs, diagnostic, contenu, distribution et mesure commerciale.
  Skill principal dès que Tim demande une stratégie SEO, GEO ou IA, y compris
  « strat SEO », « strat IA » et « stratégie complète pour X ». Il cadre la
  stratégie globale et appelle les skills spécialisés requis. Un audit ponctuel
  ou un relevé isolé de citations garde son skill dédié.
---

# Stratégie GEO — AI Search Growth System

Point d’entrée Codex du pilote. Ouvrir `AGENTS.md`, la doctrine `wiki/moc/doctrine-seo-reference.md` et `wiki/concepts/anti-ai-writing.md`, puis lire **`/Users/timothee/.claude/skills/strategie-geo/SKILL.md`**, version canonique à dix étapes et treize parties. Le template `references/template.md` précise la restitution. Si la référence canonique est absente, signaler le blocage ; ne pas revenir silencieusement à l’ancien pilote.

## Contrat commun des opportunités business — 2026-11-05

Pour toute nouvelle mission, lire `~/Code/seo-kb/wiki/methodes/opportunites-business.md` et son contrat `wiki/methodes/opportunites-business/schema.json`. La méthode et le calculateur sont communs à Stratégie GEO et Audit complet V2. Créer `data/opportunites-business.json` selon ce contrat. Les dates et références pointent vers les pièces originales ; `raw/` reste immuable.

Demande observée → opportunité accessible → valeur estimée → moyens nécessaires → mesure des résultats. Offre et périmètre d’abord ; distinguer recherches mesurées, besoins observés et hypothèses. Concurrents commerciaux, concurrents SERP et sources IA gardent leurs rôles séparés. Une page d’offre ne prouve pas une demande. Un regroupement sans comparaison SERP reste une hypothèse d’intention. L’exploration n’est pas un marché exhaustif.

Prioriser par adéquation à l’offre, intention business et opportunité démontrée, puis faisabilité, coût, dépendances et délai justifié. Conserver les exclusions. Aucun score numérique de priorité, `brand_fit`, produit de notes ou CPC ne détermine l’ordre. Le CPC n’est jamais une estimation de revenu. Les scores techniques existants restent des diagnostics techniques, séparés de la sélection business.

Le calculateur laisse les inconnues à `null`. Il ne génère aucun taux, coût ni délai. Ne jamais additionner Google, questions clients et IA, ni des scénarios alternatifs. Prudent, central et favorable ne sont renseignés que si leurs hypothèses sont documentées ; sinon afficher « non estimable avec les données disponibles ». Montrer actuel, additionnel, potentiel et capacité. Une citation IA n’est pas une vente.

Les accords portent sur l’empreinte du dossier présenté. Changer une hypothèse impose sa revalidation. Conserver cadrage, shortlist, panel, collecte payante, opportunités, plan puis livrables comme décisions distinctes. Une validation de plan n’autorise ni publication ni envoi. TASM reste un concept externe dont l’auteur est à identifier ; ne pas l’attribuer à Tim.

Exécuter avec `~/Code/seo-kb/.venv/bin/python -B`. Les manifestes `.business.json` attestent les fichiers effectivement chargés et les calculs locaux ; ils n’attestent aucune collecte externe. Réemploi audit → GEO : `importer.py`, relecture du périmètre et de la fraîcheur, sans changer les dates de collecte. Ancien format : correspondance explicite, nouvelle version à côté de l’original, état historique conservé. Aucun réassemblage de dossier livré sans demande.

### Emplacement, sélection et restitution GEO

Après les étapes 1 et 2, constituer le périmètre exploré et qualifier les candidats. La limite de cinq mots-clés concerne le cycle retenu, pas l’exploration. Après les observations de l’étape 4, présenter le registre commun et obtenir l’accord sur les opportunités avant l’architecture URL, la production et la roadmap. Une action sur l’offre, la conversion ou le suivi commercial peut conditionner la production ; documenter la preuve et la mesure du test.

La version canonique suit les dix étapes et les treize parties ci-dessous. `strategie-mot-cle` reste spécialiste des demandes isolées ; il n’est plus déclenché automatiquement pour chaque terme du pilote GEO. Les validations humaines du pilote restent obligatoires.

Enrichir la Synthèse business avec demande, concurrence, choix et limites ; le Dashboard avec scénarios, hypothèses et mesures ; Roadmap et Top des actions avec identifiants, responsable proposé, charge, coût, dépendances et critères de revue. Les dix actions sont un maximum utile ; ne pas compléter artificiellement.

```bash
~/Code/seo-kb/.venv/bin/python -B ~/.claude/skills/strategie-geo/scripts/build_dashboard.py DOSSIER 'Entreprise' --business
```

Cette commande lit `DOSSIER/data/opportunites-business.json`, calcule une fois et écrit `dashboard-business.html` plus son manifeste. Les données CSV anciennes ne remplacent pas ce contrat. Choisir une nouvelle version de dossier pour une révision ; le script refuse d’écraser le rendu. Le dashboard est un suivi, pas la preuve que la stratégie est terminée. Le rapport final conserve les treize parties et les accords.

Si `voids/` ou la commande `./kb voids` n’existent pas, déclarer le module indisponible et classer manuellement les lacunes avec leurs extraits. Lire un prompt ne vaut pas appel de l’outil. Conserver les permissions propres à `geo-citations` et le protocole des relevés ; aucun appel payant implicite.

## Mémoire et validation des phases

Créer ou reprendre `wiki/strategie-geo/YYYY-MM-DD-entreprise/` avec `strategie.md`, `etat.json`, les données et les fichiers de mémoire prévus par le pilote. Réutiliser les originaux par références. `etat.json` conserve phase, livrables, versions, message exact de Tim, dates, tâches, responsables, dépendances, blocages, outils appelés et preuves. Les pages wiki gardent frontmatter et deux wikilinks. Présenter le dashboard local vérifié selon `wiki/methodes/tableau-de-bord-par-projet-seo.md`.

1. Cadrage commercial et périmètre : proposer puis faire valider.
2. Shortlist de cinq mots-clés maximum, intentions et questions : proposer puis faire valider.
3. Protocole et budget avant collecte ; bilan des observations après collecte : deux validations distinctes.
4. Opportunités business, conditions, exclusions et priorités : faire valider avant architecture et production.
5. Architecture, roadmap et moyens ; puis chaque livrable : validations distinctes. Publication ou envoi sur autorisation séparée.
6. Bilan mesuré et révision des investissements : proposer le cycle suivant.

Une correction reprend la phase courante. Une demande d’explication ou le silence ne valide rien. Les besoins peuvent être reformulés pour le panel ; conserver formulation originale, extrait, attribution et lien vers l’adaptation. Dix à quinze questions sont une cible utile, jamais un quota à remplir sans sources.

Pour un relevé réel, lire `/Users/timothee/.claude/skills/geo-citations/SKILL.md`, découvrir les outils disponibles et documenter moteur, modèle, mode, date, pays, langue, répétitions et erreurs. Ne pas présenter une réponse API comme l’interface publique. Pas de collecte payante sans accord sur le coût.

À chaque remise, distinguer méthode documentée, commandes locales exécutées, outils externes effectivement appelés et données collectées. Actualiser `wiki/index.md` et ajouter une entrée au journal. Ne pas installer de cron.
