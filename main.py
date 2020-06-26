import config.args as args
import scraper.handler as handler
import utils.logger as logger

logger.setup()

options = args.get()

handler.scrap(options)
