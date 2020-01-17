import subprocess
import random
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from matplotlib.pyplot import imshow, show

# Never hardcode your password!
sudo_pass = '45AM15lr3990'
interface = 'wlx74da38ef3fbd'
# interface = 'wlp59s0'
# iwlist cmd
cmd = 'sudo iwlist ' + interface + ' scan'

<<<<<<< HEAD
amur = '34:41:5D:9E:EF:2B'
taswlan = '80:1F:02:EE:3B:0F'

=======
# File Names
>>>>>>> f2b0cfa12ec2152528cc083b9bfedde136eb1ee3
lab_vorne_file = 'lab_vorne.csv'
lab_hinten_file = 'lab_hinten.csv'
gang_lab_file = 'gang_lab.csv'
gang_hinten_file = 'gang_hinten.csv'
gang_notaus_file = 'gang_notaus.csv'
treppen_file = 'treppen.csv'
bssid_file = 'bssids.csv'

# Load Data
print('Loading Data', end='')
bssids = np.loadtxt(bssid_file, dtype=str)
lab_vorne = np.loadtxt(lab_vorne_file, dtype=float)
lab_hinten = np.loadtxt(lab_hinten_file, dtype=float)
gang_lab = np.loadtxt(gang_lab_file, dtype=float)
gang_hinten = np.loadtxt(gang_hinten_file, dtype=float)
gang_notaus = np.loadtxt(gang_notaus_file, dtype=float)
treppen = np.loadtxt(treppen_file, dtype=float)

# Create Data Matrix
print(end='.')
data = lab_vorne
data = np.append(data, lab_hinten, axis=0)
data = np.append(data, gang_lab, axis=0)
data = np.append(data, gang_hinten, axis=0)
data = np.append(data, gang_notaus, axis=0)
data = np.append(data, treppen, axis=0)

# Create Label Array (complex)
print(end='.')
lbls = np.array(['lab_vorne']*lab_vorne.shape[0] + ['lab_hinten']*lab_hinten.shape[0] + ['gang_lab']*gang_lab.shape[0] + ['gang_hinten']*gang_hinten.shape[0] + ['gang_notaus']*gang_notaus.shape[0] + ['treppen']*treppen.shape[0])

# Create Label Array (simplified)
# lbls = np.array(['lab']*(lab_vorne.shape[0] + lab_hinten.shape[0]) + ['gang']*(gang_lab.shape[0] + gang_hinten.shape[0] + gang_notaus.shape[0]) + ['treppen']*treppen.shape[0])

# Double the Data aritificially
print('.')
print(data.shape)
dat_rd = data - np.random.rand(data.shape[0], data.shape[1])
data = np.append(data, dat_rd, axis=0)
lbls = np.append(lbls, lbls)
print(data.shape, lbls.shape)

# Scale the data
data = scale(data)
<<<<<<< HEAD
print('data.shape:', data.shape)
# random.seed(2)
# test = data[0].reshape(1, -1)
# np.delete(data, 0)
# test_lbl = [lbls[0]]
# np.delete(lbls, 0)
# for i in range(599):
#     r = random.randint(0, data.shape[0]-1)
#     test = np.append(test, data[r].reshape(1, -1), axis=0)
#     np.delete(data, r)
#     test_lbl.append(lbls[r])
#     np.delete(lbls, r)
=======

random.seed(3)
test = data[0].reshape(1, -1)
np.delete(data, 0)
test_lbl = [lbls[0]]
np.delete(lbls, 0)
for i in range(1000):
    r = random.randint(0, data.shape[0]-1)
    test = np.append(test, data[r].reshape(1, -1), axis=0)
    np.delete(data, r)
    test_lbl.append(lbls[r])
    np.delete(lbls, r)
>>>>>>> f2b0cfa12ec2152528cc083b9bfedde136eb1ee3

# data = scale(data)
# test = scale(test)

# Training MLP
# random.seed(3)
# layers = (random.randint(9, 900), random.randint(9, 900), random.randint(9, 900))
<<<<<<< HEAD
layers = (160, 61)
print('layers', layers)
mlp = MLPClassifier(hidden_layer_sizes=layers, activation='tanh', solver='lbfgs', alpha=0.1, verbose=False)
mlp.fit(data, lbls)


pca = PCA(n_components=4)
pca.fit(data)
data_pca = pca.transform(data)
pca_knn = KNeighborsClassifier(n_neighbors=3)
pca_knn.fit(data_pca, lbls)
=======
# layers = (400, 600, 91)
layers = (156, 78)
print('hidden-layer sizes', layers)
print('Training MLP...')
# mlp = MLPClassifier(hidden_layer_sizes=layers, activation='tanh', solver='sgd', alpha=0.1, verbose=False)
# mlp.fit(data, lbls)
# print('Training MLP 2...')
# layers = (400, 900, 91)
mlp_2 = MLPClassifier(hidden_layer_sizes=layers, activation='tanh', solver='lbfgs', alpha=0.1, verbose=False)
mlp_2.fit(data, lbls)

# Training KNN
# print('Training KNN')
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(data, lbls)

# Training PCA (+ KNN)
# print('Training PCA')
# pca_score = []
# for i in range(4, 6):
#     pca = PCA(n_components=i)
#     pca.fit(data)
#     data_pca = pca.transform(data)
#     pca_knn = KNeighborsClassifier(n_neighbors=3)
#     pca_knn.fit(data_pca, lbls)
#     test_pca = pca.transform(test)
#     pca_score.append((i, round(pca_knn.score(test_pca, test_lbl), 3)))
>>>>>>> f2b0cfa12ec2152528cc083b9bfedde136eb1ee3

# test_pca = pca.transform(test)
# pca_score.append(round(pca_knn.score(test_pca, test_lbl), 3))


<<<<<<< HEAD
while input('Press enter to collect sample') != 'q':
    print('Collecting wifi sample')
    for i in range(3):
        cmd1 = subprocess.Popen(['echo',sudo_pass], stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen(['sudo','-S'] + cmd.split(), stdin=cmd1.stdout, stdout=subprocess.PIPE)
        wifi = cmd2.stdout.read().decode().lower()
=======
#     # Retreive MAC and signal strength
#     wifi = wifi.split('cell')
#     dct = {}
#     for w in wifi:
#         for line in w.split('\n'):
#             words = line.split(' ')
#             if 'address:' in words:
#                 mac = words[-1]
#             if 'signal' in words:
#                 strength = words[-4].split('=')[-1]
#                 dct[mac] = strength
                
#     signal = np.zeros_like(bssids, dtype=int)
#     for j, bssid in enumerate(bssids):
#         try:
#             signal[j] = dct[bssid]
#         except KeyError:
#             pass
    
# print('PCA', pca_score)
# print('KNN:', knn.score(test, test_lbl))
# print('MLP:', mlp.score(test, test_lbl))
print('MLP:', mlp_2.score(test, test_lbl))

# for i, t in enumerate(test):
#     if test_lbl[i] != knn.predict(t.reshape(1, -1))[0]:
#         print(test_lbl[i], knn.predict(t.reshape(1, -1))[0], knn.predict_proba(t.reshape(1, -1)))
>>>>>>> f2b0cfa12ec2152528cc083b9bfedde136eb1ee3

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
    print('MLP:', mlp.predict(scale(signal.reshape(1, -1))))
