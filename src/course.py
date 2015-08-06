from weighting import *

global IiI
IiI = 0
def iIi():
   global IiI
   IiI +=1
   return IiI

class Graham_Course():

    #Initialize variables
    def __init__(self, crn, ctype, code, rseat, stime, etime, day,
                 sem, subj, campus):
        self.crn = crn
        self.ctype = ctype
        self.code = code
        self.rseat = rseat
        self.stime = stime
        self.etime = etime
        self.day = day
        self.sem = sem
        self.subj = subj
        self.campus = campus

def time2ftime(string):
#  takes a four-character string (e.g. "1234") and returns it with a colon in the centre (e.g. "12:34")
   return string[0:2] + ":" + string[2:4]

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
      self.weight = 0
      self.ID = iIi()
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
   def add_timeslot(self, sTime, eTime, day):
      t = self.Timeslot(sTime,eTime,day)
      self.timeslots.append(t)
   def cleanup(self):
      #remove duplicate timeslots (e.g. labs listed 6 times per semester)
      self.timeslots = set(self.timeslots)
      #remove space in course code:
      self.course = self.course.replace(" ","")
   def printToScreen(self):
      print "\n"
      print self.name, self.CRN, self.cType, "@", self.campus
      for ts in self.timeslots:
         print ts.sTime,ts.eTime,ts.day
   def toDict(self):
      colors = { "Lec":"#FFFF66","Tut":"FF6699", "Lab": "#99FF99" }
      w1 = []
      w2 = []
      for t in self.timeslots:
         if (t.day>5):
            w2.append( {
              "title" : self.course + " " + self.cType + " (" + self.CRN + ")",
              "start" : time2ftime(t.sTime),
              "end"   : time2ftime(t.eTime),
              "dow"   : "[" + str(t.day-5) + "]",
              "color" : colors[self.cType],
              "textColor" : "black",
            })
         else:
            w1.append( {
              "title" : self.course + " " + self.cType + " (" + self.CRN + ")",
              "start" : time2ftime(t.sTime),
              "end"   : time2ftime(t.eTime),
              "dow"   : "[" + str(t.day) + "]",
              "color" : colors[self.cType],
              "textColor" : "black",
            })
      return w1,w2



class Timetable():
   def __init__(self,Schedule):
      a = {"ID":[],
           "CRN": [],
           "course":[],
           "campus":[],
           "cType":[],
           "remainingSeats":[],
           "sTime":[],
           "eTime":[],
           "day":[],
      }
      for CRN in query_results:
          for ts in CRN.timeslots:
              a["CRN"].append(CRN.CRN)
              a["course"].append(CRN.course)
              a["campus"].append(CRN.campus)
              a["cType"].append(CRN.cType)
              a["remainingSeats"].append(CRN.remainingSeats)
              a["sTime"].append(ts.sTime)
              a["eTime"].append(ts.eTime)
              a["day"].append(ts.day)
      self.asDict = a



















