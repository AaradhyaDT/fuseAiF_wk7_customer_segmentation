# AARADHYA DEV TAMRAKAR — Master Profile v91

*Last updated: June 12, 2026 — v91: Week 7 Clustering task plan iterated to v3. Gap analysis vs PDF revealed: category spend ratios (keyword-bucketing on Description — 5-category minimum), IQR + Z-score both required for outlier detection, StandardScaler vs RobustScaler explicit decision required (RobustScaler not in S0 imports — needs justification comment per notebook rule). Notebook `.ipynb` read — additional gaps: PDF says `single` linkage, notebook says `average` as 3rd method; resolved by running all 4 dendrograms but fitting only `Hierarchical_Ward` + `Hierarchical_Alt` (matching notebook scaffold column names for S7 compatibility); `Birch` imported in S0 (available for S10); S7 comparison table is 3-row scaffold + optional extras. Final deliverable: `Week7_Clustering_TaskPlan_v3.md`.*

*Previous: v90 — Fusemachines Week 7 Clustering Assignment logged (due June 21, 2026; UCI Online Retail II dataset; K-Means + Hierarchical + DBSCAN pipeline; full task plan `Week7_Clustering_TaskPlan.md` generated; skills added: clustering algorithms, silhouette/Davies-Bouldin/Calinski-Harabasz validation metrics, RFM feature engineering, DBSCAN parameter tuning). Today's exam: O&M Internal Test 1 (June 12, Jestha 29).*

*Previous: v89 — Nexus project added (AI Workflow Hub — personal AI operating system; repo `nexus` under AaradhyaDT; MIT license; React + FastAPI + PostgreSQL + ChromaDB; Day 1 skeleton built; session plan embedded as trigger context).*

*Previous: v88 — PrakopNet BOM updated (RA-02 433 MHz removed → RYLR890 868 MHz adopted; JSN-SR04T replaces HC-SR04; CN3791 replaces TP4056; INA219 added); Nepal LoRa frequency compliance documented (865–867 MHz legal band confirmed); RPi 4B 4GB RAM locked as gateway; feasibility verdict summarised (core demo 80% confidence; 7 additional risk gaps flagged); ChronologicalMerge key doc updated to v3.*

*Previous: v87 — Health diagnosis (chronic allergic conjunctivitis) added; Downloads folder structure documented; C: drive storage analysis noted; HimalGuard_Modifications file removed from key docs (deleted locally); Internal Test 1 context clarified; Ollama model inventory added to System Setup; IDM folder size flagged.*

---

## 📋 Session Loading Instructions

Upload this single file at the start of any Claude session. It contains:
- Full personal & academic identity
- All projects (with CV-accurate descriptions)
- Professional roles & fellowships
- Skills stack & system setup
- Family background & financial context
- Thinking style & Claude preferences
- Ceiling assessment & trajectory planning

### 🔄 Cross-Document Consistency Check (AUTO-TRIGGER)

**When this master profile is loaded alongside any other document, Claude must automatically:**

1. **Scan all uploaded documents** for references that conflict with or predate the master profile's current state
2. **Flag stale references** before proceeding with any task — do not silently use outdated information
3. **Report conflicts** in a brief table at session start: Document | Stale Reference | Current Value in Master

**Known staleness patterns to check for:**

| Check | Current Master Value |
|---|---|
| Project name | **PrakopNet** (formerly HimalGuard — flag any doc still using HimalGuard) |
| Major project direction | Idea D (PrakopNet) confirmed; Idea C (Counter-UAV) archived |
| Major project deadline | **March 2027** (boards/submission); January 2027 = coursework graduation only |
| 8th semester timeline | **Sep 2026 → Mar 2027** |
| Elective I | **EX 725 04 — Aeronautical Telecommunication** (confirmed) |
| Team project roles | PrakopNet roles (see team split table in Major Project §8) — not Counter-UAV roles |
| Masters plan | **Deferred** — only if fully-funded scholarship; not immediate post-graduation |
| Module C PM2.5 | **Included** (reinstated — viable with 6-month timeline) |
| Portfolio hosting | **Netlify + Decap CMS** (migrated from GitHub Pages, June 10, 2026) |
| Nexus project | Repo `nexus` under `AaradhyaDT`; MIT; React + FastAPI + PostgreSQL + ChromaDB; Day 1 skeleton built June 10, 2026 |

**Documents most likely to be stale:**
- `PROFILE_AaradhyaDevTamrakar_v4` — roles reference Counter-UAV; needs v5
- `PROFILE_RupeshKadel_v5` — roles reference Counter-UAV; needs v6
- `PROFILE_SankalpaLamsal_v3` — roles reference Counter-UAV; needs v4
- `PROFILE_SoniaThapa_v3` — roles reference Counter-UAV; needs v4
- `TEAM_PROFILE_SYSTEM_v11_20260610.md` — **current** (individual profiles deprecated; all 4 member profiles absorbed; PrakopNet roles live)
- `MASTER_MajorProject_ChronologicalMerge_v3_20260610.md` — **current** (Phase 6 added; BOM updated; LoRa compliance resolved)
- ~~`HimalGuard_Modifications_v1_20260608.md`~~ — **DELETED locally** (June 10, 2026). Content absorbed into ChronologicalMerge v2 and master profile. No action needed.

**Rule:** If a stale reference is found, flag it and ask whether to update before proceeding. Never silently use the stale value.

---

## 🏦 Banking & Subscriptions

### Siddhartha Bank (SBL)
| Item | Detail |
|---|---|
| **Account** | GenZ Account (active) |
| **Dollar card** | SBL E-com Card (plan: apply at branch) |
| **E-com Card fee** | NPR 500 (1st issuance), NPR 250 reload (2nd+ load) |
| **E-com Card limit** | USD 500/year (resets from first transaction date) — online foreign payments only, no ATM/POS |
| **Docs needed** | Citizenship + PAN + GenZ account details + application form at branch |

### Planned Subscriptions
| Service | Cost | Notes |
|---|---|---|
| **Claude Pro** | ~$18/month (~$216/year) | Well within E-com Card's $500/year limit |

---

## 🔑 Accounts & Identities

| Account | Email |
|---|---|
| **Primary (Claude — active)** | aaradhyadevtmr@gmail.com |
| Claude (secondary) | devtamrakaraaradhya83@gmail.com |
| Claude (alt) | xavier.valois007@gmail.com |
| **Claude (Major Project)** | majorprj79001@gmail.com |
| ChatGPT / GPT-5.3 | aaradhyadevtmr@gmail.com |
| IEEE | aaradhya.devtamkarar@ieee.org |
| Family | tamrakarfamily0@gmail.com |
| Gaming / Misc | adtgames2061@gmail.com |

### Major Project Group Accounts
| Member | Gmail | Notes |
|---|---|---|
| Aaradhya (project Claude) | majorprj79001@gmail.com | Claude account for Major Project workstream |
| Rupesh Kadel | majorprj79034@gmail.com | Has own personal account too |
| Sankalpa Lamsal | majorprj79039@gmail.com | Has own personal account too |
| Sonia Thapa | majorprj79043@gmail.com | Has own personal account too |

> Maintains Claude accounts for parallel workstreams. Uses `.md` files for cross-session continuity.

---

## 🧑 Personal Identity

| Field | Details |
|---|---|
| **Full Name** | Aaradhya Dev Tamrakar[cite: 9] |
| **Date of Birth** | January 6, 2005 (Friday, 11:45 PM)[cite: 9] |
| **Birthplace** | Chitwan, Nepal[cite: 9] |
| **Current Location** | Kathmandu, Bagmati Province, Nepal (KEC Boys' Hostel, on-campus)[cite: 9] |
| **Ethnicity** | Newar (Tamrakar)[cite: 9] |
| **Family Roots** | Patan (grandfather's origin, near Krishna Mandir), Jhapa (2 pieces of land in Damak — illiquid)[cite: 9] |
| **Phone** | +977 9844602050[cite: 9] |
| **LinkedIn** | linkedin.com/in/aaradhya-dev-tamrakar[cite: 9] |
| **GitHub** | github.com/AaradhyaDT[cite: 9] |
| **Portfolio** | aaradhyadtmr.github.io (hosted on Netlify + Decap CMS — migrated June 10, 2026)[cite: 9] |

### Vedic Astrology

| | |
|---|---|
| **Rashi** | Vrischik (Scorpio) — Scorpio Moon[cite: 9] |
| **Lagna** | Kanya (Virgo)[cite: 9] |
| **Nakshatra** | Rohini[cite: 9] |
| **Mahadasha** | Rahu Mahadasha (Jan 2022 – Jan 2040)[cite: 9] |

### Planetary Positions

| Planet | Rashi | Degrees |
|--------|-------|---------|
| Lagna | Kanya (Virgo) | 15° 43' 16"[cite: 9] |
| Surya (Sun) | Dhanu (Sagittarius) | 22° 36' 48"[cite: 9] |
| Chandra (Moon) | Vrischik (Scorpio) | 0° 16' 6"[cite: 9] |
| Mangal (Mars) | Vrischik (Scorpio) | 14° 24' 17"[cite: 9] |
| Budha (Mercury) | Dhanu (Sagittarius) | 1° 30' 11"[cite: 9] |
| Vrihaspati (Jupiter) | Kanya (Virgo) | 23° 52' 36"[cite: 9] |
| Shukra (Venus) | Dhanu (Sagittarius) | 2° 23' 5"[cite: 9] |
| Shani (Saturn) | Karkat (Cancer) | 0° 33' 26"[cite: 9] |
| Rahu | Mesh (Aries) | 4° 52' 31"[cite: 9] |
| Ketu | Tula (Libra) | 4° 52' 31"[cite: 9] |

### House Placements

| House | Sign | Planets |
|-------|------|---------|
| 1st (Lagna) | Kanya (Virgo) | Jupiter ♃[cite: 9] |
| 2nd | Tula (Libra) | Ketu[cite: 9] |
| 3rd | Vrischik (Scorpio) | Moon + Mars[cite: 9] |
| 7th | Meena (Pisces) | Rahu[cite: 9] |
| 10th | Mithun (Gemini) | Saturn[cite: 9] |
| 12th | Simha (Leo) | Sun + Mercury + Venus[cite: 9] |

### Chart Highlights

- **Kanya Lagna + Jupiter in 1st house** — methodical, detail-oriented, service-driven[cite: 9]
- **Moon + Mars conjunct in Scorpio (3rd house)** — intensity, willpower; internalizes until eruption[cite: 9]
- **Sun, Mercury, Venus in 12th house** — processes alone before externalizing; inner life dominates[cite: 9]
- **Rahu in 7th house** — karmic/unusual relationships; 18-year amplification period[cite: 9]
- **Saturn in 10th house** — career earned methodically, not gifted; slow but solid builder[cite: 9]

---

## 👨‍👩‍👦 Family Background

| Member | Age | Role / Status |
|---|---|---|
| **Father** | 53 | Senior Agency Manager, NLIC — client acquisition increasingly difficult[cite: 9] |
| **Mother** | 48 | Part-time health screening associate, IOM[cite: 9] |
| **Brother** | 15 | Just completed SEE; moving to Kathmandu for +2 Science (Computer)[cite: 9] |

- 2 pieces of land in **Damak, Jhapa** — family asset, illiquid[cite: 9]
- **Financial position:** Constrained but stable[cite: 9]. No significant safety net[cite: 9]. Brother arriving adds household pressure[cite: 9].
- **Time horizon:** ~2–3 year window before family expects financial contribution[cite: 9]. Not crisis — but a real clock[cite: 9].

### Generational Context

**Father's side:**
- Wealthy 4+ generations back
- Grandfather was the only son — yet received no inheritance
- Multiple stepmothers entered one after another (fates unconfirmed — left or deceased)
- Stepmother abuse forced grandfather to relocate to Chitwan; inheritance severed entirely despite being the sole male heir
- Root cause: outsider entry → abuse/exclusion → inheritance chain broken

**Mother's side:**
- Wealthy 4+ generations back; poverty hit ~2 generations ago
- Great-grandmother was the 2nd wife — 1st wife had no children; 3rd wife drove the others out, cutting off family support and inheritance
- Root cause: same mechanism — outsider entry → exclusion → inheritance chain broken

**Pattern recognized across both sides:**
- Identical failure mode, independently on both family lines: an external entrant chose exclusion/abuse over family continuity, severing generational wealth at a single inflection point
- Not bad luck — deliberate acts of exclusion repeated across both lineages
- Aaradhya consciously identifies as the generation that breaks this cycle on both lines

- **Loyalty hierarchy:** Immediate family of four → close friends → reciprocal cousins → behavior-based acquaintances[cite: 9]. Extended family who were extractive: no obligation[cite: 9].
- **Marriage approach:** Court marriage first, small celebration, closest only[cite: 9].

### Health

| Condition | Detail |
|---|---|
| **Chronic Allergic Conjunctivitis** | Left eye primarily; diagnosed June 10, 2026. Red eye recurring ~monthly since Falgun (Feb 2026), alternating eyes. Treatment: antihistamine eye drops (use on schedule, not just on flares). Screen-heavy sessions aggravate it. |
| **Eye care note** | Hostel environment (dust/shared spaces) is a common trigger. Avoid rubbing. Pillow hygiene matters. |

---

## 🎓 Academic Background

| Field | Details |
|---|---|
| **Institution** | Kathmandu Engineering College (KEC), IOE, Tribhuvan University[cite: 9] |
| **Degree** | Bachelor of Electronics, Communication and Information Engineering (BEI)[cite: 9] |
| **Current Level** | Year IV / Part I — 7th Semester[cite: 9] |
| **Expected Graduation** | January 2027[cite: 9] |

### Current Subjects (IV/I — 7th Semester)
Wireless Communication · Artificial Intelligence · Organization & Management · Digital Signal Analysis & Processing · RF & Microwave Engineering · **Elective I: EX 725 04 — Aeronautical Telecommunication** ✅ (confirmed) · Project Part A

> **Elective I — CNS alignment confirmed.** Aeronautical Telecommunication covers ATC communications, ILS/VOR/DME/NDB navigation aids, surveillance systems (SSR, ADS-B), ICAO standards, and CNS/ATM frameworks — directly maps to CAAN Nepal and AAI India JE career target. Exam: June 22, 2026.

### IV/II Subjects (8th Semester — incoming, Sep 2026)
Telecommunications · Professional Practice · Energy, Environment and Society · Information Systems · Elective II (EX 765) · Elective III (EX 785) · Project Part B (Major Project — PrakopNet, deadline March 2027)

> **IV/II Elective strategy (confirm at registration):** Two elective slots. Given CNS/aeronautical path and PrakopNet: Elective II → **Radar Technology (EX 725 01)** or **Satellite Communication (EX 725 02)** if available for IV/II slot. Elective III → **Data Mining (CT 785 02)** (supports PrakopNet ML analytics) or **Remote Sensing (CT 785 01)** (supports GIS/geospatial angle for PrakopNet commercialization). Confirm which options KEC offers for IV/II at registration.

### IV/I Exam Schedule (2083 — Test 1)
> **Internal Test 1 context:** Limited syllabus coverage (not full boards). Questions are provided in advance for each subject. Preparation strategy = know the given questions cold, not cover the full syllabus.

| Date (BS) | Date (AD) | Subject |
|---|---|---|
| Jestha 22 | Jun 5 | Wireless Communication ✅ |
| Jestha 25 | Jun 8 | Artificial Intelligence ✅ |
| Jestha 29 | **Jun 12** | **Organization & Management ← TODAY** |
| Asar 1 | Jun 15 | Digital Signal Analysis & Processing |
| Asar 5 | Jun 19 | RF & Microwave Engineering |
| Asar 8 | Jun 22 | Elective I — EX 725 04 Aeronautical Telecommunication ✅ |
| Asar 12 | Jun 26 | Project Part A (no written exam) |

### Study Resource Assets (assembled June 2026)
- **IV/I Syllabus** — `BEIE_IV_I_Syllabus.md` (all 7 subjects, full topic breakdown)
- **IV/II Syllabus** — `BEIE_IV_II_Syllabus.md` (all 7 subjects, full topic breakdown)
- **Full BEI Curriculum** — `BEI_Curriculum_ElectronicsCommunicationInformation.md` (all 8 sems, credit hours, marks)
- **All 8-semester subject PDFs** — individual syllabus PDFs for every semester; self-collected (not provided at orientation)
- **Past questions** — downloaded past exam papers for IV/I subjects
- **Study hub template** — `es_ct655_integrated.html` — single-file HTML exam prep hub (CT 655, III/II). Method confirmed effective. Template for IV/I subject hubs.

### Study Hub Method (from CT 655 / III/II finals)
Single-file HTML per subject: Q-sections mapped to exam slots, frequency map, predictions, past papers, Q&A, quiz, reading roadmap. Method fit for IV/I:

| Subject | Fit | Notes |
|---|---|---|
| Artificial Intelligence | Excellent | Fixed topic slots, same pattern as CT 655 |
| Org & Management | Excellent | Pure written, predictable |
| Wireless Communication | Good | Needs formula banks added |
| DSAP | Good | Needs solved-numericals section per topic |
| RF & Microwave | Good | Needs worked examples for circuit analysis |

### BEI Curriculum Coverage (Full — for project framing)

| Domain | Subjects |
|---|---|
| Core Electronics | Basic Electronics, Electronic Circuits, Analog & Digital Communication, Microprocessors & Microcontrollers, VLSI & IC Design, Power Electronics[cite: 9] |
| Communication & RF | Communication Systems, Propagation & Antenna, Fiber Optics, Satellite & Mobile Communication, Transmission Lines & Waveguides[cite: 9] |
| Information / Software | Data Structures & Algorithms, Computer Networks & Security, DBMS, OS, OOP, Web Technology[cite: 9] |
| Signal Processing & Math | Signals & Systems, Digital Signal Processing, Engineering Mathematics I–IV, Probability & Stochastic Processes[cite: 9] |
| Control & Instrumentation | Control Systems, Instrumentation & Measurement, Sensors & Transducers[cite: 9] |
| Applied | Minor Project (GCSBR) · Major Project[cite: 9] |

---

## 💼 Professional & Organizational Roles

| Role | Organization | Period |
|---|---|---|
| **Fuse AI Fellow** | Fusemachines | 2026–Present[cite: 9] |
| **Vice Chair** | IEEE KEC Student Branch | 2026/2027[cite: 9] |
| **DataCamp Fellow — Cohort 2** | NSSR | 2026–Present[cite: 9] |
| **Event Manager** | Electronics Project Club (EPC), KEC | 2026–Present[cite: 9] |
| **Vice Secretary** | IEEE KEC Student Branch | 2025–2026[cite: 9] |
| **Resource Manager** | Electronics Project Club (EPC), KEC | 2024–2026[cite: 9] |
| **Makerspace Ambassador (applied)** | KEC Maker's Space | June 2026–Present (web dev track; grants free 3D printing, laser cutting, materials, 1Gbps WiFi) |
| **Charter Membership Chairperson** | LEO Club of Damak Gold | Jan 2020 – 2025 (disbanded)[cite: 9] |
| **2nd Vice President** | LEO Club of Damak Gold | May 2020 – May 2021 (1 yr 1 mo)[cite: 9] |

---

## 🌐 Actual Situation & Path (as of June 2026)

*This section is the ground truth. Not a task log — the real picture.*[cite: 9]

### Where things stand

Aaradhya is 21, finishing BEI at KEC (graduation Jan 2027), with ~2–3 years before the family financial clock becomes a crisis[cite: 9]. He has built a stronger portfolio than most BEI students at his level — real shipped work, not just coursework — but his core gap is **finishing things**[cite: 9]. The gap between what he starts and what ships is the main ceiling limiter[cite: 9]. Completion is the only metric that matters right now[cite: 9].

He is mid-Rahu Mahadasha (through Jan 2040) — the period of maximum amplification[cite: 9]. High upside and high volatility[cite: 9]. Every decision this decade compounds[cite: 9].

### The actual path

**Clarified future goals (June 8, 2026 — in order of execution):**

1. **Fuse AI Fellowship completion** — primary focus through mid-2026. Highest CV leverage. Every week's output must be real, understood code.
2. **Graduate as BEI engineer** — Jan 2027 (coursework complete); boards/project submission March 2027. PrakopNet demo in hand.
3. **CNS/aeronautical engineering role** — post-graduation primary income path. CAAN Nepal or AAI India (Junior Executive – Electronics exam). Directly leverages RF & Microwave, signal processing, embedded background. NEC 97/100 mock score = exam-ready.
4. **PrakopNet commercialization** — post-graduation side track alongside job. First pilot: municipality, NGO, or hydropower operator. Makerspace fabrication resources make the hardware demo professional-grade.
5. **Masters** — deferred. Only viable if fully-funded scholarship (MEXT, DAAD, Erasmus Mundus) appears. Unfunded masters during the financial clock window is high-risk and competes directly with PrakopNet momentum. Target Year 3–5 post-graduation, with 2–3 years of domain context making the research output stronger.

**Phase map:**

| Phase | Period | Primary | Secondary | Background |
|---|---|---|---|---|
| Exam period | Now → Jun 26 | Exams | Fellowship (weekly deadlines hold it) | Makerspace web dev, Excelerate application |
| Fellowship final stretch | Jul → Aug 2026 | Fellowship completion | Excelerate internship (if matched) | PrakopNet architecture, DataCamp |
| 8th semester | Sep 2026 → Mar 2027 | PrakopNet demo | NEC license prep | DataCamp certs, IEEE events |
| Post-graduation | Mar → Aug 2027 | Job applications (CNS + AI/ML) | PrakopNet pilot/grant push | Upwork profile (portfolio now complete) |
| Year 1–3 | 2027–2030 | CNS/engineering job | PrakopNet commercialization | Masters prep (if funded path appears) |

**Time slot rule (completion gap countermeasure):**
One primary. One secondary. Background only for things that run themselves. Nothing enters the primary slot until the current primary ships or has an immovable external deadline. This is the structural fix for the known commitment-stacking pattern. Fellowship deadlines are the proof it works — same forcing function must be replicated for every new commitment.

**Earning timeline:**

| Milestone | Target | Earning |
|---|---|---|
| Excelerate application | This week (apply now, start Jul) | Structured project, possible pay, CV line |
| Fellowship completes | Mid-2026 | GitHub portfolio live and visible |
| PrakopNet demo | Mar 2027 | Grant applications competitive; pilot conversations viable |
| Post-graduation job | Jan–Jun 2027 | Rs. 40–70k/month Nepal / ₹6–12 LPA India |
| PrakopNet pilot | Year 1–2 | NGO grant or municipal contract upside |
| Upwork side income | Year 1 (job stable) | Rs. 15–25k/month supplementary |

**Excelerate + OpportunitiesRadar:**
- Excelerate: virtual project-based internships, 4–8 week commitments. Target: AI/ML pipeline or IoT projects. Apply this week; start July post-exams. "Intern at [Company]" reads better than "Freelancer" for CNS/engineering job applications.
- OpportunitiesRadar: discovery aggregator only. Use weekly to find Nepal-relevant AI/ML, IoT, disaster tech internships and PrakopNet-relevant grant calls.

**Phase 1 — Now to March 2027 (before graduation/boards)**[cite: 9]

The goal is to graduate with a CV that can compete for ML/AI engineering roles at ₹6–12 LPA entry (India is one option under active consideration — not confirmed), and build enough credential mass that any post-graduation move is justified rather than a leap into the dark[cite: 9].

What's currently running:
- **Fusemachines AI Fellowship** (the primary focus): Weeks 1–6 complete; **Week 7 Clustering Assignment in progress (due June 21, 2026)**[cite: 9]. This is the most valuable thing on the CV right now[cite: 9]. Every week's output needs to be real, understood code — not copy-pasted[cite: 9]. Fellowship ends mid-2026[cite: 9].
- **Portfolio website — CMS migration (June 10, 2026)**: `aaradhyadtmr.github.io` migrated from static GitHub Pages to **Decap CMS + Netlify** architecture. Projects, Experience, and Achievements now managed via CMS UI at `/admin/`. `index.html` refactored to async `loadCMSData()` fetching `/content/projects.json`, `/content/experience.json`, `/content/achievements.json`. `netlify.toml`, `admin/config.yml`, and pre-populated JSON files committed to repo.
- **IEEE KEC Vice Chair**: Running real events[cite: 9]. SPAx "Engineer Your Profile" happened May 23[cite: 9]. The risk is it becomes a title without substance — must run something that leaves a mark[cite: 9].
- **Major Project — PrakopNet** (Idea D, confirmed June 8, 2026): Solar-powered LoRa mesh multi-hazard EWS. Demo target: **March 2027 boards**. Makerspace Ambassador access (3D printing, laser cutting, 1Gbps WiFi) directly supports hardware fabrication. See Major Project section for full spec.[cite: 9]
- **DataCamp certs** (NSSR fellowship): Fully completed Phase 1 Applied AI portfolio[cite: 3, 5, 8]. Transitioning to SQL Associate + Python Data Associate pathways[cite: 8]. Data Engineer + Data Scientist + AI post-fellowship[cite: 9]. Background resource — zero conflict with Fusemachines[cite: 9].
- **Algoverse AI Research application**: Deadline May 24[cite: 9]. Research problem: "Efficient Multimodal Reasoning on Edge Devices: Quantization Strategies for Real-Time Gesture Recognition Using Optimized LLMs[cite: 9]." Grounded in live DeepSeek R1 7B on Intel Arc + GCSBR[cite: 9]. If accepted: full-time 8–12 week research block June–Aug 2026[cite: 9]. Targets NeurIPS edge ML workshops / ACL efficiency track[cite: 9].

What's been cancelled or deprioritized:
- **Robotica 6-Month Robotics Technician Program**: Cancelled[cite: 9]. Morning batch conflict, budget, and Algoverse opportunity made it the right cut[cite: 9].
- **eSewa Android Intern**: Applied May 13[cite: 9]. Outcome unknown[cite: 9]. If not selected: no disruption — it was an opportunistic application, not the plan[cite: 9].

**Phase 2 — Post-graduation (March 2027 onward)**[cite: 9]

**Primary career target: CNS/aeronautical engineering.** RF & Microwave, signal processing, embedded systems background maps directly to CNS ground infrastructure (VHF/UHF comms, ILS, DVOR, SSR, ADS-B, MLAT). NEC mock score 97/100 = exam-ready.

- **Nepal:** CAAN (Civil Aviation Authority of Nepal) CNS/electronics roles — stable, government-adjacent, limited openings per year.
- **India:** AAI Junior Executive (Electronics) — written exam path, tens of openings, BEI + NEC qualifies directly. Bangalore / Pune / Hyderabad under consideration.
- **AI/ML engineering roles:** Fusemachines fellowship credential is the pitch. ₹6–12 LPA entry India.

Strategic alignment: CNS job + PrakopNet are synergistic. Day job builds domain relationships with the same infrastructure operators who are PrakopNet's target customers (DHM, CAAN-adjacent, telecom serving remote areas).

**Masters:** Deferred unless fully-funded scholarship. Without funding: wait until Year 3–5. A thesis on edge AI for disaster EWS at that point upgrades PrakopNet's research novelty score (7.5 → 9+) and builds international fundraising network. Better research output with 2–3 years of domain experience behind it.

NI cert sequence (if AI/ML engineering path): CLAD post-fellowship (mid-2026, 6 mo LabVIEW practice) → CTD simultaneously → CLD (Year 2–3) → branch to CLED or CTA depending on first job domain[cite: 9].

### The honest constraints

- **Completion gap**: Starts well, loses momentum[cite: 9]. SysOptimizer v5, Alpha app, portfolio site fixes — all partially done[cite: 9]. The pattern is known[cite: 9]. Fellowship deadlines are the only structure that's been reliably closing things[cite: 9].
- **Financial clock**: Not crisis yet[cite: 9]. But the window is real[cite: 9]. Earning before graduation (Rs. 15–20k/month) changes psychological position significantly[cite: 9].
- **No shortcuts on understanding**: AI/local LLM environment is set up[cite: 9]. The risk is using it as a crutch rather than a tool[cite: 9]. The fellowship work has been done with genuine understanding — that needs to stay true[cite: 9].

### What would constitute success by March 2027

1. Next-gen applied GenAI competencies locked via structured training pipelines[cite: 3, 5].
2. Fusemachines fellowship completed with public GitHub deliverables for every week — visibly real work[cite: 9]
3. Major Project functional demo — runs, not just documented[cite: 9]
4. Alpha on Play Store **or** one DataCamp career cert[cite: 9]
5. Post-graduation plan concrete: offer in hand, or strong pipeline of applications[cite: 9]

---

## 🛠️ Projects

### 1. Gesture-Controlled Self-Balancing Robot (GCSBR) — Minor Project *(Completed)*
**Stack:** Computer Vision · Arduino · MPU6050 · Stepper Motors · Android · MATLAB[cite: 9]
**Rating: 9.4/10 — Examiner called it "major project level"**[cite: 9]

- Sensor fusion + PID stabilization + mobile gesture control[cite: 9]
- Firmware V6.9.1: watchdog timer, atomic writes, differential ramp, integrator bleed[cite: 9]
- MATLAB simulation → real-world hardware deployment[cite: 9]
- Android gesture-control interface (MediaPipe, CameraX, HC-05 BT)[cite: 9]
- Dual-hand gesture control; DRV8825 drivers on CNC Shield[cite: 9]
- GitHub: `AaradhyaDT/Gesture-Controlled-Self-Balancing-Robot`[cite: 9]

### 2. Text-to-SQL Agentic Pipeline (Fusemachines Week 3) *(Completed)*
**Stack:** Python · FastAPI · Streamlit · PostgreSQL · Docker · OpenAI API · Prompt Chaining[cite: 9]
**Rating: 8.7/10**[cite: 9]

- Production-grade automated Text-to-SQL pipeline and state-based FastAPI SQL Agent over `classicmodels` PostgreSQL database[cite: 9]
- Modular agent workflow: Planner → Generator → Validator → Executor → Summarizer with self-correction (up to 3 retries)[cite: 9]
- Vanilla Python prompt-chaining with GPT-4o-mini, rule-based SQL safety validation (blocking DML/DDL), structured JSON query logging[cite: 9]
- **100.0% execution success rate and 100.0% result accuracy** on 50-question benchmark, zero retries required[cite: 9]
- Streamlit chat interface + Docker/Docker Compose containerization[cite: 9]
- GitHub: `AaradhyaDT/fuseAiF_wk3_text2sql`[cite: 9]

### 3. Telco Customer Churn & CLV Machine Learning Pipeline (Fusemachines Week 4) *(Completed)*
**Stack:** Python · Scikit-learn · Pandas · NumPy · Matplotlib · Seaborn · Papermill[cite: 9]
**Rating: 8.5/10**[cite: 9]

- End-to-end classification + regression pipeline for Telco Churn and CLV modeling[cite: 9]
- Stratified 70/15/15 split; Logistic Regression / Ridge / SGD classifiers benchmarked[cite: 9]
- Custom threshold at 0.385 → top-200 high-risk budget segment[cite: 9]
- Ridge Regression best for CLV (mean CLV $1,304.70); Lasso L1 regularization paths plotted[cite: 9]
- Stratified 5-fold CV: ROC-AUC 0.841 ± 0.005; learning curves + leakage simulation[cite: 9]
- Papermill automation; full HTML report export; Graphify knowledge graph integration[cite: 9]
- GitHub: `AaradhyaDT/FUSE_AIF_2026_M1` (under `WK4/`)[cite: 9]

### 4. Telco Churn Tree-Based Ensemble Pipeline (Fusemachines Week 5) *(Completed)*
**Stack:** Python · Scikit-learn · XGBoost · imbalanced-learn · SHAP · Joblib · Matplotlib[cite: 9]
**Rating: 9.0/10**[cite: 9]

- End-to-end classification pipeline on Telco Customer Churn (7,043 rows, ~27% positive rate, binary target)[cite: 9]
- Models: Random Forest + XGBoost benchmarked against naïve baseline; AUROC, Precision, Recall, F1 as primary metrics (accuracy trap exposed)[cite: 9]
- Full Scikit-learn `ColumnTransformer` pipeline for mixed dtypes (numeric scaling + categorical encoding); `ImbPipeline` (imbalanced-learn) ensures SMOTE restricted to training folds only — zero preprocessing leakage[cite: 9]
- Hyperparameter tuning via Grid Search / Bayesian optimisation on XGBoost; documented most impactful hyperparameter[cite: 9]
- SHAP global summary plot (Q15) + local waterfall/force plot (Q16); 2-sentence retention recommendation for specific at-risk customer[cite: 9]
- Production serialization: full fitted pipeline (ColumnTransformer + SMOTE + model) saved via `joblib` as `telco_churn_pipeline_v1.joblib`[cite: 9]
- Secondary regression task: `tenure` prediction (regression model)[cite: 9]. Defined target and feature matrix, dropped `TotalCharges` leakage column to prevent mathematically defined correlation leakage[cite: 9].
- Trained unconstrained Decision Tree Regressor vs regularized XGBoost Regressor[cite: 9]. Plotted learning curves using 5-fold cross-validation showing overfitting in the unpruned baseline vs generalization in the XGBoost regressor[cite: 9].
- Verified tree model predictions are strictly bounded by the training range maximums (extrapolation check)[cite: 9].
- Model Card (Q18) completed with real metric values[cite: 9]
- GitHub: `AaradhyaDT/fuseAiF_wk5_telco_churn_ensembles`[cite: 9]

### 5. Alpha Android Super-App *(Active)*
**Stack:** Kotlin · Jetpack Compose · Material3 · DataStore · Apache POI[cite: 9]
**Rating: 8.2/10 — Primary shipping target**[cite: 9]

- Modular super-app (`com.alpha`, SDK 36, Astronomus font)[cite: 9]
- Modules: SBR gesture control (MediaPipe, CameraX, HC-05 BT) · Multi-mode calculator (STD / PROG / LOGIC) · Settings (DataStore) · Budget Tracker (eSewa parser, Apache POI, DataStore persistence — Google Drive backup in progress)[cite: 9]
- Location: `D:\Android\Projects`[cite: 9]

### 6. Edge AI Stability Detection System *(Completed)*
**Stack:** Python · Scikit-learn · FastAPI · Joblib[cite: 9]
**Rating: 7.8/10**[cite: 9]

- ML system predicting platform stability from simulated IMU sensor data (tilt_x, tilt_y, angular velocity)[cite: 9]
- 10,000-sample synthetic dataset; Random Forest classifier — **99.8% test accuracy**[cite: 9]
- REST API via FastAPI for real-time predictions; Joblib export for robotics integration[cite: 9]
- GitHub: `AaradhyaDT/stability-ai-system`[cite: 9]

### 7. SysOptimizer — Windows Optimization Tool *(v5 Active)*
**Stack:** Python · CustomTkinter · PyInstaller · WMI · PowerShell[cite: 9]
**Rating: 7.6/10**[cite: 9]

- Standalone `.exe` via PyInstaller; animated ring gauges, sparklines, process table, dark/light mode[cite: 9]
- v5: Stricter RAM reclamation, CPU boost clock fix via WMI, Background Bloat & Startup Apps overhaul[cite: 9]
- `CREATE_NO_WINDOW` creationflags — zero UI interruption[cite: 9]

### 8. Major Project — PrakopNet *(Idea D — CONFIRMED PRIMARY, June 8, 2026)*

**Full title:** Solar-Powered LoRa Mesh Multi-Hazard Monitoring and Early Warning Platform with GPS Localization and Edge AI for Remote Regions of Nepal

**Team:** Aaradhya Dev Tamrakar · Rupesh Kadel · Sankalpa Lamsal · Sonia Thapa (KEC BEI Batch 2081)

**Status as of June 10, 2026:**
Idea D (PrakopNet) is the confirmed major project direction. Idea C (Counter-UAV) has been archived. **Deadline: March 2027 (8th semester boards)** — 6 months of build time from September 2026. The team will graduate with working hardware, not just documentation.

**Timeline & Budget assessment (June 10, 2026):**
6-month build window (Sep 2026 → Mar 2027). Full-scope viable at core level (80% confidence); full scope including all 🟠–🟢 items is 50% confidence — scope-lock at project kickoff is essential. Order all import components in Month 1 (2–3 week AliExpress/Amazon India lead time). All LoRa modules are now import-only (see LoRa compliance note below).

**LoRa Frequency Compliance (confirmed June 10, 2026):**
Nepal legal band: **865–867 MHz** (IN865-867 channel plan, NTA). Max 1W TX / 4W ERP. The 433 MHz band (EU433) is legal but limited to 10 mW ERP — insufficient for the 3–15 km range claims. US915/AU915 (902–928 MHz) is **illegal** in Nepal (assigned to Ncell/NTC 4G).

**Critical BOM change (June 10, 2026):**
LoRa RA-02 (SX1276, 410–525 MHz / 433 MHz variant) **removed** from BOM — 433 MHz ERP limit invalidates range claims. Replaced with **RYLR890 (868 MHz, UART AT commands)**. Also: HC-SR04 → JSN-SR04T (waterproof); TP4056 → CN3791 (solar-rated charge controller); INA219 current sensor added (power budget measurement, thesis contribution).

**Nepal hardware availability (updated June 10, 2026):**
| Component | Source | Availability |
|---|---|---|
| ESP32-WROOM-32 (DevKit V1) | Himalayan Solution, Breadfruit | ✅ Local, same-day |
| RYLR890 (LoRa 868 MHz, UART) | Import — AliExpress / Amazon IN | ⚠️ **Order Month 1; specify 868 MHz** |
| Neo-6M GPS | Himalayan Solution | ✅ Local |
| MPU6050 | Himalayan Solution, Breadfruit | ✅ Local |
| DHT22 | Himalayan Solution, Breadfruit, Daraz | ✅ Local |
| JSN-SR04T (waterproof ultrasonic) | Import | ⚠️ Order Month 1 — not HC-SR04 |
| Capacitive soil moisture sensor | Himalayan Solution, Breadfruit | ✅ Local |
| MQ135 (air quality) | Himalayan Solution, Breadfruit | ✅ Local |
| PMS5003 (PM2.5) | Import | ⚠️ Order Month 1 (2–3 wk lead) |
| 6V 5W solar panel | Local electronics, Daraz | ✅ Local |
| CN3791 solar charge controller | Import / Daraz | ⚠️ Order Month 1 |
| 18650 Li-ion (protected, 3000–3500 mAh) | Local battery shops, Daraz | ✅ Local |
| MT3608 boost converter | Himalayan Solution, Breadfruit | ✅ Local |
| INA219 current sensor | Import / Daraz | ⚠️ Order Month 1 |
| Raspberry Pi 4B (4GB) | Breadfruit (inconsistent stock) | ⚠️ Check early; import from Amazon IN if OOS |
| Weatherproof enclosures | 3D print (KEC Makerspace) | ✅ Makerspace |

**Fusemachines fellowship → PrakopNet skill mapping (confirmed June 10, 2026):**
| Fellowship Output | PrakopNet Role |
|---|---|
| LSTM (Wk4 CLV time-series) | Core edge inference: sensor time-series → hazard score |
| SMOTE (Wk5) | Imbalanced disaster event data — same fix |
| SHAP (Wk5) | Explainability for defense: which sensor triggered alert |
| XGBoost/RF (Wk5) | Lightweight fallback classifier on gateway |
| FastAPI + Docker (Wk3) | Base station dashboard + alert API |
| Papermill (Wk4) | Automated retraining pipeline on new seasonal data |
| PC-side pipeline discipline | Training → TFLite quantization → ESP32 deployment chain |

**Team ownership (locked — see team split table above):**
- Firmware/hardware node + LoRa mesh + gateway hardware: **Rupesh** (primary) + **Sankalpa** (hardware assembly, solar, 3D design)
- ML pipeline (training → quantize → TFLite deploy) + HazardScore fusion + LaTeX thesis: **Aaradhya**
- Backend (FastAPI) + grant writing: **Aaradhya** (secondary)
- Dashboard frontend (Streamlit/Flask) + data logging + GPS visualization: **Sonia** (primary)
- Report/documentation co-lead (thesis structure, section drafts): **Sonia** (secondary)

**Architecture:**
- **Sensor Nodes:** ESP32 DevKit V1 + RYLR890 (LoRa 868 MHz, UART AT commands) + GPS (Neo-6M) + Solar subsystem (6V 5W panel → CN3791 charge controller → 18650 ×2 parallel → MT3608 boost → 5V) + INA219 power monitor + environmental sensors
- **Gateway:** Raspberry Pi 4B (4GB RAM) + RYLR890 (UART) + dashboard server + PostgreSQL + AI processing
- **AI Layer:** Federated TFLite Micro on ESP32 nodes (local binary anomaly decision) + LSTM at gateway (multi-sensor time-series → HazardScore) + TFLite runtime at gateway

**Modular Sensor Modules:**
- Module A — Flood: ultrasonic water level sensor
- Module B — Landslide: MPU6050 + optional geophone
- Module C — Air Quality: MQ135 + PM2.5
- Module D — Weather: rain gauge, wind, humidity
- Module E — Wildfire: smoke + temperature
- Module F — Structural Health: strain gauges, vibration sensors

**Build Phases:**
- Phase 1: ESP32 + LoRa + GPS + MPU6050 + DHT22 + solar subsystem → basic network
- Phase 2: Water level + rainfall monitoring
- Phase 3: Geophone + GSM backup + PM2.5

**Assessment:**
| Dimension | Current | Target |
|---|---|---|
| Academic Value | 9/10 | 9.5/10 |
| Commercial Potential | 9/10 | 9.5/10 |
| Buildability | 9/10 | 9/10 (hold) |
| Research Novelty | 7.5/10 | 8.5–9/10 |
| Nepal Relevance | 10/10 | 10/10 (hold) |

**What's locked — do not touch:**
ESP32 + LoRa SX1278 + Neo-6M GPS + Solar + 18650 per node · RPi 4B as gateway · LoRa mesh topology · LSTM + TinyML at AI layer · Module A (Flood) + Module B (Landslide) as core two · MPU6050 for seismic · DHT22 for temperature/humidity

**Phase 5 Technical Modifications (originally from HimalGuard_Modifications_v1, now in MASTER_MajorProject_ChronologicalMerge_v2):**

| Modification | Priority | Build Effort | Impact |
|---|---|---|---|
| **Federated TFLite edge inference on ESP32 nodes** — each node runs local binary anomaly model; alerts fire even if LoRa gateway link degraded; direct transfer from GCSBR + Edge AI Stability Detection work | 🔴 1 — Do not drop | 2–3 weeks | Novelty +1 point; disaster resilience |
| **Multi-hazard composite HazardScore (0–100)** — gateway fuses WaterLevel + SeismicAmplitude + RainfallRate + SlopeInstability with tunable weights per zone; threshold bands Green/Amber/Red | 🟠 4 | 1 week | Novelty +0.5; commercial clarity |
| **Solar power telemetry logging** — ADC voltage read on ESP32 → log panel voltage + battery SoC per node per interval; publishable empirical dataset (no Nepal equivalent exists) | 🟠 5 | 2–3 hrs HW + 1 day firmware | New empirical contribution |
| **Adaptive LoRa Spreading Factor** — nodes auto-select SF7–SF12 based on RSSI from last gateway ACK; graceful degradation in disaster conditions | 🟡 6 | 1 week | Disaster robustness |
| **GPS-fenced alert zones** — lat/lon polygon per deployment zone; alert propagates only if anomaly falls within boundary | 🟡 7 | 2–3 hrs (point-in-polygon) | Reduced false positives; commercial pitch strength |

**Scope cuts:**
- Modules E (Wildfire) and F (Structural Health) → document as future work
- Geophone → MPU6050 covers the need; document as upgrade option
- GSM backup → LoRa mesh handles graceful degradation; document as future work
- >3 physical nodes → build 2–3 real; simulate mesh scale in thesis
- Module C (Air Quality): MQ135 + PM2.5 ✅ (viable with 6-month timeline — procure early September)
- Module D (Weather): DHT22 + one rain sensor only

**Research novelty fix strategy (7.5 → 8.5+):**
1. **Literature gap statement (Chapter 1):** "Existing LoRa-based EWS address single-hazard monitoring in isolation. No published system demonstrates multi-hazard fusion with edge-computed composite risk scoring, GPS-tagged anomaly localization, distributed ESP32 TFLite inference, and solar-powered autonomous mesh operation validated in South Asian deployment contexts." Each clause independently verifiable on IEEE Xplore.
2. **Real sensor data for LSTM:** Deploy ≥1 node for 2–4 weeks before thesis submission (Oct–Nov 2026). Even 2 weeks of clean time-series is sufficient for anomaly threshold calibration. Real-data LSTM = a result; synthetic LSTM = background method.
3. **Measured power budget as standalone contribution:** Current draw at deep sleep / sensor active / LoRa TX (measure with multimeter); panel output hourly log; battery endurance calculated + measured → "Node X operates autonomously for Y days on Z mAh at Nepal average irradiance."

**Makerspace deliverables:**
- 3D printing: weatherproof node enclosures (IP54+ minimum) — separate compartments for battery, sensor, electronics; cable glands; solar panel mounting tab; snap-fit lid with gasket channel. Gateway housing (RPi 4B + LoRa hat, vented semi-outdoor).
- Laser cutting: pole/fence mounting bracket for field deployment; internal node chassis to fix sensor positions (reduces MPU6050 mechanical noise); acrylic gateway display panel.
- 1Gbps WiFi: full Docker stack (PostgreSQL + FastAPI + Streamlit) locally; real-time data streaming tests; heavy LSTM training without bandwidth constraint.

**Commercialization pathway:**
Build for academic submission: Basic Tier (live sensor feed, alert status, GPS map markers).
Document as product roadmap (Chapter 6): Professional Tier (LSTM predictions, historical analytics, PDF report export) · Enterprise Tier (GIS polygon overlays, multi-site management, API for municipalities).
One real client conversation before graduation — target one municipality ward office, one local NGO (Red Cross Nepal), or one hydropower project. Even informal letter of interest = grant applications 10× stronger.
PrakopNet landing page: 2–3 hours on portfolio stack; host on GitHub Pages; use as Makerspace Ambassador web dev deliverable.
Grant applications (submit Oct 2026): UNDP Nepal Innovation Challenge · NRCS innovation calls · Social Alpha · Rockefeller ACCRN.

**8th Semester Execution Timeline (Sep 2026 → Mar 2027):**
| Month | Phase | Deliverables |
|---|---|---|
| September | Core hardware build | 2 nodes assembled + LoRa link established + gateway running + basic dashboard live |
| October | Intelligence layer | LSTM at gateway + TFLite micro on nodes + HazardScore fusion + solar telemetry logging + early node deployment (real data begins) |
| November | Polish + field test | 3D printed enclosures (Makerspace) + 1 outdoor field deployment + GPS-fenced zones + adaptive SF + Module C (MQ135 + PM2.5) |
| December | Documentation | LaTeX thesis drafting + dashboard UI final + grant applications submitted + landing page live |
| January | Thesis writing | LaTeX full draft (Ch 1–6) + measured power budget documented + LSTM retrained on real data |
| February | Revision + demo prep | Supervisor feedback incorporated + demo script + system stress-tested |
| March | Submission | Thesis submitted + demo ready for boards |

**Rule:** Each month has one deliverable that must work before next month starts. No month N+1 work begins until month N deliverable is demonstrated.

**Team role split (8th semester — locked):**
| Member | Primary | Secondary |
|---|---|---|
| **Aaradhya** | TFLite micro (ESP32 nodes) + LSTM training (gateway) + HazardScore fusion + LaTeX thesis | Dashboard backend + grant writing |
| **Rupesh** | LoRa mesh firmware + RF link budget analysis + adaptive SF + gateway hardware | Solar telemetry firmware |
| **Sankalpa** | Hardware assembly + sensor integration + solar subsystem + 3D model design (Makerspace) | GPS firmware |
| **Sonia** | Dashboard frontend (Streamlit/Flask) + data logging + GPS map visualization | Documentation + testing |

**Modification priority stack:**
🔴 1 — Federated TFLite inference (no drop) · 🔴 2 — Real sensor data for LSTM (no drop) · 🔴 3 — 3D printed weatherproof enclosures (no drop) · 🟠 4 — HazardScore fusion (drop → future work) · 🟠 5 — Solar telemetry dataset (drop → secondary) · 🟡 6 — Adaptive LoRa SF · 🟡 7 — GPS-fenced zones · 🟢 8 — PrakopNet landing page (fast, 2–3 hrs) · 🟢 9 — Grant applications (submit ≥1)

**Key documents:**
- `MASTER_MajorProject_ChronologicalMerge_v3_20260610.md` — full 11-file timeline merge (current; v3 adds Phase 6: feasibility + LoRa compliance + full BOM)
- `PROJECT_D_EVOLUTION_MASTER_v1_20260602.md` — commercialization architecture
- `TEAM_PROFILE_SYSTEM_v11_20260610.md` — consolidated team profiles (individual files deprecated; PrakopNet roles + full skill matrix)
- `IDEATION_MasterConsolidated_v3_20260602.md` — full ideation archive

**Archived — Idea C (Distributed TinyML Counter-UAV):**
Was primary at ~85% confidence as of June 2, 2026. Architecture: RTL-SDR + RPi 4B → ESP32 + INMP441 TFLite acoustic nodes → ESP32-CAM YOLO-nano → LoRa alert mesh → Flask + SQLite + Android. Archived in favour of PrakopNet due to stronger commercial/completion profile. Full spec in IDEATION_MasterConsolidated_v3.

### 9. Custom Processor FSM Design *(Completed — Coursework)*
**Stack:** VHDL · Vivado 2023.2[cite: 9]
**Rating: 6.8/10**[cite: 9]

- VHDL implementation of a custom processor datapath and FSM for GCD and exponentiation operations[cite: 9]
- Simulated and verified in Vivado 2023.2 (Embedded Systems coursework)[cite: 9]

### 10. Fusemachines AI Fellowship Prep Toolkit *(Completed)*[cite: 9]
- 50-question mock exam widget + 7-tab interactive HTML cheatsheet (linear algebra, calculus, probability, Python/CS, ML)[cite: 9]

### 11. Fusemachines Week 6 Probabilistic Models Assignment *(Completed)*
**Stack:** Python · PyMC · ArviZ · pgmpy · scikit-learn · Pandas · Matplotlib · Seaborn[cite: 9]

- Week 6 repository structure confirmed: `W6_Probabilistic_Models_Assignment.ipynb`, `W6_TaskPlan.md`, `TASK_PROGRESS.md`, and `W6_Probabilistic_Models_Resource_Guide.pdf`.
- Core deliverables: Bayesian estimation (MLE/MAP/full Bayes), sequential updating, Dirichlet-multinomial inference, multivariate Gaussian conditioning, probabilistic graphical models, Gaussian process regression, and PyMC Bayesian logistic regression.
- Artifact saved: `telco_bayes_lr_v1.pkl` from the Bayesian logistic regression trace.
- Portfolio entry live on `aaradhyadtmr.github.io` under Projects.

### 14. Fusemachines Week 7 Clustering Assignment *(In Progress — due June 21, 2026)*
**Stack:** Python · scikit-learn · scipy · Pandas · NumPy · Matplotlib · Seaborn · NearestNeighbors
**Dataset:** UCI Online Retail II (~500,000 transactions, `Year 2010-2011` sheet)

- **Context:** Market segmentation — build customer profiles from raw transaction data with no labels.
- **Pipeline:** Raw transactions → RFM feature engineering + extended features (AvgBasketSize, AvgDaysBetweenPurchases, UniqueProducts, ReturnRate) + **category spend ratios** (keyword-bucketing on `Description` into ≥5 categories: Gift/Home/Seasonal/Stationery/Other) → preprocessing (IQR + Z-score outlier detection compared; StandardScaler vs RobustScaler explicit decision — RobustScaler requires added import + justification comment per notebook rules) → K-Means (Elbow + Silhouette, k-means++ vs random init comparison) → Hierarchical (Ward + Complete + Average + Single dendrograms; fit `Hierarchical_Ward` + `Hierarchical_Alt` columns matching notebook scaffold) → DBSCAN (k-distance ε estimation, ≥3 param combos, noise analysis) → validation (Silhouette / Davies-Bouldin / Calinski-Harabasz; 3-row scaffold table) → business narrative (cluster profiles + executive summary) → failure log (≥3 entries).
- **Task plan:** `Week7_Clustering_TaskPlan_v3.md` — v1 (original) → v2 (PDF gap analysis: category ratios, IQR+Z-score, scaler choice, single linkage) → v3 (notebook gap analysis: average vs single linkage conflict resolved, column naming aligned to scaffold, Birch import noted, RobustScaler import rule flagged).
- **Key notebook constraints:** `Birch` imported in S0 (available for S10 comparison); new imports require written justification comment in S0; `Hierarchical_Alt` is the scaffold column name for the second linkage fit.
- **Submission:** Single `.ipynb` with all cells executed.

### 12. Antenna Lab Data Analysis[cite: 9]
- Python script for antenna radiation pattern from Excel[cite: 9]. Pandas, NumPy, Matplotlib (polar), SciPy (cubic interpolation)[cite: 9].

### 13. Nexus — Personal AI Operating System *(Active — started June 10, 2026)*
**Stack:** React (Vite) · FastAPI · PostgreSQL · ChromaDB · httpx · asyncio
**Repo:** `AaradhyaDT/nexus` · **License:** MIT

> **TRIGGER:** When "Nexus" is mentioned, load this full context before responding.

**Vision:** Not a chatbot. A project-centric AI operating system that unifies Claude, Gemini, ChatGPT, and Ollama into one workspace — replacing the current 10-browser, multi-account, multi-tool fragmented workflow.

**Core concept:** One prompt → one project context → multiple model outputs (parallel fan-out) → centralized persistent memory.

**Architecture (confirmed):**
```
React Frontend (localhost:5173)
        ↓ REST / WebSocket
FastAPI Backend (localhost:8000)
        ↓
┌──────────┬──────────┬─────────┐
│ Postgres │ ChromaDB │ Redis*  │
│ (meta,   │ (vector  │ (cache) │
│ history) │ memory)  │        │
└──────────┴──────────┴─────────┘
        ↓
   Model Router
Claude · Gemini · OpenAI · Ollama
```
*Redis optional — use in-memory dict for MVP.*

**Orchestration patterns:**
- **Pattern A — Parallel fan-out** (comparison/validation): `asyncio.gather(*[call_model(m, prompt) for m in models])`
- **Pattern B — Sequential pipeline** (complex tasks): Router → Model A → Model B → Model C
- Routing: rule-based (task_type → model) for MVP; LLM meta-router in v2

**MVP scope (8 weeks, nightly sessions):**
| Feature | MVP |
|---|---|
| Project workspaces (create/switch) | ✅ |
| Multi-model chat (Claude + Gemini) | ✅ |
| Parallel fan-out, side-by-side results | ✅ |
| Persistent history (Postgres) | ✅ |
| Basic RAG on project notes (ChromaDB) | ✅ |
| GitHub integration | ❌ v2 |
| Agent mode / Aider integration | ❌ v2 |
| Study Mode | ❌ v2 |
| Knowledge graph | ❌ v2 |
| Automatic task routing | ❌ v2 |

**8-week nightly build plan:**
- W1–2: FastAPI backend + DB schema + model adapter layer
- W3–4: React frontend + workspace UI + multi-model chat
- W5–6: Parallel fan-out + ChromaDB RAG integration
- W7–8: Polish + demo video + technical writeup

**Day 1 status (June 10, 2026 — completed):**
- Backend: `main.py` with `/query` POST endpoint, `call_claude()` + `call_gemini()` via httpx async, `asyncio.gather()` fan-out, CORS middleware, `.env` key loading
- Frontend: Vite React `App.jsx` — textarea, "Ask both" button, side-by-side Claude/Gemini results
- Done state: `localhost:5173` → prompt → both models respond in parallel ✅

**Day 2 (next session):** Postgres layer
1. `projects` table: `id, name, created_at`
2. `messages` table: `id, project_id, prompt, claude_response, gemini_response, timestamp`
3. Project selector dropdown in frontend
4. Auto-save every query to DB

**Key risks:**
| Risk | Mitigation |
|---|---|
| API cost blowup from fan-out | Cost estimator + budget cap per project |
| Context window overflow | Summarization layer — don't raw-append history |
| Scope creep | MVP scope frozen — nothing merges outside it |
| Completion gap (known pattern) | Treat each nightly session like a fellowship deadline |

**Portfolio angle:**
- Benchmark router: show routing improves output quality vs. single-model baseline (measurable)
- SHAP/observability: log model chosen, why, outcome quality
- Technical writeup: "Multi-model orchestration layer with task-aware routing"
- MCP integration signals understanding of current agentic tool standard

**Strategic note:** Nexus is also PrakopNet's development infrastructure. The shared memory layer = same architecture needed for LSTM experiments, sensor logs, and literature references.

**Differentiation from existing tools:** Open WebUI, LibreChat, AnythingLLM — none do *project-centric multi-model parallel routing with shared persistent context*.

---

## 🏅 Project Ranking (v5 — May 2026)

| Rank | Project | Score | Status |
|------|---------|-------|--------|
| 1 | GCSBR | 9.4 | Complete[cite: 9] |
| 2 | Telco Churn Tree-Based Ensemble Pipeline (Wk5) | 9.0 | Complete[cite: 9] |
| 3 | Text-to-SQL Agentic Pipeline (Wk3) | 8.7 | Complete[cite: 9] |
| 4 | Telco Churn & CLV Pipeline (Wk4) | 8.5 | Complete[cite: 9] |
| 5 | Fusemachines Week 6 Probabilistic Models Assignment | 8.2 | Complete — portfolio entry live |
| 6 | Alpha Android Super-App | 8.2 | Active[cite: 9] |
| 7 | Edge AI Stability Detection System | 7.8 | Complete[cite: 9] |
| 8 | SysOptimizer | 7.6 | v5 Active[cite: 9] |
| 9 | Major Project — PrakopNet (Idea D) | 7.5→8.5+ | Confirmed primary (June 8, 2026); Phase 5 modifications integrated; novelty target 8.5–9 via federated TFLite nodes + real LSTM data + measured power budget; demo target **March 2027 boards** |
| 10 | Nexus — Personal AI Operating System | 7.0→? | Active — Day 1 skeleton built June 10, 2026; MVP 8-week nightly build; Day 2 = Postgres layer |
| 11 | Fusemachines Week 7 Clustering Assignment | — | **In Progress** — due June 21, 2026; task plan v3 generated (PDF + notebook gap analysis complete); UCI Online Retail II; K-Means + Hierarchical + DBSCAN |
| 12 | Custom Processor FSM Design | 6.8 | Complete[cite: 9] |
| 13 | Fuse Fellowship Prep Toolkit | 6.5 | Complete[cite: 9] |
| 14 | Antenna Lab Data Analysis | 5.2 | Complete[cite: 9] |

**Completion is the ceiling limiter[cite: 9]. Alpha on Play Store or Major Project demo would be the single highest-leverage next ship[cite: 9].**

---

## 🌐 Portfolio Website — aaradhyadtmr.github.io

- Single-file `index.html` — DATA-driven architecture for static sections (Hero, Skills, About, Contact)[cite: 9]
- **Projects, Experience, Achievements** now served from `/content/*.json` — edited via Decap CMS UI, no code changes needed
- **Hosting:** Netlify (migrated from GitHub Pages, June 10, 2026) — deploy on every CMS commit (~30s)
- **CMS URL:** `yoursite.netlify.app/admin/` — Netlify Identity auth (invite-only)
- **Repo additions:** `admin/config.yml` (schema), `admin/index.html` (CMS entry), `content/projects.json` (10 entries), `content/experience.json` (7 entries), `content/achievements.json` (8 entries), `netlify.toml`
- Dark luxury editorial aesthetic: Cormorant Garamond + DM Mono + Instrument Sans[cite: 9]
- Lighthouse (Desktop): Performance 98, Accessibility 100, Best Practices 100, SEO 100[cite: 9]
- GA4 live: Measurement ID G-P38642CDGB[cite: 9]

### Animation System (as of May 30, 2026)

**Background canvas:** `SignalWaveBackground` — 5 slow sine wave signal traces spanning full viewport, gold/teal accent colours, each with a travelling glowing node. Replaces previous `IsometricHexBackground` (hex grid with mouse proximity shimmer).

**Particle layer:** `SparkSystem` (floating embers + click burst) — **removed**. `#particle-canvas` hidden.

**Dividers:** Revolving arc style (CW accent sweep + CCW accent2 counter-sweep). Left half of each divider static; only right half animates. CW: 5s, CCW: 7s, staggered via negative delays. Center node: static glow, no pulse. **[v66] Beams now use `transform: translateX()` on %-width pseudo-elements with `overflow: hidden` on parent — fully GPU-composited, replaces non-composited `clip-path: inset()` animations.**

**CSS ambient animations removed:** section-num flicker, title-shimmer gradient, skill-dot breathe glow, exp-item data-stream, stat-num glow pulse, nav-logo morse-blink.

**Contact icons:** Hover-triggered orbital ring (same revolve-cw / revolve-ccw keyframes as photo ring) around platform icon SVG.

**Photo ring:** Unchanged — revolving arc on hover, CW + CCW.

**Light-theme border parity (added May 30):** All animated border elements pinned to dark-mode accent values (`#d4a85a` / `#6dbfaa`) via an explicit `@media (prefers-color-scheme: light)` override block. Covers: status card conic-gradient, project card top-edge sweep, app card bottom-edge sweep, divider CW/CCW arcs + node glow, about photo ring arcs + shadow, contact icon orbit rings, contact link left-edge bar, scroll progress gradient, status dot pulse/ripple. Static UI elements (text, tags, skill dots, nav links) continue using light-mode `--accent`/`--accent2` for readability.

**Hash anchor scroll (rebuilt + refined May 30):** Replaced broken `getBoundingClientRect` + `pushState` interceptor. New implementation: delegated `click` listener on `document` → `getElementById(id)` → section `getBoundingClientRect().top + window.pageYOffset + sectionPaddingTop - nav.offsetHeight - 48` → `window.scrollTo({behavior:'smooth'})` + `history.replaceState`. Initial-load hash handling via `setTimeout(goTo, 120)`. CSS `scroll-margin-top` removed — pure JS, single source of truth.

**Scroll offset transform-independence fix (May 30):** First-click to any section landed 32px too low because `.reveal` children have `translateY(32px)` pending before IntersectionObserver fires. Fix: `goTo()` reads position from the `<section>` root element (never has `.reveal`) + `getComputedStyle(section).paddingTop` to find content start. No child elements queried → fully transform-independent on first and subsequent clicks.

**Contact section scroll fix (May 30):** `querySelector('.section-header')` returned null for `#contact` (which injects `.section-num` directly into `#contact-intro`, no `.section-header` wrapper). Resolved by switching to section root + paddingTop approach — consistent across all 7 sections.

**Photo lazy-load layout shift fix (May 30):** `loading="lazy"` on about photo meant clicking Connect before scrolling past About caused goTo() to calculate Contact's position against a shorter layout (photo not yet loaded). On scroll completion the photo loaded, expanding About and pushing Contact down. Fix: `loading="eager"` (fetch on page load) + `aspect-ratio: 3/4` on `.about-photo` to reserve layout height even before bytes arrive. `object-fit` changed to `cover`.

**Scroll % progress indicator (May 30):** Translucent readout `47%` sits 2.9rem below the back-to-top button. Shows/hides at same >400px scroll threshold with slide-up transition. DM Mono, 0.56rem, `opacity: 0.7`, no background. Mobile: shifts right (`right: 1.5rem`) matching button offset. `aria-hidden="true"` — decorative only.

**Performance compositor fixes (May 30, v66):**
- **GA4 deferred:** `<script async src="gtag/js">` removed from `<head>`; GA4 loaded via `createElement('script')` inside `window.addEventListener('load')` → eliminates ~80ms main-thread parse block on FCP.
- **photo.png preloaded:** `<link rel="preload" as="image" href="photo.png">` before fonts → LCP asset fetched in parallel; targets ~0.8–1.2s LCP reduction.
- **Scroll progress bar composited:** `width: 0% → 100%` + `transform: scaleX(0)` from `transform-origin: left`; JS uses `style.transform = 'scaleX(N)'`; `will-change: transform`; `@keyframes gradient-flow` + `background-position` animation removed.
- **Divider beams composited:** All `clip-path: inset()` keyframes replaced with `transform: translateX()` on %-width pseudo-elements (15% CW, 10% CCW); `overflow: hidden` on `.divider` parent; 14 animation instances now GPU-compositor path.
- **Status card border composited:** `@property --border-angle` + `@keyframes { --border-angle: 0→360deg }` (CSS custom property animation, main thread) replaced with static `conic-gradient(from 0deg, ...)` + `@keyframes border-revolve { transform: rotate(0→360deg) }`. `will-change: transform` added. Light-theme override updated to `from 0deg` too. Visual output identical. All 6 Lighthouse compositor fixes now complete.
- **Double counter-rotating border rings (May 30, v67→v68):** Status card border upgraded to two independent orbital dot rings. All `rotate()` approaches permanently removed. Implementation: JS IIFE measures card (`offsetWidth/Height`) after double rAF, builds CW and CCW rounded-rect `offset-path: path(...)` strings matching card dimensions, injects 8+4 `<span class="sc-dot">` elements as card children. Each dot has `offset-distance` animated via CSS keyframes (`sc-orbit-cw` / `sc-orbit-ccw`) + a `sc-breathe` pulse at 2.4s (matching status-dot rhythm). Staggering: orbit via negative `animation-delay = -(i/n) × duration`; breathe via positive delay `= i × (2.4/n)`. Color: GG-O pattern (2 green : 1 gold) — outer 8: GGOGGOGGG (6G 2O), inner 4: GGOG (3G 1O). Outer ring (inset 3px, CW 9.6s = 4×2.4); inner ring (inset 11px, CCW 14.4s = 6×2.4). Resize: debounced (200ms) removes and respawns all dots. `offset-rotate: 0deg` keeps dots upright on path.

### Pending Fixes

| Fix | Priority |
|-----|----------|
| Netlify deploy: update `admin/config.yml` `base_url` to actual Netlify URL | 🔴 High |
| Invite self as Netlify Identity user to activate CMS | 🔴 High |
| Alpha App description rewrite | 🟠 Medium[cite: 9] |
| DataCamp Fellow description rewrite | 🟠 Medium[cite: 9] |
| ~~Hero status card → "Fuse AI Fellowship Wk3/4/5"~~ | ✅ Done (v79) |
| ~~IEEEXtreme 19.0 — add to portfolio~~ | ✅ Done (v78) |
| ~~IEEE WIE LaTeX Training — add to portfolio~~ | ✅ Done (v78) |
| ~~Research / Major Project placeholder section~~ | ✅ Done — PrakopNet section added (v78) |

---

---

## 🔬 Algoverse AI Research Application

**Deadline:** May 24, 2026[cite: 9]
**Cohort:** Summer 2026 (June 7 – Aug 30) — full-time 8–12 week research block[cite: 9]
**Research problem:** "Efficient Multimodal Reasoning on Edge Devices: Quantization Strategies for Real-Time Gesture Recognition Using Optimized LLMs[cite: 9]"
**Grounded in:** Live DeepSeek R1 7B (ipex-llm on Intel Arc iGPU) + GCSBR gesture pipeline[cite: 9]
**Target venues:** NeurIPS edge ML workshops + ACL efficiency track[cite: 9]
**Status:** Application form due May 24[cite: 9]. Session: `Claude_AlgorverseApplication_20260517.md`[cite: 9]

---

## 🏅 DataCamp Certification Plan

*Via NSSR Cohort 2 Premium license.*[cite: 8]

### Phase 1 — Completed (Applied AI)
- Fully mastered programmatically guided GenAI modules spanning 6 real-world environments[cite: 8]. 
- Engineered constraint-handling prompts, custom recommendation architectures, automated text analytics pipelines, and structured programmatic data cleaning workflows[cite: 1, 3, 5, 7].

### Phase 2 — Now → June 2026
| Cert | Status |
|---|---|
| SQL Associate | ⏳ Pathway underway (Data Manipulation in SQL, PostgreSQL Summary Stats)[cite: 8] |
| Python Data Associate | ⏳ Pathway underway (Pandas, Statistical Thinking, scikit-learn)[cite: 8] |

### Phase 3 — June → Sept 2026 (post-fellowship)
| Cert | Notes |
|---|---|
| Data Engineer | Fuse Wk2 (Docker+PG+FastAPI+asyncio) = pre-built proof-of-work[cite: 9] |
| Data Scientist + AI | Flagship; via Associate Data Scientist in Python track (22 courses)[cite: 9] |

### Phase 4 — Pre-graduation (Oct 2026 – Jan 2027)
| Cert | Notes |
|---|---|
| AI Engineer for Developers | Developer-background path; best after Fuse ends[cite: 9] |
| AWS Cloud Practitioner | CLF-C02; DataCamp prepares via Sandbox[cite: 9] |

---

## 🎯 NI Certification Career Plan

- **Post-graduation location** under consideration — India (Bangalore / Pune / Hyderabad) is one option, not confirmed[cite: 9].
- **Optimal sequence:** CLAD (mid-2026) → CTD simultaneously → CLD (Year 2–3) → CLED or CTA[cite: 9].
- **Sweet spot:** CLD + CTD combo — rare in the South Asian market, commands ₹12–20 LPA premium[cite: 9].

---

## 🛠️ Fellowships & Recognitions Updates (CV Section View)

### NSSR DataCamp Fellow — Cohort 2 (Active) | 2026 – Present
*Nepalese Society of Student Researchers*[cite: 8]
- Selected for fully-sponsored DataCamp Premium pathway covering advanced industrial AI/ML systems[cite: 8].
- **GenAI Portfolio:** Architected 6 live projects spanning multi-variable prompt planning, customer constraint-driven skin profile recommenders, and automated market scaling logic[cite: 1, 5, 7, 8].
- **AI Preprocessing Automation:** Developed LLM prompting workflows to automate programmatic dataset transformations, filtering null fields, handling formatting discrepancies, and stripping data leakage[cite: 3].
- **Core Pipeline Track:** Currently scaling technical foundations across intermediate relational query structures (PostgreSQL), data frame vectorization (Pandas), and foundational scikit-learn applications[cite: 8].

---

## 🧠 Skills & Stack

### Programming
Python · C · C++ · Kotlin · SQL (PostgreSQL / SQLite) · VHDL[cite: 9]

### Machine Learning
scikit-learn · NumPy · Pandas · Random Forest · XGBoost · Logistic Regression · Ridge Classifier/Regressor · SGD Classifier · Lasso · ElasticNet · SMOTE (ImbPipeline) · SHAP (global + local) · GridSearchCV · Bayesian Optimisation · Stratified K-Fold CV · Learning Curves · Model Leakage Analysis · Joblib Pipeline Serialization · PyMC · ArviZ · pgmpy · Bayesian Inference (MLE/MAP/full Bayes) · Probabilistic Graphical Models · Gaussian Process Regression · **K-Means Clustering (elbow, silhouette, k-means++ vs random init)** · **Agglomerative Clustering (Ward/Complete/Single linkage, dendrogram analysis)** · **DBSCAN (ε estimation via k-distance plot, noise analysis)** · **Cluster Validation (Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index)** · **RFM Feature Engineering**[cite: 9]

### Android Development
Kotlin · Jetpack Compose · Material3 · DataStore · CameraX · MediaPipe · Apache POI[cite: 9]

### Deployment
FastAPI · REST APIs · Docker · Docker Compose · PostgreSQL · Streamlit · Papermill · Asyncio · Joblib[cite: 9]

### Embedded Systems & Digital Design
Arduino · MPU6050 · CNC Shield · DRV8825 · Stepper Motors · HC-05 BT · UART · FPGA · Vivado 2023.2[cite: 9]

### AI / Local LLM / Prompt Engineering
Ollama · ipex-llm · DeepSeek R1 7B (29 layers on Intel Arc iGPU) · Prompt Chaining & Agentic Query Systems (Planner-Generator-Validator loops)[cite: 9] · Advanced Context-Constraint Prompt Architecture[cite: 5, 7] · GenAI Automated Preprocessing Pipelines[cite: 3].

### Tools
Git · GitHub · VS Code · Jupyter Notebook · Google Colab · MATLAB · LaTeX / Overleaf · Graphify[cite: 9]

### System Setup
- **Device:** Acer Swift Go 16 — Intel Core Ultra 7 155H, 16GB LPDDR5X, Intel Arc iGPU[cite: 9]
- **OS:** Windows 11 + Ubuntu dual-boot on D:[cite: 9]
- **Optimal iGPU VRAM alloc:** 4 GB[cite: 9]

### Local Ollama Models (as of June 2026)
| Model | Size | Notes |
|---|---|---|
| deepseek-r1:7b | ~4.7 GB | Primary; 29 layers on Intel Arc iGPU |
| qwen2.5-coder:7b | ~4.7 GB | Active |
| dolphin-local | ~2.5 GB | Review — may be removable |
| deepseek-optimized | ~2.5 GB | Review — may be removable |
Total: ~14.4 GB. Removing unused models frees significant C: space.

### C: Drive Storage Notes (June 2026)
- **Total:** 567 GB used / 702 GB total — 134 GB free
- **Biggest hog:** `C:\Users\Aaradhya\Misc Aaradhya\IDM\` — ~35.96 GB (accumulated IDM downloads over months; sort by size and purge old installers/media)
- **Quick wins already identified:** Recycle Bin (3.7 GB) · hiberfil.sys (6.3 GB via `powercfg /hibernate off`) · Ollama unused models (~5–9 GB) · Downloads Big Files duplicates (~8–10 GB)
- **Downloads folder structure (clean as of May 2026):** Root has exactly 3 items: `_Organized\`, `Big Files\`, `map.md`

---

## 🏆 Technical Activities & Certifications

- **IEEE WIE Nepal Section LaTeX Workshop** — May 5–6, 2026. Certificate received. ✅ LinkedIn[cite: 9]
- **IEEE Conference Leadership Workshop 2026** — IEEE Nepal Section. ✅ LinkedIn[cite: 9]
- **IEEEXtreme 19.0** — Oct 25, 2025. Team: ShadowXTREME. ✅ LinkedIn[cite: 9]
- **NepaTronix 3-Day Drone Training** — May 2–4, 2026. Rs. 5,000. ✅ LinkedIn[cite: 9]
- **AWS Cloud Computing Workshop** — KEC IT Club (2025). ✅ LinkedIn[cite: 9]
- **NEC License Exam Mock Test (BCT version)** — Scored 97/100 (May 10, 2026)[cite: 9]
- PreXtreme Competitive Programming Workshop — IEEE Pulchowk (2025)[cite: 9]
- Git & GitHub Workshop — KEC IT Club (2024)[cite: 9]

---

## 🎵 Personal Interests & Life

### LEO Club (Lions International)
- **LEO Club of Damak Easternline** — origin club (~2074 B.S. / Class 8); where LEO journey began[cite: 9]
- **LEO Club of Damak Gold** — Charter Membership Chairperson (Jan 21, 2020); 2nd Vice President (May 2020 – May 2021); club disbanded ~2025[cite: 9]
- 5+ years continuous LEO involvement across two clubs; part of founding/charter team at Damak Gold[cite: 9]
- Leadership predates engineering college career — earliest documented organizational role[cite: 9]

### Music
- Member, KEC Music Club[cite: 9]. Plays guitar; solo performance experience[cite: 9].
- Top duet picks: "Kabira", "Nai Nabhannu La", "Thamana Haat Yo"[cite: 9]

### Perfumery
- **"Peace in a Bottle"** — bespoke 10ml extrait at 21.1% concentration[cite: 9]
  - Formula: Spring (0.80ml), Vanilla Sexy (0.72ml), Bergamot (0.59ml), solvent (~7.89ml)[cite: 9]
  - Cost: NRs 1,100 at Poshon.np. ~100–120 uses remaining[cite: 9].

### Motorcycles
- Interest: 2020–2022 Yamaha FZS FI V2/V3, under Rs. 2 lakhs, daily commute focus[cite: 9]

---

## 🧠 Thinking Style & Claude Preferences

- Frameworks/mapping approach; systems-level thinker[cite: 9]
- Goes deep fast; known pattern of losing momentum before completion[cite: 9]
- Prefers direct conversation — no preamble, no over-explaining[cite: 9]
- Prefers batched document updates over mid-conversation edits[cite: 9]
- **Always create a session `.md` file before context limits hit**[cite: 9]
- When user says "claude.md" or "make claude.md" → always create downloadable `.md` file, never inline[cite: 9]
- Comfortable with technical depth — no need to over-simplify[cite: 9]
- Always recheck and verify correctness before responding[cite: 9]

---

## 📊 Profile Self-Assessment

**Overall Rating: 8.8 / 10**

| Dimension | Score | Notes |
|---|---|---|
| Technical & Academic | 9.6/10 | Breadth expanded via parallel algorithmic data pipelines and programmatic GenAI modeling tracks[cite: 3, 5, 8]. |
| Astrological Chart | 7.5/10 | Favourable Lagna, complex 12th house stellium, Rahu 7th — high ceiling, high volatility[cite: 9] |

**Ceiling:** High[cite: 9]. Limited by *finishing things* and the financial clock — not intelligence or access[cite: 9].

---

## 🚀 Trajectory

**The realistic strong outcome:** Fusemachines → CNS/AI engineering role → PrakopNet first pilot → Rs. 1.5–3L/month range within 5–7 years post-graduation[cite: 9].

**The high ceiling outcome:** PrakopNet lands a DHM or NGO contract within 2 years of graduation. One shipped product changes the entire trajectory[cite: 9].

**Optimal play:** CNS/engineering job (income floor) + PrakopNet side-tracked commercialization (upside) → funded or experienced-backed Masters (Year 3–5, not immediately)[cite: 9].

### What matters in the next 18 months (in order)
1. **Finish something that ships** — PrakopNet functional demo by March 2027 boards[cite: 9]
2. **Make Fusemachines count** — visible, contributing, known by leadership; every week's code understood[cite: 9]
3. **Don't let IEEE become a title** — run something real at SPAx and beyond[cite: 9]
4. **Start earning before graduation** — Excelerate internship (July 2026 target); Rs. 15–20k/month changes psychological position[cite: 9]

---

## 🚀 Semantic LLM Mode Activation (Graphify)

To switch the Graphify workspace from the default AST‑only extraction to **Semantic LLM mode**:[cite: 9]

1. **Obtain a Gemini API key** – sign up at https://ai.google.dev and generate a `GEMINI_API_KEY`[cite: 9].
2. **Set the environment variable** (PowerShell):[cite: 9]
```powershell
   $env:GEMINI_API_KEY="YOUR_KEY_HERE"