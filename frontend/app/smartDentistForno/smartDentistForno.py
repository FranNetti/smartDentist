import time
import sys
import string

from sender import MsgSender
from retriever import RandomRtv
from random import choice

args = sys.argv
if (len(args) < 3):
    print("Inserire un numero di minuti per indicare quanto aspettare fra un invio e l'altro", file=sys.stderr)
    sys.exit(1) 

id = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(20))

waitTime = int(args[1]) * 60;
rtv = RandomRtv()
sender = MsgSender()

while True:
    data = rtv.getData(id)
    sender.sendData(data)
    print("device {} | data sent".format(id))
    time.sleep(waitTime)
