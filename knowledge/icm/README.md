# ICM context routing

ICM here means the local curated context/navigation system. routes.json maps task vocabulary to bounded files, authority/status and related graph nodes. It does not call a model or a remote memory service. Each route's files must exist and its ID must be unique. Add focused context when needed, regenerate Graphify and run doctor/tests.

Use `python3 tools/nav.py route "<task>" --limit 5`. A low/no match is visible; refine the query or inspect the Vault index rather than inventing context. Exact business process extraction uses the locally pinned baseline and optional heading filter; duplicate process IDs across departments are reported explicitly.
