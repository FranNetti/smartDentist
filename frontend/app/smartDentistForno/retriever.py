import datetime

from abc import ABCMeta, abstractclassmethod
from random import uniform

class IRetriever:
    __metaclass__ = ABCMeta

    # info = a dict with all the informations that you want to send to the given url
    @abstractclassmethod
    def getData(self, id): raise NotImplementedError


class RandomRtv(IRetriever):

    
    def getData(self, id):      
        lat = uniform(-90,90)
        long = uniform(-180,180)
        doct_name = "Daniel"
        doct_surname = "Ricciardo"
        data = datetime.datetime.utcnow()
        return {
            'id' : id,
            'lat': lat,
            'long' : long,
            'doct_name' : doct_name,
            'doct_surn' : doct_surname,
            'data' : data,
        }


