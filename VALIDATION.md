# Vérification SEOKB2 2.3.1 — 13 novembre 2026

- `python3 tests/test_verification_maj.py` : 7 tests (annonce d'une version plus récente avec ses nouveautés, silence le même jour, silence si à jour, dépôt inaccessible sans blocage, ajout du hook en conservant les réglages et hooks existants, coffre neuf, réglages illisibles non touchés, réglages modifiés ensuite sans conflit ni alerte de `doctor.py`). `tests/test_install.py` : 8 tests. `tests/test_sauvegarde.py` : 4 tests.
- Coffre neuf installé par l'installateur réel, version locale forcée à 2.2.0 : le hook interroge le vrai dépôt GitHub et annonce la 2.3.0 ; un second appel le même jour ne dit rien.
- Session réelle `claude -p` (Haiku) dans ce coffre : la première réponse propose la mise à jour avec les nouveautés et indique qu'elle ne sera lancée qu'avec accord.

Limites : l'affichage du message dans le terminal interactif n'a pas été observé (le mode `-p` ne montre que la réponse). Non testé sous Windows (le hook passe par `bash`, comme les versions précédentes).

# Vérification SEOKB2 2.3.0 — 13 novembre 2026

Vérifications locales exécutées sur macOS avec Python :

- `python3 tests/test_sauvegarde.py` : 4 tests (aller-retour, exclusion de `.env*`, `_backups/` et `.seokb/base/`, destination dans le coffre refusée, rotation, restauration dans un dossier non vide refusée).
- `python3 tests/test_install.py` : 8 tests.
- Installation dans un coffre neuf par l'installateur réel : `doctor.py` indique 2.3.0, 1253 fichiers contrôlés, aucun manquant ou altéré ; les skills `brief-matin`, `reponse-fil` et `sauvegarde-coffre` arrivent dans `.claude/skills/`.
- Dashboard du coffre neuf servi en local : la page d'accueil affiche le dernier fichier de `wiki/pilotage/brief-matin/`.
- Sauvegarde du coffre neuf vers un dossier extérieur puis restauration dans un dossier vide : les notes sont retrouvées.
- Lignes ajoutées scannées : aucun chemin `/Users/`, nom de Tim, de client ou de prospect, clé ni adresse réelle.

Limites : les skills `brief-matin` et `reponse-fil` n'ont pas été exécutés par un modèle dans un coffre élève ; la version source de `brief-matin` a tourné une fois sur le coffre de Tim. Aucun connecteur Gmail ou agenda testé côté élève. Non testé sous Windows.

# Vérification SEOKB2 2.2.0 — 12 novembre 2026

Vérifications locales exécutées sur macOS (Node 22.23.4, PostgreSQL 15 local) :

- Agent prospect, avant modification : 85 tests sur 86. Le test en échec (`missions.test.ts`, relances) l'était déjà dans la source : l'email envoyé porte l'URL de l'expéditeur en dernière ligne, le test attendait le texte seul. Corrigé.
- Après neutralisation de l'identité : `tsc --noEmit` sans erreur, 87 tests sur 87 (deux tests ajoutés : bandeau configuré joint par CID, absence de bandeau sans `EMAIL_BANNER_FILE`). Une exécution sur quatre a donné 1 échec en 370 s, non reproduit à la relance (20 s) ; cause non identifiée.
- `python3 tests/test_install.py` : 8 tests.
- Installation dans un coffre neuf par l'installateur réel : `doctor.py` indique 2.2.0, 1249 fichiers contrôlés, aucun manquant ou altéré. Les 113 fichiers de l'agent arrivent dans `.seokb/base/agent-prospect/`, le skill dans `.claude/skills/agent-prospect/`. L'agent installé est identique octet pour octet à la copie testée.
- Recherche dans l'arbre de l'agent et du skill : aucun chemin `/Users/`, nom d'entreprise ou de personne de Tim, clé, ni adresse réelle. Les adresses des tests sont fictives (`.example`, `.test`).

Limites : `next build` non lancé, seulement `tsc`. Les pages du tableau de bord (`/suivi`, `/r/<jeton>`, aperçu d'email) n'ont pas été ouvertes. Aucun appel réel à Claude, à Resend ou à Gmail, aucun email envoyé. Non testé sous Windows : `scripts/db-start.sh` et `scripts/service.sh` supposent un shell POSIX.

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
