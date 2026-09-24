# Concurrent workers and integration

Do not coordinate through last-writer-wins edits to one Markdown backlog. Use the accepted claim authority or one delegated coordinator with explicit bounded work. A claim-lease JSON file describes ownership; it does not enforce it. Lease expiry requires an actual fencing/CAS mechanism before a new worker can safely supersede writes.

Use isolated branches/worktrees, preserve dirty work, record base SHA and intended write set, and avoid holding unnecessary global locks. Pin cross-repository BOMs for integrated evaluation. A locally passing component does not prove the consumer combination.

Append per-producer immutable attempt/evidence records. Reconcile results explicitly; conflicting effective leaves are contested/unknown, not a chance to choose the most favorable. Land changes only through the actual permitted integration path and recheck against the integrated baseline. Record retries, rebases and stale claims.

If no reliable multiwriter primitive is available, serialize the affected acceptance step while retaining parallel read-only or disjoint work. Missing central AgilePlus is not a reason to invent a lock that does not work or stop the entire lab.
