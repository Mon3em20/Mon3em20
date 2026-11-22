# Change Summary

## What changed

- **`README.md`**: rewritten as a dark cybersecurity portfolio: hero banner, positioning line, contact badges, clickable navigation, About, five focus areas, six featured projects, experience, research, technical arsenal, competitions, a collapsed "Other Technical Projects & Coursework" section, and a compact contact block. No JavaScript, CSS injection, iframes or third-party widgets; the only external images are shields.io contact badges.
- **`assets/cybersecurity-profile-header.svg`**: original 1280×420 banner (shield, circuit traces, network nodes, terminal strip) in the requested palette. Static, no scripts, no external fonts or images, with `<title>`/`<desc>` for accessibility.
- **`docs/REPOSITORY_AUDIT.md`**: full audit and recommendations (nothing in other repositories was modified).
- **`snake.yml`** moved to `.github/workflows/snake.yml` in a separate commit (see below).

## Why (key editorial decisions)

- **Six featured projects match your priority list.** Network security is a single card (`enterprise-network-security-lab`) because both network repos share an identical report.
- **Removed from the old README:** the AI/ML projects as featured items, and "Mini-Jira on AWS" as a featured card (a teammate's repository), demoted into the collapsed section and labelled as teammate-owned.
- **Research status is conservative.** Only Stage A and Stage B (bounded prototype) are claimed. Secure FF and SNNs are stated as not implemented. Results from separate runs are not mixed, and no performance numbers are quoted.
- **Team and scope labels** appear on the labs, the network project, the CTF (team score) and the IAM project (not deployed).
- **Fixed anchors:** headings are plain text so GitHub's auto-generated anchors are predictable; all eight internal links were checked.

## Needs your decision

1. **Research README is stale.** Your docs record a completed single-seed full-size Secure BP run. I did not feature it because you asked me not to mix runs. Tell me if you want it added with its caveats.
2. **Snake workflow**: it never ran because it was outside `.github/workflows/`. The move is committed separately; after merging, run the workflow once, confirm an `output` branch with the SVGs exists, and only then add the snake image to the README.
3. **Committed `.env` in `Library-Management-System`**; thesis repo name contains a student ID.
4. **Mini-Jira**: confirm your role before leaving it listed.
5. Confirm the certificate image is appropriate to link publicly.
6. C++ is listed because you provided it; no C++ repository was found in the account.
