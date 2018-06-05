import time
from threading import Thread
from queue import Queue
from sender import HttpPostSender

class Controller(Thread):
    
    # blocking queue, perfect for a multi-threading application
    list = Queue()
    sender = HttpPostSender()
    # a dictionary where for a type of msg there will be some types of subscribers
    urlToSend = {}
    # max wait time allowed for putting a new element in the queue
    wait_time = 3
    # number of max retransmissions for a single subscriber
    retry_times = 4

    def __init__(self, max_queue_size, url):
        list = Queue(maxsize = max_queue_size)
        urlToSend = url;
        super.__init__()

    # add new data to the blocking queue
    # id   = publisher id
    # data = the data sent by the publisher
    def addNewPublisherData(self, id, data):
        elem = {}
        elem["id"] = id
        elem["type"] = data["type"]
        elem["lat"] = data["lat"]
        elem["long"] = data["long"]
        self.list.put(elem, timeout = self.wait_time)

    def subscribe(self, type, ip_addr):
        if not (type in self.urlToSend):
            self.urlToSend["type"] = []
        self.urlToSend["type"].append(ip_addr)

    def unsubscribe(self, type, ip_addr):
        self.urlToSend["type"].remove(ip_addr)

    def run(self):
        while True:
            # get the item from the queue, if empty wait until it isn't anymore
            data = self.list.get()
            # for each subscriber to that type of event subscribe that event
            for url in self.urlToSend[data["type"]]:
                result = sender.sendData(url = url, info = data)
                x = 0
                # if there is an error in the transmission, retry until it's ok
                while result != 200 && x < self.retry_times:
                    time.sleep(1)
                    result = sender.sendData(url = url, info = data)
                    x += 1

