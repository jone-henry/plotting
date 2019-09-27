#!/usr/bin/python2.7
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import matplotlib as mpl

# Data set 1
pf1  = 'rmsf_plot/rmsf_3.0.a.feat.avg' # 8 cols x 5 rows
psf1 = 'rmsf_plot/rmsf_3.0.a.feat.std' # 8x5
pf2  = 'rmsf_plot/rmsf_3.0.b.feat.avg' # 8x5
psf2 = 'rmsf_plot/rmsf_3.0.b.feat.std' # 8x5
pf3  = 'rmsd_plot/all_rmsd_3.0.avg.trans' # 2x8
psf3 = 'rmsd_plot/all_rmsd_3.0.std.trans' # 2x8
pf4  = 'gyration_plot/all_gyrate_3.0.avg.trans' # 2x8
psf4 = 'gyration_plot/all_gyrate_3.0.std.trans' # 2x8

# Data set 2
pf5  = 'rmsf_plot/rmsf_7.4.a.feat.avg' # 8x5
psf5 = 'rmsf_plot/rmsf_7.4.a.feat.std' # 8x5
pf6  = 'rmsf_plot/rmsf_7.4.b.feat.avg' # 8x5
psf6 = 'rmsf_plot/rmsf_7.4.b.feat.std' # 8x5
pf7  = 'rmsd_plot/all_rmsd_7.4.avg.trans' # 2x8
psf7 = 'rmsd_plot/all_rmsd_7.4.std.trans' # 2x8
pf8  = 'gyration_plot/all_gyrate_7.4.avg.trans' # 2x8
psf8 = 'gyration_plot/all_gyrate_7.4.std.trans' # 2x8

# Reading in both data
a1,   b1,  c1,  d1,  e1,  f1,  g1,  h1 = np.genfromtxt(pf1,  unpack=True)
sa1, sb1, sc1, sd1, se1, sf1, sg1, sh1 = np.genfromtxt(psf1, unpack=True)
a2,   b2,  c2,  d2,  f2,  e2,  g2,  h2 = np.genfromtxt(pf2,  unpack=True)
sa2, sb2, sc2, sd2, se2, sf2, sg2, sh2 = np.genfromtxt(psf2, unpack=True)
a3,   b3 = np.genfromtxt(pf3,  unpack=True)
sa3, sb3 = np.genfromtxt(psf3, unpack=True)
a4,   b4 = np.genfromtxt(pf4,  unpack=True)
sa4, sb4 = np.genfromtxt(psf4, unpack=True)

a5,   b5,  c5,  d5,  e5,  f5,  g5,  h5 = np.genfromtxt(pf5,  unpack=True)
sa5, sb5, sc5, sd5, se5, sf5, sg5, sh5 = np.genfromtxt(psf5, unpack=True)
a6,   b6,  c6,  d6,  f6,  e6,  g6,  h6 = np.genfromtxt(pf6,  unpack=True)
sa6, sb6, sc6, sd6, se6, sf6, sg6, sh6 = np.genfromtxt(psf6, unpack=True)
a7,   b7 = np.genfromtxt(pf7,  unpack=True)
sa7, sb7 = np.genfromtxt(psf7, unpack=True)
a8,   b8 = np.genfromtxt(pf8,  unpack=True)
sa8, sb8 = np.genfromtxt(psf8, unpack=True)

# Color maps for RMSD, Rg
# Manual separation of first 16 colors of tab20
colors_1=(
        (0.1215686275, 0.4666666667, 0.7058823529, 1.0),
        (1.0000000000, 0.4980392157, 0.0549019608, 1.0),
        (0.1725490196, 0.6274509804, 0.1725490196, 1.0),
        (0.8392156863, 0.1529411765, 0.1568627451, 1.0),
        (0.5803921569, 0.4039215686, 0.7411764706, 1.0),
        (0.5490196078, 0.3372549020, 0.2941176471, 1.0),
        (0.8901960784, 0.4666666667, 0.7607843137, 1.0),
        (0.4980392157, 0.4980392157, 0.4980392157, 1.0))

colors_2=(
        (0.6823529411764706, 0.7803921568627451, 0.90980392156862740, 1.0),
        (1.0000000000000000, 0.7333333333333333, 0.47058823529411764, 1.0),
        (0.5960784313725490, 0.8745098039215686, 0.54117647058823530, 1.0),
        (1.0000000000000000, 0.5960784313725490, 0.58823529411764710, 1.0),
        (0.7725490196078432, 0.6901960784313725, 0.83529411764705890, 1.0),
        (0.7686274509803922, 0.6117647058823530, 0.58039215686274510, 1.0),
        (0.9686274509803922, 0.7137254901960784, 0.82352941176470580, 1.0),
        (0.7803921568627451, 0.7803921568627451, 0.78039215686274510, 1.0))

# Make the figure
fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(12,12))
plt.subplots_adjust(wspace=0.0, hspace=0.0, left=0.17, right=0.99, top=0.96, bottom=0.05)

# RMSF bar plot info
n_groups_1 = 5
bw  = 0.1
bw1 = bw*1
bw2 = bw*2
bw3 = bw*3
bw4 = bw*4
bw5 = bw*5
bw6 = bw*6
bw7 = bw*7
tickk = bw*3.5
index_1 = np.arange(n_groups_1)
tickarray_rmsf = ('Helix 1','Helix 2','Loop','Helix 3','Helix 4')

# Rg, RMSD bar plots info
n_groups_2 = 8
index_2    = np.arange(n_groups_2)
bw_2       = 0.3
bw1_2      = bw_2*1

# RMSF, 3.0, MA
ax1 = plt.subplot(421)
box1 = ax1.get_position() # Probably superflous
ax1.set_position([0.17, 0.76, 0.40, 0.20]) # Manually set plot position
# Plot each set of bars offset a bit so they aren't overlapping
# Set error bar line width, and color
# This should make a plot with no caps on the error bars if called as
# python2.7 plot.py
bar_a1 = plt.bar(index_1,       a1, bw, yerr=sa1, error_kw=dict(lw=1), ecolor='k') 
bar_b1 = plt.bar(index_1 + bw1, b1, bw, yerr=sb1, error_kw=dict(lw=1), ecolor='k')
bar_c1 = plt.bar(index_1 + bw2, c1, bw, yerr=sc1, error_kw=dict(lw=1), ecolor='k')
bar_d1 = plt.bar(index_1 + bw3, d1, bw, yerr=sd1, error_kw=dict(lw=1), ecolor='k')
bar_e1 = plt.bar(index_1 + bw4, e1, bw, yerr=se1, error_kw=dict(lw=1), ecolor='k')
bar_f1 = plt.bar(index_1 + bw5, f1, bw, yerr=sf1, error_kw=dict(lw=1), ecolor='k')
bar_g1 = plt.bar(index_1 + bw6, g1, bw, yerr=sg1, error_kw=dict(lw=1), ecolor='k')
bar_h1 = plt.bar(index_1 + bw7, h1, bw, yerr=sh1, error_kw=dict(lw=1), ecolor='k')
# Set axis limits
# Format the axes as needed
plt.ylim(0, 15)
plt.yticks(np.arange(0, 15, step=4), fontsize=13, fontweight='demibold')
plt.xlim(-0.3,5)
plt.xticks([], [])
ax1.tick_params(axis='y', width=1)

# RMSF, 3.0, MB
ax2 = plt.subplot(423)
box2 = ax2.get_position()
ax2.set_position([0.17, 0.55, 0.40, 0.20])
bar_a2 = plt.bar(index_1,       a2, bw, yerr=sa2, error_kw=dict(lw=1), ecolor='k')
bar_b2 = plt.bar(index_1 + bw1, b2, bw, yerr=sb2, error_kw=dict(lw=1), ecolor='k')
bar_c2 = plt.bar(index_1 + bw2, c2, bw, yerr=sc2, error_kw=dict(lw=1), ecolor='k')
bar_d2 = plt.bar(index_1 + bw3, d2, bw, yerr=sd2, error_kw=dict(lw=1), ecolor='k')
bar_e2 = plt.bar(index_1 + bw4, e2, bw, yerr=se2, error_kw=dict(lw=1), ecolor='k')
bar_f2 = plt.bar(index_1 + bw5, f2, bw, yerr=sf2, error_kw=dict(lw=1), ecolor='k')
bar_g2 = plt.bar(index_1 + bw6, g2, bw, yerr=sg2, error_kw=dict(lw=1), ecolor='k')
bar_h2 = plt.bar(index_1 + bw7, h2, bw, yerr=sh2, error_kw=dict(lw=1), ecolor='k')
plt.ylim(0, 15)
plt.yticks(np.arange(0, 15, step=4), fontsize=13, fontweight='demibold')
plt.xlim(-0.3,5)
plt.xticks(index_1 + tickk, tickarray_rmsf, fontsize=13, fontweight='demibold')
ax2.tick_params(axis='both', width=1)

# RMSD, 3.0
ax3 = plt.subplot(425)
box3 = ax3.get_position()
ax3.set_position([0.17, 0.35, 0.40, 0.15])
bar_b3 = plt.bar(index_2,         b3, bw_2, yerr=sb3, error_kw=dict(lw=1), ecolor='k', color=colors_1) # bb nl
bar_a3 = plt.bar(index_2 + bw1_2, a3, bw_2, yerr=sa3, error_kw=dict(lw=1), ecolor='k', color=colors_2) # bb
plt.ylim(0, 1)
plt.yticks(np.arange(0, 1, step=0.3), fontsize=13, fontweight='demibold')
plt.xticks([],[])
ax3.tick_params(axis='y', width=1)

# Rg, 3.0
ax4 = plt.subplot(427)
box4 = ax4.get_position()
ax4.set_position([0.17, 0.175, 0.40, 0.15])
bar_b4 = plt.bar(index_2,         b4, bw_2, yerr=sb4, error_kw=dict(lw=1), ecolor='k', color=colors_1) # bb nl
bar_a4 = plt.bar(index_2 + bw1_2, a4, bw_2, yerr=sa4, error_kw=dict(lw=1), ecolor='k', color=colors_2) # bb
plt.ylim(1, 2)
plt.yticks(np.arange(1, 2.001, step=0.3), fontsize=13, fontweight='demibold')
plt.xticks([],[])
ax4.tick_params(axis='y', width=1)

# RMSF, 7.4, MA
ax5 = plt.subplot(422)
box5 = ax5.get_position()
ax5.set_position([0.5900, 0.76, 0.40, 0.20])
bar_a5 = plt.bar(index_1,       a5, bw, yerr=sa5, error_kw=dict(lw=1), ecolor='k')
bar_b5 = plt.bar(index_1 + bw1, b5, bw, yerr=sb5, error_kw=dict(lw=1), ecolor='k')
bar_c5 = plt.bar(index_1 + bw2, c5, bw, yerr=sc5, error_kw=dict(lw=1), ecolor='k')
bar_d5 = plt.bar(index_1 + bw3, d5, bw, yerr=sd5, error_kw=dict(lw=1), ecolor='k')
bar_e5 = plt.bar(index_1 + bw4, e5, bw, yerr=se5, error_kw=dict(lw=1), ecolor='k')
bar_f5 = plt.bar(index_1 + bw5, f5, bw, yerr=sf5, error_kw=dict(lw=1), ecolor='k')
bar_g5 = plt.bar(index_1 + bw6, g5, bw, yerr=sg5, error_kw=dict(lw=1), ecolor='k')
bar_h5 = plt.bar(index_1 + bw7, h5, bw, yerr=sh5, error_kw=dict(lw=1), ecolor='k')
plt.ylim(0, 15)
plt.yticks([], [])
plt.xlim(-0.3,5)
plt.xticks([], [])

# RMSF, 7.4, MB
ax6 = plt.subplot(424)
box6 = ax6.get_position()
ax6.set_position([0.59, 0.55, 0.40, 0.20])
bar_a6 = plt.bar(index_1,       a6, bw, yerr=sa6, error_kw=dict(lw=1), ecolor='k')
bar_b6 = plt.bar(index_1 + bw1, b6, bw, yerr=sb6, error_kw=dict(lw=1), ecolor='k')
bar_c6 = plt.bar(index_1 + bw2, c6, bw, yerr=sc6, error_kw=dict(lw=1), ecolor='k')
bar_d6 = plt.bar(index_1 + bw3, d6, bw, yerr=sd6, error_kw=dict(lw=1), ecolor='k')
bar_e6 = plt.bar(index_1 + bw4, e6, bw, yerr=se6, error_kw=dict(lw=1), ecolor='k')
bar_f6 = plt.bar(index_1 + bw5, f6, bw, yerr=sf6, error_kw=dict(lw=1), ecolor='k')
bar_g6 = plt.bar(index_1 + bw6, g6, bw, yerr=sg6, error_kw=dict(lw=1), ecolor='k')
bar_h6 = plt.bar(index_1 + bw7, h6, bw, yerr=sh6, error_kw=dict(lw=1), ecolor='k')
plt.ylim(0, 15)
plt.yticks([], [])
plt.xlim(-0.3,5)
ax6.tick_params(axis='both', width=1)
plt.xticks(index_1 + tickk, tickarray_rmsf, fontsize=12, fontweight='demibold')

# RMSD, 7.4
ax7 = plt.subplot(426)
box7 = ax7.get_position()
ax7.set_position([0.59, 0.35, 0.40, 0.15])
bar_b7 = plt.bar(index_2,         b7, bw_2, yerr=sb7, error_kw=dict(lw=1), ecolor='k', color=colors_1) # bb nl
bar_a7 = plt.bar(index_2 + bw1_2, a7, bw_2, yerr=sa7, error_kw=dict(lw=1), ecolor='k', color=colors_2) # bb
plt.ylim(0, 1)
plt.yticks([], [])
plt.xticks([],[])

# Rg, 7.4
ax8 = plt.subplot(428)
box8 = ax8.get_position()
ax8.set_position([0.59, 0.175, 0.40, 0.15])
bar_b8 = plt.bar(index_2,         b8, bw_2, yerr=sb8, error_kw=dict(lw=1), ecolor='k', color=colors_1) # bb nl
bar_a8 = plt.bar(index_2 + bw1_2, a8, bw_2, yerr=sa8, error_kw=dict(lw=1), ecolor='k', color=colors_2) # bb
plt.ylim(1,2)
plt.yticks([], [])
plt.xticks([],[])
ax8.tick_params(axis='x', width=1)

## Titles ##
# Primary titles
plt.figtext(0.37, 0.98, 'pH 3.0',     va='center', ha='center', fontsize=20, fontweight='demibold')
plt.figtext(0.79, 0.98, 'pH 7.4',     va='center', ha='center', fontsize=20, fontweight='demibold')

# Y-labels
plt.figtext(0.075, 0.86,  'Monomer A', va='center', ha='center', fontsize=13, fontweight='demibold')
plt.figtext(0.075, 0.65,  'Monomer B', va='center', ha='center', fontsize=13, fontweight='demibold')
plt.figtext(0.075, 0.755, 'RMSF (nm)', va='center', ha='center', fontsize=13, fontweight='demibold')

plt.figtext(0.075, 0.425, 'RMSD (nm)', va='center', ha='center', fontsize=13, fontweight='demibold')
plt.figtext(0.075, 0.25,  'Rg (nm)',   va='center', ha='center', fontsize=13, fontweight='demibold')

# "Lines" for RMSF
fig.patches.extend([plt.Rectangle((0.075, 0.67), 0.000, 0.065,
                                  fill='none', color='k', linestyle='-',
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.075, 0.775), 0.000, 0.065,
                                  fill='none', color='k', linestyle='-',
                                  transform=fig.transFigure, figure=fig)])
# Format spines
for axis in ['top','right']:
    ax1.spines[axis].set_visible(False)
    ax2.spines[axis].set_visible(False)
    ax3.spines[axis].set_visible(False)
    ax4.spines[axis].set_visible(False)
    ax5.spines[axis].set_visible(False)
    ax6.spines[axis].set_visible(False)
    ax7.spines[axis].set_visible(False)
    ax8.spines[axis].set_visible(False)

for axis in ['bottom','left']:
    ax1.spines[axis].set_linewidth(1)
    ax2.spines[axis].set_linewidth(1)
    ax3.spines[axis].set_linewidth(1)
    ax4.spines[axis].set_linewidth(1)
    ax5.spines[axis].set_linewidth(1)
    ax6.spines[axis].set_linewidth(1)
    ax7.spines[axis].set_linewidth(1)
    ax8.spines[axis].set_linewidth(1)

## "Legend" components ##
# Labels
legend_label1 = "AI"
legend_label2 = "DR1"
legend_label3 = "DR2"
legend_label4 = "DR3"
legend_label5 = "DR4"
legend_label6 = "DR5"
legend_label7 = "DR6"
legend_label8 = "AR"

# Actual text
plt.text(0.3975, 0.085, legend_label1, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.4625, 0.085, legend_label2, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.5275, 0.085, legend_label3, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.5925, 0.085, legend_label4, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.6575, 0.085, legend_label5, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.7225, 0.085, legend_label6, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.7875, 0.085, legend_label7, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
plt.text(0.8525, 0.085, legend_label8, transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='center')
# More legend "labels"
plt.text(0.17, 0.1375, 'Backbone (no loop)', transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='left')
plt.text(0.17, 0.1125, 'Backbone (whole)'  , transform=fig.transFigure, fontweight='demibold', fontsize=15, va='center', ha='left')

# Regular color patches
fig.patches.extend([plt.Rectangle((0.375, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[0],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.44, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[1],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.505, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[2],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.57, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[3],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.635, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[4],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.7, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[5],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.765, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[6],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.830, 0.13), 0.045, 0.015,
                                  fill=True, color=colors_1[7],
                                  transform=fig.transFigure, figure=fig)])

# Light color patches
fig.patches.extend([plt.Rectangle((0.375, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[0],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.44, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[1],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.505, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[2],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.57, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[3],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.635, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[4],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.7, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[5],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.765, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[6],
                                  transform=fig.transFigure, figure=fig)])
fig.patches.extend([plt.Rectangle((0.83, 0.105), 0.045, 0.015,
                                  fill=True, color=colors_2[7],
                                  transform=fig.transFigure, figure=fig)])

# "Line"
fig.patches.extend([plt.Rectangle((0.17, 0.125), 0.705, 0.000,
                                  fill='none', color='0.65', linestyle='--',
                                  transform=fig.transFigure, figure=fig)])


plt.savefig('new_draft.svg', format="svg")
plt.close()

