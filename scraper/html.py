from bs4 import BeautifulSoup as bs

def getHrefTag(soup, tag):
  return [ t['href'] for t in soup.find_all(tag, href=True) if not t['href'].startswith('data:') ]

def getLinks(document):
  soup = bs(document, features='html.parser')
  return getHrefTag(soup, 'link') + getHrefTag(soup, 'a')
