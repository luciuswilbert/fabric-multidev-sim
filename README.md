# fabric-multidev-sim

Simulation of a four-developer Microsoft Fabric project with GitHub (personal account; the SRKK org blocks unapproved tokens).

| Branch | Fabric workspace | Owner |
|---|---|---|
| `main` | `WS_Dev` (update-only) | Lead |
| `feature/oracle` | `WS_Feat_Oracle` | Dev 1 |
| `feature/salesforce` | `WS_Feat_Salesforce` | Dev 2 |
| `feature/sqlserver` | `WS_Feat_SqlServer` | Dev 3 |
| `feature/files` | `WS_Feat_Files` | Dev 4 |

Data lives in `WS_Data_Dev` → `LH_Bronze` (not in Git), one schema per source.

- `fabric/` is the folder every code workspace syncs with. Don't edit it by hand; commit from Fabric.
- `mock-data/` holds the CSVs that were uploaded to `LH_Bronze/Files/landing/<source>/`.

Rules: no direct commits to `main`; one feature branch per developer; merge only through a PR
that passes `pr-check` and is up to date with `main`.

Solo run: one GitHub account plays every role, so required approvals are set to 0.
In a real team `main` would require 1 approval plus CODEOWNERS review.
