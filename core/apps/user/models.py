from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models

class User(AbstractUser):
    """ Пользователь """
    phone = models.CharField(
        blank=True,
        max_length=20,
        null=True,
        verbose_name="Номер телефона")
