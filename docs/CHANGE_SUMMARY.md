# Change Summary

## What changed

- **`README.md`**: rewritten as a dark cybersecurity portfolio: hero banner, positioning line, contact badges, clickable navigation, About, five focus areas, six featured projects, experience, research, technical arsenal, competitions, a collapsed "Other Technical Projects & Coursework" section, and a compact contact block. No JavaScript, CSS injection, iframes or third-party widgets; the only external images are shields.io contact badges.
- **`assets/cybersecurity-profile-header.svg`**: original 1280×420 banner (shield, circuit traces, network nodes, terminal strip) in the requested palette. Static, no scripts, no external fonts or images, with `<title>`/`<desc>` for accessibility.
- **`docs/REPOSITORY_AUDIT.md`**: full audit and recommendations (nothing in other repositories was modified).
- **`snake.yml`** moved to `.github/workflows/snake.yml` in a separate commit (see below).

## Why (key editorial decisions)

- **Six featured projects match your priority list.** Network security is a single card (`enterprise-network-security-lab`) because both network repos share an identical report.
- **Removed from the old README:** the AI/ML projects as featured items, and "Mini-Jira on AWS" (a teammate's repository); the other teammate-owned links were removed as well.
- **Research status is conservative.** Only Stage A and Stage B (bounded prototype) are claimed. Secure FF and SNNs are stated as not implemented. Results from separate runs are not mixed, and no performance numbers are quoted.
- **Team and scope labels** appear on the labs, the network project, the CTF (team score) and the IAM project (not deployed).
- **Fixed anchors:** headings are plain text so GitHub's auto-generated anchors are predictable; all eight internal links were checked.

## Follow-up decisions applied

The README stays conservative on the research (bounded prototype only). The snake workflow move is a separate commit and the README has no snake until the generated SVGs exist. Mini-Jira and the two other teammate-owned repositories were removed from the README, the certificate link was removed, and C++ stays in the skills list without any project claim. The DES entry was corrected after reading its source. Phase 2 findings, proposed patches and the approval checklist are in `REPOSITORY_CLEANUP_PLAN.md`, `SECURITY_HYGIENE_REPORT.md` and `DUPLICATE_REPOSITORY_ANALYSIS.md`.
