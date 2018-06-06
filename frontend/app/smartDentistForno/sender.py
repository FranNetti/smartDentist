from abc import ABCMeta, abstractclassmethod
from rabbitMqHandler import RabbitMqHandler
import time

class ISender:
    __metaclass__ = ABCMeta

    # info = a dict with all the informations that you want to send to the given url
    @abstractclassmethod
    def sendData(self, info): raise NotImplementedError


class MsgSender(ISender):

    rabbitSender = None

    def __init__(self):
        self.rabbitSender = RabbitMqHandler("msg_broker")
    
    def sendData(self, info):
        msg = ""
        for key, value in info.items():
            msg += "{}|{}\n".format(key,value)
        self.rabbitSender.sendMsg(msg)


