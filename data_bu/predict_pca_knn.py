import subprocess
import random
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

# Never hardcode your password!
sudo_pass = '45AM15lr3990'
interface = 'wlx74da38ef3fbd'
# interface = 'wlp59s0'
# iwlist cmd
cmd = 'sudo iwlist ' + interface + ' scan'

amur = '34:41:5D:9E:EF:2B'
taswlan = '80:1F:02:EE:3B:0F'

lab_vorne_file = 'lab_vorne.csv'
lab_hinten_file = 'lab_hinten.csv'
lab_file = 'lab.csv'
gang_lab_file = 'gang_lab.csv'
gang_hinten_file = 'gang_hinten.csv'
gang_notaus_file = 'gang_notaus.csv'
treppen_file = 'treppen.csv'


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

lbls = np.array(['lab_vorne']*lab_vorne.shape[0] + ['lab_hinten']*lab_hinten.shape[0] + ['gang_lab']*gang_lab.shape[0] + ['gang_hinten']*gang_hinten.shape[0] + ['gang_notaus']*gang_notaus.shape[0] + ['treppen']*treppen.shape[0])
# lbls = np.array(['lab']*(lab_vorne.shape[0] + lab_hinten.shape[0]) + ['gang']*(gang_lab.shape[0] + gang_hinten.shape[0] + gang_notaus.shape[0]) + ['treppen']*treppen.shape[0])
data = scale(data)
print('data.shape:', data.shape)
# random.seed(2)
test = data[0].reshape(1, -1)
np.delete(data, 0)
test_lbl = [lbls[0]]
np.delete(lbls, 0)
for i in range(599):
    r = random.randint(0, data.shape[0]-1)
    test = np.append(test, data[r].reshape(1, -1), axis=0)
    np.delete(data, r)
    test_lbl.append(lbls[r])
    np.delete(lbls, r)

# random.seed(3)
# layers = (random.randint(9, 900), random.randint(9, 900), random.randint(9, 900))
layers = (160, 61)
print('layers', layers)
mlp = MLPClassifier(hidden_layer_sizes=layers, activation='relu', solver='lbfgs', alpha=0.1, verbose=False)
mlp.fit(data, lbls)


pca = PCA(n_components=4)
pca.fit(data)
data_pca = pca.transform(data)
pca_knn = KNeighborsClassifier(n_neighbors=3)
pca_knn.fit(data_pca, lbls)
test_pca = pca.transform(test)
# pca_score.append(round(pca_knn.score(test_pca, test_lbl), 3))


while input('Press enter to collect sample') != 'q':
    print('Collecting wifi sample')
    for i in range(3):
        cmd1 = subprocess.Popen(['echo',sudo_pass], stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen(['sudo','-S'] + cmd.split(), stdin=cmd1.stdout, stdout=subprocess.PIPE)
        wifi = cmd2.stdout.read().decode().lower()

    # Retreive MAC and signal strength
    wifi = wifi.split('cell')
    dct = {}
    for w in wifi:
        for line in w.split('\n'):
            words = line.split(' ')
            if 'address:' in words:
                mac = words[-1]
            if 'signal' in words:
                strength = words[-4].split('=')[-1]
                dct[mac] = strength
                
    signal = np.zeros_like(bssids, dtype=int)
    for j, bssid in enumerate(bssids):
        try:
            signal[j] = dct[bssid]
        except KeyError:
            pass
        
    # signal_pca = pca.transform(signal.reshape(1, -1))
    # print('PCA_KNN:', pca_knn.predict(signal_pca))
    print('KNN:', pca_knn.predict(pca.transform(scale(signal.reshape(1, -1)))))
    print('MLP:', mlp.predict(signal.reshape(1, -1)))
