from django import forms
from django.core.exceptions import ValidationError
from webapp.validation.form_error_messages import *
from webapp.models import Rent


class CreateRentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = rent_error_messages


class CreateVehicleTypeForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = vehicle_type_error_messages


class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = vehicle_error_messages


class CreateCompanyCustomerForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = company_error_messages


class CreatePersonCustomerForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = person_error_messages
