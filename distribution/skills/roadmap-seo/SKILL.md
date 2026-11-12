---
name: roadmap-seo
description: "Roadmap SEO commune à plusieurs mots-clés business. « roadmap de ces mots-clés »."
---

## Quand utiliser ce skill

Agent principal de la roadmap SEO commune, lisible et suivable d'un site. Pour N mots-clés business ou importants, orchestre N missions strategie-mot-cle, consolide leurs résultats validés et propose un plan d'actions ordonné avec responsables, dépendances, critères de fin et capacité globale. Assure ensuite le suivi des statuts, blocages, réalisations et révisions. Déclencheurs : « roadmap SEO du site », « roadmap de ces mots-clés », « plan d'action global », « organise les priorités SEO », « où en est la roadmap », « actualise la roadmap ». Une stratégie sur un seul mot-clé reste dirigée par strategie-mot-cle jusqu'à sa validation.

## Intégration à la team stratégie

Les demandes globales « stratégie SEO GEO », « strat SEO GEO », « strat client », « stratégie GEO » et « stratégie SEO complète » passent par `.claude/skills/team-strategie/SKILL.md`. « C’est quoi la suite ? » reprend le projet actif sans approuver de phase. La team construit d’abord la stratégie SEO/GEO complète, en extrait ensuite 5 à 10 mots-clés business prioritaires validés, puis lance un agent strategie-mot-cle par terme et consolide la roadmap. Les mots-clés ne sont pas requis au lancement global. Un mot-clé isolé garde son workflow dédié.

En mission structurée de cette équipe, exécuter uniquement le rôle et la phase reçus. Le coordinateur conserve les états et les accords ; `keyword_adapter.py` appelle les validateurs de ce workflow et charge ses méthodes réelles. Retourner le payload métier de la phase au coordinateur, sans créer une seconde série d'états ni approuver soi-même. Pour la consolidation, le bundle de l'équipe remplace le manifeste des stratégies autonomes ; les principes de dédoublonnage, capacité, arbitrage et validation de la roadmap restent applicables. Les contrôleurs `consolidate.py` et `plan.py` du parcours autonome ne prennent pas directement ce bundle comme entrée.


# Une roadmap SEO pour le portefeuille de mots-clés du site

Travaille dans le coffre de la conversation et conserve le même contexte client pour toutes les missions. Un mot-clé business ou important retenu correspond à **une instance indépendante de `strategie-mot-cle`**. Cinq mots-clés donnent cinq stratégies et une seule roadmap globale. Le nombre de mots-clés ne fixe pas le nombre de pages.

## 1. Valider le portefeuille

Retrouve le site, ses offres, les prospects visés, la conversion, les URL existantes et la liste des mots-clés business ou importants. Pour chaque mot-clé, nomme la raison de son importance. Réutilise les recherches et pré-décisions déjà disponibles ; ne transforme pas automatiquement toutes les variantes d'une liste brute en nouvelles missions. Fais valider le portefeuille et le périmètre par l'utilisateur avant de lancer les missions. Une liste explicitement donnée comme liste à traiter vaut autorisation de ce périmètre ; ne redemande pas le même accord.

Cherche aussi les contraintes globales : capacité de collecte, de rédaction, de développement et de mise en ligne, responsables et engagements. Si elles ne sont pas connues, la consolidation peut avancer ; le calendrier ferme attend ces informations.

## 2. Lancer une mission stratégie par mot-clé

Charge `.claude/skills/strategie-mot-cle/SKILL.md` et réutilise son contrôleur. Retrouve ou initialise un état de stratégie propre à chaque mot-clé dans `wiki/strategie-mot-cle/`. Réutilise une stratégie existante lorsqu'elle correspond au coffre, au site, au besoin actuel et à la version validée ; ne relance pas silencieusement toute l'analyse.

**Délègue explicitement une mission par mot-clé à un sous-agent lorsque les outils de délégation sont disponibles.** Transmets à chacun : mot-clé exact, site, coffre, qualification business commune, fichiers utiles, chemin d'état propre et instruction de charger le skill réel. Chaque agent conserve sa mission jusqu'au bout et produit uniquement les livrables de sa stratégie. Il n'écrit pas de roadmap locale.

Exécute les missions indépendantes en parallèle dans la limite des places disponibles, puis par vagues si nécessaire. Cinq missions restent cinq missions même si trois seulement peuvent s'exécuter simultanément. Si les outils ne permettent pas de créer des sous-agents, annonce cette limite et exécute les missions séparément ; ne prétends pas avoir lancé des agents inexistants.

Chaque mission suit ses trois phases : qualification et intentions, questions du terrain, matière qualifiée. Les validations restent indépendantes. Tu peux présenter plusieurs livrables d'une même phase pour une validation groupée si l'utilisateur approuve explicitement les mots-clés et versions concernés. Un « oui » ambigu ne valide pas toutes les stratégies. Aucune mission ne dépasse son étape autorisée.

## 3. Vérifier toutes les stratégies avant consolidation

Crée dans `wiki/roadmap-seo/` un manifeste par site et portefeuille, avec les mots-clés et les chemins de leurs états. Le contrat est :

```json
{
  "site": "site-du-client.fr",
  "keywords": [
    {"keyword": "mot-clé business A", "state": "wiki/strategie-mot-cle/date-mot-cle-a.json"},
    {"keyword": "mot-clé business B", "state": "wiki/strategie-mot-cle/date-mot-cle-b.json"}
  ],
  "bundle": "wiki/roadmap-seo/site-strategies-validees.json",
  "roadmap": "wiki/roadmap-seo/site-roadmap.md"
}
```

Appelle `python3 .claude/skills/roadmap-seo/scripts/consolidate.py check --vault . --manifest CHEMIN`. Ce contrôle ne lance aucun agent : il vérifie leurs livrables et validations réellement enregistrés. Un état absent, hors coffre, associé à un autre mot-clé, incomplet ou non validé bloque l'ensemble.

Lorsque toutes les stratégies sont validées, appelle `bundle` avec les mêmes arguments. La commande réutilise les validateurs de `strategie-mot-cle`, conserve les sorties et les versions des méthodes, et prend l'empreinte des états sources. Le fichier produit est un dossier d'entrées vérifiées ; il ne constitue pas encore une roadmap.

Si un mot-clé doit sortir du portefeuille, l'utilisateur valide ce changement et le manifeste en garde la trace dans le journal du projet. Ne supprime pas silencieusement les mots-clés bloqués pour fabriquer une roadmap présentée comme complète.

## 4. Consolider les propositions à l'échelle du site

À partir du dossier validé, rapproche les intentions, les questions, les URL existantes, la matière et les pré-décisions du workflow mots-clés. Identifie les besoins équivalents et les chevauchements de pages proposés. Une page peut servir plusieurs mots-clés ; un mot-clé peut justifier plusieurs actions. Aucune fusion ou création d'URL ne découle automatiquement de cette détection.

Présente à l'utilisateur un tableau consolidé : action candidate, mots-clés servis, intentions/questions sources, destination existante ou candidate, raison business, matière exploitable, collecte manquante, dépendances et effort documenté ou à préciser. Fais valider cette consolidation et les destinations avant de dater les actions.

Les critères de priorité sont distincts : importance business, demande observée, urgence démontrée, preuve disponible, dépendances et capacité du client. Le score de matière /5 reste une information de faisabilité. Un sujet business important pauvre en preuves peut donner une tâche de collecte prioritaire. Ne trie pas tout le portefeuille sur le seul score de matière et n'invente ni volume, ni effort, ni capacité.

## 5. Produire une seule roadmap

Charge `.claude/skills/seo-roadmap-pseo/SKILL.md` pour ses principes utiles de séquencement vers la conversion. Pour ce workflow, la règle de ce workflow prime : les entrées sont les N stratégies validées. Ne substitue pas à ces entrées une génération de liste brute, un minimum de trente mots-clés, un quota de pages ou une capacité par défaut.

Écris la roadmap unique au chemin `roadmap` du manifeste. Elle comporte les actions arbitrées, leur ordre justifié, les mots-clés et livrables sources, les prérequis, les responsables, le planning compatible avec la capacité globale et la mesure attendue. Les actions prêtes, les collectes et les blocages restent identifiables. Une action commune à trois mots-clés est planifiée une seule fois.

Adapte l'horizon au mandat. Un planning 30/60/90 jours est possible ; sans capacité ou échéance connue, montre un ordre et les informations nécessaires pour le dater. Les cinq missions ne disposent pas chacune de la capacité totale du client.

Présente la roadmap et attends sa validation. La rédaction conserve ensuite brief → Hn → données → rédaction ; aucune validation de stratégie ou de roadmap ne pré-valide ces livrables. Si une stratégie source change, recharge ses pièces, refais la consolidation concernée et fais réexaminer les actions dépendantes. N'efface pas l'ancienne roadmap validée.

La collecte technique de l'audit et le suivi client peuvent apporter des contraintes ou actions prouvées. La roadmap de contenu du portefeuille conserve la traçabilité de chacune de ses stratégies sources. Une simple liste de mots-clés n'est pas une analyse terminée.

## 6. Construire le plan lisible avec son contrôleur

Le livrable principal est la page Markdown unique du manifeste. Le récap emploie des mots simples et présente l'objectif, la situation, la priorité et la décision attendue. Sépare les actions en cours, à suivre, en attente et les actions précédentes. Les tableaux se limitent à l'action, sa raison ou ce qui est attendu, qui s'en occupe et son état. Une attente nomme l'action à terminer ou la réponse nécessaire. Les identifiants internes, codes de priorité, empreintes et journaux techniques restent dans les fichiers de suivi. Le détail utile sous chaque action explique la page concernée, le résultat attendu et ce qui permet de dire que le travail est terminé. Ne recopie pas le vocabulaire technique des sources dans le récap ; reformule-le pour que l'utilisateur comprenne quoi faire et pourquoi.

Commence chaque titre d'action par le travail concret à faire et nomme sa cible. « Optimiser le SEO » n'est pas une tâche suffisante. Définis une unité réalisable et vérifiable. Dédoublonne les actions communes à plusieurs mots-clés ; justifie les priorités par le business et les dépendances. Un résultat SEO espéré est distinct du critère qui clôt le travail.

Après validation de la consolidation, prépare un JSON de proposition et appelle :

```bash
python3 .claude/skills/roadmap-seo/scripts/plan.py propose --vault . --manifest CHEMIN --input PROPOSITION.json
```

La proposition contient `objective`, `success_metric` (définition de la mesure), `horizon`, `focus`, `capacity: {confirmed: bool, description: ...}`, et `actions` ordonnées. Chaque action contient `id` stable, `order` de 1 à N, `kind: collecte|arbitrage|contenu|technique|maillage|mesure`, `title`, `target`, `priority: P1|P2|P3`, `reason`, `expected_effect`, `done_when`, `owner` (nom connu ou null), `lot`, `due` (date connue ou null), `depends_on` (identifiants), `source_refs: [{keyword: ..., ids: [m1, q1]}]`.

Le contrôleur vérifie les rattachements aux analyses, la couverture de tous les mots-clés, les doublons textuels exacts et la cohérence du graphe de dépendances. Chaque mot-clé doit conduire à une action, une collecte ou un arbitrage explicite. Un prérequis précède sa tâche. Les dates fermes sont refusées sans capacité globale confirmée ; la cohérence réelle de cette capacité avec la charge reste à examiner avec le client.

La commande crée un état JSON au même nom que la roadmap Markdown et génère sa vue lisible. Les statuts commencent à « À faire ». Montre la proposition puis attends la validation explicite du plan. Ensuite seulement :

```bash
python3 .claude/skills/roadmap-seo/scripts/plan.py approve --vault . --state ETAT.json --message "ACCORD EXACT DE L'UTILISATEUR" --user-approved
```

## 7. Suivre une seule feuille de route

À chaque reprise, appelle `plan.py status --vault . --state ETAT.json`. Le contrôleur vérifie les versions des stratégies, actualise la page lisible et indique les actions disponibles, celles en cours, les blocages, les tâches à valider et le nombre terminé. Présente d'abord la priorité actuelle, le travail en cours et la prochaine action possible. Ce compteur porte sur des actions terminées ; il ne mesure pas un pourcentage de résultat SEO.

Pour enregistrer une mise à jour autorisée et vérifiée :

```bash
python3 .claude/skills/roadmap-seo/scripts/plan.py update --vault . --state ETAT.json --action R1 --status in_progress --note "Fait observé ou instruction reçue"
python3 .claude/skills/roadmap-seo/scripts/plan.py update --vault . --state ETAT.json --action R1 --status done --note "Critère de fin vérifié" --evidence wiki/preuves/preuve-reelle.md
```

Les statuts sont `todo`, `in_progress`, `blocked`, `review`, `done`. Le démarrage, la mise en validation et la clôture exigent un responsable et des prérequis terminés. La clôture exige un fichier de preuve dans le coffre. Le script vérifie sa présence ; l'agent doit vérifier qu'il établit le critère de fin. Une publication exige une réalisation réellement vérifiée. Chaque mise à jour régénère la même page et garde l'historique.

Un changement de priorité, de contenu, de dépendance, de calendrier ou de responsable modifie le plan. Prépare sa nouvelle version avec `plan.py revise --vault . --manifest CHEMIN --input PROPOSITION.json --message "Correction ou arbitrage de l'utilisateur"`, montre-la puis attends sa validation. Les actions et statuts inchangés sont conservés ; les actions modifiées et leurs dépendants reviennent à réexaminer dans le nouveau plan. Les versions précédentes restent dans `historique/`.

Si une stratégie source change, le suivi est suspendu avec le motif. Revalide la stratégie, produis une nouvelle révision du dossier consolidé en conservant l'ancien, puis réexamine les actions affectées. Une modification de fichier ne vaut pas accord sur sa nouvelle version.
