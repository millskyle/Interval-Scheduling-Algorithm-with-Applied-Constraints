from course import *





def online(Schedule):
   weight = 0.
   counter = 0.
   for CRN in Schedule:
       for ts in CRN.timeslots:
           if this is an online course:
               weight += 1.
   return weight / counter # return a float from -1 to 1


def campus(Schedule):
   weight = 0.
   counter = 0.
   for CRN in Schedule:
       for ts in CRN.timeslots:
           if this is at the North campus:
               weight += 1.
   return weight / counter # return a float from -1 to 1



def myScore(Schedule):
   weight = 0.
   for CRN in Schedule:
       for ts in CRN.timeslots:
       #   doSomeMath
       junk=1
   return 0 # return a float from -1 to 1




def compute_schedule_score(Schedule):
   score = 0.0
   score += campus(Schedule)
   score += online(Schedule)

   return score




