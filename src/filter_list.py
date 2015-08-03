from course import *


def filter_section_list(original,courses,min_remaining_seats=0):
   print "Before:",len(original)
   results = []
   for Sec in original:
      if Sec.course in courses and Sec.remainingSeats > min_remaining_seats:
         results.append(Sec)
   return results


def types_within_subset(allcourses):
#   allcourses = filter_section_list(allcourses,courses,-1)
   allsecs = []
   for sec in allcourses:
      allsecs.append(sec.course + "_" + sec.cType)
   total = list(set(allsecs))
   return total

def get_list_of_CRNS(allcourses):
   crns = []
   for C in allcourses:
      crns.append(C.CRN)
   return crns





