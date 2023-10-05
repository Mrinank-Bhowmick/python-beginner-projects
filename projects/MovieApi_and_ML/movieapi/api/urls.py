from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", view=views.movie, name="movie"),
    path("predict/", view=views.predict, name="predict"),
]
