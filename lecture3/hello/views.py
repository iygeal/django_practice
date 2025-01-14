from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """Function to render the index page"""
    return render(request, "hello/index.html")

def iygeal(request):
    """Function to render the iygeal page"""
    return HttpResponse("Hello Iygeal!")

def greet(request, name):
    """Function to render the greet page"""
    return HttpResponse(f"Hello {name.capitalize()}!")
