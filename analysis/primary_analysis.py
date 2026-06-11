"""
Primary Analysis: HRV-Based Stress Detection Validation Study
Hypothetical analysis script — illustrates the planned ROC analysis approach.
Not run on real data.
"""

import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import os

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
        g_pred = (-group_df["rmssd"] >= operating_threshold).astype(int)
        tp = ((g_pred == 1) & (group_df["stress_event"] == 1)).sum()
        fn = ((g_pred == 0) & (group_df["stress_event"] == 1)).sum()
        tn = ((g_pred == 0) & (group_df["stress_event"] == 0)).sum()
        fp = ((g_pred == 1) & (group_df["stress_event"] == 0)).sum()
        g_sens = tp / (tp + fn) if (tp + fn) > 0 else float("nan")
        g_spec = tn / (tn + fp) if (tn + fp) > 0 else float("nan")
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
os.makedirs("analysis", exist_ok=True)
plt.savefig("analysis/roc_curve.png", dpi=150)
plt.show()
