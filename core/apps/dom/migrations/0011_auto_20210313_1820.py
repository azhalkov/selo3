# Generated by Django 3.1 on 2021-03-13 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articul', '0006_auto_20210311_0032'),
        ('dom', '0010_auto_20210309_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='art',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adress', to='articul.articul'),
        ),
    ]
