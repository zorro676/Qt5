from peewee import *
import datetime

db = MySQLDatabase('my_app', user='root', password='Pa$$w0rd',
                        host='localhost', port=3306)

TypeOfFlight = (
        (1, 'With Trainer'),
        (2, 'Solo'),
        (3, 'non')
    )

class Person(Model):
    name = CharField()
    email = CharField(null=True, unique=True)
    phone = CharField(null=True, unique=True)
    TrainingStartDate = DateTimeField(default=datetime.datetime.now())
    Address = CharField()
    birthday = DateField()

    class Meta:
        database = db

class Flight(Model):
    FlightType = CharField(choices=TypeOfFlight)
    DateOfFlight = DateTimeField(default=datetime.datetime.now())
    FlightStartTime = DateTimeField(default=datetime.datetime.now())
    FlightFinishTime = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db


class Payment( Model ):
    FlightType = CharField()
    TransferDateTime = DateTimeField( default=datetime.datetime.now() )
    TransferAmount = IntegerField()


    class Meta:
        database = db


db.connect()
db.create_tables([Person, Flight, Payment])