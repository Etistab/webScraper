import json

def load():
  with open('./default.json', 'r') as config:
    return json.load(config)
