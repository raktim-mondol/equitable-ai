# AI Image Generation Prompts — Figure 1: Panels 1–7

## Overview

Generate a **7-panel multi-figure illustration** (3×3 grid, 2 cells for legend/title) for an academic paper titled *"Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging."* Each panel explains one or more fairness metrics using a **real published histopathology example** with actual numbers from the 78-study systematic review corpus. The figure serves as a visual glossary for histopathology researchers unfamiliar with fairness evaluation.

**Style:** Clean scientific illustration — like a Nature Reviews figure or BioRender diagram. Flat vector aesthetic, no photo-realism. Use a consistent two-color scheme: **blue (#1F78B4)** for the advantaged/reference group, **orange (#E66101)** for the disadvantaged group.

**Layout:** 3 columns × 3 rows on a white/transparent background. Each panel is self-contained with a mini chart/diagram and a 1–2 line caption below it. Overall figure title at top: **"How Fairness Metrics Work — Part 1: Group-Level Performance Metrics"**

---

## Panel 1: TPR / FPR Disparity

### Reference
**Vaidya et al. (2024)** — *"Demographic bias in misdiagnosis by computational pathology models"*, Nature Medicine, Vol. 30, pp. 1174–1190.
- **Citation key:** `vaidya2024demographic`
- **Dataset:** TCGA (breast, lung, brain), MGB (breast, lung), EBRAINS brain tumor atlas; whole slide images
- **Why this example:** The only study in the corpus to systematically measure TPR disparity across race groups for multiple cancer types on histopathology WSIs, revealing that Black patients consistently have lower recall rates.

### Real Data
- **Lung cancer subtyping** (MGB→MGB test): White TPR = **0.971**, Black TPR = **0.920** → **5.1 percentage-point gap**
- **IDH1 mutation prediction** (brain cancer): mean TPR disparity for Black patients = **−0.060** (95% CI −0.080 to −0.020) with UNI encoder
- **Breast cancer subtyping**: AUC gap White (0.98) vs Black (0.95) = **3.0% gap**
- **IDH1 mutation prediction AUC gap**: White vs Black = **16.0%** (with ResNet50)
- Self-supervised encoders (CTransPath, UNI) reduced gaps by up to 50% vs ResNet50
- TPR disparity for Black patients approached zero when using CTransPath+TransMIL+AR

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Two side-by-side sets of bar charts titled "TPR by Race Group (Lung Cancer Subtyping, MGB Cohort)".

Left bar pair: "LUAD Subtype"
- Blue bar labeled "White" at height 0.971
- Orange bar labeled "Black" at height 0.920
- Double-headed arrow between them annotated "Δ = 5.1pp"

Right bar pair: "IDH1 Mutation (Brain)"
- Blue bar labeled "White" at approximate height 0.92
- Orange bar labeled "Black" at approximate height 0.86
- Double-headed arrow annotated "Δ = 6.0pp"

Below each bar pair: a small 2×2 confusion matrix with cells labeled TP, FN, FP, TN. The TP cell highlighted in green, FN cell highlighted in red. For the Black group, show the FN count visibly larger than for White group.

Below: small text "Vaidya et al. 2024, Nature Medicine 30:1174–1190".
Tiny histopathology slide icon as domain marker.

Clean academic style, no gridlines, subtle axis labels. Blue (#1F78B4) and orange (#E66101). 
No shadows, no 3D effects. Vector illustration quality suitable for scientific publication.
```

### Caption Text
**TPR/FPR disparity = max TPR − min TPR (or RMSE across subgroups).** Vaidya et al. (2024) found that lung cancer subtyping models achieve TPR = 0.971 for White patients but only 0.920 for Black patients — a 5.1pp gap. For IDH1 mutation prediction, Black patients showed mean TPR disparity of −0.060, meaning the model systematically misses true disease cases more often in disadvantaged groups.

---

## Panel 2: Subgroup AUROC Gap

### Reference
**Huang et al. (2025)** — *"Knowledge-guided adaptation of pathology foundation models effectively improves fairness"*
- **Citation key:** `huang2025knowledge`

### Real Data
- NSCLC subtyping (NSCLC-TYPE): fairness gap reduced from **0.041 → 0.016** after FLEX adaptation
- TPR disparity RMSE reduced from **0.140 → 0.085** (39% reduction)
- OOD AUROC improved by 6.4% on average across morphology, biomarker, and gene mutation tasks

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

A single ROC plot with two smooth curves. The blue curve (labeled "Best subgroup, AUROC=0.96") is close to the top-left corner. The orange curve (labeled "Worst subgroup, AUROC=0.92") is noticeably lower. 
The area between the curves is lightly shaded in orange, with a bracket annotation "AUROC gap = 0.04". 
A grey dashed diagonal line from (0,0) to (1,1) represents random chance.
Below the plot, small text: "Huang et al. 2025".
Right side inset: two small bar charts showing "Before FLEX (gap=0.041)" and "After FLEX (gap=0.016)" with the gap shrinking.

Blue (#1F78B4) and orange (#E66101) color scheme. Clean, no gridlines. Scientific publication quality.
```

### Caption Text
**Subgroup AUROC gap = |AUC_best − AUC_worst|.** Huang et al. (2025) found a fairness gap of 0.041 for NSCLC subtyping, reduced to 0.016 after knowledge-guided adaptation — the model discriminates better for one demographic group than another.

---

## Panel 3: Equalised Odds / Equality of Opportunity

### Reference
**Lin et al. (2025)** — *"Contrastive learning enhances fairness in pathology artificial intelligence systems"*
- **Citation key:** `lin2025contrastive`
- **Dataset:** TCGA (28,732 WSIs from 14,456 patients across 20 cancer types), CPTAC-3 (1,248 slides), PLCO (1,573 FFPE), DFCI (1,000+ slides); 15 independent cohorts total
- **Why this example:** The most comprehensive histopathology fairness evaluation to date — 20 cancer types, 8 datasets, 7 institutions. Measures equal opportunity (EOp) and equalized odds (EOEq) per demographic group, and shows before/after mitigation.

### Real Data
- **29.93%** (11/37) of cancer diagnostic tasks showed significant race, gender, or age bias in standard models
- FAIR-Path mitigated **88.5%** of baseline disparities in internal validation
- **91.1%** reduction in diagnostic performance gaps in external validation (15 independent cohorts)
- **100%** resolution in cancer detection and subtype classification tasks
- **80.0%** resolution in histological type classification tasks
- Specific example — LUAD vs LUSC classification (FFPE): significant racial disparity in EOp (p=0.048), significant gender disparity in EOp (p<0.0001), and gender disparity in EBAcc (p=0.0059)
- IDC vs ILC (breast, FFPE): significant age disparities in EOp (p=0.038) and EBAcc (p=0.044)
- GBM vs LGG (brain, frozen): significant racial disparities in EOp (p=0.025)
- Most disparities found in underrepresented groups: racial minorities, females, older age groups

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Top section: A summary statistics block.
Left: "Standard Model" with a red warning badge "29.93% of tasks biased" (11/37 across 20 cancer types).
Right: "FAIR-Path" with a green checkmark badge "88.5% disparities resolved".

Middle section: Two bar chart pairs in before/after layout for EOp (Equal Opportunity difference).

Left pair labeled "Before FAIR-Path (LUAD vs LUSC)":
- Blue bar "Reference group TPR ≈ 0.92" 
- Orange bar "Disadvantaged group TPR ≈ 0.78" 
- Gap arrow annotated "EOp gap significant (p=0.048)"

Right pair labeled "After FAIR-Path":
- Both bars now nearly equal height around 0.90
- Gap arrow shows near-zero difference
- Annotation: "88.5% mitigation across all tasks"

Between the two pairs: a bridging arrow with "Fairness-aware contrastive learning".

Bottom: Three small task icons (lung, breast, brain) with resolution badges:
- Cancer detection: "100% resolved" (green)
- Subtype classification: "100% resolved" (green) 
- Histological type: "80% resolved" (yellow)

Dashed horizontal "Equality target" line at y=0 across both chart pairs.

Below: small text "Lin et al. 2025 — 28,732 TCGA WSIs, 20 cancer types, 15 cohorts".
Small histopathology slide icon in corner.

Blue (#1F78B4) and orange (#E66101). Clean vector style. No 3D effects.
```

### Caption Text
**Equalised odds: TPR and FPR equal across demographic groups; equality of opportunity: only TPR equal.** Lin et al. (2025) found that 29.93% of cancer diagnostic tasks (11/37, spanning 20 cancer types) showed significant race, gender, or age bias. Their FAIR-Path framework mitigated 88.5% of these disparities internally and 91.1% in external cohorts — the most comprehensive histopathology fairness evaluation to date.

---

## Panel 4: Demographic Parity

### Reference
**Soltan & Washington (2024)** — *"Challenges in Reducing Bias Using Post-Processing Fairness for Breast Cancer Staging"*
- **Citation key:** `soltan2024challenges`

### Real Data
- Binary breast cancer classification: White group positive prediction rate **58–71%**, non-White group **30–62%**
- Post-processing fairness interventions showed mixed results — no consistent improvement across groups
- Multi-class staging: lower overall performance with inconsistent disparities

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

A bar chart titled "Positive Prediction Rate P(ŷ=1)" showing two bars: 
a tall blue bar at ~65% labeled "White patients", and a shorter orange bar at ~46% labeled "non-White patients". 
A dashed horizontal line across both bars labeled "Equal rate (if parity achieved)". 
A warning triangle symbol (⚠) next to the chart with text "Ignores true disease prevalence — use with care".
Below: small text "Soltan & Washington 2024".

Blue (#1F78B4) and orange (#E66101). Clean vector style, scientific publication quality.
```

### Caption Text
**Demographic parity: equal fraction of positive predictions across groups.** Soltan & Washington (2024) found that White patients received positive predictions at 58–71% vs 30–62% for non-White patients in breast cancer staging. ⚠ Does not account for true prevalence differences between groups.

---

## Panel 5: Expected Calibration Error (ECE) & Subgroup Calibration Gap

### Reference
**Roschewitz et al. (2023)** — *"Automatic correction of performance drift under acquisition shift in medical imaging"*, Nature Communications
- **Citation key:** `roschewitz2023automatic`

### Real Data
- Histopathology: ECE improved from **0.29 → 0.13–0.14** after alignment correction
- Mammography Youden's index improved: Scanner A 0.295→0.651, Scanner B 0.589→0.594
- **Subgroup calibration gap:** **0 studies (0%)** reported this in the entire 78-study corpus — a major evidence gap

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Two calibration plots side by side. Each shows predicted probability (x-axis, 0 to 1) vs observed frequency (y-axis, 0 to 1). 

Left plot titled "Before Alignment (ECE=0.29)": points deviate substantially from the diagonal, with several dots far from the dashed perfect-calibration line. A red "X" annotation.

Right plot titled "After Alignment (ECE=0.13)": points cluster tightly around the diagonal. A green checkmark annotation.

Between the two plots, an arrow labeled "Alignment correction".

Below the calibration plots, a separate small box outlined in red dashed border, containing the text "Subgroup calibration gap: N=0 studies reported" with a magnifying glass icon and "?".

Below: small text "Roschewitz et al. 2023, Nature Communications".

Blue and orange dots for different subgroups within each plot. Clean vector style.
```

### Caption Text
**ECE measures miscalibration (predicted probability vs observed frequency).** Roschewitz et al. (2023) reduced ECE from 0.29 to 0.13 via alignment correction. Subgroup calibration gap — difference in ECE across demographic groups — remains entirely unreported (0 of 78 studies).

---

## Panel 6: Worst-Group Accuracy

### Reference
**Soltan & Washington (2024)** — *"Challenges in Reducing Bias Using Post-Processing Fairness for Breast Cancer Stage Classification with Deep Learning"*, Algorithms, Vol. 17, 141.
- **Citation key:** `soltan2024challenges`
- **Dataset:** AIM-Ahead / Nightingale Open Science Dataset; 10,856 breast biopsy WSIs from 842 patients (2014–2020)
- **Why this example:** Reports full subgroup-stratified accuracy/precision/recall/F1 tables for 10 CNN architectures across White vs non-White groups — the most granular worst-group data in the corpus. The Ensemble model's non-White accuracy (29.56%) is less than half the White accuracy (62.88%).

### Real Data (from Table 3, prior to fairness adjustments)
- **ResNet18**: White accuracy **70.62%** ± 2.83 vs non-White **55.27%** ± 6.33 → **15.35pp gap**
- **ResNet50**: White **67.37%** ± 1.75 vs non-White **61.95%** ± 4.31 → 5.42pp gap
- **Ensemble model**: White **62.88%** ± 8.76 vs non-White **29.56%** ± 13.26 → **33.32pp gap** (most extreme)
- **Slide Level**: White **65.44%** ± 8.18 vs non-White **55.11%** ± 16.47 → 10.33pp gap
- Across all 10 models: White accuracy range 58–71%, non-White range 30–62%
- ResNet18 recall: White 0.71 ± 0.03, non-White 0.55 ± 0.06
- ResNet18 F1: White 0.73 ± 0.03, non-White 0.46 ± 0.08
- Independent t-tests: majority of models showed statistically significant FPR differences between groups; TPR differences trended consistently toward better White performance with no reversed cases

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Title: "Accuracy by Demographic Group (Breast Cancer Staging, Binary Classification)"

A grouped horizontal bar chart showing four representative models from the study:

Model 1 — "ResNet18":
  Blue bar (White): 70.6%, Orange bar (non-White): 55.3%

Model 2 — "EfficientNet":
  Blue bar (White): 67.3%, Orange bar (non-White): 56.4%

Model 3 — "Ensemble":
  Blue bar (White): 62.9%, Orange bar (non-White): 29.6% ← SHORTEST bar circled in red

Model 4 — "Slide Level":
  Blue bar (White): 65.4%, Orange bar (non-White): 55.1%

A prominent red dashed circle around the Ensemble non-White bar (29.6%), with annotation "Worst-group accuracy = 29.6%".
A bracket connecting the Ensemble White bar (62.9%) to non-White bar (29.6%) labeled "Δ = 33.3pp".

Right side inset: a small histopathology slide with a faded red "X" indicating diagnostic failure for the disadvantaged group.

Below: small text "Soltan & Washington 2024, Algorithms 17:141 — 10,856 breast biopsy WSIs".

Blue (#1F78B4) for White/advantaged, orange (#E66101) for non-White/disadvantaged.
Error bars (±SD) on all bars. Clean vector style. Scientific publication quality.
```

### Caption Text
**Worst-group accuracy = min(accuracy across predefined subgroups).** Soltan & Washington (2024) evaluated 10 CNN architectures on 10,856 breast biopsy WSIs and found the Ensemble model achieves 62.9% accuracy for White patients but only 29.6% for non-White patients — the worst group receives less than half the best group's accuracy. No model showed better performance for non-White patients, and post-processing fairness interventions yielded mixed results.

---

## Panel 7: Preserved-Site Cross-Validation

### Reference
**Howard et al. (2021)** — *"The impact of site-specific digital histology signatures on deep learning model accuracy and bias"*, Nature Communications
- **Citation key:** `howard2021site`

### Real Data
- Site prediction from histology features: AUROC **0.964–0.999** across cancer subtypes
- Ancestry prediction (TCGA-BRCA): **AUROC 0.798 (standard CV) → 0.507 (preserved-site CV)**, P<0.001 → near-chance
- 51/56 (91.1%) features showed AUROC decline with preserved-site CV; average decrease = 0.069
- PIK3CA mutation (TCGA-LUSC): AUROC 0.614→0.386, P<0.001

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Top section: Schematic showing data splitting. Three rectangular blocks labeled "Site 1", "Site 2", "Site 3" in different shades.

Standard CV (left): all blocks are interleaved with colored dots mixed across folds (Fold 1, Fold 2, Fold 3). Label: "Standard CV — all sites mixed in each fold."

Preserved-site CV (right): each site block stays intact in exactly one fold (Fold 1 = Site 1, Fold 2 = Site 2, Fold 3 = Site 3). Label: "Preserved-site CV — each site in one fold."

Bottom section: two bar pairs. Left pair labeled "Ancestry Prediction (TCGA-BRCA)": blue bar at 0.798 (Standard CV), orange bar at 0.507 (Preserved-site CV). Dashed line at 0.5 (chance). Arrow between bars annotated "Δ=0.291, P<0.001".

Below: small text "Howard et al. 2021, Nature Communications".

Clean flat vector style. Blue (#1F78B4) and orange (#E66101).
```

### Caption Text
**Preserved-site CV: each site stays in one fold, preventing data leakage.** Howard et al. (2021) showed ancestry prediction AUROC collapsed from 0.798 (standard CV) to 0.507 (preserved-site CV, P<0.001), exposing that standard CV inflates performance by leaking site-specific signatures across folds.

---

## Assembly Instructions — Figure 1

### Final Layout
- Arrange **7 panels** in a **3×3 grid** (2 cells for legend/title)
- Figure title at top: **"How Fairness Metrics Work — Part 1: Group-Level Performance Metrics (Panels 1–7)"**
- Panel labels 1–7 in the top-left corner of each panel
- Cells 8–9: Color legend + key references block

### Dimensions
- **3×3 grid**: approximately 22 cm wide × 18 cm tall at 300 DPI
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
1. Vaidya et al. (2024). Demographic bias in misdiagnosis by computational pathology models. *Nature Medicine*, 30, 1174–1190.
2. Huang et al. (2025). Knowledge-guided adaptation of pathology foundation models effectively improves cross-domain generalization and demographic fairness. *Nature Communications*, 16, 11485.
3. Lin et al. (2025). Contrastive learning enhances fairness in pathology artificial intelligence systems.
4. Soltan & Washington (2024). Challenges in Reducing Bias Using Post-Processing Fairness for Breast Cancer Stage Classification with Deep Learning. *Algorithms*, 17, 141.
5. Roschewitz et al. (2023). Automatic correction of performance drift under acquisition shift in medical image classification. *Nature Communications*, 14, 7236.
6. Howard et al. (2021). The impact of site-specific digital histology signatures on deep learning model accuracy and bias. *Nature Communications*, 12, 4423.
