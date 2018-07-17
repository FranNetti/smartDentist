from abc import ABCMeta, abstractclassmethod
from rabbitMqHandler import RabbitMqHandler
from logger import FileLogger
from pika.exceptions import ConnectionClosed
import time

class ISender:
    __metaclass__ = ABCMeta

    # info = a dict with all the informations that you want to send to the given url
    @abstractclassmethod
    def sendData(self, info): raise NotImplementedError


class MsgSender(ISender):

    rabbitSender = None
    logger = None

    def __init__(self):
        self.rabbitSender = self.createConnection()
        self.logger = FileLogger("fornoLogger.txt")
    
    def sendData(self, info):
        msg = ""
        for key, value in info.items():
            msg += "{}|{}\n".format(key,value)
        while True:
            try:
                self.rabbitSender.sendMsg(msg, "position")
                break
                # if the connection interrupts, log what happend,
                # recreate the connection and send the message again
            except ConnectionClosed as e:
                 del self.rabbitSender
                 self.logger.log("Connection interrupted with RabbitMq")
                 self.rabbitSender = self.createConnection()

    def createConnection(self):
        return RabbitMqHandler("msg_broker")
            
            
            
            


