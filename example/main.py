import json
'''
    lê o json com as instruções do risc-v
'''
with open('data/example.json', 'r') as json_file:
    members = json.load(json_file)

print(members)