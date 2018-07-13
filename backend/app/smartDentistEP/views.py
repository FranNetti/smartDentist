from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .receiver import ReceiveDataDevice
from .controller import DbrController, LogStashController
from .models import Device

def home(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("")

def ciao(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("Ciao, mi chiamo smartDentist project")

def setGpsData(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        recv = ReceiveDataDevice()
        dbCtr = DbrController()
        lsCtr = LogStashController("logstash", 8085)
        recv.processData(request.POST)
        dbCtr.saveData(Device.__class__, recv.getAllInformations())
        lsCtr.saveData(recv.getAllInformations())
        recv.printData()
        
    return HttpResponse("")



