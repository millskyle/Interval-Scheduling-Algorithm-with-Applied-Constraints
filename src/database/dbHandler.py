from dbSetup import *

#initializes the database
#Use reinit for debugging purposes
#True or 1 to clear all data in database
def init(reinit):
	if reinit:
		__deleteTables()
	__createTables()

def __deleteTables():
	Class.drop_table(True)
	Timeslot.drop_table(True)

def __createTables():
	Class.create_tables(True)
	Timeslot.create_tables(True)



#I don't know what the data structure is that holds courses
def insertCourse(coursedict):
	pass

#I'm assuming I'm just going to get a list of strings for this part
def grabCourses(courselist):
	coursesdict = {}
	for course in courselist:
		cdict = {
			'LAB' : {},
			'LEC' : {},
			'TUT' : {}
		}


		query = Class.select().\
					where(Class.code == course).\
					join(Timeslot)

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

