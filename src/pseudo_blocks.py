from course import *
from userpreferences import UserPrefs

def add_days_off_blocks():
   blocks = []
#   preferred_blocks= []
   for dayoff in range(1,11):
      pseudo = Section()
      pseudo.add_timeslot("0001","2359", dayoff)
      pseudo.CRN = "55555"
      pseudo.semester = UserPrefs.semester
      pseudo.remainingSeats = 1000
      pseudo.cType = "Lec"
      pseudo.course = "TimeOff" + str(dayoff)
      pseudo.name = "PSEUDO_DAY_OFF"
      pseudo.cleanup()
      if dayoff in [ i for i in UserPrefs.PreferredDaysOff ] + [ i+5 for i in UserPrefs.PreferredDaysOff ]:
         pseudo.weight = 10000.0
#         preferred_blocks.append(pseudo)
      else:
         pseudo.weight = 5000.0
      blocks.append(pseudo)


   return blocks #,preferred_blocks


def earlyRiser():
   score = 0.
   counter = 0.
 #  blocks = []
   preferred_blocks = []
   for timeoff in range(1,11):
      pseudo = Section()
      pseudo.add_timeslot("1700", "2359", timeoff)
      pseudo.semester = UserPrefs.semester
      pseudo.remainingSeats = 1000
      pseudo.cType = "Lec"
      pseudo.course = "TimeOff" + str(timeoff)
      pseudo.name = "PSEUDO_DAY_OFF"
      pseudo.cleanup()
      pseudo.CRN = "55555"
      if timeoff in [i for i in UserPrefs.PreferredDaysOff]:
         pseudo.weight = 1000.0
      preferred_blocks.append(pseudo)
   return preferred_blocks


