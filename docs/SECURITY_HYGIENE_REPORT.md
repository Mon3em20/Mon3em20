# Security Hygiene Report

Date: 2026-11-22. Method: read-only inspection of local clones. No secret value was printed, copied into a document, or placed in a patch. Nothing was pushed to, rewritten in, or changed in any other repository.

## Correction to an earlier finding

My previous review said `Library-Management-System` "never contained credentials". That was incomplete. The `.env` file was always empty, but a broader pattern scan found a hard-coded Supabase credential in `config/settings.py`. Details below.

## 1. `Library-Management-System`

### `.env`
Tracked in the last three of the repository's four commits. Every version in history is the empty blob (0 bytes). Commit `b09ce93` ("Remove .env from tracking") changed nothing in content. No secrets were ever in `.env`.

### Hard-coded Supabase credential (confirmed finding)

| Attribute | Value |
|---|---|
| File and lines | `config/settings.py`, lines 4 (`url`) and 5 (`key`); used by `create_client(url, key)` on line 7 |
| Introduced in | commit `36b1511` (2025-07-30); present in every later commit and in the current `main` |
| Type | JWT (HS256) whose claims are `exp`, `iat`, `iss`, `ref`, `role`; the `role` claim is **`anon`** |
| Validity | issued 2025-07-30, expires 2035-07-30 (still valid) |
| Issuer | Supabase project (project URL is on line 4) |

Assessment: an `anon` key is designed to be shipped in client applications, so by itself it is not a service-role/admin key and exposing it is lower severity than exposing a private key. It is still a credential bound to a specific project, and what a holder can do depends entirely on that project's Row Level Security (RLS) policies and table grants. If RLS is disabled or permissive on any table, anyone who finds the public key and URL can read or write that data. No service-role key was found in the repository.

Recommended remediation (in order; all need your approval and none was performed):
1. **Check the Supabase project now:** confirm RLS is enabled with restrictive policies on every table, and check logs for unexpected access. If the project is a throwaway, deleting it is the cleanest fix.
2. **Rotate the key:** regenerate or replace the project's API keys following Supabase's current dashboard procedure, so the committed value stops working. Rotation, not history cleanup, is what removes the risk.
3. **Stop hard-coding it:** apply this change by hand to `config/settings.py` (it cannot be shipped as a patch, because a diff would have to print the removed value):
   - add `import os` at the top;
   - replace the right-hand side of the `url` assignment (line 4) with `os.environ["SUPABASE_URL"]`;
   - replace the right-hand side of the `key` assignment (line 5) with `os.environ["SUPABASE_KEY"]`.
4. **Apply patch `09`** (`.gitignore`, `.env.example`, untrack the empty `.env`); then put the new values in a local, untracked `.env`.
5. **History cleanup (optional after rotation; requires explicit approval, rewrites history):** the repository has only 4 commits. With `git filter-repo`, remove or replace the value (for example `git filter-repo --replace-text <rules-file>` where the rules file lists the old value and is kept out of the repository), force-push, then ask any collaborators to re-clone. Forks, clones and caches that already copied the key are not cleaned by this; that is why rotation comes first.

## 2. Personal data in public files (student ID numbers)

| Where | What |
|---|---|
| `enterprise-network-security-lab` and `Secure-Enterprise-Network-Infrastructure` PDFs | cover pages list names and student ID numbers of all five team members (both reports) |
| thesis LaTeX repository | the repository name embeds the owner's ID; `bachelor.tex` has an ID in a comment; a register file mentions it |
| `DES-Encryption-in-CBC-Mode` | the source header (inside `SecurityProj.zip`) lists three members with IDs |
| `Employee-Attrition-Prediction-Machine-Learning-Classification` | an ID in a notebook comment |

Teammates' IDs are involved, so they should be told before action. Options: replace the PDFs with versions that blank the ID column (this needs the original source or a PDF redaction tool; do not use a visual overlay), and edit the comments. Patch `08` already removes IDs from the extracted DES source (the ZIP still contains them). Git history keeps old copies unless history is rewritten.

## 3. Tracked build, IDE and dependency artifacts (counts of tracked files)

| Repository | Artifacts |
|---|---|
| `course-booking-platform` | `node_modules/` (1,815 files), `.idea/` (10), `.iml` (2) |
| `AttackOnTitan` | `.class` (141), `.idea/` (72), `.iml` (21), `.DS_Store` (2) |
| `ImageReveal` | `node_modules/` (5), `.idea/` (6), `.iml` (1) |
| `Super-market-GUI-` | `.class` (12) |
| `Bi-Directional-Chat-Application-with-TCP-Analysis` | `.class` (3) |
| `RSA-Encryption-and-Decryption-Implementation` | `.class` (2), `.iml` (1) |
| `Multi-Core-Execution-System-Implementation` | `.iml` (1) |
| `DES-Encryption-in-CBC-Mode` | `.venv/` and `.idea/` inside `SecurityProj.zip` |

Patch `10` stops tracking `node_modules` and `.idea` in `ImageReveal` and extends its `.gitignore`. Untracking removes files from the repository, not from anyone's disk, and is reversible; it still needs your approval. For the others I recommend the same `.gitignore` plus `git rm -r --cached` once you confirm the files are not needed (the `.class` files in the chat and RSA repositories are rebuildable from source). `course-booking-platform` should also be checked for a root `.gitignore`.

## 4. What the pattern scan covered

Regular-expression scan of current file contents in the cloned repositories for AWS key IDs, GitHub, Slack, Google and OpenAI-style tokens, private-key headers, JWTs, quoted credential assignments and database URLs with passwords. The only hit was the Supabase JWT above. Not covered: the private `support-smartflow`; Git history for all repositories except `Library-Management-System` (fully reviewed); files over 2 MB and binaries; secrets in non-standard formats. Recommended next step (not run here, needs tool installation): scan every repository's full history with a dedicated scanner such as gitleaks or trufflehog, and enable GitHub secret scanning and push protection in each repository's security settings.

## 5. Other observations
- The Mini-Jira repository (owned by a teammate) tracks only `backend/.env.example`, which is the correct pattern.
- The DES and RSA repositories are educational and are labelled so in the README patches.
