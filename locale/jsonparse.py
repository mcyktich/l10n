import json
from pprint import pprint

with open('localizedstatictext.json', encoding="utf-8-sig") as data_file:    
    data = json.load(data_file)

pprint(data)