from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    """
    home(request)

    Returns a simple HttpResponse with the text "Hello, World!".
    """
    return HttpResponse("Hello, World!")
