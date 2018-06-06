import time
from queue import Queue
from sender import HttpPostSender
from receiver import MsgReceiver

# max wait time allowed for putting a new element in the queue
wait_time = 3
# number of max retransmissions for a single subscriber
retry_times = 4
url = "http://192.168.99.100:8000/gpsData/"

list = Queue(maxsize = 20)
sender = HttpPostSender()

# add new data to the blocking queue
# data = the data sent by the publisher
def addNewPublisherData(data):
    elem = {}
    elem["id"] = data["id"]
    elem["lat"] = data["lat"]
    elem["long"] = data["long"]
    list.put(elem, timeout = wait_time)

rcv = MsgReceiver(addNewPublisherData)
rcv.run()

while True:
    # get the item from the queue, if empty wait until it isn't anymore
    data = list.get()
    result = sender.sendData(url = url, info = data)
    print("data sent to the server | result {}".format(result))
    x = 0
    # if there is an error in the transmission, retry until it's ok
    while result != 200 and x < retry_times:
        time.sleep(1)
        result = sender.sendData(url = url, info = data)
        x += 1


