import json
import bottle
from database import dbHandler
from scraper import spiderworker
from coursegraph import build_graph

setup = False
dbHandler.init(setup)
scraperWorker = spiderworker.SpiderWorker()
if setup:
	scraperWorker.start()


@bottle.route('/')
def index():
    return bottle.static_file('input.html', root='static/')

@bottle.route('/input.js')
def input():
    return bottle.static_file('input.js', root='static/')

@bottle.route('/input_form')
def getCalendar():
	#Now begin the process of querying the db
	courses = dbHandler.grabCourses(['CSCI1030U','MATH1010U',''])

	build_graph.graph_optimize(courses)
	w1 = open('public_html/w1.json','r').read()
	w2 = open('public_html/w2.json','r').read()
	templ = open('public_html/cal.tmpl','r').read()
	
	return bottle.template(templ, w1=w1, w2=w2)

@bottle.route('/getAvailableCourses')
def getAvailCourses():
	return json.dumps(dbHandler.getAvailableCourses())

bottle.run(host='localhost', port=8080)
if setup:
	scraperWorker.end()
	scraperWorker.join()
