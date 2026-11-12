---
type: methode
title: Team stratégie SEO et GEO
aliases: [team-strategie, workflow-team-strategie]
tags: [seo, geo, agents, mots-cles, workflow]
created: 2026-11-12
updated: 2026-11-12
sources: 2
confidence: high
status: stable
---

# Team stratégie SEO et GEO

La team se déclenche pour « stratégie SEO GEO », « strat SEO GEO », « strat client », « stratégie SEO complète » ou « stratégie GEO ». « C'est quoi la suite ? » reprend l'équipe si un projet stratégie est identifiable. Elle retrouve les validations et indique le travail disponible ; la question ne vaut pas approbation.

Le skill est `.claude/skills/team-strategie/SKILL.md`. Les commandes sont dans [[agents/team-strategie-mode-emploi]]. La méthode métier de la stratégie complète reste [[methodes/ai-search-growth-system]] ; chaque mot-clé suit [[methodes/strategie-mot-cle-par-etapes]]. La doctrine est dans [[moc/doctrine-seo-reference]].

## Ordre du parcours

**Go-to-market → stratégie SEO/GEO complète → sélection de 5 à 10 mots-clés business prioritaires → un agent strategie-mot-cle par terme → consolidation de la roadmap.**

Le premier input est le client, son site, ses offres, ses objectifs et ses sources. Les mots-clés ne sont pas un prérequis : les termes fournis au départ sont des pistes d'exploration, pas des priorités validées. Les priorités sortent de la stratégie complète.

## Fonctionnement installé

Le code est dans `.seokb/runtime/team/`. Les données (base SQLite, briefs, workspaces, livrables) sont dans `wiki/projets/team-strategie/data/` du coffre.

| Élément | Fonction |
|---|---|
| team.py | Projets et missions SQLite, phases, accords sur empreinte, corrections et invalidation des dépendances |
| orchestration.py | Enchaînement complet, préparation idempotente, reprise et exécution par vagues avec validations |
| gtm_contracts.py | Diagnostic, segments/offre, parcours/canaux et transmission GTM versionnée |
| contracts.py | Livrables structurés par phase, provenance et contrôles des transmissions |
| providers.py | Appel réel de Claude Code (`claude -p`) ou de Codex ; résultat JSON, méthodes chargées et événements conservés |
| keyword_adapter.py | Chargement des méthodes et validation des données avec le contrôleur canonique de strategie-mot-cle |
| server.py | Dashboard local en lecture seule ; ne lance aucun agent |

Les rôles sont pilote, go-to-market, business, recherche, stratégie par mot-clé, diagnostic SEO, visibilité IA, architecture-roadmap et qualité. Le coordinateur crée les missions de chaque phase selon leurs dépendances et les validations enregistrées. La consolidation finale reçoit toutes les stratégies mot-clé approuvées et refuse un portefeuille incomplet ou un livrable modifié depuis sa validation.

Le mode `seo` traite demande, technique, contenu, maillage, conversion et mesure. Le mode `seo-geo` ajoute les observations IA, la distribution et la mesure commerciale. Un spécialiste lancé par Claude Code lit le coffre sans l'écrire : pas de Bash, pas d'écriture, pas de sous-agent ; la recherche web exige `web: true` dans le brief. Les appels payants exigent un protocole et un budget validés.

## Première partie : stratégie SEO/GEO complète

| Étape | Agent | Sortie soumise à validation |
|---|---|---|
| Cadrage | Pilote | Offres, acheteurs, problème, conversion, sources et inconnues |
| Diagnostic GTM | Go-to-market | Sources, besoins, contradictions et lacunes |
| Segments et offre | Go-to-market | Clients prioritaires proposés, alternatives, positionnement, prix et capacité |
| Parcours et canaux | Go-to-market | Parcours d'achat, goulot, moyens et économie |
| Tests et transmission | Go-to-market | Expériences proposées, mesure et cadrage SEO/GEO versionné par ID GTM |
| Diagnostic et exploration | SEO et recherche | Contrôles du site, candidats business, intentions et questions sourcées |
| Panel IA | Visibilité IA | Questions d'exploration et protocole : moteurs, modes, pays, langue, répétitions et coûts |
| Observations IA | Visibilité IA | Réponses originales, citations, erreurs et limites |
| Opportunités | Business | Besoins, opportunités, conditions et exclusions |
| Architecture | Architecture-roadmap | Destinations existantes ou candidates, preuves, chevauchements et préconisations |
| Roadmap globale | Architecture-roadmap | Actions, moyens, dépendances, distribution et mesure |
| Stratégie complète | Pilote | Synthèse globale, treize parties GEO, choix, candidats admissibles ou exclus et limites |

Le diagnostic et l'exploration SEO ne deviennent disponibles qu'après la transmission GTM approuvée. Les candidats explorés référencent les IDs GTM ; les missions reçoivent les versions approuvées et leurs empreintes. Une correction d'offre ou de cible invalide les travaux dépendants. Les sections de la synthèse référencent les phases correspondantes : un texte générique qui cite seulement le cadrage est refusé.

Une collecte GEO sans aucune réponse réelle reste bloquée : le coordinateur ne collecte pas les réponses des moteurs IA, elles arrivent d'un outil de collecte ou d'un import avec leur reçu d'origine. Un contrôle technique non réalisé reste déclaré comme tel.

## Deuxième partie : priorités business

Après validation de la stratégie complète, le rôle Business propose **5 à 10 mots-clés prioritaires**. Chaque terme est rattaché à l'offre, à la demande ou au besoin documenté, et aux conclusions de la stratégie. Son rang est justifié. Le pilote conserve les candidats exclus et leurs motifs. Un mot-clé exclu ne revient pas dans la liste sans révision de la stratégie. Si les données ne soutiennent pas le nombre attendu, le manque est signalé : aucun mot-clé n'est inventé pour remplir le quota. L'utilisateur valide cette sélection avant le lancement des agents par mot-clé.

## Troisième partie : approfondissement par mot-clé

Un agent logique distinct traite chaque terme sélectionné, par vagues selon les places disponibles. Il garde son contexte pendant ses trois phases :

1. Qualification précise et micro-intentions.
2. Questions des acheteurs : terrain, recherches, expertise, puis hypothèses identifiées.
3. Preuves propriétaires pertinentes, qualité et collectes manquantes.

Chaque phase est soumise à validation. Les agents reçoivent la stratégie globale et la sélection approuvées ; ils approfondissent le sujet sans reconstruire une stratégie globale indépendante.

## Quatrième partie : consolidation et qualité

Quand toutes les stratégies mot-clé sont validées, le rôle Architecture-roadmap affine la roadmap commune : actions dédoublonnées, preuves à collecter, pages à traiter, responsables, capacité et dépendances. Le contrôle qualité confronte ensuite cette consolidation à la stratégie globale, à la sélection et aux travaux des agents. Le dossier ne passe à terminé qu'après un contrôle conforme et la validité de toutes ses dépendances. Une correction sur un mot-clé conserve les phases globales inchangées ; une correction de la stratégie globale invalide les phases qui en dépendent.

## Go-to-market

L'agent applique le skill [[agents/go-to-market]]. Ses phases sont diagnostic commercial, segments/offre, parcours/canaux et tests/transmission. Les lectures et les propositions précèdent chaque accord humain. Le rôle Business continue de traiter les opportunités de recherche et les priorités par mot-clé.

Le workflow 4 est le défaut des nouveaux projets. Changer les mots-clés sélectionnés après la création des agents exige une nouvelle version explicite de projet ; les missions existantes ne sont pas effacées.
