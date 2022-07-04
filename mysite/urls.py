from django.urls import path
from . import views

urlpatterns = [
    #empty '' is the root URL , views.index -> goes to the views.py file, and then looks for the fun
    #function or class called index
    path('', views.index, name="index"),
    path('counter', views.counter, name="counter"),
]