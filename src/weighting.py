from course import *



def sleepyHead(Sec):
   weight = 1.0
   for ts in Sec.timeslots:
      if int(ts.sTime) < 1100:
         weight -= (15.0)*(int(ts.eTime) - int(ts.sTime))
      if int(ts.eTime) > 1500:
         weight += 1.0*(int(ts.eTime) - int(ts.sTime))
   return weight


def physics_is_better(Sec):
   if Sec.course == "PHY1010U":
      return 1.0
   else:
      return 0.5



def compute_section_weight(Sec):
   weight = 0.0
   weight += sleepyHead(Sec)
   return weight



