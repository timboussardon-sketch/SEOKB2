# Agent prospect

Agent piloté par objectif : on lui donne une cible (« 30 avocats en droit du travail à Lyon, côté employeurs, avec email prêt à relire ») et il travaille jusqu'à l'atteindre, ou s'arrête en disant pourquoi.

## Avant le premier envoi

L'agent écrit et envoie au nom de la personne configurée dans `.env.local`. Rien n'est écrit en dur dans le code.

- `SENDER_NAME` : nom de l'expéditeur. Obligatoire pour envoyer. Il signe les emails et la page de pré-audit.
- `SENDER_COMPANY` et `SENDER_URL` : facultatifs. L'URL sert aussi de contact dans le User-Agent du crawler.
- `MAIL_FROM` et `MAIL_REPLY_TO` : adresse d'envoi (domaine vérifié chez Resend) et adresse qui reçoit les réponses.
- `EMAIL_BANNER_FILE` : nom d'un PNG déposé dans `public/email/`, affiché sous l'email. Vide : pas de bandeau.

Un email approuvé part par Resend quand tu cliques sur « Envoyer » dans `/suivi`. La politique d'usage de Resend interdit la prospection à froid : le domaine d'envoi peut être suspendu. Le cadre légal de la prospection (RGPD, opposition, désinscription) reste de ta responsabilité.

## Lancer en local

```bash
npm install
npm run db:start        # PostgreSQL local dans .pgdata, port 5545
cp .env.example .env.local
npm run db:migrate
npm run build && npm start   # http://localhost:3457
npm run worker          # dans un second terminal : exécute les campagnes
npm test                # base agent_prospection_test
```

`npm start` n’écoute que sur 127.0.0.1 : le tableau de bord n’est ouvert que depuis cette machine. `DASHBOARD_PASSWORD` ajoute un mot de passe (Basic auth) si besoin.

`scripts/service.sh worker` et `scripts/service.sh web` lancent la base locale puis le worker ou le tableau de bord. Ils sont écrits pour être appelés par un gestionnaire de service (launchd sur macOS).

## Deux modes

- **Simulation** : cabinets, sites et réponses IA fictifs (domaine `.test`), aucun appel externe, coût nul. Sert à voir tout le parcours.
- **Réel** : API Claude (Messages API, outil `web_search`) pour la découverte, la mesure de présence et l'analyse. Exige `ANTHROPIC_API_KEY`. Modèle par défaut `claude-opus-5-5`. Sans clé, la campagne se bloque avec le motif.

La mesure automatique porte sur les réponses de Claude avec recherche web, ou sur celles d'un modèle d'OpenAI via Codex (`visibility_mode: OPENAI_CODEX_WEB_SEARCH`, compte ChatGPT connecté par `codex login`). Codex n'est pas l'interface ChatGPT : l'email écrit « un modèle d'OpenAI, l'éditeur de ChatGPT ». `scripts/claude-smoke.ts` vérifie l'intégration en trois appels, `scripts/run-campaign.ts` lance une campagne en ligne de commande.

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

- `src/core` : règles pures (états, erreurs, verdicts, mots-clés, contrôle factuel, SSRF, CSV, identité de l'expéditeur)
- `src/engine` : campagne, étapes, budget, revue, file pg-boss
- `src/providers` : simulation, OpenAI
- `src/prompts` : prompts versionnés
- `worker/` : worker séparé
- `app/` : tableau de bord Next.js
- `migrations/` : schéma PostgreSQL

## Non fait

- Webhooks Resend (le suivi relit l'API toutes les 10 minutes).
- Import CSV, Playwright pour les sites en JavaScript.
- Vérification d'une spécialisation certifiée : renvoyée en revue humaine.
- Purge et politique de conservation.
