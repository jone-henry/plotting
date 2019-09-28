#!/usr/bin/python2.7
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

# Top level formatting
mpl.rcParams["legend.handletextpad"] = 0.3
mpl.rcParams["font.weight"] = 'demibold'

# Dark colors
COL1d='#0000b3'
COL2d='#b30000'
COL3d='#00b300'
# Light colors
COL1l='#6666ff'
COL2l='#ff6666'
COL3l='#66ff66'

# Note: Data needs to be in the following form
# 9 columns
# 8 rows
f1 = 'all_3.0_avg.dat.tac'
f2 = 'all_7.4_avg.dat.tac'
f3 = 'all_3.0_std.dat.tac'
f4 = 'all_7.4_std.dat.tac'

# Read in and unpack
a1, b1, c1, d1, e1, f1, g1, h1, i1 = np.genfromtxt(f1, unpack=True)
a2, b2, c2, d2, e2, f2, g2, h2, i2 = np.genfromtxt(f2, unpack=True)
a3, b3, c3, d3, e3, f3, g3, h3, i3 = np.genfromtxt(f3, unpack=True)
a4, b4, c4, d4, e4, f4, g4, h4, i4 = np.genfromtxt(f4, unpack=True)

# Some extra series for plotting
x = np.repeat(1,8)
y = np.arange(1,9)

# Make figure
# Minor formatting
fig, ax = plt.subplots(figsize=(22,17))
fig.tight_layout()
plt.subplots_adjust(top=0.8, bottom=0.45, hspace=0, wspace=0)

ax1 = plt.subplot(121)
# Manually set position
ax1.set_position([0.125, 0.45, 0.775, 0.35])
# HI data
# averages
# pH 3.0
ax1.scatter(x*1,   y, s=a1*4, c=COL1d) # Large circles for these scatter series
ax1.scatter(x*2.5, y, s=b1*4, c=COL2d)
ax1.scatter(x*4,   y, s=c1*4, c=COL3d)
# pH 7.4
ax1.scatter(x*16,   y, s=a2*4, c=COL1l)
ax1.scatter(x*17.5, y, s=b2*4, c=COL2l)
ax1.scatter(x*19,   y, s=c2*4, c=COL3l)
# stdev
# pH 3.0
ax1.scatter(x*1,   y+0.3, s=a3*4, c='k', marker='_') # Lines for these scatter series
ax1.scatter(x*2.5, y+0.3, s=b3*4, c='k', marker='_')
ax1.scatter(x*4,   y+0.3, s=c3*4, c='k', marker='_')
# pH 7.4
ax1.scatter(x*16,   y+0.3, s=a4*4, c='k', marker='_')
ax1.scatter(x*17.5, y+0.3, s=b4*4, c='k', marker='_')
ax1.scatter(x*19,   y+0.3, s=c4*4, c='k', marker='_')
# HB data
# averages
# pH 3.0
ax1.scatter(x*6,   y, s=d1*4, c=COL1d)
ax1.scatter(x*7.5, y, s=e1*4, c=COL2d)
ax1.scatter(x*9,   y, s=f1*4, c=COL3d)
# pH 7.4
ax1.scatter(x*20.5, y, s=d2*4, c=COL1l)
ax1.scatter(x*22,   y, s=e2*4, c=COL2l)
ax1.scatter(x*23.5, y, s=f2*4, c=COL3l)
# stdev
# pH 3.0
ax1.scatter(x*6,   y+0.3, s=d3*4, c='k', marker='_')
ax1.scatter(x*7.5, y+0.3, s=e3*4, c='k', marker='_')
ax1.scatter(x*9,   y+0.3, s=f3*4, c='k', marker='_')
# pH 7.4
ax1.scatter(x*20.5, y+0.3, s=d4*4, c='k', marker='_')
ax1.scatter(x*22,   y+0.3, s=e4*4, c='k', marker='_')
ax1.scatter(x*23.5, y+0.3, s=f4*4, c='k', marker='_')
# SB data
# averages
# pH 3.0
ax1.scatter(x*11,   y, s=g1*4, c=COL1d)
ax1.scatter(x*12.5, y, s=h1*4, c=COL2d)
ax1.scatter(x*14,   y, s=i1*4, c=COL3d)
# pH 7.4
ax1.scatter(x*25,   y, s=g2*4, c=COL1l)
ax1.scatter(x*26.5, y, s=h2*4, c=COL2l)
ax1.scatter(x*28,   y, s=i2*4, c=COL3l)
# stdev
# pH 3.0
ax1.scatter(x*11,   y+0.3, s=g3*4, c='k', marker='_')
ax1.scatter(x*12.5, y+0.3, s=h3*4, c='k', marker='_')
ax1.scatter(x*14,   y+0.3, s=i3*4, c='k', marker='_')
# pH 7.4
ax1.scatter(x*25,   y+0.3, s=g4*4, c='k', marker='_')
ax1.scatter(x*26.5, y+0.3, s=h4*4, c='k', marker='_')
ax1.scatter(x*28,   y+0.3, s=i4*4, c='k', marker='_')

# Format the Y axis
ytick_array  = ('AR','DR6','DR5','DR4','DR3','DR2','DR1','AI')
ytick_places = (1, 2, 3, 4, 5, 6, 7, 8)
plt.yticks(ytick_places, ytick_array, fontsize=20, fontweight='demibold')
plt.tick_params(axis='y', which='both', right=False, left=False, pad=20)
plt.ylim(0.5,8.5)

# Format X axis
xtick_array  = ('HI','HB','SB','HI','HB','SB')
xtick_places = (2.5, 7.5, 12.5, 17.5, 22, 26.5)
plt.xticks(xtick_places, xtick_array, fontsize=20, fontweight='demibold')
ax1.tick_params(axis='x', which='major', labeltop=False, labelbottom=True, top=False, bottom=False)
plt.xlim(0.5,28.5)

# Minor X ticks, but lines only, and extra long to be separators between series labels
ax1.set_xticks((1,4,6,9,11,14,16,19,20.5,23.5,25,28), minor=True)
ax1.tick_params(axis='x', which='minor', labelbottom=False, length=38, width=2, color='k')

# Format spines
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_linewidth(False)

# Manual legend making for part 1
# Empty scatter plot with various marker sizes
# Circles
l1a = plt.scatter([],[], s=120, c='k')
l1b = plt.scatter([],[], s=240, c='k')
l1c = plt.scatter([],[], s=360, c='k')
l1d = plt.scatter([],[], s=480, c='k')
# Lines
l2a = plt.scatter([],[], s=8,  c='k', marker='_')
l2b = plt.scatter([],[], s=16, c='k', marker='_')
l2c = plt.scatter([],[], s=24, c='k', marker='_')
# Empty scatter plot for sample code keys
# Dark
l3a = plt.scatter([],[], s=800, c=COL1l)
l3b = plt.scatter([],[], s=800, c=COL2l)
l3c = plt.scatter([],[], s=800, c=COL3l)
# Light
l4a = plt.scatter([],[], s=800, c=COL1d)
l4b = plt.scatter([],[], s=800, c=COL2d)
l4c = plt.scatter([],[], s=800, c=COL3d)
# Labels for hacked legend
labels1 = ["30", "60", "90", "120"]
labels2 = ["2","4","6"]
labels3 = [' ',' ',' ']
labels4 = [" "," "," "]

# Set legend properties
legend_properties = {'weight':'demibold',
                     'size':'20'}

# First manual legend
# For dot sizes
leg1 = plt.legend([l1a, l1b, l1c, l1d], labels1, ncol=4, frameon=False,
                  loc = 8,
                  prop=legend_properties,
                  bbox_to_anchor=([0.125, 0.33, 0.3875, 0.05]), bbox_transform=fig.transFigure,
                  title='Count', scatterpoints = 1)
plt.setp(leg1.get_title(),fontsize='20', fontweight='demibold')

# Second manual legend
# Line sizes
leg2 = plt.legend([l2a, l2b, l2c], labels2, ncol=3, frameon=False,
                  loc = 8,
                  prop=legend_properties,
                  bbox_to_anchor=([0.125, 0.28, 0.3875, 0.05]), bbox_transform=fig.transFigure,
                  title='Standard Deviation', scatterpoints = 1)
plt.setp(leg2.get_title(),fontsize='20', fontweight='demibold')

# Third manual legend
# Dark dots
leg3 = plt.legend([l3a, l3b, l3c], labels3, ncol=3, frameon=False,
                  loc = 8,
                  prop=legend_properties,
                  bbox_to_anchor=([0.5125, 0.28, 0.3875, 0.05]), bbox_transform=fig.transFigure,
                  scatterpoints = 1)
plt.setp(leg3.get_title(),fontsize='20', fontweight='demibold')

# Fourth manual legend
# Light dots
leg4 = plt.legend([l4a, l4b, l4c], labels4, ncol=3, frameon=False,
                  loc = 8,
                  prop=legend_properties,
                  bbox_to_anchor=([0.5125, 0.33, 0.3875, 0.05]), bbox_transform=fig.transFigure,
                  scatterpoints = 1)
plt.setp(leg4.get_title(),fontsize='20', fontweight='demibold')

# Have to re-add legends after multiple calls to plt.legend
ax1.add_artist(leg1)
ax1.add_artist(leg2)
ax1.add_artist(leg3)

# Add some text labels
plt.figtext(0.558, 0.345, 'pH 3.0',fontsize='20', fontweight='demibold')#, va='center', ha='center')
plt.figtext(0.558, 0.295, 'pH 7.4',fontsize='20', fontweight='demibold')#, va='center', ha='center')
plt.figtext(0.638, 0.255, 'A',fontsize='20', fontweight='demibold')#, va='center', ha='center')
plt.figtext(0.688, 0.255, 'B',fontsize='20', fontweight='demibold')#, va='center', ha='center')
plt.figtext(0.738, 0.255, 'I',fontsize='20', fontweight='demibold')#, va='center', ha='center')

plt.savefig('occurences_test.svg', format="svg")
plt.close()
