from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from enum import Enum
import uuid
from webapp.common.validation.validation_constants import *
from django.utils import timezone


class VehicleStatus(Enum):
    READY_FOR_USE = 'READY_FOR_USE'
    LOCKED_FOR_RENT = 'LOCKED_FOR_RENT'
    LOCKED_FOR_MAINTENANCE = 'LOCKED_FOR_MAINTENANCE'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    customer_id = models.UUIDField(unique=True, default=uuid.uuid4)
    enabled = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Person(Customer):
    first_name = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    last_name = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    birth_date = models.DateField(null=True)
    person_id = models.BigIntegerField(unique=True)


class Company(Customer):
    business_name = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    business_type = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    business_id = models.BigIntegerField(unique=True)


class VehicleType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    description = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH, null=True, blank=True)
    type_of_uses = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    created = models.DateTimeField(default=timezone.now)
    km_per_maintenance = models.IntegerField(auto_created=True, default=KM_PER_MAINTENANCE_MIN_VALUE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Vehicle(models.Model):
    VEHICLE_STATUS_CHOICES = [(status.name, status.value) for status in VehicleStatus]
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    model = models.CharField(max_length=CHAR_GENERAL_MAX_LENGTH)
    year = models.IntegerField(default=YEAR_MIN_VALUE)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, null=True, blank=True)
    buy_date = models.DateField(null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=30, default=VehicleStatus.READY_FOR_USE.value)
    def __str__(self):
        return f"{self.brand} - {self.model} - {self.year} - ${self.vehicle_type.price}"


class Rent(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    payment_method = models.CharField(max_length=50)
    vehicles = models.ManyToManyField(Vehicle)
    invoice_date = models.DateField(null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # Generic relation fields to deal with child models that extends from an abstract one
    customer_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    customer_id = models.PositiveIntegerField()
    customer_object = GenericForeignKey('customer_type', 'customer_id')
