# Pass 4 — concrete state omission and generation identity

Date 2026-09-29. Program remains exactly Dino + Civis.

Dino product commit `4b2b58783d3bcebdc70f1f605faa12aef5d4a912`: RegistryEntry has SourcePackId and priority but no version/digest/generation identity. Hot reload's UpdatedEntries are pack IDs, not exact changed registry entries. Combined with no observed unregister-by-pack and a path-only patched-YAML cache, exact generation identity/replacement is now the central activation experiment.

Civis product commit `d0c647d244db55bb5936682e932e153633514000`: active CivSaveBundle component map completed to first useful denominator. Replay reconstruction was inspected directly: ModLoaded/ModUnloaded, Climate, RngDraw and several audit events are no-op during replay. The bundle persists mod guest memory but no observed loaded-mod-set/artifact identity. Runtime economy_policy has no observed save component or replay event and resets through Simulation::with_seed unless reapplied elsewhere. ResearchOutcome replay currently does not reconstruct research state. These are now exact omission/semantics probes rather than generic "save may be incomplete" concerns.

The v5 integrity manifest remains valuable: it proves bytes of serialized components, not completeness of live state. Metadata downgrade classification remains open.

Next: field/mutation inventory + isolated executable experiments where toolchain permits. No mature requirement count or completion percentage is inferred.
