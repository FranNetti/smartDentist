import time
import sys
import string

from sender import HttpPostSender
from retriever import RandomRtv
from random import choice

args = sys.argv
if (len(args) != 2):
    print("Inserire un numero di secondi per indicare quanto aspettare fra un invio e l'altro", file=sys.stderr)
    sys.exit(1) 

urlToSend = "http://127.0.0.2:56789/publishContent/{}"
id = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(20))
urlToSend.format(id)

waitTime = int(args[1])
x = 0
rtv = RandomRtv()
sender = HttpPostSender()

while True:
    data = rtv.getData()
    code = sender.sendData(urlToSend, data)
    time.sleep(waitTime)
