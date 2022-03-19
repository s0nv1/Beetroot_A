import json

dect = {}
dect['name'] = 'Ihor'
dect['age'] = 22
dect['city'] = 'Kherson'

with open('dect.json', 'w') as file_obj:
    json.dump(dect, file_obj)