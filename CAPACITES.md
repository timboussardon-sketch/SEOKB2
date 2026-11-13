# Capacités et limites de SEOKB2 2.3.0

| Composant | État et prérequis |
|---|---|
| Installation, sauvegarde, diagnostic, mise à jour | Python 3.10+ et Git ; accès GitHub pour mise à jour |
| Dashboard local et recherche de notes | Python standard ; recherche textuelle ; aucune base vectorielle requise |
| Base SEO | Corpus filtré du 5 novembre et références du pack élèves 1.5.6 ; certains anciens liens restent hors corpus |
| Skills SEO | Pack élèves 1.5.6 adapté ; les scripts métier conservent leurs dépendances propres |
| Stratégie GEO | Pilote distribué en dix étapes ; collecte réelle conditionnée aux outils disponibles et aux autorisations de coût |
| Team stratégie | Python 3.10+ et Claude Code (`claude`) ou Codex (`codex`, connexion ChatGPT) dans le PATH ; chaque mission d'un spécialiste consomme l'accès de l'élève à cet agent ; spécialistes en lecture seule sur le coffre, le coordinateur enregistre leurs livrables ; testée sur macOS, avec un faux agent et un appel réel de Claude Code |
| Dossier d'opportunités chiffré | Le validateur requiert `python -m pip install jsonschema` ; un dossier qualitatif n'en a pas besoin |
| Citations IA | Panel et analyse utilisables ; service privé de Tim absent ; connecter un outil ou fournir des observations |
| GSC, SERP, navigateurs, API | Accès de l'élève à configurer ; aucune donnée collectée par l'installation |
| Veille arXiv | Collecte manuelle par les outils web disponibles ; pas de runner personnel |
| Agent prospect | Code dans `.seokb/base/agent-prospect/`, à copier hors du coffre ; Node.js et PostgreSQL local ; simulation sans clé ; mode réel : clé API Claude ou Claude Code ; envoi : compte Resend de l'élève ; aucun envoi sans son clic |
| Brief du matin, réponse à un fil | Skills sans dépendance ; lisent le coffre ; messagerie et agenda seulement par un connecteur que l'élève autorise ; rien n'est envoyé ; aucune tâche planifiée |
| Sauvegarde du coffre | Python standard ; destination choisie par l'élève (dossier synchronisé ou disque externe) ; archive non chiffrée ; planification à faire soi-même |
| Index vectoriel, routines, newsletters, campagnes et listes de prospection de Tim | Références historiques archivées ; non installées et non promises comme actives |

La validation de cette version porte sur l'installation, la migration, la conservation des fichiers, les conflits, le diagnostic, la navigation locale et la team stratégie (coordinateur, contrats, enchaînement des phases, provider avec faux agent, un appel réel de Claude Code sur un cas fictif). Elle n'atteste pas une exécution complète de chaque workflow SEO ni une collecte externe. Les nouvelles évolutions métier du coffre de Tim qui ne figurent pas dans le pack portable sont conservées comme références historiques, sans promesse d'exécution.
