# Data Management Plan: HRV Stress Detection DCT

**Study:** Real-World Validation of HRV-Based Stress Detection on Consumer Wearables  
**Version:** 1.0 (Hypothetical)  
**Document Type:** Data Management Plan (DMP)  
**Applicable Regulations:** HIPAA, 21 CFR Part 11, FDA 2023 DCT Guidance, ICH-GCP E6(R3)

---

## 1. Data Pipeline Architecture

### End-to-End Flow

```
[Consumer Device]
     |
     | (PPG sensor → HRV/HR/activity metrics)
     | (Continuous Bluetooth transmission)
     v
[Google Health Studies App (Participant Mobile Device)]
     |
     | (TLS 1.3 encrypted transmission)
     | (EMA prompt delivery + response capture)
     | (PSS-10 weekly questionnaire capture)
     | (e-Consent signature + timestamp logging)
     v
[Google Cloud Pub/Sub Ingestion Layer]
     |
     | (Event-driven streaming ingestion)
     | (Message acknowledgement + at-least-once delivery guarantee)
     v
[Google Cloud Storage — Raw Data Bucket]
     |
     | (AES-256 encryption at rest)
     | (Access: ingestion service account only)
     | (Bucket versioning enabled; deletion protection on)
     v
[Data Processing Pipeline (Cloud Dataflow)]
     |
     | (De-identification transforms: study ID substitution, geolocation suppression)
     | (Schema validation + data quality checks)
     | (EMA-to-HRV pairing logic: 5-min pre/post EMA window HRV extraction)
     v
[Research Dataset — BigQuery Project]
     |
     | (De-identified; study ID as sole participant identifier)
     | (Access: study team with approved access list)
     | (Audit logging enabled)
     v
[Analysis Environment]
     | (Statistical analysis: Python/R with pre-registered analysis scripts)
     | (Data quality dashboard: Looker / Data Studio)
```

### Data Latency

- **Passive HRV/sensor data:** Real-time streaming with up to 15-minute lag from device to research dataset (Pub/Sub + Dataflow processing time)
- **EMA responses:** Near-real-time ingestion within 60 seconds of participant submission
- **Research dataset refresh:** Hourly batch updates from processing pipeline to BigQuery
- **Data quality dashboard:** Updated hourly from research dataset


## 1.5 — Electronic Anchor Site Designation (21 CFR Part 11 / FDA 2023 DCT Guidance)

  The FDA 2023 DCT Guidance mandates that even fully remote, paperless trials must designate a single, auditable electronic **anchor site** — a centralized location where all electronic records, source data, and audit logs are accessible to FDA inspectors on demand. This requirement does not presuppose a physical facility; in a DCT context, the anchor site is an electronic infrastructure designation, not a geographic one.

  In this study, the anchor site function is fulfilled by **Google Cloud**:

  - **Google Cloud Storage** (raw data bucket with versioning and deletion protection enabled) serves as the source data repository — the authoritative, immutable record of all participant data as received from device
  - **BigQuery** serves as the research dataset with full **Cloud Audit Logs** enabled, providing a complete, timestamped record of all query and access events
  - **Cloud Audit Logs** (Data Access logs retained for 2 years) provide the tamper-evident access trail required under 21 CFR Part 11 §11.10(e)

  **21 CFR Part 11 compliance mapping:**

  | Requirement | 21 CFR Part 11 Citation | Implementation |
  |---|---|---|
  | Trustworthy and reliable electronic records | §11.10(a) | AES-256 encryption at rest and in transit; bucket versioning prevents overwrite or deletion of source records |
  | Tamper-evident audit trails (who, what, when) | §11.10(e) | Cloud Audit Logs capture all data access and modification events with actor identity and timestamp; 2-year retention |
  | Access controls limiting data modification | §11.10(d) | Access control matrix (defined in Section 6) restricts write permissions to authorized roles only; research dataset is read-only for analysis team |
  | Electronic signatures linked to their signatories | §11.100 | e-consent timestamps, IP address logging, and consent document hash are stored in the restricted Participant Registry; signature records retained for study duration plus 2 years |

  The **Program Manager's operational responsibility** is ensuring the data pipeline from participant device to this anchor destination is continuous, lossless, and synchronized at all times. Any data integrity gaps — whether caused by sync failures, schema changes, or processing errors — must be flagged, root-caused, and resolved before data lock. Unresolved gaps at data lock constitute a protocol deviation requiring IRB notification.

  ---

  ## 2. Data Inventory

### Data Elements Collected

| Data Stream | Elements | Collection Method | Frequency |
|---|---|---|---|
| Passive HRV | RMSSD, LF/HF ratio, SDNN, pNN50 | Device PPG API | Minute-level, aggregated to 5-min epochs |
| Heart rate | BPM (instantaneous and resting) | Device PPG API | Continuous |
| Activity classification | Sedentary/light/moderate/vigorous | Device accelerometer + ML | Continuous |
| Sleep staging | Awake/light/deep/REM | Device sensors + ML | Nightly |
| EMA response | Stress level (1–10), location, activity, sleep quality | Health Studies app push | 3x/day (up to 90 responses/participant) |
| PSS-10 questionnaire | 10-item Likert scale (0–4 each item, total 0–40) | Health Studies app in-app | Weekly (4 total) |
| Device metadata | Device model, firmware version, app version | Device API | At enrollment + weekly |
| Enrollment demographics | Age group, sex, BMI, race/ethnicity | Self-reported at enrollment | Once |
| Consent data | Timestamp, IP address, quiz responses, signature hash | Health Studies app | At consent |

### Data NOT Collected

The following data is explicitly excluded from collection to minimize PHI scope:

- Full name, date of birth, address, phone number
- GPS/geolocation coordinates (app usage metadata masked to metro-area level)
- Email address (held by recruitment system only; not in research dataset)
- Photos, audio, or video
- Medical records or clinical history beyond eligibility self-report
- Financial or payment information (gift card delivery handled by separate incentive system)

---

## 3. Participant Identification and PHI Handling

### Study ID Architecture

Each enrolled participant is assigned a unique alphanumeric **Study ID** (format: `HRV-XXXXX`) at enrollment. This Study ID is the sole identifier linking participant data across all study systems.

**Study ID mapping:**
- Mapping table (Study ID ↔ Google Account identifier) stored in a separate, restricted Google Cloud project ("Participant Registry")
- Access to Participant Registry: recruitment team only (not data management or analysis team)
- Research dataset contains Study ID only — data management and analysis teams cannot reverse-lookup participant identity without Participant Registry access

### PHI Data Classification

| Data Element | PHI Status | Storage Location | Retention |
|---|---|---|---|
| Name, email, contact info | PHI | Participant Registry (restricted) | Deleted at 6 months post data lock unless required for re-contact |
| Study ID | De-identified (no PHI on its own) | Research dataset | Retained per protocol |
| Age group (not exact DOB) | De-identified | Research dataset | Retained |
| Race/ethnicity | De-identified | Research dataset | Retained |
| HRV and sensor data | De-identified (Study ID only) | Research dataset | Retained per protocol |
| Consent timestamp and IP | PHI (could identify individual) | Consent audit log (restricted) | Retained per regulatory requirement (minimum 2 years) |
| e-Consent document | PHI | Consent audit log (restricted) | Retained per regulatory requirement |

### Data Minimization Principles

1. **No unnecessary collection:** Only data elements directly required by the protocol endpoints are collected. The feasibility of collecting each data element was reviewed against protocol necessity before finalization.
2. **Age group over exact DOB:** Date of birth is not collected. Age group (5-year bands) is self-reported, providing sufficient demographic granularity for subgroup analysis without creating a quasi-identifier.
3. **Metro-area geolocation only:** Device location is not logged. App usage metadata that could reveal location is masked to metropolitan area level before ingestion.
4. **Immediate de-identification on ingestion:** The data processing pipeline performs Study ID substitution as the first transform step before data reaches the research dataset. Raw data (with Google Account identifier) is held in the raw storage bucket for a maximum of 7 days before being purged.

---

## 4. De-identification Approach

### HIPAA Safe Harbor Method

De-identification is achieved via the **HIPAA Safe Harbor method** (45 CFR §164.514(b)(2)). All 18 HIPAA Safe Harbor identifiers are either not collected (most) or explicitly suppressed (remainder):

| HIPAA Identifier | Status |
|---|---|
| Names | Not collected |
| Geographic data (smaller than state) | Geolocation suppressed; only metro-area level retained |
| Dates (except year) | Birth date not collected; event timestamps retained as relative day-in-study (Day 1–30) |
| Phone numbers | Not collected |
| Fax numbers | Not collected |
| Email addresses | Not in research dataset (Participant Registry only) |
| SSN | Not collected |
| Medical record numbers | Not collected |
| Health plan numbers | Not collected |
| Account numbers | Not collected |
| Certificate/license numbers | Not collected |
| Vehicle identifiers | Not collected |
| Device identifiers | Device model/firmware retained (not serial number) |
| Web URLs | Not collected |
| IP addresses | Not in research dataset (consent audit log only, restricted) |
| Biometric identifiers | Not collected |
| Full-face photos | Not collected |
| Any other unique identifiers | Study ID assigned (not reversible without Participant Registry access) |

### Re-identification Risk Review

After de-identification, the data manager reviews the research dataset for **rare demographic combinations** that could create re-identification risk. A combination is flagged if it has fewer than 5 participants in the dataset (k-anonymity threshold of 5). Review is performed:
- At data lock before analysis begins
- After any significant data additions (e.g., if late-enrolled participants change demographic distribution)

**Flagged combinations** are reviewed by the privacy lead. Options include:
- Aggregating to broader categories (e.g., collapsing age bands)
- Suppressing the record from the analysis dataset
- Documenting in the data use agreement that the analysis team must not attempt re-identification

---

## 5. Data Quality Management

### Automated Data Quality Dashboard

A daily automated data quality check runs against the research dataset and populates a monitoring dashboard visible to the data manager and study coordinator. Dashboard metrics:

| Metric | Good Threshold | Warning Threshold | Alert Threshold |
|---|---|---|---|
| HRV data completeness (% participants ≥70% coverage) | >85% | 75–85% | <75% |
| EMA response rate (study-wide rolling 7-day) | >65% | 55–65% | <55% |
| Daily data ingestion latency (median) | <15 min | 15–30 min | >30 min |
| Schema validation failures (count/day) | 0 | 1–2 | >2 |
| Participants with open Tier 3 coordinator flags | <5% enrolled | 5–10% | >10% |

### Data Query Management

**Query definition:** A data query is a formal data quality flag raised for a specific participant record that requires investigation and resolution. Queries are raised by the automated quality system or the data manager and tracked in the study's query management log.

**Query lifecycle:**
1. **Query raised:** Automated system or data manager identifies a data quality issue (e.g., implausible HRV value, missing required field, EMA response timestamp outside valid range)
2. **Query assigned:** Data manager assigns the query to the appropriate resolver (coordinator for participant-level issues; engineering for pipeline issues)
3. **Query resolution:** Resolver investigates and documents resolution (data corrected, data excluded, or query closed as valid outlier)
4. **SLA:** All open queries must be resolved within **5 business days** of being raised. Queries open >5 business days are escalated to the Principal Investigator.

**Query resolution options:**
- **Correction:** Data error identified and corrected with source documentation
- **Exclusion:** Data point removed from analysis dataset with reason documented
- **Confirmed valid:** Outlier investigated and confirmed as valid data point; query closed
- **Unable to resolve:** Data point excluded from primary analysis; flagged in sensitivity analysis

**Query log contents:**
- Participant Study ID
- Data element affected
- Query description and date raised
- Assigned resolver
- Resolution type and date
- Supporting documentation

### Data Lock Procedure

1. **Soft lock (Day 44, 14 days post last participant last contact):** Data manager performs final completeness check. All open queries must be resolved or escalated. No new participant data accepted after soft lock.
2. **Hard lock (Day 46):** Final database locked for analysis. Access to raw data restricted to PI and data manager only. Analysis team works from locked analysis dataset copy.
3. **Lock documentation:** Data lock certificate signed by data manager and PI, documenting: enrollment count, evaluable participant count, data completeness rates, number of queries resolved/excluded, and confirmation that de-identification review is complete.

---

## 6. Data Access and Security

### Access Control Matrix

| Role | Raw Data Bucket | Participant Registry | Research Dataset | Consent Audit Log |
|---|---|---|---|---|
| Ingestion service account | Write only | No access | No access | No access |
| Data manager | Read only | No access | Read/write | Read only |
| Study coordinator | No access | Read only | No access | Read only |
| Recruitment team | No access | Read/write | No access | No access |
| Analysis team (biostatistician) | No access | No access | Read only (locked dataset) | No access |
| PI | Read only | Read only | Read/write | Read only |

### Security Controls

- **Encryption at rest:** AES-256 for all Google Cloud Storage buckets and BigQuery datasets
- **Encryption in transit:** TLS 1.3 for all data transmission from app to ingestion layer
- **Access logging:** Cloud Audit Logs enabled for all buckets and BigQuery datasets; logs retained for 2 years
- **Principle of least privilege:** Each role has minimum access required for their function; access reviewed quarterly
- **Multi-factor authentication:** Required for all Google Cloud project accounts with data access

---

## 7. Data Retention and Destruction

### Retention Schedule

| Data Type | Retention Period | Basis |
|---|---|---|
| Research dataset (de-identified) | 7 years post study completion | Standard scientific data retention; publication support |
| Consent audit log | Minimum 2 years post study completion | 21 CFR Part 11; FDA audit readiness |
| Participant Registry (PHI) | 6 months post data lock, then deleted | Minimum necessary; re-contact period |
| Raw data bucket | 7 days post ingestion, then purged | Data minimization; PHI exposure reduction |
| Query management log | 7 years post study completion | Audit trail |

### Destruction Procedure

Participant Registry deletion (6 months post data lock):
1. Data manager schedules deletion with approval from PI
2. Google Cloud project deletion verified (cryptographic erasure of keys)
3. Destruction documented in study master file
4. Participants who requested data deletion under applicable privacy law verified as fulfilled before Registry deletion

---

## 8. Protocol Deviations Related to Data Management

**Reportable data management deviations (require IRB notification within 5 business days):**
- Unauthorized access to the Participant Registry or consent audit log
- Data breach affecting PHI of any participant
- Discovery that data from >5% of participants was collected under non-approved firmware versions without protocol provision
- Failure to honor a participant's withdrawal + data deletion request within the required timeframe

**Non-reportable protocol deviations (documented in study master file, no IRB notification required):**
- Individual query resolution exceeding 5-business-day SLA (if escalated to PI and resolved within 10 days)
- Individual participant data gap exceeding monitoring thresholds (if re-engagement attempted)
- Minor schema validation errors corrected at pipeline level without data loss

---

## 9. Data Sharing and Publication

**Data availability upon publication:**
- De-identified analysis dataset to be made available via request to PI following primary publication, subject to data use agreement
- Statistical analysis code (Python/R scripts) to be posted to the study's GitHub repository upon publication
- Study registered on ClinicalTrials.gov prior to enrollment open, with results posted within 12 months of data lock per FDAAA reporting requirements

**Data use agreement requirements for data sharing:**
- Recipient agrees not to attempt re-identification
- Recipient agrees not to share data with additional parties without PI approval
- Use restricted to health research purposes
- Compliance with applicable privacy laws (HIPAA, CCPA where applicable)
