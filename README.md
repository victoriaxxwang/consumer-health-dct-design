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

  ```python
  """
  Primary Analysis: HRV-Based Stress Detection Validation Study
  Hypothetical analysis script — illustrates the planned ROC analysis approach.
  Not run on real data.
  """

  import pandas as pd
  import numpy as np
  from sklearn.metrics import roc_curve, auc
  import matplotlib.pyplot as plt

  # ── Load de-identified research dataset ──────────────────────────────────────
  # Columns expected: study_id, epoch_timestamp, rmssd, lf_hf_ratio, sdnn,
  #                   ema_stress_score, age_group, sex, bmi_category, device_model
  df = pd.read_csv("data/research_dataset.csv")

  # ── Define stress event (reference standard) ─────────────────────────────────
  # EMA score ≥7 on 1–10 scale = stress event per pre-specified threshold
  df["stress_event"] = (df["ema_stress_score"] >= 7).astype(int)

  # ── Primary ROC analysis ──────────────────────────────────────────────────────
  # RMSSD has an inverse relationship with stress — lower RMSSD = higher stress
  # Invert so higher score = higher stress probability
  algorithm_score = -df["rmssd"]  # pre-specified in statistical analysis plan

  fpr, tpr, thresholds = roc_curve(df["stress_event"], algorithm_score)
  roc_auc = auc(fpr, tpr)

  print(f"Primary AUC: {roc_auc:.3f}")

  # ── Operating point selection (pre-specified: target ≥75% sensitivity) ───────
  target_sensitivity = 0.75
  idx = np.argmin(np.abs(tpr - target_sensitivity))
  operating_threshold = thresholds[idx]
  sensitivity = tpr[idx]
  specificity = 1 - fpr[idx]

  print(f"Operating point threshold: {operating_threshold:.4f}")
  print(f"Sensitivity: {sensitivity:.3f}  |  Specificity: {specificity:.3f}")

  df["predicted_stress"] = (algorithm_score >= operating_threshold).astype(int)

  # ── Subgroup analysis ─────────────────────────────────────────────────────────
  subgroups = ["age_group", "sex", "bmi_category", "device_model"]

  for subgroup in subgroups:
      print(f"\n── Subgroup: {subgroup} ──")
      for group, group_df in df.groupby(subgroup):
          if len(group_df) < 50:
              print(f"  {group}: n={len(group_df)} — insufficient for meaningful analysis")
              continue
          g_fpr, g_tpr, _ = roc_curve(group_df["stress_event"], -group_df["rmssd"])
          g_auc = auc(g_fpr, g_tpr)
          g_sens = g_tpr[np.argmin(np.abs(g_tpr - target_sensitivity))]
          g_spec = 1 - g_fpr[np.argmin(np.abs(g_tpr - target_sensitivity))]
          flag = "  ⚠ >10pp gap vs. overall" if abs(g_sens - sensitivity) > 0.10 else ""
          print(f"  {group}: n={len(group_df)}, AUC={g_auc:.3f}, "
                f"Sens={g_sens:.3f}, Spec={g_spec:.3f}{flag}")

  # ── Plot ROC curve ────────────────────────────────────────────────────────────
  plt.figure(figsize=(7, 6))
  plt.plot(fpr, tpr, color="#2a6a2a", lw=2, label=f"HRV model (AUC = {roc_auc:.3f})")
  plt.plot([0, 1], [0, 1], color="#aaa", lw=1, linestyle="--", label="Chance")
  plt.scatter(fpr[idx], tpr[idx], color="#8b0000", zorder=5,
              label=f"Operating point (Sens={sensitivity:.2f}, Spec={specificity:.2f})")
  plt.xlabel("False Positive Rate (1 − Specificity)")
  plt.ylabel("True Positive Rate (Sensitivity)")
  plt.title("ROC Curve — HRV Stress Detection (Primary Analysis)")
  plt.legend(loc="lower right")
  plt.tight_layout()
  plt.savefig("analysis/roc_curve.png", dpi=150)
  plt.show()
  ```
  