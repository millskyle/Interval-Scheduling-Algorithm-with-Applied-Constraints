import time

from database import dbHandler
from scraper import spiderworker

if __name__ == "__main__":
    dbHandler.init(reinit=True)

    scraperWorker = spiderworker.SpiderWorker()

    scraperWorker.start()
    
    try:
        while True:
            time.sleep(1)
    except:
        scraperWorker.end()
        scraperWorker.join()
