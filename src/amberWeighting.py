from course import *


def earlyRiser(Schedule):
   score = 0.
   counter = 0.
   for CRN in (Schedule):
      for ts in CRN.timeslots:
         if int(ts.sTime) < "1100":
            score += 1.0
         if int(ts.sTime) > "1100" and int(ts.sTime) < "1600":
            score -= 0.5
         if int(ts.sTime) > "1600":
            score -= 1.0
      counter += 1.0
   print str(counter) + "!!!"
   return score / counter

def sleepyHead(Schedule):
   score = 0.
   counter = 0.
   for CRN in (Schedule):
      for ts in CRN.timeslots:
         if int(ts.sTime) < "1100":
            score -= 1.0
         if int(ts.sTime) > "1100" and int(ts.sTime) < "1600":
            score += 0.5
         if int(ts.sTime) > "1600":
            score += 1.0
      print str(counter) + "!!!"
      counter += 1.0
   return score / counter


def physics_is_better(Schedule):
   if Sec.course == "PHY1010U":
      return 1.0
   else:
      return 0.5



