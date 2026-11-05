import { drizzle, type NodePgDatabase } from "drizzle-orm/node-postgres";
import pg from "pg";
import * as schema from "./schema";

export type Db = NodePgDatabase<typeof schema>;
export type Tx = Parameters<Parameters<Db["transaction"]>[0]>[0];

export function createDb(url: string): { db: Db; pool: pg.Pool } {
  const pool = new pg.Pool({ connectionString: url, max: 10 });
  return { db: drizzle(pool, { schema }), pool };
}

const globalForDb = globalThis as unknown as { __agentDb?: { db: Db; pool: pg.Pool } };

/** Connexion partagée de l'application. Sans DATABASE_URL, l'erreur est explicite et rien n'est simulé. */
export function getDb(): Db {
  if (!globalForDb.__agentDb) {
    const url = process.env.DATABASE_URL;
    if (!url) throw new Error("DATABASE_URL absente : la base PostgreSQL n'est pas configurée.");
    globalForDb.__agentDb = createDb(url);
  }
  return globalForDb.__agentDb.db;
}

export { schema };

/** Verrou consultatif tenu par une connexion dédiée, donc libéré si le process s'arrête. */
export function lockerFor(pool: pg.Pool) {
  return async (key: string): Promise<(() => Promise<void>) | null> => {
    const client = await pool.connect();
    try {
      const { rows } = await client.query("select pg_try_advisory_lock(hashtextextended($1, 0)) as ok", [key]);
      if (!rows[0].ok) {
        client.release();
        return null;
      }
    } catch (err) {
      client.release();
      throw err;
    }
    return async () => {
      try {
        await client.query("select pg_advisory_unlock(hashtextextended($1, 0))", [key]);
      } finally {
        client.release();
      }
    };
  };
}

export function getPool(): pg.Pool {
  getDb();
  return globalForDb.__agentDb!.pool;
}
