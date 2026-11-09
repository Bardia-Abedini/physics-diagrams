import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Arc
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'Liberation Serif', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'

# ---------- Figure 1: apparatus ----------
fig, ax = plt.subplots(figsize=(6.2, 4.0), dpi=200)
ax.set_aspect('equal'); ax.axis('off')
tx, top, bot = 0.0, 3.0, 0.6
ax.add_patch(Rectangle((tx - 0.12, bot), 0.24, top - bot, fill=False, lw=1.6))
ax.text(tx - 0.3, 1.1, 'glass tube', ha='right', va='center', fontsize=10)
th = np.radians(70.5); L = 4.2
mx, my = tx + L * np.sin(th), top - L * np.cos(th)
ax.plot([tx, tx], [top, -0.4], color='k', lw=1)          # thread down tube
ax.plot([tx, mx], [top, my], color='k', lw=1.2)          # thread to m
ax.add_patch(Rectangle((mx - 0.13, my - 0.18), 0.26, 0.36, color='0.35'))
ax.text(mx + 0.25, my, r'$m$ = 3 washers', va='center', fontsize=10)
ax.add_patch(Rectangle((tx - 0.22, -0.95), 0.44, 0.55, color='0.35'))
ax.text(tx + 0.35, -0.68, r'$M$ = 9 washers', va='center', fontsize=10)
# vertical reference + angle
ax.plot([tx, tx], [top, top + 0.0], color='k')
ax.plot([tx, tx], [top, top - 1.0], color='k', ls=':', lw=0.9)
ax.add_patch(Arc((tx, top), 1.3, 1.3, theta1=270, theta2=270 + 70.5, lw=1))
ax.text(tx + 0.25, top - 0.85, r'$\theta$', fontsize=12)
# L label
ax.text((tx + mx) / 2 + 0.1, (top + my) / 2 + 0.22, r'$L$', fontsize=13)
# R arrow
ax.annotate('', xy=(mx, my - 0.45), xytext=(tx, my - 0.45),
            arrowprops=dict(arrowstyle='<->', lw=1))
ax.plot([mx, mx], [my - 0.2, my - 0.55], color='k', lw=0.7)
ax.text((tx + mx) / 2, my - 0.75, r'$R$', ha='center', fontsize=13)
# circular path hint
ax.add_patch(matplotlib.patches.Ellipse((tx, my), 2 * (mx - tx), 0.5, fill=False, ls='--', lw=0.8))
ax.text(-3.2, my - 0.45, 'circular path', fontsize=9, ha='center')
ax.set_xlim(-4.6, 6.4); ax.set_ylim(-1.2, 3.4)
fig.tight_layout(); fig.savefig('phys_apparatus.png', bbox_inches='tight'); plt.close(fig)

# ---------- Figure 2: free body diagrams ----------
fig, axs = plt.subplots(1, 2, figsize=(6.2, 3.0), dpi=200)
for a in axs: a.set_aspect('equal'); a.axis('off'); a.set_xlim(-2, 2); a.set_ylim(-2, 2)
a = axs[0]
a.add_patch(Rectangle((-0.3, -0.3), 0.6, 0.6, color='0.35'))
a.annotate('', xy=(0, 1.6), xytext=(0, 0.3), arrowprops=dict(arrowstyle='-|>', lw=1.5, color='k'))
a.annotate('', xy=(0, -1.6), xytext=(0, -0.3), arrowprops=dict(arrowstyle='-|>', lw=1.5, color='k'))
a.text(0.15, 1.3, r'$F_T$', fontsize=13); a.text(0.15, -1.45, r'$F_g = Mg$', fontsize=13)
a.set_title('Hanging mass M', fontsize=11)
a = axs[1]
a.add_patch(Rectangle((-0.2, -0.2), 0.4, 0.4, color='0.35'))
ang = np.radians(70.5); Lv = 1.9
ex, ey = -Lv * np.sin(ang), Lv * np.cos(ang)
a.annotate('', xy=(ex, ey), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', lw=1.5, color='k'))
a.annotate('', xy=(0, -1.4), xytext=(0, -0.2), arrowprops=dict(arrowstyle='-|>', lw=1.5, color='k'))
a.plot([ex, ex], [0, ey], ls=':', color='0.4', lw=0.9); a.plot([ex, 0], [0, 0], ls=':', color='0.4', lw=0.9)
a.text(ex - 0.1, ey + 0.15, r'$F_T$', fontsize=13, ha='center')
a.text(0.15, -1.3, r'$F_g = mg$', fontsize=13)
a.text(ex / 2, -0.32, r'$F_T\sin\theta$', fontsize=10, ha='center')
a.text(ex - 0.1, ey / 2, r'$F_T\cos\theta$', fontsize=10, ha='right')
a.text(ex / 2, -0.62, '(toward centre)', fontsize=9, ha='center')
a.set_title('Orbiting mass m', fontsize=11)
fig.tight_layout(); fig.savefig('phys_fbd.png', bbox_inches='tight'); plt.close(fig)
print('ok')
