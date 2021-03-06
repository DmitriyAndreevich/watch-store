# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180227_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(null=True, upload_to='products_images/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'SliderImage',
                'verbose_name_plural': 'Slider_images',
            },
        ),
    ]
