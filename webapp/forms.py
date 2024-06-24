from django import forms
from django.contrib.auth.models import User

from webapp.common.validation.form_error_messages import *
from webapp.models import Rent, VehicleType, Vehicle, Person, Company, Customer
from django.utils  import timezone
from django.core.exceptions import ValidationError
import datetime


class CreateVehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name', 'description', 'type_of_uses', 'km_per_maintenance', 'price']
        error_messages = vehicle_type_error_messages

    name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), label='Nombre')
    description = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Descripción'}), label='Descripción')
    type_of_uses = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Tipo de Usos'}), label='Tipo de Usos')
    km_per_maintenance = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Km por Mantenimiento'}), label='Km por Mantenimiento')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True,
                               widget=forms.NumberInput(attrs={'placeholder': 'Precio'}), label='Precio')


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

        email = forms.EmailField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Email'}), label="Email")
        address = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Dirección'}), label="Dirección")
        business_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH,
                                        required=True,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'Nombre de Compañía'}), label="Nombre de Compañía")
        business_type = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': 'Tipo de Compañía'}), label="Tipo de Compañía")
        business_id = forms.IntegerField(min_value=COMPANY_ID_MIN_VALUE, max_value=COMPANY_ID_MAX_VALUE,
                                         required=True,
                                         widget=forms.NumberInput(attrs={'placeholder': 'Id de Compañía'}),
                                         label="Id de Compañía")

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

    email = forms.EmailField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='Email')
    address = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Dirección'}), label='Dirección')
    person_id = forms.IntegerField(min_value=PERSON_ID_MIN_VALUE, max_value=PERSON_ID_MAX_VALUE, required=True,
                                   widget=forms.NumberInput(
                                       attrs={'placeholder': 'Id de Persona'}), label='Id de Persona')
    first_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre'}), label='Nombre')
    last_name = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Apellido'}), label='Apellido')
    birth_date = forms.DateField(required=True,
                                 widget=forms.DateInput(attrs={'placeholder': 'Fecha de Nacimiento'}), label='Fecha de Nacimiento')


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

    brand = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Marca'}), label='Marca')
    model = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Modelo'}), label='Modelo')
    year = forms.IntegerField(min_value=2000, max_value=2100, required=True,
                              widget=forms.NumberInput(attrs={'placeholder': 'Año'}), label='Año')
    description = forms.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Descripción'}),
                                  label='Descripción')
    buy_date = forms.DateField(
        input_formats=['%m/%d/%Y','%d/%m/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'form-control mydatepicker'}), required=True,
        label='Fecha de Compra')
    # 'vehicle_type': forms.Select(attrs={'class': 'custom-select'}),


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
            'end_date' : 'Fecha hasta',
            'vehicles' : 'Vehiculos',
            'payment_method' : 'Forma de pago',
 #           'total': 'Total',
        }
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
        #obtener usuario logueado
        #a partir de este usuario obtener persona o empresa (customer)
        # poner esta instancia en la renta
        #y fin
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
            rentaux2= Rent()
            rentaux= Rent.objects.get(id=rent.id)

            #calculo el total de la factura
            total=0
            for vehicle in rentaux.vehicles.all():
                total= total + vehicle.vehicle_type.price
            dias = rent.end_date - rent.start_date 
            rent.total=total*dias.days
          
            rent.save()

            

#            for vehicle in rent.vehicles:
#                total= total + vehicle.vehicle_type.price
#            rent.total=total
#            rent.save()
        return rent
    def save_m2m(self, commit=True):
        vehiculos= self.cleaned_data.get('vehicles')
        print("vehicles:", vehiculos)
        super().save_m2m()  # Llama al método original para guardar las relaciones ManyToMany        

#            for vehicle in rent.vehicles:
#                total= total + vehicle.vehicle_type.price
#            rent.total=total
#            rent.save()
    
