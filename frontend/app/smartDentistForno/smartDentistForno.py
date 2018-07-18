import time
import sys
import string

from sender import MsgSender
from retriever import RandomRtv
from receiver import MsgReceiver
from status import StatusHandler
from random import choice

args = sys.argv
if (len(args) < 2):
    print("Inserire un numero di minuti per indicare quanto aspettare fra un invio e l'altro", file=sys.stderr)
    sys.exit(1)

id = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(20))

waitTime = int(args[1]) * 60 - 60;
rtv = RandomRtv()
sender = MsgSender()
statusHandler = StatusHandler(sender, id)
receiver = MsgReceiver(statusHandler.changeStatus, id)
receiver.start()

time.sleep(20)

while True:
    statusHandler.saveStatus(True)
    data = rtv.getData(id)
    if statusHandler.isOn():
        sender.sendData(data)
        print("device {} | data sent".format(id))
        time.sleep(60)
        statusHandler.saveStatus(False)
    time.sleep(waitTime if waitTime > 0 else 60)
