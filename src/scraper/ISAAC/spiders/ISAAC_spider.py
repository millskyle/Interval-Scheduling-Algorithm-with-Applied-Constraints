import scrapy
import logging
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest,Request
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor


def printer(string):
   print "\n"
   logging.info("KYLE: " + string)
   print "\n"


class Timeslot():
   def __init__(self, sTime, eTime, day):
      self.sTime = sTime
      self.eTime = eTime
      self.day = day
class Section():
   def __init__():
      self.CRN = 0       #41562
      self.name = ""     #Physics I
      self.subject = ""  #PHY
      self.semester = 0  #201501
      self.course = ""   #PHY1010
      self.campus = ""   #North Oshawa
      self.cType = ""    #Lec
      self.timeslots = []#List of corresponding Timeslot objects
   def add_timeslot(self, sTime, eTime, day):
      t = Timeslot(sTime,eTime,day)
      self.timeslots.append(t)




class available_courses_spider(CrawlSpider):
   name = "UOITspider"
   allowed_domains = ['https://ssbp.mycampus.ca', 'ssbp.mycampus.ca']
   def __init__(self, *args, **kwargs):
      self.start_urls = ['https://ssbp.mycampus.ca/prod/bwckschd.p_disp_dyn_sched?TRM=U']




   def start_requests(self):
      yield scrapy.Request('https://ssbp.mycampus.ca/prod/bwckschd.p_disp_dyn_sched?TRM=U', self.parseRoot)

   def parseSubjects(self, response):
      semester = response.meta['semester']
      subjects = Selector(response).xpath('//td[@class="dedefault"]/select[@id="subj_id"]/option/@value').extract()
      for subject in subjects:
         url = "https://ssbp.mycampus.ca/prod/bwckschd.p_get_crse_unsec?TRM=U&term_in="+semester+"&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_subj="+subject+"&sel_crse=&sel_title=&sel_schd=%25&sel_insm=%25&sel_from_cred=&sel_to_cred=&sel_camp=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a"
         req = scrapy.Request(url,self.parseSubjectOptions)
         req.meta['semester'] = semester
         req.meta['subject'] = subject
         if (subject == "PHY") :
            yield req

   def parseRoot(self, response):
      if "Search by Term" in response.body:
         semesters = Selector(response).xpath('//td[@class="dedefault"]/select[@name="p_term"]/option/@value').extract()
         for semester in ["201601",] : #semesters:
            req = scrapy.Request('https://ssbp.mycampus.ca/prod/bwckgens.p_proc_term_date?p_calling_proc=bwckschd.p_disp_dyn_sched&TRM=U&p_term={semester}'.format(semester=semester), self.parseSubjects)
            req.meta['semester'] = semester
            yield req


   def parseSubjectOptions(self,response):

      semester = response.meta['semester']
      subject = response.meta['subject']

      file = open('out.txt','w')
      file.write(response.body)
      file.close()

      printer("Parsing available {subject} courses for semester {semester}...".format(subject=subject,semester=semester))

      body = Selector(response).xpath('//table[@class="datadisplaytable"]')
      print body

      crns = body[0].xpath('//th[@class="ddheader"]')
      for i,ch in enumerate(crns):
         thisCRN = ch.xpath('./following-sibling::*[1]')
         seatsLeft = int(thisCRN.xpath('//tr/td[span="Seats"]/following-sibling::td[3]/text()').extract()[i])
         temp = thisCRN.xpath('//')
         print temp









