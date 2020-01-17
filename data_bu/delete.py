import subprocess
import numpy as np

# Never hardcode your password!
sudo_pass = '45AM15lr3990'
interface = 'wlx74da38ef3fbd'
# interface = 'wlp59s0'
# iwlist cmd
cmd = 'sudo iwlist ' + interface + ' scan'

fl = 'gang_lab.csv'

amur = '34:41:5D:9E:EF:2B'
taswlan = '80:1F:02:EE:3B:0F'

bssids = np.loadtxt('bssids.csv', dtype=str)


samples = np.loadtxt(fl, dtype = float)
print(bssids)
print(samples.shape)
# print('amur', amur.lower() in bssids)
print('taswlan', np.where(bssids == taswlan.lower()))
samples = np.delete(samples, 8, 1)
print(samples.shape)
    # np.savetxt(fl, samples)
    
