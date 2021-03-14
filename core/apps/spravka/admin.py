# apps/spravka/admin
from django.contrib import admin
from apps.spravka.models import Phonespravka, Kontakt


class PhonespravkaInline(admin.StackedInline):
    model = Phonespravka
    extra = 0


class KontaktAdmin(admin.ModelAdmin):
    model = Kontakt
    fields = ('name_firm', 'name_uslug', 'phone1', 'phone_video', 'app_video', 'descrip')
    list_display = ('name_firm', 'name_uslug', 'phone1', 'phone_video', 'app_video', 'descrip', )
    inlines = [PhonespravkaInline]
    # list_filter = ("tags",)
    # search_fields = ('userartikul__username',)
    # prepopulated_fields = {"slug": ("vid", "krai", "gorod",)}


admin.site.register(Kontakt, KontaktAdmin)


class PhonespravkaAdmin(admin.ModelAdmin):
    model = Phonespravka
    fields = ("art", "mesto", "tags")
    list_display = ("art", "mesto", "tags")
    list_filter = ("tags",)

    # search_fields = ('userartikul__username',)
    # prepopulated_fields = {"slug": ("vid", "krai", "gorod",)}


admin.site.register(Phonespravka, PhonespravkaAdmin)
