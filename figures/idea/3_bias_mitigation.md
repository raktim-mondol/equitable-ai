# Sankey Data: Bias Category → Mitigation Family

## Left Nodes: 8 Bias Categories (with study count)

| Code | Bias Category | n Studies |
|------|--------------|-----------|
| DB | Demographic Bias | 5 |
| RB | Representation Bias | 7 |
| CB | Confounding Bias | 6 |
| SB | Selection / Sampling Bias | 8 |
| LB | Class / Label Bias | 7 |
| IB | Institutional / Batch Bias | 7 |
| TB | Technical / Domain Shift Bias | 8 |
| AB | Algorithmic Bias | 5 |

## Right Nodes: 16 Mitigation Families (two-digit codes)

| Code | Mitigation Family |
|------|------------------|
| SN | Conventional Stain Normalization |
| DA | Data Augmentation |
| DC | Dataset Curation |
| RS | Resampling |
| CH | ComBat Harmonisation |
| DO | Domain Adaptation |
| AD | Adversarial Debiasing |
| SL | SSL / Foundation Models |
| FL | Federated Learning |
| SD | Synthetic Data / DDPM |
| FW | Fairness-aware Learning |
| TO | Threshold Optimisation |
| UC | Uncertainty Calibration |
| CM | Causal Methods |
| EC | Explanation Constraints |
| CL | Continual Learning |

## Flow Matrix: Bias → Mitigation (n = number of study-mitigation links)

```
Bias    SN  DA  DC  RS  CH  DO  AD  SL  FL  SD  FW  TO  UC  CM  EC  CL   TOTAL
DB       0   0   1   0   0   0   1   1   0   1   3   1   0   0   1   1     10
RB       0   0   3   0   0   0   0   1   1   2   0   0   0   0   0   0      7
CB       0   0   3   0   1   0   1   0   0   0   1   0   0   0   0   0      6
SB       0   0   4   1   0   0   0   1   2   1   0   0   0   0   0   0      9
LB       0   0   1   2   0   1   0   0   0   0   0   0   1   0   2   0      7
IB       0   0   2   0   2   1   1   1   1   0   0   0   0   0   0   0      8
TB       3   2   0   0   0   2   1   1   0   0   0   0   1   0   0   0     10
AB       0   0   1   0   0   0   0   0   0   0   2   1   1   0   1   1      7
```
## Sankey JSON

```json
{
  "nodes": [
    {"id": "DB", "group": "bias", "label": "Demographic Bias", "n": 5},
    {"id": "RB", "group": "bias", "label": "Representation Bias", "n": 7},
    {"id": "CB", "group": "bias", "label": "Confounding Bias", "n": 6},
    {"id": "SB", "group": "bias", "label": "Selection / Sampling Bias", "n": 8},
    {"id": "LB", "group": "bias", "label": "Class / Label Bias", "n": 7},
    {"id": "IB", "group": "bias", "label": "Institutional / Batch Bias", "n": 7},
    {"id": "TB", "group": "bias", "label": "Technical / Domain Shift Bias", "n": 8},
    {"id": "AB", "group": "bias", "label": "Algorithmic Bias", "n": 5},
    {"id": "SN", "group": "mitigation", "label": "Stain Normalization"},
    {"id": "DA", "group": "mitigation", "label": "Data Augmentation"},
    {"id": "DC", "group": "mitigation", "label": "Dataset Curation"},
    {"id": "RS", "group": "mitigation", "label": "Resampling"},
    {"id": "CH", "group": "mitigation", "label": "ComBat Harmonisation"},
    {"id": "DO", "group": "mitigation", "label": "Domain Adaptation"},
    {"id": "AD", "group": "mitigation", "label": "Adversarial Debiasing"},
    {"id": "SL", "group": "mitigation", "label": "SSL / Foundation Models"},
    {"id": "FL", "group": "mitigation", "label": "Federated Learning"},
    {"id": "SD", "group": "mitigation", "label": "Synthetic Data / DDPM"},
    {"id": "FW", "group": "mitigation", "label": "Fairness-aware Learning"},
    {"id": "TO", "group": "mitigation", "label": "Threshold Optimisation"},
    {"id": "UC", "group": "mitigation", "label": "Uncertainty Calibration"},
    {"id": "CM", "group": "mitigation", "label": "Causal Methods"},
    {"id": "EC", "group": "mitigation", "label": "Explanation Constraints"},
    {"id": "CL", "group": "mitigation", "label": "Continual Learning"}
  ],
  "links": [
    {"source": "DB", "target": "DC", "value": 1},
    {"source": "DB", "target": "AD", "value": 1},
    {"source": "DB", "target": "SL", "value": 1},
    {"source": "DB", "target": "SD", "value": 1},
    {"source": "DB", "target": "FW", "value": 3},
    {"source": "DB", "target": "TO", "value": 1},
    {"source": "DB", "target": "EC", "value": 1},
    {"source": "DB", "target": "CL", "value": 1},
    {"source": "RB", "target": "DC", "value": 3},
    {"source": "RB", "target": "SL", "value": 1},
    {"source": "RB", "target": "FL", "value": 1},
    {"source": "RB", "target": "SD", "value": 2},
    {"source": "CB", "target": "DC", "value": 3},
    {"source": "CB", "target": "CH", "value": 1},
    {"source": "CB", "target": "AD", "value": 1},
    {"source": "CB", "target": "FW", "value": 1},
    {"source": "SB", "target": "DC", "value": 4},
    {"source": "SB", "target": "RS", "value": 1},
    {"source": "SB", "target": "SL", "value": 1},
    {"source": "SB", "target": "FL", "value": 2},
    {"source": "SB", "target": "SD", "value": 1},
    {"source": "LB", "target": "DC", "value": 1},
    {"source": "LB", "target": "RS", "value": 2},
    {"source": "LB", "target": "DO", "value": 1},
    {"source": "LB", "target": "UC", "value": 1},
    {"source": "LB", "target": "EC", "value": 2},
    {"source": "IB", "target": "DC", "value": 2},
    {"source": "IB", "target": "CH", "value": 2},
    {"source": "IB", "target": "DO", "value": 1},
    {"source": "IB", "target": "AD", "value": 1},
    {"source": "IB", "target": "SL", "value": 1},
    {"source": "IB", "target": "FL", "value": 1},
    {"source": "TB", "target": "SN", "value": 3},
    {"source": "TB", "target": "DA", "value": 2},
    {"source": "TB", "target": "DO", "value": 2},
    {"source": "TB", "target": "AD", "value": 1},
    {"source": "TB", "target": "SL", "value": 1},
    {"source": "TB", "target": "UC", "value": 1},
    {"source": "AB", "target": "DC", "value": 1},
    {"source": "AB", "target": "FW", "value": 2},
    {"source": "AB", "target": "TO", "value": 1},
    {"source": "AB", "target": "UC", "value": 1},
    {"source": "AB", "target": "EC", "value": 1},
    {"source": "AB", "target": "CL", "value": 1}
  ]
}
```
