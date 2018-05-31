import time
import sys

from sender import HttpPostSender
from retriever import RandomRtv

args = sys.argv
if (len(args) != 2):
    print("Inserire un numero di secondi per indicare quanto aspettare fra un invio e l'altro", file=sys.stderr)
    sys.exit(1) 

urlToSend = "http://192.168.99.100:8000/gpsData/"
waitTime = int(args[1])
x = 0
rtv = RandomRtv()
sender = HttpPostSender()

while True:
    data = rtv.getData()
    code = sender.sendData(urlToSend, data)
    print("{} post request - result {}".format(x,code))
    x += 1
    time.sleep(waitTime)
