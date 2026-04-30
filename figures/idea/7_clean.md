# Figure: Integrated Fairness-Aware Methodology for Histopathology AI

**Panels A–B only** — pipeline and pretraining equation.

---

## Panel A — Methodological Pipeline

```
                        DATA LAYER
┌──────────────────────────────┐    ┌─────────────────────────────────┐
│ Multi-site WSIs              │    │ Paired same-patient slides      │
│ 10+ sites, 4 continents      │    │ Different stain / scanner       │
│                              │    │ + demographic metadata           │
└─────────────┬────────────────┘    └────────────────┬────────────────┘
              │                                      │
              └──────────────────┬───────────────────┘
                                 ▼
                       TRAINING LAYER
┌─────────────────────────────────────────────────────────────────┐
│ 1. Fairness-aware contrastive pretraining                       │
│    Same-patient, different-scanner slides as positive pairs.    │
│    Penalises same-site negatives.                               │
│    → TSS probe accuracy drops from >96% to ~52% (chance).       │
└──────────────────────────────┬──────────────────────────────────┘
                               │ frozen invariant features
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. Causal / counterfactual feature harmonisation                │
│    Site-balanced counterfactual survival modelling.             │
│    → Equalised survival performance across sites.               │
└──────────────────────────────┬──────────────────────────────────┘
                               │ harmonised features
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. Federated fairness-aware fine-tuning                         │
│    Subgroup parity constraints across clients.                  │
│    Privacy-preserving local updates.                            │
│    → Fairness gap reduced ~61%; OOD AUROC improved 6.4–7.2%.    │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. Conditional generative augmentation                          │
│    Synthesises underrepresented subgroups.                      │
│    Fills long-tail intersectional cells.                        │
│    → 48.5% relative improvement via conditional diffusion.      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
                     EVALUATION LAYER
┌─────────────────────────────────────────────────────────────────┐
│ 24-item Reporting Checklist (Blocks A–E)                        │
│                                                                 │
│ A. Tissue provenance    ─ sites, scanners, stains, QC log       │
│ B. Pre-processing audit ─ normaliser, template slide, augment.  │
│ C. Cohort demographics  ─ sample sizes, attribute source,       │
│                           geography, missingness disclosure     │
│ D. Fairness evaluation  ─ subgroup AUROC (ID & OOD),            │
│                           worst-group acc/AUROC, ECE,           │
│                           preserved-site leakage probe,         │
│                           MIL attention fairness summary        │
│ E. Reproducibility      ─ code, model weights, dataset access   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Panel B — Core Pretraining Equation

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

| Symbol | Meaning |
|--------|---------|
| \(\mathbf{z}_i\) | Embedding of WSI \(i\) |
| \(\mathbf{z}_i^+\) | Positive pair: same patient, different scanner/stain |
| \(\tau\) | Temperature parameter |
| \(\lambda\) | Penalty weight for same-site negatives |
| \(\mathbb{1}_{[j \neq i]}\) | Applies penalty only to distinct samples |

**Effect:** Linear-probe TSS accuracy: >96% → ~52% (chance). Diagnostic features preserved.  
Adapted from Lin et al. (2025).
