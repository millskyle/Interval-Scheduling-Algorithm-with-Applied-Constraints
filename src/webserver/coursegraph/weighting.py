from scraper.course import *
import amberWeighting
import math

def daysOff(Schedule):
   weight = 0.0
   for CRN in Schedule:
      weight += CRN.weight
   return weight


def optimumTimeOfDay(Schedule):
   optimum_time= float(1100)
   counter = 0.
   score = 0.
   for CRN in Schedule:
      for ts in CRN.timeslots:
         counter += (int(ts.eTime) - int(ts.sTime))
         score += (int(ts.eTime) - int(ts.sTime)) * (2.0 * math.exp( -1.3e-5 * ( (float(ts.sTime)+float(ts.eTime))/2.0 - optimum_time)**2 ) - 1.0)
   return score/counter


def myScore(Schedule):
   weight = 0.
   for CRN in Schedule:
      for ts in CRN.timeslots:
      #   doSomeMath
         junk=1
   return 0 # return a float from -1 to 1



def compute_schedule_score(Schedule):
   score = 0.0
#   score += optimumTimeOfDay(Schedule)
#   score+=amberWeighting.earlyRiser(Schedule)
   score+=daysOff(Schedule)
   score += myScore(Schedule)
   return score




