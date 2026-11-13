# Gap 3 — Paper Text (Audited and Corrected)
> **All numbers verified against repository CSVs via `audit/TASK1_numbers.py` and `audit/burst_at_robust.py`. Estimators and operating thresholds explicitly attributed.**

---

## A. Figure Caption

**Figure caption (≤ 3 sentences, estimators stated):**

> Fig. X. Security–availability trade-off of the robust threshold and multi-packet burst fusion. Panel (a) presents a per-episode scatter of true-stranger penetration ($\text{FAR}_B$) versus legitimate false rejection rate ($\text{FRR}$) across 20 random split episodes; large markers denote episode means (baseline: $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$; robust $\tau_{\text{robust}}$: $\text{FAR}_B = 4.43\%$, $\text{FRR} = 30.08\%$). Panel (b) shows the effect of temporal multi-packet burst fusion ($L \in \{1, 3, 5\}$ consecutive packets) evaluated at the baseline Youden threshold $\tau_{\text{Youden}}$ (not $\tau_{\text{robust}}$), where legitimate $\text{FRR}$ drops to $3.54\%$ while $\text{FAR}_B$ decreases to $10.45\%$; the unmatched familiarity-gap measure $\Delta\text{FAR} = \text{FAR}_B - \text{FAR}_A$ rises from $0.56\text{ pp}$ at $L=1$ to $1.64\text{ pp}$ at $L=5$.

---

## B. Results Subsection: Availability Cost of Robust Thresholding

### Availability Cost of Robust Thresholding

Tightening the decision threshold from the unconstrained Youden optimum to an identity-robust threshold $\tau_{\text{robust}}$—calibrated to bound the 90th-percentile false acceptance rate across held-out proxy devices to $\alpha \le 0.05$—substantially curtails true-stranger penetration. Evaluated across 20 random episodes, the episode-mean true-stranger acceptance rate ($\text{FAR}_B$) falls from **11.90%** to **4.43%**, corresponding to a **62.8%** relative reduction in rogue transmitter acceptance (source: `threshold_tradeoff.csv`, episode-mean estimator). When evaluated under the device-level bootstrap estimator (which resamples the 58 physical stranger devices across episodes to account for inter-device heterogeneity), the baseline $\text{FAR}_B$ is **11.55%** (95% CI: [7.03%, 16.53%]; source: `stats_summary.csv`). No device-level bootstrap estimate for $\text{FAR}_B$ under $\tau_{\text{robust}}$ exists in the saved experiment results (UNVERIFIED for that estimator); the paper reports the verified episode-mean value of **4.43%**.

This security enhancement incurs a severe operational availability penalty. The episode-mean false rejection rate ($\text{FRR}$) of legitimate enrolled meters surges from **8.49%** (95% CI: [7.16%, 10.06%]) under $\tau_{\text{Youden}}$ to **30.08%** under $\tau_{\text{robust}}$, representing an availability loss of **+21.59 percentage points**. Furthermore, the robust operating point introduces acute per-episode instability: across the 20 episodes, $\text{FRR}_{\text{robust}}$ spans from a minimum of **7.79%** (median **26.23%**) to a peak of **84.63%** in the worst episode (episode 4; standard deviation 17.86 pp).

To examine whether temporal aggregation can recover availability, multi-packet burst fusion was evaluated across $L \in \{1, 3, 5\}$ packets. Under the baseline Youden calibration rule ($\tau_{\text{Youden}}$), aggregating $L=5$ consecutive packets drives the legitimate $\text{FRR}$ down to **3.54%** (boosting enrolled availability to 96.46%) and improves open-set discrimination to an AUROC of **0.9670**, while $\text{FAR}_B$ decreases modestly from **11.90%** ($L=1$) to **10.45%** ($L=5$). (Note: burst fusion experiments in `scripts/07_burst_aggregation_experiment.py` were conducted at the baseline Youden threshold $\tau_{\text{Youden}}$, not $\tau_{\text{robust}}$; saved episode score files lack per-packet device identifiers, precluding multi-packet burst evaluation at $\tau_{\text{robust}}$ from existing artifacts).

---

## C. Discussion Paragraph + Limitation Sentence

### Discussion

These empirical findings demonstrate that attempting to eliminate stranger vulnerability solely by shifting a single-packet decision boundary imposes a prohibitive availability cost on legitimate AMR endpoints. While multi-packet burst fusion significantly reduces false rejections and recovers gateway availability under standard calibration, it does not eliminate stranger penetration ($\text{FAR}_B$ remains at 10.45% at $L=5$), nor does it resolve the underlying Familiar Stranger phenomenon. Furthermore, in the baseline burst aggregation sweep, the difference $\Delta\text{FAR} = \text{FAR}_B - \text{FAR}_A$ increases monotonically from 0.56 percentage points at $L=1$ to 1.64 percentage points at $L=5$. Because positive $\Delta\text{FAR}$ indicates that packet-disjoint evaluation ($\text{FAR}_A$) under-reports true stranger acceptance compared to identity-disjoint testing ($\text{FAR}_B$), this observed rise is an unmatched, confidence-interval-free observation from unstratified burst sweeps, rather than definitive evidence that fusion amplifies familiarity bias. Rigorous evaluation of burst fusion under matched-device pairing remains an important area for future investigation.

**Limitation sentence:** The experimental evaluation is restricted to a single publicly available 60-transmitter LoRa dataset collected with a single USRP N210 software-defined radio receiver at a fixed physical location, utilizing a Random Forest classifier over preamble features; generalization across diverse receiver hardware, carrier frequency offsets, varying channel conditions, or alternative deep learning architectures is not established by this study.

---

## D. LaTeX Table (booktabs)

```latex
\begin{table}[t]
\centering
\caption{Security and availability metrics across operating conditions (20 random episodes).
Baseline $\text{FAR}_B$ is reported as the device-level bootstrap mean across $n=58$ physical
strangers with 95\% CI; baseline $\text{FRR}$ and $\text{AUROC}$ report episode-level bootstrap
means with 95\% CIs from \texttt{stats\_summary.csv}. The robust threshold row ($\tau_{\text{robust}}$)
and burst aggregation rows ($L \in \{1, 3, 5\}$) report plain episode means across the 20 episodes
(no bootstrap CIs available in saved experiment tables). Burst fusion was evaluated under
$\tau_{\text{Youden}}$.}
\label{tab:gap3_results}
\begin{tabular}{@{}lcccc@{}}
\toprule
Operating Condition & $\text{FAR}_B$ (\%) & $\text{FRR}$ (\%) & AUROC & Calibration Rule \\
\midrule
Baseline $\tau_{\text{Youden}}$ ($L=1$)
  & $11.55^\dagger$ [7.03, 16.53]
  & $8.49$ [7.16, 10.06]
  & $0.9490$ [0.9367, 0.9605]
  & Youden's $J$ on proxy calibration \\
Robust threshold $\tau_{\text{robust}}$ ($L=1$)
  & $4.43$
  & $30.08$
  & $0.9490$
  & 90th-pctile proxy rejection ($\alpha \le 0.05$) \\
\midrule
Burst Fusion $L=1$
  & $11.90$
  & $8.49$
  & $0.9490$
  & Youden's $J$ (episode mean) \\
Burst Fusion $L=3$
  & $11.22$
  & $4.37$
  & $0.9642$
  & Youden's $J$ (episode mean) \\
Burst Fusion $L=5$
  & $10.45$
  & $3.54$
  & $0.9670$
  & Youden's $J$ (episode mean) \\
\bottomrule
\end{tabular}
\vspace{2pt}
\begin{flushleft}
\footnotesize
$^\dagger$Device-level bootstrap mean across 58 physical stranger devices (plain episode mean is $11.90\%$).
Robust threshold $\text{FAR}_B$ and $\text{FRR}$ have no device-level bootstrap estimates in \texttt{stats\_summary.csv}.
AUROC for $L=1$ is threshold-independent and evaluates enrolled vs.\ final-unknown test packet scores.
\end{flushleft}
\end{table}
```
