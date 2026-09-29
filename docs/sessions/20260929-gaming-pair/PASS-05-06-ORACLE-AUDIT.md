# Pass 5/6 — oracle audit and machine-evidence boundary

Date 2026-09-29. Exactly Dino + Civis.

Dino: existing hot-reload tests do not cover generation replacement/removal/patch invalidation. Runtime bridge `reloadPacks` reduces load evidence to success + pack IDs + error strings and ignores the optional protocol path parameter in the inspected handler. This cannot bind an autonomous grader to an exact effective generation or requested root. Product commits: `c366af1e1e22634e7a2a42992d75c163f3314a81`, `b17973c19a8c9659e8ef26b0524ca10c860b9688`.

Civis: existing save integrity tests are substantive for corruption detection, but guest-state tests intentionally round-trip memory for mod IDs that were never loaded, demonstrating guest-memory/active-mod decoupling. No semantic save tests were discovered for mutable economy_policy or research_cache. Integrity-test prose claiming resistance to a manifest editor is narrowed: the test leaves the unkeyed root stale; a writer able to recompute the manifest/root is outside what this BLAKE3 scheme proves. Product commits: `e60ed83745f8a3f10fafdfd216043927cd65fe91`, `3a8909db6b5e78ca6f400449086419ec9d93b4ed`.

Next execution: add expected-failure isolated tests where branch policy permits, then run when compatible toolchain is available; otherwise preserve them as executable oracle patches without false run receipts.
