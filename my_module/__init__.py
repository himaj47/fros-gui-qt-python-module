import os
import json

# cwd = os.path.expanduser("~")

import pkg_resources

# style_path = cwd + "/my_module/my_module/resources/style.json"

# icons = cwd + "/my_module/my_module/resources/icons/"
# square_icon = icons + "square.svg"
square_icon = pkg_resources.resource_filename('my_module', 'resources/icons/square.svg')
style_path = pkg_resources.resource_filename('my_module', 'resources/style.json')

with open(style_path, 'r') as file:
    json_file = json.load(file)

for list in json_file["QMainWindow"]:
    for items in list["navigation"]:
        if "restore" in items:
            for icons in items["restore"]:
                icons["normalIcon"] = square_icon
                icons["maximizedIcon"] = square_icon
            
with open(style_path, 'w') as file:
    json_file = json.dump(json_file, file, indent=2)