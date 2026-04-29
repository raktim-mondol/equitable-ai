import json, re

with open('data/experimental_78_paper.json') as f:
    papers = json.load(f)

# --- COUNT ACTUAL METRICS MENTIONED IN "FAIRNESS METRIC" FIELD ---

# Fairness-specific keyword counts
fair_kw = {
    'demographic parity': 0,
    'equalized odds': 0,
    'equal opportunity': 0,
    'TPR/FPR disparity or gap': 0,
    'subgroup AUROC gap': 0,
    'calibration by group': 0,
    'worst-group accuracy/performance': 0,
    'ECE': 0,
    'AUROC gap/disparity': 0,
    'accuracy difference/gap': 0,
    'fairness gap': 0,
    'bias score/amplification': 0,
    'differential privacy': 0,
    'performance variance across groups': 0,
    'fairness tradeoff': 0,
    'AUC/F1 across subgroups': 0,
}

papers_with_fairness = []

for i, p in enumerate(papers):
    fm = p.get('Fairness Metric', '')
    fml = fm.lower()
    
    detected = []
    
    if re.search(r'demographic parity|statistical parity', fml):
        fair_kw['demographic parity'] += 1
        detected.append('demographic parity')
    if re.search(r'equalized odds', fml):
        fair_kw['equalized odds'] += 1
        detected.append('equalized odds')
    if re.search(r'equal opportunity', fml):
        fair_kw['equal opportunity'] += 1
        detected.append('equal opportunity')
    if re.search(r'(?:TPR|FPR|true positive rate|false positive rate).*(?:gap|disparity|difference|across|between)|\bdisparity\b.*\b(?:TPR|FPR|sensitivity|specificity)\b', fml):
        fair_kw['TPR/FPR disparity or gap'] += 1
        detected.append('TPR/FPR disparity or gap')
    if re.search(r'subgroup.*(?:AUROC|AUC)|(?:AUROC|AUC).*(?:gap|disparity|difference).*(?:subgroup|group|demographic)|race-wise.*AUC|AUC.*(?:parity|gap|disparity)', fml):
        fair_kw['subgroup AUROC gap'] += 1
        detected.append('subgroup AUROC gap')
    if re.search(r'calibrat.*(?:by|per|across).*(?:group|subgroup|demographic)|group.*calibrat', fml):
        fair_kw['calibration by group'] += 1
        detected.append('calibration by group')
    if re.search(r'worst.*group.*(?:accuracy|perform)|best.*worst.*subgroup', fml):
        fair_kw['worst-group accuracy/performance'] += 1
        detected.append('worst-group')
    if re.search(r'\bECE\b|expected calibration error', fml):
        fair_kw['ECE'] += 1
        detected.append('ECE')
    if re.search(r'AUROC.*gap|AUROC.*disparity|AUROC.*diff', fml):
        fair_kw['AUROC gap/disparity'] += 1
        detected.append('AUROC gap/disparity')
    if re.search(r'accuracy.*diff|accuracy.*gap|accuracy.*disparit', fml):
        fair_kw['accuracy difference/gap'] += 1
        detected.append('accuracy gap')
    if re.search(r'fairness.*gap|fairness.*trade', fml):
        fair_kw['fairness gap'] += 1
        detected.append('fairness gap')
    if re.search(r'fairness.*trade.?off|trade.?off.*fairness', fml):
        fair_kw['fairness tradeoff'] += 1
        detected.append('fairness tradeoff')
    if re.search(r'bias.*(?:score|amplification|index)|bias.*(?:mutual|quantif)', fml):
        fair_kw['bias score/amplification'] += 1
        detected.append('bias score')
    if re.search(r'differential privacy|dp-sgd|renyi.*privacy|privacy.*budget|privacy.*epsilon|privacy.*accountant', fml):
        fair_kw['differential privacy'] += 1
        detected.append('differential privacy')
    if re.search(r'(?:AUC|AUROC|F1).*across.*(?:group|subgroup|demographic)|(?:group|subgroup|demographic).*(?:AUC|AUROC|F1)', fml):
        fair_kw['AUC/F1 across subgroups'] += 1
        detected.append('AUC/F1 across subgroups')
    if re.search(r'performance.*variance|variance.*across.*(?:group|hospital|site)', fml):
        fair_kw['performance variance across groups'] += 1
        detected.append('performance variance')
    
    if detected:
        papers_with_fairness.append((i, p, detected))

print(f'Papers with any fairness-specific metric in FM field: {len(papers_with_fairness)}')
print()
print('FAIRNESS METRIC TYPE COUNTS')
for kw, cnt in sorted(fair_kw.items(), key=lambda x: -x[1]):
    if cnt > 0:
        print(f'  {kw:<35s}: {cnt:>3d} ({cnt/78*100:.1f}%)')
print()
print()

# List all 18 papers
print('DETAIL: PAPERS REPORTING FAIRNESS METRICS')
print('=' * 80)
for idx, p, cats in papers_with_fairness:
    print(f'  #{idx+1} [{p.get("Serial No.", 0):>3d}] {p.get("Paper Title","")[:80]}')
    print(f'       Cats: {", ".join(cats)}')
    print(f'       FM:   {p.get("Fairness Metric","")[:260]}')
    print()

# Now also check broader metrics that could be construed as fairness
print()
print('BORDERLINE FAIRNESS PAPERS (bias proxied via standard metrics)')
print('=' * 80)
borderline = []
for i, p in enumerate(papers):
    fm = p.get('Fairness Metric', '').lower()
    # these mention bias or group disparities but only report standard metrics
    is_borderline = False
    if any(w in fm for w in ['bias', 'fairness', 'disparity', 'subgroup', 'demographic', 'race', 'sex', 'age', 'group']) \
       and i not in [x[0] for x in papers_with_fairness]:
        borderline.append((i, p))

for idx, p in borderline:
    print(f'  #{idx+1} [{p.get("Serial No.", 0):>3d}] {p.get("Paper Title","")[:80]}')
    print(f'       FM: {p.get("Fairness Metric","")[:260]}')
    print()
