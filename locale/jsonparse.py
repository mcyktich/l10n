import json
from pprint import pprint

with open('en_US/state.json', encoding="ANSI") as data_file:    
    data = json.load(data_file)

pprint(data)
pprint('------------------------------------------------')

with open('state.json', encoding="ANSI") as data_file:    
    data = json.load(data_file)
pprint(data)