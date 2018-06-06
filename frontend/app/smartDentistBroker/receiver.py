from abc import ABCMeta, abstractclassmethod
from threading import Thread
from rabbitMqHandler import RabbitMqHandler, CallbackHandler

class IReceiver:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def getData(self): raise NotImplementedError

class MsgReceiver(IReceiver, CallbackHandler, Thread):

    action = None
    rabbitRcv = None
    
    def __init__(self, readData):
        self.action = readData
        self.rabbitRcv = RabbitMqHandler("msg_broker")

    def run(self):
        while True:
            self.getData()

    def callback(self, ch, method, properties, body):
        elem = {}
        for row in body.splitlines():
            key, value = row.decode().split("|")
            elem[key] = value
        self.action(elem)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def getData(self):
        self.rabbitRcv.getMsg(self)


