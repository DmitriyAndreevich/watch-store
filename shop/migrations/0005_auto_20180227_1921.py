# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20180227_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': '', 'verbose_name_plural': ''},
        ),
        migrations.AddField(
            model_name='product',
            name='is_exists',
            field=models.BooleanField(default=False),
        ),
    ]
