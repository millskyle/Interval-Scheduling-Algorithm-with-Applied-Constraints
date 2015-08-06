from course import *
from userpreferences import UserPrefs
import amberWeighting
import math

def daysOff(Schedule):
   weight = 0.0
   for CRN in Schedule:
      weight += CRN.weight
   return weight


def optimumTimeOfDay(Schedule):
   optimum_time= float(UserPrefs.OptimumTimeOfDay) 
   counter = 0.
   score = 0.
   for CRN in Schedule:
      for ts in CRN.timeslots:
         counter += (int(ts.eTime) - int(ts.sTime))
         score += (int(ts.eTime) - int(ts.sTime)) * (2.0 * math.exp( -1.3e-5 * ( (float(ts.sTime)+float(ts.eTime))/2.0 - optimum_time)**2 ) - 1.0)
   return score/counter

def campusPref(Schedule):
   for CRN in Schedule:
      if UserPref.campus == "None":
         CRN.weight = 10000
      if UserPref.campus == "North" and CRN.campus:
         CRN.weight = 10000
      if UserPref.campus == "Downtown":
         CRN.weight = 10000
      elif UserPref.campus == "Online":
         CRN.weight = 10000      
 
def myScore(Schedule):
   weight = 0.
   for CRN in Schedule:
      for ts in CRN.timeslots:
         doSomeMath
         junk=1
   return 0 # return a float from -1 to 1



def compute_schedule_score(Schedule):
   score = 0.0
 #  score += optimumTimeOfDay(Schedule)
   score += daysOff(Schedule)
#   score += myScore(Schedule)
   return score




