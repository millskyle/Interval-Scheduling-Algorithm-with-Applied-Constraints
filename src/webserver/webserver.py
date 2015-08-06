import json
import bottle
from database import dbHandler
from scraper import spiderworker
from coursegraph import build_graph
from bottle import request
from coursegraph.userpreferences import UserPrefs

setup = True
dbHandler.init(setup)
scraperWorker = spiderworker.SpiderWorker()
if setup:
	scraperWorker.start()


@bottle.route('/')
def index():
    return bottle.static_file('input.html', root='static/')

@bottle.route('/stylesheet.css')
def style():
	return bottle.static_file('stylesheet.css', root='static/')

@bottle.route('/input.js')
def input():
    return bottle.static_file('input.js', root='static/')

@bottle.route('/input_form', method="POST")
def getCalendar():
	#Now begin the process of querying the db

	selectedCourses()

	inputdict = {
		'SEMESTER': semester,
		'COURSES' : mandatory_selected_courses+elective_selected_courses
	}

	courses = dbHandler.grabCourses(inputdict)
	w1, w2 = build_graph.graph_optimize(courses)
	templ = open('public_html/cal.tmpl','r').read()
	
	return bottle.template(templ, w1=w1, w2=w2)

@bottle.route('/getAvailableCourses')
def getAvailCourses():
	return json.dumps(dbHandler.getAvailableCourses())

bottle.run(host='', port=8080)
if setup:
	scraperWorker.end()
	scraperWorker.join()

def selectedCourses():
	semester = request.forms.get("semester")	
	campus_pref = request.forms.get("campus_pref")
	morning_class_pref = request.forms.get("morning_class_pref")
	afternoon_class_pref = request.forms.get("afternoon_class_pref")
	evening_class_pref = request.forms.get("evening_class_pref")
	yes_day_off = request.forms.get("yes_day_off")
	no_day_off = request.forms.get("no_day_off")
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
	yes_gaps = request.forms.get("yes_gaps")
	no_gaps = request.forms.get("no_gaps")

	UserPrefs.semester = semester
	
	if yes_day_off == "on":
		UserPrefs.MaximizeDaysOff = True
	elif no_day_off == "on":
		UserPrefs.MaximizeDaysOff = False
	
	if monday_off == "on":
		UserPrefs.PreferredDaysOff.append(1,6)

	if tuesday_off == "on":
		UserPrefs.PreferredDaysOff.append(2,7)

	if wednesday_off == "on":
		UserPrefs.PreferredDaysOff.append(3,8)

	if thursday_off == "on":
		UserPrefs.PreferredDaysOff.append(4,9)

	if friday_off == "on":
		UserPrefs.PreferredDaysOff.append(5,10)

	if morning_class_pref == "on":
		UserPrefs.PreferredDaysOff = "Morning"

	if afternoon_class_pref == "on":
		UserPrefs.PreferredDaysOff = "Afternoon"

	if evening_class_pref == "on":
		UserPrefs.PreferredDaysOff = "Evening"

	UserPrefs.optimumTimeOfDay = "1200"

	if campus_pref == "none":
		UserPrefs.preferredCampus = 0
	elif campus_pref == "North Campus":
		UserPrefs.preferredCampus = 1
	else:
		UserPrefs.preferredCampus = 2

	UserPrefs.preferredCRNs.append(CRN1,CRN2,CRN3,CRN4,CRN5)

	if yes_gaps == "on":
		UserPrefs.PreferGaps = True
	elif no_gaps == "on":
		UserPrefs.PreferGaps = False  