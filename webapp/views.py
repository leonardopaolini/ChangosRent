from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .constants import *


def index(request):
    return redirect('login')


def login_view(request):
    context = {'error': 'Usuario/Contraseña no son válidos'}
    if request.method == POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/login.html', context)
    return render(request, 'login/login.html')


@login_required
def home_view(request):
    return render(request, "home/home.html")


@login_required
def rent_view(request):
    return render(request, "home/home.html")
