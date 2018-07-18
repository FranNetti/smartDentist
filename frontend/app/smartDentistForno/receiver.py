from abc import ABCMeta, abstractclassmethod
from threading import Thread
from rabbitMqHandler import RabbitMqHandler, CallbackHandler
from pika.exceptions import ConnectionClosed
from logger import FileLogger

class IReceiver:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def getData(self): raise NotImplementedError

class MsgReceiver(IReceiver, CallbackHandler, Thread):

    action = None
    rabbitRcv = None
    logger = None
    routingKey = ""

    def __init__(self, readData, id):
        self.action = readData
        self.rabbitRcv = self.createConnection()
        self.logger = FileLogger("app/smartDentistForno/doc/log.txt")
        self.routingKey = "forno.{}".format(id)
        Thread.__init__(self)

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
        try:
            self.rabbitRcv.getMsg(self, self.routingKey)
            # if the connection interrupts, log what happend
            # and recreate the connection
        except ConnectionClosed as e:
                del self.rabbitRcv
                self.logger.log("Connection interrupted with RabbitMq")
                self.rabbitRcv = self.createConnection()

    def createConnection(self):
        return RabbitMqHandler("msg_broker")
