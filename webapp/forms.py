from django import forms
from webapp.common.validation.form_error_messages import *
from webapp.models import Rent, VehicleType, Vehicle, Person, Company


class CreateRentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        error_messages = rent_error_messages


class CreateVehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name', 'description', 'type_of_uses', 'km_per_maintenance', 'price']
        error_messages = vehicle_type_error_messages
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'type_of_uses': 'Tipo de Usos',
            'km_per_maintenance': 'Km por Mantenimiento',
            'price': 'Precio',
        }
    widgets = {
        'name': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})),
        'description': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Descripción'})),
        'type_of_uses': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(attrs={'placeholder': 'Tipo de Usos'})),
        'km_per_maintenance': forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Km por Mantenimiento'})),
        'price': forms.DecimalField(max_digits=7, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'placeholder': 'Precio'})),
    }


class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        error_messages = vehicle_error_messages


class CreateCompanyCustomerForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        error_messages = company_error_messages


class CreatePersonCustomerForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        error_messages = person_error_messages
