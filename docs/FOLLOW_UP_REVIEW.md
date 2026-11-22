# Follow-up Review

Covers the seven decisions on the redesign. Nothing outside the profile repository was modified; the other repositories were only read from local clones.

## 1. Secure BP full-size run (thesis repository `graduation-mpc-ff`)

### What was verified

| Check | Result |
|---|---|
| Source `mpc/programs/bp/bp_matched_matrix.mpc` is committed (2026-11-16) | Yes; its SHA-256 equals the digest in `integrity_manifest.txt` (`8134dd8d…83fd`) |
| Program header matches the report | Yes: 784-128-128-10, 5,000/1,000/1,000 MNIST, five epochs, 39 batches of 128 plus one of 8, SGD 0.05, Rep3 Ring 64-bit, `sfix(16,31)` |
| Plain BP seed-42 reference in `results/baselines/bp.csv` | Matches the report: train loss 2.2747 / 2.1616 / 1.8416 / 1.3058 / 0.9092, validation 76.6 % |
| Secure BP metrics (loss 0.908951, test 772/1,000, 933.263 s, 5,224.49 MB, 8,928,348 rounds) | Present **only in the written reports and `results.csv`**. The raw `full.log`, the verified input bundle and `verification_summary.json` live under `~/secure-bp-runs/` on your machine and are **not in the repository**, so a third party cannot re-derive them |
| Truncation warning (domain needs ≥ 103 bits) | Documented as unresolved in `OPEN_ISSUES.md` (priority High); quoted from the log, not independently visible |
| Other full-size attempts in the repo | Not successful and not to be mixed in: `diagnostic_fullarch_seed42_20261113` ended with exit status 1 (a fatal TruncPr communication error after the 600 s timeout), and `secure_bp_matched_seed42.log` is only a compilation log (about 10.7 M lines, no result) |
| Repo `README.md` / `docs/reports/progress.md` | Still say full-size execution is "pending"; they do not mention the completed run |

### Conclusion

A single completed seed-42 full-size run is credibly documented and internally consistent (source hash, configuration and plaintext reference agree). Its secure-side numbers are self-reported evidence until the log and input bundle are archived in the repository. It must not be described as multi-seed, benchmarked, production-scale or an improvement over plaintext training. The profile README stays conservative (bounded prototype only).

### Recommended wording for a separate research update

Use only if the raw log and bundle are archived first (or state that they are held offline).

> **Secure BP, full-size configuration (single run).** One three-party Secure Backpropagation run (MP-SPDZ v0.4.4, Rep3 Ring, 64-bit ring, `sfix(16,31)`, semi-honest honest-majority, all parties on localhost) trained a 784-128-128-10 network on a 5,000/1,000/1,000 MNIST subset for five epochs with seed 42, reaching 77.2 % test accuracy (772/1,000), matching the plaintext seed-42 reference (77.2 %). MP-SPDZ reported 933.3 s and 5.2 GB of total communication across parties. **Limitations:** a single seed with no variance estimate; localhost execution that says nothing about network performance; MP-SPDZ time and wall-clock time cover different scopes; the log reports that the computation domain is too small for low-round truncation (≥ 103 bits needed), whose numerical and security impact is unresolved. This is a feasibility result, not a benchmark and not production-scale secure training. Secure Forward-Forward is not yet implemented.

Suggested repository actions (yours to approve): update the thesis-code README status; add the raw log, hashes and metadata under `results/mpc/bp/`; and do not add the profile claim until that is done.

## 2. Snake workflow

- The workflow now lives at `.github/workflows/snake.yml` in its own commit; content is unchanged.
- Rechecked: valid YAML; triggers are the daily schedule, manual dispatch and pushes to `main`; `contents: write` is set; `Platane/snk@v3` and `crazy-max/ghaction-github-pages@v4` both resolve to existing tags.
- Scheduled workflows run only from the default branch, so nothing happens until the branch is merged. The README intentionally has no snake.
- After merging: Actions → "Generate Snake Animation" → Run workflow. Then confirm an `output` branch exists containing `github-contribution-grid-snake.svg` and `github-contribution-grid-snake-dark.svg` (open them via `https://raw.githubusercontent.com/Mon3em20/Mon3em20/output/github-contribution-grid-snake-dark.svg`). Only then add:

```html
<img src="https://raw.githubusercontent.com/Mon3em20/Mon3em20/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Contribution graph animation" />
```

## 3. `.env` audit of `Library-Management-System`

Method: full clone, then inspection of every commit on every ref, printing only sizes and hashes; no file content was printed.

- The repository has 4 commits (all 2025-07-30). `.env` exists in the last three, always as the **empty blob** (`e69de29…`, 0 bytes). Commit "Remove .env from tracking" changed nothing in content.
- No assignment to a password, secret, API key or token appears anywhere in history, and the Python code does not read environment variables.
- **Conclusion: no credentials were ever committed. No rotation or history rewrite is needed.** My earlier audit wording ("commits a `.env` file", rotate anything real) overstated this and has been corrected in `REPOSITORY_AUDIT.md`.
- Remaining low-priority hygiene (needs your approval, not done): `git rm --cached .env`, add a `.gitignore` containing `.env`, and optionally add a `.env.example`.
- If a real secret had been found, remediation would be: revoke and rotate it at the provider first, then remove it from all history with `git filter-repo --path .env --invert-paths`, force-push, ask collaborators to re-clone, and check forks and caches.
- A scan of the other clones found no other tracked `.env` (only `.env.example` in Mini-Jira).

## 4. Thesis repository name

Current: `-Abdelmonem-sayed_13006494-Biologically-Plausible-Secure-Multi-Party-Computation-thesis` (starts with a hyphen, embeds the student ID).

Recommended: **`bachelor-thesis-secure-mpc-ai`** (alternative: `secure-mpc-bachelor-thesis`). It is lowercase, ID-free and pairs with `graduation-mpc-ff`.

Consequences of renaming:
- GitHub redirects the old web and Git URLs, so existing clones and links keep working, but the redirect ends if the old name is ever re-used.
- Update local remotes (`git remote set-url origin …`) and any Overleaf/GitHub sync, since the repo contains an Overleaf template screenshot; reconnect if it is linked by name.
- No file in your other repositories links to the old name; `graduation-mpc-ff` is mentioned in the thesis knowledge base, not the other way round. Nothing links to it from the profile README.
- **The rename does not remove the ID.** It still appears in `bachelor.tex` (a comment), `docs/registers/OPEN_QUESTIONS.md`, git history, and also in a comment in `Employee-Attrition-Prediction-Machine-Learning-Classification/Copy_of_Untitled3.ipynb`. Consider whether the thesis repository should be private until submission.

## 5. Mini-Jira and other teammate-owned repositories

Mini-Jira is removed. For consistency I also removed the Online Event Ticketing System and Enterprise HR Management System links from the collapsed section, because they are the same kind of teammate-owned repository. The commit history shows commits by an "abdelmonem" author in all three (Mini-Jira 10, Ticketing 48 plus 13 as "Abdelmonem Sayed Somida", HR 25), but none of them documents your individual role. Reconsider later with a documented contribution.

## 6. CTF certificate

The README no longer links the certificate. The entry is team participation ("Flag ela rob3", team score 1,500) and now includes the competition date, 12 May 2026, which the certificate states.

What `certificate.jpeg` contains: a GIU "Certificate of Participation" (participation only, not a ranking or award) naming "Abdelmonem Sayed" (not the full name), the competition date, the names, titles and handwritten signatures of two university officials, and the GIU logo. It is a phone photo of the paper, taken at an angle. It shows no ID number, address, email, phone number or QR code. **Review before promoting:** the signatures and the officials' names; whether you want your name public in that form; and `team.jpeg` in the same repository, which I did not describe and which may show other team members who have not agreed to be public.

## 7. C++

Kept in the Programming row without any proficiency claim or project claim. No C++ repository exists in the account (the repositories use Python, Java, JavaScript/TypeScript, MIPS assembly), which the README does not contradict.
