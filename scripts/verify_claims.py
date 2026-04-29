#!/usr/bin/env python3
"""
Verify claims in chapters/03_results.tex and appendices against
data/experimental_78_paper.json.
"""

import json
import re
from collections import Counter
from pathlib import Path

PROJECT = Path("/mnt/e/fairness-review-paper/literature-review-paper_v7")
JSON_PATH = PROJECT / "data/experimental_78_paper.json"
PAPERS_DIR = PROJECT / "paper/experimental_78_papers"
RESULTS_TEX = PROJECT / "latex/chapters/03_results.tex"
S1_TEX = PROJECT / "latex/appendices/S1_included_studies.tex"
S2_TEX = PROJECT / "latex/appendices/S2_bias_taxonomy.tex"
S3_TEX = PROJECT / "latex/appendices/S3_metric_reporting.tex"

with open(JSON_PATH) as f:
    papers = json.load(f)

print(f"{'='*70}")
print(f"BASIC COUNTS")
print(f"{'='*70}")
print(f"Total papers in JSON: {len(papers)}")

# ============================================================
# 1. YEAR / TEMPORAL ANALYSIS
# ============================================================
print(f"\n{'='*70}")
print(f"1. TEMPORAL ANALYSIS")
print(f"{'='*70}")

years = []
for p in papers:
    y = p.get("Year")
    if isinstance(y, str):
        try:
            y = int(y)
        except:
            pass
    years.append(y)
year_counts = Counter(years)
# Sort keys by type
str_keys = sorted([k for k in year_counts if isinstance(k, str)])
int_keys = sorted([k for k in year_counts if isinstance(k, int)])
none_keys = [k for k in year_counts if k is None]
print(f"Year distribution: {[(k, year_counts[k]) for k in int_keys + str_keys + none_keys]}")

# Check for unreported years
unreported = [p for p in papers if p.get("Year") is None]
print(f"Unreported years (None): {len(unreported)}")

def safe_yr(y):
    if isinstance(y, (int, float)):
        return y
    if isinstance(y, str):
        try:
            return int(y)
        except:
            return None
    return None

# Temporal bins
pre2020 = sum(1 for y in years if safe_yr(y) is not None and safe_yr(y) < 2020)
d2020_22 = sum(1 for y in years if safe_yr(y) is not None and 2020 <= safe_yr(y) <= 2022)
d2023_24 = sum(1 for y in years if safe_yr(y) is not None and 2023 <= safe_yr(y) <= 2024)
d2025_26 = sum(1 for y in years if safe_yr(y) is not None and 2025 <= safe_yr(y) <= 2026)
yreported = sum(1 for y in years if safe_yr(y) is not None)

print(f"\nTemporal breakdown:")
print(f"  Pre-2020: {pre2020} (claim: 6)")
print(f"  2020-2022: {d2020_22} (claim: 17)")
print(f"  2023-2024: {d2023_24} (claim: 32)")
print(f"  2025-2026: {d2025_26} (claim: 18)")
print(f"  Unreported (null or non-numeric): {len(unreported)} (claim: 5)")
print(f"  Total with year: {yreported} + {len(unreported)} unreported = {yreported + len(unreported)}")
print(f"  Sum: {pre2020} + {d2020_22} + {d2023_24} + {d2025_26} + {len(unreported)} = {pre2020 + d2020_22 + d2023_24 + d2025_26 + len(unreported)} (should be 78)")

# Show papers with unreported years
if unreported:
    print(f"\nPapers with null/missing Year:")
    for p in unreported:
        print(f"  - {p['citation_key']}: Year={p.get('Year', 'N/A')}, Title={p.get('Paper Title','?')[:80]}")

# ============================================================
# 2. JOURNAL vs CONFERENCE
# ============================================================
print(f"\n{'='*70}")
print(f"2. JOURNAL vs CONFERENCE")
print(f"{'='*70}")

journals = []
conferences = []
for p in papers:
    jc = p.get("Journal or Conference", "")
    if jc and "conference" in jc.lower():
        conferences.append(p)
    elif jc:
        journals.append(p)
    elif jc == "" or jc is None:
        journals.append(p)  # Default to journal if unclear

# Conference keywords
conf_kw = ["conference", "proceedings", "neurips", "iclr", "iccv", "cvpr",
           "miccai", "aaai", "icml", "eccv", "ismrm", "midl"]
journals2 = []
conferences2 = []
for p in papers:
    jc = p.get("Journal or Conference", "").lower()
    jt = p.get("Full BibTeX Reference", "").lower()
    combined = jc + " " + jt
    is_conf = any(kw in combined for kw in conf_kw)
    if is_conf:
        conferences2.append(p)
    else:
        journals2.append(p)

print(f"Journals (simple): {len(journals)} / 78 = {100*len(journals)/78:.1f}% (claim: 71, 91.0%)")
print(f"Conferences (simple): {len(conferences)} / 78 = {100*len(conferences)/78:.1f}% (claim: 7, 9.0%)")
print(f"Journals (keyword): {len(journals2)} / 78 = {100*len(journals2)/78:.1f}%")
print(f"Conferences (keyword): {len(conferences2)} / 78 = {100*len(conferences2)/78:.1f}%")

if conferences2:
    print(f"\nLikely conference papers:")
    for p in conferences2:
        print(f"  - {p['citation_key']}: {p.get('Journal or Conference','?')}")

# ============================================================
# 3. CANCER TYPE ANALYSIS
# ============================================================
print(f"\n{'='*70}")
print(f"3. CANCER TYPE ANALYSIS")
print(f"{'='*70}")

cancer_types = [p.get("Cancer Type", "").lower() for p in papers]

def count_cancer(keyword, types):
    """Count papers matching cancer keyword (non-exclusive)"""
    return sum(1 for t in types if keyword in t)

# Primary focus (from the claim)
cancer_map = {
    "Breast": "breast",
    "Lung": "lung",
    "Colorectal": "colorectal",
    "Prostate": "prostate",
    "Skin/Melanoma": "skin|melanoma",
    "Multi/Pan-cancer": "multi|pan-cancer|multiple",
    "Ovarian": "ovarian",
    "Brain/Glioma": "brain|glioma|glioblastoma",
    "Kidney/Renal": "kidney|renal",
}

print("Cancer type matches (non-exclusive, any mention):")
for name, pattern in cancer_map.items():
    cnt = sum(1 for t in cancer_types if re.search(pattern, t))
    print(f"  {name}: {cnt}")

# Sample some cancer type entries to see how "multi" appears
print("\nSample cancer type entries:")
for p in papers[:10]:
    ct = p.get("Cancer Type", "")
    print(f"  [{p['citation_key']}] '{ct}'")
print("...")
multi_samples = [p for p in papers if "multi" in p.get("Cancer Type", "").lower() or "pan" in p.get("Cancer Type", "").lower()]
print(f"\nPapers mentioning 'multi' or 'pan' in cancer type: {len(multi_samples)}")

# ============================================================
# 4. FAIRNESS METRICS ANALYSIS
# ============================================================
print(f"\n{'='*70}")
print(f"4. FAIRNESS METRICS ANALYSIS")
print(f"{'='*70}")

# Check for fairness metric reporting
fairness_metrics = []
for p in papers:
    fm = p.get("Fairness Metric", "").strip()
    fairness_metrics.append(fm)

# Classify as having "any fairness metric" vs just standard metrics
standard_metrics = ["accuracy", "auroc", "auc", "f1", "sensitivity", "specificity",
                    "balanced accuracy", "precision", "recall", "kappa"]

has_fairness = []
has_standard_only = []
no_metrics = []
for p in papers:
    fm = p.get("Fairness Metric", "").lower().strip()
    if not fm or fm in ["n/a", "none", "not reported"]:
        no_metrics.append(p)
        continue
    # Check if there are metrics beyond standard ones
    is_purely_standard = True
    for sm in standard_metrics:
        fm_stripped = fm.replace(sm, "")
    # Check for fairness-specific terms
    fairness_terms = ["fairness", "disparity", "equal", "demographic", "parity",
                      "odds", "opportunity", "calibration", "ece", "worst",
                      "subgroup", "gap", "differential", "privacy",
                      "generalization", "domain", "shift", "robustness",
                      "bias", "statistical parity", "tpr", "fpr", "equity",
                      "fate", "site", "cross", "ood", "distribution",
                      "balanced accuracy gap", "balanced acc", "covariate",
                      "youden", "conformal", "coverage"]
    has_fairness_term = any(ft in fm for ft in fairness_terms)
    if has_fairness_term:
        has_fairness.append(p)
    else:
        has_standard_only.append(p)

print(f"Papers with any fairness-related metric term: {len(has_fairness)} (claim: 15, 19.2%)")
print(f"Papers with standard metrics only (or unclear): {len(has_standard_only)}")
print(f"Papers with no metrics reported: {len(no_metrics)}")

# Check specific fairness metrics
# Accuracy
accuracy_count = sum(1 for p in papers if "accuracy" in p.get("Fairness Metric", "").lower() or "accuracy" in p.get("Performance", "").lower())
print(f"\nPapers mentioning accuracy: {accuracy_count} / 78 = {100*accuracy_count/78:.1f}% (claim: 67, 85.9%)")

# AUROC
auroc_count = sum(1 for p in papers if "auc" in p.get("Fairness Metric", "").lower() or "auc" in p.get("Performance", "").lower())
print(f"Papers mentioning AUROC/AUC: {auroc_count} / 78 = {100*auroc_count/78:.1f}% (claim: 55, 70.5%)")

# F1
f1_count = sum(1 for p in papers if "f1" in p.get("Fairness Metric", "").lower() or "f1" in p.get("Performance", "").lower())
print(f"Papers mentioning F1: {f1_count} / 78 = {100*f1_count/78:.1f}% (claim: 42.3%)")

# Check the specific fairness metrics more carefully
print("\n--- Specific fairness metrics ---")
specific_checks = {
    "Subgroup AUC gap": ["subgroup auc", "subgroup auroc", "auc gap", "auroc gap", "auc difference"],
    "Worst-group accuracy": ["worst", "minimum", "min performance"],
    "TPR/FPR disparity": ["tpr", "fpr", "false positive", "false negative", "true positive", "true negative"],
    "ECE (Expected Calibration Error)": ["ece", "calibration error", "expected calibration"],
    "Preserved-site CV": ["preserved", "site cv", "site-aware", "site-stratified"],
    "Statistical/Demographic Parity": ["statistical parity", "demographic parity", "equalized odds", "equal opportunity"],
}

for name, terms in specific_checks.items():
    cnt = 0
    papers_found = []
    for p in papers:
        fm = p.get("Fairness Metric", "").lower()
        perf = p.get("Performance", "").lower()
        combined = fm + " " + perf
        if any(t in combined for t in terms):
            cnt += 1
            papers_found.append(p['citation_key'])
    print(f"  {name}: {cnt} (claim varies)")
    if papers_found:
        print(f"    Papers: {papers_found}")

# ============================================================
# 5. DATASET ANALYSIS
# ============================================================
print(f"\n{'='*70}")
print(f"5. DATASET ANALYSIS")
print(f"{'='*70}")

tcga_count = sum(1 for p in papers if "tcga" in p.get("Dataset", "").lower())
print(f"TCGA usage: {tcga_count} / 78 = {100*tcga_count/78:.1f}% (claim: 33, 42.3%)")

camelyon_count = sum(1 for p in papers if "camelyon" in p.get("Dataset", "").lower())
print(f"CAMELYON usage: {camelyon_count} / 78 = {100*camelyon_count/78:.1f}% (claim: ~7, 9.0%)")

# Check for "site" or "institution" or "single" mentions
single_site_kw = sum(1 for p in papers if "single" in p.get("Dataset", "").lower() or "single" in p.get("Bias Type / Source", "").lower())
print(f"Papers mentioning 'single' (site/data): {single_site_kw} / 78 = {100*single_site_kw/78:.1f}% (claim: 40 private single-site, 51.3%)")

# External validation
ext_val = sum(1 for p in papers if any(kw in p.get("Performance", "").lower() for kw in ["external", "external validation", "ood", "out-of-distribution"]))
print(f"Papers mentioning external/OOD validation in performance: {ext_val} / 78 = {100*ext_val/78:.1f}% (claim: 23, 29.5%)")

# Multi-institutional
multi_inst = sum(1 for p in papers if any(kw in p.get("Dataset", "").lower() for kw in ["multi-instit", "multi-instit", "multi-center", "multi-centre", "multi center", "multi centre", "multi-hospital", "multi site", "multi-source", "multiple institution", "multiple hospital"]))
print(f"Papers mentioning multi-institutional/multi-center: {multi_inst} / 78 = {100*multi_inst/78:.1f}% (claim: 23, 29.5%)")

# ============================================================
# 6. BIAS CATEGORY ANALYSIS
# ============================================================
print(f"\n{'='*70}")
print(f"6. BIAS CATEGORY ANALYSIS")
print(f"{'='*70}")

# Analyze bias types from JSON
bias_assignments = {}
for p in papers:
    bt = p.get("Bias Type / Source", "").lower()
    bias_assignments[p['citation_key']] = bt

# Categorize
bias_categories = {
    "Demographic": ["demographic", "race", "racial", "ethnic", "sex", "gender", "age", "ancestry"],
    "Institutional/Batch": ["institution", "batch", "site", "scanner", "staining", "tss", "tissue source"],
    "Selection/Sampling": ["selection", "sampling", "cohort", "convenience", "single-site", "single center"],
    "Technical/Domain-shift": ["domain shift", "distribution shift", "domain generali", "scanner", "stain"],
    "Class/Label": ["class imbalance", "label", "annotation", "inter-observer", "gleason", "grayscale"],
    "Algorithmic": ["algorithm", "architecture", "attention", "model selection", "objective"],
    "Confounding": ["confound", "shortcut", "spurious", "entanglement"],
    "Representation": ["represent", "underrepresent", "under-represent", "coverage", "skin tone", "rare"],
}

cat_counts = {}
cat_papers = {}
for cat, terms in bias_categories.items():
    matching = []
    for p in papers:
        bt = p.get("Bias Type / Source", "").lower()
        if any(t in bt for t in terms):
            matching.append(p)
    cat_counts[cat] = len(matching)
    cat_papers[cat] = [p['citation_key'] for p in matching]

print("Bias category assignments from JSON (keyword matching):")
for cat, cnt in sorted(cat_counts.items(), key=lambda x: -x[1]):
    claimed = {
        "Demographic": 5, "Institutional/Batch": 7, "Selection/Sampling": 8,
        "Technical/Domain-shift": 8, "Class/Label": 7, "Algorithmic": 5,
        "Confounding": 6, "Representation": 7
    }.get(cat, "?")
    match_str = "MATCH" if cnt == claimed else f"DIFF (claim: {claimed})"
    print(f"  {cat}: {cnt} ({match_str})")
    if cnt > 0:
        print(f"    Papers: {cat_papers[cat][:5]}{'...' if len(cat_papers[cat]) > 5 else ''}")

# Total bias category assignments
total_assignments = sum(cat_counts.values())
studies_with_bias = len(set().union(*[set(v) for v in cat_papers.values()]))
print(f"\nTotal bias category assignments: {total_assignments} (claim: 53)")
print(f"Studies with >=1 bias category: {studies_with_bias} (claim: 46, 59.0%)")
print(f"Mean assignments per study: {total_assignments/studies_with_bias:.2f} (claim: 1.15)")

# Studies reporting 1 vs 2 categories
bias_count_per_paper = Counter()
all_bias_papers = set()
for cat, paper_list in cat_papers.items():
    for pk in paper_list:
        bias_count_per_paper[pk] += 1
        all_bias_papers.add(pk)

one_cat = sum(1 for c in bias_count_per_paper.values() if c == 1)
two_cat = sum(1 for c in bias_count_per_paper.values() if c == 2)
print(f"Studies with 1 category: {one_cat} (claim: 39)")
print(f"Studies with 2 categories: {two_cat} (claim: 7)")
print(f"Median: {sorted(bias_count_per_paper.values())[len(bias_count_per_paper)//2] if bias_count_per_paper else 'N/A'} (claim: 1)")
min_c = min(bias_count_per_paper.values()) if bias_count_per_paper else 0
max_c = max(bias_count_per_paper.values()) if bias_count_per_paper else 0
print(f"Range: {min_c}--{max_c} (claim: 1--2)")

# ============================================================
# 7. MITIGATION METHODS ANALYSIS
# ============================================================
print(f"\n{'='*70}")
print(f"7. MITIGATION METHOD COVERAGE")
print(f"{'='*70}")

mitigation_methods = Counter()
for p in papers:
    mm = p.get("Mitigation Method", "").lower()
    mitigation_methods[mm] += 0  # dummy

# Check specific method families
method_checks = {
    "Stain normalization": ["stain normal", "macenko", "reinhard", "vahadane", "stain transfer", "stain adaptation", "staingan", "stainnet"],
    "Data augmentation": ["augment", "randaugment"],
    "Dataset curation": ["curation", "quality control", "grandqc", "data cleaning"],
    "Resampling/SMOTE": ["smote", "resampling", "oversampling", "undersampling"],
    "ComBat harmonization": ["combat", "harmoni"],
    "Domain adaptation": ["domain adapt", "domain adversarial", "dann", "cyclegan"],
    "Adversarial debiasing": ["adversarial", "gradient reversal", "grl"],
    "SSL/Foundation models": ["self-supervised", "ssl", "foundation model", "pretrain", "simclr"],
    "Federated learning": ["federated", "fedavg", "fedprox"],
    "Synthetic data/DDPM": ["synthetic", "ddpm", "diffusion", "gan"],
    "Fairness-aware learning": ["fairness-aware", "fair-path", "spare", "contrastive", "fair", "equitable"],
    "Threshold optimization": ["threshold", "post-hoc", "post-processing"],
    "Uncertainty calibration": ["uncertainty", "calibration", "conformal"],
    "Causal methods": ["causal"],
    "Explanation constraints": ["explain", "heatmap", "lrp", "saliency"],
    "Continual learning": ["continual", "lifelong"],
}

print("Method family coverage:")
for method, terms in method_checks.items():
    cnt = 0
    method_papers = []
    for p in papers:
        mm = p.get("Mitigation Method", "").lower()
        if any(t in mm for t in terms):
            cnt += 1
            method_papers.append(p['citation_key'])
    print(f"  {method}: {cnt} studies {method_papers[:3]}{'...' if len(method_papers) > 3 else ''}")

# ============================================================
# 8. CROSS-REFERENCE CITATION KEYS
# ============================================================
print(f"\n{'='*70}")
print(f"8. CITATION KEY VERIFICATION")
print(f"{'='*70}")

all_keys = {p['citation_key'] for p in papers}
print(f"Total unique citation keys: {len(all_keys)}")

# Extract all \citep{} references from results chapter
with open(RESULTS_TEX) as f:
    results_text = f.read()

citep_refs = set()
for m in re.finditer(r'\\citep\{([^}]+)\}', results_text):
    for ref in m.group(1).split(','):
        ref = ref.strip()
        if ref:
            citep_refs.add(ref)

citet_refs = set()
for m in re.finditer(r'\\citet\{([^}]+)\}', results_text):
    for ref in m.group(1).split(','):
        ref = ref.strip()
        if ref:
            citet_refs.add(ref)

all_cited = citep_refs | citet_refs
print(f"Unique citations in results chapter: {len(all_cited)}")

# Check if cited keys exist in the JSON (among experimental 78)
in_78 = all_cited & all_keys
not_in_78 = all_cited - all_keys
print(f"Cited and in 78-paper JSON: {len(in_78)}")
print(f"Cited but NOT in 78-paper JSON: {len(not_in_78)}")

# Check references.bib for the missing ones
with open(PROJECT / "latex/references.bib") as f:
    bib_text = f.read()

if not_in_78:
    print(f"\nChecking references.bib for citations not in 78-JSON:")
    for key in sorted(not_in_78):
        in_bib = key in bib_text
        print(f"  {key}: {'in references.bib' if in_bib else 'NOT FOUND in references.bib!'}")

# ============================================================
# 9. SPECIFIC NUMERIC CLAIM VERIFICATION
# ============================================================
print(f"\n{'='*70}")
print(f"9. SPECIFIC NUMERIC CLAIMS")
print(f"{'='*70}")

# Check specific papers for claim verification
# vaidya2024demographic - has White-Black AUROC gap 3-16% across 20 cancer types
v_paper = [p for p in papers if p['citation_key'] == 'vaidya2024demographic']
if v_paper:
    p = v_paper[0]
    print(f"vaidya2024demographic:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    print(f"  Performance: {p.get('Performance','?')[:200]}")

# howard2021site - AUROC 0.798 -> 0.507
h_paper = [p for p in papers if p['citation_key'] == 'howard2021site']
if h_paper:
    p = h_paper[0]
    print(f"\nhoward2021site:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    perf = p.get('Performance','?')
    print(f"  Performance: {perf[:300]}")

# komen2024batch - foundation model TSS
k_paper = [p for p in papers if p['citation_key'] == 'komen2024batch']
if k_paper:
    p = k_paper[0]
    print(f"\nkomen2024batch:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    print(f"  Performance: {p.get('Performance','?')[:300]}")

# kheiri2025investigation - MI = 1.47
kh_paper = [p for p in papers if p['citation_key'] == 'kheiri2025investigation']
if kh_paper:
    p = kh_paper[0]
    print(f"\nkheiri2025investigation:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    print(f"  Performance: {p.get('Performance','?')[:300]}")

# lin2025contrastive - FAIR-Path 88.5-91.1%
l_paper = [p for p in papers if p['citation_key'] == 'lin2025contrastive']
if l_paper:
    p = l_paper[0]
    print(f"\nlin2025contrastive:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    print(f"  Performance: {p.get('Performance','?')[:300]}")

# murchan2024combat - ComBat
m_paper = [p for p in papers if p['citation_key'] == 'murchan2024combat']
if m_paper:
    p = m_paper[0]
    print(f"\nmurchan2024combat:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    print(f"  Performance: {p.get('Performance','?')[:300]}")

# roschewitz2023automatic - scanner
r_paper = [p for p in papers if p['citation_key'] == 'roschewitz2023automatic']
if r_paper:
    p = r_paper[0]
    print(f"\nroschewitz2023automatic:")
    print(f"  Cancer: {p.get('Cancer Type','?')}")
    print(f"  Performance: {p.get('Performance','?')[:300]}")

print(f"\n{'='*70}")
print(f"VERIFICATION COMPLETE")
print(f"{'='*70}")
