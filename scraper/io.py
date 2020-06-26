import scraper.url as url

def save(link, document):
  with open('./dist/' + url.getFilename(link), 'w') as f:
    f.write(document)
