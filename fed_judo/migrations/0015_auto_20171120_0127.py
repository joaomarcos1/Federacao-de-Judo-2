# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-20 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0014_academia_limite_atletas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academia',
            name='limite_atletas',
            field=models.IntegerField(null=True),
        ),
    ]
