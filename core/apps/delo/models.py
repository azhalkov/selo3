# apps/delo/models

from django.db import models
# from django.utils import timezone  # мы будем получать дату создания
from datetime import date
from apps.user.models import User
from datetime import datetime


class Zadacha(models.Model):
    template_name = 'delo/zadachi_list.html'
    fromuser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, help_text='Заказчик')
    ispolnitel = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
                                   help_text='Исполнитель', related_name='ispolnitels')
    zadanie = models.CharField('Задача', max_length=128, default='Название')
    data_postanovki = models.DateTimeField('Дата задачи', default=date.today)
    is_activ = models.BooleanField('В работе', default=True)
    is_vipolneno = models.BooleanField('Задача выполнена', default=False)
    data_vipolnenija = models.DateTimeField('Дата выполнения задачи', default=datetime.now())
    descript = models.TextField('Описание', max_length=512, default='Указать задание')

    def __str__(self):
        return str(self.zadanie)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ["-data_vipolnenija"]  # сортировка дел по времени их создания

    def save(self, *args, **kwargs):
        super(Zadacha, self).save(*args, **kwargs)
