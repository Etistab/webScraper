import scraper.fetch as fetch
import scraper.html as html
import scraper.io as io
import scraper.url as url
import utils.logger as logger

def scrap(options):
  visited = set()
  visited.add(options['url'])
  document = download(options['url'])
  scrapDown(html.getLinks(document), visited, 0, options['depth'])

def scrapDown(links, visited, depth, maxDepth):
  for link in links:
    if link not in visited and depth < maxDepth:
      visited.add(link)
      document = download(link)
      scrapDown(html.getLinks(document), visited, depth + 1, maxDepth)

def download(link):
  logger.info(f'Downloading {url.getFilename(link)}...')
  document = fetch.get(link)
  io.save(link, document)
  logger.info(f'{url.getFilename(link)} was downloaded !')
  return document
