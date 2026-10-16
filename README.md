<div align="center">

# Abdelmonem Sayed Somida

**Computer Science Student (Cybersecurity) · Offensive Security · Web & Application Security**

![GIU, B.Sc. Computer Science](https://img.shields.io/badge/GIU-B.Sc._Computer_Science-1E3A5F?style=flat-square&labelColor=0B1F3A) ![Focus: offensive security](https://img.shields.io/badge/Focus-Offensive_Security-1E3A5F?style=flat-square&labelColor=0B1F3A) ![Seeking internships and entry-level roles in Europe](https://img.shields.io/badge/Seeking-Internships_%26_Entry--level_roles-1E3A5F?style=flat-square&labelColor=0B1F3A)

[Projects](#featured-projects) · [Experience](#professional-experience) · [Thesis](#bachelor-thesis-in-progress) · [Skills](#technical-skills) · [Contact](#contact)

</div>

Final-year B.Sc. Computer Science student at the German International University (GIU), specializing in cybersecurity. I have hands-on experience with web reconnaissance and application security testing from a cybersecurity internship at Breadfast, and I practice Active Directory and Linux attack paths in authorized lab environments.

I'm interested in how real systems fail (input validation, authentication and authorization, network trust boundaries) and in building software and infrastructure that avoids those failures. I'm looking for internships and entry-level roles in Germany and across Europe.

<table width="100%">
<tr>
<td width="33%" valign="top"><b>Security</b><br>Web reconnaissance and controlled application testing (internship); Active Directory and Linux labs</td>
<td width="33%" valign="top"><b>Software</b><br>Full-stack internship with JWT authentication, RBAC and API input validation</td>
<td width="33%" valign="top"><b>Research</b><br>Thesis in progress on secure multi-party computation for privacy-preserving AI</td>
</tr>
</table>

## Featured Projects

> All security work below was performed in authorized or intentionally vulnerable lab environments (TryHackMe, vulnerable VMs, OWASP Juice Shop, simulated networks, coursework).

### Offensive & Web Application Security

<table width="100%">
<tr>
<td>
<b><a href="https://github.com/Mon3em20/offensive-security-labs">Offensive Security Labs</a></b> &nbsp;<sub>TryHackMe and vulnerable VMs</sub><br>
Seven documented lab write-ups: web reconnaissance, directory enumeration, MS17-010 (EternalBlue) validation, Tomcat WAR payload deployment, Linux privilege escalation (cron abuse, PATH hijacking) and a full Active Directory chain (Kerberos enumeration, AS-REP Roasting, SMB enumeration, DCSync, NTDS extraction, Pass-the-Hash).<br>
<code>Nmap</code> <code>Gobuster</code> <code>Burp Suite</code> <code>Metasploit</code> <code>Impacket</code> <code>Kerbrute</code> <code>Evil-WinRM</code><br>
<b>Shows:</b> end-to-end attack methodology and structured technical reporting.
</td>
</tr>
<tr>
<td>
<b><a href="https://github.com/Mon3em20/owasp-juice-shop-security-testing">OWASP Juice Shop Security Testing</a></b> &nbsp;<sub>Intentionally vulnerable web app</sub><br>
Manual assessment covering stored, DOM and reflected XSS; UNION-based SQL injection and SQLi authentication bypass; brute force; weak password recovery; broken CORS; missing authorization controls; CSRF; SSRF. Each finding is documented with steps, impact and mitigation, with two PDF reports.<br>
<code>Burp Suite</code> <code>Burp Intruder</code> <code>Kali Linux</code><br>
<b>Shows:</b> manual vulnerability validation and remediation-oriented reporting.
</td>
</tr>
</table>

### Network Security & Digital Forensics

<table width="100%">
<tr>
<td>
<b><a href="https://github.com/Mon3em20/digital-forensics-investigations">Digital Forensics Investigations</a></b> &nbsp;<sub>Controlled lab evidence</sub><br>
Memory forensics on a Windows dump (process tree, user sessions, account hashes, registry artifacts) and network forensics on malicious PCAP traffic (suspicious domains, attacker IPs, FTP credential exposure, IOC extraction). Two PDF reports.<br>
<code>Volatility 3</code> <code>FTK Imager</code> <code>Wireshark</code> <code>NetworkMiner</code><br>
<b>Shows:</b> investigation workflow from artifact to indicators of compromise.
</td>
</tr>
<tr>
<td>
<b><a href="https://github.com/Mon3em20/enterprise-network-security-lab">Enterprise Network Security Architecture</a></b> &nbsp;<sub>Cisco Packet Tracer simulation</sub><br>
Multi-branch network designed and hardened with OSPF Area 0, VLAN-based design, DMZ segmentation, TACACS+ AAA, SSH v2, port security with sticky MAC, extended ACLs, IPS, IPsec VPN and centralized syslog. Two PDF reports.<br>
<code>Cisco IOS</code> <code>OSPF</code> <code>TACACS+</code> <code>IPsec</code> <code>ACLs</code><br>
<b>Shows:</b> layered, defense-in-depth network design and device hardening.
</td>
</tr>
<tr>
<td>
<b><a href="https://github.com/Mon3em20/iam-business-continuity-planning">IAM Risk Assessment &amp; Business Continuity Planning</a></b> &nbsp;<sub>Design and documentation project</sub><br>
Risk assessment, business impact analysis and disaster-recovery plan for an Active Directory / Azure AD-based IAM environment: risk register, RTO/RPO, backup and RAID design, multi-domain-controller failover, warm recovery site. Nothing is deployed.<br>
<code>NIST SP 800-30</code> <code>BIA</code> <code>Active Directory</code><br>
<b>Shows:</b> security governance and resilience thinking beyond tooling.
</td>
</tr>
</table>

### Cloud, Software & AI/ML

<table width="100%">
<tr>
<td>
<b><a href="https://github.com/youssifabozai/Mini-Jira_AWS">Mini-Jira on AWS</a></b> &nbsp;<sub>Team project · repository hosted on a teammate's account</sub><br>
Multi-team task manager with a NestJS backend on AWS: Cognito-issued JWTs with role-based endpoints, team isolation enforced server-side via DynamoDB GSIs, S3 presigned-URL uploads, SNS/SQS event fan-out, Lambda workers, EventBridge scheduled digests and CloudWatch monitoring. Includes an architecture diagram and documented API and business rules.<br>
<code>AWS Cognito</code> <code>DynamoDB</code> <code>Lambda</code> <code>SNS/SQS</code><br>
<b>Shows:</b> access-control and event-driven design on managed cloud services.
</td>
</tr>
<tr>
<td>
<b>AI/ML notebooks</b> &nbsp;<sub>Jupyter</sub><br>
<a href="https://github.com/Mon3em20/emotion-classification-distilbert-bilstm">Emotion Classification</a>: Bi-LSTM compared with a fine-tuned DistilBERT, including preprocessing, tokenization and confusion-matrix evaluation (PyTorch, Hugging Face).<br>
<a href="https://github.com/Mon3em20/deep-learning-image-captioning">Image Captioning</a>: ResNet50 feature extraction and an LSTM caption generator on MS COCO (TensorFlow/Keras).
</td>
</tr>
</table>

### Additional Projects

| Project | What it is | My part |
|---|---|---|
| [Online Event Ticketing System](https://github.com/Pedro4O4/Theater-Ticketing-System) | Next.js, NestJS and MongoDB booking platform with JWT authentication and role-based access | Team coursework; repository on a teammate's account |
| [Enterprise HR Management System](https://github.com/GIU-Software-Project-I/Main) | Modular full-stack HR platform for the GIU Software Project course | Team coursework; repository in the course organization |
| [Smart Attendance Tracking App](https://github.com/Mon3em20/smart-attendance-tracking-agile-project) | Scrum documentation for a QR/BLE lecture-attendance app | Sprint planning, risk assessment, backlog organization, team coordination, communication planning |

## Professional Experience

**Cybersecurity Intern · Breadfast** &nbsp;<sub>Jul 2026 – Aug 2026</sub>
- Web reconnaissance and technology fingerprinting (subdomain/endpoint discovery, WordPress version detection) with httpx, WhatWeb, WPScan and custom Python checks.
- Automated content discovery with ffuf, feroxbuster and dirsearch, organizing results into CSV/JSON reports.
- Controlled testing for SQL injection, XSS, OS command injection and path traversal, assessing input validation and filtering across target endpoints.

**Software Development Intern · Genesis Infotech (Arma Group)** &nbsp;<sub>Jul 2025 – Sep 2025</sub>
- Built full-stack features with Node.js, React, MongoDB and Supabase, implementing JWT authentication, RBAC authorization and API input validation.
- Developed a Python Course Management System integrating CLI workflows with database operations in a cross-functional team.

## Bachelor Thesis (in progress)

**Biologically Plausible Secure Multi-Party Computation (MPC) for Efficient Privacy-Preserving AI Training**
<br><sub>German International University (Sep–Oct 2026), then German Universities Ulm Campus, Germany (Nov 2026–Jan 2027)</sub>

I'm investigating the computational and communication overhead of privacy-preserving AI training with secure MPC, and exploring whether biologically inspired learning approaches (Forward-Forward and Spiking Neural Networks) could make secure training more efficient. The goal is a practical, testable solution evaluated against appropriate baselines.

> [!NOTE]
> Research in progress. No implementation or results are published yet.

## Technical Skills

| Area | Skills |
|---|---|
| Web & application security | Burp Suite; OWASP Top 10 testing (XSS, SQLi, CSRF, SSRF, CORS, access control); WPScan, ffuf, feroxbuster, dirsearch, httpx, WhatWeb |
| Offensive security (lab) | Kali Linux, Nmap, Metasploit, MSFVenom, Impacket, Kerbrute, Evil-WinRM, John the Ripper; Active Directory attack paths; Linux privilege escalation |
| Network security | Cisco IOS / Packet Tracer; OSPF, ACLs, TACACS+, IPsec VPN, SSH hardening, segmentation |
| Digital forensics | Volatility 3, Wireshark, FTK Imager, NetworkMiner; registry and PCAP analysis |
| Programming | Python, JavaScript/TypeScript, Java, C++, SQL |
| Secure software & cloud | Node.js, React, MongoDB, Supabase; JWT, RBAC, API input validation; AWS (Cognito, Lambda, DynamoDB) |
| Governance | NIST SP 800-30, business impact analysis, BCP/DR planning |
| AI/ML | NLP, PyTorch, TensorFlow/Keras, Hugging Face Transformers, model evaluation |
| Learning | Cloud security, DevSecOps |

## Education & Achievements

- **B.Sc. Computer Science, German International University (GIU)**, 2023 – 2027, specialization: Cybersecurity
- **GIU Capture The Flag 2026:** team participation (Digital Forensics, Cryptography, Web Security, OSINT), team score 1500 points. [Certificate and details](https://github.com/Mon3em20/CTF-2026-GIU)
- **TryHackMe:** offensive security labs on Active Directory, privilege escalation and web exploitation. [Profile](https://tryhackme.com/p/monemsomida)
- **Languages:** Arabic (native), English (B2), German (B1)

## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdelmonem_Sayed_Somida-1E3A5F?style=flat-square&logo=linkedin&logoColor=white&labelColor=0B1F3A)](https://www.linkedin.com/in/abdelmonem-sayed-somida-9739b2312) [![Email](https://img.shields.io/badge/Email-monemsomida%40gmail.com-1E3A5F?style=flat-square&logo=gmail&logoColor=white&labelColor=0B1F3A)](mailto:monemsomida@gmail.com) [![TryHackMe](https://img.shields.io/badge/TryHackMe-monemsomida-1E3A5F?style=flat-square&logo=tryhackme&logoColor=white&labelColor=0B1F3A)](https://tryhackme.com/p/monemsomida)
