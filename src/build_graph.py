import matplotlib.pyplot as plt
import networkx as nx
from JSON_io import JSON_write
from course import *
import styles
from filter_list import  * #filter_section_list, count_types_within_courses
from sample_data import generate_dense_data
import pseudo_blocks
from random import randint
from userpreferences import UserPrefs

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
   print requiredNumberOfSections,":",requiredSections



##start code

#   query_results = generate_dense_data()
#   requiredNumberOfSections = 9

#Construct the graph object
   G = nx.Graph()

#add all potential courses as nodes to the graph
   for Sec in query_results:
      G.add_node(Sec, label=Sec.course[0:2],selected=1.0)


   comment="""   for day in range(1..10)
   pseudo = Section()
   dayoff = 2
   pseudo.add_timeslot("0800","2200", dayoff)
   pseudo.add_timeslot("0800","2200", dayoff+5)
   pseudo.CRN = "55555"
   pseudo.semester="201509"
   pseudo.remainingSeats = 1000
   pseudo.cType = "Lec"
   pseudo.course = "TimeOff"
   pseudo.name = "PSEUDO_DAY_OFF"
   pseudo.weight = 10000.0
   pseudo.cleanup()
   """

   if UserPrefs.MaximizeDaysOff:
      for pseudoBlock in pseudo_blocks.add_days_off_blocks():
         G.add_node(pseudoBlock, label="XX", selected = 3.0, score = 1.0 )

   if not(UserPrefs.PreferTimeOfDay == ""):
      for pseudoBlock in pseudo_blocks.earlyRiser():
         G.add_node(pseudoBlock, label="XX", selected = 3.0, score = 1.0 )


#map the type to a float for coloring the graph output
# {
   typemapping = { 'Lec': styles.colours.lec, 'Tut':styles.colours.tut, 'Lab':styles.colours.lab, 'Oth': '#000' }
   colors = [typemapping[node.cType] for node in G.nodes() ]
# }


   for i,iSec in enumerate(G.nodes()):
      for j,jSec in enumerate(G.nodes()):
         if i<j:
            have_edge = False
            if ( (iSec.cType == jSec.cType) and (jSec.course==iSec.course)):
               #If the two sections are from the same course and are the same type, then they're incompatible.
               #draw an edge between them
               have_edge = True
            else:
               for itimeslot in iSec.timeslots:
                  for jtimeslot in jSec.timeslots:
                     if (  (itimeslot.eTime >= jtimeslot.sTime) and (itimeslot.sTime <= jtimeslot.eTime) and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     if (  (jtimeslot.eTime >= itimeslot.sTime) and (jtimeslot.sTime <= itimeslot.eTime) and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     ddd="""
                     if (itimeslot.sTime <= jtimeslot.sTime and itimeslot.eTime >= jtimeslot.eTime and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     elif (jtimeslot.sTime <= itimeslot.sTime and jtimeslot.eTime >= itimeslot.eTime and jtimeslot.day==itimeslot.day ):
                        have_edge = True
                     elif ((itimeslot.sTime <= jtimeslot.eTime and itimeslot.eTime >= jtimeslot.eTime and jtimeslot.day==itimeslot.day)):
                        #if they overlap in time, and they're on the same day, then they're incompatible.
                        have_edge = True
                     elif ((jtimeslot.sTime <= itimeslot.eTime and jtimeslot.eTime >= itimeslot.eTime and jtimeslot.day==itimeslot.day)):
                        #if they overlap in time, and they're on the same day, then they're incompatible.
                        have_edge = True
                        """
                     if (itimeslot.sTime == jtimeslot.sTime and itimeslot.day==jtimeslot.day ):
                        have_edge = True
                     if (jtimeslot.sTime == itimeslot.sTime and jtimeslot.day==itimeslot.day ):
                        have_edge = True

            if have_edge:
            #If have_edge is true, then these two nodes are incompatible with each other.
            #Add an edge between them
               G.add_edge(iSec,jSec)




 #  requiredNumberOfSections += 1


   all_valid = []
   calculate_how_many = 200
   max_attempts = 5

   best_score = -1.0e9

   globalFailure = True

   for potentialSchedule in xrange(calculate_how_many):
      successfully_scheduled_sections = 0
      tries = 0
      failure = True
      for tries in xrange(max_attempts):
#      while successfully_scheduled_sections < requiredNumberOfSections:
         # compute the maximal independent set.  
         # This is NOT the MAXIMUM independent set. Thus we must loop a few times
         # to attempt to get the best possible optimization.
         thissched = nx.maximal_independent_set(G )# , [pseudo])
         #compute the weight-score of this
         numberofblanks =0
         for CRN in thissched:
            if CRN.CRN == "55555":
               numberofblanks+=1

         successfully_scheduled_sections = len(thissched) - numberofblanks
#         print "got an MIS with",successfully_scheduled_sections,"elements"
#         tries +=1
         print "   Attempt",tries
         if (successfully_scheduled_sections >= requiredNumberOfSections):
             failure=False
             break

#         if tries > max_attempts:
#            print "Timetable creation failed for timetable option",i
#            failure = True
#            tries = 0
#            break
      if not(failure):
         globalFailure = False
         thisScore = compute_schedule_score(thissched)
         all_valid.append(thissched)
         print "Timetable option",potentialSchedule,"\t\t Score:",thisScore
         if thisScore > best_score:
            best_score = thisScore
            bestsched = thissched


   if globalFailure:
      print "FAILURE to find even one valid schedule"



   print "OUTCOME: the best timetable has score",best_score
   yoursched = bestsched

#   print nx.get_node_attributes(G, 'score')
   chosen = get_list_of_CRNS(yoursched)
   for node in sorted(G.nodes()):
      if node.CRN in chosen:
         G.node[node]['label'] = "**" + G.node[node]['label']+"**"
#         G.node[node]['selected'] = 5.0

#   for Sec in yoursched:
#      G.node[Sec]['selected'] = 5.0

   plt.figure(figsize=[24,20])
   nx.draw_spring(G,
         with_labels=True,
         labels=nx.get_node_attributes(G,'label'),
         node_color=colors,
         node_size=500,
#         linewidths=nx.get_node_attributes(G,'selected').values(),
         )
   plt.axis('off')
   plt.savefig('graph.svg')



   #JSON_write(yoursched, 'public_html/w1.json','public_html/w2.json')
   JSON_write(yoursched, 'public_html/w1.json','public_html/w2.json')




