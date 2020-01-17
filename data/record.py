import subprocess
import numpy as np

# Never hardcode your password!
sudo_pass = '45AM15lr3990'
interface = 'wlx74da38ef3fbd'
# interface = 'wlp59s0'
# iwlist cmd
cmd = 'sudo iwlist ' + interface + ' scan'

fl = 'gang_lab.csv'

bssids = np.loadtxt('bssids.csv', dtype=str)


samples = np.loadtxt(fl, dtype = float)

print(samples.shape)


for i in range(500):
    print('Sample', i)
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
    
    # if not i:
    #     samples = np.copy(signal).reshape(1,-1)
    # else:
    samples = np.append(samples, signal.reshape(1, -1), axis=0)

    print(samples.shape)
    np.savetxt(fl, samples)
    
