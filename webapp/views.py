from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from webapp.common.constants import *
from webapp.forms import CreateVehicleTypeForm, SignUpPersonCustomerForm, SignUpCompanyCustomerForm, CreateVehicleForm, \
    CreateRentForm, ResetPasswordForm
from webapp.models import VehicleType, Vehicle, Rent
from webapp.common.utils.views_utils import *
from webapp.common.api.email_api_client import notify
import logging
from django.contrib import messages

logger = logging.getLogger('webapp')


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
    return render(request, 'home/home.html')


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


def signup_person(request):
    context = {}
    if request.method == POST:
        form = SignUpPersonCustomerForm(request.POST)
        if form.is_valid():
            person = form.save()
            user = authenticate(username=person.user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                notify(sign_up_person_message(person, user))
                return redirect_to_home()
    else:
        form = SignUpPersonCustomerForm()
    context['form'] = form
    return render(request, 'customer/signup/person/signup_customer.html', context)


def signup_company(request):
    context = {}
    if request.method == POST:
        form = SignUpCompanyCustomerForm(request.POST)
        if form.is_valid():
            company = form.save()
            user = authenticate(username=company.user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                notify(sign_up_company_message(company, user))
                return redirect_to_home()
    else:
        form = SignUpCompanyCustomerForm()
    context['form'] = form
    return render(request, 'customer/signup/company/signup_customer.html', context)


@login_required(login_url='login')
def create_vehicle(request):
    context = {}
    if request.method == POST:
        form = CreateVehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateVehicleForm()
    context['form'] = form
    return render(request, 'vehicle/create_vehicle.html', context)


@login_required(login_url='login')
def edit_vehicle(request, vehicle_id):
    context = {}
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == POST:
        form = CreateVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateVehicleForm(instance=vehicle)
    context['form'] = form
    context['vehicle'] = vehicle
    return render(request, 'vehicle/edit_vehicle.html', context)


@login_required(login_url='login')
def list_vehicle(request):
    context = {}
    vehicles = Vehicle.objects.all().order_by('model')
    context['vehicles'] = vehicles
    return render(request, 'vehicle/vehicle_list.html', context)


@login_required(login_url='login')
def create_rent(request):
    context = {}
    if request.method == POST:
        form = CreateRentForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            #form.save_m2m()
            return redirect('home')
    else:
        form = CreateRentForm(request.user)
    context['form'] = form
    return render(request, 'rent/create_rent.html', context)


@login_required(login_url='login')
def list_rent(request):
    context = {}
    rents = Rent.objects.all().order_by('invoice_date')
    context['rents'] = rents
    return render(request, 'rent/rent_list.html', context)


@login_required(login_url='login')
def list_rent_by_customer(request):
    context = {}
    customer = find_customer_by_user(request.user)
    rents = customer.rents.all().order_by('invoice_date')
    context['rents'] = rents
    return render(request, 'rent/rent_list.html', context)


def request_for_password_reset(request):
    logger.info("Reset password requested!")
    if request.method == POST:
        email = request.POST['email']
        try:
            user = find_user_by_email(email)
        except User.DoesNotExist:
            user = None
            logger.warning(f"User does not exist for email {email}!")
        if user is not None:
            messages.success(request, "El reinicio de contraseña se ha generado con éxito. Revisá tu email")
            notify(reset_password_request_message(request, user, email))
        else:
            messages.error(request, "El reinicio de contraseña no pudo realizarse. Verificá que tu email se correcto")
        return render(request, 'account/reset-password-request-confirmation.html')
    return render(request, 'account/reset-password.html')


def reset_password(request, uid=None, token=None):
    logger.info('Executing password reset!')
    context = {}
    assert uid is not None and token is not None
    try:
        user = decode_password_reset_request_user(uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == POST:
            form = ResetPasswordForm(user, data=request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, 'La constraseña se modificó con éxito!')
                return render(request, 'account/reset-password-success.html')
        else:
            form = ResetPasswordForm(user)
        context['form'] = form
    else:
        messages.error(request, 'El enlace no es válido!')
    return render(request, 'account/reset-password-confirmation.html', context)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'
