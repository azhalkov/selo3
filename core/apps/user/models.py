from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Пользователь """
    first_name = models.CharField("Фамилия", max_length=255)
    last_name = models.CharField("Имя Отчество", max_length=255)
    email = models.EmailField()
    phone = models.CharField('Номер телефона', blank=True, max_length=20, null=True, )

    def __str__(self):
        return str(self.first_name)
