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

See `docs/FOLLOW_UP_REVIEW.md` for evidence. In short: README stays conservative on the research (bounded prototype only) with recommended wording for a separate update; the snake workflow move stays a separate commit and the README has no snake until the SVGs exist; `Library-Management-System` never contained credentials; a thesis repo rename is recommended but not done; Mini-Jira and the two other teammate-owned repositories were removed from the README; the certificate link was removed and the CTF entry now shows the certificate-verified date; C++ remains in the skills list without any project claim.
