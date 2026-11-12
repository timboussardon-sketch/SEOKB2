#!/bin/zsh
# Lancé par launchd : base locale, puis le worker (missions, campagnes, relevés) ou le tableau de bord.
# claude et codex se résolvent par le PATH, jamais par un chemin en dur.
# Sans locale, PostgreSQL refuse de démarrer sous launchd (« postmaster became multithreaded »).
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
cd "$(dirname "$0")/.."
./scripts/db-start.sh
npm run db:migrate
case "$1" in
  worker) exec npm run worker ;;
  web) exec npm start ;;
  *) echo "usage: service.sh worker|web" >&2; exit 2 ;;
esac
