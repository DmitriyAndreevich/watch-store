# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribers',
            name='name',
        ),
    ]
