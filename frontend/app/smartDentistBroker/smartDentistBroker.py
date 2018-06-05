from flask import Flask
from flask import request
from controller import Controller

url = "http://192.168.99.100:8000/gpsData/"
max_queue_size = 200

app = Flask(__name__)
ctr = Controller(max_queue_size, url)
ctr.start()

@app.route("/publishContent/<idElement>", methods=["POST"])
def publish(idElement):
    ctr.addNewPublisherData(idElement, request.form)
    return "", 200

@app.route("/subscribe/<type>")
def publish(type):
    ctr.subscribe(type, request.remote_addr)
    return "", 200

@app.route("/unsubscribe/<type>")
def publish(type):
    ctr.unsubscribe(type, request.remote_addr)
    return "", 200
