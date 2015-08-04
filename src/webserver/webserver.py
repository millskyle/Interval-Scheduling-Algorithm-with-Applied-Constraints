import bottle

@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='static/')

@bottle.route('/getCalendar')
def getCalendar():
	#Now begin the process of querying the db
	return "Placeholder Response"

bottle.run(host='localhost', port=8080)