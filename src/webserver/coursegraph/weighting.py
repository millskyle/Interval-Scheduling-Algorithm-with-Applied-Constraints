from scraper.course import *
import math
from userpreferences import UserPrefs

def addWeights(Schedule):
   weight = 0.0
   for CRN in Schedule:
      weight += CRN.weight
   return weight

def optimumTimeOfDay(Schedule):
   """KYLE:  Weights each course highly based on a Gaussian curve centered around
             a time in the desired block."""
   if UserPrefs.PreferTimeOfDay=="None":
      return 0.0
   else:
      opt = { "Morning":"1900","Afternoon":"1400","Evening":"0900" }
      optimum_time = float(opt.get(UserPrefs.PreferTimeOfDay,"1200"))
      score = 0.
      for CRN in Schedule:
         for ts in CRN.timeslots:
            score += (int(ts.eTime) - int(ts.sTime)) * (2.0 * math.exp( -1.3e-5 * ( (float(ts.sTime)+float(ts.eTime))/2.0 - optimum_time)**2 ) - 1.0)
         scale=1000.0
      return scale*score/len(Schedule)

def campusPref(Schedule):
   """DINO"""
   for CRN in Schedule:
      if UserPrefs.preferredCampus == "North" and CRN.campus == "North":
         CRN.weight += 1.e6/len(Schedule)
      if UserPrefs.preferredCampus == "Downtown" and CRN.campus == "Downtown":
         CRN.weight += 1.e6/len(Schedule)
      if UserPrefs.preferredCampus == "Other" and CRN.campus == "Other":
         CRN.weight += 1.e6/len(Schedule)

def preferred_crn(Schedule):
    """DINO"""
    for CRN in Schedule:
        if CRN.CRN in UserPrefs.preferredCRNs:
            CRN.weight+=1.e7

def gap_minimize(Schedule):
   """KYLE"""
   weight=0.
   alltimeslots = []
   for CRN in Schedule:
      for ts in CRN.timeslots:
         alltimeslots.append(ts)
   alltimeslots = sorted(alltimeslots, key=lambda x: str(x.day) + str(x.sTime))
   for i in xrange(len(alltimeslots)-1):
      ts1 = alltimeslots[i]
      ts2 = alltimeslots[i+1]
      if (ts2.day==ts1.day) and (int(ts2.sTime) - int(ts1.eTime)) > 20.:
         weight -= (int(ts2.sTime) - int(ts1.eTime))

   return 10.*weight/len(Schedule)



def course_density(Schedule):
#   """DINO"""
#   weight = 0.
#   for iCRN in Schedule:
#      if not(iCRN.CRN=="55555"):
#         for jCRN in Schedule:
#            for i in iCRN.timeslots:
#               for j in jCRN.timeslots:
#                  if i.day==j.day:
#                     time = int(j.eTime) - int(i.sTime)
#                     if time<=40:
#                        weight +=1000.
#   print "dino course density: ",10*weight/len(Schedule)
   return 0. #10*weight/len(Schedule)




def compute_schedule_score(Schedule):
   score = 0.0

   #Penalize timetables where sections are full
#   score -= sum( [ 1 if x.remainingSeats == 0 else 0 for x in Schedule ]  ) * 1e5

   score += optimumTimeOfDay(Schedule)

   if not(UserPrefs.preferredCampus=="None"):
      campusPref(Schedule)

   if UserPrefs.preferMinGaps == True:
      #score +=5.*course_density2(Schedule)
      score +=5.*gap_minimize(Schedule)

   score += addWeights(Schedule)

   return score




