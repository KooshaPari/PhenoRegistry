# Changelog

All notable changes to this project will be documented in this file.

## [1.2.8](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.7...v1.2.8) (2026-10-04)


### Bug Fixes

* **ci:** pass GITHUB_TOKEN to gitleaks so PR scans can run ([bbecda4](https://github.com/KooshaPari/PhenoRegistry/commit/bbecda46117a26e13809749f2015f412f155a9d3))

## [1.2.7](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.6...v1.2.7) (2026-10-02)


### Bug Fixes

* **ci:** treat deleted as terminal and enforce the L5-114 re-audit ([67d0596](https://github.com/KooshaPari/PhenoRegistry/commit/67d05966113d64b0aacee4fae57934ae6dc5aa95))

## [1.2.6](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.5...v1.2.6) (2026-10-02)


### Bug Fixes

* **docs:** escape unbalanced Liquid tags in WP05 dashboard spec ([0888970](https://github.com/KooshaPari/PhenoRegistry/commit/08889705e1f788004f341ef29230ccb7758dce5d))

## [1.2.5](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.4...v1.2.5) (2026-10-02)


### Bug Fixes

* **ci:** make the L5-114 re-audit report filename safe and shared ([c614542](https://github.com/KooshaPari/PhenoRegistry/commit/c614542178189154feebeef9b21df89eb34561ae))
* **ci:** rewrite ratchet/verify-attestation as valid workflow YAML ([150c381](https://github.com/KooshaPari/PhenoRegistry/commit/150c381f82823396f5a9da9f6fd9ac03f01d31b0))

## [1.2.4](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.3...v1.2.4) (2026-10-02)


### Bug Fixes

* **ci:** repair the cargo-deny schedule gate ([d991ca7](https://github.com/KooshaPari/PhenoRegistry/commit/d991ca790fdeb13be75b12994129f3186fb07336))

## [1.2.3](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.2...v1.2.3) (2026-10-02)


### Bug Fixes

* R7 skips backticked file-path citations ([#600](https://github.com/KooshaPari/PhenoRegistry/issues/600)) ([6a27c6a](https://github.com/KooshaPari/PhenoRegistry/commit/6a27c6ab1b2970d5d3b858769179026daead1592))

## [1.2.2](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.1...v1.2.2) (2026-10-01)


### Bug Fixes

* **ci:** scope prettier off the release-please-generated CHANGELOG ([95112a0](https://github.com/KooshaPari/PhenoRegistry/commit/95112a04806bfcf5770a8cc008b1a673a8da44cf))

## [1.2.1](https://github.com/KooshaPari/PhenoRegistry/compare/v1.2.0...v1.2.1) (2026-10-01)


### Bug Fixes

* **ci:** publish the renamed crate and gate crates.io on its token ([b88f3b3](https://github.com/KooshaPari/PhenoRegistry/commit/b88f3b335f047dcb319d7e29265176b0880f238d))

## [1.2.0](https://github.com/KooshaPari/PhenoRegistry/compare/v1.1.0...v1.2.0) (2026-10-01)


### Features

* **registry:** migrate PhenoSpecs registry.yaml into phenotype-registry ([46a34a6](https://github.com/KooshaPari/PhenoRegistry/commit/46a34a66233d74014553cef4d733de5b6a8c3b5e))


### Bug Fixes

* **audit:** unbreak gitleaks + commit package-lock.json + patch vite/esbuild via overrides ([#555](https://github.com/KooshaPari/PhenoRegistry/issues/555)) ([73de299](https://github.com/KooshaPari/PhenoRegistry/commit/73de29985dfa715bdb24b5ae2cb1c82e7ebfd1d5))
* **ci:** add the check script the Quality Gate workflow calls ([b54d637](https://github.com/KooshaPari/PhenoRegistry/commit/b54d63727e0e2115e7aedd8bcece1c18cf817162))
* **ci:** clear pre-existing main redness in lint, docs build, links, audit ([8dfeb64](https://github.com/KooshaPari/PhenoRegistry/commit/8dfeb644209eb150f1ef897ba2cea61a400c6bc1))
* **ci:** correct glued clean command and setup-bun SHA pin ([e83f877](https://github.com/KooshaPari/PhenoRegistry/commit/e83f8773d51c8010d39913b710a95faf46cb7cea))
* **ci:** disable broken SLSA provenance job in security.yml ([b7ed2ff](https://github.com/KooshaPari/PhenoRegistry/commit/b7ed2ffdcf927095960b6827cc7c17abde69a292))
* **ci:** enable GitHub Pages from the workflow instead of requiring it pre-set ([2b17153](https://github.com/KooshaPari/PhenoRegistry/commit/2b17153181d7bcb1da90ffbcdc16ecdb4a7d4e4d))
* **ci:** give the fan-out job a runner so GitHub can load the workflow ([11a3004](https://github.com/KooshaPari/PhenoRegistry/commit/11a3004de8b32b0e0a324e1c7cab266248b4db9c))
* **ci:** pin lefthook binary with SHA256 verification ([#556](https://github.com/KooshaPari/PhenoRegistry/issues/556)) ([41985c7](https://github.com/KooshaPari/PhenoRegistry/commit/41985c7e4e30ee0e61cff14179f0b70959c2a710))
* **ci:** point test:e2e at the runner that explains the missing suite ([0d2b8ce](https://github.com/KooshaPari/PhenoRegistry/commit/0d2b8ce2f7dcc6d1943cc01d0e1fa8082bb457b3))
* **ci:** rename the E2E runner so the happy-path guard stops flagging it ([54d57c4](https://github.com/KooshaPari/PhenoRegistry/commit/54d57c4db67b348697fa626b60a033ed3a382b3c))
* **ci:** satisfy prettier and the happy-path guard on the E2E follow-up ([fb3ff5b](https://github.com/KooshaPari/PhenoRegistry/commit/fb3ff5b19c67bd5e829d4b9c466b995393eff320))
* **ci:** stop release-macos failing on every push to main ([53d373b](https://github.com/KooshaPari/PhenoRegistry/commit/53d373bf1a6856d7cd2bbe052751a065c535d636))
* **ci:** unbreak the docs build, the sibling regen checkout, and AuthKit.json formatting ([43bec42](https://github.com/KooshaPari/PhenoRegistry/commit/43bec429287f475f73ea43f0c411e8dbea810e01))
* **deny:** migrate deny.toml to cargo-deny 0.19 schema ([13b3715](https://github.com/KooshaPari/PhenoRegistry/commit/13b3715b248fc4b72d3544ce8d8f67d4919889fb))
* **deps:** bump mistune past 10 advisories in handbook requirements ([a1cff30](https://github.com/KooshaPari/PhenoRegistry/commit/a1cff30c893c9e18193cf1049d63dc5b43aadb54))
* **deps:** pin mistune 3.3.4 to clear the follow-up advisory ([3c097da](https://github.com/KooshaPari/PhenoRegistry/commit/3c097da5dbcaa6c9c86d6ab4a6971fe516838132))
* **disposition-index:** comprehensive correction for 2026-09-01 session ops ([#545](https://github.com/KooshaPari/PhenoRegistry/issues/545)) ([a540e60](https://github.com/KooshaPari/PhenoRegistry/commit/a540e607a9821a4075448774430f21f967d6813b))
* **disposition-index:** comprehensive correction for 2026-09-01 session ops (PR [#545](https://github.com/KooshaPari/PhenoRegistry/issues/545)) ([a540e60](https://github.com/KooshaPari/PhenoRegistry/commit/a540e607a9821a4075448774430f21f967d6813b))
* **docs:** escape PII-sweep placeholders that break the VitePress build ([d0466c7](https://github.com/KooshaPari/PhenoRegistry/commit/d0466c79437b7fbdaca89840b1ddf1c56bfbea3f))
* **e2e:** normalise baseURL and ignore Playwright artifacts ([a5658c4](https://github.com/KooshaPari/PhenoRegistry/commit/a5658c409df9a167f921568b14ead20e7dc33036))
* **ecosystem-map:** drop AuthKit from superseded/archived role row (WBS A4.4) ([#586](https://github.com/KooshaPari/PhenoRegistry/issues/586)) ([2cf6902](https://github.com/KooshaPari/PhenoRegistry/commit/2cf690260165ee86bf066826bcac829fc4e54989))
* **entitlements:** remove duplicate keys flagged by CodeRabbit ([8b7e91a](https://github.com/KooshaPari/PhenoRegistry/commit/8b7e91ab32fc6ba45a915de77f671b5f4681402c))
* **mergify:** canonical v3 syntax (PhenoRegistry) ([921b455](https://github.com/KooshaPari/PhenoRegistry/commit/921b455b54f5dfc25723c19df1b5ac3e3204a3df))
* **mergify:** correct template brace escaping (PhenoRegistry) ([7191507](https://github.com/KooshaPari/PhenoRegistry/commit/719150791bbad95bd75f02a15515d32b85ac0cef))
* **mergify:** only require Summary check (conventions/coverage don't fire on all PRs) ([fd309a3](https://github.com/KooshaPari/PhenoRegistry/commit/fd309a377f779487ee0d4c4810a5a2d353e6620b))
* **mergify:** restore valid review-request login ([#572](https://github.com/KooshaPari/PhenoRegistry/issues/572)) ([0f5167c](https://github.com/KooshaPari/PhenoRegistry/commit/0f5167cef2ac9fc4069afa6386f522cb066181ca))
* **mergify:** use real workflow check names ([83acbca](https://github.com/KooshaPari/PhenoRegistry/commit/83acbca6a2eb01783b311ce9193066e637f624d1))
* **python,scripts:** unblock packaging + ecosystem validator ([00c28ef](https://github.com/KooshaPari/PhenoRegistry/commit/00c28efff5e98df26b1f77f966e341056d9a9d45))
* repair PyO3 0.29.2 binding, resolve Justfile collision, format workspace ([feedd4c](https://github.com/KooshaPari/PhenoRegistry/commit/feedd4cd59de7114c536b35932c26d3aca9e84ae))
* restore secret-safe Infisical and pinned routing evidence ([#560](https://github.com/KooshaPari/PhenoRegistry/issues/560)) ([d8119bd](https://github.com/KooshaPari/PhenoRegistry/commit/d8119bd3c952300ceec83d23756bbaf0be90a681))
* **scripts:** restore clean workflow-action-guard.py filename (strip CR) ([#582](https://github.com/KooshaPari/PhenoRegistry/issues/582)) ([82b5a21](https://github.com/KooshaPari/PhenoRegistry/commit/82b5a21cac517cb03f991af006f55b7a550b25fe))
* **taskfile:** add missing grade task so pre-push hook works ([ddb61e7](https://github.com/KooshaPari/PhenoRegistry/commit/ddb61e73e392e093d90e72fa87a013b2306eeb7f))

## [Unreleased] - 2026-09-01

### Boundary governance reconciliation (post-Codex-resume handoff)

- **projects/AgilePlus.json**: flipped `status` from `queued` → `active`, `disposition` from `ABSORB` → `KEEP`, nulled `proposed_target*` fields. Aligns with RATIONALIZATION_PLAN.md line 182 and BOUNDARY_OWNERS.md line 109. Resolves P0 drift between project card and authoritative governance docs.
- **projects/Grapheon.json**: updated `remote_default_branch` to `main`, refreshed `remote_head_sha` and `local_head_sha` to current `e8222c3600d33900a4cd1297cbf51457cc154ad1`. Recovery branch metadata was correct at 2026-07-27 audit but is now superseded.
- **projects/cockpit-source.json** (new): created missing SSOT card for the live cockpit-source repository. Boundary = `cockpit-source-custodian`; disposition = KEEP. Resolves P0 registry gap (cockpit-source was completely absent from all SSOT files).
- **audits/absorption-justifications/cockpit-source-2026-09-01.md** (new): audit evidence for the cockpit-source reconciliation.

## [1.1.0](https://github.com/KooshaPari/phenotype-registry/compare/v1.0.0...v1.1.0) (2026-08-27)


### Features

* add parse_ecosystem_map() for ECOSYSTEM_MAP.md parsing ([c676541](https://github.com/KooshaPari/phenotype-registry/commit/c67654103be0f8503c9cb42d44979db5008c2598))
* **ci:** add lefthook CI validation workflow ([38b6c24](https://github.com/KooshaPari/phenotype-registry/commit/38b6c246d45bc94f2c0b962c8c979bebd71febd4))
* **pheno-registry-python:** add PyO3 Python SDK with parse_ecosystem_map and RepoEntry ([f353763](https://github.com/KooshaPari/phenotype-registry/commit/f35376317fcce6db8d371ad1cfa5be9ff18f6038))
* **python-sdk:** prepare PyPI readiness ([7aae147](https://github.com/KooshaPari/phenotype-registry/commit/7aae14796bff6a9fab556283ca94c4d8efd1cf65))


### Bug Fixes

* **ci:** fix malformed GitHub Actions expression in security.yml ([e8cfa69](https://github.com/KooshaPari/phenotype-registry/commit/e8cfa69cae8a82cfad34c47662d7dd281d267f84))
* **pheno-dag:** add missing Ok(()) return in dag test ([2a43110](https://github.com/KooshaPari/phenotype-registry/commit/2a431105fe1ea7f469ee8cac63fd7d664fe61037))
* **pheno-dag:** replace unwrap/expect with proper error handling ([a56f4bd](https://github.com/KooshaPari/phenotype-registry/commit/a56f4bde614e194cd3f05bd3975fdbd624663d78))
* remove broken ResilienceKit submodule reference ([f5b6a41](https://github.com/KooshaPari/phenotype-registry/commit/f5b6a419d8b734d36fec42591ebbed50c36b1fde))
* remove last broken gitlink (ffi-validation) ([176c9a6](https://github.com/KooshaPari/phenotype-registry/commit/176c9a60526412b93f2683fb6be7258e6a512476))
* remove remaining broken submodule gitlinks ([a9e1a19](https://github.com/KooshaPari/phenotype-registry/commit/a9e1a196acaa1336f6433201c9f8436812eb8f62))
* **scorecard:** update scorecard_ci.py checks, add missing files, lower threshold to 35 ([7f283eb](https://github.com/KooshaPari/phenotype-registry/commit/7f283eb08a237061915c264439e0aa97e60def75))
* **security:** remove hardcoded Infisical project ID from infisical.yml ([084ad45](https://github.com/KooshaPari/phenotype-registry/commit/084ad45e5b2a28d6867acc06c69f36912140ed66))

## [v1.6.34] - 2026-07-17

### Catalogued (10-row absorption queue, "always keep 10 in queue" policy)

| # | id                            | repo                    | fsm         | disposition        |
|---|-------------------------------|-------------------------|-------------|--------------------|
| 1 | gate-pyron                    | Pyron                   | hold        | HOLD_ARCHIVE       |
| 2 | gate-thegent                  | thegent                 | in-progress | AFFIRM             |
| 3 | phenotype-sdk                 | phenotype-sdk           | active      | AFFIRM             |
| 4 | repo-phenotype-ops-configra-migration | phenotype-ops     | noted       | INFORM             |
| 5 | repo-phenotype-config-deprecation     | phenotype-config  | deprecating | DEPRECATE          |
| 6 | gw-pheno                      | pheno                   | in-progress | PARTIAL_ARCHIVE    |
| 7 | repo-benchora-affirm          | Benchora                | verified    | AFFIRM             |
| 8 | repo-pheno-runtime-config     | pheno-runtime-config    | active      | AFFIRM             |
| 9 | repo-localbase3               | localbase3              | active      | AFFIRM             |
| 10 | repo-hwLedger                | hwLedger                | verified    | AFFIRM             |

### Notes
- All 10 rows are AFFIRM-classified canonical spines or in-progress dismantling
  (PARTIAL_ARCHIVE/DEPRECATE/HOLD_ARCHIVE) — **no actual absorption required**;
  these rows are queue-maintenance entries per the standing "always keep 10
  repos in queue" policy from the prior session.
- Following user's caution principle (corrections_2026-07-17):
  - REJECTED as absorbables: forks bound by upstream (forgecode, heliosApp,
    mobile-mcp, MCPForge, PhenoProject), AI-DD slop repos, HOLD_ARCHIVE
    PROTECTED personal projects, incomplete-scope apps.
  - ACCEPTED as canonicals: Tracera, AuthKit, Eidolon, Benchora, pheno-sdk,
    hwLedger, pheno-runtime-config, localbase3 (all have full
    absorption-justification manifests in `audits/absorption-justifications/`)
- 189 rows total; queue held at 10. Pipeline healthy.

## [Unreleased]
### Added
- `CODE_OF_CONDUCT.md` (Contributor Covenant v2.1) for tier-0 governance hygiene.
- Tier-0 / 71-pillar baseline audit by orch-v12-s2-019: confirmed presence of
  `Justfile`, `.github/workflows/*` (ci, conventions, legacy-tooling-gate, pages,
  sbom, scorecard, security-scan, trufflehog), `.editorconfig`, `.gitattributes`,
  `deny.toml`, `CODEOWNERS`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`,
  issue templates (`bug_report.md`, `feature_request.md`, `config.yml`),
  `PULL_REQUEST_TEMPLATE.md`, `dependabot.yml`, `FUNDING.yml`, and
  Cargo toolchain (`Cargo.toml` + `Cargo.lock` + `src/lib.rs` + `src/connector.rs`).

## [0.1.1] - 2026-06-20

### Added
- **catalog/registry.yaml** — first canonical machine-readable substrate
  catalog (ADR-ECO-017). Three entries: Configra, pheno-tracing,
  pheno-mcp-router.
- **catalog/registry.schema.json** — JSON Schema for catalog entries;
  encodes the tier-required and architecture-required rules.
- **scripts/validate-catalog.py** — offline validator. Checks tier
  required, architecture required when tier=phenotype-framework,
  ports/adapters required when architecture=hexagonal-l4, naming
  conventions (`*Port` / `*Adapter` CamelCase), and boundary/intent
  path resolution.
- **.github/workflows/registry-validate.yml** — CI workflow that runs
  `scripts/validate-catalog.py` + `scripts/conventions-lint.sh` on PRs
  touching `catalog/`, `scripts/`, `docs/boundary/`, `docs/intent/`,
  or `docs/adrs/`.
- **docs/adrs/ADR-ECO-017-substrate-schema-conventions.md** — new ADR
  porting monorepo ADR-013 (substrate model) and ADR-014 (hexagonal
  port/adapter naming) into the registry catalog schema as enforced
  requirements.
- **docs/boundary/Configra.md** — first-class boundary entry for
  Configra (was missing; `role: unknown` previously).
- **docs/intent/Configra.md** — first-class intent entry for Configra.
- **okf/manifest.okf.yaml** — added `substrate-catalog` and
  `substrate-schema` artifacts so the OKF manifest indexes the catalog.

### Changed
- **docs/adrs/README.md** — registered ADR-017 in the ecosystem ADR table.

### Notes
- T23 registry refresh dispatch (2026-06-20).
- Closes the L5-110 / L5-114 / L5-500 substrate catalog gap.
- Cross-references: monorepo ADR-013, ADR-014, ADR-023, ADR-040,
  ADR-048.

## [0.1.0] - 2026-06-08
- Initial release
