from django import forms
from apps.articul.models import Articul


class ArticulForm(forms.ModelForm):
    template_name = 'articul/articul_form.html'
    """Поля формы можно поставить куда захочешь"""
    # name = forms.CharField(label="Категория")
    # description = forms.Textarea("Описание")
    # slug = forms.URLField(label='Ссылка', required=False)
    # objects = False

    class Meta:
        model = Articul
        fields = ("userartikul", "kod_phone", "zametki",)
