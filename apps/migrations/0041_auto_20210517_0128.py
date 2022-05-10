# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-05-17 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0040_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='aviso',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'Felicitaciones']], default=1),
            preserve_default=False,
        ),
    ]