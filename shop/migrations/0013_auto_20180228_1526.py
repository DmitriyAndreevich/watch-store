# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 09:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_productcardimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcardimage',
            old_name='slider_image',
            new_name='card_image',
        ),
    ]
