# Repository Audit — Mon3em20

Audit date: 2026-11-22. Method: shallow clones of 38 repositories (36 public, 1 private not inspected, 1 empty), reading READMEs, directory trees and key source files. Nothing was deleted, archived, renamed, made private or merged.

## 1. Strongest projects (used in the README)

| Rank | Repository | Verified contents |
|---|---|---|
| 1 | `offensive-security-labs` | 7 lab folders, each with README and PDF report |
| 2 | `owasp-juice-shop-security-testing` | 2 PDF reports |
| 3 | `digital-forensics-investigations` | 2 PDF reports (memory, network) |
| 4 | `enterprise-network-security-lab` | 2 PDF reports (chosen as primary network project) |
| 5 | `graduation-mpc-ff` | 151 files: code, tests, configs, logs, reports |
| 6 | `iam-business-continuity-planning` | README and 1 PDF report |

## 2. Duplicates and overlap

- **`enterprise-network-security-lab` vs `Secure-Enterprise-Network-Infrastructure`**: both contain `Enterprise_Network_Security_Architecture_Report.pdf.pdf` (byte-identical, same MD5). The `lab` repo additionally has `complete-network-security-report.pdf` and covers DMZ and IPS, so it was chosen as the single featured project. The `Secure-…` repo is the only one stating team members (5), course and personal contribution. Recommendation: copy the team and contribution statement into the `lab` README; then archive `Secure-Enterprise-Network-Infrastructure` yourself if desired.
- **Gamified-Personalizable-Educational-Platform** exists in three variants: `…Platform` (ERD.zip, schema.docx), `…Platform.` with a trailing dot (ERD.drawio, schema PDF), and `Gamified-Personalize-Educational-Platform` (empty). Consolidate into one repository.
- **`portfolio` vs `html-css-js-portofolio-tutorial`**: same assets, the second is a tutorial copy.
- **Employee-Attrition** (3 repos: `AttriPredict`, `…Data-Analysis-Preparation`, `…Prediction…`) share one dataset; `AttriPredict` and `…Data-Analysis-Preparation` ship the same CSV.

## 3. Empty or unfinished

| Repository | State |
|---|---|
| `sw` | Completely empty |
| `Gamified-Personalize-Educational-Platform` | Completely empty |
| `myproject` | README reads "this is test repo" |
| `realstates` | README is a title only |
| `Tree-Search-and-Conversion` | one `.asm` file, no README |
| `next-platform-starter` | Unmodified Netlify template fork |

## 4. Broken links, stale or inaccurate documentation

- **Profile `snake.yml` has never run.** It is at the repository root, but GitHub only runs workflows from `.github/workflows/`. Evidence: 0 workflow runs and no `output` branch (only `main`). Fix: move to `.github/workflows/snake.yml` (done on the redesign branch as a separate commit). The README does not embed the snake until `output` exists.
- `owasp-juice-shop-security-testing` README lists a `screenshots/` folder with 8 images that does not exist.
- `Secure-Enterprise-Network-Infrastructure` README lists `/screenshots`, `/configurations`, `/topology`; only the PDF exists.
- `digital-forensics-investigations` README structure block is missing its closing code fence.
- `graduation-mpc-ff` README is **stale versus its own docs**: README says full-size `bp_matched` execution is "pending", but `docs/experimental-results/secure-bp-full-run/` and the thesis repo's `CURRENT_RESEARCH_STATUS.md` record a completed single-seed (42) full-size Secure BP run with caveats (one seed, localhost only, unresolved truncation warning). The profile README deliberately describes only the bounded prototype. **Decision for you:** update the research README and, if you want it, mention the single-seed run with its caveats.
- `Bi-Directional-Chat-Application-with-TCP-Analysis`: repository has no README and contains no traffic-analysis artefacts (only client/server source), so "traffic analysis" is unverified and was not claimed.
- `RSA-Encryption-and-Decryption-Implementation`: README is only the title. Source is textbook RSA with no padding; included in the collapsed section with that caveat.
- `DES-Encryption-in-CBC-Mode`: code only inside `SecurityProj.zip`, which contains `.idea/` and `.venv/`. Extract the source into the repo.
- `CTF-2026-GIU`: no date or challenge write-ups; certificate and team photo are present.

## 5. Security hygiene

- `Library-Management-System`: the tracked `.env` is empty, but `config/settings.py` hard-codes a Supabase URL and an `anon`-role key (details and remediation in `SECURITY_HYGIENE_REPORT.md`; this corrects an earlier version of this audit).
- `ImageReveal` commits `node_modules/`; several repos commit `.idea/` and compiled `.class` files.
- The thesis LaTeX repository name embeds a student ID number (`-Abdelmonem-sayed_<student-ID>-…`). Consider renaming. It was not linked in the README.
- `support-smartflow` is private (not inspected).

## 6. Recommended descriptions and topics

| Repository | Description | Topics |
|---|---|---|
| `offensive-security-labs` | Authorized educational offensive-security lab write-ups: web, Linux privilege escalation and Active Directory attack chains | `offensive-security` `penetration-testing` `active-directory` `privilege-escalation` `kali-linux` `tryhackme` `writeups` |
| `owasp-juice-shop-security-testing` | Controlled web application security assessment of OWASP Juice Shop with PDF reports | `owasp` `juice-shop` `web-security` `burp-suite` `xss` `sql-injection` `appsec` |
| `digital-forensics-investigations` | Memory and network forensics investigations with Volatility 3, Wireshark and NetworkMiner | `digital-forensics` `dfir` `volatility3` `wireshark` `memory-forensics` `pcap-analysis` |
| `enterprise-network-security-lab` | Academic Cisco Packet Tracer enterprise network: OSPF, DMZ, TACACS+, IPsec VPN, ACLs, SYSLOG (simulated, team coursework) | `network-security` `cisco` `packet-tracer` `ospf` `ipsec` `tacacs` `acl` |
| `iam-business-continuity-planning` | Academic IAM risk assessment and business continuity design using NIST SP 800-30 | `grc` `iam` `nist-800-30` `business-continuity` `disaster-recovery` `active-directory` |
| `graduation-mpc-ff` | Bachelor thesis research: secure MPC for privacy-preserving training; plaintext BP/FF baselines and a bounded Secure BP prototype | `secure-multiparty-computation` `mp-spdz` `privacy-preserving-machine-learning` `forward-forward` `research` |

## 7. Recommended six pinned repositories

1. `offensive-security-labs`
2. `owasp-juice-shop-security-testing`
3. `digital-forensics-investigations`
4. `enterprise-network-security-lab`
5. `graduation-mpc-ff`
6. `iam-business-continuity-planning`

## 8. Portfolio website (`Mon3em20/portfolio`) cross-check — no changes made

Source files: `index.html`, `script.js`, `style.css`, `mediaqueries.css`, `assets/`.

| Issue | Evidence | Exact fix |
|---|---|---|
| Tagline "Future Ethical Hacker" | `index.html` line ~58 | Use "Cybersecurity Student \| Offensive & Application Security" |
| LinkedIn URL differs from profile | `…/in/monem-somida-9739b2312/` (lines ~67, ~454) | Replace with `https://www.linkedin.com/in/abdelmonem-sayed-somida-9739b2312` |
| CV button path likely broken | `window.open('../assets/Abdelmonem_Sayed_CV.pdf')` in `index.html`; `assets/` is at repo root next to `index.html` | Change to `assets/Abdelmonem_Sayed_CV.pdf` (also confirm the CV is current) |
| WhatsApp link malformed and exposes a phone number | `https://wa.me/01003632099` (wa.me requires international format without a leading 0) | Remove it, or use the international format only if you want it public |
| Projects not security-focused | Page lists Attack on Titan, supermarket GUI, etc.; none of the six featured security repos | Add the six featured repositories first |
| Third-party / external links | `Pedro4O4/masr7.git`, a Google Drive link | Confirm they are intended and accessible |

## 9. Limits of this audit

External links (LinkedIn, TryHackMe, third-party repositories) could not be fetched from this environment, so they were checked only for format; the two teammate-owned GitHub repositories and the Mini-Jira repository were confirmed to exist via `git ls-remote`/clone. Teammate-owned repositories were removed from the README (see `REPOSITORY_CLEANUP_PLAN.md`). PDF contents were not read; claims come from READMEs and your brief.
