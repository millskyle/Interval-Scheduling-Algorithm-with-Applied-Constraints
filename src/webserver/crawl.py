import time

from database import dbHandler
from scraper import spiderworker

if __name__ == "__main__":
    dbHandler.init()

#    scraperWorker = spiderworker.SpiderWorker()
    scraperWorker = spiderworker.simpleWorker()
    scraperWorker.runProcess()
#    scraperWorker.start()
#    
#    try:
#        while True:
#            time.sleep(1)
#    except:
#        scraperWorker.end()
#        scraperWorker.join()
