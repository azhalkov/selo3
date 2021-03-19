# Generated by Django 3.1 on 2021-03-15 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articul', '0007_remove_articul_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('image', models.ImageField(upload_to='picture/images', verbose_name='Фото')),
                ('art', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotos', to='articul.articul')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
