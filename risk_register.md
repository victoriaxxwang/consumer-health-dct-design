# Risk Register: HRV Stress Detection DCT

**Study:** Real-World Validation of HRV-Based Stress Detection on Consumer Wearables  
**Version:** 1.0 (Hypothetical)  
**Last Updated:** Pre-enrollment  
**Owner:** Clinical Research Operations Program Manager

---

## Risk Register Overview

This register covers operational, technical, regulatory, and data integrity risks for the 30-day decentralized observational study. Risks are assessed at protocol finalization and reviewed at three points during the study: (1) recruitment open, (2) mid-enrollment diversity review (week 10), and (3) data lock.

**Likelihood scale:** High (>30% probability), Medium (10–30%), Low (<10%)  
**Impact scale:** High (threatens primary endpoint or study completion), Medium (threatens secondary endpoints or timeline), Low (manageable without protocol deviation)

---

## Risk 1: App Data Gaps (Device Sync Failure)

| Field | Detail |
|---|---|
| **Category** | Technical / Data Integrity |
| **Likelihood** | High |
| **Impact** | High |
| **Risk Score** | Critical |

**Description:** The study's primary endpoint depends on continuous passive HRV data collection from participant devices. Device sync failures — caused by Bluetooth disconnection, app background refresh restrictions (iOS/Android battery optimization), device battery drain, or Google Health Studies app crashes — create HRV data gaps that reduce endpoint evaluability. A participant with <70% HRV coverage over 30 days is classified as a data completeness failure and may become non-evaluable.

**Likelihood justification:** Consumer wearable research consistently reports data gap rates of 15–25% across participants due to the naturalistic, unsupervised collection environment. This risk is rated High because it is a near-certainty at the population level even if individual probability varies.

**Impact justification:** HRV data gaps directly reduce the number of evaluable EMA-to-HRV pairings available for ROC analysis, reducing statistical power. Large-scale sync failure could invalidate the primary analysis.

**Mitigation strategies:**
1. **Automated Tier 2 monitoring:** Participants with HRV gaps >4 continuous hours/day for >3 consecutive days automatically receive a troubleshooting push notification with step-by-step resolution instructions (check device charge, verify Bluetooth enabled, check app permissions, restart device).
2. **Version-lock requirement:** Compatible device firmware versions specified in protocol. Health Studies app prompts participants to reject firmware updates during the 30-day study window. Monitoring alert fires if device firmware version departs from study-approved versions.
3. **Battery and wear reminders:** Weekly automated in-app reminder to charge device nightly and maintain ≥20 hours/day wear time.
4. **Data completeness threshold:** Participants with <70% HRV coverage at day 7 receive Tier 1 automated re-engagement nudge. Participants with <50% at day 14 trigger Tier 3 coordinator outreach.
5. **Statistical plan provision:** Pre-specified sensitivity analysis excluding participants with <70% HRV coverage to assess impact of data gaps on primary endpoint.

**Residual risk:** Medium. Mitigation reduces but does not eliminate sync failures in a fully DCT, consumer-device environment.

---

## Risk 2: EMA Non-Compliance (Notification Fatigue)

| Field | Detail |
|---|---|
| **Category** | Participant Engagement / Data Integrity |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Score** | High |

**Description:** The EMA self-report is the reference standard for the primary endpoint. If participants systematically fail to respond to EMA notifications, the number of evaluable EMA-to-HRV pairings falls below the threshold needed for ROC analysis. Notification fatigue — driven by high-frequency push notifications competing with other apps — is the primary driver.

**Likelihood justification:** Ecological momentary assessment studies report average response rates of 55–80% across participants. At 3 notifications/day over 30 days (90 total prompts), the probability of at least some participants falling below 70% response rate is medium. Participants with heavy notification loads or restrictive phone notification settings are particularly at risk.

**Impact justification:** EMA responses are the reference standard; insufficient responses cannot be imputed or substituted. If the study-wide EMA response rate falls significantly below 70%, the primary endpoint has insufficient data density to support the planned ROC analysis.

**Mitigation strategies:**
1. **3x/day hard cap:** Notification frequency capped at 3 EMA prompts per day in app logic. Participants cannot receive >3 EMA notifications in any calendar day, regardless of missed prior responses.
2. **Skip option with no consequence:** Participants can skip any individual EMA prompt without penalty. Skip responses are logged separately from non-responses to distinguish intentional skips from notification failure.
3. **Participant-selected notification windows:** At enrollment, participants choose the 1-hour windows for morning, midday, and evening prompts within prescribed ranges. Self-selected windows improve response rates by aligning with participant schedules.
4. **Progressive engagement design:** EMA prompt interface is designed for 10-second completion (single tap for Likert scale item, 3 additional tap items). Minimal friction reduces abandonment after opening.
5. **Re-engagement protocol (Tier 1):** Participants with <70% ePRO completion at day 7 receive automated encouragement message.
6. **Completion incentive:** $50 gift card contingent on completing day-30 PSS-10 questionnaire maintains engagement through the full observation window.

**Residual risk:** Medium. A participant population recruited from an active Health Studies cohort (self-selected research participants) is expected to have higher baseline engagement than a general consumer sample.

---

## Risk 3: Attrition >15% (Underpowers Primary Analysis)

| Field | Detail |
|---|---|
| **Category** | Study Integrity / Statistical |
| **Likelihood** | Medium |
| **Impact** | High |
| **Risk Score** | High |

**Description:** The sample size of 500 is calculated to maintain ≥80% power under 10% expected attrition (yielding 450 evaluable participants). If attrition exceeds 15%, the evaluable sample falls below 425, which reduces power to detect the planned 5 percentage-point sensitivity difference below the acceptable 80% threshold.

**Likelihood justification:** Consumer DCT studies report 10–20% attrition over 30 days. The 10–15% range used for planning is consistent with comparable studies using similar incentive structures. Attrition >15% is possible, particularly if there are technical issues with data collection or significant life disruption in the enrolled cohort.

**Impact justification:** Loss of statistical power in a validation study threatens the study's ability to draw conclusions about algorithm performance, particularly in subgroup analyses. A severely underpowered study cannot be published or used for regulatory purposes.

**Mitigation strategies:**
1. **10% over-enrollment buffer:** Enrollment target of 500 with 450 required as evaluable at data lock. Provides a 50-participant buffer beyond the 10% attrition assumption.
2. **$50 gift card completion incentive:** IRB-approved incentive for completing the day-30 PSS-10 questionnaire. Shown to reduce attrition by 8–12% in comparable mobile health studies.
3. **"Pause" option:** Participants can pause data collection for up to 7 days without formal withdrawal. Reduces impulsive dropout during high-stress periods (ironic, given the study topic) by preserving the option to resume.
4. **Three-tier re-engagement protocol:** Graduated outreach (automated → troubleshooting push → coordinator contact) addresses the most common drivers of dropout before they become formal withdrawals.
5. **Attrition tracking dashboard:** Weekly enrollment/attrition rate tracking against pre-specified ramp curve. If attrition rate at any weekly review exceeds 5% cumulative for that week, coordinator reviews open Tier 3 cases and investigates root cause.
6. **Statistical analysis plan provision:** If evaluable sample falls below 450, a pre-specified post-hoc power calculation documents the achieved power and constrains interpretation accordingly.

**Residual risk:** Low-Medium. The combination of financial incentive, flexible pause option, and graduated re-engagement provides strong attrition mitigation for a 30-day study.

---

## Risk 4: IRB Amendment Required Mid-Study

| Field | Detail |
|---|---|
| **Category** | Regulatory |
| **Likelihood** | Low |
| **Impact** | High |
| **Risk Score** | Medium |

**Description:** Protocol deviations, unanticipated technical issues, or participant safety concerns may require submission of an IRB amendment after enrollment opens. IRB amendment approval (even expedited) typically takes 2–6 weeks and could require a temporary enrollment hold, interrupting data collection continuity.

**Likelihood justification:** Well-designed DCT protocols for minimal-risk observational studies have low IRB amendment rates. However, novel e-consent features, data pipeline changes, or participant complaints about notification frequency could trigger amendment requirements.

**Triggers for amendment (most likely scenarios):**
- Change to EMA notification frequency or timing windows
- Addition of a new optional data stream or PRO instrument
- Change to compensation structure or eligibility criteria
- Response to participant complaint requiring consent document clarification

**Mitigation strategies:**
1. **2-week IRB buffer in timeline:** 2-week gap between IRB approval and recruitment open provides time to address any conditional approval requirements before enrollment begins, reducing post-enrollment amendment likelihood.
2. **Pre-submission IRB coordinator review:** Study coordinator meets with IRB office before formal submission to review protocol sections most likely to generate conditions or questions (e-consent flow, compensation, data handling).
3. **Protocol amendment classification plan:** Pre-classify likely amendment scenarios as minor modifications (expedited review, 1–2 week turnaround) vs. significant modifications (full board review, 4–6 weeks). Enrollment hold procedures documented in advance.
4. **Data continuity plan:** If amendment requires enrollment hold, participants already enrolled continue data collection unless amendment directly affects their participation. Hold affects new enrollment only.

**Residual risk:** Low. The minimal-risk, observational nature of this study significantly reduces the likelihood of a major IRB amendment after enrollment.

---

## Risk 5: Demographic Enrollment Targets Not Met

| Field | Detail |
|---|---|
| **Category** | Health Equity / Study Validity |
| **Likelihood** | Medium |
| **Impact** | Medium |
| **Risk Score** | Medium |

**Description:** The study's diversity targets (≥30% non-white, ≥40% age 40+, ≥40% female) may not be met if recruitment via the Google Health Studies app draws disproportionately from a younger, white, urban demographic — which tends to over-represent early adopters of consumer health technology.

**Likelihood justification:** Consumer health app users skew younger and more diverse than the general population in some metrics but remain predominantly white in the U.S. achieving ≥30% non-white enrollment through passive recruitment alone is uncertain without targeted supplementary outreach.

**Impact justification:** Failure to meet diversity targets does not invalidate the primary endpoint but substantially limits the validity and generalizability of subgroup analyses, which are a core deliverable. A study that cannot report sex-stratified or race-stratified algorithm performance is a significant missed opportunity and may fail to meet the "accessible and representative" standard for publication.

**Mitigation strategies:**
1. **Mid-enrollment diversity review at week 4 (when ~50% target enrollment expected):** Enrollment demographics reviewed against targets. If any target is tracking ≥5 percentage points below goal, targeted recruitment is activated immediately.
2. **Targeted recruitment activation:** Pre-approved targeted outreach strategy for each demographic — including geo-targeted social media promotion to ZIP codes with higher non-white population density, email outreach highlighting study's health equity mission, and partner outreach to community health organizations.
3. **Enrollment monitoring dashboard:** Real-time demographic enrollment tracking visible to study coordinator and recruitment team. Early warning system for lagging demographic targets.
4. **Flexible enrollment window extension:** If diversity targets remain unmet at week 6 (2 weeks before planned close), the IRB-approved protocol permits a 2-week enrollment window extension (to week 8) without amendment, provided overall enrollment has not yet hit 500.

**Residual risk:** Low-Medium. Active mid-enrollment intervention and flexible extension window provide meaningful corrective capacity.

---

## Risk 6: Device Firmware Update Disrupts Data Stream

| Field | Detail |
|---|---|
| **Category** | Technical |
| **Likelihood** | Low |
| **Impact** | High |
| **Risk Score** | Medium |

**Description:** Consumer device manufacturers (Google, Fitbit) release firmware updates on variable schedules. An update that changes the PPG sampling rate, HRV algorithm, or API data schema could corrupt or interrupt the study data stream mid-enrollment, creating a systematic break in HRV data for participants who accept the update.

**Likelihood justification:** Firmware update frequency varies. Over a 12-week enrollment-to-collection window, the probability of at least one significant firmware update is low but non-trivial. Google's controlled device ecosystem provides more advance notice than third-party manufacturers.

**Impact justification:** A firmware-induced data stream break affecting a significant proportion of participants (particularly if device prompts all users simultaneously) could create a systematic data gap that is statistically unignorable. Unlike individual sync failures, a systematic firmware break could invalidate entire participant datasets.

**Mitigation strategies:**
1. **Version-lock requirement:** Protocol specifies minimum and maximum compatible firmware versions. The Health Studies app monitors device firmware version and notifies participants if their device has departed from the study-approved range.
2. **Automatic monitoring alert:** Automated pipeline monitoring compares incoming data schema against expected schema daily. Any schema change triggers an immediate alert to the engineering lead and study coordinator.
3. **Google advance notice:** Coordinate with Google device team to receive advance notice of firmware updates during study period. Negotiate update hold or early access for study devices if technically feasible.
4. **Protocol deviation plan:** Pre-specified plan for how to handle data collected on non-approved firmware versions — options include exclusion from primary analysis with sensitivity analysis, or data mapping to reconcile schema differences.
5. **Subgroup stratification by firmware version:** Pre-specified analysis stratifying by firmware version as a secondary exploratory analysis to detect firmware-driven performance differences.

**Residual risk:** Low. Advance coordination with the device team and automated schema monitoring substantially reduce the probability and impact of firmware disruption.

---

## Risk Register Summary

| Risk | Likelihood | Impact | Residual Risk | Status |
|---|---|---|---|---|
| App data gaps | High | High | Medium | Active mitigation |
| EMA non-compliance | Medium | High | Medium | Active mitigation |
| Attrition >15% | Medium | High | Low-Medium | Active mitigation |
| IRB amendment | Low | High | Low | Pre-emptive mitigation |
| Demographic targets | Medium | Medium | Low-Medium | Active monitoring |
| Firmware disruption | Low | High | Low | Active monitoring |

**Risk review schedule:**
- Week 6 (recruitment open): Review risks 1, 2, 3, 5 against actual data
- Week 10 (mid-enrollment review): Full risk register review; update likelihood based on observed data
- Week 20 (data lock): Retrospective risk documentation for lessons learned
