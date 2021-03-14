# Generated by Django 3.1 on 2021-03-10 21:32

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('articul', '0005_articul_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articul',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
    ]
