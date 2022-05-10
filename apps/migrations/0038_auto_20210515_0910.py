# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-05-15 09:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0037_auto_20210515_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='propiedad',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='anuncio',
            old_name='descripción',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='anuncio',
            name='tipo_oferta',
        ),
        migrations.RemoveField(
            model_name='anuncio',
            name='updated_at_at',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='estado_propiedad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.estado_propiedad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='image',
            field=models.ImageField(upload_to='anuncio2/anuncio2/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='lat',
            field=models.CharField(default='1', max_length=80),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='lon',
            field=models.CharField(default='1', max_length=80),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='moneda',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.pais'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='precio',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='servicios',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='tipo_objeto',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='tipo_propiedad',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='titulo',
            field=models.CharField(max_length=80),
        ),
    ]
