# Generated by Django 3.1 on 2021-03-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravka', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phonespravka',
            options={'verbose_name': 'Справка', 'verbose_name_plural': 'Справки'},
        ),
        migrations.AddField(
            model_name='phonespravka',
            name='slug',
            field=models.SlugField(blank=True, max_length=86, null=True, verbose_name='Ссылка'),
        ),
    ]