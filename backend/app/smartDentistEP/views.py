import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

from .receiver import ReceiveDataDevice
from .controller import DbrController, LogStashController
from .models import *

recv = ReceiveDataDevice()
dbCtr = DbrController()
lsCtr = LogStashController("logstash", 8085)

def home(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("")

def ciao(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("Ciao, mi chiamo smartDentist project")

def setGpsData(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        recv.processData(request.POST)
        info = recv.getAllInformations()
        dbCtr.saveData(Device, info)
        lsCtr.saveData(info)
        recv.printData()

    return HttpResponse("")

def changeDeviceStatus(request):
    assert isinstance(request, HttpRequest)
    param = {}
    if request.method == 'POST':
        data = request.POST
        id = data["device_id"]
        if not(id) or id.isspace():
            param["error"] = "The id field is empty or only whitespaces, retry"
        else:
            info = {
                'id' : id,
                'status' : data["operation"] == 'on'
                }
            try:
                dbCtr.saveData(DeviceStatus, info)
            except DeviceStatus.DoesNotExist:
                param["error"] = "The device doesn't exist, insert a correct id"

    return render(request, 'smartDentistEP/manageDevice.html', param)

def getDeviceStatus(request):
    assert isinstance(request, HttpRequest)
    data = dbCtr.getJsonData(DeviceStatus)

    return JsonResponse(data)
