---
name: seo-base-publique
description: "Architecture de la base publique d'une marque : pages, FAQ, preuves, corroboration externe. « base publique »."
---

# Skill — Base Publique (corpus de confiance 3 niveaux + corroboration externe)

## Quand utiliser ce skill

Construit l'architecture de la « base publique » d'une marque : un corpus public en 3 niveaux (pages stratégiques, FAQ précises, preuves/sources) bâti sur les questions de confiance propres à son secteur — pas seulement RGPD/sécurité, mais méthode, résultats, certifications, authenticité selon le vertical — avec maillage hub-satellite, graphe d'entités marque, et plan de corroboration externe (le point non négociable : une affirmation de la marque sur elle-même ne suffit jamais, il faut des sources tierces indépendantes qui la répètent).

TOUJOURS utiliser ce skill quand l'utilisateur dit : "base publique", "construis la base publique de [site]", "architecture de confiance", "corpus de preuves du site", "quelles pages de preuve créer", "notre empreinte publique", "corroboration externe", "graphe d'entités de la marque", "quelles sont nos questions de confiance", ou demande de faire pour un site ce qui a été fait pour le client SaaS (RGPD/AI Notetaker) mais sur un autre vertical.

## Quand déclencher

Construire l'architecture complète de la **base publique** d'une marque : le corpus public, structuré et crawlable de réponses fiables sur ses questions de confiance sectorielles, pensé pour être découvert et cité par les moteurs de recherche ET les systèmes de recherche IA (AI Overview, ChatGPT, Perplexity, Gemini).

Diffère des skills qui traitent une seule brique :
- `seo-cluster-aeo` construit un cluster Know-Simple/Know/Do autour d'**un** mot-clé pilier ;
- `seo-modeles-pseo` cadre les Spokes **décisionnels** (conversion) autour d'une Money Page ;
- `seo-entites-vectorielles` cartographie les entités d'**une** page ;
- `seo-faq-query` rédige la FAQ stratégique d'**une** page (5-7 questions) ;
- `maillage-systeme` formalise le maillage interne d'un site déjà cadré.

Ici on cadre **l'architecture entière au niveau de la marque** : quelles questions de confiance couvrir, sur combien de niveaux, avec quelles preuves, et surtout — brique absente des autres skills — comment obtenir la **corroboration par des sources tierces indépendantes**. Ce skill livre l'architecture ; il invoque les autres skills pour exécuter chaque brique.

Doctrine complète : `.seokb/base/wiki/methodes/base-publique.md`.

## Doctrine (à ne jamais violer)

- **Une affirmation de la marque sur elle-même ne suffit jamais.** Toute association « marque = critère de confiance » n'a de valeur pour la recherche IA que si des sources tierces indépendantes la répètent. Le plan de corroboration externe est une sortie obligatoire du skill, pas une option.
- **Les questions de confiance sont sectorielles, jamais génériques.** Ne pas plaquer un référentiel RGPD/sécurité sur un site qui n'en a pas besoin. Identifier les questions réelles qu'un acheteur du secteur se pose avant de choisir.
- **Trois fonctions de page à ne jamais fusionner** : page SEO (attire la recherche), page de preuve (apporte la preuve vérifiable), page produit (explique la solution). Une page qui mélange les trois dilue chacune.
- **Niveau 2 nourrit niveau 1, niveau 3 crédibilise les deux.** Ne jamais publier une page de niveau 1 sans que ses preuves de niveau 3 existent ou soient identifiées comme à produire.
- **Aucune preuve, certification ou mention externe inventée.** Si une preuve n'existe pas encore, elle est marquée `[À PRODUIRE]` ou `[À VÉRIFIER AVEC LE CLIENT]` — jamais affirmée comme acquise.
- **Comparatifs strictement factuels et mesurés** — jamais accusateurs, jamais d'exagération sur un concurrent. Voir skill `comparatif-neutre`.
- **Fraîcheur = signal de confiance** sur les sujets qui évoluent (réglementation, IA, méthode, prix, certifications) : chaque page de niveau 1 ou 3 porte une date de mise à jour.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Le site / la marque à traiter | Oui |
| Le secteur et l'audience (B2B/B2C, décideur type) | Oui |
| Ce qui existe déjà (pages sécurité/conformité/à propos, certifications, contrats types) | Recommandé |
| Concurrents directs (pour les comparatifs) | Recommandé |
| Relations externes existantes (médias, partenaires, clients prêts à témoigner) | Recommandé — sinon le plan de corroboration part de zéro |

Si l'un des inputs recommandés manque, continuer mais le signaler explicitement dans le livrable plutôt que de combler par supposition.

## Pipeline (5 étapes)

### 1. Cadrer la marque et ses questions de confiance sectorielles

Ne pas partir d'un référentiel type (RGPD) par défaut. Se demander : *qu'est-ce qu'un acheteur de ce secteur vérifie avant de choisir, au-delà de ce que la marque affirme d'elle-même ?* Lister 3 à 6 questions de confiance (ex. conformité réglementaire, hébergement/sécurité, méthode et résultats mesurés, certification, authenticité/provenance, garanties). Vérifier ce qui existe déjà sur le site pour ne pas dupliquer une page qui répond déjà à la question.

### 2. Niveau 1 — pages stratégiques (cible : 10)

Croiser produit × question de confiance pour générer les grandes requêtes qu'un décideur taperait (« meilleur [catégorie] + [critère de confiance] », « [marque] est-il/elle [critère] »). Chaque page de niveau 1 doit avoir un point de conversion ou un maillage clair vers une page produit.

### 3. Niveau 2 — FAQ précises (cible : 50 à 100 questions)

Commencer par compter ce qui existe déjà (FAQ publiées, FAQ des pages, glossaire). Quand un corpus existe, le livrable est une carte par sous-thème (questions écrites / manques / statut preuve) qui montre les trous de répartition, pas une liste de 100 questions neuves. Sur le client SaaS (2026-09-02), 91 questions existaient déjà et le vrai manque était zéro question sur « ai-je le droit d'enregistrer » et zéro sur la fiabilité.

Décliner chaque question de confiance du niveau 1 en sous-questions tapables et isolément citables — jamais des labels de catégorie (« RGPD ») mais des questions complètes (« [marque] transfère-t-elle des données hors de l'UE ? »). Regrouper par sous-thème. Chaque question = une réponse courte et vérifiable, destinée à nourrir une page ou une entrée FAQ balisée (voir `seo-faq-query` pour la FAQ d'une page donnée).

### 4. Niveau 3 — preuves et sources

Pour chaque question de confiance : lister les preuves qui existent déjà (contrat, certification, page technique, politique publiée) et celles qui manquent, marquées `[À PRODUIRE]`. Identifier les comparatifs factuels possibles avec des concurrents réels. Ne jamais avancer une preuve non vérifiée.

### 5. Maillage, graphe d'entités, plan de corroboration externe, cadence

- **Maillage hub-satellite** : chaque page de niveau 3 pointe vers sa page de niveau 1, et réciproquement (déléguer le détail à `maillage-systeme` si besoin).
- **Graphe d'entités marque** : formuler les relations `Marque → est/cible/traite/conformité/hébergement/certification/intègre → [valeur]` de façon cohérente sur tout le site (déléguer le détail par page à `seo-entites-vectorielles`).
- **Relevé de ce que les tiers disent déjà** (obligatoire avant le plan) : chercher la marque sur Capterra, G2, Trustpilot, Zapier et les marketplaces des partenaires, les annuaires d'alternatives (ex. extrag.one), les pages des autres éditeurs qui la citent. Noter pour chacun le fait exact affirmé (pays de l'éditeur, hébergement, certification). C'est là que les contradictions apparaissent, et elles renvoient presque toujours à une contradiction sur le site lui-même (le client SaaS : « Belgique/Europe » sur les comparatifs, « franco-belge, France » sur la FAQ). Une fiche qui n'est pas trouvée est marquée « absence de résultat, pas preuve d'absence ».
- **Plan de corroboration externe** : lister les canaux réalistes (médias du secteur, comparateurs existants, partenaires d'intégration, clients à solliciter pour témoignage, podcasts) et l'association précise à faire confirmer par chacun. Ce n'est pas une liste de backlinks à acheter — c'est une liste de faits vérifiables à faire répéter par des tiers indépendants.
- **Cadence de fraîcheur** : pour chaque page de niveau 1/3, proposer une fréquence de revue (ex. semestrielle pour la réglementation, à chaque évolution produit pour l'IA/l'hébergement).

## Output obligatoire

```
BASE PUBLIQUE — [Marque]
Secteur : [secteur] · Audience : [B2B/B2C, persona décideur]
Questions de confiance identifiées : [liste 3-6]

NIVEAU 1 — Pages stratégiques (10)
| # | Requête stratégique | Question de confiance | Existe déjà ? | Page de preuve associée (niveau 3) |
|---|---|---|---|---|

NIVEAU 2 — FAQ précises (par sous-thème)
| Sous-thème | Question | Réponse courte vérifiable | Statut preuve |
|---|---|---|---|

NIVEAU 3 — Preuves et sources
| Preuve | Question de confiance couverte | Existe / À produire | Source vérifiable |
|---|---|---|---|

MAILLAGE
[Schéma hub → satellites, niveau 1 ↔ niveau 3]

GRAPHE D'ENTITÉS
Marque → est → [...] ; → cible → [...] ; → conformité → [...] ; → hébergement → [...] ; → certification → [...] ; → intègre → [...]

PLAN DE CORROBORATION EXTERNE
| Canal | Association à faire confirmer | Statut (relation existante / à établir) |
|---|---|---|

CADENCE DE FRAÎCHEUR
| Page | Fréquence de revue | Déclencheur de mise à jour |
|---|---|---|
```

## Retex de la première application (client SaaS B2B, 2026-09-02)

- Le niveau 3 (preuves) est celui qui manque en pratique, même sur un site qui a déjà une FAQ conformité et des comparatifs. Chaque page affirme, aucune ne prouve. Le tableau du niveau 3 est le livrable le plus utile pour le client.
- Pour une certification, la corroboration la plus forte est le registre public de l'organisme certificateur. Demander le nom de l'organisme en premier.
- Le graphe d'entités se remplit en trois colonnes : ce que dit le site, ce que disent les tiers, la formulation unique à porter partout. Les décisions de formulation (pays de l'éditeur, hébergeur) sont des décisions client, à isoler dans une liste « ce qui attend le client ».
- Ajouter une question de confiance de fiabilité produit (l'outil tient-il ses promesses) quand les tickets la placent parmi les freins : elle n'a en général aucune page.

## Règles anti-hallucination (absolues)

- Aucune certification, contrat, mention presse ou témoignage client inventé — placeholder `[À PRODUIRE]` ou `[À VÉRIFIER AVEC LE CLIENT]`.
- Aucun volume de recherche inventé sur les requêtes de niveau 1 — le décisionnel se lit dans la formulation, pas dans un chiffre supposé.
- Aucune affirmation comparative non vérifiée sur un concurrent nommé.
- Si une question de confiance sectorielle est incertaine, la signaler à Tim plutôt que de la deviner à partir d'un seul cas sectoriel (ex. RGPD).

## Enchaînement workflow

En amont : `audit-pre-call` ou `seo-pre-audit` (état SEO du prospect/client, peut révéler les questions de confiance non couvertes). En aval : `seo-entites-vectorielles` (détailler le graphe d'entités par page), `seo-faq-query` (rédiger la FAQ isolée de chaque page de niveau 1), `maillage-systeme` (formaliser le maillage complet), `comparatif-neutre` (rédiger les comparatifs de niveau 1/3), `seo-brief-contenu` (brief éditorial de chaque page stratégique).

## Sauvegarde

Si le site est suivi dans ton coffre, output dans `wiki/queries/base-publique-YYYY-MM-DD-slug.md` et mise à jour de `wiki/index.md` + `wiki/log.md` selon §6/§7 d'AGENTS.md. Pour un client hors seo-kb (vault dédié), suivre la convention de ce vault.

## Concepts liés

`base-publique` · `e-e-a-t` · `maillage-systeme` · `entites-vectorielles` · `grounding-score` · `weight-decay` · `know-simple-know-do`
