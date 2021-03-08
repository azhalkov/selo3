# apps/user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    # fieldsets = (
    #     (None, {
    #         'fields': ('email', 'first_name', 'phone', 'last_name')
    #     }),)
    # fields = ('email', 'first_name', 'phone', 'last_name',)
    list_editable = ['phone',]
    list_display = ['email', 'username', 'phone']
    admin.site.site_header = 'СЕЛЬСКАЯ НЕДВИЖИМОСТЬ'

admin.site.register(User, MyUserAdmin)