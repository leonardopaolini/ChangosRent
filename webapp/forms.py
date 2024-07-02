from django import forms
from django.contrib.auth.models import User

from webapp.common.validation.form_error_messages import *
from webapp.models import Rent, VehicleType, Vehicle, Person, Company, VehicleStatus
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.password_validation import validate_password


class MyDateInput(forms.widgets.DateInput):
    input_type = 'DateInput'
    format = '%d/%m/%Y'
    def __init__(self, attrs=None, format=None):
        # Agrega los atributos que desees aquí
        default_attrs = {'class': 'form-control border-danger', 'placeholder': 'Selecciona una fecha'}
        # default_attrs = {'class': 'form-control mydatepicker form-control border-danger', 'placeholder': 'Selecciona una fecha'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs, format=format)    


class CreateVehicleTypeForm(forms.ModelForm):

    class Meta:
        model = VehicleType
        fields = ['name', 'description', 'type_of_uses', 'km_per_maintenance', 'price']
        error_messages = vehicle_type_error_messages

    name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre','class':'form-control border-danger'}), label='Nombre')
    description = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Descripción','class':'form-control border-danger'}), label='Descripción')
    type_of_uses = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Tipo de Usos','class':'form-control border-danger'}), label='Tipo de Usos')
    km_per_maintenance = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Km por Mantenimiento','class':'form-control border-danger'}), label='Km por Mantenimiento')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True,
                            widget=forms.NumberInput(attrs={'placeholder': 'Precio','class':'form-control border-danger'}), label='Precio')


class SignUpCompanyCustomerForm(forms.ModelForm):
    user_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, label='Usuario',
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control input-lg'}))
    password = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH, required=True,
                               label='Contraseña',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control input-lg'}))
    password_confirm = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH,
                                       required=True,
                                       label='Confirmar Contraseña',
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control input-lg'}))

    class Meta:
        model = Company
        fields = ['email', 'address', 'business_name', 'business_type',
                  'business_id']
        error_messages = company_error_messages

    email = forms.EmailField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control input-lg'}), label="Email")
    address = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Dirección', 'class': 'form-control input-lg'}), label="Dirección")
    business_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH,
                                    required=True,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Nombre de Empresa', 'class': 'form-control input-lg'}), label="Nombre de Empresa")
    business_type = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Tipo de Empresa', 'class': 'form-control input-lg'}), label="Tipo de Empresa")
    business_id = forms.IntegerField(min_value=COMPANY_ID_MIN_VALUE, max_value=COMPANY_ID_MAX_VALUE,
                                     required=True,
                                     widget=forms.NumberInput(attrs={'placeholder': 'Id de Empresa', 'class': 'form-control input-lg'}),
                                     label="Id de Empresa")

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
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control input-lg'}))
    password = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH, required=True,
                               label='Contraseña',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control input-lg'}))
    password_confirm = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH,
                                       required=True,
                                       label='Confirmar Contraseña',
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control input-lg'}))

    class Meta:
        model = Person
        fields = ['email', 'address', 'person_id', 'first_name', 'last_name',
                  'birth_date']
        error_messages = person_error_messages

    email = forms.EmailField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control input-lg'}), label='Email')
    address = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Dirección', 'class': 'form-control input-lg'}), label='Dirección')
    person_id = forms.IntegerField(min_value=PERSON_ID_MIN_VALUE, max_value=PERSON_ID_MAX_VALUE, required=True,
                                   widget=forms.NumberInput(
                                       attrs={'placeholder': 'Id de Persona', 'class': 'form-control input-lg'}), label='Id de Persona')
    first_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'form-control input-lg'}), label='Nombre')
    last_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Apellido', 'class': 'form-control input-lg'}), label='Apellido')
    birth_date = forms.DateField(required=True,
                                 widget=forms.DateInput(attrs={'placeholder': 'Fecha de Nacimiento', 'class': 'form-control input-lg'}), label='Fecha de Nacimiento')

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


class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'year', 'description', 'buy_date', 'vehicle_type']
        error_messages = vehicle_error_messages
        widgets = {
            'vehicle_type': forms.Select(
                attrs={'placeholder': 'Tipo de Vehículo', 'class': 'form-control border-danger'})
        }
        labels = {
            'vehicle_type': 'Tipo de Vehículo'
        }

    brand = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Marca', 'class': 'form-control border-danger'}), label='Marca')
    model = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Modelo', 'class': 'form-control border-danger'}), label='Modelo')
    year = forms.IntegerField(min_value=2000, max_value=2100, required=True,
                              widget=forms.NumberInput(
                                  attrs={'placeholder': 'Año', 'class': 'form-control border-danger'}), label='Año')
    description = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=False,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Descripción', 'class': 'form-control border-danger'}),
                                  label='Descripción')
    buy_date = forms.DateField(
        widget=MyDateInput(),
        required=True,
        label='Fecha de Compra'
    )


class CreateRentForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CreateRentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rent
        fields = ['start_date', 'end_date', 'vehicles','payment_method']
        error_messages = rent_error_messages 
        labels = {
            'start_date': 'Fecha desde',
            'end_date': 'Fecha hasta',
            'vehicles': 'Vehiculos',
            'payment_method': 'Forma de pago'
        }


    payment_method= forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Forma de pago','class':'form-control border-danger'}),label='Forma de pago')
    start_date = forms.DateField(
        widget=MyDateInput(),
        required=True,
        label='Fecha desde')
    end_date = forms.DateField(
        widget=MyDateInput(),
        required=True,
        label='Fecha hasta')
    vehicles= forms.MultipleChoiceField(
        choices=[(item.pk, item) for item in Vehicle.objects.filter(status = VehicleStatus.READY_FOR_USE.value).order_by('model')],
        required=True,
        widget=forms.SelectMultiple(attrs={'placeholder': 'Vehiculos','class':'form-control border-danger'}),
        label='Vehiculos'
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date= cleaned_data.get("start_date")
        end_date= cleaned_data.get("end_date")
        if isinstance(start_date,datetime.date):
            if isinstance(end_date,datetime.date):
                if start_date>end_date:
                    raise ValidationError("La fecha de inicio debe ser menor que la fecha de fin")
        return cleaned_data

    def save(self, commit=True):
        rent= super().save(commit=False)
        if commit:
            user= self.user
            
            customer = Person.objects.filter(user=user).first()
            if customer is None:
                customer = Company.objects.filter(user=user).first()
            rent.customer_object = customer            
            rent.total=0
            rent.invoice_date=timezone.now().date()
            rent.save()
            self.save_m2m()

            rent_aux = Rent.objects.get(id=rent.id)

            total=0
            for vehicle in rent_aux.vehicles.all():
                total = total + vehicle.vehicle_type.price
            dias = rent.end_date - rent.start_date 
            rent.total = total*dias.days
            rent.save()
        return rent

    def save_m2m(self, commit=True):
        vehicles= self.cleaned_data.get('vehicles')
        print("vehicles:", vehicles)
        super().save_m2m()  # Llama al método original para guardar las relaciones ManyToMany        


class ResetPasswordForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    password = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH, required=True,
                               label='Contraseña',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Contraseña', 'class': 'form-control input-lg'}))
    password_confirm = forms.CharField(max_length=PASSWORD_MAX_LENGTH, min_length=PASSWORD_MIN_LENGTH,
                                       required=True,
                                       label='Confirmar Contraseña',
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'Confirmar Contraseña',
                                                  'class': 'form-control input-lg'}))

    def clean_password(self):
        validate_password(self.cleaned_data["password"])
        return self.cleaned_data["password"]

    def clean_password_confirm(self):
        validate_password(self.cleaned_data["password_confirm"])
        return self.cleaned_data["password_confirm"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation = cleaned_data.get('password_confirm')
        if password and confirmation and password != confirmation:
            raise forms.ValidationError("La contraseña y la confirmación no son iguales.")
        return self.cleaned_data


class CreateCompanyCustomerForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['business_name', 'business_type',
                  'business_id']
        error_messages = company_error_messages

    business_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH,
                                    required=True,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Nombre de Empresa', 'class': 'form-control input-lg'}), label="Nombre de Empresa")
    business_type = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Tipo de Empresa', 'class': 'form-control input-lg'}), label="Tipo de Empresa")
    business_id = forms.IntegerField(min_value=COMPANY_ID_MIN_VALUE, max_value=COMPANY_ID_MAX_VALUE,
                                     required=True,
                                     widget=forms.NumberInput(attrs={'placeholder': 'Id de Empresa', 'class': 'form-control input-lg'}),
                                     label="CUIT")



class CreatePersonCustomerForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['person_id', 'first_name', 'last_name',
                  'birth_date']
        error_messages = person_error_messages

    person_id = forms.IntegerField(min_value=PERSON_ID_MIN_VALUE, max_value=PERSON_ID_MAX_VALUE, required=True,
                                   widget=forms.NumberInput(
                                       attrs={'placeholder': 'Id de Persona', 'class': 'form-control input-lg'}),
                                    label='DNI')
    first_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'form-control input-lg'}), label='Nombre')
    last_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Apellido', 'class': 'form-control input-lg'}), label='Apellido')
    birth_date = forms.DateField(required=True,
                                widget=MyDateInput(),

                                label='Fecha de Nacimiento')

