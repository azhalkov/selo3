# Generated by Django 3.1 on 2021-03-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komunikacii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]