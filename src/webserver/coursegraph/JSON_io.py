import json
from scraper.course import *


def JSON_write(Schedule, w1_out, w2_out):
   w1jsonData = []
   w2jsonData = []
   for CC in Schedule:
      w1js,w2js = CC.toDict()
      for w1jsd in w1js:
         w1jsonData.append(w1jsd)
      for w2jsd in w2js:
         w2jsonData.append(w2jsd)

   with open(w1_out,'w') as outfile:
     json.dump(w1jsonData, outfile, sort_keys = True, indent = 4, ensure_ascii = True)

   with open(w2_out,'w') as outfile:
     json.dump(w2jsonData, outfile, sort_keys = True, indent = 4, ensure_ascii = True)



