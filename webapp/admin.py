from django.contrib import admin

from webapp.models import Person, Company, Vehicle, VehicleType, Rent

admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Rent)
admin.site.register(VehicleType)
admin.site.register(Vehicle)
