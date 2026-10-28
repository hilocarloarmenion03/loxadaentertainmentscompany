# Agent work loop

## Start and choose

Fetch live target head using the correct connected account. Read AGENTS and relevant context from route/spec/graph. Run doctor. Inspect real code, active PRs/claims and current platform state; do not infer readiness from historical notes. Choose only a manual READY task whose dependencies are integrated and scope/halo do not conflict.

## Execute

Use coordination/PROTOCOL.md to claim remotely by expected-head CAS. Create an isolated branch/worktree if supported; avoid redundant branches/PRs on every wake-up. A connector workflow can fetch exact files and create tree/commit/ref updates without local gh authentication. Keep ordinary reversible work moving without repeated permission questions. Pause only dependent work when an actual external approval or unresolved business rule is required; continue independent authorized tasks.

Read existing interfaces and original source evidence. Write complete focused code/contracts/tests, not placeholders for unavailable effects. Do not copy a SQLite DB as a distributed lock. Do not run unattended loops or enable schedules because a task is READY.

## Verify and hand off

Run checks appropriate to the actual changed code. Distinguish static checks, unit tests, browser/API/database integration, deployment status and real provider actions. Record initial failures and final corrections honestly. A build does not prove business acceptance, and a deployment record does not prove database/RLS correctness.

Update the one task registry and integration ledger, Vault evidence and handoff. Regenerate graph; doctor and tests must pass for navigation changes. Re-fetch head/claims before publishing; safe expected-head CAS and normal fast-forward only. Integrate only reviewed canonical source with exact verification evidence, then release own lease and unlock successors. Do not mark another worker's SUBMITTED packet integrated merely because it looks useful.

## Recover from interruption

Save a concrete repository packet/branch before handing off when possible. A local draft is not remotely durable; explicitly record that limitation. Release only your own active lease after confirming your writes stopped. Never steal another expired/unreleased claim. If a run is interrupted by a new user role/task, stop incompatible mutations; preserve unfinished work and record exact ownership/evidence.
