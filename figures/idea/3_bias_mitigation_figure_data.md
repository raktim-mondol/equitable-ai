# Figure: Bias Taxonomy Prevalence & Mitigation Map in Histopathology AI Fairness

**Source:** Results Chapter (chapters/03_results.tex), 78 experimental studies (data/experimental_78_paper.json)
**Date:** 2026-05-01

---

## Panel A: Bias Category Prevalence (Radial Bar / Lollipop Chart)

### Taxonomy: 8 Bias Categories (non-exclusive, 53 assignments from 46/78 studies)
**Note:** 32 studies (41.0%) focused on mitigation/technical performance without reporting explicit subgroup-specific bias evidence.
Among the 46 studies with explicit bias assignments: mean 1.15 per study, median 1, range 1–2.

| # | Bias Category | Group | n Assignments | Evidence Grade | Key Empirical Signal |
|---|---|---|---|---|---|
| 1 | **Demographic** | Patient-level | 5 | **Strong** | White–Black AUROC gap 3–16% across 20 cancers; race predictable from skin histology (AUROC ~0.70) |
| 2 | **Representation** | Patient-level | 7 | **Strong** | >70% White cohorts → lower non-White accuracy; Global South near-absent |
| 3 | **Confounding** | Patient-level | 6 | **Strong** | AUROC 0.798→0.507 (preserved-site); MI(label,center)=1.47 |
| 4 | **Selection / Sampling** | Data & label-level | 8 | **Strong** | 46.2% on TCGA; Acc 95%→79% (site removed); 5-external-cohort sensitivity 0.971–1.000 |
| 5 | **Class / Label** | Data & label-level | 7 | **Strong** | Gleason 30–53% discordance (DL 0.72 vs pathologist 0.58); stain shortcut −15% accuracy |
| 6 | **Institutional / Batch** | Technical/model-level | 7 | **Strong** | Site AUROC >0.96 on TCGA; FM TSS probe >90% (frozen), ComBat → ~0.5 |
| 7 | **Technical / Domain shift** | Technical/model-level | 8 | **Strong** | Cross-batch AUROC 0.74→0.52 (worst case); 4 normalisers fail; Youden 0.651→0.295 |
| 8 | **Algorithmic** | Technical/model-level | 5 | **Emerging** | MIL attention dilutes; model-selection > algo choice; post-processing fails |

### Suggested Color Coding for Panel A
- Patient-level: **Blue** shades
- Data & label-level: **Orange** shades
- Technical/model-level: **Teal/Green** shades

### Evidence Grade Legend
- **Strong:** ≥3 positive studies, multi-site validation
- **Emerging:** ≤2 studies, limited validation
- For Figure: Use solid fill for Strong, hatched for Emerging

---

## Panel B: Bias-to-Mitigation Mapping (Alluvial / Sankey Data)

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
| Harmonisation (ComBat) | 2 | murchan2024combat (Site AUROC →0.5, MSI preserved), bidgoli2022bias (NSGA-II: F1 +6.1%, inst. acc −36%) |
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

## Paper-Level Assignment to Bias Categories

Each paper assigned to the 8-category taxonomy based on its reported bias type(s). Non-exclusive: some papers study multiple bias types.

### 1. Demographic Bias (n=5 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Vaidya et al. - Demographic bias in misdiagnosis | 2024 | vaidya2024demographic | White–Black AUROC gap 3–16% across 20 cancers |
| 2 | Chen et al. - Predicting patient race from skin histology | 2025 | chen2025predicting | Race AUROC ~0.70 from histology; disease prevalence confound |
| 3 | Lin et al. - Contrastive learning enhances fairness (FAIR-Path) | 2025 | lin2025contrastive | 88.5–91.1% disparity reduction across 20 TCGA cancers |
| 4 | Lazarova et al. - Demographic disparities in dermatopathology | 2025 | lazarova2025demographic | Sex-based disparities in skin lesion diagnosis |
| 5 | Daneshjou et al. - Disparities in dermatology AI | 2022 | daneshjou2022disparities | DDI dataset; Fitzpatrick skin tone bias |

**Additional papers with demographic dimensions:**
- polin2025mutation — somatic mutation prevalence differences across populations
- arasteh2024preserving — sex-based disparities in privacy-preserving settings
- marinbenevic2024understanding — sex-based disparities in dermatopathology
- xu2026spare — SPARE reweighting for skin tone fairness
- ktena2024generative — conditional DDPM for demographic fairness

### 2. Representation Bias (n=7 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Soltan et al. - Challenges in reducing bias | 2024 | soltan2024challenges | >70% White cohorts; lower non-White accuracy |
| 2 | Tasci et al. - Bias in medical AI | 2022 | tasci2022bias | Rare cancer sub-types severely under-covered |
| 3 | Musa et al. - Cross-population validation | 2026 | musa2026cross | Global South populations near-absent |
| 4 | Ceccon et al. - Underrepresentation in pathology AI | 2025 | ceccon2025underrepresentation | Systematic geographic and subtype gaps |
| 5 | Ktena et al. - Generative models improve fairness | 2024 | ktena2024generative | Generative augmentation partially mitigates distributional gaps |
| 6 | Van Booven et al. - Mitigating bias in prostate cancer | 2025 | vanbooven2025mitigating | GAN synthesis for underrepresented Gleason grades (+15–32%) |
| 7 | Ling et al. - Benchmark dataset re-evaluation | 2025 | ling2025benchmark | CAMELYON: low-quality slides and erroneous labels as data-quality bias |

### 3. Confounding Bias (n=6 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Howard et al. - Site-specific digital histology signatures | 2021 | howard2021site | AUROC 0.798→0.507 preserved-site; site–demographic entanglement |
| 2 | Chen et al. - Predicting race from skin histology | 2025 | chen2025predicting | Disease prevalence differences inflate race-prediction |
| 3 | Dawood et al. - Confounding in multi-site survival analysis | 2026 | dawood2026confounding | Quantified confounding in survival prediction |
| 4 | Ly et al. - Shortcut learning detection | 2024 | ly2024shortcut | Shortcut-detection frameworks for confounders |
| 5 | Kheiri et al. - Investigation on bias factors | 2025 | kheiri2025investigation | MI(label,center)=1.47; BAcc 95%→79% |
| 6 | Lazard et al. - Identifies technical confounders | 2022 | lazard2022identifies | MI model–confounder: 0.83–0.88 before, 0.71 after correction |

### 4. Selection / Sampling Bias (n=8 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Howard et al. | 2021 | howard2021site | 35.7% features inflated; preserved-site CV |
| 2 | Kheiri et al. | 2025 | kheiri2025investigation | 46.2% on TCGA; Acc 95%→79% (site removed) |
| 3 | Celi et al. - Sources of bias | 2022 | celi2022sources | TCGA over-reliance as structural bias |
| 4 | Soltan et al. | 2024 | soltan2024challenges | Single-site >70% White → lower non-White accuracy |
| 5 | Tolkach et al. - International multi-institutional validation | 2023 | tolkach2023international | 5 external cohorts; sensitivity 0.971–1.000 |
| 6 | Raza et al. - Clinical-grade deployment | 2026 | raza2026clinical | Single-center generalization limits |
| 7 | Bussola et al. - Weakly supervised learning | 2023 | bussola2023weakly | Single-site constraints |
| 8 | Ceccon et al. | 2025 | ceccon2025underrepresentation | Geographic gap in training data |

### 5. Class / Label Bias (n=7 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Nagpal et al. - Gleason grading algorithm | 2020 | nagpal2020development | Gleason 30–50% discordance; DL 0.72 vs pathologists 0.58 |
| 2 | Kheiri et al. | 2025 | kheiri2025investigation | Grayscale −15% center discrimination; stain as labeling shortcut |
| 3 | Hägele et al. - Resolving challenges with explanation methods | 2020 | hagele2020resolving | LRP heatmaps; stain shortcut; AUROC +5% with targeted augmentation |
| 4 | Liang et al. - Dynamic label denoising | 2023 | liang2023dynamic | Noise-driven disparities attenuated |
| 5 | Reza & Ma - Imbalanced classification | 2018 | rezama2018imbalanced | SMOTE: +3.4% BAcc; failed for demographic bias |
| 6 | Sauter et al. - Validating ACE for digital histopathology | 2022 | sauter2022validating | Class-sampling-ratio, measurement, sampling, class-correlated bias discovered |
| 7 | Soltan et al. | 2024 | soltan2024challenges | Label imbalance across demographic groups |

### 6. Institutional / Batch Bias (n=7 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Howard et al. | 2021 | howard2021site | TSS AUROC >0.96 on TCGA; preserved-site CV |
| 2 | Komen et al. - Foundation models and batch effects | 2024 | komen2024batch | FM TSS probe >90% (frozen), 62–78% (fine-tuned) |
| 3 | Dehkharghanian et al. - Biased data, biased AI | 2023 | dehkharghanian2023biased | 86% site detection without explicit site training |
| 4 | Schmitt et al. - Hidden variables | 2021 | schmitt2021hidden | Age, slide preparation date, institute, scanner as hidden variables |
| 5 | Bidgoli et al. - Deep feature selection | 2022 | bidgoli2022bias | NSGA-II: F1 +6.1%, inst. acc −36–40% |
| 6 | Mazaheri et al. - Ranking loss for bias reduction | 2023 | mazaheri2023ranking | Hospital classification 73%→41.6% via ranking loss + ISL |
| 7 | Murchan et al. - ComBat harmonisation | 2024 | murchan2024combat | Site AUROC →~0.5; MSI AUROC preserved (0.669→0.669) |

### 7. Technical / Domain Shift Bias (n=8 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Lin et al. - Stain normalization evaluation | 2025 | lin2025stain | AUROC 0.74→0.52 cross-batch; 4 normalisers (Macenko, Reinhard, Vahadane, CycleGAN) fail |
| 2 | Komen et al. | 2024 | komen2024batch | Fine-tuned FMs retain 62–78% TSS; 4 norm. methods insufficient |
| 3 | Roschewitz et al. - Automatic correction of performance drift | 2023 | roschewitz2023automatic | Scanner replacement: Youden 0.651→0.295; UPA for drift correction |
| 4 | Aubreville et al. - MIDOG challenge | 2022 | aubreville2022mitosis | F1 0.748, range 0.375–0.848 across scanners |
| 5 | Franchet et al. - AugmentHist | 2024 | franchet2024bias | Color dispersion +81%, AUROC +21.7% with AugmentHist |
| 6 | Nerrienet et al. - Standardized CycleGAN | 2023 | nerrienet2023standardized | Cross-center AUROC 0.57–0.84→0.92–0.98 |
| 7 | Dunn et al. - International stain variability study | 2025 | dunn2025stain | 247 labs; 60% within 2ΔE; stain variation widespread |
| 8 | Voon et al. - Evaluating stain normalization | 2023 | voon2023evaluating | 6 methods, no significant accuracy improvement |

### 8. Algorithmic Bias (n=5 studies)

| # | Study | Year | Citation Key | Specific Finding |
|---|---|---|---|---|
| 1 | Ling et al. - Agent Aggregator with Mask Denoise | 2024 | ling2024agent | Standard MIL attention dilutes diagnostic instances |
| 2 | Zong et al. - MedFair benchmark | 2023 | zong2023medfair | Model-selection > algorithm choice; no single method beats ERM across all settings |
| 3 | Soltan et al. | 2024 | soltan2024challenges | Post-processing fairness adjustments fail to consistently reduce disparities |
| 4 | Cecconi et al. - Fairness evolution in continual learning | 2024 | cecconi2024fairness | Pseudo-Label best fairness but AUROC ↓9pp; fairness task- and attribute-dependent |
| 5 | Sauter et al. - ACE for digital histopathology | 2022 | sauter2022validating | ACE discovers class-sampling-ratio, measurement, sampling biases in CNNs |

**Additional algorithmic studies:**
- ly2024shortcut — attribution methods quantify shortcut exploitation
- skarga2023bias — shortcut exploitation in histopathology
- tschida2025evaluating — NLP biomarker: registry-level BER gaps (ratio >1.25), no racial DP/EOD/EOP disparity

---

## Panel B: Sankey Flow Data (Bias → Mitigation Family, Study Count Matrix)

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

**Legend — Mitigation Families:**
- **SN:** Conventional Stain Normalization
- **DA:** Data Augmentation
- **DC:** Dataset Curation (incl. preserved-site CV, GrandQC)
- **RS:** Resampling (SMOTE, oversampling, etc.)
- **CH:** ComBat Harmonisation
- **DO:** Domain Adaptation (CycleGAN, AIDA, DANN)
- **AD:** Adversarial Debiasing
- **SL:** SSL / Foundation Models
- **FL:** Federated Learning
- **SD:** Synthetic Data / DDPM
- **FW:** Fairness-aware Learning (FAIR-Path, SPARE, FLEX)
- **TO:** Threshold Optimisation (post-processing)
- **UC:** Uncertainty Calibration
- **CM:** Causal Methods
- **EC:** Explanation Constraints (ECGL, LRP)
- **CL:** Continual Learning

\* Some studies report multiple bias types or mitigations, so totals exceed the taxonomy n-counts.

---

## Summary Statistics for Figure Legend

| Metric | Value |
|---|---|
| Total experimental studies | N = 78 |
| Studies reporting explicit bias evidence | 46/78 (59.0%) |
| Studies focused on mitigation/technical only | 32/78 (41.0%) |
| Total bias category assignments | 53 (from 46 studies) |
| Mean assignments per study | 1.15 (median 1, range 1–2) |
| Studies reporting any fairness metric | 15/78 (19.2%) |
| Studies reporting worst-group accuracy | 4/78 (5.1%) |
| Studies using histopathology images directly | ~72/78 (92.3%) |
| Studies reporting demographic metadata | Race 28.2%, Sex 25.6%, Age 23.1% (of 39 audited public datasets) |
| Mitigation method families identified | 16 |
| Strong evidence methods | 4 (Preserved-site CV, ComBat, FAIR-Path/SPARE, Federated) |
| Moderate evidence methods | 6 (Augmentation, Adversarial, SSL/FM, Synthetic/DDPM, Threshold opt, Advanced stain) |
| Mixed/Failed methods | 3 (Conventional stain norm, Resampling for demo bias, Classical domain adaptation) |
| Emerging methods | 5 (Causal, Explanation constraints, Continual learning, Uncertainty calibration, Physical calibration) |

---

## Key Co-occurrence Patterns (Dotted Arrows in Figure)

From the taxonomy figure (Fig. 1):

1. **Institutional × Selection** — most frequent pairing; site-specific datasets create both batch effects and sampling bias (howard2021site, kheiri2025investigation)
2. **Technical × Label** — stain variation correlated with annotation quality (hagele2020resolving, kheiri2025investigation)
3. **Confounding × Selection** — site–demographic entanglement compounds sampling bias (chen2025predicting, howard2021site)

---

## Evidence Grades for Mitigation Families (Table 3 / Fig. 3 in paper)

| Mitigation Family | Stage | Evidence Grade | # Supporting Studies | Key Metric |
|---|---|---|---|---|
| Conventional stain normalization | Pre | Mixed (workflow) / Failed (fairness) | 15+ | Cross-batch AUROC near chance (0.52–0.61) |
| Data augmentation | Pre | Moderate | 20+ | RandAugment AUROC 0.827 vs 0.799; AugmentHist +21.7% AUROC |
| Dataset curation (preserved-site CV) | Data | **Strong** | 6+ | Exposed inflated performance for 35.7% features |
| Resampling (SMOTE etc.) | Data | Mixed | 4+ | +3.4% BAcc for class imbalance; failed for demographic |
| Harmonisation (ComBat) | Feature | **Strong** | 3+ | Site AUROC →~0.5; clinical signal preserved |
| Domain adaptation | In | Mixed | 10+ | AIDA: BAcc +14.2%; CORAL/IRM/GroupDRO failed on WILDS |
| Adversarial debiasing | In | Moderate | 8+ | Suppresses site features; hyperparameter-sensitive |
| SSL / foundation models | In | Moderate | 5+ | SimCLR: macro F1 66.7%→77.0%; FM TSS 62–78% (still retain) |
| Federated learning | In | **Strong** | 6+ | Prop-FFL: variance 32.54→10.00; DynamicFL: 87.4% vs 78.1% |
| Synthetic data / DDPM | Data | Moderate | 4+ | Cond. DDPM: 48.5% fairness gain, +3.2% vs augmentation |
| Fairness-aware learning | In | **Strong** | 10+ | FAIR-Path: 88.5–91.1% reduction; SPARE: +3.7–5.8%; FLEX: gap ↓61% |
| Threshold optimisation | Post | Moderate | 4+ | EO achievable; requires attribute labels at deployment |
| Uncertainty calibration | Post | Emerging | 3 | Label smoothing for MIL; conformal prediction coverage |
| Causal methods | In | Emerging | 1 | Equalised survival prediction across sites |
| Explanation constraints | In | Emerging | 2 | ECGL: 73% EOD reduction; LRP: AUROC +5% |
| Continual learning | In | Emerging | 1 | Pseudo-Label best fairness; AUROC ↓9pp; unpredictable |

---

## References (All Citation Keys Used in Figure Data)

### Demographic Bias
- vaidya2024demographic
- chen2025predicting
- lin2025contrastive
- lazarova2025demographic
- daneshjou2022disparities
- polin2025mutation
- arasteh2024preserving
- marinbenevic2024understanding

### Representation Bias
- soltan2024challenges
- tasci2022bias
- musa2026cross
- ceccon2025underrepresentation
- ktena2024generative
- vanbooven2025mitigating
- ling2025benchmark

### Confounding Bias
- howard2021site
- chen2025predicting
- dawood2026confounding
- ly2024shortcut
- kheiri2025investigation
- lazard2022identifies

### Selection / Sampling Bias
- howard2021site
- kheiri2025investigation
- celi2022sources
- soltan2024challenges
- tolkach2023international
- raza2026clinical
- bussola2023weakly
- ceccon2025underrepresentation
- weng2024grandqc

### Class / Label Bias
- nagpal2020development
- kheiri2025investigation
- hagele2020resolving
- liang2023dynamic
- rezama2018imbalanced
- sauter2022validating
- soltan2024challenges

### Institutional / Batch Bias
- howard2021site
- komen2024batch
- dehkharghanian2023biased
- schmitt2021hidden
- bidgoli2022bias
- mazaheri2023ranking
- murchan2024combat
- sikaroudi2023generalization
- chen2022pan

### Technical / Domain Shift Bias
- lin2025stain
- komen2024batch
- roschewitz2023automatic
- aubreville2022mitosis
- franchet2024bias
- nerrienet2023standardized
- dunn2025stain
- voon2023evaluating
- ji2025physical
- madusanka2025structure
- hetz2024multi
- cazaniga2024not
- faryna2024automatic

### Algorithmic Bias
- ling2024agent
- zong2023medfair
- soltan2024challenges
- cecconi2024fairness
- sauter2022validating
- ly2024shortcut
- skarga2023bias
- tschida2025evaluating

### Mitigation Methods (additional)
- koh2021wilds (WILDS-Camelyon17 benchmark)
- huang2025knowledge (FLEX)
- xu2026spare (SPARE)
- hosseini2023proportionally (Prop-FFL)
- zhang2025dynamicfl (DynamicFL)
- sufian2024mitigating
- shabazian2025joint (ECGL)
- correamedero2024causal
- bhattacharyya2025conformal
- park2025uncertainty
- haggenmuller2024federated
- lu2022federated
- adnan2022federated
- agbley2022federated
- shukla2025federated
- campanella2019clinical
- campanella2025clinical (clinical benchmark of 11 FMs)
- ciga2023self (SimCLR 57 datasets)
- vorontsov2024foundation (Virchow)
- sounderajah2021stardai (STARD-AI)
- norori2021addressing
- montezuma2025unbiased
- chen2023algorithmic
- riccilara2022addressing
- yang2024survey
- chinta2025aidriven
- olsson2022estimating
- asadiaghbolagh2024learning (AIDA)
- lafarge2019learning
- otalora2019staining
- vasiljevic2022cyclegan
- ren2019unsupervised
- ahmed2025robust (K-TOP MIL)
