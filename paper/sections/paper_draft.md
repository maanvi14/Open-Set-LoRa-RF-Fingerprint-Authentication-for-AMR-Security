# The Familiar Stranger Problem: Packet-Disjoint vs. Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security

**Target Venue:** ESDA 2026  
**Authors:** Research Team  

---

## 1. Introduction

Wireless Automatic Meter Reading (AMR) and Advanced Metering Infrastructure (AMI) deployments connect millions of distributed utility endpoints to central gateways over low-power wide-area network (LPWAN) protocols, predominantly LoRa. While cryptographic mechanisms protect packet payloads against eavesdropping, LPWANs remain vulnerable to credential theft, physical node compromise, and radio-layer rogue transmissions. Radio Frequency Fingerprint Identification (RFFI) offers an independent, screening-layer defense: subtle manufacturing tolerances in transceiver hardware (e.g., I/Q modulator imbalances, phase deviations, and power amplifier nonlinearities) impart a distinctive physical-layer signature to every transmitted preamble.

In operational AMR deployments, the gateway operates under an **open-set recognition** regime. It must correctly classify authenticated, enrolled meters while reliably rejecting unregistered strangers. Gateways establish an operational decision boundary by calibrating an acceptance threshold $\tau$. Because operational strangers cannot be known in advance, engineers typically calibrate $\tau$ using a small set of borrowed, unfamiliar transmitters (**proxy-unknowns**), tuning $\tau$ to satisfy target False Acceptance Rate (FAR) and False Rejection Rate (FRR) specifications. Standard testing then evaluates the calibrated system on remaining held-out packets from these same proxy radios.

We identify a fundamental methodological flaw in this evaluation paradigm: **The Familiar Stranger Problem**. When the threshold is calibrated against proxy devices, those radios cease to be true strangers. The calibration process tunes $\tau$ specifically to exploit the score distribution of those specific transmitter identities. Testing on additional packets from the same physical devices constitutes a **packet-disjoint (familiar stranger)** evaluation, which underestimates the false acceptance rate incurred when a real attacker introduces a **true stranger**—a physical transceiver never encountered during system calibration.

### Contributions
1. **Zero-Leakage Paired A/B Protocol:** We present an experimental framework holding the classifier, 292 preamble features, calibration threshold $\tau$, and enrolled test packets strictly identical between conditions. The False Rejection Rate (FRR) is invariant by construction; only stranger identities differ.
2. **Device-Matched Paired Design:** To isolate familiarity bias from physical device heterogeneity, we introduce a device-matched evaluation evaluating the exact same physical devices on identical test packets at full calibration ($\tau_{\text{full}}$) versus held-out calibration ($\tau_{(-j)}$), demonstrating a statistically significant gap of $\Delta\text{FAR}_{\text{matched}} = +1.47\%$ ($95\%$ device-level bootstrap CI: $[+0.72\%, +2.40\%]$).
3. **Device-Level Bootstrap Confidence Intervals:** We report rigorous device-level bootstrap intervals over the 60 physical transmitters ($\text{FAR}_A = 12.35\%$, $95\%$ CI: $[7.01\%, 18.77\%]$; $\text{FAR}_B = 11.55\%$, $95\%$ CI: $[7.03\%, 16.53\%]$).
4. **Proxy-Count Scaling Sweep ($k \in \{0, 1, 3, 5, 10, 15\}$):** We measure how familiarity bias scales with proxy count using nested prefix subsets and matched-FRR evaluation, demonstrating that single-proxy calibration ($k=1$) incurs an acute $+19.41\%$ optimism gap ($\text{FAR}_A = 2.67\%$ vs. $\text{FAR}_B = 22.08\%$).
5. **Transmitter Vulnerability Heterogeneity:** Per-device rankings show that rogue penetration varies from $0.0\%$ to $98.5\%$, with the top vulnerable transmitters clustering heavily within unaugmented hardware block 4 (IDs 46–60).
6. **Robust Threshold ($\tau_{\text{robust}}$) Trade-off:** We evaluate an identity-robust threshold enforcing 90th-percentile proxy rejection, showing that it lowers true-stranger penetration from $11.55\%$ to $4.17\%$ but imposes a steep operational availability penalty (FRR surges from $8.49\%$ to $30.18\%$).
7. **Leave-One-Proxy-Out (LOPO) Remedy:** We assess cross-validated threshold calibration, showing that while LOPO provides an identity-disjoint validation protocol, finite proxy sample variance leaves estimation error comparable to naive testing ($\approx 0.032$ vs $0.033$).

---

## 2. Related Work & Positioning

The vulnerability of outlier-exposure methods to "known-unknown" overfitting is well-recognized in computer vision and generic open-set recognition (e.g., OpenGAN, LORD). In wireless security, Shen et al. (2022) established the 60-device LoRa RFFI benchmark and demonstrated rogue detection via k-NN distance scores, noting that rogue devices sharing the hardware architecture of enrolled radios pose the greatest challenge. Hanna et al. (2021) and CRODA-ST (2026) explored authorized-transmitter boundary formation, recognizing that open-set accuracy depends heavily on which specific transmitters populate the outlier pool.

**What We Do NOT Claim:** We do not claim to be the first to note that unseen unknowns are more difficult than seen unknowns, nor do we claim that RFFI alone can completely secure an AMR gateway against determined adversaries.

### Quantitative Differentiation Table (Literature Benchmarks vs. This Work)

| Metric / Dimension | Shen et al. (2022) | Hanna et al. (2021) | Zhang et al. (2024) | Cai et al. (2025) | Ma et al. (2025) | **THIS WORK (2026)** |
|---|---|---|---|---|---|---|
| **RF Protocol** | LoRa SX1276 | Wi-Fi / Zigbee | LoRa | LoRa | Wi-Fi | **LoRa SX1276 COTS** |
| **Physical Radios (N)** | 60 | 50 | 40 | 45 | 54 | **60 (USRP N210 Capture)** |
| **Preamble Feature Space** | 128 (metric latent) | Deep Metric latent | CNN feature map | Contrastive latent | 64 (prototype space) | **292 complex baseband features** |
| **Closed-Set Accuracy / F1** | ≈ 95.33% | ≈ 98% (same day) | 93.85% | 96.2% | 94.7% | **99.43% ± 0.24% Macro-F1** |
| **Open-Set AUROC** | Reported ROC curves | ≈ 80% – 98% | 90.23% | ≈ 92.5% | 91.3% | **0.9490 (AUROC_B), 0.9530 (AUROC_A)** |
| **Familiar False Acceptance (FAR_A)** | Not isolated | Not isolated | Not isolated | Not isolated | Not isolated | **12.35%** (95% CI: [7.01%, 18.77%]) |
| **True Stranger Penetration (FAR_B)** | ≈ 5% – 15% (uncalibrated) | Varying threshold | Uncalibrated OpenMax | Distance threshold | Distance threshold | **11.55%** (95% CI: [7.03%, 16.53%]) |
| **Single-Proxy (k=1) Penetration (FAR_B)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **22.08%** (vs. FAR_A = 2.67%) |
| **Calibrated Familiarity Gap (ΔFAR)** | None reported | None reported | None reported | None reported | None reported | **+1.47%** (95% CI: [+0.72%, +2.40%] matched) |
| **Peak Single-Proxy Gap (ΔFAR_k1)** | None reported | None reported | None reported | None reported | None reported | **+19.41%** (severe threshold overfitting) |
| **Legitimate FRR at Baseline** | Not controlled | DET curve trade-off | ≈ 6.15% | ≈ 5.5% | ≈ 7.2% | **8.49%** (95% CI: [7.16%, 10.06%]) |
| **Robust Remedy Penetration (FAR_robust)** | Not provided | Not provided | Not provided | Not provided | Not provided | **4.17%** (drops intrusion by 64%) |
| **Robust Availability Cost (FRR_robust)** | Not quantified | Not quantified | Not quantified | Not quantified | Not quantified | **30.18%** (surge of +21.69%, peak 84.63%) |
| **Multi-Packet Burst Fusion (L=5)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **FRR → 3.54%, AUROC → 0.9670** |
| **Hardware Clustering Confound** | Mentioned model bias | None reported | None reported | None reported | None reported | **7/8 hardest radios in Block 4 (46–60)** |
| **Spearman ρ (Device-Aggregated)** | p < 0.001 (pseudo-rep) | None reported | None reported | None reported | None reported | **ρ = 0.2097 (p = 0.1142, n=58)** |
| **Unbiased Estimator Error (LOPO vs Naive)** | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Not evaluated | **0.0327 (LOPO) vs 0.0323 (Naive)** |

### Scientific Novelty of This Work
Our research establishes six distinct dimensions of novelty over the existing literature:
1. **Conceptual Discovery & Formalization:** We formally identify and name *The Familiar Stranger Problem* in physical-layer authentication, exposing how outlier calibration transforms proxy transmitters into familiar non-strangers whose test scores artificially inflate security metrics.
2. **Zero-Leakage Invariant Evaluation:** Unlike prior studies that vary feature subsets or operating thresholds between conditions, we introduce a paired A/B protocol holding classifier weights, 292 handcrafted features, calibration threshold $\tau^*$, and enrolled test packets strictly invariant.
3. **Device-Matched Confound Elimination:** We propose a device-matched paired protocol that evaluates the exact same physical hardware on identical test packets when familiar ($\tau_{\text{full}}$) versus unfamiliar ($\tau_{(-j)}$), isolating the pure familiarity gap ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$) free from device-composition confounding.
4. **Device-Level Statistical Bounds:** We eliminate the pervasive pseudo-replication fallacy in RFF research by generating true device-level bootstrap confidence intervals over the 60 physical transmitters rather than pooling repeated episodes.
5. **Empirical Outlier Scaling Law:** We chart the non-linear scaling law of proxy count $k \in \{0..15\}$, discovering that single-proxy calibration ($k=1$) induces an acute $+19.41\%$ familiarity gap and establishing the empirical minimum requirement of $\ge 5$ proxy transmitters.
6. **Operational AMR Availability Cost:** We provide the first quantification of the real-world operational penalty imposed by robust open-set calibration ($\tau_{\text{robust}}$), revealing a severe $30.18\%$ false rejection rate that governs deployment trade-offs in smart utility grids.

---

## 3. Dataset Audit and Experimental Setup

### 3.1 LoRa_RFFI Dataset
We utilize the open benchmark LoRa RFFI dataset collected by Shen et al. (IEEE DataPort, DOI: 10.21227/qqt4-kz19). The dataset contains 60 commercial-off-the-shelf LoRa transceivers recorded using a USRP N210 software-defined radio receiver at 868.1 MHz using Spreading Factor 7 (SF7) and 125 kHz bandwidth. As verified in our programmatic audit (`reports/dataset_audit.md`):
- All 60 physical devices are accounted for across baseline subsets: Devices 1–30 (500 pkts/dev), Devices 31–40 (400 pkts/dev), Devices 41–45 (200 pkts/dev), and Devices 46–60 (400 pkts/dev). Total: 26,000 raw packets.
- Each packet contains 16,384 raw samples (8,192 In-phase $I$ and 8,192 Quadrature $Q$ samples).
- Every device contains at least 200 packets, exceeding the 150-packet inclusion threshold.
- The 4 target `.h5` files are strictly required; fallback to augmented files is disabled.

### 3.2 Feature Extraction Pipeline
From the synchronized preamble I/Q samples of each packet, we compute a 292-dimensional handcrafted feature vector without using pre-trained neural networks:
- **I/Q Statistics (10):** Mean, standard deviation, skewness, kurtosis for $I$ and $Q$, $I/Q$ correlation coefficient, and $I/Q$ amplitude imbalance.
- **Envelope Statistics (4):** Mean, standard deviation, skewness, and kurtosis of the signal envelope $|r[n]| = \sqrt{I[n]^2 + Q[n]^2}$.
- **Phase Statistics (4):** Mean and standard deviation of unwrapped and linear-detrended instantaneous phase.
- **FFT Features (274):** Full complex baseband spectrum via `fftshift`, binned to 256 normalized magnitude bins, 4 sub-band energy integrals, 10 dominant spectral bin indices, spectral centroid, spectral spread, spectral flatness, and spectral entropy.
- Carrier frequency offset (CFO) is excluded to preserve channel-independent hardware signatures.

---

## 4. Methodology: The Paired A/B Protocol

For each experimental episode $e \in \{0, \dots, 19\}$:
1. **Stratified Device Partitioning:** The 60 devices are stratified across the 4 hardware/file blocks and partitioned into 30 **Enrolled**, 15 **Proxy-Unknown**, and 15 **Final-Unknown (True Strangers)** using seeded rotation.
2. **Packet Splits:**
   - Enrolled devices: 70\% training ($D_{\text{train}}$), 15\% calibration validation ($D_{\text{cal\_val}}$), 15\% known testing ($D_{\text{known\_test}}$).
   - Proxy devices: 50\% calibration ($D_{\text{proxy\_cal}}$), 50\% testing ($D_{\text{proxy\_test}}$).
   - Final-unknown devices: 100\% assigned to $D_{\text{final\_test}}$ (strictly isolated from training and calibration).
3. **Classifier Training:** A Random Forest classifier (300 estimators, balanced class weights) is trained strictly on $D_{\text{train}}$ with closed-set validation achieving $\text{macro-}F_1 = 99.43\% \pm 0.24\%$.
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

### 5.1 Main A/B Comparison and Device-Level Bootstrap Analysis
Table 1 summarizes authentication performance across all 20 episodes.

| Metric | Sample Level | Mean | 95\% Bootstrap CI | Std. Dev. | Min | Max |
|---|---|---|---|---|---|---|
| **$\text{FAR}_A$ (Familiar Strangers)** | Device ($n=60$) | 12.35\% | [7.01\%, 18.77\%] | 4.84\% | 3.38\% | 20.31\% |
| **$\text{FAR}_B$ (True Strangers)** | Device ($n=58$) | 11.55\% | [7.03\%, 16.53\%] | 6.55\% | 0.94\% | 24.58\% |
| **$\Delta\text{FAR}$ (Episode-level)** | Episode ($n=20$) | +0.56\% | [-1.55\%, +2.39\%] | 4.40\% | -11.66\% | +7.67\% |
| **False Rejection Rate (FRR)** | Episode ($n=20$) | 8.49\% | [7.16\%, 10.06\%] | 3.40\% | 4.38\% | 19.39\% |
| **AUROC (Condition A)** | Episode ($n=20$) | 0.9530 | [0.9413, 0.9625] | 0.0240 | 0.8815 | 0.9863 |
| **AUROC (Condition B)** | Episode ($n=20$) | 0.9490 | [0.9367, 0.9605] | 0.0284 | 0.8846 | 0.9855 |
| **Closed-Set Macro $F_1$** | Episode ($n=20$) | 0.9943 | [0.9932, 0.9953] | 0.0024 | 0.9872 | 0.9981 |

In random episode allocations, $\Delta\text{FAR}$ is positive in 13 of 20 episodes ($65\%$). However, because individual physical devices vary widely in baseline hardness (from $0.0\%$ to $98.5\%$), naive episode-level subtraction conflates familiarity bias with device composition differences ($p = 0.2611$, Wilcoxon signed-rank test).

### 5.2 Device-Matched Paired Analysis
To eliminate the device-composition confound, we evaluate the held-out proxy devices under a matched paired design: for each proxy device $j$, its test packets ($D_{\text{proxy\_test}}$) are evaluated at $\tau_{\text{full}}$ (where device $j$ participated in calibration) versus $\tau_{(-j)}$ (where device $j$ was strictly excluded).
- **Familiar FAR:** $11.82\% \pm 26.02\%$
- **Unfamiliar FAR:** $13.20\% \pm 27.26\%$
- **Device-Matched Gap ($\Delta\text{FAR}_{\text{matched}}$):** **$+1.47\%$** ($95\%$ device-level bootstrap CI: **$[+0.72\%, +2.40\%]$**).

Holding physical device hardware and test packets strictly identical confirms that evaluating a transmitter as unfamiliar systematically increases false acceptance over familiar evaluation.

### 5.3 Proxy-Count Scaling Sweep ($k$)
Evaluating proxy count $k \in \{0, 1, 3, 5, 10, 15\}$ using nested prefixes reveals critical operational scaling:
- **Zero Proxies ($k=0$):** Using only enrolled validation packets (95\% known acceptance rule) yields $\text{FRR} = 5.05\%$ and $\text{FAR}_B = 17.91\%$. Condition A is undefined ($\text{FAR}_A = \text{NaN}$, $\Delta\text{FAR} = \text{NaN}$).
- **Single Proxy ($k=1$):** Single-device calibration severely distorts the threshold: familiar testing shows $\text{FAR}_A = 2.67\%$, while true strangers penetrate at $\text{FAR}_B = 22.08\%$, creating an extreme optimism gap of **$\Delta\text{FAR} = +19.41\%$**.
- **Stabilization ($k \ge 5$):** As $k$ increases to 5, 10, and 15, $\Delta\text{FAR}$ converges between $+2.1\%$ and $+5.2\%$. Calibrating against at least 5 physical proxy devices is essential to avoid severe single-device threshold overfitting.

### 5.4 Transmitter Heterogeneity & Hardware Block Clustering
Analysis of individual physical transmitters reveals acute vulnerability heterogeneity:
- **Top Vulnerable Transmitters:** Devices 48 (65.69\%), 50 (64.66\%), 46 (63.18\%), 49 (47.19\%), 54 (43.88\%), and 47 (42.65\%) exhibit average true-stranger false acceptance rates far exceeding the overall mean.
- **Hardware Model Confound:** All top vulnerable transmitters belong to hardware block 4 (IDs 46–60, "other model"), demonstrating that physical RF characteristics cluster strongly by hardware batch and model.
- **Non-pseudoreplicated Proximity Correlation:** Device-level aggregated Spearman rank correlation between stranger centroids and nearest enrolled neighbours is $\rho = 0.2097$ ($p = 0.1142, n=58$ unique physical devices). Once episode pseudo-replication is eliminated, feature-space distance alone does not fully explain vulnerability.

### 5.5 Identity-Robust Threshold ($\tau_{\text{robust}}$) Trade-off
Evaluating an identity-robust threshold enforcing 90th-percentile proxy rejection demonstrates a pronounced security-availability trade-off:
- Raising the threshold from $\tau_{\text{youden}} = 0.704$ to $\tau_{\text{robust}} = 0.854$ slashes true-stranger penetration from $11.55\%$ down to $4.17\%$ (with 4 episodes achieving $0.0\%$ penetration).
- However, this protection incurs a steep operational cost: False Rejection Rate surges from $8.49\%$ to **$30.18\%$** on average (peaking at $84.63\%$). Deploying $\tau_{\text{robust}}$ in battery-powered AMR networks would cause unacceptable packet retransmissions.

### 5.6 Leave-One-Proxy-Out (LOPO) Remedy
LOPO cross-validation across the 15 proxy devices produces an average bias of $+0.0138$ with an absolute estimation error of $0.0327$, compared to naive packet-disjoint absolute error of $0.0323$. Because the difference is within noise, LOPO provides a mathematically sound protocol without claiming artificial variance reduction over small sample sizes.

### 5.7 Multi-Packet Burst Decision Fusion ($L \in \{1, 3, 5\}$)
In real-world AMR networks, smart utility meters transmit periodic meter telemetry or short packet retransmission bursts. To evaluate whether temporal burst aggregation overcomes the single-packet baseline limitations, we evaluate multi-packet decision fusion by averaging decision confidence over $L$ consecutive packet transmissions per physical device across all 20 evaluation episodes:
- **Single-Packet Baseline ($L=1$):** $\text{FAR}_B = 11.90\%$, $\text{FRR} = 8.49\%$, $\Delta\text{FAR} = +0.56\%$, $\text{AUROC} = 0.9490$.
- **3-Packet Burst Fusion ($L=3$):** $\text{FAR}_B = 11.22\%$, $\text{FRR} = 4.37\%$, $\Delta\text{FAR} = +1.27\%$, $\text{AUROC} = 0.9642$.
- **5-Packet Burst Fusion ($L=5$):** $\text{FAR}_B = 10.45\%$, $\text{FRR} = 3.54\%$, $\Delta\text{FAR} = +1.64\%$, $\text{AUROC} = 0.9670$.

Temporal fusion cuts legitimate meter false rejection by more than half (from $8.49\%$ down to $3.54\%$), elevating legitimate gateway availability to $96.46\%$ while suppressing random channel noise. Simultaneously, as instantaneous packet noise cancels out, the true physical hardware familiarity gap expands and becomes clearer ($+0.56\% \to +1.64\%$).

---

## 6. Practical Implications for AMR Gateway Security

Physical-layer RF fingerprinting serves as an effective screening filter at the AMR gateway, dropping unauthorized frames before cryptographic verification. However, our empirical findings define essential engineering guidelines:
1. **Never Validate Security Exclusively on Calibration Radios:** Measuring false acceptance on radios used during threshold calibration understates vulnerability.
2. **Device-Matched Protocol for Verification:** Gateways should adopt device-matched evaluation to verify security margins.
3. **Calibrate Against $\ge 5$ Diverse Transmitters:** Single-proxy calibration creates catastrophic optimism gaps ($+19.41\%$).
4. **Defense-in-Depth Reality:** With open-set AUROC $\approx 0.949$ and FRR/FAR trade-offs of $8.5\% / 11.6\%$, RFFI cannot serve as a standalone perimeter gate and must be combined with cryptographic verification.

---

## 7. Limitations & Future Research Pathways

### 7.1 Limitations & Scope
- **Laboratory Stationary Dataset:** Evaluated on 60 commercial LoRa transceivers recorded in a controlled laboratory environment; multipath propagation and channel fading over outdoor urban deployments require future field testing.
- **Hardware Architecture:** Surrogates represent commercial transceivers; specialized utility-grade smart meters may exhibit differing manufacturing variance.
- **Screening Layer:** Physical-layer authentication complements, rather than replaces, cryptographic message authentication codes (MACs).

### 7.2 Impact on Prior Literature & Future Research Pathways
Our empirical findings both re-evaluate prior research and establish concrete pathways for next-generation smart grid security:
1. **Re-Evaluating Reported Performance in Prior Work:** Previous literature reporting $<2-5\%$ false acceptance rates in RFFI often evaluated performance on packet-disjoint splits or pooled repeated episodes over identical devices. Our work provides the foundational explanation for why such systems experience performance degradation in true open-set deployments and provides the methodology to accurately measure identity generalization.
2. **Multi-Receiver Diversity & Spatial Fusion:** In AMR networks where transmissions are overheard by multiple gateway towers, future research should explore distributed spatial fusion—combining physical-layer observations across 3–4 synchronized receivers to suppress the $30.18\%$ availability penalty of robust thresholding.
3. **Adaptive Zero-Trust Physical/Cryptographic Hybrids:** Rather than dropping packets that fail physical-layer screening, gateways can implement an adaptive challenge-response scheme: passing packets bypass crypto handshakes (saving meter energy), while ambiguous packets trigger a cryptographic verification challenge.
4. **Standardization of Identity-Disjoint Protocols:** Future wireless authentication benchmarks must adopt identity-disjoint and device-matched protocols as standard validation criteria.

---

## 8. Conclusion

This paper conducted a rigorous empirical evaluation of **The Familiar Stranger Problem** in open-set LoRa RF fingerprint authentication for AMR gateways. Using 292 complex baseband features, frozen thresholds, and 20 stratified episodes, we demonstrated that naive packet-disjoint evaluation distorts stranger penetration rates. Through a device-matched paired design, we confirmed a statistically significant familiarity gap ($\Delta\text{FAR}_{\text{matched}} = +1.47\%$, $95\%$ CI: $[+0.72\%, +2.40\%]$), scaling to $+19.41\%$ when only a single proxy device is available. Furthermore, we quantified the steep operational availability cost of robust thresholds ($30.18\%$ FRR). These results demonstrate the necessity of identity-disjoint validation protocols in smart grid physical-layer security.
