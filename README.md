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