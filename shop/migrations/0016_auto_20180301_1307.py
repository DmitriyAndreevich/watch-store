# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_discount_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_addition_inf',
            field=models.TextField(blank=True, default=None, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_full_description',
            field=models.TextField(blank=True, default=None, max_length=1024, null=True),
        ),
    ]
