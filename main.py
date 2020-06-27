from time import time

import config.args as args
import scraper.handler as handler
import utils.logger as logger

logger.setup()

options = args.get()

start = time()
stats = handler.scrap(options)
end = time()

logger.info('DONE!')
logger.info(f'''Scraped {options['url']} at depth {options['depth']} in {end - start}s!''')
logger.info(f'''Processed {stats['overall']} files with {stats['failures']} failures and {stats['success']} success!''')
