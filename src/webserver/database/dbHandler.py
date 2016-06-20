import os
import re
from scraper.course import Section
from dbSetup import *
import urllib2
from urllib import urlencode
from datetime import datetime, timedelta

#initializes the database
#Use reinit for debugging purposes
#True or 1 to clear all data in database
def init(reinit=False):
    if reinit or os.getenv("DEBUG", False):
        __deleteTables()
    __createTables()

def __deleteTables():
    Timeslotdb.drop_table(True)
    Sectiondb.drop_table(True)

def __createTables():
    Sectiondb.create_table(True)
    Timeslotdb.create_table(True)
    watches.create_table(True)
    usage.create_table(True)

def email_valid(email):
    return re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", email)

def add_watch(semester, crn, email):
    if email_valid(email):
        watches.insert(email=email,active=1,crn=crn,semester=semester).execute()
    else:
        print("\n\n INVALID EMAIL CAPTURED \n\n")

def check_watches():
    #remove expired watches first
    expired = watches.select().where(watches.active == True, \
        watches.dateadded <  (datetime.now() - timedelta(days=30))  )
   
    for i,result in enumerate(expired):
        stringg="""
The watch you set on CRN {crn} has expired. Re-submit the watch at scheduler.uoitphysics.ca/add_watch  if you still wish to watch this section. """.format(crn=result.crn)
        print "\n",stringg
        post = { "b":stringg, "s": "CRN watch EXPIRED!", "e":result.email}
        url = "http://uoitphysics.ca/email/dispatch/send_simple_email.php"
        urllib2.urlopen(url, urlencode(post))
        deactivate = watches.update(active = False).where(watches.crn == result.crn, watches.semester==result.semester)
        deactivate.execute()

   #check for 
    results = watches.select().where(watches.active == True)
    print "Checking for available seats..."
    for i,result in enumerate(results):
        print result.semester,result.crn,result.email
        seatQuery = Sectiondb.select().where(Sectiondb.crn == result.crn, Sectiondb.semester == result.semester, Sectiondb.remainingseats > 0)
        for query in seatQuery:
            stringg="""
The section for which you've requested a watch,

{code} - {name}
CRN:{crn}

has {seats} seats available. """.format(code=query.code, name = query.name, seats=query.remainingseats, crn=query.crn)
            print stringg
            post = { "b":stringg, "s": "CRN available","e":result.email}
            url = "http://uoitphysics.ca/email/dispatch/send_simple_email.php"
            print "URL: ",url
            urllib2.urlopen(url, urlencode(post))
            deactivate = watches.update(active = False).where(watches.crn == query.crn, watches.semester==query.semester)
            deactivate.execute()
            print "deactivated",deactivate,"watches"

def updateCourse(sec):
    query = Sectiondb.select().\
            where(Sectiondb.crn == sec.CRN,
                  Sectiondb.semester == sec.semester)
    row = Sectiondb()

    #checks to see if we're inserting or updating
    insert = True
    if query.exists():
        row = query.get()
        insert = False

    row.crn = sec.CRN
    row.name = sec.name
    row.semester = sec.semester
    row.code = sec.course
    row.campus = sec.campus
    row.type = sec.cType
    row.remainingseats = sec.remainingSeats

    if sec.remainingSeats < 0:
        row.remainingseats = 0

    #Grabs subject from course code
    #Course code is seperated into 3 groups like so
    #(CSCI)(1010)(U)
    mo = re.match("([A-Za-z]{3,4})([0-9]{4})([A-Z])", sec.course)
    if mo: 
        row.subject = mo.groups()[0]

    row.save()

    #if updating insert the timeslots
    if insert:
        for timeslot in sec.timeslots:
            t = Timeslotdb()
            t.sid = row.id
            t.day = timeslot.day
            t.starttime = timeslot.sTime
            t.endtime = timeslot.eTime
            t.save()


#if someone uses the scheduler, add an entry to the usage table
def addUsage(semester):
    row = usage()
    row.semester = semester
    row.save()





#I'm assuming I'm just going to get a list of strings for this part
def grabCourses(courses):
    
    courselist = courses["MCOURSES"]
    ecourselist = courses["ECOURSES"]
    #sem = getSemesterCode(courses["SEMESTER"])
    sem = courses["SEMESTER"]
    print("*** {}".format(sem))
    sectionlist = []
    for course in courselist:
        createSectionsfromCourse(course, sem, sectionlist)

    esectionlist = []
    for course in ecourselist:
        createSectionsfromCourse(course, sem, sectionlist)


    return sectionlist, esectionlist

def createSectionsfromCourse(course, sem, sectionlist):
    query = Sectiondb.select().\
                    where(Sectiondb.code == course, Sectiondb.semester == sem)

    if query.exists():
        for row in query:
            #setup the section
            sec = Section()
            sec.CRN = row.crn
            sec.name = row.name
            sec.cType = row.type
            sec.course = row.code
            sec.campus = row.campus
            sec.subject = row.subject
            sec.remainingSeats = row.remainingseats

            #get the timeslots
            timequery = Timeslotdb.select().\
                        where(Timeslotdb.sid == row.id)
            for timerow in timequery:
                sec.add_timeslot(timerow.starttime,
                                 timerow.endtime,
                                 timerow.day)
            sectionlist.append(sec)


def getAvailableCourses(semester):
    retdict = {}
    #sem = getSemesterCode(semester)
    sem = semester
    coursesdict = {}
    semstring=semester

    #constructs the query for each subject
    subjectquery = Sectiondb.\
                    select(Sectiondb.subject).\
                    where(Sectiondb.semester == sem).\
                    distinct().naive()

    if subjectquery.exists():
        for subrow in subjectquery:
            coursesdict[subrow.subject] = []

            coursequery = Sectiondb.select().\
                            where(Sectiondb.subject == subrow.subject,
                                  Sectiondb.semester == sem).\
                            group_by(Sectiondb.code).\
                            distinct().naive()
            if coursequery.exists():
                for row in coursequery:
                    coursesdict[subrow.subject].append(row.code)

            retdict[semstring] = coursesdict
    else:
        print sem

    print(retdict)
    return retdict

def getSemesterCode(semester):
    opts = semester.split(" ")
    term = " ".join(opts[:-1])
    if term == 'Fall':
        sem = str(opts[-1]) + '09'
    elif term == 'Winter':
        sem = str(opts[-1]) + '01'
    elif term == 'Spring Summer':
        sem = str(opts[-1]) + '05'
    else:
        print("Received semester '{}'".format(semester))
        return

    return sem
