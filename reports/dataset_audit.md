# Dataset Audit Report

Generated automatically by `src/audit.py`. Dataset path: `C:\Users\maanv\Minor Project\data\raw`

## Files Found

| File | Size (MB) |
|------|-----------|
| `A.h5` | 262.19 |
| `A_aug_0hz.h5` | 262.19 |
| `A_aug_100hz.h5` | 262.19 |
| `A_aug_10hz.h5` | 262.19 |
| `A_aug_30hz.h5` | 262.19 |
| `A_aug_50hz.h5` | 262.19 |
| `B.h5` | 262.19 |
| `B_antenna.h5` | 262.19 |
| `B_walk.h5` | 262.19 |
| `C.h5` | 262.19 |
| `D.h5` | 262.19 |
| `E.h5` | 262.19 |
| `F.h5` | 262.19 |
| `F_antenna.h5` | 262.19 |
| `F_walk.h5` | 262.19 |
| `moving_meeting_room.h5` | 262.19 |
| `moving_office.h5` | 262.19 |
| `dataset_other_device_type.h5` | 786.58 |
| `dataset_residential.h5` | 524.39 |
| `dataset_rogue.h5` | 131.10 |
| `dataset_seen_devices.h5` | 1573.15 |
| `dataset_training_aug.h5` | 3932.88 |
| `dataset_training_aug_0hz.h5` | 3932.88 |
| `dataset_training_no_aug.h5` | 1966.44 |

## Devices vs Packets (Primary Baseline Files)

| Device ID | Packets | Flagged (< min_packets) | Hardware Group |
|-----------|---------|-------------------------|----------------|
| 1 | 500 | No | Model_1_Homogeneous |
| 2 | 500 | No | Model_1_Homogeneous |
| 3 | 500 | No | Model_1_Homogeneous |
| 4 | 500 | No | Model_1_Homogeneous |
| 5 | 500 | No | Model_1_Homogeneous |
| 6 | 500 | No | Model_1_Homogeneous |
| 7 | 500 | No | Model_1_Homogeneous |
| 8 | 500 | No | Model_1_Homogeneous |
| 9 | 500 | No | Model_1_Homogeneous |
| 10 | 500 | No | Model_1_Homogeneous |
| 11 | 500 | No | Model_1_Homogeneous |
| 12 | 500 | No | Model_1_Homogeneous |
| 13 | 500 | No | Model_1_Homogeneous |
| 14 | 500 | No | Model_1_Homogeneous |
| 15 | 500 | No | Model_1_Homogeneous |
| 16 | 500 | No | Model_1_Homogeneous |
| 17 | 500 | No | Model_1_Homogeneous |
| 18 | 500 | No | Model_1_Homogeneous |
| 19 | 500 | No | Model_1_Homogeneous |
| 20 | 500 | No | Model_1_Homogeneous |
| 21 | 500 | No | Model_1_Homogeneous |
| 22 | 500 | No | Model_1_Homogeneous |
| 23 | 500 | No | Model_1_Homogeneous |
| 24 | 500 | No | Model_1_Homogeneous |
| 25 | 500 | No | Model_1_Homogeneous |
| 26 | 500 | No | Model_1_Homogeneous |
| 27 | 500 | No | Model_1_Homogeneous |
| 28 | 500 | No | Model_1_Homogeneous |
| 29 | 500 | No | Model_1_Homogeneous |
| 30 | 500 | No | Model_1_Homogeneous |
| 31 | 400 | No | Model_1_Homogeneous |
| 32 | 400 | No | Model_1_Homogeneous |
| 33 | 400 | No | Model_1_Homogeneous |
| 34 | 400 | No | Model_1_Homogeneous |
| 35 | 400 | No | Model_1_Homogeneous |
| 36 | 400 | No | Model_1_Homogeneous |
| 37 | 400 | No | Model_1_Homogeneous |
| 38 | 400 | No | Model_1_Homogeneous |
| 39 | 400 | No | Model_1_Homogeneous |
| 40 | 400 | No | Model_1_Homogeneous |
| 41 | 200 | No | Model_1_Homogeneous |
| 42 | 200 | No | Model_1_Homogeneous |
| 43 | 200 | No | Model_1_Homogeneous |
| 44 | 200 | No | Model_1_Homogeneous |
| 45 | 200 | No | Model_1_Homogeneous |
| 46 | 400 | No | Model_2_Heterogeneous |
| 47 | 400 | No | Model_2_Heterogeneous |
| 48 | 400 | No | Model_2_Heterogeneous |
| 49 | 400 | No | Model_2_Heterogeneous |
| 50 | 400 | No | Model_2_Heterogeneous |
| 51 | 400 | No | Model_2_Heterogeneous |
| 52 | 400 | No | Model_2_Heterogeneous |
| 53 | 400 | No | Model_2_Heterogeneous |
| 54 | 400 | No | Model_2_Heterogeneous |
| 55 | 400 | No | Model_2_Heterogeneous |
| 56 | 400 | No | Model_2_Heterogeneous |
| 57 | 400 | No | Model_2_Heterogeneous |
| 58 | 400 | No | Model_2_Heterogeneous |
| 59 | 400 | No | Model_2_Heterogeneous |
| 60 | 400 | No | Model_2_Heterogeneous |

## Normalisation Verdict

- **Mean Signal Amplitude:** 0.3186
- **Standard Deviation:** 0.0122
- **Verdict:** Signal amplitude is **NOT NORMALISED** (mean $\neq 1.0$).
- **Decision:** `amplitude_normalised: false`. Envelope amplitude moments (mean, std, skewness, kurtosis) are **included** in the feature pipeline.

## Hardware / Group Information

The LoRa RFFI dataset transmitters are partitioned into two distinct transceiver hardware categories:
- **Model Group 1 (Homogeneous SX1276):** Devices 1–45 (Train, Residential, and Rogue subsets).
- **Model Group 2 (Heterogeneous Other Transceivers):** Devices 46–60 (`dataset_other_device_type.h5`).

| device_id | group |
|---|---|
| 1 | Model_1_Homogeneous |
| 2 | Model_1_Homogeneous |
| 3 | Model_1_Homogeneous |
| 4 | Model_1_Homogeneous |
| 5 | Model_1_Homogeneous |
| 6 | Model_1_Homogeneous |
| 7 | Model_1_Homogeneous |
| 8 | Model_1_Homogeneous |
| 9 | Model_1_Homogeneous |
| 10 | Model_1_Homogeneous |
| 11 | Model_1_Homogeneous |
| 12 | Model_1_Homogeneous |
| 13 | Model_1_Homogeneous |
| 14 | Model_1_Homogeneous |
| 15 | Model_1_Homogeneous |
| 16 | Model_1_Homogeneous |
| 17 | Model_1_Homogeneous |
| 18 | Model_1_Homogeneous |
| 19 | Model_1_Homogeneous |
| 20 | Model_1_Homogeneous |
| 21 | Model_1_Homogeneous |
| 22 | Model_1_Homogeneous |
| 23 | Model_1_Homogeneous |
| 24 | Model_1_Homogeneous |
| 25 | Model_1_Homogeneous |
| 26 | Model_1_Homogeneous |
| 27 | Model_1_Homogeneous |
| 28 | Model_1_Homogeneous |
| 29 | Model_1_Homogeneous |
| 30 | Model_1_Homogeneous |
| 31 | Model_1_Homogeneous |
| 32 | Model_1_Homogeneous |
| 33 | Model_1_Homogeneous |
| 34 | Model_1_Homogeneous |
| 35 | Model_1_Homogeneous |
| 36 | Model_1_Homogeneous |
| 37 | Model_1_Homogeneous |
| 38 | Model_1_Homogeneous |
| 39 | Model_1_Homogeneous |
| 40 | Model_1_Homogeneous |
| 41 | Model_1_Homogeneous |
| 42 | Model_1_Homogeneous |
| 43 | Model_1_Homogeneous |
| 44 | Model_1_Homogeneous |
| 45 | Model_1_Homogeneous |
| 46 | Model_2_Heterogeneous |
| 47 | Model_2_Heterogeneous |
| 48 | Model_2_Heterogeneous |
| 49 | Model_2_Heterogeneous |
| 50 | Model_2_Heterogeneous |
| 51 | Model_2_Heterogeneous |
| 52 | Model_2_Heterogeneous |
| 53 | Model_2_Heterogeneous |
| 54 | Model_2_Heterogeneous |
| 55 | Model_2_Heterogeneous |
| 56 | Model_2_Heterogeneous |
| 57 | Model_2_Heterogeneous |
| 58 | Model_2_Heterogeneous |
| 59 | Model_2_Heterogeneous |
| 60 | Model_2_Heterogeneous |

## Decisions Taken Because of the Audit

- [x] Confirmed 60 unique devices; all exceed `min_packets=150` (min count = 200).
- [x] Preamble shape confirmed as 16,384 samples (8,192 In-phase, 8,192 Quadrature).
- [x] CFO feature strictly excluded as CFO is already compensated by receiver baseband DSP.
- [x] Amplitude features enabled due to non-unitary receiver envelope distribution.
- [x] Stratified block sampling enabled to prevent hardware composition confounds across experimental splits.