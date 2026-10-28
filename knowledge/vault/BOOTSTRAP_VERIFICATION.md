# Bootstrap verification

Verified2026-10-28: knowledge/navigation bootstrap only. See the Git history of this file for the exact published source commit; no fabricated future SHA is embedded.

Executed from the new construction tree:

- `python3 tools/nav.py graph-build`: deterministic graph generated from route/task catalogs.
- `python3 tools/nav.py doctor`: ok=true, zero errors; pinned baseline hashes, routed paths, local Markdown links, graph freshness and task/claim invariants checked.
- `python3 -m unittest discover -s tests -v`:8tests passed. Covers offline cold start/readiness, bounded relevant routing and unknown query, exact baseline retrieval/context, graph dependencies, missing files/broken links/stale graph, cycles/false readiness, expired reserved claims/path conflicts, baseline tampering/path escape.
- status/ready/route/spec/graph commands executed successfully; only SCHEMA-CONTRACTS is manual READY, while starter-dependent work remains blocked.
- An isolated temporary copy without sibling repositories executed doctor, owner warehouse routing, exact R-A-13 retrieval and all8tests successfully. Navigation requires only included files and Python standard library.

Baseline content:2258314bytes; Git blob ad7ab944417f601804851283bfbd0ef2a10b6de1 matched live upstream metadata; SHA256bf3151dbc2c8c5d8395372422a525981405188818147e6d53772314f43df14c0.

Research: official OpenAI AGENTS.md/harness-engineering guidance and the AGENTS.md open convention were consulted; applied recommendations and source links are recorded in RESEARCH_AGENT_WORKFLOW.md.

A push/PR-only knowledge CI workflow is included. Its remote execution is not claimed here. No application build, migrations, Auth/RLS, database inspection, ETL job, deployment or cloud setup was performed by this bootstrap. No schedules created or resumed. No department repository, legacy Superadmin repository or upstream knowledge collection changed.
