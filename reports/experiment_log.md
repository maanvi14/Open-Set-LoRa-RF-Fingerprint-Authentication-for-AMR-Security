# Master Experiment Log & Execution Audit

**Project:** "The Familiar Stranger Problem": Packet-Disjoint vs Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security (ESDA 2026)  
**Workspace:** `c:\Users\maanv\Minor Project`  
**Execution Timestamp:** 2026-11-09  

---

## 1. Environment & Software Stack

- **Operating System:** Windows 11 AMD64
- **Python Version:** 3.14.2
- **Core Libraries:**
  - `numpy`: 2.5.3
  - `scipy`: 1.18.1
  - `pandas`: 3.0.6
  - `scikit-learn`: 1.9.1
  - `h5py`: 3.16.0
  - `matplotlib`: 3.11.2
  - `pytest`: 9.2.0
  - `pyarrow`: 26.0.1
  - `joblib`: 1.6.0
  - `jinja2`: 3.1.6

---

## 2. Dataset & Audit Verification (Phase 2)

- **Dataset Source:** LoRa_RFFI_dataset (Shen, Zhang, Marshall, IEEE DataPort 2022).
- **Physical Devices Verified:** 60 commercial LoRa transmitters.
- **Packets Verified:** 26,000 unaugmented physical packets across:
  - `dataset_training_no_aug.h5` (Devices 1–30, 500 packets/dev)
  - `dataset_residential.h5` (Devices 31–40, 400 packets/dev)
  - `dataset_rogue.h5` (Devices 41–45, 200 packets/dev)
  - `dataset_other_device_type.h5` (Devices 46–60, 400 packets/dev)
- **Signal Layout:** 16,384 samples/packet deinterleaved to 8,192 In-phase ($I$) and 8,192 Quadrature ($Q$).
- **No CFO Feature:** Excluded in accordance with protocol guidelines.
- **Pre-trained Models:** 5 extractors in `models/` were detected and strictly bypassed.

---

## 3. Feature Extraction Verification (Phase 3)

- **Feature Matrix:** 288 features per packet.
  - 10 I/Q statistical moments (mean, std, skewness, kurtosis, correlation, imbalance).
  - 4 phase moments (unwrapped and detrended).
  - 274 spectral features (256 normalized FFT bins, 4 sub-bands, 10 dominant bin indices, centroid, spread, flatness, entropy).
- **Output:** Cached to 60 `.parquet` files in `data/features/`.
- **Quality Check:** 0 NaN, 0 Infinite values across all 26,000 packets.
- **Determinism Test:** PASSED.

---

## 4. Test Suite Execution (Phase 4 & 5 Verification)

- **Command:** `python -m pytest tests/ -v`
- **Result:** **31 passed in 2.34s** (0 failures, 0 errors).
  - Verified no device group overlap.
  - Verified no packet leakage across train, calibration, and test splits.
  - Verified complete isolation of Final-Unknown devices.
  - Verified threshold $\tau$ immutability (`FrozenThreshold` guard).

---

## 5. Experimental Results (Phases 6–8B)

### 5.1 Paired A/B Experiment (20 Episodes)
- **Classifier:** Pipeline(StandardScaler, RandomForestClassifier(n_estimators=300, class_weight='balanced'))
- **Closed-Set Calibration Accuracy:** $95.71\% \pm 0.68\%$ macro-$F_1$.
- **Condition A (Familiar Strangers, Packet-Disjoint):** $\text{FAR}_A = 17.05\% \pm 8.31\%$ (95% CI: [14.07%, 21.24%])
- **Condition B (True Strangers, Identity-Disjoint):** $\text{FAR}_B = 21.28\% \pm 8.01\%$ (95% CI: [17.79%, 24.94%])
- **Familiarity Gap:** $\Delta\text{FAR} = +4.22\% \pm 8.75\%$ (95% CI: [+0.16%, +7.75%])
- **Hypothesis Test:** Wilcoxon signed-rank test $W = 44.0$, $p = 0.0215$ (statistically significant stranger penetration increase).
- **Directional Consistency:** $\Delta\text{FAR} > 0$ in 14 of 20 episodes (70%).
- **FRR Stability:** $25.88\% \pm 6.27\%$ (strictly identical between conditions by construction).

### 5.2 Proxy-Count Sweep ($k$)
- $k=0$ (Enrolled only): $\text{FAR}_B = 63.00\%$, $\Delta\text{FAR} = +63.00\%$, $\text{FRR} = 5.29\%$
- $k=1$ (1 Proxy device): $\text{FAR}_A = 7.76\%$, $\text{FAR}_B = 26.64\%$, $\Delta\text{FAR} = +18.89\%$, $\text{FRR} = 24.37\%$
- $k=3$: $\text{FAR}_A = 12.91\%$, $\text{FAR}_B = 22.53\%$, $\Delta\text{FAR} = +9.62\%$, $\text{FRR} = 26.30\%$
- $k=5$: $\text{FAR}_A = 17.42\%$, $\text{FAR}_B = 21.63\%$, $\Delta\text{FAR} = +4.21\%$, $\text{FRR} = 26.25\%$
- $k=10$: $\text{FAR}_A = 15.27\%$, $\text{FAR}_B = 20.99\%$, $\Delta\text{FAR} = +5.71\%$, $\text{FRR} = 26.23\%$
- $k=15$: $\text{FAR}_A = 17.05\%$, $\text{FAR}_B = 21.28\%$, $\Delta\text{FAR} = +4.22\%$, $\text{FRR} = 25.88\%$

### 5.3 Transmitter Hardness & Feature Distance
- **Hardest Transmitters (Mean $\text{FAR}_B$):** Device 47 ($83.2\%$), Device 52 ($72.4\%$), Device 48 ($65.8\%$), Device 50 ($64.6\%$).
- **Nearest-Enrolled Distance vs. $\text{FAR}_B$:** Spearman $\rho = -0.2516$ ($p = 0.0000$). Devices closer to registered clusters in feature space have significantly higher penetration rates.

### 5.4 LOPO Calibration Remedy (Phase 8B)
- **Naive Packet-Disjoint Estimation Bias:** $-0.0422$
- **Leave-One-Proxy-Out (LOPO) Estimation Bias:** $-0.0281$ (33.4% reduction in optimism bias)
- **Identity-Robust Threshold:** Enforcing held-out stranger FAR $\le 0.05$ raises threshold $\tau$ from $0.60 \to 0.81$.

---

## 6. Generated Figures & Tables (Phase 9 & 10)

- **Figures (`results/figures/`, PNG + PDF):**
  - `fig1_amr_architecture`
  - `fig2_pipeline`
  - `fig3_far_comparison`
  - `fig4_score_distributions`
  - `fig5_per_device_far`
  - `fig6_neighbour_distance`
  - `fig7_sweep_plot`
  - `fig8_estimator_bias`
  - `fig9_tradeoff`
- **Tables (`results/tables/` and `paper/tables/`):**
  - `episode_summary.csv` / `.tex`
  - `stats_summary.csv` / `.tex`
  - `sweep_results.csv` / `.tex`
  - `per_device_far_ranking_FAR_B.csv`
  - `lopo_bias.csv` / `.tex`
  - `threshold_tradeoff.csv` / `.tex`
  - `neighbour_analysis.csv` / `.tex`
- **Related Work Comparison (`paper/`):**
  - `related_work_table.csv`, `.md`, `.tex`
  - `related_work_notes.md` (fully referenced with URLs and section citations)

