import subprocess
import json

# Never hardcode your password!
sudo_pass = '1234567890'
interface = 'wlp59s0'
# iwlist cmd
cmd = 'sudo iwlist' + interface + 'scan'

# Dictionary with wifi signal strength at different locations
locations = {}

program_mode = input('To store a map enter \'map\', to output one enter the filename: ')
if program_mode == 'map':
    while input('For exit press q: ') != 'q':
        # Collect wifi sample via iwlist
        print('Collecting wifi sample...')
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
                    print('MAC=', words[-1], end='\t')
                if 'signal' in words:
                    strength = words[-4].split('=')[-1]
                    dct[mac] = strength
                    print('Signal', words[-4])

        # Input and save location
        locat = int(input('Location ID: '))
        xcoord = int(input('X-Coordinate: '))
        ycoord = int(input('Y-Coordinate: ')) 

        locations[locat] = {'location id': locat, 'x-coord': xcoord, 'y-coord': ycoord, 'signals': dct}

    with open('wifi_map.txt', mode='w') as map_file:
        map_file.write(json.dumps(locations))

else:
    with open(program_mode, mode='r') as map_file:
        wifi_map = json.loads(map_file.read())
        for locat in wifi_map:
            print('----------- ')
            for key in wifi_map[locat]:
                if key != 'signals':
                    print(key, wifi_map[locat][key])
                else:
                    print(key)
                    for sig in wifi_map[locat][key]:
                        print('\t', sig, wifi_map[locat][key][sig])
