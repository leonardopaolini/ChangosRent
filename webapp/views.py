from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from webapp.common.constants import *
from webapp.forms import CreateVehicleTypeForm
from webapp.models import VehicleType


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


@login_required(login_url='login')
def home_view(request):
    return render(request,'home/home.html')


@login_required(login_url='login')
def rent_view(request):
    return render(request, "home/home.html")


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def create_vehicle_type(request):
    context = {}
    if request.method == POST:
        form = CreateVehicleTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateVehicleTypeForm()
    context['form'] = form
    return render(request, 'vehicle_type/create_vehicle_type.html', context)


@login_required(login_url='login')
def edit_vehicle_type(request, vehicle_type_id):
    context = {}
    vehicle_type = get_object_or_404(VehicleType, pk=vehicle_type_id)
    if request.method == POST:
        form = CreateVehicleTypeForm(request.POST, instance=vehicle_type)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateVehicleTypeForm(instance=vehicle_type)
    context['form'] = form
    context['vehicle_type'] = vehicle_type
    return render(request, 'vehicle_type/edit_vehicle_type.html', context)


@login_required(login_url='login')
def list_vehicle_type(request):
    context = {}
    vehicle_types = VehicleType.objects.all().order_by('name')
    context['vehicle_types'] = vehicle_types
    return render(request, 'vehicle_type/vehicle_type_list.html', context)
