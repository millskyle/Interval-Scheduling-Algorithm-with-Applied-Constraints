import threading
import scrapy
import spider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from multiprocessing import Process

class SpiderWorker():
 	def __init__(self):
 		return

 	def run(self):
 		p = Process(target=self.runProcess)
		p.start()
		p.join()


 	def runProcess(self):
 		configure_logging()
 		runner = CrawlerRunner()
		runner.crawl(spider.available_courses_spider)
		d = runner.join()
		d.addBoth(lambda _: reactor.stop())

		reactor.run()
 		