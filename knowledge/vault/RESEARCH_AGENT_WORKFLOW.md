# Research: efficient agent operation

Reviewed2026-10-28. Primary sources:

- [OpenAI agent instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md): predictable AGENTS.md entrypoints and directory-specific instruction discovery. Applied: concise root map and explicit cross-repository application boundaries; no giant injected baseline.
- [OpenAI harness engineering](https://openai.com/index/harness-engineering/): repository-local system of record, progressive context discovery and mechanically checked boundaries. Applied: local docs, explicit task/status/evidence, generated navigation graph and CI checks. Its reported productivity is that team's observation, not a LOXADA performance claim.
- [AGENTS.md open convention](https://agents.md/): portable repository instructions complement human README. Applied: no vendor-specific hosted memory dependency.

Engineering recommendation, not a new business requirement: curated keyword routing and deterministic dependency graphs are enough initially. Add semantic search only if retrieval tests show a real missed-context problem. Build graph data from one routing/task catalog instead of hand-maintaining competing maps. Prefer readable local JSON/Markdown and Python standard-library tools so a fresh agent can navigate offline.

Autonomy needs a feedback loop: known requirements, exact active task/scope, reproducible commands, observable failures, small changes, meaningful verification and durable handoff. Worktrees isolate edits; remote claims coordinate writers. Agent role labels or timers alone do not establish exclusive execution. Expiry alone never proves a prior process stopped.

Repository text supplies context, not authentication or business approval. Preserve real external blockers. No schedule was created/resumed and no new infrastructure vendor was provisioned for this recommendation.
