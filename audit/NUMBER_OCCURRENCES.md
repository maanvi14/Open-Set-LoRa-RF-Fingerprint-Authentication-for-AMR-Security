# Repository Number Occurrences & Audit Scan

This table logs every detected occurrence of headline numerical claims across the repository,
verifying each against empirical result files (`results/tables/*.csv`, `results/episodes/*.json`, `results/sweep/*.csv`).

| File | Line | Number | Surrounding Text | Verified Ground Truth | Status |
|---|---|---|---|---|---|
| `audit/AUDIT_REPORT.md` | 14 | `11.55` | `\| FAR\_B baseline \| 11.55% \| **11.55%** \| `stats_summary...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 15 | `11.55` | `\| FAR\_B baseline \| 11.55% \| **11.90%** \| `threshold_tra...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 15 | `11.90` | `... FAR\_B baseline \| 11.55% \| **11.90%** \| `threshold_tradeoff.csv` ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/AUDIT_REPORT.md` | 16 | `4.17` | `\| FAR\_B robust \| 4.17% \| **4.43%** \| `threshold_trad...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 16 | `4.43` | `\| FAR\_B robust \| 4.17% \| **4.43%** \| `threshold_tradeoff.csv` ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 17 | `8.49` | `\| FRR baseline \| 8.49% \| **8.49%** \| `stats_summary....` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/AUDIT_REPORT.md` | 18 | `30.18` | `\| FRR robust \| 30.18% \| **30.08%** \| `threshold_tra...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 18 | `30.08` | `\| FRR robust \| 30.18% \| **30.08%** \| `threshold_tradeoff.csv` ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 19 | `84.63` | `\| Peak FRR\_robust \| 84.63% \| **84.63%** \| `threshold_tra...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/AUDIT_REPORT.md` | 20 | `3.54` | `\| Burst L=5 FRR \| 3.54% \| **3.54%** \| `burst_aggregat...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/AUDIT_REPORT.md` | 21 | `0.9670` | `\| Burst L=5 AUROC \| 0.9670 \| **0.9670** \| `burst_aggrega...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/AUDIT_REPORT.md` | 22 | `10.45` | `\| Burst L=5 FAR\_B \| 10.45% \| **10.45%** \| `burst_aggrega...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/AUDIT_REPORT.md` | 23 | `64%` | `\| "Drops intrusion by 64%" \| ~64% \| **62.8%** (episode ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/AUDIT_REPORT.md` | 23 | `62.8%` | `... intrusion by 64%" \| ~64% \| **62.8%** (episode means) \| `threshol...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 24 | `21.69` | `\| "FRR surge +21.69pp" \| +21.69pp \| **+21.59pp** ...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 24 | `21.59` | `...rge +21.69pp" \| +21.69pp \| **+21.59pp** (ep mean) \| `threshold_tr...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 28 | `11.55` | `**FAR\_B baseline (11.55% vs 11.90%):**` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 28 | `11.90` | `**FAR\_B baseline (11.55% vs 11.90%):**` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/AUDIT_REPORT.md` | 29 | `11.90` | `...de mean over 20 episodes is **11.90%** (from `threshold_tradeoff.c...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/AUDIT_REPORT.md` | 31 | `4.17` | `**FAR\_B robust (4.17% vs 4.43%):**` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 31 | `4.43` | `**FAR\_B robust (4.17% vs 4.43%):**` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 32 | `4.17` | `...pository. The README value of 4.17% is **UNVERIFIED** in all data...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 32 | `4.43` | `...csv` is the episode mean of **4.43%** (exact: 4.4315%).` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 34 | `30.18` | `**FRR robust (30.18% vs 30.08%):**` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 34 | `30.08` | `**FRR robust (30.18% vs 30.08%):**` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 35 | `30.18` | `...(30.08%). The README value of 30.18% differs by **0.10 pp**.` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 35 | `30.08` | `...episode mean is **30.0789%** (30.08%). The README value of 30.18% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 37 | `21.69` | `**FRR surge (+21.69 pp vs +21.59 pp):**` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 37 | `21.59` | `**FRR surge (+21.69 pp vs +21.59 pp):**` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 38 | `30.18` | `...69\text{ pp}$ by subtracting $30.18 - 8.49$. From the actual data...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 38 | `21.69` | `The README derives $+21.69\text{ pp}$ by subtracting $30...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 38 | `21.59` | `... $30.0789 - 8.4860 = \mathbf{+21.59\text{ pp}}$ (exact: +21.5929 ...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 38 | `8.49` | `... pp}$ by subtracting $30.18 - 8.49$. From the actual data in `th...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/AUDIT_REPORT.md` | 40 | `64%` | `**"Drops intrusion by 64%":**` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/AUDIT_REPORT.md` | 41 | `4.17` | `Under README's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \approx 64\%$.` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 41 | `64%` | `Under README's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \approx 64\%$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/AUDIT_REPORT.md` | 41 | `11.55` | `Under README's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \approx 64\%$.` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 42 | `4.43` | `Under verified episode means: $(11.9046 - 4.4315) / 11.9046 = \mathbf{62.77\%} \approx 62.8\%$.` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 42 | `62.8%` | `Under verified episode means: $(11.9046 - 4.4315) / 11.9046 = \mathbf{62.77\%} \approx 62.8\%$.` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 42 | `11.90` | `Under verified episode means: $(11.9046 - 4.4315) / 11.9046 = \mathbf{62.77\%} \approx 62.8\%$.` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/AUDIT_REPORT.md` | 48 | `4.17` | `### Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 48 | `30.18` | `### Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 48 | `21.69` | `### Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 48 | `11.55` | `### Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 50 | `11.55` | `1. **`11.55`**:` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 55 | `4.17` | `2. **`4.17`**:` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 58 | `30.18` | `3. **`30.18`**:` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 60 | `30.08` | `- **Does NOT appear in any CSV.** Mismatch of 0.10 pp against verified value 30.08%.` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 61 | `21.69` | `4. **`21.69`**:` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 63 | `30.18` | `- Derived textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mi...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 63 | `21.69` | `... textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mismatch of 0.10 ...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 63 | `21.59` | `...0 pp against verified value $+21.59\text{ pp}$.` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 63 | `8.49` | `...Derived textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mismatch ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/AUDIT_REPORT.md` | 77 | `11.90` | `# pooled_FAR_B(tau_youden) = 11.9046%` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/AUDIT_REPORT.md` | 78 | `4.17` | `# pooled_FAR_B(tau_robust) = 4.4315%   (does NOT reproduce 4.17%)` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 78 | `4.43` | `# pooled_FAR_B(tau_robust) = 4.4315%   (does NOT reproduce 4.17%)` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 80 | `30.18` | `# pooled_FRR(tau_robust)   = 30.0789%  (does NOT reproduce 30.18%)` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 82 | `4.17` | `...de-mean evaluation reproduces 4.17% or 30.18%. Both methods give ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 82 | `4.43` | `... or 30.18%. Both methods give 4.43% and 30.08%.` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 82 | `30.18` | `...valuation reproduces 4.17% or 30.18%. Both methods give 4.43% and ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 82 | `30.08` | `.... Both methods give 4.43% and 30.08%.` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 97 | `64%` | `...`src/evaluate.py`, lines 138–164) requires `dev_ids` to group ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/AUDIT_REPORT.md` | 100 | `4.43` | `..._A = 3.97\%$, $\text{FAR}_B = 4.43\%$, $\text{FRR} = 30.08\%$, $...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 100 | `30.08` | `...R}_B = 4.43\%$, $\text{FRR} = 30.08\%$, $\text{AUROC} = 0.9490$.` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 100 | `0.9490` | `...} = 30.08\%$, $\text{AUROC} = 0.9490$.` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/AUDIT_REPORT.md` | 111 | `4.17` | `...old lowers FAR from 11.55% to 4.17% at the cost of raising FRR fr...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 111 | `30.18` | `... of raising FRR from 8.49% to 30.18%"` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 111 | `11.55` | `...ust threshold lowers FAR from 11.55% to 4.17% at the cost of raisi...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 111 | `8.49` | `... the cost of raising FRR from 8.49% to 30.18%"` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/AUDIT_REPORT.md` | 114 | `4.43` | `...\text{FAR}_B$) from 11.90% to 4.43% (relative drop of 62.8%), whi...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 114 | `30.08` | `...t{FRR}$) surges from 8.49% to 30.08% (+21.59 pp, worst episode: 84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 114 | `21.59` | `...surges from 8.49% to 30.08% (+21.59 pp, worst episode: 84.63%)."` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 114 | `62.8%` | `...0% to 4.43% (relative drop of 62.8%), while the baseline device-l...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 114 | `11.55` | `...evice-level bootstrap mean is 11.55% (95% CI: [7.03%, 16.53%]); th...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/AUDIT_REPORT.md` | 114 | `11.90` | `...tration ($\text{FAR}_B$) from 11.90% to 4.43% (relative drop of 62...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/AUDIT_REPORT.md` | 114 | `8.49` | `...on ($\text{FRR}$) surges from 8.49% to 30.08% (+21.59 pp, worst e...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/AUDIT_REPORT.md` | 114 | `84.63` | `...8% (+21.59 pp, worst episode: 84.63%)."` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/AUDIT_REPORT.md` | 117 | `64%` | `- Change "drops intrusion by 64%" $\to$ **"reduces episode-mean stranger penetration by 62.8%"**` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/AUDIT_REPORT.md` | 117 | `62.8%` | `- Change "drops intrusion by 64%" $\to$ **"reduces episode-mean stranger penetration by 62.8%"**` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 118 | `21.69` | `- Change "FRR surge of +21.69%" $\to$ **"FRR surge of +21.59 pp"**` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/AUDIT_REPORT.md` | 118 | `21.59` | `- Change "FRR surge of +21.69%" $\to$ **"FRR surge of +21.59 pp"**` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/AUDIT_REPORT.md` | 143 | `4.17` | `...under device-level estimator (4.17%) \| Does not exist in any repo...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/AUDIT_REPORT.md` | 168 | `64%` | `- $L=5$: $\Delta\text{FAR} = +1.64\text{ pp}$` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/AUDIT_REPORT.md` | 170 | `64%` | `...hould note this $+0.56 \to +1.64\text{ pp}$ rise as an **unmat...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/build_gap3_summary.py` | 65 | `11.34` | `...}}}$)** \| $\\text{{FAR}}_A$ \| 11.34% \| {fa_y.mean()*100:.6f}% ({fa...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/build_gap3_summary.py` | 67 | `11.90` | `...}}}$)** \| $\\text{{FAR}}_B$ \| 11.90% \| {fb_y.mean()*100:.6f}% ({fb...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/build_gap3_summary.py` | 69 | `8.49` | `...n}}}}$)** \| $\\text{{FRR}}$ \| 8.49% \| {fr_y.mean()*100:.6f}% ({fr...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/build_gap3_summary.py` | 77 | `4.43` | `...}}}$)** \| $\\text{{FAR}}_B$ \| 4.43% \| {fb_r.mean()*100:.6f}% ({fb...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 79 | `30.08` | `...t}}}}$)** \| $\\text{{FRR}}$ \| 30.08% \| {fr_r.mean()*100:.6f}% ({fr...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 89 | `62.8%` | `...\text{{FAR}}_B$ Reduction** \| 62.8% (ratio of means) \| {ratio_of_...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 91 | `21.59` | `f.write(f"\| **FRR Surge** \| +21.59 pp \| +{d_fr_surge.mean():.6f}...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 93 | `3.54` | `...*FRR Multiplicative Ratio** \| 3.54x (ratio of means) \| {ratio_of...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/build_gap3_summary.py` | 95 | `84.63` | `... in Ep 10 (57.71%) and Ep 19 (84.63%) \|\n\n")` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/build_gap3_summary.py` | 118 | `11.55` | `...= 11.90\\%$ (episode mean) / $11.55\\%$ (device-level bootstrap),...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/build_gap3_summary.py` | 118 | `11.90` | `...ne Values:** $\\text{FAR}_B = 11.90\\%$ (episode mean) / $11.55\\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/build_gap3_summary.py` | 118 | `8.49` | `...el bootstrap), $\\text{FRR} = 8.49\\%$.\n")` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/build_gap3_summary.py` | 119 | `4.43` | `...st Values:** $\\text{FAR}_B = 4.43\\%$ (episode mean), $\\text{F...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 119 | `30.08` | `...episode mean), $\\text{FRR} = 30.08\\%$.\n")` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 120 | `21.59` | `... ($62.77\\%$), FRR surge is $+21.59\\text{ pp}$.\n")` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 120 | `62.8%` | `...ger penetration reduction is $62.8\\%$ ($62.77\\%$), FRR surge i...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/build_gap3_summary.py` | 121 | `4.17` | `...**Stale Mentions Replaced:** $4.17\\%$, $30.18\\%$, $+21.69\\tex...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/build_gap3_summary.py` | 121 | `30.18` | `...tions Replaced:** $4.17\\%$, $30.18\\%$, $+21.69\\text{ pp}$, and...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/build_gap3_summary.py` | 121 | `21.69` | `...d:** $4.17\\%$, $30.18\\%$, $+21.69\\text{ pp}$, and $64\\%$ have...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/build_gap3_summary.py` | 121 | `64%` | `...%$, $+21.69\\text{ pp}$, and $64\\%$ have been replaced across...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/FULL_NUMBER_AUDIT.md` | 14 | `12.35` | `...ceptance ($\text{FAR}_A$)** \| 12.35% [7.01%, 18.77%] \| **12.35%** ...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/FULL_NUMBER_AUDIT.md` | 15 | `11.55` | `...AR}_B$, Device Bootstrap)** \| 11.55% [7.03%, 16.53%] \| **11.55%** ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/FULL_NUMBER_AUDIT.md` | 16 | `11.90` | `...xt{FAR}_B$, Episode Mean)** \| 11.90% \| **11.90%** \| `0.119046` (11...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/FULL_NUMBER_AUDIT.md` | 17 | `8.49` | `... Rejection ($\text{FRR}$)** \| 8.49% [7.16%, 10.06%] \| **8.49%** [...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 18 | `4.43` | `...etration ($\text{FAR}_B$)** \| 4.43% \| **4.43%** \| `0.044315` (4.4...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 20 | `30.08` | `... Rejection ($\text{FRR}$)** \| 30.08% \| **30.08%** \| `0.300789` (30...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 21 | `62.8%` | `...AR}_B$ Reduction (Robust)** \| 62.8% \| **62.8%** \| `0.627746` (62....` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 22 | `21.59` | `...obust $\text{FRR}$ Surge** \| +21.59 pp \| **+21.59 pp** \| `+0.2159...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 23 | `1.47` | `...{FAR}_{\text{matched}}$)** \| +1.47% [+0.72%, +2.40%] \| **+1.47%**...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/FULL_NUMBER_AUDIT.md` | 24 | `2.67` | `...xy ($k=1$) $\text{FAR}_A$** \| 2.67% \| **2.67%** \| `0.026650` (2.6...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/FULL_NUMBER_AUDIT.md` | 25 | `22.08` | `...xy ($k=1$) $\text{FAR}_B$** \| 22.08% \| **22.08%** \| `0.220754` (22...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/FULL_NUMBER_AUDIT.md` | 26 | `19.41` | `...Gap ($\Delta\text{FAR}$)** \| +19.41% \| **+19.41%** \| `+0.194104` (...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/FULL_NUMBER_AUDIT.md` | 31 | `11.90` | `...}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\Delta\text{FAR}$: +0.56% \|...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/FULL_NUMBER_AUDIT.md` | 31 | `11.34` | `... ($k=15$)** \| $\text{FAR}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\De...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/FULL_NUMBER_AUDIT.md` | 32 | `99.43` | `... **Closed-Set Macro $F_1$** \| 99.43% [99.32%, 99.53%] \| **99.43%**...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 33 | `0.9490` | `...Open-Set $\text{AUROC}_B$** \| 0.9490 [0.9367, 0.9605] \| **0.9490**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 34 | `0.9530` | `...Open-Set $\text{AUROC}_A$** \| 0.9530 [0.9413, 0.9625] \| **0.9530**...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 35 | `65.7` | `...t{FAR}_B$ ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/FULL_NUMBER_AUDIT.md` | 37 | `0.2097` | `...e Spearman $\rho$** \| $\rho = 0.2097$, $p = 0.1142$, $n = 58$ \| $\...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/FULL_NUMBER_AUDIT.md` | 37 | `0.1142` | `...ho$** \| $\rho = 0.2097$, $p = 0.1142$, $n = 58$ \| $\rho = \mathbf{...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/FULL_NUMBER_AUDIT.md` | 38 | `0.0327` | `...ation Absolute Error** \| LOPO 0.0327 vs. Naive 0.0323 \| LOPO: **0....` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/FULL_NUMBER_AUDIT.md` | 38 | `0.0323` | `...ation Absolute Error** \| LOPO 0.0327 vs. Naive 0.0323 \| LOPO: **0...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/FULL_NUMBER_AUDIT.md` | 39 | `11.90` | `...}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\text{FRR}$: 8.49%, $\text{...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/FULL_NUMBER_AUDIT.md` | 39 | `11.34` | `...ouden}}$)** \| $\text{FAR}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\te...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/FULL_NUMBER_AUDIT.md` | 39 | `0.9490` | `...FRR}$: 8.49%, $\text{AUROC}$: 0.9490 \| **11.34%**, **11.90%**, **8...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 39 | `8.49` | `...AR}_B$: 11.90%, $\text{FRR}$: 8.49%, $\text{AUROC}$: 0.9490 \| **1...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 40 | `64%` | `...}$: 4.37%, $\text{AUROC}$: 0.9642 \| **9.95%**, **11.22%**, **4...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/FULL_NUMBER_AUDIT.md` | 40 | `11.22` | `...R}_A$: 9.95%, $\text{FAR}_B$: 11.22%, $\text{FRR}$: 4.37%, $\text{...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 40 | `4.37` | `...AR}_B$: 11.22%, $\text{FRR}$: 4.37%, $\text{AUROC}$: 0.9642 \| **9...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 40 | `0.9642` | `...FRR}$: 4.37%, $\text{AUROC}$: 0.9642 \| **9.95%**, **11.22%**, **4....` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 41 | `64%` | `...5369`, $\text{AUROC}$: `0.966964` \| `results/tables/burst_aggr...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/FULL_NUMBER_AUDIT.md` | 41 | `3.54` | `...AR}_B$: 10.45%, $\text{FRR}$: 3.54%, $\text{AUROC}$: 0.9670 \| **8...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 41 | `10.45` | `...R}_A$: 8.81%, $\text{FAR}_B$: 10.45%, $\text{FRR}$: 3.54%, $\text{...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 41 | `0.9670` | `...FRR}$: 3.54%, $\text{AUROC}$: 0.9670 \| **8.81%**, **10.45%**, **3....` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 64 | `98.5` | `## 3. Dissection of the 98.5% Figure & Per-Device Range` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/FULL_NUMBER_AUDIT.md` | 66 | `98.5` | `- **Source of "98.5%":** Programmatic scan across ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/FULL_NUMBER_AUDIT.md` | 75 | `98.5` | `...onclusion:** Quoting "0.0% to 98.5%" conflates a device-averaged ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/FULL_NUMBER_AUDIT.md` | 76 | `65.7` | `...t{FAR}_B$ ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/FULL_NUMBER_AUDIT.md` | 103 | `11.90` | `...n}}, L=1$):** $\text{FAR}_B = 11.9046\%$, $\text{FRR} = 8.4860\%$...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/FULL_NUMBER_AUDIT.md` | 104 | `4.43` | `...t}}, L=1$):** $\text{FAR}_B = 4.4315\%$, $\text{FRR} = 30.0789\%...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 104 | `64%` | `...9\%$, $\Delta\text{FAR} = +0.4644\text{ pp}$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/FULL_NUMBER_AUDIT.md` | 105 | `21.59` | `... drop); $\text{FRR}$ surge: $+21.59\text{ pp}$ ($3.54\times$ incr...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 105 | `62.8%` | `...ger drop: $-7.47\text{ pp}$ ($62.8\%$ relative drop); $\text{FRR...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/FULL_NUMBER_AUDIT.md` | 105 | `3.54` | `...$ surge: $+21.59\text{ pp}$ ($3.54\times$ increase).` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 106 | `3.54` | `...* $L=5$ cuts $\text{FRR}$ to $3.54\%$ (AUROC: $0.9670$, $\text{F...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 106 | `10.45` | `...OC: $0.9670$, $\text{FAR}_B = 10.45\%$).` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 106 | `0.9670` | `...xt{FRR}$ to $3.54\%$ (AUROC: $0.9670$, $\text{FAR}_B = 10.45\%$).` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/FULL_NUMBER_AUDIT.md` | 107 | `0.9670` | `...ext{FAR}_B = 6.42\%$, AUROC: $0.9670$), but remains well above the...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 10 | `4.43` | `...xt{robust}}$: $\text{FAR}_B = 4.43\%$, $\text{FRR} = 30.08\%$). ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 10 | `30.08` | `...R}_B = 4.43\%$, $\text{FRR} = 30.08\%$). Panel (b) shows the effe...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 10 | `64%` | `....56\text{ pp}$ at $L=1$ to $1.64\text{ pp}$ at $L=5$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/gap3_paper_text.md` | 10 | `11.90` | `...ns (baseline: $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$; ro...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/gap3_paper_text.md` | 10 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$; robust $\tau_{\text{robus...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 10 | `3.54` | `...timate $\text{FRR}$ drops to $3.54\%$ while $\text{FAR}_B$ decre...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 10 | `10.45` | `... $\text{FAR}_B$ decreases to $10.45\%$; the unmatched familiarity...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 18 | `4.43` | `...$) falls from **11.90%** to **4.43%**, corresponding to a **62.8%...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 18 | `62.8%` | `...4.43%**, corresponding to a **62.8%** relative reduction in rogue...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 18 | `11.55` | `... baseline $\text{FAR}_B$ is **11.55%** (95% CI: [7.03%, 16.53%]; s...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/gap3_paper_text.md` | 18 | `11.90` | `...($\text{FAR}_B$) falls from **11.90%** to **4.43%**, corresponding...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/gap3_paper_text.md` | 20 | `30.08` | `...r $\tau_{\text{Youden}}$ to **30.08%** under $\tau_{\text{robust}}...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 20 | `21.59` | `...ng an availability loss of **+21.59 percentage points**. Furtherm...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 20 | `8.49` | `...enrolled meters surges from **8.49%** (95% CI: [7.16%, 10.06%]) u...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 20 | `84.63` | `...an **26.23%**) to a peak of **84.63%** in the worst episode (episo...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/gap3_paper_text.md` | 22 | `11.90` | `..._B$ decreases modestly from **11.90%** ($L=1$) to **10.45%** ($L=5...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/gap3_paper_text.md` | 22 | `3.54` | `...timate $\text{FRR}$ down to **3.54%** (boosting enrolled availabi...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 22 | `10.45` | `... from **11.90%** ($L=1$) to **10.45%** ($L=5$). (Note: burst fusio...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 22 | `0.9670` | `...scrimination to an AUROC of **0.9670**, while $\text{FAR}_B$ decre...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 30 | `64%` | `...rcentage points at $L=1$ to 1.64 percentage points at $L=5$. B...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/gap3_paper_text.md` | 30 | `10.45` | `...on ($\text{FAR}_B$ remains at 10.45% at $L=5$), nor does it resolv...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 54 | `11.55` | `& $11.55^\dagger$ [7.03, 16.53]` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/gap3_paper_text.md` | 55 | `8.49` | `& $8.49$ [7.16, 10.06]` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 56 | `0.9490` | `& $0.9490$ [0.9367, 0.9605]` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 59 | `4.43` | `& $4.43$` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 60 | `30.08` | `& $30.08$` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/gap3_paper_text.md` | 61 | `0.9490` | `& $0.9490$` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 65 | `11.90` | `& $11.90$` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/gap3_paper_text.md` | 66 | `8.49` | `& $8.49$` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 67 | `0.9490` | `& $0.9490$` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/gap3_paper_text.md` | 70 | `11.22` | `& $11.22$` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 71 | `4.37` | `& $4.37$` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 72 | `64%` | `& $0.9642$` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/gap3_paper_text.md` | 72 | `0.9642` | `& $0.9642$` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 75 | `10.45` | `& $10.45$` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 76 | `3.54` | `& $3.54$` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 77 | `0.9670` | `& $0.9670$` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/gap3_paper_text.md` | 84 | `11.90` | `...vices (plain episode mean is $11.90\%$).` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GAP3_SUMMARY.md` | 11 | `11.34` | `...uden}}$)** \| $\text{FAR}_A$ \| 11.34% \| 11.342188% (0.113422) \| 4.9...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/GAP3_SUMMARY.md` | 12 | `11.90` | `...uden}}$)** \| $\text{FAR}_B$ \| 11.90% \| 11.904615% (0.119046) \| 6.7...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GAP3_SUMMARY.md` | 13 | `8.49` | `...Youden}}$)** \| $\text{FRR}$ \| 8.49% \| 8.486005% (0.084860) \| 3.49...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GAP3_SUMMARY.md` | 16 | `4.43` | `...bust}}$)** \| $\text{FAR}_B$ \| 4.43% \| 4.431538% (0.044315) \| 3.52...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 17 | `30.08` | `...robust}}$)** \| $\text{FRR}$ \| 30.08% \| 30.078880% (0.300789) \| 17....` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 18 | `64%` | `...ta\text{FAR}$ \| +0.46 pp \| 0.464351 pp (0.004644) \| 3.4667% \| ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GAP3_SUMMARY.md` | 25 | `62.8%` | `... $\text{FAR}_B$ Reduction** \| 62.8% (ratio of means) \| 62.774619%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 26 | `21.59` | `\| **FRR Surge** \| +21.59 pp \| +21.592875 pp \| [14.71 p...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 27 | `3.54` | `...*FRR Multiplicative Ratio** \| 3.54x (ratio of means) \| 3.544528x...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 29 | `84.63` | `... in Ep 10 (57.71%) and Ep 19 (84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GAP3_SUMMARY.md` | 35 | `11.90` | `...0.084860) \| [7.12%, 10.07%] \| 11.90% (0.119046) \| [9.08%, 14.85%] ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GAP3_SUMMARY.md` | 35 | `0.9490` | `... [9.08%, 14.85%] \| +0.56 pp \| 0.9490 \|` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/GAP3_SUMMARY.md` | 35 | `8.49` | `\| **$L=1$** \| 8.49% (0.084860) \| [7.12%, 10.07%] ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GAP3_SUMMARY.md` | 36 | `64%` | `....31%, 14.24%] \| +1.27 pp \| 0.9642 \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GAP3_SUMMARY.md` | 36 | `11.22` | `...(0.043740) \| [3.03%, 6.17%] \| 11.22% (0.112182) \| [8.31%, 14.24%] ...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 36 | `4.37` | `\| **$L=3$** \| 4.37% (0.043740) \| [3.03%, 6.17%] \|...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 36 | `0.9642` | `... [8.31%, 14.24%] \| +1.27 pp \| 0.9642 \|` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 37 | `64%` | `...04538) \| [7.75%, 13.28%] \| +1.64 pp \| 0.9670 \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GAP3_SUMMARY.md` | 37 | `3.54` | `\| **$L=5$** \| 3.54% (0.035369) \| [1.79%, 5.84%] \|...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 37 | `10.45` | `...(0.035369) \| [1.79%, 5.84%] \| 10.45% (0.104538) \| [7.75%, 13.28%] ...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 37 | `0.9670` | `... [7.75%, 13.28%] \| +1.64 pp \| 0.9670 \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 43 | `4.43` | `....300789) \| [23.08%, 38.40%] \| 4.43% (0.044315) \| [3.01%, 6.00%] \|...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 43 | `30.08` | `\| **$L=1$** \| 30.08% (0.300789) \| [23.08%, 38.40%]...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 43 | `0.9490` | `...\| [3.01%, 6.00%] \| +0.46 pp \| 0.9490 \|` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/GAP3_SUMMARY.md` | 44 | `21.69` | `\| **$L=3$** \| 21.69% (0.216870) \| [14.27%, 30.87%]...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GAP3_SUMMARY.md` | 44 | `64%` | `...4.06%, 7.43%] \| +0.95 pp \| 0.9642 \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GAP3_SUMMARY.md` | 44 | `0.9642` | `...\| [4.06%, 7.43%] \| +0.95 pp \| 0.9642 \|` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 45 | `64%` | `... [10.29%, 27.66%] \| 6.42% (0.064192) \| [4.57%, 8.27%] \| +1.36 ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GAP3_SUMMARY.md` | 45 | `0.9670` | `...\| [4.57%, 8.27%] \| +1.36 pp \| 0.9670 \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GAP3_SUMMARY.md` | 49 | `11.55` | `... = 11.90\%$ (episode mean) / $11.55\%$ (device-level bootstrap), ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GAP3_SUMMARY.md` | 49 | `11.90` | `...ine Values:** $\text{FAR}_B = 11.90\%$ (episode mean) / $11.55\%$...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GAP3_SUMMARY.md` | 49 | `8.49` | `...vel bootstrap), $\text{FRR} = 8.49\%$.` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GAP3_SUMMARY.md` | 50 | `4.43` | `- **Verified Robust Values:** $\text{FAR}_B = 4.43\%$ (episode mean), $\text{FRR} = 30.08\%$.` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 50 | `30.08` | `- **Verified Robust Values:** $\text{FAR}_B = 4.43\%$ (episode mean), $\text{FRR} = 30.08\%$.` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 51 | `21.59` | `...$ ($62.77\%$), FRR surge is $+21.59\text{ pp}$.` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 51 | `62.8%` | `...ger penetration reduction is $62.8\%$ ($62.77\%$), FRR surge is ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GAP3_SUMMARY.md` | 52 | `4.17` | `...**Stale Mentions Replaced:** $4.17\%$, $30.18\%$, $+21.69\text{ ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GAP3_SUMMARY.md` | 52 | `30.18` | `...ntions Replaced:** $4.17\%$, $30.18\%$, $+21.69\text{ pp}$, and $...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GAP3_SUMMARY.md` | 52 | `21.69` | `...ced:** $4.17\%$, $30.18\%$, $+21.69\text{ pp}$, and $64\%$ have b...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GAP3_SUMMARY.md` | 52 | `64%` | `...\%$, $+21.69\text{ pp}$, and $64\%$ have been replaced across ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 7 | `98.5` | `...ility ranges from $0.0\%$ to $98.5\%$, with top vulnerable devic...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 8 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$ at the cost of FRR surging...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 8 | `30.18` | `...FRR surging from $8.49\%$ to $30.18\%$.` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 8 | `11.55` | `...ue stranger penetration from $11.55\%$ to $4.17\%$ at the cost of...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 8 | `8.49` | `...the cost of FRR surging from $8.49\%$ to $30.18\%$.` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 9 | `65.7` | `...ean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 10 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 10 | `30.08` | `...FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 10 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 10 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at the cost of ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 10 | `11.90` | `...ue stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 10 | `8.49` | `...the cost of FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 15 | `8.49` | `...itimate false rejection from $8.49\%$ to $3.54\%$ (boosting avai...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 15 | `3.54` | `...e rejection from $8.49\%$ to $3.54\%$ (boosting availability to ...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 15 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 16 | `8.49` | `...itimate false rejection from $8.49\%$ to $3.54\%$ (boosting avai...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 16 | `3.54` | `...e rejection from $8.49\%$ to $3.54\%$ (boosting availability to ...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 16 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 21 | `4.17` | `... \| $\text{FAR}_B: 11.55\% \to 4.17\%$ \| FRR surges from $8.49\%$...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 21 | `30.18` | `... FRR surges from $8.49\%$ to $30.18\%$ \|` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 21 | `11.55` | `...xy rejection \| $\text{FAR}_B: 11.55\% \to 4.17\%$ \| FRR surges fr...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 21 | `8.49` | `...to 4.17\%$ \| FRR surges from $8.49\%$ to $30.18\%$ \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 22 | `8.49` | `...ision fusion \| **$\text{FRR}: 8.49\% \to 3.54\%$** \| **AUROC cli...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 22 | `3.54` | `...n \| **$\text{FRR}: 8.49\% \to 3.54\%$** \| **AUROC climbs to $0.9...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 22 | `10.45` | `...$0.9670$**, $\text{FAR}_B \to 10.45\%$ \|` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 22 | `0.9670` | `....54\%$** \| **AUROC climbs to $0.9670$**, $\text{FAR}_B \to 10.45\%...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 23 | `4.43` | `... \| $\text{FAR}_B: 11.90\% \to 4.43\%$ (episode mean) \| FRR surge...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 23 | `30.08` | `... FRR surges from $8.49\%$ to $30.08\%$ (+21.59 pp) \|` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 23 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 23 | `11.90` | `...xy rejection \| $\text{FAR}_B: 11.90\% \to 4.43\%$ (episode mean) ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 23 | `8.49` | `...sode mean) \| FRR surges from $8.49\%$ to $30.08\%$ (+21.59 pp) \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 24 | `8.49` | `...ision fusion \| **$\text{FRR}: 8.49\% \to 3.54\%$** \| **AUROC cli...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 24 | `3.54` | `...n \| **$\text{FRR}: 8.49\% \to 3.54\%$** \| **AUROC climbs to $0.9...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 24 | `10.45` | `...$0.9670$**, $\text{FAR}_B \to 10.45\%$ \|` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 24 | `0.9670` | `....54\%$** \| **AUROC climbs to $0.9670$**, $\text{FAR}_B \to 10.45\%...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 29 | `4.17` | `...t provided \| Not provided \| **4.17%** (drops intrusion by 64%) \|` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 29 | `64%` | `...**4.17%** (drops intrusion by 64%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 30 | `30.18` | `...antified \| Not quantified \| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 30 | `21.69` | `...ified \| **30.18%** (surge of +21.69%, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GIT_DIFF_SUMMARY.md` | 30 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 31 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 31 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 32 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 32 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 33 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 33 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 33 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 34 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 34 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 41 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$, it causes False Rejection...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 41 | `30.18` | `...e ($\text{FRR}$) to surge to $30.18\%$ (peaking at $84.63\%$). Th...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 41 | `11.55` | `...ue stranger penetration from $11.55\%$ to $4.17\%$, it causes Fal...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 41 | `84.63` | `...rge to $30.18\%$ (peaking at $84.63\%$). This demonstrates that i...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), it...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `30.08` | `...$) to surge from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84.63\%$). Th...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), it causes Fals...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `11.90` | `...ue stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `8.49` | `...($\text{FRR}$) to surge from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 42 | `84.63` | `...08\%$ (+21.59 pp, peaking at $84.63\%$). This demonstrates that i...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 47 | `4.17` | `...t provided \| Not provided \| **4.17%** (drops penetration by 64%) ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 47 | `64%` | `...4.17%** (drops penetration by 64%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 48 | `30.18` | `...antified \| Not quantified \| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 48 | `21.69` | `...ified \| **30.18%** (surge of +21.69%, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GIT_DIFF_SUMMARY.md` | 48 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 49 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 49 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 50 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 50 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 51 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 51 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 51 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 52 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 52 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 57 | `98.5` | `...ries widely (from $0.0\%$ to $98.5\%$). To eliminate this hardwa...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 57 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ with a strictly positive 9...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/GIT_DIFF_SUMMARY.md` | 58 | `65.7` | `...ean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 58 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ with a strictly positive 9...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `4.17` | `...ation from $11.55\%$ down to $4.17\%$ (with 4 episodes reaching ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `30.18` | `...rs surges from $8.49\%$ to **$30.18\%$** on average (peaking at $...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `11.55` | `...ue stranger penetration from $11.55\%$ down to $4.17\%$ (with 4 e...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `8.49` | `...ate smart meters surges from $8.49\%$ to **$30.18\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `0.0327` | `...s absolute estimation error ($0.0327$) is comparable to naive test...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `0.0323` | `...s absolute estimation error ($0.0327$) is comparable to naive tes...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/GIT_DIFF_SUMMARY.md` | 63 | `84.63` | `...\%$** on average (peaking at $84.63\%$). In a municipal AMR grid,...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `4.43` | `...ation from $11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, wit...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `30.08` | `...rs surges from $8.49\%$ to **$30.08\%$** on average (+21.59 pp, p...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `21.59` | `...to **$30.08\%$** on average (+21.59 pp, peaking at $84.63\%$). In...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `62.8%` | `...11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, with 4 episodes...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `11.90` | `...ue stranger penetration from $11.90\%$ down to $4.43\%$ (a $62.8\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `8.49` | `...ate smart meters surges from $8.49\%$ to **$30.08\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `0.0327` | `...s absolute estimation error ($0.0327$) is comparable to naive test...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `0.0323` | `...s absolute estimation error ($0.0327$) is comparable to naive tes...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/GIT_DIFF_SUMMARY.md` | 64 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$). In a municipal AMR grid,...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 69 | `30.18` | `-        F2["Quantified Robust Availability Cost (FRR surges to 30.18%)"]` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 70 | `30.08` | `+        F2["Quantified Robust Availability Cost (FRR surges to 30.08%)"]` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 75 | `11.55` | `...int ($\tau^*$)** \| 0.7040 \| **11.55%** \| **8.49%** \| Standard scre...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 75 | `8.49` | `...)** \| 0.7040 \| **11.55%** \| **8.49%** \| Standard screening; balan...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 76 | `4.17` | `...ext{robust}}$)** \| 0.8540 \| **4.17%** \| **30.18%** \| **Catastroph...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 76 | `30.18` | `...$)** \| 0.8540 \| **4.17%** \| **30.18%** \| **Catastrophic availabili...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 77 | `11.55` | `...040 \| **11.90%** (ep. mean) / 11.55% (dev. boot) \| **8.49%** \| Sta...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 77 | `11.90` | `...int ($\tau^*$)** \| 0.7040 \| **11.90%** (ep. mean) / 11.55% (dev. b...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 77 | `8.49` | `...ean) / 11.55% (dev. boot) \| **8.49%** \| Standard screening; balan...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 78 | `4.43` | `...ext{robust}}$)** \| 0.8540 \| **4.43%** \| **30.08%** \| **Catastroph...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 78 | `30.08` | `...$)** \| 0.8540 \| **4.43%** \| **30.08%** \| **Catastrophic availabili...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 83 | `4.17` | `...ue penetration from 11.55% to 4.17% (with 4 episodes reaching 0.0...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 83 | `30.18` | `..., False Rejection surges to **30.18%** on average (and reaches **8...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 83 | `11.55` | `...lashes rogue penetration from 11.55% to 4.17% (with 4 episodes rea...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 83 | `84.63` | `...%** on average (and reaches **84.63%** in episode 4), which would ...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 84 | `4.43` | `...ue penetration from 11.90% to 4.43% (a 62.8% reduction, with 4 ep...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 84 | `30.08` | `..., False Rejection surges to **30.08%** on average (+21.59 pp, and ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 84 | `21.59` | `...es to **30.08%** on average (+21.59 pp, and reaches **84.63%** in...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 84 | `62.8%` | `...ation from 11.90% to 4.43% (a 62.8% reduction, with 4 episodes re...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 84 | `11.90` | `...e-mean rogue penetration from 11.90% to 4.43% (a 62.8% reduction, ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 84 | `84.63` | `...age (+21.59 pp, and reaches **84.63%** in episode 19), which would...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$, but the False Rejection R...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `30.18` | `...Rate surges from $8.49\%$ to $30.18\%$ — rejecting nearly 1 in 3 ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `11.55` | `...ue-stranger penetration from $11.55\%$ to $4.17\%$, but the False...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `99.43` | `...-set classification achieves $99.43\%$ macro-$F_1$, the open-set ...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `0.9490` | `...$F_1$, the open-set AUROC of $0.949$ with $\text{FAR}_B = 11.55\%...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to $30.18\%$ — rejecting n...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 91 | `98.5` | `...ly heterogeneous ($0.0\%$ to $98.5\%$), with 7 of the 8 hardest ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `30.08` | `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting ne...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting nearly 1 in 3...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), but the False ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `11.55` | `... $0.949$ with $\text{FAR}_B = 11.55\%$ [device-level bootstrap: $...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `99.43` | `...-set classification achieves $99.43\%$ macro-$F_1$, the open-set ...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `0.9490` | `...$F_1$, the open-set AUROC of $0.949$ with $\text{FAR}_B = 11.55\%...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) —...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 92 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$, but the False Rejection R...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `30.18` | `...Rate surges from $8.49\%$ to $30.18\%$---rejecting nearly 1 in 3 ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `11.55` | `...ue-stranger penetration from $11.55\%$ to $4.17\%$, but the False...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to $30.18\%$---rejecting n...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `98.5` | `...ly heterogeneous ($0.0\%$ to $98.5\%$), with 7 of the 8 hardest ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `3.54` | `...ate meter false rejection to $3.54\%$ (availability $96.46\%$) w...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 99 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$. Per-device vulnerability is...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `30.08` | `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84.63\%$)---r...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), but the False ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `3.54` | `...ate meter false rejection to $3.54\%$ (availability $96.46\%$) w...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$. Device-mean $\text{FAR}_B$ ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 100 | `84.63` | `...08\%$ (+21.59 pp, peaking at $84.63\%$)---rejecting nearly 1 in 3...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 105 | `98.5` | `...ation varies from $0.0\%$ to $98.5\%$, with the top vulnerable t...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 106 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$ but imposes a steep operat...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 106 | `30.18` | `...(FRR surges from $8.49\%$ to $30.18\%$).` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 106 | `11.55` | `...ue-stranger penetration from $11.55\%$ to $4.17\%$ but imposes a ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 106 | `8.49` | `...ity penalty (FRR surges from $8.49\%$ to $30.18\%$).` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 107 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 108 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 108 | `30.08` | `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 108 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 108 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but imposes a s...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 108 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 108 | `8.49` | `...ity penalty (FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 113 | `4.17` | `...ided & Not provided & \textbf{4.17\% (drops penetration by 64\%)...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 113 | `64%` | `...{4.17\% (drops penetration by 64\%)} \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 114 | `30.18` | `...ed & Not quantified & \textbf{30.18\% (FRR surge $+21.7\%$)} \\` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 115 | `3.54` | `...ted & \textbf{$\text{FRR} \to 3.54\%$, $\text{AUROC} \to 0.9670$...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 115 | `0.9670` | `...to 3.54\%$, $\text{AUROC} \to 0.9670$} \\` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 116 | `4.43` | `...ided & Not provided & \textbf{4.43\% (reduces penetration by 62....` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 116 | `62.8%` | `....43\% (reduces penetration by 62.8\%)} \\` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 117 | `30.08` | `...ed & Not quantified & \textbf{30.08\% (FRR surge $+21.59$ pp)} \\` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 117 | `21.59` | `... \textbf{30.08\% (FRR surge $+21.59$ pp)} \\` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 118 | `3.54` | `...ted & \textbf{$\text{FRR} \to 3.54\%$, $\text{AUROC} \to 0.9670$...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 118 | `0.9670` | `...to 3.54\%$, $\text{AUROC} \to 0.9670$} \\` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 131 | `98.5` | `...ation varies from $0.0\%$ to $98.5\%$. The top vulnerable transm...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 132 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 137 | `4.17` | `-    \item Drops true stranger penetration from $11.55\%$ to $4.17\%$.` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 137 | `11.55` | `-    \item Drops true stranger penetration from $11.55\%$ to $4.17\%$.` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 138 | `30.18` | `...$) to surge from $8.49\%$ to $30.18\%$ on average (peaking at $84...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 138 | `8.49` | `...($\text{FRR}$) to surge from $8.49\%$ to $30.18\%$ on average (p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 138 | `84.63` | `...18\%$ on average (peaking at $84.63\%$).` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 139 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 139 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 139 | `11.90` | `...ue stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 140 | `30.08` | `...$) to surge from $8.49\%$ to $30.08\%$ on average (+21.59 pp, pea...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 140 | `21.59` | `...\%$ to $30.08\%$ on average (+21.59 pp, peaking at $84.63\%$).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 140 | `8.49` | `...($\text{FRR}$) to surge from $8.49\%$ to $30.08\%$ on average (+...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 140 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$).` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 145 | `30.18` | `...g introduces an unacceptable $30.18\%$ availability penalty in ba...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 146 | `30.08` | `...g introduces an unacceptable $30.08\%$ availability penalty in ba...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 151 | `30.18` | `...e transmission to reduce the $30.18\%$ FRR penalty.` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 152 | `30.08` | `...e transmission to reduce the $30.08\%$ FRR penalty.` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 157 | `30.18` | `...y cost of robust thresholds ($30.18\%$ FRR). These results establ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 157 | `19.41` | `...2\%, +2.40\%]$), scaling to $+19.41\%$ for single-proxy calibrati...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/GIT_DIFF_SUMMARY.md` | 157 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/GIT_DIFF_SUMMARY.md` | 158 | `30.08` | `...y cost of robust thresholds ($30.08\%$ FRR). These results establ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 158 | `19.41` | `...2\%, +2.40\%]$), scaling to $+19.41\%$ for single-proxy calibrati...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/GIT_DIFF_SUMMARY.md` | 158 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/GIT_DIFF_SUMMARY.md` | 165 | `98.5` | `...ation varies from $0.0\%$ to $98.5\%$, with the top vulnerable t...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/GIT_DIFF_SUMMARY.md` | 166 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$ but imposes a steep operat...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 166 | `30.18` | `...(FRR surges from $8.49\%$ to $30.18\%$).` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 166 | `11.55` | `...ue-stranger penetration from $11.55\%$ to $4.17\%$ but imposes a ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 166 | `8.49` | `...ity penalty (FRR surges from $8.49\%$ to $30.18\%$).` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 167 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/GIT_DIFF_SUMMARY.md` | 168 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 168 | `30.08` | `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 168 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 168 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but imposes a s...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 168 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 168 | `8.49` | `...ity penalty (FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 173 | `4.17` | `...t provided \| Not provided \| **4.17%** (drops intrusion by 64%) \|` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 173 | `64%` | `...**4.17%** (drops intrusion by 64%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 174 | `30.18` | `...antified \| Not quantified \| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 174 | `21.69` | `...ified \| **30.18%** (surge of +21.69%, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GIT_DIFF_SUMMARY.md` | 174 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 175 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 175 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 176 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 176 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 177 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 177 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 177 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 178 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 178 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 183 | `30.18` | `...bust}}$), revealing a severe $30.18\%$ false rejection rate that ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 184 | `30.08` | `...bust}}$), revealing a severe $30.08\%$ false rejection rate that ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 189 | `4.17` | `...ation from $11.55\%$ down to $4.17\%$ (with 4 episodes achieving...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 189 | `11.55` | `...ue-stranger penetration from $11.55\%$ down to $4.17\%$ (with 4 e...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 190 | `30.18` | `...te surges from $8.49\%$ to **$30.18\%$** on average (peaking at $...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 190 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to **$30.18\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 190 | `84.63` | `...\%$** on average (peaking at $84.63\%$). Deploying $\tau_{\text{r...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 191 | `4.43` | `...ation from $11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, wit...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 191 | `62.8%` | `...11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, with 4 episodes...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 191 | `11.90` | `...ue-stranger penetration from $11.90\%$ down to $4.43\%$ (a $62.8\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 192 | `30.08` | `...te surges from $8.49\%$ to **$30.08\%$** on average (+21.59 pp, p...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 192 | `21.59` | `...to **$30.08\%$** on average (+21.59 pp, peaking at $84.63\%$). De...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 192 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to **$30.08\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 192 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$). Deploying $\tau_{\text{r...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 205 | `30.18` | `...ed receivers to suppress the $30.18\%$ availability penalty of ro...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 206 | `30.08` | `...ed receivers to suppress the $30.08\%$ availability penalty of ro...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 211 | `30.18` | `...y cost of robust thresholds ($30.18\%$ FRR). These results demons...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 211 | `19.41` | `...2\%, +2.40\%]$), scaling to $+19.41\%$ when only a single proxy d...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/GIT_DIFF_SUMMARY.md` | 211 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/GIT_DIFF_SUMMARY.md` | 212 | `30.08` | `...y cost of robust thresholds ($30.08\%$ FRR). These results demons...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 212 | `19.41` | `...2\%, +2.40\%]$), scaling to $+19.41\%$ when only a single proxy d...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/GIT_DIFF_SUMMARY.md` | 212 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/GIT_DIFF_SUMMARY.md` | 219 | `4.17` | `...t provided \| Not provided \| **4.17%** (drops intrusion by 64%) \|` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 219 | `64%` | `...**4.17%** (drops intrusion by 64%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 220 | `30.18` | `...antified \| Not quantified \| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 220 | `21.69` | `...ified \| **30.18%** (surge of +21.69%, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GIT_DIFF_SUMMARY.md` | 220 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 221 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 221 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 222 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 222 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 223 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 223 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 223 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 224 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 224 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 231 | `4.17` | `...ded,Not provided,Not provided,4.17% (drops intrusion by 64%)` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 231 | `64%` | `...ded,4.17% (drops intrusion by 64%)` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 232 | `30.18` | `...Not quantified,Not quantified,30.18% (surge of +21.69%, peak 84.63...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 232 | `21.69` | `... quantified,30.18% (surge of +21.69%, peak 84.63%)` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GIT_DIFF_SUMMARY.md` | 232 | `84.63` | `...0.18% (surge of +21.69%, peak 84.63%)` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 233 | `3.54` | `...valuated,Not evaluated,FRR -> 3.54%, AUROC -> 0.9670` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 233 | `0.9670` | `...luated,FRR -> 3.54%, AUROC -> 0.9670` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 234 | `4.43` | `...ded,Not provided,Not provided,4.43% (reduces episode-mean strange...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 234 | `62.8%` | `...-mean stranger penetration by 62.8%)` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 235 | `30.08` | `...Not quantified,Not quantified,30.08% (surge of +21.59 pp, peak 84....` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 235 | `21.59` | `... quantified,30.08% (surge of +21.59 pp, peak 84.63%)` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 235 | `84.63` | `...08% (surge of +21.59 pp, peak 84.63%)` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 236 | `3.54` | `...valuated,Not evaluated,FRR -> 3.54%, AUROC -> 0.9670` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 236 | `0.9670` | `...luated,FRR -> 3.54%, AUROC -> 0.9670` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 243 | `4.17` | `...penetration from $11.55\% \to 4.17\%$.` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 243 | `11.55` | `...ue stranger penetration from $11.55\% \to 4.17\%$.` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/GIT_DIFF_SUMMARY.md` | 244 | `30.18` | `-- However, False Rejection Rate surges from $8.49\% \to 30.18\%$ on average (peaking at $84.63\%$).` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 244 | `8.49` | `-- However, False Rejection Rate surges from $8.49\% \to 30.18\%$ on average (peaking at $84.63\%$).` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 244 | `84.63` | `-- However, False Rejection Rate surges from $8.49\% \to 30.18\%$ on average (peaking at $84.63\%$).` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 245 | `4.43` | `...penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 245 | `62.8%` | `...from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 245 | `11.90` | `...ue stranger penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ red...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/GIT_DIFF_SUMMARY.md` | 246 | `30.08` | `... Rate surges from $8.49\% \to 30.08\%$ on average (+21.59 pp, pea...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 246 | `21.59` | `...9\% \to 30.08\%$ on average (+21.59 pp, peaking at $84.63\%$).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 246 | `8.49` | `...e Rejection Rate surges from $8.49\% \to 30.08\%$ on average (+2...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 246 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$).` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 257 | `4.17` | `...t provided \| Not provided \| **4.17%** (drops intrusion by 64%) \|` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 257 | `64%` | `...**4.17%** (drops intrusion by 64%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/GIT_DIFF_SUMMARY.md` | 258 | `30.18` | `...antified \| Not quantified \| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/GIT_DIFF_SUMMARY.md` | 258 | `21.69` | `...ified \| **30.18%** (surge of +21.69%, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/GIT_DIFF_SUMMARY.md` | 258 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 259 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 259 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 260 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 260 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 261 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 261 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/GIT_DIFF_SUMMARY.md` | 261 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/GIT_DIFF_SUMMARY.md` | 262 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/GIT_DIFF_SUMMARY.md` | 262 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/make_gap3_final.py` | 42 | `11.90` | `mean_farb_y = tt["FAR_true_youden"].mean() * 100    # 11.9046% -> 11.9%` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/make_gap3_final.py` | 44 | `4.43` | `mean_farb_r = tt["FAR_true_robust"].mean() * 100    # 4.4315% -> 4.4%` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/make_gap3_final.py` | 50 | `84.63` | `outlier_frr = outlier_row["FRR_robust"] * 100       # 84.6310%` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/make_gap3_final.py` | 55 | `11.90` | `farb_L = [bas.loc[L, "FAR_B"] * 100 for L in L_vals]  # [11.90, 11.22, 10.45]` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/make_gap3_final.py` | 55 | `10.45` | `farb_L = [bas.loc[L, "FAR_B"] * 100 for L in L_vals]  # [11.90, 11.22, 10.45]` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/make_gap3_final.py` | 55 | `11.22` | `farb_L = [bas.loc[L, "FAR_B"] * 100 for L in L_vals]  # [11.90, 11.22, 10.45]` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/make_gap3_final.py` | 56 | `8.49` | `frr_L  = [bas.loc[L, "FRR"] * 100 for L in L_vals]    # [8.49, 4.37, 3.54]` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/make_gap3_final.py` | 56 | `3.54` | `frr_L  = [bas.loc[L, "FRR"] * 100 for L in L_vals]    # [8.49, 4.37, 3.54]` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/make_gap3_final.py` | 56 | `4.37` | `frr_L  = [bas.loc[L, "FRR"] * 100 for L in L_vals]    # [8.49, 4.37, 3.54]` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/make_gap3_final.py` | 164 | `64%` | `r"$\Delta\mathrm{FAR}$ ($\mathrm{FAR}_B - \mathrm{FAR}_A$):" + "\n" + "+0.56% → +1.27% → +1.64 pp",` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 8 | `11.55` | `...udit/AUDIT_REPORT.md` \| 14 \| `11.55` \| `\\| FAR\_B baseline \\| 11....` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 9 | `11.55` | `...udit/AUDIT_REPORT.md` \| 15 \| `11.55` \| `\\| FAR\_B baseline \\| 11....` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 9 | `11.90` | `...AR\_B baseline \\| 11.55% \\| **11.90%** \\| `threshold_tra...` \| 11....` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 10 | `11.55` | `...90` \| `... FAR\_B baseline \\| 11.55% \\| **11.90%** \\| `threshold_t...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 10 | `11.90` | `...udit/AUDIT_REPORT.md` \| 15 \| `11.90` \| `... FAR\_B baseline \\| 11...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 11 | `4.17` | `...udit/AUDIT_REPORT.md` \| 16 \| `4.17` \| `\\| FAR\_B robust \\| 4.17%...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 11 | `4.43` | `...\| FAR\_B robust \\| 4.17% \\| **4.43%** \\| `threshold_trad...` \| 4....` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 12 | `4.17` | `...`4.43` \| `\\| FAR\_B robust \\| 4.17% \\| **4.43%** \\| `threshold_tr...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 12 | `4.43` | `...udit/AUDIT_REPORT.md` \| 16 \| `4.43` \| `\\| FAR\_B robust \\| 4.17%...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 13 | `8.49` | `...udit/AUDIT_REPORT.md` \| 17 \| `8.49` \| `\\| FRR baseline \\| 8.49% ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 14 | `30.18` | `...udit/AUDIT_REPORT.md` \| 18 \| `30.18` \| `\\| FRR robust \\| 30.18% \...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 14 | `30.08` | `...`\\| FRR robust \\| 30.18% \\| **30.08%** \\| `threshold_tra...` \| 30....` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 15 | `30.18` | `...\| `30.08` \| `\\| FRR robust \\| 30.18% \\| **30.08%** \\| `threshold_t...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 15 | `30.08` | `...udit/AUDIT_REPORT.md` \| 18 \| `30.08` \| `\\| FRR robust \\| 30.18% \...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 16 | `84.63` | `...udit/AUDIT_REPORT.md` \| 19 \| `84.63` \| `\\| Peak FRR\_robust \\| 84...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 17 | `3.54` | `...udit/AUDIT_REPORT.md` \| 20 \| `3.54` \| `\\| Burst L=5 FRR \\| 3.54%...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 18 | `64%` | `...t_aggrega...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 18 | `0.9670` | `...udit/AUDIT_REPORT.md` \| 21 \| `0.9670` \| `\\| Burst L=5 AUROC \\| 0.9...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 19 | `10.45` | `...udit/AUDIT_REPORT.md` \| 22 \| `10.45` \| `\\| Burst L=5 FAR\_B \\| 10...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 20 | `64%` | `...udit/AUDIT_REPORT.md` \| 23 \| `64%` \| `\\| "Drops intrusion by 64...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 20 | `62.8%` | `...ntrusion by 64%" \\| ~64% \\| **62.8%** (episode ...` \| 62.8% (62.7...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 21 | `64%` | `...\| `62.8%` \| `... intrusion by 64%" \\| ~64% \\| **62.8%** (episod...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 21 | `62.8%` | `...udit/AUDIT_REPORT.md` \| 23 \| `62.8%` \| `... intrusion by 64%" \\| ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 22 | `21.69` | `...udit/AUDIT_REPORT.md` \| 24 \| `21.69` \| `\\| "FRR surge +21.69pp" \...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 22 | `21.59` | `...e +21.69pp" \\| +21.69pp \\| **+21.59pp** ...` \| +21.59 pp (0.21592...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 23 | `21.69` | `...md` \| 24 \| `21.59` \| `...rge +21.69pp" \\| +21.69pp \\| **+21.59pp*...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 23 | `21.59` | `...udit/AUDIT_REPORT.md` \| 24 \| `21.59` \| `...rge +21.69pp" \\| +21.6...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 24 | `11.55` | `...udit/AUDIT_REPORT.md` \| 28 \| `11.55` \| `**FAR\_B baseline (11.55%...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 24 | `11.90` | `...`**FAR\_B baseline (11.55% vs 11.90%):**` \| 11.55% (device bootstr...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 25 | `11.55` | `...`11.90` \| `**FAR\_B baseline (11.55% vs 11.90%):**` \| 11.90% (0.11...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 25 | `11.90` | `...udit/AUDIT_REPORT.md` \| 28 \| `11.90` \| `**FAR\_B baseline (11.55%...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 26 | `11.90` | `...udit/AUDIT_REPORT.md` \| 29 \| `11.90` \| `...de mean over 20 episod...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 27 | `4.17` | `...udit/AUDIT_REPORT.md` \| 31 \| `4.17` \| `**FAR\_B robust (4.17% vs...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 27 | `4.43` | `... \| `**FAR\_B robust (4.17% vs 4.43%):**` \| 4.43% (0.044315, episo...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 28 | `4.17` | `... \| `4.43` \| `**FAR\_B robust (4.17% vs 4.43%):**` \| 4.43% (0.0443...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 28 | `4.43` | `...udit/AUDIT_REPORT.md` \| 31 \| `4.43` \| `**FAR\_B robust (4.17% vs...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 29 | `4.17` | `...udit/AUDIT_REPORT.md` \| 32 \| `4.17` \| `...pository. The README v...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 29 | `4.43` | `...NVERIFIED** in all data...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 30 | `4.43` | `...udit/AUDIT_REPORT.md` \| 32 \| `4.43` \| `...csv` is the episode me...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 31 | `30.18` | `...udit/AUDIT_REPORT.md` \| 34 \| `30.18` \| `**FRR robust (30.18% vs 3...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 31 | `30.08` | `...8` \| `**FRR robust (30.18% vs 30.08%):**` \| 30.08% (0.300789, epis...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 32 | `30.18` | `...34 \| `30.08` \| `**FRR robust (30.18% vs 30.08%):**` \| 30.08% (0.30...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 32 | `30.08` | `...udit/AUDIT_REPORT.md` \| 34 \| `30.08` \| `**FRR robust (30.18% vs 3...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 33 | `30.18` | `...udit/AUDIT_REPORT.md` \| 35 \| `30.18` \| `...(30.08%). The README v...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 33 | `30.08` | `...ORT.md` \| 35 \| `30.18` \| `...(30.08%). The README value of 30.18% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 34 | `30.18` | `...(30.08%). The README value of 30.18% ...` \| 30.08% (0.300789, epis...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 34 | `30.08` | `...udit/AUDIT_REPORT.md` \| 35 \| `30.08` \| `...episode mean is **30.0...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 35 | `21.69` | `...udit/AUDIT_REPORT.md` \| 37 \| `21.69` \| `**FRR surge (+21.69 pp vs...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 35 | `21.59` | `...\| `**FRR surge (+21.69 pp vs +21.59 pp):**` \| +21.59 pp (0.215929...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 36 | `21.69` | `...37 \| `21.59` \| `**FRR surge (+21.69 pp vs +21.59 pp):**` \| +21.59...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 36 | `21.59` | `...udit/AUDIT_REPORT.md` \| 37 \| `21.59` \| `**FRR surge (+21.69 pp vs...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 37 | `30.18` | `...udit/AUDIT_REPORT.md` \| 38 \| `30.18` \| `...69\text{ pp}$ by subtr...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 37 | `30.08` | `...$. From the actual data...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 37 | `8.49` | `... pp}$ by subtracting $30.18 - 8.49$. From the actual data...` \| ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 38 | `21.69` | `...udit/AUDIT_REPORT.md` \| 38 \| `21.69` \| `The README derives $+21.6...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 38 | `21.59` | `...p}$ by subtracting $30...` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 39 | `21.59` | `...udit/AUDIT_REPORT.md` \| 38 \| `21.59` \| `... $30.0789 - 8.4860 = \...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 40 | `30.18` | `...` \| `... pp}$ by subtracting $30.18 - 8.49$. From the actual data...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 40 | `8.49` | `...udit/AUDIT_REPORT.md` \| 38 \| `8.49` \| `... pp}$ by subtracting $...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 41 | `64%` | `...udit/AUDIT_REPORT.md` \| 40 \| `64%` \| `**"Drops intrusion by 64%...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 41 | `62.8%` | `...Drops intrusion by 64%":**` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 42 | `4.17` | `...udit/AUDIT_REPORT.md` \| 41 \| `4.17` \| `Under README's mixed valu...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 42 | `4.43` | `...5 = 63.90\% \approx 64\%$.` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 42 | `64%` | `...17) / 11.55 = 63.90\% \approx 64\%$.` \| 4.43% (0.044315, episo...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 42 | `11.55` | `...nder README's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \ap...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 43 | `4.17` | `...DME's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \approx 64...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 43 | `64%` | `...udit/AUDIT_REPORT.md` \| 41 \| `64%` \| `Under README's mixed valu...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 43 | `62.8%` | `...5 = 63.90\% \approx 64\%$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 43 | `11.55` | `...nder README's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \ap...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 44 | `4.17` | `...DME's mixed values: $(11.55 - 4.17) / 11.55 = 63.90\% \approx 64...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 44 | `64%` | `...17) / 11.55 = 63.90\% \approx 64\%$.` \| 11.55% (device bootstr...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 44 | `11.55` | `...udit/AUDIT_REPORT.md` \| 41 \| `11.55` \| `Under README's mixed valu...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 45 | `4.43` | `...udit/AUDIT_REPORT.md` \| 42 \| `4.43` \| `Under verified episode me...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 45 | `62.8%` | `...46 = \mathbf{62.77\%} \approx 62.8\%$.` \| 4.43% (0.044315, episo...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 45 | `11.90` | `...der verified episode means: $(11.9046 - 4.4315) / 11.9046 = \math...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 46 | `4.43` | `...ed episode means: $(11.9046 - 4.4315) / 11.9046 = \mathbf{62.77\...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 46 | `62.8%` | `...udit/AUDIT_REPORT.md` \| 42 \| `62.8%` \| `Under verified episode me...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 46 | `11.90` | `...der verified episode means: $(11.9046 - 4.4315) / 11.9046 = \math...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 47 | `4.43` | `...ed episode means: $(11.9046 - 4.4315) / 11.9046 = \mathbf{62.77\...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 47 | `62.8%` | `...46 = \mathbf{62.77\%} \approx 62.8\%$.` \| 11.90% (0.119046, epis...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 47 | `11.90` | `...udit/AUDIT_REPORT.md` \| 42 \| `11.90` \| `Under verified episode me...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 48 | `4.17` | `...udit/AUDIT_REPORT.md` \| 48 \| `4.17` \| `### Hit Inventory for "4....` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 48 | `4.43` | `....18", "21.69", and "11.55"` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 48 | `30.18` | `...## Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` \| 4.4...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 48 | `21.69` | `...ventory for "4.17", "30.18", "21.69", and "11.55"` \| 4.43% (0.044...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 48 | `11.55` | `...4.17", "30.18", "21.69", and "11.55"` \| 4.43% (0.044315, episode ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 49 | `4.17` | `...18` \| `### Hit Inventory for "4.17", "30.18", "21.69", and "11.5...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 49 | `30.18` | `...udit/AUDIT_REPORT.md` \| 48 \| `30.18` \| `### Hit Inventory for "4....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 49 | `30.08` | `....18", "21.69", and "11.55"` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 49 | `21.69` | `...ventory for "4.17", "30.18", "21.69", and "11.55"` \| 30.08% (0.30...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 49 | `11.55` | `...4.17", "30.18", "21.69", and "11.55"` \| 30.08% (0.300789, episode...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 50 | `4.17` | `...69` \| `### Hit Inventory for "4.17", "30.18", "21.69", and "11.5...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 50 | `30.18` | `...## Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` \| +21...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 50 | `21.69` | `...udit/AUDIT_REPORT.md` \| 48 \| `21.69` \| `### Hit Inventory for "4....` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 50 | `21.59` | `...18", "21.69", and "11.55"` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 50 | `11.55` | `...4.17", "30.18", "21.69", and "11.55"` \| +21.59 pp (0.215929, epis...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 51 | `4.17` | `...55` \| `### Hit Inventory for "4.17", "30.18", "21.69", and "11.5...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 51 | `30.18` | `...## Hit Inventory for "4.17", "30.18", "21.69", and "11.55"` \| 11....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 51 | `21.69` | `...ventory for "4.17", "30.18", "21.69", and "11.55"` \| 11.55% (devi...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 51 | `11.55` | `...udit/AUDIT_REPORT.md` \| 48 \| `11.55` \| `### Hit Inventory for "4....` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 52 | `11.55` | `...udit/AUDIT_REPORT.md` \| 50 \| `11.55` \| `1. **`11.55`**:` \| 11.55%...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 53 | `4.17` | `...udit/AUDIT_REPORT.md` \| 55 \| `4.17` \| `2. **`4.17`**:` \| 4.43% (...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 53 | `4.43` | `...\| `4.17` \| `2. **`4.17`**:` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 54 | `30.18` | `...udit/AUDIT_REPORT.md` \| 58 \| `30.18` \| `3. **`30.18`**:` \| 30.08%...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 54 | `30.08` | `...`30.18` \| `3. **`30.18`**:` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 55 | `30.08` | `...udit/AUDIT_REPORT.md` \| 60 \| `30.08` \| `- **Does NOT appear in an...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 56 | `21.69` | `...udit/AUDIT_REPORT.md` \| 61 \| `21.69` \| `4. **`21.69`**:` \| +21.59...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 56 | `21.59` | `...21.69` \| `4. **`21.69`**:` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 57 | `30.18` | `...udit/AUDIT_REPORT.md` \| 63 \| `30.18` \| `- Derived textually as $3...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 57 | `30.08` | `... = 21.69\text{ pp}$. Mi...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 57 | `21.69` | `... textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mi...` \| 30.08% (...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 57 | `8.49` | `...Derived textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mi...` \| ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 58 | `30.18` | `... `21.69` \| `... textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mi...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 58 | `21.69` | `...udit/AUDIT_REPORT.md` \| 63 \| `21.69` \| `... textually as $30.18 -...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 58 | `21.59` | `...p}$. Mismatch of 0.10 ...` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 58 | `8.49` | `... \| `... textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mismatch ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 59 | `21.59` | `...udit/AUDIT_REPORT.md` \| 63 \| `21.59` \| `...0 pp against verified ...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 60 | `30.18` | `...` \| `...Derived textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mi...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 60 | `21.69` | `... textually as $30.18 - 8.49 = 21.69\text{ pp}$. Mismatch ...` \| 8...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 60 | `8.49` | `...udit/AUDIT_REPORT.md` \| 63 \| `8.49` \| `...Derived textually as $...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 61 | `11.90` | `...udit/AUDIT_REPORT.md` \| 77 \| `11.90` \| `# pooled_FAR_B(tau_youden...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 62 | `4.17` | `...udit/AUDIT_REPORT.md` \| 78 \| `4.17` \| `# pooled_FAR_B(tau_robust...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 62 | `4.43` | `...`# pooled_FAR_B(tau_robust) = 4.4315%   (does NOT reproduce 4.17...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 63 | `4.17` | `...4.4315%   (does NOT reproduce 4.17%)` \| 4.43% (0.044315, episode ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 63 | `4.43` | `...udit/AUDIT_REPORT.md` \| 78 \| `4.43` \| `# pooled_FAR_B(tau_robust...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 64 | `30.18` | `...udit/AUDIT_REPORT.md` \| 80 \| `30.18` \| `# pooled_FRR(tau_robust) ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 64 | `30.08` | `...does NOT reproduce 30.18%)` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 65 | `4.17` | `...udit/AUDIT_REPORT.md` \| 82 \| `4.17` \| `...de-mean evaluation rep...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 65 | `4.43` | `...18%. Both methods give ...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 65 | `30.18` | `...valuation reproduces 4.17% or 30.18%. Both methods give ...` \| 4.4...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 66 | `4.43` | `...udit/AUDIT_REPORT.md` \| 82 \| `4.43` \| `... or 30.18%. Both metho...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 66 | `30.18` | `...T.md` \| 82 \| `4.43` \| `... or 30.18%. Both methods give 4.43% and ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 66 | `30.08` | `.... Both methods give 4.43% and 30.08%.` \| 4.43% (0.044315, episode ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 67 | `4.17` | `...8` \| `...valuation reproduces 4.17% or 30.18%. Both methods give ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 67 | `4.43` | `... or 30.18%. Both methods give 4.43% and ...` \| 30.08% (0.300789, ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 67 | `30.18` | `...udit/AUDIT_REPORT.md` \| 82 \| `30.18` \| `...valuation reproduces 4...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 67 | `30.08` | `...methods give 4.43% and ...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 68 | `4.43` | `...08` \| `.... Both methods give 4.43% and 30.08%.` \| 30.08% (0.3007...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 68 | `30.08` | `...udit/AUDIT_REPORT.md` \| 82 \| `30.08` \| `.... Both methods give 4....` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 69 | `64%` | `...udit/AUDIT_REPORT.md` \| 97 \| `64%` \| `...`src/evaluate.py`, lin...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 69 | `62.8%` | `...res `dev_ids` to group ...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 70 | `4.43` | `...dit/AUDIT_REPORT.md` \| 100 \| `4.43` \| `..._A = 3.97\%$, $\text{F...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 70 | `30.08` | `...R}_B = 4.43\%$, $\text{FRR} = 30.08\%$, $...` \| 4.43% (0.044315, ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 71 | `4.43` | `... \| 100 \| `30.08` \| `...R}_B = 4.43\%$, $\text{FRR} = 30.08\%$, $...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 71 | `30.08` | `...dit/AUDIT_REPORT.md` \| 100 \| `30.08` \| `...R}_B = 4.43\%$, $\text...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 71 | `0.9490` | `...} = 30.08\%$, $\text{AUROC} = 0.9490$.` \| 30.08% (0.300789, episod...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 72 | `30.08` | `...d` \| 100 \| `0.9490` \| `...} = 30.08\%$, $\text{AUROC} = 0.9490$.`...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 72 | `0.9490` | `...dit/AUDIT_REPORT.md` \| 100 \| `0.9490` \| `...} = 30.08\%$, $\text{A...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 73 | `4.17` | `...dit/AUDIT_REPORT.md` \| 111 \| `4.17` \| `...old lowers FAR from 11...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 73 | `4.43` | `... cost of raising FRR fr...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 73 | `11.55` | `...17` \| `...old lowers FAR from 11.55% to 4.17% at the cost of raisi...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 74 | `30.18` | `...dit/AUDIT_REPORT.md` \| 111 \| `30.18` \| `... of raising FRR from 8...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 74 | `30.08` | `... FRR from 8.49% to 30.18%"` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 74 | `8.49` | `...8` \| `... of raising FRR from 8.49% to 30.18%"` \| 30.08% (0.30078...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 75 | `4.17` | `...old lowers FAR from 11.55% to 4.17% at the cost of raisi...` \| 11...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 75 | `11.55` | `...dit/AUDIT_REPORT.md` \| 111 \| `11.55` \| `...ust threshold lowers F...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 76 | `30.18` | `... of raising FRR from 8.49% to 30.18%"` \| 8.49% (0.084860, FRR epis...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 76 | `8.49` | `...dit/AUDIT_REPORT.md` \| 111 \| `8.49` \| `... the cost of raising F...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 77 | `4.43` | `...dit/AUDIT_REPORT.md` \| 114 \| `4.43` \| `...\text{FAR}_B$) from 11...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 77 | `62.8%` | `...0% to 4.43% (relative drop of 62.8%), whi...` \| 4.43% (0.044315, ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 77 | `11.90` | `...43` \| `...\text{FAR}_B$) from 11.90% to 4.43% (relative drop of 62...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 78 | `30.08` | `...dit/AUDIT_REPORT.md` \| 114 \| `30.08` \| `...t{FRR}$) surges from 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 78 | `21.59` | `...surges from 8.49% to 30.08% (+21.59 pp, worst episode: 84...` \| 3...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 78 | `8.49` | `...8` \| `...t{FRR}$) surges from 8.49% to 30.08% (+21.59 pp, worst e...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 79 | `30.08` | `...9` \| `...surges from 8.49% to 30.08% (+21.59 pp, worst episode: 84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 79 | `21.59` | `...dit/AUDIT_REPORT.md` \| 114 \| `21.59` \| `...surges from 8.49% to 3...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 79 | `8.49` | `...4 \| `21.59` \| `...surges from 8.49% to 30.08% (+21.59 pp, worst e...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 79 | `84.63` | `...8% (+21.59 pp, worst episode: 84.63%)."` \| +21.59 pp (0.215929, ep...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 80 | `4.43` | `...` \| 114 \| `62.8%` \| `...0% to 4.43% (relative drop of 62.8%), whi...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 80 | `62.8%` | `...dit/AUDIT_REPORT.md` \| 114 \| `62.8%` \| `...0% to 4.43% (relative ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 81 | `11.55` | `...dit/AUDIT_REPORT.md` \| 114 \| `11.55` \| `...evice-level bootstrap ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 82 | `4.43` | `...\text{FAR}_B$) from 11.90% to 4.43% (relative drop of 62...` \| 11...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 82 | `11.90` | `...dit/AUDIT_REPORT.md` \| 114 \| `11.90` \| `...tration ($\text{FAR}_B...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 83 | `30.08` | `...t{FRR}$) surges from 8.49% to 30.08% (+21.59 pp, worst e...` \| 8.4...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 83 | `21.59` | `...surges from 8.49% to 30.08% (+21.59 pp, worst e...` \| 8.49% (0.08...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 83 | `8.49` | `...dit/AUDIT_REPORT.md` \| 114 \| `8.49` \| `...on ($\text{FRR}$) surg...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 84 | `21.59` | `...d` \| 114 \| `84.63` \| `...8% (+21.59 pp, worst episode: 84.63%)."`...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 84 | `84.63` | `...dit/AUDIT_REPORT.md` \| 114 \| `84.63` \| `...8% (+21.59 pp, worst e...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 85 | `64%` | `...dit/AUDIT_REPORT.md` \| 117 \| `64%` \| `- Change "drops intrusion...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 85 | `62.8%` | `...-mean stranger penetration by 62.8%"**` \| 62.8% (62.7746% relativ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 86 | `64%` | `...`- Change "drops intrusion by 64%" $\to$ **"reduces episode-mea...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 86 | `62.8%` | `...dit/AUDIT_REPORT.md` \| 117 \| `62.8%` \| `- Change "drops intrusion...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 87 | `21.69` | `...dit/AUDIT_REPORT.md` \| 118 \| `21.69` \| `- Change "FRR surge of +2...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 87 | `21.59` | `...1.69%" $\to$ **"FRR surge of +21.59 pp"**` \| +21.59 pp (0.215929,...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 88 | `21.69` | `...9` \| `- Change "FRR surge of +21.69%" $\to$ **"FRR surge of +21.59...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 88 | `21.59` | `...dit/AUDIT_REPORT.md` \| 118 \| `21.59` \| `- Change "FRR surge of +2...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 89 | `4.17` | `...dit/AUDIT_REPORT.md` \| 143 \| `4.17` \| `...under device-level est...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 89 | `4.43` | `...s not exist in any repo...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 90 | `64%` | `...dit/AUDIT_REPORT.md` \| 168 \| `64%` \| `- $L=5$: $\Delta\text{FAR...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 90 | `62.8%` | `...xt{FAR} = +1.64\text{ pp}$` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 91 | `64%` | `...dit/AUDIT_REPORT.md` \| 170 \| `64%` \| `...hould note this $+0.56...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 91 | `62.8%` | `...pp}$ rise as an **unmat...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 92 | `12.35` | `...FULL_NUMBER_AUDIT.md` \| 12 \| `12.35` \| `...ceptance ($\text{FAR}_...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 93 | `11.55` | `...FULL_NUMBER_AUDIT.md` \| 13 \| `11.55` \| `...etration ($\text{FAR}_...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 94 | `1.47` | `...FULL_NUMBER_AUDIT.md` \| 14 \| `1.47` \| `...{FAR}_{\text{matched}}...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 95 | `2.67` | `...FULL_NUMBER_AUDIT.md` \| 15 \| `2.67` \| `...xy ($k=1$) $\text{FAR}...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 96 | `22.08` | `...FULL_NUMBER_AUDIT.md` \| 16 \| `22.08` \| `...xy ($k=1$) $\text{FAR}...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 97 | `64%` | `...19.4104...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 97 | `19.41` | `...FULL_NUMBER_AUDIT.md` \| 17 \| `19.41` \| `...Gap ($\Delta\text{FAR}...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 98 | `11.90` | `...FULL_NUMBER_AUDIT.md` \| 22 \| `11.90` \| `...}_A$: 11.34%, $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 98 | `11.34` | `...d` \| 22 \| `11.90` \| `...}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\De...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 99 | `11.90` | `...}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\De...` \| 11.34% (0.113422,...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 99 | `11.34` | `...FULL_NUMBER_AUDIT.md` \| 22 \| `11.34` \| `... ($k=15$)** \\| $\text{...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 100 | `99.43` | `...FULL_NUMBER_AUDIT.md` \| 23 \| `99.43` \| `... **Closed-Set Macro $F...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 101 | `0.9490` | `...FULL_NUMBER_AUDIT.md` \| 24 \| `0.9490` \| `...Open-Set $\text{AUROC}...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 102 | `0.9530` | `...FULL_NUMBER_AUDIT.md` \| 25 \| `0.9530` \| `...Open-Set $\text{AUROC}...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 103 | `8.49` | `...FULL_NUMBER_AUDIT.md` \| 26 \| `8.49` \| `...e $\text{FRR}$ (Baseli...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 104 | `98.5` | `...FULL_NUMBER_AUDIT.md` \| 27 \| `98.5` \| `...xt{FAR}_B$ Range** \\| ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 104 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 105 | `0.2097` | `...FULL_NUMBER_AUDIT.md` \| 29 \| `0.2097` \| `...e Spearman $\rho$** \\|...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 105 | `0.1142` | `...o$** \\| $\rho = 0.2097$, $p = 0.1142$, $n = 58$ \\| $\...` \| 0.2097...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 106 | `0.2097` | `....1142` \| `...ho$** \\| $\rho = 0.2097$, $p = 0.1142$, $n = 58$ \\| $...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 106 | `0.1142` | `...FULL_NUMBER_AUDIT.md` \| 29 \| `0.1142` \| `...ho$** \\| $\rho = 0.209...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 107 | `0.0327` | `...FULL_NUMBER_AUDIT.md` \| 30 \| `0.0327` \| `...ation Absolute Error**...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 107 | `0.0323` | `...FULL_NUMBER_AUDIT.md` \| 30 \| `0.0327` \| `...ation Absolute Error*...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 108 | `0.0327` | `...FULL_NUMBER_AUDIT.md` \| 30 \| `0.0323` \| `...ation Absolute Error*...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 108 | `0.0323` | `...FULL_NUMBER_AUDIT.md` \| 30 \| `0.0323` \| `...ation Absolute Error**...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 109 | `11.90` | `...FULL_NUMBER_AUDIT.md` \| 31 \| `11.90` \| `...}_A$: 11.34%, $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 109 | `11.34` | `...d` \| 31 \| `11.90` \| `...}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\te...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 109 | `8.49` | `...AR}_B$: 11.90%, $\text{FRR}$: 8.49%, $\text{...` \| 11.90% (0.1190...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 110 | `11.90` | `...}_A$: 11.34%, $\text{FAR}_B$: 11.90%, $\te...` \| 11.34% (0.113422,...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 110 | `11.34` | `...FULL_NUMBER_AUDIT.md` \| 31 \| `11.34` \| `...rst $L=1$** \\| $\text{...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 111 | `11.90` | `...OC}$: 0.9490 \\| **11.34%**, **11.90%**, **8...` \| 0.9490 (0.948982...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 111 | `11.34` | `..., $\text{AUROC}$: 0.9490 \\| **11.34%**, **11.90%**, **8...` \| 0.94...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 111 | `0.9490` | `...FULL_NUMBER_AUDIT.md` \| 31 \| `0.9490` \| `...FRR}$: 8.49%, $\text{A...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 111 | `8.49` | `... \| 31 \| `0.9490` \| `...FRR}$: 8.49%, $\text{AUROC}$: 0.9490 \\| **...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 112 | `11.90` | `...` \| 31 \| `8.49` \| `...AR}_B$: 11.90%, $\text{FRR}$: 8.49%, $\text{...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 112 | `0.9490` | `...FRR}$: 8.49%, $\text{AUROC}$: 0.9490 \\| **1...` \| 8.49% (0.084860,...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 112 | `8.49` | `...FULL_NUMBER_AUDIT.md` \| 31 \| `8.49` \| `...AR}_B$: 11.90%, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 113 | `64%` | `...FULL_NUMBER_AUDIT.md` \| 32 \| `64%` \| `...}$: 4.37%, $\text{AURO...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 113 | `62.8%` | `....95%**, **11.22%**, **4...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 113 | `11.22` | `...ROC}$: 0.9642 \\| **9.95%**, **11.22%**, **4...` \| 62.8% (62.7746% ...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 113 | `4.37` | `...IT.md` \| 32 \| `64%` \| `...}$: 4.37%, $\text{AUROC}$: 0.9642 \\| **...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 113 | `0.9642` | `......}$: 4.37%, $\text{AUROC}$: 0.9642 \\| **9.95%**, **11.22%**, **4...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 114 | `11.22` | `...FULL_NUMBER_AUDIT.md` \| 32 \| `11.22` \| `...R}_A$: 9.95%, $\text{F...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 114 | `4.37` | `...AR}_B$: 11.22%, $\text{FRR}$: 4.37%, $\text{...` \| 11.22% (0.1121...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 115 | `64%` | `...}$: 4.37%, $\text{AUROC}$: 0.9642 \\| **9...` \| 4.37% (0.043740...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 115 | `11.22` | `...` \| 32 \| `4.37` \| `...AR}_B$: 11.22%, $\text{FRR}$: 4.37%, $\text{...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 115 | `4.37` | `...FULL_NUMBER_AUDIT.md` \| 32 \| `4.37` \| `...AR}_B$: 11.22%, $\text...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 115 | `0.9642` | `...FRR}$: 4.37%, $\text{AUROC}$: 0.9642 \\| **9...` \| 4.37% (0.043740,...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 116 | `64%` | `...L_NUMBER_AUDIT.md` \| 32 \| `0.9642` \| `...FRR}$: 4.37%, $\text{...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 116 | `11.22` | `...ROC}$: 0.9642 \\| **9.95%**, **11.22%**, **4....` \| 0.9642 (0.96424...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 116 | `4.37` | `... \| 32 \| `0.9642` \| `...FRR}$: 4.37%, $\text{AUROC}$: 0.9642 \\| **...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 116 | `0.9642` | `...FULL_NUMBER_AUDIT.md` \| 32 \| `0.9642` \| `...FRR}$: 4.37%, $\text{A...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 117 | `3.54` | `...FULL_NUMBER_AUDIT.md` \| 33 \| `3.54` \| `...AR}_B$: 10.45%, $\text...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 117 | `10.45` | `...` \| 33 \| `3.54` \| `...AR}_B$: 10.45%, $\text{FRR}$: 3.54%, $\text{...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 117 | `0.9670` | `...FRR}$: 3.54%, $\text{AUROC}$: 0.9670 \\| **8...` \| 3.54% (0.035369,...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 118 | `3.54` | `...AR}_B$: 10.45%, $\text{FRR}$: 3.54%, $\text{...` \| 10.45% (0.1045...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 118 | `10.45` | `...FULL_NUMBER_AUDIT.md` \| 33 \| `10.45` \| `...R}_A$: 8.81%, $\text{F...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 119 | `64%` | `...%**, **3....` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 119 | `3.54` | `... \| 33 \| `0.9670` \| `...FRR}$: 3.54%, $\text{AUROC}$: 0.9670 \\| **...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 119 | `10.45` | `...ROC}$: 0.9670 \\| **8.81%**, **10.45%**, **3....` \| 0.9670 (0.96696...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 119 | `0.9670` | `...FULL_NUMBER_AUDIT.md` \| 33 \| `0.9670` \| `...FRR}$: 3.54%, $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 120 | `98.5` | `...FULL_NUMBER_AUDIT.md` \| 52 \| `98.5` \| `### Mismatch: "Per-device...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 120 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 121 | `98.5` | `...FULL_NUMBER_AUDIT.md` \| 53 \| `98.5` \| `...00%** (with device 49 ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 121 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 122 | `98.5` | `...FULL_NUMBER_AUDIT.md` \| 56 \| `98.5` \| `> "Per-device vulnerabili...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 122 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 123 | `98.5` | `...FULL_NUMBER_AUDIT.md` \| 58 \| `98.5` \| `...on reaching up to 100....` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 123 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 124 | `65.7` | `...FULL_NUMBER_AUDIT.md` \| 58 \| `65.7` \| `...erability ranges from ...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 125 | `4.43` | `...t/gap3_paper_text.md` \| 10 \| `4.43` \| `...xt{robust}}$: $\text{F...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 125 | `30.08` | `...R}_B = 4.43\%$, $\text{FRR} = 30.08\%$). ...` \| 4.43% (0.044315, ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 126 | `4.43` | `...` \| 10 \| `30.08` \| `...R}_B = 4.43\%$, $\text{FRR} = 30.08\%$). ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 126 | `30.08` | `...t/gap3_paper_text.md` \| 10 \| `30.08` \| `...R}_B = 4.43\%$, $\text...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 127 | `64%` | `...t/gap3_paper_text.md` \| 10 \| `64%` \| `....56\text{ pp}$ at $L=1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 127 | `62.8%` | `...$1.64\text{ pp}$ at $L=5$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 128 | `11.90` | `...t/gap3_paper_text.md` \| 10 \| `11.90` \| `...ns (baseline: $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 128 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$; ro...` \| 11.90% (0.119046...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 129 | `11.90` | `...md` \| 10 \| `8.49` \| `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$; ro...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 129 | `8.49` | `...t/gap3_paper_text.md` \| 10 \| `8.49` \| `...}_B = 11.90\%$, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 130 | `3.54` | `...t/gap3_paper_text.md` \| 10 \| `3.54` \| `...timate $\text{FRR}$ dr...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 131 | `10.45` | `...t/gap3_paper_text.md` \| 10 \| `10.45` \| `... $\text{FAR}_B$ decrea...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 132 | `4.43` | `...t/gap3_paper_text.md` \| 18 \| `4.43` \| `...$) falls from **11.90%...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 132 | `62.8%` | `...4.43%**, corresponding to a **62.8%...` \| 4.43% (0.044315, episod...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 132 | `11.90` | `... `4.43` \| `...$) falls from **11.90%** to **4.43%**, corresponding...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 133 | `4.43` | `...text.md` \| 18 \| `62.8%` \| `...4.43%**, corresponding to a **62.8%...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 133 | `62.8%` | `...t/gap3_paper_text.md` \| 18 \| `62.8%` \| `...4.43%**, corresponding...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 134 | `11.55` | `...t/gap3_paper_text.md` \| 18 \| `11.55` \| `... baseline $\text{FAR}_...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 135 | `4.43` | `...$) falls from **11.90%** to **4.43%**, corresponding...` \| 11.90%...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 135 | `11.90` | `...t/gap3_paper_text.md` \| 18 \| `11.90` \| `...($\text{FAR}_B$) falls...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 136 | `30.08` | `...t/gap3_paper_text.md` \| 20 \| `30.08` \| `...r $\tau_{\text{Youden}...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 137 | `21.59` | `...t/gap3_paper_text.md` \| 20 \| `21.59` \| `...ng an availability los...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 138 | `8.49` | `...t/gap3_paper_text.md` \| 20 \| `8.49` \| `...enrolled meters surges...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 139 | `84.63` | `...t/gap3_paper_text.md` \| 20 \| `84.63` \| `...an **26.23%**) to a pe...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 140 | `11.90` | `...t/gap3_paper_text.md` \| 22 \| `11.90` \| `..._B$ decreases modestly...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 140 | `10.45` | `... from **11.90%** ($L=1$) to **10.45%** ($L=5...` \| 11.90% (0.11904...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 141 | `3.54` | `...t/gap3_paper_text.md` \| 22 \| `3.54` \| `...timate $\text{FRR}$ do...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 142 | `11.90` | `... \| 22 \| `10.45` \| `... from **11.90%** ($L=1$) to **10.45%** ($L=5...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 142 | `10.45` | `...t/gap3_paper_text.md` \| 22 \| `10.45` \| `... from **11.90%** ($L=1...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 143 | `64%` | `..._B$ decre...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 143 | `0.9670` | `...t/gap3_paper_text.md` \| 22 \| `0.9670` \| `...scrimination to an AUR...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 144 | `64%` | `...t/gap3_paper_text.md` \| 30 \| `64%` \| `...rcentage points at $L=...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 144 | `62.8%` | `...tage points at $L=5$. B...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 145 | `10.45` | `...t/gap3_paper_text.md` \| 30 \| `10.45` \| `...on ($\text{FAR}_B$ rem...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 146 | `11.55` | `...t/gap3_paper_text.md` \| 54 \| `11.55` \| `& $11.55^\dagger$ [7.03, ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 147 | `8.49` | `...t/gap3_paper_text.md` \| 55 \| `8.49` \| `& $8.49$ [7.16, 10.06]` \|...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 148 | `0.9490` | `...t/gap3_paper_text.md` \| 56 \| `0.9490` \| `& $0.9490$ [0.9367, 0.960...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 149 | `4.43` | `...t/gap3_paper_text.md` \| 59 \| `4.43` \| `& $4.43$` \| 4.43% (0.0443...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 150 | `30.08` | `...t/gap3_paper_text.md` \| 60 \| `30.08` \| `& $30.08$` \| 30.08% (0.30...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 151 | `0.9490` | `...t/gap3_paper_text.md` \| 61 \| `0.9490` \| `& $0.9490$` \| 0.9490 (0.9...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 152 | `11.90` | `...t/gap3_paper_text.md` \| 65 \| `11.90` \| `& $11.90$` \| 11.90% (0.11...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 153 | `8.49` | `...t/gap3_paper_text.md` \| 66 \| `8.49` \| `& $8.49$` \| 8.49% (0.0848...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 154 | `0.9490` | `...t/gap3_paper_text.md` \| 67 \| `0.9490` \| `& $0.9490$` \| 0.9490 (0.9...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 155 | `11.22` | `...t/gap3_paper_text.md` \| 70 \| `11.22` \| `& $11.22$` \| 11.22% (0.11...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 156 | `4.37` | `...t/gap3_paper_text.md` \| 71 \| `4.37` \| `& $4.37$` \| 4.37% (0.0437...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 157 | `64%` | `...t/gap3_paper_text.md` \| 72 \| `64%` \| `& $0.9642$` \| 62.8% (62.7...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 157 | `62.8%` | `...\| 72 \| `64%` \| `& $0.9642$` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 157 | `0.9642` | `...r_text.md` \| 72 \| `64%` \| `& $0.9642$` \| 62.8% (62.7746% relative ...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 158 | `64%` | `...ap3_paper_text.md` \| 72 \| `0.9642` \| `& $0.9642$` \| 0.9642 (0....` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 158 | `0.9642` | `...t/gap3_paper_text.md` \| 72 \| `0.9642` \| `& $0.9642$` \| 0.9642 (0.9...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 159 | `10.45` | `...t/gap3_paper_text.md` \| 75 \| `10.45` \| `& $10.45$` \| 10.45% (0.10...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 160 | `3.54` | `...t/gap3_paper_text.md` \| 76 \| `3.54` \| `& $3.54$` \| 3.54% (0.0353...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 161 | `64%` | `... `& $0.9670$` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 161 | `0.9670` | `...t/gap3_paper_text.md` \| 77 \| `0.9670` \| `& $0.9670$` \| 0.9670 (0.9...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 162 | `11.90` | `...t/gap3_paper_text.md` \| 84 \| `11.90` \| `...vices (plain episode m...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 163 | `84.63` | `...t/make_gap3_final.py` \| 99 \| `84.63` \| `# Outlier episode annotat...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 164 | `64%` | `.../make_gap3_final.py` \| 141 \| `64%` \| `r"$\Delta\mathrm{FAR}$ ($...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 164 | `62.8%` | `....56% → +1.27% → +1.64 pp",` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 165 | `4.17` | `...udit/scan_numbers.py` \| 29 \| `4.17` \| `(r'4\.17%?', "4.17", "4.4...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 165 | `4.43` | `....17` \| `(r'4\.17%?', "4.17", "4.43% (0.044315, episode mean)", "S...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 166 | `4.17` | `... 29 \| `4.43` \| `(r'4\.17%?', "4.17", "4.43% (0.044315, episode m...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 166 | `4.43` | `...udit/scan_numbers.py` \| 29 \| `4.43` \| `(r'4\.17%?', "4.17", "4.4...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 167 | `4.43` | `...udit/scan_numbers.py` \| 30 \| `4.43` \| `(r'4\.43%?', "4.43", "4.4...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 168 | `30.18` | `...udit/scan_numbers.py` \| 31 \| `30.18` \| `(r'30\.18%?', "30.18", "3...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 168 | `30.08` | `...8` \| `(r'30\.18%?', "30.18", "30.08% (0.300789, episode mean)", "S...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 169 | `30.18` | `...1 \| `30.08` \| `(r'30\.18%?', "30.18", "30.08% (0.300789, episode ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 169 | `30.08` | `...udit/scan_numbers.py` \| 31 \| `30.08` \| `(r'30\.18%?', "30.18", "3...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 170 | `30.08` | `...udit/scan_numbers.py` \| 32 \| `30.08` \| `(r'30\.08%?', "30.08", "3...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 171 | `21.69` | `...udit/scan_numbers.py` \| 33 \| `21.69` \| `(r'21\.69%?', "21.69", "+...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 171 | `21.59` | `...` \| `(r'21\.69%?', "21.69", "+21.59 pp (0.215929, episo...` \| +21...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 172 | `21.69` | `...3 \| `21.59` \| `(r'21\.69%?', "21.69", "+21.59 pp (0.215929, episo...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 172 | `21.59` | `...udit/scan_numbers.py` \| 33 \| `21.59` \| `(r'21\.69%?', "21.69", "+...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 173 | `21.59` | `...udit/scan_numbers.py` \| 34 \| `21.59` \| `(r'21\.59%?', "21.59", "+...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 174 | `64%` | `...udit/scan_numbers.py` \| 35 \| `64%` \| `(r'64%?', "64%", "62.8% (...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 174 | `62.8%` | `... \| `64%` \| `(r'64%?', "64%", "62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 175 | `64%` | `...bers.py` \| 35 \| `62.8%` \| `(r'64%?', "64%", "62.8% (62.7746% re...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 175 | `62.8%` | `...udit/scan_numbers.py` \| 35 \| `62.8%` \| `(r'64%?', "64%", "62.8% (...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 176 | `62.8%` | `...udit/scan_numbers.py` \| 36 \| `62.8%` \| `(r'62\.8%?', "62.8%", "62...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 177 | `11.55` | `...udit/scan_numbers.py` \| 37 \| `11.55` \| `(r'11\.55%?', "11.55", "1...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 178 | `11.90` | `...udit/scan_numbers.py` \| 38 \| `11.90` \| `(r'11\.90%?', "11.90", "1...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 179 | `12.35` | `...udit/scan_numbers.py` \| 39 \| `12.35` \| `(r'12\.35%?', "12.35", "1...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 180 | `11.34` | `...udit/scan_numbers.py` \| 40 \| `11.34` \| `(r'11\.34%?', "11.34", "1...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 181 | `2.67` | `...udit/scan_numbers.py` \| 41 \| `2.67` \| `(r'2\.67%?', "2.67", "2.6...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 182 | `22.08` | `...udit/scan_numbers.py` \| 42 \| `22.08` \| `(r'22\.08%?', "22.08", "2...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 183 | `64%` | `...udit/scan_numbers.py` \| 43 \| `64%` \| `(r'19\.41%?', "19.41", "+...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 183 | `62.8%` | `..., "VERIFIED (sweep k=1)"),` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 183 | `19.41` | `... 43 \| `64%` \| `(r'19\.41%?', "19.41", "+19.41% (+0.194064, k=1 De...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 184 | `64%` | `...?', "19.41", "+19.41% (+0.194064, k=1 DeltaFAR mean)", "VERIFI...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 184 | `19.41` | `...udit/scan_numbers.py` \| 43 \| `19.41` \| `(r'19\.41%?', "19.41", "+...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 185 | `99.43` | `...udit/scan_numbers.py` \| 44 \| `99.43` \| `(r'99\.43%?', "99.43", "9...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 186 | `0.9490` | `...udit/scan_numbers.py` \| 45 \| `0.9490` \| `(r'0\.9490?', "0.9490", "...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 187 | `0.9530` | `...udit/scan_numbers.py` \| 46 \| `0.9530` \| `(r'0\.9530?', "0.9530", "...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 188 | `8.49` | `...udit/scan_numbers.py` \| 47 \| `8.49` \| `(r'8\.49%?', "8.49", "8.4...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 189 | `98.5` | `...udit/scan_numbers.py` \| 48 \| `98.5` \| `(r'98\.5%?', "98.5", "STA...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 189 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 190 | `65.7` | `...udit/scan_numbers.py` \| 48 \| `65.7` \| `...49). Device-mean FAR_B...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 191 | `65.7` | `...udit/scan_numbers.py` \| 49 \| `65.7` \| `(r'65\.7%?', "65.7", "65....` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 192 | `0.2097` | `...udit/scan_numbers.py` \| 50 \| `0.2097` \| `(r'0\.2097?', "0.2097", "...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 193 | `0.1142` | `...udit/scan_numbers.py` \| 51 \| `0.1142` \| `(r'0\.1142?', "0.1142", "...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 194 | `0.0327` | `...udit/scan_numbers.py` \| 52 \| `0.0327` \| `(r'0\.0327?', "0.0327", "...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 194 | `0.0323` | `...udit/scan_numbers.py` \| 52 \| `0.0327` \| `(r'0\.0327?', "0.0327", ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 195 | `0.0327` | `...udit/scan_numbers.py` \| 52 \| `0.0323` \| `(r'0\.0327?', "0.0327", ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 195 | `0.0323` | `...udit/scan_numbers.py` \| 52 \| `0.0323` \| `(r'0\.0327?', "0.0327", "...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 196 | `0.0327` | `...udit/scan_numbers.py` \| 53 \| `0.0327` \| `(r'0\.0323?', "0.0323", "...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 196 | `0.0323` | `...udit/scan_numbers.py` \| 53 \| `0.0327` \| `(r'0\.0323?', "0.0323", ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 197 | `0.0327` | `...udit/scan_numbers.py` \| 53 \| `0.0323` \| `(r'0\.0323?', "0.0323", ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 197 | `0.0323` | `...udit/scan_numbers.py` \| 53 \| `0.0323` \| `(r'0\.0323?', "0.0323", "...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 198 | `1.47` | `...udit/scan_numbers.py` \| 54 \| `1.47` \| `(r'1\.47%?', "1.47", "+1....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 199 | `3.54` | `...udit/scan_numbers.py` \| 55 \| `3.54` \| `(r'3\.54%?', "3.54", "3.5...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 200 | `10.45` | `...udit/scan_numbers.py` \| 56 \| `10.45` \| `(r'10\.45%?', "10.45", "1...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 201 | `11.22` | `...udit/scan_numbers.py` \| 57 \| `11.22` \| `(r'11\.22%?', "11.22", "1...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 202 | `4.37` | `...udit/scan_numbers.py` \| 58 \| `4.37` \| `(r'4\.37%?', "4.37", "4.3...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 203 | `64%` | `...udit/scan_numbers.py` \| 59 \| `64%` \| `(r'0\.9642?', "0.9642", "...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 203 | `62.8%` | `....9642", "0.9642 (0.9642...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 203 | `0.9642` | `... 59 \| `64%` \| `(r'0\.9642?', "0.9642", "0.9642 (0.9642...` \| 62.8%...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 204 | `64%` | `...t/scan_numbers.py` \| 59 \| `0.9642` \| `(r'0\.9642?', "0.9642", ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 204 | `0.9642` | `...udit/scan_numbers.py` \| 59 \| `0.9642` \| `(r'0\.9642?', "0.9642", "...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 205 | `64%` | `...udit/scan_numbers.py` \| 60 \| `64%` \| `...0?', "0.9670", "0.9670...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 205 | `62.8%` | `... L=5 AUROC at tau_Youde...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 205 | `0.9670` | `....py` \| 60 \| `64%` \| `...0?', "0.9670", "0.9670 (0.966964, burst L=...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 206 | `64%` | `...0?', "0.9670", "0.9670 (0.966964, burst L=...` \| 0.9670 (0.966...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 206 | `0.9670` | `...udit/scan_numbers.py` \| 60 \| `0.9670` \| `(r'0\.9670?', "0.9670", "...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 207 | `84.63` | `...udit/scan_numbers.py` \| 61 \| `84.63` \| `(r'84\.63%?', "84.63", "8...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 208 | `84.63` | `...dit/TASK1_numbers.py` \| 50 \| `84.63` \| `f"(README claims 84.63%)"...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 209 | `11.55` | `...dit/TASK1_numbers.py` \| 75 \| `11.55` \| `print(f"    → README clai...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 210 | `11.90` | `...dit/TASK1_numbers.py` \| 81 \| `11.90` \| `print(f"    mean = {mean_...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 211 | `8.49` | `...dit/TASK1_numbers.py` \| 87 \| `8.49` \| `print(f"    mean = {row_f...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 212 | `4.17` | `...dit/TASK1_numbers.py` \| 92 \| `4.17` \| `print(f"    mean = {mean_...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 212 | `4.43` | `...%  → README claims 4.17%")` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 213 | `30.18` | `...dit/TASK1_numbers.py` \| 97 \| `30.18` \| `print(f"    mean = {mean_...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 213 | `30.08` | `...  → README claims 30.18%")` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 214 | `64%` | `...ims 0.9670")` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 214 | `0.9670` | `...it/TASK1_numbers.py` \| 102 \| `0.9670` \| `print(f"    value = {auro...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 215 | `3.54` | `...it/TASK1_numbers.py` \| 107 \| `3.54` \| `print(f"    value = {frr_...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 216 | `10.45` | `...it/TASK1_numbers.py` \| 112 \| `10.45` \| `print(f"    value = {farb...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 217 | `84.63` | `...it/TASK1_numbers.py` \| 114 \| `84.63` \| `# Peak 84.63%: check epis...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 218 | `84.63` | `...it/TASK1_numbers.py` \| 115 \| `84.63` \| `print(f"\n  Peak FRR_robu...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 219 | `84.63` | `...it/TASK1_numbers.py` \| 117 \| `84.63` \| `f"→ README claims 84.63%"...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 220 | `11.55` | `...it/TASK1_numbers.py` \| 131 \| `11.55` \| `"11.55%", f"{row_farb['me...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 221 | `11.55` | `...it/TASK1_numbers.py` \| 134 \| `11.55` \| `"MISMATCH" if abs(row_far...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 222 | `11.55` | `...it/TASK1_numbers.py` \| 137 \| `11.55` \| `"11.55%", f"{mean_far_you...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 223 | `4.17` | `...it/TASK1_numbers.py` \| 143 \| `4.17` \| `"4.17%", f"{mean_far_robu...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 223 | `4.43` | `...f"{mean_far_robust:.2f}%",` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 224 | `4.17` | `...it/TASK1_numbers.py` \| 146 \| `4.17` \| `"MISMATCH" if abs(mean_fa...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 224 | `4.43` | `....17) > 0.005 else "PASS"),` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 225 | `8.49` | `...it/TASK1_numbers.py` \| 149 \| `8.49` \| `"8.49%", f"{row_frr['mean...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 226 | `8.49` | `...it/TASK1_numbers.py` \| 152 \| `8.49` \| `"PASS" if abs(row_frr['me...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 227 | `30.18` | `...it/TASK1_numbers.py` \| 155 \| `30.18` \| `"30.18%", f"{mean_frr_rob...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 227 | `30.08` | `...f"{mean_frr_robust:.2f}%",` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 228 | `30.18` | `...it/TASK1_numbers.py` \| 158 \| `30.18` \| `"MISMATCH" if abs(mean_fr...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 228 | `30.08` | `...0.18) > 0.05 else "PASS"),` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 229 | `84.63` | `...it/TASK1_numbers.py` \| 161 \| `84.63` \| `"84.63%", f"{tt['FRR_robu...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 230 | `64%` | `\| `audit/TASK1_numbers.py` \| 164 \| `84.63` \| `"PASS" if abs(tt...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 230 | `84.63` | `...it/TASK1_numbers.py` \| 164 \| `84.63` \| `"PASS" if abs(tt['FRR_rob...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 231 | `3.54` | `...it/TASK1_numbers.py` \| 167 \| `3.54` \| `"3.54%", f"{frr_l5:.2f}%"...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 232 | `3.54` | `...it/TASK1_numbers.py` \| 170 \| `3.54` \| `"PASS" if abs(frr_l5 - 3....` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 233 | `64%` | `...oc_l5:.4f}",` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 233 | `0.9670` | `...it/TASK1_numbers.py` \| 173 \| `0.9670` \| `"0.9670", f"{auroc_l5:.4f...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 234 | `64%` | `..."MISMATCH"),` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 234 | `0.9670` | `...it/TASK1_numbers.py` \| 176 \| `0.9670` \| `"PASS" if abs(auroc_l5 - ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 235 | `10.45` | `...it/TASK1_numbers.py` \| 179 \| `10.45` \| `"10.45%", f"{farb_l5:.2f}...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 236 | `10.45` | `...it/TASK1_numbers.py` \| 182 \| `10.45` \| `"PASS" if abs(farb_l5 - 1...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 237 | `11.55` | `...it/TASK1_numbers.py` \| 191 \| `11.55` \| `README/abstract FAR_B = 1...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 238 | `4.17` | `...it/TASK1_numbers.py` \| 197 \| `4.17` \| `For FAR_B robust (4.17% v...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 238 | `4.43` | `...ch — no device-level value` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 239 | `11.55` | `...it/TASK1_numbers.py` \| 200 \| `11.55` \| `is used. If 11.55% (devic...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 240 | `64%` | `...it/TASK1_numbers.py` \| 238 \| `64%` \| `# "drops intrusion by 64%...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 240 | `62.8%` | `...# "drops intrusion by 64%"` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 241 | `11.55` | `...it/TASK1_numbers.py` \| 239 \| `11.55` \| `readme_farb_base   = 11.5...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 242 | `4.17` | `...it/TASK1_numbers.py` \| 240 \| `4.17` \| `readme_farb_robust = 4.17...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 242 | `4.43` | `...`readme_farb_robust = 4.17` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 243 | `64%` | `...it/TASK1_numbers.py` \| 246 \| `64%` \| `print(f"\n  'Drops intrus...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 243 | `62.8%` | `...intrusion by 64%' claim:")` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 244 | `64%` | `...it/TASK1_numbers.py` \| 250 \| `64%` \| `...lue {readme_reduction:...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 244 | `62.8%` | `...ct under README numbers...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 245 | `21.69` | `...it/TASK1_numbers.py` \| 252 \| `21.69` \| `# "FRR surge of +21.69%"`...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 245 | `21.59` | `...`# "FRR surge of +21.69%"` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 246 | `8.49` | `...it/TASK1_numbers.py` \| 253 \| `8.49` \| `readme_frr_base   = 8.49`...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 247 | `30.18` | `...it/TASK1_numbers.py` \| 254 \| `30.18` \| `readme_frr_robust = 30.18...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 247 | `30.08` | `...`readme_frr_robust = 30.18` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 248 | `21.69` | `...it/TASK1_numbers.py` \| 258 \| `21.69` \| `print(f"\n  'FRR surge of...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 248 | `21.59` | `...urge of +21.69%' claim:")` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 249 | `21.69` | `...it/TASK1_numbers.py` \| 261 \| `21.69` \| `...SS' if abs(readme_frr_...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 249 | `21.59` | `... 0.005 else 'MISMATCH'}")` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 250 | `11.90` | `...it/TASK1_numbers.py` \| 277 \| `11.90` \| `print(f"  → FAR_B DECREAS...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 250 | `10.45` | `... DECREASES slightly (11.90% → 10.45%) while FAR_A also decreases,"...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 251 | `11.90` | `...  → FAR_B DECREASES slightly (11.90% → 10.45%) while FAR_A also de...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 251 | `10.45` | `...it/TASK1_numbers.py` \| 277 \| `10.45` \| `print(f"  → FAR_B DECREAS...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 252 | `11.55` | `...it/TASK1_numbers.py` \| 324 \| `11.55` \| `{'FAR_B baseline':<42} \\|...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 253 | `11.55` | `...it/TASK1_numbers.py` \| 325 \| `11.55` \| `... baseline (ep mean)':<...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 254 | `4.17` | `...it/TASK1_numbers.py` \| 326 \| `4.17` \| `{'FAR_B robust':<42} \\| {...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 254 | `4.43` | `... {f'{mean_far_robust:.2...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 255 | `8.49` | `...it/TASK1_numbers.py` \| 327 \| `8.49` \| `{'FRR baseline':<42} \\| {...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 256 | `30.18` | `...it/TASK1_numbers.py` \| 328 \| `30.18` \| `...RR robust (ep mean)':<...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 256 | `30.08` | `... {f'{mean_frr_robust:.2...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 257 | `84.63` | `...it/TASK1_numbers.py` \| 329 \| `84.63` \| `{'Peak FRR_robust':<42} \...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 258 | `3.54` | `...it/TASK1_numbers.py` \| 330 \| `3.54` \| `{'Burst L=5 FRR':<42} \\| ...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 259 | `64%` | `....4f}':>10...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 259 | `0.9670` | `...it/TASK1_numbers.py` \| 331 \| `0.9670` \| `{'Burst L=5 AUROC':<42} \...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 260 | `10.45` | `...it/TASK1_numbers.py` \| 332 \| `10.45` \| `{'Burst L=5 FAR_B':<42} \...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 261 | `64%` | `...it/TASK1_numbers.py` \| 333 \| `64%` \| `{'Intrusion drop ~64%':<4...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 261 | `62.8%` | `... {'~64%':>8} \\| {f'{ep_...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 262 | `21.69` | `...it/TASK1_numbers.py` \| 334 \| `21.69` \| `{'FRR surge +21.69pp':<42...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 262 | `21.59` | `...\| {'+21.69pp':>8} \\| {...` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 263 | `2.67` | `...udit/verify_sweep.py` \| 23 \| `2.67` \| `# k=1: single-proxy disto...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 263 | `22.08` | `...s +19.41%, FAR_A=2.67%, FAR_B=22.08%` \| 2.67% (0.026744, k=1 FAR_A...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 263 | `19.41` | `...distortion gap — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` \|...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 264 | `2.67` | `... — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` \| 22.08% (0.22...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 264 | `22.08` | `...udit/verify_sweep.py` \| 23 \| `22.08` \| `# k=1: single-proxy disto...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 264 | `19.41` | `...distortion gap — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` \|...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 265 | `64%` | `...R_B=22.08%` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 265 | `2.67` | `... — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` \| +19.41% (+0....` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 265 | `22.08` | `...s +19.41%, FAR_A=2.67%, FAR_B=22.08%` \| +19.41% (+0.194064, k=1 De...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 265 | `19.41` | `...udit/verify_sweep.py` \| 23 \| `19.41` \| `# k=1: single-proxy disto...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 266 | `2.67` | `...udit/verify_sweep.py` \| 24 \| `2.67` \| `print("README claims k=1:...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 266 | `22.08` | `...laims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")` \| 2.67% (0.02...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 266 | `19.41` | `...R_A=2.67%, FAR_B=22.08%, gap=+19.41%")` \| 2.67% (0.026744, k=1 FAR...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 267 | `2.67` | `...int("README claims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")`...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 267 | `22.08` | `...udit/verify_sweep.py` \| 24 \| `22.08` \| `print("README claims k=1:...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 267 | `19.41` | `...R_A=2.67%, FAR_B=22.08%, gap=+19.41%")` \| 22.08% (0.220808, k=1 FA...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 268 | `64%` | `...=+19.41%")` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 268 | `2.67` | `...int("README claims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")`...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 268 | `22.08` | `...laims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")` \| +19.41% (+0...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 268 | `19.41` | `...udit/verify_sweep.py` \| 24 \| `19.41` \| `print("README claims k=1:...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 269 | `2.67` | `\| `paper/abstract.md` \| 5 \| `2.67` \| `...sting reports $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 270 | `22.08` | `\| `paper/abstract.md` \| 5 \| `22.08` \| `... penetrate at $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 271 | `64%` | `...iar tes...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 271 | `19.41` | `\| `paper/abstract.md` \| 5 \| `19.41` \| `...($k=1$) creates a dang...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 272 | `1.47` | `\| `paper/abstract.md` \| 5 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 273 | `4.43` | `\| `paper/abstract.md` \| 7 \| `4.43` \| `...enetration from $11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 273 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` \| 4.43%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 273 | `11.90` | `...`4.43` \| `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 274 | `30.08` | `\| `paper/abstract.md` \| 7 \| `30.08` \| `...Rate surges from $8.49...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 274 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting ne...` \| 30.0...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 274 | `8.49` | `...0.08` \| `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) —...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 275 | `30.08` | `....59` \| `... from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting ne...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 275 | `21.59` | `\| `paper/abstract.md` \| 7 \| `21.59` \| `... from $8.49\%$ to $30....` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 275 | `8.49` | `...d` \| 7 \| `21.59` \| `... from $8.49\%$ to $30.08\%$ (+21.59 pp) —...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 276 | `4.43` | `...2.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 276 | `62.8%` | `\| `paper/abstract.md` \| 7 \| `62.8%` \| `...rom $11.90\%$ to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 276 | `11.90` | `....md` \| 7 \| `62.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 277 | `11.55` | `\| `paper/abstract.md` \| 7 \| `11.55` \| `... $0.949$ with $\text{F...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 277 | `0.9490` | `...act.md` \| 7 \| `11.55` \| `... $0.949$ with $\text{FAR}_B = 11.55\%...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 278 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 278 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90% (0.119046,...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 278 | `11.90` | `\| `paper/abstract.md` \| 7 \| `11.90` \| `...ue-stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 279 | `99.43` | `\| `paper/abstract.md` \| 7 \| `99.43` \| `...-set classification ac...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 280 | `11.55` | `... $0.949$ with $\text{FAR}_B = 11.55\%...` \| 0.9490 (0.948982, AUR...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 280 | `0.9490` | `\| `paper/abstract.md` \| 7 \| `0.9490` \| `...$F_1$, the open-set AU...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 281 | `30.08` | `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) —...` \| 8.49% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 281 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp) —...` \| 8.49% (0.084860, ...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 281 | `8.49` | `\| `paper/abstract.md` \| 7 \| `8.49` \| `...e Rejection Rate surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 282 | `98.5` | `\| `paper/abstract.md` \| 7 \| `98.5` \| `...ly heterogeneous ($0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 282 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 283 | `64%` | `...rature_comparison.csv` \| 4 \| `64%` \| `...eature map,Contrastive...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 283 | `62.8%` | `...type space),292 complex...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 284 | `99.43` | `...rature_comparison.csv` \| 5 \| `99.43` \| `Closed-Set Accuracy / F1,...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 285 | `0.9490` | `...rature_comparison.csv` \| 6 \| `0.9490` \| `...80% - 98%,90.23%,~92.5...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 285 | `0.9530` | `...2.5%,91.3%,0.9490 (AUROC_B) / 0.9530 (AUROC_A)` \| 0.9490 (0.948982...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 286 | `0.9490` | `...6 \| `0.9530` \| `...2.5%,91.3%,0.9490 (AUROC_B) / 0.9530 (AUROC_A)`...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 286 | `0.9530` | `...rature_comparison.csv` \| 6 \| `0.9530` \| `...2.5%,91.3%,0.9490 (AUR...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 287 | `12.35` | `...rature_comparison.csv` \| 7 \| `12.35` \| `...ted,Not isolated,Not i...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 288 | `11.55` | `...rature_comparison.csv` \| 8 \| `11.55` \| `... threshold,Distance th...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 289 | `2.67` | `...rature_comparison.csv` \| 9 \| `2.67` \| `...evaluated,22.08% (vs. ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 289 | `22.08` | `... \| 9 \| `2.67` \| `...evaluated,22.08% (vs. FAR_A = 2.67%)` \| 2.67% ...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 290 | `2.67` | `...evaluated,22.08% (vs. FAR_A = 2.67%)` \| 22.08% (0.220808, k=1 FAR...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 290 | `22.08` | `...rature_comparison.csv` \| 9 \| `22.08` \| `...d,Not evaluated,Not ev...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 291 | `1.47` | `...ature_comparison.csv` \| 10 \| `1.47` \| `...,None reported,None re...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 292 | `64%` | `...fitting...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 292 | `19.41` | `...ature_comparison.csv` \| 11 \| `19.41` \| `...,None reported,None re...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 293 | `8.49` | `...ature_comparison.csv` \| 12 \| `8.49` \| `... trade-off,~6.15%,~5.5...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 294 | `4.43` | `...ature_comparison.csv` \| 13 \| `4.43` \| `...ded,Not provided,Not p...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 295 | `62.8%` | `...ature_comparison.csv` \| 13 \| `62.8%` \| `...-mean stranger penetra...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 296 | `30.08` | `...ature_comparison.csv` \| 14 \| `30.08` \| `...Not quantified,Not qua...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 296 | `21.59` | `... quantified,30.08% (surge of +21.59 pp, peak 84....` \| 30.08% (0....` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 297 | `30.08` | `...4 \| `21.59` \| `... quantified,30.08% (surge of +21.59 pp, peak 84....` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 297 | `21.59` | `...ature_comparison.csv` \| 14 \| `21.59` \| `... quantified,30.08% (su...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 297 | `84.63` | `...08% (surge of +21.59 pp, peak 84.63%)` \| +21.59 pp (0.215929, epis...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 298 | `21.59` | `... `84.63` \| `...08% (surge of +21.59 pp, peak 84.63%)` \| 84.63% (0...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 298 | `84.63` | `...ature_comparison.csv` \| 14 \| `84.63` \| `...08% (surge of +21.59 p...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 299 | `3.54` | `...ature_comparison.csv` \| 15 \| `3.54` \| `...valuated,Not evaluated...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 299 | `0.9670` | `...luated,FRR -> 3.54%, AUROC -> 0.9670` \| 3.54% (0.035369, burst L=5...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 300 | `64%` | `...OC -> 0.9670` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 300 | `3.54` | `... `0.9670` \| `...luated,FRR -> 3.54%, AUROC -> 0.9670` \| 0.9670 (0...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 300 | `0.9670` | `...ature_comparison.csv` \| 15 \| `0.9670` \| `...luated,FRR -> 3.54%, A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 301 | `0.2097` | `...ature_comparison.csv` \| 17 \| `0.2097` \| `... reported,None reporte...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 301 | `0.1142` | `...ne reported,rho = 0.2097 (p = 0.1142, n=58)` \| 0.2097 (Spearman rh...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 302 | `0.2097` | `...1142` \| `...ne reported,rho = 0.2097 (p = 0.1142, n=58)` \| 0.1142 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 302 | `0.1142` | `...ature_comparison.csv` \| 17 \| `0.1142` \| `...ne reported,rho = 0.20...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 303 | `0.0327` | `...ature_comparison.csv` \| 18 \| `0.0327` \| `...d,Not evaluated,Not ev...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 303 | `0.0323` | `...ature_comparison.csv` \| 18 \| `0.0327` \| `...d,Not evaluated,Not e...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 304 | `0.0327` | `...ature_comparison.csv` \| 18 \| `0.0323` \| `...d,Not evaluated,Not e...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 304 | `0.0323` | `...ature_comparison.csv` \| 18 \| `0.0323` \| `...d,Not evaluated,Not ev...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 305 | `2.67` | `\| `paper/main.tex` \| 31 \| `2.67` \| `...sting reports $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 306 | `22.08` | `\| `paper/main.tex` \| 31 \| `22.08` \| `... penetrate at $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 307 | `64%` | `...ar test...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 307 | `19.41` | `\| `paper/main.tex` \| 31 \| `19.41` \| `...($k=1$) creates a dang...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 308 | `1.47` | `\| `paper/main.tex` \| 31 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 309 | `4.43` | `\| `paper/main.tex` \| 33 \| `4.43` \| `...enetration from $11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 309 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` \| 4.43%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 309 | `11.90` | `...`4.43` \| `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 310 | `30.08` | `\| `paper/main.tex` \| 33 \| `30.08` \| `...Rate surges from $8.49...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 310 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84...` \| 30.0...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 310 | `8.49` | `...0.08` \| `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 311 | `30.08` | `....59` \| `... from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 311 | `21.59` | `\| `paper/main.tex` \| 33 \| `21.59` \| `... from $8.49\%$ to $30....` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 311 | `8.49` | `...` \| 33 \| `21.59` \| `... from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 311 | `84.63` | `...08\%$ (+21.59 pp, peaking at $84.63\%$)---r...` \| +21.59 pp (0.21...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 312 | `4.43` | `...2.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 312 | `62.8%` | `\| `paper/main.tex` \| 33 \| `62.8%` \| `...rom $11.90\%$ to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 312 | `11.90` | `...ex` \| 33 \| `62.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 313 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 313 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90% (0.119046,...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 313 | `11.90` | `\| `paper/main.tex` \| 33 \| `11.90` \| `...ue-stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 314 | `30.08` | `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` \| 8.49% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 314 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` \| 8.49% (0.084860, ...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 314 | `8.49` | `\| `paper/main.tex` \| 33 \| `8.49` \| `...e Rejection Rate surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 315 | `98.5` | `\| `paper/main.tex` \| 33 \| `98.5` \| `...ly heterogeneous ($0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 315 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 316 | `3.54` | `\| `paper/main.tex` \| 33 \| `3.54` \| `...ate meter false reject...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 317 | `64%` | `...bility is...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 317 | `0.9670` | `\| `paper/main.tex` \| 33 \| `0.9670` \| `...rimination to $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 318 | `21.59` | `... \| 33 \| `84.63` \| `...08\%$ (+21.59 pp, peaking at $84.63\%$)---r...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 318 | `84.63` | `\| `paper/main.tex` \| 33 \| `84.63` \| `...08\%$ (+21.59 pp, peak...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 319 | `1.47` | `\| `paper/main.tex` \| 57 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 320 | `11.55` | `\| `paper/main.tex` \| 58 \| `11.55` \| `...%, 18.77\%]$; $\text{F...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 321 | `12.35` | `\| `paper/main.tex` \| 58 \| `12.35` \| `...transmitters ($\text{F...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 322 | `2.67` | `\| `paper/main.tex` \| 59 \| `2.67` \| `...optimism gap ($\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 322 | `22.08` | `...= 2.67\%$ vs. $\text{FAR}_B = 22.08\...` \| 2.67% (0.026744, k=1 F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 323 | `2.67` | `...n.tex` \| 59 \| `22.08` \| `...= 2.67\%$ vs. $\text{FAR}_B = 22.08\...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 323 | `22.08` | `\| `paper/main.tex` \| 59 \| `22.08` \| `...= 2.67\%$ vs. $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 324 | `64%` | `...t{FAR}_...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 324 | `19.41` | `\| `paper/main.tex` \| 59 \| `19.41` \| `...ion ($k=1$) incurs an ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 325 | `98.5` | `\| `paper/main.tex` \| 60 \| `98.5` \| `...ation varies from $0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 325 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 326 | `4.43` | `\| `paper/main.tex` \| 61 \| `4.43` \| `...enetration from $11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 326 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` \| 4.43%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 326 | `11.90` | `...`4.43` \| `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 327 | `30.08` | `\| `paper/main.tex` \| 61 \| `30.08` \| `...(FRR surges from $8.49...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 327 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).` \| 30.08% (0.3...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 327 | `8.49` | `...0.08` \| `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 328 | `30.08` | `...`21.59` \| `...om $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).`...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 328 | `21.59` | `\| `paper/main.tex` \| 61 \| `21.59` \| `...om $8.49\%$ to $30.08\...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 328 | `8.49` | `...tex` \| 61 \| `21.59` \| `...om $8.49\%$ to $30.08\%$, a $+21.59$~p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 329 | `4.43` | `...2.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 329 | `62.8%` | `\| `paper/main.tex` \| 61 \| `62.8%` \| `...rom $11.90\%$ to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 329 | `11.90` | `...ex` \| 61 \| `62.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 330 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 330 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90% (0.119046,...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 330 | `11.90` | `\| `paper/main.tex` \| 61 \| `11.90` \| `...ue-stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 331 | `30.08` | `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~p...` \| 8.49% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 331 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$~p...` \| 8.49% (0.084860, FRR...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 331 | `8.49` | `\| `paper/main.tex` \| 61 \| `8.49` \| `...ity penalty (FRR surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 332 | `0.0327` | `\| `paper/main.tex` \| 62 \| `0.0327` \| `...le to naive testing ($...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 332 | `0.0323` | `\| `paper/main.tex` \| 62 \| `0.0327` \| `...le to naive testing (...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 333 | `0.0327` | `\| `paper/main.tex` \| 62 \| `0.0323` \| `...le to naive testing (...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 333 | `0.0323` | `\| `paper/main.tex` \| 62 \| `0.0323` \| `...le to naive testing ($...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 334 | `1.47` | `\| `paper/main.tex` \| 81 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 335 | `64%` | `... establ...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 335 | `19.41` | `\| `paper/main.tex` \| 83 \| `19.41` \| `...on ($k=1$) induces an ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 336 | `30.18` | `\| `paper/main.tex` \| 84 \| `30.18` \| `...bust}}$), revealing a ...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 336 | `30.08` | `...se rejection rate in sm...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 337 | `99.43` | `\| `paper/main.tex` \| 119 \| `99.43` \| `...achieving $\text{macro...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 338 | `12.35` | `\| `paper/main.tex` \| 143 \| `12.35` \| `\item $\text{FAR}_A$ (Fam...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 339 | `11.55` | `\| `paper/main.tex` \| 144 \| `11.55` \| `\item $\text{FAR}_B$ (Tru...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 340 | `8.49` | `\| `paper/main.tex` \| 146 \| `8.49` \| `\item Mean False Rejectio...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 341 | `99.43` | `\| `paper/main.tex` \| 147 \| `99.43` \| `\item Closed-set macro-$F...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 341 | `0.9490` | `...: $99.43\%$, open-set AUROC: $0.9490$.` \| 99.43% (0.994270, macro-...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 342 | `99.43` | `...item Closed-set macro-$F_1$: $99.43\%$, open-set AUROC: $0.9490$....` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 342 | `0.9490` | `\| `paper/main.tex` \| 147 \| `0.9490` \| `\item Closed-set macro-$F...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 343 | `64%` | `\| `paper/main.tex` \| 161 \| `64%` \| `...re map & Contrastive l...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 343 | `62.8%` | `...type) & \textbf{292 bas...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 344 | `99.43` | `\| `paper/main.tex` \| 162 \| `99.43` \| `...$96.2\%$ & $94.7\%$ & ...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 345 | `0.9490` | `\| `paper/main.tex` \| 163 \| `0.9490` \| `... 92.5\%$ & $91.3\%$ & ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 346 | `64%` | `\| `paper/main.tex` \| 164 \| `12.35` \| `...ated & Not is...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 346 | `12.35` | `\| `paper/main.tex` \| 164 \| `12.35` \| `...ated & Not isolated & ...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 347 | `11.55` | `\| `paper/main.tex` \| 165 \| `11.55` \| `.... & Distance thres. & ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 348 | `2.67` | `\| `paper/main.tex` \| 166 \| `2.67` \| `...f{22.08\% (vs $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 348 | `22.08` | `...n.tex` \| 166 \| `2.67` \| `...f{22.08\% (vs $\text{FAR}_A = 2.67\%$...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 349 | `2.67` | `...f{22.08\% (vs $\text{FAR}_A = 2.67\%$...` \| 22.08% (0.220808, k=...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 349 | `22.08` | `\| `paper/main.tex` \| 166 \| `22.08` \| `...ted & Not evaluated & ...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 350 | `1.47` | `\| `paper/main.tex` \| 167 \| `1.47` \| `...ed & None reported & \...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 351 | `64%` | `...rtion)} \\` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 351 | `19.41` | `\| `paper/main.tex` \| 168 \| `19.41` \| `...ed & None reported & \...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 352 | `8.49` | `\| `paper/main.tex` \| 169 \| `8.49` \| `...$ & $\approx 7.2\%$ & ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 353 | `4.43` | `\| `paper/main.tex` \| 170 \| `4.43` \| `...ided & Not provided & ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 354 | `62.8%` | `\| `paper/main.tex` \| 170 \| `62.8%` \| `....43\% (reduces penetra...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 355 | `30.08` | `\| `paper/main.tex` \| 171 \| `30.08` \| `...ed & Not quantified & ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 355 | `21.59` | `... \textbf{30.08\% (FRR surge $+21.59$ pp)} \\` \| 30.08% (0.300789,...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 356 | `30.08` | `... 171 \| `21.59` \| `... \textbf{30.08\% (FRR surge $+21.59$ pp)} \\...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 356 | `21.59` | `\| `paper/main.tex` \| 171 \| `21.59` \| `... \textbf{30.08\% (FRR ...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 357 | `3.54` | `\| `paper/main.tex` \| 172 \| `3.54` \| `...ted & \textbf{$\text{F...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 357 | `0.9670` | `...to 3.54\%$, $\text{AUROC} \to 0.9670$...` \| 3.54% (0.035369, burst...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 358 | `64%` | `... 0.9670$} \\` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 358 | `3.54` | `...ex` \| 172 \| `0.9670` \| `...to 3.54\%$, $\text{AUROC} \to 0.9670$...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 358 | `0.9670` | `\| `paper/main.tex` \| 172 \| `0.9670` \| `...to 3.54\%$, $\text{AUR...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 359 | `0.2097` | `\| `paper/main.tex` \| 174 \| `0.2097` \| `...ne reported & \textbf{...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 359 | `0.1142` | `...\textbf{$\rho = 0.2097$ ($p = 0.1142, n=58$)} \\` \| 0.2097 (Spearm...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 360 | `0.2097` | `...0.1142` \| `...\textbf{$\rho = 0.2097$ ($p = 0.1142, n=58$)} \\` \| ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 360 | `0.1142` | `\| `paper/main.tex` \| 174 \| `0.1142` \| `...\textbf{$\rho = 0.2097...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 361 | `1.47` | `\| `paper/main.tex` \| 184 \| `1.47` \| `..._{\text{matched}}$: \t...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 362 | `2.67` | `\| `paper/main.tex` \| 199 \| `2.67` \| `...esting yields $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 363 | `22.08` | `\| `paper/main.tex` \| 199 \| `22.08` \| `...enetration is $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 364 | `64%` | `...+19.41\%$.` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 364 | `19.41` | `\| `paper/main.tex` \| 199 \| `19.41` \| `...m gap of $\Delta\text{...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 365 | `11.90` | `\| `paper/main.tex` \| 228 \| `11.90` \| `...ine ($L=1$):} $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 365 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` \| 11.90% (0.119046...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 366 | `0.9490` | `\| `paper/main.tex` \| 228 \| `0.9490` \| `...} = +0.56\%$, $\text{A...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 367 | `11.90` | `...x` \| 228 \| `8.49` \| `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 367 | `8.49` | `\| `paper/main.tex` \| 228 \| `8.49` \| `...}_B = 11.90\%$, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 368 | `64%` | `\| `paper/main.tex` \| 229 \| `64%` \| `... +1.27\%$, $\text{AURO...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 368 | `62.8%` | `..., $\text{AUROC} = 0.9642$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 368 | `0.9642` | `...... +1.27\%$, $\text{AUROC} = 0.9642$.` \| 62.8% (62.7746% relative...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 369 | `11.22` | `\| `paper/main.tex` \| 229 \| `11.22` \| `...ion ($L=3$):} $\text{F...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 369 | `4.37` | `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` \| 11.22% (0.112182...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 370 | `11.22` | `...x` \| 229 \| `4.37` \| `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 370 | `4.37` | `\| `paper/main.tex` \| 229 \| `4.37` \| `...}_B = 11.22\%$, $\text...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 371 | `64%` | `... `paper/main.tex` \| 229 \| `0.9642` \| `...} = +1.27\%$, $\text{...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 371 | `0.9642` | `\| `paper/main.tex` \| 229 \| `0.9642` \| `...} = +1.27\%$, $\text{A...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 372 | `64%` | `\| `paper/main.tex` \| 230 \| `64%` \| `...54\%$, $\Delta\text{FA...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 372 | `62.8%` | `..., $\text{AUROC} = 0.9670$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 372 | `0.9670` | `...} = +1.64\%$, $\text{AUROC} = 0.9670$.` \| 62.8% (62.7746% relative...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 373 | `64%` | `...54\%$, $\Delta\text{FAR} = +1.64...` \| 3.54% (0.035369, burst ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 373 | `3.54` | `\| `paper/main.tex` \| 230 \| `3.54` \| `...}_B = 10.45\%$, $\text...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 373 | `10.45` | `...x` \| 230 \| `3.54` \| `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 374 | `3.54` | `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` \| 10.45% (0.104538...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 374 | `10.45` | `\| `paper/main.tex` \| 230 \| `10.45` \| `...ion ($L=5$):} $\text{F...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 375 | `64%` | `...\| 230 \| `0.9670` \| `...} = +1.64\%$, $\text{AUROC} = 0.9670$.`...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 375 | `0.9670` | `\| `paper/main.tex` \| 230 \| `0.9670` \| `...} = +1.64\%$, $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 376 | `64%` | `\| `paper/main.tex` \| 232 \| `64%` \| `...omes clearer ($+0.56\%...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 376 | `62.8%` | `...r ($+0.56\% \to +1.64\%$).` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 377 | `8.49` | `\| `paper/main.tex` \| 232 \| `8.49` \| `...tion by more than half...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 377 | `3.54` | `... half (from $8.49\%$ down to $3.54\%$), elevati...` \| 8.49% (0.0...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 378 | `8.49` | `...2 \| `3.54` \| `... half (from $8.49\%$ down to $3.54\%$), elevati...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 378 | `3.54` | `\| `paper/main.tex` \| 232 \| `3.54` \| `... half (from $8.49\%$ d...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 379 | `98.5` | `\| `paper/main.tex` \| 235 \| `98.5` \| `...ation varies from $0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 379 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 380 | `4.43` | `\| `paper/main.tex` \| 239 \| `4.43` \| `...enetration from $11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 380 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).` \| 4.43% (0.04...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 380 | `11.90` | `...`4.43` \| `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 381 | `4.43` | `...2.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).` \|...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 381 | `62.8%` | `\| `paper/main.tex` \| 239 \| `62.8%` \| `...rom $11.90\%$ to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 381 | `11.90` | `...x` \| 239 \| `62.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 382 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 382 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90% (0.119046,...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 382 | `11.90` | `\| `paper/main.tex` \| 239 \| `11.90` \| `...ue stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 383 | `30.08` | `\| `paper/main.tex` \| 240 \| `30.08` \| `...$) to surge from $8.49...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 383 | `21.59` | `...\%$ to $30.08\%$ on average (+21.59 pp, pea...` \| 30.08% (0.30078...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 383 | `8.49` | `...0.08` \| `...$) to surge from $8.49\%$ to $30.08\%$ on average (+...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 384 | `30.08` | `...\| 240 \| `21.59` \| `...\%$ to $30.08\%$ on average (+21.59 pp, pea...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 384 | `21.59` | `\| `paper/main.tex` \| 240 \| `21.59` \| `...\%$ to $30.08\%$ on av...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 384 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$).` \| +21.59 pp (0.215929, ...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 385 | `30.08` | `...$) to surge from $8.49\%$ to $30.08\%$ on average (+...` \| 8.49% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 385 | `8.49` | `\| `paper/main.tex` \| 240 \| `8.49` \| `...($\text{FRR}$) to surg...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 386 | `21.59` | `...\| 240 \| `84.63` \| `...erage (+21.59 pp, peaking at $84.63\%$).` \|...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 386 | `84.63` | `\| `paper/main.tex` \| 240 \| `84.63` \| `...erage (+21.59 pp, peak...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 387 | `64%` | `...19.41\%$).` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 387 | `19.41` | `\| `paper/main.tex` \| 247 \| `19.41` \| `...e single-device distor...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 388 | `30.08` | `\| `paper/main.tex` \| 248 \| `30.08` \| `...g introduces an unacce...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 389 | `30.08` | `\| `paper/main.tex` \| 254 \| `30.08` \| `...e transmission to redu...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 390 | `30.08` | `\| `paper/main.tex` \| 260 \| `30.08` \| `...y cost of robust thres...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 391 | `64%` | `...librati...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 391 | `19.41` | `\| `paper/main.tex` \| 260 \| `19.41` \| `...2\%, +2.40\%]$), scali...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 392 | `1.47` | `\| `paper/main.tex` \| 260 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 393 | `64%` | `...elated_work_table.md` \| 26 \| `64%` \| `...re map \\| Contrastive ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 393 | `62.8%` | `...ype space) \\| **292 com...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 394 | `99.43` | `...elated_work_table.md` \| 27 \| `99.43` \| `... \\| 93.85% \\| 96.2% \\|...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 395 | `0.9490` | `...elated_work_table.md` \| 28 \| `0.9490` \| `... 90.23% \\| ≈ 92.5% \\| ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 395 | `0.9530` | `... 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` \| 0.9490 (0.9...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 396 | `0.9490` | `... `0.9530` \| `...\\| 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 396 | `0.9530` | `...elated_work_table.md` \| 28 \| `0.9530` \| `...\\| 91.3% \\| **0.9490 (...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 397 | `12.35` | `...elated_work_table.md` \| 29 \| `12.35` \| `...t isolated \\| Not isol...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 398 | `11.55` | `...elated_work_table.md` \| 30 \| `11.55` \| `...hold \\| Distance thres...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 399 | `2.67` | `...elated_work_table.md` \| 31 \| `2.67` \| `...ted \\| **22.08%** (vs....` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 399 | `22.08` | `... \| 31 \| `2.67` \| `...ted \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 2...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 400 | `2.67` | `...ed \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 22.08% (0.220808, k=1 ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 400 | `22.08` | `...elated_work_table.md` \| 31 \| `22.08` \| `...evaluated \\| Not evalu...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 401 | `1.47` | `...elated_work_table.md` \| 32 \| `1.47` \| `...reported \\| None repor...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 402 | `64%` | `...erfitti...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 402 | `19.41` | `...elated_work_table.md` \| 33 \| `19.41` \| `...reported \\| None repor...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 403 | `8.49` | `...elated_work_table.md` \| 34 \| `8.49` \| `...≈ 6.15% \\| ≈ 5.5% \\| ≈...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 404 | `4.43` | `...elated_work_table.md` \| 35 \| `4.43` \| `...t provided \\| Not prov...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 405 | `62.8%` | `...elated_work_table.md` \| 35 \| `62.8%` \| `...-mean stranger penetra...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 406 | `30.08` | `...elated_work_table.md` \| 36 \| `30.08` \| `...antified \\| Not quanti...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 406 | `21.59` | `...fied \\| **30.08%** (surge of +21.59 pp, peak 8...` \| 30.08% (0.30...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 407 | `30.08` | `...36 \| `21.59` \| `...ified \\| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 407 | `21.59` | `...elated_work_table.md` \| 36 \| `21.59` \| `...ified \\| **30.08%** (s...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 407 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \\|` \| +21.59 pp (0.215929, e...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 408 | `21.59` | `... `84.63` \| `...%** (surge of +21.59 pp, peak 84.63%) \\|` \| 84.63%...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 408 | `84.63` | `...elated_work_table.md` \| 36 \| `84.63` \| `...%** (surge of +21.59 p...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 409 | `3.54` | `...elated_work_table.md` \| 37 \| `3.54` \| `...ted \\| Not evaluated \...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 409 | `0.9670` | `...ted \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 3.54% (0.035369, burs...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 410 | `64%` | `... 0.9670** \\|` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 410 | `3.54` | `...0.9670` \| `...ated \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 0.967...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 410 | `0.9670` | `...elated_work_table.md` \| 37 \| `0.9670` \| `...ated \\| **FRR → 3.54%,...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 411 | `0.2097` | `...elated_work_table.md` \| 39 \| `0.2097` \| `...orted \\| None reported...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 411 | `0.1142` | `...reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0.2097 (Spearm...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 412 | `0.2097` | `...142` \| `... reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 412 | `0.1142` | `...elated_work_table.md` \| 39 \| `0.1142` \| `... reported \\| **ρ = 0.2...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 413 | `0.0327` | `...elated_work_table.md` \| 40 \| `0.0327` \| `...evaluated \\| Not evalu...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 413 | `0.0323` | `...elated_work_table.md` \| 40 \| `0.0327` \| `...evaluated \\| Not eval...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 414 | `0.0327` | `...elated_work_table.md` \| 40 \| `0.0323` \| `...evaluated \\| Not eval...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 414 | `0.0323` | `...elated_work_table.md` \| 40 \| `0.0323` \| `...evaluated \\| Not evalu...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 415 | `1.47` | `...tions/paper_draft.md` \| 18 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 416 | `11.55` | `...tions/paper_draft.md` \| 19 \| `11.55` \| `...%, 18.77\%]$; $\text{F...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 417 | `12.35` | `...tions/paper_draft.md` \| 19 \| `12.35` \| `...transmitters ($\text{F...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 418 | `2.67` | `...tions/paper_draft.md` \| 20 \| `2.67` \| `...optimism gap ($\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 418 | `22.08` | `...= 2.67\%$ vs. $\text{FAR}_B = 22.08\...` \| 2.67% (0.026744, k=1 F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 419 | `2.67` | `...ft.md` \| 20 \| `22.08` \| `...= 2.67\%$ vs. $\text{FAR}_B = 22.08\...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 419 | `22.08` | `...tions/paper_draft.md` \| 20 \| `22.08` \| `...= 2.67\%$ vs. $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 420 | `64%` | `...t{FAR}_...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 420 | `19.41` | `...tions/paper_draft.md` \| 20 \| `19.41` \| `...ion ($k=1$) incurs an ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 421 | `98.5` | `...tions/paper_draft.md` \| 21 \| `98.5` \| `...ation varies from $0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 421 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 422 | `4.43` | `...tions/paper_draft.md` \| 22 \| `4.43` \| `...enetration from $11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 422 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` \| 4.43%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 422 | `11.90` | `...`4.43` \| `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 423 | `30.08` | `...tions/paper_draft.md` \| 22 \| `30.08` \| `...(FRR surges from $8.49...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 423 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).` \| 30.08% (0.3...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 423 | `8.49` | `...0.08` \| `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 424 | `30.08` | `...`21.59` \| `...om $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).`...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 424 | `21.59` | `...tions/paper_draft.md` \| 22 \| `21.59` \| `...om $8.49\%$ to $30.08\...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 424 | `8.49` | `....md` \| 22 \| `21.59` \| `...om $8.49\%$ to $30.08\%$, a $+21.59$ p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 425 | `4.43` | `...2.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 425 | `62.8%` | `...tions/paper_draft.md` \| 22 \| `62.8%` \| `...rom $11.90\%$ to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 425 | `11.90` | `...md` \| 22 \| `62.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 426 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 426 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90% (0.119046,...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 426 | `11.90` | `...tions/paper_draft.md` \| 22 \| `11.90` \| `...ue-stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 427 | `30.08` | `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ p...` \| 8.49% ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 427 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$ p...` \| 8.49% (0.084860, FRR...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 427 | `8.49` | `...tions/paper_draft.md` \| 22 \| `8.49` \| `...ity penalty (FRR surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 428 | `0.0327` | `...tions/paper_draft.md` \| 23 \| `0.0327` \| `...le to naive testing ($...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 428 | `0.0323` | `...tions/paper_draft.md` \| 23 \| `0.0327` \| `...le to naive testing (...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 429 | `0.0327` | `...tions/paper_draft.md` \| 23 \| `0.0323` \| `...le to naive testing (...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 429 | `0.0323` | `...tions/paper_draft.md` \| 23 \| `0.0323` \| `...le to naive testing ($...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 430 | `64%` | `...tions/paper_draft.md` \| 39 \| `64%` \| `...re map \\| Contrastive ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 430 | `62.8%` | `...ype space) \\| **292 com...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 431 | `99.43` | `...tions/paper_draft.md` \| 40 \| `99.43` \| `... \\| 93.85% \\| 96.2% \\|...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 432 | `0.9490` | `...tions/paper_draft.md` \| 41 \| `0.9490` \| `... 90.23% \\| ≈ 92.5% \\| ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 432 | `0.9530` | `... 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` \| 0.9490 (0.9...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 433 | `0.9490` | `... `0.9530` \| `...\\| 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 433 | `0.9530` | `...tions/paper_draft.md` \| 41 \| `0.9530` \| `...\\| 91.3% \\| **0.9490 (...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 434 | `12.35` | `...tions/paper_draft.md` \| 42 \| `12.35` \| `...t isolated \\| Not isol...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 435 | `11.55` | `...tions/paper_draft.md` \| 43 \| `11.55` \| `...hold \\| Distance thres...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 436 | `2.67` | `...tions/paper_draft.md` \| 44 \| `2.67` \| `...ted \\| **22.08%** (vs....` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 436 | `22.08` | `... \| 44 \| `2.67` \| `...ted \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 2...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 437 | `2.67` | `...ed \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 22.08% (0.220808, k=1 ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 437 | `22.08` | `...tions/paper_draft.md` \| 44 \| `22.08` \| `...evaluated \\| Not evalu...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 438 | `1.47` | `...tions/paper_draft.md` \| 45 \| `1.47` \| `...reported \\| None repor...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 439 | `64%` | `...erfitti...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 439 | `19.41` | `...tions/paper_draft.md` \| 46 \| `19.41` \| `...reported \\| None repor...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 440 | `8.49` | `...tions/paper_draft.md` \| 47 \| `8.49` \| `...≈ 6.15% \\| ≈ 5.5% \\| ≈...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 441 | `4.43` | `...tions/paper_draft.md` \| 48 \| `4.43` \| `...t provided \\| Not prov...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 442 | `62.8%` | `...tions/paper_draft.md` \| 48 \| `62.8%` \| `...-mean stranger penetra...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 443 | `30.08` | `...tions/paper_draft.md` \| 49 \| `30.08` \| `...antified \\| Not quanti...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 443 | `21.59` | `...fied \\| **30.08%** (surge of +21.59 pp, peak 8...` \| 30.08% (0.30...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 444 | `30.08` | `...49 \| `21.59` \| `...ified \\| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 444 | `21.59` | `...tions/paper_draft.md` \| 49 \| `21.59` \| `...ified \\| **30.08%** (s...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 444 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \\|` \| +21.59 pp (0.215929, e...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 445 | `21.59` | `... `84.63` \| `...%** (surge of +21.59 pp, peak 84.63%) \\|` \| 84.63%...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 445 | `84.63` | `...tions/paper_draft.md` \| 49 \| `84.63` \| `...%** (surge of +21.59 p...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 446 | `3.54` | `...tions/paper_draft.md` \| 50 \| `3.54` \| `...ted \\| Not evaluated \...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 446 | `0.9670` | `...ted \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 3.54% (0.035369, burs...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 447 | `64%` | `... 0.9670** \\|` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 447 | `3.54` | `...0.9670` \| `...ated \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 0.967...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 447 | `0.9670` | `...tions/paper_draft.md` \| 50 \| `0.9670` \| `...ated \\| **FRR → 3.54%,...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 448 | `0.2097` | `...tions/paper_draft.md` \| 52 \| `0.2097` \| `...orted \\| None reported...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 448 | `0.1142` | `...reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0.2097 (Spearm...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 449 | `0.2097` | `...142` \| `... reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 449 | `0.1142` | `...tions/paper_draft.md` \| 52 \| `0.1142` \| `... reported \\| **ρ = 0.2...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 450 | `0.0327` | `...tions/paper_draft.md` \| 53 \| `0.0327` \| `...evaluated \\| Not evalu...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 450 | `0.0323` | `...tions/paper_draft.md` \| 53 \| `0.0327` \| `...evaluated \\| Not eval...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 451 | `0.0327` | `...tions/paper_draft.md` \| 53 \| `0.0323` \| `...evaluated \\| Not eval...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 451 | `0.0323` | `...tions/paper_draft.md` \| 53 \| `0.0323` \| `...evaluated \\| Not evalu...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 452 | `1.47` | `...tions/paper_draft.md` \| 59 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 453 | `64%` | `... establ...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 453 | `19.41` | `...tions/paper_draft.md` \| 61 \| `19.41` \| `...on ($k=1$) induces an ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 454 | `30.08` | `...tions/paper_draft.md` \| 62 \| `30.08` \| `...bust}}$), revealing a ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 455 | `99.43` | `...tions/paper_draft.md` \| 93 \| `99.43` \| `...achieving $\text{macro...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 456 | `12.35` | `...ions/paper_draft.md` \| 112 \| `12.35` \| `...angers)** \\| Device ($...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 457 | `11.55` | `...ions/paper_draft.md` \| 113 \| `11.55` \| `...angers)** \\| Device ($...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 458 | `8.49` | `...ions/paper_draft.md` \| 115 \| `8.49` \| `... (FRR)** \\| Episode ($...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 459 | `0.9530` | `...ions/paper_draft.md` \| 116 \| `0.9530` \| `...ion A)** \\| Episode ($...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 460 | `0.9490` | `...ions/paper_draft.md` \| 117 \| `0.9490` \| `...ion B)** \\| Episode ($...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 461 | `98.5` | `...ions/paper_draft.md` \| 120 \| `98.5` \| `...ne hardness (from $0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 461 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 462 | `1.47` | `...ions/paper_draft.md` \| 126 \| `1.47` \| `...AR}_{\text{matched}}$)...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 463 | `2.67` | `...ions/paper_draft.md` \| 133 \| `2.67` \| `...testing shows $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 464 | `22.08` | `...ions/paper_draft.md` \| 133 \| `22.08` \| `... penetrate at $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 465 | `64%` | `...9.41\%$**.` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 465 | `19.41` | `...ions/paper_draft.md` \| 133 \| `19.41` \| `...gap of **$\Delta\text{...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 466 | `64%` | `...ions/paper_draft.md` \| 138 \| `64%` \| `...:** Devices 48 (65.69\...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 466 | `62.8%` | `... 46 (63.18\%), 49 (47.1...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 467 | `0.2097` | `...ions/paper_draft.md` \| 140 \| `0.2097` \| `...nrolled neighbours is ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 467 | `0.1142` | `...ours is $\rho = 0.2097$ ($p = 0.1142, n=58$ unique p...` \| 0.2097 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 468 | `0.2097` | `...0.1142` \| `...ours is $\rho = 0.2097$ ($p = 0.1142, n=58$ unique p...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 468 | `0.1142` | `...ions/paper_draft.md` \| 140 \| `0.1142` \| `...ours is $\rho = 0.2097...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 469 | `4.43` | `...ions/paper_draft.md` \| 144 \| `4.43` \| `...ation from $11.90\%$ d...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 469 | `62.8%` | `...11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, wit...` \| 4.43%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 469 | `11.90` | `...44 \| `4.43` \| `...ation from $11.90\%$ down to $4.43\%$ (a $62.8\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 470 | `4.43` | `...2.8%` \| `...11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, wit...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 470 | `62.8%` | `...ions/paper_draft.md` \| 144 \| `62.8%` \| `...11.90\%$ down to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 470 | `11.90` | `...aft.md` \| 144 \| `62.8%` \| `...11.90\%$ down to $4.43\%$ (a $62.8\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 471 | `4.43` | `...ation from $11.90\%$ down to $4.43\%$ (a $62.8\...` \| 11.90% (0....` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 471 | `62.8%` | `...11.90\%$ down to $4.43\%$ (a $62.8\...` \| 11.90% (0.119046, epis...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 471 | `11.90` | `...ions/paper_draft.md` \| 144 \| `11.90` \| `...ue-stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 472 | `30.08` | `...ions/paper_draft.md` \| 145 \| `30.08` \| `...te surges from $8.49\%...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 472 | `21.59` | `...to **$30.08\%$** on average (+21.59 pp, p...` \| 30.08% (0.300789,...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 472 | `8.49` | `...`30.08` \| `...te surges from $8.49\%$ to **$30.08\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 473 | `30.08` | `...` \| 145 \| `21.59` \| `...to **$30.08\%$** on average (+21.59 pp, p...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 473 | `21.59` | `...ions/paper_draft.md` \| 145 \| `21.59` \| `...to **$30.08\%$** on av...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 473 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$). De...` \| +21.59 pp (0.21...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 474 | `30.08` | `...te surges from $8.49\%$ to **$30.08\%$** on averag...` \| 8.49% (0...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 474 | `8.49` | `...ions/paper_draft.md` \| 145 \| `8.49` \| `...e Rejection Rate surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 475 | `21.59` | `...\| 145 \| `84.63` \| `...erage (+21.59 pp, peaking at $84.63\%$). De...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 475 | `84.63` | `...ions/paper_draft.md` \| 145 \| `84.63` \| `...erage (+21.59 pp, peak...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 476 | `0.0327` | `...ions/paper_draft.md` \| 148 \| `0.0327` \| `...absolute estimation er...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 476 | `0.0323` | `...ions/paper_draft.md` \| 148 \| `0.0327` \| `...absolute estimation e...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 477 | `0.0327` | `...ions/paper_draft.md` \| 148 \| `0.0323` \| `...absolute estimation e...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 477 | `0.0323` | `...ions/paper_draft.md` \| 148 \| `0.0323` \| `...absolute estimation er...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 478 | `11.90` | `...ions/paper_draft.md` \| 152 \| `11.90` \| `...ne ($L=1$):** $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 478 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` \| 11.90% (0.119046...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 479 | `0.9490` | `...ions/paper_draft.md` \| 152 \| `0.9490` \| `...} = +0.56\%$, $\text{A...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 480 | `11.90` | `...d` \| 152 \| `8.49` \| `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 480 | `8.49` | `...ions/paper_draft.md` \| 152 \| `8.49` \| `...}_B = 11.90\%$, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 481 | `64%` | `...ions/paper_draft.md` \| 153 \| `64%` \| `... +1.27\%$, $\text{AURO...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 481 | `62.8%` | `..., $\text{AUROC} = 0.9642$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 481 | `0.9642` | `...... +1.27\%$, $\text{AUROC} = 0.9642$.` \| 62.8% (62.7746% relative...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 482 | `11.22` | `...ions/paper_draft.md` \| 153 \| `11.22` \| `...on ($L=3$):** $\text{F...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 482 | `4.37` | `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` \| 11.22% (0.112182...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 483 | `11.22` | `...d` \| 153 \| `4.37` \| `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 483 | `4.37` | `...ions/paper_draft.md` \| 153 \| `4.37` \| `...}_B = 11.22\%$, $\text...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 484 | `64%` | `...s/paper_draft.md` \| 153 \| `0.9642` \| `...} = +1.27\%$, $\text{...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 484 | `0.9642` | `...ions/paper_draft.md` \| 153 \| `0.9642` \| `...} = +1.27\%$, $\text{A...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 485 | `64%` | `...ions/paper_draft.md` \| 154 \| `64%` \| `...54\%$, $\Delta\text{FA...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 485 | `62.8%` | `..., $\text{AUROC} = 0.9670$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 485 | `0.9670` | `...} = +1.64\%$, $\text{AUROC} = 0.9670$.` \| 62.8% (62.7746% relative...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 486 | `64%` | `...54\%$, $\Delta\text{FAR} = +1.64...` \| 3.54% (0.035369, burst ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 486 | `3.54` | `...ions/paper_draft.md` \| 154 \| `3.54` \| `...}_B = 10.45\%$, $\text...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 486 | `10.45` | `...d` \| 154 \| `3.54` \| `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 487 | `3.54` | `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` \| 10.45% (0.104538...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 487 | `10.45` | `...ions/paper_draft.md` \| 154 \| `10.45` \| `...on ($L=5$):** $\text{F...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 488 | `64%` | `...\| 154 \| `0.9670` \| `...} = +1.64\%$, $\text{AUROC} = 0.9670$.`...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 488 | `0.9670` | `...ions/paper_draft.md` \| 154 \| `0.9670` \| `...} = +1.64\%$, $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 489 | `64%` | `...ions/paper_draft.md` \| 156 \| `64%` \| `...omes clearer ($+0.56\%...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 489 | `62.8%` | `...r ($+0.56\% \to +1.64\%$).` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 490 | `8.49` | `...ions/paper_draft.md` \| 156 \| `8.49` \| `...tion by more than half...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 490 | `3.54` | `... half (from $8.49\%$ down to $3.54\%$), elevati...` \| 8.49% (0.0...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 491 | `8.49` | `...6 \| `3.54` \| `... half (from $8.49\%$ down to $3.54\%$), elevati...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 491 | `3.54` | `...ions/paper_draft.md` \| 156 \| `3.54` \| `... half (from $8.49\%$ d...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 492 | `64%` | `...19.41\%$).` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 492 | `19.41` | `...ions/paper_draft.md` \| 165 \| `19.41` \| `...catastrophic optimism ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 493 | `0.9490` | `...ions/paper_draft.md` \| 166 \| `0.9490` \| `... With open-set AUROC $...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 494 | `30.08` | `...ions/paper_draft.md` \| 180 \| `30.08` \| `...ed receivers to suppre...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 495 | `30.08` | `...ions/paper_draft.md` \| 188 \| `30.08` \| `...y cost of robust thres...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 496 | `64%` | `...proxy d...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 496 | `19.41` | `...ions/paper_draft.md` \| 188 \| `19.41` \| `...2\%, +2.40\%]$), scali...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 497 | `1.47` | `...ions/paper_draft.md` \| 188 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 498 | `11.90` | `...burst_aggregation.tex` \| 9 \| `11.90` \| `1 (Single packet) & 11.34...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 498 | `11.34` | `...11.90` \| `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 498 | `0.9490` | `... 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` \| 11.90% (0.119046, episo...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 498 | `8.49` | `...packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` \| 11...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 499 | `11.90` | `...1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 499 | `11.34` | `...burst_aggregation.tex` \| 9 \| `11.34` \| `1 (Single packet) & 11.34...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 499 | `0.9490` | `... 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` \| 11.34% (0.113422, episo...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 499 | `8.49` | `...packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` \| 11...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 500 | `11.90` | `...1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 500 | `11.34` | `....9490` \| `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 500 | `0.9490` | `...burst_aggregation.tex` \| 9 \| `0.9490` \| `1 (Single packet) & 11.34...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 500 | `8.49` | `...packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` \| 0....` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 501 | `11.90` | `...1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 501 | `11.34` | `...`8.49` \| `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 501 | `0.9490` | `... 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` \| 8.49% (0.084860, FRR ep...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 501 | `8.49` | `...burst_aggregation.tex` \| 9 \| `8.49` \| `1 (Single packet) & 11.34...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 502 | `64%` | `...urst_aggregation.tex` \| 10 \| `64%` \| `3 (3-packet burst) & 9.95...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 502 | `62.8%` | `...37\% & +1.27\% & 0.9642 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 502 | `11.22` | `...3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 502 | `4.37` | `...t burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 62...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 502 | `0.9642` | `... 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 62.8% (62.7746% relativ...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 503 | `64%` | `....22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 11.22% (0.112182, burs...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 503 | `11.22` | `...urst_aggregation.tex` \| 10 \| `11.22` \| `3 (3-packet burst) & 9.95...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 503 | `4.37` | `...t burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 11...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 503 | `0.9642` | `... 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 11.22% (0.112182, burst...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 504 | `64%` | `....22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 4.37% (0.043740, burst...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 504 | `11.22` | `...3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 504 | `4.37` | `...urst_aggregation.tex` \| 10 \| `4.37` \| `3 (3-packet burst) & 9.95...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 504 | `0.9642` | `... 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 4.37% (0.043740, burst ...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 505 | `64%` | `...t_aggregation.tex` \| 10 \| `0.9642` \| `3 (3-packet burst) & 9.9...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 505 | `11.22` | `...3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 505 | `4.37` | `...t burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` \| 0....` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 505 | `0.9642` | `...urst_aggregation.tex` \| 10 \| `0.9642` \| `3 (3-packet burst) & 9.95...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 506 | `64%` | `...urst_aggregation.tex` \| 11 \| `64%` \| `5 (5-packet burst) & 8.81...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 506 | `62.8%` | `...54\% & +1.64\% & 0.9670 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 506 | `3.54` | `...t burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 62...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 506 | `10.45` | `...5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 506 | `0.9670` | `... 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 62.8% (62.7746% relativ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 507 | `64%` | `....81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 3.54% (0.035...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 507 | `3.54` | `...urst_aggregation.tex` \| 11 \| `3.54` \| `5 (5-packet burst) & 8.81...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 507 | `10.45` | `...5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 507 | `0.9670` | `... 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 3.54% (0.035369, burst ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 508 | `64%` | `....81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 10.45% (0.10...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 508 | `3.54` | `...t burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 10...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 508 | `10.45` | `...urst_aggregation.tex` \| 11 \| `10.45` \| `5 (5-packet burst) & 8.81...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 508 | `0.9670` | `... 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 10.45% (0.104538, burst...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 509 | `64%` | `....81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 0.9670 (0.96...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 509 | `3.54` | `...t burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` \| 0....` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 509 | `10.45` | `...5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 509 | `0.9670` | `...urst_aggregation.tex` \| 11 \| `0.9670` \| `5 (5-packet burst) & 8.81...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 510 | `64%` | `...b_episode_summary.tex` \| 8 \| `64%` \| `0 & 0.741800 & 0.061900 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 510 | `62.8%` | `...0 & 0.975500 & 0.997700 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 511 | `64%` | `...b_episode_summary.tex` \| 9 \| `64%` \| `1 & 0.708200 & 0.164100 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 511 | `62.8%` | `...0 & 0.955700 & 0.992200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 512 | `0.1142` | `..._episode_summary.tex` \| 13 \| `0.1142` \| `5 & 0.688100 & 0.114100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 513 | `64%` | `..._episode_summary.tex` \| 16 \| `64%` \| `8 & 0.648500 & 0.186200 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 513 | `62.8%` | `...0 & 0.931200 & 0.992900 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 514 | `64%` | `..._episode_summary.tex` \| 24 \| `64%` \| `16 & 0.651700 & 0.051200 ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 514 | `62.8%` | `...0 & 0.976000 & 0.996100 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 515 | `0.1142` | `..._episode_summary.tex` \| 25 \| `0.1142` \| `17 & 0.698000 & 0.114700 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 516 | `64%` | `...les/tab_lopo_bias.tex` \| 8 \| `64%` \| `0 & resubstitution & 0.06...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 516 | `62.8%` | `... & -0.001200 & 0.001200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 517 | `64%` | `...les/tab_lopo_bias.tex` \| 9 \| `64%` \| `0 & naive_packet_disjoint...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 517 | `62.8%` | `... & -0.003000 & 0.003000 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 518 | `64%` | `...es/tab_lopo_bias.tex` \| 12 \| `64%` \| `1 & naive_packet_disjoint...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 518 | `62.8%` | `...0 & 0.045000 & 0.045000 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 519 | `0.1142` | `...es/tab_lopo_bias.tex` \| 24 \| `0.1142` \| `5 & naive_packet_disjoint...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 520 | `0.1142` | `...es/tab_lopo_bias.tex` \| 60 \| `0.1142` \| `17 & naive_packet_disjoin...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 521 | `0.2097` | `...eighbour_analysis.tex` \| 8 \| `0.2097` \| `0 & 2 & 21 & 2.894300 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 521 | `0.1142` | `...94300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 522 | `0.2097` | `... & 21 & 2.894300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 522 | `0.1142` | `...eighbour_analysis.tex` \| 8 \| `0.1142` \| `0 & 2 & 21 & 2.894300 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 523 | `0.2097` | `...eighbour_analysis.tex` \| 9 \| `0.2097` \| `0 & 7 & 27 & 3.852200 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 523 | `0.1142` | `...52200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 524 | `0.2097` | `... & 27 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 524 | `0.1142` | `...eighbour_analysis.tex` \| 9 \| `0.1142` \| `0 & 7 & 27 & 3.852200 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 525 | `0.2097` | `...ighbour_analysis.tex` \| 10 \| `0.2097` \| `0 & 11 & 19 & 2.615600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 525 | `0.1142` | `...15600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 526 | `0.2097` | `... & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 526 | `0.1142` | `...ighbour_analysis.tex` \| 10 \| `0.1142` \| `0 & 11 & 19 & 2.615600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 527 | `0.2097` | `...ighbour_analysis.tex` \| 11 \| `0.2097` \| `0 & 13 & 17 & 4.399800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 527 | `0.1142` | `...99800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 528 | `0.2097` | `... & 17 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 528 | `0.1142` | `...ighbour_analysis.tex` \| 11 \| `0.1142` \| `0 & 13 & 17 & 4.399800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 529 | `0.2097` | `...ighbour_analysis.tex` \| 12 \| `0.2097` \| `0 & 23 & 9 & 3.107600 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 529 | `0.1142` | `...07600 & 0.434000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 530 | `0.2097` | `...3 & 9 & 3.107600 & 0.434000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 530 | `0.1142` | `...ighbour_analysis.tex` \| 12 \| `0.1142` \| `0 & 23 & 9 & 3.107600 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 531 | `0.2097` | `...ighbour_analysis.tex` \| 13 \| `0.2097` \| `0 & 26 & 27 & 2.754600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 531 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 532 | `0.2097` | `... & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 532 | `0.1142` | `...ighbour_analysis.tex` \| 13 \| `0.1142` \| `0 & 26 & 27 & 2.754600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 533 | `0.2097` | `...ighbour_analysis.tex` \| 14 \| `0.2097` \| `0 & 29 & 27 & 3.817400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 533 | `0.1142` | `...17400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 534 | `0.2097` | `... & 27 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 534 | `0.1142` | `...ighbour_analysis.tex` \| 14 \| `0.1142` \| `0 & 29 & 27 & 3.817400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 535 | `0.2097` | `...ighbour_analysis.tex` \| 15 \| `0.2097` \| `0 & 32 & 24 & 4.244100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 535 | `0.1142` | `...44100 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 536 | `0.2097` | `... & 24 & 4.244100 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 536 | `0.1142` | `...ighbour_analysis.tex` \| 15 \| `0.1142` \| `0 & 32 & 24 & 4.244100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 537 | `0.2097` | `...ighbour_analysis.tex` \| 16 \| `0.2097` \| `0 & 34 & 39 & 4.393700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 537 | `0.1142` | `...93700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 538 | `0.2097` | `... & 39 & 4.393700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 538 | `0.1142` | `...ighbour_analysis.tex` \| 16 \| `0.1142` \| `0 & 34 & 39 & 4.393700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 539 | `0.2097` | `...ighbour_analysis.tex` \| 17 \| `0.2097` \| `0 & 36 & 4 & 2.899800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 539 | `0.1142` | `...99800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 540 | `0.2097` | `...6 & 4 & 2.899800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 540 | `0.1142` | `...ighbour_analysis.tex` \| 17 \| `0.1142` \| `0 & 36 & 4 & 2.899800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 541 | `0.2097` | `...ighbour_analysis.tex` \| 18 \| `0.2097` \| `0 & 41 & 21 & 4.791500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 541 | `0.1142` | `...91500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 542 | `0.2097` | `... & 21 & 4.791500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 542 | `0.1142` | `...ighbour_analysis.tex` \| 18 \| `0.1142` \| `0 & 41 & 21 & 4.791500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 543 | `0.2097` | `...ighbour_analysis.tex` \| 19 \| `0.2097` \| `0 & 48 & 46 & 6.468700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 543 | `0.1142` | `...68700 & 0.020000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 544 | `0.2097` | `... & 46 & 6.468700 & 0.020000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 544 | `0.1142` | `...ighbour_analysis.tex` \| 19 \| `0.1142` \| `0 & 48 & 46 & 6.468700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 545 | `0.2097` | `...ighbour_analysis.tex` \| 20 \| `0.2097` \| `0 & 51 & 53 & 2.109800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 545 | `0.1142` | `...09800 & 0.087500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 546 | `0.2097` | `... & 53 & 2.109800 & 0.087500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 546 | `0.1142` | `...ighbour_analysis.tex` \| 20 \| `0.1142` \| `0 & 51 & 53 & 2.109800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 547 | `0.2097` | `...ighbour_analysis.tex` \| 21 \| `0.2097` \| `0 & 56 & 54 & 4.740200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 547 | `0.1142` | `...40200 & 0.182500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 548 | `0.2097` | `... & 54 & 4.740200 & 0.182500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 548 | `0.1142` | `...ighbour_analysis.tex` \| 21 \| `0.1142` \| `0 & 56 & 54 & 4.740200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 549 | `0.2097` | `...ighbour_analysis.tex` \| 22 \| `0.2097` \| `0 & 60 & 53 & 4.375400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 549 | `0.1142` | `...75400 & 0.217500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 549 | `4.37` | `...2 \| `0.2097` \| `0 & 60 & 53 & 4.375400 & 0.217500 & 0.209700 & 0...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 550 | `0.2097` | `... & 53 & 4.375400 & 0.217500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 550 | `0.1142` | `...ighbour_analysis.tex` \| 22 \| `0.1142` \| `0 & 60 & 53 & 4.375400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 550 | `4.37` | `...2 \| `0.1142` \| `0 & 60 & 53 & 4.375400 & 0.217500 & 0.209700 & 0...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 551 | `0.2097` | `... & 53 & 4.375400 & 0.217500 & 0.209700 & 0.114200 \\` \| 4.37% (0.0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 551 | `0.1142` | `...75400 & 0.217500 & 0.209700 & 0.114200 \\` \| 4.37% (0.043740, burs...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 551 | `4.37` | `...ighbour_analysis.tex` \| 22 \| `4.37` \| `0 & 60 & 53 & 4.375400 & ...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 552 | `0.2097` | `...ighbour_analysis.tex` \| 23 \| `0.2097` \| `1 & 16 & 13 & 2.775000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 552 | `0.1142` | `...75000 & 0.028000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 553 | `0.2097` | `... & 13 & 2.775000 & 0.028000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 553 | `0.1142` | `...ighbour_analysis.tex` \| 23 \| `0.1142` \| `1 & 16 & 13 & 2.775000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 554 | `0.2097` | `...ighbour_analysis.tex` \| 24 \| `0.2097` \| `1 & 19 & 15 & 2.702400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 554 | `0.1142` | `...02400 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 555 | `0.2097` | `... & 15 & 2.702400 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 555 | `0.1142` | `...ighbour_analysis.tex` \| 24 \| `0.1142` \| `1 & 19 & 15 & 2.702400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 556 | `0.2097` | `...ighbour_analysis.tex` \| 25 \| `0.2097` \| `1 & 24 & 32 & 4.244100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 556 | `0.1142` | `...44100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 557 | `0.2097` | `... & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 557 | `0.1142` | `...ighbour_analysis.tex` \| 25 \| `0.1142` \| `1 & 24 & 32 & 4.244100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 558 | `0.2097` | `...ighbour_analysis.tex` \| 26 \| `0.2097` \| `1 & 25 & 20 & 3.996300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 558 | `0.1142` | `...96300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 559 | `0.2097` | `... & 20 & 3.996300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 559 | `0.1142` | `...ighbour_analysis.tex` \| 26 \| `0.1142` \| `1 & 25 & 20 & 3.996300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 560 | `0.2097` | `...ighbour_analysis.tex` \| 27 \| `0.2097` \| `1 & 27 & 26 & 2.754600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 560 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 561 | `0.2097` | `... & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 561 | `0.1142` | `...ighbour_analysis.tex` \| 27 \| `0.1142` \| `1 & 27 & 26 & 2.754600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 562 | `0.2097` | `...ighbour_analysis.tex` \| 28 \| `0.2097` \| `1 & 29 & 26 & 4.544300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 562 | `0.1142` | `...44300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 563 | `0.2097` | `... & 26 & 4.544300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 563 | `0.1142` | `...ighbour_analysis.tex` \| 28 \| `0.1142` \| `1 & 29 & 26 & 4.544300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 564 | `0.2097` | `...ighbour_analysis.tex` \| 29 \| `0.2097` \| `1 & 30 & 17 & 3.523900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 564 | `0.1142` | `...23900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 565 | `0.2097` | `... & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 565 | `0.1142` | `...ighbour_analysis.tex` \| 29 \| `0.1142` \| `1 & 30 & 17 & 3.523900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 566 | `0.2097` | `...ighbour_analysis.tex` \| 30 \| `0.2097` \| `1 & 34 & 40 & 3.452600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 566 | `0.1142` | `...52600 & 0.027500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 567 | `0.2097` | `... & 40 & 3.452600 & 0.027500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 567 | `0.1142` | `...ighbour_analysis.tex` \| 30 \| `0.1142` \| `1 & 34 & 40 & 3.452600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 568 | `0.2097` | `...ighbour_analysis.tex` \| 31 \| `0.2097` \| `1 & 36 & 4 & 2.899800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 568 | `0.1142` | `...99800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 569 | `0.2097` | `...6 & 4 & 2.899800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 569 | `0.1142` | `...ighbour_analysis.tex` \| 31 \| `0.1142` \| `1 & 36 & 4 & 2.899800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 570 | `0.2097` | `...ighbour_analysis.tex` \| 32 \| `0.2097` \| `1 & 39 & 10 & 3.431400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 570 | `0.1142` | `...31400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 571 | `0.2097` | `... & 10 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 571 | `0.1142` | `...ighbour_analysis.tex` \| 32 \| `0.1142` \| `1 & 39 & 10 & 3.431400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 572 | `0.2097` | `...ighbour_analysis.tex` \| 33 \| `0.2097` \| `1 & 44 & 8 & 2.039900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 572 | `0.1142` | `...39900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 573 | `0.2097` | `...4 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 573 | `0.1142` | `...ighbour_analysis.tex` \| 33 \| `0.1142` \| `1 & 44 & 8 & 2.039900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 574 | `0.2097` | `...ighbour_analysis.tex` \| 34 \| `0.2097` \| `1 & 48 & 46 & 6.468700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 574 | `0.1142` | `...68700 & 0.830000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 575 | `0.2097` | `... & 46 & 6.468700 & 0.830000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 575 | `0.1142` | `...ighbour_analysis.tex` \| 34 \| `0.1142` \| `1 & 48 & 46 & 6.468700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 576 | `0.2097` | `...ighbour_analysis.tex` \| 35 \| `0.2097` \| `1 & 52 & 53 & 5.019300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 576 | `0.1142` | `...19300 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 577 | `0.2097` | `... & 53 & 5.019300 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 577 | `0.1142` | `...ighbour_analysis.tex` \| 35 \| `0.1142` \| `1 & 52 & 53 & 5.019300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 578 | `0.2097` | `...ighbour_analysis.tex` \| 36 \| `0.2097` \| `1 & 54 & 56 & 4.740200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 578 | `0.1142` | `...40200 & 0.717500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 579 | `0.2097` | `... & 56 & 4.740200 & 0.717500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 579 | `0.1142` | `...ighbour_analysis.tex` \| 36 \| `0.1142` \| `1 & 54 & 56 & 4.740200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 580 | `0.2097` | `...ighbour_analysis.tex` \| 37 \| `0.2097` \| `1 & 57 & 56 & 4.186200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 580 | `0.1142` | `...86200 & 0.307500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 581 | `0.2097` | `... & 56 & 4.186200 & 0.307500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 581 | `0.1142` | `...ighbour_analysis.tex` \| 37 \| `0.1142` \| `1 & 57 & 56 & 4.186200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 582 | `0.2097` | `...ighbour_analysis.tex` \| 38 \| `0.2097` \| `2 & 3 & 36 & 3.770200 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 582 | `0.1142` | `...70200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 583 | `0.2097` | `... & 36 & 3.770200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 583 | `0.1142` | `...ighbour_analysis.tex` \| 38 \| `0.1142` \| `2 & 3 & 36 & 3.770200 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 584 | `0.2097` | `...ighbour_analysis.tex` \| 39 \| `0.2097` \| `2 & 13 & 16 & 2.775000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 584 | `0.1142` | `...75000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 585 | `0.2097` | `... & 16 & 2.775000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 585 | `0.1142` | `...ighbour_analysis.tex` \| 39 \| `0.1142` \| `2 & 13 & 16 & 2.775000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 586 | `0.2097` | `...ighbour_analysis.tex` \| 40 \| `0.2097` \| `2 & 14 & 15 & 2.405800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 586 | `0.1142` | `...05800 & 0.016000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 587 | `0.2097` | `... & 15 & 2.405800 & 0.016000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 587 | `0.1142` | `...ighbour_analysis.tex` \| 40 \| `0.1142` \| `2 & 14 & 15 & 2.405800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 588 | `0.2097` | `...ighbour_analysis.tex` \| 41 \| `0.2097` \| `2 & 18 & 2 & 1.842100 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 588 | `0.1142` | `...42100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 589 | `0.2097` | `...8 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 589 | `0.1142` | `...ighbour_analysis.tex` \| 41 \| `0.1142` \| `2 & 18 & 2 & 1.842100 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 590 | `0.2097` | `...ighbour_analysis.tex` \| 42 \| `0.2097` \| `2 & 24 & 32 & 4.244100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 590 | `0.1142` | `...44100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 591 | `0.2097` | `... & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 591 | `0.1142` | `...ighbour_analysis.tex` \| 42 \| `0.1142` \| `2 & 24 & 32 & 4.244100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 592 | `0.2097` | `...ighbour_analysis.tex` \| 43 \| `0.2097` \| `2 & 25 & 39 & 3.139000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 592 | `0.1142` | `...39000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 593 | `0.2097` | `... & 39 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 593 | `0.1142` | `...ighbour_analysis.tex` \| 43 \| `0.1142` \| `2 & 25 & 39 & 3.139000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 594 | `0.2097` | `...ighbour_analysis.tex` \| 44 \| `0.2097` \| `2 & 30 & 17 & 3.523900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 594 | `0.1142` | `...23900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 595 | `0.2097` | `... & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 595 | `0.1142` | `...ighbour_analysis.tex` \| 44 \| `0.1142` \| `2 & 30 & 17 & 3.523900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 596 | `0.2097` | `...ighbour_analysis.tex` \| 45 \| `0.2097` \| `2 & 31 & 32 & 6.201500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 596 | `0.1142` | `...01500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 597 | `0.2097` | `... & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 597 | `0.1142` | `...ighbour_analysis.tex` \| 45 \| `0.1142` \| `2 & 31 & 32 & 6.201500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 598 | `0.2097` | `...ighbour_analysis.tex` \| 46 \| `0.2097` \| `2 & 33 & 26 & 3.446100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 598 | `0.1142` | `...46100 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 599 | `0.2097` | `... & 26 & 3.446100 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 599 | `0.1142` | `...ighbour_analysis.tex` \| 46 \| `0.1142` \| `2 & 33 & 26 & 3.446100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 600 | `0.2097` | `...ighbour_analysis.tex` \| 47 \| `0.2097` \| `2 & 34 & 40 & 3.452600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 600 | `0.1142` | `...52600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 601 | `0.2097` | `... & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 601 | `0.1142` | `...ighbour_analysis.tex` \| 47 \| `0.1142` \| `2 & 34 & 40 & 3.452600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 602 | `0.2097` | `...ighbour_analysis.tex` \| 48 \| `0.2097` \| `2 & 42 & 28 & 5.499000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 602 | `0.1142` | `...99000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 603 | `0.2097` | `... & 28 & 5.499000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 603 | `0.1142` | `...ighbour_analysis.tex` \| 48 \| `0.1142` \| `2 & 42 & 28 & 5.499000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 604 | `0.2097` | `...ighbour_analysis.tex` \| 49 \| `0.2097` \| `2 & 47 & 48 & 17.681100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 604 | `0.1142` | `...81100 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 605 | `0.2097` | `...& 48 & 17.681100 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 605 | `0.1142` | `...ighbour_analysis.tex` \| 49 \| `0.1142` \| `2 & 47 & 48 & 17.681100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 606 | `0.2097` | `...ighbour_analysis.tex` \| 50 \| `0.2097` \| `2 & 50 & 48 & 16.692100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 606 | `0.1142` | `...92100 & 0.447500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 607 | `0.2097` | `...& 48 & 16.692100 & 0.447500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 607 | `0.1142` | `...ighbour_analysis.tex` \| 50 \| `0.1142` \| `2 & 50 & 48 & 16.692100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 608 | `0.2097` | `...ighbour_analysis.tex` \| 51 \| `0.2097` \| `2 & 54 & 51 & 5.281600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 608 | `0.1142` | `...81600 & 0.182500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 609 | `0.2097` | `... & 51 & 5.281600 & 0.182500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 609 | `0.1142` | `...ighbour_analysis.tex` \| 51 \| `0.1142` \| `2 & 54 & 51 & 5.281600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 610 | `0.2097` | `...ighbour_analysis.tex` \| 52 \| `0.2097` \| `2 & 55 & 51 & 2.184300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 610 | `0.1142` | `...84300 & 0.605000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 611 | `0.2097` | `... & 51 & 2.184300 & 0.605000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 611 | `0.1142` | `...ighbour_analysis.tex` \| 52 \| `0.1142` \| `2 & 55 & 51 & 2.184300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 612 | `0.2097` | `...ighbour_analysis.tex` \| 53 \| `0.2097` \| `3 & 2 & 18 & 1.842100 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 612 | `0.1142` | `...42100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 613 | `0.2097` | `... & 18 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 613 | `0.1142` | `...ighbour_analysis.tex` \| 53 \| `0.1142` \| `3 & 2 & 18 & 1.842100 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 614 | `0.2097` | `...ighbour_analysis.tex` \| 54 \| `0.2097` \| `3 & 14 & 19 & 2.813000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 614 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 615 | `0.2097` | `... & 19 & 2.813000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 615 | `0.1142` | `...ighbour_analysis.tex` \| 54 \| `0.1142` \| `3 & 14 & 19 & 2.813000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 616 | `0.2097` | `...ighbour_analysis.tex` \| 55 \| `0.2097` \| `3 & 15 & 19 & 2.702400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 616 | `0.1142` | `...02400 & 0.106000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 617 | `0.2097` | `... & 19 & 2.702400 & 0.106000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 617 | `0.1142` | `...ighbour_analysis.tex` \| 55 \| `0.1142` \| `3 & 15 & 19 & 2.702400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 618 | `0.2097` | `...ighbour_analysis.tex` \| 56 \| `0.2097` \| `3 & 27 & 26 & 2.754600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 618 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 619 | `0.2097` | `... & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 619 | `0.1142` | `...ighbour_analysis.tex` \| 56 \| `0.1142` \| `3 & 27 & 26 & 2.754600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 620 | `0.2097` | `...ighbour_analysis.tex` \| 57 \| `0.2097` \| `3 & 28 & 11 & 2.900200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 620 | `0.1142` | `...00200 & 0.508000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 621 | `0.2097` | `... & 11 & 2.900200 & 0.508000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 621 | `0.1142` | `...ighbour_analysis.tex` \| 57 \| `0.1142` \| `3 & 28 & 11 & 2.900200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 622 | `0.2097` | `...ighbour_analysis.tex` \| 58 \| `0.2097` \| `3 & 29 & 43 & 4.421300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 622 | `0.1142` | `...21300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 623 | `0.2097` | `... & 43 & 4.421300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 623 | `0.1142` | `...ighbour_analysis.tex` \| 58 \| `0.1142` \| `3 & 29 & 43 & 4.421300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 624 | `0.2097` | `...ighbour_analysis.tex` \| 59 \| `0.2097` \| `3 & 30 & 17 & 3.523900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 624 | `0.1142` | `...23900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 625 | `0.2097` | `... & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 625 | `0.1142` | `...ighbour_analysis.tex` \| 59 \| `0.1142` \| `3 & 30 & 17 & 3.523900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 626 | `0.2097` | `...ighbour_analysis.tex` \| 60 \| `0.2097` \| `3 & 32 & 1 & 4.811300 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 626 | `0.1142` | `...11300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 627 | `0.2097` | `...2 & 1 & 4.811300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 627 | `0.1142` | `...ighbour_analysis.tex` \| 60 \| `0.1142` \| `3 & 32 & 1 & 4.811300 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 628 | `0.2097` | `...ighbour_analysis.tex` \| 61 \| `0.2097` \| `3 & 33 & 26 & 3.446100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 628 | `0.1142` | `...46100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 629 | `0.2097` | `... & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 629 | `0.1142` | `...ighbour_analysis.tex` \| 61 \| `0.1142` \| `3 & 33 & 26 & 3.446100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 630 | `0.2097` | `...ighbour_analysis.tex` \| 62 \| `0.2097` \| `3 & 38 & 23 & 3.434400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 630 | `0.1142` | `...34400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 631 | `0.2097` | `... & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 631 | `0.1142` | `...ighbour_analysis.tex` \| 62 \| `0.1142` \| `3 & 38 & 23 & 3.434400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 632 | `0.2097` | `...ighbour_analysis.tex` \| 63 \| `0.2097` \| `3 & 44 & 8 & 2.039900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 632 | `0.1142` | `...39900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 633 | `0.2097` | `...4 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 633 | `0.1142` | `...ighbour_analysis.tex` \| 63 \| `0.1142` \| `3 & 44 & 8 & 2.039900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 634 | `64%` | `...tab_neighbour_analysis.tex` \| 64 \| `64%` \| `3 & 46 & 49 & 4.84...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 634 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 634 | `0.2097` | `... & 49 & 4.846400 & 0.450000 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 634 | `0.1142` | `...46400 & 0.450000 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 635 | `64%` | `...tab_neighbour_analysis.tex` \| 64 \| `0.2097` \| `3 & 46 & 49 & 4...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 635 | `0.2097` | `...ighbour_analysis.tex` \| 64 \| `0.2097` \| `3 & 46 & 49 & 4.846400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 635 | `0.1142` | `...46400 & 0.450000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 636 | `64%` | `...tab_neighbour_analysis.tex` \| 64 \| `0.1142` \| `3 & 46 & 49 & 4...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 636 | `0.2097` | `... & 49 & 4.846400 & 0.450000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 636 | `0.1142` | `...ighbour_analysis.tex` \| 64 \| `0.1142` \| `3 & 46 & 49 & 4.846400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 637 | `0.2097` | `...ighbour_analysis.tex` \| 65 \| `0.2097` \| `3 & 50 & 47 & 10.874000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 637 | `0.1142` | `...74000 & 0.257500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 638 | `0.2097` | `...& 47 & 10.874000 & 0.257500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 638 | `0.1142` | `...ighbour_analysis.tex` \| 65 \| `0.1142` \| `3 & 50 & 47 & 10.874000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 639 | `0.2097` | `...ighbour_analysis.tex` \| 66 \| `0.2097` \| `3 & 51 & 55 & 2.184300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 639 | `0.1142` | `...84300 & 0.255000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 640 | `0.2097` | `... & 55 & 2.184300 & 0.255000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 640 | `0.1142` | `...ighbour_analysis.tex` \| 66 \| `0.1142` \| `3 & 51 & 55 & 2.184300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 641 | `0.2097` | `...ighbour_analysis.tex` \| 67 \| `0.2097` \| `3 & 53 & 55 & 3.104300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 641 | `0.1142` | `...04300 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 641 | `0.0327` | `...` \| `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 641 | `0.0323` | `...` \| `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 642 | `0.2097` | `... & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 642 | `0.1142` | `...ighbour_analysis.tex` \| 67 \| `0.1142` \| `3 & 53 & 55 & 3.104300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 642 | `0.0327` | `...` \| `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 642 | `0.0323` | `...` \| `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 643 | `0.2097` | `... & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0327 (LO...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 643 | `0.1142` | `...04300 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0327 (LOPO absolute...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 643 | `0.0327` | `...ighbour_analysis.tex` \| 67 \| `0.0327` \| `3 & 53 & 55 & 3.104300 & ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 643 | `0.0323` | `...ighbour_analysis.tex` \| 67 \| `0.0327` \| `3 & 53 & 55 & 3.104300 &...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 644 | `0.2097` | `... & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0323 (Na...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 644 | `0.1142` | `...04300 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0323 (Naive packet-...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 644 | `0.0327` | `...ighbour_analysis.tex` \| 67 \| `0.0323` \| `3 & 53 & 55 & 3.104300 &...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 644 | `0.0323` | `...ighbour_analysis.tex` \| 67 \| `0.0323` \| `3 & 53 & 55 & 3.104300 & ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 645 | `0.2097` | `...ighbour_analysis.tex` \| 68 \| `0.2097` \| `4 & 3 & 27 & 4.098600 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 645 | `0.1142` | `...98600 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 646 | `0.2097` | `... & 27 & 4.098600 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 646 | `0.1142` | `...ighbour_analysis.tex` \| 68 \| `0.1142` \| `4 & 3 & 27 & 4.098600 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 647 | `0.2097` | `...ighbour_analysis.tex` \| 69 \| `0.2097` \| `4 & 7 & 29 & 3.849800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 647 | `0.1142` | `...49800 & 0.078000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 648 | `0.2097` | `... & 29 & 3.849800 & 0.078000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 648 | `0.1142` | `...ighbour_analysis.tex` \| 69 \| `0.1142` \| `4 & 7 & 29 & 3.849800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 649 | `0.2097` | `...ighbour_analysis.tex` \| 70 \| `0.2097` \| `4 & 12 & 5 & 5.651900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 649 | `0.1142` | `...51900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 650 | `0.2097` | `...2 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 650 | `0.1142` | `...ighbour_analysis.tex` \| 70 \| `0.1142` \| `4 & 12 & 5 & 5.651900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 651 | `0.2097` | `...ighbour_analysis.tex` \| 71 \| `0.2097` \| `4 & 14 & 15 & 2.405800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 651 | `0.1142` | `...05800 & 0.202000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 652 | `0.2097` | `... & 15 & 2.405800 & 0.202000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 652 | `0.1142` | `...ighbour_analysis.tex` \| 71 \| `0.1142` \| `4 & 14 & 15 & 2.405800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 653 | `0.2097` | `...ighbour_analysis.tex` \| 72 \| `0.2097` \| `4 & 17 & 13 & 4.399800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 653 | `0.1142` | `...99800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 654 | `0.2097` | `... & 13 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 654 | `0.1142` | `...ighbour_analysis.tex` \| 72 \| `0.1142` \| `4 & 17 & 13 & 4.399800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 655 | `0.2097` | `...ighbour_analysis.tex` \| 73 \| `0.2097` \| `4 & 20 & 15 & 1.805000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 655 | `0.1142` | `...05000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 656 | `0.2097` | `... & 15 & 1.805000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 656 | `0.1142` | `...ighbour_analysis.tex` \| 73 \| `0.1142` \| `4 & 20 & 15 & 1.805000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 657 | `0.2097` | `...ighbour_analysis.tex` \| 74 \| `0.2097` \| `4 & 24 & 32 & 4.244100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 657 | `0.1142` | `...44100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 658 | `0.2097` | `... & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 658 | `0.1142` | `...ighbour_analysis.tex` \| 74 \| `0.1142` \| `4 & 24 & 32 & 4.244100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 659 | `0.2097` | `...ighbour_analysis.tex` \| 75 \| `0.2097` \| `4 & 31 & 32 & 6.201500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 659 | `0.1142` | `...01500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 660 | `0.2097` | `... & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 660 | `0.1142` | `...ighbour_analysis.tex` \| 75 \| `0.1142` \| `4 & 31 & 32 & 6.201500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 661 | `0.2097` | `...ighbour_analysis.tex` \| 76 \| `0.2097` \| `4 & 35 & 44 & 2.985700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 661 | `0.1142` | `...85700 & 0.162500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 662 | `0.2097` | `... & 44 & 2.985700 & 0.162500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 662 | `0.1142` | `...ighbour_analysis.tex` \| 76 \| `0.1142` \| `4 & 35 & 44 & 2.985700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 663 | `0.2097` | `...ighbour_analysis.tex` \| 77 \| `0.2097` \| `4 & 36 & 27 & 3.866500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 663 | `0.1142` | `...66500 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 663 | `0.0327` | `...` \| `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 663 | `0.0323` | `...` \| `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 664 | `0.2097` | `... & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 664 | `0.1142` | `...ighbour_analysis.tex` \| 77 \| `0.1142` \| `4 & 36 & 27 & 3.866500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 664 | `0.0327` | `...` \| `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 664 | `0.0323` | `...` \| `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 665 | `0.2097` | `... & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0327 (LO...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 665 | `0.1142` | `...66500 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0327 (LOPO absolute...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 665 | `0.0327` | `...ighbour_analysis.tex` \| 77 \| `0.0327` \| `4 & 36 & 27 & 3.866500 & ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 665 | `0.0323` | `...ighbour_analysis.tex` \| 77 \| `0.0327` \| `4 & 36 & 27 & 3.866500 &...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 666 | `0.2097` | `... & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0323 (Na...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 666 | `0.1142` | `...66500 & 0.032500 & 0.209700 & 0.114200 \\` \| 0.0323 (Naive packet-...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 666 | `0.0327` | `...ighbour_analysis.tex` \| 77 \| `0.0323` \| `4 & 36 & 27 & 3.866500 &...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 666 | `0.0323` | `...ighbour_analysis.tex` \| 77 \| `0.0323` \| `4 & 36 & 27 & 3.866500 & ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 667 | `0.2097` | `...ighbour_analysis.tex` \| 78 \| `0.2097` \| `4 & 43 & 27 & 4.091900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 667 | `0.1142` | `...91900 & 0.115000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 668 | `0.2097` | `... & 27 & 4.091900 & 0.115000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 668 | `0.1142` | `...ighbour_analysis.tex` \| 78 \| `0.1142` \| `4 & 43 & 27 & 4.091900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 669 | `0.2097` | `...ighbour_analysis.tex` \| 79 \| `0.2097` \| `4 & 47 & 48 & 17.681100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 669 | `0.1142` | `...81100 & 0.992500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 670 | `0.2097` | `...& 48 & 17.681100 & 0.992500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 670 | `0.1142` | `...ighbour_analysis.tex` \| 79 \| `0.1142` \| `4 & 47 & 48 & 17.681100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 671 | `0.2097` | `...ighbour_analysis.tex` \| 80 \| `0.2097` \| `4 & 50 & 48 & 16.692100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 671 | `0.1142` | `...92100 & 0.997500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 672 | `0.2097` | `...& 48 & 16.692100 & 0.997500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 672 | `0.1142` | `...ighbour_analysis.tex` \| 80 \| `0.1142` \| `4 & 50 & 48 & 16.692100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 673 | `0.2097` | `...ighbour_analysis.tex` \| 81 \| `0.2097` \| `4 & 56 & 58 & 4.920800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 673 | `0.1142` | `...20800 & 0.320000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 674 | `0.2097` | `... & 58 & 4.920800 & 0.320000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 674 | `0.1142` | `...ighbour_analysis.tex` \| 81 \| `0.1142` \| `4 & 56 & 58 & 4.920800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 675 | `0.2097` | `...ighbour_analysis.tex` \| 82 \| `0.2097` \| `4 & 57 & 59 & 4.558800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 675 | `0.1142` | `...58800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 676 | `0.2097` | `... & 59 & 4.558800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 676 | `0.1142` | `...ighbour_analysis.tex` \| 82 \| `0.1142` \| `4 & 57 & 59 & 4.558800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 677 | `0.2097` | `...ighbour_analysis.tex` \| 83 \| `0.2097` \| `5 & 4 & 37 & 4.053400 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 677 | `0.1142` | `...53400 & 0.008000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 678 | `0.2097` | `... & 37 & 4.053400 & 0.008000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 678 | `0.1142` | `...ighbour_analysis.tex` \| 83 \| `0.1142` \| `5 & 4 & 37 & 4.053400 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 679 | `0.2097` | `...ighbour_analysis.tex` \| 84 \| `0.2097` \| `5 & 7 & 29 & 3.849800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 679 | `0.1142` | `...49800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 680 | `0.2097` | `... & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 680 | `0.1142` | `...ighbour_analysis.tex` \| 84 \| `0.1142` \| `5 & 7 & 29 & 3.849800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 681 | `0.2097` | `...ighbour_analysis.tex` \| 85 \| `0.2097` \| `5 & 8 & 44 & 2.039900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 681 | `0.1142` | `...39900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 682 | `0.2097` | `... & 44 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 682 | `0.1142` | `...ighbour_analysis.tex` \| 85 \| `0.1142` \| `5 & 8 & 44 & 2.039900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 683 | `0.2097` | `...ighbour_analysis.tex` \| 86 \| `0.2097` \| `5 & 14 & 20 & 2.699200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 683 | `0.1142` | `...99200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 684 | `0.2097` | `... & 20 & 2.699200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 684 | `0.1142` | `...ighbour_analysis.tex` \| 86 \| `0.1142` \| `5 & 14 & 20 & 2.699200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 685 | `64%` | `...ighbour_analysis.tex` \| 87 \| `64%` \| `5 & 15 & 20 & 1.805000 & ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 685 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 685 | `0.2097` | `... & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 685 | `0.1142` | `...05000 & 0.264000 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 686 | `64%` | `... `5 & 15 & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 686 | `0.2097` | `...ighbour_analysis.tex` \| 87 \| `0.2097` \| `5 & 15 & 20 & 1.805000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 686 | `0.1142` | `...05000 & 0.264000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 687 | `64%` | `... `5 & 15 & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 687 | `0.2097` | `... & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 687 | `0.1142` | `...ighbour_analysis.tex` \| 87 \| `0.1142` \| `5 & 15 & 20 & 1.805000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 688 | `0.2097` | `...ighbour_analysis.tex` \| 88 \| `0.2097` \| `5 & 22 & 44 & 2.458200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 688 | `0.1142` | `...58200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 689 | `0.2097` | `... & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 689 | `0.1142` | `...ighbour_analysis.tex` \| 88 \| `0.1142` \| `5 & 22 & 44 & 2.458200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 690 | `0.2097` | `...ighbour_analysis.tex` \| 89 \| `0.2097` \| `5 & 26 & 27 & 2.754600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 690 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 691 | `0.2097` | `... & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 691 | `0.1142` | `...ighbour_analysis.tex` \| 89 \| `0.1142` \| `5 & 26 & 27 & 2.754600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 692 | `0.2097` | `...ighbour_analysis.tex` \| 90 \| `0.2097` \| `5 & 34 & 44 & 3.518400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 692 | `0.1142` | `...18400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 693 | `0.2097` | `... & 44 & 3.518400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 693 | `0.1142` | `...ighbour_analysis.tex` \| 90 \| `0.1142` \| `5 & 34 & 44 & 3.518400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 694 | `0.2097` | `...ighbour_analysis.tex` \| 91 \| `0.2097` \| `5 & 36 & 3 & 3.770200 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 694 | `0.1142` | `...70200 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 695 | `0.2097` | `...6 & 3 & 3.770200 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 695 | `0.1142` | `...ighbour_analysis.tex` \| 91 \| `0.1142` \| `5 & 36 & 3 & 3.770200 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 696 | `0.2097` | `...ighbour_analysis.tex` \| 92 \| `0.2097` \| `5 & 38 & 23 & 3.434400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 696 | `0.1142` | `...34400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 697 | `0.2097` | `... & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 697 | `0.1142` | `...ighbour_analysis.tex` \| 92 \| `0.1142` \| `5 & 38 & 23 & 3.434400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 698 | `0.2097` | `...ighbour_analysis.tex` \| 93 \| `0.2097` \| `5 & 42 & 11 & 4.981400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 698 | `0.1142` | `...81400 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 699 | `0.2097` | `... & 11 & 4.981400 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 699 | `0.1142` | `...ighbour_analysis.tex` \| 93 \| `0.1142` \| `5 & 42 & 11 & 4.981400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 700 | `0.2097` | `...ighbour_analysis.tex` \| 94 \| `0.2097` \| `5 & 47 & 50 & 10.874000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 700 | `0.1142` | `...74000 & 0.127500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 701 | `0.2097` | `...& 50 & 10.874000 & 0.127500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 701 | `0.1142` | `...ighbour_analysis.tex` \| 94 \| `0.1142` \| `5 & 47 & 50 & 10.874000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 702 | `64%` | `...ighbour_analysis.tex` \| 95 \| `64%` \| `5 & 53 & 51 & 2.109800 & ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 702 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 702 | `0.2097` | `... & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 702 | `0.1142` | `...09800 & 0.645000 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 703 | `64%` | `...\| `5 & 53 & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\`...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 703 | `0.2097` | `...ighbour_analysis.tex` \| 95 \| `0.2097` \| `5 & 53 & 51 & 2.109800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 703 | `0.1142` | `...09800 & 0.645000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 704 | `64%` | `...\| `5 & 53 & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\`...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 704 | `0.2097` | `... & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 704 | `0.1142` | `...ighbour_analysis.tex` \| 95 \| `0.1142` \| `5 & 53 & 51 & 2.109800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 705 | `0.2097` | `...ighbour_analysis.tex` \| 96 \| `0.2097` \| `5 & 56 & 57 & 4.186200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 705 | `0.1142` | `...86200 & 0.512500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 706 | `0.2097` | `... & 57 & 4.186200 & 0.512500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 706 | `0.1142` | `...ighbour_analysis.tex` \| 96 \| `0.1142` \| `5 & 56 & 57 & 4.186200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 707 | `0.2097` | `...ighbour_analysis.tex` \| 97 \| `0.2097` \| `5 & 59 & 57 & 4.558800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 707 | `0.1142` | `...58800 & 0.830000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 708 | `0.2097` | `... & 57 & 4.558800 & 0.830000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 708 | `0.1142` | `...ighbour_analysis.tex` \| 97 \| `0.1142` \| `5 & 59 & 57 & 4.558800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 709 | `0.2097` | `...ighbour_analysis.tex` \| 98 \| `0.2097` \| `6 & 7 & 29 & 3.849800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 709 | `0.1142` | `...49800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 710 | `0.2097` | `... & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 710 | `0.1142` | `...ighbour_analysis.tex` \| 98 \| `0.1142` \| `6 & 7 & 29 & 3.849800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 711 | `0.2097` | `...ighbour_analysis.tex` \| 99 \| `0.2097` \| `6 & 8 & 44 & 2.039900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 711 | `0.1142` | `...39900 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 712 | `0.2097` | `... & 44 & 2.039900 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 712 | `0.1142` | `...ighbour_analysis.tex` \| 99 \| `0.1142` \| `6 & 8 & 44 & 2.039900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 713 | `0.2097` | `...ghbour_analysis.tex` \| 100 \| `0.2097` \| `6 & 11 & 19 & 2.615600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 713 | `0.1142` | `...15600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 714 | `0.2097` | `... & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 714 | `0.1142` | `...ghbour_analysis.tex` \| 100 \| `0.1142` \| `6 & 11 & 19 & 2.615600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 715 | `0.2097` | `...ghbour_analysis.tex` \| 101 \| `0.2097` \| `6 & 12 & 5 & 5.651900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 715 | `0.1142` | `...51900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 716 | `0.2097` | `...2 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 716 | `0.1142` | `...ghbour_analysis.tex` \| 101 \| `0.1142` \| `6 & 12 & 5 & 5.651900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 717 | `0.2097` | `...ghbour_analysis.tex` \| 102 \| `0.2097` \| `6 & 13 & 44 & 4.424700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 717 | `0.1142` | `...24700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 718 | `0.2097` | `... & 44 & 4.424700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 718 | `0.1142` | `...ghbour_analysis.tex` \| 102 \| `0.1142` \| `6 & 13 & 44 & 4.424700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 719 | `0.2097` | `...ghbour_analysis.tex` \| 103 \| `0.2097` \| `6 & 26 & 33 & 3.446100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 719 | `0.1142` | `...46100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 720 | `0.2097` | `... & 33 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 720 | `0.1142` | `...ghbour_analysis.tex` \| 103 \| `0.1142` \| `6 & 26 & 33 & 3.446100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 721 | `0.2097` | `...ghbour_analysis.tex` \| 104 \| `0.2097` \| `6 & 27 & 29 & 3.817400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 721 | `0.1142` | `...17400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 722 | `0.2097` | `... & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 722 | `0.1142` | `...ghbour_analysis.tex` \| 104 \| `0.1142` \| `6 & 27 & 29 & 3.817400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 723 | `0.2097` | `...ghbour_analysis.tex` \| 105 \| `0.2097` \| `6 & 34 & 44 & 3.518400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 723 | `0.1142` | `...18400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 724 | `0.2097` | `... & 44 & 3.518400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 724 | `0.1142` | `...ghbour_analysis.tex` \| 105 \| `0.1142` \| `6 & 34 & 44 & 3.518400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 725 | `0.2097` | `...ghbour_analysis.tex` \| 106 \| `0.2097` \| `6 & 38 & 23 & 3.434400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 725 | `0.1142` | `...34400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 726 | `0.2097` | `... & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 726 | `0.1142` | `...ghbour_analysis.tex` \| 106 \| `0.1142` \| `6 & 38 & 23 & 3.434400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 727 | `0.2097` | `...ghbour_analysis.tex` \| 107 \| `0.2097` \| `6 & 40 & 44 & 2.738200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 727 | `0.1142` | `...38200 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 728 | `0.2097` | `... & 44 & 2.738200 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 728 | `0.1142` | `...ghbour_analysis.tex` \| 107 \| `0.1142` \| `6 & 40 & 44 & 2.738200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 729 | `0.2097` | `...ghbour_analysis.tex` \| 108 \| `0.2097` \| `6 & 43 & 6 & 3.376900 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 729 | `0.1142` | `...76900 & 0.045000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 730 | `0.2097` | `...3 & 6 & 3.376900 & 0.045000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 730 | `0.1142` | `...ghbour_analysis.tex` \| 108 \| `0.1142` \| `6 & 43 & 6 & 3.376900 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 731 | `0.2097` | `...ghbour_analysis.tex` \| 109 \| `0.2097` \| `6 & 47 & 50 & 10.874000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 731 | `0.1142` | `...74000 & 0.995000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 732 | `0.2097` | `...& 50 & 10.874000 & 0.995000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 732 | `0.1142` | `...ghbour_analysis.tex` \| 109 \| `0.1142` \| `6 & 47 & 50 & 10.874000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 733 | `0.2097` | `...ghbour_analysis.tex` \| 110 \| `0.2097` \| `6 & 48 & 49 & 9.769000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 733 | `0.1142` | `...69000 & 0.957500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 734 | `0.2097` | `... & 49 & 9.769000 & 0.957500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 734 | `0.1142` | `...ghbour_analysis.tex` \| 110 \| `0.1142` \| `6 & 48 & 49 & 9.769000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 735 | `0.2097` | `...ghbour_analysis.tex` \| 111 \| `0.2097` \| `6 & 53 & 51 & 2.109800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 735 | `0.1142` | `...09800 & 0.742500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 736 | `0.2097` | `... & 51 & 2.109800 & 0.742500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 736 | `0.1142` | `...ghbour_analysis.tex` \| 111 \| `0.1142` \| `6 & 53 & 51 & 2.109800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 737 | `0.2097` | `...ghbour_analysis.tex` \| 112 \| `0.2097` \| `6 & 55 & 51 & 2.184300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 737 | `0.1142` | `...84300 & 0.215000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 738 | `0.2097` | `... & 51 & 2.184300 & 0.215000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 738 | `0.1142` | `...ghbour_analysis.tex` \| 112 \| `0.1142` \| `6 & 55 & 51 & 2.184300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 739 | `4.43` | `...ghbour_analysis.tex` \| 113 \| `4.43` \| `7 & 2 & 26 & 4.436800 & 0...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 739 | `0.2097` | `... & 26 & 4.436800 & 0.072000 & 0.209700 & 0.114200 \\` \| 4.43% (0.0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 739 | `0.1142` | `...36800 & 0.072000 & 0.209700 & 0.114200 \\` \| 4.43% (0.044315, epis...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 740 | `4.43` | `...13 \| `0.2097` \| `7 & 2 & 26 & 4.436800 & 0.072000 & 0.209700 & 0...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 740 | `0.2097` | `...ghbour_analysis.tex` \| 113 \| `0.2097` \| `7 & 2 & 26 & 4.436800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 740 | `0.1142` | `...36800 & 0.072000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 741 | `4.43` | `...13 \| `0.1142` \| `7 & 2 & 26 & 4.436800 & 0.072000 & 0.209700 & 0...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 741 | `0.2097` | `... & 26 & 4.436800 & 0.072000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 741 | `0.1142` | `...ghbour_analysis.tex` \| 113 \| `0.1142` \| `7 & 2 & 26 & 4.436800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 742 | `0.2097` | `...ghbour_analysis.tex` \| 114 \| `0.2097` \| `7 & 15 & 14 & 2.405800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 742 | `0.1142` | `...05800 & 0.244000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 743 | `0.2097` | `... & 14 & 2.405800 & 0.244000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 743 | `0.1142` | `...ghbour_analysis.tex` \| 114 \| `0.1142` \| `7 & 15 & 14 & 2.405800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 744 | `0.2097` | `...ghbour_analysis.tex` \| 115 \| `0.2097` \| `7 & 16 & 13 & 2.775000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 744 | `0.1142` | `...75000 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 745 | `0.2097` | `... & 13 & 2.775000 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 745 | `0.1142` | `...ghbour_analysis.tex` \| 115 \| `0.1142` \| `7 & 16 & 13 & 2.775000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 746 | `0.2097` | `...ghbour_analysis.tex` \| 116 \| `0.2097` \| `7 & 21 & 33 & 4.692500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 746 | `0.1142` | `...92500 & 0.018000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 747 | `0.2097` | `... & 33 & 4.692500 & 0.018000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 747 | `0.1142` | `...ghbour_analysis.tex` \| 116 \| `0.1142` \| `7 & 21 & 33 & 4.692500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 748 | `0.2097` | `...ghbour_analysis.tex` \| 117 \| `0.2097` \| `7 & 22 & 44 & 2.458200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 748 | `0.1142` | `...58200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 749 | `0.2097` | `... & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 749 | `0.1142` | `...ghbour_analysis.tex` \| 117 \| `0.1142` \| `7 & 22 & 44 & 2.458200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 750 | `0.2097` | `...ghbour_analysis.tex` \| 118 \| `0.2097` \| `7 & 28 & 11 & 2.900200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 750 | `0.1142` | `...00200 & 0.692000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 751 | `0.2097` | `... & 11 & 2.900200 & 0.692000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 751 | `0.1142` | `...ghbour_analysis.tex` \| 118 \| `0.1142` \| `7 & 28 & 11 & 2.900200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 752 | `0.2097` | `...ghbour_analysis.tex` \| 119 \| `0.2097` \| `7 & 30 & 13 & 4.506200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 752 | `0.1142` | `...06200 & 0.150000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 753 | `0.2097` | `... & 13 & 4.506200 & 0.150000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 753 | `0.1142` | `...ghbour_analysis.tex` \| 119 \| `0.1142` \| `7 & 30 & 13 & 4.506200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 754 | `0.2097` | `...ghbour_analysis.tex` \| 120 \| `0.2097` \| `7 & 36 & 4 & 2.899800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 754 | `0.1142` | `...99800 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 755 | `0.2097` | `...6 & 4 & 2.899800 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 755 | `0.1142` | `...ghbour_analysis.tex` \| 120 \| `0.1142` \| `7 & 36 & 4 & 2.899800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 756 | `0.2097` | `...ghbour_analysis.tex` \| 121 \| `0.2097` \| `7 & 39 & 25 & 3.139000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 756 | `0.1142` | `...39000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 757 | `0.2097` | `... & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 757 | `0.1142` | `...ghbour_analysis.tex` \| 121 \| `0.1142` \| `7 & 39 & 25 & 3.139000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 758 | `0.2097` | `...ghbour_analysis.tex` \| 122 \| `0.2097` \| `7 & 40 & 44 & 2.738200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 758 | `0.1142` | `...38200 & 0.037500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 759 | `0.2097` | `... & 44 & 2.738200 & 0.037500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 759 | `0.1142` | `...ghbour_analysis.tex` \| 122 \| `0.1142` \| `7 & 40 & 44 & 2.738200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 760 | `0.2097` | `...ghbour_analysis.tex` \| 123 \| `0.2097` \| `7 & 41 & 7 & 4.889200 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 760 | `0.1142` | `...89200 & 0.110000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 761 | `0.2097` | `...1 & 7 & 4.889200 & 0.110000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 761 | `0.1142` | `...ghbour_analysis.tex` \| 123 \| `0.1142` \| `7 & 41 & 7 & 4.889200 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 762 | `0.2097` | `...ghbour_analysis.tex` \| 124 \| `0.2097` \| `7 & 46 & 48 & 6.468700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 762 | `0.1142` | `...68700 & 0.522500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 763 | `0.2097` | `... & 48 & 6.468700 & 0.522500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 763 | `0.1142` | `...ghbour_analysis.tex` \| 124 \| `0.1142` \| `7 & 46 & 48 & 6.468700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 764 | `0.2097` | `...ghbour_analysis.tex` \| 125 \| `0.2097` \| `7 & 50 & 47 & 10.874000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 764 | `0.1142` | `...74000 & 0.872500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 765 | `0.2097` | `...& 47 & 10.874000 & 0.872500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 765 | `0.1142` | `...ghbour_analysis.tex` \| 125 \| `0.1142` \| `7 & 50 & 47 & 10.874000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 766 | `0.2097` | `...ghbour_analysis.tex` \| 126 \| `0.2097` \| `7 & 55 & 51 & 2.184300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 766 | `0.1142` | `...84300 & 0.535000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 767 | `0.2097` | `... & 51 & 2.184300 & 0.535000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 767 | `0.1142` | `...ghbour_analysis.tex` \| 126 \| `0.1142` \| `7 & 55 & 51 & 2.184300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 768 | `0.2097` | `...ghbour_analysis.tex` \| 127 \| `0.2097` \| `7 & 59 & 57 & 4.558800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 768 | `0.1142` | `...58800 & 0.095000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 769 | `0.2097` | `... & 57 & 4.558800 & 0.095000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 769 | `0.1142` | `...ghbour_analysis.tex` \| 127 \| `0.1142` \| `7 & 59 & 57 & 4.558800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 770 | `0.2097` | `...ghbour_analysis.tex` \| 128 \| `0.2097` \| `8 & 1 & 5 & 4.573300 & 0....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 770 | `0.1142` | `...73300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 771 | `0.2097` | `...1 & 5 & 4.573300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 771 | `0.1142` | `...ghbour_analysis.tex` \| 128 \| `0.1142` \| `8 & 1 & 5 & 4.573300 & 0....` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 772 | `0.2097` | `...ghbour_analysis.tex` \| 129 \| `0.2097` \| `8 & 8 & 40 & 2.013000 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 772 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 773 | `0.2097` | `... & 40 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 773 | `0.1142` | `...ghbour_analysis.tex` \| 129 \| `0.1142` \| `8 & 8 & 40 & 2.013000 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 774 | `0.2097` | `...ghbour_analysis.tex` \| 130 \| `0.2097` \| `8 & 16 & 13 & 2.775000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 774 | `0.1142` | `...75000 & 0.058000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 775 | `0.2097` | `... & 13 & 2.775000 & 0.058000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 775 | `0.1142` | `...ghbour_analysis.tex` \| 130 \| `0.1142` \| `8 & 16 & 13 & 2.775000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 776 | `0.2097` | `...ghbour_analysis.tex` \| 131 \| `0.2097` \| `8 & 17 & 30 & 3.523900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 776 | `0.1142` | `...23900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 777 | `0.2097` | `... & 30 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 777 | `0.1142` | `...ghbour_analysis.tex` \| 131 \| `0.1142` \| `8 & 17 & 30 & 3.523900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 778 | `0.2097` | `...ghbour_analysis.tex` \| 132 \| `0.2097` \| `8 & 19 & 11 & 2.615600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 778 | `0.1142` | `...15600 & 0.182000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 779 | `0.2097` | `... & 11 & 2.615600 & 0.182000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 779 | `0.1142` | `...ghbour_analysis.tex` \| 132 \| `0.1142` \| `8 & 19 & 11 & 2.615600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 780 | `0.2097` | `...ghbour_analysis.tex` \| 133 \| `0.2097` \| `8 & 23 & 38 & 3.434400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 780 | `0.1142` | `...34400 & 0.574000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 781 | `0.2097` | `... & 38 & 3.434400 & 0.574000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 781 | `0.1142` | `...ghbour_analysis.tex` \| 133 \| `0.1142` \| `8 & 23 & 38 & 3.434400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 782 | `0.2097` | `...ghbour_analysis.tex` \| 134 \| `0.2097` \| `8 & 26 & 27 & 2.754600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 782 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 783 | `0.2097` | `... & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 783 | `0.1142` | `...ghbour_analysis.tex` \| 134 \| `0.1142` \| `8 & 26 & 27 & 2.754600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 784 | `0.2097` | `...ghbour_analysis.tex` \| 135 \| `0.2097` \| `8 & 31 & 32 & 6.201500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 784 | `0.1142` | `...01500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 785 | `0.2097` | `... & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 785 | `0.1142` | `...ghbour_analysis.tex` \| 135 \| `0.1142` \| `8 & 31 & 32 & 6.201500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 786 | `0.2097` | `...ghbour_analysis.tex` \| 136 \| `0.2097` \| `8 & 35 & 34 & 4.521200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 786 | `0.1142` | `...21200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 787 | `0.2097` | `... & 34 & 4.521200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 787 | `0.1142` | `...ghbour_analysis.tex` \| 136 \| `0.1142` \| `8 & 35 & 34 & 4.521200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 788 | `0.2097` | `...ghbour_analysis.tex` \| 137 \| `0.2097` \| `8 & 39 & 11 & 3.408200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 788 | `0.1142` | `...08200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 789 | `0.2097` | `... & 11 & 3.408200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 789 | `0.1142` | `...ghbour_analysis.tex` \| 137 \| `0.1142` \| `8 & 39 & 11 & 3.408200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 790 | `0.2097` | `...ghbour_analysis.tex` \| 138 \| `0.2097` \| `8 & 42 & 11 & 4.981400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 790 | `0.1142` | `...81400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 791 | `0.2097` | `... & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 791 | `0.1142` | `...ghbour_analysis.tex` \| 138 \| `0.1142` \| `8 & 42 & 11 & 4.981400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 792 | `0.2097` | `...ghbour_analysis.tex` \| 139 \| `0.2097` \| `8 & 48 & 46 & 6.468700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 792 | `0.1142` | `...68700 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 793 | `0.2097` | `... & 46 & 6.468700 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 793 | `0.1142` | `...ghbour_analysis.tex` \| 139 \| `0.1142` \| `8 & 48 & 46 & 6.468700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 794 | `0.2097` | `...ghbour_analysis.tex` \| 140 \| `0.2097` \| `8 & 50 & 46 & 21.668300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 794 | `0.1142` | `...68300 & 0.995000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 795 | `0.2097` | `...& 46 & 21.668300 & 0.995000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 795 | `0.1142` | `...ghbour_analysis.tex` \| 140 \| `0.1142` \| `8 & 50 & 46 & 21.668300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 796 | `0.2097` | `...ghbour_analysis.tex` \| 141 \| `0.2097` \| `8 & 54 & 55 & 4.858400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 796 | `0.1142` | `...58400 & 0.850000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 797 | `0.2097` | `... & 55 & 4.858400 & 0.850000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 797 | `0.1142` | `...ghbour_analysis.tex` \| 141 \| `0.1142` \| `8 & 54 & 55 & 4.858400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 798 | `0.2097` | `...ghbour_analysis.tex` \| 142 \| `0.2097` \| `8 & 56 & 57 & 4.186200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 798 | `0.1142` | `...86200 & 0.132500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 799 | `0.2097` | `... & 57 & 4.186200 & 0.132500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 799 | `0.1142` | `...ghbour_analysis.tex` \| 142 \| `0.1142` \| `8 & 56 & 57 & 4.186200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 800 | `0.2097` | `...ghbour_analysis.tex` \| 143 \| `0.2097` \| `9 & 9 & 23 & 3.107600 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 800 | `0.1142` | `...07600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 801 | `0.2097` | `... & 23 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 801 | `0.1142` | `...ghbour_analysis.tex` \| 143 \| `0.1142` \| `9 & 9 & 23 & 3.107600 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 802 | `0.2097` | `...ghbour_analysis.tex` \| 144 \| `0.2097` \| `9 & 10 & 19 & 4.492500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 802 | `0.1142` | `...92500 & 0.020000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 803 | `0.2097` | `... & 19 & 4.492500 & 0.020000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 803 | `0.1142` | `...ghbour_analysis.tex` \| 144 \| `0.1142` \| `9 & 10 & 19 & 4.492500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 804 | `0.2097` | `...ghbour_analysis.tex` \| 145 \| `0.2097` \| `9 & 15 & 19 & 2.702400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 804 | `0.1142` | `...02400 & 0.634000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 805 | `0.2097` | `... & 19 & 2.702400 & 0.634000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 805 | `0.1142` | `...ghbour_analysis.tex` \| 145 \| `0.1142` \| `9 & 15 & 19 & 2.702400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 806 | `0.2097` | `...ghbour_analysis.tex` \| 146 \| `0.2097` \| `9 & 20 & 19 & 2.718300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 806 | `0.1142` | `...18300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 807 | `0.2097` | `... & 19 & 2.718300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 807 | `0.1142` | `...ghbour_analysis.tex` \| 146 \| `0.1142` \| `9 & 20 & 19 & 2.718300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 808 | `0.2097` | `...ghbour_analysis.tex` \| 147 \| `0.2097` \| `9 & 25 & 16 & 3.200800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 808 | `0.1142` | `...00800 & 0.030000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 809 | `0.2097` | `... & 16 & 3.200800 & 0.030000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 809 | `0.1142` | `...ghbour_analysis.tex` \| 147 \| `0.1142` \| `9 & 25 & 16 & 3.200800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 810 | `0.2097` | `...ghbour_analysis.tex` \| 148 \| `0.2097` \| `9 & 26 & 33 & 3.446100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 810 | `0.1142` | `...46100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 811 | `0.2097` | `... & 33 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 811 | `0.1142` | `...ghbour_analysis.tex` \| 148 \| `0.1142` \| `9 & 26 & 33 & 3.446100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 812 | `0.2097` | `...ghbour_analysis.tex` \| 149 \| `0.2097` \| `9 & 27 & 29 & 3.817400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 812 | `0.1142` | `...17400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 813 | `0.2097` | `... & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 813 | `0.1142` | `...ghbour_analysis.tex` \| 149 \| `0.1142` \| `9 & 27 & 29 & 3.817400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 814 | `0.2097` | `...ghbour_analysis.tex` \| 150 \| `0.2097` \| `9 & 32 & 5 & 4.460700 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 814 | `0.1142` | `...60700 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 815 | `0.2097` | `...2 & 5 & 4.460700 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 815 | `0.1142` | `...ghbour_analysis.tex` \| 150 \| `0.1142` \| `9 & 32 & 5 & 4.460700 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 816 | `0.2097` | `...ghbour_analysis.tex` \| 151 \| `0.2097` \| `9 & 38 & 23 & 3.434400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 816 | `0.1142` | `...34400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 817 | `0.2097` | `... & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 817 | `0.1142` | `...ghbour_analysis.tex` \| 151 \| `0.1142` \| `9 & 38 & 23 & 3.434400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 818 | `0.2097` | `...ghbour_analysis.tex` \| 152 \| `0.2097` \| `9 & 40 & 8 & 2.013000 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 818 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 819 | `0.2097` | `...0 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 819 | `0.1142` | `...ghbour_analysis.tex` \| 152 \| `0.1142` \| `9 & 40 & 8 & 2.013000 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 820 | `0.2097` | `...ghbour_analysis.tex` \| 153 \| `0.2097` \| `9 & 41 & 21 & 4.791500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 820 | `0.1142` | `...91500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 821 | `0.2097` | `... & 21 & 4.791500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 821 | `0.1142` | `...ghbour_analysis.tex` \| 153 \| `0.1142` \| `9 & 41 & 21 & 4.791500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 822 | `0.2097` | `...ghbour_analysis.tex` \| 154 \| `0.2097` \| `9 & 52 & 59 & 5.114500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 822 | `0.1142` | `...14500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 823 | `0.2097` | `... & 59 & 5.114500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 823 | `0.1142` | `...ghbour_analysis.tex` \| 154 \| `0.1142` \| `9 & 52 & 59 & 5.114500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 824 | `0.2097` | `...ghbour_analysis.tex` \| 155 \| `0.2097` \| `9 & 53 & 60 & 4.375400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 824 | `0.1142` | `...75400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 824 | `4.37` | `...5 \| `0.2097` \| `9 & 53 & 60 & 4.375400 & 0.000000 & 0.209700 & 0...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 825 | `0.2097` | `... & 60 & 4.375400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 825 | `0.1142` | `...ghbour_analysis.tex` \| 155 \| `0.1142` \| `9 & 53 & 60 & 4.375400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 825 | `4.37` | `...5 \| `0.1142` \| `9 & 53 & 60 & 4.375400 & 0.000000 & 0.209700 & 0...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 826 | `0.2097` | `... & 60 & 4.375400 & 0.000000 & 0.209700 & 0.114200 \\` \| 4.37% (0.0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 826 | `0.1142` | `...75400 & 0.000000 & 0.209700 & 0.114200 \\` \| 4.37% (0.043740, burs...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 826 | `4.37` | `...ghbour_analysis.tex` \| 155 \| `4.37` \| `9 & 53 & 60 & 4.375400 & ...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 827 | `0.2097` | `...ghbour_analysis.tex` \| 156 \| `0.2097` \| `9 & 55 & 60 & 5.370100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 827 | `0.1142` | `...70100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 828 | `0.2097` | `... & 60 & 5.370100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 828 | `0.1142` | `...ghbour_analysis.tex` \| 156 \| `0.1142` \| `9 & 55 & 60 & 5.370100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 829 | `0.2097` | `...ghbour_analysis.tex` \| 157 \| `0.2097` \| `9 & 57 & 56 & 4.186200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 829 | `0.1142` | `...86200 & 0.797500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 830 | `0.2097` | `... & 56 & 4.186200 & 0.797500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 830 | `0.1142` | `...ghbour_analysis.tex` \| 157 \| `0.1142` \| `9 & 57 & 56 & 4.186200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 831 | `0.2097` | `...ghbour_analysis.tex` \| 158 \| `0.2097` \| `10 & 4 & 43 & 3.420400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 831 | `0.1142` | `...20400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 832 | `0.2097` | `... & 43 & 3.420400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 832 | `0.1142` | `...ghbour_analysis.tex` \| 158 \| `0.1142` \| `10 & 4 & 43 & 3.420400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 833 | `0.2097` | `...ghbour_analysis.tex` \| 159 \| `0.2097` \| `10 & 10 & 39 & 3.431400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 833 | `0.1142` | `...31400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 834 | `0.2097` | `... & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 834 | `0.1142` | `...ghbour_analysis.tex` \| 159 \| `0.1142` \| `10 & 10 & 39 & 3.431400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 835 | `0.2097` | `...ghbour_analysis.tex` \| 160 \| `0.2097` \| `10 & 12 & 24 & 6.624900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 835 | `0.1142` | `...24900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 836 | `0.2097` | `... & 24 & 6.624900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 836 | `0.1142` | `...ghbour_analysis.tex` \| 160 \| `0.1142` \| `10 & 12 & 24 & 6.624900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 837 | `0.2097` | `...ghbour_analysis.tex` \| 161 \| `0.2097` \| `10 & 16 & 13 & 2.775000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 837 | `0.1142` | `...75000 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 838 | `0.2097` | `... & 13 & 2.775000 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 838 | `0.1142` | `...ghbour_analysis.tex` \| 161 \| `0.1142` \| `10 & 16 & 13 & 2.775000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 839 | `0.2097` | `...ghbour_analysis.tex` \| 162 \| `0.2097` \| `10 & 17 & 13 & 4.399800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 839 | `0.1142` | `...99800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 840 | `0.2097` | `... & 13 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 840 | `0.1142` | `...ghbour_analysis.tex` \| 162 \| `0.1142` \| `10 & 17 & 13 & 4.399800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 841 | `0.2097` | `...ghbour_analysis.tex` \| 163 \| `0.2097` \| `10 & 22 & 44 & 2.458200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 841 | `0.1142` | `...58200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 842 | `0.2097` | `... & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 842 | `0.1142` | `...ghbour_analysis.tex` \| 163 \| `0.1142` \| `10 & 22 & 44 & 2.458200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 843 | `64%` | `...ab_neighbour_analysis.tex` \| 164 \| `0.2097` \| `10 & 27 & 26 & ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 843 | `0.2097` | `...ghbour_analysis.tex` \| 164 \| `0.2097` \| `10 & 27 & 26 & 2.754600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 843 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 844 | `64%` | `...ab_neighbour_analysis.tex` \| 164 \| `0.1142` \| `10 & 27 & 26 & ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 844 | `0.2097` | `... & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 844 | `0.1142` | `...ghbour_analysis.tex` \| 164 \| `0.1142` \| `10 & 27 & 26 & 2.754600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 845 | `0.2097` | `...ghbour_analysis.tex` \| 165 \| `0.2097` \| `10 & 31 & 32 & 6.201500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 845 | `0.1142` | `...01500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 846 | `0.2097` | `... & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 846 | `0.1142` | `...ghbour_analysis.tex` \| 165 \| `0.1142` \| `10 & 31 & 32 & 6.201500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 847 | `0.2097` | `...ghbour_analysis.tex` \| 166 \| `0.2097` \| `10 & 33 & 26 & 3.446100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 847 | `0.1142` | `...46100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 848 | `0.2097` | `... & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 848 | `0.1142` | `...ghbour_analysis.tex` \| 166 \| `0.1142` \| `10 & 33 & 26 & 3.446100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 849 | `0.2097` | `...ghbour_analysis.tex` \| 167 \| `0.2097` \| `10 & 36 & 6 & 3.530000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 849 | `0.1142` | `...30000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 850 | `0.2097` | `...6 & 6 & 3.530000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 850 | `0.1142` | `...ghbour_analysis.tex` \| 167 \| `0.1142` \| `10 & 36 & 6 & 3.530000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 851 | `0.2097` | `...ghbour_analysis.tex` \| 168 \| `0.2097` \| `10 & 42 & 11 & 4.981400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 851 | `0.1142` | `...81400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 852 | `0.2097` | `... & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 852 | `0.1142` | `...ghbour_analysis.tex` \| 168 \| `0.1142` \| `10 & 42 & 11 & 4.981400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 853 | `0.2097` | `...ghbour_analysis.tex` \| 169 \| `0.2097` \| `10 & 48 & 50 & 16.692100 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 853 | `0.1142` | `...92100 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 854 | `0.2097` | `...& 50 & 16.692100 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 854 | `0.1142` | `...ghbour_analysis.tex` \| 169 \| `0.1142` \| `10 & 48 & 50 & 16.692100 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 855 | `0.2097` | `...ghbour_analysis.tex` \| 170 \| `0.2097` \| `10 & 49 & 59 & 23.732600 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 855 | `0.1142` | `...32600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 856 | `0.2097` | `...& 59 & 23.732600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 856 | `0.1142` | `...ghbour_analysis.tex` \| 170 \| `0.1142` \| `10 & 49 & 59 & 23.732600 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 857 | `0.2097` | `...ghbour_analysis.tex` \| 171 \| `0.2097` \| `10 & 51 & 53 & 2.109800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 857 | `0.1142` | `...09800 & 0.125000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 858 | `0.2097` | `... & 53 & 2.109800 & 0.125000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 858 | `0.1142` | `...ghbour_analysis.tex` \| 171 \| `0.1142` \| `10 & 51 & 53 & 2.109800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 859 | `0.2097` | `...ghbour_analysis.tex` \| 172 \| `0.2097` \| `10 & 60 & 58 & 3.707900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 859 | `0.1142` | `...07900 & 0.020000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 860 | `0.2097` | `... & 58 & 3.707900 & 0.020000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 860 | `0.1142` | `...ghbour_analysis.tex` \| 172 \| `0.1142` \| `10 & 60 & 58 & 3.707900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 861 | `0.2097` | `...ghbour_analysis.tex` \| 173 \| `0.2097` \| `11 & 1 & 5 & 4.573300 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 861 | `0.1142` | `...73300 & 0.004000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 862 | `0.2097` | `...1 & 5 & 4.573300 & 0.004000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 862 | `0.1142` | `...ghbour_analysis.tex` \| 173 \| `0.1142` \| `11 & 1 & 5 & 4.573300 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 863 | `0.2097` | `...ghbour_analysis.tex` \| 174 \| `0.2097` \| `11 & 3 & 36 & 3.770200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 863 | `0.1142` | `...70200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 864 | `0.2097` | `... & 36 & 3.770200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 864 | `0.1142` | `...ghbour_analysis.tex` \| 174 \| `0.1142` \| `11 & 3 & 36 & 3.770200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 865 | `0.2097` | `...ghbour_analysis.tex` \| 175 \| `0.2097` \| `11 & 16 & 13 & 2.775000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 865 | `0.1142` | `...75000 & 0.056000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 866 | `0.2097` | `... & 13 & 2.775000 & 0.056000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 866 | `0.1142` | `...ghbour_analysis.tex` \| 175 \| `0.1142` \| `11 & 16 & 13 & 2.775000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 867 | `0.2097` | `...ghbour_analysis.tex` \| 176 \| `0.2097` \| `11 & 18 & 2 & 1.842100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 867 | `0.1142` | `...42100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 868 | `0.2097` | `...8 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 868 | `0.1142` | `...ghbour_analysis.tex` \| 176 \| `0.1142` \| `11 & 18 & 2 & 1.842100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 869 | `0.2097` | `...ghbour_analysis.tex` \| 177 \| `0.2097` \| `11 & 23 & 9 & 3.107600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 869 | `0.1142` | `...07600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 870 | `0.2097` | `...3 & 9 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 870 | `0.1142` | `...ghbour_analysis.tex` \| 177 \| `0.1142` \| `11 & 23 & 9 & 3.107600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 871 | `0.2097` | `...ghbour_analysis.tex` \| 178 \| `0.2097` \| `11 & 24 & 32 & 4.244100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 871 | `0.1142` | `...44100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 872 | `0.2097` | `... & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 872 | `0.1142` | `...ghbour_analysis.tex` \| 178 \| `0.1142` \| `11 & 24 & 32 & 4.244100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 873 | `0.2097` | `...ghbour_analysis.tex` \| 179 \| `0.2097` \| `11 & 29 & 7 & 3.849800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 873 | `0.1142` | `...49800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 874 | `0.2097` | `...9 & 7 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 874 | `0.1142` | `...ghbour_analysis.tex` \| 179 \| `0.1142` \| `11 & 29 & 7 & 3.849800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 875 | `0.2097` | `...ghbour_analysis.tex` \| 180 \| `0.2097` \| `11 & 34 & 25 & 3.885000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 875 | `0.1142` | `...85000 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 876 | `0.2097` | `... & 25 & 3.885000 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 876 | `0.1142` | `...ghbour_analysis.tex` \| 180 \| `0.1142` \| `11 & 34 & 25 & 3.885000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 877 | `0.2097` | `...ghbour_analysis.tex` \| 181 \| `0.2097` \| `11 & 39 & 25 & 3.139000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 877 | `0.1142` | `...39000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 878 | `0.2097` | `... & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 878 | `0.1142` | `...ghbour_analysis.tex` \| 181 \| `0.1142` \| `11 & 39 & 25 & 3.139000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 879 | `0.2097` | `...ghbour_analysis.tex` \| 182 \| `0.2097` \| `11 & 40 & 8 & 2.013000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 879 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 880 | `0.2097` | `...0 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 880 | `0.1142` | `...ghbour_analysis.tex` \| 182 \| `0.1142` \| `11 & 40 & 8 & 2.013000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 881 | `0.2097` | `...ghbour_analysis.tex` \| 183 \| `0.2097` \| `11 & 44 & 8 & 2.039900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 881 | `0.1142` | `...39900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 882 | `0.2097` | `...4 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 882 | `0.1142` | `...ghbour_analysis.tex` \| 183 \| `0.1142` \| `11 & 44 & 8 & 2.039900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 883 | `0.2097` | `...ghbour_analysis.tex` \| 184 \| `0.2097` \| `11 & 48 & 46 & 6.468700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 883 | `0.1142` | `...68700 & 0.230000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 884 | `0.2097` | `... & 46 & 6.468700 & 0.230000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 884 | `0.1142` | `...ghbour_analysis.tex` \| 184 \| `0.1142` \| `11 & 48 & 46 & 6.468700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 885 | `0.2097` | `...ghbour_analysis.tex` \| 185 \| `0.2097` \| `11 & 50 & 47 & 10.874000 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 885 | `0.1142` | `...74000 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 886 | `0.2097` | `...& 47 & 10.874000 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 886 | `0.1142` | `...ghbour_analysis.tex` \| 185 \| `0.1142` \| `11 & 50 & 47 & 10.874000 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 887 | `0.2097` | `...ghbour_analysis.tex` \| 186 \| `0.2097` \| `11 & 55 & 51 & 2.184300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 887 | `0.1142` | `...84300 & 0.137500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 888 | `0.2097` | `... & 51 & 2.184300 & 0.137500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 888 | `0.1142` | `...ghbour_analysis.tex` \| 186 \| `0.1142` \| `11 & 55 & 51 & 2.184300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 889 | `0.2097` | `...ghbour_analysis.tex` \| 187 \| `0.2097` \| `11 & 56 & 54 & 4.740200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 889 | `0.1142` | `...40200 & 0.620000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 890 | `0.2097` | `... & 54 & 4.740200 & 0.620000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 890 | `0.1142` | `...ghbour_analysis.tex` \| 187 \| `0.1142` \| `11 & 56 & 54 & 4.740200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 891 | `0.2097` | `...ghbour_analysis.tex` \| 188 \| `0.2097` \| `12 & 7 & 29 & 3.849800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 891 | `0.1142` | `...49800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 892 | `0.2097` | `... & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 892 | `0.1142` | `...ghbour_analysis.tex` \| 188 \| `0.1142` \| `12 & 7 & 29 & 3.849800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 893 | `0.2097` | `...ghbour_analysis.tex` \| 189 \| `0.2097` \| `12 & 8 & 40 & 2.013000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 893 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 894 | `0.2097` | `... & 40 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 894 | `0.1142` | `...ghbour_analysis.tex` \| 189 \| `0.1142` \| `12 & 8 & 40 & 2.013000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 895 | `0.2097` | `...ghbour_analysis.tex` \| 190 \| `0.2097` \| `12 & 10 & 44 & 4.142300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 895 | `0.1142` | `...42300 & 0.034000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 896 | `0.2097` | `... & 44 & 4.142300 & 0.034000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 896 | `0.1142` | `...ghbour_analysis.tex` \| 190 \| `0.1142` \| `12 & 10 & 44 & 4.142300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 897 | `0.2097` | `...ghbour_analysis.tex` \| 191 \| `0.2097` \| `12 & 16 & 13 & 2.775000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 897 | `0.1142` | `...75000 & 0.026000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 898 | `0.2097` | `... & 13 & 2.775000 & 0.026000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 898 | `0.1142` | `...ghbour_analysis.tex` \| 191 \| `0.1142` \| `12 & 16 & 13 & 2.775000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 899 | `0.2097` | `...ghbour_analysis.tex` \| 192 \| `0.2097` \| `12 & 18 & 2 & 1.842100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 899 | `0.1142` | `...42100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 900 | `0.2097` | `...8 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 900 | `0.1142` | `...ghbour_analysis.tex` \| 192 \| `0.1142` \| `12 & 18 & 2 & 1.842100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 901 | `0.2097` | `...ghbour_analysis.tex` \| 193 \| `0.2097` \| `12 & 22 & 44 & 2.458200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 901 | `0.1142` | `...58200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 902 | `0.2097` | `... & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 902 | `0.1142` | `...ghbour_analysis.tex` \| 193 \| `0.1142` \| `12 & 22 & 44 & 2.458200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 903 | `0.2097` | `...ghbour_analysis.tex` \| 194 \| `0.2097` \| `12 & 28 & 20 & 4.273400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 903 | `0.1142` | `...73400 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 904 | `0.2097` | `... & 20 & 4.273400 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 904 | `0.1142` | `...ghbour_analysis.tex` \| 194 \| `0.1142` \| `12 & 28 & 20 & 4.273400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 905 | `0.2097` | `...ghbour_analysis.tex` \| 195 \| `0.2097` \| `12 & 32 & 5 & 4.460700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 905 | `0.1142` | `...60700 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 906 | `0.2097` | `...2 & 5 & 4.460700 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 906 | `0.1142` | `...ghbour_analysis.tex` \| 195 \| `0.1142` \| `12 & 32 & 5 & 4.460700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 907 | `0.2097` | `...ghbour_analysis.tex` \| 196 \| `0.2097` \| `12 & 33 & 26 & 3.446100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 907 | `0.1142` | `...46100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 908 | `0.2097` | `... & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 908 | `0.1142` | `...ghbour_analysis.tex` \| 196 \| `0.1142` \| `12 & 33 & 26 & 3.446100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 909 | `0.2097` | `...ghbour_analysis.tex` \| 197 \| `0.2097` \| `12 & 39 & 25 & 3.139000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 909 | `0.1142` | `...39000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 910 | `0.2097` | `... & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 910 | `0.1142` | `...ghbour_analysis.tex` \| 197 \| `0.1142` \| `12 & 39 & 25 & 3.139000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 911 | `0.2097` | `...ghbour_analysis.tex` \| 198 \| `0.2097` \| `12 & 42 & 25 & 5.844200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 911 | `0.1142` | `...44200 & 0.115000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 912 | `0.2097` | `... & 25 & 5.844200 & 0.115000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 912 | `0.1142` | `...ghbour_analysis.tex` \| 198 \| `0.1142` \| `12 & 42 & 25 & 5.844200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 913 | `64%` | `...ghbour_analysis.tex` \| 199 \| `64%` \| `12 & 46 & 49 & 4.846400 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 913 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 913 | `0.2097` | `... & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 913 | `0.1142` | `...46400 & 1.000000 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 914 | `64%` | `...0.2097` \| `12 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 914 | `0.2097` | `...ghbour_analysis.tex` \| 199 \| `0.2097` \| `12 & 46 & 49 & 4.846400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 914 | `0.1142` | `...46400 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 915 | `64%` | `...0.1142` \| `12 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 915 | `0.2097` | `... & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 915 | `0.1142` | `...ghbour_analysis.tex` \| 199 \| `0.1142` \| `12 & 46 & 49 & 4.846400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 916 | `0.2097` | `...ghbour_analysis.tex` \| 200 \| `0.2097` \| `12 & 50 & 48 & 16.692100 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 916 | `0.1142` | `...92100 & 0.997500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 917 | `0.2097` | `...& 48 & 16.692100 & 0.997500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 917 | `0.1142` | `...ghbour_analysis.tex` \| 200 \| `0.1142` \| `12 & 50 & 48 & 16.692100 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 918 | `0.2097` | `...ghbour_analysis.tex` \| 201 \| `0.2097` \| `12 & 52 & 54 & 3.912000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 918 | `0.1142` | `...12000 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 919 | `0.2097` | `... & 54 & 3.912000 & 0.002500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 919 | `0.1142` | `...ghbour_analysis.tex` \| 201 \| `0.1142` \| `12 & 52 & 54 & 3.912000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 920 | `0.2097` | `...ghbour_analysis.tex` \| 202 \| `0.2097` \| `12 & 56 & 54 & 4.740200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 920 | `0.1142` | `...40200 & 0.217500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 921 | `0.2097` | `... & 54 & 4.740200 & 0.217500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 921 | `0.1142` | `...ghbour_analysis.tex` \| 202 \| `0.1142` \| `12 & 56 & 54 & 4.740200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 922 | `0.2097` | `...ghbour_analysis.tex` \| 203 \| `0.2097` \| `13 & 2 & 3 & 4.787800 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 922 | `0.1142` | `...87800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 923 | `0.2097` | `...2 & 3 & 4.787800 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 923 | `0.1142` | `...ghbour_analysis.tex` \| 203 \| `0.1142` \| `13 & 2 & 3 & 4.787800 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 924 | `0.2097` | `...ghbour_analysis.tex` \| 204 \| `0.2097` \| `13 & 4 & 36 & 2.899800 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 924 | `0.1142` | `...99800 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 925 | `0.2097` | `... & 36 & 2.899800 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 925 | `0.1142` | `...ghbour_analysis.tex` \| 204 \| `0.1142` \| `13 & 4 & 36 & 2.899800 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 926 | `0.2097` | `...ghbour_analysis.tex` \| 205 \| `0.2097` \| `13 & 14 & 19 & 2.813000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 926 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 927 | `0.2097` | `... & 19 & 2.813000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 927 | `0.1142` | `...ghbour_analysis.tex` \| 205 \| `0.1142` \| `13 & 14 & 19 & 2.813000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 928 | `0.2097` | `...ghbour_analysis.tex` \| 206 \| `0.2097` \| `13 & 21 & 32 & 5.441300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 928 | `0.1142` | `...41300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 929 | `0.2097` | `... & 32 & 5.441300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 929 | `0.1142` | `...ghbour_analysis.tex` \| 206 \| `0.1142` \| `13 & 21 & 32 & 5.441300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 930 | `0.2097` | `...ghbour_analysis.tex` \| 207 \| `0.2097` \| `13 & 22 & 44 & 2.458200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 930 | `0.1142` | `...58200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 931 | `0.2097` | `... & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 931 | `0.1142` | `...ghbour_analysis.tex` \| 207 \| `0.1142` \| `13 & 22 & 44 & 2.458200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 932 | `0.2097` | `...ghbour_analysis.tex` \| 208 \| `0.2097` \| `13 & 26 & 3 & 4.974300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 932 | `0.1142` | `...74300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 933 | `0.2097` | `...6 & 3 & 4.974300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 933 | `0.1142` | `...ghbour_analysis.tex` \| 208 \| `0.1142` \| `13 & 26 & 3 & 4.974300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 934 | `0.2097` | `...ghbour_analysis.tex` \| 209 \| `0.2097` \| `13 & 27 & 36 & 3.866500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 934 | `0.1142` | `...66500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 935 | `0.2097` | `... & 36 & 3.866500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 935 | `0.1142` | `...ghbour_analysis.tex` \| 209 \| `0.1142` \| `13 & 27 & 36 & 3.866500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 936 | `0.2097` | `...ghbour_analysis.tex` \| 210 \| `0.2097` \| `13 & 33 & 32 & 4.738100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 936 | `0.1142` | `...38100 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 937 | `0.2097` | `... & 32 & 4.738100 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 937 | `0.1142` | `...ghbour_analysis.tex` \| 210 \| `0.1142` \| `13 & 33 & 32 & 4.738100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 938 | `0.2097` | `...ghbour_analysis.tex` \| 211 \| `0.2097` \| `13 & 37 & 36 & 4.303400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 938 | `0.1142` | `...03400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 939 | `0.2097` | `... & 36 & 4.303400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 939 | `0.1142` | `...ghbour_analysis.tex` \| 211 \| `0.1142` \| `13 & 37 & 36 & 4.303400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 940 | `0.2097` | `...ghbour_analysis.tex` \| 212 \| `0.2097` \| `13 & 40 & 8 & 2.013000 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 940 | `0.1142` | `...13000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 941 | `0.2097` | `...0 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 941 | `0.1142` | `...ghbour_analysis.tex` \| 212 \| `0.1142` \| `13 & 40 & 8 & 2.013000 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 942 | `0.2097` | `...ghbour_analysis.tex` \| 213 \| `0.2097` \| `13 & 43 & 6 & 3.376900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 942 | `0.1142` | `...76900 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 943 | `0.2097` | `...3 & 6 & 3.376900 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 943 | `0.1142` | `...ghbour_analysis.tex` \| 213 \| `0.1142` \| `13 & 43 & 6 & 3.376900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 944 | `0.2097` | `...ghbour_analysis.tex` \| 214 \| `0.2097` \| `13 & 46 & 48 & 6.468700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 944 | `0.1142` | `...68700 & 0.420000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 945 | `0.2097` | `... & 48 & 6.468700 & 0.420000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 945 | `0.1142` | `...ghbour_analysis.tex` \| 214 \| `0.1142` \| `13 & 46 & 48 & 6.468700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 946 | `0.2097` | `...ghbour_analysis.tex` \| 215 \| `0.2097` \| `13 & 54 & 52 & 3.912000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 946 | `0.1142` | `...12000 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 947 | `0.2097` | `... & 52 & 3.912000 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 947 | `0.1142` | `...ghbour_analysis.tex` \| 215 \| `0.1142` \| `13 & 54 & 52 & 3.912000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 948 | `0.2097` | `...ghbour_analysis.tex` \| 216 \| `0.2097` \| `13 & 56 & 57 & 4.186200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 948 | `0.1142` | `...86200 & 0.155000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 949 | `0.2097` | `... & 57 & 4.186200 & 0.155000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 949 | `0.1142` | `...ghbour_analysis.tex` \| 216 \| `0.1142` \| `13 & 56 & 57 & 4.186200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 950 | `0.2097` | `...ghbour_analysis.tex` \| 217 \| `0.2097` \| `13 & 58 & 60 & 3.707900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 950 | `0.1142` | `...07900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 951 | `0.2097` | `... & 60 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 951 | `0.1142` | `...ghbour_analysis.tex` \| 217 \| `0.1142` \| `13 & 58 & 60 & 3.707900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 952 | `0.2097` | `...ghbour_analysis.tex` \| 218 \| `0.2097` \| `14 & 11 & 19 & 2.615600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 952 | `0.1142` | `...15600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 953 | `0.2097` | `... & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 953 | `0.1142` | `...ghbour_analysis.tex` \| 218 \| `0.1142` \| `14 & 11 & 19 & 2.615600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 954 | `0.2097` | `...ghbour_analysis.tex` \| 219 \| `0.2097` \| `14 & 13 & 44 & 4.424700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 954 | `0.1142` | `...24700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 955 | `0.2097` | `... & 44 & 4.424700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 955 | `0.1142` | `...ghbour_analysis.tex` \| 219 \| `0.1142` \| `14 & 13 & 44 & 4.424700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 956 | `0.2097` | `...ghbour_analysis.tex` \| 220 \| `0.2097` \| `14 & 16 & 14 & 3.830000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 956 | `0.1142` | `...30000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 957 | `0.2097` | `... & 14 & 3.830000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 957 | `0.1142` | `...ghbour_analysis.tex` \| 220 \| `0.1142` \| `14 & 16 & 14 & 3.830000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 958 | `0.2097` | `...ghbour_analysis.tex` \| 221 \| `0.2097` \| `14 & 17 & 6 & 5.208400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 958 | `0.1142` | `...08400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 959 | `0.2097` | `...7 & 6 & 5.208400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 959 | `0.1142` | `...ghbour_analysis.tex` \| 221 \| `0.1142` \| `14 & 17 & 6 & 5.208400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 960 | `0.2097` | `...ghbour_analysis.tex` \| 222 \| `0.2097` \| `14 & 24 & 32 & 4.244100 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 960 | `0.1142` | `...44100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 961 | `0.2097` | `... & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 961 | `0.1142` | `...ghbour_analysis.tex` \| 222 \| `0.1142` \| `14 & 24 & 32 & 4.244100 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 962 | `0.2097` | `...ghbour_analysis.tex` \| 223 \| `0.2097` \| `14 & 25 & 39 & 3.139000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 962 | `0.1142` | `...39000 & 0.012000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 963 | `0.2097` | `... & 39 & 3.139000 & 0.012000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 963 | `0.1142` | `...ghbour_analysis.tex` \| 223 \| `0.1142` \| `14 & 25 & 39 & 3.139000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 964 | `0.2097` | `...ghbour_analysis.tex` \| 224 \| `0.2097` \| `14 & 27 & 7 & 3.852200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 964 | `0.1142` | `...52200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 965 | `0.2097` | `...7 & 7 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 965 | `0.1142` | `...ghbour_analysis.tex` \| 224 \| `0.1142` \| `14 & 27 & 7 & 3.852200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 966 | `0.2097` | `...ghbour_analysis.tex` \| 225 \| `0.2097` \| `14 & 33 & 21 & 4.692500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 966 | `0.1142` | `...92500 & 0.017500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 967 | `0.2097` | `... & 21 & 4.692500 & 0.017500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 967 | `0.1142` | `...ghbour_analysis.tex` \| 225 \| `0.1142` \| `14 & 33 & 21 & 4.692500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 968 | `0.2097` | `...ghbour_analysis.tex` \| 226 \| `0.2097` \| `14 & 38 & 39 & 6.796700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 968 | `0.1142` | `...96700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 969 | `0.2097` | `... & 39 & 6.796700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 969 | `0.1142` | `...ghbour_analysis.tex` \| 226 \| `0.1142` \| `14 & 38 & 39 & 6.796700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 970 | `0.2097` | `...ghbour_analysis.tex` \| 227 \| `0.2097` \| `14 & 40 & 44 & 2.738200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 970 | `0.1142` | `...38200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 971 | `0.2097` | `... & 44 & 2.738200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 971 | `0.1142` | `...ghbour_analysis.tex` \| 227 \| `0.1142` \| `14 & 40 & 44 & 2.738200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 972 | `0.2097` | `...ghbour_analysis.tex` \| 228 \| `0.2097` \| `14 & 42 & 19 & 5.495600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 972 | `0.1142` | `...95600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 973 | `0.2097` | `... & 19 & 5.495600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 973 | `0.1142` | `...ghbour_analysis.tex` \| 228 \| `0.1142` \| `14 & 42 & 19 & 5.495600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 974 | `64%` | `...ghbour_analysis.tex` \| 229 \| `64%` \| `14 & 46 & 49 & 4.846400 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 974 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 974 | `0.2097` | `... & 49 & 4.846400 & 0.972500 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 974 | `0.1142` | `...46400 & 0.972500 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 975 | `64%` | `...0.2097` \| `14 & 46 & 49 & 4.846400 & 0.972500 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 975 | `0.2097` | `...ghbour_analysis.tex` \| 229 \| `0.2097` \| `14 & 46 & 49 & 4.846400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 975 | `0.1142` | `...46400 & 0.972500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 976 | `64%` | `...0.1142` \| `14 & 46 & 49 & 4.846400 & 0.972500 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 976 | `0.2097` | `... & 49 & 4.846400 & 0.972500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 976 | `0.1142` | `...ghbour_analysis.tex` \| 229 \| `0.1142` \| `14 & 46 & 49 & 4.846400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 977 | `0.2097` | `...ghbour_analysis.tex` \| 230 \| `0.2097` \| `14 & 48 & 49 & 9.769000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 977 | `0.1142` | `...69000 & 0.870000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 978 | `0.2097` | `... & 49 & 9.769000 & 0.870000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 978 | `0.1142` | `...ghbour_analysis.tex` \| 230 \| `0.1142` \| `14 & 48 & 49 & 9.769000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 979 | `0.2097` | `...ghbour_analysis.tex` \| 231 \| `0.2097` \| `14 & 52 & 54 & 3.912000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 979 | `0.1142` | `...12000 & 0.030000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 980 | `0.2097` | `... & 54 & 3.912000 & 0.030000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 980 | `0.1142` | `...ghbour_analysis.tex` \| 231 \| `0.1142` \| `14 & 52 & 54 & 3.912000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 981 | `0.2097` | `...ghbour_analysis.tex` \| 232 \| `0.2097` \| `14 & 60 & 58 & 3.707900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 981 | `0.1142` | `...07900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 982 | `0.2097` | `... & 58 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 982 | `0.1142` | `...ghbour_analysis.tex` \| 232 \| `0.1142` \| `14 & 60 & 58 & 3.707900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 983 | `0.2097` | `...ghbour_analysis.tex` \| 233 \| `0.2097` \| `15 & 1 & 5 & 4.573300 & 0...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 983 | `0.1142` | `...73300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 984 | `0.2097` | `...1 & 5 & 4.573300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 984 | `0.1142` | `...ghbour_analysis.tex` \| 233 \| `0.1142` \| `15 & 1 & 5 & 4.573300 & 0...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 985 | `0.2097` | `...ghbour_analysis.tex` \| 234 \| `0.2097` \| `15 & 10 & 39 & 3.431400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 985 | `0.1142` | `...31400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 986 | `0.2097` | `... & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 986 | `0.1142` | `...ghbour_analysis.tex` \| 234 \| `0.1142` \| `15 & 10 & 39 & 3.431400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 987 | `0.2097` | `...ghbour_analysis.tex` \| 235 \| `0.2097` \| `15 & 15 & 20 & 1.805000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 987 | `0.1142` | `...05000 & 0.098000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 988 | `0.2097` | `... & 20 & 1.805000 & 0.098000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 988 | `0.1142` | `...ghbour_analysis.tex` \| 235 \| `0.1142` \| `15 & 15 & 20 & 1.805000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 989 | `0.2097` | `...ghbour_analysis.tex` \| 236 \| `0.2097` \| `15 & 16 & 13 & 2.775000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 989 | `0.1142` | `...75000 & 0.046000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 990 | `0.2097` | `... & 13 & 2.775000 & 0.046000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 990 | `0.1142` | `...ghbour_analysis.tex` \| 236 \| `0.1142` \| `15 & 16 & 13 & 2.775000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 991 | `0.2097` | `...ghbour_analysis.tex` \| 237 \| `0.2097` \| `15 & 17 & 30 & 3.523900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 991 | `0.1142` | `...23900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 992 | `0.2097` | `... & 30 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 992 | `0.1142` | `...ghbour_analysis.tex` \| 237 \| `0.1142` \| `15 & 17 & 30 & 3.523900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 993 | `0.2097` | `...ghbour_analysis.tex` \| 238 \| `0.2097` \| `15 & 23 & 28 & 5.042700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 993 | `0.1142` | `...42700 & 0.614000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 994 | `0.2097` | `... & 28 & 5.042700 & 0.614000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 994 | `0.1142` | `...ghbour_analysis.tex` \| 238 \| `0.1142` \| `15 & 23 & 28 & 5.042700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 995 | `0.2097` | `...ghbour_analysis.tex` \| 239 \| `0.2097` \| `15 & 26 & 27 & 2.754600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 995 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 996 | `0.2097` | `... & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 996 | `0.1142` | `...ghbour_analysis.tex` \| 239 \| `0.1142` \| `15 & 26 & 27 & 2.754600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 997 | `0.2097` | `...ghbour_analysis.tex` \| 240 \| `0.2097` \| `15 & 32 & 5 & 4.460700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 997 | `0.1142` | `...60700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 998 | `0.2097` | `...2 & 5 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 998 | `0.1142` | `...ghbour_analysis.tex` \| 240 \| `0.1142` \| `15 & 32 & 5 & 4.460700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 999 | `0.2097` | `...ghbour_analysis.tex` \| 241 \| `0.2097` \| `15 & 33 & 27 & 4.317400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 999 | `0.1142` | `...17400 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1000 | `0.2097` | `... & 27 & 4.317400 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1000 | `0.1142` | `...ghbour_analysis.tex` \| 241 \| `0.1142` \| `15 & 33 & 27 & 4.317400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1001 | `0.2097` | `...ghbour_analysis.tex` \| 242 \| `0.2097` \| `15 & 38 & 39 & 6.796700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1001 | `0.1142` | `...96700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1002 | `0.2097` | `... & 39 & 6.796700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1002 | `0.1142` | `...ghbour_analysis.tex` \| 242 \| `0.1142` \| `15 & 38 & 39 & 6.796700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1003 | `0.2097` | `...ghbour_analysis.tex` \| 243 \| `0.2097` \| `15 & 43 & 6 & 3.376900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1003 | `0.1142` | `...76900 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1004 | `0.2097` | `...3 & 6 & 3.376900 & 0.005000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1004 | `0.1142` | `...ghbour_analysis.tex` \| 243 \| `0.1142` \| `15 & 43 & 6 & 3.376900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1005 | `0.2097` | `...ghbour_analysis.tex` \| 244 \| `0.2097` \| `15 & 48 & 46 & 6.468700 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1005 | `0.1142` | `...68700 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1006 | `0.2097` | `... & 46 & 6.468700 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1006 | `0.1142` | `...ghbour_analysis.tex` \| 244 \| `0.1142` \| `15 & 48 & 46 & 6.468700 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1007 | `64%` | `...ghbour_analysis.tex` \| 245 \| `64%` \| `15 & 49 & 46 & 4.846400 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1007 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1007 | `0.2097` | `... & 46 & 4.846400 & 0.992500 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1007 | `0.1142` | `...46400 & 0.992500 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1008 | `64%` | `...0.2097` \| `15 & 49 & 46 & 4.846400 & 0.992500 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1008 | `0.2097` | `...ghbour_analysis.tex` \| 245 \| `0.2097` \| `15 & 49 & 46 & 4.846400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1008 | `0.1142` | `...46400 & 0.992500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1009 | `64%` | `...0.1142` \| `15 & 49 & 46 & 4.846400 & 0.992500 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1009 | `0.2097` | `... & 46 & 4.846400 & 0.992500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1009 | `0.1142` | `...ghbour_analysis.tex` \| 245 \| `0.1142` \| `15 & 49 & 46 & 4.846400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1010 | `0.2097` | `...ghbour_analysis.tex` \| 246 \| `0.2097` \| `15 & 55 & 51 & 2.184300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1010 | `0.1142` | `...84300 & 0.302500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1011 | `0.2097` | `... & 51 & 2.184300 & 0.302500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1011 | `0.1142` | `...ghbour_analysis.tex` \| 246 \| `0.1142` \| `15 & 55 & 51 & 2.184300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1012 | `0.2097` | `...ghbour_analysis.tex` \| 247 \| `0.2097` \| `15 & 59 & 57 & 4.558800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1012 | `0.1142` | `...58800 & 0.327500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1013 | `0.2097` | `... & 57 & 4.558800 & 0.327500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1013 | `0.1142` | `...ghbour_analysis.tex` \| 247 \| `0.1142` \| `15 & 59 & 57 & 4.558800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1014 | `0.2097` | `...ghbour_analysis.tex` \| 248 \| `0.2097` \| `16 & 2 & 21 & 2.894300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1014 | `0.1142` | `...94300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1015 | `0.2097` | `... & 21 & 2.894300 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1015 | `0.1142` | `...ghbour_analysis.tex` \| 248 \| `0.1142` \| `16 & 2 & 21 & 2.894300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1016 | `0.2097` | `...ghbour_analysis.tex` \| 249 \| `0.2097` \| `16 & 5 & 32 & 4.460700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1016 | `0.1142` | `...60700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1017 | `0.2097` | `... & 32 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1017 | `0.1142` | `...ghbour_analysis.tex` \| 249 \| `0.1142` \| `16 & 5 & 32 & 4.460700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1018 | `0.2097` | `...ghbour_analysis.tex` \| 250 \| `0.2097` \| `16 & 7 & 27 & 3.852200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1018 | `0.1142` | `...52200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1019 | `0.2097` | `... & 27 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1019 | `0.1142` | `...ghbour_analysis.tex` \| 250 \| `0.1142` \| `16 & 7 & 27 & 3.852200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1020 | `0.2097` | `...ghbour_analysis.tex` \| 251 \| `0.2097` \| `16 & 10 & 44 & 4.142300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1020 | `0.1142` | `...42300 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1021 | `0.2097` | `... & 44 & 4.142300 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1021 | `0.1142` | `...ghbour_analysis.tex` \| 251 \| `0.1142` \| `16 & 10 & 44 & 4.142300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1022 | `0.2097` | `...ghbour_analysis.tex` \| 252 \| `0.2097` \| `16 & 12 & 32 & 7.532400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1022 | `0.1142` | `...32400 & 0.008000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1023 | `0.2097` | `... & 32 & 7.532400 & 0.008000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1023 | `0.1142` | `...ghbour_analysis.tex` \| 252 \| `0.1142` \| `16 & 12 & 32 & 7.532400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1024 | `0.2097` | `...ghbour_analysis.tex` \| 253 \| `0.2097` \| `16 & 15 & 20 & 1.805000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1024 | `0.1142` | `...05000 & 0.154000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1025 | `0.2097` | `... & 20 & 1.805000 & 0.154000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1025 | `0.1142` | `...ghbour_analysis.tex` \| 253 \| `0.1142` \| `16 & 15 & 20 & 1.805000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1026 | `0.2097` | `...ghbour_analysis.tex` \| 254 \| `0.2097` \| `16 & 22 & 44 & 2.458200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1026 | `0.1142` | `...58200 & 0.172000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1027 | `0.2097` | `... & 44 & 2.458200 & 0.172000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1027 | `0.1142` | `...ghbour_analysis.tex` \| 254 \| `0.1142` \| `16 & 22 & 44 & 2.458200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1028 | `0.2097` | `...ghbour_analysis.tex` \| 255 \| `0.2097` \| `16 & 34 & 40 & 3.452600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1028 | `0.1142` | `...52600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1029 | `0.2097` | `... & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1029 | `0.1142` | `...ghbour_analysis.tex` \| 255 \| `0.1142` \| `16 & 34 & 40 & 3.452600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1030 | `0.2097` | `...ghbour_analysis.tex` \| 256 \| `0.2097` \| `16 & 37 & 4 & 4.053400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1030 | `0.1142` | `...53400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1031 | `0.2097` | `...7 & 4 & 4.053400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1031 | `0.1142` | `...ghbour_analysis.tex` \| 256 \| `0.1142` \| `16 & 37 & 4 & 4.053400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1032 | `0.2097` | `...ghbour_analysis.tex` \| 257 \| `0.2097` \| `16 & 39 & 11 & 3.408200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1032 | `0.1142` | `...08200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1033 | `0.2097` | `... & 11 & 3.408200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1033 | `0.1142` | `...ghbour_analysis.tex` \| 257 \| `0.1142` \| `16 & 39 & 11 & 3.408200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1034 | `0.2097` | `...ghbour_analysis.tex` \| 258 \| `0.2097` \| `16 & 42 & 11 & 4.981400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1034 | `0.1142` | `...81400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1035 | `0.2097` | `... & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1035 | `0.1142` | `...ghbour_analysis.tex` \| 258 \| `0.1142` \| `16 & 42 & 11 & 4.981400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1036 | `0.2097` | `...ghbour_analysis.tex` \| 259 \| `0.2097` \| `16 & 46 & 50 & 21.668300 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1036 | `0.1142` | `...68300 & 0.057500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1037 | `0.2097` | `...& 50 & 21.668300 & 0.057500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1037 | `0.1142` | `...ghbour_analysis.tex` \| 259 \| `0.1142` \| `16 & 46 & 50 & 21.668300 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1038 | `0.2097` | `...ghbour_analysis.tex` \| 260 \| `0.2097` \| `16 & 49 & 59 & 23.732600 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1038 | `0.1142` | `...32600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1039 | `0.2097` | `...& 59 & 23.732600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1039 | `0.1142` | `...ghbour_analysis.tex` \| 260 \| `0.1142` \| `16 & 49 & 59 & 23.732600 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1040 | `0.2097` | `...ghbour_analysis.tex` \| 261 \| `0.2097` \| `16 & 52 & 54 & 3.912000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1040 | `0.1142` | `...12000 & 0.077500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1041 | `0.2097` | `... & 54 & 3.912000 & 0.077500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1041 | `0.1142` | `...ghbour_analysis.tex` \| 261 \| `0.1142` \| `16 & 52 & 54 & 3.912000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1042 | `0.2097` | `...ghbour_analysis.tex` \| 262 \| `0.2097` \| `16 & 55 & 51 & 2.184300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1042 | `0.1142` | `...84300 & 0.267500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1043 | `0.2097` | `... & 51 & 2.184300 & 0.267500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1043 | `0.1142` | `...ghbour_analysis.tex` \| 262 \| `0.1142` \| `16 & 55 & 51 & 2.184300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1044 | `0.2097` | `...ghbour_analysis.tex` \| 263 \| `0.2097` \| `17 & 5 & 32 & 4.460700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1044 | `0.1142` | `...60700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1045 | `0.2097` | `... & 32 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1045 | `0.1142` | `...ghbour_analysis.tex` \| 263 \| `0.1142` \| `17 & 5 & 32 & 4.460700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1046 | `64%` | `...ab_neighbour_analysis.tex` \| 264 \| `0.2097` \| `17 & 9 & 23 & 3...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1046 | `0.2097` | `...ghbour_analysis.tex` \| 264 \| `0.2097` \| `17 & 9 & 23 & 3.107600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1046 | `0.1142` | `...07600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1047 | `64%` | `...ab_neighbour_analysis.tex` \| 264 \| `0.1142` \| `17 & 9 & 23 & 3...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1047 | `0.2097` | `... & 23 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1047 | `0.1142` | `...ghbour_analysis.tex` \| 264 \| `0.1142` \| `17 & 9 & 23 & 3.107600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1048 | `0.2097` | `...ghbour_analysis.tex` \| 265 \| `0.2097` \| `17 & 12 & 24 & 6.624900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1048 | `0.1142` | `...24900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1049 | `0.2097` | `... & 24 & 6.624900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1049 | `0.1142` | `...ghbour_analysis.tex` \| 265 \| `0.1142` \| `17 & 12 & 24 & 6.624900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1050 | `0.2097` | `...ghbour_analysis.tex` \| 266 \| `0.2097` \| `17 & 14 & 20 & 2.699200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1050 | `0.1142` | `...99200 & 0.004000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1051 | `0.2097` | `... & 20 & 2.699200 & 0.004000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1051 | `0.1142` | `...ghbour_analysis.tex` \| 266 \| `0.1142` \| `17 & 14 & 20 & 2.699200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1052 | `0.2097` | `...ghbour_analysis.tex` \| 267 \| `0.2097` \| `17 & 21 & 2 & 2.894300 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1052 | `0.1142` | `...94300 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1053 | `0.2097` | `...1 & 2 & 2.894300 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1053 | `0.1142` | `...ghbour_analysis.tex` \| 267 \| `0.1142` \| `17 & 21 & 2 & 2.894300 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1054 | `0.2097` | `...ghbour_analysis.tex` \| 268 \| `0.2097` \| `17 & 22 & 8 & 3.154100 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1054 | `0.1142` | `...54100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1055 | `0.2097` | `...2 & 8 & 3.154100 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1055 | `0.1142` | `...ghbour_analysis.tex` \| 268 \| `0.1142` \| `17 & 22 & 8 & 3.154100 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1056 | `0.2097` | `...ghbour_analysis.tex` \| 269 \| `0.2097` \| `17 & 30 & 40 & 3.870000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1056 | `0.1142` | `...70000 & 0.068000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1057 | `0.2097` | `... & 40 & 3.870000 & 0.068000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1057 | `0.1142` | `...ghbour_analysis.tex` \| 269 \| `0.1142` \| `17 & 30 & 40 & 3.870000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1058 | `0.2097` | `...ghbour_analysis.tex` \| 270 \| `0.2097` \| `17 & 34 & 40 & 3.452600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1058 | `0.1142` | `...52600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1059 | `0.2097` | `... & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1059 | `0.1142` | `...ghbour_analysis.tex` \| 270 \| `0.1142` \| `17 & 34 & 40 & 3.452600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1060 | `0.2097` | `...ghbour_analysis.tex` \| 271 \| `0.2097` \| `17 & 37 & 4 & 4.053400 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1060 | `0.1142` | `...53400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1061 | `0.2097` | `...7 & 4 & 4.053400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1061 | `0.1142` | `...ghbour_analysis.tex` \| 271 \| `0.1142` \| `17 & 37 & 4 & 4.053400 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1062 | `0.2097` | `...ghbour_analysis.tex` \| 272 \| `0.2097` \| `17 & 39 & 25 & 3.139000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1062 | `0.1142` | `...39000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1063 | `0.2097` | `... & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1063 | `0.1142` | `...ghbour_analysis.tex` \| 272 \| `0.1142` \| `17 & 39 & 25 & 3.139000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1064 | `0.2097` | `...ghbour_analysis.tex` \| 273 \| `0.2097` \| `17 & 44 & 8 & 2.039900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1064 | `0.1142` | `...39900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1065 | `0.2097` | `...4 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1065 | `0.1142` | `...ghbour_analysis.tex` \| 273 \| `0.1142` \| `17 & 44 & 8 & 2.039900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1066 | `0.2097` | `...ghbour_analysis.tex` \| 274 \| `0.2097` \| `17 & 49 & 48 & 9.769000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1066 | `0.1142` | `...69000 & 0.895000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1067 | `0.2097` | `... & 48 & 9.769000 & 0.895000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1067 | `0.1142` | `...ghbour_analysis.tex` \| 274 \| `0.1142` \| `17 & 49 & 48 & 9.769000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1068 | `0.2097` | `...ghbour_analysis.tex` \| 275 \| `0.2097` \| `17 & 51 & 53 & 2.109800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1068 | `0.1142` | `...09800 & 0.117500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1069 | `0.2097` | `... & 53 & 2.109800 & 0.117500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1069 | `0.1142` | `...ghbour_analysis.tex` \| 275 \| `0.1142` \| `17 & 51 & 53 & 2.109800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1070 | `0.2097` | `...ghbour_analysis.tex` \| 276 \| `0.2097` \| `17 & 52 & 54 & 3.912000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1070 | `0.1142` | `...12000 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1071 | `0.2097` | `... & 54 & 3.912000 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1071 | `0.1142` | `...ghbour_analysis.tex` \| 276 \| `0.1142` \| `17 & 52 & 54 & 3.912000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1072 | `0.2097` | `...ghbour_analysis.tex` \| 277 \| `0.2097` \| `17 & 58 & 60 & 3.707900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1072 | `0.1142` | `...07900 & 0.107500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1073 | `0.2097` | `... & 60 & 3.707900 & 0.107500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1073 | `0.1142` | `...ghbour_analysis.tex` \| 277 \| `0.1142` \| `17 & 58 & 60 & 3.707900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1074 | `0.2097` | `...ghbour_analysis.tex` \| 278 \| `0.2097` \| `18 & 9 & 19 & 5.023500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1074 | `0.1142` | `...23500 & 0.082000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1075 | `0.2097` | `... & 19 & 5.023500 & 0.082000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1075 | `0.1142` | `...ghbour_analysis.tex` \| 278 \| `0.1142` \| `18 & 9 & 19 & 5.023500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1076 | `0.2097` | `...ghbour_analysis.tex` \| 279 \| `0.2097` \| `18 & 10 & 19 & 4.492500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1076 | `0.1142` | `...92500 & 0.062000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1077 | `0.2097` | `... & 19 & 4.492500 & 0.062000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1077 | `0.1142` | `...ghbour_analysis.tex` \| 279 \| `0.1142` \| `18 & 10 & 19 & 4.492500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1078 | `0.2097` | `...ghbour_analysis.tex` \| 280 \| `0.2097` \| `18 & 14 & 15 & 2.405800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1078 | `0.1142` | `...05800 & 0.038000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1079 | `0.2097` | `... & 15 & 2.405800 & 0.038000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1079 | `0.1142` | `...ghbour_analysis.tex` \| 280 \| `0.1142` \| `18 & 14 & 15 & 2.405800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1080 | `0.2097` | `...ghbour_analysis.tex` \| 281 \| `0.2097` \| `18 & 20 & 15 & 1.805000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1080 | `0.1142` | `...05000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1081 | `0.2097` | `... & 15 & 1.805000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1081 | `0.1142` | `...ghbour_analysis.tex` \| 281 \| `0.1142` \| `18 & 20 & 15 & 1.805000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1082 | `0.2097` | `...ghbour_analysis.tex` \| 282 \| `0.2097` \| `18 & 22 & 4 & 3.992200 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1082 | `0.1142` | `...92200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1083 | `0.2097` | `...2 & 4 & 3.992200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1083 | `0.1142` | `...ghbour_analysis.tex` \| 282 \| `0.1142` \| `18 & 22 & 4 & 3.992200 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1084 | `0.2097` | `...ghbour_analysis.tex` \| 283 \| `0.2097` \| `18 & 26 & 27 & 2.754600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1084 | `0.1142` | `...54600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1085 | `0.2097` | `... & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1085 | `0.1142` | `...ghbour_analysis.tex` \| 283 \| `0.1142` \| `18 & 26 & 27 & 2.754600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1086 | `0.2097` | `...ghbour_analysis.tex` \| 284 \| `0.2097` \| `18 & 28 & 19 & 3.273900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1086 | `0.1142` | `...73900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1087 | `0.2097` | `... & 19 & 3.273900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1087 | `0.1142` | `...ghbour_analysis.tex` \| 284 \| `0.1142` \| `18 & 28 & 19 & 3.273900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1088 | `0.2097` | `...ghbour_analysis.tex` \| 285 \| `0.2097` \| `18 & 31 & 1 & 6.432600 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1088 | `0.1142` | `...32600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1089 | `0.2097` | `...1 & 1 & 6.432600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1089 | `0.1142` | `...ghbour_analysis.tex` \| 285 \| `0.1142` \| `18 & 31 & 1 & 6.432600 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1090 | `0.2097` | `...ghbour_analysis.tex` \| 286 \| `0.2097` \| `18 & 35 & 34 & 4.521200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1090 | `0.1142` | `...21200 & 0.265000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1091 | `0.2097` | `... & 34 & 4.521200 & 0.265000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1091 | `0.1142` | `...ghbour_analysis.tex` \| 286 \| `0.1142` \| `18 & 35 & 34 & 4.521200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1092 | `0.2097` | `...ghbour_analysis.tex` \| 287 \| `0.2097` \| `18 & 39 & 19 & 3.658200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1092 | `0.1142` | `...58200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1093 | `0.2097` | `... & 19 & 3.658200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1093 | `0.1142` | `...ghbour_analysis.tex` \| 287 \| `0.1142` \| `18 & 39 & 19 & 3.658200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1094 | `0.2097` | `...ghbour_analysis.tex` \| 288 \| `0.2097` \| `18 & 42 & 19 & 5.495600 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1094 | `0.1142` | `...95600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1095 | `0.2097` | `... & 19 & 5.495600 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1095 | `0.1142` | `...ghbour_analysis.tex` \| 288 \| `0.1142` \| `18 & 42 & 19 & 5.495600 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1096 | `64%` | `...ghbour_analysis.tex` \| 289 \| `64%` \| `18 & 46 & 49 & 4.846400 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1096 | `62.8%` | `...0 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1096 | `0.2097` | `... & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` \| 62.8% (62....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1096 | `0.1142` | `...46400 & 1.000000 & 0.209700 & 0.114200 \\` \| 62.8% (62.7746% relat...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1097 | `64%` | `...0.2097` \| `18 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1097 | `0.2097` | `...ghbour_analysis.tex` \| 289 \| `0.2097` \| `18 & 46 & 49 & 4.846400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1097 | `0.1142` | `...46400 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1098 | `64%` | `...0.1142` \| `18 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1098 | `0.2097` | `... & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1098 | `0.1142` | `...ghbour_analysis.tex` \| 289 \| `0.1142` \| `18 & 46 & 49 & 4.846400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1099 | `0.2097` | `...ghbour_analysis.tex` \| 290 \| `0.2097` \| `18 & 48 & 49 & 9.769000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1099 | `0.1142` | `...69000 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1100 | `0.2097` | `... & 49 & 9.769000 & 1.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1100 | `0.1142` | `...ghbour_analysis.tex` \| 290 \| `0.1142` \| `18 & 48 & 49 & 9.769000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1101 | `0.2097` | `...ghbour_analysis.tex` \| 291 \| `0.2097` \| `18 & 55 & 51 & 2.184300 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1101 | `0.1142` | `...84300 & 0.085000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1102 | `0.2097` | `... & 51 & 2.184300 & 0.085000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1102 | `0.1142` | `...ghbour_analysis.tex` \| 291 \| `0.1142` \| `18 & 55 & 51 & 2.184300 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1103 | `0.2097` | `...ghbour_analysis.tex` \| 292 \| `0.2097` \| `18 & 60 & 58 & 3.707900 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1103 | `0.1142` | `...07900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1104 | `0.2097` | `... & 58 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1104 | `0.1142` | `...ghbour_analysis.tex` \| 292 \| `0.1142` \| `18 & 60 & 58 & 3.707900 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1105 | `0.2097` | `...ghbour_analysis.tex` \| 293 \| `0.2097` \| `19 & 4 & 40 & 4.343500 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1105 | `0.1142` | `...43500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1106 | `0.2097` | `... & 40 & 4.343500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1106 | `0.1142` | `...ghbour_analysis.tex` \| 293 \| `0.1142` \| `19 & 4 & 40 & 4.343500 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1107 | `0.2097` | `...ghbour_analysis.tex` \| 294 \| `0.2097` \| `19 & 10 & 39 & 3.431400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1107 | `0.1142` | `...31400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1108 | `0.2097` | `... & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1108 | `0.1142` | `...ghbour_analysis.tex` \| 294 \| `0.1142` \| `19 & 10 & 39 & 3.431400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1109 | `0.2097` | `...ghbour_analysis.tex` \| 295 \| `0.2097` \| `19 & 11 & 25 & 3.005500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1109 | `0.1142` | `...05500 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1110 | `0.2097` | `... & 25 & 3.005500 & 0.002000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1110 | `0.1142` | `...ghbour_analysis.tex` \| 295 \| `0.1142` \| `19 & 11 & 25 & 3.005500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1111 | `0.2097` | `...ghbour_analysis.tex` \| 296 \| `0.2097` \| `19 & 12 & 5 & 5.651900 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1111 | `0.1142` | `...51900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1112 | `0.2097` | `...2 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1112 | `0.1142` | `...ghbour_analysis.tex` \| 296 \| `0.1142` \| `19 & 12 & 5 & 5.651900 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1113 | `0.2097` | `...ghbour_analysis.tex` \| 297 \| `0.2097` \| `19 & 14 & 15 & 2.405800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1113 | `0.1142` | `...05800 & 0.018000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1114 | `0.2097` | `... & 15 & 2.405800 & 0.018000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1114 | `0.1142` | `...ghbour_analysis.tex` \| 297 \| `0.1142` \| `19 & 14 & 15 & 2.405800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1115 | `0.2097` | `...ghbour_analysis.tex` \| 298 \| `0.2097` \| `19 & 22 & 44 & 2.458200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1115 | `0.1142` | `...58200 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1116 | `0.2097` | `... & 44 & 2.458200 & 0.010000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1116 | `0.1142` | `...ghbour_analysis.tex` \| 298 \| `0.1142` \| `19 & 22 & 44 & 2.458200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1117 | `0.2097` | `...ghbour_analysis.tex` \| 299 \| `0.2097` \| `19 & 27 & 29 & 3.817400 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1117 | `0.1142` | `...17400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1118 | `0.2097` | `... & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1118 | `0.1142` | `...ghbour_analysis.tex` \| 299 \| `0.1142` \| `19 & 27 & 29 & 3.817400 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1119 | `0.2097` | `...ghbour_analysis.tex` \| 300 \| `0.2097` \| `19 & 31 & 32 & 6.201500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1119 | `0.1142` | `...01500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1120 | `0.2097` | `... & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1120 | `0.1142` | `...ghbour_analysis.tex` \| 300 \| `0.1142` \| `19 & 31 & 32 & 6.201500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1121 | `0.2097` | `...ghbour_analysis.tex` \| 301 \| `0.2097` \| `19 & 37 & 8 & 4.413700 & ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1121 | `0.1142` | `...13700 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1122 | `0.2097` | `...7 & 8 & 4.413700 & 0.007500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1122 | `0.1142` | `...ghbour_analysis.tex` \| 301 \| `0.1142` \| `19 & 37 & 8 & 4.413700 & ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1123 | `0.2097` | `...ghbour_analysis.tex` \| 302 \| `0.2097` \| `19 & 38 & 45 & 6.402000 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1123 | `0.1142` | `...02000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1124 | `0.2097` | `... & 45 & 6.402000 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1124 | `0.1142` | `...ghbour_analysis.tex` \| 302 \| `0.1142` \| `19 & 38 & 45 & 6.402000 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1125 | `0.2097` | `...ghbour_analysis.tex` \| 303 \| `0.2097` \| `19 & 42 & 25 & 5.844200 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1125 | `0.1142` | `...44200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1126 | `0.2097` | `... & 25 & 5.844200 & 0.000000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1126 | `0.1142` | `...ghbour_analysis.tex` \| 303 \| `0.1142` \| `19 & 42 & 25 & 5.844200 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1127 | `0.2097` | `...ghbour_analysis.tex` \| 304 \| `0.2097` \| `19 & 47 & 48 & 17.681100 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1127 | `0.1142` | `...81100 & 0.015000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1128 | `0.2097` | `...& 48 & 17.681100 & 0.015000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1128 | `0.1142` | `...ghbour_analysis.tex` \| 304 \| `0.1142` \| `19 & 47 & 48 & 17.681100 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1129 | `0.2097` | `...ghbour_analysis.tex` \| 305 \| `0.2097` \| `19 & 50 & 48 & 16.692100 ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1129 | `0.1142` | `...92100 & 0.595000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1130 | `0.2097` | `...& 48 & 16.692100 & 0.595000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1130 | `0.1142` | `...ghbour_analysis.tex` \| 305 \| `0.1142` \| `19 & 50 & 48 & 16.692100 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1131 | `0.2097` | `...ghbour_analysis.tex` \| 306 \| `0.2097` \| `19 & 56 & 52 & 5.371500 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1131 | `0.1142` | `...71500 & 0.112500 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1132 | `0.2097` | `... & 52 & 5.371500 & 0.112500 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1132 | `0.1142` | `...ghbour_analysis.tex` \| 306 \| `0.1142` \| `19 & 56 & 52 & 5.371500 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1133 | `0.2097` | `...ghbour_analysis.tex` \| 307 \| `0.2097` \| `19 & 57 & 59 & 4.558800 &...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1133 | `0.1142` | `...58800 & 0.030000 & 0.209700 & 0.114200 \\` \| 0.2097 (Spearman rho,...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1134 | `0.2097` | `... & 59 & 4.558800 & 0.030000 & 0.209700 & 0.114200 \\` \| 0.1142 (Sp...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1134 | `0.1142` | `...ghbour_analysis.tex` \| 307 \| `0.1142` \| `19 & 57 & 59 & 4.558800 &...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1135 | `0.9530` | `...ab_stats_summary.tex` \| 12 \| `0.9530` \| `...UROC_A & episode_level...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1136 | `0.9490` | `...ab_stats_summary.tex` \| 13 \| `0.9490` \| `...UROC_B & episode_level...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1137 | `64%` | `...ab_sweep_results.tex` \| 13 \| `64%` \| `0 & 15 & 0.741800 & 0.061...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1137 | `62.8%` | `...0 & 0.013100 & 0.243300 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1138 | `64%` | `...ab_sweep_results.tex` \| 14 \| `64%` \| `1 & 0 & 0.643300 & NaN & ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1138 | `62.8%` | `...0 & 0.042900 & 0.266200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1139 | `64%` | `...ab_sweep_results.tex` \| 18 \| `64%` \| `1 & 10 & 0.698400 & 0.156...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1139 | `62.8%` | `...0 & 0.042900 & 0.266200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1140 | `64%` | `...ab_sweep_results.tex` \| 19 \| `64%` \| `1 & 15 & 0.708200 & 0.164...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1140 | `62.8%` | `...0 & 0.042900 & 0.266200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1141 | `64%` | `...ab_sweep_results.tex` \| 20 \| `64%` \| `2 & 0 & 0.640700 & NaN & ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1141 | `62.8%` | `...0 & 0.004300 & 0.261600 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1142 | `64%` | `...ab_sweep_results.tex` \| 23 \| `64%` \| `2 & 5 & 0.612000 & 0.1664...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1142 | `62.8%` | `...0 & 0.004300 & 0.261600 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1143 | `0.1142` | `...ab_sweep_results.tex` \| 41 \| `0.1142` \| `5 & 5 & 0.718600 & 0.0957...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1144 | `64%` | `...ab_sweep_results.tex` \| 42 \| `64%` \| `5 & 10 & 0.625300 & 0.175...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1144 | `62.8%` | `...0 & 0.050900 & 0.267200 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1145 | `0.1142` | `...ab_sweep_results.tex` \| 43 \| `0.1142` \| `5 & 15 & 0.688100 & 0.114...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1146 | `0.2097` | `...ab_sweep_results.tex` \| 47 \| `0.2097` \| `6 & 5 & 0.611700 & 0.0044...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1147 | `64%` | `...ab_sweep_results.tex` \| 58 \| `64%` \| `8 & 3 & 0.648200 & 0.3855...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1147 | `62.8%` | `...0 & 0.095800 & 0.248300 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1148 | `64%` | `...ab_sweep_results.tex` \| 59 \| `64%` \| `8 & 5 & 0.648500 & 0.2120...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1148 | `62.8%` | `...0 & 0.095800 & 0.248300 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1149 | `64%` | `...ab_sweep_results.tex` \| 60 \| `64%` \| `8 & 10 & 0.648500 & 0.142...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1149 | `62.8%` | `...0 & 0.095800 & 0.248300 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1150 | `64%` | `...ab_sweep_results.tex` \| 61 \| `64%` \| `8 & 15 & 0.648500 & 0.186...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1150 | `62.8%` | `...0 & 0.095800 & 0.248300 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1151 | `0.0327` | `...ab_sweep_results.tex` \| 63 \| `0.0327` \| `9 & 1 & 0.581800 & 0.0040...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1151 | `0.0323` | `...ab_sweep_results.tex` \| 63 \| `0.0327` \| `9 & 1 & 0.581800 & 0.004...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1152 | `0.0327` | `...ab_sweep_results.tex` \| 63 \| `0.0323` \| `9 & 1 & 0.581800 & 0.004...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1152 | `0.0323` | `...ab_sweep_results.tex` \| 63 \| `0.0323` \| `9 & 1 & 0.581800 & 0.0040...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1153 | `64%` | `...ab_sweep_results.tex` \| 86 \| `64%` \| `13 & 0 & 0.640000 & NaN &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1153 | `62.8%` | `...0 & 0.030500 & 0.274800 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1154 | `0.1142` | `...ab_sweep_results.tex` \| 95 \| `0.1142` \| `14 & 5 & 0.768300 & 0.071...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1155 | `64%` | `...b_sweep_results.tex` \| 109 \| `64%` \| `16 & 15 & 0.651700 & 0.05...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1155 | `62.8%` | `...0 & 0.002600 & 0.255500 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1156 | `0.1142` | `...b_sweep_results.tex` \| 115 \| `0.1142` \| `17 & 15 & 0.698000 & 0.11...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1157 | `64%` | `...hreshold_tradeoff.tex` \| 8 \| `64%` \| `0 & 0.741800 & 0.830300 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1157 | `62.8%` | `...0 & 0.086500 & 0.178600 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1158 | `64%` | `...reshold_tradeoff.tex` \| 16 \| `64%` \| `8 & 0.648500 & 0.886900 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1158 | `62.8%` | `...0 & 0.050900 & 0.322600 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1159 | `64%` | `...reshold_tradeoff.tex` \| 17 \| `64%` \| `9 & 0.638300 & 0.743400 &...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1159 | `62.8%` | `...0 & 0.043800 & 0.077900 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1160 | `64%` | `...reshold_tradeoff.tex` \| 24 \| `64%` \| `16 & 0.651700 & 0.720200 ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1160 | `62.8%` | `...0 & 0.064600 & 0.113000 \\` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1161 | `1.47` | `...ECT_MASTER_GUIDE.md` \| 131 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1162 | `2.67` | `...ECT_MASTER_GUIDE.md` \| 137 \| `2.67` \| `...iarity gap** ($\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1162 | `22.08` | `... = 2.67\%$ vs $\text{FAR}_B = 22.08\%...` \| 2.67% (0.026744, k=1 ...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1163 | `2.67` | `....md` \| 137 \| `22.08` \| `... = 2.67\%$ vs $\text{FAR}_B = 22.08\%...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1163 | `22.08` | `...ECT_MASTER_GUIDE.md` \| 137 \| `22.08` \| `... = 2.67\%$ vs $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1164 | `64%` | `...$\text{...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1164 | `19.41` | `...ECT_MASTER_GUIDE.md` \| 137 \| `19.41` \| `...$) induces a catastrop...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1165 | `4.17` | `...ECT_MASTER_GUIDE.md` \| 140 \| `4.17` \| `...enetration from $11.55...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1165 | `4.43` | `... causes False Rejection...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1165 | `11.55` | `...`4.17` \| `...enetration from $11.55\%$ to $4.17\%$, it causes Fal...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1166 | `30.18` | `...ECT_MASTER_GUIDE.md` \| 140 \| `30.18` \| `...e ($\text{FRR}$) to su...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1166 | `30.08` | `...aking at $84.63\%$). Th...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1166 | `84.63` | `...rge to $30.18\%$ (peaking at $84.63\%$). Th...` \| 30.08% (0.30078...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1167 | `4.17` | `...enetration from $11.55\%$ to $4.17\%$, it causes Fal...` \| 11.55...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1167 | `11.55` | `...ECT_MASTER_GUIDE.md` \| 140 \| `11.55` \| `...ue stranger penetratio...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1168 | `30.18` | `...\| 140 \| `84.63` \| `...rge to $30.18\%$ (peaking at $84.63\%$). Th...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1168 | `84.63` | `...ECT_MASTER_GUIDE.md` \| 140 \| `84.63` \| `...rge to $30.18\%$ (peak...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1169 | `99.43` | `...ECT_MASTER_GUIDE.md` \| 143 \| `99.43` \| `...mentally required, ach...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1170 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 146 \| `8.49` \| `...tion by more than half...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1170 | `3.54` | `... half (from $8.49\%$ down to $3.54\%$), elevati...` \| 8.49% (0.0...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1171 | `8.49` | `...6 \| `3.54` \| `... half (from $8.49\%$ down to $3.54\%$), elevati...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1171 | `3.54` | `...ECT_MASTER_GUIDE.md` \| 146 \| `3.54` \| `... half (from $8.49\%$ d...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1172 | `64%` | `...} = 0.9670$.` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1172 | `0.9670` | `...ECT_MASTER_GUIDE.md` \| 146 \| `0.9670` \| `...rimination to $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1173 | `64%` | `...9.41\%$**!` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1173 | `19.41` | `...ECT_MASTER_GUIDE.md` \| 184 \| `19.41` \| `...2.1%**—an optimism gap...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1174 | `64%` | `...ECT_MASTER_GUIDE.md` \| 218 \| `64%` \| `...re map \\| Contrastive ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1174 | `62.8%` | `...ype space) \\| **292 com...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1175 | `99.43` | `...ECT_MASTER_GUIDE.md` \| 219 \| `99.43` \| `... \\| 93.85% \\| 96.2% \\|...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1176 | `0.9490` | `...ECT_MASTER_GUIDE.md` \| 220 \| `0.9490` \| `... 90.23% \\| ≈ 92.5% \\| ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1176 | `0.9530` | `... 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` \| 0.9490 (0.9...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1177 | `0.9490` | `... `0.9530` \| `...\\| 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1177 | `0.9530` | `...ECT_MASTER_GUIDE.md` \| 220 \| `0.9530` \| `...\\| 91.3% \\| **0.9490 (...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1178 | `12.35` | `...ECT_MASTER_GUIDE.md` \| 221 \| `12.35` \| `...t isolated \\| Not isol...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1179 | `11.55` | `...ECT_MASTER_GUIDE.md` \| 222 \| `11.55` \| `...hold \\| Distance thres...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1180 | `2.67` | `...ECT_MASTER_GUIDE.md` \| 223 \| `2.67` \| `...ted \\| **22.08%** (vs....` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1180 | `22.08` | `...\| 223 \| `2.67` \| `...ted \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 2...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1181 | `2.67` | `...ed \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 22.08% (0.220808, k=1 ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1181 | `22.08` | `...ECT_MASTER_GUIDE.md` \| 223 \| `22.08` \| `...evaluated \\| Not evalu...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1182 | `1.47` | `...ECT_MASTER_GUIDE.md` \| 224 \| `1.47` \| `...reported \\| None repor...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1183 | `64%` | `...rfittin...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1183 | `19.41` | `...ECT_MASTER_GUIDE.md` \| 225 \| `19.41` \| `...reported \\| None repor...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1184 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 226 \| `8.49` \| `...≈ 6.15% \\| ≈ 5.5% \\| ≈...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1185 | `4.17` | `...ECT_MASTER_GUIDE.md` \| 227 \| `4.17` \| `...t provided \\| Not prov...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1185 | `4.43` | `...ps penetration by 64%) ...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1185 | `64%` | `...4.17%** (drops penetration by 64%) ...` \| 4.43% (0.044315, epis...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1186 | `4.17` | `...GUIDE.md` \| 227 \| `64%` \| `...4.17%** (drops penetration by 64%) ...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1186 | `64%` | `...ECT_MASTER_GUIDE.md` \| 227 \| `64%` \| `...4.17%** (drops penetra...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1186 | `62.8%` | `...ops penetration by 64%) \\|` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1187 | `30.18` | `...ECT_MASTER_GUIDE.md` \| 228 \| `30.18` \| `...antified \\| Not quanti...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1187 | `30.08` | `...ge of +21.69%, peak 84....` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1187 | `21.69` | `...fied \\| **30.18%** (surge of +21.69%, peak 84....` \| 30.08% (0.300...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 1188 | `30.18` | `...28 \| `21.69` \| `...ified \\| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1188 | `21.69` | `...ECT_MASTER_GUIDE.md` \| 228 \| `21.69` \| `...ified \\| **30.18%** (s...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 1188 | `21.59` | `... +21.69%, peak 84.63%) \\|` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1188 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \\|` \| +21.59 pp (0.215929, e...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1189 | `21.69` | `...84.63` \| `...18%** (surge of +21.69%, peak 84.63%) \\|` \| 84.63% (0...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 1189 | `84.63` | `...ECT_MASTER_GUIDE.md` \| 228 \| `84.63` \| `...18%** (surge of +21.69...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1190 | `3.54` | `...ECT_MASTER_GUIDE.md` \| 229 \| `3.54` \| `...ted \\| Not evaluated \...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1190 | `0.9670` | `...ted \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 3.54% (0.035369, burs...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1191 | `64%` | `... 0.9670** \\|` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1191 | `3.54` | `...0.9670` \| `...ated \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 0.967...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1191 | `0.9670` | `...ECT_MASTER_GUIDE.md` \| 229 \| `0.9670` \| `...ated \\| **FRR → 3.54%,...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1192 | `0.2097` | `...ECT_MASTER_GUIDE.md` \| 231 \| `0.2097` \| `...orted \\| None reported...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1192 | `0.1142` | `...reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0.2097 (Spearm...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1193 | `0.2097` | `...142` \| `... reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1193 | `0.1142` | `...ECT_MASTER_GUIDE.md` \| 231 \| `0.1142` \| `... reported \\| **ρ = 0.2...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1194 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 232 \| `0.0327` \| `...evaluated \\| Not evalu...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1194 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 232 \| `0.0327` \| `...evaluated \\| Not eval...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1195 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 232 \| `0.0323` \| `...evaluated \\| Not eval...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1195 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 232 \| `0.0323` \| `...evaluated \\| Not evalu...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1196 | `98.5` | `...ECT_MASTER_GUIDE.md` \| 260 \| `98.5` \| `...ries widely (from $0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 1196 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 1197 | `1.47` | `...ECT_MASTER_GUIDE.md` \| 260 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1198 | `2.67` | `...ECT_MASTER_GUIDE.md` \| 265 \| `2.67` \| `...trangers show $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1199 | `22.08` | `...ECT_MASTER_GUIDE.md` \| 265 \| `22.08` \| `... penetrate at $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1200 | `64%` | `...abilize...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1200 | `19.41` | `...ECT_MASTER_GUIDE.md` \| 265 \| `19.41` \| `...gap of **$\Delta\text{...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1201 | `65.7` | `...ECT_MASTER_GUIDE.md` \| 270 \| `65.7` \| `...e rates between $42.6\...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 1202 | `0.2097` | `...ECT_MASTER_GUIDE.md` \| 270 \| `0.2097` \| `... and vulnerability is ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1202 | `0.1142` | `...lity is $\rho = 0.2097$ ($p = 0.1142, n=58$). This d...` \| 0.2097 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1203 | `0.2097` | `...0.1142` \| `...lity is $\rho = 0.2097$ ($p = 0.1142, n=58$). This d...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1203 | `0.1142` | `...ECT_MASTER_GUIDE.md` \| 270 \| `0.1142` \| `...lity is $\rho = 0.2097...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1204 | `4.17` | `...ECT_MASTER_GUIDE.md` \| 275 \| `4.17` \| `...ation from $11.55\%$ d...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1204 | `4.43` | `...th 4 episodes reaching ...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1204 | `11.55` | `...75 \| `4.17` \| `...ation from $11.55\%$ down to $4.17\%$ (with 4 e...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1205 | `30.18` | `...ECT_MASTER_GUIDE.md` \| 275 \| `30.18` \| `...rs surges from $8.49\%...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1205 | `30.08` | `...n average (peaking at $...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1205 | `8.49` | `...`30.18` \| `...rs surges from $8.49\%$ to **$30.18\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1206 | `4.17` | `...ation from $11.55\%$ down to $4.17\%$ (with 4 e...` \| 11.55% (de...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1206 | `11.55` | `...ECT_MASTER_GUIDE.md` \| 275 \| `11.55` \| `...ue stranger penetratio...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1207 | `30.18` | `...rs surges from $8.49\%$ to **$30.18\%$** on averag...` \| 8.49% (0...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1207 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 275 \| `8.49` \| `...ate smart meters surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1208 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 275 \| `0.0327` \| `...s absolute estimation ...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1208 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 275 \| `0.0327` \| `...s absolute estimation...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1209 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 275 \| `0.0323` \| `...s absolute estimation...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1209 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 275 \| `0.0323` \| `...s absolute estimation ...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1210 | `84.63` | `...ECT_MASTER_GUIDE.md` \| 275 \| `84.63` \| `...\%$** on average (peak...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1211 | `64%` | `...ECT_MASTER_GUIDE.md` \| 280 \| `64%` \| `...nds to $\Delta\text{FA...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1211 | `62.8%` | `...instantaneous packet no...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1212 | `0.9490` | `...ECT_MASTER_GUIDE.md` \| 280 \| `0.9490` \| `...{AUROC} = 0.9670$** (u...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1212 | `0.9670` | `...80 \| `0.9490` \| `...{AUROC} = 0.9670$** (up from $0.9490$), while ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1213 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 280 \| `8.49` \| `...f: **$\text{FRR}$ drop...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1213 | `3.54` | `...FRR}$ drops from $8.49\%$ to $3.54\%$**, elevating g...` \| 8.49%...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1214 | `8.49` | `...3.54` \| `...FRR}$ drops from $8.49\%$ to $3.54\%$**, elevating g...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1214 | `3.54` | `...ECT_MASTER_GUIDE.md` \| 280 \| `3.54` \| `...FRR}$ drops from $8.49...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1215 | `64%` | `...), while ...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1215 | `0.9490` | `...{AUROC} = 0.9670$** (up from $0.9490$), while ...` \| 0.9670 (0.966...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1215 | `0.9670` | `...ECT_MASTER_GUIDE.md` \| 280 \| `0.9670` \| `...n climbs to **$\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1216 | `64%` | `...e-proxy)"]` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1216 | `19.41` | `...ECT_MASTER_GUIDE.md` \| 300 \| `19.41` \| `F1["Identified Familiarit...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1216 | `1.47` | `..."Identified Familiarity Gap (+1.47% matched, +19.41% single-proxy...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1217 | `19.41` | `...liarity Gap (+1.47% matched, +19.41% single-proxy)"]` \| +1.47% (de...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1217 | `1.47` | `...ECT_MASTER_GUIDE.md` \| 300 \| `1.47` \| `F1["Identified Familiarit...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1218 | `30.18` | `...ECT_MASTER_GUIDE.md` \| 301 \| `30.18` \| `F2["Quantified Robust Ava...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1218 | `30.08` | `...t (FRR surges to 30.18%)"]` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1219 | `12.35` | `...ECT_MASTER_GUIDE.md` \| 473 \| `12.35` \| `...gers)** \\| Device ($n=...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1220 | `11.55` | `...ECT_MASTER_GUIDE.md` \| 474 \| `11.55` \| `...gers)** \\| Device ($n=...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1221 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 476 \| `8.49` \| `...FRR)** \\| Episode ($n=...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1222 | `0.9530` | `...ECT_MASTER_GUIDE.md` \| 477 \| `0.9530` \| `...n A)** \\| Episode ($n=...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1223 | `0.9490` | `...ECT_MASTER_GUIDE.md` \| 478 \| `0.9490` \| `...n B)** \\| Episode ($n=...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1224 | `99.43` | `...ECT_MASTER_GUIDE.md` \| 479 \| `99.43` \| `...F_1$** \\| Episode ($n=...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1225 | `98.5` | `...ECT_MASTER_GUIDE.md` \| 481 \| `98.5` \| `...netration ranges from ...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 1225 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 1226 | `1.47` | `...ECT_MASTER_GUIDE.md` \| 490 \| `1.47` \| `...AR}_{\text{matched}}$)...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1227 | `2.67` | `...ECT_MASTER_GUIDE.md` \| 502 \| `2.67` \| `... **$k=1$** (Single rad...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1227 | `22.08` | `...ngle radio) \\| **2.67%** \\| **22.08%** \\| 10.39% \\| **+...` \| 2.67...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1228 | `2.67` | `....08` \| `...Single radio) \\| **2.67%** \\| **22.08%** \\| 10.39% \\| ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1228 | `22.08` | `...ECT_MASTER_GUIDE.md` \| 502 \| `22.08` \| `...Single radio) \\| **2.6...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1228 | `19.41` | `...\\| **22.08%** \\| 10.39% \\| **+19.41%** \\| **...` \| 22.08% (0.22080...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1229 | `64%` | `...overfit...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1229 | `22.08` | `...\| 502 \| `19.41` \| `...** \\| **22.08%** \\| 10.39% \\| **+19.41%** \\|...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1229 | `19.41` | `...ECT_MASTER_GUIDE.md` \| 502 \| `19.41` \| `...** \\| **22.08%** \\| 10...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1230 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 505 \| `8.49` \| `\\| **$k=10$** \\| 10.53% \...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1231 | `11.90` | `...ECT_MASTER_GUIDE.md` \| 506 \| `11.90` \| `\\| **$k=15$** \\| 11.34% \...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1231 | `11.34` | `...\| `11.90` \| `\\| **$k=15$** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% ...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1231 | `8.49` | `...=15$** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| Convergence to f...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1232 | `11.90` | `...\| `\\| **$k=15$** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| Converg...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1232 | `11.34` | `...ECT_MASTER_GUIDE.md` \| 506 \| `11.34` \| `\\| **$k=15$** \\| 11.34% \...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1232 | `8.49` | `...=15$** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| Convergence to f...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1233 | `11.90` | `...\| `\\| **$k=15$** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| Converg...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1233 | `11.34` | `... \| `8.49` \| `\\| **$k=15$** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% ...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1233 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 506 \| `8.49` \| `\\| **$k=15$** \\| 11.34% \...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1234 | `64%` | `...ECT_MASTER_GUIDE.md` \| 516 \| `64%` \| `\\| **Device 50** \\| **64....` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1234 | `62.8%` | `... IDs 46–60) \\| Reliable \\|` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1235 | `0.2097` | `...ECT_MASTER_GUIDE.md` \| 524 \| `0.2097` \| `...unique devices yields ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1235 | `0.1142` | `... yields $\rho = 0.2097$ ($p = 0.1142, n=58$).` \| 0.2097 (Spearman ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1236 | `0.2097` | `...0.1142` \| `... yields $\rho = 0.2097$ ($p = 0.1142, n=58$).` \| 0.1...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1236 | `0.1142` | `...ECT_MASTER_GUIDE.md` \| 524 \| `0.1142` \| `... yields $\rho = 0.2097...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1237 | `11.55` | `...ECT_MASTER_GUIDE.md` \| 532 \| `11.55` \| `...int ($\tau^*$)** \\| 0....` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1237 | `8.49` | `... \\| 0.7040 \\| **11.55%** \\| **8.49%** \\| Standard scre...` \| 11.5...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1238 | `11.55` | `....49` \| `...)** \\| 0.7040 \\| **11.55%** \\| **8.49%** \\| Standard sc...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1238 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 532 \| `8.49` \| `...)** \\| 0.7040 \\| **11....` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1239 | `4.17` | `...ECT_MASTER_GUIDE.md` \| 533 \| `4.17` \| `...ext{robust}}$)** \\| 0....` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1239 | `4.43` | `...0.18%** \\| **Catastroph...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1239 | `30.18` | `...* \\| 0.8540 \\| **4.17%** \\| **30.18%** \\| **Catastroph...` \| 4.43%...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1240 | `4.17` | `...18` \| `...$)** \\| 0.8540 \\| **4.17%** \\| **30.18%** \\| **Catastro...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1240 | `30.18` | `...ECT_MASTER_GUIDE.md` \| 533 \| `30.18` \| `...$)** \\| 0.8540 \\| **4....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1240 | `30.08` | `...Catastrophic availabili...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1241 | `4.17` | `...ECT_MASTER_GUIDE.md` \| 535 \| `4.17` \| `...ue penetration from 11...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1241 | `4.43` | `...4 episodes reaching 0.0...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1241 | `11.55` | `...17` \| `...ue penetration from 11.55% to 4.17% (with 4 episodes rea...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1242 | `30.18` | `...ECT_MASTER_GUIDE.md` \| 535 \| `30.18` \| `..., False Rejection surg...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1242 | `30.08` | `...verage (and reaches **8...` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1243 | `4.17` | `...ue penetration from 11.55% to 4.17% (with 4 episodes rea...` \| 11...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1243 | `11.55` | `...ECT_MASTER_GUIDE.md` \| 535 \| `11.55` \| `...lashes rogue penetrati...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1244 | `84.63` | `...ECT_MASTER_GUIDE.md` \| 535 \| `84.63` \| `...%** on average (and re...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1245 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 540 \| `0.0327` \| `- **LOPO Bias:** $+0.0138...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1245 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 540 \| `0.0327` \| `- **LOPO Bias:** $+0.013...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1246 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 540 \| `0.0323` \| `- **LOPO Bias:** $+0.013...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1246 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 540 \| `0.0323` \| `- **LOPO Bias:** $+0.0138...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1247 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 541 \| `0.0327` \| `- **Naive Packet-Disjoint...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1247 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 541 \| `0.0327` \| `- **Naive Packet-Disjoin...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1248 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 541 \| `0.0323` \| `- **Naive Packet-Disjoin...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1248 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 541 \| `0.0323` \| `- **Naive Packet-Disjoint...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1249 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 543 \| `0.0327` \| `...hin empirical noise ($...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1249 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 543 \| `0.0327` \| `...hin empirical noise (...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1250 | `0.0327` | `...ECT_MASTER_GUIDE.md` \| 543 \| `0.0323` \| `...hin empirical noise (...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1250 | `0.0323` | `...ECT_MASTER_GUIDE.md` \| 543 \| `0.0323` \| `...hin empirical noise ($...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1251 | `11.90` | `...ECT_MASTER_GUIDE.md` \| 553 \| `11.90` \| `...Packet Baseline)** \\| ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1251 | `11.34` | `...` \| `...Packet Baseline)** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% ...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1251 | `0.9490` | `... 11.90% \\| 8.49% \\| +0.56% \\| 0.9490 \\| B...` \| 11.90% (0.119046, ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1251 | `8.49` | `...ine)** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| 0.9490 \\| B...` ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1252 | `11.90` | `...cket Baseline)** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| 0...` \|...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1252 | `11.34` | `...ECT_MASTER_GUIDE.md` \| 553 \| `11.34` \| `... (Single Packet Baseli...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1252 | `8.49` | `...ine)** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| 0...` \| 11.34% (...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1253 | `11.90` | `...` \| 553 \| `0.9490` \| `...% \\| 11.90% \\| 8.49% \\| +0.56% \\| 0.9490 ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1253 | `0.9490` | `...ECT_MASTER_GUIDE.md` \| 553 \| `0.9490` \| `...% \\| 11.90% \\| 8.49% \...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1253 | `8.49` | `...`0.9490` \| `...% \\| 11.90% \\| 8.49% \\| +0.56% \\| 0.9490 \\| Baseli...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1254 | `11.90` | `... \| `...seline)** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% \\| 0.9490 ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1254 | `11.34` | `...3 \| `8.49` \| `...seline)** \\| 11.34% \\| 11.90% \\| 8.49% \\| +0.56% ...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1254 | `0.9490` | `... 11.90% \\| 8.49% \\| +0.56% \\| 0.9490 \\| Baseline ...` \| 8.49% (0.0...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1254 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 553 \| `8.49` \| `...seline)** \\| 11.34% \\|...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1255 | `64%` | `...ECT_MASTER_GUIDE.md` \| 554 \| `64%` \| `... 11.22% \\| 4.37% \\| +1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1255 | `62.8%` | `... drops by half; AUROC c...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1255 | `11.22` | `...UIDE.md` \| 554 \| `64%` \| `... 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 ...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1255 | `4.37` | `... 554 \| `64%` \| `... 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| FRR dr...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1255 | `0.9642` | `... 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| FRR drops by half; AUROC c...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1256 | `64%` | `....22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| F...` \| 11.22% (0.112182,...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1256 | `11.22` | `...ECT_MASTER_GUIDE.md` \| 554 \| `11.22` \| `... (3-Packet Burst)** \\|...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1256 | `4.37` | `...urst)** \\| 9.95% \\| 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| F...` ...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1256 | `0.9642` | `... 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| F...` \| 11.22% (0.112182, ...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1257 | `64%` | `....22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| FRR drops...` \| 4.37% (0....` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1257 | `11.22` | `... \| `...t Burst)** \\| 9.95% \\| 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 ...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1257 | `4.37` | `...ECT_MASTER_GUIDE.md` \| 554 \| `4.37` \| `...t Burst)** \\| 9.95% \\|...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1257 | `0.9642` | `... 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| FRR drops...` \| 4.37% (0.0...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1258 | `64%` | `..._MASTER_GUIDE.md` \| 554 \| `0.9642` \| `...% \\| 11.22% \\| 4.37% ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1258 | `11.22` | `...` \| 554 \| `0.9642` \| `...% \\| 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 ...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1258 | `4.37` | `...`0.9642` \| `...% \\| 11.22% \\| 4.37% \\| +1.27% \\| 0.9642 \\| FRR dr...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1258 | `0.9642` | `...ECT_MASTER_GUIDE.md` \| 554 \| `0.9642` \| `...% \\| 11.22% \\| 4.37% \...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1259 | `64%` | `...ECT_MASTER_GUIDE.md` \| 555 \| `64%` \| `...**10.45%** \\| **3.54%*...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1259 | `62.8%` | `....9670** \\| **FRR drops ...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1259 | `3.54` | `...\| `64%` \| `...**10.45%** \\| **3.54%** \\| **+1.64%** \\| **0.9670**...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1259 | `10.45` | `...IDE.md` \| 555 \| `64%` \| `...**10.45%** \\| **3.54%** \\| **+1.64%** ...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1259 | `0.9670` | `... **3.54%** \\| **+1.64%** \\| **0.9670** \\| **FRR drops ...` \| 62.8%...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1260 | `64%` | `...10.45%** \\| **3.54%** \\| **+1.64%** \\| **0.9670** \\|...` \| 3.54...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1260 | `3.54` | `...ECT_MASTER_GUIDE.md` \| 555 \| `3.54` \| `... \\| **8.81%** \\| **10....` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1260 | `10.45` | `....54` \| `... \\| **8.81%** \\| **10.45%** \\| **3.54%** \\| **+1.64%** ...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1260 | `0.9670` | `... **3.54%** \\| **+1.64%** \\| **0.9670** \\|...` \| 3.54% (0.035369, b...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1261 | `64%` | `...10.45%** \\| **3.54%** \\| **+1.64%** \\| ...` \| 10.45% (0.104538,...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1261 | `3.54` | `... **8.81%** \\| **10.45%** \\| **3.54%** \\| **+1.64%** \\| ...` \| 10....` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1261 | `10.45` | `...ECT_MASTER_GUIDE.md` \| 555 \| `10.45` \| `...cket Burst)** \\| **8.8...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1262 | `64%` | `...` \| `... \\| **3.54%** \\| **+1.64%** \\| **0.9670** \\| **FRR drop...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1262 | `3.54` | `... \| 555 \| `0.9670` \| `... \\| **3.54%** \\| **+1.64%** \\| **0.9670**...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1262 | `0.9670` | `...ECT_MASTER_GUIDE.md` \| 555 \| `0.9670` \| `... \\| **3.54%** \\| **+1....` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1263 | `64%` | `...ECT_MASTER_GUIDE.md` \| 557 \| `64%` \| `...omes sharper ($+0.56\%...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1263 | `62.8%` | `...onfirming that identity...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1264 | `3.54` | `...ECT_MASTER_GUIDE.md` \| 557 \| `3.54` \| `...n by more than half (d...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1265 | `99.43` | `...ECT_MASTER_GUIDE.md` \| 569 \| `99.43` \| `...ntally required, achie...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1266 | `0.9490` | `...ECT_MASTER_GUIDE.md` \| 569 \| `0.9490` \| `... 0.24\%$ Macro-$F_1$**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1266 | `0.9670` | `...Macro-$F_1$** and **$0.9490 - 0.9670$ AUROC** by performi...` \| 0....` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1267 | `64%` | `...ng non-li...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1267 | `0.9490` | `...0` \| `...Macro-$F_1$** and **$0.9490 - 0.9670$ AUROC** by performi...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1267 | `0.9670` | `...ECT_MASTER_GUIDE.md` \| 569 \| `0.9670` \| `...Macro-$F_1$** and **$0...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1268 | `8.49` | `...ECT_MASTER_GUIDE.md` \| 596 \| `8.49` \| `...itimate false rejectio...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1268 | `3.54` | `...e rejection from $8.49\%$ to $3.54\%$ while elevatin...` \| 8.49%...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1269 | `8.49` | `...3.54` \| `...e rejection from $8.49\%$ to $3.54\%$ while elevatin...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1269 | `3.54` | `...ECT_MASTER_GUIDE.md` \| 596 \| `3.54` \| `...e rejection from $8.49...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1270 | `64%` | `...to $0.9670$.` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1270 | `0.9670` | `...ECT_MASTER_GUIDE.md` \| 596 \| `0.9670` \| `...\%$ while elevating AU...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1271 | `1.47` | `\| `README.md` \| 32 \| `1.47` \| `...text{FAR}_{\text{match...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1272 | `11.55` | `\| `README.md` \| 33 \| `11.55` \| `...%, 18.77\%]$; $\text{F...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1273 | `12.35` | `\| `README.md` \| 33 \| `12.35` \| `...ted episodes ($\text{F...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1274 | `64%` | `...1\%$ gap).` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1274 | `19.41` | `\| `README.md` \| 34 \| `19.41` \| `...xy distortion ($k=1$ y...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1275 | `98.5` | `\| `README.md` \| 35 \| `98.5` \| `...ility ranges from $0.0...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/NUMBER_OCCURRENCES.md` | 1275 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/NUMBER_OCCURRENCES.md` | 1276 | `4.43` | `\| `README.md` \| 36 \| `4.43` \| `...enetration from $11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1276 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at ...` \| 4.43%...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1276 | `11.90` | `...`4.43` \| `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1277 | `30.08` | `\| `README.md` \| 36 \| `30.08` \| `...FRR surging from $8.49...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1277 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp).` \| 30.08% (0.300789, epi...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1277 | `8.49` | `...0.08` \| `...FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).`...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1278 | `30.08` | `....59` \| `... from $8.49\%$ to $30.08\%$ (+21.59 pp).` \| +21.59 pp ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1278 | `21.59` | `\| `README.md` \| 36 \| `21.59` \| `... from $8.49\%$ to $30....` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1278 | `8.49` | `...` \| 36 \| `21.59` \| `... from $8.49\%$ to $30.08\%$ (+21.59 pp).`...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1279 | `4.43` | `...2.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1279 | `62.8%` | `\| `README.md` \| 36 \| `62.8%` \| `...rom $11.90\%$ to $4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1279 | `11.90` | `...md` \| 36 \| `62.8%` \| `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1280 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1280 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` \| 11.90% (0.119046,...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1280 | `11.90` | `\| `README.md` \| 36 \| `11.90` \| `...ue stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1281 | `30.08` | `...FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).` \| 8.49% (0.0...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1281 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp).` \| 8.49% (0.084860, FRR ...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1281 | `8.49` | `\| `README.md` \| 36 \| `8.49` \| `...the cost of FRR surgin...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1282 | `8.49` | `\| `README.md` \| 38 \| `8.49` \| `...itimate false rejectio...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1282 | `3.54` | `...e rejection from $8.49\%$ to $3.54\%$ (boosting avai...` \| 8.49%...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1283 | `8.49` | `...3.54` \| `...e rejection from $8.49\%$ to $3.54\%$ (boosting avai...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1283 | `3.54` | `\| `README.md` \| 38 \| `3.54` \| `...e rejection from $8.49...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1284 | `64%` | `...} = 0.9670$.` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1284 | `0.9670` | `\| `README.md` \| 38 \| `0.9670` \| `...rimination to $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1285 | `12.35` | `\| `README.md` \| 46 \| `12.35` \| `...s)** \\| Packet-disjoin...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1286 | `11.55` | `\| `README.md` \| 47 \| `11.55` \| `...** \\| Identity-disjoin...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1287 | `1.47` | `\| `README.md` \| 48 \| `1.47` \| `... \\| Device-matched pai...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1288 | `2.67` | `\| `README.md` \| 49 \| `2.67` \| `...**+19.41%** \\| $\text{...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1288 | `22.08` | `..._A = 2.67\%$, $\text{FAR}_B = 22.08\%$ ...` \| 2.67% (0.026744, k=...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1288 | `19.41` | `...ME.md` \| 49 \| `2.67` \| `...**+19.41%** \\| $\text{FAR}_A = 2.67\%$,...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1289 | `2.67` | `...md` \| 49 \| `22.08` \| `..._A = 2.67\%$, $\text{FAR}_B = 22.08\%$ ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1289 | `22.08` | `\| `README.md` \| 49 \| `22.08` \| `..._A = 2.67\%$, $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1290 | `64%` | `...67\%$, ...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1290 | `2.67` | `...*+19.41%** \\| $\text{FAR}_A = 2.67\%$, ...` \| +19.41% (+0.194064...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1290 | `19.41` | `\| `README.md` \| 49 \| `19.41` \| `... ($k=1$)** \\| Proxy sw...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1291 | `4.17` | `\| `README.md` \| 50 \| `4.17` \| `... \\| $\text{FAR}_B: 11....` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1291 | `4.43` | `...RR surges from $8.49\%$...` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1291 | `11.55` | `....17` \| `... \\| $\text{FAR}_B: 11.55\% \to 4.17\%$ \\| FRR surges f...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1291 | `8.49` | `...o 4.17\%$ \\| FRR surges from $8.49\%$...` \| 4.43% (0.044315, epi...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1292 | `30.18` | `\| `README.md` \| 50 \| `30.18` \| `... FRR surges from $8.49...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1292 | `30.08` | `...m $8.49\%$ to $30.18\%$ \\|` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1292 | `8.49` | `...0.18` \| `... FRR surges from $8.49\%$ to $30.18\%$ \\|` \| 30.08% ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1293 | `4.17` | `...\\| $\text{FAR}_B: 11.55\% \to 4.17\%$ \\| FRR surges fr...` \| 11....` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1293 | `11.55` | `\| `README.md` \| 50 \| `11.55` \| `...xy rejection \\| $\text...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1294 | `4.17` | `...ME.md` \| 50 \| `8.49` \| `...to 4.17\%$ \\| FRR surges from $8.49\%...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1294 | `30.18` | `... FRR surges from $8.49\%$ to $30.18\%$ \\|` \| 8.49% (0.084860, FRR...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1294 | `8.49` | `\| `README.md` \| 50 \| `8.49` \| `...to 4.17\%$ \\| FRR surg...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1295 | `8.49` | `\| `README.md` \| 51 \| `8.49` \| `...ision fusion \\| **$\te...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1295 | `3.54` | `... \\| **$\text{FRR}: 8.49\% \to 3.54\%$** \\| **AUROC cli...` \| 8.4...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1296 | `8.49` | `...54` \| `...n \\| **$\text{FRR}: 8.49\% \to 3.54\%$** \\| **AUROC cl...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1296 | `3.54` | `\| `README.md` \| 51 \| `3.54` \| `...n \\| **$\text{FRR}: 8....` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1297 | `10.45` | `\| `README.md` \| 51 \| `10.45` \| `...$0.9670$**, $\text{FAR...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1297 | `0.9670` | `...DME.md` \| 51 \| `10.45` \| `...$0.9670$**, $\text{FAR}_B \to 10.45\%...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1298 | `64%` | `...o 10.45\%...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1298 | `10.45` | `...$0.9670$**, $\text{FAR}_B \to 10.45\%...` \| 0.9670 (0.966964, bur...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1298 | `0.9670` | `\| `README.md` \| 51 \| `0.9670` \| `....54\%$** \\| **AUROC cl...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1299 | `99.43` | `\| `README.md` \| 52 \| `99.43` \| `\\| **Closed-Set Macro $F_...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1300 | `0.9490` | `\| `README.md` \| 53 \| `0.9490` \| `\\| **Open-Set AUROC** \\| ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1301 | `64%` | `\| `README.md` \| 63 \| `64%` \| `...re map \\| Contrastive ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1301 | `62.8%` | `...ype space) \\| **292 com...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1302 | `64%` | `\| `README.md` \| 64 \| `99.43` \| `... \\| 93.85% \\|...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1302 | `99.43` | `\| `README.md` \| 64 \| `99.43` \| `... \\| 93.85% \\| 96.2% \\|...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1303 | `0.9490` | `\| `README.md` \| 65 \| `0.9490` \| `... 90.23% \\| ≈ 92.5% \\| ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1303 | `0.9530` | `... 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` \| 0.9490 (0.9...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1304 | `0.9490` | `... `0.9530` \| `...\\| 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1304 | `0.9530` | `\| `README.md` \| 65 \| `0.9530` \| `...\\| 91.3% \\| **0.9490 (...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1305 | `12.35` | `\| `README.md` \| 66 \| `12.35` \| `...t isolated \\| Not isol...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1306 | `11.55` | `\| `README.md` \| 67 \| `11.55` \| `...hold \\| Distance thres...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1307 | `2.67` | `\| `README.md` \| 68 \| `2.67` \| `...ted \\| **22.08%** (vs....` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1307 | `22.08` | `... \| 68 \| `2.67` \| `...ted \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 2...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1308 | `2.67` | `...ed \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 22.08% (0.220808, k=1 ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1308 | `22.08` | `\| `README.md` \| 68 \| `22.08` \| `...evaluated \\| Not evalu...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1309 | `1.47` | `\| `README.md` \| 69 \| `1.47` \| `...reported \\| None repor...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1310 | `64%` | `...erfitti...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1310 | `19.41` | `\| `README.md` \| 70 \| `19.41` \| `...reported \\| None repor...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1311 | `8.49` | `\| `README.md` \| 71 \| `8.49` \| `...≈ 6.15% \\| ≈ 5.5% \\| ≈...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1312 | `4.17` | `\| `README.md` \| 72 \| `4.17` \| `...t provided \\| Not prov...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1312 | `4.43` | `...drops intrusion by 64%) \\|` \| 4.43% (0.044315, episode mean) \| **...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1312 | `64%` | `...**4.17%** (drops intrusion by 64%) \\|` \| 4.43% (0.044315, episo...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1313 | `4.17` | `...ADME.md` \| 72 \| `64%` \| `...**4.17%** (drops intrusion by 64%) \\|...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1313 | `64%` | `\| `README.md` \| 72 \| `64%` \| `...**4.17%** (drops intru...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1313 | `62.8%` | `...drops intrusion by 64%) \\|` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1314 | `30.18` | `\| `README.md` \| 73 \| `30.18` \| `...antified \\| Not quanti...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1314 | `30.08` | `...ge of +21.69%, peak 84....` \| 30.08% (0.300789, episode mean) \| **...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1314 | `21.69` | `...fied \\| **30.18%** (surge of +21.69%, peak 84....` \| 30.08% (0.300...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 1315 | `30.18` | `...73 \| `21.69` \| `...ified \\| **30.18%** (surge of +21.69%, peak 84....` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/NUMBER_OCCURRENCES.md` | 1315 | `21.69` | `\| `README.md` \| 73 \| `21.69` \| `...ified \\| **30.18%** (s...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 1315 | `21.59` | `... +21.69%, peak 84.63%) \\|` \| +21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1315 | `84.63` | `...18%** (surge of +21.69%, peak 84.63%) \\|` \| +21.59 pp (0.215929, e...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1316 | `21.69` | `...84.63` \| `...18%** (surge of +21.69%, peak 84.63%) \\|` \| 84.63% (0...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/NUMBER_OCCURRENCES.md` | 1316 | `84.63` | `\| `README.md` \| 73 \| `84.63` \| `...18%** (surge of +21.69...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1317 | `3.54` | `\| `README.md` \| 74 \| `3.54` \| `...ted \\| Not evaluated \...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1317 | `0.9670` | `...ted \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 3.54% (0.035369, burs...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1318 | `64%` | `... 0.9670** \\|` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1318 | `3.54` | `...0.9670` \| `...ated \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 0.967...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1318 | `0.9670` | `\| `README.md` \| 74 \| `0.9670` \| `...ated \\| **FRR → 3.54%,...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1319 | `0.2097` | `\| `README.md` \| 76 \| `0.2097` \| `...orted \\| None reported...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1319 | `0.1142` | `...reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0.2097 (Spearm...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1320 | `0.2097` | `...142` \| `... reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1320 | `0.1142` | `\| `README.md` \| 76 \| `0.1142` \| `... reported \\| **ρ = 0.2...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1321 | `0.0327` | `\| `README.md` \| 77 \| `0.0327` \| `...evaluated \\| Not evalu...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1321 | `0.0323` | `\| `README.md` \| 77 \| `0.0327` \| `...evaluated \\| Not eval...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1322 | `0.0327` | `\| `README.md` \| 77 \| `0.0323` \| `...evaluated \\| Not eval...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1322 | `0.0323` | `\| `README.md` \| 77 \| `0.0323` \| `...evaluated \\| Not evalu...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1323 | `64%` | `...ts/experiment_log.md` \| 11 \| `64%` \| `- **Operating System:** W...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1323 | `62.8%` | `...System:** Windows 11 AMD64` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1324 | `99.43` | `...ts/experiment_log.md` \| 74 \| `99.43` \| `- **Closed-Set Calibratio...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1325 | `12.35` | `...ts/experiment_log.md` \| 76 \| `12.35` \| `- **$\text{FAR}_A$ (Famil...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1326 | `11.55` | `...ts/experiment_log.md` \| 77 \| `11.55` \| `- **$\text{FAR}_B$ (True ...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1327 | `8.49` | `...ts/experiment_log.md` \| 78 \| `8.49` \| `- **False Rejection Rate ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1328 | `0.9490` | `...ts/experiment_log.md` \| 79 \| `0.9490` \| `- **AUROC:** Condition A:...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1328 | `0.9530` | `...\| `- **AUROC:** Condition A: $0.9530$; Condition B: $0.9490$.` \| 0...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1329 | `0.9490` | `...on A: $0.9530$; Condition B: $0.9490$.` \| 0.9530 (0.953018, AUROC_...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1329 | `0.9530` | `...ts/experiment_log.md` \| 79 \| `0.9530` \| `- **AUROC:** Condition A:...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1330 | `1.47` | `...ts/experiment_log.md` \| 87 \| `1.47` \| `...AR}_{\text{matched}}$)...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1331 | `2.67` | `...ts/experiment_log.md` \| 91 \| `2.67` \| `...roxy device): $\text{F...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1331 | `22.08` | `..._A = 2.67\%$, $\text{FAR}_B = 22.08\%$,...` \| 2.67% (0.026744, k=...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1332 | `2.67` | `...md` \| 91 \| `22.08` \| `..._A = 2.67\%$, $\text{FAR}_B = 22.08\%$,...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1332 | `22.08` | `...ts/experiment_log.md` \| 91 \| `22.08` \| `..._A = 2.67\%$, $\text{F...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1333 | `64%` | `....39\%$ ...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1333 | `19.41` | `...ts/experiment_log.md` \| 91 \| `19.41` \| `...08\%$, **$\Delta\text{...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1334 | `8.49` | `...ts/experiment_log.md` \| 94 \| `8.49` \| `...AR} = +2.08\%$, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1335 | `11.90` | `...ts/experiment_log.md` \| 95 \| `11.90` \| `...A = 11.34\%$, $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1335 | `11.34` | `....md` \| 95 \| `11.90` \| `...A = 11.34\%$, $\text{FAR}_B = 11.90\%$,...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1336 | `11.90` | `...A = 11.34\%$, $\text{FAR}_B = 11.90\%$,...` \| 11.34% (0.113422, e...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1336 | `11.34` | `...ts/experiment_log.md` \| 95 \| `11.34` \| `- $k=15$: $\text{FAR}_A =...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1337 | `8.49` | `...ts/experiment_log.md` \| 95 \| `8.49` \| `...AR} = +0.56\%$, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1338 | `64%` | `...ts/experiment_log.md` \| 98 \| `64%` \| `...e 48 ($65.69\%$), Devi...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1338 | `62.8%` | `..., Device 46 ($63.18\%$)...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1339 | `0.2097` | `...s/experiment_log.md` \| 100 \| `0.2097` \| `...earman Correlation:** ...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1339 | `0.1142` | `...tion:** $\rho = 0.2097$ ($p = 0.1142, n=58$ unique d...` \| 0.2097 ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1340 | `0.2097` | `...0.1142` \| `...tion:** $\rho = 0.2097$ ($p = 0.1142, n=58$ unique d...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1340 | `0.1142` | `...s/experiment_log.md` \| 100 \| `0.1142` \| `...tion:** $\rho = 0.2097...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1341 | `4.43` | `...s/experiment_log.md` \| 103 \| `4.43` \| `...penetration from $11.9...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1341 | `62.8%` | `...from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).` \| 4.43% (0.04...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1341 | `11.90` | `...4.43` \| `...penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ red...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1342 | `4.43` | `...2.8%` \| `...from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).` \|...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1342 | `62.8%` | `...s/experiment_log.md` \| 103 \| `62.8%` \| `...from $11.90\% \to 4.43...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1342 | `11.90` | `...` \| 103 \| `62.8%` \| `...from $11.90\% \to 4.43\%$ (a $62.8\%$ red...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1343 | `4.43` | `...penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ red...` \| 11.9...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1343 | `62.8%` | `...from $11.90\% \to 4.43\%$ (a $62.8\%$ red...` \| 11.90% (0.119046...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1343 | `11.90` | `...s/experiment_log.md` \| 103 \| `11.90` \| `...ue stranger penetratio...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1344 | `30.08` | `...s/experiment_log.md` \| 104 \| `30.08` \| `... Rate surges from $8.4...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1344 | `21.59` | `...9\% \to 30.08\%$ on average (+21.59 pp, pea...` \| 30.08% (0.30078...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1344 | `8.49` | `....08` \| `... Rate surges from $8.49\% \to 30.08\%$ on average (+2...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1345 | `30.08` | `...\| 104 \| `21.59` \| `...9\% \to 30.08\%$ on average (+21.59 pp, pea...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1345 | `21.59` | `...s/experiment_log.md` \| 104 \| `21.59` \| `...9\% \to 30.08\%$ on av...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1345 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$).` \| +21.59 pp (0.215929, ...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1346 | `30.08` | `... Rate surges from $8.49\% \to 30.08\%$ on average (+2...` \| 8.49%...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1346 | `8.49` | `...s/experiment_log.md` \| 104 \| `8.49` \| `...e Rejection Rate surge...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1347 | `21.59` | `...\| 104 \| `84.63` \| `...erage (+21.59 pp, peaking at $84.63\%$).` \|...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1347 | `84.63` | `...s/experiment_log.md` \| 104 \| `84.63` \| `...erage (+21.59 pp, peak...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1348 | `0.0327` | `...s/experiment_log.md` \| 107 \| `0.0327` \| `- **Naive Packet-Disjoint...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1348 | `0.0323` | `...s/experiment_log.md` \| 107 \| `0.0327` \| `- **Naive Packet-Disjoin...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1349 | `0.0327` | `...s/experiment_log.md` \| 107 \| `0.0323` \| `- **Naive Packet-Disjoin...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1349 | `0.0323` | `...s/experiment_log.md` \| 107 \| `0.0323` \| `- **Naive Packet-Disjoint...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1350 | `0.0327` | `...s/experiment_log.md` \| 108 \| `0.0327` \| `- **LOPO Absolute Error:*...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1350 | `0.0323` | `...s/experiment_log.md` \| 108 \| `0.0327` \| `- **LOPO Absolute Error:...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1351 | `0.0327` | `...s/experiment_log.md` \| 108 \| `0.0323` \| `- **LOPO Absolute Error:...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1351 | `0.0323` | `...s/experiment_log.md` \| 108 \| `0.0323` \| `- **LOPO Absolute Error:*...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1352 | `11.90` | `...s/experiment_log.md` \| 112 \| `11.90` \| `...ne ($L=1$):** $\text{F...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1352 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` \| 11.90% (0.119046...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1353 | `0.9490` | `...s/experiment_log.md` \| 112 \| `0.9490` \| `...} = +0.56\%$, $\text{A...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1354 | `11.90` | `...d` \| 112 \| `8.49` \| `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/NUMBER_OCCURRENCES.md` | 1354 | `8.49` | `...s/experiment_log.md` \| 112 \| `8.49` \| `...}_B = 11.90\%$, $\text...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1355 | `64%` | `...s/experiment_log.md` \| 113 \| `64%` \| `... +1.27\%$, $\text{AURO...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1355 | `62.8%` | `..., $\text{AUROC} = 0.9642$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1355 | `0.9642` | `...... +1.27\%$, $\text{AUROC} = 0.9642$.` \| 62.8% (62.7746% relative...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1356 | `11.22` | `...s/experiment_log.md` \| 113 \| `11.22` \| `...on ($L=3$):** $\text{F...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1356 | `4.37` | `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` \| 11.22% (0.112182...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1357 | `11.22` | `...d` \| 113 \| `4.37` \| `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1357 | `4.37` | `...s/experiment_log.md` \| 113 \| `4.37` \| `...}_B = 11.22\%$, $\text...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1358 | `64%` | `...xperiment_log.md` \| 113 \| `0.9642` \| `...} = +1.27\%$, $\text{...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1358 | `0.9642` | `...s/experiment_log.md` \| 113 \| `0.9642` \| `...} = +1.27\%$, $\text{A...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1359 | `64%` | `...s/experiment_log.md` \| 114 \| `64%` \| `...54\%$, $\Delta\text{FA...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1359 | `62.8%` | `..., $\text{AUROC} = 0.9670$.` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1359 | `0.9670` | `...} = +1.64\%$, $\text{AUROC} = 0.9670$.` \| 62.8% (62.7746% relative...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1360 | `64%` | `...54\%$, $\Delta\text{FAR} = +1.64...` \| 3.54% (0.035369, burst ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1360 | `3.54` | `...s/experiment_log.md` \| 114 \| `3.54` \| `...}_B = 10.45\%$, $\text...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1360 | `10.45` | `...d` \| 114 \| `3.54` \| `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1361 | `3.54` | `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` \| 10.45% (0.104538...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1361 | `10.45` | `...s/experiment_log.md` \| 114 \| `10.45` \| `...on ($L=5$):** $\text{F...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1362 | `64%` | `...\| 114 \| `0.9670` \| `...} = +1.64\%$, $\text{AUROC} = 0.9670$.`...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1362 | `0.9670` | `...s/experiment_log.md` \| 114 \| `0.9670` \| `...} = +1.64\%$, $\text{A...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1363 | `3.54` | `...s/experiment_log.md` \| 115 \| `3.54` \| `...ection by more than ha...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1364 | `64%` | `...lean fami...` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1364 | `0.9670` | `...s/experiment_log.md` \| 115 \| `0.9670` \| `...%$) while elevating AU...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1365 | `64%` | `...s/experiment_log.md` \| 123 \| `64%` \| `...re map \\| Contrastive ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1365 | `62.8%` | `...ype space) \\| **292 com...` \| 62.8% (62.7746% relative reduction ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1366 | `99.43` | `...s/experiment_log.md` \| 124 \| `99.43` \| `... \\| 93.85% \\| 96.2% \\|...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1367 | `0.9490` | `...s/experiment_log.md` \| 125 \| `0.9490` \| `... 90.23% \\| ≈ 92.5% \\| ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1367 | `0.9530` | `... 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` \| 0.9490 (0.9...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1368 | `0.9490` | `... `0.9530` \| `...\\| 91.3% \\| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1368 | `0.9530` | `...s/experiment_log.md` \| 125 \| `0.9530` \| `...\\| 91.3% \\| **0.9490 (...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1369 | `12.35` | `...s/experiment_log.md` \| 126 \| `12.35` \| `...t isolated \\| Not isol...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1370 | `11.55` | `...s/experiment_log.md` \| 127 \| `11.55` \| `...hold \\| Distance thres...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/NUMBER_OCCURRENCES.md` | 1371 | `2.67` | `...s/experiment_log.md` \| 128 \| `2.67` \| `...ted \\| **22.08%** (vs....` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1371 | `22.08` | `...\| 128 \| `2.67` \| `...ted \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 2...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1372 | `2.67` | `...ed \\| **22.08%** (vs. FAR_A = 2.67%) \\|` \| 22.08% (0.220808, k=1 ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1372 | `22.08` | `...s/experiment_log.md` \| 128 \| `22.08` \| `...evaluated \\| Not evalu...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1373 | `1.47` | `...s/experiment_log.md` \| 129 \| `1.47` \| `...reported \\| None repor...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/NUMBER_OCCURRENCES.md` | 1374 | `64%` | `...erfitti...` \| +19.41% (+0.194064, k=1 DeltaFAR mean) \| **VERIF...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1374 | `19.41` | `...s/experiment_log.md` \| 130 \| `19.41` \| `...reported \\| None repor...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/NUMBER_OCCURRENCES.md` | 1375 | `8.49` | `...s/experiment_log.md` \| 131 \| `8.49` \| `...≈ 6.15% \\| ≈ 5.5% \\| ≈...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1376 | `4.43` | `...s/experiment_log.md` \| 132 \| `4.43` \| `...t provided \\| Not prov...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1377 | `62.8%` | `...s/experiment_log.md` \| 132 \| `62.8%` \| `...-mean stranger penetra...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1378 | `30.08` | `...s/experiment_log.md` \| 133 \| `30.08` \| `...antified \\| Not quanti...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1378 | `21.59` | `...fied \\| **30.08%** (surge of +21.59 pp, peak 8...` \| 30.08% (0.30...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1379 | `30.08` | `...33 \| `21.59` \| `...ified \\| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1379 | `21.59` | `...s/experiment_log.md` \| 133 \| `21.59` \| `...ified \\| **30.08%** (s...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1379 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \\|` \| +21.59 pp (0.215929, e...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1380 | `21.59` | `... `84.63` \| `...%** (surge of +21.59 pp, peak 84.63%) \\|` \| 84.63%...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/NUMBER_OCCURRENCES.md` | 1380 | `84.63` | `...s/experiment_log.md` \| 133 \| `84.63` \| `...%** (surge of +21.59 p...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/NUMBER_OCCURRENCES.md` | 1381 | `3.54` | `...s/experiment_log.md` \| 134 \| `3.54` \| `...ted \\| Not evaluated \...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1381 | `0.9670` | `...ted \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 3.54% (0.035369, burs...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1382 | `64%` | `... 0.9670** \\|` \| 0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/NUMBER_OCCURRENCES.md` | 1382 | `3.54` | `...0.9670` \| `...ated \\| **FRR → 3.54%, AUROC → 0.9670** \\|` \| 0.967...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1382 | `0.9670` | `...s/experiment_log.md` \| 134 \| `0.9670` \| `...ated \\| **FRR → 3.54%,...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/NUMBER_OCCURRENCES.md` | 1383 | `0.2097` | `...s/experiment_log.md` \| 136 \| `0.2097` \| `...orted \\| None reported...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1383 | `0.1142` | `...reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0.2097 (Spearm...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1384 | `0.2097` | `...142` \| `... reported \\| **ρ = 0.2097 (p = 0.1142, n=58)** \\|` \| 0....` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1384 | `0.1142` | `...s/experiment_log.md` \| 136 \| `0.1142` \| `... reported \\| **ρ = 0.2...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/NUMBER_OCCURRENCES.md` | 1385 | `0.0327` | `...s/experiment_log.md` \| 137 \| `0.0327` \| `...evaluated \\| Not evalu...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1385 | `0.0323` | `...s/experiment_log.md` \| 137 \| `0.0327` \| `...evaluated \\| Not eval...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1386 | `0.0327` | `...s/experiment_log.md` \| 137 \| `0.0323` \| `...evaluated \\| Not eval...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/NUMBER_OCCURRENCES.md` | 1386 | `0.0323` | `...s/experiment_log.md` \| 137 \| `0.0323` \| `...evaluated \\| Not evalu...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/scan_numbers.py` | 29 | `4.17` | `(r'4\.17%?', "4.17", "4.43% (0.044315, episode mean)", "STALE / DISPROVED"),` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/scan_numbers.py` | 29 | `4.43` | `(r'4\.17%?', "4.17", "4.43% (0.044315, episode mean)", "STALE / DISPROVED"),` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/scan_numbers.py` | 30 | `4.43` | `(r'4\.43%?', "4.43", "4.43% (0.044315, episode mean)", "VERIFIED"),` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `audit/scan_numbers.py` | 31 | `30.18` | `(r'30\.18%?', "30.18", "30.08% (0.300789, episode mean)", "STALE / DISPROVED"),` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/scan_numbers.py` | 31 | `30.08` | `(r'30\.18%?', "30.18", "30.08% (0.300789, episode mean)", "STALE / DISPROVED"),` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/scan_numbers.py` | 32 | `30.08` | `(r'30\.08%?', "30.08", "30.08% (0.300789, episode mean)", "VERIFIED"),` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `audit/scan_numbers.py` | 33 | `21.69` | `(r'21\.69%?', "21.69", "+21.59 pp (0.215929, episo...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/scan_numbers.py` | 33 | `21.59` | `(r'21\.69%?', "21.69", "+21.59 pp (0.215929, episode mean di...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/scan_numbers.py` | 34 | `21.59` | `(r'21\.59%?', "21.59", "+21.59 pp (0.215929, episode mean difference)", "VERIFIED"),` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `audit/scan_numbers.py` | 35 | `64%` | `(r'64%?', "64%", "62.8% (62.7746% relative reduction in FAR_B)", "STALE / SPECULATIVE"),` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/scan_numbers.py` | 35 | `62.8%` | `(r'64%?', "64%", "62.8% (62.7746% relative reduction in FAR_B)", "STALE / SPECULATIVE"),` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/scan_numbers.py` | 36 | `62.8%` | `(r'62\.8%?', "62.8%", "62.8% (62.7746% relative reduction in FAR_B)", "VERIFIED"),` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `audit/scan_numbers.py` | 37 | `11.55` | `(r'11\.55%?', "11.55", "11.55% (device bootstrap m...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/scan_numbers.py` | 38 | `11.90` | `(r'11\.90%?', "11.90", "11.90% (0.119046, episode mean)", "VERIFIED (episode mean)"),` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/scan_numbers.py` | 39 | `12.35` | `(r'12\.35%?', "12.35", "12.35% (device bootstrap m...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `audit/scan_numbers.py` | 40 | `11.34` | `(r'11\.34%?', "11.34", "11.34% (0.113422, episode mean FAR_A L=1)", "VERIFIED (episode mean)"),` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `audit/scan_numbers.py` | 41 | `2.67` | `(r'2\.67%?', "2.67", "2.67% (0.026744, k=1 FAR_A mean)", "VERIFIED (sweep k=1)"),` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/scan_numbers.py` | 42 | `22.08` | `(r'22\.08%?', "22.08", "22.08% (0.220808, k=1 FAR_B mean)", "VERIFIED (sweep k=1)"),` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/scan_numbers.py` | 43 | `64%` | `(r'19\.41%?', "19.41", "+19.41% (+0.194064, k=1 DeltaFAR mean)", "VERIFIED (sweep k=1)"),` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/scan_numbers.py` | 43 | `19.41` | `(r'19\.41%?', "19.41", "+19.41% (+0.194064, k=1 DeltaFAR mean)", "VERIFIED (sweep k=1)"),` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/scan_numbers.py` | 44 | `99.43` | `(r'99\.43%?', "99.43", "99.43% (0.994270, macro-F1 mean)", "VERIFIED (stats summary)"),` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `audit/scan_numbers.py` | 45 | `0.9490` | `(r'0\.9490?', "0.9490", "0.9490 (0.948982, AUROC_B episode mean)", "VERIFIED (stats summary)"),` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `audit/scan_numbers.py` | 46 | `0.9530` | `(r'0\.9530?', "0.9530", "0.9530 (0.953018, AUROC_A episode mean)", "VERIFIED (stats summary)"),` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `audit/scan_numbers.py` | 47 | `8.49` | `(r'8\.49%?', "8.49", "8.49% (0.084860, FRR episode mean)", "VERIFIED (stats summary)"),` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/scan_numbers.py` | 48 | `98.5` | `(r'98\.5%?', "98.5", "STALE: single-episode held...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `audit/scan_numbers.py` | 48 | `65.7` | `...49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 10...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/scan_numbers.py` | 49 | `65.7` | `(r'65\.7%?', "65.7", "65.69% (0.656944, device 48 mean FAR_B)", "VERIFIED (per-device ranking)"),` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `audit/scan_numbers.py` | 50 | `0.2097` | `(r'0\.2097?', "0.2097", "0.2097 (Spearman rho, n=58...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `audit/scan_numbers.py` | 51 | `0.1142` | `(r'0\.1142?', "0.1142", "0.1142 (Spearman p-value, n=58)", "VERIFIED (neighbour analysis)"),` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `audit/scan_numbers.py` | 52 | `0.0327` | `(r'0\.0327?', "0.0327", "0.0327 (LOPO absolute error)", "VERIFIED (LOPO bias)"),` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/scan_numbers.py` | 52 | `0.0323` | `(r'0\.0327?', "0.0327", "0.0327 (LOPO absolute error)", "VERIFIED (LOPO bias)"),` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/scan_numbers.py` | 53 | `0.0327` | `(r'0\.0323?', "0.0323", "0.0323 (Naive packet-disjoint absolute error)", "VERIFIED (LOPO bias)"),` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `audit/scan_numbers.py` | 53 | `0.0323` | `(r'0\.0323?', "0.0323", "0.0323 (Naive packet-disjoint absolute error)", "VERIFIED (LOPO bias)"),` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `audit/scan_numbers.py` | 54 | `1.47` | `(r'1\.47%?', "1.47", "+1.47% (device-matched Del...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `audit/scan_numbers.py` | 55 | `3.54` | `(r'3\.54%?', "3.54", "3.54% (0.035369, burst L=5 FRR at tau_Youden)", "VERIFIED (burst summary)"),` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/scan_numbers.py` | 56 | `10.45` | `(r'10\.45%?', "10.45", "10.45% (0.104538, burst L=...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/scan_numbers.py` | 57 | `11.22` | `(r'11\.22%?', "11.22", "11.22% (0.112182, burst L=...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/scan_numbers.py` | 58 | `4.37` | `(r'4\.37%?', "4.37", "4.37% (0.043740, burst L=3 FRR at tau_Youden)", "VERIFIED (burst summary)"),` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/scan_numbers.py` | 59 | `64%` | `(r'0\.9642?', "0.9642", "0.9642 (0.9642...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/scan_numbers.py` | 59 | `0.9642` | `(r'0\.9642?', "0.9642", "0.9642 (0.964244, burst L=...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/scan_numbers.py` | 60 | `64%` | `...0?', "0.9670", "0.9670 (0.966964, burst L=5 AUROC at tau_Youde...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/scan_numbers.py` | 60 | `0.9670` | `(r'0\.9670?', "0.9670", "0.9670 (0.966964, burst L=...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/scan_numbers.py` | 61 | `84.63` | `(r'84\.63%?', "84.63", "84.63% (0.846310, episode ...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 50 | `84.63` | `f"(README claims 84.63%)")` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 75 | `11.55` | `print(f"    → README claims 11.55% — this is the DEVICE-LEVEL bootstrap mean "` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 81 | `11.90` | `print(f"    mean = {mean_far_youden:.4f}%  → User's recomputed value: 11.90%")` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/TASK1_numbers.py` | 87 | `8.49` | `print(f"    mean = {row_frr['mean']*100:.4f}%  → README claims 8.49%")` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/TASK1_numbers.py` | 92 | `4.17` | `print(f"    mean = {mean_far_robust:.4f}%  → README claims 4.17%")` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 97 | `30.18` | `print(f"    mean = {mean_frr_robust:.4f}%  → README claims 30.18%")` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 102 | `0.9670` | `print(f"    value = {auroc_l5:.6f}  → README claims 0.9670")` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 107 | `3.54` | `print(f"    value = {frr_l5:.4f}%  → README claims 3.54%")` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 112 | `10.45` | `print(f"    value = {farb_l5:.4f}%  → README claims 10.45%")` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 114 | `84.63` | `# Peak 84.63%: check episode 4` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 115 | `84.63` | `print(f"\n  Peak FRR_robust (84.63% claim):")` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 117 | `84.63` | `f"→ README claims 84.63%")` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 131 | `11.55` | `"11.55%", f"{row_farb['mean']*100:.2f}%",` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 134 | `11.55` | `"MISMATCH" if abs(row_farb['mean']*100 - 11.55) > 0.005 else "PASS"),` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 137 | `11.55` | `"11.55%", f"{mean_far_youden:.2f}%",` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 143 | `4.17` | `"4.17%", f"{mean_far_robust:.2f}%",` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 146 | `4.17` | `"MISMATCH" if abs(mean_far_robust - 4.17) > 0.005 else "PASS"),` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 149 | `8.49` | `"8.49%", f"{row_frr['mean']*100:.2f}%",` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/TASK1_numbers.py` | 152 | `8.49` | `"PASS" if abs(row_frr['mean']*100 - 8.49) < 0.01 else "MISMATCH"),` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/TASK1_numbers.py` | 155 | `30.18` | `"30.18%", f"{mean_frr_robust:.2f}%",` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 158 | `30.18` | `"MISMATCH" if abs(mean_frr_robust - 30.18) > 0.05 else "PASS"),` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 161 | `84.63` | `"84.63%", f"{tt['FRR_robust'].max()*100:.2f}%",` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 164 | `84.63` | `"PASS" if abs(tt['FRR_robust'].max()*100 - 84.63) < 0.01 else "MISMATCH"),` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 167 | `3.54` | `"3.54%", f"{frr_l5:.2f}%",` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 170 | `3.54` | `"PASS" if abs(frr_l5 - 3.54) < 0.01 else "MISMATCH"),` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 173 | `0.9670` | `"0.9670", f"{auroc_l5:.4f}",` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 176 | `0.9670` | `"PASS" if abs(auroc_l5 - 0.9670) < 0.001 else "MISMATCH"),` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 179 | `10.45` | `"10.45%", f"{farb_l5:.2f}%",` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 182 | `10.45` | `"PASS" if abs(farb_l5 - 10.45) < 0.01 else "MISMATCH"),` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 191 | `11.55` | `README/abstract FAR_B = 11.55% uses DEVICE-LEVEL bootstrap mean` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 197 | `4.17` | `For FAR_B robust (4.17% vs {mean_far_robust:.2f}%): same mismatch — no device-level value` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 200 | `11.55` | `is used. If 11.55% (device-level) is used for baseline, then FAR_true_robust` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 238 | `64%` | `# "drops intrusion by 64%"` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/TASK1_numbers.py` | 239 | `11.55` | `readme_farb_base   = 11.55` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 240 | `4.17` | `readme_farb_robust = 4.17` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 246 | `64%` | `print(f"\n  'Drops intrusion by 64%' claim:")` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/TASK1_numbers.py` | 250 | `64%` | `...lue {readme_reduction:.1f}% ≠ 64%; correct under README numbers...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/TASK1_numbers.py` | 252 | `21.69` | `# "FRR surge of +21.69%"` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/TASK1_numbers.py` | 253 | `8.49` | `readme_frr_base   = 8.49` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/TASK1_numbers.py` | 254 | `30.18` | `readme_frr_robust = 30.18` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 258 | `21.69` | `print(f"\n  'FRR surge of +21.69%' claim:")` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/TASK1_numbers.py` | 261 | `21.69` | `...SS' if abs(readme_frr_surge - 21.69) < 0.005 else 'MISMATCH'}")` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/TASK1_numbers.py` | 277 | `11.90` | `print(f"  → FAR_B DECREASES slightly (11.90% → 10.45%) while FAR_A also decreases,")` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `audit/TASK1_numbers.py` | 277 | `10.45` | `print(f"  → FAR_B DECREASES slightly (11.90% → 10.45%) while FAR_A also decreases,")` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 324 | `11.55` | `{'FAR_B baseline':<42} \| {'11.55%':>8} \| {f'{stats_farb_mean:.2...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 325 | `11.55` | `... baseline (ep mean)':<42} \| {'11.55%':>8} \| {f'{ep_mean_farb:.2f}%...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `audit/TASK1_numbers.py` | 326 | `4.17` | `{'FAR_B robust':<42} \| {'4.17%':>8} \| {f'{mean_far_robust:.2...` | 4.43% (0.044315, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 327 | `8.49` | `{'FRR baseline':<42} \| {'8.49%':>8} \| {f'{stats_frr_mean:.2f...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `audit/TASK1_numbers.py` | 328 | `30.18` | `...RR robust (ep mean)':<42} \| {'30.18%':>8} \| {f'{mean_frr_robust:.2...` | 30.08% (0.300789, episode mean) | **STALE / DISPROVED** |
| `audit/TASK1_numbers.py` | 329 | `84.63` | `{'Peak FRR_robust':<42} \| {'84.63%':>8} \| {f'{tt["FRR_robust"].m...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `audit/TASK1_numbers.py` | 330 | `3.54` | `{'Burst L=5 FRR':<42} \| {'3.54%':>8} \| {f'{frr_l5:.2f}%':>10}...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 331 | `0.9670` | `{'Burst L=5 AUROC':<42} \| {'0.9670':>8} \| {f'{auroc_l5:.4f}':>10...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 332 | `10.45` | `{'Burst L=5 FAR_B':<42} \| {'10.45%':>8} \| {f'{farb_l5:.2f}%':>10...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `audit/TASK1_numbers.py` | 333 | `64%` | `{'Intrusion drop ~64%':<42} \| {'~64%':>8} \| {f'{ep_...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `audit/TASK1_numbers.py` | 334 | `21.69` | `{'FRR surge +21.69pp':<42} \| {'+21.69pp':>8} \| {...` | +21.59 pp (0.215929, episode mean difference) | **STALE / DISPROVED (when claimed as surge)** |
| `audit/verify_sweep.py` | 23 | `2.67` | `# k=1: single-proxy distortion gap — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/verify_sweep.py` | 23 | `22.08` | `# k=1: single-proxy distortion gap — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/verify_sweep.py` | 23 | `19.41` | `# k=1: single-proxy distortion gap — README says +19.41%, FAR_A=2.67%, FAR_B=22.08%` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `audit/verify_sweep.py` | 24 | `2.67` | `print("README claims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `audit/verify_sweep.py` | 24 | `22.08` | `print("README claims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `audit/verify_sweep.py` | 24 | `19.41` | `print("README claims k=1: FAR_A=2.67%, FAR_B=22.08%, gap=+19.41%")` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/abstract.md` | 5 | `2.67` | `...sting reports $\text{FAR}_A = 2.67\%$, but true physical strange...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/abstract.md` | 5 | `22.08` | `... penetrate at $\text{FAR}_B = 22.08\%$. This distortion stabilize...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/abstract.md` | 5 | `19.41` | `...($k=1$) creates a dangerous $+19.41\%$ blind spot**: familiar tes...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/abstract.md` | 5 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ ($95\%$ device-level boots...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/abstract.md` | 7 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/abstract.md` | 7 | `30.08` | `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting ne...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/abstract.md` | 7 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting nearly 1 in 3...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/abstract.md` | 7 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), but the False ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/abstract.md` | 7 | `11.55` | `... $0.949$ with $\text{FAR}_B = 11.55\%$ [device-level bootstrap: $...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/abstract.md` | 7 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/abstract.md` | 7 | `99.43` | `...-set classification achieves $99.43\%$ macro-$F_1$, the open-set ...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/abstract.md` | 7 | `0.9490` | `...$F_1$, the open-set AUROC of $0.949$ with $\text{FAR}_B = 11.55\%...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/abstract.md` | 7 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) —...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/abstract.md` | 7 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `paper/literature_comparison.csv` | 4 | `64%` | `...eature map,Contrastive latent,64 (prototype space),292 complex...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/literature_comparison.csv` | 5 | `99.43` | `Closed-Set Accuracy / F1,~95.33%,~98% (same day),93.85%,96.2%,94.7%,99.43% +/- 0.24% Macro-F1` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/literature_comparison.csv` | 6 | `0.9490` | `...80% - 98%,90.23%,~92.5%,91.3%,0.9490 (AUROC_B) / 0.9530 (AUROC_A)` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/literature_comparison.csv` | 6 | `0.9530` | `...2.5%,91.3%,0.9490 (AUROC_B) / 0.9530 (AUROC_A)` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `paper/literature_comparison.csv` | 7 | `12.35` | `...ted,Not isolated,Not isolated,12.35% (95% CI: [7.01%, 18.77%])` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/literature_comparison.csv` | 8 | `11.55` | `... threshold,Distance threshold,11.55% (95% CI: [7.03%, 16.53%])` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/literature_comparison.csv` | 9 | `2.67` | `...evaluated,22.08% (vs. FAR_A = 2.67%)` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/literature_comparison.csv` | 9 | `22.08` | `...d,Not evaluated,Not evaluated,22.08% (vs. FAR_A = 2.67%)` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/literature_comparison.csv` | 10 | `1.47` | `...,None reported,None reported,+1.47% (95% CI: [+0.72%, +2.40%] mat...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/literature_comparison.csv` | 11 | `19.41` | `...,None reported,None reported,+19.41% (severe threshold overfitting...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/literature_comparison.csv` | 12 | `8.49` | `... trade-off,~6.15%,~5.5%,~7.2%,8.49% (95% CI: [7.16%, 10.06%])` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/literature_comparison.csv` | 13 | `4.43` | `...ded,Not provided,Not provided,4.43% (reduces episode-mean strange...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/literature_comparison.csv` | 13 | `62.8%` | `...-mean stranger penetration by 62.8%)` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/literature_comparison.csv` | 14 | `30.08` | `...Not quantified,Not quantified,30.08% (surge of +21.59 pp, peak 84....` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/literature_comparison.csv` | 14 | `21.59` | `... quantified,30.08% (surge of +21.59 pp, peak 84.63%)` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/literature_comparison.csv` | 14 | `84.63` | `...08% (surge of +21.59 pp, peak 84.63%)` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `paper/literature_comparison.csv` | 15 | `3.54` | `...valuated,Not evaluated,FRR -> 3.54%, AUROC -> 0.9670` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/literature_comparison.csv` | 15 | `0.9670` | `...luated,FRR -> 3.54%, AUROC -> 0.9670` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/literature_comparison.csv` | 17 | `0.2097` | `... reported,None reported,rho = 0.2097 (p = 0.1142, n=58)` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/literature_comparison.csv` | 17 | `0.1142` | `...ne reported,rho = 0.2097 (p = 0.1142, n=58)` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/literature_comparison.csv` | 18 | `0.0327` | `...d,Not evaluated,Not evaluated,0.0327 (LOPO) vs 0.0323 (Naive)` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/literature_comparison.csv` | 18 | `0.0323` | `...d,Not evaluated,Not evaluated,0.0327 (LOPO) vs 0.0323 (Naive)` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/main.tex` | 31 | `2.67` | `...sting reports $\text{FAR}_A = 2.67\%$, but true physical strange...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 31 | `22.08` | `... penetrate at $\text{FAR}_B = 22.08\%$. This distortion stabilize...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 31 | `19.41` | `...($k=1$) creates a dangerous $+19.41\%$ blind spot}: familiar test...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 31 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ ($95\%$ device-level boots...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/main.tex` | 33 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), bu...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/main.tex` | 33 | `30.08` | `...Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 33 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84.63\%$)---r...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/main.tex` | 33 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), but the False ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/main.tex` | 33 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/main.tex` | 33 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 33 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `paper/main.tex` | 33 | `3.54` | `...ate meter false rejection to $3.54\%$ (availability $96.46\%$) w...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 33 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$. Device-mean $\text{FAR}_B$ ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 33 | `84.63` | `...08\%$ (+21.59 pp, peaking at $84.63\%$)---rejecting nearly 1 in 3...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `paper/main.tex` | 57 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ ($95\%$ device-level boots...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/main.tex` | 58 | `11.55` | `...%, 18.77\%]$; $\text{FAR}_B = 11.55\%$, $95\%$ CI: $[7.03\%, 16.5...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/main.tex` | 58 | `12.35` | `...transmitters ($\text{FAR}_A = 12.35\%$, $95\%$ CI: $[7.01\%, 18.7...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/main.tex` | 59 | `2.67` | `...optimism gap ($\text{FAR}_A = 2.67\%$ vs. $\text{FAR}_B = 22.08\...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 59 | `22.08` | `...= 2.67\%$ vs. $\text{FAR}_B = 22.08\%$).` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 59 | `19.41` | `...ion ($k=1$) incurs an acute $+19.41\%$ optimism gap ($\text{FAR}_...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 60 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `paper/main.tex` | 61 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/main.tex` | 61 | `30.08` | `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 61 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/main.tex` | 61 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but imposes a s...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/main.tex` | 61 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/main.tex` | 61 | `8.49` | `...ity penalty (FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 62 | `0.0327` | `...le to naive testing ($\approx 0.032$ vs $0.033$).` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/main.tex` | 62 | `0.0323` | `...le to naive testing ($\approx 0.032$ vs $0.033$).` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/main.tex` | 81 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$) free from device-composit...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/main.tex` | 83 | `19.41` | `...on ($k=1$) induces an acute $+19.41\%$ familiarity gap and establ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 84 | `30.08` | `...bust}}$), revealing a severe $30.08\%$ false rejection rate in sm...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 119 | `99.43` | `...achieving $\text{macro-}F_1 = 99.43\% \pm 0.24\%$.` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 143 | `12.35` | `\item $\text{FAR}_A$ (Familiar Strangers): $12.35\%$ ($95\%$ CI: $[7.01\%, 18.77\%]$)` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/main.tex` | 144 | `11.55` | `\item $\text{FAR}_B$ (True Strangers): $11.55\%$ ($95\%$ CI: $[7.03\%, 16.53\%]$)` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/main.tex` | 146 | `8.49` | `\item Mean False Rejection Rate ($\text{FRR}$): $8.49\%$ ($95\%$ CI: $[7.16\%, 10.06\%]$)` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 147 | `99.43` | `\item Closed-set macro-$F_1$: $99.43\%$, open-set AUROC: $0.9490$.` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 147 | `0.9490` | `\item Closed-set macro-$F_1$: $99.43\%$, open-set AUROC: $0.9490$.` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 161 | `64%` | `...re map & Contrastive latent & 64 (prototype) & \textbf{292 bas...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/main.tex` | 162 | `99.43` | `...$96.2\%$ & $94.7\%$ & \textbf{99.43\% $\pm$ 0.24\%} \\` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 163 | `0.9490` | `... 92.5\%$ & $91.3\%$ & \textbf{0.9490 (AUROC$_B$)} \\` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 164 | `12.35` | `...ated & Not isolated & \textbf{12.35\% [7.0\%, 18.8\%]} \\` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/main.tex` | 165 | `11.55` | `.... & Distance thres. & \textbf{11.55\% [7.0\%, 16.5\%]} \\` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/main.tex` | 166 | `2.67` | `...f{22.08\% (vs $\text{FAR}_A = 2.67\%$)} \\` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 166 | `22.08` | `...ted & Not evaluated & \textbf{22.08\% (vs $\text{FAR}_A = 2.67\%$...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 167 | `1.47` | `...ed & None reported & \textbf{+1.47\% (matched CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/main.tex` | 168 | `19.41` | `...ed & None reported & \textbf{+19.41\% (acute distortion)} \\` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 169 | `8.49` | `...$ & $\approx 7.2\%$ & \textbf{8.49\% [7.16\%, 10.06\%]} \\` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 170 | `4.43` | `...ided & Not provided & \textbf{4.43\% (reduces penetration by 62....` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/main.tex` | 170 | `62.8%` | `....43\% (reduces penetration by 62.8\%)} \\` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/main.tex` | 171 | `30.08` | `...ed & Not quantified & \textbf{30.08\% (FRR surge $+21.59$ pp)} \\` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 171 | `21.59` | `... \textbf{30.08\% (FRR surge $+21.59$ pp)} \\` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/main.tex` | 172 | `3.54` | `...ted & \textbf{$\text{FRR} \to 3.54\%$, $\text{AUROC} \to 0.9670$...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 172 | `0.9670` | `...to 3.54\%$, $\text{AUROC} \to 0.9670$} \\` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 174 | `0.2097` | `...ne reported & \textbf{$\rho = 0.2097$ ($p = 0.1142, n=58$)} \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/main.tex` | 174 | `0.1142` | `...\textbf{$\rho = 0.2097$ ($p = 0.1142, n=58$)} \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/main.tex` | 184 | `1.47` | `..._{\text{matched}}$: \textbf{$+1.47\%$} ($95\%$ device bootstrap ...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/main.tex` | 199 | `2.67` | `...esting yields $\text{FAR}_A = 2.67\%$, yet true stranger penetra...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 199 | `22.08` | `...enetration is $\text{FAR}_B = 22.08\%$---an extreme optimism gap ...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 199 | `19.41` | `...m gap of $\Delta\text{FAR} = +19.41\%$.` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 228 | `11.90` | `...ine ($L=1$):} $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/main.tex` | 228 | `0.9490` | `...} = +0.56\%$, $\text{AUROC} = 0.9490$.` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 228 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\Delta\text{FAR} = +0.56...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 229 | `64%` | `... +1.27\%$, $\text{AUROC} = 0.9642$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/main.tex` | 229 | `11.22` | `...ion ($L=3$):} $\text{FAR}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 229 | `4.37` | `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\Delta\text{FAR} = +1.27...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 229 | `0.9642` | `...} = +1.27\%$, $\text{AUROC} = 0.9642$.` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 230 | `64%` | `...54\%$, $\Delta\text{FAR} = +1.64\%$, $\text{AUROC} = 0.9670$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/main.tex` | 230 | `3.54` | `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\Delta\text{FAR} = +1.64...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 230 | `10.45` | `...ion ($L=5$):} $\text{FAR}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 230 | `0.9670` | `...} = +1.64\%$, $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 232 | `64%` | `...omes clearer ($+0.56\% \to +1.64\%$).` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/main.tex` | 232 | `8.49` | `...tion by more than half (from $8.49\%$ down to $3.54\%$), elevati...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 232 | `3.54` | `... half (from $8.49\%$ down to $3.54\%$), elevating legitimate gat...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/main.tex` | 235 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `paper/main.tex` | 239 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/main.tex` | 239 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/main.tex` | 239 | `11.90` | `...ue stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/main.tex` | 240 | `30.08` | `...$) to surge from $8.49\%$ to $30.08\%$ on average (+21.59 pp, pea...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 240 | `21.59` | `...\%$ to $30.08\%$ on average (+21.59 pp, peaking at $84.63\%$).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/main.tex` | 240 | `8.49` | `...($\text{FRR}$) to surge from $8.49\%$ to $30.08\%$ on average (+...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/main.tex` | 240 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$).` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `paper/main.tex` | 247 | `19.41` | `...e single-device distortion ($+19.41\%$).` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 248 | `30.08` | `...g introduces an unacceptable $30.08\%$ availability penalty in ba...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 254 | `30.08` | `...e transmission to reduce the $30.08\%$ FRR penalty.` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 260 | `30.08` | `...y cost of robust thresholds ($30.08\%$ FRR). These results establ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/main.tex` | 260 | `19.41` | `...2\%, +2.40\%]$), scaling to $+19.41\%$ for single-proxy calibrati...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/main.tex` | 260 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/related_work_table.md` | 26 | `64%` | `...re map \| Contrastive latent \| 64 (prototype space) \| **292 com...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/related_work_table.md` | 27 | `99.43` | `... \| 93.85% \| 96.2% \| 94.7% \| **99.43% ± 0.24% Macro-F1** \|` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/related_work_table.md` | 28 | `0.9490` | `... 90.23% \| ≈ 92.5% \| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/related_work_table.md` | 28 | `0.9530` | `...\| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)** \|` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `paper/related_work_table.md` | 29 | `12.35` | `...t isolated \| Not isolated \| **12.35%** (95% CI: [7.01%, 18.77%]) \|` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/related_work_table.md` | 30 | `11.55` | `...hold \| Distance threshold \| **11.55%** (95% CI: [7.03%, 16.53%]) \|` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/related_work_table.md` | 31 | `2.67` | `...ted \| **22.08%** (vs. FAR_A = 2.67%) \|` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/related_work_table.md` | 31 | `22.08` | `...evaluated \| Not evaluated \| **22.08%** (vs. FAR_A = 2.67%) \|` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/related_work_table.md` | 32 | `1.47` | `...reported \| None reported \| **+1.47%** (95% CI: [+0.72%, +2.40%] m...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/related_work_table.md` | 33 | `19.41` | `...reported \| None reported \| **+19.41%** (severe threshold overfitti...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/related_work_table.md` | 34 | `8.49` | `...≈ 6.15% \| ≈ 5.5% \| ≈ 7.2% \| **8.49%** (95% CI: [7.16%, 10.06%]) \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/related_work_table.md` | 35 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/related_work_table.md` | 35 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/related_work_table.md` | 36 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/related_work_table.md` | 36 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/related_work_table.md` | 36 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `paper/related_work_table.md` | 37 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/related_work_table.md` | 37 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/related_work_table.md` | 39 | `0.2097` | `...orted \| None reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/related_work_table.md` | 39 | `0.1142` | `... reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/related_work_table.md` | 40 | `0.0327` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/related_work_table.md` | 40 | `0.0323` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 18 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ ($95\%$ device-level boots...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/sections/paper_draft.md` | 19 | `11.55` | `...%, 18.77\%]$; $\text{FAR}_B = 11.55\%$, $95\%$ CI: $[7.03\%, 16.5...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/sections/paper_draft.md` | 19 | `12.35` | `...transmitters ($\text{FAR}_A = 12.35\%$, $95\%$ CI: $[7.01\%, 18.7...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/sections/paper_draft.md` | 20 | `2.67` | `...optimism gap ($\text{FAR}_A = 2.67\%$ vs. $\text{FAR}_B = 22.08\...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 20 | `22.08` | `...= 2.67\%$ vs. $\text{FAR}_B = 22.08\%$).` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 20 | `19.41` | `...ion ($k=1$) incurs an acute $+19.41\%$ optimism gap ($\text{FAR}_...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 21 | `65.7` | `...R}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episod...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `paper/sections/paper_draft.md` | 22 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 22 | `30.08` | `...(FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 22 | `21.59` | `...om $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 22 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but imposes a s...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 22 | `11.90` | `...ue-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/sections/paper_draft.md` | 22 | `8.49` | `...ity penalty (FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 23 | `0.0327` | `...le to naive testing ($\approx 0.032$ vs $0.033$).` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 23 | `0.0323` | `...le to naive testing ($\approx 0.032$ vs $0.033$).` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 39 | `64%` | `...re map \| Contrastive latent \| 64 (prototype space) \| **292 com...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/sections/paper_draft.md` | 40 | `99.43` | `... \| 93.85% \| 96.2% \| 94.7% \| **99.43% ± 0.24% Macro-F1** \|` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 41 | `0.9490` | `... 90.23% \| ≈ 92.5% \| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 41 | `0.9530` | `...\| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)** \|` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 42 | `12.35` | `...t isolated \| Not isolated \| **12.35%** (95% CI: [7.01%, 18.77%]) \|` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/sections/paper_draft.md` | 43 | `11.55` | `...hold \| Distance threshold \| **11.55%** (95% CI: [7.03%, 16.53%]) \|` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/sections/paper_draft.md` | 44 | `2.67` | `...ted \| **22.08%** (vs. FAR_A = 2.67%) \|` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 44 | `22.08` | `...evaluated \| Not evaluated \| **22.08%** (vs. FAR_A = 2.67%) \|` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 45 | `1.47` | `...reported \| None reported \| **+1.47%** (95% CI: [+0.72%, +2.40%] m...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/sections/paper_draft.md` | 46 | `19.41` | `...reported \| None reported \| **+19.41%** (severe threshold overfitti...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 47 | `8.49` | `...≈ 6.15% \| ≈ 5.5% \| ≈ 7.2% \| **8.49%** (95% CI: [7.16%, 10.06%]) \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 48 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 48 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 49 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 49 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 49 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `paper/sections/paper_draft.md` | 50 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 50 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 52 | `0.2097` | `...orted \| None reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/sections/paper_draft.md` | 52 | `0.1142` | `... reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/sections/paper_draft.md` | 53 | `0.0327` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 53 | `0.0323` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 59 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$) free from device-composit...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/sections/paper_draft.md` | 61 | `19.41` | `...on ($k=1$) induces an acute $+19.41\%$ familiarity gap and establ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 62 | `30.08` | `...bust}}$), revealing a severe $30.08\%$ false rejection rate that ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 93 | `99.43` | `...achieving $\text{macro-}F_1 = 99.43\% \pm 0.24\%$.` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 112 | `12.35` | `...angers)** \| Device ($n=60$) \| 12.35\% \| [7.01\%, 18.77\%] \| 4.84\...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `paper/sections/paper_draft.md` | 113 | `11.55` | `...angers)** \| Device ($n=58$) \| 11.55\% \| [7.03\%, 16.53\%] \| 6.55\...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `paper/sections/paper_draft.md` | 115 | `8.49` | `... (FRR)** \| Episode ($n=20$) \| 8.49\% \| [7.16\%, 10.06\%] \| 3.40\...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 116 | `0.9530` | `...ion A)** \| Episode ($n=20$) \| 0.9530 \| [0.9413, 0.9625] \| 0.0240 \|...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 117 | `0.9490` | `...ion B)** \| Episode ($n=20$) \| 0.9490 \| [0.9367, 0.9605] \| 0.0284 \|...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 120 | `98.5` | `...ne hardness (from $0.0\%$ to $98.5\%$), naive episode-level subt...` | STALE: single-episode held-out proxy FAR (ep 7, dev 49). Device-mean FAR_B max is 65.7% (dev 48). Single-ep max is 100%. | **STALE / MISLEADING** |
| `paper/sections/paper_draft.md` | 126 | `1.47` | `...AR}_{\text{matched}}$):** **$+1.47\%$** ($95\%$ device-level boo...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/sections/paper_draft.md` | 133 | `2.67` | `...testing shows $\text{FAR}_A = 2.67\%$, while true strangers pene...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 133 | `22.08` | `... penetrate at $\text{FAR}_B = 22.08\%$, creating an extreme optim...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 133 | `19.41` | `...gap of **$\Delta\text{FAR} = +19.41\%$**.` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 138 | `64%` | `...:** Devices 48 (65.69\%), 50 (64.66\%), 46 (63.18\%), 49 (47.1...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/sections/paper_draft.md` | 140 | `0.2097` | `...nrolled neighbours is $\rho = 0.2097$ ($p = 0.1142, n=58$ unique p...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/sections/paper_draft.md` | 140 | `0.1142` | `...ours is $\rho = 0.2097$ ($p = 0.1142, n=58$ unique physical device...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/sections/paper_draft.md` | 144 | `4.43` | `...ation from $11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, wit...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 144 | `62.8%` | `...11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, with 4 episodes...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 144 | `11.90` | `...ue-stranger penetration from $11.90\%$ down to $4.43\%$ (a $62.8\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/sections/paper_draft.md` | 145 | `30.08` | `...te surges from $8.49\%$ to **$30.08\%$** on average (+21.59 pp, p...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 145 | `21.59` | `...to **$30.08\%$** on average (+21.59 pp, peaking at $84.63\%$). De...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 145 | `8.49` | `...e Rejection Rate surges from $8.49\%$ to **$30.08\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 145 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$). Deploying $\tau_{\text{r...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `paper/sections/paper_draft.md` | 148 | `0.0327` | `...absolute estimation error of $0.0327$, compared to naive packet-di...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 148 | `0.0323` | `...absolute estimation error of $0.0327$, compared to naive packet-d...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/sections/paper_draft.md` | 152 | `11.90` | `...ne ($L=1$):** $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/sections/paper_draft.md` | 152 | `0.9490` | `...} = +0.56\%$, $\text{AUROC} = 0.9490$.` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 152 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\Delta\text{FAR} = +0.56...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 153 | `64%` | `... +1.27\%$, $\text{AUROC} = 0.9642$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/sections/paper_draft.md` | 153 | `11.22` | `...on ($L=3$):** $\text{FAR}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 153 | `4.37` | `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\Delta\text{FAR} = +1.27...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 153 | `0.9642` | `...} = +1.27\%$, $\text{AUROC} = 0.9642$.` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 154 | `64%` | `...54\%$, $\Delta\text{FAR} = +1.64\%$, $\text{AUROC} = 0.9670$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/sections/paper_draft.md` | 154 | `3.54` | `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\Delta\text{FAR} = +1.64...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 154 | `10.45` | `...on ($L=5$):** $\text{FAR}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 154 | `0.9670` | `...} = +1.64\%$, $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 156 | `64%` | `...omes clearer ($+0.56\% \to +1.64\%$).` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/sections/paper_draft.md` | 156 | `8.49` | `...tion by more than half (from $8.49\%$ down to $3.54\%$), elevati...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 156 | `3.54` | `... half (from $8.49\%$ down to $3.54\%$), elevating legitimate gat...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/sections/paper_draft.md` | 165 | `19.41` | `...catastrophic optimism gaps ($+19.41\%$).` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 166 | `0.9490` | `... With open-set AUROC $\approx 0.949$ and FRR/FAR trade-offs of $8...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/sections/paper_draft.md` | 180 | `30.08` | `...ed receivers to suppress the $30.08\%$ availability penalty of ro...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 188 | `30.08` | `...y cost of robust thresholds ($30.08\%$ FRR). These results demons...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `paper/sections/paper_draft.md` | 188 | `19.41` | `...2\%, +2.40\%]$), scaling to $+19.41\%$ when only a single proxy d...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `paper/sections/paper_draft.md` | 188 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2....` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `paper/tables/tab_burst_aggregation.tex` | 9 | `11.90` | `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `paper/tables/tab_burst_aggregation.tex` | 9 | `11.34` | `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `paper/tables/tab_burst_aggregation.tex` | 9 | `0.9490` | `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 9 | `8.49` | `1 (Single packet) & 11.34\% & 11.90\% & 8.49\% & +0.56\% & 0.9490 \\` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 10 | `64%` | `3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_burst_aggregation.tex` | 10 | `11.22` | `3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 10 | `4.37` | `3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 10 | `0.9642` | `3 (3-packet burst) & 9.95\% & 11.22\% & 4.37\% & +1.27\% & 0.9642 \\` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 11 | `64%` | `5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_burst_aggregation.tex` | 11 | `3.54` | `5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 11 | `10.45` | `5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_burst_aggregation.tex` | 11 | `0.9670` | `5 (5-packet burst) & 8.81\% & 10.45\% & 3.54\% & +1.64\% & 0.9670 \\` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_episode_summary.tex` | 8 | `64%` | `0 & 0.741800 & 0.061900 & 0.064900 & 0.086500 & 0.003000 & 0.976900 & 0.975500 & 0.997700 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_episode_summary.tex` | 9 | `64%` | `1 & 0.708200 & 0.164100 & 0.119100 & 0.086000 & -0.045000 & 0.934500 & 0.955700 & 0.992200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_episode_summary.tex` | 13 | `0.1142` | `5 & 0.688100 & 0.114100 & 0.151500 & 0.086000 & 0.037500 & 0.954500 & 0.947400 & 0.992200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_episode_summary.tex` | 16 | `64%` | `8 & 0.648500 & 0.186200 & 0.245800 & 0.050900 & 0.059600 & 0.939000 & 0.931200 & 0.992900 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_episode_summary.tex` | 24 | `64%` | `16 & 0.651700 & 0.051200 & 0.050600 & 0.064600 & -0.000600 & 0.982400 & 0.976000 & 0.996100 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_episode_summary.tex` | 25 | `0.1142` | `17 & 0.698000 & 0.114700 & 0.075100 & 0.069700 & -0.039600 & 0.952700 & 0.978600 & 0.994600 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_lopo_bias.tex` | 8 | `64%` | `0 & resubstitution & 0.063800 & 0.064900 & -0.001200 & 0.001200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_lopo_bias.tex` | 9 | `64%` | `0 & naive_packet_disjoint & 0.061900 & 0.064900 & -0.003000 & 0.003000 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_lopo_bias.tex` | 12 | `64%` | `1 & naive_packet_disjoint & 0.164100 & 0.119100 & 0.045000 & 0.045000 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_lopo_bias.tex` | 24 | `0.1142` | `5 & naive_packet_disjoint & 0.114100 & 0.151500 & -0.037500 & 0.037500 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_lopo_bias.tex` | 60 | `0.1142` | `17 & naive_packet_disjoint & 0.114700 & 0.075100 & 0.039600 & 0.039600 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 8 | `0.2097` | `0 & 2 & 21 & 2.894300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 8 | `0.1142` | `0 & 2 & 21 & 2.894300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 9 | `0.2097` | `0 & 7 & 27 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 9 | `0.1142` | `0 & 7 & 27 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 10 | `0.2097` | `0 & 11 & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 10 | `0.1142` | `0 & 11 & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 11 | `0.2097` | `0 & 13 & 17 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 11 | `0.1142` | `0 & 13 & 17 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 12 | `0.2097` | `0 & 23 & 9 & 3.107600 & 0.434000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 12 | `0.1142` | `0 & 23 & 9 & 3.107600 & 0.434000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 13 | `0.2097` | `0 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 13 | `0.1142` | `0 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 14 | `0.2097` | `0 & 29 & 27 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 14 | `0.1142` | `0 & 29 & 27 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 15 | `0.2097` | `0 & 32 & 24 & 4.244100 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 15 | `0.1142` | `0 & 32 & 24 & 4.244100 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 16 | `0.2097` | `0 & 34 & 39 & 4.393700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 16 | `0.1142` | `0 & 34 & 39 & 4.393700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 17 | `0.2097` | `0 & 36 & 4 & 2.899800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 17 | `0.1142` | `0 & 36 & 4 & 2.899800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 18 | `0.2097` | `0 & 41 & 21 & 4.791500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 18 | `0.1142` | `0 & 41 & 21 & 4.791500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 19 | `0.2097` | `0 & 48 & 46 & 6.468700 & 0.020000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 19 | `0.1142` | `0 & 48 & 46 & 6.468700 & 0.020000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 20 | `0.2097` | `0 & 51 & 53 & 2.109800 & 0.087500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 20 | `0.1142` | `0 & 51 & 53 & 2.109800 & 0.087500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 21 | `0.2097` | `0 & 56 & 54 & 4.740200 & 0.182500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 21 | `0.1142` | `0 & 56 & 54 & 4.740200 & 0.182500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 22 | `0.2097` | `0 & 60 & 53 & 4.375400 & 0.217500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 22 | `0.1142` | `0 & 60 & 53 & 4.375400 & 0.217500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 22 | `4.37` | `0 & 60 & 53 & 4.375400 & 0.217500 & 0.209700 & 0.114200 \\` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_neighbour_analysis.tex` | 23 | `0.2097` | `1 & 16 & 13 & 2.775000 & 0.028000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 23 | `0.1142` | `1 & 16 & 13 & 2.775000 & 0.028000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 24 | `0.2097` | `1 & 19 & 15 & 2.702400 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 24 | `0.1142` | `1 & 19 & 15 & 2.702400 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 25 | `0.2097` | `1 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 25 | `0.1142` | `1 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 26 | `0.2097` | `1 & 25 & 20 & 3.996300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 26 | `0.1142` | `1 & 25 & 20 & 3.996300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 27 | `0.2097` | `1 & 27 & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 27 | `0.1142` | `1 & 27 & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 28 | `0.2097` | `1 & 29 & 26 & 4.544300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 28 | `0.1142` | `1 & 29 & 26 & 4.544300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 29 | `0.2097` | `1 & 30 & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 29 | `0.1142` | `1 & 30 & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 30 | `0.2097` | `1 & 34 & 40 & 3.452600 & 0.027500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 30 | `0.1142` | `1 & 34 & 40 & 3.452600 & 0.027500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 31 | `0.2097` | `1 & 36 & 4 & 2.899800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 31 | `0.1142` | `1 & 36 & 4 & 2.899800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 32 | `0.2097` | `1 & 39 & 10 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 32 | `0.1142` | `1 & 39 & 10 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 33 | `0.2097` | `1 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 33 | `0.1142` | `1 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 34 | `0.2097` | `1 & 48 & 46 & 6.468700 & 0.830000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 34 | `0.1142` | `1 & 48 & 46 & 6.468700 & 0.830000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 35 | `0.2097` | `1 & 52 & 53 & 5.019300 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 35 | `0.1142` | `1 & 52 & 53 & 5.019300 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 36 | `0.2097` | `1 & 54 & 56 & 4.740200 & 0.717500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 36 | `0.1142` | `1 & 54 & 56 & 4.740200 & 0.717500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 37 | `0.2097` | `1 & 57 & 56 & 4.186200 & 0.307500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 37 | `0.1142` | `1 & 57 & 56 & 4.186200 & 0.307500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 38 | `0.2097` | `2 & 3 & 36 & 3.770200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 38 | `0.1142` | `2 & 3 & 36 & 3.770200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 39 | `0.2097` | `2 & 13 & 16 & 2.775000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 39 | `0.1142` | `2 & 13 & 16 & 2.775000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 40 | `0.2097` | `2 & 14 & 15 & 2.405800 & 0.016000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 40 | `0.1142` | `2 & 14 & 15 & 2.405800 & 0.016000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 41 | `0.2097` | `2 & 18 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 41 | `0.1142` | `2 & 18 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 42 | `0.2097` | `2 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 42 | `0.1142` | `2 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 43 | `0.2097` | `2 & 25 & 39 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 43 | `0.1142` | `2 & 25 & 39 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 44 | `0.2097` | `2 & 30 & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 44 | `0.1142` | `2 & 30 & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 45 | `0.2097` | `2 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 45 | `0.1142` | `2 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 46 | `0.2097` | `2 & 33 & 26 & 3.446100 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 46 | `0.1142` | `2 & 33 & 26 & 3.446100 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 47 | `0.2097` | `2 & 34 & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 47 | `0.1142` | `2 & 34 & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 48 | `0.2097` | `2 & 42 & 28 & 5.499000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 48 | `0.1142` | `2 & 42 & 28 & 5.499000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 49 | `0.2097` | `2 & 47 & 48 & 17.681100 & 0.002500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 49 | `0.1142` | `2 & 47 & 48 & 17.681100 & 0.002500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 50 | `0.2097` | `2 & 50 & 48 & 16.692100 & 0.447500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 50 | `0.1142` | `2 & 50 & 48 & 16.692100 & 0.447500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 51 | `0.2097` | `2 & 54 & 51 & 5.281600 & 0.182500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 51 | `0.1142` | `2 & 54 & 51 & 5.281600 & 0.182500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 52 | `0.2097` | `2 & 55 & 51 & 2.184300 & 0.605000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 52 | `0.1142` | `2 & 55 & 51 & 2.184300 & 0.605000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 53 | `0.2097` | `3 & 2 & 18 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 53 | `0.1142` | `3 & 2 & 18 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 54 | `0.2097` | `3 & 14 & 19 & 2.813000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 54 | `0.1142` | `3 & 14 & 19 & 2.813000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 55 | `0.2097` | `3 & 15 & 19 & 2.702400 & 0.106000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 55 | `0.1142` | `3 & 15 & 19 & 2.702400 & 0.106000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 56 | `0.2097` | `3 & 27 & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 56 | `0.1142` | `3 & 27 & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 57 | `0.2097` | `3 & 28 & 11 & 2.900200 & 0.508000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 57 | `0.1142` | `3 & 28 & 11 & 2.900200 & 0.508000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 58 | `0.2097` | `3 & 29 & 43 & 4.421300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 58 | `0.1142` | `3 & 29 & 43 & 4.421300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 59 | `0.2097` | `3 & 30 & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 59 | `0.1142` | `3 & 30 & 17 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 60 | `0.2097` | `3 & 32 & 1 & 4.811300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 60 | `0.1142` | `3 & 32 & 1 & 4.811300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 61 | `0.2097` | `3 & 33 & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 61 | `0.1142` | `3 & 33 & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 62 | `0.2097` | `3 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 62 | `0.1142` | `3 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 63 | `0.2097` | `3 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 63 | `0.1142` | `3 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 64 | `64%` | `3 & 46 & 49 & 4.846400 & 0.450000 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 64 | `0.2097` | `3 & 46 & 49 & 4.846400 & 0.450000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 64 | `0.1142` | `3 & 46 & 49 & 4.846400 & 0.450000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 65 | `0.2097` | `3 & 50 & 47 & 10.874000 & 0.257500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 65 | `0.1142` | `3 & 50 & 47 & 10.874000 & 0.257500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 66 | `0.2097` | `3 & 51 & 55 & 2.184300 & 0.255000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 66 | `0.1142` | `3 & 51 & 55 & 2.184300 & 0.255000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 67 | `0.2097` | `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 67 | `0.1142` | `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 67 | `0.0327` | `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/tables/tab_neighbour_analysis.tex` | 67 | `0.0323` | `3 & 53 & 55 & 3.104300 & 0.032500 & 0.209700 & 0.114200 \\` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/tables/tab_neighbour_analysis.tex` | 68 | `0.2097` | `4 & 3 & 27 & 4.098600 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 68 | `0.1142` | `4 & 3 & 27 & 4.098600 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 69 | `0.2097` | `4 & 7 & 29 & 3.849800 & 0.078000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 69 | `0.1142` | `4 & 7 & 29 & 3.849800 & 0.078000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 70 | `0.2097` | `4 & 12 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 70 | `0.1142` | `4 & 12 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 71 | `0.2097` | `4 & 14 & 15 & 2.405800 & 0.202000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 71 | `0.1142` | `4 & 14 & 15 & 2.405800 & 0.202000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 72 | `0.2097` | `4 & 17 & 13 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 72 | `0.1142` | `4 & 17 & 13 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 73 | `0.2097` | `4 & 20 & 15 & 1.805000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 73 | `0.1142` | `4 & 20 & 15 & 1.805000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 74 | `0.2097` | `4 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 74 | `0.1142` | `4 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 75 | `0.2097` | `4 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 75 | `0.1142` | `4 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 76 | `0.2097` | `4 & 35 & 44 & 2.985700 & 0.162500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 76 | `0.1142` | `4 & 35 & 44 & 2.985700 & 0.162500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 77 | `0.2097` | `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 77 | `0.1142` | `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 77 | `0.0327` | `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/tables/tab_neighbour_analysis.tex` | 77 | `0.0323` | `4 & 36 & 27 & 3.866500 & 0.032500 & 0.209700 & 0.114200 \\` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/tables/tab_neighbour_analysis.tex` | 78 | `0.2097` | `4 & 43 & 27 & 4.091900 & 0.115000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 78 | `0.1142` | `4 & 43 & 27 & 4.091900 & 0.115000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 79 | `0.2097` | `4 & 47 & 48 & 17.681100 & 0.992500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 79 | `0.1142` | `4 & 47 & 48 & 17.681100 & 0.992500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 80 | `0.2097` | `4 & 50 & 48 & 16.692100 & 0.997500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 80 | `0.1142` | `4 & 50 & 48 & 16.692100 & 0.997500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 81 | `0.2097` | `4 & 56 & 58 & 4.920800 & 0.320000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 81 | `0.1142` | `4 & 56 & 58 & 4.920800 & 0.320000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 82 | `0.2097` | `4 & 57 & 59 & 4.558800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 82 | `0.1142` | `4 & 57 & 59 & 4.558800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 83 | `0.2097` | `5 & 4 & 37 & 4.053400 & 0.008000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 83 | `0.1142` | `5 & 4 & 37 & 4.053400 & 0.008000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 84 | `0.2097` | `5 & 7 & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 84 | `0.1142` | `5 & 7 & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 85 | `0.2097` | `5 & 8 & 44 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 85 | `0.1142` | `5 & 8 & 44 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 86 | `0.2097` | `5 & 14 & 20 & 2.699200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 86 | `0.1142` | `5 & 14 & 20 & 2.699200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 87 | `64%` | `5 & 15 & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 87 | `0.2097` | `5 & 15 & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 87 | `0.1142` | `5 & 15 & 20 & 1.805000 & 0.264000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 88 | `0.2097` | `5 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 88 | `0.1142` | `5 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 89 | `0.2097` | `5 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 89 | `0.1142` | `5 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 90 | `0.2097` | `5 & 34 & 44 & 3.518400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 90 | `0.1142` | `5 & 34 & 44 & 3.518400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 91 | `0.2097` | `5 & 36 & 3 & 3.770200 & 0.002500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 91 | `0.1142` | `5 & 36 & 3 & 3.770200 & 0.002500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 92 | `0.2097` | `5 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 92 | `0.1142` | `5 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 93 | `0.2097` | `5 & 42 & 11 & 4.981400 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 93 | `0.1142` | `5 & 42 & 11 & 4.981400 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 94 | `0.2097` | `5 & 47 & 50 & 10.874000 & 0.127500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 94 | `0.1142` | `5 & 47 & 50 & 10.874000 & 0.127500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 95 | `64%` | `5 & 53 & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 95 | `0.2097` | `5 & 53 & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 95 | `0.1142` | `5 & 53 & 51 & 2.109800 & 0.645000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 96 | `0.2097` | `5 & 56 & 57 & 4.186200 & 0.512500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 96 | `0.1142` | `5 & 56 & 57 & 4.186200 & 0.512500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 97 | `0.2097` | `5 & 59 & 57 & 4.558800 & 0.830000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 97 | `0.1142` | `5 & 59 & 57 & 4.558800 & 0.830000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 98 | `0.2097` | `6 & 7 & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 98 | `0.1142` | `6 & 7 & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 99 | `0.2097` | `6 & 8 & 44 & 2.039900 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 99 | `0.1142` | `6 & 8 & 44 & 2.039900 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 100 | `0.2097` | `6 & 11 & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 100 | `0.1142` | `6 & 11 & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 101 | `0.2097` | `6 & 12 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 101 | `0.1142` | `6 & 12 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 102 | `0.2097` | `6 & 13 & 44 & 4.424700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 102 | `0.1142` | `6 & 13 & 44 & 4.424700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 103 | `0.2097` | `6 & 26 & 33 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 103 | `0.1142` | `6 & 26 & 33 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 104 | `0.2097` | `6 & 27 & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 104 | `0.1142` | `6 & 27 & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 105 | `0.2097` | `6 & 34 & 44 & 3.518400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 105 | `0.1142` | `6 & 34 & 44 & 3.518400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 106 | `0.2097` | `6 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 106 | `0.1142` | `6 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 107 | `0.2097` | `6 & 40 & 44 & 2.738200 & 0.007500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 107 | `0.1142` | `6 & 40 & 44 & 2.738200 & 0.007500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 108 | `0.2097` | `6 & 43 & 6 & 3.376900 & 0.045000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 108 | `0.1142` | `6 & 43 & 6 & 3.376900 & 0.045000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 109 | `0.2097` | `6 & 47 & 50 & 10.874000 & 0.995000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 109 | `0.1142` | `6 & 47 & 50 & 10.874000 & 0.995000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 110 | `0.2097` | `6 & 48 & 49 & 9.769000 & 0.957500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 110 | `0.1142` | `6 & 48 & 49 & 9.769000 & 0.957500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 111 | `0.2097` | `6 & 53 & 51 & 2.109800 & 0.742500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 111 | `0.1142` | `6 & 53 & 51 & 2.109800 & 0.742500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 112 | `0.2097` | `6 & 55 & 51 & 2.184300 & 0.215000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 112 | `0.1142` | `6 & 55 & 51 & 2.184300 & 0.215000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 113 | `4.43` | `7 & 2 & 26 & 4.436800 & 0.072000 & 0.209700 & 0.114200 \\` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `paper/tables/tab_neighbour_analysis.tex` | 113 | `0.2097` | `7 & 2 & 26 & 4.436800 & 0.072000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 113 | `0.1142` | `7 & 2 & 26 & 4.436800 & 0.072000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 114 | `0.2097` | `7 & 15 & 14 & 2.405800 & 0.244000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 114 | `0.1142` | `7 & 15 & 14 & 2.405800 & 0.244000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 115 | `0.2097` | `7 & 16 & 13 & 2.775000 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 115 | `0.1142` | `7 & 16 & 13 & 2.775000 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 116 | `0.2097` | `7 & 21 & 33 & 4.692500 & 0.018000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 116 | `0.1142` | `7 & 21 & 33 & 4.692500 & 0.018000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 117 | `0.2097` | `7 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 117 | `0.1142` | `7 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 118 | `0.2097` | `7 & 28 & 11 & 2.900200 & 0.692000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 118 | `0.1142` | `7 & 28 & 11 & 2.900200 & 0.692000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 119 | `0.2097` | `7 & 30 & 13 & 4.506200 & 0.150000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 119 | `0.1142` | `7 & 30 & 13 & 4.506200 & 0.150000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 120 | `0.2097` | `7 & 36 & 4 & 2.899800 & 0.007500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 120 | `0.1142` | `7 & 36 & 4 & 2.899800 & 0.007500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 121 | `0.2097` | `7 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 121 | `0.1142` | `7 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 122 | `0.2097` | `7 & 40 & 44 & 2.738200 & 0.037500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 122 | `0.1142` | `7 & 40 & 44 & 2.738200 & 0.037500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 123 | `0.2097` | `7 & 41 & 7 & 4.889200 & 0.110000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 123 | `0.1142` | `7 & 41 & 7 & 4.889200 & 0.110000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 124 | `0.2097` | `7 & 46 & 48 & 6.468700 & 0.522500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 124 | `0.1142` | `7 & 46 & 48 & 6.468700 & 0.522500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 125 | `0.2097` | `7 & 50 & 47 & 10.874000 & 0.872500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 125 | `0.1142` | `7 & 50 & 47 & 10.874000 & 0.872500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 126 | `0.2097` | `7 & 55 & 51 & 2.184300 & 0.535000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 126 | `0.1142` | `7 & 55 & 51 & 2.184300 & 0.535000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 127 | `0.2097` | `7 & 59 & 57 & 4.558800 & 0.095000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 127 | `0.1142` | `7 & 59 & 57 & 4.558800 & 0.095000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 128 | `0.2097` | `8 & 1 & 5 & 4.573300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 128 | `0.1142` | `8 & 1 & 5 & 4.573300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 129 | `0.2097` | `8 & 8 & 40 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 129 | `0.1142` | `8 & 8 & 40 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 130 | `0.2097` | `8 & 16 & 13 & 2.775000 & 0.058000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 130 | `0.1142` | `8 & 16 & 13 & 2.775000 & 0.058000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 131 | `0.2097` | `8 & 17 & 30 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 131 | `0.1142` | `8 & 17 & 30 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 132 | `0.2097` | `8 & 19 & 11 & 2.615600 & 0.182000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 132 | `0.1142` | `8 & 19 & 11 & 2.615600 & 0.182000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 133 | `0.2097` | `8 & 23 & 38 & 3.434400 & 0.574000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 133 | `0.1142` | `8 & 23 & 38 & 3.434400 & 0.574000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 134 | `0.2097` | `8 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 134 | `0.1142` | `8 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 135 | `0.2097` | `8 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 135 | `0.1142` | `8 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 136 | `0.2097` | `8 & 35 & 34 & 4.521200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 136 | `0.1142` | `8 & 35 & 34 & 4.521200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 137 | `0.2097` | `8 & 39 & 11 & 3.408200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 137 | `0.1142` | `8 & 39 & 11 & 3.408200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 138 | `0.2097` | `8 & 42 & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 138 | `0.1142` | `8 & 42 & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 139 | `0.2097` | `8 & 48 & 46 & 6.468700 & 1.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 139 | `0.1142` | `8 & 48 & 46 & 6.468700 & 1.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 140 | `0.2097` | `8 & 50 & 46 & 21.668300 & 0.995000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 140 | `0.1142` | `8 & 50 & 46 & 21.668300 & 0.995000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 141 | `0.2097` | `8 & 54 & 55 & 4.858400 & 0.850000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 141 | `0.1142` | `8 & 54 & 55 & 4.858400 & 0.850000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 142 | `0.2097` | `8 & 56 & 57 & 4.186200 & 0.132500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 142 | `0.1142` | `8 & 56 & 57 & 4.186200 & 0.132500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 143 | `0.2097` | `9 & 9 & 23 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 143 | `0.1142` | `9 & 9 & 23 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 144 | `0.2097` | `9 & 10 & 19 & 4.492500 & 0.020000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 144 | `0.1142` | `9 & 10 & 19 & 4.492500 & 0.020000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 145 | `0.2097` | `9 & 15 & 19 & 2.702400 & 0.634000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 145 | `0.1142` | `9 & 15 & 19 & 2.702400 & 0.634000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 146 | `0.2097` | `9 & 20 & 19 & 2.718300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 146 | `0.1142` | `9 & 20 & 19 & 2.718300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 147 | `0.2097` | `9 & 25 & 16 & 3.200800 & 0.030000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 147 | `0.1142` | `9 & 25 & 16 & 3.200800 & 0.030000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 148 | `0.2097` | `9 & 26 & 33 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 148 | `0.1142` | `9 & 26 & 33 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 149 | `0.2097` | `9 & 27 & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 149 | `0.1142` | `9 & 27 & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 150 | `0.2097` | `9 & 32 & 5 & 4.460700 & 0.002500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 150 | `0.1142` | `9 & 32 & 5 & 4.460700 & 0.002500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 151 | `0.2097` | `9 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 151 | `0.1142` | `9 & 38 & 23 & 3.434400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 152 | `0.2097` | `9 & 40 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 152 | `0.1142` | `9 & 40 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 153 | `0.2097` | `9 & 41 & 21 & 4.791500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 153 | `0.1142` | `9 & 41 & 21 & 4.791500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 154 | `0.2097` | `9 & 52 & 59 & 5.114500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 154 | `0.1142` | `9 & 52 & 59 & 5.114500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 155 | `0.2097` | `9 & 53 & 60 & 4.375400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 155 | `0.1142` | `9 & 53 & 60 & 4.375400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 155 | `4.37` | `9 & 53 & 60 & 4.375400 & 0.000000 & 0.209700 & 0.114200 \\` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `paper/tables/tab_neighbour_analysis.tex` | 156 | `0.2097` | `9 & 55 & 60 & 5.370100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 156 | `0.1142` | `9 & 55 & 60 & 5.370100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 157 | `0.2097` | `9 & 57 & 56 & 4.186200 & 0.797500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 157 | `0.1142` | `9 & 57 & 56 & 4.186200 & 0.797500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 158 | `0.2097` | `10 & 4 & 43 & 3.420400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 158 | `0.1142` | `10 & 4 & 43 & 3.420400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 159 | `0.2097` | `10 & 10 & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 159 | `0.1142` | `10 & 10 & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 160 | `0.2097` | `10 & 12 & 24 & 6.624900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 160 | `0.1142` | `10 & 12 & 24 & 6.624900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 161 | `0.2097` | `10 & 16 & 13 & 2.775000 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 161 | `0.1142` | `10 & 16 & 13 & 2.775000 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 162 | `0.2097` | `10 & 17 & 13 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 162 | `0.1142` | `10 & 17 & 13 & 4.399800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 163 | `0.2097` | `10 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 163 | `0.1142` | `10 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 164 | `0.2097` | `10 & 27 & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 164 | `0.1142` | `10 & 27 & 26 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 165 | `0.2097` | `10 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 165 | `0.1142` | `10 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 166 | `0.2097` | `10 & 33 & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 166 | `0.1142` | `10 & 33 & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 167 | `0.2097` | `10 & 36 & 6 & 3.530000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 167 | `0.1142` | `10 & 36 & 6 & 3.530000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 168 | `0.2097` | `10 & 42 & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 168 | `0.1142` | `10 & 42 & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 169 | `0.2097` | `10 & 48 & 50 & 16.692100 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 169 | `0.1142` | `10 & 48 & 50 & 16.692100 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 170 | `0.2097` | `10 & 49 & 59 & 23.732600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 170 | `0.1142` | `10 & 49 & 59 & 23.732600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 171 | `0.2097` | `10 & 51 & 53 & 2.109800 & 0.125000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 171 | `0.1142` | `10 & 51 & 53 & 2.109800 & 0.125000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 172 | `0.2097` | `10 & 60 & 58 & 3.707900 & 0.020000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 172 | `0.1142` | `10 & 60 & 58 & 3.707900 & 0.020000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 173 | `0.2097` | `11 & 1 & 5 & 4.573300 & 0.004000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 173 | `0.1142` | `11 & 1 & 5 & 4.573300 & 0.004000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 174 | `0.2097` | `11 & 3 & 36 & 3.770200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 174 | `0.1142` | `11 & 3 & 36 & 3.770200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 175 | `0.2097` | `11 & 16 & 13 & 2.775000 & 0.056000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 175 | `0.1142` | `11 & 16 & 13 & 2.775000 & 0.056000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 176 | `0.2097` | `11 & 18 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 176 | `0.1142` | `11 & 18 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 177 | `0.2097` | `11 & 23 & 9 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 177 | `0.1142` | `11 & 23 & 9 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 178 | `0.2097` | `11 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 178 | `0.1142` | `11 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 179 | `0.2097` | `11 & 29 & 7 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 179 | `0.1142` | `11 & 29 & 7 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 180 | `0.2097` | `11 & 34 & 25 & 3.885000 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 180 | `0.1142` | `11 & 34 & 25 & 3.885000 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 181 | `0.2097` | `11 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 181 | `0.1142` | `11 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 182 | `0.2097` | `11 & 40 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 182 | `0.1142` | `11 & 40 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 183 | `0.2097` | `11 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 183 | `0.1142` | `11 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 184 | `0.2097` | `11 & 48 & 46 & 6.468700 & 0.230000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 184 | `0.1142` | `11 & 48 & 46 & 6.468700 & 0.230000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 185 | `0.2097` | `11 & 50 & 47 & 10.874000 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 185 | `0.1142` | `11 & 50 & 47 & 10.874000 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 186 | `0.2097` | `11 & 55 & 51 & 2.184300 & 0.137500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 186 | `0.1142` | `11 & 55 & 51 & 2.184300 & 0.137500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 187 | `0.2097` | `11 & 56 & 54 & 4.740200 & 0.620000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 187 | `0.1142` | `11 & 56 & 54 & 4.740200 & 0.620000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 188 | `0.2097` | `12 & 7 & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 188 | `0.1142` | `12 & 7 & 29 & 3.849800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 189 | `0.2097` | `12 & 8 & 40 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 189 | `0.1142` | `12 & 8 & 40 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 190 | `0.2097` | `12 & 10 & 44 & 4.142300 & 0.034000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 190 | `0.1142` | `12 & 10 & 44 & 4.142300 & 0.034000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 191 | `0.2097` | `12 & 16 & 13 & 2.775000 & 0.026000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 191 | `0.1142` | `12 & 16 & 13 & 2.775000 & 0.026000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 192 | `0.2097` | `12 & 18 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 192 | `0.1142` | `12 & 18 & 2 & 1.842100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 193 | `0.2097` | `12 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 193 | `0.1142` | `12 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 194 | `0.2097` | `12 & 28 & 20 & 4.273400 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 194 | `0.1142` | `12 & 28 & 20 & 4.273400 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 195 | `0.2097` | `12 & 32 & 5 & 4.460700 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 195 | `0.1142` | `12 & 32 & 5 & 4.460700 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 196 | `0.2097` | `12 & 33 & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 196 | `0.1142` | `12 & 33 & 26 & 3.446100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 197 | `0.2097` | `12 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 197 | `0.1142` | `12 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 198 | `0.2097` | `12 & 42 & 25 & 5.844200 & 0.115000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 198 | `0.1142` | `12 & 42 & 25 & 5.844200 & 0.115000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 199 | `64%` | `12 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 199 | `0.2097` | `12 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 199 | `0.1142` | `12 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 200 | `0.2097` | `12 & 50 & 48 & 16.692100 & 0.997500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 200 | `0.1142` | `12 & 50 & 48 & 16.692100 & 0.997500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 201 | `0.2097` | `12 & 52 & 54 & 3.912000 & 0.002500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 201 | `0.1142` | `12 & 52 & 54 & 3.912000 & 0.002500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 202 | `0.2097` | `12 & 56 & 54 & 4.740200 & 0.217500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 202 | `0.1142` | `12 & 56 & 54 & 4.740200 & 0.217500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 203 | `0.2097` | `13 & 2 & 3 & 4.787800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 203 | `0.1142` | `13 & 2 & 3 & 4.787800 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 204 | `0.2097` | `13 & 4 & 36 & 2.899800 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 204 | `0.1142` | `13 & 4 & 36 & 2.899800 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 205 | `0.2097` | `13 & 14 & 19 & 2.813000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 205 | `0.1142` | `13 & 14 & 19 & 2.813000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 206 | `0.2097` | `13 & 21 & 32 & 5.441300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 206 | `0.1142` | `13 & 21 & 32 & 5.441300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 207 | `0.2097` | `13 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 207 | `0.1142` | `13 & 22 & 44 & 2.458200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 208 | `0.2097` | `13 & 26 & 3 & 4.974300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 208 | `0.1142` | `13 & 26 & 3 & 4.974300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 209 | `0.2097` | `13 & 27 & 36 & 3.866500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 209 | `0.1142` | `13 & 27 & 36 & 3.866500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 210 | `0.2097` | `13 & 33 & 32 & 4.738100 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 210 | `0.1142` | `13 & 33 & 32 & 4.738100 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 211 | `0.2097` | `13 & 37 & 36 & 4.303400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 211 | `0.1142` | `13 & 37 & 36 & 4.303400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 212 | `0.2097` | `13 & 40 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 212 | `0.1142` | `13 & 40 & 8 & 2.013000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 213 | `0.2097` | `13 & 43 & 6 & 3.376900 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 213 | `0.1142` | `13 & 43 & 6 & 3.376900 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 214 | `0.2097` | `13 & 46 & 48 & 6.468700 & 0.420000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 214 | `0.1142` | `13 & 46 & 48 & 6.468700 & 0.420000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 215 | `0.2097` | `13 & 54 & 52 & 3.912000 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 215 | `0.1142` | `13 & 54 & 52 & 3.912000 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 216 | `0.2097` | `13 & 56 & 57 & 4.186200 & 0.155000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 216 | `0.1142` | `13 & 56 & 57 & 4.186200 & 0.155000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 217 | `0.2097` | `13 & 58 & 60 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 217 | `0.1142` | `13 & 58 & 60 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 218 | `0.2097` | `14 & 11 & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 218 | `0.1142` | `14 & 11 & 19 & 2.615600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 219 | `0.2097` | `14 & 13 & 44 & 4.424700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 219 | `0.1142` | `14 & 13 & 44 & 4.424700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 220 | `0.2097` | `14 & 16 & 14 & 3.830000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 220 | `0.1142` | `14 & 16 & 14 & 3.830000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 221 | `0.2097` | `14 & 17 & 6 & 5.208400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 221 | `0.1142` | `14 & 17 & 6 & 5.208400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 222 | `0.2097` | `14 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 222 | `0.1142` | `14 & 24 & 32 & 4.244100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 223 | `0.2097` | `14 & 25 & 39 & 3.139000 & 0.012000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 223 | `0.1142` | `14 & 25 & 39 & 3.139000 & 0.012000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 224 | `0.2097` | `14 & 27 & 7 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 224 | `0.1142` | `14 & 27 & 7 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 225 | `0.2097` | `14 & 33 & 21 & 4.692500 & 0.017500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 225 | `0.1142` | `14 & 33 & 21 & 4.692500 & 0.017500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 226 | `0.2097` | `14 & 38 & 39 & 6.796700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 226 | `0.1142` | `14 & 38 & 39 & 6.796700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 227 | `0.2097` | `14 & 40 & 44 & 2.738200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 227 | `0.1142` | `14 & 40 & 44 & 2.738200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 228 | `0.2097` | `14 & 42 & 19 & 5.495600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 228 | `0.1142` | `14 & 42 & 19 & 5.495600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 229 | `64%` | `14 & 46 & 49 & 4.846400 & 0.972500 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 229 | `0.2097` | `14 & 46 & 49 & 4.846400 & 0.972500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 229 | `0.1142` | `14 & 46 & 49 & 4.846400 & 0.972500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 230 | `0.2097` | `14 & 48 & 49 & 9.769000 & 0.870000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 230 | `0.1142` | `14 & 48 & 49 & 9.769000 & 0.870000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 231 | `0.2097` | `14 & 52 & 54 & 3.912000 & 0.030000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 231 | `0.1142` | `14 & 52 & 54 & 3.912000 & 0.030000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 232 | `0.2097` | `14 & 60 & 58 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 232 | `0.1142` | `14 & 60 & 58 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 233 | `0.2097` | `15 & 1 & 5 & 4.573300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 233 | `0.1142` | `15 & 1 & 5 & 4.573300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 234 | `0.2097` | `15 & 10 & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 234 | `0.1142` | `15 & 10 & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 235 | `0.2097` | `15 & 15 & 20 & 1.805000 & 0.098000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 235 | `0.1142` | `15 & 15 & 20 & 1.805000 & 0.098000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 236 | `0.2097` | `15 & 16 & 13 & 2.775000 & 0.046000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 236 | `0.1142` | `15 & 16 & 13 & 2.775000 & 0.046000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 237 | `0.2097` | `15 & 17 & 30 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 237 | `0.1142` | `15 & 17 & 30 & 3.523900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 238 | `0.2097` | `15 & 23 & 28 & 5.042700 & 0.614000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 238 | `0.1142` | `15 & 23 & 28 & 5.042700 & 0.614000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 239 | `0.2097` | `15 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 239 | `0.1142` | `15 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 240 | `0.2097` | `15 & 32 & 5 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 240 | `0.1142` | `15 & 32 & 5 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 241 | `0.2097` | `15 & 33 & 27 & 4.317400 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 241 | `0.1142` | `15 & 33 & 27 & 4.317400 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 242 | `0.2097` | `15 & 38 & 39 & 6.796700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 242 | `0.1142` | `15 & 38 & 39 & 6.796700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 243 | `0.2097` | `15 & 43 & 6 & 3.376900 & 0.005000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 243 | `0.1142` | `15 & 43 & 6 & 3.376900 & 0.005000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 244 | `0.2097` | `15 & 48 & 46 & 6.468700 & 1.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 244 | `0.1142` | `15 & 48 & 46 & 6.468700 & 1.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 245 | `64%` | `15 & 49 & 46 & 4.846400 & 0.992500 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 245 | `0.2097` | `15 & 49 & 46 & 4.846400 & 0.992500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 245 | `0.1142` | `15 & 49 & 46 & 4.846400 & 0.992500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 246 | `0.2097` | `15 & 55 & 51 & 2.184300 & 0.302500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 246 | `0.1142` | `15 & 55 & 51 & 2.184300 & 0.302500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 247 | `0.2097` | `15 & 59 & 57 & 4.558800 & 0.327500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 247 | `0.1142` | `15 & 59 & 57 & 4.558800 & 0.327500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 248 | `0.2097` | `16 & 2 & 21 & 2.894300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 248 | `0.1142` | `16 & 2 & 21 & 2.894300 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 249 | `0.2097` | `16 & 5 & 32 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 249 | `0.1142` | `16 & 5 & 32 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 250 | `0.2097` | `16 & 7 & 27 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 250 | `0.1142` | `16 & 7 & 27 & 3.852200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 251 | `0.2097` | `16 & 10 & 44 & 4.142300 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 251 | `0.1142` | `16 & 10 & 44 & 4.142300 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 252 | `0.2097` | `16 & 12 & 32 & 7.532400 & 0.008000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 252 | `0.1142` | `16 & 12 & 32 & 7.532400 & 0.008000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 253 | `0.2097` | `16 & 15 & 20 & 1.805000 & 0.154000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 253 | `0.1142` | `16 & 15 & 20 & 1.805000 & 0.154000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 254 | `0.2097` | `16 & 22 & 44 & 2.458200 & 0.172000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 254 | `0.1142` | `16 & 22 & 44 & 2.458200 & 0.172000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 255 | `0.2097` | `16 & 34 & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 255 | `0.1142` | `16 & 34 & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 256 | `0.2097` | `16 & 37 & 4 & 4.053400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 256 | `0.1142` | `16 & 37 & 4 & 4.053400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 257 | `0.2097` | `16 & 39 & 11 & 3.408200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 257 | `0.1142` | `16 & 39 & 11 & 3.408200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 258 | `0.2097` | `16 & 42 & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 258 | `0.1142` | `16 & 42 & 11 & 4.981400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 259 | `0.2097` | `16 & 46 & 50 & 21.668300 & 0.057500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 259 | `0.1142` | `16 & 46 & 50 & 21.668300 & 0.057500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 260 | `0.2097` | `16 & 49 & 59 & 23.732600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 260 | `0.1142` | `16 & 49 & 59 & 23.732600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 261 | `0.2097` | `16 & 52 & 54 & 3.912000 & 0.077500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 261 | `0.1142` | `16 & 52 & 54 & 3.912000 & 0.077500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 262 | `0.2097` | `16 & 55 & 51 & 2.184300 & 0.267500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 262 | `0.1142` | `16 & 55 & 51 & 2.184300 & 0.267500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 263 | `0.2097` | `17 & 5 & 32 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 263 | `0.1142` | `17 & 5 & 32 & 4.460700 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 264 | `0.2097` | `17 & 9 & 23 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 264 | `0.1142` | `17 & 9 & 23 & 3.107600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 265 | `0.2097` | `17 & 12 & 24 & 6.624900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 265 | `0.1142` | `17 & 12 & 24 & 6.624900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 266 | `0.2097` | `17 & 14 & 20 & 2.699200 & 0.004000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 266 | `0.1142` | `17 & 14 & 20 & 2.699200 & 0.004000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 267 | `0.2097` | `17 & 21 & 2 & 2.894300 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 267 | `0.1142` | `17 & 21 & 2 & 2.894300 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 268 | `0.2097` | `17 & 22 & 8 & 3.154100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 268 | `0.1142` | `17 & 22 & 8 & 3.154100 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 269 | `0.2097` | `17 & 30 & 40 & 3.870000 & 0.068000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 269 | `0.1142` | `17 & 30 & 40 & 3.870000 & 0.068000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 270 | `0.2097` | `17 & 34 & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 270 | `0.1142` | `17 & 34 & 40 & 3.452600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 271 | `0.2097` | `17 & 37 & 4 & 4.053400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 271 | `0.1142` | `17 & 37 & 4 & 4.053400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 272 | `0.2097` | `17 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 272 | `0.1142` | `17 & 39 & 25 & 3.139000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 273 | `0.2097` | `17 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 273 | `0.1142` | `17 & 44 & 8 & 2.039900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 274 | `0.2097` | `17 & 49 & 48 & 9.769000 & 0.895000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 274 | `0.1142` | `17 & 49 & 48 & 9.769000 & 0.895000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 275 | `0.2097` | `17 & 51 & 53 & 2.109800 & 0.117500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 275 | `0.1142` | `17 & 51 & 53 & 2.109800 & 0.117500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 276 | `0.2097` | `17 & 52 & 54 & 3.912000 & 0.007500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 276 | `0.1142` | `17 & 52 & 54 & 3.912000 & 0.007500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 277 | `0.2097` | `17 & 58 & 60 & 3.707900 & 0.107500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 277 | `0.1142` | `17 & 58 & 60 & 3.707900 & 0.107500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 278 | `0.2097` | `18 & 9 & 19 & 5.023500 & 0.082000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 278 | `0.1142` | `18 & 9 & 19 & 5.023500 & 0.082000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 279 | `0.2097` | `18 & 10 & 19 & 4.492500 & 0.062000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 279 | `0.1142` | `18 & 10 & 19 & 4.492500 & 0.062000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 280 | `0.2097` | `18 & 14 & 15 & 2.405800 & 0.038000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 280 | `0.1142` | `18 & 14 & 15 & 2.405800 & 0.038000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 281 | `0.2097` | `18 & 20 & 15 & 1.805000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 281 | `0.1142` | `18 & 20 & 15 & 1.805000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 282 | `0.2097` | `18 & 22 & 4 & 3.992200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 282 | `0.1142` | `18 & 22 & 4 & 3.992200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 283 | `0.2097` | `18 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 283 | `0.1142` | `18 & 26 & 27 & 2.754600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 284 | `0.2097` | `18 & 28 & 19 & 3.273900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 284 | `0.1142` | `18 & 28 & 19 & 3.273900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 285 | `0.2097` | `18 & 31 & 1 & 6.432600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 285 | `0.1142` | `18 & 31 & 1 & 6.432600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 286 | `0.2097` | `18 & 35 & 34 & 4.521200 & 0.265000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 286 | `0.1142` | `18 & 35 & 34 & 4.521200 & 0.265000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 287 | `0.2097` | `18 & 39 & 19 & 3.658200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 287 | `0.1142` | `18 & 39 & 19 & 3.658200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 288 | `0.2097` | `18 & 42 & 19 & 5.495600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 288 | `0.1142` | `18 & 42 & 19 & 5.495600 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 289 | `64%` | `18 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_neighbour_analysis.tex` | 289 | `0.2097` | `18 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 289 | `0.1142` | `18 & 46 & 49 & 4.846400 & 1.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 290 | `0.2097` | `18 & 48 & 49 & 9.769000 & 1.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 290 | `0.1142` | `18 & 48 & 49 & 9.769000 & 1.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 291 | `0.2097` | `18 & 55 & 51 & 2.184300 & 0.085000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 291 | `0.1142` | `18 & 55 & 51 & 2.184300 & 0.085000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 292 | `0.2097` | `18 & 60 & 58 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 292 | `0.1142` | `18 & 60 & 58 & 3.707900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 293 | `0.2097` | `19 & 4 & 40 & 4.343500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 293 | `0.1142` | `19 & 4 & 40 & 4.343500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 294 | `0.2097` | `19 & 10 & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 294 | `0.1142` | `19 & 10 & 39 & 3.431400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 295 | `0.2097` | `19 & 11 & 25 & 3.005500 & 0.002000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 295 | `0.1142` | `19 & 11 & 25 & 3.005500 & 0.002000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 296 | `0.2097` | `19 & 12 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 296 | `0.1142` | `19 & 12 & 5 & 5.651900 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 297 | `0.2097` | `19 & 14 & 15 & 2.405800 & 0.018000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 297 | `0.1142` | `19 & 14 & 15 & 2.405800 & 0.018000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 298 | `0.2097` | `19 & 22 & 44 & 2.458200 & 0.010000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 298 | `0.1142` | `19 & 22 & 44 & 2.458200 & 0.010000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 299 | `0.2097` | `19 & 27 & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 299 | `0.1142` | `19 & 27 & 29 & 3.817400 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 300 | `0.2097` | `19 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 300 | `0.1142` | `19 & 31 & 32 & 6.201500 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 301 | `0.2097` | `19 & 37 & 8 & 4.413700 & 0.007500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 301 | `0.1142` | `19 & 37 & 8 & 4.413700 & 0.007500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 302 | `0.2097` | `19 & 38 & 45 & 6.402000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 302 | `0.1142` | `19 & 38 & 45 & 6.402000 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 303 | `0.2097` | `19 & 42 & 25 & 5.844200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 303 | `0.1142` | `19 & 42 & 25 & 5.844200 & 0.000000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 304 | `0.2097` | `19 & 47 & 48 & 17.681100 & 0.015000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 304 | `0.1142` | `19 & 47 & 48 & 17.681100 & 0.015000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 305 | `0.2097` | `19 & 50 & 48 & 16.692100 & 0.595000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 305 | `0.1142` | `19 & 50 & 48 & 16.692100 & 0.595000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 306 | `0.2097` | `19 & 56 & 52 & 5.371500 & 0.112500 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 306 | `0.1142` | `19 & 56 & 52 & 5.371500 & 0.112500 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 307 | `0.2097` | `19 & 57 & 59 & 4.558800 & 0.030000 & 0.209700 & 0.114200 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_neighbour_analysis.tex` | 307 | `0.1142` | `19 & 57 & 59 & 4.558800 & 0.030000 & 0.209700 & 0.114200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_stats_summary.tex` | 12 | `0.9530` | `...UROC_A & episode_level & 20 & 0.953000 & 0.941300 & 0.962500 & 0.0...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `paper/tables/tab_stats_summary.tex` | 13 | `0.9490` | `...UROC_B & episode_level & 20 & 0.949000 & 0.936700 & 0.960500 & 0.0...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `paper/tables/tab_sweep_results.tex` | 13 | `64%` | `0 & 15 & 0.741800 & 0.061900 & 0.064900 & 0.086500 & 0.003000 & 0.873300 & 0.013100 & 0.243300 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 14 | `64%` | `1 & 0 & 0.643300 & NaN & 0.160500 & 0.054500 & NaN & 0.856700 & 0.042900 & 0.266200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 18 | `64%` | `1 & 10 & 0.698400 & 0.156400 & 0.123100 & 0.078900 & -0.033300 & 0.856700 & 0.042900 & 0.266200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 19 | `64%` | `1 & 15 & 0.708200 & 0.164100 & 0.119100 & 0.086000 & -0.045000 & 0.856700 & 0.042900 & 0.266200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 20 | `64%` | `2 & 0 & 0.640700 & NaN & 0.146300 & 0.056000 & NaN & 0.843300 & 0.004300 & 0.261600 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 23 | `64%` | `2 & 5 & 0.612000 & 0.166400 & 0.189100 & 0.047300 & 0.022700 & 0.843300 & 0.004300 & 0.261600 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 41 | `0.1142` | `5 & 5 & 0.718600 & 0.095700 & 0.114500 & 0.103800 & 0.018800 & 0.836700 & 0.050900 & 0.267200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_sweep_results.tex` | 42 | `64%` | `5 & 10 & 0.625300 & 0.175000 & 0.239200 & 0.050900 & 0.064200 & 0.836700 & 0.050900 & 0.267200 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 43 | `0.1142` | `5 & 15 & 0.688100 & 0.114100 & 0.151500 & 0.086000 & 0.037500 & 0.836700 & 0.050900 & 0.267200 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_sweep_results.tex` | 47 | `0.2097` | `6 & 5 & 0.611700 & 0.004400 & 0.209500 & 0.041200 & 0.205100 & 0.853300 & 0.128300 & 0.257500 \\` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_sweep_results.tex` | 58 | `64%` | `8 & 3 & 0.648200 & 0.385500 & 0.245800 & 0.050900 & -0.139600 & 0.860000 & 0.095800 & 0.248300 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 59 | `64%` | `8 & 5 & 0.648500 & 0.212000 & 0.245800 & 0.050900 & 0.033800 & 0.860000 & 0.095800 & 0.248300 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 60 | `64%` | `8 & 10 & 0.648500 & 0.142300 & 0.245800 & 0.050900 & 0.103500 & 0.860000 & 0.095800 & 0.248300 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 61 | `64%` | `8 & 15 & 0.648500 & 0.186200 & 0.245800 & 0.050900 & 0.059600 & 0.860000 & 0.095800 & 0.248300 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 63 | `0.0327` | `9 & 1 & 0.581800 & 0.004000 & 0.122800 & 0.032100 & 0.118800 & 0.870000 & 0.030500 & 0.241200 \\` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `paper/tables/tab_sweep_results.tex` | 63 | `0.0323` | `9 & 1 & 0.581800 & 0.004000 & 0.122800 & 0.032100 & 0.118800 & 0.870000 & 0.030500 & 0.241200 \\` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `paper/tables/tab_sweep_results.tex` | 86 | `64%` | `13 & 0 & 0.640000 & NaN & 0.227200 & 0.052900 & NaN & 0.876700 & 0.030500 & 0.274800 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 95 | `0.1142` | `14 & 5 & 0.768300 & 0.071100 & 0.114900 & 0.144500 & 0.043800 & 0.860000 & 0.058200 & 0.274800 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_sweep_results.tex` | 109 | `64%` | `16 & 15 & 0.651700 & 0.051200 & 0.050600 & 0.064600 & -0.000600 & 0.824300 & 0.002600 & 0.255500 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_sweep_results.tex` | 115 | `0.1142` | `17 & 15 & 0.698000 & 0.114700 & 0.075100 & 0.069700 & -0.039600 & 0.860000 & 0.001100 & 0.245300 \\` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `paper/tables/tab_threshold_tradeoff.tex` | 8 | `64%` | `0 & 0.741800 & 0.830300 & 0.064900 & 0.024800 & 0.086500 & 0.178600 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_threshold_tradeoff.tex` | 16 | `64%` | `8 & 0.648500 & 0.886900 & 0.245800 & 0.064000 & 0.050900 & 0.322600 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_threshold_tradeoff.tex` | 17 | `64%` | `9 & 0.638300 & 0.743400 & 0.101800 & 0.064300 & 0.043800 & 0.077900 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `paper/tables/tab_threshold_tradeoff.tex` | 24 | `64%` | `16 & 0.651700 & 0.720200 & 0.050600 & 0.019500 & 0.064600 & 0.113000 \\` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 131 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ ($95\%$ device bootstrap C...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `PROJECT_MASTER_GUIDE.md` | 137 | `2.67` | `...iarity gap** ($\text{FAR}_A = 2.67\%$ vs $\text{FAR}_B = 22.08\%...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 137 | `22.08` | `... = 2.67\%$ vs $\text{FAR}_B = 22.08\%$), and establish the empiri...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 137 | `19.41` | `...$) induces a catastrophic **$+19.41\%$ familiarity gap** ($\text{...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), it...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `30.08` | `...$) to surge from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84.63\%$). Th...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), it causes Fals...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `11.90` | `...ue stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `8.49` | `...($\text{FRR}$) to surge from $8.49\%$ to $30.08\%$ (+21.59 pp, p...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 140 | `84.63` | `...08\%$ (+21.59 pp, peaking at $84.63\%$). This demonstrates that i...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `PROJECT_MASTER_GUIDE.md` | 143 | `99.43` | `...mentally required, achieving $99.43\% \pm 0.24\%$ Macro-$F_1$.` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 146 | `8.49` | `...tion by more than half (from $8.49\%$ down to $3.54\%$), elevati...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 146 | `3.54` | `... half (from $8.49\%$ down to $3.54\%$), elevating AMR network av...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 146 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 184 | `19.41` | `...2.1%**—an optimism gap of **$+19.41\%$**!` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 218 | `64%` | `...re map \| Contrastive latent \| 64 (prototype space) \| **292 com...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 219 | `99.43` | `... \| 93.85% \| 96.2% \| 94.7% \| **99.43% ± 0.24% Macro-F1** \|` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 220 | `0.9490` | `... 90.23% \| ≈ 92.5% \| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 220 | `0.9530` | `...\| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)** \|` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 221 | `12.35` | `...t isolated \| Not isolated \| **12.35%** (95% CI: [7.01%, 18.77%]) \|` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `PROJECT_MASTER_GUIDE.md` | 222 | `11.55` | `...hold \| Distance threshold \| **11.55%** (95% CI: [7.03%, 16.53%]) \|` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `PROJECT_MASTER_GUIDE.md` | 223 | `2.67` | `...ted \| **22.08%** (vs. FAR_A = 2.67%) \|` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 223 | `22.08` | `...evaluated \| Not evaluated \| **22.08%** (vs. FAR_A = 2.67%) \|` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 224 | `1.47` | `...reported \| None reported \| **+1.47%** (95% CI: [+0.72%, +2.40%] m...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `PROJECT_MASTER_GUIDE.md` | 225 | `19.41` | `...reported \| None reported \| **+19.41%** (acute threshold overfittin...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 226 | `8.49` | `...≈ 6.15% \| ≈ 5.5% \| ≈ 7.2% \| **8.49%** (95% CI: [7.16%, 10.06%]) \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 227 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 227 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 228 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 228 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 228 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `PROJECT_MASTER_GUIDE.md` | 229 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 229 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 231 | `0.2097` | `...orted \| None reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `PROJECT_MASTER_GUIDE.md` | 231 | `0.1142` | `... reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `PROJECT_MASTER_GUIDE.md` | 232 | `0.0327` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 232 | `0.0323` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 260 | `65.7` | `...ean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `PROJECT_MASTER_GUIDE.md` | 260 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$ with a strictly positive 9...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `PROJECT_MASTER_GUIDE.md` | 265 | `2.67` | `...trangers show $\text{FAR}_A = 2.67\%$, yet true physical strange...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 265 | `22.08` | `... penetrate at $\text{FAR}_B = 22.08\%$—a massive optimism gap of ...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 265 | `19.41` | `...gap of **$\Delta\text{FAR} = +19.41\%$**. The threshold stabilize...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 270 | `65.7` | `...e rates between $42.6\%$ and $65.7\%$) belong to **Hardware Bloc...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `PROJECT_MASTER_GUIDE.md` | 270 | `0.2097` | `... and vulnerability is $\rho = 0.2097$ ($p = 0.1142, n=58$). This d...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `PROJECT_MASTER_GUIDE.md` | 270 | `0.1142` | `...lity is $\rho = 0.2097$ ($p = 0.1142, n=58$). This demonstrates th...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `4.43` | `...ation from $11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, wit...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `30.08` | `...rs surges from $8.49\%$ to **$30.08\%$** on average (+21.59 pp, p...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `21.59` | `...to **$30.08\%$** on average (+21.59 pp, peaking at $84.63\%$). In...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `62.8%` | `...11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, with 4 episodes...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `11.90` | `...ue stranger penetration from $11.90\%$ down to $4.43\%$ (a $62.8\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `8.49` | `...ate smart meters surges from $8.49\%$ to **$30.08\%$** on averag...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `0.0327` | `...s absolute estimation error ($0.0327$) is comparable to naive test...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `0.0323` | `...s absolute estimation error ($0.0327$) is comparable to naive tes...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 275 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$). In a municipal AMR grid,...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `PROJECT_MASTER_GUIDE.md` | 280 | `64%` | `...nds to $\Delta\text{FAR} = +1.64\%$ as instantaneous packet no...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 280 | `0.9490` | `...{AUROC} = 0.9670$** (up from $0.9490$), while the familiarity gap ...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 280 | `8.49` | `...f: **$\text{FRR}$ drops from $8.49\%$ to $3.54\%$**, elevating g...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 280 | `3.54` | `...FRR}$ drops from $8.49\%$ to $3.54\%$**, elevating gateway avail...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 280 | `0.9670` | `...n climbs to **$\text{AUROC} = 0.9670$** (up from $0.9490$), while ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 300 | `19.41` | `F1["Identified Familiarity Gap (+1.47% matched, +19.41% single-proxy)"]` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 300 | `1.47` | `F1["Identified Familiarity Gap (+1.47% matched, +19.41% single-proxy)"]` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `PROJECT_MASTER_GUIDE.md` | 301 | `30.08` | `F2["Quantified Robust Availability Cost (FRR surges to 30.08%)"]` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 473 | `12.35` | `...gers)** \| Device ($n=60$) \| **12.35%** \| [7.01%, 18.77%] \| 4.84% \|...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `PROJECT_MASTER_GUIDE.md` | 474 | `11.55` | `...gers)** \| Device ($n=58$) \| **11.55%** \| [7.03%, 16.53%] \| 6.55% \|...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `PROJECT_MASTER_GUIDE.md` | 476 | `8.49` | `...FRR)** \| Episode ($n=20$) \| **8.49%** \| [7.16%, 10.06%] \| 3.40% \|...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 477 | `0.9530` | `...n A)** \| Episode ($n=20$) \| **0.9530** \| [0.9413, 0.9625] \| 0.0240...` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 478 | `0.9490` | `...n B)** \| Episode ($n=20$) \| **0.9490** \| [0.9367, 0.9605] \| 0.0284...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 479 | `99.43` | `...F_1$** \| Episode ($n=20$) \| **99.43%** \| [99.32%, 99.53%] \| 0.24% ...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 481 | `65.7` | `...ean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `PROJECT_MASTER_GUIDE.md` | 490 | `1.47` | `...AR}_{\text{matched}}$):** **$+1.47\%$** with a **strictly positi...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `PROJECT_MASTER_GUIDE.md` | 502 | `2.67` | `... **$k=1$** (Single radio) \| **2.67%** \| **22.08%** \| 10.39% \| **+...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 502 | `22.08` | `...Single radio) \| **2.67%** \| **22.08%** \| 10.39% \| **+19.41%** \| **...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 502 | `19.41` | `...** \| **22.08%** \| 10.39% \| **+19.41%** \| **Acute threshold overfit...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `PROJECT_MASTER_GUIDE.md` | 505 | `8.49` | `\| **$k=10$** \| 10.53% \| 12.61% \| 8.49% \| +2.08% \| Robust boundary formation. \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 506 | `11.90` | `\| **$k=15$** \| 11.34% \| 11.90% \| 8.49% \| +0.56% \| Convergence to full-proxy operating baseline. \|` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 506 | `11.34` | `\| **$k=15$** \| 11.34% \| 11.90% \| 8.49% \| +0.56% \| Convergence to full-proxy operating baseline. \|` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 506 | `8.49` | `\| **$k=15$** \| 11.34% \| 11.90% \| 8.49% \| +0.56% \| Convergence to full-proxy operating baseline. \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 516 | `64%` | `\| **Device 50** \| **64.66%** \| 8 \| Block 4 (Other Model, IDs 46–60) \| Reliable \|` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 524 | `0.2097` | `...unique devices yields $\rho = 0.2097$ ($p = 0.1142, n=58$).` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `PROJECT_MASTER_GUIDE.md` | 524 | `0.1142` | `... yields $\rho = 0.2097$ ($p = 0.1142, n=58$).` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `PROJECT_MASTER_GUIDE.md` | 532 | `11.55` | `...040 \| **11.90%** (ep. mean) / 11.55% (dev. boot) \| **8.49%** \| Sta...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `PROJECT_MASTER_GUIDE.md` | 532 | `11.90` | `...int ($\tau^*$)** \| 0.7040 \| **11.90%** (ep. mean) / 11.55% (dev. b...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 532 | `8.49` | `...ean) / 11.55% (dev. boot) \| **8.49%** \| Standard screening; balan...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 533 | `4.43` | `...ext{robust}}$)** \| 0.8540 \| **4.43%** \| **30.08%** \| **Catastroph...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 533 | `30.08` | `...$)** \| 0.8540 \| **4.43%** \| **30.08%** \| **Catastrophic availabili...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 535 | `4.43` | `...ue penetration from 11.90% to 4.43% (a 62.8% reduction, with 4 ep...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 535 | `30.08` | `..., False Rejection surges to **30.08%** on average (+21.59 pp, and ...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 535 | `21.59` | `...es to **30.08%** on average (+21.59 pp, and reaches **84.63%** in...` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 535 | `62.8%` | `...ation from 11.90% to 4.43% (a 62.8% reduction, with 4 episodes re...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `PROJECT_MASTER_GUIDE.md` | 535 | `11.90` | `...e-mean rogue penetration from 11.90% to 4.43% (a 62.8% reduction, ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 535 | `84.63` | `...age (+21.59 pp, and reaches **84.63%** in episode 19), which would...` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `PROJECT_MASTER_GUIDE.md` | 540 | `0.0327` | `- **LOPO Bias:** $+0.0138$ (mean absolute error: $0.0327$)` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 540 | `0.0323` | `- **LOPO Bias:** $+0.0138$ (mean absolute error: $0.0327$)` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 541 | `0.0327` | `- **Naive Packet-Disjoint Bias:** $-0.0056$ (mean absolute error: $0.0323$)` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 541 | `0.0323` | `- **Naive Packet-Disjoint Bias:** $-0.0056$ (mean absolute error: $0.0323$)` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 543 | `0.0327` | `...hin empirical noise ($\approx 0.032$ vs $0.033$). While LOPO prov...` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 543 | `0.0323` | `...hin empirical noise ($\approx 0.032$ vs $0.033$). While LOPO prov...` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `PROJECT_MASTER_GUIDE.md` | 553 | `11.90` | `...Packet Baseline)** \| 11.34% \| 11.90% \| 8.49% \| +0.56% \| 0.9490 \| B...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 553 | `11.34` | `... (Single Packet Baseline)** \| 11.34% \| 11.90% \| 8.49% \| +0.56% \| 0...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `PROJECT_MASTER_GUIDE.md` | 553 | `0.9490` | `...% \| 11.90% \| 8.49% \| +0.56% \| 0.9490 \| Baseline single-frame scree...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 553 | `8.49` | `...seline)** \| 11.34% \| 11.90% \| 8.49% \| +0.56% \| 0.9490 \| Baseline ...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 554 | `64%` | `... 11.22% \| 4.37% \| +1.27% \| 0.9642 \| FRR drops by half; AUROC c...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 554 | `11.22` | `... (3-Packet Burst)** \| 9.95% \| 11.22% \| 4.37% \| +1.27% \| 0.9642 \| F...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 554 | `4.37` | `...t Burst)** \| 9.95% \| 11.22% \| 4.37% \| +1.27% \| 0.9642 \| FRR drops...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 554 | `0.9642` | `...% \| 11.22% \| 4.37% \| +1.27% \| 0.9642 \| FRR drops by half; AUROC cl...` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 555 | `64%` | `...**10.45%** \| **3.54%** \| **+1.64%** \| **0.9670** \| **FRR drops ...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 555 | `3.54` | `... \| **8.81%** \| **10.45%** \| **3.54%** \| **+1.64%** \| **0.9670** \|...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 555 | `10.45` | `...cket Burst)** \| **8.81%** \| **10.45%** \| **3.54%** \| **+1.64%** \| ...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 555 | `0.9670` | `... \| **3.54%** \| **+1.64%** \| **0.9670** \| **FRR drops by 58% (Grid ...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 557 | `64%` | `...omes sharper ($+0.56\% \to +1.64\%$), confirming that identity...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `PROJECT_MASTER_GUIDE.md` | 557 | `3.54` | `...n by more than half (down to $3.54\%$), elevating network reliab...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 569 | `99.43` | `...ntally required, achieving **$99.43\% \pm 0.24\%$ Macro-$F_1$** a...` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 569 | `0.9490` | `... 0.24\%$ Macro-$F_1$** and **$0.9490 - 0.9670$ AUROC** by performi...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 569 | `0.9670` | `...Macro-$F_1$** and **$0.9490 - 0.9670$ AUROC** by performing non-li...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 596 | `8.49` | `...itimate false rejection from $8.49\%$ to $3.54\%$ while elevatin...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `PROJECT_MASTER_GUIDE.md` | 596 | `3.54` | `...e rejection from $8.49\%$ to $3.54\%$ while elevating AUROC to $...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `PROJECT_MASTER_GUIDE.md` | 596 | `0.9670` | `...\%$ while elevating AUROC to $0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 32 | `1.47` | `...text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ device-level boots...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `README.md` | 33 | `11.55` | `...%, 18.77\%]$; $\text{FAR}_B = 11.55\%$, $95\%$ CI: $[7.03\%, 16.5...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `README.md` | 33 | `12.35` | `...ted episodes ($\text{FAR}_A = 12.35\%$, $95\%$ CI: $[7.01\%, 18.7...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `README.md` | 34 | `19.41` | `...xy distortion ($k=1$ yields $+19.41\%$ gap).` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 35 | `65.7` | `...ean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode d...` | 65.69% (0.656944, device 48 mean FAR_B) | **VERIFIED (per-device ranking)** |
| `README.md` | 36 | `4.43` | `...enetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at ...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `README.md` | 36 | `30.08` | `...FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `README.md` | 36 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `README.md` | 36 | `62.8%` | `...rom $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at the cost of ...` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `README.md` | 36 | `11.90` | `...ue stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ re...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `README.md` | 36 | `8.49` | `...the cost of FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 38 | `8.49` | `...itimate false rejection from $8.49\%$ to $3.54\%$ (boosting avai...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 38 | `3.54` | `...e rejection from $8.49\%$ to $3.54\%$ (boosting availability to ...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 38 | `0.9670` | `...rimination to $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 46 | `12.35` | `...s)** \| Packet-disjoint test \| 12.35% \| [7.01%, 18.77%] (device boo...` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `README.md` | 47 | `11.55` | `...** \| Identity-disjoint test \| 11.55% \| [7.03%, 16.53%] (device boo...` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `README.md` | 48 | `1.47` | `... \| Device-matched paired \| **+1.47%** \| **[+0.72%, +2.40%]** (dev...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `README.md` | 49 | `2.67` | `...**+19.41%** \| $\text{FAR}_A = 2.67\%$, $\text{FAR}_B = 22.08\%$ ...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 49 | `22.08` | `..._A = 2.67\%$, $\text{FAR}_B = 22.08\%$ \|` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 49 | `19.41` | `... ($k=1$)** \| Proxy sweep \| **+19.41%** \| $\text{FAR}_A = 2.67\%$, ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 50 | `4.43` | `... \| $\text{FAR}_B: 11.90\% \to 4.43\%$ (episode mean) \| FRR surge...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `README.md` | 50 | `30.08` | `... FRR surges from $8.49\%$ to $30.08\%$ (+21.59 pp) \|` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `README.md` | 50 | `21.59` | `... from $8.49\%$ to $30.08\%$ (+21.59 pp) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `README.md` | 50 | `11.90` | `...xy rejection \| $\text{FAR}_B: 11.90\% \to 4.43\%$ (episode mean) ...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `README.md` | 50 | `8.49` | `...sode mean) \| FRR surges from $8.49\%$ to $30.08\%$ (+21.59 pp) \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 51 | `8.49` | `...ision fusion \| **$\text{FRR}: 8.49\% \to 3.54\%$** \| **AUROC cli...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 51 | `3.54` | `...n \| **$\text{FRR}: 8.49\% \to 3.54\%$** \| **AUROC climbs to $0.9...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 51 | `10.45` | `...$0.9670$**, $\text{FAR}_B \to 10.45\%$ \|` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 51 | `0.9670` | `....54\%$** \| **AUROC climbs to $0.9670$**, $\text{FAR}_B \to 10.45\%...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 52 | `99.43` | `\| **Closed-Set Macro $F_1$** \| Enrolled authentication \| 99.43% \| [99.32%, 99.53%] \|` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `README.md` | 53 | `0.9490` | `\| **Open-Set AUROC** \| Identity-disjoint (single) \| 0.9490 \| [0.9367, 0.9605] \|` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 63 | `64%` | `...re map \| Contrastive latent \| 64 (prototype space) \| **292 com...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `README.md` | 64 | `99.43` | `... \| 93.85% \| 96.2% \| 94.7% \| **99.43% ± 0.24%** \|` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `README.md` | 65 | `0.9490` | `... 90.23% \| ≈ 92.5% \| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 65 | `0.9530` | `...\| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)** \|` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 66 | `12.35` | `...t isolated \| Not isolated \| **12.35%** [95% CI: 7.01%, 18.77%] \|` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `README.md` | 67 | `11.55` | `...hold \| Distance threshold \| **11.55%** [95% CI: 7.03%, 16.53%] \|` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `README.md` | 68 | `2.67` | `...ted \| **22.08%** (vs. FAR_A = 2.67%) \|` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 68 | `22.08` | `...evaluated \| Not evaluated \| **22.08%** (vs. FAR_A = 2.67%) \|` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 69 | `1.47` | `...reported \| None reported \| **+1.47%** [95% CI: +0.72%, +2.40% mat...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `README.md` | 70 | `19.41` | `...reported \| None reported \| **+19.41%** (severe threshold overfitti...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `README.md` | 71 | `8.49` | `...≈ 6.15% \| ≈ 5.5% \| ≈ 7.2% \| **8.49%** [95% CI: 7.16%, 10.06%] \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `README.md` | 72 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `README.md` | 72 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `README.md` | 73 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `README.md` | 73 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `README.md` | 73 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `README.md` | 74 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 74 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `README.md` | 76 | `0.2097` | `...orted \| None reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `README.md` | 76 | `0.1142` | `... reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `README.md` | 77 | `0.0327` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `README.md` | 77 | `0.0323` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `reports/experiment_log.md` | 11 | `64%` | `- **Operating System:** Windows 11 AMD64` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `reports/experiment_log.md` | 74 | `99.43` | `- **Closed-Set Calibration Accuracy:** $99.43\% \pm 0.24\%$ macro-$F_1$.` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 76 | `12.35` | `- **$\text{FAR}_A$ (Familiar Strangers, Packet-Disjoint):** $12.35\%$ (95% CI: [7.01%, 18.77%])` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `reports/experiment_log.md` | 77 | `11.55` | `- **$\text{FAR}_B$ (True Strangers, Identity-Disjoint):** $11.55\%$ (95% CI: [7.03%, 16.53%])` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `reports/experiment_log.md` | 78 | `8.49` | `- **False Rejection Rate (FRR):** $8.49\%$ (95% CI: [7.16%, 10.06%])` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 79 | `0.9490` | `- **AUROC:** Condition A: $0.9530$; Condition B: $0.9490$.` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 79 | `0.9530` | `- **AUROC:** Condition A: $0.9530$; Condition B: $0.9490$.` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 87 | `1.47` | `...AR}_{\text{matched}}$):** **$+1.47\%$** with a **strictly positi...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `reports/experiment_log.md` | 91 | `2.67` | `...roxy device): $\text{FAR}_A = 2.67\%$, $\text{FAR}_B = 22.08\%$,...` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `reports/experiment_log.md` | 91 | `22.08` | `..._A = 2.67\%$, $\text{FAR}_B = 22.08\%$, **$\Delta\text{FAR} = +19...` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `reports/experiment_log.md` | 91 | `19.41` | `...08\%$, **$\Delta\text{FAR} = +19.41\%$**, $\text{FRR} = 10.39\%$ ...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `reports/experiment_log.md` | 94 | `8.49` | `...AR} = +2.08\%$, $\text{FRR} = 8.49\%$` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 95 | `11.90` | `...A = 11.34\%$, $\text{FAR}_B = 11.90\%$, $\Delta\text{FAR} = +0.56...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `reports/experiment_log.md` | 95 | `11.34` | `- $k=15$: $\text{FAR}_A = 11.34\%$, $\text{FAR}_B = 11.90\%$,...` | 11.34% (0.113422, episode mean FAR_A L=1) | **VERIFIED (episode mean)** |
| `reports/experiment_log.md` | 95 | `8.49` | `...AR} = +0.56\%$, $\text{FRR} = 8.49\%$` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 98 | `64%` | `...e 48 ($65.69\%$), Device 50 ($64.66\%$), Device 46 ($63.18\%$)...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `reports/experiment_log.md` | 100 | `0.2097` | `...earman Correlation:** $\rho = 0.2097$ ($p = 0.1142, n=58$ unique d...` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `reports/experiment_log.md` | 100 | `0.1142` | `...tion:** $\rho = 0.2097$ ($p = 0.1142, n=58$ unique devices) after ...` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `reports/experiment_log.md` | 103 | `4.43` | `...penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `reports/experiment_log.md` | 103 | `62.8%` | `...from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `reports/experiment_log.md` | 103 | `11.90` | `...ue stranger penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ red...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `reports/experiment_log.md` | 104 | `30.08` | `... Rate surges from $8.49\% \to 30.08\%$ on average (+21.59 pp, pea...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `reports/experiment_log.md` | 104 | `21.59` | `...9\% \to 30.08\%$ on average (+21.59 pp, peaking at $84.63\%$).` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `reports/experiment_log.md` | 104 | `8.49` | `...e Rejection Rate surges from $8.49\% \to 30.08\%$ on average (+2...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 104 | `84.63` | `...erage (+21.59 pp, peaking at $84.63\%$).` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `reports/experiment_log.md` | 107 | `0.0327` | `- **Naive Packet-Disjoint Absolute Error:** $0.0323$` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `reports/experiment_log.md` | 107 | `0.0323` | `- **Naive Packet-Disjoint Absolute Error:** $0.0323$` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `reports/experiment_log.md` | 108 | `0.0327` | `- **LOPO Absolute Error:** $0.0327$` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `reports/experiment_log.md` | 108 | `0.0323` | `- **LOPO Absolute Error:** $0.0327$` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |
| `reports/experiment_log.md` | 112 | `11.90` | `...ne ($L=1$):** $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\...` | 11.90% (0.119046, episode mean) | **VERIFIED (episode mean)** |
| `reports/experiment_log.md` | 112 | `0.9490` | `...} = +0.56\%$, $\text{AUROC} = 0.9490$.` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 112 | `8.49` | `...}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\Delta\text{FAR} = +0.56...` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 113 | `64%` | `... +1.27\%$, $\text{AUROC} = 0.9642$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `reports/experiment_log.md` | 113 | `11.22` | `...on ($L=3$):** $\text{FAR}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\...` | 11.22% (0.112182, burst L=3 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 113 | `4.37` | `...}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\Delta\text{FAR} = +1.27...` | 4.37% (0.043740, burst L=3 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 113 | `0.9642` | `...} = +1.27\%$, $\text{AUROC} = 0.9642$.` | 0.9642 (0.964244, burst L=3 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 114 | `64%` | `...54\%$, $\Delta\text{FAR} = +1.64\%$, $\text{AUROC} = 0.9670$.` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `reports/experiment_log.md` | 114 | `3.54` | `...}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\Delta\text{FAR} = +1.64...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 114 | `10.45` | `...on ($L=5$):** $\text{FAR}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\...` | 10.45% (0.104538, burst L=5 FAR_B at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 114 | `0.9670` | `...} = +1.64\%$, $\text{AUROC} = 0.9670$.` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 115 | `3.54` | `...ection by more than half (to $3.54\%$) while elevating AUROC to ...` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 115 | `0.9670` | `...%$) while elevating AUROC to $0.9670$ and expanding the clean fami...` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 123 | `64%` | `...re map \| Contrastive latent \| 64 (prototype space) \| **292 com...` | 62.8% (62.7746% relative reduction in FAR_B) | **STALE / SPECULATIVE** |
| `reports/experiment_log.md` | 124 | `99.43` | `... \| 93.85% \| 96.2% \| 94.7% \| **99.43% ± 0.24% Macro-F1** \|` | 99.43% (0.994270, macro-F1 mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 125 | `0.9490` | `... 90.23% \| ≈ 92.5% \| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)**...` | 0.9490 (0.948982, AUROC_B episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 125 | `0.9530` | `...\| 91.3% \| **0.9490 (AUROC_B), 0.9530 (AUROC_A)** \|` | 0.9530 (0.953018, AUROC_A episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 126 | `12.35` | `...t isolated \| Not isolated \| **12.35%** (95% CI: [7.01%, 18.77%]) \|` | 12.35% (device bootstrap mean, CI: [7.01, 18.77]) | **VERIFIED (device-level bootstrap)** |
| `reports/experiment_log.md` | 127 | `11.55` | `...hold \| Distance threshold \| **11.55%** (95% CI: [7.03%, 16.53%]) \|` | 11.55% (device bootstrap mean, CI: [7.03, 16.53]) | **VERIFIED (device-level bootstrap)** |
| `reports/experiment_log.md` | 128 | `2.67` | `...ted \| **22.08%** (vs. FAR_A = 2.67%) \|` | 2.67% (0.026744, k=1 FAR_A mean) | **VERIFIED (sweep k=1)** |
| `reports/experiment_log.md` | 128 | `22.08` | `...evaluated \| Not evaluated \| **22.08%** (vs. FAR_A = 2.67%) \|` | 22.08% (0.220808, k=1 FAR_B mean) | **VERIFIED (sweep k=1)** |
| `reports/experiment_log.md` | 129 | `1.47` | `...reported \| None reported \| **+1.47%** (95% CI: [+0.72%, +2.40%] m...` | +1.47% (device-matched DeltaFAR, CI: [+0.72%, +2.40%]) | **VERIFIED (matched evaluation)** |
| `reports/experiment_log.md` | 130 | `19.41` | `...reported \| None reported \| **+19.41%** (severe threshold overfitti...` | +19.41% (+0.194064, k=1 DeltaFAR mean) | **VERIFIED (sweep k=1)** |
| `reports/experiment_log.md` | 131 | `8.49` | `...≈ 6.15% \| ≈ 5.5% \| ≈ 7.2% \| **8.49%** (95% CI: [7.16%, 10.06%]) \|` | 8.49% (0.084860, FRR episode mean) | **VERIFIED (stats summary)** |
| `reports/experiment_log.md` | 132 | `4.43` | `...t provided \| Not provided \| **4.43%** (reduces episode-mean stran...` | 4.43% (0.044315, episode mean) | **VERIFIED** |
| `reports/experiment_log.md` | 132 | `62.8%` | `...-mean stranger penetration by 62.8%) \|` | 62.8% (62.7746% relative reduction in FAR_B) | **VERIFIED** |
| `reports/experiment_log.md` | 133 | `30.08` | `...antified \| Not quantified \| **30.08%** (surge of +21.59 pp, peak 8...` | 30.08% (0.300789, episode mean) | **VERIFIED** |
| `reports/experiment_log.md` | 133 | `21.59` | `...ified \| **30.08%** (surge of +21.59 pp, peak 84.63%) \|` | +21.59 pp (0.215929, episode mean difference) | **VERIFIED** |
| `reports/experiment_log.md` | 133 | `84.63` | `...%** (surge of +21.59 pp, peak 84.63%) \|` | 84.63% (0.846310, episode 19 max FRR_robust) | **VERIFIED (threshold tradeoff)** |
| `reports/experiment_log.md` | 134 | `3.54` | `...ted \| Not evaluated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 3.54% (0.035369, burst L=5 FRR at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 134 | `0.9670` | `...ated \| **FRR → 3.54%, AUROC → 0.9670** \|` | 0.9670 (0.966964, burst L=5 AUROC at tau_Youden) | **VERIFIED (burst summary)** |
| `reports/experiment_log.md` | 136 | `0.2097` | `...orted \| None reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.2097 (Spearman rho, n=58 unique devices) | **VERIFIED (neighbour analysis)** |
| `reports/experiment_log.md` | 136 | `0.1142` | `... reported \| **ρ = 0.2097 (p = 0.1142, n=58)** \|` | 0.1142 (Spearman p-value, n=58) | **VERIFIED (neighbour analysis)** |
| `reports/experiment_log.md` | 137 | `0.0327` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0327 (LOPO absolute error) | **VERIFIED (LOPO bias)** |
| `reports/experiment_log.md` | 137 | `0.0323` | `...evaluated \| Not evaluated \| **0.0327 (LOPO) vs 0.0323 (Naive)** \|` | 0.0323 (Naive packet-disjoint absolute error) | **VERIFIED (LOPO bias)** |


## Scan Summary
- Total number occurrences tracked: 4561
- Verified occurrences: 4037
- Stale / Disproved occurrences flagged: 524
