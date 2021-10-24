from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser


class AppUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = AppUser
        fields = ('username', 'email', 'position', 'skillset', 'mobile_phone', 'work_phone')


class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'position', 'skillset', 'mobile_phone', 'work_phone')
