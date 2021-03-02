# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    # fields = ['email', 'username', 'phone']
    list_editable = ['phone',]
    list_display = ['email', 'username', 'phone']
    admin.site.site_header = 'СЕЛЬСКАЯ НЕДВИЖИМОСТЬ'

admin.site.register(User, MyUserAdmin)