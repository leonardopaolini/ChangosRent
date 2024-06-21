from django import forms
from django.contrib.auth.models import User

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
        'name': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre'})),
        'description': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=False,
                                       widget=forms.TextInput(attrs={'placeholder': 'Descripción'})),
        'type_of_uses': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                        widget=forms.TextInput(attrs={'placeholder': 'Tipo de Usos'})),
        'km_per_maintenance': forms.IntegerField(required=True, widget=forms.NumberInput(
            attrs={'placeholder': 'Km por Mantenimiento'})),
        'price': forms.DecimalField(max_digits=7, decimal_places=2, required=True,
                                    widget=forms.NumberInput(attrs={'placeholder': 'Precio'})),
    }


class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        error_messages = vehicle_error_messages


class SignUpCompanyCustomerForm(forms.ModelForm):
    user_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, label='Usuario',
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    password = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH, required=True,
                               label='Contraseña',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password_confirm = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH,
                                       required=True,
                                       label='Confirmar Contraseña',
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'Confirmar Contraseña'}))
    class Meta:
        model = Company
        fields = ['email', 'address', 'business_name', 'business_type',
                  'business_id']
        error_messages = company_error_messages
        labels = {
            'email': 'Email',
            'address': 'Dirección',
            'business_name': 'Nombre de la Compañía',
            'business_type': 'Tipo de Compañia',
            'business_id': 'Id de Compañia',
        }

    widgets = {
        'email': forms.EmailField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Email'})),
        'address': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Dirección'})),
        'business_name': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH,
                                         required=True, widget=forms.TextInput(
                attrs={'placeholder': 'Nombre de Compañía'})),
        'business_type': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                         widget=forms.TextInput(
                                             attrs={'placeholder': 'Tipo de Compañía'})),
        'business_id': forms.IntegerField(min_value=COMPANY_ID_MIN_VALUE, max_value=COMPANY_ID_MAX_VALUE,
                                          required=True,
                                          widget=forms.NumberInput(attrs={'placeholder': 'Id de Compañía'})),
    }

    def save(self, commit=True):
        company = super().save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data['user_name'],
                email=company.email,
                password=self.cleaned_data['password'],
                first_name=company.business_name,
                last_name=company.business_name,
            )
            company.user = user
            company.save()
        return company


class SignUpPersonCustomerForm(forms.ModelForm):
    user_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, label='Usuario',
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    password = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH, required=True,
                               label='Contraseña',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password_confirm = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH,
                                       required=True,
                                       label='Confirmar Contraseña',
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'Confirmar Contraseña'}))

    class Meta:
        model = Person
        fields = ['email', 'address', 'person_id', 'first_name', 'last_name',
                  'birth_date']
        error_messages = person_error_messages
        labels = {
            'email': 'Email',
            'address': 'Dirección',
            'person_id': 'Id de Persona',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'birth_date': 'Fecha de Nacimiento',
        }

    widgets = {
        'email': forms.EmailField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Email'})),
        'address': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Dirección'})),
        'person_id': forms.IntegerField(min_value=PERSON_ID_MIN_VALUE, max_value=PERSON_ID_MAX_VALUE, required=True,
                                        widget=forms.NumberInput(
                                            attrs={'placeholder': 'Id de Persona'})),
        'first_name': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Nombre'})),
        'last_name': forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Apellido'})),
        'birth_date': forms.DateField(required=True,
                                      widget=forms.DateInput(attrs={'placeholder': 'Fecha de Nacimiento'})),
    }

    def save(self, commit=True):
        person = super().save(commit=False)
        if commit:
            user = User.objects.create_user(
                username=self.cleaned_data['user_name'],
                email=person.email,
                password=self.cleaned_data['password'],
                first_name=person.first_name,
                last_name=person.last_name,
            )
            person.user = user
            person.save()
        return person
