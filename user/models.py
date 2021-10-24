from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    email = models.CharField(max_length=30, blank=False, default='')
    position = models.CharField(max_length=30, blank=False, default=' ')
    skillset = models.CharField(max_length=200, blank=False, default=' ')
    mobile_phone = models.CharField(max_length=10, blank=False, default='0000000000')
    work_phone = models.CharField(max_length=10, blank=True, default='0000000000')
