# Paper Outline
## "The Familiar Stranger Problem": Packet-Disjoint vs Identity-Disjoint Evaluation of Open-Set LoRa RF Fingerprint Authentication for AMR Gateway Security

### Sections

1. **Introduction** — Open with the Familiar Stranger story; motivate the Familiarity Gap; state contributions.
2. **Related Work** — Use table from Phase 10; positioning paragraph per §0.2.
3. **Dataset and Audit** — LoRa_RFFI dataset; audit findings; scope limits.
4. **Method** — Experimental design; device groups; feature pipeline; threshold calibration; LOPO.
5. **Metrics** — FAR, FRR, AUROC, macro-F1, ΔF​AR definition, device-level CI methodology.
6. **Results**
   - 6.1 A/B comparison (packet-disjoint vs identity-disjoint)
   - 6.2 Device-matched paired analysis (confound elimination)
   - 6.3 Proxy-count sweep ($k \in \{0, 1, 3, 5, 10, 15\}$)
   - 6.4 Per-device hardness and hardware model clustering
   - 6.5 LOPO estimator bias and identity-robust threshold trade-off
   - 6.6 Multi-packet burst decision fusion ($L \in \{1, 3, 5\}$)
7. **Discussion** — Interpret ΔF​AR; practical implications for AMR gateway evaluation.
8. **Limitations** — See §0.5 and Phase 11 requirements.
9. **Conclusion** — Answer all questions from Phase 11.

_Fill sections only after results are available (Phase 11)._

