import { expect, test } from "@playwright/test";

/**
 * Smoke tests for the published documentation site.
 *
 * The `test:e2e` runner printed "not implemented" because no specs existed.
 * These are the first real ones, aimed at the failure modes that have
 * actually broken this site rather than at generic page-load checks.
 */

/**
 * Paths that exist in the VitePress build output.
 *
 * These are relative on purpose. A leading slash would be resolved against
 * the domain root rather than the `baseURL` path, which breaks on
 * project-scoped Pages deployments such as `/PhenoRegistry/`.
 */
const ROUTES = ["", "SSOT.html", "GLOBAL_HANDBOOK.html"];

test.describe("documentation site", () => {
  test("serves the home page", async ({ page }) => {
    const response = await page.goto("");
    expect(response?.status()).toBe(200);
    await expect(page).toHaveTitle(/Phenotype Registry/);
  });

  test("renders client-side navigation", async ({ page }) => {
    await page.goto("");
    // VitePress ships a JS-driven shell; a build that emitted raw markdown
    // would still return 200 but render no site chrome.
    await expect(
      page.locator(".VPNav, .VPSidebar, .VPLocalNav").first(),
    ).toBeVisible();
  });

  /**
   * Regression guard for the PII placeholder defect.
   *
   * A PII scrubbing pass wrote bare `<REDACTED>` into prose, which Vue
   * parses as an HTML tag. That broke both VitePress builds and produced
   * unreadable output rather than an obvious error, so it is worth pinning.
   * See commit d0466c7.
   */
  test("does not emit unescaped REDACTED tags into the DOM", async ({
    page,
  }) => {
    await page.goto("");
    const strayTags = await page
      .locator("redacted")
      .evaluateAll((nodes) => nodes.map((n) => n.tagName));
    expect(strayTags, "bare <REDACTED> parsed as an element").toEqual([]);
  });
});

test.describe("known routes", () => {
  for (const route of ROUTES.slice(1)) {
    test(`${route} responds 200`, async ({ page }) => {
      const response = await page.goto(route);
      expect(response?.status(), `${route} should be published`).toBe(200);
    });
  }
});
