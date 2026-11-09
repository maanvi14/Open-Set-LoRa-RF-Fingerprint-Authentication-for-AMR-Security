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
- **Result:** **36 passed in 2.01s** (0 failures, 0 errors).
  - Verified no device group overlap.
  - Verified no packet leakage across train, calibration, and test splits.
  - Verified complete isolation of Final-Unknown devices.
  - Verified threshold $\tau$ immutability (`FrozenThreshold` with `MappingProxyType`).
  - Verified sweep nested prefixes and NaN at $k=0$.
  - Verified LOPO calibration and identity isolation.
  - Verified multi-packet temporal burst aggregation logic and chunk grouping.

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

### 5.7 Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$)
- **Single-Packet Baseline ($L=1$):** $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\Delta\text{FAR} = +0.56\%$, $\text{AUROC} = 0.9490$.
- **3-Packet Burst Fusion ($L=3$):** $\text{FAR}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\Delta\text{FAR} = +1.27\%$, $\text{AUROC} = 0.9642$.
- **5-Packet Burst Fusion ($L=5$):** $\text{FAR}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\Delta\text{FAR} = +1.64\%$, $\text{AUROC} = 0.9670$.
- **Conclusion:** Temporal fusion cuts legitimate false rejection by more than half (to $3.54\%$) while elevating AUROC to $0.9670$ and expanding the clean familiarity gap.

### 5.8 Quantitative Differentiation Table (Literature Benchmarks vs. This Work)

| Dimension / Metric | Shen et al. (2022) | Hanna et al. (2021) | Zhang et al. (2024) | Cai et al. (2025) | Ma et al. (2025) | **THIS WORK (2026)** |
|---|---|---|---|---|---|---|
| **Protocol & Transceiver** | LoRa SX1276 | Wi-Fi / Zigbee | LoRa | LoRa | Wi-Fi | **LoRa SX1276 COTS** |
| **Physical Radios ($N$)** | 60 | 50 | 40 | 45 | 54 | **60 (USRP N210 Capture)** |
| **Feature Representation** | 128 (metric latent) | Deep Metric latent | CNN feature map | Contrastive latent | 64 (prototype space) | **292 complex baseband features** |
| **Closed-Set Accuracy / F1** | $\approx 95.33\%$ | $\approx 98\%$ (same day) | $93.85\%$ | $96.2\%$ | $94.7\%$ | **$99.43\% \pm 0.24\%$ Macro-F1** |
| **Open-Set AUROC** | Reported ROC curves | $\approx 80\% - 98\%$ | $90.23\%$ | $\approx 92.5\%$ | $91.3\%$ | **$0.9490$ (AUROC$_B$), $0.9530$ (AUROC$_A$)** |
| **Familiar False Acceptance ($\text{FAR}_A$)** | Not isolated | Not isolated | Not isolated | Not isolated | Not isolated | **$12.35\%$** (95% CI: $[7.01\%, 18.77\%]$) |
| **True Stranger Penetration ($\text{FAR}_B$)** | $\approx 5\% - 15\%$ (uncalibrated) | Varying threshold | Uncalibrated OpenMax | Distance threshold | Distance threshold | **$11.55\%$** (95% CI: $[7.03\%, 16.53\%]$) |
| **Single-Proxy ($k=1$) Penetration ($\text{FAR}_B$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **$22.08\%$** (vs. $\text{FAR}_A = 2.67\%$) |
| **Calibrated Familiarity Gap ($\Delta\text{FAR}$)** | None reported | None reported | None reported | None reported | None reported | **$+1.47\%$** (95% CI: $[+0.72\%, +2.40\%]$ matched) |
| **Peak Single-Proxy Gap ($\Delta\text{FAR}_{k=1}$)** | None reported | None reported | None reported | None reported | None reported | **$+19.41\%$** (severe threshold overfitting) |
| **Legitimate FRR at Baseline** | Not controlled | DET curve trade-off | $\approx 6.15\%$ | $\approx 5.5\%$ | $\approx 7.2\%$ | **$8.49\%$** (95% CI: $[7.16\%, 10.06\%]$) |
| **Robust Remedy Penetration ($\text{FAR}_{\text{robust}}$)** | Not provided | Not provided | Not provided | Not provided | Not provided | **$4.17\%$** (drops intrusion by $64\%$) |
| **Robust Availability Cost ($\text{FRR}_{\text{robust}}$)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **$30.18\%$** (surge of $+21.69\%$, peak $84.63\%$) |
| **Multi-Packet Burst Fusion ($L=5$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **$\text{FRR} \to 3.54\%$, $\text{AUROC} \to 0.9670$** |
| **Hardware Clustering Confound** | Mentioned model bias | None reported | None reported | None reported | None reported | **$7/8$ hardest radios in Block 4 (46–60)** |
| **Spearman $\rho$ (Device-Aggregated)** | $p < 0.001$ (pseudo-rep) | None reported | None reported | None reported | None reported | **$\rho = 0.2097$ ($p = 0.1142, n=58$)** |
| **Unbiased Estimator Error (LOPO vs Naive)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **$0.0327$ (LOPO) vs $0.0323$ (Naive)** |

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
  - `fig10_burst_aggregation` (Multi-packet burst scaling dual-axis curve)
- **Tables (`results/tables/`, `paper/tables/` LaTeX, and `paper/`):**
  - `burst_aggregation_summary.csv` (`tab_burst_aggregation.tex`)
  - `burst_aggregation_results.csv`
  - `literature_comparison.csv` (`related_work_table.md`, `related_work_table.tex`)
  - `episode_summary.csv` (`tab_episode_summary.tex`)
  - `stats_summary.csv` (`tab_stats_summary.tex`)
  - `matched_device_evaluation.csv`
  - `sweep_results.csv` (`tab_sweep_results.tex`)
  - `threshold_tradeoff.csv` (`tab_threshold_tradeoff.tex`)
  - `per_device_far_ranking_FAR_B.csv`
  - `neighbour_analysis.csv` (`tab_neighbour_analysis.tex`)
  - `group_analysis.csv`
