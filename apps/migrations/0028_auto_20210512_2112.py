# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-05-12 21:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0027_anuncio_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo_propiedad',
            old_name='tipo_oferta',
            new_name='tipo_ofertas',
        ),
    ]
