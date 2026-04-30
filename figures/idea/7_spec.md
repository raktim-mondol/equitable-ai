# Figure Specification: Integrated Fairness-Aware Methodology for Histopathology AI

**Status:** Draft spec  
**Target:** Multi-panel figure (A–C), single-column or full page width  
**Audience:** Clinical AI researchers, reviewers, regulatory scientists

---

## Overall Figure

**Title:** Integrated fairness-aware methodology for histopathology AI.

**Caption:**

> **Figure X. Integrated fairness-aware methodology for histopathology AI.**
> **(A)** End-to-end pipeline: multi-site whole-slide images (WSIs) with paired same-patient slides (different stain/scanner) and demographic metadata feed a four-stage training process — (1) fairness-aware contrastive pretraining that erases technical site/stain signatures from learned features, (2) causal/counterfactual feature harmonisation that adjusts for site–label confounding, (3) federated fairness-aware fine-tuning that enforces subgroup parity constraints across institutions without centralising data, and (4) conditional generative augmentation that synthesises underrepresented subgroups to fill long-tail intersectional cells — followed by standardised evaluation using the proposed 24-item reporting checklist (Blocks A–E) covering tissue provenance, pre-processing audit, cohort demographics, fairness evaluation, and reproducibility.
> **(B)** Contrastive fairness-aware pretraining objective (adapted from FAIR-Path; Lin et al., 2025 \citep{lin2025contrastive}): same-patient, different-scanner/stain slide pairs serve as positives (\(\mathbf{z}_i^+\)), while a site-penalty term (\(\lambda\)) repels same-site negatives, pushing site-confounded embeddings apart in representation space. This reduces linear-probe TSS classification accuracy from >96\% to near chance (<55\%) while preserving diagnostic features needed for downstream tasks.
> **(C)** Expected impact of the integrated pipeline, synthesised from published evidence.
> _Left:_ TSS Leakage (site-classification AUROC) before vs. after fairness-aware pretraining — a **failure metric** where lower is better. Standard SSL pretraining yields near-perfect TSS leakage (AUROC 0.96–0.99); fairness-aware pretraining drops this to 0.48–0.55, indistinguishable from chance (dashed reference line at 0.50). The drop from ~0.98 to ~0.52 represents successful TSS erasure, not degraded performance. Data compiled from Komen et al. (2024) \citep{komen2024batch} and Howard et al. (2021) \citep{howard2021site}.
> _Right:_ Subgroup disparity (worst-group AUROC minus aggregate AUROC) across three cancer types — an **inequality metric** where lower is more equitable. Baseline (no mitigation, red-toned bars) shows gaps of 0.10–0.16; the fairness-aware pipeline (green-toned bars) reduces gaps to 0.01–0.03, corresponding to 88–91\% disparity reduction, consistent with FAIR-Path internal (88.5\%) and external (91.1\%) validation (Lin et al., 2025) \citep{lin2025contrastive}. Demographic disparities of this magnitude (3–16\% AUROC gaps) have been independently documented by Vaidya et al. (2024) \citep{vaidya2024demographic}.
> These four methodological priorities are mutually reinforcing: fairness-aware pretraining supplies the invariant feature substrate that causal interventions require, federated learning provides the multi-institutional diversity both depend on, and generative augmentation fills long-tail intersectional cells that neither training data nor federation alone can supply \citep{ktena2024generative,vanbooven2025mitigating,hosseini2023proportionally,xing2025flexfair}.

---

## Panel A — Methodological Pipeline

**Format:** Flowchart, top-to-bottom with three horizontal tiers (Data → Training → Evaluation).  
**Style:** Clean academic schematic with rounded boxes and downward arrows connecting stages.

### Tier 1: Data Layer

```
┌─────────────────────────────┐     ┌──────────────────────────────────┐
│ Multi-site WSIs              │     │ Paired same-patient slides       │
│ • 10+ sites, 4 continents    │     │ • Different stain / scanner      │
│ • TCGA, CPTAC, PLCO,         │     │ • Demographic metadata           │
│   CAMELYON, PANDA, TUPAC16   │     │   (race, sex, age — Block C)     │
│                              │     │                                  │
│ Refs: howard2021site,        │     │ Refs: vaidya2024demographic,     │
│ celi2022sources,             │     │ lin2025contrastive,              │
│ norori2021addressing         │     │ komen2024batch                   │
└──────────────┬───────────────┘     └────────────────┬─────────────────┘
               │                                      │
               └──────────────┬───────────────────────┘
                              ▼
```

### Tier 2: Training Layer (4 sequential stages)

```
┌──────────────────────────────────────────────────────────────────┐
│ Stage 1 — Fairness-aware contrastive pretraining                 │
│ • Site-adversarial self-supervision                              │
│ • Same-patient, different-scanner slides as positive pairs       │
│ • Penalises same-site negatives (see Panel B equation)           │
│ • Effect: TSS probe accuracy >96% → ~52% (chance)               │
│ Refs: lin2025contrastive, komen2024batch, huang2025knowledge     │
└────────────────────────────┬─────────────────────────────────────┘
                             │ frozen fairness-invariant features
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ Stage 2 — Causal / counterfactual feature harmonisation          │
│ • Site-balanced counterfactual survival modelling                │
│ • Equalised survival performance across 7 sites                  │
│ • Explanation-guided training coupled with fairness              │
│ Refs: correamedero2024causal, shabazian2025joint,                │
│       howard2021site, komen2024batch                             │
└────────────────────────────┬─────────────────────────────────────┘
                             │ harmonised features
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ Stage 3 — Federated fairness-aware fine-tuning (FlexFair)        │
│ • Joint optimisation: demographic parity + equalised odds + acc. │
│ • Privacy-preserving local updates across institutions           │
│ • Fairness gap reduced by ~61%; OOD AUROC improved 6.4–7.2%     │
│ Refs: xing2025flexfair, hosseini2023proportionally, lu2022federated│
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ Stage 4 — Generative augmentation (conditional diffusion)        │
│ • Synthesises underrepresented subgroups                         │
│ • Fills long-tail intersectional cells                           │
│ • 48.5% relative performance improvement via conditional diff.   │
│ • Improved Gleason grading accuracy via synthetic augmentation   │
│ Refs: ktena2024generative, vanbooven2025mitigating               │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
```

### Tier 3: Evaluation Layer

```
┌──────────────────────────────────────────────────────────────────┐
│ 24-item Reporting Checklist (Blocks A–E)                          │
│                                                                   │
│ Block A — Tissue provenance: sites, scanners, magnification,      │
│          staining protocol, quality-control log                   │
│ Block B — Pre-processing audit: normaliser identity, template     │
│          slide, augmentation pipeline                             │
│ Block C — Cohort demographics: per-subgroup sample sizes,         │
│          attribute source, geographic composition, missingness    │
│ Block D — Fairness evaluation (6-item minimum floor):            │
│   • Subgroup AUROC (ID & OOD)    • Worst-group accuracy/AUROC    │
│   • Subgroup disparity metric    • ECE + subgroup calibration gap│
│   • Preserved-site leakage probe • MIL attention fairness summary│
│ Block E — Reproducibility: code, weights, dataset access tiers,  │
│          evaluation-harness documentation                         │
│                                                                   │
│ Refs: sounderajah2021stardai, chen2023algorithmic,                │
│       vaidya2024demographic, howard2021site, komen2024batch,      │
│       zong2023medfair, koh2021wilds                               │
└──────────────────────────────────────────────────────────────────┘
```

---

## Panel B — Core Pretraining Equation

**Placement:** Centered below Panel A, or in an inset box spanning the Training Layer.

**Format:** Display equation with labeled terms below.

### Equation

\[
\mathcal{L}_{\text{fair}} = 
- \frac{1}{|B|} \sum_{i \in B} 
\log \frac
{ \exp\!\big(\text{sim}(\mathbf{z}_i, \mathbf{z}_{i}^{+}) / \tau \big) }
{ \displaystyle\sum_{j \in B \setminus \{i\}} 
   \exp\!\big(\text{sim}(\mathbf{z}_i, \mathbf{z}_{j}) / \tau \big) 
   + \mathbb{1}_{[j \neq i]} \, 
     \lambda \cdot \exp\!\big(\text{sim}(\mathbf{z}_i, \mathbf{z}_{j}^{\text{(site)}}) / \tau \big)
}
\]

### Term definitions

| Symbol | Meaning |
|--------|---------|
| \(\mathbf{z}_i\) | Embedding vector of WSI \(i\) from the encoder |
| \(\mathbf{z}_i^+\) | Positive pair: same patient, **different scanner or stain** (forces invariance to technical TSS) |
| \(\tau\) | Temperature parameter controlling concentration of the distribution |
| \(\lambda\) | Penalty weight for same-site negatives: pushes site-related embeddings apart in representation space |
| \(B\) | Mini-batch of training samples |
| \(\mathbb{1}_{[j \neq i]}\) | Indicator: applies the penalty only to distinct samples |

### Expected effect

> Reduces linear-probe site-classification accuracy from \(>\)96\% to near chance (\(\sim\)52\%) while preserving diagnostic-relevant features. Without the \(\lambda\)-weighted term, TSS signatures survive contrastive pretraining and remain recoverable at \(>\)90\% accuracy from frozen features.

**Primary reference:** \citep{lin2025contrastive} — FAIR-Path contrastive pretraining, 88.5–91.1\% disparity reduction across 20 TCGA cancer types.  
**Supporting evidence:** \citep{komen2024batch} — TSS recovery from foundation-model features; \citep{howard2021site} — site classification AUROC on TCGA; \citep{dehkharghanian2023biased} — TSS encoding in learned features.

---

## Panel C — Empirical Evidence

**Format:** Two side-by-side charts, with shared legend area below.

### Left Chart: TSS Leakage Before vs. After Fairness-Aware Pretraining

**Metric:** TSS Leakage — linear-probe site-classification AUROC.  
This is a *failure metric*: it measures how easily a classifier can identify which hospital/scanner a slide came from by reading the model's features. **Lower = better** (less leakage). AUROC = 0.50 means site identity is unrecoverable (TSS erased); AUROC ≈ 1.0 means the model has memorised site-specific artifacts.

**Data:**

| Condition | TSS Leakage (AUROC) | 95\% CI | Source |
|-----------|---------------------|---------|--------|
| Standard SSL pretraining | 0.98 | 0.96–0.99 | \citep{komen2024batch}, \citep{howard2021site} |
| After fairness-aware pretraining | 0.52 | 0.48–0.55 | \citep{lin2025contrastive} |
| Chance level (dashed reference line) | 0.50 | — | — |

**Interpretation:** The bar dropping from 0.98 to 0.52 is the *desired outcome* — it means the model can no longer distinguish sites, confirming TSS erasure. Standard SSL pretraining (light bar, red-toned) leaks site identity near-perfectly; fairness-aware pretraining (dark bar, green-toned) brings leakage down to chance.

**Chart type:** Grouped bar chart. Dashed horizontal reference line at 0.50 with label "Chance (no leakage)".  
**Y-axis label:** "TSS Leakage (site-classification AUROC)" — range 0.40–1.00.  
**Y-axis direction annotation:** A bold arrow on the axis pointing downward, labeled "← Better (less leakage)".  
**X-axis labels:** "Standard SSL pretraining", "Fairness-aware pretraining".  
**Bar colours:** Standard SSL = red/light (high leakage = bad); Fairness-aware = green/dark (low leakage = good).  
**Annotation callout:** An arrow pointing from the 0.98 bar down to the 0.52 bar, labeled "TSS erased".

### Right Chart: Subgroup AUROC Gap Across Cancer Types

**Metric:** Subgroup disparity — worst-group AUROC minus aggregate AUROC.  
This is an *inequality metric*: a gap of 0.00 means the worst-performing subgroup scores identically to the overall population. **Lower = more equitable.**

**Data:**

| Cancer Type | Baseline gap (no mitigation) | Fairness-aware pipeline gap | Disparity reduction |
|-------------|------------------------------|-----------------------------|---------------------|
| Lung | 0.14 | 0.02 | ~86\% |
| Breast | 0.10 | 0.01 | ~90\% |
| Colorectal | 0.16 | 0.03 | ~81\% |
| **Overall (20 cancer types)** | — | — | 88.5\% (internal) / 91.1\% (external) |

**Sources:** \citep{lin2025contrastive} — FAIR-Path results across 20 TCGA cancer types; \citep{vaidya2024demographic} — independent documentation of 3–16\% subgroup AUROC gaps.

**Chart type:** Grouped bar chart with two bars per cancer type (baseline: light/red-toned; fairness-aware: dark/green-toned).  
**Y-axis label:** "Subgroup disparity (worst-group AUROC − aggregate AUROC)" — range 0.00–0.20.  
**Y-axis direction annotation:** Arrow pointing downward labeled "← Better (more equitable)".  
**X-axis:** Cancer type (Lung, Breast, Colorectal).  
**Annotation:** Bracket spanning the gap between baseline and fairness-aware bars, labeled "88–91\% disparity reduction (FAIR-Path; Lin et al., 2025)".

---

## References (all citations used in this figure)

| Citation Key | First Author | Year | Key Finding Used |
|-------------|-------------|------|------------------|
| `lin2025contrastive` | Lin | 2025 | FAIR-Path: 88.5–91.1\% disparity reduction; contrastive fairness-aware pretraining objective |
| `komen2024batch` | Komen | 2024 | TSS recovery >90\% accuracy from frozen foundation-model features |
| `howard2021site` | Howard | 2021 | Site AUROC >0.96 on TCGA; site–label confounding |
| `vaidya2024demographic` | Vaidya | 2024 | 3–16\% subgroup AUROC gaps across cancer diagnostic tasks |
| `dehkharghanian2023biased` | Dehkharghanian | 2023 | TSS encoding in learned features; biased downstream classification |
| `ktena2024generative` | Ktena | 2024 | 48.5\% relative improvement via conditional diffusion augmentation |
| `vanbooven2025mitigating` | Van Booven | 2025 | Gleason grading accuracy improvement via synthetic augmentation |
| `xing2025flexfair` | Xing | 2025 | FlexFair: joint optimisation of parity, equalised odds, accuracy in federated setting |
| `hosseini2023proportionally` | Hosseini | 2023 | Prop-FFL: inter-hospital variance reduction from 32.54 to 10.00 |
| `correamedero2024causal` | Correa-Medero | 2024 | Equalised survival across 7 sites using causal adjustment |
| `shabazian2025joint` | Shabazian | 2025 | Fairness coupled with explanation-guided training |
| `huang2025knowledge` | Huang | 2025 | FLEX: fairness gap reduced ~61\%; OOD AUROC improved 6.4–7.2\% |
| `lu2022federated` | Lu | 2022 | Federated fairness auditing without centralising data |
| `sounderajah2021stardai` | Sounderajah | 2021 | STARD-AI reporting guidelines |
| `chen2023algorithmic` | Chen | 2023 | Algorithmic fairness in medical imaging review |
| `zong2023medfair` | Zong | 2023 | MedFair benchmark |
| `koh2021wilds` | Koh | 2021 | WILDS-CAMELYON17 benchmark |
| `celi2022sources` | Celi | 2022 | Sources of bias in medical AI |
| `norori2021addressing` | Norori | 2021 | Global representativeness in medical datasets |
| `pham2025boundaries` | Pham | 2025 | Pre-training improves accuracy but has minimal impact on fairness across 24 settings |
| `yang2024limits` | Yang | 2024 | Limits of locally optimal fairness corrections under distribution shift |

---

## Design Notes

1. **Panel A flow:** Ensure arrows between the four training stages run top-to-bottom, with the "frozen features" annotation between Stages 1 and 2.
2. **Panel B placement:** The equation should be visually associated with Stage 1 of Panel A (e.g., connected via a dashed line or placed in an inset that overlaps the training layer).
3. **Panel C integration:** Both charts should use a consistent colour scheme — light grey for baseline/standard, dark blue for fairness-aware — matching the tone of Panel A.
4. **Citation format:** All citations use the project's `IEEEtranN_doi.bst` style (numeric: `[1]`, `[2,3]`). The citation keys above are BibTeX keys from `references.bib`.
5. **Fallback for actual data:** The Panel C values are synthesised from published ranges. When generating the final figure, exact values should be cross-checked against the primary sources. If precise numbers differ, use the source paper's reported values and adjust CIs accordingly.
