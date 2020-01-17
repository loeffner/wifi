
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA


lab_vorne_file = 'lab_vorne.csv'
lab_hinten_file = 'lab_hinten.csv'
gang_lab_file = 'gang_lab.csv'
gang_hinten_file = 'gang_hinten.csv'
gang_notaus_file = 'gang_notaus.csv'
treppen_file = 'treppen.csv'

def plot_signals(data, bssids, ax=None, typ='bar', title='Wifi Localization', label='hello'):
    if typ == 'bar':
        for i, bssid in enumerate(bssids):
            plt.bar(i, -data[i], label=bssid)
        plt.title(title)
        plt.ylabel('Signal Strength')
        plt.xticks(range(len(bssids)), bssids, rotation='vertical')
        plt.subplots_adjust(bottom=0.3)
    elif typ == '2d':
        if not ax:
            print('For scatterplot please provide ax')
            return
        ax.scatter(data[:,0], data[:,1], alpha=0.5, label=label)
        ax.legend()
    elif typ == '3d':
        if not ax:
            print('For scatterplot please provide ax')
            return
        ax.scatter(data[:,0], data[:,1], data[:,2], alpha=0.5, label=label)
        ax.legend()

bssids = np.loadtxt('bssids.csv', dtype=str)

lab_vorne = np.loadtxt(lab_vorne_file, dtype=float)
lab_hinten = np.loadtxt(lab_hinten_file, dtype=float)
# lab = np.loadtxt(lab_file, dtype=float)
gang_lab = np.loadtxt(gang_lab_file, dtype=float)
gang_hinten = np.loadtxt(gang_hinten_file, dtype=float)
gang_notaus = np.loadtxt(gang_notaus_file, dtype=float)
treppen = np.loadtxt(treppen_file, dtype=float)

data = lab_vorne
data = np.append(data, lab_hinten, axis=0)
# data = np.append(data, np.loadtxt(lab_file, dtype=float), axis=0)
data = np.append(data, gang_lab, axis=0)
data = np.append(data, gang_hinten, axis=0)
data = np.append(data, gang_notaus, axis=0)
data = np.append(data, treppen, axis=0)

## 2d scatterplot
# pca = PCA(n_components=2)
# pca.fit(data)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# lab_vorne_pca = pca.transform(lab_vorne[::10])
# plot_signals(lab_vorne_pca, bssids, ax=ax, typ='2d', title='pca', label='lab_vorne')
# lab_hinten_pca = pca.transform(lab_hinten[::10])
# plot_signals(lab_hinten_pca, bssids, ax=ax, typ='2d', title='pca', label='lab_hinten')
# gang_lab_pca = pca.transform(gang_lab[::10])
# plot_signals(gang_lab_pca, bssids, ax=ax, typ='2d', title='pca', label='gang_lab')
# gang_notaus_pca = pca.transform(gang_notaus[::10])
# plot_signals(gang_notaus_pca, bssids, ax=ax, typ='2d', title='pca', label='gang_notaus')
# gang_hinten_pca = pca.transform(gang_hinten[::10])
# plot_signals(gang_hinten_pca, bssids, ax=ax, typ='2d', title='pca', label='gang_hinten')
# treppen_pca = pca.transform(treppen[::10])
# plot_signals(treppen_pca, bssids, ax=ax, typ='2d', title='pca', label='treppen')

## 3d Scatterplot
pca = PCA(n_components=3)
pca.fit(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lab_vorne_pca = pca.transform(lab_vorne[::10])
plot_signals(lab_vorne_pca, bssids, ax=ax, typ='3d', title='pca', label='lab_vorne')
lab_hinten_pca = pca.transform(lab_hinten[::10])
plot_signals(lab_hinten_pca, bssids, ax=ax, typ='3d', title='pca', label='lab_hinten')
gang_lab_pca = pca.transform(gang_lab[::10])
plot_signals(gang_lab_pca, bssids, ax=ax, typ='3d', title='pca', label='gang_lab')
gang_notaus_pca = pca.transform(gang_notaus[::10])
plot_signals(gang_notaus_pca, bssids, ax=ax, typ='3d', title='pca', label='gang_notaus')
gang_hinten_pca = pca.transform(gang_hinten[::10])
plot_signals(gang_hinten_pca, bssids, ax=ax, typ='3d', title='pca', label='gang_hinten')
treppen_pca = pca.transform(treppen[::10])
plot_signals(treppen_pca, bssids, ax=ax, typ='3d', title='pca', label='treppen')

## Barplot of Median
# plot_signals(np.median(lab_vorne, axis=0), bssids, title='lab_vorne')
# plt.figure()
# plot_signals(np.median(lab_hinten, axis=0), bssids, title='lab_hinten')
# plt.figure()
# plot_signals(np.median(gang_lab, axis=0), bssids, title='gang_lab')
# plt.figure()
# plot_signals(np.median(gang_hinten, axis=0), bssids, title='gang_hinten')
# plt.figure()
# plot_signals(np.median(gang_notaus, axis=0), bssids, title='gang_notaus')
# plt.figure()
# plot_signals(np.median(treppen, axis=0), bssids, title='treppen')

plt.show()