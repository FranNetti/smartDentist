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

    def saveData(self, info):

        host = 'logstash'

        test_logger = logging.getLogger('python-logstash-logger')
        test_logger.setLevel(logging.INFO)
        #test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
        test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

        # add extra field to logstash message
        extra = {
            'device_id': info["id"],
            'latitudine': info["pos"].lat,
            'longitudine': info["pos"].long
        }
        test_logger.info('Nuova posizione', extra=extra)
