# Vérification SEOKB2 2.1.0 — 12 novembre 2026

Vérifications locales exécutées avec Python sur macOS.

Team stratégie :

- 84 tests (`tests/team`, jsonschema 4.25.1), sans appel de modèle : contrats métier, enchaînement des phases (go-to-market, stratégie, mots-clés, roadmap), validations humaines, reprise après interruption, et provider (commande Claude Code en lecture seule, trace d'exécution, erreurs sans relance, extraction du JSON, Codex avec connexion ChatGPT, arrêt à l'échéance).
- Installation dans un coffre neuf par l'installateur réel : `doctor.py` indique `2.1.0` et aucun fichier manquant ou altéré ; le dashboard du coffre et celui de la team répondent en HTTP (page, script, feuille de style).
- Deux appels réels de Claude Code (Sonnet 5.5) sur une entreprise fictive, dans un coffre jetable : lecture seule, aucun refus de permission. Le premier a été refusé par le contrat (`business.problem` nul, alors que l'instruction autorisait des valeurs nulles) ; l'instruction de la mission de cadrage a été corrigée. Le second (5 tours, 61 s, 0,28 $) a livré un cadrage accepté par les contrats, enregistré avec son coût et ses méthodes.

Autres skills portés avec leur code :

- `roadmap-seo` : 15 tests. `strategie-mot-cle` : 10 tests, contre le workflow installé chez l'élève.
- `maillage-systeme` : crawl d'un site fictif servi en local ; une page reçoit trois liens d'une page et un lien d'une autre, le script compte 2 pages sources et 4 liens.

Installation, migration, conflits, retour arrière : `python3 tests/test_install.py` (8 tests).

Limites : les tests ont été exécutés sur macOS, pas sur Windows (le provider écarte `--json-schema` sous Windows et demande le JSON dans le prompt, sans test réel). Un seul appel de Claude Code de la mission de cadrage a abouti ; les autres phases (go-to-market, exploration, stratégie, roadmap) sont validées avec des réponses simulées, pas avec un modèle. Le mode Codex n'a pas été exécuté. Les skills `go-to-market` et `strategie-geo` n'ont pas été lancés sur un client réel. Voir CAPACITES.md.

# Vérification SEOKB2 2.0.0 — 6 novembre 2026

Vérifications locales exécutées avec Python sur macOS :

- Installation neuve et installation dans un chemin contenant des espaces.
- Migration depuis les fichiers Git de la version 1.5.5.
- Migration depuis une copie complète de la version 1.5.6, avec skills déjà copiés dans .claude/skills.
- Conservation des notes, des sources et des réglages personnels.
- Réinstallation sans changement ; conflit local refusé avant écriture.
- Liens symboliques refusés ; restauration des fichiers après une erreur d'écriture simulée.
- Retour arrière d'une installation neuve.
- Diagnostic des coffres migrés : aucun fichier géré manquant ou altéré.
- Contrôle HTTP du dashboard : accueil, sources, base commune, recherche, lecture d'une note personnelle et du catalogue commun. Traversée hors coffre refusée.
- Validation des skills seokb et mise-a-jour avec quick_validate.py.

Limites : le navigateur de contrôle était indisponible, donc aucune validation visuelle n'est attestée. Les tests ont été exécutés sur macOS, pas sur Windows. Les workflows SEO et les intégrations externes ne sont pas tous exécutés par ces tests.
