from course import *


def generate_independent_data():
    independent_nodes = []

    course = 0
    for day in range(1,11):
        for sTime in range(8,20):
           course += 1
           Sec = Section()
           Sec.add_timeslot(str(sTime*100).zfill(4), str(sTime*100+50).zfill(4),day)

           Sec.CRN = str(course)            #41562
           Sec.name = "testcourse" + str(course)
           Sec.subject = ""       #PHY
           Sec.semester = "201509"       #201501
           Sec.course = str(course).zfill(4)
           Sec.campus = ""        #North Oshawa
           Sec.cType = "Lec"         #Lec
           Sec.remainingSeats = 100 #34 

           Sec.printToScreen()
           independent_nodes.append(Sec)


    return independent_nodes







