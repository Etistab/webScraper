import scraper.fetch as fetch
import scraper.html as html
import scraper.io as io
import scraper.url as url
import utils.logger as logger

def scrap(options):
  def scrapDown(links, depth):
    maxDepth = options['depth']
    for link in links:
      if options['crossorigin'] == True or url.getDomain(options['url']) == url.getDomain(link):
        if link not in visited and depth < maxDepth:
          visited.add(link)
          try:
            document = download(link)
            scrapDown(html.getLinks(document), depth + 1)
          except Exception as e:
            logger.info(e)
            logger.info(f'Skipping {link}!')

  def download(link):
    logger.info(f'Downloading {url.getFilename(link)}...')
    stats['overall'] += 1
    try:
      document = fetch.get(link)
      logger.info(f'{url.getFilename(link)} was downloaded from origin {url.getDomain(link)}!')
      io.save(link, document, { 'outputDir': options['outputDir'] })
    except Exception as e:
      stats['failures'] += 1
      raise e
    stats['success'] += 1
    return document

  visited = set()
  stats = { 'overall': 0, 'success': 0, 'failures': 0 }
  visited.add(options['url'])
  try:
    document = download(options['url'])
    scrapDown(html.getLinks(document), 0)
  except Exception as e:
    logger.info(e)
  return stats
