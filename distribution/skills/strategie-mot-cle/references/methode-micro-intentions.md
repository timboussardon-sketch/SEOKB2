# Méthode micro-intentions

Méthode chargée à l'étape 1 de `strategie-mot-cle` par `scripts/workflow.py load-method --phase 1`.
Les variables entre `${…}` sont les entrées de la méthode : le mot-clé pivot, son contexte, la zone visée et le nombre de requêtes par liste.

## Usage

Méthode micro-intentions.

Appelle generate_micro_intentions(topic, context) sur le ou les mots-clés principaux. Tu reçois un tableau [{query, cat, want}] : les déclinaisons d'intention réellement tapées, classées en Know-Simple, Know ou Do, pour viser le Fully Meets des Quality Raters.

Rends une phrase d'intro courte, puis TOUS les éléments reçus dans un bloc de code de langage micro : tableau JSON [{query, cat, want}], recopié fidèlement, sans rien inventer ni retirer. C'est ce bloc qui alimente l'onglet Micro-intentions, un tableau markdown ne l'alimente pas. Termine par le bloc suggestions.

Pour aller plus loin sur une requête à enjeu, charge `needs_met_rrf` : il cartographie les intentions latentes et dit ce qui manque pour passer de Highly Meets à Fully Meets.

## Prompt de génération

```
# ROLE
Tu es un expert en semantique vectorielle ET en intention marketing.
Ta mission n'est PAS de generer des requetes thematiques generiques.
Ta mission est de detecter des MICRO-INTENTIONS BUSINESS : des requetes
formulees par des humains a un moment precis du parcours d'achat, avec
un signal transactionnel implicite exploitable commercialement.

# INPUT
- Mot-cle pivot : "${keyword}"
- Contexte : ${context ? `"${context}"` : "aucun"}
${geoContext}

# DEFINITION : MICRO-INTENTION BUSINESS
Une micro-intention business, c'est une requete qui :
1. Revele une etape precise du funnel (decouverte / comparaison / decision / post-achat)
2. Contient un signal monetisable (prix, devis, alternative, ROI, delai, garantie, objection)
3. Peut etre tracee a un persona ou un contexte declencheur (profil, situation de vie, urgence, budget, deadline)
4. Est formulee en langage naturel reel (style Google Suggest / People Also Ask / forums / Reddit), pas en requete keywordee artificielle

# REGLE N°1 — ANTI-HALLUCINATION
N'invente jamais de volume de recherche ni de difficulte. Ces metriques viennent
d'un outil (GSC, Ahrefs, Semrush, Keyword Planner). Si une metrique chiffree non
sourcable est necessaire, ecris [À SOURCER]. Tu structures et qualifies l'intention,
tu n'estimes aucun chiffre de trafic ni de concurrence.

# REGLES DE GENERATION
- Syntaxe utilisateur reelle : contractions, fautes frequentes tolerees, questions completes, "comment", "pourquoi", "meilleur", "vs", "sans", "pas cher", "pour [persona]"
- Leviers d'expansion semantique a exploiter : modificateurs (comment, pourquoi, prix, avis, meilleur, vs, sans), questions type People Also Ask, longue traine de 3 mots et plus, co-occurrences et entites liees, synonymes et variantes lexicales
- Zero repetition lexicale entre requetes (varie les tournures, synonymes, angles)
- Maximum 1 variable modifiee par requete (sinon on perd la traction vectorielle)
- Annees 2026+ uniquement si le sujet l'exige (tendance, conformite, techno recente)
- Pas de mots-cles "seo-oses" (ex: "best top 10 guide ultime 2026") — on cherche la voix de l'utilisateur, pas celle du SEO
- Chaque requete doit revealer une ACTION BUSINESS possible (page dediee, lead magnet, outil, article, comparatif, calculateur)
- Methode : generer large puis filtrer le bruit — produis large, puis retire avant de livrer ce qui est hors-sujet, hors-intention par rapport au mot-cle pivot, et les doublons

# TAXONOMIE (Know-Simple / Know / Do)
Genere EXACTEMENT 3 listes de ${queriesPerList} requetes chacune :

## 1. KNOW-SIMPLE — Requete factuelle simple (brique AEO)
Definition : requete factuelle simple, reponse courte et directe (definition, date, chiffre).
Signaux : "qu'est-ce que", "definition de", "c'est quoi", "combien", "quand", "qui",
chiffre ou fait unique attendu, reponse en une phrase.
→ Ces requetes atterrissent sur une reponse atomique, un snippet, une FAQ courte.

## 2. KNOW — Requete de comprehension et d'evaluation
Definition : requete de comprehension, d'approfondissement, de comparaison ou d'evaluation avant decision.
Signaux : fonctionnement, regles, chiffres, etudes, methodologie,
comparatif objectif, limites, "pourquoi", "comment ca marche", "difference entre"
→ Ces requetes atterrissent sur un article de fond, un guide, une FAQ experte, un comparatif.

## 3. DO — Requete d'action ou de transaction
Definition : requete d'action ou de transaction (acheter, s'inscrire, telecharger, utiliser un outil, obtenir un devis).
Signaux : achat, devis, demo, essai, inscription, commande, abonnement,
remplacement, migration, tarif, prix, "comment acheter", "ou trouver"
→ Ces requetes atterrissent sur une landing, un pricing, un formulaire, un outil.

# FORMAT DE SORTIE (JSON strict, aucun texte hors JSON)

ACCENTS FRANÇAIS OBLIGATOIRES : tout texte français doit conserver ses accents (é è ê à â ù û ç î ï ô). Jamais "evaluer" mais "évaluer", jamais "selectionner" mais "sélectionner", jamais "referencement" mais "référencement", etc.

[
  {
    "query": "string — la requete telle qu'un humain la tape",
    "list_category": "Know-Simple | Know | Do",
    "funnel_stage": "Know-Simple | Know | Do",
    "persona_hint": "string — persona ou contexte declencheur infere",
    "business_signal": "string — le signal monetisable present (ex: 'comparaison', 'sensibilite prix', 'objection engagement', 'recherche ROI', 'remplacement')",
    "pain_point": "string — la friction ou l'objection sous-jacente (ou 'aucune')",
    "key_vector": "string — 2-3 termes qui ancrent la requete dans son champ semantique",
    "cosine_similarity_to_pivot": 0.0,
    "vector_distance": "Proche | Moyen | Loin",
    "intention_score": "0-100 — probabilite que la requete debouche sur une action business",
    "content_format_suggere": "landing | pricing | comparatif | calculateur | article-expert | cas-client | FAQ | outil-gratuit | lead-magnet",
    "monetization_angle": "string — comment cette requete peut etre monetisee concretement (1 phrase)"
  }
]

# QUALITE
Avant de rendre le JSON, verifie mentalement :
- Les ${totalQueries} requetes sont-elles vraiment distinctes (pas 10 reformulations du meme truc) ?
- Au moins 5 requetes contiennent-elles une objection ou un pain point explicite ?
- Au moins 5 requetes nomment-elles un persona ou un contexte precis ?
- Au moins 3 requetes comparent-elles a un concurrent, alternative ou statu quo ?
- Ne score que ce qui est reellement estimable a partir des signaux de la requete (presence d'un signal transactionnel, etape de funnel). Ne force jamais des ecarts de score artificiels pour "varier" : si le potentiel d'action business n'est pas estimable, mets [À SOURCER] plutot qu'un chiffre invente. Deux requetes au signal equivalent peuvent legitimement avoir le meme score.

Si non, regenere la liste concernee.

CONTRAINTE TEMPORELLE : Si tu dois mentionner une année, utilise toujours 2026 ou ultérieur. Ne jamais référencer 2025, 2024 ou années antérieures. Cependant, n'inclus des années que si elles sont vraiment nécessaires au contexte.

Rends uniquement le JSON final, sans commentaire.
```
