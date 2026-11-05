#!/bin/sh
# Démarre un PostgreSQL local dédié au projet (données dans .pgdata, port 5544).
set -e
cd "$(dirname "$0")/.."
PORT=5544
if [ ! -d .pgdata ]; then
  initdb -D .pgdata -U agent --auth=trust -E UTF8 --locale=C >/dev/null
fi
if ! pg_isready -q -h 127.0.0.1 -p $PORT; then
  pg_ctl -D .pgdata -o "-p $PORT -c listen_addresses=127.0.0.1" -l .pgdata/server.log -w start >/dev/null
fi
for DB in agent_avocats agent_avocats_test; do
  psql -h 127.0.0.1 -p $PORT -U agent -d postgres -tAc "select 1 from pg_database where datname='$DB'" | grep -q 1 \
    || createdb -h 127.0.0.1 -p $PORT -U agent "$DB"
done
echo "PostgreSQL prêt : postgresql://agent@127.0.0.1:$PORT/agent_avocats"
