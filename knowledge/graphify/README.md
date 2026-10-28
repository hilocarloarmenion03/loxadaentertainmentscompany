# Graphify navigation

This is the repository's lightweight deterministic Graphify implementation, not an installed third-party product. Nodes come from knowledge/icm/routes.json and coordination/tasks.json. Edges encode document relationships and task prerequisites; they are navigation/dependency evidence, not claims of implemented business integration.

`python3 tools/nav.py graph-build` writes graph.json. `python3 tools/nav.py graph merch --depth 2` traverses neighbors. `doctor` rejects stale generated output, dangling nodes, missing files and task dependency cycles. Do not hand-edit graph.json or build a second competing task board.
