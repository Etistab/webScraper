from urllib.parse import urlparse

def getDomain(url):
  return urlparse(url).netloc

def getPath(url):
  return urlparse(url).path

def getFilename(url):
  name = getPath(url).split('/').pop()
  return name if len(name) > 0 else 'index.html'

def getRelativePath(url):
  rel = [ seg for seg in getPath(url).split('/') if len(seg) > 0 ]
  if len(rel) == 0:
    return ''
  rel.pop()
  return '/'.join(rel)
