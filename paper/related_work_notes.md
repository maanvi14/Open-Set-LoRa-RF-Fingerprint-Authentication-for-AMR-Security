# Detailed Evidence & Source Notes for Related Work Comparison Table

Every entry in `paper/related_work_table.csv` is documented here with verification links and paper excerpts.

---

### 1. Shen et al. (2022) — LoRa_RFFI Dataset Paper
- **Title:** *Towards Scalable and Channel-Robust Radio Frequency Fingerprint Identification for LoRa*
- **Venue:** IEEE Transactions on Information Forensics and Security (TIFS), vol. 17, 2022.
- **URL/DOI:** [10.1109/TIFS.2022.3168270](https://doi.org/10.1109/TIFS.2022.3168270) / [arXiv:2107.02867](https://arxiv.org/abs/2107.02867)
- **Signal / Devices:** 60 commercial LoRa transmitters, SX1276 transceivers, USRP N210 receiver at 868.1 MHz, SF7.
- **Open-Set / Rogue Detection:** Evaluates rogue transmitter detection using a k-NN distance metric with a pre-set threshold on extracted deep features.
- **Familiar vs True Stranger Comparison:** *No evidence found in cited paper*. Rogue transmitters (devices 41–45) are evaluated separately from seen devices, but no paired study comparing packet-disjoint proxy devices against identity-disjoint test devices at an identical frozen calibrated threshold is performed.

---

### 2. Hanna et al. (2021)
- **Title:** *Open-Set Wireless Transmitter Authorization via Deep Metric Learning*
- **Venue:** IEEE Transactions on Cognitive Communications and Networking, 2021.
- **URL:** [10.1109/TCCN.2021.3090680](https://doi.org/10.1109/TCCN.2021.3090680)
- **Open-Set Approach:** Uses known unauthorized transmitters during training to assist metric learning boundary formation, and tests on a separate held-out set of unauthorized transmitters.
- **Familiar vs True Stranger Comparison:** *No evidence found in cited paper*. While they separate known outliers from unseen outliers, they do not quantify a frozen-threshold calibration familiarity gap ($\Delta\text{FAR}$) or evaluate proxy-count sensitivity.

---

### 3. Awan et al. (2023)
- **Title:** *Radio Frequency Fingerprinting for Advanced Metering Infrastructure in Smart Grids*
- **Venue:** Electronics, 12(24), 4914, 2023.
- **URL:** [10.3390/electronics12244914](https://doi.org/10.3390/electronics12244914)
- **Framing:** Specifically focuses on smart meters and AMI gateway security, motivating physical-layer authentication to prevent device impersonation.
- **Method:** Evaluates standard closed-set classifiers and simple probability thresholding without identity-disjoint stranger evaluation.

---

### 4. Cai et al. — JRFFP-SC (2025)
- **Title:** *Joint Radio Frequency Fingerprint and Preamble Synchronization for LoRa*
- **Venue:** arXiv:2501.15391, 2025.
- **Setup:** Uses a 45-device commercial LoRa dataset. Applies contrastive loss and distance thresholds. Unknown evaluation does not examine proxy familiarity effects.

---

### 5. CRODA-ST (2026)
- **Title:** *Calibrated Robust Open-Set Domain Adaptation for Source-Target RFF*
- **Venue:** arXiv:2607.02567, 2026.
- **Relevance:** Formulates open-set RF fingerprinting as a threshold reliability calibration problem. Notes that tuning on seen outliers can overfit to specific source characteristics.
- **Limitation:** Does not provide device-level bootstrap confidence intervals or Leave-One-Proxy-Out remedy testing.

---

### 6. Non-RF Context: Kong et al. (OpenGAN, 2021) & Koch et al. (LORD, 2023)
- **Context:** Landmark works in generic Open Set Recognition (OSR) and Out-of-Distribution (OOD) detection.
- **Relevance:** OpenGAN demonstrates that synthesizing or exposing models to outlier classes allows setting tighter open-set boundaries, but models can overfit to specific outlier exposure features. LORD establishes density estimation for out-of-distribution detection.
- **Citation Purpose:** Provides conceptual lineage demonstrating that known-unknown overfitting is a general machine learning phenomenon, which our work now rigorously measures and remedies in the domain of physical RF fingerprinting for AMR gateways.
