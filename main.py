import config.args as args
import scraper.handler as handler

options = args.get()

handler.scrap(options)
