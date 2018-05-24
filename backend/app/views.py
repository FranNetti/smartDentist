from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def ciao(request):
    assert isinstance(request, HttpRequest)
    return HttpResponse("Ciao, mi chiamo smartDentist project")

def home(request):
    return HttpResponse("")
