# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-05-15 00:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0035_auto_20210515_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car2',
            name='image',
        ),
        migrations.RemoveField(
            model_name='car2',
            name='precio',
        ),
    ]
