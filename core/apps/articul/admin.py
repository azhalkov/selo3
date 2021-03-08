from django.contrib import admin
from apps.articul.models import Articul


class ArticulAdmin(admin.ModelAdmin):
    model = Articul
    fields = ['userartikul', 'status', 'kod_phone']
    list_display = ('userartikul', 'artikuls', 'status', 'nomer', 'id')
    list_filter = ('artikuls', 'userartikul')
    search_fields = ('userartikul__username',)


admin.site.register(Articul, ArticulAdmin)
