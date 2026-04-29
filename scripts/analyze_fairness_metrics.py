import json, re

with open('data/experimental_78_paper.json', 'r') as f:
    papers = json.load(f)

print(f'Total papers: {len(papers)}')
print()

# --- Patterns ---
accuracy_pat = re.compile(r'\b(?:test\s*)?accuracy\b', re.IGNORECASE)
auroc_pat = re.compile(
    r'\b(?:AUC[- ]?ROC|AUROC|AUC(?:\s*\(?ROC\)?)?|area\s+under\s+(?:the\s+)?'
    r'(?:receiver[-\s]?operating[-\s]?)?(?:ROC\s+)?curve)\b', re.IGNORECASE)
f1_pat = re.compile(r'\bF1[-\s]?(?:score)?\b', re.IGNORECASE)
sens_spec_pat = re.compile(
    r'\b(?:sensitivity|specificity|recall|True\s+Positive\s+Rate|TPR)\b', re.IGNORECASE)
bal_acc_pat = re.compile(r'\bbalanc(?:e|ed)\s*(?:d\s*)?accuracy\b', re.IGNORECASE)
cohen_pat = re.compile(r"\bCohen['\u2019]?s?\s*\u03ba\b|\bkappa\b", re.IGNORECASE)
worst_group_pat = re.compile(r'\bworst[-\s]?group\s*(?:accuracy|performance|error)\b', re.IGNORECASE)
ece_pat = re.compile(r'\bECE\b|Expected\s+Calibration\s+Error', re.IGNORECASE)
subgroup_cal_pat = re.compile(r'\bsubgroup\s+calibration\s+gap\b', re.IGNORECASE)

dem_parity_pat = re.compile(
    r'\b(?:Demographic|Statistical)\s+Parity\b', re.IGNORECASE)
eq_odds_pat = re.compile(r'\bEqualiz?ed\s+Odds?\b', re.IGNORECASE)
eq_opp_pat = re.compile(r'\bEqual\s+Opportunity\b', re.IGNORECASE)
tpr_fpr_disp_pat = re.compile(
    r'\b(?:TPR|FPR)\s*(?:Disparity|Difference|Gap)\b|'
    r'\bdisparit(?:y|ies)\s*in\s*(?:TPR|FPR|sensitivity|specificity)\b', re.IGNORECASE)
subgroup_auroc_pat = re.compile(
    r'\bsubgroup\s*[-\s]?AUROC\b|\bAUROC\s*disparity\b|'
    r'\bAUROC\s*(?:difference|gap)\s*(?:across|by|between)\s*(?:groups?|subgroups?)\b',
    re.IGNORECASE)
calibration_group_pat = re.compile(
    r'\bcalibrat(?:ion|ed)\s*(?:by|per|across)\s*(?:group|subgroup|demographic)\b|'
    r'\bgroup[-\s]?(?:wise|specific|level)\s+calibrat', re.IGNORECASE)
disp_imp_pat = re.compile(
    r'\b(?:disproportionality|dispar(?:ate|ity)\s*impact)\b', re.IGNORECASE)
spearman_fair_pat = re.compile(
    r'\bSpearman.*correlation.*(?:fairness|sample\s*size|age)\b|'
    r'\bPearson.*correlation.*(?:fairness|demographic|performance)\b', re.IGNORECASE)
diff_privacy_pat = re.compile(
    r'\bDifferential\s+Privacy\b|\bDP[-\s]SGD\b|'
    r'\bPrivacy\s*(?:Budget|Loss|Accountant|epsilon|guarantee)\b|'
    r'\bRényi\s+Differential\s+Privacy\b', re.IGNORECASE)

# Fairness mention patterns (broad)
fairness_mention_pat = re.compile(
    r'\b(?:fairness|disparity|disparate|demographic|subgroup|bias|equal|'
    r'privacy|differential|worst|calibration|correlation.*group|'
    r'TPR|FPR|group.*performance)\b', re.IGNORECASE)

counts = {
    'accuracy': 0, 'auroc': 0, 'f1': 0, 'sensitivity_specificity': 0,
    'balanced_accuracy': 0, 'cohen_kappa': 0,
    'worst_group_accuracy': 0, 'ece': 0, 'subgroup_calibration_gap': 0,
    'demographic_parity': 0, 'equalized_odds': 0, 'equal_opportunity': 0,
    'tpr_fpr_disparity': 0, 'subgroup_auroc_gap': 0,
    'calibration_by_group': 0, 'disparate_impact': 0,
    'spearman_correlation': 0, 'differential_privacy': 0,
}

papers_with_any_fairness = set()
fairness_paper_set = set()
any_fairness_keyword_set = set()

for i, p in enumerate(papers):
    fm = p.get('Fairness Metric', '')

    if accuracy_pat.search(fm):
        counts['accuracy'] += 1
    if auroc_pat.search(fm):
        counts['auroc'] += 1
    if f1_pat.search(fm):
        counts['f1'] += 1
    if sens_spec_pat.search(fm):
        counts['sensitivity_specificity'] += 1
    if bal_acc_pat.search(fm):
        counts['balanced_accuracy'] += 1
    if cohen_pat.search(fm):
        counts['cohen_kappa'] += 1

    is_fairness = False
    if worst_group_pat.search(fm):
        counts['worst_group_accuracy'] += 1
        is_fairness = True
    if ece_pat.search(fm):
        counts['ece'] += 1
        is_fairness = True
    if subgroup_cal_pat.search(fm):
        counts['subgroup_calibration_gap'] += 1
        is_fairness = True
    if dem_parity_pat.search(fm):
        counts['demographic_parity'] += 1
        is_fairness = True
    if eq_odds_pat.search(fm):
        counts['equalized_odds'] += 1
        is_fairness = True
    if eq_opp_pat.search(fm):
        counts['equal_opportunity'] += 1
        is_fairness = True
    if tpr_fpr_disp_pat.search(fm):
        counts['tpr_fpr_disparity'] += 1
        is_fairness = True
    if subgroup_auroc_pat.search(fm):
        counts['subgroup_auroc_gap'] += 1
        is_fairness = True
    if calibration_group_pat.search(fm):
        counts['calibration_by_group'] += 1
        is_fairness = True
    if disp_imp_pat.search(fm):
        counts['disparate_impact'] += 1
        is_fairness = True
    if spearman_fair_pat.search(fm):
        counts['spearman_correlation'] += 1
        is_fairness = True
    if diff_privacy_pat.search(fm):
        counts['differential_privacy'] += 1
        is_fairness = True

    if is_fairness:
        papers_with_any_fairness.add(i)

    if fairness_mention_pat.search(fm):
        fairness_paper_set.add(i)
        any_fairness_keyword_set.add(i)

# --- Results ---
print('=' * 70)
print('STANDARD METRICS')
print('=' * 70)
for m in ['accuracy', 'auroc', 'f1', 'sensitivity_specificity',
          'balanced_accuracy', 'cohen_kappa']:
    pct = counts[m] / 78 * 100
    print(f'  {m:<30s}: {counts[m]:>3d} / 78 = {pct:.1f}%')

print()
print('=' * 70)
print('FAIRNESS-SPECIFIC METRICS')
print('=' * 70)
for m in ['worst_group_accuracy', 'ece', 'subgroup_calibration_gap',
          'demographic_parity', 'equalized_odds', 'equal_opportunity',
          'tpr_fpr_disparity', 'subgroup_auroc_gap', 'calibration_by_group',
          'disparate_impact', 'spearman_correlation', 'differential_privacy']:
    pct = counts[m] / 78 * 100
    print(f'  {m:<30s}: {counts[m]:>3d} / 78 = {pct:.1f}%')

print()
print(f'Papers with STRICT fairness metrics: {len(papers_with_any_fairness)} / 78 '
      f'= {len(papers_with_any_fairness)/78*100:.1f}%')
print(f'Papers with BROAD fairness keywords: {len(fairness_paper_set)} / 78 '
      f'= {len(fairness_paper_set)/78*100:.1f}%')

# --- Detailed per-paper for fairness papers ---
print()
print('=' * 70)
print('PAPER-BY-PAPER: PAPERS WITH FAIRNESS KEYWORDS')
print('=' * 70)
for i in sorted(fairness_paper_set):
    p = papers[i]
    fm = p.get('Fairness Metric', '')
    # Detect which categories
    cats = []
    if worst_group_pat.search(fm): cats.append('worst-group')
    if ece_pat.search(fm): cats.append('ECE')
    if subgroup_cal_pat.search(fm): cats.append('subgroup-cal-gap')
    if dem_parity_pat.search(fm): cats.append('demographic-parity')
    if eq_odds_pat.search(fm): cats.append('equalized-odds')
    if eq_opp_pat.search(fm): cats.append('equal-opportunity')
    if tpr_fpr_disp_pat.search(fm): cats.append('tpr/fpr-disparity')
    if subgroup_auroc_pat.search(fm): cats.append('subgroup-auroc-gap')
    if calibration_group_pat.search(fm): cats.append('calibration-by-group')
    if disp_imp_pat.search(fm): cats.append('disparate-impact')
    if spearman_fair_pat.search(fm): cats.append('spearman-fairness')
    if diff_privacy_pat.search(fm): cats.append('differential-privacy')

    print(f'  [{i:>3d}] {p.get("Paper Title", "")[:80]}')
    if cats:
        print(f'        Categories: {", ".join(cats)}')
    print(f'        FM: {fm[:200]}')
    print()

# --- Comparison with claimed numbers ---
print()
print('=' * 70)
print('COMPARISON WITH CLAIMED VALUES IN RESULTS CHAPTER')
print('=' * 70)
comparisons = [
    ('Any fairness metric', 15, 19.2, len(papers_with_any_fairness)),
    ('Worst-group accuracy', 5, 6.4, counts['worst_group_accuracy']),
    ('ECE', 2, 2.6, counts['ece']),
    ('Subgroup calibration gap', 0, 0.0, counts['subgroup_calibration_gap']),
    ('Accuracy', 67, 85.9, counts['accuracy']),
    ('AUROC', 55, 70.5, counts['auroc']),
    ('F1', 33, 42.3, counts['f1']),
    ('Sensitivity/specificity', 31, 39.7, counts['sensitivity_specificity']),
    ('Balanced accuracy', 14, 17.9, counts['balanced_accuracy']),
    ("Cohen's kappa", 7, 9.0, counts['cohen_kappa']),
]

print(f'{"Metric":<30s} {"Claimed N":>9s} {"Claimed %":>8s} {"Our N":>6s} {"Our %":>6s} {"Match":>6s}')
print('-' * 70)
for name, claimed_n, claimed_pct, our_n in comparisons:
    our_pct = our_n / 78 * 100
    match = 'YES' if our_n == claimed_n else f'DIFF({our_n - claimed_n:+d})'
    print(f'{name:<30s} {claimed_n:>9d} {claimed_pct:>7.1f}% {our_n:>6d} {our_pct:>5.1f}% {match:>6s}')
