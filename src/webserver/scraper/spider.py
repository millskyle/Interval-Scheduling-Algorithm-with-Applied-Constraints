import scrapy
import unicodedata
import logging
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest,Request
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
import time
import networkx as nx
from  course import *
from database import dbHandler

def time2int(string):
    try:
        t = time.strptime(string, "%I:%M %p")
    except ValueError:
        return "0000"
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
    d = { 'M':1,'T':2,'W':3,'R':4,'F':5 }
    return d.get(day,-1)

def printer(string):
    print "\n"
    logging.info("KYLE: " + string)
    print "\n"

#f = open('courses.txt','w')
#f.write('CRN CTYPE CODE RSEAT STIME ETIME DAY SEM SUBJ \n')

class available_courses_spider(CrawlSpider):
    name = "UOITspider"
    allowed_domains = ['https://ssbp.mycampus.ca', 'ssbp.mycampus.ca']
    def __init__(self, *args, **kwargs):
        self.start_urls = ['https://ssbp.mycampus.ca/prod_uoit/bwckschd.p_disp_dyn_sched?TRM=U']

    def start_requests(self):
        yield scrapy.Request('https://ssbp.mycampus.ca/prod_uoit/bwckschd.p_disp_dyn_sched?TRM=U', self.parseSemesterChoicePage)

    def parseSubjectChoicePage(self, response):
        semester = response.meta['semester']
        subjects = Selector(response).xpath('//td[@class="dedefault"]/select[@id="subj_id"]/option/@value').extract()
        for subject in subjects:
            #if subject=='HLSC':  #for debugging a specific subject
               url = "https://ssbp.mycampus.ca/prod_uoit/bwckschd.p_get_crse_unsec?TRM=U&term_in="+semester+"&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_subj="+subject+"&sel_crse=&sel_title=&sel_schd=%25&sel_insm=%25&sel_from_cred=&sel_to_cred=&sel_camp=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a"
               req = scrapy.Request(url,self.parseSubjectOptions)
               req.meta['semester'] = semester
               req.meta['subject'] = subject
               yield req

    def parseSemesterChoicePage(self, response):
        if "Search by Term" in response.body:
            semesters = Selector(response).xpath('//td[@class="dedefault"]/select[@name="p_term"]/option/@value').extract()
            for semester in semesters:
                req = scrapy.Request('https://ssbp.mycampus.ca/prod_uoit/bwckgens.p_proc_term_date?p_calling_proc=bwckschd.p_disp_dyn_sched&TRM=U&p_term={semester}'.format(semester=semester), self.parseSubjectChoicePage)
                req.meta['semester'] = semester
                if semester != '':
                    if int(semester) > 201607:
                        yield req


    def parseSubjectOptions(self,response):

        semester = response.meta['semester']
        subject = response.meta['subject']

        printer("Parsing available {subject} courses for semester {semester}...".format(subject=subject,semester=semester))

        body = Selector(response).xpath('//table[@class="datadisplaytable"]')

        crns = body[0].xpath('//th[@class="ddheader"]')
        for i,ch in enumerate(crns):
            try:
                Sec = Section()
                Sec.semester = semester
                header = ch.xpath('..//th[@class="ddheader"]/text()').extract()[i]
                thisCRN = ch.xpath('.//following-sibling::*[1]')
                text = thisCRN.xpath('.//span[@class="fieldlabeltext"]/..').extract()[0]
                if "North Oshawa" in text:
                    Sec.campus = "North"
#                    print "North Campus"
                elif "Downtown Oshawa" in text:
                    Sec.campus = "Downtown"
#                    print "Downtown campus"
                else:
                    Sec.campus = "Other"
#                    print "OTHER CAMPUS"
#                if "Online Delivery" in text:
#                    print "ONLINE"
                Sec.remainingSeats = int(thisCRN.xpath('.//tr/td[span="Seats"]/following-sibling::td[3]/text()').extract()[0])
                meetingtimes = thisCRN.xpath('.//table[caption="Scheduled Meeting Times"]/tr[td[@class="dbdefault"]] ')
                Sec.name,Sec.CRN,Sec.course,section_number = header.split(" - ")

                for mt in meetingtimes:
                    fields = mt.xpath('.//td[@class="dbdefault"]/text()|.//td[@class="dbdefault"]//*/text()').extract()
                    #The "week" field includes a non-breaking space (&nbsp;) so it must be dealt with
                    week = unicodedata.normalize('NFKD', fields[0]).encode('ascii','ignore')
                    if str(fields[3]) in ['M','T','W','R','F']:
                        day = day2int(fields[3])
                        startTime,endTime = [time2int(i) for i in fields[2].split(" - ")]
                        dateRange = fields[5].split(' - ')
                        #print 'KYLE DEBUG:',fields
                        cType = string2courseType(fields[6])
                    
                    else:
                        day = -1
                        startTime,endTime = ["0001", "0002"]
                        cType = string2courseType(fields[4])

                    if (week==' W1'):
                        days = [day]
                    elif (week==' W2'):
                        days = [day+5]
                    else:
                        days = [day,day+5]

                    if not(cType=='Lec' and dateRange[0]==dateRange[1] ):
                        for d in days:
                            Sec.add_timeslot(startTime,endTime,d)

                Sec.cleanup()
#                print fields
                Sec.cType = cType

                allcourses.append(Sec)

#                for ts in Sec.timeslots:
#                    f.write("{CRN} {CTYPE} {CODE} {RSEAT} {STIME} {ETIME} {DAY} {SEM} {SUBJ} \n".format(
#                          CRN=Sec.CRN,
#                          CTYPE=Sec.cType,
#                          CODE=Sec.course,
#                          RSEAT=Sec.remainingSeats,
#                          STIME=ts.sTime,
#                          ETIME=ts.eTime,
#                          DAY=ts.day,
#                          SEM=semester,
#                          SUBJ=subject ) )
#

                Sec.printToScreen()
                dbHandler.updateCourse(Sec)  #insert the course into the database.    dbHandler must take care of converting the Section() object to a database query/object.



            except ValueError:
                print "Error parsing course schedule information for {0}".format(header)









