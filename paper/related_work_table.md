# Related Work Comparison Table

| Work | Year | Signal / dataset | #dev | Open-set method | Threshold type | Unknown test disjoint from calib? | Unknowns used in calib/train? | Reports FAR/FRR at frozen tau? | Paired familiar-vs-true stranger comparison? | Device-level CIs? | Proxy-count sweep? | Leave-identity-out (LOPO) calibration? | AMR / smart grid? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kong et al. (OpenGAN) | 2021 | Non-RF (CV) | N/A | OpenGAN discriminator | Score-based | Yes | Yes | No | No evidence found | No | No | No | No |
| Hanna et al. | 2021 | ISM band (WiFi/Zigbee) | 50 | Metric learning | Distance threshold | Yes | Yes | Yes | No evidence found | No | No | No | No |
| Shen et al. | 2022 | LoRa I/Q (868 MHz) | 60 | k-NN anomaly score | Fixed distance | Partly | No | Yes | No evidence found | No | No | No | No |
| Awan et al. | 2023 | Smart grid AMI | 20 | SVM / RF | Prob threshold | No | Yes | Yes | No evidence found | No | No | No | Yes |
| Koch et al. (LORD) | 2023 | Non-RF (CV) | N/A | Density OOD | Logit threshold | Yes | Yes | Yes | No evidence found | No | No | No | No |
| Zhang et al. | 2024 | LoRa preamble I/Q | 40 | CNN + OpenMax | EVT threshold | Partly | No | Yes | No evidence found | No | No | No | No |
| Cai et al. (JRFFP-SC) | 2025 | LoRa preamble I/Q | 45 | Contrastive learning | Distance threshold | Yes | Yes | Yes | No evidence found | No | No | No | No |
| Ma et al. | 2025 | Wi-Fi preamble I/Q | 54 | Prototypical network | Distance threshold | Yes | Yes | Yes | No evidence found | No | No | No | No |
| Owusu et al. | 2026 | IoT Wireless | 30 | Ensemble anomaly | Percentile | Partly | No | Yes | No evidence found | No | No | No | No |
| CRODA-ST | 2026 | RFF | 60 | Source-calibrated OOD | Calibrated tau | Yes | Yes | Yes | No evidence found | No | No | No | No |
| HoRFFI | 2026 | LoRa RF | 60 | Higher-order RFF | EVT threshold | Yes | Yes | Yes | No evidence found | No | No | No | No |
| **OUR WORK** | **2026** | **LoRa preamble I/Q (60 dev)** | **60** | **Random Forest** | **Frozen Youden / LOPO** | **Yes** | **Yes (Proxy)** | **Yes** | **Yes (Paired A/B)** | **Yes (Device CIs)** | **Yes (k=0..15)** | **Yes (LOPO remedy)** | **Yes** |

---

## Quantitative Differentiation Table: Reported Literature Numbers vs. Our Results

| Dimension / Metric | Shen et al. (2022) | Hanna et al. (2021) | Zhang et al. (2024) | Cai et al. (2025) | Ma et al. (2025) | **OUR WORK (2026)** |
|---|---|---|---|---|---|---|
| **Protocol & Transceiver** | LoRa SX1276 | Wi-Fi / Zigbee | LoRa | LoRa | Wi-Fi | **LoRa SX1276 COTS** |
| **Physical Radios (N)** | 60 | 50 | 40 | 45 | 54 | **60 (USRP N210 Capture)** |
| **Feature Representation** | 128 (metric latent) | Deep Metric latent | CNN feature map | Contrastive latent | 64 (prototype space) | **292 complex baseband features** |
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

