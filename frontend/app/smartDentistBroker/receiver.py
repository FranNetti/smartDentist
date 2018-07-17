import time
import requests

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
    routingKey = "position"
    
    def __init__(self, readData):
        self.action = readData
        self.rabbitRcv = self.createConnection()
        self.logger = FileLogger("brokerLog.txt")
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

class PollingUpdater(Thread):

    url = ""
    waitTime = 30
    rabbitSender = None
    logger = None

    def __init__(self, url):
        self.url = url
        self.rabbitSender = self.createConnection()
        self.logger = FileLogger("fornoLogger.txt")
        Thread.__init__(self)

    def run(self):
        while True:
            self.getAndUpdate()
            time.sleep(self.waitTime)

    def createConnection(self):
        return RabbitMqHandler("msg_broker")

    def getAndUpdate(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            response = r.json()
            print(response)
            for deviceData in response["devices"]:
                while True:
                    try:
                        id = deviceData["id"]
                        self.rabbitSender.sendMsg(deviceData, "change.{}".format(id))
                        break
                        # if the connection interrupts, log what happend,
                        # recreate the connection and send the message again
                    except ConnectionClosed as e:
                         del self.rabbitSender
                         self.logger.log("Connection interrupted with RabbitMq")
                         self.rabbitSender = self.createConnection()

