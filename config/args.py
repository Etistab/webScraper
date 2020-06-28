import argparse
import config.loader as loader

def get():
  target = loader.load()
  target.update({ (k, v) for k, v in vars(parseArgs()).items() if v != None })
  return target

def parseArgs():
  parser = argparse.ArgumentParser(description='Scraps a website.')
  parser.add_argument('url', metavar='URL', type=str, help='url of the website')
  parser.add_argument('-o', '--output', type=str, dest='outputDir', help='defines the output directory')
  parser.add_argument('-d', '--depth', type=int, dest='depth', help='defines the scraping depth')
  parser.add_argument('-c', dest='crossorigin', action='store_const', const=True, help='allows the scraper to fetch documents from a different origin')
  return parser.parse_args()
