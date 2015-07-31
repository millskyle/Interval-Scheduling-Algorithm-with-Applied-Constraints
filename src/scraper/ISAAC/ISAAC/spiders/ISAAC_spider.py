import scrapy
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest,Request
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor


def printer(string):
   print "KYLE: " + string


class available_courses_spider(CrawlSpider):
   name = "UOITspider"
   allowed_domains = ['ssbp.mycampus.ca']
   def __init__(self, *args, **kwargs):
      self.start_urls = ['https://ssbp.mycampus.ca/prod/bwckschd.p_disp_dyn_sched?TRM=U']




   def start_requests(self):
      yield scrapy.Request('https://ssbp.mycampus.ca/prod/bwckschd.p_disp_dyn_sched?TRM=U', self.parse)


   def parse(self, response):
      printer("Parser called")
      if "Search by Term" in response.body:
         printer("On main homepage")
         semesters = Selector(response).xpath('//td[@class="dedefault"]/select[@name="p_term"]/option/@value').extract()
         for semester in ["201601"] : #semesters:
            print semester
         



