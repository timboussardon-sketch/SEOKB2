---
name: seo-faq-query
description: "FAQ stratégique d'une page, 5 à 7 questions, balisage FAQPage. « fais la FAQ », « FAQ query »."
---

# Skill — FAQ Query

## Quand utiliser ce skill

Génère la FAQ stratégique d'une page, conçue comme un levier décisionnel et non comme du
remplissage. Reverse engineering sémantique, diversité RRF (Reciprocal Rank Fusion), objectif
Fully Meets : 5 à 7 questions maximum, chacune activant un vecteur sémantique unique, chaque
réponse citable isolément et destinée au balisage FAQPage. Verrouillage strict de la
perspective utilisateur (B2B ou B2C) et filtrage des questions qui n'aident pas à décider.
TOUJOURS utiliser ce skill quand l'utilisateur dit : "/seo-faq-query", "fais la FAQ", "FAQ query",
"ajoute une FAQ à cette page", "la FAQ de la page pilier", "questions FAQ RRF", "FAQPage
schema", ou quand une page publiée n'a pas encore sa FAQ. La FAQ est obligatoire sur toute
page publique : ne jamais en écrire une sans passer par ce skill.

## Contexte et rôle

Tu es expert SEO et ingénieur IA, spécialisé en reverse engineering sémantique, optimisation RRF
(Reciprocal Rank Fusion) et atteinte du score Fully Meets.

La FAQ d'une page pilier est un levier décisionnel. Elle couvre les micro-intentions latentes,
décisionnelles et transactionnelles, renforce la diversité RRF, et supprime le besoin d'une
requête secondaire critique. Une FAQ informative ou pédagogique est un échec.

## Entrées requises

| Entrée | Obligatoire | Exemple |
|---|---|---|
| Thème principal ou requête cible | Oui | « arrêter la cigarette mais pas le joint » |
| Perspective utilisateur : B2B ou B2C + rôle précis + contexte d'usage | Oui | B2C, fumeur qui consomme aussi du cannabis, cherche à arrêter le tabac seul |
| Objectif stratégique de la page | Oui | Lead gen / Conversion / Expertise Fully Meets |
| Corpus sourcé de la page | Oui sur un sujet à enjeu | fiches `raw/` déjà écrites |

Sans perspective utilisateur explicite, ne pas générer : la demander.

## Règles de filtrage, non négociables

Exclure toute question ou réponse qui :

- n'aide pas directement à une décision, une action ou une réduction de risque,
- ne contribue pas explicitement à l'atteinte du niveau Fully Meets,
- n'active pas un signal RRF distinct et mesurable.

### Verrouillage B2B / B2C

Exclure toute question ou réponse qui ne correspond pas strictement à la perspective définie.

- Perspective B2B : exclure le langage, les scénarios et la logique B2C (usage personnel,
  assurance individuelle, paiement particulier, confort domestique).
- Perspective B2C : exclure la logique B2B (retour sur investissement d'entreprise, process
  interne, contractualisation cadre, multi-sites, décision collective).

### Interdictions formelles

- Aucune redondance sémantique entre questions.
- Aucune question pédagogique ou générique.
- Aucune reformulation déguisée d'un même besoin.

En cas de conflit entre richesse sémantique et utilité business, privilégier toujours l'utilité
décisionnelle pour la perspective utilisateur.

## Tâche : déploiement RRF

Générer 5 à 7 questions maximum, destinées à un balisage `FAQPage`, avec une diversité sémantique
stricte. Chaque question active un vecteur sémantique unique du cluster.

Typologies à piocher selon la pertinence, jamais toutes systématiquement :

- **Transactionnelle** : coût, investissement, rentabilité.
- **Comparative ou décisionnelle** : choix de la solution adaptée au contexte utilisateur.
- **Implémentation** : process réel, point de friction opérationnel.
- **Risque ou conformité** : erreurs critiques, contraintes légales ou techniques.
- **Longue traîne experte** : spécificité élevée, E-E-A-T renforcé.
- **Définition avancée**, optionnelle, uniquement si une entité complexe bloque la décision.

## Exigences sur les réponses

Chaque réponse est :

- courte, précise, jamais générique,
- porteuse d'une information actionnable ou décisionnelle,
- construite pour lever explicitement une objection,
- rédigée avec un niveau d'autorité expert,
- citable isolément sans perte de contexte, prête pour une reprise en AI Overview.

## Format de sortie

Liste structurée, question par question. Pour chaque question, dans cet ordre :

1. la question,
2. la réponse,
3. une ligne distincte : **Vecteur sémantique couvert :** description concise du signal activé.

Aucun tableau. Aucun texte hors FAQ.

## Contrôles RRF avant livraison

- Aucun chevauchement sémantique entre deux questions.
- Un signal RRF distinct par question.
- La FAQ suffit à atteindre Fully Meets sans requête secondaire critique.

## Règles maison qui s'appliquent par-dessus

- **Une FAQ est toujours un accordéon, avec un signe plus à droite de chaque question.** Règle de
  design : six réponses dépliées alourdissent la page
  pour rien. La question seule est visible, le plus ouvre la réponse. À construire avec `details`
  et `summary` natifs plutôt qu'avec du JavaScript : la réponse reste présente dans le HTML livré,
  donc lisible par un moteur et reprise dans le balisage `FAQPage`.
- **Style de la FAQ = style de la FAQ de la home du site concerné.** Ouvrir la home, reprendre le
  composant existant tel quel, mêmes classes, même markup, même comportement. Jamais de variante
  locale. Si le site n'a pas encore de FAQ sur sa home, le signaler à l'utilisateur : la première FAQ créée
  devient la référence, ce n'est pas un choix à faire en passant.
- Ton de voix du site, jamais un ton générique : sur un site qui a déjà des articles, aller y
  chercher le registre, notamment le tutoiement ou le vouvoiement.
- Aucune tournure de rédaction automatique : pas d'antithèse « ce n'est pas X, c'est Y », pas de
  mise en scène (« il faut savoir que »), pas de suspense, pas de tiret cadratin.
- Sur un sujet à enjeu (santé, droit, argent), chaque chiffre d'une réponse vient d'une source
  vérifiée du corpus, jamais de la connaissance générale du modèle. Une question sans source
  disponible est écartée, pas comblée.
- Mots bannis : jamais « gains rapides », « territoire », « concurrent », « lien mort »,
  « Money Page », ni tiret cadratin.

## Enchaînement

En amont : `seo-clustering-mots-cles` pour connaître le cluster de la page, `seo-mots-cles-decisionnels`
pour repérer les intentions Do. En aval : `seo-donnees-structurees` pour le balisage `FAQPage`,
`seo-needs-met-rrf` pour l'évaluation du résultat.
