# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161023_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=150, unique=True),
        ),
    ]