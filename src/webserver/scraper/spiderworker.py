import time
import scrapy
import spider
import threading
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from multiprocessing import Process

class SpiderWorker(threading.Thread):
 	def __init__(self):
 		super(SpiderWorker, self).__init__()
 		self.exit = False
 		self.interval_time = 7200
 		self.callbackInt = [0]

 	def run(self):
 		while not self.exit:
 			start_time = time.time()

 			if (1):
		 		p = Process(target=self.runProcess)
				p.start()
				p.join()

			duration = time.time() - start_time
			for i in range(int(self.interval_time - duration)):
				if not self.exit:
					time.sleep(1)
				else:
					break;

	def end(self):
		self.exit = True

 	def runProcess(self):
 		configure_logging()
 		runner = CrawlerRunner()
		runner.crawl(spider.available_courses_spider)
		d = runner.join()
		d.addBoth(lambda _: reactor.stop())

		reactor.run()
 		