import { migrate } from "drizzle-orm/node-postgres/migrator";
import { createDb } from "./client";

export async function runMigrations(url: string): Promise<void> {
  const { db, pool } = createDb(url);
  try {
    await migrate(db, { migrationsFolder: new URL("../../migrations", import.meta.url).pathname });
  } finally {
    await pool.end();
  }
}

if (process.argv[1] && import.meta.url.endsWith(process.argv[1].split("/").pop()!)) {
  const url = process.env.DATABASE_URL;
  if (!url) {
    console.error("DATABASE_URL absente.");
    process.exit(1);
  }
  await runMigrations(url);
  console.log("Migrations appliquées.");
}
