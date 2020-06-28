import json

def load():
  with open('./config/default.json', 'r') as config:
    return json.load(config)
