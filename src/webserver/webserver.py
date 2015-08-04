import json
import bottle
from scraper import spiderworker
from database import dbHandler

dbHandler.init()
scraperWorker = spiderworker.SpiderWorker()
# scraperWorker.run()


@bottle.route('/')
def index():
    return bottle.static_file('input.html', root='static/')

@bottle.route('/input.js')
def input():
    return bottle.static_file('input.js', root='static/')

@bottle.route('/getCalendar')
def getCalendar():
	#Now begin the process of querying the db
	return "Placeholder Response"

@bottle.route('/getAvailableCourses')
def getAvailCourses():
	return json.dumps(dbHandler.getAvailableCourses())

bottle.run(host='localhost', port=8080)
