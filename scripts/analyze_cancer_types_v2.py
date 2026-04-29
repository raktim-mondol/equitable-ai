#!/usr/bin/env python3
"""
Comprehensive cancer type analysis matching the paper's claim methodology.
Counts are NON-EXCLUSIVE: a paper studying breast + lung counts under both.

For "primary focus": paper studies this cancer type (from Cancer Type field, Dataset, and experiments)
For "any mention": any mention across all fields (Cancer Type, Title, Key Findings, Dataset, etc.)
"""

import json
import re
from collections import Counter, defaultdict

with open('/mnt/e/fairness-review-paper/literature-review-paper_v7/data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")
print()

# =====================================================================
# Detection functions with dataset-aware hints
# =====================================================================

# Known breast cancer datasets
BREAST_DATASETS = [
    'CAMELYON', 'BACH', 'BreakHis', 'BreastPathQ', 'TIGER', 
    'ICIAR', 'BreastKf', 'IDC', 'BHI', 'MITOS-ATYPIA',
    'PACS04', 'PACS05', 'PACS08', 'Nomorad',
    'ABCTB', 'METABRIC', 'MSK.*breast',
]

def get_combined_text(paper):
    fields = [
        'Cancer Type', 'Paper Title', 'Key Findings', 'Dataset',
        'Full BibTeX Reference', 'Bias Type / Source',
    ]
    parts = []
    for f in fields:
        v = paper.get(f, '')
        if v:
            parts.append(str(v))
    return ' '.join(parts)

def match_breast(text, dataset_text=""):
    t = text.lower()
    d = dataset_text.lower() if dataset_text else t
    
    # Direct mentions
    if re.search(r'\bbreast\b', t): return True
    if re.search(r'\bBRCA\b', t): return True
    
    # Check datasets
    for ds in BREAST_DATASETS:
        if re.search(ds, d, re.IGNORECASE): 
            return True
    
    return False

def match_prostate(text, dataset_text=""):
    t = text.lower()
    d = dataset_text.lower() if dataset_text else t
    
    if re.search(r'\bprostate\b', t): return True
    if re.search(r'\bPRAD\b', t): return True
    if re.search(r'\bGleason\b', d): return True  # Gleason grading is prostate-specific
    if re.search(r'\bSTHLM3\b', d): return True   # prostate screening trial
    
    return False

def match_skin(text, dataset_text=""):
    t = text.lower()
    d = dataset_text.lower() if dataset_text else t
    
    patterns = [
        r'\bskin\b', r'\bmelanoma\b', r'\bmelanocytic\b',
        r'basal cell carcinoma', r'squamous cell carcinoma.*skin',
        r'dermatolog', r'dermatoscop', r'dermatopatholog',
        r'\bnevus\b', r'\bnevi\b', r'\bSKCM\b',
        r'fitzpatrick', r'ISIC', r'cutaneous',
        r'\bHAM10000\b', r'\bDDI\b.*skin',
        r'\bPH2\b', r'\bDermofit\b',
    ]
    return any(re.search(p, t, re.IGNORECASE) for p in patterns) or \
           any(re.search(p, d, re.IGNORECASE) for p in patterns[:3])

def match_lung(text, dataset_text=""):
    t = text.lower()
    d = dataset_text.lower() if dataset_text else t
    
    patterns = [
        r'\blung\b', r'\bLUAD\b', r'\bLUSC\b', r'\bNSCLC\b',
        r'pulmonary', r'lung adenocarcinoma', r'lung squamous',
        r'\bNLST\b', r'\bLIDC\b',
        r'chest.*xray', r'chest.*x-ray',  # some lung papers use chest X-rays
    ]
    return any(re.search(p, t, re.IGNORECASE) for p in patterns)

def match_colorectal(text, dataset_text=""):
    t = text.lower()
    d = dataset_text.lower() if dataset_text else t
    
    patterns = [
        r'\bcolorectal\b', r'\bcolon\b', r'\brectal\b',
        r'\bCOAD\b', r'\bREAD\b', r'\bCOADREAD\b', r'\bCRC\b',
        r'colorectal cancer', r'colon cancer', r'rectal cancer',
        r'\bNCT-CRC\b', r'\bCCFR\b',
    ]
    # "polyp" alone is too generic for colorectal (it can be nasal, etc.)
    # but check context
    if re.search(r'\bpolyp\b.*\b(colon|colorectal|colonoscopy)\b', t, re.IGNORECASE):
        return True
    
    return any(re.search(p, t, re.IGNORECASE) for p in patterns)

# =====================================================================
# Determine PRIMARY STUDY cancer types (non-exclusive)
# Based on Cancer Type field + Dataset field
# =====================================================================

def get_primary_study_types(paper):
    """Get cancer types the paper PRIMARY studies (non-exclusive)."""
    ct = paper.get('Cancer Type', '')
    ds = paper.get('Dataset', '')
    title = paper.get('Paper Title', '')
    kf = paper.get('Key Findings', '')
    
    # Combined text for primary detection
    primary_text = f"{ct} | {title} | {ds}"
    
    result = set()
    
    if match_breast(primary_text, ds):
        result.add('Breast')
    if match_prostate(primary_text, ds):
        result.add('Prostate')
    if match_skin(primary_text, ds):
        result.add('Skin/Melanoma')
    if match_lung(primary_text, ds):
        result.add('Lung')
    if match_colorectal(primary_text, ds):
        result.add('Colorectal')

    # Check if multi-cancer (has multiple cancer types in Cancer Type field)
    ct_lower = ct.lower()
    cancer_indicators_in_ct = 0
    for check_fn, _ in [(match_breast_name, 'breast'), (match_prostate_name, 'prostate'), 
                         (match_skin_name, 'skin'), (match_lung_name, 'lung'), 
                         (match_colorectal_name, 'colorectal')]:
        if check_fn(ct):
            cancer_indicators_in_ct += 1
    
    if cancer_indicators_in_ct >= 3:
        result.add('Multi-cancer')
    elif any(x in ct_lower for x in ['pan-cancer', 'multiple cancer type', 'multi-organ', '33 cancer type',
                                       '20 cancer type', '14 cancer type']):
        result.add('Multi-cancer')
    
    return result

# Simple name-only matchers (without dataset hints)
def match_breast_name(t):
    t = t.lower()
    return bool(re.search(r'\bbreast\b', t) or re.search(r'\bBRCA\b', t))

def match_prostate_name(t):
    t = t.lower()
    return bool(re.search(r'\bprostate\b', t) or re.search(r'\bPRAD\b', t))

def match_skin_name(t):
    t = t.lower()
    return bool(re.search(r'\bskin\b', t) or re.search(r'\bmelanoma\b', t) or re.search(r'\bdermatolog', t))

def match_lung_name(t):
    t = t.lower()
    return bool(re.search(r'\blung\b', t) or re.search(r'\bLUAD\b', t) or re.search(r'\bLUSC\b', t))

def match_colorectal_name(t):
    t = t.lower()
    return bool(re.search(r'\bcolorectal\b', t) or re.search(r'\bcolon\b', t) or re.search(r'\bCOAD\b', t))


def get_any_mention_types(paper):
    """Get cancer types ANYWHERE in the paper (non-exclusive)."""
    ct = paper.get('Cancer Type', '')
    ds = paper.get('Dataset', '')
    title = paper.get('Paper Title', '')
    kf = paper.get('Key Findings', '')
    bib = paper.get('Full BibTeX Reference', '')
    bias = paper.get('Bias Type / Source', '')
    
    all_text = f"{ct} | {title} | {ds} | {kf} | {bib} | {bias}"
    
    result = set()
    
    if match_breast(all_text, ds):
        result.add('Breast')
    if match_prostate(all_text, ds):
        result.add('Prostate')
    if match_skin(all_text, ds):
        result.add('Skin/Melanoma')
    if match_lung(all_text, ds):
        result.add('Lung')
    if match_colorectal(all_text, ds):
        result.add('Colorectal')
    
    return result


# =====================================================================
# Count
# =====================================================================

primary_study_counts = Counter()
any_mention_counts = Counter()
year_counts = Counter()

# Track which papers have each type
primary_papers = defaultdict(list)
any_papers = defaultdict(list)

for paper in papers:
    sn = paper.get('Serial No.', '?')
    year = paper.get('Year', 'Unknown')
    year_counts[year] += 1
    
    primary = get_primary_study_types(paper)
    any_ = get_any_mention_types(paper)
    
    for c in primary:
        primary_study_counts[c] += 1
        primary_papers[c].append(sn)
    
    for c in any_:
        any_mention_counts[c] += 1
        any_papers[c].append(sn)

# =====================================================================
# Report
# =====================================================================

print("=" * 80)
print("PRIMARY STUDY COUNTS (non-exclusive, from Cancer Type + Dataset)")
print("=" * 80)
for cancer in ['Breast', 'Prostate', 'Skin/Melanoma', 'Lung', 'Colorectal', 'Multi-cancer']:
    count = primary_study_counts.get(cancer, 0)
    pct = count / len(papers) * 100
    print(f"  {cancer:<18s}: {count:3d} ({pct:.1f}%)  SNs: {primary_papers.get(cancer, [])}")

print()
print("=" * 80)
print("ANY MENTION COUNTS (non-exclusive, from all fields)")
print("=" * 80)
for cancer in ['Breast', 'Prostate', 'Skin/Melanoma', 'Lung', 'Colorectal']:
    count = any_mention_counts.get(cancer, 0)
    pct = count / len(papers) * 100
    print(f"  {cancer:<18s}: {count:3d} ({pct:.1f}%)  SNs: {any_papers.get(cancer, [])}")

print()
print("=" * 80)
print("COMPARISON WITH PAPER CLAIMS")
print("=" * 80)

claims_primary = [
    ('Breast', 44, 56.4),
    ('Multi-cancer', 24, 30.8),
    ('Prostate', 15, 19.2),
    ('Skin/Melanoma', 10, 12.8),
    ('Lung', 9, 11.5),
    ('Colorectal', 8, 10.3),
]

claims_any = [
    ('Lung', 28, 35.9),
    ('Prostate', 21, 26.9),
    ('Colorectal', 21, 26.9),
    ('Skin/Melanoma', 13, 16.7),
]

print("\nPrimary focus:")
for cancer, claimed_n, claimed_pct in claims_primary:
    actual = primary_study_counts.get(cancer, 0)
    actual_pct = actual / len(papers) * 100
    diff = actual - claimed_n
    match_str = "MATCH" if abs(diff) <= 2 else f"OFF BY {diff:+d}"
    print(f"  {cancer:<18s}: Claimed={claimed_n:3d} ({claimed_pct}%), Actual={actual:3d} ({actual_pct:.1f}%), {match_str}")

print("\nAny mention:")
for cancer, claimed_n, claimed_pct in claims_any:
    actual = any_mention_counts.get(cancer, 0)
    actual_pct = actual / len(papers) * 100
    diff = actual - claimed_n
    match_str = "MATCH" if abs(diff) <= 2 else f"OFF BY {diff:+d}"
    print(f"  {cancer:<18s}: Claimed={claimed_n:3d} ({claimed_pct}%), Actual={actual:3d} ({actual_pct:.1f}%), {match_str}")

# =====================================================================
# DETAILED MATRIX
# =====================================================================

print()
print("=" * 80)
print("DETAILED PER-PAPER CANCER TYPE MATRIX")
print("=" * 80)
print(f"{'SN':>4s} {'Year':>4s} {'B':1s}{'P':1s}{'S':1s}{'L':1s}{'C':1s}{'M':1s} | {'Cancer Type field'}")
print("-" * 80)

for paper in papers:
    sn = paper.get('Serial No.', '?')
    year = paper.get('Year', '?')
    primary = get_primary_study_types(paper)
    any_ = get_any_mention_types(paper)
    b = '*' if 'Breast' in primary else ('b' if 'Breast' in any_ else '.')
    p = '*' if 'Prostate' in primary else ('p' if 'Prostate' in any_ else '.')
    s = '*' if 'Skin/Melanoma' in primary else ('s' if 'Skin/Melanoma' in any_ else '.')
    l = '*' if 'Lung' in primary else ('l' if 'Lung' in any_ else '.')
    c = '*' if 'Colorectal' in primary else ('c' if 'Colorectal' in any_ else '.')
    m = '*' if 'Multi-cancer' in primary else '.'
    ct = paper.get('Cancer Type', 'N/A')[:90]
    title = paper.get('Paper Title', '')[:60]
    print(f"{sn:4d} {year:4d} {b}{p}{s}{l}{c}{m} | {ct}")
    
print()
print("Legend: * = primary study, lowercase = any mention, . = none")
print("Columns: B=Breast, P=Prostate, S=Skin/Melanoma, L=Lung, C=Colorectal, M=Multi-cancer")

# =====================================================================
# SEPARATE CHECK: BREAST via CAMELYON datasets
# =====================================================================

print()
print("=" * 80)
print("PAPERS USING BREAST DATASETS (CAMELYON, BACH, BreakHis, etc.)")
print("=" * 80)
for paper in papers:
    ds = paper.get('Dataset', '')
    if any(re.search(d, ds, re.IGNORECASE) for d in BREAST_DATASETS):
        sn = paper.get('Serial No.', '?')
        ct = paper.get('Cancer Type', '')
        matches = [d for d in BREAST_DATASETS if re.search(d, ds, re.IGNORECASE)]
        print(f"  [{sn}] CT={ct[:50]:<50s} Datasets: {', '.join(set(matches))}")
