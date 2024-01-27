import itertools

import requests
import json
gist_layout = 'https://gist.github.com/prosody-speaks/1cb2c6b3a76e36112f7bcff9e4908fdb/raw/136aba0453ccf38bf037827e7262f14f72526487/layout.kbd.json'
k8_matrix = 'https://github.com/Keychron/qmk_firmware/raw/bluetooth_playground/keyboards/keychron/k8_pro/iso/rgb/info.json'
k8_via = 'https://github.com/Keychron/qmk_firmware/raw/bluetooth_playground/keyboards/keychron/k8_pro/via_json/k8_pro_iso_rgb.json'

keys_to_add ={

}
response = requests.get(gist_layout)
gist = json.loads(response.text)
response = requests.get(k8_matrix)
matrix = json.loads(response.text)
response = requests.get(k8_via)
via = json.loads(response.text)

layouts = matrix.get('layouts')
layout = next(item for item in layouts.items())[1]['layout']



# Using islice() + items()
# Get first N items in dictionary
# layout = dict(itertools.islice(layouts.items(), N))
# layout = dict(itertools.islice(layouts, 1))
...