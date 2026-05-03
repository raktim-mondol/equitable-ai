import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ── Panel: 6.5 cm × 6.5 cm at 300 DPI ─────────────
CM = 1/2.54  # cm to inches
fig, ax = plt.subplots(figsize=(6.5*CM, 6.5*CM), dpi=300)

# ── Colours ───────────────────────────────────────
TEAL    = '#2C6E7B'
CRIMSON = '#C44E52'
AMBER   = '#D4943A'
GREY    = '#9E9E9E'

# ── Data ──────────────────────────────────────────
g1_vals = [0.971, 0.920, 0.965]   # MGB-Lung
g2_vals = [0.960, 0.950, 0.916]   # TCGA-LUAD/LUSC

# ── Bar positions ─────────────────────────────────
g1_x = [1.0, 2.0, 3.0]
g2_x = [4.5, 5.5, 6.5]
bar_w = 0.7

# ── Plot bars ─────────────────────────────────────
for x, v, c in [(g1_x[0], g1_vals[0], TEAL), (g1_x[1], g1_vals[1], CRIMSON), (g1_x[2], g1_vals[2], AMBER),
                (g2_x[0], g2_vals[0], TEAL), (g2_x[1], g2_vals[1], CRIMSON), (g2_x[2], g2_vals[2], AMBER)]:
    ax.bar(x, v, width=bar_w, color=c, linewidth=0.4, edgecolor='white')

# ── Value labels above bars (4 pt, #999999) ───────
for x, v in zip(g1_x, g1_vals):
    ax.text(x, v + 0.002, f'{v:.3f}', ha='center', va='bottom', fontsize=4, color='#999999')
for x, v in zip(g2_x, g2_vals):
    ax.text(x, v + 0.002, f'{v:.3f}', ha='center', va='bottom', fontsize=4, color='#999999')

# ── Bar labels below (5 pt, #666666) ──────────────
label_map = [(1.0, 'White'), (2.0, 'Black'), (3.0, 'Asian'),
             (4.5, 'White'), (5.5, 'Black'), (6.5, 'Asian')]
for x, lbl in label_map:
    ax.text(x, 0.8785, lbl, ha='center', va='top', fontsize=5, color='#666666')

# ── Cohort subtitles (5.5 pt, #666666) ────────────
ax.text(2.0, 0.999, 'MGB-Lung', ha='center', va='bottom', fontsize=5.5, color='#666666')
ax.text(5.5, 0.999, 'TCGA-LUAD/LUSC', ha='center', va='bottom', fontsize=5.5, color='#666666')

# ── Δ arrows ──────────────────────────────────────
# Group 1: White → Black
y_top1 = 0.986
ax.annotate('', xy=(2.0, g1_vals[1]+0.002), xytext=(2.0, y_top1),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=0.8))
ax.plot([g1_x[0], g1_x[1]], [y_top1, y_top1], color='#555555', lw=0.8, clip_on=False)
ax.text(1.5, y_top1 + 0.002, 'Δ = 5.1 pp', ha='center', va='bottom', fontsize=5, color='#444444')

# Group 2: White → Asian
y_top2 = 0.976
ax.annotate('', xy=(6.5, g2_vals[2]+0.002), xytext=(6.5, y_top2),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=0.8))
ax.plot([g2_x[0], g2_x[2]], [y_top2, y_top2], color='#555555', lw=0.8, clip_on=False)
ax.text(5.5, y_top2 + 0.002, 'Δ = 4.4 pp', ha='center', va='bottom', fontsize=5, color='#444444')

# ── Axes ──────────────────────────────────────────
ax.set_xlim(0.2, 7.3)
ax.set_ylim(0.88, 1.02)
ax.set_ylabel('TPR', fontsize=5.5, color='#666666', labelpad=3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(GREY)
ax.spines['bottom'].set_color(GREY)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)
ax.set_xticks([])
ax.tick_params(axis='y', labelsize=5, colors='#999999', pad=2)
ax.set_yticks([0.88, 0.90, 0.92, 0.94, 0.96, 0.98, 1.00])

# ── Title (7 pt bold, #333333) ────────────────────
ax.set_title('TPR Disparity by Race Group', fontsize=7, fontweight='bold',
             color='#333333', pad=8, loc='center')

# ── Panel label "A" (9 pt bold, black) ────────────
ax.text(0.02, 0.96, 'A', transform=ax.transAxes, fontsize=9, fontweight='bold',
        color='#000000', va='top', ha='left')

# ── Task annotation (4.5 pt italic, #999999) ──────
ax.text(3.75, 0.884, 'Task: Lung cancer subtyping — distinguish LUAD from LUSC on WSIs',
        ha='center', va='top', fontsize=4.5, color='#999999', style='italic')

# ── Equation box ──────────────────────────────────
bx, by = 0.6, 0.868
bw, bh = 6.2, 0.013
rect = FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.005",
    edgecolor='#D0D0D0', facecolor='#F0F5F5', lw=0.5, transform=ax.transData)
ax.add_patch(rect)
ax.text(bx + 0.15, by + bh/2, 'ΔTPR  =  max  TPR  −  min  TPR',
        ha='left', va='center', fontsize=6, color=TEAL, fontfamily='monospace',
        fontweight='bold', transform=ax.transData)

# ── Save ──────────────────────────────────────────
out = '/mnt/e/fairness-review-paper/literature-review-paper_v8/figures/idea/panel_A.png'
fig.savefig(out, dpi=300, facecolor='white', edgecolor='none', bbox_inches='tight',
            pad_inches=0.03)
# Re-open and force-crop to square
from PIL import Image
img = Image.open(out)
sz = max(img.size)
square = Image.new('RGB', (sz, sz), 'white')
square.paste(img, ((sz - img.size[0]) // 2, (sz - img.size[1]) // 2))
square.save(out, dpi=(300, 300))
w = sz / 300 * 2.54
print(f'Saved → {out}  ({sz}x{sz}px, {w:.1f}x{w:.1f} cm)')
