#!/usr/bin/env python3
"""
Bias-to-Mitigation Mapping Sankey Diagram
Source: Results Chapter (chapters/03_results.tex), 78 experimental studies
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import PathPatch, FancyArrowPatch
from matplotlib.path import Path
import numpy as np

# Set font to match paper style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 9
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 11

# Color palette for bias categories (left side)
bias_colors = {
    'Demographic': '#FF6B6B',
    'Representation': '#4ECDC4',
    'Confounding': '#45B7D1',
    'Selection/Sampling': '#FFA07A',
    'Class/Label': '#98D8C8',
    'Institutional/Batch': '#F7DC6F',
    'Technical/Domain Shift': '#BB8FCE',
    'Algorithmic': '#82E0AA'
}

# Color palette for mitigation families (right side)
mitigation_colors = {
    'Stain Normalization': '#E8DAEF',
    'Data Augmentation': '#D5F5E3',
    'Dataset Curation': '#FDEBD0',
    'Resampling': '#FADBD8',
    'Fairness-aware Learning': '#D6EAF8',
    'Domain Adaptation': '#F9E79F',
    'Adversarial Debiasing': '#EBDEF0',
    'SSL/Foundation': '#D7BDE2',
    'Federated Learning': '#A9DFBF',
    'Synthetic Data': '#AED6F1',
    'Continual Learning': '#F8C471',
    'Post-processing': '#F1948A',
    'Uncertainty Calibration': '#85C1E9',
    'Harmonisation': '#82E0AA',
    'Explanation Constraints': '#F5B7B1',
    'Advanced Stain': '#D2B4DE',
    'Physical Calibration': '#AED6F1'
}

# Sankey flow data: Bias Category → Mitigation Family → count
sankey_data = {
    'Demographic': {
        'Dataset Curation': 1,
        'Adversarial Debiasing': 1,
        'SSL/Foundation': 1,
        'Synthetic Data': 1,
        'Fairness-aware Learning': 3,
        'Post-processing': 1,
        'Explanation Constraints': 1,
        'Continual Learning': 1
    },
    'Representation': {
        'Dataset Curation': 3,
        'Synthetic Data': 2,
        'SSL/Foundation': 1,
        'Federated Learning': 1
    },
    'Confounding': {
        'Dataset Curation': 3,
        'Fairness-aware Learning': 1,
        'Adversarial Debiasing': 1,
        'Harmonisation': 1
    },
    'Selection/Sampling': {
        'Dataset Curation': 4,
        'Resampling': 1,
        'SSL/Foundation': 1,
        'Federated Learning': 2,
        'Synthetic Data': 1
    },
    'Class/Label': {
        'Dataset Curation': 1,
        'Resampling': 2,
        'Domain Adaptation': 1,
        'Uncertainty Calibration': 1,
        'Explanation Constraints': 2
    },
    'Institutional/Batch': {
        'Dataset Curation': 2,
        'Harmonisation': 2,
        'SSL/Foundation': 1,
        'Adversarial Debiasing': 1,
        'Federated Learning': 1,
        'Domain Adaptation': 1
    },
    'Technical/Domain Shift': {
        'Stain Normalization': 3,
        'Data Augmentation': 2,
        'Domain Adaptation': 2,
        'Advanced Stain': 1,
        'Physical Calibration': 1,
        'Uncertainty Calibration': 1,
        'Adversarial Debiasing': 1,
        'SSL/Foundation': 1
    },
    'Algorithmic': {
        'Dataset Curation': 1,
        'Fairness-aware Learning': 2,
        'Explanation Constraints': 1,
        'Uncertainty Calibration': 1,
        'Continual Learning': 1,
        'Post-processing': 1
    }
}

# Calculate totals
bias_totals = {}
for bias, mits in sankey_data.items():
    bias_totals[bias] = sum(mits.values())

mitigation_totals = {}
for bias, mits in sankey_data.items():
    for mit, count in mits.items():
        mitigation_totals[mit] = mitigation_totals.get(mit, 0) + count

# Order biases and mitigations
bias_order = [
    'Demographic',
    'Representation', 
    'Confounding',
    'Selection/Sampling',
    'Class/Label',
    'Institutional/Batch',
    'Technical/Domain Shift',
    'Algorithmic'
]

mitigation_order = [
    'Stain Normalization',
    'Data Augmentation',
    'Dataset Curation',
    'Resampling',
    'Fairness-aware Learning',
    'Domain Adaptation',
    'Adversarial Debiasing',
    'SSL/Foundation',
    'Federated Learning',
    'Synthetic Data',
    'Continual Learning',
    'Post-processing',
    'Uncertainty Calibration',
    'Harmonisation',
    'Explanation Constraints',
    'Advanced Stain',
    'Physical Calibration'
]

# Filter to only mitigations that have data
mitigation_order = [m for m in mitigation_order if m in mitigation_totals]

# Create figure
fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(7, 11.7, 'Bias-to-Mitigation Mapping in Histopathology AI Fairness', 
        fontsize=16, fontweight='bold', ha='center', va='top')
ax.text(7, 11.3, 'Source: Results Chapter • 78 experimental studies', 
        fontsize=10, ha='center', va='top', alpha=0.7)

# Layout parameters
left_x = 3
right_x = 11
bias_heights = {}
mitigation_heights = {}

# Calculate y-positions for bias categories (left)
total_bias = sum(bias_totals.values())
current_y = 10.5
for bias in bias_order:
    if bias in bias_totals:
        height = (bias_totals[bias] / total_bias) * 9
        bias_heights[bias] = {'y': current_y - height/2, 'height': height}
        current_y -= height + 0.15

# Calculate y-positions for mitigation families (right)
total_mitigation = sum(mitigation_totals.values())
current_y = 10.5
for mit in mitigation_order:
    if mit in mitigation_totals:
        height = (mitigation_totals[mit] / total_mitigation) * 9
        mitigation_heights[mit] = {'y': current_y - height/2, 'height': height}
        current_y -= height + 0.15

# Draw bias category boxes (left)
for bias in bias_order:
    if bias in bias_heights:
        info = bias_heights[bias]
        rect = mpatches.Rectangle(
            (left_x - 1.5, info['y']), 
            1.2, 
            info['height'],
            facecolor=bias_colors.get(bias, '#CCCCCC'),
            edgecolor='black',
            linewidth=1,
            alpha=0.85
        )
        ax.add_patch(rect)
        
        # Label with word wrapping
        label_text = bias.replace('/', '/\n').replace(' ', '\n')
        ax.text(left_x - 0.9, info['y'] + info['height']/2, 
                f'{bias}\n(n={bias_totals[bias]})',
                ha='center', va='center', fontsize=8, fontweight='bold')

# Draw mitigation family boxes (right)
for mit in mitigation_order:
    if mit in mitigation_heights:
        info = mitigation_heights[mit]
        rect = mpatches.Rectangle(
            (right_x, info['y']), 
            1.2, 
            info['height'],
            facecolor=mitigation_colors.get(mit, '#CCCCCC'),
            edgecolor='black',
            linewidth=1,
            alpha=0.85
        )
        ax.add_patch(rect)
        
        # Label
        ax.text(right_x + 0.6, info['y'] + info['height']/2, 
                f'{mit}\n(n={mitigation_totals[mit]})',
                ha='left', va='center', fontsize=8)

# Draw Sankey flows with curved paths
for bias in bias_order:
    if bias not in sankey_data:
        continue
    
    bias_info = bias_heights[bias]
    bias_y_start = bias_info['y'] + bias_info['height'] * 0.95
    flow_spacing = bias_info['height'] * 0.85 / sum(sankey_data[bias].values())
    
    # Sort mitigations by their y-position
    mits_for_bias = [(mit, count) for mit, count in sankey_data[bias].items() 
                     if mit in mitigation_heights]
    mits_for_bias.sort(key=lambda x: mitigation_heights[x[0]]['y'], reverse=True)
    
    current_offset = 0
    for mit, count in mits_for_bias:
        mit_info = mitigation_heights[mit]
        
        # Starting position on bias side
        start_y = bias_y_start - current_offset - flow_spacing * count / 2
        current_offset += flow_spacing * count
        
        # Ending position on mitigation side
        mit_flow_height = (count / mitigation_totals[mit]) * mit_info['height'] * 0.85
        mit_y_start = mit_info['y'] + mit_info['height'] * 0.95
        mit_y_offset = mit_info['height'] * 0.85 / mitigation_totals[mit]
        
        # Find position within mitigation box
        mit_counts = [(b, c) for b, mits in sankey_data.items() 
                      for mb, c in mits.items() if mb == mit]
        mit_total = sum(c for _, c in mit_counts)
        
        # Calculate cumulative position for this flow in mitigation
        cum_pos = 0
        for b, c in mit_counts:
            if b == bias:
                break
            cum_pos += mit_info['height'] * 0.85 * c / mit_total
        
        end_y = mit_y_start - cum_pos - mit_flow_height / 2
        
        # Create curved flow using quadratic Bezier approximation
        # Control points
        cp1_x = left_x + 0.8
        cp1_y = start_y
        cp2_x = right_x - 0.8
        cp2_y = end_y
        
        # Create path using cubic Bezier
        vertices = [
            (left_x, start_y),
            (cp1_x, cp1_y),
            (cp2_x, cp2_y),
            (right_x, end_y)
        ]
        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
        path = Path(vertices, codes)
        
        # Create flow with width proportional to count
        flow_width = max(0.08, count * 0.04)
        flow_path = PathPatch(path, facecolor=bias_colors.get(bias, '#CCCCCC'),
                              edgecolor='none', alpha=0.4, linewidth=0)
        ax.add_patch(flow_path)

# Add section labels
ax.text(left_x - 0.9, 10.8, 'Bias Categories', fontsize=11, fontweight='bold', ha='center')
ax.text(right_x + 0.6, 10.8, 'Mitigation Families', fontsize=11, fontweight='bold', ha='left')

# Add total count
ax.text(7, 0.3, f'Total flows: {total_bias} studies mapped to {len(mitigation_order)} mitigation strategies',
        fontsize=9, ha='center', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Save figure
output_path = '/mnt/e/fairness-review-paper/literature-review-paper_v8/figures/bias_sankey.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f'Sankey diagram saved to: {output_path}')

# Also save as PDF
pdf_path = '/mnt/e/fairness-review-paper/literature-review-paper_v8/figures/bias_sankey.pdf'
plt.savefig(pdf_path, bbox_inches='tight', facecolor='white')
print(f'PDF saved to: {pdf_path}')

print('Done!')
