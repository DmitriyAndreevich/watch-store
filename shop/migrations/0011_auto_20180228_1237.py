# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='product_price',
        ),
    ]
