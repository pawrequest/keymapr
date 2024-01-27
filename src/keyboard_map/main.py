from dataclasses import dataclass
from typing import Dict, List, Optional

import requests
import json
from googly import get_sheets_values


@dataclass
class PaulKey:
    input_key_str: Optional[str] = None
    output_key_str: Optional[str] = None
    program: Optional[str] = None
    category: Optional[str] = None
    command: Optional[str] = None
    base_key: Optional[str] = None
    layer: Optional[int] = None
    location: Optional[tuple] = None
    key_xpos: Optional[int] = None
    key_ypos: Optional[int] = None
    key_mods: Optional[List] = None
    matrix: Optional[List] = None
    metadata: Optional[Dict] = None


def get_paul_keys(values):
    paul_keys = []
    headers = values[0]
    for row_count, row in enumerate(values[1:]):
        key_dict = {}
        for col_count, key in enumerate(row):
            key_dict.update({headers[col_count]: row[col_count]})
        paul_keys.append(PaulKey(**key_dict))
    return paul_keys


values = get_sheets_values()
# from_sheets = get_paul_keys(values=values)

# prosody_gist = r'https://gist.github.com/prosody-speaks/1cb2c6b3a76e36112f7bcff9e4908fdb/raw/136aba0453ccf38bf037827e7262f14f72526487/layout.kbd.json'
matrix_link = r'https://github.com/Keychron/qmk_firmware/raw/bluetooth_playground/keyboards/keychron/k8_pro/iso/rgb/info.json'
via_link = r'https://github.com/Keychron/qmk_firmware/raw/bluetooth_playground/keyboards/keychron/k8_pro/via_json/k8_pro_iso_rgb.json'
local_base_layout = r'E:\Dev\keyboard_map\layouts\tkl2.json'

# response = requests.get(prosody_gist)
# prosody_layout = json.loads(response.text)


with open(local_base_layout, 'rb') as f:
    local_layout = json.load(f)

response = requests.get(matrix_link)
matrix = json.loads(response.text)
matrix_layouts = matrix.get('layouts')
matrix_layout = next(item for item in matrix_layouts.items())[1]['layout']

response = requests.get(via_link)
via = json.loads(response.text)
via_keymap = via['layouts']['keymap']

keys_list = []
for m_key in matrix_layout:
    # key_mat = tuple(m_key['matrix'])
    keys_list.append(PaulKey(key_xpos=m_key['x'], key_ypos=m_key['y'], matrix=m_key['matrix']))

metadata = None
pks = []


for row in via_keymap:
    for key in row:
        if isinstance(key, dict):
            metadata = key
            continue
        if isinstance(key, str):
            split = key.split(',')
            atup = list([int(split[0]), int(split[1])])

            pk = next(ma_key for ma_key in keys_list if ma_key.matrix == atup)
            pks.append(pk)
            ...
        ...

...
