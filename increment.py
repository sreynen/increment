import json

with open('data.json', 'r', encoding='utf8') as data_file:
  data = json.load(data_file)
  
data['value'] += 1

with open('data.json', 'w', encoding='utf8') as data_file:
  json.dump(data, data_file)
