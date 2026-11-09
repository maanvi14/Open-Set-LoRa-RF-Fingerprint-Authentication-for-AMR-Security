# The Familiar Stranger Problem: Packet-Disjoint vs. Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security

**Target Venue:** ESDA 2026  
**Authors:** Research Team  

---

## 1. Introduction

Wireless Automatic Meter Reading (AMR) and Advanced Metering Infrastructure (AMI) deployments connect millions of distributed utility endpoints to central gateways over low-power wide-area network (LPWAN) protocols, primarily LoRa. While cryptographic mechanisms protect packet payloads against eavesdropping, LPWANs remain vulnerable to credential theft, physical node compromise, and radio-layer rogue transmissions. Radio Frequency Fingerprint Identification (RFFI) offers an independent, screening-layer defense: subtle manufacturing tolerances in transceiver hardware (e.g., I/Q modulator imbalances, phase deviations, and power amplifier nonlinearities) impart a distinctive physical-layer signature to every transmitted preamble.

In operational AMR deployments, the gateway operates under an **open-set recognition** regime. It must correctly classify authenticated, enrolled meters while reliably rejecting unregistered strangers. Gateways establish an operational decision boundary by calibrating a confidence threshold $\tau$. Because operational strangers cannot be known in advance, engineers typically calibrate $\tau$ using a small set of borrowed, unfamiliar transmitters (**proxy-unknowns**), tuning $\tau$ to satisfy target False Acceptance Rate (FAR) and False Rejection Rate (FRR) specifications. Standard testing then evaluates the calibrated system on remaining held-out packets from these same proxy radios.

We identify a fundamental methodological flaw in this evaluation paradigm: **The Familiar Stranger Problem**. When the threshold is calibrated against proxy devices, those radios cease to be true strangers. The calibration process tunes $\tau$ specifically to exploit the score distribution of those specific transmitter identities. Testing on additional packets from the same physical devices constitutes a **packet-disjoint (familiar stranger)** evaluation, which severely underestimates the false acceptance rate incurred when a real attacker introduces a **true stranger**—a physical transceiver never encountered during system calibration.

### Contributions
1. **Controlled Paired A/B Protocol:** We present an experimental framework holding the classifier, 288 preamble features, calibration threshold $\tau$, and enrolled test packets strictly identical between conditions. The False Rejection Rate (FRR) is invariant by construction; only stranger identities differ.
2. **Quantification of the Familiarity Gap ($\Delta\text{FAR}$):** Across 20 seeded episodes on the 60-device benchmark LoRa dataset, we prove that true strangers incur significantly higher penetration rates than familiar strangers ($\Delta\text{FAR} = +4.22\%$, $p = 0.0215$), with gaps exceeding $+17\%$ in specific transmitter splits.
3. **Proxy-Count Sweep ($k \in \{0, 1, 3, 5, 10, 15\}$):** We measure how the familiarity gap evolves with the number of available proxy devices, showing that zero-proxy calibration yields a catastrophic 63.00\% true stranger penetration, while single-proxy calibration incurs an acute $+18.89\%$ estimation bias.
4. **Hardness Explanation:** Device-level ranking and nearest-enrolled-neighbour distance correlation ($\rho = -0.2516$, $p < 0.0001$) demonstrate that transmitter vulnerability is strongly heterogeneous.
5. **Leave-One-Proxy-Out (LOPO) Remedy:** We demonstrate that holding out transmitter identities during proxy calibration reduces empirical true-stranger estimation bias from $-0.0422$ to $-0.0281$.

---

## 2. Related Work & Positioning

The vulnerability of outlier-exposure methods to "known-unknown" overfitting is well-recognized in computer vision and generic open-set recognition (e.g., OpenGAN, LORD). In wireless security, Shen et al. (2022) established the 60-device LoRa RFFI benchmark and demonstrated rogue detection via k-NN distance scores, noting that rogue devices sharing the hardware architecture of enrolled radios pose the greatest challenge. Hanna et al. (2021) and CRODA-ST (2026) explored authorized-transmitter boundary formation, recognizing that open-set accuracy depends heavily on which specific transmitters populate the outlier pool.

**What We Do NOT Claim:** We do not claim to be the first to note that unseen unknowns are more difficult than seen unknowns, nor do we propose a new radio modulation or deep neural network architecture.

**What We DO Claim:** We provide the first systematic paired A/B measurement isolating the **identity familiarity bias** on a calibrated, frozen authentication threshold in LoRa RFFI, accompanied by device-level bootstrap confidence intervals, proxy-count scaling sweeps, and a validated Leave-One-Proxy-Out calibration remedy.

---

## 3. Dataset Audit and Experimental Setup

### 3.1 LoRa_RFFI Dataset
We utilize the open benchmark LoRa RFFI dataset collected by Shen et al. (IEEE DataPort, DOI: 10.21227/qqt4-kz19). The dataset contains 60 commercial-off-the-shelf LoRa transceivers recorded using a USRP N210 software-defined radio receiver at 868.1 MHz using Spreading Factor 7 (SF7) and 125 kHz bandwidth. As verified in our Phase 2 audit (`reports/dataset_audit.md`):
- All 60 physical devices are accounted for across baseline subsets: Devices 1–30 (500 pkts/dev), Devices 31–40 (400 pkts/dev), Devices 41–45 (200 pkts/dev), and Devices 46–60 (400 pkts/dev).
- Each packet contains 16,384 raw samples (8,192 In-phase $I$ and 8,192 Quadrature $Q$ samples).
- Every device contains at least 200 packets, exceeding the 150-packet inclusion threshold.

### 3.2 Feature Extraction Pipeline
From the synchronized preamble I/Q samples of each packet, we compute a 288-dimensional handcrafted feature vector without using pre-trained neural networks:
- **I/Q Statistics (10):** Mean, standard deviation, skewness, kurtosis for $I$ and $Q$, $I/Q$ correlation coefficient, and $I/Q$ amplitude imbalance.
- **Phase Statistics (4):** Mean and standard deviation of unwrapped and linear-detrended instantaneous phase.
- **FFT Features (274):** 256 normalized FFT magnitude spectrum bins, 4 sub-band energy integrals, 10 dominant spectral bin indices, spectral centroid, spectral spread, spectral flatness, and spectral entropy.
- In accordance with our guidelines, carrier frequency offset (CFO) is strictly excluded.

---

## 4. Methodology: The Paired A/B Protocol

For each experimental episode $e \in \{0, \dots, 19\}$:
1. **Device Partitioning:** The 60 devices are partitioned into 30 **Enrolled**, 15 **Proxy-Unknown**, and 15 **Final-Unknown (True Strangers)** using seeded random rotation.
2. **Packet Splits:**
   - Enrolled devices: 70\% training ($D_{\text{train}}$), 15\% calibration validation ($D_{\text{cal\_val}}$), 15\% known testing ($D_{\text{known\_test}}$).
   - Proxy devices: 50\% calibration ($D_{\text{proxy\_cal}}$), 50\% testing ($D_{\text{proxy\_test}}$).
   - Final-unknown devices: 100\% assigned to $D_{\text{final\_test}}$ (strictly isolated from training and calibration).
3. **Classifier Training:** A Random Forest classifier (300 estimators, balanced class weights) is trained strictly on $D_{\text{train}}$ with closed-set calibration validation achieving $\text{macro-}F_1 = 95.71\% \pm 0.68\%$.
4. **Frozen Threshold Calibration:** The operational acceptance score is defined as maximum posterior class probability:
   $$s(x) = \max_{c \in \text{Enrolled}} P(y=c \mid x)$$
   The threshold $\tau^*$ is calibrated by maximizing Youden's $J$-statistic ($J = \text{TPR} + \text{TNR} - 1$) on positive validation packets ($D_{\text{cal\_val}}$) against negative proxy calibration packets ($D_{\text{proxy\_cal}}$). Once computed, $\tau^*$ is permanently **frozen**.
5. **Evaluation Tracks:**
   - **Condition A (Packet-Disjoint / Familiar Strangers):** $\text{FAR}_A = P(s(x) \ge \tau^* \mid x \in D_{\text{proxy\_test}})$
   - **Condition B (Identity-Disjoint / True Strangers):** $\text{FAR}_B = P(s(x) \ge \tau^* \mid x \in D_{\text{final\_test}})$
   - **Known False Rejection:** $\text{FRR} = P(s(x) < \tau^* \mid x \in D_{\text{known\_test}})$ (strictly identical between conditions).
   - **Familiarity Gap:** $\Delta\text{FAR} = \text{FAR}_B - \text{FAR}_A$.

---

## 5. Experimental Results

### 5.1 Main A/B Comparison and Familiarity Gap
Table 1 summarizes authentication performance across all 20 episodes.

| Metric | Mean | 95\% Bootstrap CI | Std. Dev. | Min | Max |
|---|---|---|---|---|---|
| **$\text{FAR}_A$ (Familiar Strangers)** | 17.05\% | [14.07\%, 21.24\%] | 8.31\% | 8.80\% | 46.21\% |
| **$\text{FAR}_B$ (True Strangers)** | **21.28\%** | **[17.79\%, 24.94\%]** | 8.01\% | 8.10\% | 39.84\% |
| **Familiarity Gap ($\Delta\text{FAR}$)** | **+4.22\%** | **[+0.16\%, +7.75\%]** | 8.75\% | -22.36\% | **+17.00\%** |
| **False Rejection Rate (FRR)** | 25.88\% | [23.28\%, 28.85\%] | 6.27\% | 17.13\% | 37.99\% |
| **AUROC (Condition A)** | 0.8532 | [0.8326, 0.8711] | 0.0436 | 0.7402 | 0.9162 |
| **AUROC (Condition B)** | 0.8391 | [0.8223, 0.8547] | 0.0372 | 0.7369 | 0.8940 |

The Familiarity Gap $\Delta\text{FAR}$ is positive in **70.0\% of episodes** (14 out of 20), confirming that testing on familiar strangers yields an overly optimistic security assessment. A Wilcoxon signed-rank test confirms that $\text{FAR}_B$ is significantly higher than $\text{FAR}_A$ ($W = 44.0, p = 0.0215$).

### 5.2 Proxy-Count Sweep Analysis ($k$)
We systematically evaluated the effect of varying the number of proxy devices $k \in \{0, 1, 3, 5, 10, 15\}$ available during calibration:
- **Zero Proxies ($k=0$):** Using only enrolled validation packets (threshold at 95\% known acceptance) results in $\text{FRR} = 5.29\%$, but permits an alarming **$\text{FAR}_B = 63.00\%$** on true strangers.
- **Single Proxy ($k=1$):** Tuning on a single borrowed radio causes severe threshold overfitting: familiar test strangers show $\text{FAR}_A = 7.76\%$, while true strangers penetrate at $\text{FAR}_B = 26.64\%$, creating a massive **$\Delta\text{FAR} = +18.89\%$**.
- **Generalization Regime ($k \ge 5$):** As $k$ reaches 5, 10, and 15 devices, $\Delta\text{FAR}$ stabilizes between $+4.2\%$ and $+5.7\%$. Thus, utilities must calibrate against at least 5 to 10 distinct physical transmitters to avoid extreme device-specific threshold distortion.

### 5.3 Transmitter Hardness & Feature Proximity
Per-device ranking across evaluation episodes reveals substantial transmitter heterogeneity. Devices 47, 52, 48, and 50 exhibited average true-stranger false acceptance rates between **64.5\% and 83.2\%**, consistently penetrating the gateway.

Feature-space analysis between stranger centroids and their nearest enrolled neighbour reveals a negative Spearman rank correlation ($\rho = -0.2516, p < 0.0001$). Strangers physically closer to enrolled clusters in feature space systematically achieve higher acceptance rates, confirming that manufacturing proximity governs vulnerability.

### 5.4 Leave-One-Proxy-Out (LOPO) Calibration Remedy
To provide utilities with an honest estimate of stranger false acceptance without requiring additional test radios, we evaluated **Leave-One-Proxy-Out (LOPO)** cross-validation over the available proxy devices during calibration:
- **Naive Packet-Disjoint Estimate:** Average bias relative to true-stranger penetration is **$-0.0422$** (underestimating true stranger risk by 4.22 percentage points).
- **LOPO Estimate:** Yields an average bias of **$-0.0281$**, reducing estimation bias by **33.4\%**.
- **Identity-Robust Threshold ($\tau_{\text{robust}}$):** Setting $\tau$ to enforce a 90th-percentile held-out stranger FAR $\le 0.05$ raises the mean threshold from $\tau^* = 0.60$ to $\tau_{\text{robust}} = 0.81$, substantially lowering stranger penetration at an expected increase in legitimate packet retransmissions.

---

## 6. Practical Implications for AMR Gateway Security

Physical-layer RF fingerprinting serves as an effective, zero-overhead screening filter at the AMR gateway, discarding spoofed frames before they consume cryptographic verification resources. However, our findings highlight critical deployment directives:
1. **Never Validate Security on Familiar Radios:** Quoting false acceptance rates derived from the same transmitter pool used to tune gateway sensitivity misrepresents deployment security by up to 17 percentage points.
2. **Procure at Least 5–10 Calibration Transmitters:** Single-device outlier exposure produces extreme vulnerability to unseen hardware.
3. **Adopt LOPO for SLA Specification:** Gateway service level agreements should report LOPO-calibrated bounds rather than standard train/test splits.

---

## 7. Limitations & Scope

- **Dataset Constraints:** Evaluated on 60 commercial LoRa transceivers recorded in a stationary laboratory environment; multi-receiver diversity and dynamic channel fading require future outdoor investigation.
- **Transmitter Equivalence:** Commercial LoRa transceivers serve as empirical surrogates for utility smart meters.
- **Screening Layer Role:** RFFI constitutes a defense-in-depth screening mechanism and is not a replacement for standard end-to-end cryptographic authentication.

---

## 8. Conclusion

This study identified and empirically measured **The Familiar Stranger Problem** in open-set LoRa RF fingerprinting for AMR gateways. Across 20 experimental episodes, we proved that evaluating threshold performance on familiar strangers underestimates true-stranger penetration by an average of $+4.22\%$ ($p = 0.0215$), with single-proxy calibration underestimating risk by $+18.89\%$. By incorporating Leave-One-Proxy-Out (LOPO) calibration, utilities can mitigate this bias and establish rigorous physical-layer access controls for smart utility infrastructure.

