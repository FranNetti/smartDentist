import pika
import time
from pika.exceptions import ConnectionClosed
from abc import ABCMeta, abstractclassmethod

class CallbackHandler:
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def callback(self, ch, method, properties, body): raise NotImplementedError

class RabbitMqHandler:

    hostName = ""
    queue_name = "forno"
    retry_times = 10
    wait_time = 5

    # since rabbitMq could not be ready when initializing this class,
    # the class may attempt more than one time before establish a connection
    # so the first thing to do is to wait until the service is on.
    # after a certain time though, it raise an exception
    def __init__(self, hostName):
        self.hostName = hostName
        x = 0
        while x < self.retry_times:
            try:
                conn = pika.BlockingConnection(pika.ConnectionParameters(hostName))
                conn.close()
                break
            except ConnectionClosed as e:
                time.sleep(self.wait_time)
                x += 1
        if x >= self.retry_times:
            raise ConnectionClosed()

    def sendMsg(self, msg):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.hostName))
        channel = conn.channel()
        channel.queue_declare(self.queue_name)
        channel.basic_publish(exchange='',
                      routing_key=self.queue_name,
                      body=msg)
        conn.close()

    # callbackObj = an object that implements the interface CallbackHandler
    def getMsg(self, callbackObj):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.hostName))
        channel = conn.channel()
        channel.queue_declare(self.queue_name)
        channel.basic_consume(callbackObj.callback,
                      queue = self.queue_name)
        channel.start_consuming()


