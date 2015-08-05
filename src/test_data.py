from course import *
from random import randint



N = 40
ccode = {0:"PHY1010", 1:"CHEM1010", 2:"BIO1010",3:"CSCI1040",4:"MATH1010"}
ctype = {0:"Lec", 1:"Tut", 2:"Lab" }
clength = {1:50,0:80,2:170}




def generate_independent_data():
   nodes = []
   for i in range(0,N):
      course = ccode[randint(0,4)]
      day1 = randint(1,10)
      day2 = randint(1,10)
      while not(day2==day1):
         day2 = randint(1,10)
      Sec = Section()
      Sec.CRN = str(randint(0,99999)    )        #41562
      Sec.name = "testcourse" + str(course)
      Sec.subject = ""       #PHY
      Sec.semester = "201509"       #201501
      Sec.course = course #str(course).zfill(4)
      Sec.campus = ""        #North Oshawa
      ran = randint(0,2)
      Sec.cType = ctype[ran]
      Sec.remainingSeats = 100 #34 
      sTime1 = randint(8,20)
      length = clength[ran]
      sTime2 = randint(8,20)
      Sec.add_timeslot(str(sTime1*100).zfill(4), str(sTime1*100+length).zfill(4),day1)
      Sec.add_timeslot(str(sTime2*100).zfill(4), str(sTime2*100+length).zfill(4),day2)
      if ran==0:
         Sec.add_timeslot(str(sTime1*100).zfill(4), str(sTime1*100+length).zfill(4),day1+5)
         Sec.add_timeslot(str(sTime2*100).zfill(4), str(sTime2*100+length).zfill(4),day2+5)
      nodes.append(Sec)



   return nodes







