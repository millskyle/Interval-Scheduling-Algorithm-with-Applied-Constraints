import json
import bottle
from scraper import spiderworker
from database import dbHandler

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

@bottle.route('/calendar')
def getCalendar():
	#Now begin the process of querying the db
	courses = dbHandler.grabCourses(['CSCI1010U'])
	print courses
	return "Placeholder Response"

@bottle.route('/getAvailableCourses')
def getAvailCourses():
	return json.dumps(dbHandler.getAvailableCourses())

bottle.run(host='localhost', port=8080)
if setup:
	scraperWorker.end()
	scraperWorker.join()