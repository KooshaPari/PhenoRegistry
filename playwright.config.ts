import { defineConfig, devices } from "@playwright/test";

/**
 * E2E config for the VitePress documentation site.
 *
 * By default this drives a local preview server. In CI the E2E Tests
 * workflow runs `bun run build` first and then points E2E_BASE_URL at the
 * published site, so the suite can also verify what users actually receive
 * rather than only a local build.
 */
/**
 * A leading slash in a spec path (e.g. "/SSOT.html") discards the entire
 * base path, so every test resolves against the domain root and 404s on a
 * project-scoped Pages site. Specs therefore use relative paths, which keeps
 * the base path only when the base itself ends in a slash.
 *
 * Enforce that here rather than trusting the caller's spelling: a bare
 * `process.env.E2E_BASE_URL` made this an unguarded trap.
 */
const baseURL = (process.env.E2E_BASE_URL ?? "http://127.0.0.1:4173").replace(
  /\/*$/,
  "/",
);

export default defineConfig({
  testDir: "./tests/e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? [["github"], ["html", { open: "never" }]] : "list",
  use: {
    // Normalised above; do not use process.env.E2E_BASE_URL directly.
    baseURL,
    trace: "on-first-retry",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
  ...(process.env.E2E_BASE_URL
    ? {}
    : {
        webServer: {
          command: "bunx vitepress preview docs",
          url: "http://127.0.0.1:4173/",
          timeout: 120_000,
          reuseExistingServer: !process.env.CI,
        },
      }),
});
