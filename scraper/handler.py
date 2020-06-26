import scraper.fetch as fetch
import scraper.html as html
import scraper.io as io

def scrap(options):
  visited = set()
  visited.add(options['url'])
  document = fetch.get(options['url'])
  io.save(options['url'], document)
  scrapDown(html.getLinks(document), visited, 0, options['depth'])

def scrapDown(links, visited, depth, maxDepth):
  for link in links:
    if link not in visited and depth < maxDepth:
      visited.add(link)
      document = fetch.get(link)
      io.save(link, document)
      scrapDown(html.getLinks(document), visited, depth + 1, maxDepth)
