# Account and repository boundaries

CONFIRMED owner identities; no credentials belong here.

| System | Account email | GitHub owner | Construction target |
| --- | --- | --- | --- |
| Owner | hilocarloarmenion03@gmail.com | hilocarloarmenion03 | Separate Superadmin application repo under hilocarloarmenion03; exact name pending |
| Manga/LN | lozadatech01@gmail.com | lozadatech01 | Existing mangalighnovelsubsystem candidate; verify user starter target |
| Anime | hebratech01@gmail.com | hebratech01 | Existing animesubsystem candidate; verify user starter target |
| Merch | padregandatech01@gmail.com | padregandatech01 | Existing merchandise candidate; verify user starter target |

The Manga repository name really contains `mangalighnovelsubsystem` at the prior inspection; do not silently rename it to the Supabase project's spelling.

Prior read-only observations on2026-10-28:

| System | Vercel project | Supabase project/ref | Supabase observed state |
| --- | --- | --- | --- |
| Owner | superadmin (legacy) | admin / wrhaxigoqbydbjvigljv | INACTIVE |
| Manga | lozadatech01 | mangalightnovelsubsystem / vkyqexnfefwdhttsdhxf | INACTIVE |
| Anime | animesubsystem | anime / rplfvkmjwsndfuwcklqu | INACTIVE |
| Merch | merchandise | merchandise / hxwihcejbxzqhpdocoxd | INACTIVE |

These are historical observations, not canonical deployment bindings. User is creating starters; re-fetch actual target bindings. A separate loxada-connected-preview deployment under Owner hosts a historical browser-local prototype; it is not the production Superadmin. Do not delete it or unrelated guider/mcptest resources as cleanup.

Connector workflow: discover tools and inspect connected account metadata; select the exact owner/account. Never fall back to despairarc000 for construction writes, another connected identity, cached credentials or an unverified default. Connector IDs are session-specific capabilities and should be discovered rather than treated as portable credentials. Local gh authentication was not configured in the prior workspace; prefer connected GitHub tools. A new runner may have different setup.

If permission/runtime/network/database access is unavailable, record one exact blocker and continue independent permitted work. Repository knowledge cannot supply missing external authorization; do not ask for passwords or commit secrets. Starter Auth is plumbing, not verified role authorization or business RLS.
