import peewee
import MySQLdb
import datetime

dbname = 'MyCampusSections'
dbuser = 'hackweek'
dbpass = 'hackweekteam'

db = peewee.MySQLDatabase(dbname, user=dbuser, passwd=dbpass)

#Base Models for tables to avoid annoying excess code
class BaseModel(peewee.Model):
	class Meta:
		database = db

#Base Tables used to store information
#These classes define both the tables and can be used to store row information
#More info on usage can be found in dbHandler
class Sectiondb(BaseModel):
	id = peewee.PrimaryKeyField() #pretty much just used for joins don't touch
	crn = peewee.IntegerField()
	name = peewee.TextField()
	campus = peewee.TextField()
	code = peewee.CharField()
	type = peewee.CharField(max_length=3)
	remainingseats = peewee.IntegerField()
	semester = peewee.CharField()
	subject = peewee.CharField()

class Timeslotdb(BaseModel):
	id = peewee.PrimaryKeyField()
	sid = peewee.ForeignKeyField(Sectiondb, to_field="id")
	day = peewee.IntegerField()
	starttime = peewee.IntegerField()
	endtime = peewee.IntegerField()
