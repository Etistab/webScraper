from os.path import join

import scraper.url as url

def save(link, document, options):
  with open(join(options['outputDir'], url.getFilename(link)), 'w') as f:
    f.write(document)
