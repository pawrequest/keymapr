import pyautogui
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



keyboard_layout = {
    'Q': ((100, 100), (150, 150)),
    'W': ((150, 100), (200, 150)),
    'E': ((200, 100), (250, 150)),
    # ...
}

command_names = {
    'Ctrl+C': 'Copy',
    'Ctrl+V': 'Paste',
    'Ctrl+Z': 'Undo',
    # ...
}


keyboard_region = (100, 100, 400, 200)  # (left, top, width, height)
keyboard_image = pyautogui.screenshot(region=keyboard_region)


font = ImageFont.truetype('arial.ttf', 14)

draw = ImageDraw.Draw(keyboard_image)

for key, command in command_names.items():
    if key in keyboard_layout:
        key_coordinates = keyboard_layout[key]
        x, y = (key_coordinates[0][0] + key_coordinates[1][0]) // 2, (key_coordinates[0][1] + key_coordinates[1][1]) // 2
        draw.text((x, y), command, font=font, fill=(255, 255, 255))


keyboard_image.save('keyboard_shortcuts.png')