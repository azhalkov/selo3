# apps/picture/admin
from django.contrib import admin
from apps.picture.models import Foto


class FotoAdmin(admin.ModelAdmin):
    model = Foto
    fields = ("title", "art", "image",)
    list_display = ("title", "art", "image",)
    # list_filter = ('artikuls', 'userartikul')
    # search_fields = ('userartikul__username',)
    # prepopulated_fields = {"slug": ("vid", "krai", "gorod",)}


admin.site.register(Foto, FotoAdmin)

