# from idlelib.query import Query

from django.http import HttpResponse
from django.shortcuts import render
from adminapp.models import Admin



def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def facultylogin(request):
    return render(request,"facultylogin.html")

def studentlogin(request):
    return render(request,"studentlogin.html")

def contactfunction(request):
    return render(request,"contact.html")


