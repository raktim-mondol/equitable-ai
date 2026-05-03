import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Figure setup — 300 DPI, print-quality
fig, ax = plt.subplots(figsize=(7.5, 6.5), dpi=300)

# ── Data ──────────────────────────────────────────
# Group 1: MGB-Lung
g1_x = [0.8, 1.2, 1.6]
g1_vals = [0.971, 0.920, 0.965]
# Group 2: TCGA-LUAD/LUSC
g2_x = [2.8, 3.2, 3.6]
g2_vals = [0.960, 0.950, 0.916]

# Colors from the style palette
TEAL    = '#2C6E7B'   # White / reference
CRIMSON = '#C44E52'   # Black
AMBER   = '#D4943A'   # Asian

# ── Bars ──────────────────────────────────────────
bar_w = 0.25
ax.bar(g1_x[0], g1_vals[0], width=bar_w, color=TEAL,    edgecolor='white', linewidth=0.4)
ax.bar(g1_x[1], g1_vals[1], width=bar_w, color=CRIMSON, edgecolor='white', linewidth=0.4)
ax.bar(g1_x[2], g1_vals[2], width=bar_w, color=AMBER,   edgecolor='white', linewidth=0.4)
ax.bar(g2_x[0], g2_vals[0], width=bar_w, color=TEAL,    edgecolor='white', linewidth=0.4)
ax.bar(g2_x[1], g2_vals[1], width=bar_w, color=CRIMSON, edgecolor='white', linewidth=0.4)
ax.bar(g2_x[2], g2_vals[2], width=bar_w, color=AMBER,   edgecolor='white', linewidth=0.4)

# ── Value labels above bars ────────────────────────
for x, val in zip(g1_x, g1_vals):
    ax.text(x, val + 0.002, f'{val:.3f}', ha='center', va='bottom', fontsize=9, color='#555555')
for x, val in zip(g2_x, g2_vals):
    ax.text(x, val + 0.002, f'{val:.3f}', ha='center', va='bottom', fontsize=9, color='#555555')

# ── Bar labels below bars ──────────────────────────
labels = ['White', 'Black', 'Asian', 'White', 'Black', 'Asian']
all_x = [0.8, 1.2, 1.6, 2.8, 3.2, 3.6]
for x, lbl in zip(all_x, labels):
    ax.text(x, 0.878, lbl, ha='center', va='top', fontsize=9, color='#666666')

# ── Cohort subtitles ───────────────────────────────
ax.text(1.2, 0.998, 'MGB-Lung', ha='center', va='bottom', fontsize=11, color='#555555')
ax.text(3.2, 0.998, 'TCGA-LUAD/LUSC', ha='center', va='bottom', fontsize=11, color='#555555')

# ── Δ arrows ───────────────────────────────────────
# Group 1: White → Black (5.1 pp)
y_arrow1 = 0.980
ax.annotate('', xy=(1.2, 0.922), xytext=(1.2, y_arrow1),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.2))
ax.plot([0.8, 1.2], [y_arrow1, y_arrow1], color='#555555', lw=1.2)
ax.text(1.0, 0.984, 'Δ = 5.1 pp', ha='center', va='bottom', fontsize=10, color='#333333', fontweight='bold')

# Group 2: White → Asian (4.4 pp)
y_arrow2 = 0.970
ax.annotate('', xy=(3.6, 0.918), xytext=(3.6, y_arrow2),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.2))
ax.plot([2.8, 3.6], [y_arrow2, y_arrow2], color='#555555', lw=1.2)
ax.text(3.2, 0.974, 'Δ = 4.4 pp', ha='center', va='bottom', fontsize=10, color='#333333', fontweight='bold')

# ── Axes ───────────────────────────────────────────
ax.set_ylim(0.88, 1.02)
ax.set_ylabel('TPR', fontsize=13, color='#333333', labelpad=6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#999999')
ax.spines['bottom'].set_color('#999999')
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)
ax.set_xticks([])  # no x ticks — labels are custom below bars
ax.tick_params(axis='y', labelsize=9, colors='#999999')

# ── Title + panel label ────────────────────────────
ax.text(0.5, 1.08, 'TPR Disparity by Race Group', ha='center', va='center',
        fontsize=14, fontweight='bold', color='#333333', transform=ax.transAxes)
ax.text(0.02, 1.08, 'A', ha='center', va='center',
        fontsize=14, fontweight='bold', color='#000000', transform=ax.transAxes)

# ── Task annotation ────────────────────────────────
ax.text(2.2, 0.888, 'Task: Lung cancer subtyping — distinguish LUAD from LUSC on WSIs',
        ha='center', va='top', fontsize=8, color='#999999', style='italic')

# ── Equation box ───────────────────────────────────
box_x, box_y, box_w, box_h = 0.25, 0.856, 4.7, 0.025
rect = FancyBboxPatch((box_x, box_y), box_w, box_h,
    boxstyle="round,pad=0.01", edgecolor='#D0D0D0', facecolor='#F0F5F5', lw=1.0,
    transform=ax.transData)
ax.add_patch(rect)
ax.text(box_x + 0.08, box_y + box_h/2, 'ΔTPR', ha='left', va='center',
        fontsize=9, color=TEAL, fontfamily='monospace', fontweight='bold',
        transform=ax.transData)
ax.text(box_x + 0.65, box_y + box_h/2, '= max  TPR  − min  TPR',
        ha='left', va='center', fontsize=9, color='#444444', fontfamily='monospace',
        transform=ax.transData)

# ── Save ───────────────────────────────────────────
plt.tight_layout(pad=0.5)
outpath = '/mnt/e/fairness-review-paper/literature-review-paper_v8/figures/idea/panel_A.png'
fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print(f'Saved → {outpath}')
