# Figure: Bias-to-Mitigation Mapping in Histopathology AI Fairness

**Source:** Results Chapter (chapters/03_results.tex), 78 experimental studies (data/experimental_78_paper.json)
**Date:** 2026-05-01

---

## Bias-to-Mitigation Mapping (Alluvial / Sankey Data)

### Left Nodes: 8 Bias Categories | Right Nodes: 16 Mitigation Families

Data format: `BiasCategory → MitigationFamily [n_studies]`

#### Demographic Bias (n=5) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Fairness-aware learning | 3 | lin2025contrastive (FAIR-Path: 88.5–91.1% reduction), xu2026spare (SPARE: 3.7–5.8% gain), polin2025mutation (FACL) |
| SSL / foundation models | 1 | vorontsov2024foundation (Virchow), chen2025predicting |
| Synthetic data / DDPM | 1 | ktena2024generative (48.5% fairness gain), vanbooven2025mitigating |
| Post-processing / Threshold opt | 1 | soltan2024challenges (EO achievable; resampling failed for demographic) |
| Explanation constraints | 1 | shabazian2025joint (ECGL: 73% EOD reduction) |
| Continual learning | 1 | cecconi2024fairness |
| Dataset curation | 1 | daneshjou2022disparities (DDI dataset fine-tuning) |
| Adversarial debiasing | 1 | lazarova2025demographic |

#### Representation Bias (n=7) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Dataset curation | 3 | soltan2024challenges, tasci2022bias, ceccon2025underrepresentation |
| Synthetic data / DDPM | 2 | ktena2024generative, vanbooven2025mitigating |
| SSL / foundation models | 1 | ling2025benchmark (CAMELYON re-processing) |
| Federated learning | 1 | musa2026cross |

#### Confounding Bias (n=6) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Dataset curation (preserved-site CV) | 3 | howard2021site, ly2024shortcut, dawood2026confounding |
| Harmonisation (ComBat) | 1 | lazard2022identifies |
| Fairness-aware learning | 1 | kheiri2025investigation |
| Adversarial debiasing | 1 | chen2025predicting (shortcut detection) |

#### Selection / Sampling Bias (n=8) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Dataset curation (preserved-site CV) | 4 | howard2021site, kheiri2025investigation, celi2022sources, weng2024grandqc (GrandQC) |
| Federated learning | 2 | raza2026clinical, bussola2023weakly |
| Resampling (SMOTE etc.) | 1 | rezama2018imbalanced (+3.4% BAcc) |
| SSL / foundation models | 1 | tolkach2023international |
| Synthetic data / DDPM | 1 | ceccon2025underrepresentation |

#### Class / Label Bias (n=7) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Resampling (SMOTE etc.) | 2 | rezama2018imbalanced, soltan2024challenges |
| Explanation constraints | 2 | hagele2020resolving (LRP +5% AUROC), kheiri2025investigation |
| Dataset curation | 1 | liang2023dynamic (dynamic label denoising) |
| Domain adaptation | 1 | nagpal2020development (DL Gleason 0.72 vs 0.58) |
| Uncertainty calibration | 1 | sauter2022validating (ACE concept-based explanations) |

#### Institutional / Batch Bias (n=7) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Harmonisation (ComBat) | 2 | murchan2024combat (Site AUROC →~0.5, MSI preserved), bidgoli2022bias (NSGA-II: F1 +6.1%, inst. acc −36%) |
| Dataset curation | 2 | howard2021site (preserved-site CV), mazaheri2023ranking (ranking loss: 73%→41.6%) |
| SSL / foundation models | 1 | komen2024batch (FM TSS 62-78% fine-tuned, >90% frozen) |
| Adversarial debiasing | 1 | dehkharghanian2023biased (86% site detection) |
| Federated learning | 1 | schmitt2021hidden |
| Domain adaptation | 1 | sikaroudi2023generalization (KimiaNet +3% OOD) |

#### Technical / Domain Shift Bias (n=8) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Conventional stain normalization | 3 | lin2025stain (4 normalisers fail), komen2024batch, voon2023evaluating (6 methods, no significant improvement) |
| Data augmentation | 2 | franchet2024bias (AugmentHist: +81% color, +21.7% AUROC), faryna2024automatic (RandAugment: AUROC 0.827 vs 0.799) |
| Domain adaptation | 2 | nerrienet2023standardized (CycleGAN: 0.57–0.84→0.92–0.98), aubreville2022mitosis (MIDOG: F1 0.748, range 0.375–0.848) |
| Advanced stain methods | 1 | madusanka2025structure (SSIM 0.9663), hetz2024multi (MultiStain-CycleGAN: domain acc 0.672) |
| Physical calibration | 1 | ji2025physical (Gleason κ 0.35–0.44→0.45–0.74) |
| Uncertainty calibration | 1 | roschewitz2023automatic (Youden 0.651→0.295) |
| Adversarial debiasing | 1 | otalora2019staining (DANN + color aug best) |
| SSL / foundation models | 1 | dunn2025stain (60% labs within 2ΔE) |

#### Algorithmic Bias (n=5) → Mitigations

| Mitigation Family | n Studies | Citation Keys |
|---|---|---|
| Fairness-aware learning | 2 | zong2023medfair (model-selection > algo), xu2026spare |
| Dataset curation / evaluation protocols | 1 | ling2024agent (AMD-MIL attention) |
| Explanation constraints | 1 | ly2024shortcut, skarga2023bias |
| Uncertainty calibration | 1 | sauter2022validating (ACE for dermatopathology) |
| Continual learning | 1 | cecconi2024fairness |
| Post-processing | 1 | tschida2025evaluating (NLP biomarker: BER gap >1.25, no racial DP/EOD/EOP disparity) |

---

## Sankey Flow Data Matrix (Bias → Mitigation Family, Study Count)

```
                        Mitigation Family
Bias Category           SN  DA  DC  RS  CH  DO  AD  SL  FL  SD  FW  TO  UC  CM  EC  CL   TOTAL
─────────────────────────────────────────────────────────────────────────────────────────────────
Demographic             0   0   1   0   0   0   1   1   0   1   3   1   0   0   1   1     10*
Representation          0   0   3   0   0   0   0   1   1   2   0   0   0   0   0   0      7
Confounding             0   0   3   0   1   0   1   0   0   0   1   0   0   0   0   0      6
Selection/Sampling      0   0   4   1   0   0   0   1   2   1   0   0   0   0   0   0      9*
Class/Label             0   0   1   2   0   1   0   0   0   0   0   0   1   0   2   0      7
Institutional/Batch     0   0   2   0   2   1   1   1   1   0   0   0   0   0   0   0      8*
Technical/Domain shift  3   2   0   0   0   2   1   1   0   0   0   0   1   0   0   0     10*
Algorithmic             0   0   1   0   0   0   0   0   0   0   2   1   1   0   1   1      7
─────────────────────────────────────────────────────────────────────────────────────────────────
TOTAL (by mitigation)   3   2  15   3   3   4   4   5   4   4   6   2   3   0   4   2      ~64**
```

\* Some studies report multiple bias types or mitigations, so totals exceed the taxonomy n-counts.

### Legend — Mitigation Families

| Abbrev | Mitigation Family | Abbrev | Mitigation Family |
|---|---|---|---|
| **SN** | Conventional Stain Normalization | **FL** | Federated Learning |
| **DA** | Data Augmentation | **SD** | Synthetic Data / DDPM |
| **DC** | Dataset Curation (incl. preserved-site CV, GrandQC) | **FW** | Fairness-aware Learning (FAIR-Path, SPARE, FLEX) |
| **RS** | Resampling (SMOTE, oversampling, etc.) | **TO** | Threshold Optimisation (post-processing) |
| **CH** | ComBat Harmonisation | **UC** | Uncertainty Calibration |
| **DO** | Domain Adaptation (CycleGAN, AIDA, DANN) | **CM** | Causal Methods |
| **AD** | Adversarial Debiasing | **EC** | Explanation Constraints (ECGL, LRP) |
| **SL** | SSL / Foundation Models | **CL** | Continual Learning |

---

## Summary Statistics for Figure Legend

| Metric | Value |
|---|---|
| Total experimental studies | N = 78 |
| Studies reporting explicit bias evidence | 46/78 (59.0%) |
| Studies focused on mitigation/technical only | 32/78 (41.0%) |
| Total bias category assignments | 53 (from 46 studies) |
| Mean assignments per study | 1.15 (median 1, range 1–2) |
| Mitigation method families identified | 16 |
| Strong evidence methods | 4 (Preserved-site CV, ComBat, FAIR-Path/SPARE, Federated) |
| Moderate evidence methods | 6 (Augmentation, Adversarial, SSL/FM, Synthetic/DDPM, Threshold opt, Advanced stain) |
| Mixed/Failed methods | 3 (Conventional stain norm, Resampling for demo bias, Classical domain adaptation) |
| Emerging methods | 5 (Causal, Explanation constraints, Continual learning, Uncertainty calibration, Physical calibration) |

---

## Key Co-occurrence Patterns (Dotted Arrows in Figure)

1. **Institutional × Selection** — most frequent pairing; site-specific datasets create both batch effects and sampling bias (howard2021site, kheiri2025investigation)
2. **Technical × Label** — stain variation correlated with annotation quality (hagele2020resolving, kheiri2025investigation)
3. **Confounding × Selection** — site–demographic entanglement compounds sampling bias (chen2025predicting, howard2021site)
