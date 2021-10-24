from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30, blank=False, default='')
    last_name = models.CharField(max_length=30, blank=False, default = '')
    mobile_phone = models.CharField(max_length=10, blank=False, default='')
    work_phone = models.CharField(max_length=10, blank=True, default='')
    comments = models.CharField(max_length=200, blank=True, default='')
