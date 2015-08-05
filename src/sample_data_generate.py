from course import *
from random import randint



N = 400
ccode = {0:"PHY1010", 1:"CHEM1010", 2:"BIO1010",3:"CSCI1040",4:"MATH1010",5:"HIST1000"}
ctype = {0:"Lec", 1:"Tut", 2:"Lab" }
clength = {1:50,0:80,2:170}



f = open("sample_data.py","w")

f.write("from course import *\n")
f.write("def generate_dense_data():\n")
f.write("  nodes = [] \n")

def time_add(string, minutes_to_add):
   string=string.zfill(4)
   hours=int(string[0:2])
   minutes=int(string[2:4])

   hours+=((minutes+minutes_to_add) - (minutes + minutes_to_add)%60)/60.
   minutes=(minutes + minutes_to_add)%60
   return str(int(hours)).zfill(2) + str(int(minutes)).zfill(2)



def generate_independent_data():
   counter = 10000
   nodes = []
   for i in range(0,N):
      counter+=1
      course = ccode[randint(0,5)]
      day1 = randint(1,5)
      day2 = randint(1,5)
      day3 = randint(1,5)
      while (day2==day1):
         day2 = randint(1,5)
      while (day3==day1) or (day3==day2):
         day3 = randint(1,5)
      f.write("  Sec = Section() \n")
      f.write("  Sec.CRN = '{0}'\n".format( str(counter) ))
      f.write("  Sec.name = '{0}'\n".format(str(course)))
      f.write("  Sec.subject = ''\n" )       #PHY
      f.write("  Sec.semester = '201509'\n")       #201501
      f.write("  Sec.course = '{0}'\n".format(course)) #str(course).zfill(4)
      f.write("  Sec.campus = ''\n" )       #North Oshawa
      ran = randint(0,2)
      f.write("  Sec.cType = '{0}'\n".format(ctype[ran]))
      f.write("  Sec.remainingSeats = 100 \n") #34 
      week = randint(0,1)
      length = clength[ran]
      sTime1 = randint(8,20)
      sTime2 = randint(8,20)
      sTime3 = randint(8,20)
      if ran==0: #if it's a lecture
         f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime1*100).zfill(4), time_add(str(sTime1*100),length) ,day1))
         f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime2*100).zfill(4), time_add(str(sTime2*100),length) ,day2))
         f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime1*100).zfill(4), time_add(str(sTime1*100),length) ,day1+5))
         f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime2*100).zfill(4), time_add(str(sTime2*100),length)  ,day2+5))
      else:
         f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime1*100).zfill(4), time_add(str(sTime1*100),length) ,day1+5*week))
         f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime2*100).zfill(4), time_add(str(sTime2*100),length), day2+5*week))
         if randint(0,2)==7:
            f.write("  Sec.add_timeslot('{0}','{1}',{2})\n".format(str(sTime3*100).zfill(4), time_add(str(sTime3*100),length), day3+5*week))
      f.write("  Sec.cleanup()\n")
      f.write("  Sec.printToScreen()\n")
      #if ran==0 and binary==0:
#         Sec.add_timeslot(str(sTime1*100).zfill(4), str(sTime1*100+length).zfill(4),day1+5)
#         Sec.add_timeslot(str(sTime2*100).zfill(4), str(sTime2*100+length).zfill(4),day2+5)
#      else:
#         Sec.add_timeslot(str(sTime1*100).zfill(4), str(sTime1*100+length).zfill(4),day1)
#         Sec.add_timeslot(str(sTime2*100).zfill(4), str(sTime2*100+length).zfill(4),day2)
      f.write("  nodes.append(Sec)\n")
   f.write("  return nodes \n")











