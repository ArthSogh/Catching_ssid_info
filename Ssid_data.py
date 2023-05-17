import subprocess
import time


def writing_on_file(new_text):

    with open("Pico_log.txt", mode="a") as myfile: myfile.write(f"{new_text},\n")

def get_ssid_names():
    ssid_names = [0]
    while True:
        try:
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'])
            output = output.decode('latin-1')
            lines = output.split('\n')
            # print(output)
            for line in lines:
                if 'SSID' in line:
                    ssid = line.split(':')[1].strip()
                    # print(line)
                    # print(ssid)
                    if ssid.startswith('PICO') and ssid != ssid_names[len(ssid_names)-1] and ssid != ssid_names[len(ssid_names)-2]:
                        ssid_names.append(ssid)
                        writing_on_file(ssid)
                        print(ssid_names)
                        time.sleep(120)
            # return ssid_names
        except subprocess.CalledProcessError:
            print("Failed to retrieve SSID names.")
            return []

# Usage
ssids = get_ssid_names()
# for ssid in ssids:
#     print(ssid)
