# Per-File Git Diff Summary (Part 1 & Gap 3 Corrections)

## `README.md`

```diff
@@ -35,2 +35,2 @@ To set that threshold, engineers need example strangers. So they borrow some unf
-6. **Hardness & Hardware Grouping:** Per-device vulnerability ranges from $0.0\%$ to $98.5\%$, with top vulnerable devices clustering tightly within hardware block 4 (IDs 46–60).
-7. **Availability Cost of Robust Thresholding ($\tau_{\text{robust}}$):** Reduces true stranger penetration from $11.55\%$ to $4.17\%$ at the cost of FRR surging from $8.49\%$ to $30.18\%$.
+6. **Hardness & Hardware Grouping:** Device-mean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode device penetration reaches up to 100%. Top vulnerable devices cluster tightly within hardware block 4 (IDs 46–60).
+7. **Availability Cost of Robust Thresholding ($\tau_{\text{robust}}$):** Reduces episode-mean true stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) at the cost of FRR surging from $8.49\%$ to $30.08\%$ (+21.59 pp).
```

```diff
@@ -38 +38 @@ To set that threshold, engineers need example strangers. So they borrow some unf
-9. **Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$):** Temporal fusion cuts legitimate false rejection from $8.49\%$ to $3.54\%$ (boosting availability to $96.46\%$) while elevating open-set discrimination to $\text{AUROC} = 0.9670$.
+9. **Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$ at $\tau^*$):** Evaluated at the baseline Youden threshold $\tau^*$, temporal fusion cuts legitimate false rejection from $8.49\%$ to $3.54\%$ (boosting availability to $96.46\%$) while elevating open-set discrimination to $\text{AUROC} = 0.9670$.
```

```diff
@@ -50,2 +50,2 @@ To set that threshold, engineers need example strangers. So they borrow some unf
-| **Robust threshold ($\tau_{\text{robust}}$)** | 90th-pctile proxy rejection | $\text{FAR}_B: 11.55\% \to 4.17\%$ | FRR surges from $8.49\%$ to $30.18\%$ |
-| **Multi-Packet Burst Fusion ($L=5$)** | Temporal decision fusion | **$\text{FRR}: 8.49\% \to 3.54\%$** | **AUROC climbs to $0.9670$**, $\text{FAR}_B \to 10.45\%$ |
+| **Robust threshold ($\tau_{\text{robust}}$)** | 90th-pctile proxy rejection | $\text{FAR}_B: 11.90\% \to 4.43\%$ (episode mean) | FRR surges from $8.49\%$ to $30.08\%$ (+21.59 pp) |
+| **Multi-Packet Burst Fusion ($L=5$, $\tau^*$)** | Temporal decision fusion | **$\text{FRR}: 8.49\% \to 3.54\%$** | **AUROC climbs to $0.9670$**, $\text{FAR}_B \to 10.45\%$ |
```

```diff
@@ -72,3 +72,3 @@ To set that threshold, engineers need example strangers. So they borrow some unf
-| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.17%** (drops intrusion by 64%) |
-| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.18%** (surge of +21.69%, peak 84.63%) |
-| **Multi-Packet Burst Fusion (L=5)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
+| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.43%** (reduces episode-mean stranger penetration by 62.8%) |
+| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.08%** (surge of +21.59 pp, peak 84.63%) |
+| **Multi-Packet Burst Fusion (L=5, $\tau^*$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
```

## `PROJECT_MASTER_GUIDE.md`

```diff
@@ -140 +140 @@ We discover and document the non-linear scaling law of outlier exposure in physi
-We compute for the first time the real-world operational penalty of identity-robust thresholding: while $\tau_{\text{robust}}$ successfully drops true stranger penetration from $11.55\%$ to $4.17\%$, it causes False Rejection Rate ($\text{FRR}$) to surge to $30.18\%$ (peaking at $84.63\%$). This demonstrates that in battery-operated AMR networks, robust RFF cannot serve as an impenetrable perimeter gate and must be framed as a defense-in-depth screening layer.
+We compute for the first time the real-world operational penalty of identity-robust thresholding: while $\tau_{\text{robust}}$ reduces episode-mean true stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), it causes False Rejection Rate ($\text{FRR}$) to surge from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84.63\%$). This demonstrates that in battery-operated AMR networks, robust RFF cannot serve as an impenetrable perimeter gate and must be framed as a defense-in-depth screening layer.
```

```diff
@@ -227,3 +227,3 @@ The following table contrasts the actual empirical numbers reported by key exist
-| **Robust Remedy Acceptance (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.17%** (drops penetration by 64%) |
-| **Robust Availability Penalty (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.18%** (surge of +21.69%, peak 84.63%) |
-| **Multi-Packet Burst Fusion (L=5)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
+| **Robust Remedy Acceptance (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.43%** (reduces episode-mean stranger penetration by 62.8%) |
+| **Robust Availability Penalty (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.08%** (surge of +21.59 pp, peak 84.63%) |
+| **Multi-Packet Burst Fusion (L=5, $\tau^*$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
```

```diff
@@ -260 +260 @@ The following table contrasts the actual empirical numbers reported by key exist
-  In random episode allocations, the mean familiarity gap is $\Delta\text{FAR} = +0.56\%$ ($95\%$ CI: $[-1.55\%, +2.39\%]$, positive in $65\%$ of episodes). However, naive episode-level pooling masks the familiarity effect because baseline transmitter hardness varies widely (from $0.0\%$ to $98.5\%$). To eliminate this hardware confound, our novel **Device-Matched Paired Design** evaluates the exact same physical devices on identical test packets at $\tau_{\text{full}}$ (familiar) versus $\tau_{(-j)}$ (unfamiliar). This isolates the pure familiarity effect, proving a **statistically significant gap of $\Delta\text{FAR}_{\text{matched}} = +1.47\%$ with a strictly positive 95% device bootstrap CI: $[+0.72\%, +2.40\%]$**.
+  In random episode allocations, the mean familiarity gap is $\Delta\text{FAR} = +0.56\%$ ($95\%$ CI: $[-1.55\%, +2.39\%]$, positive in $65\%$ of episodes). However, naive episode-level pooling masks the familiarity effect because baseline transmitter hardness varies widely (Device-mean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode device penetration reaches up to 100%.). To eliminate this hardware confound, our novel **Device-Matched Paired Design** evaluates the exact same physical devices on identical test packets at $\tau_{\text{full}}$ (familiar) versus $\tau_{(-j)}$ (unfamiliar). This isolates the pure familiarity effect, proving a **statistically significant gap of $\Delta\text{FAR}_{\text{matched}} = +1.47\%$ with a strictly positive 95% device bootstrap CI: $[+0.72\%, +2.40\%]$**.
```

```diff
@@ -275 +275 @@ The following table contrasts the actual empirical numbers reported by key exist
-  LOPO provides a mathematically rigorous identity-disjoint validation protocol, but its absolute estimation error ($0.0327$) is comparable to naive testing ($0.0323$) due to finite proxy sample variance. Enforcing an identity-robust threshold ($\tau_{\text{robust}}$) slashes true stranger penetration from $11.55\%$ down to $4.17\%$ (with 4 episodes reaching $0.0\%$ penetration). However, this protection incurs a **catastrophic availability penalty**: the False Rejection Rate ($\text{FRR}$) of legitimate smart meters surges from $8.49\%$ to **$30.18\%$** on average (peaking at $84.63\%$). In a municipal AMR grid, rejecting 1 in 3 valid meter packets would trigger network packet storms and rapidly drain meter batteries.
+  LOPO provides a mathematically rigorous identity-disjoint validation protocol, but its absolute estimation error ($0.0327$) is comparable to naive testing ($0.0323$) due to finite proxy sample variance. Enforcing an identity-robust threshold ($\tau_{\text{robust}}$) reduces episode-mean true stranger penetration from $11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, with 4 episodes reaching $0.0\%$ penetration). However, this protection incurs a **catastrophic availability penalty**: the False Rejection Rate ($\text{FRR}$) of legitimate smart meters surges from $8.49\%$ to **$30.08\%$** on average (+21.59 pp, peaking at $84.63\%$). In a municipal AMR grid, rejecting 1 in 3 valid meter packets would trigger network packet storms and rapidly drain meter batteries.
```

```diff
@@ -301 +301 @@ flowchart TD
-        F2["Quantified Robust Availability Cost (FRR surges to 30.18%)"]
+        F2["Quantified Robust Availability Cost (FRR surges to 30.08%)"]
```

```diff
@@ -481 +481 @@ All reported numbers are calculated from 20 seeded experimental episodes across
-> **Key Finding:** In random episode device splits, $\Delta\text{FAR}$ is positive in 65% of episodes (13 of 20). However, naive episode-level pooling masks the familiarity effect because physical device heterogeneity is vast (individual device penetration ranges from 0.0% to 98.5%).
+> **Key Finding:** In random episode device splits, $\Delta\text{FAR}$ is positive in 65% of episodes (13 of 20). However, naive episode-level pooling masks the familiarity effect because physical device heterogeneity is vast (device-mean FAR_B ranges from 0.0% to 65.7% (device 48); single-episode device penetration reaches up to 100%).
```

```diff
@@ -532,2 +532,2 @@ The empirical vulnerability ranking across the 60 physical devices demonstrates
-| **Youden Operating Point ($\tau^*$)** | 0.7040 | **11.55%** | **8.49%** | Standard screening; balanced false alarms. |
-| **Identity-Robust Point ($\tau_{\text{robust}}$)** | 0.8540 | **4.17%** | **30.18%** | **Catastrophic availability loss!** Nearly 1 in 3 legitimate meter readings rejected. |
+| **Youden Operating Point ($\tau^*$)** | 0.7040 | **11.90%** (ep. mean) / 11.55% (dev. boot) | **8.49%** | Standard screening; balanced false alarms. |
+| **Identity-Robust Point ($\tau_{\text{robust}}$)** | 0.8540 | **4.43%** | **30.08%** | **Catastrophic availability loss!** Nearly 1 in 3 legitimate meter readings rejected. |
```

```diff
@@ -535 +535 @@ The empirical vulnerability ranking across the 60 physical devices demonstrates
-> Setting $\tau_{\text{robust}}$ to enforce 90th-percentile proxy rejection slashes rogue penetration from 11.55% to 4.17% (with 4 episodes reaching 0.0% penetration). However, False Rejection surges to **30.18%** on average (and reaches **84.63%** in episode 4), which would trigger severe radio retransmissions and drain meter batteries.
+> Setting $\tau_{\text{robust}}$ to enforce 90th-percentile proxy rejection reduces episode-mean rogue penetration from 11.90% to 4.43% (a 62.8% reduction, with 4 episodes reaching 0.0% penetration). However, False Rejection surges to **30.08%** on average (+21.59 pp, and reaches **84.63%** in episode 19), which would trigger severe radio retransmissions and drain meter batteries.
```

## `paper/abstract.md`

```diff
@@ -7 +7 @@ Our most striking finding concerns **proxy-count sensitivity**. Evaluating acros
-A key negative result concerns the cost of mitigation: an identity-robust threshold ($\tau_{\text{robust}}$) reduces true-stranger penetration from $11.55\%$ to $4.17\%$, but the False Rejection Rate surges from $8.49\%$ to $30.18\%$ — rejecting nearly 1 in 3 legitimate meter packets, which is operationally unacceptable for battery-powered AMR networks. Per-device vulnerability is severely heterogeneous ($0.0\%$ to $98.5\%$), with 7 of the 8 hardest rogues clustering in a single hardware block, though device-aggregated Spearman correlation between feature distance and vulnerability is not statistically significant ($\rho = 0.21$, $p = 0.11$, $n = 58$). While closed-set classification achieves $99.43\%$ macro-$F_1$, the open-set AUROC of $0.949$ with $\text{FAR}_B = 11.55\%$ and $\text{FRR} = 8.49\%$ confirms that RFFI serves as a defense-in-depth screening layer, not a standalone security gate. These findings establish that physical-layer authentication must be evaluated under identity-disjoint protocols with $\ge 5$ diverse proxy devices to avoid dangerously overestimating real-world protection.
+A key negative result concerns the cost of mitigation: an identity-robust threshold ($\tau_{\text{robust}}$) reduces episode-mean true-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), but the False Rejection Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp) — rejecting nearly 1 in 3 legitimate meter packets, which is operationally unacceptable for battery-powered AMR networks. Device-mean $\text{FAR}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episode device penetration reaches up to $100\%$, with 7 of the 8 hardest rogues clustering in a single hardware block, though device-aggregated Spearman correlation between feature distance and vulnerability is not statistically significant ($\rho = 0.21$, $p = 0.11$, $n = 58$). While closed-set classification achieves $99.43\%$ macro-$F_1$, the open-set AUROC of $0.949$ with $\text{FAR}_B = 11.55\%$ [device-level bootstrap: $11.55\%$, episode mean: $11.90\%$] and $\text{FRR} = 8.49\%$ confirms that RFFI serves as a defense-in-depth screening layer, not a standalone security gate. These findings establish that physical-layer authentication must be evaluated under identity-disjoint protocols with $\ge 5$ diverse proxy devices to avoid dangerously overestimating real-world protection.
```

## `paper/main.tex`

```diff
@@ -33 +33 @@ Our most striking finding concerns \textbf{proxy-count sensitivity}. Evaluating
-A key negative result concerns the cost of mitigation: an identity-robust threshold ($\tau_{\text{robust}}$) reduces true-stranger penetration from $11.55\%$ to $4.17\%$, but the False Rejection Rate surges from $8.49\%$ to $30.18\%$---rejecting nearly 1 in 3 legitimate meter packets, which is operationally unacceptable for battery-powered AMR networks. Temporal multi-packet burst fusion ($L=5$) reduces legitimate meter false rejection to $3.54\%$ (availability $96.46\%$) while elevating open-set discrimination to $\text{AUROC} = 0.9670$. Per-device vulnerability is severely heterogeneous ($0.0\%$ to $98.5\%$), with 7 of the 8 hardest rogues clustering in a single hardware block. These findings establish that physical-layer authentication must be evaluated under identity-disjoint protocols with $\ge 5$ diverse proxy devices to avoid dangerously overestimating real-world protection.
+A key negative result concerns the cost of mitigation: an identity-robust threshold ($\tau_{\text{robust}}$) reduces episode-mean true-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction), but the False Rejection Rate surges from $8.49\%$ to $30.08\%$ (+21.59 pp, peaking at $84.63\%$)---rejecting nearly 1 in 3 legitimate meter packets, which is operationally unacceptable for battery-powered AMR networks. Temporal multi-packet burst fusion ($L=5$, evaluated at $\tau_{\text{Youden}}$) reduces legitimate meter false rejection to $3.54\%$ (availability $96.46\%$) while elevating open-set discrimination to $\text{AUROC} = 0.9670$. Device-mean $\text{FAR}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episode device penetration reaches up to $100\%$, with 7 of the 8 hardest rogues clustering in a single hardware block. These findings establish that physical-layer authentication must be evaluated under identity-disjoint protocols with $\ge 5$ diverse proxy devices to avoid dangerously overestimating real-world protection.
```

```diff
@@ -60,2 +60,2 @@ We identify a fundamental methodological flaw in this evaluation paradigm: \text
-    \item \textbf{Transmitter Vulnerability Heterogeneity:} Per-device rankings show that rogue penetration varies from $0.0\%$ to $98.5\%$, with the top vulnerable transmitters clustering heavily within unaugmented hardware block 4 (IDs 46--60).
-    \item \textbf{Robust Threshold ($\tau_{\text{robust}}$) Trade-off:} We evaluate an identity-robust threshold enforcing 90th-percentile proxy rejection, showing that it lowers true-stranger penetration from $11.55\%$ to $4.17\%$ but imposes a steep operational availability penalty (FRR surges from $8.49\%$ to $30.18\%$).
+    \item \textbf{Transmitter Vulnerability Heterogeneity:} Device-mean $\text{FAR}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episode device penetration reaches up to $100\%$, with the top vulnerable transmitters clustering heavily within unaugmented hardware block 4 (IDs 46--60).
+    \item \textbf{Robust Threshold ($\tau_{\text{robust}}$) Trade-off:} We evaluate an identity-robust threshold enforcing 90th-percentile proxy rejection, showing that it reduces episode-mean true-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but imposes a steep operational availability penalty (FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$~pp increase).
```

```diff
@@ -84 +84 @@ Our research establishes six distinct dimensions of novelty over existing wirele
-    \item \textbf{Operational AMR Availability Cost:} We provide the first quantification of the real-world operational penalty imposed by robust open-set calibration ($\tau_{\text{robust}}$), revealing a severe $30.18\%$ false rejection rate in smart grid networks.
+    \item \textbf{Operational AMR Availability Cost:} We provide the first quantification of the real-world operational penalty imposed by robust open-set calibration ($\tau_{\text{robust}}$), revealing a severe $30.08\%$ false rejection rate in smart grid networks.
```

```diff
@@ -170,3 +170,3 @@ Legitimate Baseline FRR & Not controlled & DET trade-off & $\approx 6.15\%$ & $\
-Robust Remedy $\text{FAR}_{\text{robust}}$ & Not provided & Not provided & Not provided & Not provided & Not provided & \textbf{4.17\% (drops penetration by 64\%)} \\
-Robust Availability Penalty & Not quantified & Not quantified & Not quantified & Not quantified & Not quantified & \textbf{30.18\% (FRR surge $+21.7\%$)} \\
-Multi-Packet Burst Fusion ($L=5$) & Not evaluated & Not evaluated & Not evaluated & Not evaluated & Not evaluated & \textbf{$\text{FRR} \to 3.54\%$, $\text{AUROC} \to 0.9670$} \\
+Robust Remedy $\text{FAR}_{\text{robust}}$ & Not provided & Not provided & Not provided & Not provided & Not provided & \textbf{4.43\% (reduces penetration by 62.8\%)} \\
+Robust Availability Penalty & Not quantified & Not quantified & Not quantified & Not quantified & Not quantified & \textbf{30.08\% (FRR surge $+21.59$ pp)} \\
+Multi-Packet Burst Fusion ($L=5$, $\tau^*$) & Not evaluated & Not evaluated & Not evaluated & Not evaluated & Not evaluated & \textbf{$\text{FRR} \to 3.54\%$, $\text{AUROC} \to 0.9670$} \\
```

```diff
@@ -224,2 +224,2 @@ Evaluating proxy counts $k \in \{0, 1, 3, 5, 10, 15\}$ using nested prefixes rev
-\subsection{Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$)}
-In operational AMR networks, utility meters transmit periodic meter telemetry or short packet retransmission bursts. To evaluate whether temporal burst aggregation overcomes the single-packet baseline trade-off, we evaluate multi-packet decision fusion by averaging decision confidence over $L$ consecutive packet transmissions per physical device across all 20 evaluation episodes. Table~\ref{tab:burst_aggregation} and Figure~\ref{fig:burst} summarize the empirical results:
+\subsection{Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$ at $\tau^*$)}
+In operational AMR networks, utility meters transmit periodic meter telemetry or short packet retransmission bursts. To evaluate whether temporal burst aggregation overcomes the single-packet baseline trade-off, we evaluate multi-packet decision fusion by averaging decision confidence over $L$ consecutive packet transmissions per physical device across all 20 evaluation episodes, operating at the baseline Youden threshold $\tau^*$ (as opposed to $\tau_{\text{robust}}$). Table~\ref{tab:burst_aggregation} and Figure~\ref{fig:burst} summarize the empirical results:
```

```diff
@@ -235 +235 @@ Temporal burst fusion cuts legitimate meter false rejection by more than half (f
-Per-device vulnerability analysis reveals that rogue penetration varies from $0.0\%$ to $98.5\%$. The top vulnerable transmitters (IDs 46, 47, 48, 49, 50, 54 with $\text{FAR}_B > 42\% - 65\%$) cluster heavily in hardware block 4 (IDs 46--60).
+Per-device vulnerability analysis reveals that device-mean $\text{FAR}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episode device penetration reaches up to $100\%$. The top vulnerable transmitters (IDs 46, 47, 48, 49, 50, 54 with $\text{FAR}_B > 42\% - 65\%$) cluster heavily in hardware block 4 (IDs 46--60).
```

```diff
@@ -239,2 +239,2 @@ Evaluating an identity-robust threshold ($\tau_{\text{robust}}$) enforcing 90th-
-    \item Drops true stranger penetration from $11.55\%$ to $4.17\%$.
-    \item But forces False Rejection Rate ($\text{FRR}$) to surge from $8.49\%$ to $30.18\%$ on average (peaking at $84.63\%$).
+    \item Reduces episode-mean true stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction).
+    \item But forces False Rejection Rate ($\text{FRR}$) to surge from $8.49\%$ to $30.08\%$ on average (+21.59 pp, peaking at $84.63\%$).
```

```diff
@@ -248 +248 @@ In AMR gateway deployments, RFFI provides an effective physical-layer screening
-    \item Robust thresholding introduces an unacceptable $30.18\%$ availability penalty in battery-powered AMR networks.
+    \item Robust thresholding introduces an unacceptable $30.08\%$ availability penalty in battery-powered AMR networks.
```

```diff
@@ -254 +254 @@ Our findings outline key directions for wireless physical-layer security:
-    \item \textbf{Multi-Receiver Spatial Fusion:} Combining physical observations across multiple gateway towers overhearing the same transmission to reduce the $30.18\%$ FRR penalty.
+    \item \textbf{Multi-Receiver Spatial Fusion:} Combining physical observations across multiple gateway towers overhearing the same transmission to reduce the $30.08\%$ FRR penalty.
```

```diff
@@ -260 +260 @@ Our findings outline key directions for wireless physical-layer security:
-This paper identified and evaluated \textit{The Familiar Stranger Problem} in open-set LoRa RF fingerprinting for AMR gateways. Using 292 complex baseband features, frozen thresholds, and 20 stratified episodes, we demonstrated that naive packet-disjoint evaluation distorts stranger penetration. Through a device-matched paired design, we confirmed a statistically significant familiarity gap ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2.40\%]$), scaling to $+19.41\%$ for single-proxy calibration. Furthermore, we quantified the operational availability cost of robust thresholds ($30.18\%$ FRR). These results establish the necessity of identity-disjoint evaluation protocols in smart grid physical-layer security.
+This paper identified and evaluated \textit{The Familiar Stranger Problem} in open-set LoRa RF fingerprinting for AMR gateways. Using 292 complex baseband features, frozen thresholds, and 20 stratified episodes, we demonstrated that naive packet-disjoint evaluation distorts stranger penetration. Through a device-matched paired design, we confirmed a statistically significant familiarity gap ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2.40\%]$), scaling to $+19.41\%$ for single-proxy calibration. Furthermore, we quantified the operational availability cost of robust thresholds ($30.08\%$ FRR). These results establish the necessity of identity-disjoint evaluation protocols in smart grid physical-layer security.
```

## `paper/sections/paper_draft.md`

```diff
@@ -21,2 +21,2 @@ We identify a fundamental methodological flaw in this evaluation paradigm: **The
-5. **Transmitter Vulnerability Heterogeneity:** Per-device rankings show that rogue penetration varies from $0.0\%$ to $98.5\%$, with the top vulnerable transmitters clustering heavily within unaugmented hardware block 4 (IDs 46–60).
-6. **Robust Threshold ($\tau_{\text{robust}}$) Trade-off:** We evaluate an identity-robust threshold enforcing 90th-percentile proxy rejection, showing that it lowers true-stranger penetration from $11.55\%$ to $4.17\%$ but imposes a steep operational availability penalty (FRR surges from $8.49\%$ to $30.18\%$).
+5. **Transmitter Vulnerability Heterogeneity:** Device-mean $\text{FAR}_B$ ranges from $0.0\%$ to $65.7\%$ (device 48); single-episode device penetration reaches up to $100\%$, with the top vulnerable transmitters clustering heavily within unaugmented hardware block 4 (IDs 46–60).
+6. **Robust Threshold ($\tau_{\text{robust}}$) Trade-off:** We evaluate an identity-robust threshold enforcing 90th-percentile proxy rejection, showing that it reduces episode-mean true-stranger penetration from $11.90\%$ to $4.43\%$ (a $62.8\%$ reduction) but imposes a steep operational availability penalty (FRR surges from $8.49\%$ to $30.08\%$, a $+21.59$ pp increase).
```

```diff
@@ -48,3 +48,3 @@ The vulnerability of outlier-exposure methods to "known-unknown" overfitting is
-| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.17%** (drops intrusion by 64%) |
-| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.18%** (surge of +21.69%, peak 84.63%) |
-| **Multi-Packet Burst Fusion (L=5)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
+| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.43%** (reduces episode-mean stranger penetration by 62.8%) |
+| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.08%** (surge of +21.59 pp, peak 84.63%) |
+| **Multi-Packet Burst Fusion (L=5, $\tau^*$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
```

```diff
@@ -62 +62 @@ Our research establishes six distinct dimensions of novelty over the existing li
-6. **Operational AMR Availability Cost:** We provide the first quantification of the real-world operational penalty imposed by robust open-set calibration ($\tau_{\text{robust}}$), revealing a severe $30.18\%$ false rejection rate that governs deployment trade-offs in smart utility grids.
+6. **Operational AMR Availability Cost:** We provide the first quantification of the real-world operational penalty imposed by robust open-set calibration ($\tau_{\text{robust}}$), revealing a severe $30.08\%$ false rejection rate that governs deployment trade-offs in smart utility grids.
```

```diff
@@ -144,2 +144,2 @@ Evaluating an identity-robust threshold enforcing 90th-percentile proxy rejectio
-- Raising the threshold from $\tau_{\text{youden}} = 0.704$ to $\tau_{\text{robust}} = 0.854$ slashes true-stranger penetration from $11.55\%$ down to $4.17\%$ (with 4 episodes achieving $0.0\%$ penetration).
-- However, this protection incurs a steep operational cost: False Rejection Rate surges from $8.49\%$ to **$30.18\%$** on average (peaking at $84.63\%$). Deploying $\tau_{\text{robust}}$ in battery-powered AMR networks would cause unacceptable packet retransmissions.
+- Raising the threshold from $\tau_{\text{youden}} = 0.704$ to $\tau_{\text{robust}} = 0.854$ reduces episode-mean true-stranger penetration from $11.90\%$ down to $4.43\%$ (a $62.8\%$ reduction, with 4 episodes achieving $0.0\%$ penetration).
+- However, this protection incurs a steep operational cost: False Rejection Rate surges from $8.49\%$ to **$30.08\%$** on average (+21.59 pp, peaking at $84.63\%$). Deploying $\tau_{\text{robust}}$ in battery-powered AMR networks would cause unacceptable packet retransmissions.
```

```diff
@@ -150,2 +150,2 @@ LOPO cross-validation across the 15 proxy devices produces an average bias of $+
-### 5.7 Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$)
-In real-world AMR networks, smart utility meters transmit periodic meter telemetry or short packet retransmission bursts. To evaluate whether temporal burst aggregation overcomes the single-packet baseline limitations, we evaluate multi-packet decision fusion by averaging decision confidence over $L$ consecutive packet transmissions per physical device across all 20 evaluation episodes:
+### 5.7 Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$ at $\tau^*$)
+In real-world AMR networks, smart utility meters transmit periodic meter telemetry or short packet retransmission bursts. To evaluate whether temporal burst aggregation overcomes the single-packet baseline limitations, we evaluate multi-packet decision fusion by averaging decision confidence over $L$ consecutive packet transmissions per physical device across all 20 evaluation episodes, operating at the baseline Youden threshold $\tau^*$ (as opposed to $\tau_{\text{robust}}$):
```

```diff
@@ -180 +180 @@ Our empirical findings both re-evaluate prior research and establish concrete pa
-2. **Multi-Receiver Diversity & Spatial Fusion:** In AMR networks where transmissions are overheard by multiple gateway towers, future research should explore distributed spatial fusion—combining physical-layer observations across 3–4 synchronized receivers to suppress the $30.18\%$ availability penalty of robust thresholding.
+2. **Multi-Receiver Diversity & Spatial Fusion:** In AMR networks where transmissions are overheard by multiple gateway towers, future research should explore distributed spatial fusion—combining physical-layer observations across 3–4 synchronized receivers to suppress the $30.08\%$ availability penalty of robust thresholding.
```

```diff
@@ -188 +188 @@ Our empirical findings both re-evaluate prior research and establish concrete pa
-This paper conducted a rigorous empirical evaluation of **The Familiar Stranger Problem** in open-set LoRa RF fingerprint authentication for AMR gateways. Using 292 complex baseband features, frozen thresholds, and 20 stratified episodes, we demonstrated that naive packet-disjoint evaluation distorts stranger penetration rates. Through a device-matched paired design, we confirmed a statistically significant familiarity gap ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2.40\%]$), scaling to $+19.41\%$ when only a single proxy device is available. Furthermore, we quantified the steep operational availability cost of robust thresholds ($30.18\%$ FRR). These results demonstrate the necessity of identity-disjoint validation protocols in smart grid physical-layer security.
+This paper conducted a rigorous empirical evaluation of **The Familiar Stranger Problem** in open-set LoRa RF fingerprint authentication for AMR gateways. Using 292 complex baseband features, frozen thresholds, and 20 stratified episodes, we demonstrated that naive packet-disjoint evaluation distorts stranger penetration rates. Through a device-matched paired design, we confirmed a statistically significant familiarity gap ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2.40\%]$), scaling to $+19.41\%$ when only a single proxy device is available. Furthermore, we quantified the steep operational availability cost of robust thresholds ($30.08\%$ FRR). These results demonstrate the necessity of identity-disjoint validation protocols in smart grid physical-layer security.
```

## `paper/related_work_table.md`

```diff
@@ -35,3 +35,3 @@
-| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.17%** (drops intrusion by 64%) |
-| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.18%** (surge of +21.69%, peak 84.63%) |
-| **Multi-Packet Burst Fusion (L=5)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
+| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.43%** (reduces episode-mean stranger penetration by 62.8%) |
+| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.08%** (surge of +21.59 pp, peak 84.63%) |
+| **Multi-Packet Burst Fusion (L=5, $\tau^*$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
```

## `paper/literature_comparison.csv`

```diff
@@ -13,3 +13,3 @@ Legitimate FRR at Baseline,Not controlled,DET curve trade-off,~6.15%,~5.5%,~7.2%
-Robust Remedy Penetration (FAR_robust),Not provided,Not provided,Not provided,Not provided,Not provided,4.17% (drops intrusion by 64%)
-Robust Availability Cost (FRR_robust),Not quantified,Not quantified,Not quantified,Not quantified,Not quantified,30.18% (surge of +21.69%, peak 84.63%)
-Multi-Packet Burst Fusion (L=5),Not evaluated,Not evaluated,Not evaluated,Not evaluated,Not evaluated,FRR -> 3.54%, AUROC -> 0.9670
+Robust Remedy Penetration (FAR_robust),Not provided,Not provided,Not provided,Not provided,Not provided,4.43% (reduces episode-mean stranger penetration by 62.8%)
+Robust Availability Cost (FRR_robust),Not quantified,Not quantified,Not quantified,Not quantified,Not quantified,30.08% (surge of +21.59 pp, peak 84.63%)
+Multi-Packet Burst Fusion (L=5, tau_youden),Not evaluated,Not evaluated,Not evaluated,Not evaluated,Not evaluated,FRR -> 3.54%, AUROC -> 0.9670
```

## `reports/experiment_log.md`

```diff
@@ -103,2 +103,2 @@
-- Raising threshold from $\tau_{\text{youden}} = 0.704 \to \tau_{\text{robust}} = 0.854$ drops true stranger penetration from $11.55\% \to 4.17\%$.
-- However, False Rejection Rate surges from $8.49\% \to 30.18\%$ on average (peaking at $84.63\%$).
+- Raising threshold from $\tau_{\text{youden}} = 0.704 \to \tau_{\text{robust}} = 0.854$ reduces episode-mean true stranger penetration from $11.90\% \to 4.43\%$ (a $62.8\%$ reduction).
+- However, False Rejection Rate surges from $8.49\% \to 30.08\%$ on average (+21.59 pp, peaking at $84.63\%$).
```

```diff
@@ -111 +111 @@
-### 5.7 Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$)
+### 5.7 Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$ at $\tau^*$)
```

```diff
@@ -132,3 +132,3 @@
-| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.17%** (drops intrusion by 64%) |
-| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.18%** (surge of +21.69%, peak 84.63%) |
-| **Multi-Packet Burst Fusion (L=5)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
+| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.43%** (reduces episode-mean stranger penetration by 62.8%) |
+| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.08%** (surge of +21.59 pp, peak 84.63%) |
+| **Multi-Packet Burst Fusion (L=5, $\tau^*$)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
```
