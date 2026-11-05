# Scan ArXiv SEO/GEO — 2026-09-25

*Scan hebdomadaire de la littérature arXiv pertinente SEO/GEO/AEO. Collecte déterministe (API arXiv, script `arxiv-fetch.py`) + scoring /50 par candidat. Aucun envoi, sous-doc de brèves (`breves-IA/scan-arxiv/`).*

## Verdict de la semaine

Premier run du pipeline scoré — fenêtre élargie à 30 jours pour rattraper le retard depuis les 2 éditions manuelles d'avril (jamais automatisées). 21 candidats examinés, 6 au-dessus du seuil de rétention (30/50), 1 sous le seuil malgré un sujet dans le périmètre (Agent2UCB, 27/50). Deux axes dominent : l'ingénierie défensive/offensive du GEO (3 benchmarks d'attaque/défense publiés en moins de 3 semaines, un seul retenu pour éviter le doublon) et la dégradation structurelle d'un signal de ranking sur-optimisé (CHASE, qui prolonge Retrieval Collapse). Prochaine édition en fenêtre 8 jours.

## Études retenues

### 1. ChatGPT recommande "au choix unique" dans 79 % des réponses — et les sources changent à chaque requête — `Score : 40/50`

**Source** : https://arxiv.org/abs/2609.18729
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Les moteurs conversationnels n'ont pas une réponse stable sur les recommandations produit — la même question posée deux fois change de marque citée et de sources affichées.

Audit de 1 536 réponses à 2 528 requêtes commerciales réelles (jeu ConsumerQ) sur ChatGPT (interface + API), Gemini (interface + API), Google AI Overviews. ChatGPT exprime une préférence produit à la première personne dans 79 % de ses réponses, contre 7 % pour Gemini et 2 % pour AI Overviews. Les produits recommandés varient d'une requête à l'autre. Les domaines de sources affichés se recoupent à seulement 5,4 % entre ChatGPT et Gemini pour une même requête (0 domaine commun dans 76,7 % des comparaisons). Les API affichent des sources différentes de leurs interfaces grand public.

**Lien avec la doctrine du vault** : nuance méthodologique directe pour `[[concepts/metriques-visibilite-geo]]` — un audit GEO fait sur une seule interface ou une seule API ne représente pas ce que voit réellement un consommateur.

---

### 2. La langue de la requête décide quelle marque locale apparaît — pas la position IP — `Score : 38/50`

**Source** : https://arxiv.org/abs/2608.30052
**Signal** : 🟢 Opportunité
**Impact business en 1 ligne** : Pour apparaître dans les recommandations d'un moteur génératif sur un marché local, la langue de la requête pèse davantage que la position géographique de l'utilisateur.

Sonde contrôlée de 234 exécutions sur ChatGPT web (déconnecté) + API, 4 pays de sortie × 6 langues de requête, 6 runs identiques par cellule (29-30 août 2026). La recommandation en tête est instable (change sur 4/6 prompts). C'est la langue de la requête, pas la localisation, qui décide si des fournisseurs locaux apparaissent : 0 marque locale sur 6 runs en anglais en Estonie et en Turquie, contre une présence quasi systématique en langue locale. Langue et localisation agissent séparément (turc depuis Berlin, russe depuis Tallinn : les fournisseurs du pays associé à la langue apparaissent, pas ceux du pays de connexion).

**Lien avec la doctrine du vault** : donnée actionnable directe pour la base de clients francophones — le contenu en français reste le levier de visibilité locale en GEO, pas l'infrastructure de géolocalisation. Cohérent avec `[[concepts/seo-multi-plateforme]]`.

---

### 3. Le SEO optimisé en boucle homogénéise le contenu et le déconnecte de sa qualité réelle — `Score : 37/50`

**Source** : https://arxiv.org/abs/2608.30466
**Signal** : 🔴 Menace
**Impact business en 1 ligne** : Plus un écosystème de contenu s'optimise pour un même signal de ranking IA, moins ce ranking reflète la qualité réelle.

CHASE simule 20 tours d'optimisation répétée de documents contre un signal de ranking LLM, sur 6 domaines (ranking validé comme proxy de visibilité réelle, AUC rang-citation 0,853 ± 0,093). L'alignement qualité-ranking se dégrade dans les 6 domaines entre R0 et R20 (Spearman rho : -0,018 à -0,107, moyenne -0,068). Les documents les plus proches du profil recherché par le signal deviennent, au fil des rounds, de moins en moins alignés avec un jugement de qualité indépendant.

**Lien avec la doctrine du vault** : prolonge directement `[[concepts/retrieval-collapse]]` (NAVER, scan avril) — ici la dégradation vient de l'optimisation elle-même plutôt que de la pollution externe du pool de documents. Renforce `[[concepts/data-proprietaire]]`.

---

### 4. Défendre un moteur génératif contre le GEO malveillant : le taux de succès d'attaque tombe de 50 % à 6 % — `Score : 32/50`

**Source** : https://arxiv.org/abs/2609.02964
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Les moteurs génératifs commencent à se doter de défenses efficaces contre le GEO manipulateur.

GEO Defender combine un reranker défensif (résidu préférentiel appris sur un reranker gelé) et une bibliothèque d'expérience générée sans fine-tuning du LLM cible. Testé sur 2 LLM propriétaires + 3 open source, contre 7 attaques GEO : taux de succès moyen des attaques 50,32 % → 6,20 %, 94,12 % de l'usage des preuves légitimes préservé.

**Lien avec la doctrine du vault** : deux papers concurrents publiés la même quinzaine (Counter-GEO-Bench, HAE-GEO) confirment que la manipulation par réécriture GEO devient un axe de recherche pris au sérieux côté moteurs. Argument de plus pour `[[concepts/e-e-a-t]]` contre le GEO en boîte noire pur.

---

### 5. Les "scores de visibilité GEO" vendus par les outils sont méthodologiquement fragiles — `Score : 32/50`

**Source** : https://arxiv.org/abs/2609.06811
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Un score de visibilité GEO dépend entièrement du corpus de prompts et des poids choisis par qui le construit.

Revue critique du cadre méthodologique des scores de visibilité GEO. Le corpus de prompts choisi sélectionne les situations évaluées, les poids déterminent leur importance relative — ensemble ils définissent un "marché de réponses" qui ne représente pas nécessairement la demande réelle. Une citation seule n'établit pas la contribution d'une source. Cadre théorique, pas de nouvelle expérience.

**Lien avec la doctrine du vault** : munition directe en prospection quand un prospect arrive avec un score d'un outil concurrent. Complète `[[concepts/metriques-visibilite-geo]]`.

---

### 6. La stratégie GEO optimale change dès que les concurrents optimisent aussi — `Score : 31/50`

**Source** : https://arxiv.org/abs/2608.27631
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Une stratégie GEO efficace aujourd'hui perd de son efficacité mécaniquement quand les concurrents l'adoptent aussi.

Formalise le choix de stratégie de réécriture GEO comme un problème combinatoire sensible à la concurrence. Pipeline en deux phases (recherche bayésienne combinatoire puis fine-tuning sur les traces de raisonnement). État de l'art sur geo-bench et un jeu concurrentiel augmenté, transfert hors-distribution.

**Lien avec la doctrine du vault** : argument pour vendre l'accompagnement GEO en continu plutôt qu'un audit figé.

---

## Écartés

Sous le seuil malgré un sujet dans le périmètre :
- 2608.29063 — Agent2UCB, agent GEO avec garde-fou SEO E-E-A-T (score 27/50 — papier démo, pas de venue, GEO-Bench synthétique, peu de nouveauté vs AgenticGEO déjà couvert en avril)

Hors périmètre ou redondants (pas scorés en détail) :
- 2609.24407 — audit Baidu/Google AI Search (focus Chine, moins prioritaire base clients FR/EU)
- 2609.23354 — framework de construction de contexte pour AI Search (interne moteur, peu actionnable praticien)
- 2609.11915 — Generative Marketing Mix Modeling (outil de mesure marketing interne firme)
- 2609.11998 — cache constant Block Diffusion (architecture ML générique, hors-scope)
- 2609.08071 — politique d'inventaire par LLM (supply chain, hors-scope)
- 2609.07559 — validation d'un score de contenu déterministe (dense méthodo, pas de finding GEO actionnable en 1 lecture abstract)
- 2609.07341 — réseaux de neurones associatifs non réciproques (hors-scope total)
- 2609.06798 — AI Overviews santé Baidu/Google (niche santé)
- 2609.06027 — HAE-GEO, benchmark poisoning agents (redondant avec GEO Defender, thème attaque/défense)
- 2609.02316 — Counter-GEO-Bench (redondant avec GEO Defender)
- 2609.00813 — recherche budget-aware par RL (générique, hors-scope)
- 2609.00319 — citations IA santé mentale (niche santé)
- 2608.30023 — PersonaGen-1M, corpus de personas acheteurs (dataset recherche, pas actionnable direct)
- 2609.01645 — écart de vocabulaire dans les systèmes de retrieval public (équité sociale, hors-scope SEO)

## Candidats à ingestion complète

Les 6 études retenues cette semaine ont déjà été traitées en ingestion complète le jour même (`raw/papers/scan-arxiv-2026-09-25.md` + `wiki/sources/2026-09-25-scan-arxiv-25-septembre.md`), avant la mise en place du sous-doc scoré — pas d'action supplémentaire nécessaire. À partir de la prochaine édition, ingestion complète seulement sur demande de Tim (cf. skill).

## Candidat INFO DU JOUR newsletter Algorithme

Oui — CHASE (2608.30466). Angle possible : "Optimiser pour le même signal que tout le monde finit par casser ce signal." Second choix : la langue de la requête (2608.30052), plus surprenant et actionnable pour les clients francophones.
