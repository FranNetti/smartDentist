from abc import ABCMeta, abstractclassmethod
from .models import *

class IDbController:
    __metaclass__ = ABCMeta

    # model = the db element that you want to save
    # dict = a dictionary with all the informations to save
    @abstractclassmethod
    def saveData(self, model, dict): raise NotImplementedError


# Class for a controller that manage a relational db
class DbrController(IDbController):
    
    def saveData(self, model, info):
        if model == Device.__class__ :
            id = info["id"]
            pos = info["pos"]
            device = Device(device_id = id, lat = pos.lat, long = pos.long)
            device.save()

