import logging
import logstash

from abc import ABCMeta, abstractclassmethod
from .models import *

class IDbController:
    __metaclass__ = ABCMeta

    # model = the db element that you want to save
    # dict = a dictionary with all the informations to save
    @abstractclassmethod
    def saveData(self, model, dict): raise NotImplementedError


# Class for a controller that manages a relational db
class DbrController(IDbController):
    
    def saveData(self, model, info):
        if model == Device.__class__ :
            id = info["id"]
            pos = info["pos"]
            device = Device(device_id = id, lat = pos.lat, long = pos.long)
            device.save()

# Class for a controller that loads data into the logstash
class LogStashController():

    logger = None

    def __init__(self, hostName, port):
        logger = logging.getLogger('python-logstash-logger')
        logger.setLevel(logging.INFO)
        logger.addHandler(logstash.TCPLogstashHandler(hostName, port, "smartDentistInfo", version=1))
        self.logger = logger

    def saveData(self, info):
        extra = {
            'device_id': info["id"],
            'device_position' : "{},{}".format(info["pos"].lat,info["pos"].long)
        }
        self.logger.info('Nuova posizione segnalata', extra=extra)



