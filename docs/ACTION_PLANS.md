# Action Plans for Security-Sensitive Work

**Status: plans only. Nothing here has been executed.** Every step that rewrites history, force-pushes, renames, archives, deletes, rotates a secret, or alters a team document needs your explicit approval at that moment. No credential value or student ID number appears in this document.

## 1. Student-ID redaction

### Inventory (locations only)

| Location | Affects |
|---|---|
| `enterprise-network-security-lab`: both PDFs (cover pages) | five team members |
| `Secure-Enterprise-Network-Infrastructure`: Milestone 2 PDF | five team members |
| `DES-Encryption-in-CBC-Mode`: `SecurityProj.zip` (source header comment) | three group members |
| `Employee-Attrition-Prediction-Machine-Learning-Classification`: notebook comment | the owner |
| Thesis LaTeX repository: repository name, a comment in `bachelor.tex`, a register file | the owner |

### Sequence
1. **Notify every affected teammate first** (network team: four teammates; DES group: two). Suggested message: "Our public coursework repositories show student ID numbers on report cover pages. I plan to replace the PDFs with versions that remove the ID column and, if you agree, remove older copies from Git history. Please reply if you object or want to review." Wait for replies; do not redact team documents before this.
2. **Choose a method per file.** Preferred: regenerate the PDF from its source (the Packet Tracer guide was converted from Markdown, so re-export with the ID column removed). Acceptable: a redaction tool that deletes the underlying text. Not acceptable: a black box drawn over text, which leaves the text extractable.
3. **Verify** locally with counts only: `pdftotext file.pdf - | grep -cE '[0-9]{8}'` should print `0`. Also check the PDF metadata and bookmarks.
4. **Ship through a pull request** per repository (never to `main` directly) and show you each diff.
5. **History:** the old PDFs and ZIP remain in Git history, in forks and in cached views, so step 4 alone does not remove them. See section 3.
6. **DES (Patch 08 is on hold):** do not publish the extracted source as the cleaned project until the original ZIP and its history are handled. The ZIP also bundles about 1,300 `.venv` and IDE files. Proposed order: teammates agree, then history cleanup removes the old ZIP, then add the cleaned source with the group-attribution README (educational limitations preserved: no key schedule, fixed IV, zero padding, encryption only, DES obsolete).
7. Edit the single comments in the notebook and `bachelor.tex` in their own small PRs.

## 2. Thesis repository rename

- Current name embeds the student ID; proposed: **`bachelor-thesis-secure-mpc-ai`** (alternative `secure-mpc-bachelor-thesis`).
- Before: tell any collaborator or supervisor with the old URL; check whether Overleaf is synced by name; decide whether to make the repository private until submission (Settings, "Change visibility").
- Do: Settings, "Repository name", rename. GitHub then redirects the old web and Git URLs.
- After: `git remote set-url origin <new-url>` in every clone; reconnect Overleaf; confirm links in `graduation-mpc-ff` docs (the thesis repository is not linked from the profile README).
- The rename does not remove the ID from file contents or history (see section 1).
- Optional, separate decision: `Bi-Directional-Chat-Application-with-TCP-Analysis` could be renamed (for example `java-tcp-chat`) because it contains no traffic analysis; GitHub redirects apply.

## 3. Git history cleanup (rewrite)

Needed only for: the old Supabase key in `Library-Management-System` (after the project owner has reviewed RLS and decided on rotation), the old PDFs, the DES ZIP, and ID occurrences in the thesis repository. Each repository is a separate approval.

1. **Prerequisites.** Key rotation or deactivation (if applicable) is done first; rotation is what removes the key risk. Teammates have been notified for team repositories.
2. **Backup.** `git clone --mirror <repo-url> backup.git` and keep it private.
3. **Rewrite** in a fresh clone with `git filter-repo`:
   - paths: `git filter-repo --path <file> --invert-paths`
   - text values: `git filter-repo --replace-text rules.txt`, where `rules.txt` lists the old values and stays outside every repository and out of terminal logs and chat.
4. **Inspect** the result locally (`git log --stat`, tests, `pdftotext` counts) before pushing.
5. **Force-push (explicit approval each time)** with `git push --force-with-lease`, temporarily relaxing branch protection if enabled, then restoring it. Never on a repository with open teammate work you have not coordinated.
6. **Afterwards:** collaborators must re-clone (or `git fetch` and hard-reset). Open PRs against old commits break. Forks keep the old objects.
7. **Cached data:** GitHub can still serve old commits by SHA until garbage-collected; request removal through GitHub Support (for sensitive data) with the repository and commit SHAs. This is part of why rotation comes first.
8. **Small repositories first:** `Library-Management-System` has only 4 commits and is the simplest.

## 4. Full-history secret scanning

The Phase 2 scan covered current file contents with patterns, plus the complete history of one repository. A complete job covers every commit in every repository.

1. **Tools** (to install, not yet done): gitleaks and trufflehog.
2. **Mirror-clone every repository** you own (36 public plus the private one; private ones need your own authenticated access, and I have not inspected `support-smartflow`).
3. **Scan with output redaction on**, for example `gitleaks detect --source <repo> --redact --report-format json --report-path <file>` and, optionally, `trufflehog git file://<repo> --redact`. Keep reports out of repositories and chats because they contain locations and fingerprints.
4. **Triage** each finding: real or false positive; if real, determine the provider and scope, revoke or rotate at the provider, then decide on history cleanup (section 3).
5. **Prevent recurrence:** enable GitHub secret scanning and push protection (Settings, Code security) on every repository, add a `.gitignore` with `.env`, and consider a pre-commit hook running gitleaks.
6. **Already known:** one confirmed hit (Supabase `anon`-role key in `Library-Management-System`); see `docs/supabase-key-migration/` for the RLS check guide and the local migration script.
