import time
import sys
import string

from sender import MsgSender
from retriever import RandomRtv
from receiver import MsgReceiver
from random import choice

args = sys.argv
if (len(args) < 2):
    print("Inserire un numero di minuti per indicare quanto aspettare fra un invio e l'altro", file=sys.stderr)
    sys.exit(1)

id = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(20))

def changeState(data):
    if(data["id"] == id):
        status = data["status"]
        print("status device {}|{}".format(id, status))

waitTime = int(args[1]) * 60;
rtv = RandomRtv()
sender = MsgSender()
receiver = MsgReceiver(changeState, id)
receiver.start()

while True:
    data = rtv.getData(id)
    sender.sendData(data)
    print("device {} | data sent".format(id))
    time.sleep(waitTime)
