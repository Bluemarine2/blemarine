# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-03-23 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('deler', models.CharField(max_length=80)),
                ('clasifi', models.CharField(max_length=150)),
                ('asunto', models.CharField(max_length=150)),
                ('comentario', models.CharField(max_length=140)),
                ('fecha', models.DateTimeField()),
                ('image', models.ImageField(upload_to='con/')),
            ],
        ),
        migrations.AlterField(
            model_name='comentario',
            name='clasifi',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='deler',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
