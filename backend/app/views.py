from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ciao(request):
    return HttpResponse("Ciao, mi chiamo smartDentist project")
