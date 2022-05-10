# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-05-07 02:54
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_auto_20210507_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripción', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at_at', models.DateTimeField(auto_now_add=True)),
                ('precio', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000000)])),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
                ('image', models.ImageField(upload_to='propiedad/')),
                ('index', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_alquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('tipo_alquiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_alquiler')),
                ('tipo_oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_oferta')),
            ],
        ),
        migrations.AddField(
            model_name='tipo_objeto',
            name='tipo_propiedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_propiedad'),
        ),
        migrations.AddField(
            model_name='tipo_alquiler',
            name='tipo_oferta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_oferta'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='propiedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.propiedad'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='tipo_alquiler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_alquiler'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='tipo_objeto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_objeto'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='tipo_oferta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_oferta'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='tipo_propiedad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.tipo_propiedad'),
        ),
    ]
