from course import *
def generate_dense_data():
  nodes = [] 
  Sec = Section() 
  Sec.CRN = '10001'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',10)
  Sec.add_timeslot('0800','1050',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10002'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',7)
  Sec.add_timeslot('1700','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10003'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('1100','1220',8)
  Sec.add_timeslot('0800','0920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10004'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',3)
  Sec.add_timeslot('1100','1150',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10005'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',3)
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('2000','2120',8)
  Sec.add_timeslot('1800','1920',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10006'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',9)
  Sec.add_timeslot('1000','1050',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10007'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',1)
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('0900','1020',6)
  Sec.add_timeslot('1800','1920',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10008'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',8)
  Sec.add_timeslot('1900','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10009'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',3)
  Sec.add_timeslot('1900','2150',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10010'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('2000','2120',9)
  Sec.add_timeslot('0800','0920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10011'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('1400','1520',6)
  Sec.add_timeslot('1300','1420',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10012'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('1800','1920',6)
  Sec.add_timeslot('1800','1920',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10013'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',8)
  Sec.add_timeslot('0900','0950',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10014'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',2)
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1900','2020',7)
  Sec.add_timeslot('1800','1920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10015'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',2)
  Sec.add_timeslot('1700','1820',1)
  Sec.add_timeslot('1400','1520',7)
  Sec.add_timeslot('1700','1820',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10016'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',5)
  Sec.add_timeslot('0800','0850',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10017'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',4)
  Sec.add_timeslot('1700','1750',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10018'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('1600','1720',4)
  Sec.add_timeslot('0900','1020',8)
  Sec.add_timeslot('1600','1720',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10019'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',2)
  Sec.add_timeslot('1600','1850',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10020'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',4)
  Sec.add_timeslot('1700','1820',3)
  Sec.add_timeslot('1900','2020',9)
  Sec.add_timeslot('1700','1820',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10021'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1800','1920',6)
  Sec.add_timeslot('1000','1120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10022'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',9)
  Sec.add_timeslot('1200','1450',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10023'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',6)
  Sec.add_timeslot('1500','1550',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10024'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',4)
  Sec.add_timeslot('1300','1550',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10025'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',5)
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('1800','1920',10)
  Sec.add_timeslot('1100','1220',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10026'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('1800','1920',5)
  Sec.add_timeslot('0900','1020',8)
  Sec.add_timeslot('1800','1920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10027'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',10)
  Sec.add_timeslot('1200','1250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10028'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',8)
  Sec.add_timeslot('2000','2250',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10029'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',6)
  Sec.add_timeslot('2000','2250',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10030'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',7)
  Sec.add_timeslot('1400','1650',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10031'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',2)
  Sec.add_timeslot('1100','1150',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10032'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',10)
  Sec.add_timeslot('1300','1350',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10033'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',3)
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1500','1620',8)
  Sec.add_timeslot('2000','2120',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10034'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',2)
  Sec.add_timeslot('1100','1150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10035'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1320',4)
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1200','1320',9)
  Sec.add_timeslot('1800','1920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10036'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',7)
  Sec.add_timeslot('1400','1450',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10037'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',5)
  Sec.add_timeslot('2000','2120',1)
  Sec.add_timeslot('1700','1820',10)
  Sec.add_timeslot('2000','2120',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10038'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',2)
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('0800','0920',7)
  Sec.add_timeslot('0900','1020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10039'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',3)
  Sec.add_timeslot('2000','2050',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10040'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',10)
  Sec.add_timeslot('0800','0850',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10041'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',8)
  Sec.add_timeslot('1800','2050',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10042'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',4)
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('0800','0920',9)
  Sec.add_timeslot('1400','1520',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10043'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',5)
  Sec.add_timeslot('1000','1250',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10044'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('2000','2120',10)
  Sec.add_timeslot('1600','1720',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10045'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',9)
  Sec.add_timeslot('1200','1250',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10046'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',8)
  Sec.add_timeslot('1400','1450',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10047'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',3)
  Sec.add_timeslot('1300','1420',1)
  Sec.add_timeslot('1300','1420',8)
  Sec.add_timeslot('1300','1420',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10048'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1550',10)
  Sec.add_timeslot('0900','1150',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10049'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',2)
  Sec.add_timeslot('1600','1720',3)
  Sec.add_timeslot('0800','0920',7)
  Sec.add_timeslot('1600','1720',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10050'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',5)
  Sec.add_timeslot('0800','0920',1)
  Sec.add_timeslot('1500','1620',10)
  Sec.add_timeslot('0800','0920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10051'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('1000','1120',2)
  Sec.add_timeslot('2000','2120',9)
  Sec.add_timeslot('1000','1120',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10052'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',5)
  Sec.add_timeslot('1500','1750',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10053'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',2)
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1000','1120',7)
  Sec.add_timeslot('0900','1020',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10054'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',6)
  Sec.add_timeslot('1900','2150',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10055'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',4)
  Sec.add_timeslot('1000','1250',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10056'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',6)
  Sec.add_timeslot('1900','2150',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10057'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',4)
  Sec.add_timeslot('1900','2150',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10058'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',6)
  Sec.add_timeslot('1600','1850',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10059'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',2)
  Sec.add_timeslot('1700','1750',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10060'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',9)
  Sec.add_timeslot('0800','0850',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10061'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',5)
  Sec.add_timeslot('1200','1250',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10062'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',9)
  Sec.add_timeslot('0800','1050',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10063'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1000','1120',3)
  Sec.add_timeslot('1800','1920',6)
  Sec.add_timeslot('1000','1120',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10064'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',5)
  Sec.add_timeslot('1600','1650',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10065'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',1)
  Sec.add_timeslot('1800','2050',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10066'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',3)
  Sec.add_timeslot('0900','1150',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10067'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',10)
  Sec.add_timeslot('1900','1950',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10068'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1100','1220',2)
  Sec.add_timeslot('1000','1120',9)
  Sec.add_timeslot('1100','1220',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10069'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',3)
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('1500','1620',8)
  Sec.add_timeslot('1300','1420',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10070'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',5)
  Sec.add_timeslot('1500','1620',1)
  Sec.add_timeslot('1700','1820',10)
  Sec.add_timeslot('1500','1620',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10071'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',9)
  Sec.add_timeslot('1900','1950',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10072'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',4)
  Sec.add_timeslot('1400','1650',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10073'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',1)
  Sec.add_timeslot('1500','1620',2)
  Sec.add_timeslot('1900','2020',6)
  Sec.add_timeslot('1500','1620',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10074'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',2)
  Sec.add_timeslot('1200','1250',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10075'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',10)
  Sec.add_timeslot('1200','1250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10076'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('1800','1920',4)
  Sec.add_timeslot('1800','1920',7)
  Sec.add_timeslot('1800','1920',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10077'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',5)
  Sec.add_timeslot('0800','0920',3)
  Sec.add_timeslot('1400','1520',10)
  Sec.add_timeslot('0800','0920',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10078'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',5)
  Sec.add_timeslot('1800','1850',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10079'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',10)
  Sec.add_timeslot('1300','1550',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10080'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',2)
  Sec.add_timeslot('0800','0920',3)
  Sec.add_timeslot('1100','1220',7)
  Sec.add_timeslot('0800','0920',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10081'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',1)
  Sec.add_timeslot('1900','2020',3)
  Sec.add_timeslot('1900','2020',6)
  Sec.add_timeslot('1900','2020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10082'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('2000','2120',9)
  Sec.add_timeslot('1300','1420',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10083'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('1600','1720',5)
  Sec.add_timeslot('1100','1220',9)
  Sec.add_timeslot('1600','1720',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10084'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',5)
  Sec.add_timeslot('1800','1850',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10085'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',4)
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1500','1620',9)
  Sec.add_timeslot('2000','2120',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10086'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',5)
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1600','1720',10)
  Sec.add_timeslot('1000','1120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10087'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',7)
  Sec.add_timeslot('1700','1750',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10088'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',5)
  Sec.add_timeslot('1400','1650',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10089'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',6)
  Sec.add_timeslot('1900','2150',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10090'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',9)
  Sec.add_timeslot('0800','1050',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10091'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',7)
  Sec.add_timeslot('1900','1950',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10092'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',6)
  Sec.add_timeslot('1200','1250',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10093'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',10)
  Sec.add_timeslot('1200','1450',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10094'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',8)
  Sec.add_timeslot('1200','1450',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10095'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('2000','2120',9)
  Sec.add_timeslot('1300','1420',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10096'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',2)
  Sec.add_timeslot('1700','1750',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10097'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',4)
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('0900','1020',9)
  Sec.add_timeslot('0800','0920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10098'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',5)
  Sec.add_timeslot('1600','1720',4)
  Sec.add_timeslot('1700','1820',10)
  Sec.add_timeslot('1600','1720',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10099'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1800','1920',5)
  Sec.add_timeslot('1000','1120',9)
  Sec.add_timeslot('1800','1920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10100'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('1700','1820',5)
  Sec.add_timeslot('1300','1420',7)
  Sec.add_timeslot('1700','1820',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10101'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',7)
  Sec.add_timeslot('1200','1450',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10102'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',8)
  Sec.add_timeslot('1000','1250',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10103'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',7)
  Sec.add_timeslot('1200','1250',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10104'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',9)
  Sec.add_timeslot('1700','1750',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10105'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('1300','1420',3)
  Sec.add_timeslot('1600','1720',7)
  Sec.add_timeslot('1300','1420',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10106'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',8)
  Sec.add_timeslot('1200','1450',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10107'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('1400','1520',3)
  Sec.add_timeslot('1400','1520',6)
  Sec.add_timeslot('1400','1520',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10108'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1400','1520',2)
  Sec.add_timeslot('0900','1020',10)
  Sec.add_timeslot('1400','1520',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10109'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',8)
  Sec.add_timeslot('1400','1650',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10110'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',1)
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('1000','1120',6)
  Sec.add_timeslot('1300','1420',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10111'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',3)
  Sec.add_timeslot('1400','1520',4)
  Sec.add_timeslot('1000','1120',8)
  Sec.add_timeslot('1400','1520',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10112'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',7)
  Sec.add_timeslot('1400','1450',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10113'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',5)
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('1000','1120',10)
  Sec.add_timeslot('1800','1920',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10114'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',1)
  Sec.add_timeslot('1100','1150',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10115'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('1200','1320',4)
  Sec.add_timeslot('1600','1720',6)
  Sec.add_timeslot('1200','1320',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10116'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('1500','1620',3)
  Sec.add_timeslot('1300','1420',10)
  Sec.add_timeslot('1500','1620',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10117'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1750',9)
  Sec.add_timeslot('1900','2150',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10118'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('1300','1420',1)
  Sec.add_timeslot('1600','1720',7)
  Sec.add_timeslot('1300','1420',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10119'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',4)
  Sec.add_timeslot('1700','1820',3)
  Sec.add_timeslot('1300','1420',9)
  Sec.add_timeslot('1700','1820',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10120'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',4)
  Sec.add_timeslot('1400','1520',2)
  Sec.add_timeslot('1300','1420',9)
  Sec.add_timeslot('1400','1520',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10121'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',4)
  Sec.add_timeslot('0800','0920',3)
  Sec.add_timeslot('0800','0920',9)
  Sec.add_timeslot('0800','0920',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10122'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',4)
  Sec.add_timeslot('1100','1150',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10123'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',6)
  Sec.add_timeslot('1700','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10124'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',8)
  Sec.add_timeslot('1300','1350',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10125'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',1)
  Sec.add_timeslot('1600','1720',5)
  Sec.add_timeslot('0800','0920',6)
  Sec.add_timeslot('1600','1720',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10126'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('2000','2120',10)
  Sec.add_timeslot('1100','1220',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10127'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',7)
  Sec.add_timeslot('1700','1750',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10128'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',5)
  Sec.add_timeslot('1400','1650',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10129'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',2)
  Sec.add_timeslot('1300','1420',3)
  Sec.add_timeslot('1400','1520',7)
  Sec.add_timeslot('1300','1420',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10130'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',1)
  Sec.add_timeslot('1700','1820',3)
  Sec.add_timeslot('1700','1820',6)
  Sec.add_timeslot('1700','1820',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10131'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',4)
  Sec.add_timeslot('1000','1120',2)
  Sec.add_timeslot('1800','1920',9)
  Sec.add_timeslot('1000','1120',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10132'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',2)
  Sec.add_timeslot('1200','1250',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10133'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',9)
  Sec.add_timeslot('1400','1450',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10134'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',8)
  Sec.add_timeslot('1800','1850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10135'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',4)
  Sec.add_timeslot('1800','2050',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10136'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',1)
  Sec.add_timeslot('1300','1550',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10137'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1800','1920',4)
  Sec.add_timeslot('0900','1020',10)
  Sec.add_timeslot('1800','1920',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10138'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',10)
  Sec.add_timeslot('1700','1750',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10139'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',7)
  Sec.add_timeslot('1700','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10140'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',1)
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('1500','1620',6)
  Sec.add_timeslot('1100','1220',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10141'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1320',4)
  Sec.add_timeslot('1700','1820',2)
  Sec.add_timeslot('1200','1320',9)
  Sec.add_timeslot('1700','1820',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10142'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',3)
  Sec.add_timeslot('0900','1020',2)
  Sec.add_timeslot('1300','1420',8)
  Sec.add_timeslot('0900','1020',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10143'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',7)
  Sec.add_timeslot('1000','1050',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10144'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',10)
  Sec.add_timeslot('1200','1450',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10145'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',3)
  Sec.add_timeslot('1400','1520',4)
  Sec.add_timeslot('0800','0920',8)
  Sec.add_timeslot('1400','1520',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10146'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',4)
  Sec.add_timeslot('1300','1550',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10147'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',10)
  Sec.add_timeslot('1700','1950',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10148'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',5)
  Sec.add_timeslot('0900','1020',4)
  Sec.add_timeslot('1800','1920',10)
  Sec.add_timeslot('0900','1020',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10149'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',8)
  Sec.add_timeslot('1400','1450',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10150'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',1)
  Sec.add_timeslot('0800','1050',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10151'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',2)
  Sec.add_timeslot('1500','1620',4)
  Sec.add_timeslot('1500','1620',7)
  Sec.add_timeslot('1500','1620',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10152'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('1600','1720',6)
  Sec.add_timeslot('0800','0920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10153'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',3)
  Sec.add_timeslot('0900','0950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10154'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',1)
  Sec.add_timeslot('1500','1620',2)
  Sec.add_timeslot('0900','1020',6)
  Sec.add_timeslot('1500','1620',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10155'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',6)
  Sec.add_timeslot('1800','2050',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10156'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',2)
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('1100','1220',7)
  Sec.add_timeslot('0900','1020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10157'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',8)
  Sec.add_timeslot('1400','1650',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10158'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1550',7)
  Sec.add_timeslot('1300','1550',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10159'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',6)
  Sec.add_timeslot('1800','1850',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10160'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',9)
  Sec.add_timeslot('1000','1050',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10161'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',4)
  Sec.add_timeslot('1500','1750',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10162'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',7)
  Sec.add_timeslot('1400','1450',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10163'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',3)
  Sec.add_timeslot('1500','1620',4)
  Sec.add_timeslot('2000','2120',8)
  Sec.add_timeslot('1500','1620',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10164'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('1600','1720',7)
  Sec.add_timeslot('0900','1020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10165'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',4)
  Sec.add_timeslot('0900','0950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10166'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',1)
  Sec.add_timeslot('0900','1150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10167'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',7)
  Sec.add_timeslot('1100','1150',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10168'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',6)
  Sec.add_timeslot('1200','1450',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10169'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',5)
  Sec.add_timeslot('1400','1520',3)
  Sec.add_timeslot('1400','1520',10)
  Sec.add_timeslot('1400','1520',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10170'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',3)
  Sec.add_timeslot('1900','1950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10171'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',5)
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1000','1120',10)
  Sec.add_timeslot('1000','1120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10172'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',5)
  Sec.add_timeslot('1700','1820',3)
  Sec.add_timeslot('1500','1620',10)
  Sec.add_timeslot('1700','1820',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10173'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1100','1220',8)
  Sec.add_timeslot('0900','1020',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10174'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',7)
  Sec.add_timeslot('1200','1250',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10175'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('1700','1820',3)
  Sec.add_timeslot('1400','1520',6)
  Sec.add_timeslot('1700','1820',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10176'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',3)
  Sec.add_timeslot('1700','1750',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10177'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1750',2)
  Sec.add_timeslot('0900','1150',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10178'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',6)
  Sec.add_timeslot('1900','1950',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10179'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',6)
  Sec.add_timeslot('1200','1250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10180'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',1)
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('2000','2120',6)
  Sec.add_timeslot('0900','1020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10181'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',1)
  Sec.add_timeslot('1400','1520',2)
  Sec.add_timeslot('2000','2120',6)
  Sec.add_timeslot('1400','1520',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10182'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',1)
  Sec.add_timeslot('1600','1850',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10183'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',2)
  Sec.add_timeslot('2000','2050',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10184'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',7)
  Sec.add_timeslot('1400','1450',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10185'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',3)
  Sec.add_timeslot('0900','0950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10186'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',1)
  Sec.add_timeslot('1800','1850',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10187'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',10)
  Sec.add_timeslot('2000','2050',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10188'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',9)
  Sec.add_timeslot('2000','2250',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10189'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('1700','1820',4)
  Sec.add_timeslot('1100','1220',8)
  Sec.add_timeslot('1700','1820',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10190'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',3)
  Sec.add_timeslot('1000','1250',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10191'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',6)
  Sec.add_timeslot('1000','1050',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10192'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('1900','2020',1)
  Sec.add_timeslot('1300','1420',7)
  Sec.add_timeslot('1900','2020',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10193'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',1)
  Sec.add_timeslot('0800','0920',4)
  Sec.add_timeslot('1900','2020',6)
  Sec.add_timeslot('0800','0920',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10194'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',6)
  Sec.add_timeslot('0900','0950',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10195'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1300','1420',7)
  Sec.add_timeslot('2000','2120',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10196'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',10)
  Sec.add_timeslot('1100','1350',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10197'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',8)
  Sec.add_timeslot('0900','1150',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10198'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',3)
  Sec.add_timeslot('1600','1850',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10199'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',1)
  Sec.add_timeslot('1900','2150',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10200'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',10)
  Sec.add_timeslot('1900','1950',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10201'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('1200','1320',4)
  Sec.add_timeslot('1600','1720',7)
  Sec.add_timeslot('1200','1320',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10202'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',9)
  Sec.add_timeslot('1300','1350',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10203'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',5)
  Sec.add_timeslot('1400','1650',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10204'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',7)
  Sec.add_timeslot('2000','2250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10205'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1300','1420',7)
  Sec.add_timeslot('1800','1920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10206'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',7)
  Sec.add_timeslot('1000','1250',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10207'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',9)
  Sec.add_timeslot('0900','0950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10208'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',3)
  Sec.add_timeslot('1100','1220',2)
  Sec.add_timeslot('0800','0920',8)
  Sec.add_timeslot('1100','1220',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10209'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',7)
  Sec.add_timeslot('1300','1550',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10210'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1700','1820',4)
  Sec.add_timeslot('0900','1020',10)
  Sec.add_timeslot('1700','1820',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10211'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',6)
  Sec.add_timeslot('2000','2250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10212'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',4)
  Sec.add_timeslot('0800','1050',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10213'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('1600','1720',6)
  Sec.add_timeslot('1600','1720',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10214'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',10)
  Sec.add_timeslot('1100','1350',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10215'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',10)
  Sec.add_timeslot('1600','1650',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10216'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',6)
  Sec.add_timeslot('1200','1250',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10217'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',2)
  Sec.add_timeslot('0900','1150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10218'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',3)
  Sec.add_timeslot('2000','2120',2)
  Sec.add_timeslot('1900','2020',8)
  Sec.add_timeslot('2000','2120',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10219'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',5)
  Sec.add_timeslot('0900','0950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10220'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',1)
  Sec.add_timeslot('1400','1520',3)
  Sec.add_timeslot('1100','1220',6)
  Sec.add_timeslot('1400','1520',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10221'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('2000','2120',10)
  Sec.add_timeslot('1400','1520',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10222'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',2)
  Sec.add_timeslot('1600','1720',4)
  Sec.add_timeslot('0800','0920',7)
  Sec.add_timeslot('1600','1720',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10223'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',1)
  Sec.add_timeslot('1700','1820',2)
  Sec.add_timeslot('2000','2120',6)
  Sec.add_timeslot('1700','1820',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10224'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',5)
  Sec.add_timeslot('1600','1850',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10225'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',3)
  Sec.add_timeslot('1300','1550',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10226'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',1)
  Sec.add_timeslot('1100','1350',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10227'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',10)
  Sec.add_timeslot('1400','1650',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10228'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',9)
  Sec.add_timeslot('1700','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10229'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',3)
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('1600','1720',8)
  Sec.add_timeslot('1300','1420',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10230'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',2)
  Sec.add_timeslot('1800','2050',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10231'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('1500','1620',3)
  Sec.add_timeslot('1800','1920',7)
  Sec.add_timeslot('1500','1620',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10232'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('1600','1720',6)
  Sec.add_timeslot('1600','1720',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10233'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',10)
  Sec.add_timeslot('1800','1850',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10234'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('2000','2120',10)
  Sec.add_timeslot('1100','1220',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10235'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',4)
  Sec.add_timeslot('1200','1320',1)
  Sec.add_timeslot('1400','1520',9)
  Sec.add_timeslot('1200','1320',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10236'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',9)
  Sec.add_timeslot('1700','1950',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10237'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',5)
  Sec.add_timeslot('0900','0950',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10238'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',10)
  Sec.add_timeslot('1000','1050',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10239'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',9)
  Sec.add_timeslot('1900','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10240'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',7)
  Sec.add_timeslot('1600','1850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10241'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',1)
  Sec.add_timeslot('1700','1750',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10242'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',4)
  Sec.add_timeslot('2000','2120',2)
  Sec.add_timeslot('1300','1420',9)
  Sec.add_timeslot('2000','2120',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10243'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',4)
  Sec.add_timeslot('0800','0850',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10244'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',8)
  Sec.add_timeslot('1700','1950',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10245'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',3)
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('1900','2020',8)
  Sec.add_timeslot('1300','1420',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10246'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',6)
  Sec.add_timeslot('1100','1350',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10247'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',2)
  Sec.add_timeslot('1300','1550',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10248'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',3)
  Sec.add_timeslot('0900','1150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10249'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',1)
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('0800','0920',6)
  Sec.add_timeslot('0900','1020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10250'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('1500','1620',2)
  Sec.add_timeslot('0900','1020',8)
  Sec.add_timeslot('1500','1620',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10251'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('1600','1720',3)
  Sec.add_timeslot('0800','0920',10)
  Sec.add_timeslot('1600','1720',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10252'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',1)
  Sec.add_timeslot('2000','2050',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10253'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',8)
  Sec.add_timeslot('0800','0850',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10254'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',3)
  Sec.add_timeslot('0900','1150',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10255'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('1500','1620',5)
  Sec.add_timeslot('1100','1220',8)
  Sec.add_timeslot('1500','1620',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10256'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',3)
  Sec.add_timeslot('1500','1750',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10257'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',7)
  Sec.add_timeslot('2000','2050',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10258'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',1)
  Sec.add_timeslot('1700','1820',4)
  Sec.add_timeslot('1300','1420',6)
  Sec.add_timeslot('1700','1820',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10259'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',4)
  Sec.add_timeslot('1700','1950',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10260'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1550',1)
  Sec.add_timeslot('2000','2250',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10261'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',9)
  Sec.add_timeslot('1100','1150',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10262'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',6)
  Sec.add_timeslot('1300','1350',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10263'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('2000','2120',9)
  Sec.add_timeslot('1300','1420',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10264'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',3)
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('2000','2120',8)
  Sec.add_timeslot('1100','1220',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10265'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',1)
  Sec.add_timeslot('1500','1620',2)
  Sec.add_timeslot('1900','2020',6)
  Sec.add_timeslot('1500','1620',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10266'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('0800','0920',1)
  Sec.add_timeslot('1300','1420',7)
  Sec.add_timeslot('0800','0920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10267'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',5)
  Sec.add_timeslot('1900','1950',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10268'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1100','1220',5)
  Sec.add_timeslot('1800','1920',6)
  Sec.add_timeslot('1100','1220',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10269'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',7)
  Sec.add_timeslot('1300','1550',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10270'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',3)
  Sec.add_timeslot('1900','2150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10271'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',6)
  Sec.add_timeslot('1800','2050',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10272'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',4)
  Sec.add_timeslot('1000','1120',2)
  Sec.add_timeslot('1600','1720',9)
  Sec.add_timeslot('1000','1120',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10273'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',3)
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('1500','1620',8)
  Sec.add_timeslot('1800','1920',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10274'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',1)
  Sec.add_timeslot('1400','1450',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10275'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',7)
  Sec.add_timeslot('1900','2150',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10276'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',2)
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1800','1920',7)
  Sec.add_timeslot('1000','1120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10277'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',10)
  Sec.add_timeslot('1900','2150',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10278'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',9)
  Sec.add_timeslot('1500','1750',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10279'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',2)
  Sec.add_timeslot('1600','1850',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10280'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',4)
  Sec.add_timeslot('1600','1850',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10281'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',5)
  Sec.add_timeslot('0900','1150',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10282'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',8)
  Sec.add_timeslot('2000','2050',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10283'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1750',2)
  Sec.add_timeslot('1300','1550',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10284'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',1)
  Sec.add_timeslot('0900','0950',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10285'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',3)
  Sec.add_timeslot('2000','2050',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10286'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',1)
  Sec.add_timeslot('1100','1150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10287'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1750',8)
  Sec.add_timeslot('0900','1150',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10288'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',6)
  Sec.add_timeslot('1400','1450',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10289'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1620',3)
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('1500','1620',8)
  Sec.add_timeslot('2000','2120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10290'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',6)
  Sec.add_timeslot('1600','1650',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10291'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',6)
  Sec.add_timeslot('1300','1550',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10292'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',5)
  Sec.add_timeslot('1300','1420',3)
  Sec.add_timeslot('1300','1420',10)
  Sec.add_timeslot('1300','1420',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10293'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1100','1220',5)
  Sec.add_timeslot('1800','1920',6)
  Sec.add_timeslot('1100','1220',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10294'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',2)
  Sec.add_timeslot('0800','1050',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10295'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',4)
  Sec.add_timeslot('0900','1150',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10296'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('1000','1120',9)
  Sec.add_timeslot('1600','1720',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10297'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',2)
  Sec.add_timeslot('1100','1350',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10298'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',5)
  Sec.add_timeslot('1200','1320',4)
  Sec.add_timeslot('1700','1820',10)
  Sec.add_timeslot('1200','1320',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10299'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('1900','2020',5)
  Sec.add_timeslot('1100','1220',9)
  Sec.add_timeslot('1900','2020',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10300'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',6)
  Sec.add_timeslot('1500','1550',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10301'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',6)
  Sec.add_timeslot('1000','1250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10302'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',5)
  Sec.add_timeslot('1100','1150',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10303'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',1)
  Sec.add_timeslot('1500','1550',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10304'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',1)
  Sec.add_timeslot('1700','1750',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10305'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',1)
  Sec.add_timeslot('0800','1050',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10306'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1750',5)
  Sec.add_timeslot('1600','1650',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10307'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',5)
  Sec.add_timeslot('1300','1350',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10308'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',5)
  Sec.add_timeslot('1300','1550',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10309'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1420',2)
  Sec.add_timeslot('1200','1320',1)
  Sec.add_timeslot('1300','1420',7)
  Sec.add_timeslot('1200','1320',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10310'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',3)
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('2000','2120',8)
  Sec.add_timeslot('1600','1720',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10311'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',6)
  Sec.add_timeslot('2000','2050',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10312'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',3)
  Sec.add_timeslot('1500','1620',5)
  Sec.add_timeslot('1700','1820',8)
  Sec.add_timeslot('1500','1620',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10313'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',10)
  Sec.add_timeslot('1500','1550',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10314'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',4)
  Sec.add_timeslot('1200','1250',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10315'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',5)
  Sec.add_timeslot('1900','1950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10316'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',10)
  Sec.add_timeslot('1600','1850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10317'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',6)
  Sec.add_timeslot('1900','2150',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10318'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',2)
  Sec.add_timeslot('1200','1250',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10319'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1850',1)
  Sec.add_timeslot('1400','1450',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10320'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',3)
  Sec.add_timeslot('1100','1350',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10321'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',10)
  Sec.add_timeslot('2000','2050',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10322'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',3)
  Sec.add_timeslot('1900','1950',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10323'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','1050',6)
  Sec.add_timeslot('2000','2250',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10324'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',8)
  Sec.add_timeslot('1600','1850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10325'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',2)
  Sec.add_timeslot('1500','1550',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10326'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',6)
  Sec.add_timeslot('1000','1250',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10327'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',2)
  Sec.add_timeslot('1900','2020',5)
  Sec.add_timeslot('2000','2120',7)
  Sec.add_timeslot('1900','2020',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10328'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1550',5)
  Sec.add_timeslot('1200','1450',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10329'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',3)
  Sec.add_timeslot('1300','1550',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10330'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',8)
  Sec.add_timeslot('1600','1850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10331'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',3)
  Sec.add_timeslot('1500','1550',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10332'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',3)
  Sec.add_timeslot('1300','1350',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10333'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','0950',9)
  Sec.add_timeslot('0800','0850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10334'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',2)
  Sec.add_timeslot('2000','2050',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10335'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',4)
  Sec.add_timeslot('1800','1850',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10336'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',1)
  Sec.add_timeslot('1600','1650',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10337'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1320',4)
  Sec.add_timeslot('0900','1020',2)
  Sec.add_timeslot('1200','1320',9)
  Sec.add_timeslot('0900','1020',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10338'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',4)
  Sec.add_timeslot('1900','1950',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10339'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','1920',3)
  Sec.add_timeslot('1500','1620',1)
  Sec.add_timeslot('1800','1920',8)
  Sec.add_timeslot('1500','1620',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10340'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',9)
  Sec.add_timeslot('2000','2250',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10341'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',8)
  Sec.add_timeslot('1500','1550',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10342'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',1)
  Sec.add_timeslot('1000','1120',4)
  Sec.add_timeslot('1000','1120',6)
  Sec.add_timeslot('1000','1120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10343'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',3)
  Sec.add_timeslot('1300','1350',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10344'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',10)
  Sec.add_timeslot('1400','1450',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10345'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1200','1320',1)
  Sec.add_timeslot('0900','1020',10)
  Sec.add_timeslot('1200','1320',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10346'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',2)
  Sec.add_timeslot('0800','1050',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10347'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',7)
  Sec.add_timeslot('0800','1050',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10348'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2250',6)
  Sec.add_timeslot('1900','2150',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10349'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',1)
  Sec.add_timeslot('1200','1320',5)
  Sec.add_timeslot('2000','2120',6)
  Sec.add_timeslot('1200','1320',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10350'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',3)
  Sec.add_timeslot('1900','1950',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10351'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',3)
  Sec.add_timeslot('1300','1550',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10352'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',2)
  Sec.add_timeslot('1200','1450',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10353'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1020',5)
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('0900','1020',10)
  Sec.add_timeslot('1800','1920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10354'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',5)
  Sec.add_timeslot('1200','1320',1)
  Sec.add_timeslot('1000','1120',10)
  Sec.add_timeslot('1200','1320',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10355'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',10)
  Sec.add_timeslot('1600','1850',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10356'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',3)
  Sec.add_timeslot('1700','1820',1)
  Sec.add_timeslot('1400','1520',8)
  Sec.add_timeslot('1700','1820',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10357'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1150',6)
  Sec.add_timeslot('1800','1850',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10358'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',8)
  Sec.add_timeslot('2000','2250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10359'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1120',2)
  Sec.add_timeslot('1800','1920',3)
  Sec.add_timeslot('1000','1120',7)
  Sec.add_timeslot('1800','1920',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10360'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',3)
  Sec.add_timeslot('1000','1250',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10361'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',1)
  Sec.add_timeslot('1300','1350',5)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10362'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',3)
  Sec.add_timeslot('1900','2150',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10363'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',2)
  Sec.add_timeslot('0900','1020',3)
  Sec.add_timeslot('1700','1820',7)
  Sec.add_timeslot('0900','1020',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10364'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2150',10)
  Sec.add_timeslot('2000','2250',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10365'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',1)
  Sec.add_timeslot('1700','1750',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10366'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',7)
  Sec.add_timeslot('0900','1150',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10367'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',3)
  Sec.add_timeslot('1800','2050',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10368'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',8)
  Sec.add_timeslot('1500','1550',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10369'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',3)
  Sec.add_timeslot('2000','2250',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10370'
  Sec.name = 'BIO1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'BIO1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',2)
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('1900','2020',7)
  Sec.add_timeslot('1400','1520',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10371'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',10)
  Sec.add_timeslot('1400','1650',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10372'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','2020',4)
  Sec.add_timeslot('0900','1020',1)
  Sec.add_timeslot('1900','2020',9)
  Sec.add_timeslot('0900','1020',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10373'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1520',1)
  Sec.add_timeslot('1600','1720',3)
  Sec.add_timeslot('1400','1520',6)
  Sec.add_timeslot('1600','1720',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10374'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2050',2)
  Sec.add_timeslot('1800','1850',1)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10375'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1300','1350',10)
  Sec.add_timeslot('1700','1750',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10376'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1450',6)
  Sec.add_timeslot('1200','1250',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10377'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1350',7)
  Sec.add_timeslot('1500','1750',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10378'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0900','1150',1)
  Sec.add_timeslot('1600','1850',3)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10379'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('2000','2120',5)
  Sec.add_timeslot('2000','2120',4)
  Sec.add_timeslot('2000','2120',10)
  Sec.add_timeslot('2000','2120',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10380'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1500','1550',4)
  Sec.add_timeslot('1600','1650',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10381'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('1600','1720',2)
  Sec.add_timeslot('1100','1220',9)
  Sec.add_timeslot('1600','1720',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10382'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('0800','0920',10)
  Sec.add_timeslot('1600','1720',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10383'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1400','1650',2)
  Sec.add_timeslot('1800','2050',4)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10384'
  Sec.name = 'CHEM1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CHEM1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('0800','0850',10)
  Sec.add_timeslot('0800','0850',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10385'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1320',5)
  Sec.add_timeslot('0800','0920',1)
  Sec.add_timeslot('1200','1320',10)
  Sec.add_timeslot('0800','0920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10386'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('1000','1120',5)
  Sec.add_timeslot('1100','1220',8)
  Sec.add_timeslot('1000','1120',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10387'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1250',3)
  Sec.add_timeslot('1000','1050',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10388'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1200','1450',9)
  Sec.add_timeslot('0900','1150',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10389'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1050',9)
  Sec.add_timeslot('1400','1450',8)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10390'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1000','1250',8)
  Sec.add_timeslot('1700','1950',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10391'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1900','1950',6)
  Sec.add_timeslot('1400','1450',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10392'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1800','2050',6)
  Sec.add_timeslot('2000','2250',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10393'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1820',1)
  Sec.add_timeslot('0800','0920',4)
  Sec.add_timeslot('1700','1820',6)
  Sec.add_timeslot('0800','0920',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10394'
  Sec.name = 'MATH1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'MATH1010'
  Sec.campus = ''
  Sec.cType = 'Tut'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1650',8)
  Sec.add_timeslot('0800','0850',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10395'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1720',1)
  Sec.add_timeslot('0800','0920',5)
  Sec.add_timeslot('1600','1720',6)
  Sec.add_timeslot('0800','0920',10)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10396'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',4)
  Sec.add_timeslot('1200','1320',2)
  Sec.add_timeslot('1100','1220',9)
  Sec.add_timeslot('1200','1320',7)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10397'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',1)
  Sec.add_timeslot('1800','1920',4)
  Sec.add_timeslot('1100','1220',6)
  Sec.add_timeslot('1800','1920',9)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10398'
  Sec.name = 'HIST1000'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'HIST1000'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1700','1950',5)
  Sec.add_timeslot('1100','1350',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10399'
  Sec.name = 'PHY1010'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'PHY1010'
  Sec.campus = ''
  Sec.cType = 'Lab'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1600','1850',5)
  Sec.add_timeslot('2000','2250',2)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  Sec = Section() 
  Sec.CRN = '10400'
  Sec.name = 'CSCI1040'
  Sec.subject = ''
  Sec.semester = '201509'
  Sec.course = 'CSCI1040'
  Sec.campus = ''
  Sec.cType = 'Lec'
  Sec.remainingSeats = 100 
  Sec.add_timeslot('1100','1220',3)
  Sec.add_timeslot('1800','1920',1)
  Sec.add_timeslot('1100','1220',8)
  Sec.add_timeslot('1800','1920',6)
  Sec.cleanup()
  Sec.printToScreen()
  nodes.append(Sec)
  return nodes 
