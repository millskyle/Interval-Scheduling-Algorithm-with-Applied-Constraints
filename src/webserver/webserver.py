import json
import bottle
from scraper import spiderworker
from database import dbHandler

dbHandler.init(True)
scraperWorker = spiderworker.SpiderWorker()
scraperWorker.run()


@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='static/')

@bottle.route('/getCalendar')
def getCalendar():
	#Now begin the process of querying the db
	return "Placeholder Response"

@bottle.route('/getAvailableCourses')
def getAvailCourses():
	return json.dumps(dbHandler.getAvailableCourses())

bottle.run(host='localhost', port=8080)