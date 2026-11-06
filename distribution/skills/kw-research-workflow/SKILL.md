---
name: kw-research-workflow
description: "Recherche de mots-clés quasi automatique : Keyword Planner, GSC, verbatims, pSEO, Google Sheet scoré. « recherche mots-clés »."
---

# Skill — Workflow Recherche Mots-Clés (orchestrateur)

## Quand utiliser ce skill

Orchestrer la recherche de mots-clés complète en mode quasi-automatique.
Enchaîne les 5 étapes (Keyword Planner CSV → GSC CSV → DeepSearch web →
verbatims → pSEO) et produit un Google Sheet final scoré sur 5 critères
(volume, CPC, intérêt business, difficulté, YoY, signaux de demande séparés). Étape 1 du
workflow mots-clés complet en 14 étapes ; la sortie finale est le rapport de pré-décision
(une pré-décision URL par cluster ou la raison de la non-décision, score business sur 5,
documents du vault, matière qualifiée, SERP) ; sans lui le workflow n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur mentionne : recherche mots-clés,
workflow keyword research, analyse mots-clés complète, "trouve-moi des mots-clés
pour [client]", brief mots-clés, kw research, "j'ai un nouveau client à analyser",
audit mots-clés, "fais-moi le workflow complet", ou uploade un export Keyword
Planner / GSC et veut un livrable scoré et priorisé.

## Rôle

Exécuter le workflow recherche mots-clés Boussardon de bout en bout en chaînant 5 phases. L'utilisateur fournit la matière première (CSV + verbatims). Le skill produit le livrable final : un Google Sheet (ou .xlsx local) scoré sur 5 critères, avec une synthèse en 5 lignes des actions prioritaires.

Ce skill orchestre, il ne réinvente pas. Il appelle les sous-skills existants : `seo-quick-win`, `seo-cannibalisation`, `seo-programmatique-pseo`.

---

## Phase 0 — Cadrage (BLOQUANT)

Avant TOUTE exécution, poser les 6 questions suivantes en une seule passe via AskUserQuestion :

1. Quel est le **secteur / activité** du client ?
2. Quelle est l'**offre principale** à pousser commercialement ?
3. Qui est le **persona cible** (rôle, taille d'entreprise, zone géo) ?
4. As-tu un **export Keyword Planner** (CSV) ? Si non : skip phase 1.
5. As-tu un **export GSC** sur 90 jours ? Si non : noter "site neuf, à activer post-data".
6. As-tu des **verbatims clients** (calls, mails, témoignages) ? Si non : tenter Gmail/LinkedIn MCP, sinon flagger comme manquant.

**NE PAS lancer la phase 1 avant d'avoir les réponses.**

---

## Phase 1 — Keyword Planner

Si CSV fourni :
1. Lire le CSV depuis le dossier Cowork (Read tool, ou skill `xlsx` si .xlsx)
2. Filtrer : volume > 100, exclure les requêtes brand
3. Tagger chaque mot-clé par intention probable :
   - **Décisionnelle** : prix, comparatif, meilleur, avis, vs
   - **Transactionnelle** : achat, devis, urgence, réserver
   - **Informationnelle** : comment, pourquoi, qu'est-ce que, guide
   - **Navigationnelle** : marque + terme
4. Garder une liste interne avec : mot-clé, volume, CPC, intention.

Si pas de CSV : skip et noter "phase 1 = à compléter manuellement".

---

## Phase 2 — Search Console

Si CSV GSC fourni :
1. Appeler le skill `seo-quick-win` sur le CSV → récupérer le top 10 quick wins
2. Si plusieurs URLs apparaissent sur les mêmes requêtes : appeler `seo-cannibalisation`
3. Identifier les **content gaps** : requêtes avec impressions > 100 sans page dédiée
4. Tagger ces nouveaux mots-clés "content_gap" dans la liste interne

Si pas de GSC : noter "site neuf — bypass phase 2" et passer.

---

## Phase 3 — DeepSearch web (équivalent Grok via WebSearch Claude)

Lancer 4 recherches en séquence, **dans cet ordre exact**.

### Search 1 — Cartographier le consensus
```
WebSearch : "[SUJET] guide" OR "[SUJET] définition" OR "comment [VERBE] [SUJET]"
```
Synthétiser : les 5-7 affirmations les plus répétées + les stats les plus citées avec source.

### Search 2 — Données fraîches praticiens
```
WebSearch : "[SUJET] case study 2025" OR "[SUJET] retour expérience" OR
            "[SUJET] résultats" site:reddit.com OR site:medium.com
```
Récupérer : retours terrain chiffrés, échecs documentés, débats experts.

### Search 3 — Stats récentes (< 60 jours)
```
WebSearch : "[SUJET] étude 2025" OR "[SUJET] rapport 2026" OR
            "[SUJET] benchmark" filetype:pdf
```
Récupérer : sources primaires, chiffres vérifiables avec date < 60 jours.

### Search 4 — Synthèse (PAS de search ici)
Croiser les résultats des 3 recherches précédentes. Sortir un tableau :

| Angle | Source consensus | Source contradiction | Pourquoi c'est un gap |

Tagger ces mots-clés "angle_exclusif" dans la liste interne.

---

## Phase 4 — Données propriétaires

Si verbatims fournis (file ou collés) :
1. Lire les verbatims (Read tool)
2. Extraire les formulations qui reviennent **3 fois ou plus**
3. Identifier les pain points en langage naturel
4. Tagger ces formulations "verbatim_client" — ce sont des mots-clés longue traîne haute intention

Si Gmail MCP connecté ET utilisateur d'accord :
1. Demander permission de scanner les mails du persona (boîte cliente)
2. Extraire les questions récurrentes en signature de prospects
3. Tagger "verbatim_email"

Si LinkedIn MCP connecté :
1. Scanner les commentaires des posts du client (engagement > 5)
2. Extraire les expressions répétées
3. Tagger "verbatim_linkedin"

Si rien de tout ça : flagger "phase 4 = à compléter manuellement par le client".

---

## Phase 5 — pSEO (appel sous-skill)

Appeler le skill `seo-programmatique-pseo` avec en entrée :
- Le contexte client de la phase 0
- La liste de mots-clés agrégée (phases 1 + 2 + 3 + 4)
- Les verbatims propriétaires (phase 4)

Récupérer en sortie :
- 5 modèles pSEO proposés (au minimum)
- La matrice de priorisation
- Les keywords longue traîne par modèle

Ajouter ces keywords à la liste interne, taggés "pseo_model_X".

---

## Phase 6 — Livrable final

Construire le tableau final avec **5 colonnes scorées** dans cet ordre :

| Mot-clé | Volume | CPC | Intérêt business (1-5) | Difficulté (1-5) | YoY (%) | Signaux de demande |

Règles de scoring :
- **Volume** : depuis Keyword Planner (chiffre brut). Si absent : N/A.
- **CPC** : depuis Keyword Planner (€). Si absent : N/A.
- **Intérêt business** : note 1-5 basée sur l'intention (Décisionnelle = 5, Transactionnelle = 4, Info = 2-3, Navi = 1) ET le tag (verbatim_client = +1, content_gap = +1).
- **Difficulté** : note 1-5 basée sur la position GSC actuelle (top 3 = 1, position 4-10 = 2, 11-20 = 3, hors top 20 = 4, pas de page = 5). Si pas de GSC : 3 par défaut.
- **YoY** : tendance Keyword Planner ou Google Trends (% évolution). Si absent : N/A.
- **Signaux de demande** : affichés séparément, jamais agrégés en niveau ; signaux possédés (variantes Suggest, impressions GSC, fréquence dans les calls, acteurs spécialisés ; PAA, YouTube, Trends si disponibles), signaux bruts à côté. Méthode : audit-complet-v2/demande-observee.md. Remplace le volume quand il manque, ne l'estime jamais.

### Si Google Sheets MCP connecté
1. Créer un nouveau Sheet nommé "KW_Research_[Client]_[Date]"
2. Coller les 6 colonnes (mot-clé + 5 scores)
3. Ajouter une 7e colonne "Tag" pour la traçabilité (kp / gsc_qw / content_gap / angle_exclusif / verbatim_X / pseo_model_X)
4. Mise en forme : header gras orange, alternance lignes, freeze 1ère ligne
5. Tri par défaut : Intérêt business desc, Difficulté asc
6. Filtre actif sur toutes les colonnes
7. Récupérer le lien partageable

### Sinon
1. Appeler le skill `xlsx` pour créer le .xlsx équivalent
2. Sauvegarder dans le dossier Cowork de l'utilisateur sous `KW_Research_[Client]_[Date].xlsx`

---

## Phase 7 — Synthèse finale (OBLIGATOIRE)

Puis enchaîner les étapes 2 à 14 du workflow complet (`.seokb/base/wiki/methodes/workflow-mots-cles-complet.md`) jusqu'au rapport de pré-décision.

Sortir une synthèse en **exactement 5 lignes** dans le chat (avant le lien) :

```
TOP 3 QUICK WINS         : [3 mots-clés depuis phase 2]
TOP 3 ANGLES EXCLUSIFS   : [3 angles depuis phase 3]
TOP 3 VERBATIMS CLIENT   : [3 mots-clés depuis phase 4]
MODÈLE pSEO PRIORITAIRE  : [Nom + ratio impact/effort depuis phase 5]
LIVRABLE                 : [Lien Google Sheet OU chemin .xlsx]
```

---

## Ce que l'agent NE DOIT PAS faire

- Lancer la phase 1 sans avoir validé le cadrage phase 0
- Inventer des chiffres de volume si Keyword Planner absent — laisser N/A
- Sauter la phase 4 (verbatims) : c'est ce qui différencie le livrable d'un export Ahrefs
- Sortir le livrable sans la synthèse 5 lignes
- Mettre dans le Sheet des mots-clés sans intention identifiée
- Faire les 4 WebSearch en parallèle : ils sont séquentiels par construction (chaque search dépend de la précédente)
- Recommander un modèle pSEO sans données propriétaires en phase 4

---

## Critère de qualité

Le livrable est bon si :

1. Chaque mot-clé du Sheet a une **intention identifiée** (colonne intérêt business notée)
2. Au moins **30% des mots-clés viennent des phases 3-4** (pas que Keyword Planner)
3. Le Sheet est **trié et filtré** sur les 5 colonnes scorées
4. La **synthèse 5 lignes** est livrée AVANT le lien
5. Au moins **1 modèle pSEO** est priorisé avec son ratio impact/effort
6. Le tag de provenance est présent pour chaque mot-clé (traçabilité)

---

## Temps total visé

- Phase 0 (cadrage) : 2 min — questions à l'utilisateur
- Phases 1+2 (lecture CSV) : 30 sec automatique
- Phase 3 (4 WebSearch) : 3-4 min automatique
- Phase 4 (verbatims) : 1 min si fichier, 5 min si Gmail/LinkedIn scan
- Phase 5 (pSEO) : 2 min via sous-skill
- Phase 6+7 (livrable + synthèse) : 1 min

**Total : 10 à 15 minutes** pour un workflow complet vs 2 à 3 sessions en mode manuel.

---

## Pages liées dans le wiki

Doctrine et fondations :
- [[wiki/syntheses/process-keyword-research-5-etapes]] — synthèse doctrinale du workflow (le présent skill en est l'orchestrateur outillé)
- [[wiki/concepts/mots-cles-actionnels]] — terme signature, définition de l'intention business ciblée
- [[wiki/concepts/methode-organikk-4-piliers]] — cadre doctrinal (Surprise / Grounding / pSEO / AEO)
- [[wiki/concepts/data-proprietaire]] — fondation de la phase 4 (verbatims)
- [[raw/notes/process-seo-b2b-2026]] — article pilier qui formalise la doctrine

Sous-skills appelés :
- [[raw/notes/skill-quick-win]] — phase 2 (GSC)
- [[raw/notes/skill-cannibalisation]] — phase 2 (si conflits détectés)
- [[raw/notes/skill-programmatique-pseo]] — phase 5

Outputs et données :
- [[raw/data/keyword-research-2026-05-02]] — exemple de scrape Google Suggest (étape 1 alternative au Keyword Planner)
- Output dossier wiki : `wiki/queries/kw-research-YYYY-MM-DD-slug.md`

## Sortie de pré-décision (obligatoire)

Ce skill est une étape du workflow mots-clés complet (`.seokb/base/wiki/methodes/workflow-mots-cles-complet.md`). Sa sortie porte un `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ) et nourrit le rapport de pré-décision, seule sortie visible du workflow ; toute sortie de ce skill qui contredit ce rapport devient OBSOLÈTE. Format complet : `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`.

Ce que le rapport de pré-décision rend, et que ce skill doit rendre possible sur son périmètre :

1. Diagnostic en trois lignes.
2. Pré-décision par marché (5 max) : Marché / Page / Score business sur 5 (intention 0-2, proximité offre 0-2, conversion directe 0-1) / Docs du vault (documents qui traitent le sujet, par type : transcripts, clients, notes, wiki) / Matière qualifiée (objection, cas, méthode, preuve, résultat, verbatim) / SERP (compatible, à vérifier, non vérifiée) / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. Ce qui est bloqué, et par quoi : statut, raison, actions autorisées, actions interdites ; « décision stratégique requise » quand c'est le positionnement (c'est la décision de Tim) ; « pré-décision impossible avant analyse SERP de N requêtes » sinon. Jamais « à trancher ».
4. À ne pas produire maintenant.
5. Fiabilité, une ligne ; analyse technique derrière ; logs du workflow en annexe.

Règles : signaux de demande séparés (Suggest, Search Console, calls, acteurs), jamais agrégés en verdict, aucun volume estimé ; matière comptée en documents du vault puis qualifiée par lecture, jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC, « chevauchement potentiel à vérifier » ; une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un cas ou un relevé réel par page programmatique ; scores /10 en backend ; Faible / Moyen / Élevé, jamais d'anglais ; la certitude affichée ne dépasse jamais la couverture des données.

