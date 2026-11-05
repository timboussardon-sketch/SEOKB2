# Comment je mesure si une IA cite un site : la méthode, les étapes, les prompts

_Timothée · 6 oct. 2026_

> **En résumé**
> - D'une réponse IA à la suivante, seules 30 % des marques restent présentes (AirOps). Une mesure isolée ne prouve rien : je prends 30 mesures par sujet.
> - J'ai supprimé le score sur 100. Il reste trois métriques : présence en source, nom cité dans le texte, évolution dans le temps.
> - Aucun LLM ne juge la mesure. Je lis les champs de citation renvoyés par les API, et une regex cherche le nom de la marque.

---

## Pourquoi mesurer

Une citation IA n'est jamais acquise. AirOps l'a chiffré : sur deux réponses posées à la suite, 30 % des marques restent présentes. Sur cinq requêtes d'affilée, 20 %. Semrush a vu Reddit passer d'environ 60 % à environ 10 % des citations ChatGPT entre août et mi-septembre 2025.

Sur Google, une URL a une position. Dans une réponse d'IA, une URL peut être citée 0, 1 ou N fois. Et être cité dans le premier paragraphe ou à la dernière ligne, ce n'est pas pareil. Il faut le mesurer.

## La réflexion

**J'ai supprimé le score sur 100.** Le premier plan en avait un, avec une pondération par position de citation (+100, +70, +40, +10). Il est arbitraire : le client demandera pourquoi il est passé de 61 à 57, et tu n'auras aucune réponse. Je garde trois métriques :

1. **Présence** : le domaine apparaît dans les sources citées de la réponse.
2. **Recommandation** : le nom de la marque est écrit dans le corps du texte.
3. **Évolution** : ces deux taux, relevé après relevé.

**Aucun LLM pour juger.** La recherche (Aggarwal, 2024) propose une « Subjective Impression » notée par GPT-4 sur sept critères. Coût : un appel LLM par évaluation. Les API renvoient déjà les citations dans des champs structurés (`url_citation` chez OpenAI, `groundingChunks` chez Gemini, `search_results` chez Perplexity, `web_search_result_location` chez Claude). Je compare les domaines.

**Les questions viennent de la Search Console.** Les requêtes déjà tapées par tes visiteurs, reformulées comme on les pose à une IA. Jamais un mot-clé brut.

**Calibration avant tout build.** Un script pose les questions aux API et extrait les citations. Rien ne se construit tant que la calibration ne passe pas. (Au 3 juillet, les gates n'étaient pas passés.)

## Deux outils, deux façons d'avoir 30 mesures

**geo-citations** : la même question, posée 30 fois, sur ChatGPT, Gemini et Perplexity. Coût d'un relevé : questions × moteurs × 30 appels.

**Le tracker de citations** : un mot-clé, 30 prompts différents, chacun posé une fois. Les prompts sont figés au premier relevé, sinon les relevés ne se comparent plus.

Le tracker vise ChatGPT. Sans clé OpenAI, il tourne aujourd'hui sur Claude : il mesure donc les citations de Claude. Premier relevé, sur « Quel est le meilleur outil de prise de notes avec IA en ce moment ? » : zéro citation, zéro source web.

(Le 1er août, j'avais aussi dessiné chaque relevé en bougie boursière, verte ou rouge. C'était creux : sans 30 runs par mot-clé, sur plusieurs moteurs et plusieurs semaines, il n'y a rien à lire.)

## Les étapes

1. Tirer les requêtes Search Console du site et les reformuler en questions posées à une IA.
2. Relire le jeu de questions à la main.
3. Configurer le site : domaine, variantes du nom de marque, questions, nombre de runs.
4. Annoncer le coût (questions × moteurs × runs) avant de lancer.
5. Lancer le relevé, recherche web activée, localisation France.
6. Calculer présence, rang de première citation, page citée, recommandation. Un fichier JSON par relevé, avec le texte complet de la réponse et la version du modèle.
7. Lister les domaines cités à la place du site.
8. Pour un sujet où le site est absent, lire les 2 ou 3 pages citées à sa place et en tirer une action par sujet.

## Les prompts

Le format d'une question suivie, sur Organikk :

```json
{
  "targets": ["organikk.co"],
  "nameVariants": ["Organikk"],
  "runs": 30,
  "questions": [
    "Quel consultant SEO recommandes-tu à Lyon ?",
    "Quel consultant SEO B2B recommandes-tu à Lyon ?"
  ]
}
```

Le prompt qui génère les 30 formulations d'un mot-clé, en un appel :

```
Tu écris des prompts que de vrais humains tapent dans un assistant IA.

Mot-clé : « {mot-clé} »

Écris exactement 30 prompts en français, formulés comme un humain qui parle
à un assistant IA (question ou demande naturelle, pas un mot-clé SEO brut).
Varie les intentions :
- des questions de recommandation directe (« quel est le meilleur… »,
  « que me conseilles-tu… »)
- des demandes de liste (« quels sont les outils/sites pour… »)
- des comparaisons (« X ou plutôt quoi ? », « quelle alternative à… »)
  sans citer le site cible
- des questions de débutant qui décrivent le besoin sans vocabulaire technique
- des questions avec un contexte précis (métier, contrainte, budget,
  France/Europe, RGPD si pertinent)
- quelques questions de confiance (« à qui se fier pour… »,
  « quel site est fiable pour… »)

Règles :
- 30 prompts, tous différents, une seule idée par prompt
- chaque prompt doit être une demande à laquelle l'assistant répond en citant
  des sites ou des noms d'outils/services
- ne jamais citer un site ou un nom de produit précis dans le prompt
- longueur naturelle : de 6 à 25 mots

Réponds uniquement en JSON : {"prompts": ["...", "..."]}
```

Sorties sur « outil prise de note IA » : « Je suis journaliste, quel service me transcrit mes interviews en français correctement ? », « Avocat, j'ai besoin de retranscrire des audiences : quelles solutions sérieuses existent ? ».

Ces 30 prompts ont été écrits par Claude Opus 5. Aucun n'est observé chez un vrai client. Relis-les avant le premier relevé : après, ils sont figés.

La détection de recommandation, une regex :

```js
const re = new RegExp(
  `(?<![\\p{L}\\p{N}])${variant}(?![\\p{L}\\p{N}])`, 'giu'
)
```

`\b` gère mal les caractères accentués, d'où les bornes `\p{L}\p{N}`.

## Le skill

Le skill Claude Code `geo-citations` pilote l'outil, avec quatre règles dures :

- jamais de relevé sans annoncer `questions × moteurs × runs = N appels` et attendre mon go ;
- minimum 30 runs pour tout résultat montré, sinon l'écrire : « ceci n'est pas un échantillon crédible » ;
- aucune question inventée : elles viennent de moi ou d'un export Search Console ;
- aucun relevé hebdo planifié sans mon accord.

---

→ *Tu veux le monter sur ton site ? Réponds à ce mail.*

**Sources :**
- AirOps, 2026 State of AI Search
- Semrush AI Visibility Index
- Aggarwal et al., GEO: Generative Engine Optimization, arXiv 2311.09735
