#!/usr/bin/env python3
"""
RECONCILIATION ATTEMPT: Try to match the claimed numbers by varying definitions.

Theory 1: "Primary focus" = cancer type is the MAIN target (not just one of many)
Theory 2: Multi-cancer papers that are general/pan-cancer don't count toward individual types
Theory 3: Only papers with the cancer type explicitly in the Cancer Type field count
"""
import json, re
from collections import Counter

with open('/mnt/e/fairness-review-paper/literature-review-paper_v7/data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

N = 78

def studies_cancer_type(paper, patterns, negative_checks=None):
    """Check if a paper STUDIES a cancer type (not just mentions it)."""
    ct = str(paper.get('Cancer Type', '')).lower()
    title = str(paper.get('Paper Title', '')).lower()
    ds = str(paper.get('Dataset', '')).lower()
    kf = str(paper.get('Key Findings', '')).lower()
    combined = f"{ct} | {title} | {ds} | {kf}"
    
    for pat in patterns:
        if re.search(pat, combined, re.IGNORECASE):
            return True
    return False

# APPROACH 1: Count papers where the cancer type is EXPLICITLY in Cancer Type field
print("=" * 80)
print("APPROACH 1: Cancer Type field only (explicit mention)")
print("=" * 80)

ct_breast = [r'\bbreast\b', r'\bBRCA\b']
ct_prostate = [r'\bprostate\b', r'\bPRAD\b']
ct_skin = [r'\bmelanoma\b', r'\bmelanocytic\b', r'\bSKCM\b', r'basal cell carcinoma', r'squamous cell carcinoma', r'\bdermatolog']
ct_lung = [r'\blung\b', r'\bLUAD\b', r'\bLUSC\b', r'\bNSCLC\b']
ct_colorectal = [r'\bcolorectal\b', r'\bcoad\b', r'\bcoadread\b', r'\bcolon cancer\b']

counts_ct = {}
for name, patterns in [('Breast', ct_breast), ('Prostate', ct_prostate), ('Skin/Melanoma', ct_skin),
                        ('Lung', ct_lung), ('Colorectal', ct_colorectal)]:
    count = sum(1 for p in papers 
                if re.search('|'.join(patterns), str(p.get('Cancer Type', '')), re.IGNORECASE))
    counts_ct[name] = count
    print(f"  {name:<18s}: {count:3d} ({count/N*100:.1f}%)")

# Multi-cancer: CT field indicates multiple cancer types
multi_ct = sum(1 for p in papers 
               if any(x in str(p.get('Cancer Type', '')).lower() 
                     for x in ['pan-cancer', 'multiple cancer type', 'multi-organ', '33 cancer', '20 cancer', '14 cancer', 'six tumor',
                               '; breast;', '; lung;', '; prostate;', '; colorectal;', '; skin;', '; melanoma;']))
print(f"  Multi-cancer      : {multi_ct:3d} ({multi_ct/N*100:.1f}%)")

# APPROACH 2: Strict definition - cancer type is a primary study focus
# Papers about a SPECIFIC cancer type count, but papers with >3 cancer types are "multi-cancer" only
print()
print("=" * 80)
print("APPROACH 2: Strict primary (papers with 1-2 cancer types from CT field)")
print("=" * 80)
# Count cancer types mentioned in CT field per paper
ct_indicators = {
    'Breast': [r'\bbreast\b', r'\bbrca\b'],
    'Prostate': [r'\bprostate\b', r'\bprad\b'],
    'Skin': [r'\bmelanoma\b', r'\bmelanocytic\b', r'\bskcm\b', r'basal cell carcinoma', r'squamous cell carcinoma', r'\bdermatolog'],
    'Lung': [r'\blung\b', r'\bluad\b', r'\blusc\b', r'\bnsclc\b'],
    'Colorectal': [r'\bcolorectal\b', r'\bcoad\b', r'\bcoadread\b', r'\bcolon cancer\b', r'\brectal cancer\b'],
}

paper_types = []
for paper in papers:
    ct = str(paper.get('Cancer Type', '')).lower()
    found = []
    for name, patterns in ct_indicators.items():
        if any(re.search(p, ct) for p in patterns):
            found.append(name)
    paper_types.append((paper.get('Serial No.', '?'), found, ct[:80]))

strict_counts = Counter()
for sn, found, ct in paper_types:
    if len(found) >= 3:
        strict_counts['Multi-cancer'] += 1
    else:
        for f in found:
            strict_counts[f] += 1
    # Also: if CT says pan-cancer/multiple, count as multi
    if any(x in ct for x in ['pan-cancer', 'multiple cancer type', '33 cancer', '20 cancer', '14 cancer']):
        if 'Multi-cancer' not in [f for f in found if len(found) >= 3]:
            strict_counts['Multi-cancer'] += 1

for name in ['Breast', 'Prostate', 'Skin', 'Lung', 'Colorectal', 'Multi-cancer']:
    count = strict_counts.get(name, 0)
    print(f"  {name:<18s}: {count:3d} ({count/N*100:.1f}%)")

# APPROACH 3: Use Dataset-aware detection for primary study (paper explicitly tests on this cancer)
print()
print("=" * 80)
print("APPROACH 3: Dataset-aware primary study detection")
print("=" * 80)

def primary_study_breast(paper):
    ct = str(paper.get('Cancer Type', '')).lower()
    ds = str(paper.get('Dataset', '')).lower()
    title = str(paper.get('Paper Title', '')).lower()
    kf = str(paper.get('Key Findings', '')).lower()
    combined = f"{ct} | {ds} | {title} | {kf}"
    
    # Breast cancer studied if:
    # 1. Explicit breast/BRCA in Cancer Type field
    # 2. Uses breast-specific dataset (CAMELYON, BreakHis, etc.)
    if re.search(r'\bbreast\b|\bBRCA\b', ct):
        return True
    # Breast-specific datasets
    breast_ds = [r'\bCAMELYON\b', r'\bBreakHis\b', r'\bBACH\b', r'\bBreastPathQ\b', 
                 r'\bMITOS-ATYPIA\b', r'\bICIAR\b', r'\bBreastKf\b',
                 r'\bPACS04\b', r'\bPACS05\b', r'\bPACS08\b', r'\bNomorad\b', r'\bTIGER\b']
    for pat in breast_ds:
        if re.search(pat, ds, re.IGNORECASE):
            return True
    # 3. If multi-cancer and includes breast data
    if 'breast' in combined or 'brca' in combined:
        return True
    return False

def primary_study_lung(paper):
    ct = str(paper.get('Cancer Type', '')).lower()
    ds = str(paper.get('Dataset', '')).lower()
    title = str(paper.get('Paper Title', '')).lower()
    kf = str(paper.get('Key Findings', '')).lower()
    combined = f"{ct} | {ds} | {title} | {kf}"
    
    # Must have lung cancer SPECIFICALLY
    # Not just chest X-rays for general purposes unless using lung cancer datasets
    if re.search(r'\blung\b|\bLUAD\b|\bLUSC\b|\bNSCLC\b|\bpulmonary\b', combined):
        # But exclude papers where lung is only mentioned in passing
        # (e.g., "chest X-ray" alone without lung cancer context)
        if re.search(r'\blung cancer\b|\blung adenocarcinoma\b|\blung squamous\b|\bLUAD\b|\bLUSC\b|\bNSCLC\b', combined):
            return True
        # Chest X-ray papers are lung-related
        if re.search(r'\bchest\b.*\bx.?ray\b|\bchestx', combined):
            # Only count if specifically about lung disease/cancer
            if re.search(r'\bcancer\b|\bcarcinoma\b|\btumor\b|\bmalignan|\bneoplasm', combined):
                return True
            return False  # Generic chest X-ray papers don't count as lung cancer
    return False

counts_ds = Counter()
for name in ['Breast', 'Prostate', 'Skin', 'Lung', 'Colorectal']:
    counts_ds[name] = 0

for paper in papers:
    if primary_study_breast(paper): counts_ds['Breast'] += 1
    if re.search(r'\bprostate\b|\bPRAD\b', str(paper.get('Cancer Type', '')) + ' ' + str(paper.get('Dataset', '')), re.IGNORECASE):
        counts_ds['Prostate'] += 1
    if re.search(r'\bmelanoma\b|\bSKCM\b|\bdermatolog|\bdermatoscop|\bdermatopatholog|basal cell carcinoma|squamous cell carcinoma.*skin|fitzpatrick', 
                 str(paper.get('Cancer Type', '')) + ' ' + str(paper.get('Dataset', '')), re.IGNORECASE):
        counts_ds['Skin'] += 1
    if primary_study_lung(paper): counts_ds['Lung'] += 1
    if re.search(r'\bcolorectal\b|\bCOAD\b|\bCOADREAD\b|\bcolon cancer\b', str(paper.get('Cancer Type', '')) + ' ' + str(paper.get('Dataset', '')), re.IGNORECASE):
        counts_ds['Colorectal'] += 1

# Multi-cancer: papers studying 3+ cancer types
multi_count = 0
for paper in papers:
    ct = str(paper.get('Cancer Type', '')).lower()
    ds = str(paper.get('Dataset', '')).lower()
    title = str(paper.get('Paper Title', '')).lower()
    kf = str(paper.get('Key Findings', '')).lower()
    combined = f"{ct} | {ds} | {title} | {kf}"
    
    n_types = 0
    for name, patterns in [('B', [r'\bbreast\b|\bbrca\b|\bcamelyon\b']),
                           ('P', [r'\bprostate\b|\bprad\b']),
                           ('S', [r'\bmelanoma\b|\bskcm\b|\bdermatolog']),
                           ('L', [r'\blung\b|\bluad\b|\blusc\b|\bnsclc\b']),
                           ('C', [r'\bcolorectal\b|\bcoad\b|\bcoadread\b|\bcolon cancer\b'])]:
        if any(re.search(p, combined) for p in patterns):
            n_types += 1
    if n_types >= 3:
        multi_count += 1

counts_ds['Multi-cancer'] = multi_count

for name in ['Breast', 'Prostate', 'Skin', 'Lung', 'Colorectal', 'Multi-cancer']:
    count = counts_ds.get(name, 0) if name != 'Skin' else counts_ds.get('Skin', 0)
    print(f"  {name:<18s}: {count:3d} ({count/N*100:.1f}%)")

# APPROACH 4: Direct comparison
print()
print("=" * 80)
print("SUMMARY COMPARISON")
print("=" * 80)

claims_primary = [
    ('Breast', 44, 56.4),
    ('Multi-cancer', 24, 30.8),
    ('Prostate', 15, 19.2),
    ('Skin/Melanoma', 10, 12.8),
    ('Lung', 9, 11.5),
    ('Colorectal', 8, 10.3),
]

print(f"{'Cancer Type':<18s} {'Claim':>6s} {'CT_only':>8s} {'Strict':>8s} {'DS_aware':>8s}")
for label, claimed_n, claimed_pct in claims_primary:
    key = label.split('/')[0]
    ct_v = counts_ct.get(label if label == 'Multi-cancer' else key, 0)
    if label == 'Multi-cancer':
        ct_v = multi_ct
    strict_v = strict_counts.get(key if key != 'Skin/Melanoma' else 'Skin', 0)
    if label == 'Multi-cancer':
        strict_v = strict_counts.get('Multi-cancer', 0)
    ds_v = counts_ds.get(key if key != 'Skin/Melanoma' else 'Skin', 0)
    if label == 'Multi-cancer':
        ds_v = counts_ds.get('Multi-cancer', 0)
    print(f"  {label:<18s} {claimed_n:4d}    {ct_v:4d}      {strict_v:4d}      {ds_v:4d}")

print()
print("Closest match approach for each:")
print("  Breast:   CT-only=27, DS-aware=35, Claimed=44 → closest is DS-aware but still -9")
print("  Multi:    All approaches ~12-17, Claimed=24 → significant gap of -7 to -12")
print("  Prostate: DS-aware=14, Claimed=15 → close match")
print("  Skin:     DS-aware ~14, Claimed=10 → overcount by 4")
print("  Lung:     DS-aware=22 (strictest still >>9), Claimed=9 → huge overcount")
print("  CRC:      DS-aware=13, Claimed=8 → overcount by 5")
