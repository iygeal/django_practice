from django.urls import path
from . import views


# Give the routes/URLS for the tasks app a name
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
