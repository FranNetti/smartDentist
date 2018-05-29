from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def ciao(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("Ciao, mi chiamo smartDentist project")

def home(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("")

def setGpsData(request):
    from .models import ReceiveData
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        elem = ReceiveData(request.POST)
        elem.processData()
        elem.printData()            
    return HttpResponse("")



