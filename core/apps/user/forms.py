# apps/user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'phone')

class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'phone')