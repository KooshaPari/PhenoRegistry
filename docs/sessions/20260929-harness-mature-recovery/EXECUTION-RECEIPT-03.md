# Execution receipt 3 — native feedback and differentiation falsification

Date: 2026-09-29. Program HARNESS-MATURE-20260929 remains OPEN.

## HeliosLite candidate #322
Dedicated oracle CI on head `19092646...` executed 8 adversarial tests: 7 passed and the signal-specific witness failed because the fixture had been mangled to `kill -TERM $`, producing shell exit 2. This was a test-fixture defect, not accepted product evidence. The fixture is corrected at head `8451b952ef26f0720ee5e87d25eda6da1bc38700` using a quoting-safe Python parent-signal command. A fresh dedicated run is queued.

On the previous head, the normal Platform Tests workflow later passed, along with Cargo Deny, Trunk Check, CodeQL, secrets scan, performance benchmark and one CI workflow; other workflows were queued/cancelled/skipped. A skipped/cancelled check is not green.

## KCode candidate #14
The targeted native job now reached Rust compilation. It found four concrete integration errors: a name collision with the existing server::util::ServerIdentity and three additional Pong constructors lacking the new optional identity fields. The runtime identity type was renamed to RuntimeServerIdentity; debug/keepalive producers explicitly emit identity fields as None; post-subscribe Ping is routed through the same full responder as pre-subscribe Ping so connection phase cannot silently change identity semantics. Current candidate head: `11cb8c0003a7e4d52633947f69819f702aa8d8cb`. Fresh native CI is queued.

Important semantic distinction: a generic keepalive Pong is not treated as runtime attestation. Full version/git/PID/executable-SHA identity is emitted by an actual Ping responder.

## Existence gate
Current upstream jcode materially falsifies historical differentiation claims. Generic swarm coordination, harness API/SDK and elicitation/discovery are present upstream today. KCode frozen master is 136 commits ahead and 2,320 behind the inspected current-upstream control; those 136 commits are now a retained-patch search space, not a value score. Audit/generated/branding work does not count as behavioral differentiation.

Potential surviving KCode differentiation is narrower: exact runtime/evidence identity; demonstrably different provider/subscription routes; native Windows/Pine obligations; owned Pheno integrations; and specific retained patches absent upstream. Each remains unverified.

No merge, architecture freeze, product-existence verdict or completion percentage is authorized by this receipt.