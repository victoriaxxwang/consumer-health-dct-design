# Study Design: HRV-Based Stress Detection Validation in Consumer Wearables

**Working Title:** Real-World Validation of a Photoplethysmography-Derived HRV Stress Detection Algorithm on Consumer Wearables: A Decentralized Observational Study  
**Protocol Version:** 1.0 (Hypothetical)  
**Study Type:** Prospective observational, single arm, fully decentralized  
**Regulatory Classification:** Non-significant risk (NSR) device study | IRB: Expedited review (minimal risk)

---

## Section 1 — Study Overview

### Hypothesis

A photoplethysmography (PPG)-derived heart rate variability (HRV) algorithm deployed on consumer wearables (Pixel Watch / Fitbit) can detect acute psychological stress events with ≥75% sensitivity and ≥70% specificity when validated against ecological momentary assessment (EMA) self-report as the reference standard in a free-living, real-world population.

### Scientific Rationale

HRV has been established as a reliable physiological correlate of the autonomic nervous system's response to psychological stress. Consumer wearables now passively capture sufficient PPG signal quality to derive HRV metrics (RMSSD, LF/HF ratio, SDNN) at minute-level resolution. However, published validation studies have predominantly used laboratory stressors in controlled populations — creating a significant distribution gap between benchmark performance and real-world consumer use. This study addresses that gap directly, generating evidence in a demographically representative, free-living cohort using only the device, the Google Health Studies app, and passive + active data collection — no site visits required.

### Endpoints

**Primary Endpoint:**  
Algorithm sensitivity and specificity for acute stress events, measured against EMA self-report (1–10 Likert scale, ≥7 classified as a stress event). Evaluated at a pre-specified HRV operating point using a receiver operating characteristic (ROC) curve.

**Secondary Endpoints:**
- Subgroup algorithm performance by age group (18–39, 40–59, 60+), biological sex (male/female/other), BMI category (underweight/normal/overweight/obese), and device model (Pixel Watch Gen 2/3, Fitbit Sense 2/Versa 4)
- Data completeness rate: proportion of enrolled participants with ≥70% HRV data coverage over the 30-day observation window
- App engagement retention: proportion of enrolled participants completing the week-4 PSS-10 questionnaire (30-day retention proxy)

### Study Design Rationale

**Fully decentralized:** No site visits eliminates geographic selection bias and participant burden, enabling recruitment of a nationally representative sample. The Google Health Studies app provides a validated e-consent, data collection, and participant communication platform designed for DCT execution.

**Observational, single arm:** No intervention means no requirement for randomization, blinding, or control arm. The study is purely validating an algorithm against a gold standard (EMA) in naturalistic conditions — matching the device's intended use environment.

**NSR classification:** The wearable is a passive monitoring device capturing data the participant would generate in daily life. No therapeutic intervention occurs, and the study presents no incremental physical risk. This supports an expedited IRB pathway and significantly reduces regulatory overhead.

---

## Section 2 — Participant Recruitment

### Sample Size and Power Rationale

**Target enrollment: N = 500**

Statistical power calculation: To detect a 5 percentage-point difference in algorithm sensitivity (e.g., 75% vs. 70%) with 80% power at α = 0.05 using a two-sided test requires approximately 450 evaluable participants. Assuming 10% attrition over the 30-day observation window, the enrollment target is set at 500 to ensure at least 450 evaluable participants at data lock.

Subgroup analysis adequacy: The enrolled sample of 500 (assuming minimum 450 evaluable) is sufficient to power primary subgroup comparisons (age, sex) with at least 100 participants per subgroup if diversity targets are met, enabling meaningful performance stratification without requiring additional enrollment.

### Recruitment Strategy

**Primary channel:** Google Health Studies app in-app invitation to the existing opt-in research cohort. Eligible participants meeting device ownership and demographic criteria receive a push notification describing the study and a direct link to the consent flow.

**Secondary channel:** Email outreach to current Health Studies participants who have not opened the in-app invitation within 7 days. Subject line and preview text A/B tested to optimize open rates.

**Tertiary channel:** If enrollment velocity falls below target rate at week 4 (see monitoring section), targeted social media promotion via Google's owned channels to specific demographic segments where enrollment is lagging.

**Enrollment timeline:** 8-week active recruitment window. Enrollment rate tracked weekly against a pre-specified ramp curve (weeks 1–2: 20% of target; weeks 3–5: 60% cumulative; weeks 6–8: 100%).

### Eligibility Criteria

**Inclusion:**
- Age ≥18 years
- Owns and regularly wears a compatible device (Pixel Watch Gen 2 or 3, Fitbit Sense 2, or Fitbit Versa 4) with firmware version ≥ study-specified minimum
- Active Google account linked to Google Health Studies app
- Able to complete English-language ePRO (EMA and PSS-10)
- Willing to wear the device ≥20 hours/day during the 30-day observation window

**Exclusion:**
- Diagnosed cardiac arrhythmia (atrial fibrillation, flutter, frequent ectopic beats) — confounds HRV interpretation
- Pacemaker or implantable cardiac device — confounds PPG-derived HRV
- Current pregnancy — HRV patterns differ significantly from baseline population
- Participation in another interventional study that may affect HRV (e.g., pharmacological studies involving autonomic agents)

### Diversity Enrollment Targets

The study's "accessible and representative" mandate requires that the enrolled sample reflect the demographic breadth of consumer wearable users — not the convenience sample typically enrolled in academic DCTs.

| Demographic | Target | Rationale |
|---|---|---|
| Non-white participants | ≥30% | PPG signal quality varies by skin tone; subgroup performance must be evaluated in a racially diverse sample to detect algorithmic bias |
| Participants age 40+ | ≥40% | HRV patterns change with age; stress detection algorithm must perform in middle-aged and older adults who represent a significant share of consumer health product users |
| Female participants | ≥40% | Hormonal variation and autonomic differences between biological sexes require adequate female representation to validate sex-stratified performance |

**Mid-enrollment diversity review:** At week 4 (when approximately 50% of enrollment target is expected to be reached), the study coordinator reviews enrollment demographics against targets. If any target is tracking ≥5 percentage points below goal, targeted recruitment outreach is activated for that demographic segment before enrollment closes.

### Device Access Policy / BYOD Contingency Plan

This study uses a **Bring Your Own Device (BYOD)** model: participants are expected to own a compatible consumer wearable (Pixel Watch Gen 2/3 or Fitbit Sense 2/Versa 4) at enrollment. Ownership of a compatible device is listed as an inclusion criterion.

The FDA 2023 DCT Guidance requires that sponsors using a BYOD model provide **alternative technological accommodations** so that lack of device access does not become a de facto exclusion criterion.

**BYOD contingency plan:**

1. Eligible participants who meet all other inclusion criteria but do not own a compatible device at screening are offered a **loaner device** for the 30-day study duration, shipped directly to their home address with a prepaid return label
2. The **loaner device pool is set at 5% of enrollment target (25 devices)** — sufficient to accommodate expected BYOD-ineligible participants without materially changing study operations or logistics complexity
3. Loaner device recipients are enrolled under identical protocol conditions; device type is recorded as a stratification variable and included in subgroup analysis to detect any systematic performance differences between BYOD and loaner device cohorts
4. All loaner devices are pre-configured with the Health Studies app, firmware version-locked, and factory-reset between participants to eliminate cross-participant data contamination

**Loaner device logistics:**

| Parameter | Specification |
|---|---|
| Device pool size | 25 units (5% of 500-participant target) |
| Shipment method | Tracked mail, 2-day delivery; signature required |
| Return method | Prepaid return label included in shipment |
| Firmware version | Pre-configured and locked before shipment; matches BYOD participant firmware version |
| Data pipeline | Identical to BYOD participants — same Health Studies app, same sync process, same processing pipeline |

**Health equity rationale:** The BYOD contingency plan specifically enables enrollment of lower-income participants and non-urban populations — demographics that are systematically underrepresented in academic clinical trials but are core to the study's "accessible and representative" mandate. The operational complexity of managing 25 provisioned devices is justified by the diversity targets it enables: without this accommodation, the device ownership requirement would disproportionately screen out the same populations the DCT model is designed to include.

---

## Section 3 — Decentralized Operations

### e-Consent Design

The consent process is fully app-based and designed in compliance with FDA 2023 DCT Guidance, 21 CFR Part 50, and ICH-GCP E6(R3).

**Consent flow:**
1. Participant selects "Learn More" from the in-app invitation
2. Full informed consent document presented in scrollable, plain-language format (8th-grade reading level target)
3. Audio narration option available (accessibility compliance)
4. Video summary option: 3-minute animated explainer covering study purpose, data collection, and participant rights
5. Three-question comprehension quiz — participants must answer all 3 correctly to proceed (incorrect answers redirect to relevant consent section with explanatory text)
6. Electronic signature with timestamp and IP address logging
7. Confirmation screen with participant ID and study contact information

**Withdrawal and data rights:**
- 48-hour post-consent withdrawal window: participant may withdraw without any data being retained. All data collected in the 48-hour window is deleted upon withdrawal request.
- After 48-hour window: participant may withdraw at any time. Data collected up to withdrawal date is retained (as disclosed in consent) unless participant requests deletion under applicable privacy law.
- "Pause" option (up to 7 days): participant can temporarily pause data collection without formal withdrawal, preserving their enrollment status.

### Data Streams

**Stream 1 — Passive continuous sensor data (device API):**
- HRV metrics (RMSSD, LF/HF ratio) at minute-level resolution, aggregated to 5-minute epochs for storage efficiency
- Heart rate (BPM), activity classification (sedentary/light/moderate/vigorous), sleep staging
- Data transmitted via device API → Health Studies app → encrypted Google Cloud storage on a continuous wireless sync basis (Wi-Fi preferred; cellular fallback)
- Data gaps logged and flagged for automated monitoring

**Stream 2 — Active EMA push notifications (3x/day):**
- Notification schedule: morning (8–9 AM), midday (12–1 PM), evening (6–7 PM) — participant-selected time windows at enrollment
- Prompt: "How stressed do you feel right now? (1–10)" + 3 context items: location type (home/work/commute/other), activity type (working/exercising/resting/social/other), sleep quality last night (1–5)
- 2-minute response window from notification delivery
- Participant opt: can skip any individual prompt with no consequence (no penalty applied to completeness calculation for skips vs. non-response)
- Maximum 3 notifications/day hard-capped in app to prevent notification fatigue

**Stream 3 — Weekly PSS-10 PRO questionnaire:**
- Cohen Perceived Stress Scale (10-item version) delivered in-app at end of weeks 1, 2, 3, and 4
- Validated instrument for subjective stress burden; used as a longitudinal validation complement to EMA
- Estimated completion time: 3–4 minutes
- Completion required for $50 completion incentive eligibility

### Remote Monitoring Protocol / Risk-Based Monitoring (RBM)

**Risk-Based Monitoring (RBM)** is the FDA-endorsed approach to trial oversight that replaces traditional on-site Source Data Verification (SDV) with centralized, data-driven monitoring. In a fully decentralized trial context, there are no site visits — RBM is not merely preferred, it is the only viable monitoring methodology.

This study implements RBM through a **statistical threshold-based trigger system**: rather than scheduling monitoring visits at fixed intervals, the system continuously analyzes participant data streams for patterns indicating data quality risk — completeness thresholds, sync failure patterns, and demographic enrollment drift. Monitoring action is triggered by data anomalies, not by calendar.

The **Principal Investigator (PI) retains ultimate accountability** for all data and remote participants per ICH-GCP E6(R3) §4.2 and the FDA 2023 DCT Guidance — the automated RBM system does not replace investigator oversight, it protects it by surfacing anomalies that require PI-level review before they affect data integrity at scale.

**PI accountability workflow:**
- **Tier 1 and Tier 2 triggers** are handled automatically with no human action required; the system documents trigger events and automated responses in the audit log
- **Tier 3 triggers** require study coordinator action within 1 business day of trigger; coordinator documents action taken and outcome
- Any **Tier 3 trigger unresolved within 5 business days**, or any data integrity issue affecting **>5% of enrolled participants**, automatically escalates to the PI for review and documented decision — ensuring the PI maintains meaningful oversight across all 500 participants without requiring manual review of routine monitoring events

> **Future iteration note:** Automated AI triaging tools — such as conversational health AI agents — could handle routine participant check-ins at Tier 1, provided the escalation logic ensures all flagged anomalies route to the PI rather than being resolved autonomously. This architecture would reduce coordinator burden while preserving investigator accountability as a hard constraint, not a design preference.


### Monitoring Trigger Thresholds

Automated monitoring runs daily against participant data. Three trigger tiers:

**Tier 1 — Automated re-engagement nudge (no coordinator action):**
- Trigger: participant ePRO completion <70% at day 7 (fewer than 14.7 of 21 scheduled EMA prompts responded to)
- Action: automated in-app push notification — "We noticed you've missed a few check-ins. It only takes 30 seconds! Your responses are important to the study."

**Tier 2 — Participant troubleshooting push:**
- Trigger: HRV data gaps >4 continuous hours/day for >3 consecutive days (device sync failure pattern)
- Action: automated in-app troubleshooting guide push — step-by-step instructions for checking device charge, Bluetooth settings, and app permissions. Logs support ticket in study tracking system.

**Tier 3 — Coordinator outreach (human action required):**
- Trigger: ePRO completion <50% at day 14 (fewer than 21 of 42 scheduled prompts)
- Action: study coordinator contacts participant via in-app message and email within 1 business day. Coordinator assesses barriers, offers troubleshooting, documents outreach in trial management system.

### Dropout Management

**Expected attrition:** 10–15% over 30-day window, based on comparable consumer DCT benchmarks.

**Mitigation strategies:**
- 10% over-enrollment (enroll 500, require 450 evaluable) to maintain statistical power under expected attrition
- $50 gift card completion incentive (distributed via email upon completion of day-30 PSS-10 questionnaire; IRB-approved incentive amount and delivery method)
- "Pause" protocol (see e-consent section) allows participants to temporarily pause without withdrawal, reducing impulsive dropout during high-burden periods
- Three-tier re-engagement protocol (see monitoring section) addresses the most common attrition drivers before they result in formal withdrawal

---

## Section 4 — Data Management

See `data_management_plan.md` for the full data pipeline specification, de-identification schema, and query management SLAs.

### Summary

**Pipeline:** Consumer device → Google Health Studies app (encrypted in transit) → Google Cloud Storage (encrypted at rest, AES-256) → de-identified research dataset (separate project with access controls)

**PHI handling:** Participant identity linked to study data by study ID only. No name, date of birth, or contact information stored in the research dataset. Contact information held separately by the Health Studies recruitment system and linked only via study ID.

**De-identification method:** HIPAA Safe Harbor (18 identifiers removed). Geolocation data suppressed (GPS data not collected; app usage geolocation masked to metro area). Rare demographic combinations reviewed by data manager for re-identification risk before analysis dataset is finalized.

**Data lock:** 14 days post last participant last contact (day 44 post last enrolled participant's day 30).

---

## Section 5 — Risk Register

See `risk_register.md` for the full risk register with detailed mitigation plans.

### Summary Table

| Risk | Likelihood | Impact | Primary Mitigation |
|---|---|---|---|
| App data gaps (device sync failure) | High | High | Automated Tier 2 monitoring; <70% ePRO trigger |
| EMA non-compliance (notification fatigue) | Medium | High | 3x/day max; skip option; no consequence for skips |
| Attrition >15% (underpowers study) | Medium | High | 10% over-enrollment; 3-tier re-engagement protocol |
| IRB amendment needed mid-study | Low | High | 2-week IRB buffer built into timeline; pre-IND meeting if needed |
| Demographic targets not met at 30 days | Medium | Medium | Week-4 diversity review; targeted recruitment activation |
| Device firmware update disrupts data stream | Low | High | Version-lock requirement; automated monitoring alert |

---

## Section 6 — AI Model Evaluation Plan

### Primary Analysis

**Receiver Operating Characteristic (ROC) curve** analysis comparing algorithm-detected stress events (output probability) against EMA reference standard (≥7/10 = stress event). Primary performance metrics:

- **AUC:** Area under the ROC curve — aggregate discrimination performance
- **Sensitivity** at pre-specified operating point (chosen to optimize for consumer use case: sensitivity prioritized over specificity to minimize missed stress events)
- **Specificity** at the same pre-specified operating point
- **Positive predictive value (PPV)** and **negative predictive value (NPV)** at operating point, calculated at the observed prevalence in the study population
- **95% confidence intervals** for all metrics, calculated using DeLong's method for AUC and exact binomial for sensitivity/specificity

**Operating point selection:** Pre-specified in the statistical analysis plan before data lock to prevent post-hoc optimization. Operating point chosen based on published clinical significance thresholds for HRV-based stress detection (targeting ≥75% sensitivity, ≥70% specificity).

### Subgroup Analysis

Subgroup performance is not exploratory — it is a **core deliverable of this study**, tied directly to the "accessible and representative" mandate. The algorithm must perform equitably across demographic groups, not just in aggregate.

**Required subgroup analyses:**
- Age group: 18–39 vs. 40–59 vs. 60+ (AUC and sensitivity/specificity at operating point for each)
- Biological sex: male vs. female vs. other/non-binary (minimum 50 participants in each stratum for meaningful analysis)
- BMI category: normal vs. overweight vs. obese (underweight analyzed descriptively only if N <30)
- Device model: Pixel Watch Gen 2 vs. Gen 3 vs. Fitbit Sense 2 vs. Versa 4 — to detect hardware-driven performance differences in PPG signal quality

**Bias analysis:** For any subgroup where algorithm performance falls >10 percentage points below overall performance on sensitivity or specificity, the analysis plan requires a root cause investigation (signal quality, demographic representation in algorithm training data, or data completeness differential).

### Real-World vs. Benchmark Gap Analysis

This study's results are compared against published HRV stress detection benchmarks to document the distribution shift between controlled laboratory validation and real-world consumer use:

- **Benchmark sources:** Published studies using Trier Social Stress Test (TSST) or laboratory stress paradigms with HRV-based detection
- **Distribution shift documentation:** Comparison of population characteristics (age, BMI, sex, activity level) between benchmark populations and this study cohort
- **Performance gap analysis:** If real-world AUC is lower than benchmark AUC, pre-specified hypotheses (label noise from EMA self-report, confounding from naturalistic activity patterns, device placement variation) are evaluated against available data

### Reporting Standard

The study is designed to **publication-ready standard** using the **CONSORT-DCT extension checklist** (Calvert et al., 2020) for reporting decentralized clinical trials, even though this is not an FDA submission. This ensures the study design and analysis can support:

- Peer-reviewed publication in digital health or clinical informatics journals
- Internal evidence dossier for regulatory pre-submission discussions
- Transparency and reproducibility documentation for public posting on ClinicalTrials.gov

---

## Section 7 — Operational Timeline

| Milestone | Timeline | Owner | Dependencies |
|---|---|---|---|
| IRB submission | Week 1 | Study Coordinator | Protocol finalization, e-consent document approval |
| IRB approval (expedited) | Week 3–4 | IRB Office | IRB submission |
| App/data pipeline QC sign-off | Week 5 | Engineering Lead + Data Manager | IRB approval |
| Recruitment portal opens | Week 6 | Recruitment Team | Pipeline QC, IRB approval |
| Mid-enrollment diversity review | Week 10 | Study Coordinator | 50% enrollment target reached |
| Enrollment target reached (N=500) | Week 14 | Recruitment Team | Continuous |
| Data collection complete (last participant day 30) | Week 18 | Study Coordinator | Enrollment complete |
| Data lock | Week 20 | Data Manager | Data collection complete + 14-day adjudication window |
| Statistical analysis complete | Week 24 | Biostatistician | Data lock |
| Manuscript draft complete | Week 28 | PI + Study Coordinator | Analysis complete |

**Total study duration:** ~28 weeks from IRB submission to manuscript draft.

**Key timeline risk:** IRB amendment required mid-study (estimated probability: 10–15% based on comparable DCT studies). A 2-week IRB response buffer is built into the timeline between IRB approval and recruitment open. A protocol deviation requiring IRB amendment after enrollment opens could delay data collection completion by 2–4 weeks. Mitigation: pre-IRB submission review with IRB coordinator to identify potential issues before formal submission.
