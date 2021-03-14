# Generated by Django 3.1 on 2021-03-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articul', '0002_auto_20210308_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articul',
            options={'ordering': ['-artikuls'], 'verbose_name': 'Артикул', 'verbose_name_plural': 'Артикулы'},
        ),
        migrations.AddField(
            model_name='articul',
            name='is_oplata',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AddField(
            model_name='articul',
            name='zametki',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Для заметок'),
        ),
    ]