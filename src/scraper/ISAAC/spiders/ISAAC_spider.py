import scrapy
import matplotlib.pyplot as plt
import unicodedata
import logging
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest,Request
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
import time
import networkx as nx


G = nx.Graph()

def time2int(string):
   t = time.strptime(string, "%I:%M %p")
   return time.strftime('%H%M',t)

def string2courseType(string):
   if (string=="Lecture"):
      return "Lec"
   elif (string=="Laboratory"):
      return "Lab"
   elif (string=="Tutorial"):
      return "Tut"
   else:
      return "Oth"

allcourses = []

def day2int(day):
   return { 'M':1,'T':2,'W':3,'R':4,'F':5 }[day]


def printer(string):
   print "\n"
   logging.info("KYLE: " + string)
   print "\n"


class Timeslot():
   def __init__(self, sTime, eTime, day):
      self.key="{0}{1}{2}".format(sTime,eTime,day)
      self.sTime = sTime
      self.eTime = eTime
      self.day = day
   def __hash__(self):
      return hash(self.key)
   def __eq__(self, other):
      return self.key == other.key
class Section():
   def __init__(self):
      self.CRN = 0            #41562
      self.name = ""          #Physics I
      self.subject = ""       #PHY
      self.semester = 0       #201501
      self.course = ""        #PHY1010
      self.campus = ""        #North Oshawa
      self.cType = ""         #Lec
      self.remainingSeats = 0 #34
      self.timeslots = []     #List of corresponding Timeslot objects
   def add_timeslot(self, sTime, eTime, day):
      t = Timeslot(sTime,eTime,day)
      self.timeslots.append(t)
   def cleanup(self):
      #remove duplicate timeslots (e.g. labs listed 6 times per semester)
      self.timeslots = set(self.timeslots)
      #remove space in course code:
      self.course = self.course.replace(" ","")
   def printToScreen(self):
      print "\n"
      print self.name, self.CRN, self.cType
      for ts in self.timeslots:
         print ts.sTime,ts.eTime,ts.day

f = open('courses.txt','w')
f.write('CRN CTYPE CODE RSEAT STIME ETIME DAY SEM SUBJ \n')

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
         if (subject == "PHY" or subject == "CHEM" or subject == "CSCI" or subject == "BIOL" or subject == "MATH" ) :
#         if (1==1):
            yield req

   def parseRoot(self, response):
      if "Search by Term" in response.body:
         semesters = Selector(response).xpath('//td[@class="dedefault"]/select[@name="p_term"]/option/@value').extract()
         for semester in ["201509"] : #semesters:
            req = scrapy.Request('https://ssbp.mycampus.ca/prod/bwckgens.p_proc_term_date?p_calling_proc=bwckschd.p_disp_dyn_sched&TRM=U&p_term={semester}'.format(semester=semester), self.parseSubjects)
            req.meta['semester'] = semester
            yield req


   def parseSubjectOptions(self,response):

      semester = response.meta['semester']
      subject = response.meta['subject']

      printer("Parsing available {subject} courses for semester {semester}...".format(subject=subject,semester=semester))

      body = Selector(response).xpath('//table[@class="datadisplaytable"]')
      print body

      crns = body[0].xpath('//th[@class="ddheader"]')
      for i,ch in enumerate(crns):
         Sec = Section()
         header = ch.xpath('..//th[@class="ddheader"]/text()').extract()[i]
         thisCRN = ch.xpath('.//following-sibling::*[1]')
         Sec.remainingSeats = int(thisCRN.xpath('.//tr/td[span="Seats"]/following-sibling::td[3]/text()').extract()[0])
         meetingtimes = thisCRN.xpath('.//table[caption="Scheduled Meeting Times"]/tr[td[@class="dbdefault"]] ')
         Sec.name,Sec.CRN,Sec.course,section_number = header.split(" - ")

         for mt in meetingtimes:
            fields = mt.xpath('.//td[@class="dbdefault"]/text()').extract()
            week = unicodedata.normalize('NFKD', fields[0]).encode('ascii','ignore')
            day = day2int(fields[3])
            startTime,endTime = [time2int(i) for i in fields[2].split(" - ")]
            if (week==' W1'):
               days = [day]
            elif (week==' W2'):
               days = [day+5]
            else:
               days = [day,day+5]


            for d in days:
               Sec.add_timeslot(startTime,endTime,d)

         Sec.cleanup()
         Sec.cType = string2courseType(fields[6])

         for ts in Sec.timeslots:
            f.write("{CRN} {CTYPE} {CODE} {RSEAT} {STIME} {ETIME} {DAY} {SEM} {SUBJ} \n".format(
                 CRN=Sec.CRN,
                 CTYPE=Sec.cType,
                 CODE=Sec.course,
                 RSEAT=Sec.remainingSeats,
                 STIME=ts.sTime,
                 ETIME=ts.eTime,
                 DAY=ts.day,
                 SEM=semester,
                 SUBJ=subject ) )



         Sec.printToScreen()

         if (Sec.course in ['PHY1010U','CHEM1010U','BIOL1010U','CSCI1010U','MATH1010U']):
#            if (Sec.remainingSeats > 0):
            if (1==1):

               G.add_node(Sec,unique=Sec.course[0:2])

               allcourses.append(Sec)
         print "----------------------------------------------------------------"


      edges = []
      val_map = { 'Lec': 1.0, 'Tut':0.75, 'Lab':0.25, 'Oth':0.0 }
      colors = [val_map[node.cType] for node in G.nodes() ]
      print len(colors),len(G.nodes())
      print colors

      for i,iSec in enumerate(allcourses):
         for j,jSec in enumerate(allcourses):
            if i<j:
         #      print jSec.cType,iSec.cType
               have_edge = False
               #If the two sections are from the same course and are the same type, they're incompatible
               if ( (iSec.cType == jSec.cType) and (jSec.course==iSec.course)):
                  have_edge = True
               for itimeslot in iSec.timeslots:
                  for jtimeslot in jSec.timeslots:
                     if ( (jtimeslot.sTime <= itimeslot.eTime and jtimeslot.eTime >= itimeslot.eTime and jtimeslot.day==itimeslot.day) ):
                        have_edge = True

               if have_edge:
                  G.add_edge(iSec,jSec)
                  edges.append([i,j]) #G.add_edge(i,j)

      print "Your schedule: "
      for CC in nx.maximal_independent_set(G):
         print "  "
         print CC.course, CC.cType, CC.CRN
         for ts in CC.timeslots:
            print "   ",ts.day, ts.sTime, ts.eTime

      nx.draw_networkx(G,with_labels=True,labels=nx.get_node_attributes(G,'unique'), cmap=plt.get_cmap('jet'), node_color=colors,vmin=0, vmax=1.0)
      plt.show()



      print "done"










