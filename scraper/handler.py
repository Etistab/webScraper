import scraper.fetch as fetch
import scraper.html as html
import scraper.io as io
import scraper.url as url
import utils.logger as logger

def scrap(options):
  visited = set()
  stats = { 'overall': 0, 'success': 0, 'failures': 0 }
  visited.add(options['url'])
  document = download(options['url'], stats)
  scrapDown(html.getLinks(document), visited, 0, options['depth'], stats)
  return stats

def scrapDown(links, visited, depth, maxDepth, stats):
  for link in links:
    if link not in visited and depth < maxDepth:
      visited.add(link)
      try:
        document = download(link, stats)
        scrapDown(html.getLinks(document), visited, depth + 1, maxDepth, stats)
      except Exception as e:
        logger.info(e)
        logger.info(f'Skipping {link}!')

def download(link, stats):
  logger.info(f'Downloading {url.getFilename(link)}...')
  stats['overall'] += 1
  try:
    document = fetch.get(link)
  except:
    stats['failures'] += 1
    raise Exception(f'Unable to fetch {link}!')
  io.save(link, document)
  stats['success'] += 1
  logger.info(f'{url.getFilename(link)} was downloaded !')
  return document
