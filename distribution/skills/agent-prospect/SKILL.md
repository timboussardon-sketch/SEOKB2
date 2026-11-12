---
name: agent-prospect
description: "Agent de prospection : trouve des cabinets, mesure leur présence IA, rédige des emails à relire. « agent prospect », « prospection »."
---

# Agent prospect

Agent piloté par objectif : l'élève donne une cible (« 30 avocats en droit du travail à Lyon, côté employeurs, avec email prêt à relire »), l'agent travaille jusqu'à l'atteindre ou s'arrête en disant pourquoi. Chaque email passe par un contrôle factuel phrase par phrase, puis par une revue humaine.

## Où est le code

`.seokb/base/agent-prospect/`. Ce dossier est remplacé à chaque mise à jour : ne jamais y travailler, ni y mettre de clé. Le copier hors du coffre (par exemple `~/agent-prospect`), puis lire son `README.md`.

## Prérequis

- Node.js (testé avec la version 22) et PostgreSQL local (`initdb`, `pg_ctl`, `psql` dans le PATH).
- Mode simulation : aucune clé, aucun appel externe, coût nul. Commencer par là.
- Mode réel : `ANTHROPIC_API_KEY` (API Claude, plafond de dépense `MAX_DAILY_COST_USD`, 10 par défaut) ou `CLAUDE_BACKEND=max` avec Claude Code.
- Envoi : compte Resend, domaine d'envoi vérifié, `RESEND_API_KEY`, `MAIL_FROM`, `MAIL_REPLY_TO`.

## Lancer

Dans la copie : `npm install`, `npm run db:start`, `cp .env.example .env.local`, `npm run db:migrate`, `npm run build && npm start` (http://localhost:3457), `npm run worker` dans un second terminal.

Renseigner dans `.env.local` l'identité de l'élève : `SENDER_NAME` (obligatoire pour envoyer), `SENDER_COMPANY`, `SENDER_URL`. Sans elle, l'agent signe « [SENDER_NAME à renseigner] » et refuse d'envoyer.

## Règles

- Aucun envoi sans accord explicite de l'élève : un email part quand il clique sur « Envoyer » dans `/suivi`. `AUTO_SEND` et `MISSIONS_ENABLED` sont à `false` par défaut ; ne pas les passer à `true` sans son accord.
- La politique d'usage de Resend interdit la prospection à froid : le domaine d'envoi peut être suspendu. Le dire à l'élève avant le premier envoi réel.
- Le code est réglé sur la prospection d'avocats (prompts, cibles de mission, ville `MISSION_CITIES`). Une autre cible demande de modifier les prompts de `src/prompts/` et les cibles de `src/core/mission.ts` : le proposer, ne pas le faire en silence.
- Ne jamais committer `.env.local` ni les exports de campagne.
