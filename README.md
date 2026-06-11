# Consumer Health DCT Design: HRV Stress Detection Validation Study

  Most of my clinical research experience has been researcher-coordinated and site-based — coordinators managing participant contact, data collected in structured environments, monitoring built around physical visits. Decentralized clinical trials invert that model: participants run their own data collection from home, there is no site infrastructure to lean on, and the operational requirements shift in specific ways as a result.

  This protocol works through what that infrastructure actually requires. The study validates an HRV-based stress detection algorithm on consumer wearables (Pixel Watch, Fitbit Sense 2) across 500 participants in a fully decentralized, no-site-visit design — recruitment, consent, and data collection all run through the Google Health Studies app.

  Built against FDA 2023 DCT Guidance, 21 CFR Part 11, and ICH-GCP E6(R3).

  > **Disclaimer:** Hypothetical study design built for portfolio purposes. Not affiliated with Google. All participant data, timelines, and scenarios are fictional.

  ## Repository Contents

  | File | Description |
  |---|---|
  | `study_design.md` | Full 7-section protocol: overview, recruitment and BYOD equity policy, DCT operations with risk-based monitoring (RBM), PI accountability framework, AI evaluation methodology, and project timeline |
  | `data_management_plan.md` | End-to-end data pipeline (Pub/Sub → Dataflow → GCS → BigQuery), 21 CFR Part 11 anchor site designation, HIPAA Safe Harbor de-identification, access control matrix, and query SLAs |
  | `risk_register.md` | Risk register with likelihood/impact ratings and documented mitigation strategies |

  ## Why I Made These Design Choices

  **Why 500 participants, not an arbitrary round number:**
  The sample size flows from a power calculation. Detecting a 5 percentage-point difference in sensitivity (75% vs. 70%) with 80% power at α = 0.05 requires ~450 evaluable participants. Assuming 10% attrition, 500 enrollees provides the buffer. The subgroup analyses (age, sex, device model) need at least 100 participants per stratum to be meaningful — that math also works at 500 with the diversity targets met.

  **Why 30 days:**
  Long enough to capture within-person stress variability across different contexts — work week, weekend, high-demand periods — without asking too much of a consumer cohort. Lab stress paradigms compress everything into an hour; that's precisely the distribution gap this study is designed to close. 30 days also aligns with comparable consumer DCT benchmarks for retention modeling.

  **Why HRV over step count or sleep staging:**
  HRV is directly tied to sympathetic/parasympathetic balance — the physiological mechanism behind acute psychological stress. Step count and sleep staging both confound stress signal with physical activity and recovery patterns. RMSSD specifically is the metric most sensitive to acute autonomic changes and least dependent on device sampling rate, which matters when you're comparing performance across four hardware variants with different PPG implementations.

  **Why EMA self-report as the reference standard instead of cortisol:**
  Cortisol is a stronger physiological ground truth, but it requires biospecimen collection — which eliminates the no-site-visit design entirely. EMA self-report introduces label noise (people misclassify their own stress state), but it reflects the ecological reality of how this algorithm would actually be used. If the algorithm is going to flag stress events in daily life, the reference standard should be the user's own perception of stress in daily life — not a lab-controlled stressor.

See [analysis/primary_analysis.py](analysis/primary_analysis.py) for the planned ROC analysis implementation.
