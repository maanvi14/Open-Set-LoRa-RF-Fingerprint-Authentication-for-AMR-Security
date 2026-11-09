# Packet-Disjoint vs Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security

> 📖 **Comprehensive Project Monograph:** For a complete, self-contained walkthrough covering mathematical formulation, real-world smart grid attack scenarios, full 292-feature breakdown, literature comparison table, all 9 publication figures, all generated tables, and reproduction guidelines, please read [**`PROJECT_MASTER_GUIDE.md`**](PROJECT_MASTER_GUIDE.md).

---

## The Story

A utility runs thousands of wireless smart meters. Each meter sends readings to a gateway over LoRa. To catch rogue transmitters, the gateway uses **RF fingerprinting (RFF)**: tiny hardware imperfections make each radio's signal unique. A classifier learns the registered meters and a confidence threshold decides "known" vs "stranger".

To set that threshold, engineers need example strangers. So they borrow some unfamiliar radios (**PROXY-UNKNOWN** devices), tune the threshold on them, then test on **more packets from those same radios** and report "FAR is very low, system is secure."

**The flaw:** those radios are no longer strangers. The system met them during calibration. They are **FAMILIAR STRANGERS**. A real attacker brings a **TRUE STRANGER** — a physical radio never seen in any form.

> **Research question:** With classifier, features, and frozen threshold held identical, how much does measured false acceptance change when test strangers are *familiar* (packet-disjoint) vs *true* (identity-disjoint)?
>
> We call the difference the **Familiarity Gap**:
> `ΔFAR = FAR(identity-disjoint) − FAR(packet-disjoint)`

---

## What We Claim (and What We Do NOT Claim)

### We do NOT claim:
- First to notice proxy-vs-unseen difference
- First open-set LoRa authentication
- Any new RFF method

### We DO claim (Core Novelty & Contributions):
1. **First Discovery & Formalization:** We formally identify and name *The Familiar Stranger Problem* in physical-layer RFF authentication, exposing how outlier calibration transforms proxy transmitters into familiar non-strangers whose test scores artificially inflate security metrics.
2. **Controlled Paired A/B Protocol:** Same classifier + same 292 baseband features + same threshold + same known-device test packets; only the identity of unknown test devices changes.
3. **Device-Matched Paired Design:** Evaluating the exact same physical devices on identical test packets at $\tau_{\text{full}}$ vs. $\tau_{(-j)}$ to eliminate device-composition confounding ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ device-level bootstrap CI: $[+0.72\%, +2.40\%]$).
4. **Device-Level Bootstrap Confidence Intervals:** Resampled over the 60 physical devices rather than pseudo-replicated episodes ($\text{FAR}_A = 12.35\%$, $95\%$ CI: $[7.01\%, 18.77\%]$; $\text{FAR}_B = 11.55\%$, $95\%$ CI: $[7.03\%, 16.53\%]$).
5. **Proxy-Count Scaling Sweep ($k \in \{0, 1, 3, 5, 10, 15\}$):** Nested prefixes and matched-FRR evaluation, revealing acute single-proxy distortion ($k=1$ yields $+19.41\%$ gap).
6. **Hardness & Hardware Grouping:** Per-device vulnerability ranges from $0.0\%$ to $98.5\%$, with top vulnerable devices clustering tightly within hardware block 4 (IDs 46–60).
7. **Availability Cost of Robust Thresholding ($\tau_{\text{robust}}$):** Reduces true stranger penetration from $11.55\%$ to $4.17\%$ at the cost of FRR surging from $8.49\%$ to $30.18\%$.
8. **Leave-One-Proxy-Out (LOPO) Remedy:** Cross-validated threshold calibration protocol evaluated against naive testing.
9. **Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$):** Temporal fusion cuts legitimate false rejection from $8.49\%$ to $3.54\%$ (boosting availability to $96.46\%$) while elevating open-set discrimination to $\text{AUROC} = 0.9670$.

---

## Key Empirical Findings

| Evaluation Metric | Condition / Method | Value | 95% Confidence Interval |
|---|---|---|---|
| **$\text{FAR}_A$ (Familiar Strangers)** | Packet-disjoint test | 12.35% | [7.01%, 18.77%] (device bootstrap) |
| **$\text{FAR}_B$ (True Strangers)** | Identity-disjoint test | 11.55% | [7.03%, 16.53%] (device bootstrap) |
| **$\Delta\text{FAR}_{\text{matched}}$** | Device-matched paired | **+1.47%** | **[+0.72%, +2.40%]** (device bootstrap) |
| **Single-proxy distortion ($k=1$)** | Proxy sweep | **+19.41%** | $\text{FAR}_A = 2.67\%$, $\text{FAR}_B = 22.08\%$ |
| **Robust threshold ($\tau_{\text{robust}}$)** | 90th-pctile proxy rejection | $\text{FAR}_B: 11.55\% \to 4.17\%$ | FRR surges from $8.49\%$ to $30.18\%$ |
| **Multi-Packet Burst Fusion ($L=5$)** | Temporal decision fusion | **$\text{FRR}: 8.49\% \to 3.54\%$** | **AUROC climbs to $0.9670$**, $\text{FAR}_B \to 10.45\%$ |
| **Closed-Set Macro $F_1$** | Enrolled authentication | 99.43% | [99.32%, 99.53%] |
| **Open-Set AUROC** | Identity-disjoint (single) | 0.9490 | [0.9367, 0.9605] |

---

## Quantitative Differentiation: Our Work vs Prior State-of-the-Art

| Dimension / Metric | Shen et al. (2022) | Hanna et al. (2021) | Zhang et al. (2024) | Cai et al. (2025) | Ma et al. (2025) | **OUR WORK (2026)** |
|---|---|---|---|---|---|---|
| **Wireless Protocol** | LoRa SX1276 | Wi-Fi / Zigbee | LoRa | LoRa | Wi-Fi | **LoRa (SX1276 COTS)** |
| **Physical Radios ($N$)** | 60 | 50 | 40 | 45 | 54 | **60 (USRP N210 Capture)** |
| **Preamble Features** | 128 (metric latent) | Deep Metric latent | CNN feature map | Contrastive latent | 64 (prototype space) | **292 complex baseband features** |
| **Closed-Set Macro-F1** | $\approx 95.33\%$ | $\approx 98\%$ (same day) | $93.85\%$ | $96.2\%$ | $94.7\%$ | **$99.43\% \pm 0.24\%$** |
| **Open-Set AUROC** | Reported ROC curves | $\approx 80\% - 98\%$ | $90.23\%$ | $\approx 92.5\%$ | $91.3\%$ | **$0.9490$ (AUROC$_B$), $0.9530$ (AUROC$_A$)** |
| **Familiar False Acceptance ($\text{FAR}_A$)** | Not isolated | Not isolated | Not isolated | Not isolated | Not isolated | **$12.35\%$** [95% CI: $7.01\%, 18.77\%$] |
| **True Stranger Penetration ($\text{FAR}_B$)** | $\approx 5\% - 15\%$ (uncalibrated) | Varying threshold | Uncalibrated OpenMax | Distance threshold | Distance threshold | **$11.55\%$** [95% CI: $7.03\%, 16.53\%$] |
| **Single-Proxy ($k=1$) Penetration** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **$22.08\%$** (vs. $\text{FAR}_A = 2.67\%$) |
| **Calibrated Familiarity Gap ($\Delta\text{FAR}$)** | None reported | None reported | None reported | None reported | None reported | **$+1.47\%$** [95% CI: $+0.72\%, +2.40\%$ matched] |
| **Peak Single-Proxy Gap ($\Delta\text{FAR}_{k=1}$)** | None reported | None reported | None reported | None reported | None reported | **$+19.41\%$** (severe threshold overfitting) |
| **Legitimate FRR at Baseline** | Not controlled | DET curve trade-off | $\approx 6.15\%$ | $\approx 5.5\%$ | $\approx 7.2\%$ | **$8.49\%$** [95% CI: $7.16\%, 10.06\%$] |
| **Robust Remedy Penetration ($\text{FAR}_{\text{robust}}$)** | Not provided | Not provided | Not provided | Not provided | Not provided | **$4.17\%$** (drops intrusion by $64\%$) |
| **Robust Availability Cost ($\text{FRR}_{\text{robust}}$)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **$30.18\%$** (surge of $+21.69\%$, peak $84.63\%$) |
| **Hardware Clustering Confound** | Mentioned model bias | None reported | None reported | None reported | None reported | **$7/8$ hardest radios in Block 4 (46–60)** |
| **Spearman $\rho$ (Device-Aggregated)** | $p < 0.001$ (pseudo-rep) | None reported | None reported | None reported | None reported | **$\rho = 0.2097$ ($p = 0.1142, n=58$)** |
| **Estimator Error (LOPO vs Naive)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **$0.0327$ (LOPO) vs $0.0323$ (Naive)** |

---

## Pipeline

```
                         ┌─────────────────────────────────────────────────┐
                         │               RAW DATASET (60 devices)           │
                         └────────────────────┬────────────────────────────┘
                                              │  Phase 2: Audit
                              ┌───────────────┼────────────────┐
                              ▼               ▼                ▼
                         ENROLLED(30)   PROXY(15)      FINAL-UNKNOWN(15)
                              │               │                │
                     ┌────────┴────────┐  ┌───┴────┐          │ (never touched until
                     │                 │  │        │           │  evaluation)
                  train(70%)  cal-val(15%) PROXY   PROXY
                             known-test(15%) _CAL   _TEST
                                   │        │        │         │
                                   └────────┘        │         │
                               Phase 5: Fit RF +     │         │
                               Calibrate τ ──────────┘         │
                               (frozen)                        │
                                   │                           │
                     ┌─────────────┴──────────────┐           │
                     │  Condition A (packet-disjoint)│          │
                     │  FAR on PROXY_TEST            │          │
                     └───────────────────────────────┘          │
                                                                │
                     ┌──────────────────────────────────────────┴──┐
                     │  Condition B (identity-disjoint)              │
                     │  FAR on FINAL_TEST                            │
                     └───────────────────────────────────────────────┘
                                      ΔFAR = FAR_B − FAR_A
```

---

## Run Instructions

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place dataset files in data/raw/
#    (see Dataset section below)

# 3. Run pipeline stage by stage
python scripts/01_audit.py          # Phase 2 — produces reports/dataset_audit.md
python scripts/02_extract_features.py  # Phase 3 — produces data/features/
python scripts/03_run_episodes.py      # Phases 4–6 — produces results/episodes/
python scripts/04_proxy_sweep.py       # Phase 7 — produces results/sweep/
python scripts/05_analyse.py           # Phase 8 + 8B — produces results/tables/
python scripts/06_make_figures_tables.py  # Phase 9 — produces results/figures/ + LaTeX
python scripts/07_burst_aggregation_experiment.py # Temporal multi-packet fusion (L in {1, 3, 5})

# 4. Run all tests
pytest tests/ -v

# 5. Quick smoke test (3 devices per group, 2 episodes)
python scripts/03_run_episodes.py --smoke
```

---

## Dataset

**LoRa_RFFI_dataset** — Shen, Zhang, Marshall, IEEE DataPort 2022
- DOI: [10.21227/qqt4-kz19](https://doi.org/10.21227/qqt4-kz19)
- Source paper: Shen et al., IEEE TIFS 2022 ([arXiv 2107.02867](https://arxiv.org/abs/2107.02867))
- Code: [github.com/gxhen/LoRa_RFFI](https://github.com/gxhen/LoRa_RFFI)
- 60 commercial LoRa devices, preamble I/Q, one USRP N210 receiver
- SF7, 125 kHz, 868.1 MHz, ~15.55 GB

**Access:** Free IEEE account required. After download, place all files in `data/raw/`.

---

## Scope Limitations

- Commercial LoRa radios, **not** real AMR meters
- One receiver, one controlled setting — cannot claim cross-receiver or deployment robustness
- Preamble-only features; no CFO feature used
- Not an impersonation/replay-attack study
- 60 physical devices total; episodes reuse them (not independent)
- Calibration assumes some labelled unknown samples are available

---

## Folder Structure

```
Minor Project/
├── README.md
├── requirements.txt
├── config.yaml
├── docs/                    # proposal PDF, notes
├── data/
│   ├── raw/                 # place dataset here
│   ├── interim/
│   └── features/
├── src/
│   ├── config.py            # load config.yaml
│   ├── audit.py             # dataset audit logic
│   ├── loader.py            # streaming HDF5 loader
│   ├── features.py          # feature extraction pipeline
│   ├── splits.py            # seeded device/packet splitting
│   ├── model.py             # Random Forest pipeline
│   ├── threshold.py         # frozen threshold calibration
│   ├── evaluate.py          # FAR, FRR, AUROC, macro-F1
│   ├── episodes.py          # multi-episode orchestration
│   ├── sweep.py             # proxy-count sweep
│   ├── lopo.py              # Leave-One-Proxy-Out calibration
│   ├── stats.py             # bootstrap CIs, Wilcoxon
│   ├── neighbours.py        # nearest-enrolled-neighbour analysis
│   ├── groups.py            # hardware-model grouping (if available)
│   ├── plots.py             # all figure generation
│   └── utils.py             # shared utilities
├── scripts/
│   ├── 01_audit.py
│   ├── 02_extract_features.py
│   ├── 03_run_episodes.py
│   ├── 04_proxy_sweep.py
│   ├── 05_analyse.py
│   └── 06_make_figures_tables.py
├── tests/
│   ├── test_splits_no_leakage.py
│   ├── test_threshold_frozen.py
│   ├── test_metrics.py
│   └── test_sweep.py
├── notebooks/
│   ├── 00_colab_runner.ipynb
│   └── 01_explore_results.ipynb
├── results/
│   ├── episodes/
│   ├── sweep/
│   ├── tables/
│   └── figures/
├── reports/
│   ├── dataset_audit.md
│   └── experiment_log.md
└── paper/
    ├── outline.md
    ├── abstract.md
    ├── references.bib
    ├── related_work_table.csv
    ├── related_work_table.md
    ├── related_work_table.tex
    ├── related_work_notes.md
    └── sections/
```

