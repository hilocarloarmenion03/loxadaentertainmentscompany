# Superadmin scope

Apply root AGENTS.md. Read contracts/README.md, knowledge/vault/ACCOUNTS.md and pinned Owner baseline sections before source changes. This directory owns Superadmin only; do not import department business engines, credentials or raw customer data.

Detect the actual starter and its package manifest/lockfile before installs/builds. Keep server-only secrets out of public bundles. Validate authentication, actual-role authorization and data isolation at the database boundary; no default Superadmin account. Use versioned migrations and source-authenticated exact requests/permissions, separate from analytics.

Record actual browser -> API -> database -> response evidence where implemented. Missing infrastructure stays BLOCKED, not mocked as a successful integration.
