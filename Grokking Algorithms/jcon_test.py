import json

with open('dect.json') as file_obj:
    dect = json.load(file_obj)
for k, v in dect.items():
    print(k, ':', v)