# Adversarial oracle catalog

Apply where relevant to every critical behavior:
- happy path;
- invalid input;
- missing dependency;
- dependency timeout/failure;
- authorization denied;
- approval absent/stale/wrong actor;
- wrong product/candidate/config/environment evidence;
- missing/skipped/collector-failed evidence;
- stale evidence;
- conflicting evidence;
- duplicate/replayed event;
- reordered event;
- disconnect/reconnect;
- process crash before dispatch;
- crash after external effect before acknowledgement;
- crash after acknowledgement before terminal state;
- worker replacement;
- client replacement;
- corrupted persistence/event history;
- concurrent writers;
- cancellation during model/tool/effect;
- budget/resource exhaustion;
- queue saturation/backpressure;
- provider capability mismatch;
- protocol/version mismatch;
- migration/upgrade/rollback;
- malicious/untrusted tool output;
- grader unavailable/version mismatch;
- mutation test: remove each guard and ask whether a false green can be manufactured.

Critical failures fail closed unless the contract explicitly defines a degraded mode.
