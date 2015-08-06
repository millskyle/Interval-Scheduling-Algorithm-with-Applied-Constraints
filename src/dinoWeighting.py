from course import *
from userpreferences import UserPrefs


def course_density(Schedule):
    weight = 0.
    counter = 0.
    for iCRN in Schedule:
        if UserPrefs.preferMinGaps == True:
            if not(iCRN.CRN=="55555"):
                for jCRN in Schedule:
                    for i in iCRN.timeslots:
                        for j in jCRN.timeslots:
                        #mints=min(i.sTime)
                        #maxts=max(j.eTime)
                            if i.day==j.day:
                                time = int(j.eTime) - int(i.sTime)
                                if time<=40:
                                    weight += 1
                                    counter+=1

                            #if time<=40:
                            #    weight+=1.
                            #    counter+=1.
#                            else:
#                                weight -=1.
#                                counter-=1.
    return weight/counter


def preferred_crn(Schedule):
    for CRN in Schedule:
        if CRN.CRN in UserPrefs.preferredCRNs:
            CRN.weight=1.e6







