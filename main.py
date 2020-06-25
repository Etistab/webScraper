import config.args as args
import scraper.fetch as fetch

url = args.get()['url']

print(fetch.get(url))
