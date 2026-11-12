import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["tests/**/*.test.ts"],
    env: {
      SENDER_NAME: "Camille Test",
      SENDER_COMPANY: "Cabinet Test",
      SENDER_URL: "https://exemple.test",
      EMAIL_BANNER_FILE: "banniere-test.png",
    },
    fileParallelism: false,
    testTimeout: 60_000,
    hookTimeout: 60_000,
  },
});
