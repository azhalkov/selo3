# apps/picture/models
from django.db import models

# Create your models here.
from apps.articul.models import Articul


class Foto(models.Model):
    title = models.CharField('Название', max_length=128)
    art = models.ForeignKey(Articul, null=True, on_delete=models.SET_NULL, related_name='fotos')
    image = models.ImageField('Фото', upload_to='picture/images')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
