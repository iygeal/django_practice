from django.shortcuts import render

# Global variables
tasks = ["foo", "bar", "baz"]

# Create your views here.


def index(request):
    """Defines the index page"""
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
