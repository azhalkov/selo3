from django.contrib import admin
from apps.dom.models import Adres, Komunikacii


class AdresAdmin(admin.ModelAdmin):
    model = Adres
    fields = ("vid", "krai", "gorod", "raion", "mikroraion", "ulica", "nomer_doma", "nomer_podezda",
              "nomer_kvartiri", "is_activ", 'slug')
    list_display = ("vid", "gorod", "ulica", "nomer_doma", "nomer_podezda", "nomer_kvartiri", "is_activ")
    # list_filter = ('artikuls', 'userartikul')
    # search_fields = ('userartikul__username',)
    prepopulated_fields = {"slug": ("vid", "krai", "gorod",)}


admin.site.register(Adres, AdresAdmin)


class KomunikaciiAdmin(admin.ModelAdmin):
    model = Komunikacii
    fields = ("art", "vodoprovod", "data_voda", "otoplenie", "data_otoplenie", "kanalizacii",
              "data_kanalizacii", "descreption")
    list_display = ("art", "vodoprovod", "otoplenie", "kanalizacii")

    # list_filter = ('artikuls', 'userartikul')
    # search_fields = ('userartikul__username',)
    # prepopulated_fields = {"slug": ("vid", "krai", "gorod",)}


admin.site.register(Komunikacii, KomunikaciiAdmin)

