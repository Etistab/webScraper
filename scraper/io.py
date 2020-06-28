from pathlib import Path
import os.path as path
import scraper.url as url
import utils.logger as logger

def checkDir(dir):
  return path.isdir(dir)

def save(link, document, options):
  try:
    p = path.join(options['outputDir'], url.getDomain(link), url.getRelativePath(link))
    Path(p).mkdir(parents=True, exist_ok=True)
    with open(path.join(p, url.getFilename(link)), 'w') as f:
      f.write(document)
  except:
    raise Exception(f'An error occurred while saving {link}!')
