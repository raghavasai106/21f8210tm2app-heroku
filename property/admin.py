from django.contrib import admin

# Register your models here.
from property.models import Property, Apartment

admin.site.register(Property)
admin.site.register(Apartment)