# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20161023_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_posted',
            field=models.BooleanField(default=False, verbose_name='Опублікована'),
        ),
    ]
