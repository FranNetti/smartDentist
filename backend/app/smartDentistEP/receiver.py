from abc import ABCMeta, abstractclassmethod

class IReceiveData:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def processData(self, dict): raise NotImplementedError

    @abstractclassmethod
    def getAllInformations(self): raise NotImplementedError

class DoctorField(object):

    name = ""
    surname = ""
    
    def __init__(self, name, surname):
        super()
        self.name = name;
        self.surname = surname;

    def getCredentials(self):
        return self.name + " " + self.surname

class CoordinateField(object):

    lat = 0.0
    long = 0.0

    def __init__(self, lat, long):
        super()
        self.lat = lat;
        self.long = long;

    def getCoordinates(self):
        return self.lat, self.long;

# Class for analysing data about a device
class ReceiveDataDevice(IReceiveData):

    # device's id - REQUIRED
    id = 0
    # device's position coordinates - REQUIRED
    pos = None
    # device's user - OPTIONAL
    doct = None
    # other options - OPTIONAL
    other = {}
    
    # dict => informations about a device 
    def __init__(self, dict):
        self.processData(dict)

    def __init__(self):
        pass

    # dict => informations about a device 
    def processData(self, dict):
        self.id = dict["id"]
        self.pos = CoordinateField(dict["lat"],dict["long"])
        doct_name = ""
        doct_surn = ""
        # after the required fields that I'm sure are in the dictionary
        # I'm saving all the other infos that are contained
        for field, value in dict.items():
            if field == "doct_name":
                doct_name = value
            elif field == "doct_surn":
                doct_surn = value
            elif (field != "lat" and field != "long"):
                self.other[field] = value
        # I can create a doctor only if I have both his name and surname
        if doct_name and doct_surn:
            self.doct = DoctorField(doct_name, doct_surn)

    def printData(self):
        with open("app/smartDentistEP/doc/coordinateGps.txt", "at") as myfile:
            str  = "id dispositivo: {}".format(self.id)
            str += "\nlat: {}".format(self.pos.lat)
            str += "\nlong: {}".format(self.pos.long)
            str += "\ndottore: {}".format(self.doct.getCredentials() if self.doct else "")
            self.printMonitorAndFile(str, myfile)
            for field, value in self.other.items():
                self.printMonitorAndFile("{}: {}".format(field, value), myfile)
            self.printMonitorAndFile("--------------------------------------------", myfile)

    def printMonitorAndFile(self, msg, myfile):
        print(msg, file=myfile)
        print(msg)

    def getAllInformations(self):
        dict = {}
        dict["id"] = self.id
        dict["pos"] = self.pos
        dict["doct"] = self.doct
        dict["other"] = self.other
        return dict