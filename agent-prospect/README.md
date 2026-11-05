# Agent prospect (agent avocats)

Copie du code au 2026-10-02 du dépôt `~/Code/prospection`. La copie de travail, avec sa base PostgreSQL et son `.env.local`, reste dans `~/Code/prospection/agent-avocats/`. Page wiki : [[agents/agent-avocats]].

Agent piloté par objectif : on lui donne une cible (« 30 avocats en droit du travail à Lyon, côté employeurs, avec email prêt à relire ») et il travaille jusqu'à l'atteindre, ou s'arrête en disant pourquoi.

Aucun email n'est envoyé par cette version. Elle s'arrête aux brouillons relus et approuvés.

## Lancer en local

```bash
npm install
npm run db:start        # PostgreSQL local dans .pgdata, port 5544
cp .env.example .env.local
npm run db:migrate
npm run build && npm start   # http://localhost:3456
npm run worker          # dans un second terminal : exécute les campagnes
npm test                # 67 tests, base agent_avocats_test
```

En production (`npm start`), le tableau de bord exige `DASHBOARD_PASSWORD` (Basic auth, identifiant libre).

## Deux modes

- **Simulation** : cabinets, sites et réponses IA fictifs (domaine `.test`), aucun appel externe, coût nul. Sert à voir tout le parcours.
- **Réel** : API Claude (Messages API, outil `web_search`) pour la découverte, la mesure de présence et l'analyse. Exige `ANTHROPIC_API_KEY`. Modèle par défaut `claude-opus-5-5`. Sans clé, la campagne se bloque avec le motif.

La mesure automatique porte sur les réponses de Claude avec recherche web, ou sur celles d'un modèle d'OpenAI via Codex (`visibility_mode: OPENAI_CODEX_WEB_SEARCH`, compte ChatGPT connecté par `codex login`, aucun coût à l'appel). Codex n'est pas l'interface ChatGPT : l'email écrit « un modèle d'OpenAI, l'éditeur de ChatGPT ». Pour ChatGPT, les réponses se relèvent à la main : page « Saisir des réponses de ChatGPT » d'une campagne (5 questions, 1 à 3 passages). L'email ne nomme ChatGPT que dans ce cas.

Premier essai réel le 2026-10-01 (droit du travail, Lyon, cible 2) : 5 cabinets trouvés, 1 prêt à relire, 4 en revue, 4,23 $ engagés dont 2,71 $ pour les 15 réponses de mesure. `scripts/claude-smoke.ts` vérifie l'intégration en trois appels, `scripts/run-campaign.ts` lance une campagne en ligne de commande.

## Boucles

| Boucle | Sortie | Limite |
|---|---|---|
| Campagne | objectif atteint, sinon découverte relancée | tours, résultats, tours vides, budget |
| Découverte | candidats dédupliqués par domaine | `max_discovery_rounds`, `max_candidates_per_round` |
| Qualification | QUALIFIED, REJECTED (motif typé), revue | extraits revérifiés dans la page |
| Enrichissement | adresse publiée ou NO_PUBLIC_EMAIL | 10 pages par site |
| Présence IA | 15 réponses valides ou INCONCLUSIVE | 2 relances par créneau |
| Pré-audit | constats CONFIRMED / HYPOTHESIS / INSUFFICIENT_DATA | pages lues seulement |
| Mots-clés | 20 au plus, jamais complétés | 2 tours |
| Email | brouillon + contrôle factuel phrase par phrase | 2 réécritures, puis revue humaine |

## Arborescence

- `src/core` : règles pures (états, erreurs, verdicts, mots-clés, contrôle factuel, SSRF, CSV)
- `src/engine` : campagne, étapes, budget, revue, file pg-boss
- `src/providers` : simulation, OpenAI
- `src/prompts` : prompts versionnés
- `worker/` : worker séparé
- `app/` : tableau de bord Next.js
- `migrations/` : schéma PostgreSQL

## Non fait

- Envoi (Resend, webhooks, outbox) : absent. Tout contact reste `PROVIDER_BLOCKED`.
- Import CSV, Playwright pour les sites en JavaScript.
- Vérification d'une spécialisation certifiée : renvoyée en revue humaine.
- Purge et politique de conservation.
