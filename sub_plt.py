#!/usr/bin/python2.7
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as mpatches
import numpy as np

### 3.0, A

ar2 = ['2', '3', '4', '5', '6', '7', '8']
for v2 in ar2:
    data = np.genfromtxt('it_matrix_3.0_{}a.dat'.format(v2))
    data_ref = np.genfromtxt('it_matrix_3.0_1a.dat'.format(v2))
    result = np.absolute(data - data_ref)

    colors = [(1,1,1),(1,0.647,0),(0,1,0),(1,0,1)]
    cmap_name = 'my_list'
    cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=4)
    plt.rcParams["legend.fontsize"] = 15
    fig, ax = plt.subplots(figsize=(7,7))
    ax.imshow(result, interpolation='nearest', cmap=cm, aspect='equal', origin='lower', vmin=0, vmax=3)
    ax.set_title('Sub. from Ref - pH 3.0, Run {}A'.format(v2), size=20, weight='bold')
    ax.set_xlabel('Residue Index', size=15, weight='bold')
    ax.set_ylabel('Residue Index', size=15, weight='bold')
    ax.set_xticks(np.arange(-0.5, 102, 10))
    ax.set_yticks(np.arange(-0.5, 102, 10))
    ax.set_xticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.set_yticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.grid(which='major', color='k', lw=0.2)
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
    op = mpatches.Patch(color='orange', label='Hydrophobic')
    gp = mpatches.Patch(color='lime', label='H-bonds')
    mp = mpatches.Patch(color='magenta', label='Salt-Bridge')
    f = plt.legend(handles=[op,gp,mp],bbox_to_anchor=(1.05, 1), loc=2,
                   borderaxespad=0., frameon=False, title="Interaction Type")
    title = f.get_title()
    title.set_fontsize(15)
    title.set_fontweight('bold')
    plt.savefig("subtraction_3.0_{}a.svg".format(v2), bbox_inches='tight')
    plt.close(fig)

### 3.0, B
    
ar2 = ['2', '3', '4', '5', '6', '7', '8']
for v2 in ar2:
    data = np.genfromtxt('it_matrix_3.0_{}b.dat'.format(v2))
    data_ref = np.genfromtxt('it_matrix_3.0_1b.dat'.format(v2))
    result = np.absolute(data - data_ref)

    colors = [(1,1,1),(1,0.647,0),(0,1,0),(1,0,1)]
    cmap_name = 'my_list'
    cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=4)
    plt.rcParams["legend.fontsize"] = 15
    fig, ax = plt.subplots(figsize=(7,7))
    ax.imshow(result, interpolation='nearest', cmap=cm, aspect='equal', origin='lower', vmin=0, vmax=3)
    ax.set_title('Sub. from Ref - pH 3.0, Run {}B'.format(v2), size=20, weight='bold')
    ax.set_xlabel('Residue Index', size=15, weight='bold')
    ax.set_ylabel('Residue Index', size=15, weight='bold')
    ax.set_xticks(np.arange(-0.5, 102, 10))
    ax.set_yticks(np.arange(-0.5, 102, 10))
    ax.set_xticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.set_yticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.grid(which='major', color='k', lw=0.2)
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
    op = mpatches.Patch(color='orange', label='Hydrophobic')
    gp = mpatches.Patch(color='lime', label='H-bonds')
    mp = mpatches.Patch(color='magenta', label='Salt-Bridge')
    f = plt.legend(handles=[op,gp,mp],bbox_to_anchor=(1.05, 1), loc=2,
                   borderaxespad=0., frameon=False, title="Interaction Type")
    title = f.get_title()
    title.set_fontsize(15)
    title.set_fontweight('bold')
    plt.savefig("subtraction_3.0_{}b.svg".format(v2), bbox_inches='tight')
    plt.close(fig)

### 7.4, B
    
ar2 = ['2', '3', '4', '5', '6', '7', '8']
for v2 in ar2:
    data = np.genfromtxt('it_matrix_7.4_{}a.dat'.format(v2))
    data_ref = np.genfromtxt('it_matrix_7.4_1a.dat'.format(v2))
    result = np.absolute(data - data_ref)

    colors = [(1,1,1),(1,0.647,0),(0,1,0),(1,0,1)]
    cmap_name = 'my_list'
    cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=4)
    plt.rcParams["legend.fontsize"] = 15
    fig, ax = plt.subplots(figsize=(7,7))
    ax.imshow(result, interpolation='nearest', cmap=cm, aspect='equal', origin='lower', vmin=0, vmax=3)
    ax.set_title('Sub. from Ref - pH 7.4, Run {}A'.format(v2), size=20, weight='bold')
    ax.set_xlabel('Residue Index', size=15, weight='bold')
    ax.set_ylabel('Residue Index', size=15, weight='bold')
    ax.set_xticks(np.arange(-0.5, 102, 10))
    ax.set_yticks(np.arange(-0.5, 102, 10))
    ax.set_xticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.set_yticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.grid(which='major', color='k', lw=0.2)
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
    op = mpatches.Patch(color='orange', label='Hydrophobic')
    gp = mpatches.Patch(color='lime', label='H-bonds')
    mp = mpatches.Patch(color='magenta', label='Salt-Bridge')
    f = plt.legend(handles=[op,gp,mp],bbox_to_anchor=(1.05, 1), loc=2,
                   borderaxespad=0., frameon=False, title="Interaction Type")
    title = f.get_title()
    title.set_fontsize(15)
    title.set_fontweight('bold')
    plt.savefig("subtraction_7.4_{}a.svg".format(v2), bbox_inches='tight')
    plt.close(fig)

### 7.4, B
    
ar2 = ['2', '3', '4', '5', '6', '7', '8']
for v2 in ar2:
    data = np.genfromtxt('it_matrix_7.4_{}b.dat'.format(v2))
    data_ref = np.genfromtxt('it_matrix_7.4_1b.dat'.format(v2))
    result = np.absolute(data - data_ref)

    colors = [(1,1,1),(1,0.647,0),(0,1,0),(1,0,1)]
    cmap_name = 'my_list'
    cm = LinearSegmentedColormap.from_list(
        cmap_name, colors, N=4)
    plt.rcParams["legend.fontsize"] = 15
    fig, ax = plt.subplots(figsize=(7,7))
    ax.imshow(result, interpolation='nearest', cmap=cm, aspect='equal', origin='lower', vmin=0, vmax=3)
    ax.set_title('Sub. from Ref - pH 7.4, Run {}B'.format(v2), size=20, weight='bold')
    ax.set_xlabel('Residue Index', size=15, weight='bold')
    ax.set_ylabel('Residue Index', size=15, weight='bold')
    ax.set_xticks(np.arange(-0.5, 102, 10))
    ax.set_yticks(np.arange(-0.5, 102, 10))
    ax.set_xticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.set_yticklabels(np.arange(1, 103, 10), size=12, weight='bold')
    ax.grid(which='major', color='k', lw=0.2)
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
    op = mpatches.Patch(color='orange', label='Hydrophobic')
    gp = mpatches.Patch(color='lime', label='H-bonds')
    mp = mpatches.Patch(color='magenta', label='Salt-Bridge')
    f = plt.legend(handles=[op,gp,mp],bbox_to_anchor=(1.05, 1), loc=2,
                   borderaxespad=0., frameon=False, title="Interaction Type")
    title = f.get_title()
    title.set_fontsize(15)
    title.set_fontweight('bold')
    plt.savefig("subtraction_7.4_{}b.svg".format(v2), bbox_inches='tight')
    plt.close(fig)
