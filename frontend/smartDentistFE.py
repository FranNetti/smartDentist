import random
import datetime
import requests
import time
import string
import sys

from random import uniform

args = sys.argv
if (len(args) != 2):
    print("Inserire un numero di secondi per indicare quanto aspettare fra un invio e l'altro", file=sys.stderr)
    sys.exit(1) 

urlToSend = "http://192.168.99.100:8000/gpsData/"
waitTime = int(args[1])
x = 0

while True:
    id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    lat = uniform(0,90)
    long = uniform(0,180)
    doct_name = "Daniel"
    doct_surname = "Ricciardo"
    data = datetime.datetime.utcnow()
    r = requests.post(urlToSend, data = {
        'id': id,
        'lat': lat,
        'long' : long,
        'doct_name' : doct_name,
        'doct_surname' : doct_surname,
        'data' : data
        })
    print("{} post request - result {}".format(x,r.status_code))
    x += 1
    time.sleep(waitTime)
