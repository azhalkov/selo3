from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField



'''класс Form будет иметь поле формы для каждого указанного поля модели
 в порядке, указанном в атрибуте fields'''
class ZadachaForm(forms.ModelForm):

    class Meta:
        model = Zadacha
        exclude = ['data_postanovki', 'is_vipolneno', 'is_activ',]


