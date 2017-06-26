# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 09:38
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blogs', '0017_remove_blogs_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]