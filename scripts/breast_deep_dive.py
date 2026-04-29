#!/usr/bin/env python3
"""
Deep-dive: Check every paper for breast cancer.
Prints ALL papers with their breast-related evidence.
"""
import json, re

with open('/mnt/e/fairness-review-paper/literature-review-paper_v7/data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

# For each paper, extract breast evidence across ALL fields
print("=" * 120)
print("COMPLETE BREAST CANCER EVIDENCE PER PAPER")
print("=" * 120)

breast_patterns = [r'\bbreast\b', r'\bBRCA\b', r'\bCAMELYON\b', r'\bBreakHis\b', 
                   r'\bBACH\b', r'\bBreastPathQ\b', r'\bMITOS-ATYPIA\b', r'\bICIAR\b',
                   r'\bBreastKf\b', r'\bPACS04\b', r'\bPACS05\b', r'\bPACS08\b', r'\bNomorad\b',
                   r'\bTIGER\b', r'\bBHI\b', r'\bABCTB\b', r'\bMETABRIC\b']

breast_count = 0
for paper in papers:
    sn = paper.get('Serial No.', '?')
    ct = str(paper.get('Cancer Type', ''))
    ds = str(paper.get('Dataset', ''))
    title = str(paper.get('Paper Title', ''))
    kf = str(paper.get('Key Findings', ''))
    
    combined = f"{ct} {ds} {title} {kf}"
    combined_lower = combined.lower()
    
    matches = []
    for pat in breast_patterns:
        if re.search(pat, combined_lower):
            matches.append(pat)
    
    if matches:
        breast_count += 1
        # Find exact context
        contexts = []
        if 'breast' in combined_lower:
            for line in combined.split('. '):
                if 'breast' in line.lower() or 'brca' in line.lower():
                    contexts.append(line.strip()[:120])
        print(f"\n[{sn}] **BREAST** (CT: {ct[:80]})")
        print(f"  Dataset patterns: {sorted(set(m.replace(r'\\\\b', '').replace(r'\\\\', '').strip() for m in matches))}")
        for ctx in contexts[:3]:
            print(f"  Context: {ctx}")
    else:
        print(f"\n[{sn}] NO breast evidence found. CT: {ct[:80]}")
        # But check if TCGA pan-cancer → might include BRCA
        if 'tcga' in ct.lower() and ('33' in ct or 'multiple' in ct or 'pan-cancer' in ct):
            print(f"  NOTE: TCGA pan-cancer paper - BRCA likely included but not explicitly mentioned")
        if 'gynecological' in ct.lower():
            print(f"  NOTE: 'gynecological' cancers mentioned - may include breast")

print(f"\n\nTotal with breast evidence: {breast_count}/{len(papers)}")
