# DCT Portfolio Slide Deck

  **Format:** 6-slide investor-memo style presentation  
  **Template:** Off-white (#F8F8F6) background, deep teal (#2A6B6B) accent, Inter + DM Mono typography  
  **Live preview:** Deployed via Replit — see the main README for the link  

  ---

  ## Slide Outline

  ### Slide 01 — Title
  **HRV-Based Stress Detection Validation Study**  
  A hypothetical 500-participant decentralized clinical trial validating a PPG-derived HRV stress detection algorithm on consumer wearables.  
  *Prepared by: Victoria Wang | June 2026 | Portfolio — not affiliated with Google*

  ---

  ### Slide 02 — Study Design
  **A 500-participant, fully decentralized observational study validates HRV stress detection against an EMA reference standard**

  - **Hypothesis:** PPG-derived HRV algorithm on Pixel Watch / Fitbit detects acute stress with ≥75% sensitivity and ≥70% specificity vs. EMA self-report (≥7/10 Likert)
  - **Design:** Prospective observational, single arm, NSR device classification, expedited IRB pathway
  - **Primary endpoint:** ROC curve analysis at a pre-specified operating point
  - **Sample size:** 500 enrolled (450 evaluable), powered at 80% to detect a 5 pp sensitivity difference
  - **Diversity mandate:** ≥30% non-white, ≥40% age 40+, ≥40% female — subgroup performance is a core deliverable, not an exploratory analysis

  ---

  ### Slide 03 — DCT Operations
  **The protocol orchestrates three data streams entirely on-device with no site visits**

  | Stream | Type | Description |
  |--------|------|-------------|
  | Stream 1 | Passive | HRV (RMSSD, LF/HF ratio) at 5-min epochs, HR, activity, sleep staging via device PPG API → encrypted GCS |
  | Stream 2 | Active EMA | 3x/day push notifications; participant-selected windows; 2-min response window; 3x/day hard cap |
  | Stream 3 | Weekly PSS-10 | Cohen PSS-10 questionnaire at weeks 1–4; completion required for $50 incentive |

  **Remote Monitoring (3-Tier):**
  - Tier 1: Automated nudge at <70% ePRO day 7
  - Tier 2: Troubleshooting push at >4h HRV gaps × 3 days
  - Tier 3: Coordinator outreach at <50% ePRO day 14

  **e-Consent:** FDA 2023 DCT Guidance compliant; 3-question comprehension quiz; 48-hour withdrawal window with full data deletion

  ---

  ### Slide 04 — Risk Register
  **Four of six identified risks have active automated mitigations; two require proactive monitoring**

  | Risk | Likelihood | Impact | Primary Mitigation |
  |------|------------|--------|-------------------|
  | App data gaps (sync failure) | High | High | Tier 2 auto-troubleshooting; firmware version lock |
  | EMA non-compliance | Medium | High | 3x/day cap; skip option; self-selected windows |
  | Attrition >15% | Medium | High | 10% over-enrollment; $50 incentive; pause protocol |
  | IRB amendment mid-study | Low | High | 2-week IRB buffer; pre-submission coordinator review |
  | Demographic targets not met | Medium | Medium | Week-4 diversity review; targeted outreach activation |
  | Firmware update disrupts stream | Low | High | Schema change monitoring alert; Google device team notice |

  ---

  ### Slide 05 — Data Management
  **PHI is separated at ingestion and purged within 7 days, leaving a de-identified BigQuery research dataset**

  **Pipeline:** Device → Health Studies App (TLS 1.3) → Cloud Pub/Sub → Raw GCS bucket (AES-256) → Cloud Dataflow (de-id transforms) → BigQuery research dataset

  - Participant identity linked by Study ID only; Participant Registry held in a separate restricted GCP project
  - De-identification: HIPAA Safe Harbor (18 identifiers); geolocation suppressed to metro area
  - Data lock: soft lock day 44; hard lock day 46; all queries resolved before lock
  - Retention: research dataset 7 yr | Registry deleted 6 mo post lock | Consent audit log 2 yr (21 CFR Part 11)

  ---

  ### Slide 06 — Portfolio Closing
  **This protocol demonstrates operational DCT fluency across study design, health equity, risk management, and data governance**

  - Full documentation: [github.com/victoriaxxwang/consumer-health-dct-design](https://github.com/victoriaxxwang/consumer-health-dct-design)
  - Repository contents: Study Design · Risk Register · Data Management Plan
  - Victoria Wang — Clinical Research Operations PM Portfolio

  ---

  *This slide deck is a portfolio artifact demonstrating DCT protocol design competency. It is not affiliated with Google or any sponsor organization.*
  