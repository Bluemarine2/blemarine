# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-03-23 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_distribuidor'),
    ]

    operations = [
        migrations.CreateModel(
            name='distribuidor2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=160)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo', models.CharField(max_length=90)),
                ('categoria', models.CharField(max_length=2)),
                ('image', models.ImageField(upload_to='dis/')),
            ],
        ),
    ]
