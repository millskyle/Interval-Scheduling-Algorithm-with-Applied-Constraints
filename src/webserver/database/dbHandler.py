from dbSetup import *

#initializes the database
#Use reinit for debugging purposes
#True or 1 to clear all data in database
def init(reinit=False):
	if reinit:
		__deleteTables()
	__createTables()

def __deleteTables():
	Sectiondb.drop_table(True)
	Timeslotdb.drop_table(True)

def __createTables():
	Sectiondb.create_table(True)
	Timeslotdb.create_table(True)

@db.atomic() #ensures changes are rolledback once an error occurs
def insertCourse(section):
	sec = Sectiondb()
	sec.crn = section.CRN
	sec.name = section.name
	sec.subject = section.subject
	sec.semester = section.semester
	sec.code = section.course
	sec.campus = section.campus
	sec.type = section.cType
	sec.remainingseats = section.remainingSeats
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
	for section in sectionlist:
		insertCourse(section)
		

#I'm assuming I'm just going to get a list of strings for this part
def grabCourses(courselist):
	coursesdict = {}
	for course in courselist:
		cdict = {
			'LAB' : {},
			'LEC' : {},
			'TUT' : {}
		}


		query = Sectiondb.select().\
					where(Sectiondb.code == course).\
					join(Timeslotdb)

		if query.exists():
			for row in query:
				t = {
						'day' 		: row.day,
						'stime'		: row.starttime,
						'etime'		: row.endtime
					}
				if row.crn in cdict[row.type]:
					cdict[row.type][row.crn]['timeslots'].append(t)
				else:
					r = {
						'rseats' 	: row.remainingseats,
						'sem'	 	: row.semester,
						'subject'	: row.subject,
						'timeslots'	: [t]
					}

					cdict[row.type][row.crn] = r
		coursesdict[course] = cdict
	return coursesdict


def getAvailableCourses():
	retdict = {}

	subjectquery = Sectiondb.select(Sectiondb.subject).distinct()
	if subjectquery.exists():
		for subrow in subjectquery:
			retdict[subrow.subject] = []

			coursequery = Sectiondb.select().\
							where(Sectiondb.subject == subrow.subject)
			if coursequery.exists():
				for row in coursequery:
					retdict[subrow.subject].append(row.code)
	return retdict


