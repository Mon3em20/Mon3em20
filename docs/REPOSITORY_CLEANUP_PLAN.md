# Repository Cleanup Plan (Phase 2)

Companion documents: [`DUPLICATE_REPOSITORY_ANALYSIS.md`](DUPLICATE_REPOSITORY_ANALYSIS.md), [`SECURITY_HYGIENE_REPORT.md`](SECURITY_HYGIENE_REPORT.md), [`ACTION_PLANS.md`](ACTION_PLANS.md) (ID redaction, rename, history cleanup, full-history scanning) and [`supabase-key-migration/`](supabase-key-migration/) (RLS check guide and local migration script).

## Status after approvals

Nothing has been merged. Each approved patch is an open pull request on its own branch; `main` was never pushed to.

| Patch | Repository | Pull request |
|---|---|---|
| 01 | `enterprise-network-security-lab` | [#1](https://github.com/Mon3em20/enterprise-network-security-lab/pull/1) |
| 02 | `Secure-Enterprise-Network-Infrastructure` | [#1](https://github.com/Mon3em20/Secure-Enterprise-Network-Infrastructure/pull/1) |
| 03 | `owasp-juice-shop-security-testing` | [#1](https://github.com/Mon3em20/owasp-juice-shop-security-testing/pull/1) |
| 04 | `digital-forensics-investigations` | [#1](https://github.com/Mon3em20/digital-forensics-investigations/pull/1) |
| 05 | `graduation-mpc-ff` | [#1](https://github.com/Mon3em20/graduation-mpc-ff/pull/1) |
| 06 | `Bi-Directional-Chat-Application-with-TCP-Analysis` | [#1](https://github.com/Mon3em20/Bi-Directional-Chat-Application-with-TCP-Analysis/pull/1) |
| 07 | `RSA-Encryption-and-Decryption-Implementation` | [#1](https://github.com/Mon3em20/RSA-Encryption-and-Decryption-Implementation/pull/1) |
| 08 | `DES-Encryption-in-CBC-Mode` | **on hold** (the original ZIP and its history still contain student identifiers) |
| 09 | `Library-Management-System` | [#1](https://github.com/Mon3em20/Library-Management-System/pull/1) (`.env` untracking, `.gitignore`, `.env.example` only) |
| 10 | `ImageReveal` | [#2](https://github.com/Mon3em20/ImageReveal/pull/2) |

Not done, by instruction: no history rewrite, force-push, key rotation, archiving, deletion, renaming, PDF redaction or metadata change. The `settings.py` migration is a local script, not a PR, so that no diff shows the old value. Patch 05 was strengthened with extra limitations after the original patch file was drafted; the file in `proposed-fixes/` matches the pull request.

## 1. Proposed documentation fixes (separate diffs)

Each file in [`proposed-fixes/`](proposed-fixes/) is a `git format-patch` mail for one repository, one commit each. All ten were checked with `git apply --check` against fresh clones of the current `main` of the target repository and apply cleanly. They were built on local branches in scratch clones that are not pushed.

| # | Repository | Change | Evidence it rests on |
|---|---|---|---|
| 01 | `enterprise-network-security-lab` | Add team members, course, the owner-written contribution list, milestone descriptions; fix truncated report section; label as simulated team coursework | Both PDFs and the other repo's README |
| 02 | `Secure-Enterprise-Network-Infrastructure` | Point to the primary repo; replace the structure block that lists nonexistent folders | Repository tree |
| 03 | `owasp-juice-shop-security-testing` | Remove the nonexistent `screenshots/` tree and close the code fence | Repository tree (only README and `reports/`) |
| 04 | `digital-forensics-investigations` | Add the missing closing code fence | README end |
| 05 | `graduation-mpc-ff` | Record the single-seed matched-size Secure BP run with its limitations; remove the "execution pending" statement | `docs/experimental-results/secure-bp-full-run/`, source hash matches the manifest, plaintext seed-42 values match `bp.csv` |
| 06 | `Bi-Directional-Chat-Application-with-TCP-Analysis` | Add a README describing the actual code; state that it contains no traffic analysis | Source files |
| 07 | `RSA-Encryption-and-Decryption-Implementation` | Add a README with educational and security limitations | `src/RSA.java` |
| 08 | `DES-Encryption-in-CBC-Mode` | Extract `cpc.py` from the ZIP (student IDs removed), rewrite the README to what the code does | ZIP contents, `cpc.py` |
| 09 | `Library-Management-System` | Add `.gitignore` and `.env.example`; untrack the empty `.env` (the `settings.py` change is manual, see the security report) | Git history |
| 10 | `ImageReveal` | Stop tracking `node_modules` and `.idea`; extend `.gitignore` | Repository tree |

Findings worth knowing about because they changed the wording:
- **DES** is group coursework (three members listed in the source) and the code has **no key schedule**: all 16 round keys are one fixed constant, the IV is all zeros, padding is zero bits, and there is no decryption. The old README ("key scheduling", "padding and IV chaining for security") overstated it. I made the same correction in the profile README.
- **Thesis README**: the repository's own documents record a completed single-seed run of the matched-size model, while the README said it was pending. Patch 05 states it conservatively. The raw log and inputs are not in the repository, so the numbers rest on the written report.
- **TCP chat**: the repository contains no traffic analysis, and the client has a hard-coded, malformed IP address.

To apply one patch after approval (example for `01`):

```bash
git clone https://github.com/Mon3em20/enterprise-network-security-lab
cd enterprise-network-security-lab
git switch -c docs/team-and-contribution
git am path/to/docs/proposed-fixes/01-enterprise-network-security-lab-readme.patch
git push -u origin docs/team-and-contribution   # then review a pull request; do not push to main
```

## 2. Proposed repository metadata (not applied)

The current description and topic values could not be read from this environment, so these are proposals to review. GitHub limits descriptions to 350 characters and topics to lowercase letters, numbers and hyphens (up to 20).

| Repository | Proposed description | Proposed topics |
|---|---|---|
| `offensive-security-labs` | Authorized educational lab write-ups: web recon, directory enumeration, MS17-010, Tomcat WAR deployment, Linux privilege escalation, cron/PATH hijacking and an Active Directory attack chain. | `offensive-security`, `penetration-testing`, `active-directory`, `privilege-escalation`, `kali-linux`, `tryhackme`, `writeups` |
| `owasp-juice-shop-security-testing` | Controlled assessment of OWASP Juice Shop covering XSS, SQL injection, CSRF, SSRF, CORS and authentication weaknesses, with two PDF reports. | `owasp`, `juice-shop`, `web-security`, `burp-suite`, `appsec`, `xss`, `sql-injection` |
| `digital-forensics-investigations` | Windows memory forensics and malicious-PCAP analysis with Volatility 3, FTK Imager, Wireshark and NetworkMiner (lab environments, two PDF reports). | `digital-forensics`, `dfir`, `memory-forensics`, `volatility3`, `wireshark`, `pcap-analysis` |
| `enterprise-network-security-lab` | Team coursework: simulated multi-branch Cisco Packet Tracer network with OSPF, DMZ, TACACS+, SSH v2, port security, ACLs, IPsec VPN and SYSLOG. Not a production deployment. | `network-security`, `cisco`, `packet-tracer`, `ospf`, `ipsec`, `tacacs`, `acl` |
| `iam-business-continuity-planning` | Academic IAM risk assessment and continuity design using NIST SP 800-30: BIA, RTO/RPO, backup and disaster-recovery planning. Design only, not deployed. | `grc`, `iam`, `nist-800-30`, `business-continuity`, `disaster-recovery`, `active-directory` |
| `graduation-mpc-ff` | Bachelor thesis research on secure MPC for privacy-preserving training: plaintext BP/FF baselines and bounded Secure BP experiments in MP-SPDZ. Secure Forward-Forward is future work. | `secure-multiparty-computation`, `mp-spdz`, `privacy-preserving-machine-learning`, `forward-forward`, `research` |

Recommended pinned repositories, unchanged from the first review: the six above, in that order.

## 3. Thesis repository name and privacy

Current name: `-Abdelmonem-sayed_<student-ID>-Biologically-Plausible-Secure-Multi-Party-Computation-thesis` (leading hyphen, embeds the student ID).

**Recommended name: `bachelor-thesis-secure-mpc-ai`** (alternative: `secure-mpc-bachelor-thesis`), which pairs with `graduation-mpc-ff`.

Things a rename affects:
- GitHub redirects the old web and Git URLs, so existing clones keep working until the old name is reused by anyone; update local remotes with `git remote set-url origin <new-url>`.
- The thesis repository contains an Overleaf template screenshot; if it is synced with Overleaf, reconnect it after renaming.
- No other repository in the account, and not the profile README, links to the old name. `graduation-mpc-ff` is mentioned in the thesis repository's knowledge base (that direction is unaffected).
- A rename does **not** remove the ID from the file contents (`bachelor.tex` comment, one register file) or from Git history; it also remains in the old URL until redirects are dropped. The privacy follow-ups in the security report apply, and you may prefer to keep the repository private until the thesis is submitted.

## 4. Recommended clean organization

- **Pinned (6):** the six cybersecurity repositories above.
- **Keep, secondary:** `emotion-classification-distilbert-bilstm`, `deep-learning-image-captioning`, `Employee-Attrition-Data-Analysis-Preparation`, `Employee-Attrition-Prediction-Machine-Learning-Classification`, `DES-Encryption-in-CBC-Mode`, `RSA-Encryption-and-Decryption-Implementation`, `Bi-Directional-Chat-Application-with-TCP-Analysis`, `smart-attendance-tracking-agile-project`, `portfolio`, `Gamified-Personalizable-Educational-Platform`, `CTF-2026-GIU`.
- **Archive candidates (after the steps in the duplicate analysis):** `Secure-Enterprise-Network-Infrastructure`, `html-css-js-portofolio-tutorial`, `AttriPredict`, `Gamified-Personalizable-Educational-Platform.`, `next-platform-starter`.
- **Empty or stub (your call: delete or archive):** `sw`, `Gamified-Personalize-Educational-Platform`, `myproject`, `realstates`.
- **Dependent on content decisions:** the profile README (this repository's branch) also changed the DES wording and removed teammate-owned repositories, per your instructions.

## 5. Approval checklist

Tick what you approve; I will do only the ticked items, one repository branch at a time, never touching `main` directly.

**A. Safe documentation fixes** (create a branch in the target repository, push the branch, open a pull request for you to merge)
- [ ] A1 Patch 01, network primary README
- [ ] A2 Patch 02, duplicate network README pointer
- [ ] A3 Patch 03, Juice Shop README
- [ ] A4 Patch 04, Digital Forensics code fence
- [ ] A5 Patch 05, thesis-code README status
- [ ] A6 Patch 06, TCP chat README
- [ ] A7 Patch 07, RSA README
- [ ] A8 Patch 08, DES README and extracted source
- [ ] A9 READMEs for `portfolio` and the two attrition repositories (not yet drafted)

**B. Repository metadata updates**
- [ ] B1 Apply the descriptions and topics in section 2 (as proposed, or edited by you)
- [ ] B2 Update the pinned repositories on your profile (a manual step in the GitHub UI)

**C. Consolidation and archiving** (each is a settings change in GitHub, reversible by unarchiving, except deletion)
- [ ] C1 Archive `Secure-Enterprise-Network-Infrastructure` (after A1 and A2)
- [ ] C2 Execute the Gamified plan (copy files into the canonical repository, then archive the dotted variant)
- [ ] C3 Delete or archive the empty `Gamified-Personalize-Educational-Platform`
- [ ] C4 Archive `html-css-js-portofolio-tutorial`
- [ ] C5 Archive `AttriPredict`
- [ ] C6 Decide on `sw`, `myproject`, `realstates`, `next-platform-starter`

**D. Security-sensitive operations** (do first; some are on your side of the fence)
- [ ] D1 Check Row Level Security and access logs on the Supabase project (yours to do)
- [ ] D2 Rotate the Supabase keys (yours to do)
- [ ] D3 Make the manual `config/settings.py` change, then apply patch 09
- [ ] D4 Rewrite `Library-Management-System` history to remove the old value (only after D2; force-push)
- [ ] D5 Apply patch 10 (`ImageReveal`) and untrack `node_modules`, `.idea`, `.class` and `.DS_Store` in the other repositories
- [ ] D6 Redact student ID numbers in the two network PDFs after telling your teammates
- [ ] D7 Rename the thesis repository to `bachelor-thesis-secure-mpc-ai` (or keep it private until submission)
- [ ] D8 Enable GitHub secret scanning and push protection; scan full history with gitleaks or trufflehog
