from django.contrib import admin
from .models import Zadacha



# Register your models here.
class ZadachaAdmin(admin.ModelAdmin):
    model = Zadacha
    fields = ['zadanie', 'data_vipolnenija', 'descript', 'fromuser', 'ispolnitel', 'is_activ', 'is_vipolneno', ]
    list_display = ('zadanie', 'is_vipolneno', 'data_vipolnenija', 'descript',
                    'fromuser', 'ispolnitel', 'is_activ', 'data_postanovki')
    # prepopulated_fields = {"slug": ("name",)}
    # exclude = ['data_postanovki']  # исключить поля из показа
    # empty_value_display = '-empty-'

    # list_editable = ['is_activ', 'is_vipolneno',]


admin.site.register(Zadacha, ZadachaAdmin)
