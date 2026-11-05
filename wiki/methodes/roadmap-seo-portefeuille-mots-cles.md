---
type: methode
title: Une stratégie par mot-clé et une roadmap SEO commune
aliases: [roadmap-seo-portefeuille, consolidation-strategies-mots-cles]
tags: [seo, agents, roadmap, mots-cles, orchestration]
created: 2026-10-24
updated: 2026-10-24
sources: 3
confidence: medium
status: draft
---

# Une stratégie par mot-clé et une roadmap SEO commune

Consigne de Tim du 24 octobre : les mots-clés business ou importants du site sont analysés séparément par l'agent stratégie mot-clé ; leurs résultats alimentent ensuite une seule roadmap. Cinq mots-clés donnent cinq missions et cinq dossiers de stratégie, puis un plan pour l'ensemble du site. [[methodes/strategie-mot-cle-par-etapes]]

Le skill `.agents/skills/roadmap-seo/SKILL.md` orchestre ce parcours. Son script `scripts/consolidate.py` vérifie les états réellement enregistrés et produit le dossier d'entrées de la roadmap. La commande de contrôle ne crée pas de sous-agents et ne remplace pas leurs recherches. La délégation appartient à l'agent principal et doit être tracée lorsqu'elle est disponible.

## Parcours et validations

| Moment | Résultat | Validation attendue |
|---|---|---|
| Portefeuille | Mots-clés retenus, contexte client, raison de leur importance et contraintes du site | Périmètre donné ou validé par Tim |
| Missions indépendantes | Pour chaque mot-clé : qualification et intentions, questions du terrain, matière qualifiée | Trois validations propres à chaque stratégie |
| Consolidation du site | Actions candidates, besoins communs, destinations, preuves, collecte et dépendances | Arbitrage du consultant sur les actions et destinations |
| Roadmap unique | Ordre, responsables, planning global et mesure attendue | Validation du plan commun |

Les agents travaillent en parallèle dans la limite des outils disponibles, puis par vagues. Le nombre de missions reste égal au nombre de mots-clés ; le nombre de processus simultanés dépend de la capacité d'exécution. Une validation groupée n'est recevable que si Tim approuve explicitement les livrables et mots-clés concernés. Le dossier final conserve les validations individuelles.

## Contrôle des entrées

Un manifeste du portefeuille référence le site, chaque mot-clé et son fichier d'état, le dossier consolidé et le chemin de la roadmap commune. `check` indique le nombre attendu, les stratégies validées et les blocages. `bundle` exige que toutes les stratégies aient leurs trois phases validées, leurs traces d'accord, leurs versions de méthodes chargées et leurs données conformes aux contrôles du skill stratégie. Les états appartiennent au même coffre et leurs mots-clés correspondent au manifeste.

Le dossier consolidé contient les copies des résultats validés et les empreintes SHA-256 des états. Une entrée modifiée pendant la consolidation la bloque. Un dossier déjà produit est réutilisé si les entrées sont identiques ; un changement demande une nouvelle révision pour préserver l'historique. La cohérence sémantique du contexte client et des propositions reste examinée par l'agent et le consultant.

La présence des empreintes atteste les versions des fichiers utilisées. Elle ne prouve pas un appel API ou une recherche terrain. Les livrables conservent leur provenance réelle, y compris les hypothèses et les collectes absentes.

## Consolider avant de programmer

La roadmap regroupe les besoins équivalents et les actions communes aux mots-clés. Un mot-clé n'impose pas une page ; une page peut couvrir plusieurs formulations. Une destination nouvelle reste soumise aux pré-décisions URL et aux vérifications prévues par la méthode mots-clés. Aucun regroupement proposé ne lance une fusion ou une redirection automatique. [[methodes/rapport-mots-cles-format]]

Le tableau d'arbitrage présente, pour chaque action, les mots-clés servis, les intentions et questions sources, la destination, la justification business, la matière, les données à collecter et les dépendances. La validation de ce tableau précède le calendrier.

La priorité croise l'importance business, la demande observée, les urgences démontrées, les dépendances et les ressources du client. Le score de matière ne suffit pas à classer tous les sujets. Un mot-clé important pauvre en données peut justifier une collecte avant sa rédaction.

## Une capacité globale et un plan commun

Le séquencement peut réutiliser les principes de `seo-roadmap-pseo`, mais sa liste brute et ses valeurs par défaut ne remplacent pas les stratégies validées. L'horizon dépend du mandat et la capacité s'applique à tout le portefeuille. Si le client peut produire deux pages sur une période, cinq agents ne lui donnent pas cinq fois cette capacité.

La roadmap commune distingue les actions prêtes, les collectes et les blocages. Chaque ligne conserve ses mots-clés et analyses sources, son responsable, ses prérequis, son ordre justifié et sa mesure. Un travail partagé entre plusieurs mots-clés n'est planifié qu'une fois.

La validation du plan ne pré-valide pas la rédaction. Pour chaque page retenue, brief, Hn, données et texte suivent leurs propres étapes. Un changement dans une stratégie source conduit à réexaminer les actions affectées et à conserver les versions précédentes du plan. [[moc/doctrine-seo-reference]] [[methodes/framework-creation-agent-specialise]]

## État de réalisation

Le contrat d'orchestration, le contrôle de consolidation, le contrôleur de plan et de suivi et leurs tests sont installés dans le skill local. Une liste réelle de mots-clés et le contexte du site sont nécessaires pour lancer les sous-agents. Aucun lancement réel de plusieurs agents ou calendrier client n'est attesté par les tests unitaires de cette méthode.

## Une page lisible pour travailler

La page principale répond à quatre questions : où en est-on, que fait-on maintenant, qu'attend-on et qu'a-t-on déjà fait ? Les tableaux montrent l'action, sa raison ou la réponse attendue, qui s'en occupe et son état. Ils séparent le travail en cours, la suite, les attentes et les actions précédentes.

Les noms de fichiers, les identifiants internes, les codes de priorité et les journaux techniques restent dans les fichiers de suivi. Une attente nomme le travail à terminer ou la décision nécessaire, avec des mots simples. Le détail d'une action explique la page concernée, le résultat attendu et ce qui permet de la considérer terminée.

Un travail commun à plusieurs mots-clés occupe une seule ligne, avec plusieurs références stratégiques. Les prérequis forment un graphe sans cycle et sont placés avant les tâches qui en dépendent. La cohérence sémantique du regroupement et des priorités est soumise au consultant.

## Proposition, validation et suivi

`scripts/plan.py propose` reçoit la proposition d'actions, vérifie ses sources et produit la page Markdown et son état. La roadmap reste proposée jusqu'à `approve`, appelé avec l'accord explicite de Tim sur ce plan. Une tâche ne démarre pas sur une version non validée.

`status` expose les actions disponibles et les blocages et actualise la page, y compris les avertissements sur les stratégies modifiées. `update` enregistre un statut et un fait documenté, puis régénère la même page. Les statuts sont À faire, En cours, Bloquée, À valider et Terminée. Une tâche en attente de prérequis ou sans responsable est signalée ; le contrôleur bloque son démarrage. Une tâche terminée possède une preuve dans le coffre, dont l'agent vérifie le contenu au regard du critère de fin. Un fichier existant ne démontre pas, à lui seul, une publication ou un résultat SEO.

Le nombre d'actions terminées décrit l'exécution du plan. La mesure SEO et business conserve ses sources et ses jalons propres. Le suivi client et le reporting peuvent lire cet état ; ils ne doivent pas tenir une seconde liste concurrente de ces actions.

`revise` prépare un changement du plan, conserve son historique et demande une nouvelle validation. Les actions inchangées conservent leur suivi ; les actions modifiées, celles affectées par une stratégie source changée et leurs dépendants sont réexaminées. Une stratégie modifiée bloque le suivi jusqu'à sa nouvelle consolidation.
