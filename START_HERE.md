# Start here

## Ten-minute cold start

1. Read this map, CURRENT_STATE and DECISIONS.
2. `python3 tools/nav.py status` distinguishes knowledge readiness from application readiness.
3. `python3 tools/nav.py route "<business/task words>"` returns a bounded context packet with file paths and why to read them.
4. `python3 tools/nav.py spec R-A-13` retrieves exact matching process definitions, not the full baseline. Process codes repeat across departments: inspect each returned section/path before using a rule. Use `--contains merchandise` to filter broad heading context if applicable, or route by department first.
5. `python3 tools/nav.py graph merch` and `python3 tools/nav.py ready` expose prerequisite work. Claim remotely as described in coordination/PROTOCOL.md.
6. Inspect actual target repository/runtime before implementation. Use the setup/runbooks rather than asking the user to reconstruct this chat.

## Source precedence

Latest explicit user instruction > recorded confirmed decisions > accepted pinned v1.0 > reviewed construction contracts > observed runtime/code > proposed designs > historical research. Code can demonstrate behavior but cannot silently redefine business requirements. If a genuine conflict remains, preserve both sources and open a bounded decision request; do not reinterpret an old proposal as approved.

## Navigation map

- [Vault index](knowledge/vault/INDEX.md): human decisions, requirements, architecture, current state and handoff.
- [ICM routing catalog](knowledge/icm/routes.json): curated task-to-context mapping, no paid embedding service.
- [Graphify guide](knowledge/graphify/README.md): deterministic entity/dependency graph from routes/tasks; no external Graphify package required.
- [Specification provenance](knowledge/specification/PROVENANCE.md): exact offline v1.0 snapshot and integrity hash.
- [Runbook](runbooks/AGENT_WORKFLOW.md): inspect, claim, execute, validate, hand off.
- [Bootstrap runbook](runbooks/STARTER_HANDOFF.md): inspect the starter the user creates without assuming deployment readiness.
- [Task board](coordination/tasks.json), [claims](coordination/claims.json), [integration ledger](coordination/integrations.json).
- [System repository boundaries](knowledge/vault/SYSTEM_REPOSITORIES.md) and [shared contract index](contracts/README.md).

This repository is the construction system of record. Keep large original research upstream; import a pinned necessary reference with provenance when agents would otherwise need hidden context. Never copy an upstream schedule, stale lock or prototype task board as active authority here.
