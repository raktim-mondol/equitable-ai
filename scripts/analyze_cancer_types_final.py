#!/usr/bin/env python3
"""
Final rigorous count: Count papers where each cancer type is STUDIED.
Uses Cancer Type field, Paper Title, Dataset, and Key Findings.
"""
import json, re
from collections import Counter

with open('/mnt/e/fairness-review-paper/literature-review-paper_v7/data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

N = len(papers)
print(f"Total papers: {N}")

def all_text(paper):
    fields = ['Cancer Type', 'Paper Title', 'Key Findings', 'Dataset', 'Full BibTeX Reference']
    return ' '.join(str(paper.get(f, '')) for f in fields)

# Searcher
def any_match(text, patterns):
    t = text.lower()
    return any(re.search(p, t, re.IGNORECASE) for p in patterns)

# Count per cancer type
results = {}
cancer_sns = {}

for name, patterns in [
    ('Breast', [r'\bbreast\b', r'\bBRCA\b', r'\bCAMELYON\b', r'\bBreakHis\b', r'\bBACH\b',
                 r'\bBreastPathQ\b', r'\bMITOS-ATYPIA\b', r'\bICIAR\b', r'\bBreastKf\b',
                 r'\bPACS04\b', r'\bPACS05\b', r'\bPACS08\b', r'\bNomorad\b']),
    ('Prostate', [r'\bprostate\b', r'\bPRAD\b', r'\bGleason\b']),
    ('Skin', [r'\bmelanoma\b', r'\bmelanocytic\b', r'\bdermatolog', r'\bdermatoscop', r'\bdermatopatholog',
              r'\bSKCM\b', r'\bfitzpatrick\b', r'basal cell carcinoma', r'cutaneous.*malignan',
              r'\bISIC\b', r'\bHAM10000\b', r'\bDermofit\b', r'\bPH2\b', r'\bnevus\b', r'\bnevi\b',
              r'skin.*(?:cancer|lesion|disease|tone)']),
    ('Lung', [r'\blung\b', r'\bLUAD\b', r'\bLUSC\b', r'\bNSCLC\b', r'\bpulmonary\b',
              r'chest.*x.?ray', r'\bchestx', r'\bChestXpert\b', r'\bLIDC\b', r'\bNLST\b']),
    ('Colorectal', [r'\bcolorectal\b', r'\bcoad\b', r'\bcoadread\b', r'\bcolon cancer\b', r'\brectal cancer\b',
                    r'\bCCFR\b', r'\bNCT-CRC\b']),
]:
    count = 0
    sns = []
    for p in papers:
        txt = all_text(p)
        if any_match(txt, patterns):
            count += 1
            sns.append(p.get('Serial No.', '?'))
    results[name] = count
    cancer_sns[name] = sns
    print(f"{name:<14s}: {count:3d} ({count/N*100:.1f}%)  SNs: {sns}")

# Multi-cancer: papers with 3+ of the above types studied
print()
multi_sns = []
for p in papers:
    txt = all_text(p)
    n_types = sum(1 for name in ['Breast','Prostate','Skin','Lung','Colorectal']
                  if any_match(txt, 
                    {'Breast': [r'\bbreast\b', r'\bBRCA\b', r'\bCAMELYON\b'],
                     'Prostate': [r'\bprostate\b', r'\bPRAD\b',],
                     'Skin': [r'\bmelanoma\b', r'\bdermatolog', r'\bSKCM\b',],
                     'Lung': [r'\blung\b', r'\bLUAD\b', r'\bLUSC\b', r'\bNSCLC\b',],
                     'Colorectal': [r'\bcolorectal\b', r'\bcoad\b', r'\bcolon cancer\b',]}[name]))
    if n_types >= 3:
        multi_sns.append(p.get('Serial No.', '?'))
    # Also: explicit pan-cancer / multi-organ in CT or Title
    ct = str(p.get('Cancer Type', '')).lower()
    title = str(p.get('Paper Title', '')).lower()
    if any(x in ct for x in ['pan-cancer', 'multiple cancer type', 'multi-organ', 
                               '33 cancer', '20 cancer', '14 cancer', 'six tumor',
                               'multiple organ', 'diverse organ']) and p.get('Serial No.') not in multi_sns:
        multi_sns.append(p.get('Serial No.', '?'))
    if ('multiple cancer' in title or 'pan-cancer' in title or 'multi-cancer' in title) and p.get('Serial No.') not in multi_sns:
        multi_sns.append(p.get('Serial No.', '?'))

multi_sns = sorted(set(multi_sns))
print(f"Multi-cancer     : {len(multi_sns):3d} ({len(multi_sns)/N*100:.1f}%)  SNs: {multi_sns}")

# =====================
# COMPARE
# =====================
print()
print("=" * 80)
print("COMPARISON WITH PAPER CLAIMS")
print("=" * 80)

claims = {
    'Breast': (44, 56.4),
    'Multi-cancer': (24, 30.8),
    'Prostate': (15, 19.2),
    'Skin/Melanoma': (10, 12.8),
    'Lung': (9, 11.5),
    'Colorectal': (8, 10.3),
}

name_map = {'Skin/Melanoma': 'Skin', 'Multi-cancer': 'Multi-cancer'}

print("\nPrimary focus (non-exclusive):")
for label, (claimed_n, claimed_pct) in claims.items():
    key = name_map.get(label, label)
    actual = len(multi_sns) if key == 'Multi-cancer' else results.get(key, 0)
    actual_pct = actual / N * 100
    diff = actual - claimed_n
    flag = ""
    if abs(diff) > 2:
        flag = f"  <<< DIFF={diff:+d}"
    print(f"  {label:<18s}: Claimed={claimed_n:3d} ({claimed_pct}%), Actual={actual:3d} ({actual_pct:.1f}%){flag}")

# Also show what the "any mention" from more fields would be
# Using key findings only
print()
print("\n'Any mention' using ALL fields including Key Findings & BibTeX:")

# For any mention, simply check ALL text including bias, limitations, etc.
for cancer_name, patterns in [
    ('Lung', [r'\blung\b', r'\bLUAD\b', r'\bLUSC\b', r'\bNSCLC\b', r'\bpulmonary\b',
              r'chest x.?ray', r'chestx', r'ChestXpert', r'LIDC', r'NLST']),
    ('Prostate', [r'\bprostate\b', r'\bPRAD\b']),
    ('Colorectal', [r'\bcolorectal\b', r'\bcoad\b', r'\bcoadread\b', r'\bcolon\b.*cancer',
                    r'\brectal\b.*cancer', r'\bCCFR\b']),
    ('Skin/Melanoma', [r'\bmelanoma\b', r'\bmelanocytic\b', r'\bdermatolog', r'\bSKCM\b',
                        r'\bfitzpatrick\b', r'basal cell carcinoma', r'cutaneous.*malignan']),
]:
    count = 0
    for p in papers:
        # Use EVERY field
        all_f = ' '.join(str(v) for v in p.values() if isinstance(v, str))
        if any_match(all_f, patterns):
            count += 1
    pct = count / N * 100
    print(f"  {cancer_name:<18s}: {count:3d} ({pct:.1f}%)")

# Year distribution
print()
print("=" * 80)
print("YEAR DISTRIBUTION")
print("=" * 80)
year_counts = Counter(p.get('Year', '?') for p in papers)
for yr in sorted(year_counts.keys()):
    print(f"  {yr}: {year_counts[yr]} papers")
print(f"  Total: {sum(year_counts.values())}")
