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

