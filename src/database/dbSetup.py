import peewee
import MySQLdb
import datetime

dbname = ''
dbuser = ''
dbpass = ''

db = peewee.MySQLDatabase(dbname, user=dbuser, passwd=dbpass)

#Base Models for tables to avoid annoying excess code
class BaseModel(peewee.Model):
	class Meta:
		database = db

#Base Tables used to store information
#These classes define both the tables and can be used to store row information
#More info on usage can be found in dbHandler
class Class(BaseModel):
	id = peewee.PrimaryKeyField() #pretty much just used for joins don't touch
	crn = peewee.IntegerField()
	code = peewee.CharField()
	type = peewee.CharField(max_length=3)
	remainingseats = peewee.IntegerField()
	semester = peewee.CharField()
	subject = peewee.CharField()

class Timeslot(BaseModel):
	id = peewee.PrimaryKeyField()
	cid = peewee.ForeignKeyField(Class, to_field="id")
	day = peewee.IntegerField()
	starttime = peewee.IntegerField()
	endtime = peewee.IntegerField()