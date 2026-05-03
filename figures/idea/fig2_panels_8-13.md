# AI Image Generation Prompts — Figure 2: Panels H–M

## Overview

Generate a **6-panel multi-figure illustration** (3×2 grid) for an academic paper titled *"Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging."* Each panel explains one fairness metric using a **real published histopathology example** with actual numbers from the 78-study systematic review corpus. The figure serves as a visual glossary for histopathology researchers.

**Figure title (top):** **"How Fairness Metrics Work — Part 2: Site, Distribution Shift & Deployment Metrics"**

---

## Global Style Specification (ALL panels)

Every panel must obey these rules exactly. These are **identical** to Figure 1 — the two figures form a matched pair.

### Geometry
- **Panel canvas:** 7.0 cm wide × 5.5 cm tall (chart area only; caption is separate text, not part of the image)
- **Bounding box:** Tight — trim all excess whitespace around the chart. Panels have no border stroke. Internal margin ≤2 mm from chart elements to canvas edge
- **Panel label:** Bold uppercase letter (H, I, J, K, L, M) in 9 pt sans-serif, top-left corner, 2 mm from canvas edges, colour #000000
- **Chart area:** Centered within the canvas, 6.0 cm × 4.0 cm, axes drawn with 0.5 pt #9E9E9E strokes, no gridlines

### Typography
- **Panel title:** 7 pt sans-serif bold, #333333, centered above chart
- **Axis labels:** 5.5 pt sans-serif, #666666
- **Tick labels:** 5 pt sans-serif, #999999
- **Data labels / annotations:** 5 pt sans-serif, #444444
- **Equation text:** 6 pt monospace (#2C6E7B), placed in a pale tint box (#F0F5F5, 1 pt #D0D0D0 border, 2 pt corner radius) at bottom of chart area, 1.5 mm padding
- **Caption (outside panel):** NOT included in the image — supplied separately as text

### Colour Palette

| Role | Colour | Hex |
|------|--------|-----|
| Reference / advantaged / clean setup (bar fill) | Deep teal | **#2C6E7B** |
| Disadvantaged / confounded / OOD failure (bar fill) | Muted crimson | **#C44E52** |
| Success / improvement (text & icon only, never bar fill) | Sea green | **#4A9E8E** |
| Section background tint (never bar fill) | Warm stone | **#D4C5C2** |
| Knowledge gap / warning (text & icon only, never bar fill) | Amber | **#E08E45** |
| Neutral reference lines / chance | Cool grey | **#9E9E9E** |
| Emphasis stroke / annotation arrow | Charcoal | **#555555** |
| Background | White | **#FFFFFF** |

**Critical colour rule:** Bar fills always use group-identity colours (deep teal for reference/advantaged/large-data, muted crimson for disadvantaged/confounded/small-data). Never use sea green, warm stone, or amber as bar fills. Before/after mitigation is conveyed through layout, labels, arrows, and annotation text — not through bar colour changes. Section background tints and success/warning badges may use warm stone, sea green, or amber sparingly as non-bar accents.

### Visual Style
- **Flat vector aesthetic** — no gradients, no 3D extrusions, no drop shadows, no photo-realistic textures
- **Stroke width:** All bar outlines 0.4 pt, all connector lines 0.6 pt, all emphasis strokes 1.0 pt
- **Fill opacity:** Bars at 85% opacity for a professional printed look
- **Markers:** Small filled circles (radius 2 pt) for data points on scatter/calibration plots
- **No icons, no watermarks, no domain markers** on any panel

### What NOT to include on any panel
- No panel border stroke — panels are borderless
- No author names, journal names, year, or citation keys
- No reference text of any kind
- No "Data from…" or "See Table…" footnotes
- No legend or colour swatches inside the panel (legend is a separate strip below the grid)
- No emoji, clip-art, decorative elements, or domain icons

---

## Panel H — In-Distribution vs Out-of-Distribution (OOD) Gap

### Equation
$$\text{OOD Gap} = \text{AUROC}_{\text{ID}} - \text{AUROC}_{\text{OOD}} \qquad \text{or} \qquad \text{Acc}_{\text{ID}} - \text{Acc}_{\text{OOD}}$$

### Real Data (from Komen et al. 2024 — TCGA-LUSC-5, CAMELYON16)
- Tissue source site (TSS) prediction accuracy from features: >90% on TCGA-LUSC-5, ~100% on CAMELYON16 — via linear probing
- Cancer classification when TSS ⟂ label (uncorrelated): >90% accuracy
- Cancer classification when TSS ~ label (correlated): collapses to <20–50% — dramatic OOD failure
- Stain normalization (Reinhard, Macenko): TSS prediction reduced but linear probe accuracies remained >80% (TCGA-LUSC-5) and >97% (CAMELYON16)
- Foundation models do NOT eliminate batch effects; site signatures dominate distances in feature space
- Corroborating: WILDS-CAMELYON17 benchmark shows 22.9 pp ID–OOD accuracy gap; CORAL, IRM, and Group DRO all leave this gap largely unresolved on histopathology data

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "H" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #2C6E7B.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "ID vs OOD Gap (Site Confounding)" — 7 pt sans-serif bold, #333333.

TOP ROW: Two scenario schematics side by side (each ~2.6 cm wide).

LEFT SCENARIO — "TSS ⟂ Label (Uncorrelated)" (5 pt bold #555555):
- Two site blocks: Site A (deep teal tint #2C6E7B at 12%), Site B (muted crimson tint #C44E52 at 12%), each ~1.0 cm × 1.0 cm.
- Disease labels (+ and −) evenly mixed across both sites (small balanced +/- markers).
- Arrow below pointing to a deep teal bar (#2C6E7B) at height proportional to ~92%, width 1.0 cm.
- Label: "Classification ≈ 92% — learns disease, not site" (4.5 pt #4A9E8E).

RIGHT SCENARIO — "TSS ~ Label (Correlated)" (5 pt bold #555555):
- Site A (deep teal tint): mostly + disease labels.
- Site B (muted crimson tint): mostly − disease labels.
- Arrow below pointing to a muted crimson bar (#C44E52) at height proportional to ~35%, width 1.0 cm.
- Label: "Classification ≈ 35% — exploits site as shortcut" (4.5 pt #C44E52).

Bridge arrow between scenarios: "When site predicts label → OOD collapse" (5 pt #555555, 0.6 pt stroke).

BOTTOM ROW: Small bar chart "Site Prediction Accuracy from Features".
- Deep teal bar (#2C6E7B) at >90%, label "TCGA-LUSC-5" (4.5 pt #666666).
- Muted crimson bar (#C44E52) at ~100%, label "CAMELYON16" (4.5 pt #666666).
- Annotation: "Features encode site near-perfectly even in foundation models" (4.5 pt #555555).

Equation box at bottom: "OOD Gap = Acc_ID − Acc_OOD" in 6 pt monospace #2C6E7B, pale tint box (#F0F5F5 fill, 1 pt #D0D0D0 border, 2 pt corner radius, 1.5 mm padding).

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**ID vs OOD evaluation exposes site-confounded shortcuts.** Komen et al. (2024) showed that histopathology foundation model features encode tissue source site with >90–100% accuracy via linear probing. When site correlates with disease label, cancer classification collapses from >90% to <20–50% under distribution shift — demonstrating that even state-of-the-art models fail OOD when batch effects are not controlled.

---

## Panel I — Bias Proxy Metrics (Site Classification, Mutual Information)

### Equation
$$\text{MI}(X; Y) = \sum_{x \in X} \sum_{y \in Y} P(x,y) \log \frac{P(x,y)}{P(x)P(y)} \qquad \text{Site-Classifiability} = \max_f \text{Acc}(f(\text{features}) \to \text{site})$$

### Real Data (from Kheiri et al. 2025, Scientific Reports)
- KimiaNet feature extractor: Cancer-type classification 99%, but Data center classification 96% simultaneously — features encode site identity almost as strongly as disease
- Mutual information MI(label, center) = 1.47 for TCGA — strong cancer-site dependency
- With co-slice exclusion: Cancer-Acc drops to 48%, Center-Acc remains 60%
- Fair subset (balanced LUAD/LUSC): Cancer-Acc 79%, Center-Acc 66%
- EfficientNet consistently: Cancer-Acc 83%, Center-Acc 68% across all settings

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "I" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #2C6E7B.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Bias Proxy: Site-Classifiability & MI" — 7 pt sans-serif bold, #333333.

LEFT HALF: Simplified neural probe diagram.
- Input box: "Histopathology Patch" (4.5 pt #555555, 0.5 pt #9E9E9E border, ~1.0 cm × 0.5 cm).
- Arrow down to feature extractor box: "CNN Feature Extractor" (5 pt #555555, 0.5 pt #2C6E7B border, #2C6E7B at 6% fill, ~1.5 cm × 0.6 cm).
- Two output arrows from extractor, splitting to:
  - TOP HEAD: "Cancer Classifier" box → accuracy "99%" in sea green (#4A9E8E, 7 pt bold).
  - BOTTOM HEAD: "Site Probe" box → accuracy "96%" in amber (#E08E45, 7 pt bold), with amber "!" beside it (10 pt bold).
- Annotation below diagram: "If a linear probe achieves 96% site accuracy, features encode batch effects almost as strongly as disease." (4 pt #555555, 2 lines, italic).

RIGHT HALF: Bar chart "Mutual Information (TCGA)".
- Deep teal bar (#2C6E7B, 85% opacity): MI(cancer type, site) = 1.47, labeled "Label–Site dependency" (4.5 pt #666666).
- Muted crimson bar (#C44E52, 85% opacity): MI(features, site) comparably high, labeled "Feature–Site dependency" (4.5 pt #666666).
- Annotation: "High MI → strong confounding" (4.5 pt #C44E52).

Equation box at bottom: "MI(X;Y) = Σ Σ P(x,y) log[P(x,y) / P(x)P(y)]" in 5.5 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Bias proxy: site-classification accuracy from learned features and mutual information.** Kheiri et al. (2025) showed that a linear probe on KimiaNet features achieves 96% accuracy at identifying which hospital a slide came from — nearly matching cancer classification accuracy (99%). High site-classifiability indicates features are confounded by batch effects rather than encoding pure disease signal. Mutual information MI(label, center) = 1.47 quantifies this dependency directly.

---

## Panel J — TPR Disparity RMSE (Multi-Subgroup Disparity Summary)

### Equation
$$\text{TPR-RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \text{TPR}_i - \overline{\text{TPR}} \right)^2}$$

### Real Data (from Huang et al. 2025, Nature Communications 16:11485 — TCGA, 16 clinical tasks)
- C-UAD-EGFR task: TPR disparity RMSE reduced from 0.140 → 0.085 (39% reduction) by FLEX
- C-BRCA-TYPE task: FLEX yields significantly tighter and more equitable performance curves across race groups
- RMSE summarises per-group TPR deviations from the mean into a single number — lower = fairer
- Unlike simple max−min TPR gap, RMSE detects when multiple subgroups are disadvantaged, not just the worst one
- Statistical significance: NSCLC-CTE P = 0.018, BRCA-PR P = 0.048, CRCA-CTLA4 P = 0.004, CLUAD-EGFR P = 0.004

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "J" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #2C6E7B.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "TPR Disparity RMSE (C-UAD-EGFR)" — 7 pt sans-serif bold, #333333.

TOP: Schematic showing 4 subgroups (Race A, B, C, D) each with a TPR bar at different heights. A dashed population-mean reference line (#9E9E9E, 0.4 pt) runs horizontally. Small deviation arrows (0.4 pt #9E9E9E) from each bar to the mean line. Bars use deep teal (#2C6E7B) for subgroups at/above mean, muted crimson (#C44E52) for subgroups below mean. Annotation: "RMSE captures deviations across ALL subgroups, not just max−min gap" (4.5 pt #555555).

MIDDLE ROW: Before/after comparison (two sections, each ~2.5 cm wide, separated by a bridge arrow).

LEFT SECTION — "Before FLEX" (label 5 pt bold #555555, warm stone tint #D4C5C2 at 8% background):
- 4 TPR bars at heights ~0.82, 0.88, 0.91, 0.96 with wide spread.
  Bars at/above mean: deep teal (#2C6E7B). Bars below mean: muted crimson (#C44E52).
- Annotation below: "TPR disparity RMSE = 0.140" (5 pt #C44E52, bold).

RIGHT SECTION — "After FLEX" (label 5 pt bold #555555, warm stone tint #D4C5C2 at 8% background):
- Same 4 bars now tightly clustered at heights ~0.88, 0.90, 0.91, 0.93.
  Bars still use deep teal (#2C6E7B) for groups at/above mean, muted crimson (#C44E52) for groups below mean.
  The reduction in spread is visually obvious — bars are tightly grouped.
- Annotation below: "TPR disparity RMSE = 0.085 (↓ 39%)" (5 pt #4A9E8E, bold).

Bridge arrow between sections: "Knowledge-guided adaptation (FLEX)" (5 pt #555555, 0.6 pt stroke).

BOTTOM: Small annotation: "Significant improvements: NSCLC-CTE P=0.018, BRCA-PR P=0.048, CRCA-CTLA4 P=0.004, CLUAD-EGFR P=0.004" (4 pt #555555).

Equation box at bottom: "TPR-RMSE = √(1/n · Σ(TPR_i − TPR_mean)²)" in 6 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**TPR disparity RMSE = root-mean-square of per-subgroup TPR deviations from the mean.** Unlike simple max−min TPR gap, RMSE captures disparities across ALL subgroups simultaneously — penalising when multiple groups are disadvantaged. Huang et al. (2025) reduced TPR disparity RMSE from 0.140 to 0.085 (39% reduction) in the C-UAD-EGFR task using FLEX, demonstrating that knowledge-guided adaptation tightens per-group recall uniformly.

---

## Panel K — Equal Balanced Accuracy (EBAcc) & AUROC Difference (AUROCDiff)

### Equation
$$\text{EBAcc} = \left| \text{BalAcc}_a - \text{BalAcc}_b \right| \qquad \text{AUROCDiff} = \left| \text{AUC}_a - \text{AUC}_b \right| \qquad \text{BalAcc} = \frac{\text{TPR} + \text{TNR}}{2}$$

### Real Data (from Lin et al. 2025 — TCGA: 28,732 WSIs, 14,456 patients, 20 cancer types)
- EBAcc: FAIR-Path resolved disparities in 100% of cancer detection and subtype classification tasks, 80% in histological type classification
- AUROCDiff: Significant AUC differences between demographic groups present in 29.93% (11/37) of tasks before mitigation
- FAIR-Path achieved 88.5% mitigation of EBAcc/AUROCDiff disparities in internal validation
- 91.1% reduction in external validation across 15 independent cohorts
- IDC vs ILC (breast, FFPE): significant age disparities in EBAcc (p = 0.044)
- GBM vs LGG (brain, frozen): significant racial disparities in EOp (p = 0.025)

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "K" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #2C6E7B.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "EBAcc & AUROCDiff" — 7 pt sans-serif bold, #333333.

Two metric sub-panels side by side (equal width, ~2.8 cm each).

LEFT SUB-PANEL — "Equal Balanced Accuracy (EBAcc)" (6 pt bold #333333):
Before/after bar pairs, shared y-axis:
  - TOP ROW ("Before" — 5 pt bold #555555):
    Deep teal bar (#2C6E7B) at height ~0.88, labeled "Reference" (4 pt #666666).
    Muted crimson bar (#C44E52) at height ~0.81, labeled "Disadvantaged" (4 pt #666666).
    Gap bracket annotated "EBAcc gap" (4.5 pt #C44E52).
  - BOTTOM ROW ("After FAIR-Path" — 5 pt bold #555555):
    Deep teal bar (#2C6E7B) at height ~0.88, labeled "Reference" (4 pt #666666).
    Muted crimson bar (#C44E52) at height ~0.88, labeled "Disadvantaged" (4 pt #666666).
    Both bars now equal height — gap visually closed.
    Annotation: "Gap closed" (4.5 pt #4A9E8E).
  Mini badge below: "100% resolved — detection & subtyping" (4 pt #4A9E8E).

RIGHT SUB-PANEL — "AUC Difference (AUROCDiff)" (6 pt bold #333333):
Two small overlaid ROC curves (axes ~1.5 cm × 1.5 cm):
  - Deep teal curve (#2C6E7B, 0.8 pt): AUC = 0.91.
  - Muted crimson curve (#C44E52, 0.8 pt): AUC = 0.84.
  - Shaded region between curves (#C44E52 at 8% opacity), annotated "AUROCDiff = 0.07" (4.5 pt #555555).
  - Dashed diagonal (#9E9E9E, 0.3 pt).
  Mini text: "After FAIR-Path → near zero" (4 pt #4A9E8E).

BOTTOM: Summary stat — "29.93% (11/37) tasks affected — 88.5% mitigated internally, 91.1% in external cohorts" (4.5 pt #555555, centered, 2 lines).

Equation box at bottom (compact, spans full width): "EBAcc = |BalAcc_a − BalAcc_b|    AUROCDiff = |AUC_a − AUC_b|    BalAcc = (TPR+TNR)/2" in 5 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**EBAcc = |BalAcc_groupA − BalAcc_groupB|; AUROCDiff = |AUC_groupA − AUC_groupB|.** Lin et al. (2025) showed that 29.93% of diagnostic tasks exhibited significant EBAcc or AUROCDiff disparities across race, gender, and age. FAIR-Path resolved 100% of these in cancer detection/subtyping and 88.5% overall — demonstrating that balanced accuracy and AUROC gaps are correctable without sacrificing overall performance.

---

## Panel L — Youden's Index (Threshold Sensitivity Under Distribution Shift)

### Equation
$$J = \text{TPR} + \text{TNR} - 1 = \max_t \left( \text{sensitivity}(t) + \text{specificity}(t) - 1 \right)$$

### Real Data (from Roschewitz et al. 2023, Nature Communications 14:7236 — OPTIMAM + WILDS Camelyon17)
- Mammography (breast screening) — before vs after UPA alignment:
  - Scanner A: J = 0.295 → 0.651 (2.2× improvement)
  - Scanner B: J = 0.589 → 0.594 (maintained)
  - Scanner D: J = 0.644 → 0.640 (maintained)
- Histopathology (Camelyon17, tissue classification):
  - Site S4: J = 0.868 → 0.864 (preserved near ceiling)
  - Site S5: J = 0.859 → 0.863 (preserved near ceiling)
- ROC-AUC preserved across all domains (mammography 0.85–0.93, histopathology 0.97–0.98)
- UPA requires only ~250 unlabelled cases (1,000 images) from the new domain for alignment
- ECE preserved after alignment (0.13 → 0.14 vs 0.29 before) — calibration transfers with Youden's Index

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "L" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #2C6E7B.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Youden's Index Under Distribution Shift" — 7 pt sans-serif bold, #333333.

TOP LEFT: Conceptual ROC diagram (axes ~1.5 cm × 1.5 cm).
- ROC curve (#2C6E7B, 0.8 pt stroke) from (0,0) to (1,1), convex toward top-left.
- Dashed diagonal (#9E9E9E, 0.3 pt).
- Point P marked on curve shoulder with filled charcoal dot (#555555, radius 2.5 pt).
- Perpendicular dashed line from P to diagonal, annotated "J = TPR + TNR − 1" (4.5 pt #555555).
- Label: "J = distance from diagonal to curve shoulder" (4 pt #666666).

TOP RIGHT: Small formula card — "J = max_t [sensitivity(t) + specificity(t) − 1]" (5 pt monospace #2C6E7B, pale tint box).

BOTTOM (main chart area, ~4.5 cm wide): Grouped bar chart "Youden's Index Before vs After UPA Alignment".

Each scanner/site has two bars side by side: both use charcoal (#555555 at 85% opacity) since these are the same metric (Youden's J) for the same scanner, just at different times. "Before UPA" bars have a subtle hatch pattern overlay or are simply labeled; "After UPA" bars are the same charcoal fill without hatch. Distinction is via labels and arrows.

GROUP 1 — "Breast Screening (Mammography)" (subtitle 5 pt bold #666666):
  Scanner A: Before 0.295, After 0.651 — dramatic improvement. Upward arrow annotated "2.2×" (4.5 pt #4A9E8E, bold).
  Scanner B: Before 0.589, After 0.594 — nearly unchanged, annotation "maintained" (4 pt #9E9E9E).
  Scanner D: Before 0.644, After 0.640 — nearly unchanged, annotation "maintained" (4 pt #9E9E9E).

GROUP 2 — "Histopathology (Camelyon17)" (subtitle 5 pt bold #666666):
  Site S4: Before 0.868, After 0.864 — preserved near ceiling.
  Site S5: Before 0.859, After 0.863 — preserved near ceiling.

Dashed horizontal reference line at J = 1.0 (#9E9E9E, 0.3 pt) labeled "Perfect classifier" (4 pt #9E9E9E).

Annotation: "UPA preserves clinical operating point without labelled data from new domain" (4 pt #555555, italic).

Equation box at bottom: "J = TPR + TNR − 1" in 6 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Youden's Index J = TPR + TNR − 1; supports threshold choice under distribution shift.** Roschewitz et al. (2023) demonstrated that when a model is deployed to a new scanner or hospital site, the clinical operating point (where sensitivity ≈ specificity) can drift substantially — Scanner A's J collapsed from 0.651 to 0.295. Their unsupervised prediction alignment (UPA) restored the operating point using only ~250 unlabelled cases, preserving both Youden's Index and calibration (ECE 0.13) across domains.

---

## Panel M — Inter-Hospital Performance Variance (Federated Learning Equity)

### Equation
$$\text{Var}_{\text{hosp}} = \frac{1}{K} \sum_{k=1}^{K} \left( \text{Acc}_k - \overline{\text{Acc}} \right)^2 \qquad \text{Prop-FFL: } \min_{\theta} \prod_{k=1}^{K} \mathcal{L}_k(\theta)$$

### Real Data (from Hosseini et al. 2023, IEEE Trans Med Imaging 42(7):1982–1995)
- TCGA Kidney (4 hospitals, 642,277 patches):
  - Hospital accuracies: 78.84%, 77.12%, 76.21%, 84.36%
  - Prop-FFL variance = 10.00 vs FedSGD variance = 32.54 → **69% variance reduction**
  - q-FedSGD variance = 11.22 (Prop-FFL still better by 11%)
- TCGA Lung (6 hospitals, 303,053 patches):
  - Hospital accuracies: 72.23%, 76.81%, 74.57%, 74.60%, 76.44%, **60.81%** (worst)
  - Prop-FFL variance = 29.84 vs FedSGD variance = 40.13 → **26% variance reduction**
- Prop-FFL objective: maximise the product of relative training losses across hospitals, encouraging uniform convergence
- Standard FedSGD/FedAvg minimises average loss, allowing the model to be biased toward hospitals with larger datasets

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "M" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #2C6E7B.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Inter-Hospital Variance (Federated Learning)" — 7 pt sans-serif bold, #333333.

TOP ROW: Federated learning schematic.
- Central server icon (circle, 0.8 cm diameter, #2C6E7B stroke 0.5 pt, white fill) in center.
- 4 hospital icons (small rounded rectangles, each ~0.6 cm × 0.5 cm): H1 (large dataset), H2 (medium), H3 (medium), H4 (small — scarce data). Arranged around the server.
- Upward arrows (model updates, 0.4 pt #9E9E9E) from hospitals to server.
- Downward arrows (aggregated model, 0.4 pt #2C6E7B) from server to hospitals.
- Label: "Federated Learning — hospitals share model updates, not data" (4 pt #555555).

BOTTOM ROW: Side-by-side bar chart comparison "TCGA Kidney (4 hospitals)" (5 pt bold #666666).

Consistent colour rule: deep teal (#2C6E7B) for hospitals with large/medium datasets, muted crimson (#C44E52) for the worst-performing or smallest-data hospital. Same colour assignment in both FedSGD and Prop-FFL sections.

LEFT — "Standard FedSGD — Minimises Average Loss" (4.5 pt bold #555555):
- H1: deep teal bar at height ~85% (large-data hospital)
- H2: deep teal bar at height ~75%
- H3: deep teal bar at height ~82%
- H4: muted crimson bar (#C44E52) at height ~68%, noticeably shortest
- Large-data hospitals (H1, H3) get taller bars — bias toward data-rich sites.
- Annotation below: "Var = 32.54 — large spread" (5 pt #C44E52, bold).

RIGHT — "Prop-FFL — Minimises Performance Variance" (4.5 pt bold #555555):
- H1: deep teal bar at height ~79%
- H2: deep teal bar at height ~77%
- H3: deep teal bar at height ~76%
- H4: muted crimson bar (#C44E52) at height ~84%, now tallest — small-data hospital better served
- All bars tightly grouped — equity achieved. Same colours as left panel; improvement is visible from the H4 bar now being tall rather than short.
- Annotation below: "Var = 10.00 — 69% reduction" (5 pt #4A9E8E, bold).

Bridge arrow between left and right: "Prop-FFL: hospitals with worse performance contribute more to loss" (4.5 pt #555555, 0.6 pt stroke).

Equation box at bottom: "Var_hosp = (1/K)·Σ(Acc_k − Acc_mean)²    Prop-FFL: min_θ Π L_k(θ)" in 5 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Inter-hospital variance = Var(accuracy across participating hospitals in federated learning).** Hosseini et al. (2023) showed that standard federated learning (FedSGD) produces highly variable per-hospital accuracy (Var = 32.54 on TCGA Kidney), with the model biased toward hospitals contributing more data. Their Prop-FFL reduces this variance by 69% (Var = 10.00) by enforcing proportional fairness — hospitals with worse performance contribute more heavily to the loss, ensuring equity across participating sites.

---

## Assembly Instructions — Figure 2

### Final Layout
- Arrange **6 panels (H–M)** in a **3 × 2 grid**
- **Row 1:** Panels H, I, J
- **Row 2:** Panels K, L, M
- Colour legend: placed in a narrow horizontal strip below the grid (0.8 cm tall, full grid width)
- Each panel is borderless; the grid arrangement provides visual separation via gutters

### Dimensions
- **Full grid:** exactly 22.0 cm wide × 13.0 cm tall at 300 DPI (2598 × 1535 px)
- **Each panel cell:** 7.0 cm wide × 5.5 cm tall
- **Gutters:** 0.3 cm horizontal, 0.3 cm vertical between panels
- **Grid margins:** 0.5 cm top, 0.5 cm bottom, 0.5 cm left, 0.5 cm right
- **Bounding box:** Crop exactly to grid margins + legend strip — zero whitespace beyond the outermost panel edges

### Colour Legend (below grid — separate from panels, not rendered inside any panel image)
- Deep teal (#2C6E7B) = Reference / advantaged / large-data / clean setup
- Muted crimson (#C44E52) = Disadvantaged / confounded / OOD failure / small-data
- Charcoal (#555555) = Metric value (before/after comparisons)
- Amber (#E08E45) = Knowledge gap / caution / warning
- Sea green (#4A9E8E) = Improvement / resolution (text and badges only)

### Shared Footer (below legend strip, not inside any panel)
"Data from 78-study systematic review of fairness in histopathology AI. See Table 1 for the full 15-metric inventory and reporting frequency."

### Cross-Reference Note
Figure 1 (Panels A–G) covers group-level performance metrics (TPR/FPR disparity, AUROC gap, equalised odds, demographic parity, ECE, worst-group accuracy, preserved-site CV). Figure 2 (Panels H–M) covers site-level, distribution-shift, and deployment metrics. The two figures together form a complete 13-metric visual glossary. Captions should reference individual panels by letter (e.g., "Panel A shows…"; "Compare Panels C and K for…").

### References (for figure caption — NOT on figure)
7. Komen et al. (2024). Do Histopathological Foundation Models Eliminate Batch Effects? A Comparative Study.
8. Kheiri et al. (2025). Investigation on potential bias factors in histopathology datasets. *Scientific Reports*.
9. Huang et al. (2025). Knowledge-guided adaptation of pathology foundation models effectively improves cross-domain generalization and demographic fairness. *Nature Communications*, 16, 11485.
10. Lin et al. (2025). Contrastive learning enhances fairness in pathology artificial intelligence systems.
11. Roschewitz et al. (2023). Automatic correction of performance drift under acquisition shift in medical image classification. *Nature Communications*, 14, 7236.
12. Hosseini et al. (2023). Proportionally Fair Hospital Collaborations in Federated Learning of Histopathology Images. *IEEE Transactions on Medical Imaging*, 42(7), 1982–1995.
