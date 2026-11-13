# AUDIT REPORT — Gap 3 (Availability Cost of Robust Thresholding)
> Repo: `Open-Set-LoRa-RF-Fingerprint-Authentication-for-AMR-Security`  
> Auditor scripts: `audit/TASK1_numbers.py`, `audit/burst_at_robust.py` (updated 2026-11-13)  
> **RULE: No existing `results/`, `src/`, `scripts/`, `tests/` files were modified.**

---

## 1. Mismatch Table

All values computed by `audit/TASK1_numbers.py` and `audit/burst_at_robust.py` from raw CSVs. Never rounded to match README.

| Claim | README value | Recomputed value | Source file | Estimator | Status |
|---|---|---|---|---|---|
| FAR\_B baseline | 11.55% | **11.55%** | `stats_summary.csv` | Device-level bootstrap mean (58 physical devices) | ✅ PASS |
| FAR\_B baseline | 11.55% | **11.90%** | `threshold_tradeoff.csv` | Plain episode mean (20 eps) | ❌ MISMATCH |
| FAR\_B robust | 4.17% | **4.43%** | `threshold_tradeoff.csv` | Plain episode mean (20 eps) | ❌ MISMATCH |
| FRR baseline | 8.49% | **8.49%** | `stats_summary.csv` | Episode-level bootstrap mean (20 eps) | ✅ PASS |
| FRR robust | 30.18% | **30.08%** | `threshold_tradeoff.csv` | Plain episode mean (20 eps) | ❌ MISMATCH (0.10 pp) |
| Peak FRR\_robust | 84.63% | **84.63%** | `threshold_tradeoff.csv` ep4 | Single episode maximum | ✅ PASS |
| Burst L=5 FRR | 3.54% | **3.54%** | `burst_aggregation_summary.csv` | Episode mean (20 eps) | ✅ PASS |
| Burst L=5 AUROC | 0.9670 | **0.9670** | `burst_aggregation_summary.csv` | Episode mean (20 eps) | ✅ PASS |
| Burst L=5 FAR\_B | 10.45% | **10.45%** | `burst_aggregation_summary.csv` | Episode mean (20 eps) | ✅ PASS |
| "Drops intrusion by 64%" | ~64% | **62.8%** (episode means) | `threshold_tradeoff.csv` | Episode mean, both terms | ❌ MISMATCH |
| "FRR surge +21.69pp" | +21.69pp | **+21.59pp** (ep mean) | `threshold_tradeoff.csv` | Episode mean, both terms | ❌ MISMATCH (0.10 pp) |

### Root Cause of Mismatches

**FAR\_B baseline (11.55% vs 11.90%):**  
README uses the **device-level bootstrap mean** over 58 physical stranger devices (across all episodes) from `stats_summary.csv`. The plain episode mean over 20 episodes is **11.90%** (from `threshold_tradeoff.csv`). These answer different statistical questions (physical device-level penetration vs per-episode packet acceptance). The figure scatter plot annotates the episode mean (11.9%), creating an internal inconsistency between the figure and the abstract text.

**FAR\_B robust (4.17% vs 4.43%):**  
No device-level estimate of $\text{FAR}_B$ at $\tau_{\text{robust}}$ exists in `stats_summary.csv` or any other CSV in the repository. The README value of 4.17% is **UNVERIFIED** in all data tables; the only verifiable value from `threshold_tradeoff.csv` is the episode mean of **4.43%** (exact: 4.4315%).

**FRR robust (30.18% vs 30.08%):**  
In `threshold_tradeoff.csv`, the episode mean is **30.0789%** (30.08%). The README value of 30.18% differs by **0.10 pp**.

**FRR surge (+21.69 pp vs +21.59 pp):**  
The README derives $+21.69\text{ pp}$ by subtracting $30.18 - 8.49$. From the actual data in `threshold_tradeoff.csv`, the surge is $30.0789 - 8.4860 = \mathbf{+21.59\text{ pp}}$ (exact: +21.5929 pp), resulting in a mismatch of **0.10 pp**.

**"Drops intrusion by 64%":**  
Under README's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \approx 64\%$.  
Under verified episode means: $(11.9046 - 4.4315) / 11.9046 = \mathbf{62.77\%} \approx 62.8\%$.

---

## 2. Repo-wide Search & Pooled Packet-Level Evaluation (Task 1)

### Hit Inventory for "4.17", "30.18", "21.69", and "11.55"

1. **`11.55`**:
   - `results/tables/stats_summary.csv`: Line 3 (`FAR_B,device_level,58,0.115507...`). Estimator: **device-level bootstrap mean** over 58 physical stranger devices.
   - `README.md`: lines 33, 36, 47, 50, 67.
   - `PROJECT_MASTER_GUIDE.md`: lines 140, 222, 275, 474, 532, 535.
   - `paper/abstract.md`, `paper/main.tex` (lines 33, 58, 61, 144, 165, 239), `paper/sections/paper_draft.md` (lines 19, 22, 43, 113, 144), `reports/experiment_log.md` (lines 77, 103, 127).
2. **`4.17`**:
   - Appears in `README.md` (lines 36, 50, 72), `PROJECT_MASTER_GUIDE.md` (lines 140, 227, 275, 533, 535), `paper/abstract.md` (line 7), `paper/main.tex` (lines 33, 61, 170, 239), `paper/sections/paper_draft.md` (lines 22, 48, 144), `paper/related_work_table.md` (line 35), `reports/experiment_log.md` (lines 103, 132).
   - **Does NOT appear in any CSV in `results/tables/` or JSON in `results/episodes/`.** Estimator: **UNVERIFIED**.
3. **`30.18`**:
   - Appears in `README.md` (lines 36, 50, 73), `PROJECT_MASTER_GUIDE.md` (lines 140, 228, 275, 301, 533), `paper/abstract.md` (line 7), `paper/main.tex` (lines 33, 61, 171, 239), `paper/sections/paper_draft.md` (lines 22, 49, 144), `paper/related_work_table.md` (line 36), `reports/experiment_log.md` (lines 103, 133).
   - **Does NOT appear in any CSV.** Mismatch of 0.10 pp against verified value 30.08%.
4. **`21.69`**:
   - Appears in `README.md` (line 73), `PROJECT_MASTER_GUIDE.md` (line 228), `paper/sections/paper_draft.md` (line 49), `paper/related_work_table.md` (line 36), `reports/experiment_log.md` (line 133).
   - Derived textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mismatch of 0.10 pp against verified value $+21.59\text{ pp}$.

### Pooled Packet-Level Evaluation Across 20 Episodes
Across the 20 episodes, there are exactly:
- $20 \times 6500 = 130,000$ final test stranger packets
- $20 \times 1965 = 39,300$ known test enrolled packets

Because each episode has an identical number of packets, the **pooled packet-level rates are mathematically identical to the unweighted episode means**:

```python
# Code snippet (audit/TASK1_numbers.py / pooled evaluation):
total_final_packets = sum(len(np.load(f"results/episodes/raw_scores_episode_{ep:03d}.npz")['scores_final_test']) for ep in range(20))
total_known_packets = sum(len(np.load(f"results/episodes/raw_scores_episode_{ep:03d}.npz")['scores_known_test']) for ep in range(20))
# Pooled rates:
# pooled_FAR_B(tau_youden) = 11.9046%
# pooled_FAR_B(tau_robust) = 4.4315%   (does NOT reproduce 4.17%)
# pooled_FRR(tau_youden)   = 8.4860%
# pooled_FRR(tau_robust)   = 30.0789%  (does NOT reproduce 30.18%)
```
**Conclusion:** Neither pooled packet-level evaluation nor episode-mean evaluation reproduces 4.17% or 30.18%. Both methods give 4.43% and 30.08%.

---

## 3. Burst Aggregation Threshold & Sufficiency Audit (Task 2)

1. **Threshold check in `scripts/07_burst_aggregation_experiment.py`:**
   Line 73:
   ```python
   tau = calibrate_threshold(s_val, s_pcal, method="youden").tau
   ```
   **Confirmed:** `scripts/07_burst_aggregation_experiment.py` explicitly uses **`tau_youden`**, NOT $\tau_{\text{robust}}$. Burst aggregation was never executed at $\tau_{\text{robust}}$ in the existing pipeline.

2. **Sufficiency of saved scores (`results/episodes/raw_scores_episode_*.npz`):**
   - Implemented in `audit/burst_at_robust.py`.
   - `aggregate_burst_scores` (`src/evaluate.py`, lines 138–164) requires `dev_ids` to group consecutive packets belonging to the same physical device.
   - `raw_scores_episode_*.npz` contains only 1D score arrays (`scores_known_test`, `scores_proxy_test`, `scores_final_test`, `scores_known_val`, `scores_proxy_cal`, `tau`), with no device identifiers or boundaries.
   - Devices have unequal packet counts ($3200/15 \approx 213.33$, $6500/15 \approx 433.33$, $1965/30 = 65.50$), making boundary reconstruction from flat arrays impossible.
   - For $L=1$ (trivial single packet), evaluation at $\tau_{\text{robust}}$ yields: $\text{FAR}_A = 3.97\%$, $\text{FAR}_B = 4.43\%$, $\text{FRR} = 30.08\%$, $\text{AUROC} = 0.9490$.
   - **Conclusion:** The saved scores in `raw_scores_episode_*.npz` are **NOT SUFFICIENT** to evaluate burst aggregation for $L \in \{3, 5\}$ at $\tau_{\text{robust}}$. Per instructions, execution stopped.

---

## 4. Proposed Revisions for README and Paper

> **Proposed edits only — no source files modified.**

### Proposed Revision A — Abstract / Contributions
**Current:**
> "An identity-robust threshold lowers FAR from 11.55% to 4.17% at the cost of raising FRR from 8.49% to 30.18%"

**Proposed:**
> "An identity-robust threshold lowers episode-mean true-stranger penetration ($\text{FAR}_B$) from 11.90% to 4.43% (relative drop of 62.8%), while the baseline device-level bootstrap mean is 11.55% (95% CI: [7.03%, 16.53%]); this incurs an operational availability cost, as episode-mean false rejection ($\text{FRR}$) surges from 8.49% to 30.08% (+21.59 pp, worst episode: 84.63%)."

### Proposed Revision B — Relative Reduction Claims
- Change "drops intrusion by 64%" $\to$ **"reduces episode-mean stranger penetration by 62.8%"**
- Change "FRR surge of +21.69%" $\to$ **"FRR surge of +21.59 pp"**

### Proposed Revision C — Burst Fusion Description
- Clarify that burst aggregation was evaluated at the baseline Youden threshold ($\tau_{\text{Youden}}$), not $\tau_{\text{robust}}$.
- Change panel (b) subtitle from "Burst fusion recovers availability at no FAR cost" $\to$ **"Burst fusion reduces FRR; FAR_B decreases modestly"**.

---

## 5. Figure Issues Fixed in `audit/gap3_final.png`

| Issue | Present in original | Fix in `gap3_final.png` |
|---|---|---|
| Panel (b) y-axis non-zero baseline (~3% floor) | ✅ Yes | Fixed: `ax.set_ylim(bottom=0)` |
| "3.5" label at L=5 clipped/truncated | ✅ Yes | Fixed: text labels placed above markers with vertical offset |
| Colorblind-unsafe colors | Partial | Replaced with Wong (2011) palette: #0072B2, #D55E00, #009E73 |
| Typo "ΔDeltaFAR" | ✅ Yes | Corrected to "$\Delta\text{FAR}$" |
| Subplot (b) title misrepresents operational scope | ✅ Yes | Revised to reflect baseline threshold evaluation |
| Figure caption did not state estimators | ✅ Yes | Caption explicitly states episode means over 20 episodes |

---

## 6. UNVERIFIED Items

| Item | Reason |
|---|---|
| $\text{FAR}_B$ at $\tau_{\text{robust}}$ under device-level estimator (4.17%) | Does not exist in any repository CSV or table; would require re-running bootstrap analysis over held-out device scores at $\tau_{\text{robust}}$. |
| 95% CI for $\text{FAR}_B$ robust | Not in `stats_summary.csv`. |
| 95% CI for $\text{FRR}$ robust | Not in `stats_summary.csv`. |
| 95% CI for burst $L \in \{1, 3, 5\}$ metrics | Not in `stats_summary.csv` or `burst_aggregation_summary.csv`. |
| Multi-packet burst fusion ($L \in \{3, 5\}$) at $\tau_{\text{robust}}$ | Not evaluated in repo; saved scores lack per-packet device IDs needed for grouping. |

---

## 7. Leakage Check Summary (Task 1, Item 8)

**Result: NO LEAKAGE. $\tau_{\text{robust}}$ is calibrated strictly from proxy-calibration scores.**

- `src/lopo.py` lines 221–251 (`_compute_tau_robust`): consumes `proxy_cal_scores` and `scores_known_val` only.
- `src/lopo.py` line 191: $\tau_{\text{robust}}$ calibrated from proxy calibration scores.
- `src/lopo.py` line 196: `scores_final_all` evaluated at $\tau_{\text{robust}}$ for testing only.
- `src/lopo.py` lines 128–129: Hard assertion guarantees `assert held_id not in split.final_unknown_ids`.
- `src/threshold.py` lines 134–180: `calibrate_threshold` accepts only calibration scores.

---

## 8. DeltaFAR Rise in Burst Sweeps

In unstratified burst sweeps, $\Delta\text{FAR} = \text{FAR}_B - \text{FAR}_A$ increases monotonically:
- $L=1$: $\Delta\text{FAR} = +0.56\text{ pp}$
- $L=3$: $\Delta\text{FAR} = +1.27\text{ pp}$
- $L=5$: $\Delta\text{FAR} = +1.64\text{ pp}$

Because positive $\Delta\text{FAR}$ indicates that packet-disjoint evaluation ($\text{FAR}_A$) **under-reports** true-stranger penetration relative to identity-disjoint evaluation ($\text{FAR}_B$), the paper should note this $+0.56 \to +1.64\text{ pp}$ rise as an **unmatched, CI-free observation** from unstratified sweeps, rather than definitive evidence that burst fusion amplifies familiarity bias.

---

*End of Audit Report. Generated by `audit/TASK1_numbers.py`, `audit/burst_at_robust.py`, `audit/make_gap3.py`, `audit/make_gap3_final.py`.*
