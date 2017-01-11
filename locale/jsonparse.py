import json
from pprint import pprint

with open('localizedstatictext.json', encoding="ANSI") as data_file:    
    data = json.load(data_file)

pprint(data)