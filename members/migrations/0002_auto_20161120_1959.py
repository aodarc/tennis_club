# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 19:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='height',
            field=models.SmallIntegerField(help_text='Зріст вказувати в СМ', validators=[django.core.validators.MaxValueValidator(230), django.core.validators.MinValueValidator(50)], verbose_name='Зріст'),
        ),
    ]
