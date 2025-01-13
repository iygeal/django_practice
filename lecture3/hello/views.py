from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """Function to render the index page"""
    return HttpResponse("Hello, world!")
