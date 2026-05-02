# AI Image Generation Prompts — Figure 2: Panels 8–13

## Overview

Generate a **6-panel multi-figure illustration** (3×2 grid) for an academic paper titled *"Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging."* Each panel explains one or more fairness metrics using a **real published histopathology example** with actual numbers from the 78-study systematic review corpus. The figure serves as a visual glossary for histopathology researchers unfamiliar with fairness evaluation.

**Style:** Clean scientific illustration — like a Nature Reviews figure or BioRender diagram. Flat vector aesthetic, no photo-realism. Use a consistent two-color scheme: **blue (#1F78B4)** for the advantaged/reference group, **orange (#E66101)** for the disadvantaged group.

**Layout:** 3 columns × 2 rows on a white/transparent background. Each panel is self-contained with a mini chart/diagram and a 1–2 line caption below it. Overall figure title at top: **"How Fairness Metrics Work — Part 2: Site, Distribution Shift & Deployment Metrics"**

---

## Panel 8: In-Distribution vs Out-of-Distribution (OOD) Gap

### Reference
**Komen et al. (2024)** — *"Do Histopathological Foundation Models Eliminate Batch Effects? A Comparative Study"*
- **Citation key:** `komen2024batch`
- **Dataset:** TCGA-LUSC-5 (5 tissue source sites, ~250,000 patches); CAMELYON16 (2 sites, ~100,000 patches)
- **Why this example:** Directly investigates whether foundation models eliminate site-specific batch effects in histopathology. Shows that even state-of-the-art pathology foundation models encode site identity, and when batch effects correlate with labels, performance collapses OOD.

### Real Data
- **TSS (tissue source site) prediction accuracy: >90% on TCGA-LUSC-5, ~100% on CAMELYON16** — features encode site identity nearly perfectly via linear probing
- **Cancer classification drops from >90% (uncorrelated data) to <20–50% (fully correlated TSS-label data)** — dramatic OOD failure
- Stain normalization (Reinhard, Macenko) reduced TSS prediction but linear probe accuracies remained **>80% (TCGA-LUSC-5)** and **>97% (CAMELYON16)**
- Foundation models do NOT eliminate batch effects; site signatures dominate distances in feature space
- **Corroborating evidence:** WILDS-CAMELYON17 benchmark shows **22.9pp** ID–OOD accuracy gap (Koh et al. 2021, cited in the paper's discussion); CORAL, IRM, and Group DRO all leave this gap largely unresolved on histopathology data

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Top section: Schematic showing two scenarios side by side.

Left scenario (labeled "Uncorrelated: TSS ⟂ Label"):
- Two site blocks (Site A blue, Site B orange) with disease labels (+ and -) evenly mixed across both sites
- Bar below: Cancer classification accuracy at 92% (tall green bar)
- Label: "Model learns disease, not site"

Right scenario (labeled "Correlated: TSS ~ Label"):
- Site A (blue) has mostly positive disease labels (+), Site B (orange) has mostly negative labels (-)
- Bar below: Cancer classification accuracy at 35% (short red bar)
- Label: "Model exploits site as shortcut — OOD collapse"

Middle: A bridge arrow between scenarios labeled "When training site predicts label, OOD performance collapses to <20-50%".

Bottom section: Bar chart showing "Site prediction accuracy from features". 
Two bars: "TCGA-LUSC-5" at >90% (blue) and "CAMELYON16" at ~100% (orange).
Annotation: "Features encode site identity near-perfectly even in foundation models."

Below: small text "Komen et al. 2024 — TCGA-LUSC-5, CAMELYON16".

Blue (#1F78B4) for advantaged/clean setup, orange (#E66101) for confounded/OOD setup. 
Red (#D55E00) for performance collapse. Clean vector style.
```

### Caption Text
**ID vs OOD evaluation exposes site-confounded shortcuts.** Komen et al. (2024) showed that histopathology foundation model features encode tissue source site with >90–100% accuracy via linear probing. When site correlates with disease label, cancer classification collapses from >90% to <20–50% under distribution shift — demonstrating that even state-of-the-art models fail OOD when batch effects are not controlled.

---

## Panel 9: Bias Proxy Metrics (Site Classification, Mutual Information)

### Reference
**Kheiri et al. (2025)** — *"Investigation on potential bias factors in histopathology datasets"*
- **Citation key:** `kheiri2025investigation`

### Real Data
- KimiaNet feature extractor: **Cancer-type classification 99%**, but **Data center classification 96%** simultaneously — features encode site identity almost as strongly as disease
- Mutual information MI(label, center) = **1.47** for TCGA — strong cancer-site dependency
- With co-slice exclusion: Cancer-Acc drops to 48%, Center-Acc remains 60%
- Fair subset (balanced LUAD/LUSC): Cancer-Acc 79%, Center-Acc 66%
- EfficientNet consistently: Cancer-Acc 83%, Center-Acc 68% across all settings

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Left side: A simple neural network diagram. Input = a histopathology patch → feature extractor (CNN, blue box) → two output heads:
- Top head labeled "Cancer Classifier" with accuracy badge "99%"
- Bottom head labeled "Site Probe" with accuracy badge "96%"
Both accuracies shown prominently. A red exclamation mark next to "96%" emphasizing that features contain strong site signal.

Right side: A bar chart showing Mutual Information. Two bars:
- Blue bar: MI(cancer type, site) = 1.47, labeled "Label-Site dependency"
- Orange bar: MI(features, site) with a high value

Below: small text "Kheiri et al. 2025".

A small inset text: "If a probe achieves 96% site accuracy, features encode batch effects almost as strongly as disease — a bias red flag."

Clean vector style. Blue (#1F78B4) and orange (#E66101).
```

### Caption Text
**Bias proxy: site-classification accuracy from learned features.** Kheiri et al. (2025) showed that a linear probe on KimiaNet features achieves 96% accuracy at identifying which hospital a slide came from — nearly matching cancer classification accuracy (99%). High site-classifiability indicates features are confounded by batch effects rather than encoding pure disease signal. Mutual information MI(label, center) = 1.47 quantifies this dependency.

---

## Panel 10: TPR Disparity RMSE (Multi-Subgroup Disparity Summary)

### Reference
**Huang et al. (2025)** — *"Knowledge-guided adaptation of pathology foundation models effectively improves cross-domain generalization and demographic fairness"*, Nature Communications, Vol. 16, 11485.
- **Citation key:** `huang2025knowledge`
- **Dataset:** TCGA (9,900+ slides), CPTAC, NFH in-house; 16 clinical tasks; self-reported race + genetic ancestry
- **Why this example:** The only study reporting TPR disparity RMSE — a more robust alternative to simple max−min TPR disparity because it accounts for all subgroups simultaneously rather than just extremes. RMSE penalises large disparities in any subgroup.

### Real Data
- **C-UAD-EGFR task**: TPR disparity RMSE reduced from **0.140 → 0.085** (39% reduction) by FLEX
- **C-BRCA-TYPE task**: FLEX yields significantly tighter and more equitable performance curves across race groups
- RMSE summarises per-group TPR deviations from the mean into a single number — lower = fairer
- Comparison to simple max−min TPR gap: RMSE detects when multiple subgroups are disadvantaged, not just the worst one
- Statistical significance: NSCLC-CTE P=0.018, BRCA-PR P=0.048, CRCA-CTLA4 P=0.004, CLUAD-EGFR P=0.004 (Wilcoxon signed-rank, FLEX vs Original)

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Top: A schematic showing 4 subgroups (race A, race B, race C, race D) each with a TPR bar deviating from a population-mean reference line (dashed horizontal). Highlight that RMSE captures deviations across ALL groups, not just the max−min gap.

Middle: A before/after comparison for the C-UAD-EGFR task.

Left box labeled "Before FLEX":
- 4 TPR bars at different heights (e.g., 0.82, 0.88, 0.91, 0.96) with wide spread
- Annotation below: "TPR disparity RMSE = 0.140"

Right box labeled "After FLEX":
- Same 4 bars now tightly clustered (e.g., 0.88, 0.90, 0.91, 0.93)
- Annotation below: "TPR disparity RMSE = 0.085 (↓ 39%)"

Arrow between the two boxes connecting them.

Bottom: A small RMSE formula: RMSE = √(1/n · Σ(TPRᵢ − TPR_mean)²)

Below: small text "Huang et al. 2025, Nature Communications 16:11485 — TCGA 16 tasks".

Blue (#1F78B4) for reference/advantaged, orange (#E66101) for disadvantaged subgroups.
Clean vector style. Scientific publication quality.
```

### Caption Text
**TPR disparity RMSE = root-mean-square of per-subgroup TPR deviations from the mean.** Unlike simple max−min TPR gap, RMSE captures disparities across ALL subgroups simultaneously. Huang et al. (2025) reduced TPR disparity RMSE from 0.140 to 0.085 (39% reduction) in the C-UAD-EGFR task using FLEX, demonstrating that knowledge-guided adaptation tightens per-group recall uniformly.

---

## Panel 11: Equal Balanced Accuracy (EBAcc) & AUROC Difference (AUROCDiff)

### Reference
**Lin et al. (2025)** — *"Contrastive learning enhances fairness in pathology artificial intelligence systems"*
- **Citation key:** `lin2025contrastive`
- **Dataset:** TCGA (28,732 WSIs, 14,456 patients, 20 cancer types), CPTAC-3, PLCO, DFCI, Medical University of Vienna — 8 datasets, 7 institutions
- **Why this example:** The only study reporting EBAcc and AUCDiff across 20 cancer types. EBAcc ensures balanced accuracy is equal across groups (not just TPR), and AUCDiff captures per-group discriminative power differences — complementary to EOp and EOEq.

### Real Data
- **EBAcc (Equal Balanced Accuracy)**: FAIR-Path resolved disparities in 100% of cancer detection and subtype classification tasks, 80% in histological type classification
- **AUCDiff (AUC Difference)**: Significant AUROC differences between demographic groups were present in 29.93% (11/37) of tasks before mitigation
- FAIR-Path achieved **88.5% mitigation** of EBAcc/AUCDiff disparities in internal validation
- **91.1% reduction** in external validation across 15 independent cohorts
- Specific example — IDC vs ILC (breast, FFPE): significant age disparities in EBAcc (p=0.044)
- GBM vs LGG (brain, frozen): significant racial disparities in EOp (p=0.025)
- Paired with EOp and EOEq (Panel 3, Figure 1), EBAcc + AUCDiff provide a complete picture of group-wise fairness

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Two metric panels side by side.

Left sub-panel: "Equal Balanced Accuracy (EBAcc)"
A pair of bar charts with two groups (reference group = blue, disadvantaged group = orange).
Before: blue at ~0.88 balanced accuracy, orange at ~0.81 → gap visible.
After FAIR-Path: both at ~0.88 → gap closed.
Annotation: "100% resolution in cancer detection & subtype classification"

Right sub-panel: "AUC Difference (AUCDiff)"
Two small ROC curves overlaid. Blue curve AUC=0.91, orange curve AUC=0.84.
A shaded region between curves, annotated "AUCDiff = 0.07 before mitigation".
A second inset: "After FAIR-Path: AUCDiff → near zero".

Bottom: summary text "29.93% (11/37) tasks affected → 88.5% mitigated".

Below: small text "Lin et al. 2025 — 28,732 TCGA WSIs, 20 cancer types".

Blue (#1F78B4) and orange (#E66101). Clean vector style. 
Green (#33A02C) for post-mitigation equality.
```

### Caption Text
**EBAcc = |BalAcc_groupA − BalAcc_groupB|; AUROCDiff = |AUC_groupA − AUC_groupB|.** Lin et al. (2025) showed that 29.93% of diagnostic tasks exhibited significant EBAcc or AUCDiff disparities across race, gender, and age. FAIR-Path resolved 100% of these in cancer detection/subtyping and 88.5% overall — demonstrating that balanced accuracy and AUROC gaps are correctable without sacrificing performance.

---

## Panel 12: Youden's Index (Threshold Sensitivity Under Distribution Shift)

### Reference
**Roschewitz et al. (2023)** — *"Automatic correction of performance drift under acquisition shift in medical image classification"*, Nature Communications, Vol. 14, Article 7236.
- **Citation key:** `roschewitz2023automatic`
- **Dataset:** OPTIMAM (UK breast screening mammography, 12,828 cases); WILDS Camelyon17 (histopathology, 302,436 training images, 5 sites)
- **Why this example:** The only study reporting Youden's Index in a fairness context. J = TPR + TNR − 1 quantifies the optimal operating point of a classifier, and its preservation under domain shift is critical for safe deployment — if J collapses on a new site, the model's clinical utility is compromised for that population.

### Real Data
- **Mammography (breast screening) — before vs after UPA alignment:**
  - Scanner A: Youden's Index **0.295 → 0.651** (2.2× improvement)
  - Scanner B: **0.589 → 0.594** (maintained)
  - Scanner D: **0.644 → 0.640** (maintained)
- **Histopathology (Camelyon17, tissue classification) — before vs after UPA:**
  - Site S4: Youden's Index **0.868 → 0.864** (preserved near ceiling)
  - Site S5: **0.859 → 0.863** (preserved near ceiling)
- ROC-AUC preserved across all domains (mammography 0.85–0.93, histopathology 0.97–0.98)
- UPA requires only ~250 unlabelled cases (1,000 images) from the new domain for alignment
- ECE preserved after alignment (0.13→0.14 vs 0.29 before) — calibration transfers with Youden's Index

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Top section: A conceptual diagram showing a classifier's ROC curve with the Youden's Index point marked.
- ROC curve from (0,0) to (1,1), point P marked at the shoulder
- Annotation: "J = TPR + TNR − 1 = distance from diagonal"
- The point P is the operating point where sensitivity ≈ specificity

Middle section: Bar chart comparing Youden's Index before vs after UPA alignment.
Two groups of bars:
Group 1 (Breast Screening, 3 scanners):
  Scanner A: before 0.295 (gray), after 0.651 (green) — dramatic improvement
  Scanner B: before 0.589 (gray), after 0.594 (green) — maintained
  Scanner D: before 0.644 (gray), after 0.640 (green) — maintained

Group 2 (Histopathology, 2 sites):
  Site S4: before 0.868 (gray), after 0.864 (green) — preserved
  Site S5: before 0.859 (gray), after 0.863 (green) — preserved

A horizontal dashed line at J=1.0 labeled "Perfect classifier."

Annotation: "UPA preserves clinical operating point under acquisition shift without any labelled data from the new domain."

Below: small text "Roschewitz et al. 2023, Nature Communications 14:7236 — OPTIMAM + WILDS Camelyon17".

Gray (#BABABA) for before, green (#33A02C) for after alignment. Clean vector style.
```

### Caption Text
**Youden's Index J = TPR + TNR − 1; supports threshold choice under distribution shift.** Roschewitz et al. (2023) demonstrated that when a model is deployed to a new scanner or hospital site, the clinical operating point (where sensitivity ≈ specificity) can drift substantially — Scanner A's J collapsed from 0.651 to 0.295. Their unsupervised prediction alignment (UPA) restored the operating point using only 250 unlabelled cases, preserving both Youden's Index and calibration (ECE 0.13) across domains.

---

## Panel 13: Inter-Hospital Performance Variance (Federated Learning Equity)

### Reference
**Hosseini et al. (2023)** — *"Proportionally Fair Hospital Collaborations in Federated Learning of Histopathology Images"*, IEEE Transactions on Medical Imaging, Vol. 42, No. 7, pp. 1982–1995.
- **Citation key:** `hosseini2023proportionally`
- **Dataset:** TCGA Kidney (4 hospitals, 642,277 patches); TCGA Lung (6 hospitals, 303,053 patches)
- **Why this example:** The only study measuring inter-hospital performance variance as a fairness metric in federated histopathology learning. Prop-FFL explicitly minimises the variance of accuracy across participating hospitals, preventing the global model from favouring large-data hospitals at the expense of smaller ones.

### Real Data
- **TCGA Kidney (4 hospitals) — Prop-FFL accuracy per hospital:**
  - Hospital 1: 78.84%, Hospital 2: 77.12%, Hospital 3: 76.21%, Hospital 4: 84.36%
  - **Prop-FFL variance = 10.00** vs FedSGD variance = 32.54 → **69% variance reduction**
  - q-FedSGD variance = 11.22 (Prop-FFL still better by 11%)
- **TCGA Lung (6 hospitals) — Prop-FFL accuracy per hospital:**
  - 72.23% / 76.81% / 74.57% / 74.60% / 76.44% / **60.81%** (worst hospital)
  - **Prop-FFL variance = 29.84** vs FedSGD variance = 40.13 → **26% variance reduction**
- Prop-FFL objective: maximise the product of relative training losses across hospitals, encouraging uniform convergence
- Standard FedSGD/FedAvg minimises average loss, allowing the model to be biased toward hospitals with larger datasets

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Top section: Schematic of federated learning. 
A central server icon in the middle, connected to 4 hospital icons (H1, H2, H3, H4) arranged around it, each shown with different dataset sizes (H1 large, H4 small). Arrows going up (model updates) and down (aggregated model).

Bottom section: Side-by-side comparison.

Left: "Standard FedSGD — Minimises Average Loss"
Bar chart for Kidney dataset, 4 hospitals:
- H1: 85% (tall blue bar)
- H2: 75% (medium blue bar)
- H3: 82% (tall blue bar)  
- H4: 68% (short orange bar — worst)
Variance annotation: "Var = 32.54 — large spread"
Large hospital icons get better performance.

Right: "Prop-FFL — Minimises Performance Variance"
Same 4 hospitals:
- H1: 79% (medium bar)
- H2: 77% (medium bar)
- H3: 76% (medium bar)
- H4: 84% (tall bar — improved!)
Variance annotation: "Var = 10.00 — 69% reduction"

A bridging arrow: "Proportional fairness: hospitals with worse performance contribute more to the loss function."

Below: small text "Hosseini et al. 2023, IEEE Trans Med Imaging 42(7):1982–1995 — TCGA Kidney 642K patches".

Blue (#1F78B4) for larger-data hospitals, orange (#E66101) for worst-performing/small-data hospitals.
Green (#33A02C) for Prop-FFL improvement. Clean vector style.
```

### Caption Text
**Inter-hospital variance = Var(accuracy across participating hospitals in federated learning).** Hosseini et al. (2023) showed that standard federated learning (FedSGD) produces highly variable per-hospital accuracy (Var=32.54 on TCGA Kidney), with the model biased toward hospitals contributing more data. Their Prop-FFL reduces this variance by 69% (Var=10.00) by enforcing proportional fairness — hospitals with worse performance contribute more heavily to the loss, ensuring equity across participating sites.

---

## Assembly Instructions — Figure 2

### Final Layout
- Arrange **6 panels** in a **3×2 grid**
- Figure title at top: **"How Fairness Metrics Work — Part 2: Site, Distribution Shift & Deployment Metrics (Panels 8–13)"**
- Panel labels 8–13 in the top-left corner of each panel
- Color legend placed below the grid or in a small inset

### Dimensions
- **3×2 grid**: approximately 22 cm wide × 13 cm tall at 300 DPI
- Each panel: ~5.0 cm × 5.0 cm (chart area) + 1.2 cm (caption)
- Gutters: 0.4 cm horizontal, 0.4 cm vertical between panels

### Color Palette
- Advantaged group: **#1F78B4** (blue)
- Disadvantaged group: **#E66101** (orange)
- After mitigation / improvement: **#33A02C** (green)
- Before mitigation / baseline: **#BABABA** (grey)
- Knowledge gap / missing: **#D55E00** (red)
- Neutral / reference lines: **#999999** (grey)
- Background: **#FFFFFF** (white)

### Color Legend
- 🟦 Blue (#1F78B4) = Advantaged / Reference group
- 🟧 Orange (#E66101) = Disadvantaged group
- 🟩 Green (#33A02C) = After mitigation
- ⬜ Grey (#BABABA) = Before mitigation / Baseline

### Shared Footer
"Data from 78-study systematic review of fairness in histopathology AI (Mondol et al., 2026). See Table 1 for full 15-metric inventory."

### References for Figure Caption
7. Komen et al. (2024). Do Histopathological Foundation Models Eliminate Batch Effects? A Comparative Study.
8. Kheiri et al. (2025). Investigation on potential bias factors in histopathology datasets. *Scientific Reports*.
9. Huang et al. (2025). Knowledge-guided adaptation of pathology foundation models effectively improves cross-domain generalization and demographic fairness. *Nature Communications*, 16, 11485.
10. Lin et al. (2025). Contrastive learning enhances fairness in pathology artificial intelligence systems.
11. Roschewitz et al. (2023). Automatic correction of performance drift under acquisition shift in medical image classification. *Nature Communications*, 14, 7236.
12. Hosseini et al. (2023). Proportionally Fair Hospital Collaborations in Federated Learning of Histopathology Images. *IEEE Transactions on Medical Imaging*, 42(7), 1982–1995.
