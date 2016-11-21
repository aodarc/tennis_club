# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва альбому')),
                ('main_img', models.ImageField(upload_to='', verbose_name='Обкладинка альбому')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('alt', models.CharField(blank=True, max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='gallery.Album', verbose_name='Альбом')),
            ],
        ),
    ]
