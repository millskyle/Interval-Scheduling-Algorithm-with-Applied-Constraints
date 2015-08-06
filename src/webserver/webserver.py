import json
import bottle
from database import dbHandler
from scraper import spiderworker
from coursegraph import build_graph
from bottle import request
from coursegraph.userpreferences import UserPrefs

setup = False
dbHandler.init(setup)
scraperWorker = spiderworker.SpiderWorker()
if setup:
	scraperWorker.start()


def selectedCourses():
	semester = request.forms.get("semester")
	campus_pref = request.forms.get("campus_pref")
	morning_class_pref = request.forms.get("morning_class_pref")
	afternoon_class_pref = request.forms.get("afternoon_class_pref")
	evening_class_pref = request.forms.get("evening_class_pref")
	day_off = request.forms.get("day_off")
	monday_off = request.forms.get("monday_off")
	tuesday_off = request.forms.get("tuesday_off")
	wednesday_off = request.forms.get("wednesday_off")
	thursday_off = request.forms.get("thursday_off")
	friday_off = request.forms.get("friday_off")
	CRN1 = request.forms.get("CRN1")
	CRN2 = request.forms.get("CRN2")
	CRN3 = request.forms.get("CRN3")
	CRN4 = request.forms.get("CRN4")
	CRN5 = request.forms.get("CRN5")
	mingaps = request.forms.get("mingaps")

	UserPrefs.semester = semester

	if day_off == "yes":
		UserPrefs.MaximizeDaysOff = True
	elif day_off == "no":
		UserPrefs.MaximizeDaysOff = False
	
	if monday_off == "on":
		UserPrefs.PreferredDaysOff += [1,6]

	if tuesday_off == "on":
		UserPrefs.PreferredDaysOff += [2,7]

	if wednesday_off == "on":
		UserPrefs.PreferredDaysOff += [3,8]

	if thursday_off == "on":
		UserPrefs.PreferredDaysOff += [4,9]

	if friday_off == "on":
		UserPrefs.PreferredDaysOff += [5,10]

	if morning_class_pref == "on":
		UserPrefs.PreferTimeOfDay = "Morning"

	if afternoon_class_pref == "on":
		UserPrefs.PreferTimeOfDay = "Afternoon"

	if evening_class_pref == "on":
		UserPrefs.PreferTimeOfDay = "Evening"

	UserPrefs.optimumTimeOfDay = "1200"

	if campus_pref == "none":
		UserPrefs.preferredCampus = "None"
	elif campus_pref == "North Campus":
		UserPrefs.preferredCampus = "North"
	else:
		UserPrefs.preferredCampus = "Downtown"

	UserPrefs.preferredCRNs += [CRN1,CRN2,CRN3,CRN4,CRN5]

	if mingaps == "yes":
		UserPrefs.preferMinGaps = True
	elif mingaps == "no":
		UserPrefs.preferMinGaps = False  

@bottle.route('/')
def index():
    return bottle.static_file('input.html', root='static/')

@bottle.route('/stylesheet.css')
def style():
	return bottle.static_file('stylesheet.css', root='static/')

@bottle.route('/template.css')
def style():
	return bottle.static_file('template.css', root='static/')

@bottle.route('/input.js')
def input():
    return bottle.static_file('input.js', root='static/')

@bottle.route('/input_form', method="POST")
def getCalendar():
	#Now begin the process of querying the db
	semester = request.forms.get("semester")
	mandatory_selected_courses = request.forms.getall("mandatory_selected_courses")
	elective_selected_courses = request.forms.getall("elective_selected_courses")
	selectedCourses()

	inputdict = {
		'SEMESTER': semester,
		'MCOURSES' : mandatory_selected_courses,
		'ECOURSES' : elective_selected_courses
	}

	courses, ecourses = dbHandler.grabCourses(inputdict)
	calendars = build_graph.graph_optimize(courses+ecourses)
	templ = open('public_html/cal2.tmpl','r').read()
	
	return bottle.template(templ, calendars=calendars)

@bottle.route('/getAvailableCourses/<sem>')
def getAvailCourses(sem):
	print request.body.read()
	return json.dumps(dbHandler.getAvailableCourses(sem))

bottle.run(host='', port=8080)
if setup:
	scraperWorker.end()
	scraperWorker.join()