from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from enum import Enum
import uuid
from django.utils import timezone


class RentStatus(Enum):
    CREATED = 'CREATED'
    UPDATED = 'UPDATED'
    CANCELLED = 'CANCELLED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'


class Customer(models.Model):
    RENT_STATUS_CHOICES = [(status.name, status.value) for status in RentStatus]
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    customer_id = models.UUIDField(unique=True, default=uuid.uuid4)
    enabled = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True


class Person(Customer):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    person_id = models.BigIntegerField(unique=True)


class Company(Customer):
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    business_id = models.BigIntegerField(unique=True)


class VehicleType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    type_of_uses = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now())
    km_per_maintenance = models.IntegerField(auto_created=True, default=2000)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(default=0)
    description = models.CharField(max_length=500, null=True)
    buy_date = models.DateField(null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING)
 
    #reemplar estos 3 campos por uno de status con estos estados + uno de bloqueo temporal por carrito
    ready_for_use = models.BooleanField(default=True)
    lock_for_rent = models.BooleanField(default=False)
    lock_for_maintenance = models.BooleanField(default=False)


class Rent(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(default=timezone.now())
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    # llevar este statusd a vehiculo y que funcione como cuando se agregue a la renta se pone un estatus blockeado temporal y que cuando se confirme la renta se pase a bloqueado 
    status = models.CharField(max_length=10, default=RentStatus.CREATED.value)
    payment_method = models.CharField(max_length=50)
    vehicles = models.ManyToManyField(Vehicle)
    invoice_date = models.DateField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # Generic relation fields to deal with child models that extends from an abstract one
    customer_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    customer_id = models.PositiveIntegerField()
    customer_object = GenericForeignKey('customer_type', 'customer_id')
