from dict_construct import dict_construct
from course import Course
import random

def find_required_events(course_dict, course_code_list):
    """Finds the required events (e.g. labs) for courses in the 
    course code list
    Returns list with all required events

    Keyword arguments:
    course_dict: the dictionary containing relevant courses
    course_code_list: list containing all the desired course codes
    """
    #Initialize an empty event list
    event_list = []

    for code in course_code_list:
        for ctype in course_dict[code].keys():
            #Add a tuple with the course code and type to the event list
            event_list.append([code, ctype])

    return event_list

def check_conflict(day, stime, schedule):
    """Checks that the course does not conflict with any
    existing courses in the schedule
    """
    for event in schedule[day]:
        #Check if there is an overlap between the two classes
        if event.stime <= stime < event.etime:
            return True
        else:
            return False

def build_schedule(course_dict, course_code_list,conflict_thresh=100):
    """Builds a schedule with the courses in the list
    Returns dictionary containing the schedule

    Keyword arguments:
    course_dict: the dictionary containing relevant courses
    course_code_list: list containing all the desired course codes
    conflict_thresh: number of times the program will try and find a new course
    to fix conflicts
    """
    
    #Initialize the schedule
    #Will be schedule['DAY'] = list of events
    schedule = dict_construct(1,list)

    #Get relevant courses and their lectures, labs and tutorials
    #List returned is [[code, ctype]]
    ev_list = find_required_events(course_dict, course_code_list)

    for event in ev_list:
        code = event[0]
        ctype = event[1]
    
        #Boolean that says if the time can be added
        able_to_add = False
        #Counter for the number of attempts at conflict resolution
        add_attempts = 0 

        while able_to_add == False:
            #Initialize a queue to store events temporarily 
            ev_queue = []

            #Get a random CRN for the course and ctype
            crn = str(random.sample(course_dict[code][ctype],1)[0])
        
            for time_data in course_dict[code][ctype][crn]['TIMES']:
                #Get the time data for the course
                stime = time_data[0]
                etime = time_data[1]
                day = time_data[2]

                #Check for conflicts 
                if check_conflict(day, stime, schedule) == True:
                    break
                #If no conflicts create an instance of the courses class
                #and append it to the queue
                else:
                    rseat = course_dict[code][ctype][crn]['CINFO'][0]
                    sem = course_dict[code][ctype][crn]['CINFO'][1]
                    subj = course_dict[code][ctype][crn]['CINFO'][2]
                    campus = course_dict[code][ctype][crn]['CINFO'][3]
                    #Add to the queue
                    #Tuple of day and class instance
                    ev_queue.append((day, Course(crn, ctype, code, rseat, stime, 
                                                 etime, day, sem, subj, campus)))
    
            #Check that there were no conflicts
            if len(ev_queue) == len(course_dict[code][ctype][crn]['TIMES']):
                #Add the courses to the schedule
                for i in ev_queue:
                    schedule[i[0]].append(i[1])
                
                able_to_add = True

            #If the counter is larger than the threshold then break
            if add_attempts > conflict_thresh:
                print "Could not add %s %s section" % (code, ctype)
                break
            #Increment the counter 
            add_attempts += 1

    return schedule

def print_schedule(schedule):
    """Prints the contents of the schedule

    Keyword arguments:
    schedule: dictionary containing the scheduled events
    """

    print "CRN CTYPE CODE RSEAT STIME ETIME DAY SEM SUBJ CAMPUS"

    for day in schedule.keys():
        for event in schedule[day]:
            print event.crn, event.ctype, event.code, event.rseat, \
                  event.stime, event.etime, event.day, event.sem, \
                  event.subj, event.campus




