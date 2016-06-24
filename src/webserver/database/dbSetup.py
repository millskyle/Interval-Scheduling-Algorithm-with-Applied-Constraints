import peewee
from playhouse.db_url import connect
import datetime
import os

db = connect(os.getenv("DATABASE_URL", "sqlite:///scheduling.db"))

#Base Models for tables to avoid annoying excess code
class BaseModel(peewee.Model):
    class Meta:
        database = db

#Base Tables used to store information
#These classes define both the tables and can be used to store row information
#More info on usage can be found in dbHandler
class Sectiondb(BaseModel):
    id = peewee.PrimaryKeyField() #pretty much just used for joins don't touch
    crn = peewee.CharField()
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
    starttime = peewee.CharField()
    endtime = peewee.CharField()

class watches(BaseModel):
   id = peewee.PrimaryKeyField()
   dateadded = peewee.DateTimeField(default=datetime.datetime.now)
   active = peewee.BooleanField(default=True)
   email = peewee.CharField()
   crn = peewee.CharField()
   semester = peewee.CharField()


class usage(BaseModel):
   id = peewee.PrimaryKeyField()
   semester = peewee.CharField()
   date = peewee.DateTimeField(default=datetime.datetime.now)
    
