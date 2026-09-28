import { expect, test } from "@playwright/test";

test("homepage renders and has expected title", async ({ page }) => {
  await page.goto("./");
  // The site title is declared in docs/.vitepress/config.mts. This previously
  // asserted /PhenoHandbook/, which is a different site and never matched.
  await expect(page).toHaveTitle(/Phenotype Registry/);
});

test("patterns page loads and shows sidebar", async ({ page }) => {
  await page.goto("patterns/architecture/hexagonal");
  await expect(page.locator("aside").first()).toBeVisible();
});

test("hexagonal pattern page loads", async ({ page }) => {
  await page.goto("patterns/architecture/hexagonal");
  await expect(page.getByRole("heading", { level: 1 })).toContainText(
    "Hexagonal Architecture",
  );
});
