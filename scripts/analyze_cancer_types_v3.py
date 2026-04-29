#!/usr/bin/env python3
"""
Manual-rigorous cancer type analysis. Avoids false positives from substring matching.
Each paper is analyzed by checking the Cancer Type field first, then Title, then Dataset.
"""

import json
import re
from collections import Counter, defaultdict

with open('/mnt/e/fairness-review-paper/literature-review-paper_v7/data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

# Cancer-type abbreviations in TCGA
TCGA_CODES = {
    'BRCA': 'Breast',
    'PRAD': 'Prostate', 
    'SKCM': 'Skin',
    'LUAD': 'Lung',
    'LUSC': 'Lung',
    'COAD': 'Colorectal',
    'READ': 'Colorectal',
    'COADREAD': 'Colorectal',
    'CRC': 'Colorectal',
    'KIRC': 'Kidney',
    'KIRP': 'Kidney',
    'KICH': 'Kidney',
    'HNSC': 'Head/Neck',
    'LIHC': 'Liver',
    'LGG': 'Brain',
    'GBM': 'Brain',
    'STAD': 'Stomach',
    'BLCA': 'Bladder',
    'UCEC': 'Uterine',
    'PAAD': 'Pancreatic',
    'THCA': 'Thyroid',
    'OV': 'Ovarian',
}

def get_ct_field(paper):
    return paper.get('Cancer Type', '')

def get_title(paper):
    return paper.get('Paper Title', '')

def get_kf(paper):
    return paper.get('Key Findings', '')

def get_dataset(paper):
    return paper.get('Dataset', '')

def has_keyword(text, *keywords):
    t = text.lower()
    return any(re.search(r'\b' + re.escape(kw.lower()) + r'\b', t) for kw in keywords)

def has_phrase(text, *phrases):
    t = text.lower()
    return any(p.lower() in t for p in phrases)

# =====================================================================
# Determine if paper STUDIES each cancer type (non-exclusive)
# =====================================================================

def studies_breast(paper):
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    ds = get_dataset(paper).lower()
    kf = get_kf(paper).lower()
    combined = f"{ct} | {title} | {ds} | {kf}"
    
    # Direct mention
    if 'breast' in combined or 'brca' in combined:
        return True
    
    # Breast-specific datasets (but beware false positives)
    if 'camelyon' in ds and 'breast' not in combined:
        # CAMELYON = breast cancer lymph node metastases. Most CAMELYON papers ARE breast.
        # BUT check if this is truly studying breast cancer or just using it as a generic testbed
        pass  # We'll count CAMELYON as breast since it's breast cancer tissue
    
    # Only count if CAMELYON is explicitly used as data
    return False

def studies_prostate(paper):
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    ds = get_dataset(paper).lower()
    kf = get_kf(paper).lower()
    combined = f"{ct} | {title} | {ds} | {kf}"
    
    if has_keyword(combined, 'prostate', 'prad'):
        return True
    # Gleason grading is prostate-specific
    if 'gleason' in combined and ('prostate' in combined or 'prad' in combined):
        return True
    return False

def studies_skin(paper):
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    ds = get_dataset(paper).lower()
    kf = get_kf(paper).lower()
    combined = f"{ct} | {title} | {ds} | {kf}"
    
    if has_keyword(combined, 'melanoma', 'melanocytic', 'skcm'):
        return True
    if has_phrase(combined, 'basal cell carcinoma', 'squamous cell carcinoma'):
        return True
    if has_keyword(combined, 'dermatolog', 'dermatoscop', 'dermatopatholog'):
        return True
    if has_keyword(combined, 'cutaneous'):
        return True
    if has_phrase(combined, 'fitzpatrick'):
        return True
    if 'skin' in combined and ('cancer' in combined or 'lesion' in combined or 'disease' in combined or 
                                'melanoma' in combined or 'nevus' in combined or 'nevi' in combined):
        return True
    return False

def studies_lung(paper):
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    ds = get_dataset(paper).lower()
    kf = get_kf(paper).lower()
    combined = f"{ct} | {title} | {ds} | {kf}"
    
    if has_keyword(combined, 'lung', 'luad', 'lusc', 'nsclc'):
        return True
    if 'pulmonary' in combined:
        return True
    if 'chest x-ray' in combined or 'chest xray' in combined or 'chestx' in combined:
        return True  # Some papers include lung imaging
    return False

def studies_colorectal(paper):
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    ds = get_dataset(paper).lower()
    kf = get_kf(paper).lower()
    combined = f"{ct} | {title} | {ds} | {kf}"
    
    if has_keyword(combined, 'colorectal', 'coad', 'coadread', 'colon cancer'):
        return True
    if has_keyword(combined, 'rectal cancer'):
        return True
    if 'colon' in combined or 'colorectal' in combined:
        if 'cancer' in combined or 'carcinoma' in combined or 'adenocarcinoma' in combined or 'polyp' in combined:
            return True
    if 'ccfr' in combined.lower():
        return True
    return False

def is_multicancer(paper):
    """Paper studies 3+ cancer types as its primary domain."""
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    
    # Explicit multi
    if any(x in ct for x in ['pan-cancer', 'multiple cancer type', 'multi-organ', 
                                '33 cancer type', '20 cancer type', '14 cancer type',
                                '12 tumor type', 'six tumor type']):
        return True
    
    # Count distinct cancer types in CT field
    cancers_in_ct = 0
    for kw in ['breast', 'brca', 'lung', 'luad', 'lusc', 'prostate', 'prad', 
               'skin', 'melanoma', 'skcm', 'colorectal', 'colon', 'coad', 'coadread',
               'kidney', 'renal', 'kirc', 'kirp', 'brain', 'gbm', 'lgg', 'liver', 'lihc',
               'head and neck', 'hnsc', 'stomach', 'stad', 'bladder', 'blca', 
               'uterine', 'ucec', 'pancreatic', 'paad', 'thyroid', 'thca',
               'ovarian', 'endometrial', 'cervical', 'esophageal']:
        if kw in ct:
            cancers_in_ct += 1
    
    if cancers_in_ct >= 3:
        return True
    
    # Check title for multi-cancer
    if 'pan-cancer' in title or 'multi-cancer' in title:
        return True
    
    return False


# =====================================================================
# MAIN ANALYSIS
# =====================================================================

primary_counts = Counter()
any_counts = Counter()
all_primary = defaultdict(list)
all_any = defaultdict(list)
year_counts = Counter()

print(f"{'SN':>4s} {'Yr':>3s}  B  P  S  L  C  M | Cancer Type")
print("-" * 80)

for paper in papers:
    sn = paper.get('Serial No.', '?')
    yr = paper.get('Year', '?')
    year_counts[yr] += 1
    
    b = studies_breast(paper)
    p = studies_prostate(paper)
    s = studies_skin(paper)
    l = studies_lung(paper)
    c = studies_colorectal(paper)
    m = is_multicancer(paper)
    
    # Primary = the paper studies this cancer type
    study_types = []
    if b: study_types.append('Breast'); primary_counts['Breast'] += 1; all_primary['Breast'].append(sn)
    if p: study_types.append('Prostate'); primary_counts['Prostate'] += 1; all_primary['Prostate'].append(sn)
    if s: study_types.append('Skin/Melanoma'); primary_counts['Skin/Melanoma'] += 1; all_primary['Skin/Melanoma'].append(sn)
    if l: study_types.append('Lung'); primary_counts['Lung'] += 1; all_primary['Lung'].append(sn)
    if c: study_types.append('Colorectal'); primary_counts['Colorectal'] += 1; all_primary['Colorectal'].append(sn)
    if m: primary_counts['Multi-cancer'] += 1; all_primary['Multi-cancer'].append(sn)
    
    b_s = '*' if b else '.'
    p_s = '*' if p else '.'
    s_s = '*' if s else '.'
    l_s = '*' if l else '.'
    c_s = '*' if c else '.'
    m_s = '*' if m else '.'
    
    ct_display = get_ct_field(paper)[:80]
    print(f"{sn:4d} {yr:3d}  {b_s}  {p_s}  {s_s}  {l_s}  {c_s}  {m_s} | {ct_display}")

# =====================================================================
# Now manually count CAMELYON papers for breast (all that explicitly study it)
# =====================================================================
print()
print("=" * 80)
print("ADDITIONAL BREAST PAPERS (using CAMELYON or other breast datasets)")
print("=" * 80)

for paper in papers:
    sn = paper.get('Serial No.', '?')
    ds = get_dataset(paper).lower()
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    
    # Papers that use CAMELYON (breast cancer lymph nodes) but don't have breast in CT
    has_camelyon = 'camelyon' in ds
    
    # Papers with BreakHis, BACH, etc.
    has_breast_dataset = False
    for pat in ['breakhis', 'bach', 'breastpathq', 'tiger', 'iciar', 'breastkf']:
        if pat in ds:
            has_breast_dataset = True
            break
    
    if (has_camelyon or has_breast_dataset):
        has_breast_in_ct = 'breast' in ct or 'brca' in ct
        if not has_breast_in_ct:
            print(f"  [{sn}] CT={ct[:70]:<70s} Camelyon={has_camelyon} BreastDS={has_breast_dataset}")

# Also check: which papers have breast in Key Findings but not in Cancer Type
print()
print("=" * 80)
print("BREAST IN KEY FINDINGS BUT NOT CT")
print("=" * 80)
for paper in papers:
    sn = paper.get('Serial No.', '?')
    ct = get_ct_field(paper).lower()
    kf = get_kf(paper).lower()
    if 'breast' not in ct and 'brca' not in ct:
        if 'breast' in kf or 'brca' in kf:
            print(f"  [{sn}] CT={ct[:70]:<70s}")
            # Print the relevant excerpt
            for line in kf.split('.'):
                if 'breast' in line.lower() or 'brca' in line.lower():
                    print(f"       -> {line.strip()[:120]}")

# Also check: which papers mention breast in title but not CT
print()
print("=" * 80)
print("BREAST IN TITLE BUT NOT CT")
print("=" * 80)
for paper in papers:
    sn = paper.get('Serial No.', '?')
    ct = get_ct_field(paper).lower()
    title = get_title(paper).lower()
    if 'breast' not in ct and 'brca' not in ct:
        if 'breast' in title or 'brca' in title:
            print(f"  [{sn}] CT={ct[:70]:<70s} Title={title[:100]}")
