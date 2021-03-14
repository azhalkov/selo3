# Generated by Django 3.1 on 2021-03-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zadacha',
            name='data_postanovki',
            field=models.DateTimeField(default='12-03-2021', verbose_name='Дата задачи'),
        ),
        migrations.AlterField(
            model_name='zadacha',
            name='is_vipolneno',
            field=models.BooleanField(default=False, verbose_name='Задача выполнена'),
        ),
    ]
