from django.contrib import admin
from .models import Property, Apartment

class PropertyAdmin(admin.ModelAdmin):
   model = Property
   list_display = ['property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years']
   list_filter = ['property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years']
   fieldset = (
         ('Property Information', {
            'fields': ('property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years')
        })
   )
   add_fieldset = (
         ('Property Information', {
            'fields': ('property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years')
        })
   )

class ApartmentAdmin(admin.ModelAdmin):
   model = Apartment
   list_display = ['apt_num', 'size_in_sqft', 'number_of_bedrooms', 'description', 'property_id', 'client_id']
   fieldset = (
         ('Apartment Information', {
            'fields': ('apt_num', 'size_in_sqft', 'number_of_bedrooms', 'description', 'property_id', 'client_id')
        })
   )
   add_fieldset = (
         ('Apartment Information', {
            'fields': ('apt_num', 'size_in_sqft', 'number_of_bedrooms', 'description', 'property_id', 'client_id')
        })
   )

admin.site.register(Property, PropertyAdmin)
admin.site.register(Apartment, ApartmentAdmin)
