import matplotlib.pyplot as plt
import networkx as nx
import json
from course import *


##NOTE:  At this point, it is assumed that the variable query_results is 
#        a list of all potential courses (as Section() objects), returned 
#        from some database query or web scraping action.

query_results = []


#Construct the graph object
G = nx.Graph()


#add all potential courses as nodes to the graph
for Sec in query_results:
   G.add_node(Sec, label=Sec.course[0:2])


edges = []
val_map = { 'Lec': 1.0, 'Tut':0.75, 'Lab':0.25, 'Oth':0.0 }
colors = [val_map[node.cType] for node in G.nodes() ]


for i,iSec in enumerate(allcourses):
   for j,jSec in enumerate(allcourses):
      if i<j:
         have_edge = False
         #If the two sections are from the same course and are the same type, they're incompatible
         if ( (iSec.cType == jSec.cType) and (jSec.course==iSec.course)):
            have_edge = True
         for itimeslot in iSec.timeslots:
            for jtimeslot in jSec.timeslots:
               if ( (jtimeslot.sTime <= itimeslot.eTime and jtimeslot.eTime >= itimeslot.eTime and jtimeslot.day==itimeslot.day) ):
                  have_edge = True

         if have_edge:
            G.add_edge(iSec,jSec)
            edges.append([i,j])

print "Your schedule: "
requiredNumberOfSections = 10
x = 0
tries = 0
while x < requiredNumberOfSections:
   yoursched = nx.maximal_independent_set(G)
   x =  len(yoursched)
   tries +=1
   print "Attempt ",tries
   if tries > 1000:
      print "Unsuccessful at making a schedule which includes all courses.  The best one possible has been created, but please check for missing courses/sections"
      break


w1jsonData = []
w2jsonData = []
for CC in yoursched:
   print "  "
   w1js,w2js = CC.toDict()
   for w1jsd in w1js:
      w1jsonData.append(w1jsd)
   for w2jsd in w2js:
      w2jsonData.append(w2jsd)

   print CC.course, CC.cType, CC.CRN
   for ts in CC.timeslots:
      print "   ",ts.day, ts.sTime, ts.eTime

nx.draw_networkx(G,with_labels=True,labels=nx.get_node_attributes(G,'unique'), cmap=plt.get_cmap('jet'), node_color=colors,vmin=0, vmax=1.0)
plt.savefig('graph.svg')




with open('w1.json','w') as outfile:
  json.dump(w1jsonData, outfile, sort_keys = True, indent = 4, ensure_ascii = True)

with open('w2.json','w') as outfile:
  json.dump(w2jsonData, outfile, sort_keys = True, indent = 4, ensure_ascii = True)


print "done"




