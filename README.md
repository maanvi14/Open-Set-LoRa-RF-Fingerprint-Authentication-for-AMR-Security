# Packet-Disjoint vs Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security
### "The Familiar Stranger Problem" in Physical-Layer Device Authentication

> **Conference target:** ESDA 2026

---

## The Story

A utility runs thousands of wireless smart meters. Each meter sends readings to a gateway over LoRa. To catch rogue transmitters, the gateway uses **RF fingerprinting (RFF)**: tiny hardware imperfections make each radio's signal unique. A classifier learns the registered meters and a confidence threshold decides "known" vs "stranger".

To set that threshold, engineers need example strangers. So they borrow some unfamiliar radios (**PROXY-UNKNOWN** devices), tune the threshold on them, then test on **more packets from those same radios** and report "FAR is very low, system is secure."

**The flaw:** those radios are no longer strangers. The system met them during calibration. They are **FAMILIAR STRANGERS**. A real attacker brings a **TRUE STRANGER** — a physical radio never seen in any form.

> **Research question:** With classifier, features, and frozen threshold held identical, how much does measured false acceptance change when test strangers are *familiar* (packet-disjoint) vs *true* (identity-disjoint)?
>
> We call the difference the **Familiarity Gap**:
> `ΔF​AR = FAR(identity-disjoint) − FAR(packet-disjoint)`

---

## What We Claim (and What We Do NOT Claim)

### We do NOT claim:
- First to notice proxy-vs-unseen difference
- First open-set LoRa authentication
- Any new RFF method

### We DO claim (potential methodological/measurement contribution; literature check still required):
1. A **controlled paired A/B protocol** on a calibrated, frozen threshold: same classifier + same features + same threshold + same known-device test packets; only the identity of unknown test devices changes.
2. A **named, quantified metric** (Familiarity Gap, ΔF​AR) with **device-level confidence intervals** (bootstrap over devices, not packets).
3. A **proxy-count sweep**: how does ΔF​AR change as calibration uses 0, 1, 3, 5, 10, or 15 proxy devices?
4. A **hardness explanation**: per-device FAR, nearest-enrolled-neighbour distance vs FAR, and hardware-model analysis where documented.
5. Built-in **leakage audit** (automated assertions + pytest).
6. **AMR-gateway framing** as a screening layer that complements cryptographic authentication.
7. A **remedy test (LOPO)**: Leave-One-Proxy-Out calibration — using only proxy data, estimate FAR on a held-out identity and test whether this estimate is less optimistic than the naive packet-disjoint estimate.

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
                                      ΔF​AR = FAR_B − FAR_A
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

