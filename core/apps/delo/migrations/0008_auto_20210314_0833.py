# Generated by Django 3.1 on 2021-03-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delo', '0007_auto_20210313_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zadacha',
            name='data_postanovki',
            field=models.DateTimeField(default='2021-03-14', verbose_name='Дата задачи'),
        ),
    ]