from django import forms
from apps.dom.models import Adres


class AdresForm(forms.ModelForm):
    """Поля формы можно поставить куда захочешь"""
    # name = forms.CharField(label="Категория")
    # description = forms.Textarea("Описание")
    # slug = forms.URLField(label='Ссылка', required=False)
    # objects = False

    class Meta:
        model = Adres
        fields = ("art", "vid", "krai", "gorod", "raion", "mikroraion", "ulica", "nomer_doma", "nomer_podezda",
                       "nomer_kvartiri", "date_pub", "is_activ")