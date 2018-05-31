from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .receiver import ReceiveDataDevice
from .controller import DbrController
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
        ctr = DbrController()
        recv.processData(request.POST)
        ctr.saveData(Device.__class__, recv.getAllInformations())
        recv.printData()
    return HttpResponse("")



