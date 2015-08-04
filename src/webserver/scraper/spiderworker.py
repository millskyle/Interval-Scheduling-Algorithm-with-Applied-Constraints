import threading
import scrapy
import spider
from scrapy.crawler import CrawlerProcess

class SpiderWorker(threading.Thread):
 	def __init__(self):
 		super(SpiderWorker, self).__init__()
 		dbHandler = None

 	def run(self):
 		process = CrawlerProcess({
		    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
		})

		process.crawl(spider.available_courses_spider)
		process.start()
		process.stop()
 		