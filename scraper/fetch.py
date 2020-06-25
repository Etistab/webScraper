import requests as req

def get(url):
  return req.get(url).text
