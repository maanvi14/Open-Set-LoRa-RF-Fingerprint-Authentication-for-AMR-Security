# Master Experiment Log & Execution Audit

**Project:** "The Familiar Stranger Problem": Packet-Disjoint vs Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security (ESDA 2026)  
**Workspace:** `c:\Users\maanv\Minor Project`  
**Execution Timestamp:** 2026-11-09  

---

## 1. Environment & Software Stack

- **Operating System:** Windows 11 AMD64
- **Python Version:** 3.12.7
- **Core Libraries:**
  - `numpy`: 2.2.6
  - `scipy`: 1.15.2
  - `pandas`: 2.2.3
  - `scikit-learn`: 1.6.1
  - `h5py`: 3.13.0
  - `matplotlib`: 3.10.1
  - `pytest`: 7.4.4
  - `pyarrow`: 19.0.1
  - `joblib`: 1.4.2
  - `jinja2`: 3.1.6

---

## 2. Dataset & Audit Verification (Phase 2)

- **Dataset Source:** LoRa_RFFI_dataset (Shen, Zhang, Marshall, IEEE DataPort 2022, DOI: 10.21227/qqt4-kz19).
- **Physical Devices Verified:** 60 commercial LoRa transmitters.
- **Packets Verified:** 26,000 unaugmented physical packets across:
  - `LoRa_RFFI_dataset_train_1_30.h5` (Devices 1–30, 500 packets/dev)
  - `LoRa_RFFI_dataset_residential_31_40.h5` (Devices 31–40, 400 packets/dev)
  - `LoRa_RFFI_dataset_rogue_41_45.h5` (Devices 41–45, 200 packets/dev)
  - `LoRa_RFFI_dataset_other_model_46_60.h5` (Devices 46–60, 400 packets/dev)
- **Signal Layout:** 16,384 samples/packet deinterleaved to 8,192 In-phase ($I$) and 8,192 Quadrature ($Q$).
- **No CFO Feature:** Excluded in accordance with protocol guidelines.
- **Pre-trained Models:** 5 extractors in `models/` were detected and strictly bypassed.
- **Strict Loader Guard:** Fallback to augmented files strictly disabled in `src/loader.py`.

---

## 3. Feature Extraction Verification (Phase 3)

- **Feature Matrix:** 292 features per packet.
  - 10 I/Q statistical moments (mean, std, skewness, kurtosis, correlation, imbalance).
  - 4 envelope statistics (mean, std, skewness, kurtosis of $|r[n]| = \sqrt{I^2+Q^2}$).
  - 4 phase moments (unwrapped and detrended instantaneous phase).
  - 274 spectral features (full baseband complex FFT with `fftshift` average-pooled to 256 normalized magnitude bins, 4 sub-bands, 10 dominant bin indices, centroid, spread, flatness, entropy).
- **Output:** Cached to 60 `.parquet` files in `data/features/`.
- **Quality Check:** 0 NaN, 0 Infinite values across all 26,000 packets.
- **Determinism Test:** PASSED.

---

## 4. Test Suite Execution (Phase 4 & 5 Verification)

- **Command:** `pytest tests/ -v`
- **Result:** **35 passed in 3.56s** (0 failures, 0 errors).
  - Verified no device group overlap.
  - Verified no packet leakage across train, calibration, and test splits.
  - Verified complete isolation of Final-Unknown devices.
  - Verified threshold $\tau$ immutability (`FrozenThreshold` with `MappingProxyType`).
  - Verified sweep nested prefixes and NaN at $k=0$.
  - Verified LOPO calibration and identity isolation.

---

## 5. Experimental Results (Phases 6–8B)

### 5.1 Paired A/B Experiment (20 Seeded Episodes)
- **Classifier:** Pipeline(StandardScaler, RandomForestClassifier(n_estimators=300, class_weight='balanced'))
- **Closed-Set Calibration Accuracy:** $99.43\% \pm 0.24\%$ macro-$F_1$.
- **Device-Level Bootstrap Analysis ($n=60$ devices):**
  - **$\text{FAR}_A$ (Familiar Strangers, Packet-Disjoint):** $12.35\%$ (95% CI: [7.01%, 18.77%])
  - **$\text{FAR}_B$ (True Strangers, Identity-Disjoint):** $11.55\%$ (95% CI: [7.03%, 16.53%])
  - **False Rejection Rate (FRR):** $8.49\%$ (95% CI: [7.16%, 10.06%])
- **AUROC:** Condition A: $0.9530$; Condition B: $0.9490$.
- **Episode Familiarity Gap:** $\Delta\text{FAR} = +0.56\%$ (positive in 13 of 20 episodes, 65%).
- **Raw Decision Scores:** Saved per episode to `results/episodes/raw_scores_episode_*.npz`.

### 5.2 Device-Matched Paired Design (Confound Elimination)
- Evaluates identical physical devices on identical test packets at $\tau_{\text{full}}$ (familiar) vs $\tau_{(-j)}$ (unfamiliar).
- **Familiar FAR:** $11.82\% \pm 26.02\%$
- **Unfamiliar FAR:** $13.20\% \pm 27.26\%$
- **Matched Gap ($\Delta\text{FAR}_{\text{matched}}$):** **$+1.47\%$** with a **strictly positive 95% device-level bootstrap CI: $[+0.72\%, +2.40\%]$**.

### 5.3 Proxy-Count Sweep ($k$) with Nested Prefixes
- $k=0$ (Enrolled only, 95% known acceptance rule): $\text{FAR}_A = \text{NaN}$, $\text{FAR}_B = 17.91\%$, $\text{FRR} = 5.05\%$, $\Delta\text{FAR} = \text{NaN}$
- $k=1$ (1 Proxy device): $\text{FAR}_A = 2.67\%$, $\text{FAR}_B = 22.08\%$, **$\Delta\text{FAR} = +19.41\%$**, $\text{FRR} = 10.39\%$ (Acute single-proxy distortion)
- $k=3$: $\text{FAR}_A = 9.66\%$, $\text{FAR}_B = 13.76\%$, $\Delta\text{FAR} = +4.10\%$, $\text{FRR} = 9.49\%$
- $k=5$: $\text{FAR}_A = 8.37\%$, $\text{FAR}_B = 13.53\%$, $\Delta\text{FAR} = +5.16\%$, $\text{FRR} = 8.36\%$
- $k=10$: $\text{FAR}_A = 10.53\%$, $\text{FAR}_B = 12.61\%$, $\Delta\text{FAR} = +2.08\%$, $\text{FRR} = 8.49\%$
- $k=15$: $\text{FAR}_A = 11.34\%$, $\text{FAR}_B = 11.90\%$, $\Delta\text{FAR} = +0.56\%$, $\text{FRR} = 8.49\%$

### 5.4 Transmitter Hardness & Hardware Clustering
- **Top Vulnerable Transmitters (Mean $\text{FAR}_B$):** Device 48 ($65.69\%$), Device 50 ($64.66\%$), Device 46 ($63.18\%$), Device 49 ($47.19\%$), Device 54 ($43.88\%$), Device 47 ($42.65\%$).
- **Hardware Block 4 Clustering:** 7 of top 8 hardest devices belong to unaugmented hardware block 4 (IDs 46–60, "other model").
- **Device-Level Spearman Correlation:** $\rho = 0.2097$ ($p = 0.1142, n=58$ unique devices) after removing pseudo-replication.

### 5.5 Identity-Robust Threshold ($\tau_{\text{robust}}$) Trade-off
- Raising threshold from $\tau_{\text{youden}} = 0.704 \to \tau_{\text{robust}} = 0.854$ drops true stranger penetration from $11.55\% \to 4.17\%$.
- However, False Rejection Rate surges from $8.49\% \to 30.18\%$ on average (peaking at $84.63\%$).

### 5.6 Leave-One-Proxy-Out (LOPO) Remedy (Phase 8B)
- **Naive Packet-Disjoint Absolute Error:** $0.0323$
- **LOPO Absolute Error:** $0.0327$
- Absolute estimation error between LOPO and naive testing is within empirical noise.

---

## 6. Generated Figures & Tables (Phase 9 & 10)

- **Figures (`results/figures/`, PNG + PDF):**
  - `fig1_amr_architecture`
  - `fig2_pipeline`
  - `fig3_far_comparison`
  - `fig4_score_distributions` (Generated from empirical `.npz` decision score arrays)
  - `fig5_per_device_far`
  - `fig6_neighbour_distance`
  - `fig7_sweep_plot`
  - `fig8_estimator_bias`
  - `fig9_tradeoff` (Generated from real $(\text{FRR}, \text{FAR})$ pairs)
- **Tables (`results/tables/` and `paper/tables/` LaTeX):**
  - `episode_summary.csv` (`tab_episode_summary.tex`)
  - `stats_summary.csv` (`tab_stats_summary.tex`)
  - `matched_device_evaluation.csv`
  - `sweep_results.csv` (`tab_sweep_results.tex`)
  - `threshold_tradeoff.csv` (`tab_threshold_tradeoff.tex`)
  - `per_device_far_ranking_FAR_B.csv`
  - `neighbour_analysis.csv` (`tab_neighbour_analysis.tex`)
  - `group_analysis.csv`
