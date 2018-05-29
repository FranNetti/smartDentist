from django.db import models
import datetime

# Create your models here.

class Device(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    lat = models.DecimalField(max_digits = 7, decimal_places = 5)
    long = models.DecimalField(max_digits = 8, decimal_places = 5)

    def __str__(self):
        return "Device: {} | lat: {} - long: {}".format(self.id,self.lat,self.long)

class Doctor(object):

    name = ""
    surname = ""
    
    def __init__(self, name, surname):
        super()
        self.name = name;
        self.surname = surname;

    def getCredentials(self):
        return self.name + " " + self.surname

class Coordinate(object):

    lat = 0.0
    long = 0.0

    def __init__(self, lat, long):
        super()
        self.lat = lat;
        self.long = long;

    def getCoordinates(self):
        return self.lat, self.long;

class ReceiveData(object):

    dict = {}
    id = 0
    pos = None
    doct = None
    other = {}
    
    def __init__(self, dict):
        super()
        self.dict = dict;

    def processData(self):
        self.id = self.dict["id"]
        self.pos = Coordinate(self.dict["lat"],self.dict["long"])
        doct_name = ""
        doct_surn = ""
        for a,b in self.dict.items():
            if a == "doct_name":
                doct_name = b
            elif a == "doct_surn":
                doct_surn = b
            elif (a != "lat" and a != "long"):
                self.other[a] = b
        if doct_name and doct_surn:
            self.doct = Doctor(doct_name, doct_surn)

    def printData(self):
        device = Device(id = self.id, lat = self.pos.lat, long = self.pos.long)
        device.save()
        print(Device.objects.all())
        #with open("app/coordinateGps.txt", "at") as myfile:
        #    str  = "id dispositivo: {}".format(self.id)
        #    str += "\nlat: {}".format(self.pos.lat)
        #    str += "\nlong: {}".format(self.pos.long)
        #    str += "\ndottore: {}".format(self.doct.getCredentials() if self.dottore else "")
        #    self.printMonitorAndFile(str, myfile)
        #    for a,b in self.other.items():
        #        str = "{}: {}".format(a,b)
        #        self.printMonitorAndFile(str, myfile)
        #    self.printMonitorAndFile("--------------------------------------------", myfile)

    def printMonitorAndFile(self, msg, myfile):
        print(msg, file=myfile)
        print(msg)
