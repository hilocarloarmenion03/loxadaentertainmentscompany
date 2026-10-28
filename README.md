# Loxada Entertainments Company

Construction knowledge hub for all four systems, and the home of the Superadmin implementation.

Start with [START_HERE.md](START_HERE.md). Agents read [AGENTS.md](AGENTS.md).

| Location | Responsibility |
| --- | --- |
| despairarc000/loxadaentertainments | Existing research, information and business knowledge; upstream reference |
| This repository | Construction ICM, Graphify, Vault, shared interface contracts, integration evidence, Superadmin application |
| lozadatech01 | Manga & Light Novel application and its own deployment/database |
| hebratech01 | Anime application and its own deployment/database |
| padregandatech01 | Merchandise application and its own deployment/database |

Exactly three operating departments and one Owner governance/BI service. Department code is not placed in this repository.

## Navigation

```sh
python3 tools/nav.py status
python3 tools/nav.py route "merch invoice acceptance"
python3 tools/nav.py spec R-A-13
python3 tools/nav.py graph owner
python3 tools/nav.py ready
python3 tools/nav.py doctor
python3 -m unittest discover -s tests -v
```

Python3.11+ standard library only; navigation works offline. No hosted knowledge service, npm package, paid API, chat memory or copied local database is needed. The full pinned v1.0 baseline is included for offline reference; use focused retrieval rather than loading it all.

The user is setting up the Vercel/Supabase starters. Superadmin source is reserved under apps/superadmin; this bootstrap does not create an application or claim production readiness. Existing department repository names and resources are recorded as observations, not permission to overwrite them. All scheduled tasks remain paused.
