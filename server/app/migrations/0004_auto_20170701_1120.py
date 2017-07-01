# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170629_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='name_en',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='영문명'),
        ),
        migrations.AddField(
            model_name='university',
            name='name_short',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='축약명'),
        ),
        migrations.AddField(
            model_name='university',
            name='name_short_en',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='축약영문명'),
        ),
    ]