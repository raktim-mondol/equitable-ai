#!/usr/bin/env python3
"""Analyze cancer types across 78 experimental papers from experimental_78_paper.json."""

import json
import re
from collections import Counter, defaultdict

# Load the JSON
with open('/mnt/e/fairness-review-paper/literature-review-paper_v7/data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")
print()

# =====================================================================
# Helper: check if a text mentions a cancer type
# =====================================================================

def contains_breast(text):
    t = text.lower()
    return bool(re.search(r'\bbreast\b', t) or re.search(r'\bbrca\b', t))

def contains_prostate(text):
    t = text.lower()
    return bool(re.search(r'\bprostate\b', t) or re.search(r'\bprad\b', t))

def contains_skin(text):
    t = text.lower()
    patterns = [
        r'\bskin\b', r'\bmelanoma\b', r'\bmelanocytic\b', r'\bBCC\b',
        r'basal cell carcinoma', r'squamous cell carcinoma.*skin',
        r'dermatolog', r'dermatopatholog', r'dermatoscopic',
        r'\bnevus\b', r'\bnevi\b', r'\bSKCM\b',
        r'fitzpatrick', r'ISIC', r'cutaneous',
        r'\bHAM10000\b',
    ]
    return any(re.search(p, t, re.IGNORECASE) for p in patterns)

def contains_lung(text):
    t = text.lower()
    patterns = [
        r'\blung\b', r'\bLUAD\b', r'\bLUSC\b', r'\bNSCLC\b',
        r'pulmonary', r'lung adenocarcinoma', r'lung squamous',
        r'\bNLST\b', r'\bLIDC\b',
    ]
    return any(re.search(p, t, re.IGNORECASE) for p in patterns)

def contains_colorectal(text):
    t = text.lower()
    patterns = [
        r'\bcolorectal\b', r'\bcolon\b', r'\brectal\b',
        r'\bCOAD\b', r'\bREAD\b', r'\bCOADREAD\b', r'\bCRC\b',
        r'colorectal cancer', r'colon cancer', r'rectal cancer',
        r'\bpolyp\b', r'\bCCFR\b', r'NCT-CRC',
    ]
    return any(re.search(p, t, re.IGNORECASE) for p in patterns)

# =====================================================================
# Determine PRIMARY cancer type (most specific) -> one label per paper
# =====================================================================

def classify_primary(paper):
    """Classify the PRIMARY cancer type from the 'Cancer Type' field."""
    ct = paper.get('Cancer Type', '')
    ct_lower = ct.lower()

    # Check for explicit single cancer types
    if contains_breast(ct) and not any(x in ct_lower for x in ['multi', 'pan-cancer', 'multiple', 'general', 'not cancer']):
        # Check if it's breast-primary or multi
        other_cancers = ['lung', 'prostate', 'colorectal', 'colon', 'skin', 'melanoma', 'ovarian', 'bladder',
                          'pleural', 'kidney', 'renal', 'brain', 'thyroid', 'liver', 'stomach', 'head and neck',
                          'pancreatic', 'endometrial', 'cervical', 'esophagus']
        found_others = [o for o in other_cancers if o in ct_lower]
        if not found_others or all(o in ['luminal', 'invasive carcinoma'] for o in found_others):
            return 'Breast'

    if contains_lung(ct) and not any(x in ct_lower for x in ['multi', 'pan-cancer', 'multiple', 'general', 'not cancer']):
        other_cancers = ['breast', 'prostate', 'colorectal', 'colon', 'skin', 'melanoma', 'ovarian', 'bladder',
                          'pleural', 'kidney', 'renal', 'brain', 'thyroid', 'liver', 'stomach', 'head and neck']
        found_others = [o for o in other_cancers if o in ct_lower]
        if not found_others:
            return 'Lung'

    if contains_prostate(ct) and not any(x in ct_lower for x in ['multi', 'pan-cancer', 'multiple', 'general', 'not cancer']):
        other_cancers = ['breast', 'lung', 'colorectal', 'colon', 'skin', 'melanoma', 'ovarian', 'bladder',
                          'pleural', 'kidney', 'renal', 'brain']
        found_others = [o for o in other_cancers if o in ct_lower]
        if not found_others:
            return 'Prostate'

    if contains_skin(ct) and not any(x in ct_lower for x in ['multi', 'pan-cancer', 'multiple', 'general', 'not cancer']):
        return 'Skin/Melanoma'

    if contains_colorectal(ct) and not any(x in ct_lower for x in ['multi', 'pan-cancer', 'multiple', 'general', 'not cancer']):
        return 'Colorectal'

    # Check for multi-cancer / pan-cancer
    if any(x in ct_lower for x in ['multi', 'pan-cancer', 'multiple cancer', 'multiple (', 'several',
                                     'tumor types across', '33 cancer types']):
        return 'Multi-cancer'

    # Check for General / not cancer-specific
    if any(x in ct_lower for x in ['general', 'not cancer-specific', 'not reported']):
        return 'General/NR'

    # Other specific cancers
    if 'ovarian' in ct_lower:
        return 'Other (Ovarian)'
    if 'pancreatic' in ct_lower:
        return 'Other (Pancreatic)'
    if 'kidney' in ct_lower or 'renal' in ct_lower:
        return 'Other (Kidney/Renal)'

    # If no match, return raw
    if ct == 'Not Reported (NR)' or ct == '':
        return 'General/NR'

    return f'Other: {ct[:60]}'


# =====================================================================
# Classify ALL cancer types mentioned (non-exclusive)
# =====================================================================

def get_all_cancer_types(paper):
    """Get ALL cancer types mentioned in any relevant field."""
    fields_to_check = [
        paper.get('Cancer Type', ''),
        paper.get('Paper Title', ''),
        paper.get('Key Findings', ''),
        paper.get('Dataset', ''),
    ]
    # Also check Full BibTeX Reference for paper title data
    if 'Full BibTeX Reference' in paper:
        fields_to_check.append(paper.get('Full BibTeX Reference', ''))

    combined = ' '.join(fields_to_check)

    result = set()
    if contains_breast(combined):
        result.add('Breast')
    if contains_prostate(combined):
        result.add('Prostate')
    if contains_skin(combined):
        result.add('Skin/Melanoma')
    if contains_lung(combined):
        result.add('Lung')
    if contains_colorectal(combined):
        result.add('Colorectal')

    return result

# =====================================================================
# Analysis
# =====================================================================

print("=" * 80)
print("PAPER-BY-PAPER ANALYSIS")
print("=" * 80)

primary_counts = Counter()
all_mentions = Counter()
year_counts = Counter()
breast_primary_list = []
prostate_primary_list = []
skin_primary_list = []
lung_primary_list = []
colorectal_primary_list = []
multi_primary_list = []

for i, paper in enumerate(papers):
    sn = paper.get('Serial No.', '?')
    title = paper.get('Paper Title', 'N/A')
    year = paper.get('Year', 'Unknown')
    primary = classify_primary(paper)
    all_cancers = get_all_cancer_types(paper)

    primary_counts[primary] += 1
    year_counts[year] += 1

    for c in all_cancers:
        all_mentions[c] += 1

    if primary == 'Breast':
        breast_primary_list.append(sn)
    elif primary == 'Prostate':
        prostate_primary_list.append(sn)
    elif primary == 'Skin/Melanoma':
        skin_primary_list.append(sn)
    elif primary == 'Lung':
        lung_primary_list.append(sn)
    elif primary == 'Colorectal':
        colorectal_primary_list.append(sn)
    elif primary == 'Multi-cancer':
        multi_primary_list.append(sn)

    print(f"[{sn}] Year={year} | Primary: {primary:<25s} | All: {', '.join(sorted(all_cancers)) if all_cancers else 'None'}")
    print(f"     Cancer Type field: {paper.get('Cancer Type', 'N/A')[:100]}")
    print(f"     Title: {title[:100]}")
    print()

# =====================================================================
# SUMMARY
# =====================================================================

print()
print("=" * 80)
print("SUMMARY: PRIMARY CANCER TYPE COUNTS")
print("=" * 80)
for ct, count in primary_counts.most_common():
    pct = count / len(papers) * 100
    print(f"  {ct:<30s}: {count:3d} ({pct:.1f}%)")

print()
print("=" * 80)
print("SUMMARY: ALL CANCER TYPE MENTIONS (non-exclusive)")
print("=" * 80)
print(f"  Total papers: {len(papers)}")
for cancer in ['Breast', 'Prostate', 'Skin/Melanoma', 'Lung', 'Colorectal']:
    count = all_mentions.get(cancer, 0)
    pct = count / len(papers) * 100
    print(f"  {cancer:<15s}: {count:3d} ({pct:.1f}%)")

print()
print("=" * 80)
print("COMPARISON WITH CLAIMS")
print("=" * 80)
claims_primary = {
    'Breast': (44, 56.4),
    'Multi-cancer': (24, 30.8),
    'Prostate': (15, 19.2),
    'Skin/Melanoma': (10, 12.8),
    'Lung': (9, 11.5),
    'Colorectal': (8, 10.3),
}
claims_any = {
    'Lung': (28, 35.9),
    'Prostate': (21, 26.9),
    'Colorectal': (21, 26.9),
    'Skin/Melanoma': (13, 16.7),
}

print("\nPrimary focus:")
for cancer, (claimed_n, claimed_pct) in claims_primary.items():
    actual = primary_counts.get(cancer, 0)
    actual_pct = actual / len(papers) * 100
    diff = actual - claimed_n
    print(f"  {cancer:<20s}: Claimed={claimed_n} ({claimed_pct}%), Actual={actual} ({actual_pct:.1f}%), Diff={diff:+d}")

print("\nAny mention:")
for cancer, (claimed_n, claimed_pct) in claims_any.items():
    actual = all_mentions.get(cancer, 0)
    actual_pct = actual / len(papers) * 100
    diff = actual - claimed_n
    print(f"  {cancer:<20s}: Claimed={claimed_n} ({claimed_pct}%), Actual={actual} ({actual_pct:.1f}%), Diff={diff:+d}")

# Try to see if there's a looser definition that matches
print()
print("=" * 80)
print("LOOSER DEFINITIONS (using only Cancer Type field for 'primary')")
print("=" * 80)

def classify_primary_loose(paper):
    ct = paper.get('Cancer Type', '').lower()

    # Breast first
    if contains_breast(ct):
        # Also check if it's explicitly multi-cancer in the field
        other_indicators = contains_lung(ct) or contains_prostate(ct) or contains_skin(ct) or contains_colorectal(ct)
        # If the field says "breast; ..." with other cancers, it's multi
        if other_indicators and (';' in ct or ',' in ct or '/' in ct or '&' in ct):
            return 'Multi-cancer'
        return 'Breast'

    if any(x in ct for x in ['pan-cancer', 'multiple cancer type', 'multi-cancer', 'multiple (', 'multi-organ']):
        return 'Multi-cancer'

    # Check specific
    if contains_lung(ct):
        return 'Lung'
    if contains_prostate(ct):
        return 'Prostate'
    if contains_skin(ct):
        return 'Skin/Melanoma'
    if contains_colorectal(ct):
        return 'Colorectal'

    return 'Other/General'


# =====================================================================
# Print paper lists per primary type
# =====================================================================
print()
print("=" * 80)
print("PAPER SERIAL NUMBERS BY PRIMARY CANCER TYPE")
print("=" * 80)
print(f"Breast primary ({len(breast_primary_list)}): {breast_primary_list}")
print(f"Prostate primary ({len(prostate_primary_list)}): {prostate_primary_list}")
print(f"Skin/Melanoma primary ({len(skin_primary_list)}): {skin_primary_list}")
print(f"Lung primary ({len(lung_primary_list)}): {lung_primary_list}")
print(f"Colorectal primary ({len(colorectal_primary_list)}): {colorectal_primary_list}")
print(f"Multi-cancer primary ({len(multi_primary_list)}): {multi_primary_list}")

# Special: check multi-cancer papers for breast mentions
print()
print("=" * 80)
print("BREAST IN MULTI-CANCER PAPERS")
print("=" * 80)
for paper in papers:
    primary = classify_primary(paper)
    if primary == 'Multi-cancer':
        all_c = get_all_cancer_types(paper)
        if 'Breast' in all_c:
            print(f"  [{paper.get('Serial No.', '?')}] {paper.get('Paper Title', '')[:80]}")

# Year distribution
print()
print("=" * 80)
print("YEAR DISTRIBUTION")
print("=" * 80)
for year in sorted(year_counts.keys()):
    print(f"  {year}: {year_counts[year]} papers")

# Check: papers that have breast in all mentions but primary is NOT breast
print()
print("=" * 80)
print("BREAST MENTIONS (ALL fields) WHERE PRIMARY IS NOT BREAST")
print("=" * 80)
for paper in papers:
    primary = classify_primary(paper)
    all_c = get_all_cancer_types(paper)
    if 'Breast' in all_c and primary != 'Breast':
        print(f"  [{paper.get('Serial No.', '?')}] Primary={primary}: {paper.get('Paper Title', '')[:80]}")
        print(f"       Cancer Type field: {paper.get('Cancer Type', '')[:100]}")
