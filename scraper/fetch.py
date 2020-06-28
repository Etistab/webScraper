import requests as req

def get(url):
  try:
    return req.get(url).text
  except:
    raise Exception(f'An error occurred while fetching {url}!')
