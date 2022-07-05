from django.urls import path
from . import views

urlpatterns = [
    #empty '' is the root URL , views.index -> goes to the views.py file, and then looks for the fun
    #function or class called index
    path('', views.index, name="index"),
    path('counter', views.counter, name="counter"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]