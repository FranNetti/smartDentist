from abc import ABCMeta, abstractclassmethod
import requests

class ISender:
    __metaclass__ = ABCMeta

    # info = a dict with all the informations that you want to send to the given url
    @abstractclassmethod
    def sendData(self, url, info): raise NotImplementedError


class HttpPostSender(ISender):
    
    def sendData(self, url, info):
         r = requests.post(url, data = info)
         return r.status_code


