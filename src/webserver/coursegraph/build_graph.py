import matplotlib.pyplot as plt
import networkx as nx
from JSON_io import JSON_dump
from scraper.course import *
import styles
from filter_list import  * #filter_section_list, count_types_within_courses
from weighting import *
import pseudo_blocks
from random import randint
from userpreferences import UserPrefs
from config import config

def graph_optimize(query_results):
##NOTE:  At this point, it is assumed that the variable query_results is 
#        a list of all potential courses (as Section() objects), returned 
#        from some database query or web scraping action.

#  populate this list with Section() objects from the query
#   query_results = []

#  populate this with the total number of sections that should be on
#  the calendar, assuming there are no scheduling impossibilities 
#  (e.g.  1 tutorial, 1 lab and 1 lecture each for 3 courses would 
#  result in requiredNumberOfSections = 9)
   requiredSections = types_within_subset(query_results)
   requiredNumberOfSections = len(requiredSections)


  #remove all empty sections from the query
   query_results = [i for i in query_results if i.remainingSeats > 0 ]


   for i in range(10):
      print "!"*100
   for CRN in query_results:
      CRN.printToScreen()

#  SOME CONFIGURATION:
   calculate_how_many = config.generate_this_many_schedules
   max_attempts = config.maximum_attempts_per_schedule

##start code

#   query_results = generate_dense_data() #uncomment this and the next line to use fake course data
#   requiredNumberOfSections = 9

#Construct the graph object
   G = nx.Graph()
#   iG = ig.Graph()
#add all potential courses as nodes to the graph
   for Sec in query_results:
      G.add_node(Sec, label=Sec.course[0:2],selected=1.0)


   if len(UserPrefs.preferredCRNs) > 0:
      preferred_crn(G.nodes())



   # If the user wants days off, create pseudo-events that span every day.  
   # Weight them so that if possible, they will be selected.
   if UserPrefs.MaximizeDaysOff:
      for pseudoBlock in pseudo_blocks.add_days_off_blocks():
         G.add_node(pseudoBlock, label="XX", selected = 3.0, score = 1.0 )

   # If the user prefers to have mornings (or afternoons or evenings) FREE, then
   # create the corresponding pseudo-blocks to conflict with all courses at those times.
   if not(UserPrefs.PreferTimeOfDay == ""):
      for pseudoBlock in pseudo_blocks.TimeCut():
         G.add_node(pseudoBlock, label="XX", selected = 3.0, score = 1.0 )


#map the type to a float for coloring the graph output
# {
   typemapping = { 'Lec': styles.colours.lec, 'Tut':styles.colours.tut, 'Lab':styles.colours.lab, 'Oth': styles.colours.oth }
   colors = [typemapping[node.cType] for node in G.nodes() ]
# }


   all_edges = []
#  Add edges between the nodes, representing conflicts (two courses for which a user
#  cannot be simultaneously registered.
   for i,iSec in enumerate(G.nodes()):
      for j,jSec in enumerate(G.nodes()):
         if i<j:
            have_edge = False
            if ( (iSec.cType == jSec.cType) and (jSec.course==iSec.course)):
               # If the two sections are from the same course
               # and are the same type, then they're incompatible.
               # (e.g. can't take two physics tutorials)
               have_edge = True
            else:
               for itimeslot in iSec.timeslots:
                  for jtimeslot in jSec.timeslots:
                     #If they overlap in time:
                     if (  (itimeslot.eTime >= jtimeslot.sTime) and (itimeslot.sTime <= jtimeslot.eTime) and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     elif (  (jtimeslot.eTime >= itimeslot.sTime) and (jtimeslot.sTime <= itimeslot.eTime) and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     elif (itimeslot.sTime == jtimeslot.sTime and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     elif (jtimeslot.sTime == itimeslot.sTime and jtimeslot.day==itimeslot.day ):
                        have_edge = True

            if have_edge:
            #If have_edge is, at this point, true then
            #these two nodes are incompatible with each other.
            #Add an edge between them
               G.add_edge(iSec,jSec)


   all_valid = []
   consolation = []
   best_score = -1.0e9

   globalFailure = True


   # Here we begin generating many different schedules.  After each schedule
   # is found (and verified to contain the correct number of courses), it is scored and
   # added to a list of all valid courses.
   for potentialSchedule in xrange(calculate_how_many):
      print "Attempting to build schedule",potentialSchedule
      successfully_scheduled_sections = 0
      tries = 0
      bestTry = []
      bestTryCount = 0
      failure = True
      for tries in xrange(max_attempts):
         # compute the maximal independent set.  
         # This is NOT the MAXIMUM independent set. Thus we must loop a few times
         # to get the largest possible set.
         thissched = nx.maximal_independent_set(G)

         # We need to count the number of pseudo-blocks in the generated schedule since we
         # must only break out of this loop once we have enough sections in our schedule.  
         # Pseudo blocks count, my default, and must be subtracted.
         numberofblanks = 0
         for CRN in thissched:
            if CRN.CRN == "55555":
               numberofblanks+=1
         successfully_scheduled_sections = len(thissched)

         #print "   Attempt",tries
         if (successfully_scheduled_sections >= requiredNumberOfSections + numberofblanks):
            failure=False
            break
         else:
            if successfully_scheduled_sections > bestTryCount:
               bestTryCount = successfully_scheduled_sections
               bestTry = thissched
            thissched = bestTry


      #Remove all pseudo events now.  They've served their purpose.
      newsched = []
      for i in range(len(thissched)):
         if not(thissched[i].CRN=="55555"):
            newsched.append(thissched[i])
      thissched = newsched


      #Build a timetable object to hold timetable and associated data.
      thisTimeTable = Timetable(thissched, compute_schedule_score(thissched))

      if not(failure):
         thisTimeTable.isValid = "VALID"
         globalFailure = False
         all_valid.append(thisTimeTable)
         #print "Timetable option",potentialSchedule,"\t\t Score:",thisScore
         #if thisScore > best_score:
         #   best_score = thisScore
         #   bestsched = thissched
      else:
         consolation.append(thisTimeTable)
         thisTimeTable.isValid = "INVALID"


   all_valid = sorted(all_valid, key = lambda x: x.score, reverse=True)
   consolation = sorted(consolation, key = lambda x: len(x.Schedule), reverse=True)



   if globalFailure:
      print "FAILURE to find even one valid schedule"

   good_schedules = len(all_valid)
   if good_schedules >= config.number_of_schedules_to_show_user:
      schedules_to_return = all_valid[0:config.number_of_schedules_to_show_user]
   else:
      schedules_to_return = all_valid[0:good_schedules] + consolation[0:config.number_of_schedules_to_show_user - good_schedules]

   for tt in schedules_to_return:
      missingCourses(tt,requiredSections)
      tt.notes.append("List of CRNs displayed on this time table:")
      last_course = ""
      stringg = ""
      for CRN in sorted(tt.Schedule, key=lambda x: x.course):
         if not(CRN.course == last_course):
            tt.notes.append(stringg)
            stringg = CRN.course + ": "
            last_course = CRN.course
         else:
            stringg = stringg + ", "
         stringg = stringg + CRN.CRN #+ ", "
      tt.notes.append(stringg)


      print len(tt.Schedule)
      for wn in tt.warnings:
         print wn
      for nn in tt.notes:
         print nn

   print "FOUND",len(schedules_to_return),"schedules to return"

   returnData = []
   for thisSchedule in schedules_to_return:
      thisSchedule.w1JSON,thisSchedule.w2JSON = JSON_dump(thisSchedule.Schedule)
      returnData.append(  [ thisSchedule.w1JSON,thisSchedule.w2JSON,thisSchedule.notes,thisSchedule.warnings,thisSchedule.score    ]  )


   return returnData

