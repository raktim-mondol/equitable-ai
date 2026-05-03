# AI Image Generation Prompts — Figure 1: Panels A–G

## Overview

Generate a **7-panel multi-figure illustration** (3×3 grid, 2 cells used for legend/title) for an academic paper titled *"Towards Equitable AI in Pathology: A Systematic Review of Fairness Challenges and Debiasing Methods in Histopathology Imaging."* Each panel explains one fairness metric using a **real published histopathology example** with actual numbers from the 78-study systematic review corpus. The figure serves as a visual glossary for histopathology researchers.

**Figure title:** Centered at top of the grid, 10 pt sans-serif bold, #000000: **How Fairness Metrics Work — Part 1: Group-Level Performance Metrics**

---

## Global Style Specification (ALL panels)

Every panel must obey these rules exactly.

### Geometry
- **Panel canvas:** 7.0 cm wide × 5.5 cm tall (chart area only; caption is separate text, not part of the image)
- **Bounding box:** Tight — trim all excess whitespace around the chart. Panels have no border stroke. Internal margin ≤2 mm from chart elements to canvas edge
- **Panel label:** Bold uppercase letter (A, B, C, …) in 9 pt sans-serif, top-left corner, 2 mm from canvas edges, colour #000000
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
| Reference / advantaged group (bar fill) | Deep teal | **#2C6E7B** |
| Disadvantaged group (bar fill) | Muted crimson | **#C44E52** |
| Success / resolution badge (text & icon only, never bar fill) | Sea green | **#4A9E8E** |
| Section background tint (never bar fill) | Warm stone | **#D4C5C2** |
| Knowledge gap / warning (text & icon only, never bar fill) | Amber | **#E08E45** |
| Neutral reference lines / chance | Cool grey | **#9E9E9E** |
| Emphasis stroke / annotation arrow | Charcoal | **#555555** |
| Background | White | **#FFFFFF** |

**Critical colour rule:** Bar fills always use group-identity colours (deep teal for reference/advantaged, muted crimson for disadvantaged). Never use sea green, warm stone, or amber as bar fills. Before/after mitigation is conveyed through layout, labels, arrows, and annotation text — not through bar colour changes. Section background tints and success/warning badges may use warm stone, sea green, or amber sparingly as non-bar accents.

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
- No legend or colour swatches inside the panel (legend is a separate cell in the grid)
- No emoji, clip-art, decorative elements, or domain icons

---

## Panel A — TPR / FPR Disparity

### Equation
$$\Delta \text{TPR} = \max_g \text{TPR}_g - \min_g \text{TPR}_g$$

### Real Data (from Vaidya et al. 2024, Nature Medicine 30:1174–1190)
- Lung cancer subtyping (MGB→MGB test): White TPR = 0.971, Black TPR = 0.920 → 5.1 pp gap
- IDH1 mutation prediction (brain cancer): mean TPR disparity for Black patients = −0.060 (95% CI −0.080 to −0.020) with UNI encoder
- Breast cancer subtyping AUC gap: White 0.98 vs Black 0.95 = 3.0% gap
- IDH1 mutation prediction AUC gap: White vs Black = 16.0% (with ResNet50)
- Self-supervised encoders (CTransPath, UNI) reduced gaps by up to 50% vs ResNet50

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "A" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "TPR by Race Group (Lung Cancer Subtyping)" — 7 pt sans-serif bold, #333333.

Two side-by-side bar pairs sharing a common y-axis "TPR" (range 0.8–1.0):

LEFT PAIR — "LUAD Subtype" (subtitle 5.5 pt #666666):
- Bar 1: deep teal (#2C6E7B) at height proportional to 0.971, 0.4 pt outline, 85% fill opacity. Label below bar: "White" (5 pt #666666).
- Bar 2: muted crimson (#C44E52) at height proportional to 0.920, 0.4 pt outline, 85% fill opacity. Label below bar: "Black" (5 pt #666666).
- Double-headed vertical arrow between bar tops, 0.6 pt #555555 stroke, annotated "Δ = 5.1 pp" (5 pt #444444).

RIGHT PAIR — "IDH1 Mutation (Brain)" (subtitle 5.5 pt #666666):
- Bar 1: deep teal (#2C6E7B) at height proportional to ~0.92. Label: "White" (5 pt #666666).
- Bar 2: muted crimson (#C44E52) at height proportional to ~0.86. Label: "Black" (5 pt #666666).
- Double-headed vertical arrow annotated "Δ = 6.0 pp" (5 pt #444444).

Below bar pairs: small annotation "Higher TPR = better recall of true disease cases" (4.5 pt #999999, italic).

Equation box at bottom of chart: "ΔTPR = max_g TPR_g − min_g TPR_g" in 6 pt monospace #2C6E7B, pale tint box (#F0F5F5 fill, 1 pt #D0D0D0 border, 2 pt corner radius, 1.5 mm padding).

No reference text. No author names. No border. No icons. Flat vectors only — no gradients, shadows, or 3D effects.
```

### Caption Text (for separate use — NOT rendered on figure)
**TPR/FPR disparity = max TPR − min TPR (or RMSE across subgroups).** Vaidya et al. (2024) found that lung cancer subtyping models achieve TPR = 0.971 for White patients but only 0.920 for Black patients — a 5.1 pp gap. For IDH1 mutation prediction, Black patients showed mean TPR disparity of −0.060, meaning the model systematically misses more true disease cases in disadvantaged groups.

---

## Panel B — Subgroup AUROC Gap

### Equation
$$\text{AUROC Gap} = \left| \max_g \text{AUC}_g - \min_g \text{AUC}_g \right|$$

### Real Data (from Huang et al. 2025, Nature Communications 16:11485)
- NSCLC subtyping (NSCLC-TYPE): fairness gap reduced from 0.041 → 0.016 after FLEX adaptation
- TPR disparity RMSE reduced from 0.140 → 0.085 (39% reduction)
- OOD AUROC improved by 6.4% on average across morphology, biomarker, and gene mutation tasks

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "B" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Subgroup AUROC Gap (NSCLC Subtyping)" — 7 pt sans-serif bold, #333333.

LEFT HALF (~55% width): Single ROC plot (axes ~2.5 cm × 2.5 cm). 
- Deep teal curve (#2C6E7B, 1.0 pt stroke): hugging top-left, labeled "Best subgroup, AUC = 0.96" (5 pt #2C6E7B).
- Muted crimson curve (#C44E52, 1.0 pt stroke): noticeably lower, labeled "Worst subgroup, AUC = 0.92" (5 pt #C44E52).
- Area between curves shaded with #C44E52 at 10% opacity.
- Bracket annotation between curves: "AUROC gap = 0.04" (5 pt #444444).
- Dashed diagonal from (0,0) to (1,1): 0.4 pt #9E9E9E, labeled "Chance" (4 pt #9E9E9E).

RIGHT HALF (~45% width): Before/after gap comparison (two horizontal bars, same colour):
- Label "AUROC Gap" (5.5 pt bold #666666) above.
- Top bar: charcoal (#555555) at width proportional to 0.041, 85% opacity, labeled "Before FLEX" (5 pt #666666).
- Bottom bar: charcoal (#555555) at width proportional to 0.016, 85% opacity, labeled "After FLEX" (5 pt #666666).
- Downward arrow between bars annotated "↓ 61%" (5 pt #4A9E8E, bold).
- Note: both bars use the same charcoal fill; before/after is indicated by labels and the reduction arrow.

Equation box at bottom: "AUROC Gap = | max_g AUC_g − min_g AUC_g |" in 6 pt monospace #2C6E7B, pale tint box (#F0F5F5 fill, 1 pt #D0D0D0 border, 2 pt corner radius, 1.5 mm padding).

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Subgroup AUROC gap = |AUC_best − AUC_worst|.** Huang et al. (2025) found a fairness gap of 0.041 for NSCLC subtyping, reduced to 0.016 after knowledge-guided adaptation — the model discriminates better for one demographic group than another, a gap that can be substantially narrowed with targeted adaptation.

---

## Panel C — Equalised Odds / Equality of Opportunity

### Equation
$$\text{EOp} = \left| \text{TPR}_a - \text{TPR}_b \right| \qquad \text{EOEq} = \max\left( \left|\text{TPR}_a - \text{TPR}_b\right|,\; \left|\text{FPR}_a - \text{FPR}_b\right| \right)$$

### Real Data (from Lin et al. 2025)
- 29.93% (11/37) of cancer diagnostic tasks showed significant race, gender, or age bias in standard models
- FAIR-Path mitigated 88.5% of baseline disparities in internal validation
- 91.1% reduction in diagnostic performance gaps in external validation (15 independent cohorts)
- 100% resolution in cancer detection and subtype classification tasks; 80% in histological type classification
- LUAD vs LUSC (FFPE): significant racial disparity in EOp (p = 0.048), gender disparity in EOp (p < 0.0001)

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "C" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Equalised Odds (EOp / EOEq)" — 7 pt sans-serif bold, #333333.

TOP ROW: Two summary stat blocks (each ~1.8 cm × 0.75 cm, warm stone tint #D4C5C2 at 12%).
- Left block: text "29.93% of tasks biased" + "11/37 across 20 cancer types" (5 pt #555555). Small amber "!" badge (#E08E45, 6 pt bold).
- Right block: text "88.5% disparities resolved" + "91.1% in external validation" (5 pt #555555). Small sea green "✓" badge (#4A9E8E, 6 pt bold).

MIDDLE ROW: Before/after EOp bar pairs for "LUAD vs LUSC (FFPE)" (subtitle 5.5 pt #666666).

LEFT SECTION — "Before FAIR-Path" (label 5 pt bold #555555):
- Deep teal bar (#2C6E7B) at height ~0.92, labeled "Reference TPR" (4.5 pt #666666).
- Muted crimson bar (#C44E52) at height ~0.78, labeled "Disadvantaged TPR" (4.5 pt #666666).
- Vertical gap arrow (0.6 pt #555555) annotated "EOp gap significant (p = 0.048)" in 4.5 pt #C44E52.

RIGHT SECTION — "After FAIR-Path" (label 5 pt bold #555555):
- Deep teal bar (#2C6E7B) at height ~0.90, labeled "Reference TPR" (4.5 pt #666666).
- Muted crimson bar (#C44E52) at height ~0.90, labeled "Disadvantaged TPR" (4.5 pt #666666).
- Both bars now at equal height — gap visually closed.
- Annotation: "EOp gap resolved" (4.5 pt #4A9E8E).

Dashed "Equality" reference line (#9E9E9E, 0.4 pt) spanning across both sections.
Bridge arrow between sections: "Fairness-aware contrastive learning" (5 pt #555555, 0.6 pt).

BOTTOM ROW: Three compact resolution badges (text only):
- "Cancer detection: 100% resolved" (4.5 pt #4A9E8E)
- "Subtype classification: 100% resolved" (4.5 pt #4A9E8E)
- "Histological type: 80% resolved" (4.5 pt #E08E45)

Equation box at bottom: "EOp = |TPR_a − TPR_b|    EOEq = max(|TPR_a−TPR_b|, |FPR_a−FPR_b|)" in 5.5 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Equalised odds: TPR and FPR equal across demographic groups; equality of opportunity: only TPR equal.** Lin et al. (2025) found that 29.93% of cancer diagnostic tasks (11/37, spanning 20 cancer types) showed significant race, gender, or age bias. Their FAIR-Path framework mitigated 88.5% of these disparities internally and 91.1% in external cohorts — the most comprehensive histopathology fairness evaluation to date.

---

## Panel D — Demographic Parity

### Equation
$$\text{DP} = \left| P(\hat{Y}=1 \mid G=a) - P(\hat{Y}=1 \mid G=b) \right|$$

### Real Data (from Soltan & Washington 2024, Algorithms 17:141)
- Binary breast cancer classification: White group positive prediction rate 58–71%, non-White group 30–62%
- Post-processing fairness interventions showed mixed results — no consistent improvement across groups
- Multi-class staging: lower overall performance with inconsistent disparities

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "D" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Demographic Parity (Breast Cancer Staging)" — 7 pt sans-serif bold, #333333.

LEFT (~60% of chart width): Bar chart "Positive Prediction Rate P(ŷ = 1)".
- Deep teal bar (#2C6E7B, 85% opacity): height at ~65%, label "White patients" below (5 pt #666666).
- Muted crimson bar (#C44E52, 85% opacity): height at ~46%, label "Non-White patients" below (5 pt #666666).
- Dashed horizontal line (#9E9E9E, 0.4 pt) spanning both bars at y = 55%, labeled "Equal rate (if parity achieved)" (4.5 pt #9E9E9E).
- Vertical gap bracket between bar tops annotated "Δ = 19 pp" (5 pt #444444).

RIGHT (~40% of chart width): Warning inset box with amber (#E08E45 at 8% opacity) fill, 0.5 pt amber (#E08E45) solid border.
- Amber warning triangle (△, 12 pt, #E08E45).
- Text: "Does not account for true disease prevalence — use with caution" (4.5 pt #555555, 2 lines, centered).

Equation box at bottom: "DP = | P(ŷ=1 | G=a) − P(ŷ=1 | G=b) |" in 6 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Demographic parity: equal fraction of positive predictions across groups.** Soltan & Washington (2024) found that White patients received positive predictions at 58–71% vs 30–62% for non-White patients in breast cancer staging. Important caveat: demographic parity does not account for true prevalence differences between groups and can be satisfied while providing poor care to all groups.

---

## Panel E — Expected Calibration Error (ECE) & Subgroup Calibration Gap

### Equation
$$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n} \left| \text{acc}(B_m) - \text{conf}(B_m) \right| \qquad \text{Subgroup Cal. Gap} = \left| \text{ECE}_a - \text{ECE}_b \right|$$

### Real Data (from Roschewitz et al. 2023, Nature Communications 14:7236)
- Histopathology: ECE improved from 0.29 → 0.13–0.14 after alignment correction
- Mammography Youden's index improved: Scanner A 0.295 → 0.651, Scanner B 0.589 → 0.594
- **Subgroup calibration gap: 0 studies (0%) reported this in the entire 78-study corpus** — a major evidence gap

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "E" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Expected Calibration Error (ECE)" — 7 pt sans-serif bold, #333333.

TOP ROW: Two calibration plots side by side (each ~1.8 cm × 2.0 cm).
X-axis: "Predicted probability" (4.5 pt #999999), range 0–1.
Y-axis: "Observed frequency" (4.5 pt #999999), range 0–1.
Dashed perfect-calibration diagonal in each: 0.4 pt #9E9E9E.

LEFT PLOT — "Before Alignment (ECE = 0.29)":
- Data points as filled circles (radius 2 pt) in charcoal (#555555 at 70% opacity).
- Several points noticeably far from diagonal.
- Small amber "✗" (#E08E45, 7 pt) in top-left corner of plot.

RIGHT PLOT — "After Alignment (ECE = 0.13)":
- Data points as filled circles (radius 2 pt) in charcoal (#555555 at 70% opacity).
- Points clustered tightly around diagonal.
- Small sea green "✓" (#4A9E8E, 7 pt) in top-left corner of plot.
- Note: both plots use the same point colour; improvement is shown by proximity to diagonal.

Arrow between plots: "Alignment correction" (5 pt #555555, 0.6 pt).

BOTTOM ROW: Separate box with amber dashed border (0.5 pt #E08E45), amber tint fill (#E08E45 at 6% opacity).
- Text: "Subgroup calibration gap: 0 of 78 studies reported" (5 pt #C44E52, bold).
- Second line: "Major evidence gap — urgent research need" (4.5 pt #555555).

Equation box at bottom (sits beside the gap box, narrower): "ECE = Σ (|B_m|/n) · |acc(B_m) − conf(B_m)|" in 5 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**ECE measures miscalibration (predicted probability vs observed frequency).** Roschewitz et al. (2023) reduced ECE from 0.29 to 0.13 via unsupervised prediction alignment. Subgroup calibration gap — the difference in ECE across demographic groups — remains entirely unreported in the histopathology fairness literature (0 of 78 studies), representing a critical evidence gap for safe clinical deployment.

---

## Panel F — Worst-Group Accuracy

### Equation
$$\text{WGA} = \min_{g \in \mathcal{G}} \; \text{Accuracy}_g$$

### Real Data (from Soltan & Washington 2024, Algorithms 17:141 — 10,856 breast biopsy WSIs, 842 patients)
- ResNet18: White accuracy 70.62% ± 2.83 vs non-White 55.27% ± 6.33 → 15.35 pp gap
- ResNet50: White 67.37% ± 1.75 vs non-White 61.95% ± 4.31 → 5.42 pp gap
- Ensemble model: White 62.88% ± 8.76 vs non-White 29.56% ± 13.26 → **33.32 pp gap** (most extreme)
- Slide Level: White 65.44% ± 8.18 vs non-White 55.11% ± 16.47 → 10.33 pp gap
- Across all 10 models: White accuracy range 58–71%, non-White range 30–62%

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "F" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Worst-Group Accuracy (Breast Cancer Staging)" — 7 pt sans-serif bold, #333333.

Grouped horizontal bar chart showing 4 models. Each model has two bars side by side: deep teal (#2C6E7B) for "White patients", muted crimson (#C44E52) for "non-White patients". Thin error bars (0.3 pt #9E9E9E, ±SD) on all bars. Consistent colour assignment across all 4 models — never changes.

Model 1 — "ResNet18" (label 5 pt #666666):
  Teal bar at 70.6%, Crimson bar at 55.3% → gap bracket "15.4 pp" (4.5 pt #555555)

Model 2 — "EfficientNet" (label 5 pt #666666):
  Teal bar at 67.3%, Crimson bar at 56.4% → gap bracket "10.9 pp" (4.5 pt #555555)

Model 3 — "Ensemble" (label 5 pt #666666) ← MARKED AS WORST:
  Teal bar at 62.9%, Crimson bar at 29.6%
  The crimson non-White bar is the shortest across all models — encircle it with a charcoal dashed ring (#555555, 0.6 pt stroke, diameter ~0.8 cm).
  Bold annotation with leader line: "Worst-group accuracy = 29.6%" (5 pt #C44E52, bold).
  Gap bracket: "Δ = 33.3 pp" (4.5 pt #C44E52, bold).

Model 4 — "Slide Level" (label 5 pt #666666):
  Teal bar at 65.4%, Crimson bar at 55.1% → gap bracket "10.3 pp" (4.5 pt #555555)

Small annotation bottom-left: "No model showed better performance for non-White patients" (4.5 pt #555555, italic).

Equation box at bottom: "WGA = min_{g ∈ G} Accuracy_g" in 6 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Worst-group accuracy = min(accuracy across predefined subgroups).** Soltan & Washington (2024) evaluated 10 CNN architectures on 10,856 breast biopsy WSIs and found the Ensemble model achieves 62.9% accuracy for White patients but only 29.6% for non-White patients — the worst group receives less than half the best group's accuracy. No model showed better performance for non-White patients; post-processing interventions yielded mixed results.

---

## Panel G — Preserved-Site Cross-Validation

### Equation
$$\text{Site-leakage} = \text{AUROC}_{\text{standard CV}} - \text{AUROC}_{\text{preserved-site CV}}$$

### Real Data (from Howard et al. 2021, Nature Communications 12:4423)
- Site prediction from histology features: AUROC 0.964–0.999 across cancer subtypes
- Ancestry prediction (TCGA-BRCA): AUROC 0.798 (standard CV) → 0.507 (preserved-site CV), P < 0.001 → near-chance
- 51/56 (91.1%) features showed AUROC decline with preserved-site CV; average decrease = 0.069
- PIK3CA mutation (TCGA-LUSC): AUROC 0.614 → 0.386, P < 0.001

### AI Image Generation Prompt

```
Scientific illustration, clean flat vector style, white background. Panel canvas 7.0 cm × 5.5 cm, borderless. Tight bounding box — trim all excess whitespace. Panel label "G" in 9 pt bold sans-serif at top-left corner, 2 mm from edges, colour #000000.

Chart area 6.0 cm × 4.0 cm centered. No gridlines. Axis strokes 0.5 pt #9E9E9E. Tick labels 5 pt #999999.

Title: "Preserved-Site Cross-Validation" — 7 pt sans-serif bold, #333333.

TOP ROW: Data-splitting schematic (two scenarios side by side, each ~2.5 cm wide).

LEFT — "Standard CV" (5 pt bold #555555):
Three rectangular site blocks (Site 1, Site 2, Site 3) in light tint fills (3 shades of warm stone #D4C5C2 at 40%, 25%, 10%). Coloured dots (patients) from each site interleaved across Fold 1, Fold 2, Fold 3 boxes below. Label: "All sites mixed in each fold — data leakage" (4.5 pt #C44E52).

RIGHT — "Preserved-Site CV" (5 pt bold #555555):
Same three site blocks, but each site stays intact in exactly one fold. Fold 1 = only Site 1 dots, Fold 2 = only Site 2 dots, Fold 3 = only Site 3 dots. Label: "Each site in one fold — no leakage" (4.5 pt #4A9E8E).

BOTTOM ROW: Bar chart "Ancestry Prediction (TCGA-BRCA)" — y-axis AUROC 0.0–1.0.
- Deep teal bar (#2C6E7B): height at 0.798, label "Standard CV" below (5 pt #666666).
- Muted crimson bar (#C44E52): height at 0.507, label "Preserved-site CV" below (5 pt #666666).
- Dashed horizontal line at 0.5 (#9E9E9E, 0.4 pt) labeled "Chance" (4.5 pt #9E9E9E).
- Downward arrow between bars annotated "Δ = 0.291, P < 0.001" (5 pt #C44E52, bold).
- Small annotation: "51/56 features declined; avg Δ = 0.069" (4.5 pt #555555).

Equation box at bottom: "Site-leakage = AUROC_standard − AUROC_preserved-site" in 6 pt monospace #2C6E7B, pale tint box.

No reference text. No author names. No border. No icons. Flat vectors only.
```

### Caption Text (for separate use — NOT rendered on figure)
**Preserved-site CV: each site stays in one fold, preventing data leakage.** Howard et al. (2021) showed ancestry prediction AUROC collapsed from 0.798 (standard CV) to 0.507 (preserved-site CV, P < 0.001) — exposing that standard CV inflates performance by leaking site-specific digital histology signatures across folds, a finding confirmed across 91.1% of extracted features.

---

## Assembly Instructions — Figure 1

### Final Layout
- Arrange **7 panels (A–G)** in a **3 × 3 grid** — cells (1,1) through (3,3)
- **Cell (1,1):** Title block + colour legend
- **Cells (1,2), (1,3):** Panels A, B
- **Cells (2,1), (2,2), (2,3):** Panels C, D, E
- **Cells (3,1), (3,2):** Panels F, G
- **Cell (3,3):** Key takeaways / "Part 1 → Part 2" bridge text (optional)
- Each panel is borderless; the grid arrangement provides visual separation via gutters

### Dimensions
- **Full grid:** exactly 22.0 cm wide × 18.0 cm tall at 300 DPI (2598 × 2126 px)
- **Each panel cell:** 7.0 cm wide × 5.5 cm tall
- **Gutters:** 0.3 cm horizontal, 0.3 cm vertical between panels
- **Grid margins:** 0.5 cm top, 0.5 cm bottom, 0.5 cm left, 0.5 cm right
- **Bounding box:** Crop exactly to grid margins — zero whitespace beyond the outermost panel edges

### Colour Legend (cell 1,1 — separate from panels, not rendered inside any panel image)
- Deep teal (#2C6E7B) = Reference / advantaged group
- Muted crimson (#C44E52) = Disadvantaged group
- Charcoal (#555555) = Metric value (before/after comparisons)
- Amber (#E08E45) = Knowledge gap / caution
- Sea green (#4A9E8E) = Improvement / resolution (text and badges only)

### Shared Footer (below grid, not inside any panel)
"Data from 78-study systematic review of fairness in histopathology AI. See Table 1 for the full 15-metric inventory and reporting frequency."

### References (for figure caption — NOT on figure)
1. Vaidya et al. (2024). Demographic bias in misdiagnosis by computational pathology models. *Nature Medicine*, 30, 1174–1190.
2. Huang et al. (2025). Knowledge-guided adaptation of pathology foundation models effectively improves cross-domain generalization and demographic fairness. *Nature Communications*, 16, 11485.
3. Lin et al. (2025). Contrastive learning enhances fairness in pathology artificial intelligence systems.
4. Soltan & Washington (2024). Challenges in Reducing Bias Using Post-Processing Fairness for Breast Cancer Stage Classification with Deep Learning. *Algorithms*, 17, 141.
5. Roschewitz et al. (2023). Automatic correction of performance drift under acquisition shift in medical image classification. *Nature Communications*, 14, 7236.
6. Howard et al. (2021). The impact of site-specific digital histology signatures on deep learning model accuracy and bias. *Nature Communications*, 12, 4423.
