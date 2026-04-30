# AI Image Generation Prompts: 9-Panel Fairness Metrics Figure

## Overview

Generate a **3×3 grid illustration** for an academic paper titled *"Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging."* Each of the 9 panels explains one fairness metric using a **real published example** with actual numbers from the literature. The figure serves as a visual glossary for histopathology researchers unfamiliar with fairness evaluation.

**Style:** Clean scientific illustration style — like a Nature Reviews figure or BioRender diagram. Flat vector aesthetic, no photo-realism. Use a consistent two-color scheme: **blue (#1F78B4)** for the advantaged/reference group, **orange (#E66101)** for the disadvantaged group.

**Layout:** 3 columns × 3 rows on a white/transparent background. Each panel is self-contained with a mini chart/diagram and a 1–2 line caption below it. Overall figure title at top: **"How Fairness Metrics Work — A Visual Guide with Real Examples from Histopathology AI"**

---

## Panel 1: TPR / FPR Disparity

### Reference
**Vaidya et al. (2024)** — *"Demographic bias in misdiagnosis by computational pathology models"*, Nature Medicine.
- **Citation key:** `vaidya2024demographic`

### Real Data
- Breast cancer subtyping: White patients AUROC ≈ 0.98 vs Black patients AUROC ≈ 0.95 → **3.0% gap**
- IDH1 mutation prediction (brain cancer): White vs Black AUROC gap = **16.0%**
- TPR disparity: model correctly flags disease less often for Black patients

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Two side-by-side vertical bar charts titled "TPR by Group (Breast Subtyping)". 
Left chart shows one tall blue bar at 0.98 labeled "White", right chart shows a shorter orange bar at 0.95 labeled "Black". 
A double-headed arrow between the two bars annotated "Δ = 3% gap". 
Below the charts, small text: "Vaidya et al. 2024, Nature Medicine". 
Below that: a small 2x2 confusion matrix for each group showing TP, FN, FP, TN counts with TP highlighted.

Clean academic style, no gridlines, subtle axis labels. Blue (#1F78B4) and orange (#E66101) color scheme. 
No shadows, no 3D effects. Vector illustration quality suitable for scientific publication.
```

### Caption Text
**TPR/FPR disparity = max TPR − min TPR.** In Vaidya et al. (2024), breast cancer subtyping shows a 3% TPR gap between White (0.98) and Black (0.95) patients; IDH1 mutation prediction shows a 16% gap — the model systematically misses disease more often in disadvantaged groups.

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
- **Dataset:** TCGA (28,732 WSIs from 14,456 patients across 20 cancer types), CPTAC-3, PLCO, DFCI
- **Why this example:** Uses real histopathology WSIs to measure fairness across race, gender, and age groups — the only study in the corpus to systematically evaluate equalised odds across 20 cancer types on pathology images.

### Real Data
- **88.5%** of baseline disparities mitigated in internal validation across 20 cancer types
- **91.1%** reduction in diagnostic performance gaps in external validation (15 independent cohorts)
- **100%** resolution in cancer detection and subtype classification tasks
- Standard deep learning models showed significant demographic biases (race, gender, age) affecting **29.93%** of cancer diagnostic tasks
- No significant AUROC drop in most tasks after fairness intervention

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Left side: Two bar chart pairs showing "Before FAIR-Path" and "After FAIR-Path" for Equal Opportunity Difference.
Before: a tall blue bar (reference group TPR ~0.92) and a shorter orange bar (disadvantaged group TPR ~0.78), with a gap arrow annotated "EOp gap". 
After: both bars nearly equal height around 0.90, gap nearly closed. Arrow between the pairs labeled "88.5% reduction".

Right side: A small grid of organ icons (lung, breast, colon, kidney, brain) with checkmarks indicating "100% resolution in cancer detection and subtype classification".

A dashed horizontal "Equality target" line across both chart pairs at y=0 difference.

Below: small text "Lin et al. 2025 — TCGA 28,732 WSIs, 20 cancer types".
Small histopathology slide icon in corner as domain marker.

Blue (#1F78B4) and orange (#E66101). Clean vector style. No 3D effects.
```

### Caption Text
**Equalised odds: TPR and FPR equal across demographic groups.** Lin et al. (2025) applied fairness-aware contrastive learning (FAIR-Path) to 28,732 TCGA WSIs across 20 cancer types, mitigating 88.5% of baseline diagnostic disparities internally and 91.1% in external cohorts — the most comprehensive histopathology-specific fairness evaluation to date.

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
**Soltan & Washington (2024)** — *"Challenges in Reducing Bias Using Post-Processing Fairness for Breast Cancer Stage Classification with Deep Learning"*
- **Citation key:** `soltan2024challenges`
- **Dataset:** AIM-Ahead / Nightingale Open Science Dataset; 10,856 breast biopsy WSIs from 842 patients
- **Why this example:** Directly measures group-stratified accuracy on histopathology slides, revealing that the worst-performing demographic group (non-White patients) receives substantially lower accuracy — a clear demonstration of worst-group accuracy as an equity metric.

### Real Data
- Binary breast cancer staging: **White patients 58–71% accuracy** vs **non-White patients 30–62% accuracy** across models
- Worst-group (non-White at lower bound): just **30%** accuracy — less than half the best-group performance
- Post-processing fairness interventions showed mixed results with no consistent improvement across groups
- Multi-class staging: lower overall performance with inconsistent disparities between groups

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

A horizontal bar chart titled "Accuracy by Demographic Group (Breast Cancer Staging)".

Four bars showing a stark gradient:
1. "White, age <60" — blue bar at 71%
2. "White, age 60+" — blue bar at 65%
3. "non-White, age <60" — orange bar at 62%  
4. "non-White, age 60+" — orange bar at 30% (shortest, circled in red)

A prominent red dashed circle around the shortest bar (30%), with annotation "Worst-group accuracy = 30%".
A bracket connecting the highest bar (71%) to the lowest (30%) labeled "41pp gap".

Right side: inset showing a breast biopsy histopathology slide with a faded/red "X" overlay on the disadvantaged group side, indicating the model fails more often for these patients.

Below: small text "Soltan & Washington 2024 — 10,856 breast biopsy WSIs".

Blue (#1F78B4) for advantaged subgroups, orange (#E66101) for disadvantaged subgroups. 
Clean vector style. Scientific publication quality.
```

### Caption Text
**Worst-group accuracy = min(accuracy across predefined subgroups).** Soltan & Washington (2024) found that breast cancer staging models achieve 58–71% accuracy for White patients but only 30–62% for non-White patients — the worst group receives less than half the best group's accuracy. This metric directly quantifies equity of service in histopathology AI.

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

## Panel 8: In-Distribution vs Out-of-Distribution (OOD) Gap

### Reference
**Ly et al. (2024)** — *"Shortcut learning in medical AI hinders generalization: method for estimating AI model performance without external validation"*
- **Citation key:** `ly2024shortcut`

### Real Data
- COVID-19 detection (Kaggle→International): source AUROC **0.99**, external AUROC **0.64** → **Δ = 0.36 (36pp drop)**
- MIMIC-CXR → CheXpert: source 0.85, external 0.73 → Δ = 0.12
- Average across 10 benchmarks: source 0.87, external 0.68 → **20% overestimation** without calibration
- DABIS estimate (calibrated): 0.73 vs actual: 0.68 (underestimates by only 4%)

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background, single panel 8cm x 6cm.

Two paired bar groups showing dramatic performance drop.

Left pair labeled "COVID-19 Detection":
- Blue bar at 0.99 labeled "In-distribution (Kaggle)"
- Orange bar at 0.64 labeled "OOD (International hospitals)"
- Arrow between them annotated "Δ = 36 percentage points"

Right pair labeled "Chest X-ray Classification":
- Blue bar at 0.85 labeled "In-distribution (MIMIC-CXR)"
- Orange bar at 0.73 labeled "OOD (CheXpert)"
- Arrow between them annotated "Δ = 12 percentage points"

Below the bars, small schematic showing two microscope slides with different staining patterns to suggest domain shift.

Below: small text "Ly et al. 2024".

Clean vector style. Blue (#1F78B4) for ID, orange (#E66101) for OOD. A red downward arrow emphasizing the performance drop.
```

### Caption Text
**ID vs OOD evaluation separates seen from unseen hospitals/scanners.** Ly et al. (2024) found a 36-percentage-point gap between in-distribution (AUROC 0.99) and external validation (AUROC 0.64) for COVID-19 detection — shortcut learning inflates ID performance, while OOD evaluation reveals true generalisation.

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

## Global Figure Assembly Instructions

### Final Layout
- Arrange the 9 panels in a 3×3 grid
- Add a figure title at the top: **"How Fairness Metrics Work — A Visual Guide with Real Examples from Histopathology AI"**
- Add panel labels (a)–(i) or 1–9 in the top-left corner of each panel
- Add a small color legend at the bottom: 🟦 Blue = Advantaged/Reference group | 🟧 Orange = Disadvantaged group
- Include a single footer: "Data from 78-study systematic review of fairness in histopathology AI (Mondol et al., 2026). See Table 1 for full metric inventory."

### Dimensions
- Total figure: approximately 18 cm wide × 22 cm tall at 300 DPI
- Each panel: ~5.5 cm × 5.5 cm (chart area) + 1.5 cm (caption)
- Gutters: 0.4 cm horizontal, 0.5 cm vertical between panels

### Color Palette
- Advantaged group: **#1F78B4** (blue)
- Disadvantaged group: **#E66101** (orange)
- After mitigation / improvement: **#33A02C** (green)
- Knowledge gap / missing: **#D55E00** (red)
- Neutral / reference lines: **#999999** (grey)
- Background: **#FFFFFF** (white)

### References to Include in Figure Caption

1. Vaidya et al. (2024). Demographic bias in misdiagnosis by computational pathology models. *Nature Medicine*. `vaidya2024demographic`
2. Huang et al. (2025). Knowledge-guided adaptation of pathology foundation models effectively improves fairness. `huang2025knowledge`
3. Shabazian et al. (2025). Joint optimization of accuracy and fairness. *BMC Medical Informatics and Decision Making*. `shabazian2025joint`
4. Soltan & Washington (2024). Challenges in Reducing Bias Using Post-Processing Fairness for Breast Cancer Staging. `soltan2024challenges`
5. Roschewitz et al. (2023). Automatic correction of performance drift under acquisition shift in medical imaging. *Nature Communications*. `roschewitz2023automatic`
6. Xu et al. (2026). Rethinking fairness in medical imaging: Maximizing group-specific performance with SPARE. `xu2026spare`
7. Howard et al. (2021). The impact of site-specific digital histology signatures on deep learning model accuracy and bias. *Nature Communications*. `howard2021site`
8. Ly et al. (2024). Shortcut learning in medical AI hinders generalization. `ly2024shortcut`
9. Kheiri et al. (2025). Investigation on potential bias factors in histopathology datasets. `kheiri2025investigation`
