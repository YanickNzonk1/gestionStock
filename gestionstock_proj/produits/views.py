from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1 style='color: red; font-family: bookman old style;'> Hello World from Yanick!!</h1>")

