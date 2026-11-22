# Duplicate Repository Analysis

Evidence comes from full or shallow clones, file hashes, commit histories and PDF text extraction (2026-11-22). Nothing was deleted, archived, renamed or merged, and nothing was pushed to any repository other than the redesign branch of this one.

## 1. Network security: `enterprise-network-security-lab` vs `Secure-Enterprise-Network-Infrastructure`

| Item | `enterprise-network-security-lab` | `Secure-Enterprise-Network-Infrastructure` |
|---|---|---|
| Files | README, `complete-network-security-report.pdf` (76 pp.), `Enterprise_Network_Security_Architecture_Report.pdf.pdf` (38 pp.) | README, the same 38-page PDF |
| Shared report | byte-identical (same MD5) | byte-identical |
| Report identity | 76 pp.: "Milestone 1" (Cisco Packet Tracer configuration guide, April 2026); 38 pp.: "Milestone 2: Network Expansion" (dated 13 May 2026) | Milestone 2 only |
| Team list | none in README | five members, course, instructor |
| Individual contribution | none | "My Contribution" list written by the repository owner |
| README accuracy | truncated: announces two reports but describes only one | lists `/screenshots`, `/configurations`, `/topology` that do not exist |
| Created | 2026-05-08, README updated 2026-05-20 | 2026-05-19 |

Content check against the PDFs: VLANs, IPsec VPN, port security and sticky MAC appear only in Milestone 2; DMZ, IPS and extended ACLs are mainly in Milestone 1. Both reports list the same five team members and neither assigns individual sections, so the only documented individual contribution is the owner-written list in the second repository's README.

**Decision: primary = `enterprise-network-security-lab`** (superset of documents). Proposed fixes:
- Patch `01`: copies the team list, course and instructor, and the owner's contribution list (attributed to its source README) into the primary README, fixes the truncated report section, states the work is simulated team coursework, and adds a related-repository note. No contribution was invented; the patch states that the reports do not assign individual sections.
- Patch `02`: adds a pointer to the primary repository in the duplicate and replaces its structure block with what actually exists.

**Archive plan for `Secure-Enterprise-Network-Infrastructure` (not executed):**
1. Review and merge patches `01` and `02` (approval items A1, A2).
2. Confirm no external page links to the duplicate (the profile README does not).
3. Archive it through Settings, then "Archive this repository". Archiving is reversible; deletion is not and is not recommended, because it holds the earlier contribution write-up.
4. Privacy follow-up (see the security report): both PDFs print student ID numbers for five people.

## 2. Gamified platform: three variants

| Repository | Files | History |
|---|---|---|
| `Gamified-Personalizable-Educational-Platform` | `ERD.zip` (contains one `ERD.drawio`), `schema.docx` | one commit, 2024-11-16 |
| `Gamified-Personalizable-Educational-Platform.` (trailing dot) | `ERD.drawio`, `Schema project.pdf` (4 pp.) | one commit, 2024-11-16 |
| `Gamified-Personalize-Educational-Platform` | empty (no commits) | none |

Evidence: the `ERD.drawio` inside the ZIP is byte-identical to the standalone `ERD.drawio` (same MD5). The PDF is an export of the DOCX (document title "schema.docx"; extracted text matches 99.7%). So variants 1 and 2 hold the same two documents in different formats, and variant 3 holds nothing. None contains code, a README or a team list.

**Canonical: `Gamified-Personalizable-Educational-Platform`** (clean name, the editable DOCX, and the ZIP). Consolidation plan, in order, each step needing approval:
1. Add to the canonical repository: the extracted `ERD.drawio` (identical), `Schema project.pdf`, and a README that describes the content accurately (relational schema and ERD for a gamified, personalized learning platform; learner, course, module, assessment, interaction-log and learning-path tables) with team information if you can supply it. Record in the README that the files originated in the dotted repository (commit `717607a`).
2. Archive the dotted variant after step 1 so its history is preserved.
3. Remove the empty variant (nothing to preserve) or archive it. Deletion is your decision.
No patch was prepared because the additions are binary files; the steps above need only normal Git operations.

## 3. Portfolio: `portfolio` vs `html-css-js-portofolio-tutorial`

- All 20 files in `assets/` are byte-identical in both repositories.
- `index.html` (portfolio) equals `inex.html` (tutorial copy, misspelled so it cannot be served as a site's index page).
- `style.css` is identical. `script.js` differs only in line endings (CRLF vs LF). `mediaqueries.css` in `portfolio` has one extra line (`position: sticky`), from the later commit "stiky nav for mobile".
- The tutorial copy nests everything under `portfolio/`, has a README that contains only its title, and was last pushed 2025-07-29 10:02 versus 11:51 for `portfolio`.

**Canonical: `portfolio`** (newer, correct filename, the sticky-navigation fix). It has no README; add one. **Recommendation for the tutorial copy:** it carries no unique content; after confirming nothing deploys from it (check Pages/Netlify), archive it (or make it private). Separately, apply the website fixes from `REPOSITORY_AUDIT.md` §8 to `portfolio`, which needs your authorization.

## 4. Employee attrition: three repositories

| Repository | Date | Contents |
|---|---|---|
| `AttriPredict` | 2025-04-20 | title-only README, `main.py` (456 lines, pandas/EDA and data-preparation tasks), the dataset CSV, an empty `project2.py` |
| `Employee-Attrition-Data-Analysis-Preparation` | 2025-05-25 | the same `main.py` and CSV (identical Git blobs), no README |
| `Employee-Attrition-Prediction-Machine-Learning-Classification` | 2025-05-16 | a Colab notebook with classification models (Random Forest, SVM, KNN, Gaussian Naive Bayes, XGBoost, SMOTE, a small Keras network) and a title-only README |

`AttriPredict` and `Data-Analysis-Preparation` are **true duplicates**. The Prediction repository is a **separate project stage** (modelling, not data preparation) and must be kept. A student ID appears in a comment in the Prediction notebook.

Recommendation: keep `Employee-Attrition-Data-Analysis-Preparation` (descriptive name, later cleanup commits) as stage 1 and `...Prediction...` as stage 2; add a short README to each linking the two and stating the dataset source if known; archive `AttriPredict` after confirming that it adds nothing (its only extra file, `project2.py`, is empty). Because a duplicate of the CSV is in two repositories, confirm the dataset license before keeping it public.

## 5. Other repositories noted

`next-platform-starter` carries the unchanged "Next.js on Netlify Platform Starter" README and its only visible commit is from an automated dependency bot, so it appears to be an unmodified template fork. It is a candidate for archiving or deletion at your discretion.
