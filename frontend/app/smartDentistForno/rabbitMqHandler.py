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
    exchange_name = "smartForno"
    wait_time = 5

    # since rabbitMq could not be ready when initializing this class,
    # the class may attempt more than one time before establish a connection
    # so the first thing to do is to wait until the service is on.
    # after a certain time though, it raise an exception
    def __init__(self, hostName):
        self.hostName = hostName
        while True:
            try:
                conn = pika.BlockingConnection(pika.ConnectionParameters(hostName))
                conn.close()
                break
            except ConnectionClosed as e:
                time.sleep(self.wait_time)
    
    # routingKey => the routing key of the desired message queue
    def sendMsg(self, msg, routingKey):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.hostName))
        channel = conn.channel()
        #declare an exchange point where all routes will be routed by a match with the routing key
        channel.exchange_declare(exchange=self.exchange_name,exchange_type='topic')
        channel.basic_publish(exchange=self.exchange_name,
                              routing_key=routingKey,
                              body=msg)
        conn.close()

    # callbackObj => an object that implements the interface CallbackHandler
    # routingKey => the routing key of the desired message queue
    def getMsg(self, callbackObj, routingKey):

                #result = channel.queue_declare(exclusive=True)
        #queue_name = result.method.queue


        conn = pika.BlockingConnection(pika.ConnectionParameters(self.hostName))
        channel = conn.channel()
        #declare an exchange point where all routes will be routed by a match with the routing key
        channel.exchange_declare(exchange=self.exchange_name,exchange_type='topic')
        #create an anonymous queue that will be deleted once the connection is closed
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        #bind the queue created with the routing key
        channel.queue_bind(exchange=self.exchange_name,
                           queue=queue_name,
                           routing_key=routingKey)
        channel.basic_consume(callbackObj.callback,
                              queue = queue_name)
        channel.start_consuming()


