#!/usr/bin/python2.7
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

mpl.rcParams["legend.handletextpad"] = 0.2
mpl.rcParams["font.weight"] = 'demibold'

COL1='#0000ff'
COL2='#ff0000'
COL3='#007f00'

f1 = 'plot_3.0_avg.dat'
f2 = 'plot_7.4_avg.dat'
f3 = 'plot_3.0_std.dat'
f4 = 'plot_7.4_std.dat'

y, x, a1, b1, c1, d1, e1, f1, g1, h1, i1 = np.genfromtxt(f1, unpack=True)
y, x, a2, b2, c2, d2, e2, f2, g2, h2, i2 = np.genfromtxt(f2, unpack=True)
y, x, a3, b3, c3, d3, e3, f3, g3, h3, i3 = np.genfromtxt(f3, unpack=True)
y, x, a4, b4, c4, d4, e4, f4, g4, h4, i4 = np.genfromtxt(f4, unpack=True)

fig, ax = plt.subplots(figsize=(22,17))

# 7.4, HI data
# averages
ax.scatter(x, y*1,   s=a2*4, c=COL1)
ax.scatter(x, y*2.5, s=b2*4, c=COL2)
ax.scatter(x, y*4,   s=c2*4, c=COL3)
# stdev
ax.scatter(x, y*1.5, s=a4*4, c='k', marker='_')
ax.scatter(x, y*3,   s=b4*4, c='k', marker='_')
ax.scatter(x, y*4.5, s=c4*4, c='k', marker='_')

# 7.4, HB data
# averages
ax.scatter(x, y*6,   s=d2*4, c=COL1)
ax.scatter(x, y*7.5, s=e2*4, c=COL2)
ax.scatter(x, y*9,   s=f2*4, c=COL3)
# stdev
ax.scatter(x, y*6.5, s=d4*4, c='k', marker='_')
ax.scatter(x, y*8,   s=e4*4, c='k', marker='_')
ax.scatter(x, y*9.5, s=f4*4, c='k', marker='_')

# 7.4, SB data
# averages
ax.scatter(x, y*11,   s=g2*4, c=COL1)
ax.scatter(x, y*12.5, s=h2*4, c=COL2)
ax.scatter(x, y*14,   s=i2*4, c=COL3)
#stdev
ax.scatter(x, y*11.5, s=g4*4, c='k', marker='_')
ax.scatter(x, y*13,   s=h4*4, c='k', marker='_')
ax.scatter(x, y*14.5, s=i4*4, c='k', marker='_')

# 3.0, HI data
# averages
ax.scatter(x, y*16,   s=a1*4, c=COL1)
ax.scatter(x, y*17.5, s=b1*4, c=COL2)
ax.scatter(x, y*19,   s=c1*4, c=COL3)
# stdev
ax.scatter(x, y*16.5, s=a3*4, c='k', marker='_')
ax.scatter(x, y*18,   s=b3*4, c='k', marker='_')
ax.scatter(x, y*19.5, s=c3*4, c='k', marker='_')

# 3.0, HB data
# averages
ax.scatter(x, y*21,   s=d1*4, c=COL1)
ax.scatter(x, y*22.5, s=e1*4, c=COL2)
ax.scatter(x, y*24,   s=f1*4, c=COL3)
# stdev
ax.scatter(x, y*21.5, s=d3*4, c='k', marker='_')
ax.scatter(x, y*23,   s=e3*4, c='k', marker='_')
ax.scatter(x, y*24.5, s=f3*4, c='k', marker='_')

# 3.0, SB data
# averages
ax.scatter(x, y*26,   s=g1*4, c=COL1)
ax.scatter(x, y*27.5, s=h1*4, c=COL2)
ax.scatter(x, y*29,   s=i1*4, c=COL3)
#stdev
ax.scatter(x, y*26.5, s=g3*4, c='k', marker='_')
ax.scatter(x, y*28,   s=h3*4, c='k', marker='_')
ax.scatter(x, y*29.5, s=i3*4, c='k', marker='_')

box = ax.get_position()
ax.set_position([0.2, 0.2, 0.25, 0.80])

tick_array = ('A','B','I','A','B','I','A','B','I','A','B','I','A','B','I','A','B','I',)
tick_places = (1, 2.5, 4, 6, 7.5, 9, 11, 12.5, 14, 16, 17.5, 19, 21, 22.5, 24, 26, 27.5, 29)
plt.yticks(tick_places, tick_array, fontsize=20, fontweight='demibold')
plt.tick_params(axis='y', which='both', right=False, left=False)
plt.ylim(0,30)
for tick in ax.yaxis.get_minor_ticks():
        tick.label1.set_horizontalalignment('center')

plt.axhline(5,   xmin=-0.2, linestyle='--', c='0.5', linewidth=2, clip_on=False)
plt.axhline(10,  xmin=-0.2, linestyle='--', c='0.5', linewidth=2, clip_on=False)
plt.axhline(15,  xmin=-0.35, linestyle='-',  c='0.5', linewidth=2, clip_on=False)
plt.axhline(20,  xmin=-0.2, linestyle='--', c='0.5', linewidth=2, clip_on=False)
plt.axhline(25,  xmin=-0.2, linestyle='--', c='0.5', linewidth=2, clip_on=False)

# special ticking for x axis
tickarray_2=('DR1','DR3','DR5','AR')
tickarray_1=('AI','DR2','DR4','DR6')
plt.xticks(np.arange(1, 9, step=2), tickarray_1, fontweight='demibold', rotation=0, fontsize=20)
minorLocator = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minorLocator)
ax.set_xticklabels(tickarray_2, minor=True, fontweight='demibold')
ax.tick_params(which='major', width=2.00, length=5)
ax.tick_params(which='minor', width=2.00, length=35, labelsize=20)

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(2.0)

# manual legend making
l1a = plt.scatter([],[], s=120, c='k')
l1b = plt.scatter([],[], s=240, c='k')
l1c = plt.scatter([],[], s=360, c='k')
l1d = plt.scatter([],[], s=480, c='k')

l2a = plt.scatter([],[], s=20, c='k', marker='_')
l2b = plt.scatter([],[], s=40, c='k', marker='_')
l2c = plt.scatter([],[], s=60, c='k', marker='_')

labels1 = ["30", "60", "90", "120"]
labels2 = ["5","10","15"]

legend_properties = {'weight':'demibold',
                     'size':'20'}

leg1 = plt.legend([l1a, l1b, l1c, l1d], labels1, ncol=4, frameon=False,
                  loc = 8,
                  prop=legend_properties,
                  bbox_to_anchor=([0.2, 0.07, 0.25, 0.2]), bbox_transform=fig.transFigure,
                  title='Contacts Count', scatterpoints = 1)
plt.setp(leg1.get_title(),fontsize='20', fontweight='demibold')

leg2 = plt.legend([l2a, l2b, l2c], labels2, ncol=3, frameon=False,
                  loc = 8,
                  prop=legend_properties,
                  bbox_to_anchor=([0.2, 0.02, 0.25, 0.2]), bbox_transform=fig.transFigure,
                  title='Standard Deviation', scatterpoints = 1)
plt.setp(leg2.get_title(),fontsize='20', fontweight='demibold')

ax.add_artist(leg1)

# adding secondary, tertiary y axis labels
# places calculation
#p_1 = (((2.343/31) * 0.8) + 0.2)
#plt.figtext(0.18, p_1, 'Test', fontsize=20)
#p_2 = (((7.343/31) * 0.8) + 0.2)
#plt.figtext(0.18, p_2, 'Test', fontsize=20)

ax2 = ax.twinx()
ax2.set_position([0.2, 0.2, 0.25, 0.80])
plt.ylim(0,30)
tick_array_2 = ('HI','HB','SB','HI','HB','SB')
tick_places_2 = (2.5, 7.5, 12.5, 17.5, 22.5, 27.5)
plt.yticks(tick_places_2, tick_array_2, fontsize=20, fontweight='demibold')
plt.tick_params(axis='y', which='both', right=False, left=False)
for tick in ax2.yaxis.get_minor_ticks():
        tick.label1.set_horizontalalignment('center')
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.yaxis.tick_left()
ax2.tick_params(axis='y', which='major', pad=45)

ax3 = ax.twinx()
ax3.set_position([0.2, 0.2, 0.25, 0.80])
plt.ylim(0,30)
tick_array_3 = ('7.4','pH','3.0','pH')
tick_places_3 = (7, 8, 22, 23)
plt.yticks(tick_places_3, tick_array_3, fontsize=20, fontweight='demibold')
plt.tick_params(axis='y', which='both', right=False, left=False)
for tick in ax3.yaxis.get_minor_ticks():
        tick.label1.set_horizontalalignment('center')
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.yaxis.tick_left()
ax3.tick_params(axis='y', which='major', pad=100)

plt.savefig('test.svg', format="svg")
plt.close()
