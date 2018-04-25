#!/usr/bin/python2.7
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as mpatches
import numpy as np

colors = [(1,1,1),(1,0.647,0),(0,1,0),(1,0,1)]
cmap_name = 'my_list'
cm = LinearSegmentedColormap.from_list(
    cmap_name, colors, N=4)
ar1 = ['3.0','7.4']
for v1 in ar1:
    ar2 = ['1', '2', '3', '4', '5', '6', '7', '8']
    for v2 in ar2:
        ar3 = ['a','b']
        for v3 in ar3:
            plt.rcParams["legend.fontsize"] = 15
            data = np.genfromtxt('it_matrix_{}_{}{}.dat'.format(v1,v2,v3))
            data_ref = np.genfromtxt('it_matrix_{}_1{}.dat'.format(v1,v3))
            fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14,7))
            axs[0].imshow(data, interpolation='nearest', cmap=cm, aspect='equal', origin='lower', vmin=0, vmax=3)
            axs[1].imshow(data_ref, interpolation='nearest', cmap=cm, aspect='equal', origin='lower', vmin=0, vmax=3)
            axs[0].set_title('pH {}, Run {}{}'.format(v1,v2,v3), size=20, weight='bold')
            axs[1].set_title('pH {}, Run 1{} Reference'.format(v1,v3), size=20, weight='bold')
            axs[0].set_xlabel('Residue Index', size=15, weight='bold')
            axs[1].set_xlabel('Residue Index', size=15, weight='bold')
            axs[0].set_ylabel('Residue Index', size=15, weight='bold')
            fig.tight_layout(pad=0.1)
            axs[0].set_xticks(np.arange(-0.5, 102, 10))
            axs[0].set_yticks(np.arange(-0.5, 102, 10))
            axs[0].set_xticklabels(np.arange(1, 103, 10), size=12, weight='bold')
            axs[0].set_yticklabels(np.arange(1, 103, 10), size=12, weight='bold')
            axs[1].set_yticklabels([])
            axs[1].set_yticks(np.arange(-0.5, 102, 10))
            axs[1].set_xticks(np.arange(-0.5, 102, 10))
            axs[1].set_xticklabels(np.arange(1, 103, 10), size=12, weight='bold')
            axs[0].grid(which='major', color='k', lw=0.2)
            axs[1].grid(which='major', color='k', lw=0.2)
            op = mpatches.Patch(color='orange', label='Hydrophobic')
            gp = mpatches.Patch(color='lime', label='H-bonds')
            mp = mpatches.Patch(color='magenta', label='Salt-Bridge')
            f = plt.legend(handles=[op,gp,mp],bbox_to_anchor=(1.05, 1), loc=2,
                       borderaxespad=0., frameon=False, title="Interaction Type")
            title = f.get_title()
            title.set_fontsize(15)
            title.set_fontweight('bold')
            plt.savefig("comparison_{}_{}{}.svg".format(v1,v2,v3), bbox_inches='tight')
            plt.close(fig)
