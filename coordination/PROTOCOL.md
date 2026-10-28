# Remote coordination protocol

The company repository's coordination/tasks.json is the construction board. claims.json stores active/released/submitted claims; integrations.json stores exact evidence. No copied prototype task board/SQLite lock is authoritative. All schedules are paused.

A single designated integrator coordinates a work unit; other agents own an isolated task packet/branch within an explicit scope plus dependency halo. Knowledge/graph regeneration, contracts used by multiple systems, Superadmin shared source/schema and integration records need one reserved writer. Independent department work belongs in its account/repo; reserve the relevant counterpart contract here before cross-system changes.

## Claim transaction

1. Fetch live branch head H, tasks and claims. Check target task READY, dependencies INTEGRATED, and no active or submitted claim has overlapping path prefix or semantic halo. Check exact account/repository.
2. Generate unique nonce, owner, task ID, exact base H, proposed paths/halo, started_at and explicit UTC expires_at. Record claim and task CLAIMED in one candidate tree/commit whose parent is H.
3. Update ref with expected_sha=H, force=false (normal fast-forward). Reread the claim from the committed ref and verify nonce. On mismatch refetch/inspect; never force-push or retry a stale ownership decision.
4. Check/renew the exact live nonce by CAS before expiry. A local file edit or independent clone is not a claim. Expired/unreleased claims remain reserved: require recorded confirmation prior writer stopped, then integrator revokes/requeues. Do not auto-steal based on wall clock.
5. Before submission refetch head, board and claim; verify ownership/expiry and scope. Submit immutable code/tests/patch/RESULT packet, exact original base and actual commands/results, then set SUBMITTED with packet commit. Scope stays reserved until review.
6. Integrator reviews, applies canonical source, verifies affected behavior, records actual commit/evidence and state INTEGRATED before unlocking successors. REJECTED/REVISION_REQUIRED preserves original packet and explicitly releases/reissues scope for its owner. APPROVED is not INTEGRATED.
7. Release own claim after writes stop. Stopped scheduling does not prove an already-running process stopped. Record real run-status evidence; do not fabricate it.

Parallel helper delegation is optional and task-dependent. Do not create five permanent schedules to simulate a continuously running team. Prefer short useful independent jobs with clear inputs/outputs, remote reservation and one integrator. No useful authorized ready work -> one bounded blocker, no repetitive heartbeat reports.
