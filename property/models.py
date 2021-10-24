from django.db import models

# Create your models here.
from client.models import Client


class Property(models.Model):
    property_name = models.CharField(max_length=30, default='', blank=False)
    street_address = models.CharField(max_length=40, default='', blank=False)
    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=2, default='NE')
    zipcode = models.CharField(max_length=9, default='00000')
    age_in_years = models.CharField(max_length=2, default = '', blank=True)

    class Meta:
        verbose_name_plural = 'Properties'

class Apartment(models.Model):
    size_in_sqft = models.IntegerField(default='', blank=False)
    number_of_bedrooms = models.IntegerField(default='', blank=False)
    floor = models.IntegerField(default='', blank=False)
    description = models.CharField(max_length=300, default=' ', blank=False)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
