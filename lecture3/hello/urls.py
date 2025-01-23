#!/usr/bin/env python3
"""Module that defines routes for the hello app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")
]
