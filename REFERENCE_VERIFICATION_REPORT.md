# Discussion Chapter Reference Verification Report

**Date**: 2026-04-28  
**File verified**: `chapters/04_discussion.tex`  
**References verified**: 65 citation keys across 64 unique papers (63 from `discussion_reference.json` + 3 extra)  
**Method**: Each claim was checked against the original paper in the verification folder.

---

## Summary

| Verdict | Count |
|---------|-------|
| SUPPORTED / APPROXIMATELY SUPPORTED | 32 |
| PARTIALLY SUPPORTED (minor issues) | 4 |
| CONTRADICTED / INACCURATE | 4 |
| OVERSTATED (range doesn't match) | 1 |
| MISATTRIBUTED (wrong citation) | 1 |
| UNVERIFIABLE (review's own analysis) | ~15 |

---

## CRITICAL ISSUES (must fix)

### 1. **"TSS-prediction AUROC remains above 0.96 after normalization"** — CONTRADICTED
- **Location**: §4.2 (line 69)
- **Paper cited**: `howard2021site`
- **What paper actually says**: After stain normalization, "average OVR AUROC of over **0.850**" — NOT >0.96. The >0.96 figure is the PRE-normalization baseline (range 0.964–0.999).
- **Suggested fix**: Change to "above 0.85" or clarify that this is the baseline before normalization.

### 2. **"3–16% AUROC gaps across 20 cancer types"** — CONTRADICTED (wrong paper context)
- **Location**: §4.2 (line 55)
- **Paper cited**: `vaidya2024demographic`
- **What paper actually says**: Vaidya et al. study only **3 tasks** (breast subtyping, lung subtyping, IDH1 mutation), not 20 cancer types. The "20 cancer types" applies to `lin2025contrastive` (FAIR-Path).
- **Suggested fix**: Change to "across 3 cancer diagnostic tasks" when citing Vaidya, or move the 20-cancer-types claim to the lin2025contrastive citation.

### 3. **"41-percentage-point accuracy differences across racial groups"** — INACCURATE
- **Location**: §4.2 (line 55)
- **Paper cited**: `soltan2024challenges`
- **What paper actually says**: 41% is a **background mortality statistic** (Black vs White breast cancer death rate), NOT an experimental accuracy finding. Actual measured accuracy gaps: ~15pp (ResNet18) and ~33pp (ensemble).
- **Suggested fix**: Replace with "accuracy differences of up to 33 percentage points."

### 4. **vanbooven2025 "improved demographic parity"** — NOT SUPPORTED
- **Location**: §4.4 (line 143)
- **Paper cited**: `vanbooven2025mitigating`
- **What paper actually says**: The paper shows Gleason grading accuracy improvements from synthetic data. It does NOT mention "demographic parity," does NOT evaluate any fairness metric, and does NOT perform stratified subgroup analysis.
- **Suggested fix**: Replace with "improved Gleason grading accuracy via synthetic data augmentation" or similar accurate description.

---

## MODERATE ISSUES (should fix)

### 5. **"48.5% relative fairness improvement"** — MISLEADING
- **Location**: §4.4 (line 143)
- **Paper cited**: `ktena2024generative`
- **What paper actually says**: The paper itself classifies 48.5% as a **relative performance improvement** (diagnostic accuracy), NOT a fairness improvement. The absolute fairness improvement is ±30.0%. The paper explicitly distinguishes between the two.
- **Suggested fix**: Either cite ±30.0% as the fairness improvement, or describe 48.5% as "relative diagnostic performance improvement."

### 6. **"cross-batch AUROC degradation of 0.13–0.44"** — OVERSTATED
- **Location**: §4.2 (line 55)
- **Paper cited**: `lin2025stain`
- **What paper actually found**: Within-method degradation ranges 0.22–0.36. The range 0.13–0.44 is not found in the data.
- **Suggested fix**: Replace with "0.22–0.36."

### 7. **"overall AUROC of 0.98"** — PARTIALLY SUPPORTED
- **Location**: §4.1 (line 14)
- **Paper cited**: `vaidya2024demographic`
- **Issue**: 0.98 is the AUROC for the **White subgroup** on a specific model (UNI-100K), not an "overall" metric across all patients. The overall AUROC was ~0.96.
- **Suggested fix**: Clarify that 0.98 is subgroup-specific or use the correct overall value.

---

## MINOR ISSUES

### 8. **"3.9 years younger" attributed to celi2022sources instead of wang2018tcga**
- **Location**: §4.2 (line 63)
- **Issue**: This statistic originates from `wang2018tcga`. The citation should credit the primary source.
- **Suggested fix**: Change citation to `\citep{wang2018tcga}` or add it alongside celi2022sources.

### 9. **dehkharghanian2023 cited for "AUROC >0.96"**
- **Location**: §4.1 (line 12)
- **Issue**: dehkharghanian2023 reports **accuracy** (70% DenseNet, 86% KimiaNet), not AUROC. The >0.96 AUROC comes only from howard2021site.
- **Suggested fix**: Either remove dehkharghanian2023 from this specific numeric claim or note that it reports accuracy, not AUROC.

### 10. **"underdiagnosis rates exceeding 50%"** — UNVERIFIABLE in text
- **Location**: §4.2 (line 65)
- **Paper cited**: `seyyedkalantari2021underdiagnosis`
- **Issue**: The >50% figure may be in a figure (not extractable from markdown). The paper text confirms intersectional underdiagnosis qualitatively but no explicit >50% threshold was found in the text.

---

## CONFIRMED CORRECT (key claims verified)

| Claim | Paper | Verdict |
|-------|-------|---------|
| Linear probes recover TSS >90% accuracy | komen2024batch | ✓ Exact |
| Site-class AUROC >0.96 on TCGA (pre-normalization) | howard2021site | ✓ Exact (0.964–0.999) |
| ComBat reduces TSS AUROC to chance (~0.5) | murchan2024combat | ✓ Exact |
| FAIR-Path mitigated 88.5–91.1% of disparities across 20 cancer types | lin2025contrastive | ✓ Exact |
| Prop-FFL reduced variance 32.54 → 10.00 | hosseini2023proportionally | ✓ Exact |
| R=0.82 demographic-encoding vs subgroup unfairness | yang2024limits | ✓ Exact |
| 30% false-negative-rate gaps across age groups | yang2024limits | ✓ Exact |
| 3.6% FDA devices reported race/ethnicity, 99.1% no SES data | muralidharan2024fda | ✓ Exact |
| FL melanoma AUROC 0.913 vs centralized 0.905 | haggenmuller2024federated | ✓ Exact (external test set) |
| CORAL/IRM/Group DRO: 22.9-point gap WILDS-CAMELYON17 | koh2021wilds | ✓ Exact (93.2 vs 70.3) |
| TCGA: 8/13 cancer types under-represent Black patients | wang2018tcga | ✓ Exact |
| TCGA: 3.9 years younger than US cancer population | wang2018tcga | ✓ Exact |
| SPARE: improved group accuracy 3.7–5.8% | xu2026spare | ✓ Approximate |
| FLEX: ~61% fairness gap reduction, OOD +6.4–7.2% | huang2025knowledge | ✓ Approximate |
| Center identity: 50% (grayscale) vs 59% (RGB) | kheiri2025investigation | ✓ Exact |
| F1 variation 0.09–0.27 across scanners | aubreville2022mitosis | ✓ Approximate |
| >70% White patients in cohort | soltan2024challenges | ✓ Exact |

---

## CITATION KEY ISSUES

### Keys in discussion but NOT in discussion_reference.json:
1. **`correamedero2024causal`** — Correa-Medero et al., "Causal Debiasing for Unknown Bias in Histopathology" (medRxiv 2024). Paper found and verified. Needs JSON entry.
2. **`shabazian2025joint`** — Shabazian et al., BMC Medical Informatics and Decision Making (2025). Paper found. Needs JSON entry.
3. **`kheiri2024bias`** — This is the SAME paper as `kheiri2025investigation` (Kheiri et al., Scientific Reports 2025). The citation uses wrong year (2024 vs 2025). The JSON entry is `kheiri2025investigation`. The discussion should use `kheiri2025investigation` not `kheiri2024bias`.

---

## PAPERS NOT FOUND (no markdown file available)
- **`euaiact2024`** — EU AI Act legislation. Expected: no academic paper exists. OK.

---

## RECOMMENDED ACTIONS (priority order)

1. **Fix line 69**: "above 0.96 after normalization" → "above 0.85" (TSS-prediction AUROC)
2. **Fix line 55**: "20 cancer types" for Vaidya citation → "3 cancer diagnostic tasks"
3. **Fix line 55**: "41-percentage-point" → "up to 33 percentage points"
4. **Fix line 143**: Remove claim about vanbooven2025 "demographic parity" — paper doesn't evaluate it
5. **Fix line 143**: "48.5% relative fairness improvement" → "48.5% relative performance improvement" (or cite ±30.0% fairness)
6. **Fix line 55**: "0.13–0.44" → "0.22–0.36" (cross-batch AUROC degradation)
7. **Fix line 63**: Change citation from celi2022sources to wang2018tcga for "3.9 years"
8. **Fix line 12**: Consider dropping dehkharghanian2023 from the "AUROC >0.96" claim (it reports accuracy, not AUROC)
9. **Add to JSON**: `correamedero2024causal` and `shabazian2025joint`
10. **Fix citation key**: Change `kheiri2024bias` to `kheiri2025investigation` in discussion
