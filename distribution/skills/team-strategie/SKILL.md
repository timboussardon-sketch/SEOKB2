---
name: team-strategie
description: "Équipe d'agents pour une stratégie SEO GEO complète. « strat SEO GEO », « stratégie SEO complète »."
---

## Quand utiliser ce skill

Piloter une équipe pour une stratégie SEO GEO complète ou une stratégie client : cadrage go-to-market, stratégie SEO/GEO complète, sélection de 5 à 10 mots-clés business prioritaires ensuite, puis un agent strategie-mot-cle par terme et roadmap affinée. Déclencheurs : « stratégie SEO GEO », « strat SEO GEO », « strat client », « stratégie SEO complète », « stratégie GEO », « team stratégie ». « C'est quoi la suite ? » reprend cette équipe quand le contexte concerne une stratégie client ; sans projet identifiable, demander lequel.

# Team stratégie SEO et GEO

L'utilisateur s'adresse au pilote ; le coordinateur conserve les projets, les missions, les livrables et leurs validations. Un agent Go-to-market prépare les choix commerciaux et les transmet aux spécialistes SEO/GEO. Un agent distinct traite chaque mot-clé business. Les rôles travaillent à la demande, sans cron.

## Prérequis

- Claude Code (commande `claude`) ou Codex (commande `codex`, connexion ChatGPT) dans le PATH. Le coordinateur lance chaque spécialiste avec cet agent. `SEOKB_TEAM_AGENT=claude` ou `codex` impose le choix ; sans variable, Claude Code passe en premier. Chaque mission consomme l'accès de l'utilisateur à cet agent : limiter les vagues avec `--max-jobs`, et fixer un plafond par mission avec `SEOKB_TEAM_MAX_BUDGET_USD` si l'accès est facturé à l'usage.
- Python 3.10+. Un dossier d'opportunités chiffré passe par un validateur qui requiert `python -m pip install jsonschema` ; un dossier qualitatif, sans estimation chiffrée, n'en a pas besoin.
- Les skills `go-to-market`, `strategie-geo`, `strategie-mot-cle`, `strategie-contenu`, `roadmap-seo`, `geo-citations`, `seo-recherche-mots-cles`, `indexation-check`, `maillage-systeme` et `seo-core-web-vitals`. Un fichier de méthode absent arrête la mission et nomme le fichier manquant : mettre SEOKB2 à jour (`python .seokb/runtime/update.py`), puis relancer la session.

Dans la suite, RACINE désigne `.seokb/runtime/team` (relatif à la racine du coffre) et `python` désigne la commande Python du poste (`python3`, `python` ou `py -3`). Lancer les commandes avec `-X utf8`, comme le dashboard du coffre.

## Entrée et routage

**Ordre : cadrage commercial Go-to-market → stratégie SEO/GEO complète → sélection de 5 à 10 mots-clés business prioritaires → un agent strategie-mot-cle pour chacun → consolidation de la roadmap.**

L'entrée est le client, son site, ses offres, ses objectifs, son coffre et les données disponibles. Aucune liste de mots-clés n'est obligatoire au lancement. Les termes éventuellement fournis sont des pistes d'exploration ; leur présence ne vaut pas sélection finale. Après le cadrage initial du pilote, l'agent `go-to-market` exécute son diagnostic, ses choix d'offre, son parcours commercial et sa transmission en phases validées. La stratégie globale exécute ensuite la méthode GEO/SEO et ses validations, puis le pilote en extrait les 5 à 10 priorités business justifiées. Ne pas remplacer cette stratégie complète par un simple cadrage ou par une liste de termes. Ne pas inventer des mots-clés pour atteindre un quota : une sélection insuffisamment étayée reste en attente. Un mot-clé explicitement demandé seul conserve son workflow isolé.

Lire `.seokb/AGENTS.md`, `.seokb/base/wiki/moc/doctrine-seo-reference.md`, `.seokb/base/wiki/agents/team-strategie.md` et `.seokb/base/wiki/agents/team-strategie-mode-emploi.md`. La méthode GEO reste `.claude/skills/strategie-geo/SKILL.md` ; son rôle devient métier sous ce pilote. Le workflow technique n'atteste jamais une collecte.

Si tu reçois déjà une mission structurée (project, mission, upstream), exécute seulement ce rôle et cette phase. Ne relance ni équipe ni sous-pilote.

## Reprendre avant de créer

Données : `wiki/projets/team-strategie/data/` du coffre (base `team.sqlite3`, briefs, workspaces, livrables).

Exécuter `python -X utf8 RACINE/team.py status`. Retrouver le client par site, coffre, demande et contexte de conversation ; ne jamais choisir le dernier projet global par défaut. Pour « c'est quoi la suite ? », appeler `next ID_PROJET`, lire les livrables et leurs validations, puis expliquer la phase actuelle, ce qui attend l'utilisateur et la prochaine tâche possible. Cette question seule n'approuve aucun livrable. Une action déjà autorisée peut continuer ; une phase en revue reste en attente de validation.

Lancer le dashboard : `python -X utf8 RACINE/server.py --port 0`, vérifier que l'adresse imprimée répond, puis la transmettre. `--port 9013` fixe le port par défaut. Ne pas arrêter un autre service occupant le port.

## Lancer le workflow complet

Préparer un brief JSON dans `wiki/projets/team-strategie/data/briefs/` : `name`, `site`, `objective`, `request` exact, `mode` (`seo` ou `seo-geo`), `vault` absolu du client (le coffre actuel par défaut), `keywords` facultatif (pistes seulement), `sources`, contexte commercial et contraintes. Le format de projet est le workflow 4 par défaut. `web: true` autorise la recherche publique nécessaire, jamais une dépense API implicite.

`python -X utf8 RACINE/team.py start BRIEF.json` crée le projet au format workflow 4 et sa mission de cadrage.

Le pilote emploie ensuite :

```sh
python -X utf8 RACINE/team.py next ID_PROJET
python -X utf8 RACINE/team.py prepare ID_PROJET
python -X utf8 RACINE/team.py run-ready ID_PROJET --max-jobs 3 --workers 3
```

`next` lit seulement. `prepare` crée de façon idempotente les prochaines missions dont les prérequis sont validés. `run-ready` exécute une vague bornée de missions disponibles ; il ne valide aucun retour et ne franchit aucune phase humaine. Répéter les vagues pour les autres agents de la même phase autorisée, selon les limites disponibles. Les échecs demandent un diagnostic puis une reprise explicite.

Présenter les livrables et leur portée. Après l'accord exact de l'utilisateur sur la version présentée :

```sh
python -X utf8 RACINE/team.py approve ID_MISSION SHA --message "ACCORD EXACT DE L'UTILISATEUR" --user-approved
```

Une validation groupée doit identifier les mots-clés et versions ; enregistrer les accords correspondants individuellement. L'autorisation de construire la team n'approuve aucun livrable client.

## Transmissions entre les agents

| Phase | Responsable et entrée | Sortie attendue avant transmission |
|---|---|---|
| Cadrage global | Pilote ; client, site, offres, objectifs et données | Périmètre commercial et inconnues, sans exiger de mots-clés |
| Diagnostic commercial GTM | Go-to-market ; cadrage initial validé | Sources, besoins, faits, contradictions et accès manquants |
| Segments et offre | Go-to-market ; diagnostic GTM validé | Segments comparés, rôles acheteurs, alternatives, positionnement, prix et capacité |
| Parcours et canaux | Go-to-market ; offre validée | Parcours, goulot, canaux, moyens et économie avec limites |
| Tests et transmission | Go-to-market ; parcours validé | Expériences proposées, mesure, roadmap conditionnelle et fiche SEO/GEO versionnée par ID GTM |
| Diagnostic et exploration | SEO et recherche ; transmission GTM validée | Constats, candidats business, intentions et questions sourcées à l'échelle du site |
| Panel et observations GEO | Visibilité IA ; exploration validée | Protocole validé puis réponses originales, sources et limites |
| Opportunités, architecture et roadmap globales | Business puis architecture-roadmap | Stratégie globale construite par étapes validées, avec preuves, distribution et mesure |
| Stratégie SEO/GEO complète | Pilote ; phases globales approuvées | Dossier complet en treize parties GEO, choix et limites |
| Priorités business | Business ; stratégie complète validée | 5 à 10 mots-clés prioritaires issus de la stratégie, rang justifié et références |
| Stratégies par mot-clé | Un agent par mot-clé sélectionné | Intentions → questions terrain → preuves, avec accord séparé à chaque phase |
| Consolidation | Architecture-roadmap ; toutes les stratégies mot-clé validées | Roadmap affinée et commune, collectes et dépendances dédoublonnées |
| Contrôle final | Qualité ; stratégie globale, sélection et consolidation approuvées | Conformité ou corrections |

Le rôle `go-to-market` applique `.claude/skills/go-to-market/SKILL.md` et les références de sa phase, dont `references/passage-seo-geo.md` pour la transmission. Le provider charge ces fichiers et conserve leurs empreintes. Les quatre phases sont `gtm-diagnostic` (sections 1–2), `gtm-offre` (3–4), `gtm-parcours` (5–6), `gtm-transmission` (7–8). Chaque phase attend son accord humain avant la suivante ; le spécialiste exécute uniquement la sous-mission reçue.

Réutiliser un dossier GTM existant en vérifiant ses sources, sa fraîcheur et les accords exacts ; un test ou un ancien diagnostic non validé n'est pas une transmission approuvée. La fiche partagée conserve offres, segments, zones, langues, rôles, besoins, alternatives, preuves, prix, moyens, conversions et rôle du SEO/GEO par références aux phases approuvées. Les candidats SEO portent leurs IDs GTM. Une modification commerciale implique une révision de la phase concernée et de ses dépendants.

L'ajout du rôle ne lance aucun test commercial, campagne ou dépense. Le rôle Business conserve l'évaluation des opportunités de recherche et la sélection des mots-clés après la stratégie complète ; il ne remplace pas le Go-to-market.

Le mode `seo` omet panel et observations IA. La phase globale conserve ses validations : on ne lance pas une mission monolithique qui les contourne. L'exploration peut étudier davantage de candidats que les priorités finales. Aucun agent `strategie-mot-cle` n'est créé avant validation de la stratégie complète et de la sélection. Chaque agent conserve son identité logique et ses phases précédentes.

Les workflows 1, 2 et 3 restent lisibles et exécutables ; le workflow 4 s'applique aux nouveaux projets. Changer la liste prioritaire après le lancement des agents demande une nouvelle version explicite de projet ; ne pas effacer les missions précédentes.

Chaque retour doit respecter son contrat métier dans `contracts.py` : un Markdown générique ne suffit pas. Les références aux entrées portent leur mission et leur empreinte ; modifier une entrée invalide les dépendances. Les payloads mots-clés gardent le validateur canonique dans `keyword_adapter.py`.

Le parcours complet se termine seulement lorsque le contrôle final est validé avec un verdict conforme et que les dépendances restent valides. Une roadmap seule ou un fichier présent n'est pas une stratégie terminée. « C'est quoi la suite ? » montre les propositions en attente, les blocages précis ou les prochaines tâches autorisées.

## Outils, limites et corrections

Chaque spécialiste reçoit la méthode réelle et le contrat de sa phase. Le provider local charge les fichiers de méthode avant l'appel. Les données et citations doivent provenir des sources du client ou de collectes attestées. Un outil absent se signale ; il ne se remplace pas par une observation inventée. Les réponses IA existantes peuvent être exploitées depuis leurs fichiers originaux. La collecte des réponses des moteurs IA (phase `observations`) n'est pas faite par le coordinateur : elle exige un outil de collecte ou des réponses fournies, importées avec leur reçu d'origine. Les appels payants ne sont pas activés par le workflow local ; une collecte nécessitant un fournisseur payant reste bloquée jusqu'à son exécution distincte autorisée et documentée.

Un spécialiste lancé par Claude Code lit le coffre du client et la base commune ; il n'a ni Bash, ni écriture, ni sous-agent. Son livrable revient en JSON et le coordinateur l'enregistre. La recherche web n'est ouverte que si le brief porte `web: true`.

`python -X utf8 RACINE/team.py revise ID_MISSION --message "CORRECTION"` conserve l'ancien résultat et remet les dépendants à examiner. `retry` traite un échec technique après diagnostic ; `recover` traite une interruption lorsque le processus propriétaire est arrêté. Aucune relance automatique illimitée.

Les spécialistes écrivent dans leur workspace. La rédaction conserve ses phases ; publication et envoi restent distincts. L'interface du dashboard sert au suivi : la priorité est l'exécution des missions et la transmission correcte des livrables.

## Provenance et remise

Le pilote est responsable du catalogue, du journal et des documents communs. Conserver les sources originales du coffre client et ne jamais écrire dans raw/. Une API n'est pas l'interface publique d'un moteur IA ; erreur ou collecte absente ne signifie pas absence de citation.

Les résultats keyword contiennent `keyword_payload`, contrôlé par `keyword_adapter.py` avec le workflow canonique. Le journal d'exécution conserve les méthodes chargées et les événements du vrai appel, avec l'agent, le modèle et le coût rapportés par Claude Code. `submit` sert aussi à enregistrer un résultat produit dans une session déléguée : nommer honnêtement cette provenance et ne jamais la faire passer pour un appel CLI.

À chaque remise : lien du dashboard, phase et périmètre, livrable, sources, agents et outils réellement exécutés, limites et décision attendue. Distinguer configuration, essais techniques et mission client réelle.
