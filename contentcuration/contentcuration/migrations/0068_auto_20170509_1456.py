# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-09 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0067_auto_20170427_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='thumbnail_encoding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentnode',
            name='thumbnail_encoding',
            field=models.TextField(blank=True, null=True),
        ),
    ]
