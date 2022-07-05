from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate

from django.http import HttpResponse
from .models import Feature


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    #if the user is trying to create an account then follow this
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

#check if the passwords matched if so then we want to check if the email or username is already in the database
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                # otherwise everything worked and we want to create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
#if the passwords dont match then send an error
        else:
            messages.info(request, "Passwords did not match")
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        #if the user exists, if the user is None then they are not on the platform...
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        #redirect to the homepage
        else:
            messages.info(request, "Credentials do not match our system, try again")
            return redirect('login')
    else:
        return render(request, 'login.html')
    #otherwise just show the login.html as they are just looking at this page

def logout(request):
    auth.logout(request)
    return redirect("/")

def post(request,pk):
    #will take a request and then the value pk
    return render(request, 'post.html', {'pk':pk})

def counter(request):
    posts = [1, 2, 3, 4, 'rafi', 'robyn', 'daku']
    return render(request, 'counter.html', {'posts': posts})