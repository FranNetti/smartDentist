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
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        lat = request.POST["lat"]
        long = request.POST["long"]
        str = "latitudine: {} | longitudine: {}".format(lat,long)
        print(str)
        with open("app/coordinateGps.txt", "at") as myfile:
            print(str, file=myfile)
    return HttpResponse("")

