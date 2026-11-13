# Gap 3 Summary: Operational Security–Availability Tradeoff and Burst Recovery

> **Definition:** Gap 3 evaluates the operational security–availability tradeoff incurred by shifting from the baseline Youden acceptance threshold ($\tau_{\mathrm{Youden}}$) to an identity-robust threshold ($\tau_{\mathrm{robust}}$), and quantifies whether multi-packet burst fusion ($L \in \{1, 3, 5\}$) can recover the availability lost without sacrificing stranger rejection.

All numbers are strictly recomputed from `results/tables/threshold_tradeoff.csv`, `results/tables/burst_aggregation_results.csv`, and `results/tables/burst_robust_results.csv`.

## 1. Operating Point Comparison (L=1, n=20 episodes)

| Operating Point | Metric | Reported / Rounded | Unrounded Value | Std Dev | 95% Bootstrap CI | Estimator | Source File |
|---|---|---|---|---|---|---|---|
| **Baseline ($\tau_{\mathrm{Youden}}$)** | $\text{FAR}_A$ | 11.34% | 11.342188% (0.113422) | 4.9679% | [9.27%, 13.47%] | Episode mean (n=20) | `burst_aggregation_results.csv` |
| **Baseline ($\tau_{\mathrm{Youden}}$)** | $\text{FAR}_B$ | 11.90% | 11.904615% (0.119046) | 6.7237% | [9.12%, 14.77%] | Episode mean (n=20) | `threshold_tradeoff.csv` |
| **Baseline ($\tau_{\mathrm{Youden}}$)** | $\text{FRR}$ | 8.49% | 8.486005% (0.084860) | 3.4903% | [7.15%, 10.10%] | Episode mean (n=20) | `threshold_tradeoff.csv` |
| **Baseline ($\tau_{\mathrm{Youden}}$)** | $\Delta\text{FAR}$ | +0.56 pp | 0.562428 pp (0.005624) | 4.5185% | [-1.43 pp, 2.39 pp] | Episode mean (n=20) | Paired difference |
| **Robust ($\tau_{\mathrm{robust}}$)** | $\text{FAR}_A$ | 3.97% | 3.967188% (0.039672) | 1.9360% | [3.13%, 4.77%] | Episode mean (n=20) | `burst_robust_results.csv` |
| **Robust ($\tau_{\mathrm{robust}}$)** | $\text{FAR}_B$ | 4.43% | 4.431538% (0.044315) | 3.5252% | [2.98%, 5.97%] | Episode mean (n=20) | `threshold_tradeoff.csv` |
| **Robust ($\tau_{\mathrm{robust}}$)** | $\text{FRR}$ | 30.08% | 30.078880% (0.300789) | 17.8633% | [23.10%, 38.29%] | Episode mean (n=20) | `threshold_tradeoff.csv` |
| **Robust ($\tau_{\mathrm{robust}}$)** | $\Delta\text{FAR}$ | +0.46 pp | 0.464351 pp (0.004644) | 3.4667% | [-0.96 pp, 1.97 pp] | Episode mean (n=20) | Paired difference |

## 2. Quantitative Trade-off Shifts (Baseline $\to$ Robust)

| Tradeoff Metric | Reported Value | Unrounded Value | 95% Paired Bootstrap CI | Estimator / Note |
|---|---|---|---|---|
| **Absolute $\text{FAR}_B$ Change** | -7.47 pp | -7.473077 pp | [-9.93 pp, -5.29 pp] | Mean of paired episode differences |
| **Relative $\text{FAR}_B$ Reduction** | 62.8% (ratio of means) | 62.774619% (ratio of means) / 62.983104% (mean of ratios) | [52.31%, 73.26%] | Paired per-episode bootstrap resampled |
| **FRR Surge** | +21.59 pp | +21.592875 pp | [14.71 pp, 29.79 pp] | Mean of paired episode differences |
| **FRR Multiplicative Ratio** | 3.54x (ratio of means) | 3.544528x (ratio of means) / 3.877155x (mean of ratios) | [2.91x, 4.94x] | Paired per-episode bootstrap resampled |
| **Episodes with $\text{FAR}_B^{\mathrm{robust}} < \text{FAR}_B^{\mathrm{baseline}}$** | 20 / 20 (100.0%) | 20 / 20 | [20, 20] | Security gain is 100% consistent across all episodes |
| **Episodes with $\text{FRR}^{\mathrm{robust}} > 50\%$** | 2 / 20 (10.0%) | 2 / 20 | [0, 4] | Severe outage in Ep 10 (57.71%) and Ep 19 (84.63%) |

## 3. Burst Fusion Recovery at Baseline Youden Threshold ($\tau_{\mathrm{Youden}}$)

| Burst Length ($L$) | Legitimate FRR (Mean) | 95% Bootstrap CI | Stranger $\text{FAR}_B$ (Mean) | 95% Bootstrap CI | $\Delta\text{FAR}$ | AUROC |
|---|---|---|---|---|---|---|
| **$L=1$** | 8.49% (0.084860) | [7.12%, 10.07%] | 11.90% (0.119046) | [9.08%, 14.85%] | +0.56 pp | 0.9490 |
| **$L=3$** | 4.37% (0.043740) | [3.03%, 6.17%] | 11.22% (0.112182) | [8.31%, 14.24%] | +1.27 pp | 0.9642 |
| **$L=5$** | 3.54% (0.035369) | [1.79%, 5.84%] | 10.45% (0.104538) | [7.75%, 13.28%] | +1.64 pp | 0.9670 |

## 4. Burst Fusion Recovery at Robust Threshold ($\tau_{\mathrm{robust}}$)

| Burst Length ($L$) | Legitimate FRR (Mean) | 95% Bootstrap CI | Stranger $\text{FAR}_B$ (Mean) | 95% Bootstrap CI | $\Delta\text{FAR}$ | AUROC |
|---|---|---|---|---|---|---|
| **$L=1$** | 30.08% (0.300789) | [23.08%, 38.40%] | 4.43% (0.044315) | [3.01%, 6.00%] | +0.46 pp | 0.9490 |
| **$L=3$** | 21.69% (0.216870) | [14.27%, 30.87%] | 5.72% (0.057156) | [4.06%, 7.43%] | +0.95 pp | 0.9642 |
| **$L=5$** | 18.13% (0.181298) | [10.29%, 27.66%] | 6.42% (0.064192) | [4.57%, 8.27%] | +1.36 pp | 0.9670 |

## 5. Summary of Gap 3 Verification Status Across Repository Text

- **Verified Baseline Values:** $\text{FAR}_B = 11.90\%$ (episode mean) / $11.55\%$ (device-level bootstrap), $\text{FRR} = 8.49\%$.
- **Verified Robust Values:** $\text{FAR}_B = 4.43\%$ (episode mean), $\text{FRR} = 30.08\%$.
- **Verified Shifts:** Stranger penetration reduction is $62.8\%$ ($62.77\%$), FRR surge is $+21.59\text{ pp}$.
- **Stale Mentions Replaced:** $4.17\%$, $30.18\%$, $+21.69\text{ pp}$, and $64\%$ have been replaced across all manuscript and documentation files.
