# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20180301_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=255)),
                ('your_email', models.EmailField(max_length=75)),
                ('your_phone', models.CharField(max_length=255)),
                ('your_message', models.TextField()),
            ],
        ),
    ]
