# Dataset Audit Report: LoRa_RFFI_dataset

Generated automatically by `src/audit.py`.  
Target Workspace: `c:\Users\maanv\Minor Project`  
Raw Data Path: `data/raw/`  

---

## 1. Executive Summary & File Inventory

The complete dataset archive (~15.55 GB) has been downloaded, verified, and placed into `data/raw/`. It contains 24 HDF5 files distributed across training and evaluation conditions, plus 5 pre-trained feature extractors in `models/` (which per our hard rules will **not** be used, as we train from scratch on enrolled devices).

### 1.1 Key Data Files

| Category | File | Size | Packets | Devices | Device ID Range |
|---|---|---|---|---|---|
| **Clean Baseline Training** | `Train/dataset_training_no_aug.h5` | 1.97 GB | 15,000 | 30 | `[1, 30]` (500 pkts/dev) |
| **Augmented Training** | `Train/dataset_training_aug.h5` | 3.93 GB | 30,000 | 30 | `[1, 30]` |
| **Augmented Training (0Hz)** | `Train/dataset_training_aug_0hz.h5` | 3.93 GB | 30,000 | 30 | `[1, 30]` |
| **Seen Devices Test** | `Test/dataset_seen_devices.h5` | 1.57 GB | 12,000 | 30 | `[1, 30]` (400 pkts/dev) |
| **Residential Test (Same Type)**| `Test/dataset_residential.h5` | 524 MB | 4,000 | 10 | `[31, 40]` (400 pkts/dev) |
| **Rogue Devices Test** | `Test/dataset_rogue.h5` | 131 MB | 1,000 | 5 | `[41, 45]` (200 pkts/dev) |
| **Other Device Type (Heterogeneous)**| `Test/dataset_other_device_type.h5`| 786 MB | 6,000 | 15 | `[46, 60]` (400 pkts/dev) |
| **Channel Variations (A..F, walk, etc.)**| `Test/channel_problem/*.h5` | ~4.2 GB | 2,000 ea | 10 ea | `[31, 40]` |

---

## 2. All 60 Physical Devices Accounted For

Every single device from 1 to 60 is present in the dataset:
- **Devices 1–30**: Primary pool of 30 commercial LoRa transmitters. In `dataset_training_no_aug.h5` (500 pkts/dev) and `dataset_seen_devices.h5` (400 pkts/dev).
- **Devices 31–40**: Unseen pool from identical hardware model in `dataset_residential.h5` (400 pkts/dev) and channel problem conditions (200 pkts/dev each).
- **Devices 41–45**: Rogue pool in `dataset_rogue.h5` (200 pkts/dev).
- **Devices 46–60**: Transmitters from different hardware models/manufacturers in `dataset_other_device_type.h5` (400 pkts/dev).

**Minimum Packet Count Verification:**  
Every device has between **200 and 500 unaugmented packets** (minimum 200 >= threshold 150). No device needs to be excluded due to packet starvation.

---

## 3. Data Layout, Preamble Length, and Normalization

- **HDF5 Keys**: Each file contains `['data', 'label', 'CFO', 'RSS']`.
- **Packet Shape**: `data` array has shape `(N, 16384)` with `float64`.
- **I/Q Layout**: 
  - First 8,192 elements represent In-phase ($I$) samples.
  - Second 8,192 elements represent Quadrature ($Q$) samples.
  - Total preamble length = 8,192 complex samples.
- **Normalization & Amplitude**:
  - Sample standard deviations: $\sigma_I \approx 0.148$, $\sigma_Q \approx 0.157$.
  - Magnitude: $\mu_{|r|} \approx 0.217 \pm 0.008$.
  - Signals have undergone hardware AGC / receiver scaling.
  - CFO is already compensated by receiver DSP. Per hard rules, no raw CFO feature is used.
  - Amplitude statistics will be included as relative envelope variation metrics (mean, std, skew, kurtosis of envelope).

---

## 4. Hardware / Group Information

The dataset partition naturally reveals hardware model boundaries:
- **Model Group 1 (Homogeneous)**: Devices `1–45` (same commercial transceiver model).
- **Model Group 2 (Heterogeneous)**: Devices `46–60` (`dataset_other_device_type.h5`, different manufacturer/hardware).

This directly enables the **Phase 8 hardware-model hardness analysis**: comparing false acceptance of true strangers that share the enrolled hardware model (`31–45`) versus strangers with distinct hardware (`46–60`).

---

## 5. Decisions Taken Because of the Audit

1. **Loader strategy**:
   - Devices `1–30` sourced from `Train/dataset_training_no_aug.h5` (or balanced 400 packets each).
   - Devices `31–40` sourced from `Test/dataset_residential.h5` (400 pkts each).
   - Devices `41–45` sourced from `Test/dataset_rogue.h5` (200 pkts each).
   - Devices `46–60` sourced from `Test/dataset_other_device_type.h5` (400 pkts each).
2. **Packet layout**: Deinterleave `(16384,)` into `I = data[:8192]`, `Q = data[8192:]` or `(8192, 2)`.
3. **Labels**: Device labels are 1-indexed integers `1..60`. Convert to integer IDs.
4. **Pre-trained models**: Completely excluded. The Random Forest classifier is trained strictly on enrolled training packets from scratch.
