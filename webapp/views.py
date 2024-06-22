from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from webapp.common.constants import *
from webapp.forms import CreateVehicleTypeForm, SignUpPersonCustomerForm, SignUpCompanyCustomerForm
from webapp.models import VehicleType
from webapp.common.utils.views_utils import get_menu, redirect_to_login, redirect_to_home


def index(request):
    return redirect_to_login()


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
    if request.method == GET and request.user.is_authenticated:
        return redirect_to_home()
    return render(request, 'login/login.html')


@login_required(login_url='login')
def home_view(request):
    return render(request, 'home/home.html', {'menu': get_menu(request)})


@login_required(login_url='login')
def rent_view(request):
    return render(request, "home/home.html")


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect_to_login()


@login_required(login_url='login')
def create_vehicle_type(request):
    context = {}
    if request.method == POST:
        form = CreateVehicleTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect_to_home()
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
            return redirect_to_home()
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


def select_customer_type(request):
    if request.method == 'POST':
        customer_type = request.POST.get('customer_type')
        if customer_type == 'person':
            return redirect('signup_person')
        elif customer_type == 'company':
            return redirect('signup_company')
    return render(request, 'customer/signup/customer_type_selection.html')


def signup_person(request):
    context = {}
    if request.method == 'POST':
        form = SignUpPersonCustomerForm(request.POST)
        if form.is_valid():
            person = form.save()
            user = authenticate(username=person.user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect_to_home()
    else:
        form = SignUpPersonCustomerForm()
    context['form'] = form
    return render(request, 'customer/signup/signup_customer.html', context)


def signup_company(request):
    context = {}
    if request.method == 'POST':
        form = SignUpCompanyCustomerForm(request.POST)
        if form.is_valid():
            company = form.save()
            user = authenticate(username=company.user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect_to_home()
    else:
        form = SignUpCompanyCustomerForm()
    context['form'] = form
    return render(request, 'customer/signup/signup_customer.html', context)