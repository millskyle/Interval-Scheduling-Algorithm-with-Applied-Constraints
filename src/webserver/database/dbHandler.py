import re
from scraper.course import Section
from dbSetup import *

#initializes the database
#Use reinit for debugging purposes
#True or 1 to clear all data in database
def init(reinit=False):
	if reinit:
		__deleteTables()
	__createTables()

def __deleteTables():
	Timeslotdb.drop_table(True)
	Sectiondb.drop_table(True)

def __createTables():
	Sectiondb.create_table(True)
	Timeslotdb.create_table(True)

@db.atomic()
def updateCourse(sec):
	query = Sectiondb.select().\
			where(Sectiondb.crn == sec.CRN)

	row = Sectiondb()
	if query.exists():
		row = query.get()

		row.crn = sec.CRN
		row.name = sec.name
		row.semester = sec.semester
		row.code = sec.course
		row.campus = sec.campus
		row.type = sec.cType
		row.remainingseats = sec.remainingSeats
		row.save()

	else:
		row.crn = sec.CRN
		row.name = sec.name
		row.semester = sec.semester
		row.code = sec.course
		row.campus = sec.campus
		row.type = sec.cType
		row.remainingseats = sec.remainingSeats
		row.save()

		for timeslot in sec.timeslots:
			t = Timeslotdb()
			t.sid = row.id
			t.day = timeslot.day
			t.starttime = timeslot.sTime
			t.endtime = timeslot.eTime
			t.save()



def insertCourse(section):
	sec = Sectiondb()
	sec.crn = section.CRN
	sec.name = section.name
	sec.semester = section.semester
	sec.code = section.course
	sec.campus = section.campus
	sec.type = section.cType
	sec.remainingseats = section.remainingSeats


	mo = re.match("([A-Za-z]{3,4})([0-9]{4})([UTG])", section.course)
	if mo: 
		sec.subject = mo.groups()[0]

	sec.save()

	for timeslot in section.timeslots:
		t = Timeslotdb()
		t.sid = sec.id
		t.day = timeslot.day
		t.starttime = timeslot.sTime
		t.endtime = timeslot.eTime
		t.save()


#I don't know what the data structure is that holds courses
def insertCourses(sectionlist):
	with db.atomic():
		for section in sectionlist:
			insertCourse(section)
		

#I'm assuming I'm just going to get a list of strings for this part
def grabCourses(courses):
	sectionlist = []
	courselist = courses["COURSES"]
	tsem = courses["SEMESTER"]
	sem = ""
	opts = tsem.split(" ")
	if opts[0] == 'Fall':
		sem = str(opts[1]) + '09'
	elif opts[0] == 'Winter':
		sem = str(opts[1]) + '01'
	elif opts[0] == 'Spring/Summer':
		sem = str(opts[1]) + '05'
	else:
		print "if this happens someone goofed"
		print "in dbHandler grabCourses"
		return

	for course in courselist:
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
	return sectionlist

def getAvailableCourses():
	retdict = {}

	semesterquery = Sectiondb.\
					select(Sectiondb.semester).\
					group_by(Sectiondb.semester)
	if semesterquery.exists():
		for semesterrow in semesterquery:
			coursesdict = {}
			semstring=""
			mo = re.match("([0-9]{4})([0-9]{2})", semesterrow.semester)
			if mo: 
				if mo.groups()[1] == '09':
					semstring = "Fall "
				if mo.groups()[1] == '01':
					semstring = "Winter "
				if mo.groups()[1] == '05':
					semstring = "Spring/Summer "
				semstring += mo.groups()[0]

			subjectquery = Sectiondb.\
							select(Sectiondb.subject).\
							where(Sectiondb.semester == semesterrow.semester).\
							distinct().naive()

			if subjectquery.exists():
				for subrow in subjectquery:
					coursesdict[subrow.subject] = []

					coursequery = Sectiondb.select().\
									where(Sectiondb.subject == subrow.subject, Sectiondb.semester == semesterrow.semester).\
									group_by(Sectiondb.code).\
									distinct().naive()
					if coursequery.exists():
						for row in coursequery:
							coursesdict[subrow.subject].append(row.code)

			retdict[semstring] = coursesdict
	return retdict
