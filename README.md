# Abdelmonem Sayed Somida

**Computer Science Student (Cybersecurity) · Offensive Security · Web & Application Security**

Final-year B.Sc. Computer Science student at the German International University (GIU), specializing in cybersecurity. I have hands-on experience with web reconnaissance and application security testing from a cybersecurity internship at Breadfast, and I practice Active Directory and Linux attack paths in authorized lab environments. I also completed a software development internship and am writing my bachelor thesis on privacy-preserving AI training with secure multi-party computation.

I'm interested in how real systems fail (input validation, authentication and authorization, network trust boundaries) and in building software and infrastructure that avoids those failures. I'm looking for internships and entry-level roles in Germany and across Europe.

## Current Focus

- **Offensive security:** web reconnaissance, Active Directory attack paths, Linux privilege escalation (authorized labs)
- **Web application security:** OWASP Top 10 testing with Burp Suite; injection, XSS, CSRF, SSRF, access control
- **Network security and forensics:** enterprise network hardening, memory and PCAP analysis
- **Research:** secure multi-party computation for efficient privacy-preserving AI training (bachelor thesis, in progress)
- **Learning next:** cloud security and DevSecOps

## Featured Projects

All security work below was performed in authorized or intentionally vulnerable lab environments (TryHackMe, vulnerable VMs, OWASP Juice Shop, simulated networks, coursework).

### Offensive Security & Web Application Security

**1. [Offensive Security Labs](https://github.com/Mon3em20/offensive-security-labs)**
- **What:** Seven documented lab write-ups: web reconnaissance, directory enumeration, MS17-010 (EternalBlue) validation, Tomcat WAR payload deployment, Linux privilege escalation (cron abuse, PATH hijacking), and a full Active Directory chain (Kerberos enumeration, AS-REP Roasting, SMB enumeration, DCSync, NTDS extraction, Pass-the-Hash).
- **Tools:** Nmap, Gobuster, Burp Suite, Metasploit/MSFVenom, Impacket, Kerbrute, Evil-WinRM, John the Ripper
- **Demonstrates:** end-to-end attack methodology and structured technical reporting.

**2. [OWASP Juice Shop Security Testing](https://github.com/Mon3em20/owasp-juice-shop-security-testing)**
- **What:** Structured manual assessment of an intentionally vulnerable web app: stored, DOM and reflected XSS; UNION-based SQL injection and SQLi authentication bypass; brute force; weak password recovery; broken CORS; missing authorization controls; CSRF; SSRF. Each finding is documented with steps, impact and mitigation, with two PDF reports.
- **Tools:** Burp Suite (incl. Intruder), browser developer tools, Kali Linux
- **Demonstrates:** manual vulnerability validation and remediation-oriented reporting.

### Network Security & Digital Forensics

**3. [Digital Forensics Investigations](https://github.com/Mon3em20/digital-forensics-investigations)**
- **What:** Memory forensics on a Windows memory dump (process tree, user sessions, account hashes, registry artifacts) and network forensics on malicious PCAP traffic (suspicious domains, attacker IPs, FTP credential exposure, IOC extraction). Two PDF investigation reports.
- **Tools:** Volatility 3, FTK Imager, Registry Viewer, Wireshark, NetworkMiner
- **Demonstrates:** incident-investigation workflow from artifact to indicators of compromise.

**4. [Enterprise Network Security Architecture](https://github.com/Mon3em20/enterprise-network-security-lab)**
- **What:** Multi-branch enterprise network designed and hardened in Cisco Packet Tracer (simulation): OSPF Area 0, VLAN-based design, DMZ segmentation, TACACS+ AAA, SSH v2, port security with sticky MAC, extended ACLs, IPS, IPsec VPN and centralized syslog. Two PDF reports.
- **Demonstrates:** layered, defense-in-depth network design and device hardening.

**5. [IAM Risk Assessment & Business Continuity Planning](https://github.com/Mon3em20/iam-business-continuity-planning)**
- **What:** Risk assessment, business impact analysis and disaster-recovery plan for an Active Directory / Azure AD-based IAM environment using NIST SP 800-30: risk register, RTO/RPO, backup and RAID design, multi-domain-controller failover, warm recovery site. A design and documentation project; nothing is deployed.
- **Demonstrates:** security governance and resilience thinking beyond tooling.

### Cloud Security & Secure Software Engineering

**6. [Mini-Jira on AWS](https://github.com/youssifabozai/Mini-Jira_AWS)** (team project; repository hosted on a teammate's account)
- **What:** Multi-team task manager on AWS with a NestJS backend. Cognito-issued JWTs with role-based endpoints, team isolation enforced server-side via DynamoDB GSIs, S3 presigned-URL uploads, SNS/SQS event fan-out, Lambda workers, EventBridge scheduled digests and CloudWatch monitoring. Includes an architecture diagram and documented API and business rules.
- **Demonstrates:** access-control and event-driven design on managed cloud services.

### AI/ML

**7. [Emotion Classification: Bi-LSTM vs. DistilBERT](https://github.com/Mon3em20/emotion-classification-distilbert-bilstm)**
- **What:** Text emotion classification comparing a Bi-LSTM with a fine-tuned DistilBERT, including preprocessing, tokenization, vocabulary creation and confusion-matrix evaluation (PyTorch, Hugging Face Transformers; Jupyter notebook).

**8. [Deep Learning Image Captioning](https://github.com/Mon3em20/deep-learning-image-captioning)**
- **What:** Image captioning pipeline on MS COCO: ResNet50 feature extraction and an LSTM caption generator (TensorFlow/Keras; Jupyter notebook).

### Additional Projects (team coursework)

- [Online Event Ticketing System](https://github.com/Pedro4O4/Theater-Ticketing-System): Next.js, NestJS and MongoDB booking platform with JWT authentication and role-based access (user, organizer, admin). Team repository on a teammate's account.
- [Enterprise HR Management System](https://github.com/GIU-Software-Project-I/Main): modular full-stack HR platform built for the GIU Software Project course. Team repository in the course organization.
- [Smart Attendance Tracking App (Agile planning)](https://github.com/Mon3em20/smart-attendance-tracking-agile-project): Scrum documentation for a QR/BLE lecture-attendance app. My part: sprint planning, risk assessment, backlog organization, team coordination and communication planning.

## Technical Skills

| Area | Skills |
|---|---|
| Web & application security | Burp Suite, OWASP Top 10 testing (XSS, SQLi, CSRF, SSRF, CORS, access control), WPScan, ffuf, feroxbuster, dirsearch, httpx, WhatWeb |
| Offensive security (lab) | Kali Linux, Nmap, Metasploit, MSFVenom, Impacket, Kerbrute, Evil-WinRM, John the Ripper; Active Directory attack paths; Linux privilege escalation |
| Network security | Cisco IOS / Packet Tracer; OSPF, ACLs, TACACS+, IPsec VPN, SSH hardening, segmentation |
| Digital forensics | Volatility 3, Wireshark, FTK Imager, NetworkMiner, registry and PCAP analysis |
| Programming | Python, JavaScript/TypeScript, Java, C++, SQL |
| Secure software & cloud | Node.js, React, MongoDB, Supabase; JWT authentication, RBAC, API input validation; AWS (Cognito, Lambda, DynamoDB) |
| Risk & governance | NIST SP 800-30, business impact analysis, BCP/DR planning |
| AI/ML | NLP, PyTorch, TensorFlow/Keras, Hugging Face Transformers, model evaluation |
| Learning | Cloud security, DevSecOps |

## Professional Experience

**Cybersecurity Intern, Breadfast** (Jul 2026 – Aug 2026)
- Performed web reconnaissance and technology fingerprinting (subdomain/endpoint discovery, WordPress version detection) using httpx, WhatWeb, WPScan and custom Python checks.
- Automated content discovery with ffuf, feroxbuster and dirsearch, organizing results into CSV/JSON reports.
- Conducted controlled testing for SQL injection, XSS, OS command injection and path traversal, assessing input validation and filtering across target endpoints.

**Software Development Intern, Genesis Infotech (Arma Group)** (Jul 2025 – Sep 2025)
- Built full-stack features with Node.js, React, MongoDB and Supabase, implementing JWT authentication, RBAC authorization and API input validation.
- Developed a Python Course Management System integrating CLI workflows with database operations in a cross-functional team.

## Bachelor Thesis (in progress)

**Biologically Plausible Secure Multi-Party Computation (MPC) for Efficient Privacy-Preserving AI Training**
German International University (Sep–Oct 2026), then German Universities Ulm Campus, Germany (Nov 2026–Jan 2027)

I'm investigating the computational and communication overhead of privacy-preserving AI training with secure MPC, and exploring whether biologically inspired learning approaches (Forward-Forward and Spiking Neural Networks) could make secure training more efficient. The goal is a practical, testable solution evaluated against appropriate baselines.

**Status:** research in progress. No implementation or results are published yet.

## Education & Achievements

- **B.Sc. Computer Science, German International University (GIU)**, 2023 – 2027, specialization: Cybersecurity
- **GIU Capture The Flag 2026:** team participation (Digital Forensics, Cryptography, Web Security, OSINT), team score 1500 points. [Certificate and details](https://github.com/Mon3em20/CTF-2026-GIU)
- **TryHackMe:** offensive security labs on Active Directory, privilege escalation and web exploitation. [Profile](https://tryhackme.com/p/monemsomida)
- **Languages:** Arabic (native), English (B2), German (B1)

## Contact

[LinkedIn](https://www.linkedin.com/in/abdelmonem-sayed-somida-9739b2312) · [Email](mailto:monemsomida@gmail.com) · [TryHackMe](https://tryhackme.com/p/monemsomida)
