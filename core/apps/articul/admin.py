from django.contrib import admin
from apps.articul.models import Articul


class ArticulAdmin(admin.ModelAdmin):
    model = Articul
    fields = ['userartikul', 'data_vidan', 'status', 'kod_phone', "zametki", "is_oplata"]
    list_display = ('userartikul', 'artikuls', 'status', 'nomer', 'id', "is_oplata", "zametki")
    list_filter = ('artikuls', 'userartikul')
    search_fields = ('userartikul__username',)
    # list_editable = ('tags',)


admin.site.register(Articul, ArticulAdmin)
